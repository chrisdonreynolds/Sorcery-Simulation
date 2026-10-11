#!/usr/bin/env python3
"""
Project Sorcery - AI Bot Evolution & 1v1 Tournament Simulation
==============================================================
Loads AI bot DNA genomes, conducts 1v1 matches across the 100-bot population,
evaluates Multi-Objective Fitness (Outcome, Peak Combo Setup, Net Damage),
ranks bots, and mutates only the bottom 40% while preserving high-scoring
partial-combo bots and allowing them to serve as cloning parents.

Features:
- Multi-Objective Fitness: w_outcome*S_outcome + w_combo*S_combo + w_damage*S_damage
- Action Masking: strictly restricts policy output logits to valid, craftable spells
- 80-feature observation vector handling with automatic DNA layer-1 migration
- Support for Reverse Curriculum board states (initial_board_state in play_duel)
- Fitness-Ranked Selection protecting partial progress (top 60% survive)
"""

import argparse
import copy
import json
import os
import random
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np

# Ensure project_sorcery engine can be imported
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

# Search fallback locations for project_sorcery
for search_dir in [
    SCRIPT_DIR,
    SCRIPT_DIR.parent,
    SCRIPT_DIR / "downloads",
    SCRIPT_DIR.parent / "downloads",
    SCRIPT_DIR / "project_sorcery_simulation",
]:
    if search_dir.exists() and str(search_dir) not in sys.path:
        sys.path.append(str(search_dir))

try:
    from project_sorcery import (
        ProjectSorceryGame,
        Wizard,
        get_registry,
        get_spell_class,
        PREFIX_TO_CLASS,
        MULTI_CONDITION_REQUIREMENTS,
        get_castable_spells_from_pool,
        evaluate_multi_condition_score,
    )
except ImportError:
    try:
        from project_sorcery_simulation.project_sorcery import (
            ProjectSorceryGame,
            Wizard,
            get_registry,
            get_spell_class,
            PREFIX_TO_CLASS,
            MULTI_CONDITION_REQUIREMENTS,
            get_castable_spells_from_pool,
            evaluate_multi_condition_score,
        )
    except ImportError as e:
        raise ImportError(f"Could not import project_sorcery engine: {e}")


def resolve_file_path(filename: str, custom_path: Optional[str] = None) -> Path:
    """Finds a file in common project directories."""
    if custom_path and os.path.exists(custom_path):
        return Path(custom_path).resolve()

    candidate_dirs = [
        SCRIPT_DIR,
        SCRIPT_DIR / "project_sorcery_simulation",
        SCRIPT_DIR.parent / "project_sorcery_simulation",
        Path.cwd() / "project_sorcery_simulation",
        Path.cwd(),
        SCRIPT_DIR / "downloads",
        SCRIPT_DIR.parent / "downloads",
        Path.cwd() / "downloads",
    ]

    for d in candidate_dirs:
        p = d / filename
        if p.exists():
            return p.resolve()

    return (SCRIPT_DIR / filename).resolve()


def migrate_dna_registry(data: Dict[str, Any]) -> int:
    """
    Pads existing 75-feature weights_layer_1 arrays with 5 rows of small random weights
    to adapt to the 80-feature observation vector, preventing matrix multiplication crashes.
    """
    migrated = 0
    for bot in data.get("bots", []):
        dna = bot.get("dna", {})
        if "weights_layer_1" not in dna:
            continue
        w1 = np.array(dna["weights_layer_1"], dtype=np.float32)
        if w1.shape[0] < 80 and w1.shape[0] > 0:
            needed = 80 - w1.shape[0]
            pad = np.random.normal(0.0, 0.05, size=(needed, w1.shape[1])).astype(np.float32)
            new_w1 = np.vstack([w1, pad])
            dna["weights_layer_1"] = [[round(float(v), 4) for v in row] for row in np.round(new_w1, 4).tolist()]
            dna["architecture"] = [80, 48, 32, 125]
            dna["total_parameters"] = 80 * 48 + 48 + 48 * 32 + 32 + 32 * 125 + 125
            migrated += 1

    meta = data.setdefault("meta", {})
    model_arch = meta.setdefault("model_architecture", {})
    model_arch["input_dimension"] = 80
    model_arch["total_parameters_per_bot"] = 9581
    model_arch["input_feature_description"] = (
        "80 normalized features (75 tactical + 5 normalized rune counts F,W,E,L,D) "
        "extracted via ProjectSorceryGame.get_observation_vector(player_idx)"
    )
    return migrated


