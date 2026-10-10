#!/usr/bin/env python3
"""
Project Sorcery - AI Bot Evolution & 1v1 Tournament Simulation
==============================================================
Loads AI bot DNA genomes, conducts 50 random 1v1 matches across the 100-bot
population, and mutates the neural network DNA of the losing bots.

Rules & Constraints:
- Population: 100 bots loaded from ai_bots_dna.json
- Matches per iteration: 50 1v1 matches (50 randomly pitted against the other 50)
- Wizard parameters at match start:
    - Max HP / Starting HP: 1000.0
    - Base stats: 100.0 each (Potency, Defense, Luck, Speed)
- Losers of each match undergo consequential mutation of their neural network DNA.
- Updated DNA and performance statistics are saved back to ai_bots_dna.json.
- Each call to main() executes one complete iteration of 50 matches and mutations.
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
    )
except ImportError:
    try:
        from project_sorcery_simulation.project_sorcery import (
            ProjectSorceryGame,
            Wizard,
            get_registry,
            get_spell_class,
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


class NeuralBotPolicy:
    """
    Feedforward Multi-Layer Perceptron (MLP) policy for Project Sorcery AI Bots.
    Architecture: [75 inputs -> 48 LeakyReLU -> 32 LeakyReLU -> 125 Logits -> Softmax]
    """

    def __init__(self, bot_dict: Dict[str, Any], action_catalog: List[str]):
        self.bot_id = bot_dict.get("bot_id", "Unknown")
        self.name = bot_dict.get("name", self.bot_id)
        self.action_catalog = action_catalog

        dna = bot_dict["dna"]
        self.w1 = np.array(dna["weights_layer_1"], dtype=np.float32)
        self.b1 = np.array(dna["biases_layer_1"], dtype=np.float32)
        self.w2 = np.array(dna["weights_layer_2"], dtype=np.float32)
        self.b2 = np.array(dna["biases_layer_2"], dtype=np.float32)
        self.w3 = np.array(dna["weights_layer_3"], dtype=np.float32)
        self.b3 = np.array(dna["biases_layer_3"], dtype=np.float32)

        hyperparams = bot_dict.get("genetic_hyperparameters", {})
        self.temperature = float(hyperparams.get("temperature", 1.0))
        self.decision_mode = hyperparams.get("decision_mode", "softmax_sample")

    def __call__(self, obs: Dict[str, Any]) -> str:
        """Takes game state dict containing feature_vector and outputs 3-rune recipe."""
        feature_vec = obs.get("feature_vector")
        if feature_vec is None:
            raise ValueError(f"Observation missing 'feature_vector' for bot {self.bot_id}")

        x = np.array(feature_vec, dtype=np.float32)

        # Layer 1
        z1 = np.dot(x, self.w1) + self.b1
        h1 = np.where(z1 > 0, z1, z1 * 0.01)

        # Layer 2
        z2 = np.dot(h1, self.w2) + self.b2
        h2 = np.where(z2 > 0, z2, z2 * 0.01)

        # Layer 3 (Output logits over 125 actions)
        logits = np.dot(h2, self.w3) + self.b3

        # Scaled softmax
        scaled_logits = logits / max(1e-5, self.temperature)
        shifted_logits = scaled_logits - np.max(scaled_logits)
        exp_logits = np.exp(shifted_logits)
        probs = exp_logits / np.sum(exp_logits)

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
        dna[key] = np.round(mutated_arr, 4).tolist()

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


def play_duel(
    bot_a: Dict[str, Any],
    bot_b: Dict[str, Any],
    action_catalog: List[str],
    spell_data_path: str,
    max_turns: int = 50,
) -> Dict[str, Any]:
    """
    Conducts a single 1v1 duel between bot_a and bot_b.
    Returns match statistics and identifies the winner and loser.
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

    obs_a, obs_b = game.reset()

    while not game.is_over:
        action_a = policy_a(obs_a)
        action_b = policy_b(obs_b)
        obs_a, obs_b, r1, r2, done, info = game.step(action_a, action_b)

    # Determine Winner and Loser
    if game.winner == wiz_a.name:
        winner_bot = bot_a
        loser_bot = bot_b
        winner_wiz = wiz_a
        loser_wiz = wiz_b
        result_type = "win_p1"
    elif game.winner == wiz_b.name:
        winner_bot = bot_b
        loser_bot = bot_a
        winner_wiz = wiz_b
        loser_wiz = wiz_a
        result_type = "win_p2"
    else:
        # Tie breaker on remaining HP
        if wiz_a.current_health > wiz_b.current_health:
            winner_bot, loser_bot = bot_a, bot_b
            winner_wiz, loser_wiz = wiz_a, wiz_b
            result_type = "tiebreaker_p1"
        elif wiz_b.current_health > wiz_a.current_health:
            winner_bot, loser_bot = bot_b, bot_a
            winner_wiz, loser_wiz = wiz_b, wiz_a
            result_type = "tiebreaker_p2"
        else:
            if random.random() < 0.5:
                winner_bot, loser_bot = bot_a, bot_b
                winner_wiz, loser_wiz = wiz_a, wiz_b
            else:
                winner_bot, loser_bot = bot_b, bot_a
                winner_wiz, loser_wiz = wiz_b, wiz_a
            result_type = "tiebreaker_draw_resolved"

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

        hp_diff = (wiz.current_health - (1000.0 if not is_winner else 0.0)) / 1000.0
        bonus = 10.0 if is_winner else -10.0
        tracker["fitness"] = round(tracker.get("fitness", 0.0) + hp_diff + bonus, 2)

    update_bot_stats(bot_a, winner_bot is bot_a, wiz_a, spells_cast_a, classes_used_a)
    update_bot_stats(bot_b, winner_bot is bot_b, wiz_b, spells_cast_b, classes_used_b)

    return {
        "bot_a_id": bot_a["bot_id"],
        "bot_b_id": bot_b["bot_id"],
        "winner_id": winner_bot["bot_id"],
        "loser_id": loser_bot["bot_id"],
        "winner_bot": winner_bot,
        "loser_bot": loser_bot,
        "turns": game.current_turn,
        "p1_final_hp": wiz_a.current_health,
        "p2_final_hp": wiz_b.current_health,
        "result_type": result_type,
    }


