#!/usr/bin/env python3
"""
Project Sorcery - High-Precision Spell Balancing & Simulation Suite
====================================================================
Runs the main tournament loop of the Project Sorcery simulation,
records detailed telemetry over the target evaluation window (last 5,000 games),
and executes sophisticated balancing algorithms to adjust spell formula knobs
(b, n, max_potential) inside spell_data.json.

Key Capabilities:
1. Runs the simulation engine (supporting both game-count and iteration modes).
2. Telemetry extraction across the last 5,000 games:
   - Spell cast frequencies, win rates (Bayesian smoothed), damage/healing metrics.
   - Conditional payoff verification: exact trigger rate vs missed condition rate.
   - Group telemetry: 15 Classes, Status Appliers vs Beneficiaries (e.g. Frosty,
     Burning, Bleeding), Weather Appliers vs Beneficiaries (e.g. Sunny, Rain),
     and Location synergies.
3. Algorithms for Spell Balancing:
   - Score-Based Knob Balancing Engine: Each algorithm votes to increase/decrease
     a knob's buff/nerf score by at most 1 (aggregated score clamped to -3 to +3).
   - Win Rate Outlier Tuner: Votes +/-1 score for win rate outliers (<46.5% or >53.5%).
   - Pick Rate Tuner: Votes +1 for low pickrate (<800/10k) and -1 for high pickrate (>7,000/10k).
     Spells with pick rate < 150 per 10,000 matches are not adjusted.
   - Cleanse & Rune (WWW) Tuner: Inversely adjusts b (nerfs increase potency penalty b, buffs decrease it).
   - Conditional Payoff Tuner: Adjusts (b, n) spread score (+/-1) for conditional spells.
   - Score Aggregation & Synthesis: Aggregates scores (max +/-3), applies single 2%, 3%, 5%
     buff/nerf, and clamps bounds to [0, 200] for b and [0, 20] for n.
   - Status & Buff Magnitude Tuner: Clamps status effect knobs strictly between 0% and 75%.
"""

import argparse
import copy
import csv
import json
import math
import os
import random
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

# Ensure simulation and project_sorcery modules are accessible
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

for search_dir in [
    SCRIPT_DIR,
    SCRIPT_DIR.parent,
    SCRIPT_DIR / "downloads",
    SCRIPT_DIR.parent / "downloads",
]:
    if search_dir.exists() and str(search_dir) not in sys.path:
        sys.path.append(str(search_dir))

try:
    import simulation
    import project_sorcery
    from project_sorcery import (
        Location,
        ProjectSorceryGame,
        SpellKnob,
        SpellKnobsRegistry,
        SpellResolver,
        Weather,
        Wizard,
        get_registry,
        get_spell_class,
        MULTI_CONDITION_REQUIREMENTS,
        BUFF_CONFIGS,
        STATUS_CONFIGS,
        DEFAULT_BUFF_CONFIGS,
        DEFAULT_STATUS_CONFIGS,
        load_status_buff_knobs,
    )
except ImportError as e:
    raise ImportError(f"Could not import Project Sorcery modules: {e}")


# =============================================================================
# 1. SYNERGY CONSTANTS & CONDITION CHECKING ENGINE
# =============================================================================

STATUS_EFFECTS = [
    "Frosty", "Burning", "Bleeding", "Stunned", "Entangled", "Cursed",
    "Asleep", "Jinxed", "Vulnerable", "Weakened", "Slowed", "Polymorphed", "Poisoned", "Infected"
]

WEATHERS = [
    "Sunny", "Raining", "Blizzard", "Darkness", "Storming", "Blood Rain", "Snowing", "Windy", "Sandstorm", "Clear"
]

LOCATIONS = [
    "Jungle", "Enchanted Forest", "Tundra", "Swamp", "Graveyard", "Space"
]

BUFFS = [
    "Charged", "Shielded", "Lucky", "Quickened", "Invisible", "Blessed"
]

# Hard-coded floor for b for all ultimate spells
ULTIMATE_B_FLOOR: float = 20.0

# Bounds for special spells to preserve specific design intent
SPECIAL_BOUNDS: Dict[str, Tuple[float, float, float, float]] = {
    # recipe: (min_b, max_b, min_n, max_n)
    "WWW": (0.0, 200.0, 0.0, 0.0),     # Cleanse & Extra Rune (b: potency penalty)
    "EEE": (2.0, 10.0, 1.5, 3.5),      # % max health damage
    "EEL": (0.2, 1.5, 0.0, 0.0),       # Health scaling factor
    "EED": (2.0, 10.0, 0.0, 0.0),      # 4-12 instances scaling with luck
    "FED": (2.0, 10.0, 1.5, 3.5),      # Multi-hit formula
    "LED": (0.2, 1.5, 0.0, 0.0),       # Speed scaling factor
    "DLD": (20.0, 60.0, 1.5, 3.5),     # Execute missing health scaling
}