class NeuralBotPolicy:
    """
    Feedforward Multi-Layer Perceptron (MLP) policy for Project Sorcery AI Bots.
    Architecture: [80 inputs -> 48 LeakyReLU -> 32 LeakyReLU -> 125 Logits -> Softmax]
    Enhanced with:
    - Action Masking: strictly sets uncraftable spell logits to -infinity
    - 80-feature observation vector processing (including 5 normalized rune counts)
    - Bot memory tracking of previous turns in the match
    - Live awareness of secondary match-long class multipliers
    - Live awareness of multi-condition combo scores and setup impact
    """

    def __init__(self, bot_dict: Dict[str, Any], action_catalog: List[str]):
        self.bot_id = bot_dict.get("bot_id", "Unknown")
        self.name = bot_dict.get("name", self.bot_id)
        self.action_catalog = action_catalog
        self.memory: List[Dict[str, Any]] = []

        dna = bot_dict["dna"]
        w1_raw = np.array(dna["weights_layer_1"], dtype=np.float32)
        # Fallback padding if not yet migrated
        if w1_raw.shape[0] < 80:
            needed = 80 - w1_raw.shape[0]
            pad = np.random.normal(0.0, 0.05, size=(needed, w1_raw.shape[1])).astype(np.float32)
            w1_raw = np.vstack([w1_raw, pad])

        self.w1 = w1_raw
        self.b1 = np.array(dna["biases_layer_1"], dtype=np.float32)
        self.w2 = np.array(dna["weights_layer_2"], dtype=np.float32)
        self.b2 = np.array(dna["biases_layer_2"], dtype=np.float32)
        self.w3 = np.array(dna["weights_layer_3"], dtype=np.float32)
        self.b3 = np.array(dna["biases_layer_3"], dtype=np.float32)

        hyperparams = bot_dict.get("genetic_hyperparameters", {})
        self.temperature = float(hyperparams.get("temperature", 1.0))
        self.decision_mode = hyperparams.get("decision_mode", "softmax_sample")

    def __call__(self, obs: Dict[str, Any]) -> str:
        """Takes game state dict and outputs a valid, craftable 3-rune recipe."""
        # 1. Update bot memory of previous game states in this match
        prev_turn = self.memory[-1].get("turn", 1) if self.memory else None
        if prev_turn is None or obs.get("turn", 1) <= prev_turn:
            self.memory.clear()
        self.memory.append(obs)

        feature_vec = obs.get("feature_vector")
        if feature_vec is None:
            raise ValueError(f"Observation missing 'feature_vector' for bot {self.bot_id}")

        # Feedforward MLP (aligned to DNA input dimension 80)
        x = np.array(feature_vec[:self.w1.shape[0]], dtype=np.float32)

        # Layer 1
        z1 = np.dot(x, self.w1) + self.b1
        h1 = np.where(z1 > 0, z1, z1 * 0.01)

        # Layer 2
        z2 = np.dot(h1, self.w2) + self.b2
        h2 = np.where(z2 > 0, z2, z2 * 0.01)

        # Layer 3 (Output logits over 125 actions)
        logits = np.dot(h2, self.w3) + self.b3

        # 2. Integrate Bot Visibility: Rune Pool, Class Multipliers, and Combo Setup Impact
        me_info = obs.get("me", {})
        rune_pool = me_info.get("rune_pool", [])
        castable_spells = me_info.get("castable_spells", obs.get("castable_spells", []))
        if not castable_spells and rune_pool:
            castable_spells = get_castable_spells_from_pool(rune_pool, self.action_catalog)

        class_multipliers = me_info.get("class_multipliers", {})
        combo_impacts = obs.get("combo_setup_impact", {})

        # Heuristic tactical bias for setting up multi-condition combos & class multipliers
        for idx, recipe in enumerate(self.action_catalog):
            if recipe in combo_impacts:
                total_adv = combo_impacts[recipe].get("total_advance", 0.0)
                if total_adv > 0:
                    logits[idx] += total_adv * 2.5

            prefix = recipe[:2].upper()
            if prefix in PREFIX_TO_CLASS:
                cls_val = PREFIX_TO_CLASS[prefix].value
                c_mult = class_multipliers.get(cls_val, 1.0)
                if c_mult > 1.0:
                    logits[idx] += (c_mult - 1.0) * 3.0

        # 3. ACTION MASKING: Set logits to -inf for spells that cannot be crafted
        if castable_spells:
            castable_set = set(castable_spells)
            for idx, recipe in enumerate(self.action_catalog):
                if recipe not in castable_set:
                    logits[idx] = -np.inf

        # 4. Numerically stable masked softmax
        valid_mask = logits > -1e9
        if np.any(valid_mask):
            scaled_logits = logits / max(1e-5, self.temperature)
            max_valid = np.max(scaled_logits[valid_mask])
            shifted = np.where(valid_mask, scaled_logits - max_valid, -np.inf)
            exp_logits = np.where(valid_mask, np.exp(shifted), 0.0)
            sum_exp = np.sum(exp_logits)
            if sum_exp > 0:
                probs = exp_logits / sum_exp
            else:
                probs = np.zeros(len(logits))
                probs[valid_mask] = 1.0 / np.sum(valid_mask)
        else:
            probs = np.ones(len(logits)) / len(logits)

        if self.decision_mode == "softmax_sample":
            action_idx = int(np.random.choice(len(probs), p=probs))
        else:
            action_idx = int(np.argmax(probs))

        return self.action_catalog[action_idx]