def run_tournament_iteration(
    dna_path: Optional[Union[str, Path]] = None,
    spell_data_path: Optional[Union[str, Path]] = None,
    verbose: bool = True,
) -> Dict[str, Any]:
    """
    Executes one tournament iteration:
    1. Loads 100 bots from ai_bots_dna.json.
    2. Randomly partitions into two groups of 50.
    3. Runs 50 1v1 matches (1000 max HP, 100 base stats).
    4. Mutates the 50 losing bots.
    5. Saves updated DNA back to disk.
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
    losers_to_mutate = []

    start_time = time.time()
    if verbose:
        print("\n" + "=" * 70)
        print(f"Starting 50 1v1 Matches (Iteration with {len(bots)} Bots)")
        print("=" * 70)

    for match_num in range(50):
        idx_a = group_1_indices[match_num]
        idx_b = group_2_indices[match_num]
        bot_a = bots[idx_a]
        bot_b = bots[idx_b]

        result = play_duel(
            bot_a=bot_a,
            bot_b=bot_b,
            action_catalog=action_catalog,
            spell_data_path=str(actual_spell_path),
            max_turns=50,
        )
        match_results.append(result)
        losers_to_mutate.append(result["loser_bot"])

        if verbose:
            print(
                f"Match {match_num + 1:02d}/50: "
                f"{bot_a['name']} ({bot_a['bot_id']}) vs {bot_b['name']} ({bot_b['bot_id']}) "
                f"-> Winner: {result['winner_id']} in {result['turns']} turns "
                f"(HP: {result['p1_final_hp']:.0f} vs {result['p2_final_hp']:.0f})"
            )

    elapsed_time = time.time() - start_time
    if verbose:
        print("-" * 70)
        print(f"Completed 50 1v1 matches in {elapsed_time:.2f}s ({elapsed_time/50:.4f}s/match)")
        print(f"Mutating {len(losers_to_mutate)} losing bot genomes...")

    # Mutate losing bots
    mutated_count = 0
    for loser in losers_to_mutate:
        mutate_bot_dna(loser)
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
        json.dump(data, f, indent=2)
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
) -> Dict[str, Any]:
    """
    Main entry point:
    Pits 50 bots at random against the other half, executes 50 1v1 matches,
    mutates the losing bots, and saves the updated DNA JSON.
    """
    return run_tournament_iteration(
        dna_path=dna_path,
        spell_data_path=spell_data_path,
        verbose=verbose,
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