def tag_spell_synergies(recipe: str, spell_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extracts semantic synergy relationships for a spell from description and conditions:
    identifies what statuses, weathers, locations, and buffs it applies or benefits from.
    """
    desc = spell_data.get("description", "")
    cond = spell_data.get("condition_required", "")
    
    tags = {
        "recipe": recipe,
        "class": spell_data.get("class", ""),
        "category": spell_data.get("category", ""),
        "applies_status": [],
        "benefits_status": [],
        "applies_weather": [],
        "benefits_weather": [],
        "applies_location": [],
        "benefits_location": [],
        "applies_buff": [],
        "benefits_buff": [],
    }

    desc_lower = desc.lower()
    cond_lower = cond.lower()

    # Status parsing
    for st in STATUS_EFFECTS:
        st_low = st.lower()
        is_recoil_only = (
            f"{st_low} to the caster" in desc_lower
            or f"{st_low} to caster" in desc_lower
            or f"caster {st_low}" in desc_lower
        ) and not (
            f"{st_low} to both" in desc_lower
            or f"caster and the target" in desc_lower
            or f"caster and target" in desc_lower
            or ("target" in desc_lower and (f"applies {st_low}" in desc_lower or f"afflicts {st_low}" in desc_lower))
        )

        if not is_recoil_only:
            if any(w in desc_lower for w in [
                f"applies {st_low}", f"afflicts {st_low}", f"inflicts {st_low}",
                f"target is now {st_low}", f"{st_low} to the target", f"{st_low} to target",
                f"{st_low} on target", f"{st_low} to both", f"apply {st_low}"
            ]):
                tags["applies_status"].append(st)

        if (
            st_low in cond_lower
            or f"target is {st_low}" in desc_lower
            or f"if target has {st_low}" in desc_lower
            or f"if the target is {st_low}" in desc_lower
            or f"if {st_low}" in desc_lower
        ):
            if st in ("Bleeding", "Weakened") and (f"caster is {st_low}" in desc_lower or f"caster is {st_low}" in cond_lower):
                tags["benefits_status"].append(st)
            elif not (f"caster is {st_low}" in desc_lower and "target is" not in desc_lower):
                tags["benefits_status"].append(st)

    # Weather parsing
    for w in WEATHERS:
        w_low = w.lower()
        if (
            f"weather condition to {w_low}" in desc_lower
            or f"weather to {w_low}" in desc_lower
            or (f"to {w_low}" in desc_lower and "weather" in desc_lower)
        ):
            tags["applies_weather"].append(w)
        if (
            w_low in cond_lower
            or f"weather is {w_low}" in desc_lower
            or f"weather condition is {w_low}" in desc_lower
        ):
            tags["benefits_weather"].append(w)

    # Location parsing
    for loc in LOCATIONS:
        loc_low = loc.lower()
        if f"location to {loc_low}" in desc_lower or (f"location is {loc_low}" in desc_lower and "changes the location" in desc_lower):
            tags["applies_location"].append(loc)
        if loc_low in cond_lower or f"location is {loc_low}" in desc_lower:
            tags["benefits_location"].append(loc)

    # Buff parsing
    for bf in BUFFS:
        bf_low = bf.lower()
        if any(w in desc_lower for w in [
            f"grants the caster the {bf_low}", f"grants the caster {bf_low}",
            f"grant the caster the {bf_low}", f"grant the caster {bf_low}",
            f"grants the {bf_low}", f"caster gains {bf_low}",
            f"gives the caster {bf_low}", f"gives the caster the {bf_low}",
            f"caster {bf_low}", f"granted {bf_low}", f"{bf_low} buff"
        ]) or (bf_low == "lucky" and "charged and lucky" in desc_lower) or (bf_low == "quickened" and ("charged and quickened" in desc_lower or "lucky and quickened" in desc_lower)):
            if not (f"if the caster is {bf_low}" in desc_lower or f"if caster is {bf_low}" in desc_lower or (f"caster {bf_low}," in desc_lower and f"gives the caster {bf_low}" not in desc_lower)):
                tags["applies_buff"].append(bf)

        if recipe == "WFD" and bf in ["Shielded", "Lucky"]:
            tags["benefits_buff"].append(bf)
        elif recipe != "WWF" and (
            (bf_low in cond_lower and "target is" not in cond_lower)
            or f"caster is {bf_low}" in desc_lower
            or f"if caster is {bf_low}" in desc_lower
            or f"if the caster is {bf_low}" in desc_lower
            or (f"caster {bf_low}," in desc_lower and f"gives the caster {bf_low}" not in desc_lower)
        ):
            tags["benefits_buff"].append(bf)

    return tags


def is_spell_condition_active(recipe: str, caster: Wizard, target: Wizard, env: Any) -> bool:
    """
    Evaluates whether the conditional requirements for a spell were active
    at the exact moment of casting.
    """
    t_deb = target.debuffs
    c_deb = caster.debuffs
    c_buf = caster.buffs
    t_buf = target.buffs
    w = env.weather
    loc = env.location

    if recipe == "FFD":
        return "Burning" in t_deb or "Vulnerable" in t_deb
    elif recipe == "WWF":
        return "Charged" in t_buf or "Burning" in t_deb
    elif recipe == "WWD":
        return any(st in t_deb for st in ["Weakened", "Vulnerable", "Slowed", "Jinxed"])
    elif recipe == "EEF":
        return "Frosty" in t_deb
    elif recipe == "EEE":
        return False
    elif recipe == "LLF":
        return "Cursed" in c_deb
    elif recipe == "LLD":
        return w == Weather.SUNNY or "Blessed" in c_buf
    elif recipe == "DDF":
        return "Asleep" in t_deb
    elif recipe == "FWD":
        return ("Cursed" in t_deb) or (w == Weather.BLOOD_RAIN) or (loc == Location.GRAVEYARD)
    elif recipe == "WFF":
        return "Bleeding" in t_deb
    elif recipe == "WFD":
        return "Shielded" in c_buf or "Lucky" in c_buf
    elif recipe == "FEW":
        return "Entangled" in t_deb
    elif recipe == "FED":
        return len(t_deb) > 0
    elif recipe == "EFF":
        return "Vulnerable" in t_deb
    elif recipe == "EFD":
        return ("Entangled" in t_deb) or (loc == Location.JUNGLE)
    elif recipe == "FLF":
        return "Stunned" in t_deb
    elif recipe == "FLD":
        return ("Stunned" in t_deb) or ("Charged" in c_buf) or (w == Weather.STORMING)
    elif recipe == "LFF":
        return "Vulnerable" in t_deb
    elif recipe == "LFE":
        return w == Weather.STORMING
    elif recipe == "LFL":
        return "Weakened" in c_deb
    elif recipe == "LFD":
        return "Charged" in c_buf
    elif recipe == "FDF":
        return "Invisible" in c_buf
    elif recipe == "FDD":
        return ("Jinxed" in t_deb) or (w == Weather.DARKNESS)
    elif recipe == "DFF":
        return "Bleeding" in c_deb or w == Weather.BLOOD_RAIN
    elif recipe == "DFD":
        return (caster.max_health - caster.current_health) / max(1.0, caster.max_health) >= 0.20
    elif recipe == "WEF":
        return loc == Location.JUNGLE
    elif recipe == "WED":
        return bool(env.seedling_active or env.seedling_rained_on or env.seedling_sunny_on)
    elif recipe == "EWF":
        return w == Weather.SUNNY
    elif recipe == "EWD":
        return "Entangled" in t_deb
    elif recipe == "WLF":
        return "Cursed" in t_deb
    elif recipe == "WLD":
        return ("Asleep" in t_deb) or (w == Weather.DARKNESS) or (loc == Location.ENCHANTED_FOREST)
    elif recipe == "LWF":
        return loc == Location.ENCHANTED_FOREST
    elif recipe == "LWD":
        return "Polymorphed" in t_deb
    elif recipe == "WDF":
        return w == Weather.RAINING
    elif recipe == "WDD":
        return (w == Weather.BLIZZARD) or (loc == Location.TUNDRA)
    elif recipe == "DWD":
        return "Frosty" in t_deb
    elif recipe == "ELF":
        return "Bleeding" in c_deb
    elif recipe == "ELD":
        return w == Weather.RAINING
    elif recipe == "LEF":
        return "Burning" in t_deb
    elif recipe == "EDF":
        return "Weakened" in t_deb
    elif recipe == "EDD":
        return ("Bleeding" in t_deb) or (loc == Location.SWAMP)
    elif recipe == "DEF":
        return (target.base_potency - target.get_effective_stat("potency")) / max(1.0, target.base_potency) >= 0.20
    elif recipe == "DEL":
        return "Bleeding" in t_deb
    elif recipe == "LDL":
        return "Jinxed" in t_deb
    elif recipe == "LDD":
        return any(st in t_deb for st in ["Jinxed", "Weakened", "Slowed", "Vulnerable"])
    elif recipe == "DLF":
        return "Slowed" in t_deb
    elif recipe == "DLL":
        return w == Weather.DARKNESS
    elif recipe == "DLD":
        return (target.max_health - target.current_health) / max(1.0, target.max_health) >= 0.20

    return False


# =============================================================================
# 2. TELEMETRY RECORDER & COMBAT TRACKER
# =============================================================================

@dataclass
class CastRecord:
    recipe: str
    caster: str
    target: str
    damage: float
    healing: float
    condition_active: bool
    notes: str
    ultimate: bool


@dataclass
class DuelTelemetry:
    p1_name: str
    p2_name: str
    winner_name: str
    turns: int
    casts: List[CastRecord] = field(default_factory=list)


class SimulationTelemetryTracker:
    """
    Hooks into the simulation engine to passively collect granular spell metrics,
    win contributions, and conditional payoff triggers specifically during
    the designated evaluation window (the last 5,000 games).
    """

    def __init__(self, eval_start_game: int, total_games: int, spell_data: Dict[str, Any]):
        self.eval_start_game = eval_start_game
        self.total_games = total_games
        self.spell_data = spell_data
        self.current_game_index = 0
        self.recorded_duels: List[DuelTelemetry] = []

        # Current duel in flight
        self.current_duel_casts: List[CastRecord] = []
        self.run_duel_casts: List[CastRecord] = []
        self.all_recorded_duels: List[DuelTelemetry] = []
        self.synergy_map = {r: tag_spell_synergies(r, s) for r, s in spell_data.items()}

        # Original functions saved for cleanup
        self.orig_resolve = SpellResolver.resolve
        self.orig_play_duel = simulation.play_duel

    def install_hooks(self):
        tracker = self

        def hooked_resolve(resolver_self, recipe, caster, target, env, *args, **kwargs):
            cond_active = is_spell_condition_active(recipe, caster, target, env)
            log = tracker.orig_resolve(resolver_self, recipe, caster, target, env, *args, **kwargs)

            caster_id = getattr(caster, "bot_id", caster.name)
            target_id = getattr(target, "bot_id", target.name)

            rec = CastRecord(
                recipe=recipe,
                caster=caster_id,
                target=target_id,
                damage=log.get("damage_dealt", 0.0),
                healing=log.get("healing_done", 0.0),
                condition_active=cond_active,
                notes=log.get("notes", ""),
                ultimate=log.get("ultimate_triggered", False),
            )
            tracker.run_duel_casts.append(rec)

            if tracker.current_game_index >= tracker.eval_start_game:
                tracker.current_duel_casts.append(rec)

            return log

        def hooked_play_duel(bot_a, bot_b, action_catalog, spell_data_path, max_turns=50, initial_board_state=None, **kwargs):
            tracker.current_duel_casts = []
            tracker.run_duel_casts = []
            result = tracker.orig_play_duel(bot_a, bot_b, action_catalog, spell_data_path, max_turns, initial_board_state=initial_board_state, **kwargs)

            p1_id = bot_a.get("bot_id", bot_a.get("name", "bot_a"))
            p2_id = bot_b.get("bot_id", bot_b.get("name", "bot_b"))
            winner_id = result.get("winner_id", "")

            # Record duel telemetry for the entire run
            run_duel = DuelTelemetry(
                p1_name=p1_id,
                p2_name=p2_id,
                winner_name=winner_id,
                turns=result.get("turns", 0),
                casts=list(tracker.run_duel_casts),
            )
            tracker.all_recorded_duels.append(run_duel)

            if tracker.current_game_index >= tracker.eval_start_game:
                duel_data = DuelTelemetry(
                    p1_name=p1_id,
                    p2_name=p2_id,
                    winner_name=winner_id,
                    turns=result.get("turns", 0),
                    casts=list(tracker.current_duel_casts),
                )
                tracker.recorded_duels.append(duel_data)

            tracker.current_game_index += 1
            return result

        SpellResolver.resolve = hooked_resolve
        simulation.play_duel = hooked_play_duel

    def remove_hooks(self):
        SpellResolver.resolve = self.orig_resolve
        simulation.play_duel = self.orig_play_duel

    def compute_spell_metrics(self, duels: List[DuelTelemetry]) -> Tuple[Dict[str, Dict[str, Any]], int]:
        """
        Calculates granular per-spell metrics across an arbitrary list of duel records.
        Tracks:
        - The amount of times each spell was cast during the run.
        - The amount of damage each spell did during the run.
        - The amount of times each conditional spell was cast while its conditions were met during the run.
        - The winrate of each spell.
        """
        per_spell: Dict[str, Dict[str, Any]] = {}
        for r, data in self.spell_data.items():
            is_cond = ((float(data.get("n", 0.0)) > 0.0) or (data.get("condition_required", "None") != "None") or (data.get("category") in ("Conditional Strike", "Ultimate"))) and r != "EEE"
            per_spell[r] = {
                "recipe": r,
                "spell": r,
                "class": data.get("class", "Unknown"),
                "category": data.get("category", "Unknown"),
                "b": float(data.get("b", 0.0)),
                "n": float(data.get("n", 0.0)),
                "max_potential": float(data.get("max_potential", 0.0)),
                "condition_required": data.get("condition_required", "None"),
                "is_conditional": is_cond,
                "casts": 0,
                "cast_count": 0,
                "times_cast": 0,
                "caster_wins": 0,
                "caster_losses": 0,
                "total_damage": 0.0,
                "damage": 0.0,
                "total_healing": 0.0,
                "condition_checks": 0,
                "condition_triggers": 0,
                "conditional_casts_met": 0,
                "condition_met_casts": 0,
                "times_condition_met": 0,
                "conditional_casts_while_conditions_met": 0,
                "payoff_damage_sum": 0.0,
                "base_damage_sum": 0.0,
            }

        total_casts_all = 0

        for duel in duels:
            winner = duel.winner_name
            p1_casts: Dict[str, int] = {}
            p2_casts: Dict[str, int] = {}

            for c in duel.casts:
                r = c.recipe
                if r not in per_spell:
                    continue

                sp = per_spell[r]
                sp["casts"] += 1
                sp["cast_count"] += 1
                sp["times_cast"] += 1
                total_casts_all += 1
                sp["total_damage"] += c.damage
                sp["damage"] += c.damage
                sp["total_healing"] += c.healing

                if sp["is_conditional"]:
                    sp["condition_checks"] += 1
                    if c.condition_active:
                        sp["condition_triggers"] += 1
                        sp["conditional_casts_met"] += 1
                        sp["condition_met_casts"] += 1
                        sp["times_condition_met"] += 1
                        sp["conditional_casts_while_conditions_met"] += 1
                        sp["payoff_damage_sum"] += c.damage
                    else:
                        sp["base_damage_sum"] += c.damage

                if c.caster == duel.p1_name:
                    p1_casts[r] = p1_casts.get(r, 0) + 1
                elif c.caster == duel.p2_name:
                    p2_casts[r] = p2_casts.get(r, 0) + 1

            # Attribute 1 win or 1 loss per wizard per duel who cast the spell (prevents spam-cast loss inflation)
            for r, cnt in p1_casts.items():
                if cnt > 0:
                    if duel.p1_name == winner:
                        per_spell[r]["caster_wins"] += 1
                    else:
                        per_spell[r]["caster_losses"] += 1

            for r, cnt in p2_casts.items():
                if cnt > 0:
                    if duel.p2_name == winner:
                        per_spell[r]["caster_wins"] += 1
                    else:
                        per_spell[r]["caster_losses"] += 1

        raw_bayesian_list = []
        for r, sp in per_spell.items():
            casts = sp["casts"]
            wins = sp["caster_wins"]
            losses = sp["caster_losses"]
            total_resolved = wins + losses

            raw_wr = round(wins / max(1, total_resolved), 4) if total_resolved > 0 else 0.0
            k = 12.0
            bayesian_wr = round((wins + k * 0.5) / (total_resolved + k), 4) if total_resolved > 0 else 0.50
            if total_resolved > 0:
                raw_bayesian_list.append(bayesian_wr)

            sp["raw_win_rate"] = raw_wr
            sp["uncentered_bayesian_win_rate"] = bayesian_wr
            sp["bayesian_win_rate"] = bayesian_wr
            sp["winrate"] = raw_wr
            sp["win_rate"] = raw_wr
            sp["wins"] = wins
            sp["losses"] = losses
            sp["pick_rate"] = round(casts / max(1, total_casts_all), 5) if total_casts_all > 0 else 0.0
            sp["avg_damage"] = round(sp["total_damage"] / max(1, casts), 2) if casts > 0 else 0.0
            sp["avg_healing"] = round(sp["total_healing"] / max(1, casts), 2) if casts > 0 else 0.0
            sp["total_damage"] = round(sp["total_damage"], 2)
            sp["damage"] = round(sp["damage"], 2)

            cond_checks = sp["condition_checks"]
            cond_trigs = sp["condition_triggers"]
            sp["trigger_rate"] = round(cond_trigs / max(1, cond_checks), 4) if cond_checks > 0 else 0.0
            sp["avg_payoff_damage"] = round(sp["payoff_damage_sum"] / max(1, cond_trigs), 2) if cond_trigs > 0 else 0.0
            missed = cond_checks - cond_trigs
            sp["avg_base_damage"] = round(sp["base_damage_sum"] / max(1, missed), 2) if missed > 0 else 0.0

        # Center Bayesian win rates around the run median to prevent macro skew from mass-nerfing all spells
        if raw_bayesian_list:
            sorted_wr = sorted(raw_bayesian_list)
            mid = len(sorted_wr) // 2
            median_wr = sorted_wr[mid] if len(sorted_wr) % 2 == 1 else 0.5 * (sorted_wr[mid - 1] + sorted_wr[mid])
            for r, sp in per_spell.items():
                if (sp["wins"] + sp["losses"]) > 0:
                    centered = max(0.0, min(1.0, 0.50 + (sp["uncentered_bayesian_win_rate"] - median_wr)))
                    sp["bayesian_win_rate"] = round(centered, 4)

        return per_spell, total_casts_all

    def compute_run_spell_metrics(self) -> Dict[str, Dict[str, Any]]:
        """
        Compiles spell telemetry strictly for the post-training evaluation matches (e.g., 5000 matches).
        """
        metrics, _ = self.compute_spell_metrics(self.recorded_duels)
        return metrics

    def compute_eval_spell_metrics(self) -> Dict[str, Dict[str, Any]]:
        """
        Compiles spell telemetry strictly for the post-training evaluation matches (e.g., 5000 matches).
        """
        metrics, _ = self.compute_spell_metrics(self.recorded_duels)
        return metrics

    def compute_aggregates(self) -> Dict[str, Any]:
        """
        Compiles all raw duel records into structured aggregate telemetry
        for individual spells, classes, and synergy groups.
        """
        eval_game_count = len(self.recorded_duels)
        print(f"\n[Telemetry] Compiling aggregate data from {eval_game_count} evaluated games...")

        per_spell, total_casts_all = self.compute_spell_metrics(self.recorded_duels)
        # Class level aggregation
        class_stats: Dict[str, Dict[str, Any]] = {}
        for r, sp in per_spell.items():
            cls_name = sp["class"]
            if cls_name not in class_stats:
                class_stats[cls_name] = {
                    "class": cls_name,
                    "total_casts": 0,
                    "total_wins": 0,
                    "total_losses": 0,
                    "total_damage": 0.0,
                    "spells": [],
                }
            cs = class_stats[cls_name]
            cs["total_casts"] += sp["casts"]
            cs["total_wins"] += sp["caster_wins"]
            cs["total_losses"] += sp["caster_losses"]
            cs["total_damage"] += sp["total_damage"]
            cs["spells"].append(r)

        for cls_name, cs in class_stats.items():
            tot = cs["total_wins"] + cs["total_losses"]
            cs["win_rate"] = round(cs["total_wins"] / max(1, tot), 4)
            cs["bayesian_win_rate"] = round((cs["total_wins"] + 25.0 * 0.5) / (tot + 25.0), 4)
            cs["avg_damage_per_cast"] = round(cs["total_damage"] / max(1, cs["total_casts"]), 2)

        # Synergy Groups aggregation
        synergy_groups: Dict[str, Dict[str, Any]] = {}
        group_specs = []
        for st in STATUS_EFFECTS:
            group_specs.append((st, "status", st))
        for wt in WEATHERS:
            group_specs.append((wt, "weather", wt))
        for loc in LOCATIONS:
            group_specs.append((loc, "location", loc))
        for bf in BUFFS:
            group_specs.append((bf, "buff", bf))

        for name, kind, key in group_specs:
            appliers = []
            beneficiaries = []
            for r, tag in self.synergy_map.items():
                if kind == "status":
                    if key in tag.get("applies_status", []): appliers.append(r)
                    if key in tag.get("benefits_status", []): beneficiaries.append(r)
                elif kind == "weather":
                    if key in tag.get("applies_weather", []): appliers.append(r)
                    if key in tag.get("benefits_weather", []): beneficiaries.append(r)
                elif kind == "location":
                    if key in tag.get("applies_location", []): appliers.append(r)
                    if key in tag.get("benefits_location", []): beneficiaries.append(r)
                elif kind == "buff":
                    if key in tag.get("applies_buff", []): appliers.append(r)
                    if key in tag.get("benefits_buff", []): beneficiaries.append(r)

            def summarize_group(recipes: List[str]) -> Dict[str, Any]:
                c_sum = sum(per_spell[rec]["casts"] for rec in recipes)
                w_sum = sum(per_spell[rec]["caster_wins"] for rec in recipes)
                l_sum = sum(per_spell[rec]["caster_losses"] for rec in recipes)
                trig_sum = sum(per_spell[rec]["condition_triggers"] for rec in recipes)
                chk_sum = sum(per_spell[rec]["condition_checks"] for rec in recipes)
                tot = w_sum + l_sum
                return {
                    "recipes": recipes,
                    "casts": c_sum,
                    "wins": w_sum,
                    "losses": l_sum,
                    "win_rate": round(w_sum / max(1, tot), 4),
                    "bayesian_win_rate": round((w_sum + 15.0 * 0.5) / (tot + 15.0), 4),
                    "trigger_rate": round(trig_sum / max(1, chk_sum), 4) if chk_sum > 0 else 0.0,
                }

            synergy_groups[f"status_{name}" if kind == "status" else f"{kind}_{name}"] = {
                "name": name,
                "kind": kind,
                "appliers": summarize_group(appliers),
                "beneficiaries": summarize_group(beneficiaries),
            }

        return {
            "evaluated_games": eval_game_count,
            "total_casts": total_casts_all,
            "per_spell": per_spell,
            "classes": class_stats,
            "synergies": synergy_groups,
        }


# =============================================================================
# 3. BALANCING ALGORITHMS ENGINE
# =============================================================================


# =============================================================================
# 1.5 CONDITION COMPLEXITY & CALIBRATED TARGET SYSTEM
# =============================================================================

def get_spell_condition_complexity(recipe: str, spell_data: Optional[Dict[str, Any]] = None) -> int:
    """
    Determines the number of distinct environmental, status, buff, or state
    prerequisites required for a conditional spell's payoff to trigger.
    
    Compounding probability: P(all k conditions) ≈ product of individual probabilities.
    Higher condition counts necessitate lower target trigger thresholds and protective
    floors against dead-card syndrome.
    """
    EXPLICIT_COMPLEXITY: Dict[str, int] = {
        # 4 conditions:
        "LDD": 4,  # Jinxed + Weakened + Slowed + Vulnerable
        # 3 conditions:
        "FWD": 3,  # Cursed + Blood Rain + Graveyard
        "FLD": 3,  # Stunned + Charged + Storming
        "WLD": 3,  # Asleep + Darkness + Enchanted Forest
        "WED": 3,  # Seedling active + rained on + sunny on
        # 2 conditions:
        "EDD": 2,  # Bleeding + Swamp
        "EFD": 2,  # Entangled + Jungle
        "FDD": 2,  # Jinxed + Darkness
        "LLD": 2,  # Sunny + Blessed
        "WDD": 2,  # Blizzard + Tundra
    }
    if recipe in EXPLICIT_COMPLEXITY:
        return EXPLICIT_COMPLEXITY[recipe]

    # Dynamic fallback based on condition description
    if spell_data:
        cond_text = spell_data.get("condition_required", "")
        if cond_text and cond_text.lower() != "none":
            parts = [
                p.strip()
                for p in cond_text.replace("AND", "and").replace(",", " and ").split(" and ")
                if p.strip()
            ]
            if len(parts) > 1:
                return len(parts)

    return 1


def get_condition_complexity_targets(num_conditions: int) -> Tuple[float, float, float, int]:
    """
    Returns (target_min, target_optimal, target_max, min_casts)
    calibrated to the compounding difficulty of satisfying N independent conditions.
    """
    if num_conditions == 1:
        # Single condition (e.g. Frosty, Burning, Bleeding, Raining, Health threshold)
        # Healthy synergy window: 30% to 55%
        return 0.30, 0.40, 0.55, 25
    elif num_conditions == 2:
        # Dual condition (e.g. Status + Location, Weather + Buff)
        # Healthy synergy window: 16% to 36%
        return 0.16, 0.24, 0.36, 15
    elif num_conditions == 3:
        # Triple condition (e.g. Status + Weather + Location)
        # Healthy synergy window: 8% to 20%
        return 0.08, 0.12, 0.20, 10
    else:
        # 4+ conditions (e.g. LDD with 4 debuffs)
        # Healthy synergy window: 3% to 12%
        return 0.03, 0.06, 0.12, 8


class SpellBalancingEngine:
    """
    Executes score-based balancing algorithms over aggregate simulation telemetry:
    1. Status & Buff Magnitude Tuner: Clamps status effect knobs between 0% and 75%.
    2. Algorithm Win Rate: Votes +/-1 score for win rate outliers (<46.5% or >53.5%).
    3. Algorithm Pick Rate: Votes +1 for low pick rate (<800/10k) and -1 for high pick rate (>7,000/10k).
       Excludes spells with <150 casts per 10,000 matches from adjustments.
    4. Algorithm Cleanse Tuner: When WWW is overtuned/undertuned, marks WWW for nerf/buff. Inversely adjusts b instead of adjusting all other spells.
    5. Algorithm Conditional Payoff: Adjusts spread for conditional spells (b +/-1, n -/+1).
    6. Score Aggregation & Synthesis: Aggregates scores clamped to [-3, +3], applies single 2%, 3%, 5%
       buff/nerf, and clamps bounds to [0, 200] for b and [0, 20] for n.
    """

    def __init__(
        self,
        spell_data: Dict[str, Any],
        telemetry: Dict[str, Any],
        target_win_rate: float = 0.50,
        win_rate_tolerance: float = 0.035,
    ):
        self.original_spell_data = copy.deepcopy(spell_data)
        self.tuned_spell_data = copy.deepcopy(spell_data)
        self.telemetry = telemetry
        self.target_win_rate = target_win_rate
        self.win_rate_tolerance = win_rate_tolerance
        self.changelog: List[Dict[str, Any]] = []

    def run_all_algorithms(self) -> Dict[str, Any]:
        """Runs the complete suite of balancing algorithms using score aggregation."""
        print("\n" + "=" * 75)
        print("EXECUTING ADVANCED SPELL BALANCING ALGORITHMS (SCORE-BASED ENGINE)")
        print("=" * 75)

        # Stage 1: Status & Buff Magnitude Balancing Module (clamped 0% to 75%)
        status_buff_knobs = self.tune_status_and_buff_magnitudes(output_path=getattr(self, "status_buff_knobs_path", "status_buff_knobs.json"))

        # Stage 2: Separate algorithms each voting +/-1 score per knob
        winrate_votes = self.algorithm_winrate()
        pickrate_votes = self.algorithm_pickrate()
        cleanse_votes = self.algorithm_cleanse_counterbalance()
        conditional_votes = self.algorithm_conditional_payoffs()

        # Stage 3: Score aggregation (clamped to [-3, +3]) & unified application (2%, 3%, 5%)
        final_modifications = self.apply_unified_adjustments([
            winrate_votes,
            pickrate_votes,
            cleanse_votes,
            conditional_votes,
        ])

        return {
            "changelog": self.changelog,
            "modifications_count": len(self.changelog),
            "final_spell_data": self.tuned_spell_data,
            "status_buff_knobs": status_buff_knobs,
        }

    def tune_status_and_buff_magnitudes(self, output_path: str = "status_buff_knobs.json") -> Dict[str, Any]:
        """
        Status & Buff Magnitude Balancing Module:
        Computes aggregate centered winrate across all spells that apply each specific buff or debuff.
        - If aggregate winrate > 53.5%, scale magnitude downward smoothly (max -5% per run).
        - If aggregate winrate < 46.5%, scale magnitude upward smoothly (max +5% per run).
        Anchors bounds within [0.60x, 1.40x] of design default and strictly within [0%, 75%].
        Saves tuned magnitudes to status_buff_knobs.json and reloads in-memory configs.
        """
        print("\n--- [Status & Buff Magnitude Balancing Module] ---")
        per_spell = self.telemetry["per_spell"]

        tuned_buffs = {}
        tuned_statuses = {}

        # 1. Buffs
        for buff_name, b_cfg in BUFF_CONFIGS.items():
            curr_mag = float(b_cfg["magnitude"])
            default_mag = float(DEFAULT_BUFF_CONFIGS.get(buff_name, b_cfg).get("magnitude", curr_mag))
            applier_recipes = []
            for r, sp_data in self.original_spell_data.items():
                s_tags = tag_spell_synergies(r, sp_data)
                if buff_name in s_tags.get("applies_buff", []):
                    applier_recipes.append(r)

            tot_casts = sum(per_spell.get(r, {}).get("casts", 0) for r in applier_recipes)
            wrs = [per_spell[r]["bayesian_win_rate"] for r in applier_recipes if r in per_spell and per_spell[r].get("casts", 0) > 0]
            agg_wr = sum(wrs) / len(wrs) if wrs else 0.50

            new_mag = curr_mag
            if agg_wr > 0.535:
                delta = agg_wr - 0.50
                scaling = max(0.95, 1.0 - (delta * 0.8))
                new_mag = curr_mag * scaling
                print(f"  * Buff '{buff_name}' overtuned (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude {curr_mag*100:.1f}% -> {new_mag*100:.1f}%")
            elif agg_wr < 0.465 and tot_casts >= 10:
                delta = 0.50 - agg_wr
                scaling = min(1.05, 1.0 + (delta * 0.8))
                new_mag = curr_mag * scaling
                print(f"  * Buff '{buff_name}' undertuned (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude {curr_mag*100:.1f}% -> {new_mag*100:.1f}%")
            else:
                print(f"  * Buff '{buff_name}' balanced (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude remains {curr_mag*100:.1f}%")

            new_mag = max(0.60 * default_mag, min(1.40 * default_mag, new_mag))
            new_mag = max(0.05, min(0.75, new_mag))
            tuned_buffs[buff_name] = round(new_mag, 4)

        # 2. Status Effects (strictly clamped between 0% and 75% and anchored to DEFAULT_STATUS_CONFIGS)
        for st_name, s_cfg in STATUS_CONFIGS.items():
            if st_name in ("Blinded", "Wet", "Shocked"):
                continue
            curr_mag = float(s_cfg["magnitude"])
            default_mag = float(DEFAULT_STATUS_CONFIGS.get(st_name, s_cfg).get("magnitude", curr_mag))
            applier_recipes = []
            for r, sp_data in self.original_spell_data.items():
                s_tags = tag_spell_synergies(r, sp_data)
                if st_name in s_tags.get("applies_status", []):
                    applier_recipes.append(r)

            tot_casts = sum(per_spell.get(r, {}).get("casts", 0) for r in applier_recipes)
            wrs = [per_spell[r]["bayesian_win_rate"] for r in applier_recipes if r in per_spell and per_spell[r].get("casts", 0) > 0]
            agg_wr = sum(wrs) / len(wrs) if wrs else 0.50

            new_mag = curr_mag
            scaling = 1.0
            if agg_wr > 0.535:
                delta = agg_wr - 0.50
                scaling = max(0.95, 1.0 - (delta * 0.8))
                new_mag = curr_mag * scaling
                print(f"  * Status '{st_name}' overtuned (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude {curr_mag*100:.1f}% -> {new_mag*100:.1f}%")
            elif agg_wr < 0.465 and tot_casts >= 10:
                delta = 0.50 - agg_wr
                scaling = min(1.05, 1.0 + (delta * 0.8))
                new_mag = curr_mag * scaling
                print(f"  * Status '{st_name}' undertuned (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude {curr_mag*100:.1f}% -> {new_mag*100:.1f}%")
            else:
                print(f"  * Status '{st_name}' balanced (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude remains {curr_mag*100:.1f}%")

            new_mag = max(0.60 * default_mag, min(1.40 * default_mag, new_mag))
            new_mag = max(0.0, min(0.75, new_mag))

            if "escalation_rate" in s_cfg:
                curr_esc = float(s_cfg["escalation_rate"])
                default_esc = float(DEFAULT_STATUS_CONFIGS.get(st_name, s_cfg).get("escalation_rate", curr_esc))
                scaling_esc = scaling if (agg_wr > 0.535 or (agg_wr < 0.465 and tot_casts >= 10)) else 1.0
                new_esc = curr_esc * scaling_esc
                new_esc = max(0.60 * default_esc, min(1.40 * default_esc, new_esc))
                new_esc = max(0.0, min(0.75, new_esc))
                tuned_statuses[st_name] = {
                    "magnitude": round(new_mag, 4),
                    "escalation_rate": round(new_esc, 4),
                }
                print(f"    -> Tuned escalation rate for '{st_name}': {curr_esc*100:.2f}% -> {new_esc*100:.2f}% (clamped [0%, 75%])")
            else:
                tuned_statuses[st_name] = round(new_mag, 4)

        result = {
            "buffs": tuned_buffs,
            "statuses": tuned_statuses
        }

        out_p = Path(output_path).resolve()
        with open(out_p, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        if SCRIPT_DIR / "status_buff_knobs.json" != out_p:
            try:
                with open(SCRIPT_DIR / "status_buff_knobs.json", "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2)
            except Exception:
                pass
        load_status_buff_knobs(out_p)
        print(f"[Status/Buff Knobs] Exported tuned status & buff magnitudes to: {out_p}")
        return result

    def algorithm_winrate(self) -> Dict[str, Dict[str, Any]]:
        """
        Algorithm 1: Win Rate Outlier Tuner
        Evaluates Bayesian smoothed win rate for each spell against target equilibrium (50% +/- tolerance).
        - Low win rate (< 46.5%): +1 score to buff knob b.
        - High win rate (> 53.5%): -1 score to nerf knob b.
        - Spells with pick rate < 150 per 10k matches are ignored.
        Each separate algorithm can only modify a knob score by at most +/-1.
        """
        print("\n--- [Algorithm 1: Win Rate Outlier Tuner] ---")
        votes: Dict[str, Dict[str, Any]] = {}
        per_spell = self.telemetry["per_spell"]
        eval_games = self.telemetry.get("evaluated_games", 10000)

        for r in self.original_spell_data.keys():
            votes[r] = {"b": 0, "n": 0, "reasons": []}
            sp = per_spell.get(r, {})
            casts = sp.get("casts", 0)
            casts_per_10k = casts * (10000.0 / max(1, eval_games))

            # Requirement 8: If pick rate < 150 per 10,000 matches, do not adjust
            if casts_per_10k < 150:
                continue

            wr = sp.get("bayesian_win_rate", 0.50)
            delta = wr - self.target_win_rate

            if delta < -self.win_rate_tolerance:
                votes[r]["b"] = 1
                reason = f"Win rate undertuned ({wr*100:.1f}% < 46.5%) -> +1 buff score for b"
                votes[r]["reasons"].append(reason)
                print(f"  * [Win Rate Tuner] [{r}] {reason}")
            elif delta > self.win_rate_tolerance:
                votes[r]["b"] = -1
                reason = f"Win rate overtuned ({wr*100:.1f}% > 53.5%) -> -1 nerf score for b"
                votes[r]["reasons"].append(reason)
                print(f"  * [Win Rate Tuner] [{r}] {reason}")

        return votes

    def algorithm_pickrate(self) -> Dict[str, Dict[str, Any]]:
        """
        Algorithm 2: Pick Rate Tuner
        Evaluates cast frequencies normalized per 10,000 matches relative to uniform equilibrium volume.
        - Requirement 8: If pick rate < 150 per 10k matches, do not adjust values.
        - Low pick rate (< low_threshold per 10k matches, ~0.60x uniform share): +1 score to buff under-utilized spells.
        - High pick rate (> high_threshold per 10k matches, ~1.45x uniform share): -1 score to nerf over-spammed spells.
        Each separate algorithm can only modify a knob score by at most +/-1.
        """
        print("\n--- [Algorithm 2: Pick Rate Tuner] ---")
        votes: Dict[str, Dict[str, Any]] = {}
        per_spell = self.telemetry["per_spell"]
        eval_games = self.telemetry.get("evaluated_games", 10000)
        total_casts = self.telemetry.get("total_casts", sum(s.get("casts", 0) for s in per_spell.values()))
        num_spells = max(1, len(self.original_spell_data))
        expected_per_10k = (total_casts / float(num_spells)) * (10000.0 / max(1, eval_games))
        low_threshold = max(800.0, round(expected_per_10k * 0.60, 0)) if total_casts > 0 else 800.0
        high_threshold = max(7000.0, round(expected_per_10k * 1.45, 0)) if total_casts > 0 else 7000.0

        for r in self.original_spell_data.keys():
            votes[r] = {"b": 0, "n": 0, "reasons": []}
            sp = per_spell.get(r, {})
            casts = sp.get("casts", 0)
            casts_per_10k = casts * (10000.0 / max(1, eval_games))

            # Requirement 8: If pick rate < 150 per 10,000 matches, do not adjust
            if casts_per_10k < 150:
                continue

            n_val = float(self.original_spell_data[r].get("n", 0.0))
            desc_text = self.original_spell_data[r].get("description", "")
            uses_n_multiplier = ("(n*b)" in desc_text) or ("**n" in desc_text) or (r in ("EEE", "DFD", "DEF", "DLD", "EWF", "WWD"))
            num_cond = get_spell_condition_complexity(r, sp)
            target_min, _, _, _ = get_condition_complexity_targets(num_cond)
            trig_rate = sp.get("trigger_rate", 0.0)

            # Low pick rate -> +1 buff score
            if casts_per_10k < low_threshold:
                votes[r]["b"] = 1
                if uses_n_multiplier and n_val > 0 and trig_rate >= target_min:
                    votes[r]["n"] = 1
                reason = f"Low pick rate ({casts_per_10k:.0f} casts per 10k < {low_threshold:.0f}) -> +1 buff score"
                votes[r]["reasons"].append(reason)
                print(f"  * [Pick Rate Tuner] [{r}] {reason}")

            # High pick rate -> -1 nerf score
            elif casts_per_10k > high_threshold:
                votes[r]["b"] = -1
                if uses_n_multiplier and n_val > 0:
                    votes[r]["n"] = -1
                reason = f"High pick rate ({casts_per_10k:.0f} casts per 10k > {high_threshold:.0f}) -> -1 nerf score"
                votes[r]["reasons"].append(reason)
                print(f"  * [Pick Rate Tuner] [{r}] {reason}")

        return votes

    def algorithm_cleanse_counterbalance(self) -> Dict[str, Dict[str, Any]]:
        """
        Algorithm 3: Cleanse (WWW) Tuner
        If WWW is overtuned (> 53.5% win rate), mark WWW for nerf (-1 score).
        If WWW is undertuned (< 46.5% win rate), mark WWW for buff (+1 score).
        Instead of adjusting all other spells, inversely adjusts WWW's b value (nerfs increase b, buffs decrease b).
        Spells with pick rate < 150 per 10k matches are excluded.
        Each separate algorithm can only modify a knob score by at most +/-1.
        """
        print("\n--- [Algorithm 3: Cleanse Tuner] ---")
        votes: Dict[str, Dict[str, Any]] = {}
        for r in self.original_spell_data.keys():
            votes[r] = {"b": 0, "n": 0, "reasons": []}

        per_spell = self.telemetry["per_spell"]
        eval_games = self.telemetry.get("evaluated_games", 10000)

        www_info = per_spell.get("WWW", {})
        www_wr = www_info.get("bayesian_win_rate", 0.50)
        www_casts = www_info.get("casts", 0)
        www_casts_per_10k = www_casts * (10000.0 / max(1, eval_games))

        if www_casts_per_10k < 150:
            return votes

        if www_wr > (self.target_win_rate + self.win_rate_tolerance):
            reason_www = f"WWW Cleanse: WWW overtuned (WR: {www_wr*100:.1f}%) -> -1 nerf score for WWW (inversely increases potency penalty b)"
            print(f"  * [Cleanse Tuner] {reason_www}")
            votes["WWW"]["b"] = -1
            votes["WWW"]["reasons"].append(reason_www)

        elif www_wr < (self.target_win_rate - self.win_rate_tolerance):
            reason_www = f"WWW Cleanse: WWW undertuned (WR: {www_wr*100:.1f}%) -> +1 buff score for WWW (inversely decreases potency penalty b)"
            print(f"  * [Cleanse Tuner] {reason_www}")
            votes["WWW"]["b"] = 1
            votes["WWW"]["reasons"].append(reason_www)

        return votes

    def algorithm_conditional_payoffs(self) -> Dict[str, Dict[str, Any]]:
        """
        Algorithm 4: Conditional Payoff & Work-Towards Tuner
        Dynamically adjusts the spread between base factor (b) and payoff multiplier (n) via scores:
        - Under-triggered: widen spread (b -1 score, n +1 score). For Ultimates, protect b floor (+0) and buff setups (+1 score).
        - Over-triggered / Dead-card / Combo-warping: compress spread (b +1 score, n -1 score).
        - In equilibrium: 0 score delta.
        Spells with pick rate < 150 per 10k matches are excluded.
        Each separate algorithm can only modify a knob score by at most +/-1.
        """
        print("\n--- [Algorithm 4: Conditional Payoff & Work-Towards Tuner] ---")
        votes: Dict[str, Dict[str, Any]] = {}
        for r in self.original_spell_data.keys():
            votes[r] = {"b": 0, "n": 0, "reasons": []}

        per_spell = self.telemetry["per_spell"]
        eval_games = self.telemetry.get("evaluated_games", 10000)

        total_casts = self.telemetry.get("total_casts", sum(s.get("casts", 0) for s in per_spell.values()))
        expected_per_10k = (total_casts / float(max(1, len(self.original_spell_data)))) * (10000.0 / max(1, eval_games))
        low_pick_threshold = max(800.0, round(expected_per_10k * 0.60, 0)) if total_casts > 0 else 800.0

        for r, sp in per_spell.items():
            if r == "EEE":
                continue
            n_orig = float(self.original_spell_data.get(r, {}).get("n", 0.0))
            cond_req = self.original_spell_data.get(r, {}).get("condition_required", "None")
            if n_orig <= 0 and cond_req == "None":
                continue

            casts = sp.get("casts", 0)
            casts_per_10k = casts * (10000.0 / max(1, eval_games))
            if casts_per_10k < 150:
                continue

            num_cond = get_spell_condition_complexity(r, sp)
            target_min, target_opt, target_max, min_casts = get_condition_complexity_targets(num_cond)
            trig_rate = sp.get("trigger_rate", 0.0)
            wr = sp.get("bayesian_win_rate", 0.50)

            # Scenario A: Dead-Card Trap Rescue for multi-condition spells
            if num_cond >= 2 and trig_rate < target_min and (casts < min_casts or wr < 0.485):
                votes[r]["b"] = 1
                votes[r]["n"] = -1
                reason = (
                    f"Multi-condition setup trap (N={num_cond}, Trig: {trig_rate*100:.1f}% vs {target_min*100:.0f}%, "
                    f"Casts: {casts}, WR: {wr*100:.1f}%) -> Compress spread: b +1 score, n -1 score"
                )
                votes[r]["reasons"].append(reason)
                print(f"  * [Conditional Payoff Tuner] [{r}] {reason}")

            # Scenario B: Under-triggered condition (incentivize setup)
            elif trig_rate < target_min:
                category = self.original_spell_data.get(r, {}).get("category", "")
                desc_text = self.original_spell_data.get(r, {}).get("description", "")
                uses_n_multiplier = ("(n*b)" in desc_text) or ("**n" in desc_text) or (r in ("EEE", "DFD", "DEF", "DLD", "EWF", "WWD"))
                if category == "Ultimate":
                    # Floor protection: DO NOT cut ultimate base floor
                    votes[r]["b"] = 0
                    votes[r]["n"] = 1
                    reason = (
                        f"Ultimate payoff under-triggered (N={num_cond}, Trig: {trig_rate*100:.1f}% vs {target_min*100:.0f}%). "
                        f"Protected base floor (b +0), buffed payoff: n +1 score"
                    )
                    votes[r]["reasons"].append(reason)
                    print(f"  * [Conditional Payoff Tuner] [{r}] {reason}")

                    # Buff appliers / setups for this ultimate
                    reqs = MULTI_CONDITION_REQUIREMENTS.get(r, [])
                    for req_type, req_val in reqs:
                        for setup_r, setup_data in per_spell.items():
                            if setup_r == r:
                                continue
                            setup_casts = setup_data.get("casts", 0)
                            setup_casts_per_10k = setup_casts * (10000.0 / max(1, eval_games))
                            if setup_casts_per_10k < 150:
                                continue
                            s_tags = tag_spell_synergies(setup_r, self.original_spell_data.get(setup_r, {}))
                            applies = False
                            if req_type == "weather" and getattr(req_val, "value", str(req_val)) in s_tags.get("applies_weather", []):
                                applies = True
                            elif req_type == "location" and getattr(req_val, "value", str(req_val)) in s_tags.get("applies_location", []):
                                applies = True
                            elif req_type == "caster_buff" and req_val in s_tags.get("applies_buff", []):
                                applies = True
                            elif req_type == "target_debuff" and req_val in s_tags.get("applies_status", []):
                                applies = True
                            if applies:
                                votes[setup_r]["b"] = 1
                                setup_reason = f"Buffed setup spell [{setup_r}] (+1 score to b) for under-triggered Ultimate [{r}]"
                                if setup_reason not in votes[setup_r]["reasons"]:
                                    votes[setup_r]["reasons"].append(setup_reason)

                elif uses_n_multiplier:
                    # Widen spread for spells that scale payoff with (n*b).
                    # If the spell is already undertuned in winrate or low in pickrate, protect base floor b (+0)
                    # so b does not cancel out buffs from the Win Rate / Pick Rate tuners.
                    if wr < (self.target_win_rate - 0.015) or casts_per_10k < low_pick_threshold:
                        votes[r]["b"] = 0
                        votes[r]["n"] = 1
                        reason = (
                            f"Conditional payoff under-triggered (N={num_cond}, Trig: {trig_rate*100:.1f}% vs {target_min*100:.0f}%, "
                            f"WR: {wr*100:.1f}%) -> Protected base b (+0), buffed payoff: n +1 score"
                        )
                    else:
                        votes[r]["b"] = -1
                        votes[r]["n"] = 1
                        reason = (
                            f"Conditional payoff under-triggered (N={num_cond}, Trig: {trig_rate*100:.1f}% vs {target_min*100:.0f}%) -> "
                            f"Widen spread: b -1 score, n +1 score"
                        )
                    votes[r]["reasons"].append(reason)
                    print(f"  * [Conditional Payoff Tuner] [{r}] {reason}")
                else:
                    # Fixed status/buff/weather conditional spell (e.g. DLL): protect base floor b from draining into unused n
                    votes[r]["b"] = 0
                    votes[r]["n"] = 0
                    reason = (
                        f"Fixed-effect conditional spell under-triggered (N={num_cond}, Trig: {trig_rate*100:.1f}% vs {target_min*100:.0f}%) -> "
                        f"Protected base damage b (status/buff payoff tuned via status_buff_knobs)"
                    )
                    votes[r]["reasons"].append(reason)
                    print(f"  * [Conditional Payoff Tuner] [{r}] {reason}")

            # Scenario C: Over-triggered / Trivialized condition
            elif trig_rate > target_max:
                desc_text = self.original_spell_data.get(r, {}).get("description", "")
                uses_n_multiplier = ("(n*b)" in desc_text) or ("**n" in desc_text) or (r in ("EEE", "DFD", "DEF", "DLD", "EWF", "WWD"))
                if uses_n_multiplier:
                    votes[r]["b"] = 1
                    votes[r]["n"] = -1
                    reason = (
                        f"Condition triggers excessively (N={num_cond}, Trig: {trig_rate*100:.1f}% vs {target_max*100:.0f}%) -> "
                        f"Compress spread: b +1 score, n -1 score"
                    )
                    votes[r]["reasons"].append(reason)
                    print(f"  * [Conditional Payoff Tuner] [{r}] {reason}")

            # Scenario D: Combo win-rate warping
            elif wr > 0.54 and sp.get("payoff_damage_sum", 0) > sp.get("total_damage", 1) * 0.65:
                desc_text = self.original_spell_data.get(r, {}).get("description", "")
                uses_n_multiplier = ("(n*b)" in desc_text) or ("**n" in desc_text) or (r in ("EEE", "DFD", "DEF", "DLD", "EWF", "WWD"))
                if uses_n_multiplier:
                    votes[r]["b"] = 1
                    votes[r]["n"] = -1
                    reason = (
                        f"Combo payoff warping win rate ({wr*100:.1f}%) -> Compress spread: b +1 score, n -1 score"
                    )
                    votes[r]["reasons"].append(reason)
                    print(f"  * [Conditional Payoff Tuner] [{r}] {reason}")

            else:
                reason = f"Conditional payoff in equilibrium (N={num_cond}, Trig: {trig_rate*100:.1f}%)"
                votes[r]["reasons"].append(reason)

        # Enforce that no single algorithm increases/decreases any knob score by more than 1
        for r in votes:
            votes[r]["b"] = max(-1, min(1, votes[r]["b"]))
            votes[r]["n"] = max(-1, min(1, votes[r]["n"]))

        return votes

    def algorithm_individual_outliers(self) -> Dict[str, Dict[str, Any]]:
        """
        Legacy wrapper combining winrate, pickrate, and cleanse counterbalance votes.
        """
        w_votes = self.algorithm_winrate()
        p_votes = self.algorithm_pickrate()
        c_votes = self.algorithm_cleanse_counterbalance()
        combined: Dict[str, Dict[str, Any]] = {}
        for r in self.original_spell_data.keys():
            combined[r] = {
                "b": w_votes.get(r, {}).get("b", 0) + p_votes.get(r, {}).get("b", 0) + c_votes.get(r, {}).get("b", 0),
                "n": w_votes.get(r, {}).get("n", 0) + p_votes.get(r, {}).get("n", 0) + c_votes.get(r, {}).get("n", 0),
                "reasons": w_votes.get(r, {}).get("reasons", []) + p_votes.get(r, {}).get("reasons", []) + c_votes.get(r, {}).get("reasons", []),
            }
        return combined

    def apply_unified_adjustments(self, *algorithm_votes_args) -> List[Dict[str, Any]]:
        """
        Aggregates buff/nerf scores across all algorithms for each knob (clamped to [-3, +3]),
        applies a single percentage adjustment based on score:
            +3 -> +5%, +2 -> +3%, +1 -> +2%
            -3 -> -5%, -2 -> -3%, -1 -> -2%
             0 -> 0%
        Clamps each knob to sanity bounds: 0 to 200 for b, 0 to 20 for n.
        Spells with pick rate < 150 per 10k matches are not adjusted.
        """
        algorithm_votes = []
        for arg in algorithm_votes_args:
            if isinstance(arg, list):
                algorithm_votes.extend(arg)
            elif isinstance(arg, dict):
                algorithm_votes.append(arg)

        SCORE_TO_PERCENT = {
            3: 0.05,
            2: 0.03,
            1: 0.02,
            0: 0.00,
           -1: -0.02,
           -2: -0.03,
           -3: -0.05,
        }

        eval_games = self.telemetry.get("evaluated_games", 10000)
        per_spell = self.telemetry["per_spell"]
        modifications = []

        print("\n--- [Stage 3: Score Aggregation & Bounds Enforcement] ---")

        for r, orig_data in self.original_spell_data.items():
            b_orig = float(orig_data.get("b", 0.0))
            n_orig = float(orig_data.get("n", 0.0))
            mp_orig = float(orig_data.get("max_potential", 0.0))
            category = orig_data.get("category", "")

            # Requirement 8: If a spell has a pick rate of less than 150 per 10,000 matches, do not adjust its values
            sp_telem = per_spell.get(r, {})
            casts = sp_telem.get("casts", 0)
            casts_per_10k = casts * (10000.0 / max(1, eval_games))
            if casts_per_10k < 150:
                continue

            # Aggregate scores across all algorithms
            raw_b_score = 0
            raw_n_score = 0
            all_reasons = []

            for algo in algorithm_votes:
                if r in algo:
                    raw_b_score += algo[r].get("b", 0)
                    raw_n_score += algo[r].get("n", 0)
                    for reason in algo[r].get("reasons", []):
                        if reason and reason not in all_reasons:
                            all_reasons.append(reason)

            # Mirror spell WLL casts the target's last spell using that spell's own knobs
            if r == "WLL":
                continue

            desc_text = orig_data.get("description", "")
            uses_n_multiplier = ("(n*b)" in desc_text) or ("**n" in desc_text) or (r in ("EEE", "DFD", "DEF", "DLD", "EWF", "WWD"))

            # Spells with b == 0.0 that have no b scaling (EWE, LWE) are tuned via status/buff magnitudes
            if b_orig == 0.0 and r in ("EWE", "LWE"):
                continue

            # Clamp scores between -3 and +3
            b_score = max(-3, min(3, raw_b_score))
            n_score = max(-3, min(3, raw_n_score)) if (n_orig > 0 and uses_n_multiplier) else 0

            b_pct = SCORE_TO_PERCENT[b_score]
            n_pct = SCORE_TO_PERCENT[n_score] if (n_orig > 0 and uses_n_multiplier) else 0.0

            # Apply single buff/nerf percentage
            if r in ("WWW", "DFW", "DFE"):
                # WWW (potency penalty) and DFW / DFE (self-damage to caster) use b as a caster cost/penalty.
                # Inversely adjust b value: Nerfs increase b (larger penalty), Buffs decrease b (smaller penalty).
                b_new = b_orig * (1.0 - b_pct)
            else:
                b_new = b_orig * (1.0 + b_pct)

            # Enforce 2-decimal precision & minimum step for small-b spells (<10.0) so they never freeze on rounding
            if b_orig < 10.0:
                if b_score != 0 and abs(round(b_new, 2) - b_orig) < 0.01:
                    step_dir = -1.0 if (r in ("WWW", "DFW", "DFE") and b_score > 0) or (r not in ("WWW", "DFW", "DFE") and b_score < 0) else 1.0
                    b_new = b_orig + step_dir * 0.02
                b_new = round(b_new, 2)
            else:
                b_new = round(b_new, 1)

            # Requirement 5: Sanity floor and ceiling value clamping (0 to 200 for b) + SPECIAL_BOUNDS enforcement
            b_new = max(0.0, min(200.0, b_new))
            if category == "Ultimate":
                b_new = max(ULTIMATE_B_FLOOR, b_new)
            if r in SPECIAL_BOUNDS:
                min_b, max_b, _, _ = SPECIAL_BOUNDS[r]
                b_new = max(min_b, min(max_b, b_new))
            b_new = round(b_new, 2) if b_orig < 10.0 else round(b_new, 1)

            if n_orig > 0 and uses_n_multiplier:
                n_new = n_orig * (1.0 + n_pct)
                # Requirement 5: Sanity floor and ceiling value clamping (0 to 20 for n) + SPECIAL_BOUNDS enforcement
                n_new = max(0.0, min(20.0, n_new))
                if r in SPECIAL_BOUNDS:
                    _, _, min_n, max_n = SPECIAL_BOUNDS[r]
                    if max_n > 0:
                        n_new = max(min_n, min(max_n, n_new))
                n_new = round(n_new, 2)
            else:
                n_new = n_orig

            # Atomic max_potential calculation: (1 + n) * b if (n > 0 and uses_n_multiplier) else b
            if n_new > 0 and uses_n_multiplier:
                mp_new = round((1.0 + n_new) * b_new, 2 if b_new < 10.0 else 1)
            else:
                mp_new = round(b_new, 2 if b_new < 10.0 else 1)

            changed = (abs(b_new - b_orig) >= 0.01) or (abs(n_new - n_orig) >= 0.01)
            if changed:
                entry = {
                    "recipe": r,
                    "class": orig_data.get("class"),
                    "category": category,
                    "b_old": b_orig,
                    "b_new": b_new,
                    "b_delta_pct": round(((b_new - b_orig) / max(1e-5, b_orig)) * 100, 1),
                    "n_old": n_orig,
                    "n_new": n_new,
                    "n_delta_pct": round(((n_new - n_orig) / max(1e-5, n_orig)) * 100, 1) if n_orig > 0 else 0.0,
                    "max_potential_old": mp_orig,
                    "max_potential_new": mp_new,
                    "b_score": b_score,
                    "n_score": n_score,
                    "reasons": all_reasons,
                }
                modifications.append(entry)
                self.changelog.append(entry)

                self.tuned_spell_data[r]["b"] = b_new
                self.tuned_spell_data[r]["n"] = n_new
                self.tuned_spell_data[r]["max_potential"] = mp_new

                print(
                    f"  * [{r}] Tuning applied: b {b_orig} -> {b_new} (score: {b_score:+d}, {b_pct*100:+.0f}%), "
                    f"n {n_orig} -> {n_new} (score: {n_score:+d}, {n_pct*100:+.0f}%), max_potential: {mp_orig} -> {mp_new}"
                )

        print(f"\n[Synthesis Complete] {len(modifications)} of {len(self.original_spell_data)} spells tuned.")
        return modifications


def run_balance_simulation_suite(
    stage1_matches: int = 2000,
    stage2_matches: int = 2000,
    stage3_matches: int = 2000,
    stage4_matches: int = 2000,
    eval_matches: int = 5000,
    curriculum_path: Optional[str] = None,
    spell_data_path: Optional[str] = None,
    dna_path: Optional[str] = None,
    apply_tuning: bool = True,
    data_log_path: Optional[str] = None,
    knob_log_path: Optional[str] = None,
    sync_interval: int = 50,
    verbose: bool = True,
    total_games: Optional[int] = None,
    eval_games: Optional[int] = None,
    mode: str = "games",
    iterations: Optional[int] = None,
    eval_exploration_rate: float = 0.08,
    persistent_dqn_agent: Optional[Any] = None,
) -> Dict[str, Any]:
    """
    Restructured 5-Phase Iteration Workflow:
    ├── Stage 1 Training: 2,000 matches (Random sampling from Stage 1 Board States)
    ├── Stage 2 Training: 2,000 matches (Random sampling from Stage 2 Board States)
    ├── Stage 3 Training: 2,000 matches (Random sampling from Stage 3 Board States)
    ├── Stage 4 Training: 2,000 matches (Random sampling from Stage 4 Board States)
    └── Evaluation & Balancing: 5,000 matches (Standard unseeded matches from Turn 1)
         ├── Evaluate Multi-Objective Fitness & Select Top Performers
         ├── Run Status & Buff Magnitude Tuner (Clamped between 0% and 75%)
         ├── Run Score-Based Balancing Algorithms (Win Rate, Pick Rate, Cleanse, Conditional)
         ├── Aggregate Scores (-3 to +3) and Apply Single Buff/Nerf (2%, 3%, 5%)
         └── Export updated spell_data.json and status_buff_knobs.json
    """
    resolved_spell_path = simulation.resolve_file_path("spell_data.json", spell_data_path)
    resolved_dna_path = simulation.resolve_file_path("ai_bots_dna.json", dna_path)

    if not resolved_spell_path.exists():
        raise FileNotFoundError(f"Spell data not found at: {resolved_spell_path}")
    if not resolved_dna_path.exists():
        raise FileNotFoundError(f"AI Bots DNA not found at: {resolved_dna_path}")

    with open(resolved_spell_path, "r", encoding="utf-8") as f:
        spell_data = json.load(f)

    # Resolve Curriculum Board States (checks training_stages.json first, then curriculum_board_states.json)
    if curriculum_path:
        curr_path = Path(curriculum_path).resolve()
    else:
        ts_p = simulation.resolve_file_path("training_stages.json")
        if ts_p.exists():
            curr_path = ts_p
        else:
            curr_path = simulation.resolve_file_path("curriculum_board_states.json")

    if not curr_path.exists():
        raise FileNotFoundError(f"Training stages file not found at: {curr_path}")

    with open(curr_path, "r", encoding="utf-8") as f:
        curriculum_data = json.load(f)

    if isinstance(curriculum_data, list):
        stage1_states = list(curriculum_data[0].values()) if len(curriculum_data) > 0 else []
        stage2_states = list(curriculum_data[1].values()) if len(curriculum_data) > 1 else []
        stage3_states = list(curriculum_data[2].values()) if len(curriculum_data) > 2 else []
        stage4_states = list(curriculum_data[3].values()) if len(curriculum_data) > 3 else []
    elif isinstance(curriculum_data, dict):
        stage1_states = list(curriculum_data.get("stage_1", curriculum_data.get("1", curriculum_data.get(1, {}))).values())
        stage2_states = list(curriculum_data.get("stage_2", curriculum_data.get("2", curriculum_data.get(2, {}))).values())
        stage3_states = list(curriculum_data.get("stage_3", curriculum_data.get("3", curriculum_data.get(3, {}))).values())
        stage4_states = list(curriculum_data.get("stage_4", curriculum_data.get("4", curriculum_data.get(4, {}))).values())
    else:
        stage1_states, stage2_states, stage3_states, stage4_states = [], [], [], []

    if eval_games is not None:
        eval_matches = eval_games

    target_total = None
    if mode == "iterations":
        if iterations is not None:
            target_total = iterations
        elif total_games is not None:
            target_total = total_games
    elif total_games is not None:
        target_total = total_games

    if target_total is not None:
        if eval_games is None and target_total < eval_matches:
            eval_matches = max(50, target_total // 2)
        rem = max(0, target_total - eval_matches)
        stage1_matches = rem // 4
        stage2_matches = rem // 4
        stage3_matches = rem // 4
        stage4_matches = rem - (stage1_matches + stage2_matches + stage3_matches)

    total_curriculum_matches = stage1_matches + stage2_matches + stage3_matches + stage4_matches
    total_run_matches = total_curriculum_matches + eval_matches

    print("=" * 75)
    print("PROJECT SORCERY - 5-PHASE CURRICULUM SIMULATION & SPELL BALANCING SUITE")
    print("=" * 75)
    print(f"Stage 1 Training Matches:  {stage1_matches:,} (Sampling from Stage 1 Board States)")
    print(f"Stage 2 Training Matches:  {stage2_matches:,} (Sampling from Stage 2 Board States)")
    print(f"Stage 3 Training Matches:  {stage3_matches:,} (Sampling from Stage 3 Board States)")
    print(f"Stage 4 Training Matches:  {stage4_matches:,} (Sampling from Stage 4 Board States)")
    print(f"Evaluation Matches:        {eval_matches:,} (Standard unseeded matches from Turn 1)")
    print(f"Total Matches Scheduled:   {total_run_matches:,}")
    print(f"Curriculum Source:         {curr_path}")
    print(f"Spell Data Path:           {resolved_spell_path}")
    print(f"AI Bots DNA Path:          {resolved_dna_path}")
    print(f"Apply Tuning to JSON:      {apply_tuning}")
    print("=" * 75)

    # Fast Registry Cache during Batch Loop
    cached_registry = get_registry(str(resolved_spell_path))
    orig_get_registry = project_sorcery.get_registry
    project_sorcery.get_registry = lambda path=None: cached_registry

    # Initialize Persistent DQNAgent to preserve replay buffer and optimizer across all stages and iterations
    action_catalog = cached_registry.all_recipes()
    if persistent_dqn_agent is None:
        with open(resolved_dna_path, "r", encoding="utf-8") as f:
            raw_dna = json.load(f)
        bots = raw_dna.get("bots", [])
        best_bot = max(bots, key=lambda b: b.get("performance_tracker", {}).get("win_rate", 0.5)) if bots else {}
        persistent_dqn_agent = simulation.get_global_dqn_agent(
            action_catalog=action_catalog,
            weights_dict=best_bot.get("dna"),
            reset=False,
            eval_epsilon=eval_exploration_rate,
        )
        # Refresh exploration epsilon at the start of each cycle so the agent adapts to updated spell knobs
        if persistent_dqn_agent is not None:
            persistent_dqn_agent.epsilon = max(persistent_dqn_agent.epsilon, 0.35)

    # Fast In-Memory DNA Cache during Batch Loop with safe disk sync
    cached_dna_data = None
    orig_json_dump = json.dump
    orig_json_load = json.load
    iteration_count = 0

    def fast_json_load(fp, *args, **kwargs):
        nonlocal cached_dna_data
        if cached_dna_data is not None and "ai_bots_dna" in getattr(fp, "name", ""):
            return cached_dna_data
        data = orig_json_load(fp, *args, **kwargs)
        if "ai_bots_dna" in getattr(fp, "name", ""):
            cached_dna_data = data
        return data

    def fast_json_dump(obj, fp, *args, **kwargs):
        nonlocal cached_dna_data, iteration_count
        if "tmp.json" in getattr(fp, "name", ""):
            cached_dna_data = obj
            iteration_count += 1
            if sync_interval > 0 and iteration_count % sync_interval == 0:
                orig_json_dump(obj, fp, separators=(",", ":"))
            return
        return orig_json_dump(obj, fp, *args, **kwargs)

    orig_replace = Path.replace
    def safe_replace(self, target):
        if "tmp.json" in str(self) and "ai_bots_dna" in str(target):
            if self.exists() and self.stat().st_size > 2:
                orig_replace(self, target)
            elif self.exists():
                self.unlink()
            return target
        return orig_replace(self, target)

    json.load = fast_json_load
    json.dump = fast_json_dump
    Path.replace = safe_replace

    start_wall_time = time.time()

    # Initialize Telemetry Tracker for Evaluation Phase
    eval_iters = math.ceil(eval_matches / 50)
    actual_eval_games = eval_iters * 50
    tracker = SimulationTelemetryTracker(
        eval_start_game=0,
        total_games=actual_eval_games,
        spell_data=spell_data,
    )

    try:
        # Phase 1 to 4: Progressive Reverse Curriculum Training
        curriculum_stages = [
            ("Stage 1", stage1_matches, stage1_states),
            ("Stage 2", stage2_matches, stage2_states),
            ("Stage 3", stage3_matches, stage3_states),
            ("Stage 4", stage4_matches, stage4_states),
        ]

        for st_name, st_count, st_boards in curriculum_stages:
            if st_count <= 0:
                continue
            st_iters = math.ceil(st_count / 50)
            if verbose:
                print(f"\n[Curriculum {st_name} Training] Simulating {st_count:,} matches across {st_iters} iterations (DQN Persistent Replay Buffer & Optimizer)...")
            for it in range(1, st_iters + 1):
                simulation.main(
                    dna_path=str(resolved_dna_path),
                    spell_data_path=str(resolved_spell_path),
                    verbose=False,
                    board_states=st_boards,
                    dqn_agent=persistent_dqn_agent,
                    eval_mode=False,
                )
                if verbose and (it % 10 == 0 or it == st_iters):
                    replay_sz = len(persistent_dqn_agent.replay_buffer) if persistent_dqn_agent else 0
                    eps_val = persistent_dqn_agent.epsilon if persistent_dqn_agent else 0.0
                    print(f"  * {st_name}: Iteration {it:3d}/{st_iters} complete ({it*50:,}/{st_count:,} matches | Replay Buffer: {replay_sz:,} | eps={eps_val:.3f})")

        # Phase 5: Evaluation & Balancing (Standard unseeded matches from Turn 1)
        if verbose:
            print(f"\n[Evaluation Phase] Simulating {eval_matches:,} unseeded duels across {eval_iters} iterations (Forced Exploration Rate={eval_exploration_rate:.3f} for ~200 casts per spell)...")
        tracker.install_hooks()
        for it in range(1, eval_iters + 1):
            simulation.main(
                dna_path=str(resolved_dna_path),
                spell_data_path=str(resolved_spell_path),
                verbose=False,
                board_states=None,
                dqn_agent=persistent_dqn_agent,
                eval_mode=True,
                forced_exploration_rate=eval_exploration_rate,
            )
            if verbose and (it % 20 == 0 or it == eval_iters):
                print(f"  * Eval: Iteration {it:3d}/{eval_iters} complete ({it*50:,}/{eval_matches:,} matches recorded)")

    finally:
        project_sorcery.get_registry = orig_get_registry
        json.load = orig_json_load
        json.dump = orig_json_dump
        Path.replace = orig_replace
        tracker.remove_hooks()

        if cached_dna_data is not None:
            print(f"\n[Persistence] Writing finalized bot DNA to: {resolved_dna_path}")
            tmp_path = resolved_dna_path.with_suffix(".final.tmp")
            with open(tmp_path, "w", encoding="utf-8") as f:
                orig_json_dump(cached_dna_data, f, separators=(",", ":"))
            tmp_path.replace(resolved_dna_path)

    total_sim_time = time.time() - start_wall_time
    print(f"\n[Simulation Complete] {total_run_matches:,} total matches ({actual_eval_games:,} evaluated) in {total_sim_time:.1f}s.")

    # Compile Telemetry from Evaluation Window
    telemetry = tracker.compute_aggregates()

    # Execute Balancing Algorithms (A, B, C and status/buff magnitude tuner)
    tuner = SpellBalancingEngine(
        spell_data=spell_data,
        telemetry=telemetry,
        target_win_rate=0.50,
        win_rate_tolerance=0.035,
    )
    tuner.status_buff_knobs_path = str(resolved_spell_path.parent / "status_buff_knobs.json")
    tuning_results = tuner.run_all_algorithms()
    changelog = tuning_results["changelog"]
    tuned_spell_data = tuning_results["final_spell_data"]
    status_buff_knobs = tuning_results.get("status_buff_knobs", {})

    # Persist Tuned Spells to spell_data.json (no backups created)
    if apply_tuning and len(changelog) > 0:
        print(f"[Update] Writing {len(changelog)} tuned spells to: {resolved_spell_path}")
        tmp_spell = resolved_spell_path.with_suffix(".tmp.json")
        with open(tmp_spell, "w", encoding="utf-8") as f:
            json.dump(tuned_spell_data, f, indent=2)
        tmp_spell.replace(resolved_spell_path)
        print("[Update] spell_data.json successfully updated with tuned knobs!")

    eval_matches_count = len(tracker.recorded_duels)
    run_meta = {
        "simulation_mode": "5-phase_curriculum_and_eval",
        "total_games": eval_matches_count,
        "eval_games": eval_matches_count,
        "total_run_matches": total_run_matches,
        "curriculum_games": total_curriculum_matches,
        "elapsed_seconds": round(total_sim_time, 2),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    # Append Data Log for this run (strictly CSV format only, looking exclusively at post-training evaluation matches)
    target_data_log_path = Path(data_log_path).resolve() if data_log_path else (resolved_spell_path.parent / "data_log.csv")
    eval_spell_metrics = telemetry["per_spell"]
    saved_log_path = append_data_log(
        log_path=target_data_log_path,
        run_meta=run_meta,
        spell_metrics=eval_spell_metrics,
        eval_spell_metrics=eval_spell_metrics,
    )

    if not data_log_path and SCRIPT_DIR != resolved_spell_path.parent:
        try:
            append_data_log(
                log_path=(SCRIPT_DIR / "data_log.csv"),
                run_meta=run_meta,
                spell_metrics=eval_spell_metrics,
                eval_spell_metrics=eval_spell_metrics,
            )
        except Exception:
            pass

    # Append Knob Log for this run (strictly CSV format only, listing each change it makes to each knob)
    target_knob_log_path = Path(knob_log_path).resolve() if knob_log_path else (resolved_spell_path.parent / "knob_log.csv")
    saved_knob_log_path = append_knob_log(
        log_path=target_knob_log_path,
        run_meta=run_meta,
        changelog=changelog,
        status_buff_knobs=status_buff_knobs,
        tuned_spell_data=tuned_spell_data,
        original_spell_data=spell_data,
    )

    if not knob_log_path and SCRIPT_DIR != resolved_spell_path.parent:
        try:
            append_knob_log(
                log_path=(SCRIPT_DIR / "knob_log.csv"),
                run_meta=run_meta,
                changelog=changelog,
                status_buff_knobs=status_buff_knobs,
                tuned_spell_data=tuned_spell_data,
                original_spell_data=spell_data,
            )
        except Exception:
            pass

    return {
        "status": "success",
        "total_games": total_run_matches,
        "eval_games": len(tracker.recorded_duels),
        "curriculum_games": total_curriculum_matches,
        "modifications_count": len(changelog),
        "changelog": changelog,
        "status_buff_knobs": status_buff_knobs,
        "knob_log_path": str(target_knob_log_path),
        "elapsed_seconds": total_sim_time,
    }


def append_data_log(
    log_path: Path,
    run_meta: Dict[str, Any],
    spell_metrics: Optional[Dict[str, Dict[str, Any]]] = None,
    run_spell_metrics: Optional[Dict[str, Dict[str, Any]]] = None,
    eval_spell_metrics: Optional[Dict[str, Dict[str, Any]]] = None,
) -> Path:
    """
    Appends telemetry data points for each spell from the post-training evaluation matches
    (e.g., the 5,000 post-training matches) to the CSV data log.
    Strictly outputs ONLY a .csv file (no .json, .jsonl, or .log files).
    Does NOT evaluate all matches across curriculum training, only the post-training matches.

    Data points recorded per spell:
    1. The amount of times each spell was cast during post-training evaluation.
    2. The amount of damage each spell did during post-training evaluation.
    3. The amount of times each conditional spell was cast while its conditions were met during post-training evaluation.
    4. The winrate of each spell during post-training evaluation.
    """
    csv_path = Path(log_path).resolve()
    if csv_path.suffix != ".csv":
        csv_path = csv_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    csv_exists = csv_path.exists()
    csv_headers = [
        "run_id",
        "timestamp",
        "total_games",
        "recipe",
        "class",
        "category",
        "is_conditional",
        "casts",
        "total_damage",
        "conditional_casts_met",
        "winrate",
        "wins",
        "losses",
    ]

    run_id = 1
    if csv_exists:
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = [r for r in reader if r]
                if len(rows) > 1:
                    last_run_id = int(rows[-1][0])
                    run_id = last_run_id + 1
        except Exception:
            run_id = 1
    run_meta["run_id"] = run_id

    timestamp = run_meta.get("timestamp", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    # Use the count of post-training evaluation matches (e.g., 5000), not total matches
    total_games = run_meta.get("eval_games", run_meta.get("total_games", 5000))

    # Target exclusively the post-training evaluation metrics
    target_metrics = eval_spell_metrics or spell_metrics or run_spell_metrics
    if target_metrics is None:
        raise ValueError("No spell metrics provided to append_data_log")

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not csv_exists:
            writer.writerow(csv_headers)
        for recipe, sp in sorted(target_metrics.items()):
            is_cond = sp.get("is_conditional", False)
            cond_trigs = sp.get("conditional_casts_met", sp.get("condition_triggers", 0)) if is_cond else 0
            casts = sp.get("casts", 0)
            damage = round(float(sp.get("total_damage", sp.get("damage", 0.0))), 2)
            winrate = round(float(sp.get("winrate", sp.get("raw_win_rate", 0.0))), 4)
            wins = int(sp.get("wins", sp.get("caster_wins", 0)))
            losses = int(sp.get("losses", sp.get("caster_losses", 0)))

            writer.writerow([
                run_id,
                timestamp,
                total_games,
                recipe,
                sp.get("class", "Unknown"),
                sp.get("category", "Unknown"),
                is_cond,
                casts,
                damage,
                cond_trigs,
                winrate,
                wins,
                losses,
            ])

    print(f"[Data Log] Successfully appended run #{run_id} to CSV log: {csv_path}")
    return csv_path


def append_knob_log(
    log_path: Union[str, Path],
    run_meta: Dict[str, Any],
    changelog: Optional[List[Dict[str, Any]]] = None,
    tuned_spell_data: Optional[Dict[str, Any]] = None,
    original_spell_data: Optional[Dict[str, Any]] = None,
    status_buff_knobs: Optional[Dict[str, Any]] = None,
) -> Path:
    """
    Appends a log of each change made to each knob after a balancing run to the CSV knob log.
    Strictly outputs ONLY a .csv file (no .json, .jsonl, or .log files).
    Creates the CSV file with headers if it does not already exist, or appends new records.

    Data points recorded per knob change:
    1. run_id: Sequential integer identifying the simulation run.
    2. timestamp: ISO-8601 UTC timestamp of the run.
    3. total_games: Number of evaluated matches in the run.
    4. recipe: The spell recipe identifier (e.g., 'FFD').
    5. class: Spell class (e.g., 'Fire').
    6. category: Spell category (e.g., 'Conditional Strike').
    7. knob: Specific formula knob modified ('b', 'n', or 'max_potential').
    8. old_value: Value of the knob prior to tuning.
    9. new_value: Value of the knob after tuning.
    10. delta: Absolute net change (new_value - old_value).
    11. delta_pct: Percentage change relative to the old value.
    12. reasons: Justification(s) from the balancing algorithms.
    """
    csv_path = Path(log_path).resolve()
    if csv_path.suffix != ".csv":
        csv_path = csv_path.with_suffix(".csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    csv_exists = csv_path.exists()
    csv_headers = [
        "run_id",
        "timestamp",
        "total_games",
        "recipe",
        "class",
        "category",
        "knob",
        "old_value",
        "new_value",
        "delta",
        "delta_pct",
        "reasons",
    ]

    run_id = run_meta.get("run_id")
    if run_id is None:
        run_id = 1
        if csv_exists:
            try:
                with open(csv_path, "r", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    rows = [r for r in reader if r]
                    if len(rows) > 1:
                        last_run_id = int(rows[-1][0])
                        run_id = last_run_id + 1
            except Exception:
                run_id = 1
        run_meta["run_id"] = run_id

    timestamp = run_meta.get("timestamp", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    total_games = run_meta.get("eval_games", run_meta.get("total_games", 5000))

    knob_changes = []

    # 1. Spell formula knob adjustments (b, n, max_potential)
    if changelog:
        for entry in changelog:
            recipe = entry.get("recipe", "")
            sp_class = entry.get("class", "Unknown")
            category = entry.get("category", "Unknown")
            all_reasons = entry.get("reasons", [])
            if isinstance(all_reasons, list):
                reasons_str = "; ".join(str(r) for r in all_reasons)
            else:
                reasons_str = str(all_reasons)

            # Knob 'b'
            b_old = entry.get("b_old")
            b_new = entry.get("b_new")
            if b_old is not None and b_new is not None and abs(float(b_new) - float(b_old)) >= 0.01:
                b_delta = round(float(b_new) - float(b_old), 4)
                b_delta_pct = entry.get("b_delta_pct")
                if b_delta_pct is None:
                    b_delta_pct = round(((float(b_new) - float(b_old)) / max(1e-5, float(b_old))) * 100, 1)
                knob_changes.append([
                    run_id,
                    timestamp,
                    total_games,
                    recipe,
                    sp_class,
                    category,
                    "b",
                    round(float(b_old), 2),
                    round(float(b_new), 2),
                    b_delta,
                    b_delta_pct,
                    reasons_str,
                ])

            # Knob 'n'
            n_old = entry.get("n_old")
            n_new = entry.get("n_new")
            if n_old is not None and n_new is not None and abs(float(n_new) - float(n_old)) >= 0.01:
                n_delta = round(float(n_new) - float(n_old), 4)
                n_delta_pct = entry.get("n_delta_pct")
                if n_delta_pct is None:
                    n_delta_pct = round(((float(n_new) - float(n_old)) / max(1e-5, float(n_old))) * 100, 1) if float(n_old) > 0 else 0.0
                knob_changes.append([
                    run_id,
                    timestamp,
                    total_games,
                    recipe,
                    sp_class,
                    category,
                    "n",
                    round(float(n_old), 2),
                    round(float(n_new), 2),
                    n_delta,
                    n_delta_pct,
                    reasons_str,
                ])

            # Knob 'max_potential'
            mp_old = entry.get("max_potential_old")
            mp_new = entry.get("max_potential_new")
            if mp_old is not None and mp_new is not None and abs(float(mp_new) - float(mp_old)) >= 0.01:
                mp_delta = round(float(mp_new) - float(mp_old), 4)
                mp_delta_pct = round(((float(mp_new) - float(mp_old)) / max(1e-5, float(mp_old))) * 100, 1)
                mp_reason = reasons_str if reasons_str else "Recalculated max_potential = (1 + n) * b"
                knob_changes.append([
                    run_id,
                    timestamp,
                    total_games,
                    recipe,
                    sp_class,
                    category,
                    "max_potential",
                    round(float(mp_old), 2),
                    round(float(mp_new), 2),
                    mp_delta,
                    mp_delta_pct,
                    mp_reason,
                ])

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not csv_exists:
            writer.writerow(csv_headers)
        for row in knob_changes:
            writer.writerow(row)

    print(f"[Knob Log] Successfully appended {len(knob_changes)} knob change(s) for run #{run_id} to CSV log: {csv_path}")
    return csv_path



# =============================================================================
# 5. CLI INTERFACE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Project Sorcery 5-Phase Curriculum Simulation & Spell Balancing Engine"
    )
    parser.add_argument(
        "--stage1-matches",
        type=int,
        default=2000,
        help="Stage 1 training matches (default: 2000)",
    )
    parser.add_argument(
        "--stage2-matches",
        type=int,
        default=2000,
        help="Stage 2 training matches (default: 2000)",
    )
    parser.add_argument(
        "--stage3-matches",
        type=int,
        default=2000,
        help="Stage 3 training matches (default: 2000)",
    )
    parser.add_argument(
        "--stage4-matches",
        type=int,
        default=2000,
        help="Stage 4 training matches (default: 2000)",
    )
    parser.add_argument(
        "--eval-matches",
        type=int,
        default=5000,
        help="Unseeded evaluation matches (default: 5000)",
    )
    parser.add_argument(
        "--eval-exploration-rate",
        type=float,
        default=0.08,
        help="Forced exploration rate during evaluation games to ensure spell coverage (~200 casts per spell, default: 0.08)",
    )
    parser.add_argument(
        "--curriculum",
        type=str,
        default=None,
        help="Path to training_stages.json or curriculum_board_states.json",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Quick run mode for testing (50 matches per stage, 100 eval matches)",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["games", "iterations"],
        default="games",
        help="Execution mode: 'games' (runs total matches, e.g. 10000) or 'iterations' (calls main N times)",
    )
    parser.add_argument(
        "--total-games",
        type=int,
        default=None,
        help="Total games to simulate in 'games' mode (default: 10000)",
    )
    parser.add_argument(
        "--eval-games",
        type=int,
        default=None,
        help="Number of games at end to collect aggregate telemetry from (default: 5000)",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=None,
        help="Number of iterations if mode is 'iterations' (default: 10000)",
    )
    parser.add_argument(
        "--cycles",
        type=int,
        default=1,
        help="Number of continuous tuning cycles to execute in loop (default: 1)",
    )
    parser.add_argument(
        "--spells",
        type=str,
        default=None,
        help="Path to spell_data.json (default: auto-detected)",
    )
    parser.add_argument(
        "--dna",
        type=str,
        default=None,
        help="Path to ai_bots_dna.json (default: auto-detected)",
    )
    parser.add_argument(
        "--no-tuning",
        action="store_true",
        help="Do not apply modifications to spell_data.json (dry run telemetry only)",
    )
    parser.add_argument(
        "--data-log",
        type=str,
        default=None,
        help="Custom path for CSV data log file (default: data_log.csv in simulation directory)",
    )
    parser.add_argument(
        "--knob-log",
        type=str,
        default=None,
        help="Custom path for CSV knob log file (default: knob_log.csv in simulation directory)",
    )
    parser.add_argument(
        "--sync-interval",
        type=int,
        default=50,
        help="Iterations between flushing bot DNA to disk (default: 50)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress progress logging during simulation",
    )

    args = parser.parse_args()

    total_runs = args.iterations if args.mode == "iterations" else args.total_games

    for cycle_num in range(1, args.cycles + 1):
        if args.cycles > 1:
            print()
            print("#" * 75)
            print(f"### TUNING CYCLE {cycle_num} OF {args.cycles} ###")
            print("#" * 75)
            print()

        if args.quick:
            s1, s2, s3, s4, ev = 50, 50, 50, 50, 100
        elif args.mode == "iterations" or args.iterations is not None:
            target_total = args.iterations if args.iterations is not None else (args.total_games if args.total_games is not None else 10000)
            if args.eval_games is not None:
                ev = args.eval_games
            elif args.eval_matches != 5000:
                ev = args.eval_matches
            else:
                ev = min(5000, target_total // 2) if target_total < 10000 else 5000
            rem = max(0, target_total - ev)
            s1 = rem // 4
            s2 = rem // 4
            s3 = rem // 4
            s4 = rem - (s1 + s2 + s3)
        elif args.total_games is not None:
            target_total = args.total_games
            if args.eval_games is not None:
                ev = args.eval_games
            elif args.eval_matches != 5000:
                ev = args.eval_matches
            else:
                ev = min(5000, target_total // 2) if target_total < 10000 else 5000
            rem = max(0, target_total - ev)
            s1 = rem // 4
            s2 = rem // 4
            s3 = rem // 4
            s4 = rem - (s1 + s2 + s3)
        elif args.eval_games is not None:
            ev = args.eval_games
            s1 = args.stage1_matches
            s2 = args.stage2_matches
            s3 = args.stage3_matches
            s4 = args.stage4_matches
        else:
            s1 = args.stage1_matches
            s2 = args.stage2_matches
            s3 = args.stage3_matches
            s4 = args.stage4_matches
            ev = args.eval_matches

        run_balance_simulation_suite(
            stage1_matches=s1,
            stage2_matches=s2,
            stage3_matches=s3,
            stage4_matches=s4,
            eval_matches=ev,
            curriculum_path=args.curriculum,
            spell_data_path=args.spells,
            dna_path=args.dna,
            apply_tuning=not args.no_tuning,
            data_log_path=args.data_log,
            knob_log_path=args.knob_log,
            sync_interval=args.sync_interval,
            verbose=not args.quiet,
            total_games=args.total_games,
            eval_games=args.eval_games,
            mode=args.mode,
            iterations=args.iterations,
                    eval_exploration_rate=args.eval_exploration_rate,
        )


if __name__ == "__main__":
    main()