def mutate_bot_dna(bot: Dict[str, Any]) -> None:
    """
    Applies Gaussian mutation to the neural network weights and biases of a bot.
    Uses the bot's mutation_rate and mutation_power hyperparameters.
    """
    dna = bot["dna"]
    hyperparams = bot.get("genetic_hyperparameters", {})
    mut_rate = float(hyperparams.get("mutation_rate", 0.05))
    mut_power = float(hyperparams.get("mutation_power", 0.08))

    weight_keys = [
        "weights_layer_1",
        "biases_layer_1",
        "weights_layer_2",
        "biases_layer_2",
        "weights_layer_3",
        "biases_layer_3",
    ]

    for key in weight_keys:
        if key not in dna:
            continue
        arr = np.array(dna[key], dtype=np.float32)
        mask = np.random.rand(*arr.shape) < mut_rate
        noise = np.random.normal(0.0, mut_power, size=arr.shape).astype(np.float32)
        mutated_arr = arr + mask * noise
        mutated_list = np.round(mutated_arr, 4).tolist()
        if arr.ndim == 2:
            dna[key] = [[round(float(v), 4) for v in row] for row in mutated_list]
        else:
            dna[key] = [round(float(v), 4) for v in mutated_list]

    bot["generation"] = bot.get("generation", 0) + 1


def create_wizard_for_bot(bot: Dict[str, Any]) -> Wizard:
    """
    Instantiates a Wizard for a match with strict baseline rules:
    Max HP: 1000.0, Base stats: 100.0 each.
    """
    return Wizard(
        name=bot["bot_id"],
        starting_hp=1000.0,
        base_potency=100.0,
        base_defense=100.0,
        base_luck=100.0,
        base_speed=100.0,
    )


def count_active_combo_conditions(caster: Wizard, target: Wizard, env: Any) -> int:
    """Counts maximum simultaneously active combo prerequisites for any multi-condition spell."""
    max_met = 0
    for recipe, reqs in MULTI_CONDITION_REQUIREMENTS.items():
        met = 0
        for req_type, req_val in reqs:
            if req_type == "weather":
                if env.weather == req_val: met += 1
            elif req_type == "location":
                if env.location == req_val: met += 1
            elif req_type == "caster_buff":
                if req_val in caster.buffs: met += 1
            elif req_type == "target_debuff":
                if req_val in target.debuffs: met += 1
            elif req_type == "seedling":
                if req_val == "active" and env.seedling_active: met += 1
                elif req_val == "rained_on" and env.seedling_rained_on: met += 1
                elif req_val == "sunny_on" and env.seedling_sunny_on: met += 1
        if met > max_met:
            max_met = met
    return max_met


def play_duel(
    bot_a: Dict[str, Any],
    bot_b: Dict[str, Any],
    action_catalog: List[str],
    spell_data_path: str,
    max_turns: int = 50,
    initial_board_state: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Conducts a single 1v1 duel between bot_a and bot_b.
    Evaluates Multi-Objective Fitness:
      Fitness = w_outcome * S_outcome + w_combo * S_combo + w_damage * S_damage
    """
    wiz_a = create_wizard_for_bot(bot_a)
    wiz_b = create_wizard_for_bot(bot_b)

    policy_a = NeuralBotPolicy(bot_a, action_catalog)
    policy_b = NeuralBotPolicy(bot_b, action_catalog)

    game = ProjectSorceryGame(
        player1=wiz_a,
        player2=wiz_b,
        spell_data_path=spell_data_path,
        max_turns=max_turns,
    )

    obs_a, obs_b = game.reset(initial_board_state=initial_board_state)

    # Track peak simultaneous active combo conditions throughout the duel
    peak_conditions_a = count_active_combo_conditions(wiz_a, wiz_b, game.env)
    peak_conditions_b = count_active_combo_conditions(wiz_b, wiz_a, game.env)

    while not game.is_over:
        action_a = policy_a(obs_a)
        action_b = policy_b(obs_b)
        obs_a, obs_b, r1, r2, done, info = game.step(action_a, action_b)

        peak_conditions_a = max(peak_conditions_a, count_active_combo_conditions(wiz_a, wiz_b, game.env))
        peak_conditions_b = max(peak_conditions_b, count_active_combo_conditions(wiz_b, wiz_a, game.env))

    # Determine Winner and Loser
    if game.winner == wiz_a.name:
        winner_bot = bot_a
        loser_bot = bot_b
        winner_wiz = wiz_a
        loser_wiz = wiz_b
        result_type = "win_p1"
        s_outcome_a = 1.0
        s_outcome_b = -1.0
    elif game.winner == wiz_b.name:
        winner_bot = bot_b
        loser_bot = bot_a
        winner_wiz = wiz_b
        loser_wiz = wiz_a
        result_type = "win_p2"
        s_outcome_a = -1.0
        s_outcome_b = 1.0
    else:
        # Tie breaker on remaining HP
        if wiz_a.current_health > wiz_b.current_health:
            winner_bot, loser_bot = bot_a, bot_b
            winner_wiz, loser_wiz = wiz_a, wiz_b
            result_type = "tiebreaker_p1"
            s_outcome_a = 1.0
            s_outcome_b = -1.0
        elif wiz_b.current_health > wiz_a.current_health:
            winner_bot, loser_bot = bot_b, bot_a
            winner_wiz, loser_wiz = wiz_b, wiz_a
            result_type = "tiebreaker_p2"
            s_outcome_a = -1.0
            s_outcome_b = 1.0
        else:
            if random.random() < 0.5:
                winner_bot, loser_bot = bot_a, bot_b
                winner_wiz, loser_wiz = wiz_a, wiz_b
                s_outcome_a = 1.0
                s_outcome_b = -1.0
            else:
                winner_bot, loser_bot = bot_b, bot_a
                winner_wiz, loser_wiz = wiz_b, wiz_a
                s_outcome_a = -1.0
                s_outcome_b = 1.0
            result_type = "tiebreaker_draw_resolved"

    # Multi-Objective Fitness Evaluation
    # 1. Match Outcome: +1.0 for Win, -1.0 for Loss (w_outcome = 1.0)
    w_outcome = 1.0

    # 2. Max Combo Prerequisites Active: +0.25 per active condition at peak setup (w_combo = 1.0)
    w_combo = 1.0
    s_combo_a = 0.25 * float(peak_conditions_a)
    s_combo_b = 0.25 * float(peak_conditions_b)

    # 3. Net Damage Differential: (Damage Dealt - Damage Taken) / 1000.0 (w_damage = 0.5)
    w_damage = 0.5
    s_damage_a = (wiz_a.damage_dealt - wiz_a.damage_taken) / 1000.0
    s_damage_b = (wiz_b.damage_dealt - wiz_b.damage_taken) / 1000.0

    fitness_a = round(w_outcome * s_outcome_a + w_combo * s_combo_a + w_damage * s_damage_a, 4)
    fitness_b = round(w_outcome * s_outcome_b + w_combo * s_combo_b + w_damage * s_damage_b, 4)

    # Track spell and class usage from combat logs
    spells_cast_a: Dict[str, int] = {}
    spells_cast_b: Dict[str, int] = {}
    classes_used_a: Dict[str, int] = {}
    classes_used_b: Dict[str, int] = {}

    for turn_entry in game.combat_logs:
        for event in turn_entry.get("events", []):
            actor = event.get("caster")
            recipe = event.get("recipe")
            if not recipe:
                continue
            spell_cls = event.get("class", "Unknown")
            if actor == wiz_a.name:
                spells_cast_a[recipe] = spells_cast_a.get(recipe, 0) + 1
                classes_used_a[spell_cls] = classes_used_a.get(spell_cls, 0) + 1
            elif actor == wiz_b.name:
                spells_cast_b[recipe] = spells_cast_b.get(recipe, 0) + 1
                classes_used_b[spell_cls] = classes_used_b.get(spell_cls, 0) + 1

    # Update Performance Trackers
    def update_bot_stats(
        bot: Dict[str, Any],
        is_winner: bool,
        wiz: Wizard,
        spells_cast: Dict[str, int],
        classes_used: Dict[str, int],
        match_fitness: float,
        peak_conditions: int,
    ):
        tracker = bot.setdefault("performance_tracker", {})
        tracker["matches_played"] = tracker.get("matches_played", 0) + 1
        if is_winner:
            tracker["wins"] = tracker.get("wins", 0) + 1
        else:
            tracker["losses"] = tracker.get("losses", 0) + 1

        matches = tracker["matches_played"]
        tracker["win_rate"] = round(tracker.get("wins", 0) / max(1, matches), 4)
        tracker["damage_dealt"] = round(tracker.get("damage_dealt", 0.0) + wiz.damage_dealt, 1)
        tracker["damage_taken"] = round(tracker.get("damage_taken", 0.0) + wiz.damage_taken, 1)
        tracker["healing_done"] = round(tracker.get("healing_done", 0.0) + wiz.healing_done, 1)
        tracker["turns_survived"] = tracker.get("turns_survived", 0) + game.current_turn

        spell_counts = tracker.setdefault("spell_usage_counts", {})
        for s, c in spells_cast.items():
            spell_counts[s] = spell_counts.get(s, 0) + c

        class_counts = tracker.setdefault("class_usage_counts", {})
        for cls_name, c in classes_used.items():
            class_counts[cls_name] = class_counts.get(cls_name, 0) + c

        tracker["last_match_fitness"] = match_fitness
        tracker["fitness"] = round(tracker.get("fitness", 0.0) + match_fitness, 4)
        tracker["peak_combo_conditions"] = max(tracker.get("peak_combo_conditions", 0), peak_conditions)

    update_bot_stats(bot_a, winner_bot is bot_a, wiz_a, spells_cast_a, classes_used_a, fitness_a, peak_conditions_a)
    update_bot_stats(bot_b, winner_bot is bot_b, wiz_b, spells_cast_b, classes_used_b, fitness_b, peak_conditions_b)

    return {
        "bot_a_id": bot_a["bot_id"],
        "bot_b_id": bot_b["bot_id"],
        "winner_id": winner_bot["bot_id"],
        "loser_id": loser_bot["bot_id"],
        "winner_bot": winner_bot,
        "loser_bot": loser_bot,
        "fitness_a": fitness_a,
        "fitness_b": fitness_b,
        "peak_conditions_a": peak_conditions_a,
        "peak_conditions_b": peak_conditions_b,
        "turns": game.current_turn,
        "p1_final_hp": wiz_a.current_health,
        "p2_final_hp": wiz_b.current_health,
        "result_type": result_type,
    }


def run_tournament_iteration(
    dna_path: Optional[Union[str, Path]] = None,
    spell_data_path: Optional[Union[str, Path]] = None,
    verbose: bool = True,
    board_states: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Executes one tournament iteration:
    1. Loads 100 bots from ai_bots_dna.json (and migrates DNA to 80-dim if needed).
    2. Randomly partitions into two groups of 50.
    3. Runs 50 1v1 matches (1000 max HP, 100 base stats).
    4. Evaluates Multi-Objective Fitness for each bot.
    5. Ranks all bots by fitness and mutates only the bottom 40% (allowing high-scoring
       partial-combo bots to survive or serve as cloning parents).
    6. Saves updated DNA back to disk.
    """
    actual_dna_path = resolve_file_path("ai_bots_dna.json", str(dna_path) if dna_path else None)
    actual_spell_path = resolve_file_path("spell_data.json", str(spell_data_path) if spell_data_path else None)

    if not actual_dna_path.exists():
        raise FileNotFoundError(f"AI Bots DNA JSON not found at: {actual_dna_path}")
    if not actual_spell_path.exists():
        raise FileNotFoundError(f"Spell data JSON not found at: {actual_spell_path}")

    if verbose:
        print(f"Loading bot population from: {actual_dna_path}")
        print(f"Loading spell data from:      {actual_spell_path}")

    with open(actual_dna_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Automatic migration routine for DNA dimensions
    migrated_count = migrate_dna_registry(data)
    if migrated_count > 0 and verbose:
        print(f"[Migration] Automatically migrated {migrated_count} bots to 80-dimensional input layer.")

    bots: List[Dict[str, Any]] = data.get("bots", [])
    if len(bots) < 100:
        raise ValueError(f"Expected 100 bots in population, found {len(bots)}.")

    action_catalog = data.get("meta", {}).get("action_catalog")
    if not action_catalog:
        registry = get_registry(str(actual_spell_path))
        action_catalog = registry.all_recipes()

    # Enforce base stats & starting HP on all bots in metadata
    for b in bots:
        b["wizard_stats"] = {
            "starting_hp": 1000.0,
            "base_potency": 100.0,
            "base_defense": 100.0,
            "base_luck": 100.0,
            "base_speed": 100.0,
        }

    # Pit 50 at random against the other half
    indices = list(range(len(bots)))
    random.shuffle(indices)

    group_1_indices = indices[:50]
    group_2_indices = indices[50:100]

    match_results = []
    start_time = time.time()
    if verbose:
        print("\n" + "=" * 70)
        mode_str = "Curriculum Board States" if board_states else "Standard Duels"
        print(f"Starting 50 1v1 Matches ({mode_str} with {len(bots)} Bots)")
        print("=" * 70)

    for match_num in range(50):
        idx_a = group_1_indices[match_num]
        idx_b = group_2_indices[match_num]
        bot_a = bots[idx_a]
        bot_b = bots[idx_b]

        init_state = None
        if board_states:
            init_state = random.choice(board_states)

        result = play_duel(
            bot_a=bot_a,
            bot_b=bot_b,
            action_catalog=action_catalog,
            spell_data_path=str(actual_spell_path),
            max_turns=50,
            initial_board_state=init_state,
        )
        match_results.append(result)

        if verbose:
            print(
                f"Match {match_num + 1:02d}/50: "
                f"{bot_a['name']} ({bot_a['bot_id']}) vs {bot_b['name']} ({bot_b['bot_id']}) "
                f"-> Winner: {result['winner_id']} in {result['turns']} turns | "
                f"Fitness: [A: {result['fitness_a']:+.2f}, B: {result['fitness_b']:+.2f}] "
                f"(Peak Setup: A={result['peak_conditions_a']}, B={result['peak_conditions_b']})"
            )

    elapsed_time = time.time() - start_time

    # Fitness-Ranked Selection:
    # Rank all 100 bots by their Multi-Objective Fitness score in this iteration.
    # Top 60% survive; only bottom 40% are mutated/cloned.
    ranked_bots = sorted(
        bots,
        key=lambda b: b.get("performance_tracker", {}).get("last_match_fitness", 0.0),
        reverse=True,
    )
    cutoff = int(len(bots) * 0.60)  # 60 bots survive
    survivors = ranked_bots[:cutoff]
    bottom_bots = ranked_bots[cutoff:]  # 40 bots in bottom 40%

    if verbose:
        print("-" * 70)
        print(f"Completed 50 1v1 matches in {elapsed_time:.2f}s ({elapsed_time/50:.4f}s/match)")
        print(
            f"Fitness-Ranked Selection: Top {len(survivors)} bots survived (score range: "
            f"{survivors[-1]['performance_tracker']['last_match_fitness']:+.2f} to "
            f"{survivors[0]['performance_tracker']['last_match_fitness']:+.2f})."
        )
        print(f"Mutating {len(bottom_bots)} bots in bottom 40% (score cutoff: "
              f"{bottom_bots[0]['performance_tracker']['last_match_fitness']:+.2f})...")

    mutated_count = 0
    for bot in bottom_bots:
        crossover_rate = float(bot.get("genetic_hyperparameters", {}).get("crossover_rate", 0.70))
        # Allow high-scoring partial-combo bots to serve as cloning parents
        if random.random() < crossover_rate and survivors:
            parent = random.choice(survivors)
            bot["dna"] = copy.deepcopy(parent["dna"])
        mutate_bot_dna(bot)
        mutated_count += 1

    # Update metadata
    meta = data.setdefault("meta", {})
    meta["last_trained_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    meta["total_training_iterations"] = meta.get("total_training_iterations", 0) + 1
    meta["total_matches_simulated"] = meta.get("total_matches_simulated", 0) + 50

    if verbose:
        print(f"Saving updated DNA and performance stats to: {actual_dna_path}")

    # Write atomically
    temp_dna_path = actual_dna_path.with_suffix(".tmp.json")
    with open(temp_dna_path, "w", encoding="utf-8") as f:
        json.dump(data, f, separators=(",", ":"))
    temp_dna_path.replace(actual_dna_path)

    if verbose:
        print(f"Saved successfully! Iteration {meta['total_training_iterations']} complete.\n")

    return {
        "status": "success",
        "matches_played": 50,
        "mutated_bots_count": mutated_count,
        "elapsed_seconds": elapsed_time,
        "iteration": meta["total_training_iterations"],
        "dna_path": str(actual_dna_path),
        "results": match_results,
    }


def main(
    dna_path: Optional[Union[str, Path]] = None,
    spell_data_path: Optional[Union[str, Path]] = None,
    verbose: bool = True,
    board_states: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """
    Main entry point:
    Executes one complete iteration of 50 matches and fitness-ranked mutations.
    """
    return run_tournament_iteration(
        dna_path=dna_path,
        spell_data_path=spell_data_path,
        verbose=verbose,
        board_states=board_states,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Project Sorcery AI Bot Evolution Runner")
    parser.add_argument("--dna", type=str, default=None, help="Path to ai_bots_dna.json")
    parser.add_argument("--spells", type=str, default=None, help="Path to spell_data.json")
    parser.add_argument("--iterations", type=int, default=1, help="Number of 50-match iterations to run (default: 1)")
    parser.add_argument("--quiet", action="store_true", help="Suppress verbose match logging")

    args = parser.parse_args()

    for i in range(args.iterations):
        if args.iterations > 1:
            print(f"\n>>> Running Iteration {i+1} of {args.iterations} <<<")
        main(dna_path=args.dna, spell_data_path=args.spells, verbose=not args.quiet)
