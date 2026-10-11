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
   - Conditional Payoff Tuner: Detects when conditional payoffs are not being worked
     towards/triggered and widens the spread between base factor (b) and payoff (n).
   - Group-Level Synergy Tuner: Detects over/under-tuned classes and synergy pairs
     (e.g., "spells that apply Frosty" vs "spells that benefit from Frosty",
     "spells that benefit from Sunny"), tuning setup floors and payoff ceilings.
   - Individual Outlier Tuner: Regresses win-rate and combat impact outliers back
     toward equilibrium (50% win rate) using smooth, non-linear confidence scaling.
   - Architectural Constraints: Preserves category bounds and recalculates
     max_potential = (1 + n) * b atomically.
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
    )
except ImportError as e:
    raise ImportError(f"Could not import Project Sorcery modules: {e}")


# =============================================================================
# 1. SYNERGY CONSTANTS & CONDITION CHECKING ENGINE
# =============================================================================

STATUS_EFFECTS = [
    "Frosty", "Burning", "Bleeding", "Stunned", "Entangled", "Cursed",
    "Asleep", "Blinded", "Vulnerable", "Weakened", "Slowed", "Polymorphed", "Poisoned", "Infected"
]

WEATHERS = [
    "Sunny", "Raining", "Blizzard", "Darkness", "Storming", "Blood Rain", "Snowing", "Windy", "Sandstorm", "Clear"
]

LOCATIONS = [
    "Jungle", "Enchanted Forest", "Tundra", "Swamp", "Graveyard", "Space"
]

BUFFS = [
    "Charged", "Shielded", "Honed", "Quickened", "Invisible", "Blessed"
]

# Hard-coded floor for b for all ultimate spells
ULTIMATE_B_FLOOR: float = 20.0

# Bounds for special spells to preserve specific design intent
SPECIAL_BOUNDS: Dict[str, Tuple[float, float, float, float]] = {
    # recipe: (min_b, max_b, min_n, max_n)
    "WWW": (1.0, 1.0, 0.0, 0.0),       # Cleanse utility
    "EEE": (2.0, 10.0, 1.5, 3.5),      # % max health damage
    "EEL": (0.2, 1.5, 0.0, 0.0),       # Health scaling factor
    "EED": (2.0, 10.0, 0.0, 0.0),      # 10 instances
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

    # Status parsing
    for st in STATUS_EFFECTS:
        if any(w in desc for w in [
            f"applies {st}", f"afflicts {st}", f"inflicts {st}",
            f"target is now {st}", f"{st} to the target", f"{st} to both"
        ]):
            tags["applies_status"].append(st)
        if (
            st.lower() in cond.lower()
            or f"target is {st}" in desc
            or f"target is {st.lower()}" in desc
            or f"if target has {st}" in desc
            or f"if the target is {st}" in desc
        ):
            tags["benefits_status"].append(st)

    # Weather parsing
    for w in WEATHERS:
        if (
            f"weather condition to {w}" in desc
            or f"weather to {w}" in desc
            or (f"to {w}" in desc and "weather" in desc)
        ):
            tags["applies_weather"].append(w)
        if (
            w.lower() in cond.lower()
            or f"weather is {w}" in desc.lower()
            or f"weather is {w.lower()}" in desc.lower()
        ):
            tags["benefits_weather"].append(w)

    # Location parsing
    for loc in LOCATIONS:
        if f"location to {loc}" in desc or (f"location is {loc}" in desc and "Changes the location" in desc):
            tags["applies_location"].append(loc)
        if loc.lower() in cond.lower() or f"location is {loc}" in desc.lower():
            tags["benefits_location"].append(loc)

    # Buff parsing
    for bf in BUFFS:
        if any(w in desc for w in [f"grants the caster the {bf}", f"grants the {bf}", f"caster gains {bf}"]):
            tags["applies_buff"].append(bf)
        if bf.lower() in cond.lower() or f"caster is {bf}" in desc or f"if caster is {bf}" in desc:
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
    elif recipe == "EEF":
        return "Frosty" in t_deb
    elif recipe == "EEE":
        return target.current_health < target.max_health
    elif recipe == "LLF":
        return "Cursed" in c_deb
    elif recipe == "LLD":
        return w == Weather.SUNNY and "Blessed" in c_buf
    elif recipe == "DDF":
        return "Asleep" in t_deb
    elif recipe == "FWD":
        return "Cursed" in t_deb and w == Weather.BLOOD_RAIN and loc == Location.GRAVEYARD
    elif recipe == "WFF":
        return "Bleeding" in t_deb
    elif recipe == "WFD":
        return "Shielded" in c_buf or "Honed" in c_buf
    elif recipe == "FEW":
        return "Entangled" in t_deb
    elif recipe == "FED":
        return len(t_deb) > 0
    elif recipe == "EFF":
        return "Vulnerable" in t_deb
    elif recipe == "EFD":
        return "Entangled" in t_deb and loc == Location.JUNGLE
    elif recipe == "FLF":
        return "Stunned" in t_deb
    elif recipe == "FLD":
        return "Stunned" in t_deb and "Charged" in c_buf and w == Weather.STORMING
    elif recipe == "LFF":
        return "Vulnerable" in t_deb
    elif recipe == "LFL":
        return w == Weather.DARKNESS
    elif recipe == "LFD":
        return "Charged" in c_buf
    elif recipe == "FDF":
        return "Invisible" in c_buf
    elif recipe == "FDD":
        return "Blinded" in t_deb and w == Weather.DARKNESS
    elif recipe == "DFF":
        return "Bleeding" in c_deb
    elif recipe == "DFD":
        return caster.current_health < caster.max_health
    elif recipe == "WEF":
        return loc == Location.JUNGLE
    elif recipe == "WED":
        return bool(env.seedling_active and env.seedling_rained_on and env.seedling_sunny_on)
    elif recipe == "EWF":
        return w == Weather.SUNNY
    elif recipe == "EWD":
        return "Entangled" in t_deb
    elif recipe == "WLF":
        return "Cursed" in t_deb
    elif recipe == "WLD":
        return "Asleep" in t_deb and w == Weather.DARKNESS and loc == Location.ENCHANTED_FOREST
    elif recipe == "LWF":
        return loc == Location.ENCHANTED_FOREST
    elif recipe == "LWD":
        return "Polymorphed" in t_deb
    elif recipe == "WDF":
        return w == Weather.RAINING
    elif recipe == "WDD":
        return w == Weather.BLIZZARD and loc == Location.TUNDRA
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
        return "Bleeding" in t_deb and loc == Location.SWAMP
    elif recipe == "DEF":
        return target.get_effective_stat("potency") < target.base_potency
    elif recipe == "DEL":
        return "Bleeding" in t_deb
    elif recipe == "LDL":
        return "Blinded" in t_deb
    elif recipe == "LDD":
        return {"Blinded", "Weakened", "Slowed", "Vulnerable"}.issubset(set(t_deb.keys()))
    elif recipe == "DLF":
        return "Slowed" in t_deb
    elif recipe == "DLL":
        return w == Weather.DARKNESS
    elif recipe == "DLD":
        return target.current_health < target.max_health

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

        def hooked_resolve(resolver_self, recipe, caster, target, env):
            cond_active = is_spell_condition_active(recipe, caster, target, env)
            log = tracker.orig_resolve(resolver_self, recipe, caster, target, env)

            rec = CastRecord(
                recipe=recipe,
                caster=caster.name,
                target=target.name,
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

            # Record duel telemetry for the entire run
            run_duel = DuelTelemetry(
                p1_name=bot_a["bot_id"],
                p2_name=bot_b["bot_id"],
                winner_name=result.get("winner_id", ""),
                turns=result.get("turns", 0),
                casts=list(tracker.run_duel_casts),
            )
            tracker.all_recorded_duels.append(run_duel)

            if tracker.current_game_index >= tracker.eval_start_game:
                duel_data = DuelTelemetry(
                    p1_name=bot_a["bot_id"],
                    p2_name=bot_b["bot_id"],
                    winner_name=result.get("winner_id", ""),
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
            is_cond = (float(data.get("n", 0.0)) > 0.0) or (data.get("condition_required", "None") != "None") or (data.get("category") in ("Conditional Strike", "Ultimate"))
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

            for r, cnt in p1_casts.items():
                if duel.p1_name == winner:
                    per_spell[r]["caster_wins"] += cnt
                else:
                    per_spell[r]["caster_losses"] += cnt

            for r, cnt in p2_casts.items():
                if duel.p2_name == winner:
                    per_spell[r]["caster_wins"] += cnt
                else:
                    per_spell[r]["caster_losses"] += cnt

        for r, sp in per_spell.items():
            casts = sp["casts"]
            wins = sp["caster_wins"]
            losses = sp["caster_losses"]
            total_resolved = wins + losses

            raw_wr = round(wins / max(1, total_resolved), 4) if total_resolved > 0 else 0.0
            k = 12.0
            bayesian_wr = round((wins + k * 0.5) / (total_resolved + k), 4) if total_resolved > 0 else 0.50

            sp["raw_win_rate"] = raw_wr
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
        "LDD": 4,  # Blinded + Weakened + Slowed + Vulnerable
        # 3 conditions:
        "FWD": 3,  # Cursed + Blood Rain + Graveyard
        "FLD": 3,  # Stunned + Charged + Storming
        "WLD": 3,  # Asleep + Darkness + Enchanted Forest
        "WED": 3,  # Seedling active + rained on + sunny on
        # 2 conditions:
        "EDD": 2,  # Bleeding + Swamp
        "EFD": 2,  # Entangled + Jungle
        "FDD": 2,  # Blinded + Darkness
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
    Executes multi-tiered tuning algorithms over aggregate simulation telemetry:
    1. Conditional Payoff & Setup Engine: Adjusts the (b, n) spread for under-triggered payoffs.
    2. Group Synergy Tuner: Balances classes, status appliers vs beneficiaries, and weather setups.
    3. Individual Performance Tuner: Regresses individual win rate and damage outliers.
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
        """Runs the complete suite of balancing algorithms in sequential stages."""
        print("\n" + "=" * 75)
        print("EXECUTING ADVANCED SPELL BALANCING ALGORITHMS")
        print("=" * 75)

        # Stage 1: Group-Level Synergy & Class Tuning (Algorithm A: Classes & Status/Buff Magnitudes)
        group_adjustments = self.algorithm_group_tuning()
        status_buff_knobs = self.tune_status_and_buff_magnitudes()

        # Stage 2: Conditional Payoff & Work-Towards Tuning
        conditional_adjustments = self.algorithm_conditional_payoffs()

        # Stage 3: Individual Outlier & Combat Impact Tuning
        individual_adjustments = self.algorithm_individual_outliers()

        # Stage 4: Unified Multi-Knob Solver & Constraint Enforcement
        final_modifications = self.apply_unified_adjustments(
            group_adjustments, conditional_adjustments, individual_adjustments
        )

        return {
            "changelog": self.changelog,
            "modifications_count": len(self.changelog),
            "final_spell_data": self.tuned_spell_data,
            "status_buff_knobs": status_buff_knobs,
        }

    def tune_status_and_buff_magnitudes(self, output_path: str = "status_buff_knobs.json") -> Dict[str, Any]:
        """
        Algorithm A Extension: Status & Buff Magnitude Balancing Module
        Computes aggregate Bayesian winrate across all spells that apply each specific buff or debuff.
        - If aggregate winrate > 53.5%, damp/reduce baseline magnitude proportionally.
        - If aggregate winrate < 46.5%, scale magnitude upward proportionally (safety clamp +/- 25%).
        Saves tuned magnitudes to status_buff_knobs.json.
        """
        print("\n--- [Algorithm A: Status & Buff Magnitude Balancing Module] ---")
        per_spell = self.telemetry["per_spell"]
        k = 12.0

        tuned_buffs = {}
        tuned_statuses = {}

        # 1. Buffs
        for buff_name, b_cfg in BUFF_CONFIGS.items():
            base_mag = b_cfg["magnitude"]
            applier_recipes = []
            for r, sp_data in self.original_spell_data.items():
                s_tags = tag_spell_synergies(r, sp_data)
                if buff_name in s_tags.get("applies_buff", []):
                    applier_recipes.append(r)

            tot_wins = sum(per_spell.get(r, {}).get("caster_wins", 0) for r in applier_recipes)
            tot_losses = sum(per_spell.get(r, {}).get("caster_losses", 0) for r in applier_recipes)
            tot_resolved = tot_wins + tot_losses
            tot_casts = sum(per_spell.get(r, {}).get("casts", 0) for r in applier_recipes)

            agg_wr = (tot_wins + k * 0.5) / (tot_resolved + k) if tot_resolved > 0 else 0.50

            new_mag = base_mag
            if agg_wr > 0.535:
                delta = agg_wr - 0.50
                scaling = max(0.75, 1.0 - (delta * 2.0))
                new_mag = base_mag * scaling
                print(f"  * Buff '{buff_name}' overtuned (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude {base_mag*100:.1f}% -> {new_mag*100:.1f}%")
            elif agg_wr < 0.465 and tot_casts >= 10:
                delta = 0.50 - agg_wr
                scaling = min(1.25, 1.0 + (delta * 2.0))
                new_mag = base_mag * scaling
                print(f"  * Buff '{buff_name}' undertuned (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude {base_mag*100:.1f}% -> {new_mag*100:.1f}%")
            else:
                print(f"  * Buff '{buff_name}' balanced (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude remains {base_mag*100:.1f}%")

            new_mag = max(0.75 * base_mag, min(1.25 * base_mag, new_mag))
            tuned_buffs[buff_name] = round(new_mag, 4)

        # 2. Status Effects
        for st_name, s_cfg in STATUS_CONFIGS.items():
            base_mag = s_cfg["magnitude"]
            applier_recipes = []
            for r, sp_data in self.original_spell_data.items():
                s_tags = tag_spell_synergies(r, sp_data)
                if st_name in s_tags.get("applies_status", []):
                    applier_recipes.append(r)

            tot_wins = sum(per_spell.get(r, {}).get("caster_wins", 0) for r in applier_recipes)
            tot_losses = sum(per_spell.get(r, {}).get("caster_losses", 0) for r in applier_recipes)
            tot_resolved = tot_wins + tot_losses
            tot_casts = sum(per_spell.get(r, {}).get("casts", 0) for r in applier_recipes)

            agg_wr = (tot_wins + k * 0.5) / (tot_resolved + k) if tot_resolved > 0 else 0.50

            new_mag = base_mag
            if agg_wr > 0.535:
                delta = agg_wr - 0.50
                scaling = max(0.75, 1.0 - (delta * 2.0))
                new_mag = base_mag * scaling
                print(f"  * Status '{st_name}' overtuned (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude {base_mag*100:.1f}% -> {new_mag*100:.1f}%")
            elif agg_wr < 0.465 and tot_casts >= 10:
                delta = 0.50 - agg_wr
                scaling = min(1.25, 1.0 + (delta * 2.0))
                new_mag = base_mag * scaling
                print(f"  * Status '{st_name}' undertuned (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude {base_mag*100:.1f}% -> {new_mag*100:.1f}%")
            else:
                print(f"  * Status '{st_name}' balanced (WR: {agg_wr*100:.1f}%, Casts: {tot_casts}) -> Magnitude remains {base_mag*100:.1f}%")

            new_mag = max(0.75 * base_mag, min(1.25 * base_mag, new_mag))
            tuned_statuses[st_name] = round(new_mag, 4)

        result = {
            "buffs": tuned_buffs,
            "statuses": tuned_statuses
        }

        out_p = Path(output_path).resolve()
        with open(out_p, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        print(f"[Status/Buff Knobs] Exported tuned status & buff magnitudes to: {out_p}")
        return result

    def algorithm_group_tuning(self) -> Dict[str, Dict[str, float]]:
        """
        Algorithm A: Group Synergy & Archetype Balancing
        Evaluates Class performance and Status/Weather synergy pairs:
        - Detects over-tuned or under-tuned classes (win rate > 53.5% or < 46.5%).
        - Detects status/weather synergy imbalances (e.g. Frosty appliers vs beneficiaries,
          Sunny summoners vs beneficiaries).
        """
        print("\n--- [Algorithm A: Group Synergy & Archetype Balancing] ---")
        adjustments: Dict[str, Dict[str, float]] = {}
        for r in self.tuned_spell_data.keys():
            adjustments[r] = {"b_mult": 1.0, "n_mult": 1.0, "reasons": []}

        # 1. Class Tuning
        classes = self.telemetry["classes"]
        for cls_name, cs in classes.items():
            wr = cs["bayesian_win_rate"]
            delta = wr - self.target_win_rate

            if abs(delta) > self.win_rate_tolerance:
                damping = 0.40
                if delta > 0:
                    class_factor = max(0.88, 1.0 - (delta * damping))
                    reason = f"Class {cls_name} overtuned (WR: {wr*100:.1f}%, factor: {class_factor:.3f})"
                else:
                    class_factor = min(1.14, 1.0 + (abs(delta) * damping))
                    reason = f"Class {cls_name} undertuned (WR: {wr*100:.1f}%, factor: {class_factor:.3f})"

                print(f"  * {reason}")
                for rec in cs["spells"]:
                    adjustments[rec]["b_mult"] *= class_factor
                    adjustments[rec]["reasons"].append(reason)

        # 2. Synergy Group Tuning (e.g. Frosty, Sunny, Burning, etc.)
        synergies = self.telemetry["synergies"]
        for syn_key, syn_info in synergies.items():
            name = syn_info["name"]
            kind = syn_info["kind"]
            appliers = syn_info["appliers"]
            beneficiaries = syn_info["beneficiaries"]

            # Appliers evaluation
            if appliers["recipes"] and appliers["casts"] >= 15:
                app_wr = appliers["bayesian_win_rate"]
                app_delta = app_wr - self.target_win_rate

                if app_delta > self.win_rate_tolerance:
                    app_mult = max(0.90, 1.0 - (app_delta * 0.35))
                    reason = f"{kind.capitalize()} '{name}' appliers overtuned on own (WR: {app_wr*100:.1f}%)"
                    print(f"  * {reason} -> Appliers nerfed by {app_mult:.3f}")
                    for r in appliers["recipes"]:
                        adjustments[r]["b_mult"] *= app_mult
                        adjustments[r]["reasons"].append(reason)

                elif app_delta < -self.win_rate_tolerance or appliers["casts"] < 30:
                    app_mult = min(1.12, 1.0 + (abs(app_delta) * 0.35))
                    reason = f"{kind.capitalize()} '{name}' appliers undertuned (WR: {app_wr*100:.1f}%, casts: {appliers['casts']})"
                    print(f"  * {reason} -> Appliers buffed by {app_mult:.3f}")
                    for r in appliers["recipes"]:
                        adjustments[r]["b_mult"] *= app_mult
                        adjustments[r]["reasons"].append(reason)

            # Beneficiaries evaluation
            if beneficiaries["recipes"] and beneficiaries["casts"] >= 15:
                ben_wr = beneficiaries["bayesian_win_rate"]
                ben_delta = ben_wr - self.target_win_rate

                if ben_delta > self.win_rate_tolerance:
                    payoff_nerf = max(0.88, 1.0 - (ben_delta * 0.40))
                    reason = f"{kind.capitalize()} '{name}' beneficiaries overtuned (WR: {ben_wr*100:.1f}%)"
                    print(f"  * {reason} -> Beneficiaries payoff adjusted by {payoff_nerf:.3f}")
                    for r in beneficiaries["recipes"]:
                        adjustments[r]["n_mult"] *= payoff_nerf
                        adjustments[r]["reasons"].append(reason)

                elif ben_delta < -self.win_rate_tolerance:
                    payoff_buff = min(1.15, 1.0 + (abs(ben_delta) * 0.40))
                    reason = f"{kind.capitalize()} '{name}' beneficiaries undertuned (WR: {ben_wr*100:.1f}%)"
                    print(f"  * {reason} -> Beneficiaries payoff buffed by {payoff_buff:.3f}")
                    for r in beneficiaries["recipes"]:
                        adjustments[r]["n_mult"] *= payoff_buff
                        adjustments[r]["reasons"].append(reason)

        return adjustments

    def algorithm_conditional_payoffs(self) -> Dict[str, Dict[str, float]]:
        """
        Algorithm B: Conditional Payoff & Work-Towards Tuning
        Dynamically adjusts the spread between the base factor (b) and payoff multiplier (n)
        with calibrated, bidirectional triggers based on condition complexity (N_cond):

        1. WIDEN SPREAD (decrease b, increase n):
           Triggered when conditional spells are under-triggered (trigger_rate < target_min),
           indicating players are casting the spell unconditionally for raw base stats
           without respecting or setting up the synergy.

        2. COMPRESS SPREAD (increase b, decrease n):
           Triggered under three explicit, calibrated scenarios:
           a) OVER-TRIGGERED / TRIVIALIZED (trigger_rate > target_max):
              The condition is met too easily for its complexity tier, converting situational
              burst into routine, unearned baseline damage.
           b) DEAD-CARD RESCUE (num_conditions >= 2, trigger_rate < target_min, and low casts / low win rate):
              Multi-condition setups are too difficult to achieve in live combat. Continually
              slashing 'b' makes the spell an unplayable dead card. Raising 'b' rescues baseline
              viability while trimming 'n'.
           c) COMBO WARPING (trigger_rate in range, but high win rate driven heavily by payoff damage):
              Reins in polarized burst spikes while preserving setup intent.

        3. DO NOTHING (target_min <= trigger_rate <= target_max):
           The spell operates within its healthy synergy equilibrium window.
        """
        print("\n--- [Algorithm B: Conditional Payoff & Work-Towards Tuner] ---")
        adjustments: Dict[str, Dict[str, float]] = {}
        per_spell = self.telemetry["per_spell"]

        for r, sp in per_spell.items():
            adjustments[r] = {"b_spread_mult": 1.0, "n_spread_mult": 1.0, "reasons": []}
            if sp["n"] <= 0 and sp["condition_required"] == "None":
                continue

            num_cond = get_spell_condition_complexity(r, sp)
            target_min, target_opt, target_max, min_casts = get_condition_complexity_targets(num_cond)

            casts = sp["casts"]
            trig_rate = sp["trigger_rate"]
            wr = sp["bayesian_win_rate"]

            # Trigger to DECREASE SPREAD: Scenario A (Dead-Card Trap Rescue for multi-condition spells)
            if num_cond >= 2 and trig_rate < target_min and (casts < min_casts or wr < 0.485):
                b_increase = 0.08
                n_reduction = 0.06
                b_spread_mult = 1.0 + b_increase
                n_spread_mult = 1.0 - n_reduction

                reason = (
                    f"Multi-condition setup trap (N={num_cond} conditions, Trigger Rate: {trig_rate*100:.1f}% vs "
                    f"{target_min*100:.0f}% floor, Casts: {casts}, WR: {wr*100:.1f}%). "
                    f"Compressing spread to rescue baseline floor: b +{b_increase*100:.1f}%, n -{n_reduction*100:.1f}%"
                )
                print(f"  * [{r}] {reason}")
                adjustments[r]["b_spread_mult"] = b_spread_mult
                adjustments[r]["n_spread_mult"] = n_spread_mult
                adjustments[r]["reasons"].append(reason)

            # Trigger to INCREASE SPREAD: Under-triggered condition (incentivize setup)
            elif trig_rate < target_min:
                deficit = max(0.0, min(1.0, (target_min - trig_rate) / target_min))
                category = sp.get("category", "")

                if category == "Ultimate":
                    # Hard-coded floor protection: DO NOT cut ultimate base floor
                    b_spread_mult = 1.0
                    n_increase = 0.10 + 0.20 * deficit
                    n_spread_mult = 1.0 + n_increase

                    # Shift tuner focus: Buff the appliers / setups for this ultimate
                    reqs = MULTI_CONDITION_REQUIREMENTS.get(r, [])
                    buffed_setups = []
                    for req_type, req_val in reqs:
                        for setup_r, setup_data in self.telemetry["per_spell"].items():
                            if setup_r == r:
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
                                setup_adj = adjustments.setdefault(setup_r, {"b_spread_mult": 1.0, "n_spread_mult": 1.0, "reasons": []})
                                setup_adj["b_spread_mult"] = max(setup_adj.get("b_spread_mult", 1.0), 1.15)
                                setup_reason = f"Buffed setup spell [{setup_r}] (+15.0% b tempo) to facilitate under-triggered Ultimate [{r}]"
                                if setup_reason not in setup_adj["reasons"]:
                                    setup_adj["reasons"].append(setup_reason)
                                buffed_setups.append(setup_r)

                    reason = (
                        f"Ultimate payoff under-triggered (N={num_cond} conditions, Trigger Rate: {trig_rate*100:.1f}% vs "
                        f"{target_min*100:.0f}% floor, Casts: {casts}). Shifted tuner focus: protected ultimate base floor at {sp['b']} "
                        f"(hard-coded floor >= {ULTIMATE_B_FLOOR}) and buffed appliers/setups ({', '.join(buffed_setups)}) with +15% b tempo."
                    )
                    print(f"  * [{r}] {reason}")
                    adjustments[r]["b_spread_mult"] = b_spread_mult
                    adjustments[r]["n_spread_mult"] = n_spread_mult
                    adjustments[r]["reasons"].append(reason)

                elif num_cond >= 2:
                    # Multi-condition spells: affect spread gently rather than severely
                    b_reduction = 0.04 + 0.04 * deficit
                    b_spread_mult = 1.0 - b_reduction
                    b_initial = float(self.original_spell_data[r].get("b", sp["b"]))
                    b_floor = 0.70 * b_initial
                    if sp["b"] * b_spread_mult < b_floor:
                        b_spread_mult = max(b_spread_mult, b_floor / max(1e-5, sp["b"]))

                    n_increase = 0.06 + 0.08 * deficit
                    n_spread_mult = 1.0 + n_increase

                    reason = (
                        f"Multi-condition payoff under-triggered (N={num_cond} conditions, Trigger Rate: {trig_rate*100:.1f}% vs "
                        f"{target_min*100:.0f}% floor, Casts: {casts}). Mild spread adjustment: b -{b_reduction*100:.1f}%, n +{n_increase*100:.1f}%"
                    )
                    print(f"  * [{r}] {reason}")
                    adjustments[r]["b_spread_mult"] = b_spread_mult
                    adjustments[r]["n_spread_mult"] = n_spread_mult
                    adjustments[r]["reasons"].append(reason)

                else:
                    if casts < min_casts and num_cond == 1:
                        pick_penalty = max(0.0, (min_casts - casts) / min_casts)
                        deficit = max(deficit, 0.40 + 0.60 * pick_penalty)

                    b_reduction = 0.06 + 0.12 * deficit
                    b_spread_mult = 1.0 - b_reduction

                    # Algorithm B Hard Floor Constraint: b_min = 0.60 * b_initial
                    b_initial = float(self.original_spell_data[r].get("b", sp["b"]))
                    b_floor = 0.60 * b_initial
                    if sp["b"] * b_spread_mult < b_floor:
                        b_spread_mult = max(b_spread_mult, b_floor / max(1e-5, sp["b"]))

                    n_increase = 0.12 + 0.25 * deficit
                    n_spread_mult = 1.0 + n_increase

                    reason = (
                        f"Conditional payoff under-triggered (N={num_cond} conditions, Trigger Rate: {trig_rate*100:.1f}% vs "
                        f"{target_min*100:.0f}% floor, Casts: {casts}). "
                        f"Increasing spread: b -{b_reduction*100:.1f}%, n +{n_increase*100:.1f}%"
                    )
                    print(f"  * [{r}] {reason}")
                    adjustments[r]["b_spread_mult"] = b_spread_mult
                    adjustments[r]["n_spread_mult"] = n_spread_mult
                    adjustments[r]["reasons"].append(reason)

            # Trigger to DECREASE SPREAD: Scenario B (Over-triggered / Trivialized condition)
            elif trig_rate > target_max:
                excess = max(0.0, min(1.0, (trig_rate - target_max) / (1.0 - target_max)))
                wr_amp = max(0.0, (wr - 0.50) * 0.4) if wr > 0.52 else 0.0

                b_increase = 0.05 + 0.10 * excess + wr_amp
                b_spread_mult = 1.0 + b_increase

                n_reduction = 0.08 + 0.16 * excess + wr_amp
                n_spread_mult = 1.0 - n_reduction

                reason = (
                    f"Condition triggers excessively (N={num_cond} conditions, Trigger Rate: {trig_rate*100:.1f}% vs "
                    f"{target_max*100:.0f}% ceiling, WR: {wr*100:.1f}%). "
                    f"Compressing spread: b +{b_increase*100:.1f}%, n -{n_reduction*100:.1f}%"
                )
                print(f"  * [{r}] {reason}")
                adjustments[r]["b_spread_mult"] = b_spread_mult
                adjustments[r]["n_spread_mult"] = n_spread_mult
                adjustments[r]["reasons"].append(reason)

            # Trigger to DECREASE SPREAD: Scenario C (Combo win-rate warping despite normal trigger rate)
            elif wr > 0.54 and sp.get("payoff_damage_sum", 0) > sp.get("total_damage", 1) * 0.65:
                b_spread_mult = 1.03
                n_spread_mult = 0.92
                reason = (
                    f"Condition triggers within target window ({trig_rate*100:.1f}%), but combo payoff is "
                    f"warping win rate ({wr*100:.1f}%). Compressing spread: b +3.0%, n -8.0%"
                )
                print(f"  * [{r}] {reason}")
                adjustments[r]["b_spread_mult"] = b_spread_mult
                adjustments[r]["n_spread_mult"] = n_spread_mult
                adjustments[r]["reasons"].append(reason)

            # DO NOTHING: Healthy equilibrium
            else:
                reason = (
                    f"Conditional payoff in equilibrium (N={num_cond} conditions, Trigger Rate: {trig_rate*100:.1f}% "
                    f"within [{target_min*100:.0f}%-{target_max*100:.0f}%] target window, WR: {wr*100:.1f}%)."
                )
                adjustments[r]["reasons"].append(reason)

        return adjustments

    def algorithm_individual_outliers(self) -> Dict[str, Dict[str, float]]:
        """
        Algorithm C: Individual Spell Outlier & Performance Tuner
        Uses Bayesian smoothed win rate and average damage per cast vs category
        benchmarks to correct remaining single-spell imbalances.
        """
        print("\n--- [Algorithm C: Individual Spell Performance Tuner] ---")
        adjustments: Dict[str, Dict[str, float]] = {}
        per_spell = self.telemetry["per_spell"]

        for r, sp in per_spell.items():
            adjustments[r] = {"b_indiv_mult": 1.0, "reasons": []}
            casts = sp["casts"]
            wr = sp["bayesian_win_rate"]
            delta = wr - self.target_win_rate

            confidence = min(1.0, math.sqrt(max(1, casts) / 50.0))

            if abs(delta) > self.win_rate_tolerance:
                adjustment_strength = 0.45 * (abs(delta) ** 1.1) * confidence
                adjustment_strength = min(0.18, adjustment_strength)

                if delta > 0:
                    mult = 1.0 - adjustment_strength
                    reason = f"Individual spell overtuned (WR: {wr*100:.1f}%, Casts: {casts}, mult: {mult:.3f})"
                else:
                    mult = 1.0 + adjustment_strength
                    reason = f"Individual spell undertuned (WR: {wr*100:.1f}%, Casts: {casts}, mult: {mult:.3f})"

                print(f"  * [{r}] {reason}")
                adjustments[r]["b_indiv_mult"] = mult
                adjustments[r]["reasons"].append(reason)

        return adjustments

    def apply_unified_adjustments(
        self,
        group_adj: Dict[str, Dict[str, float]],
        cond_adj: Dict[str, Dict[str, float]],
        indiv_adj: Dict[str, Dict[str, float]],
    ) -> List[Dict[str, Any]]:
        """
        Synthesizes all tuning factors, applies safe clamping bounds,
        recomputes max_potential, and records an audited changelog.
        """
        print("\n--- [Stage 4: Unified Multi-Knob Synthesis & Bounds Enforcement] ---")
        modifications = []

        for r, orig_data in self.original_spell_data.items():
            b_orig = float(orig_data.get("b", 0.0))
            n_orig = float(orig_data.get("n", 0.0))
            mp_orig = float(orig_data.get("max_potential", 0.0))
            category = orig_data.get("category", "")

            # Combine multipliers
            g_b = group_adj.get(r, {}).get("b_mult", 1.0)
            g_n = group_adj.get(r, {}).get("n_mult", 1.0)
            c_b = cond_adj.get(r, {}).get("b_spread_mult", 1.0)
            c_n = cond_adj.get(r, {}).get("n_spread_mult", 1.0)
            i_b = indiv_adj.get(r, {}).get("b_indiv_mult", 1.0)

            total_b_factor = g_b * c_b * i_b
            total_n_factor = g_n * c_n

            # Bounds determination (respecting each spell's architectural baseline)
            if r in SPECIAL_BOUNDS:
                min_b, max_b, min_n, max_n = SPECIAL_BOUNDS[r]
            else:
                # b bounds based on category floor and original design scale
                if category in ["Setup - Weather", "Setup - Location"]:
                    min_b = min(b_orig * 0.6, 10.0)
                    max_b = max(b_orig * 1.4, 35.0)
                elif category == "Ultimate":
                    min_b = max(ULTIMATE_B_FLOOR, 20.0)
                    max_b = max(b_orig * 1.4, 45.0)
                elif category == "Conditional Strike":
                    min_b = min(b_orig * 0.6, 14.0)
                    max_b = max(b_orig * 1.4, 48.0)
                elif category == "Buff / Sustain":
                    min_b = min(b_orig * 0.6, 15.0)
                    max_b = max(b_orig * 1.4, 70.0)
                elif category == "Debuff / Control":
                    min_b = min(b_orig * 0.6, 10.0)
                    max_b = max(b_orig * 1.4, 60.0)
                else:  # Direct Damage
                    min_b = min(b_orig * 0.6, 20.0)
                    max_b = max(b_orig * 1.4, 85.0)

                # n bounds: preserve and scale n if spell has an active payoff multiplier
                if n_orig > 0:
                    if category == "Ultimate":
                        min_n = min(n_orig * 0.7, 3.0)
                        max_n = max(n_orig * 1.6, 8.0)
                    else:
                        min_n = min(n_orig * 0.7, 1.5)
                        max_n = max(n_orig * 1.6, 4.5)
                else:
                    min_n, max_n = 0.0, 0.0

            b_new = max(min_b, min(max_b, b_orig * total_b_factor))
            if category == "Ultimate":
                b_new = max(ULTIMATE_B_FLOOR, b_new)
            is_conditional = (n_orig > 0) or (orig_data.get("condition_required", "None") != "None")
            if is_conditional:
                b_new = max(round(0.60 * b_orig, 1), b_new)
            b_new = round(b_new, 1)

            if n_orig > 0:
                n_new = max(min_n, min(max_n, n_orig * total_n_factor))
                n_new = round(n_new, 1)
            else:
                n_new = 0.0

            # Recompute max_potential formula: (1 + n) * b if n > 0 else b
            if n_new > 0:
                mp_new = round((1.0 + n_new) * b_new, 1)
            else:
                mp_new = round(b_new, 1)

            changed = (abs(b_new - b_orig) >= 0.1) or (abs(n_new - n_orig) >= 0.1)

            if changed:
                all_reasons = (
                    group_adj.get(r, {}).get("reasons", [])
                    + cond_adj.get(r, {}).get("reasons", [])
                    + indiv_adj.get(r, {}).get("reasons", [])
                )
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
                    "reasons": all_reasons,
                }
                modifications.append(entry)
                self.changelog.append(entry)

                self.tuned_spell_data[r]["b"] = b_new
                self.tuned_spell_data[r]["n"] = n_new
                self.tuned_spell_data[r]["max_potential"] = mp_new

        print(f"\n[Synthesis Complete] {len(modifications)} of 125 spells tuned.")
        return modifications


# =============================================================================
# 4. SIMULATION ORCHESTRATOR & BATCH RUNNER
# =============================================================================

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
    sync_interval: int = 50,
    verbose: bool = True,
    total_games: Optional[int] = None,
    eval_games: Optional[int] = None,
    mode: str = "games",
) -> Dict[str, Any]:
    """
    Restructured 5-Phase Iteration Workflow:
    ├── Stage 1 Training: 2,000 matches (Random sampling from Stage 1 Board States)
    ├── Stage 2 Training: 2,000 matches (Random sampling from Stage 2 Board States)
    ├── Stage 3 Training: 2,000 matches (Random sampling from Stage 3 Board States)
    ├── Stage 4 Training: 2,000 matches (Random sampling from Stage 4 Board States)
    └── Evaluation & Balancing: 5,000 matches (Standard unseeded matches from Turn 1)
         ├── Evaluate Multi-Objective Fitness & Select Top Performers
         ├── Run Algorithm A (Classes & Status/Buff Magnitudes)
         ├── Run Algorithm B (Conditional Spreads with b Floor)
         ├── Run Algorithm C (Outlier Regressions)
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

    # Resolve Curriculum Board States
    curr_path = Path(curriculum_path).resolve() if curriculum_path else simulation.resolve_file_path("curriculum_board_states.json")
    if not curr_path.exists():
        if generate_board_states is not None:
            print("[Curriculum] Generating curriculum_board_states.json...")
            generate_board_states.generate_curriculum(str(resolved_spell_path), str(curr_path))
        else:
            raise FileNotFoundError(f"Curriculum board states not found at: {curr_path}")

    with open(curr_path, "r", encoding="utf-8") as f:
        curriculum_data = json.load(f)

    stage1_states = list(curriculum_data[0].values()) if len(curriculum_data) > 0 else []
    stage2_states = list(curriculum_data[1].values()) if len(curriculum_data) > 1 else []
    stage3_states = list(curriculum_data[2].values()) if len(curriculum_data) > 2 else []
    stage4_states = list(curriculum_data[3].values()) if len(curriculum_data) > 3 else []

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

    # Fast In-Memory DNA Cache during Batch Loop
    cached_dna_data = None
    orig_json_dump = json.dump
    orig_json_load = json.load

    def fast_json_load(fp, *args, **kwargs):
        nonlocal cached_dna_data
        if cached_dna_data is not None and "ai_bots_dna" in getattr(fp, "name", ""):
            return cached_dna_data
        data = orig_json_load(fp, *args, **kwargs)
        if "ai_bots_dna" in getattr(fp, "name", ""):
            cached_dna_data = data
        return data

    def fast_json_dump(obj, fp, *args, **kwargs):
        nonlocal cached_dna_data
        if "tmp.json" in getattr(fp, "name", ""):
            cached_dna_data = obj
            fp.write("{}")
            return
        return orig_json_dump(obj, fp, *args, **kwargs)

    json.load = fast_json_load
    json.dump = fast_json_dump

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
                print(f"\n[Curriculum {st_name} Training] Simulating {st_count:,} matches across {st_iters} iterations...")
            for it in range(1, st_iters + 1):
                simulation.main(
                    dna_path=str(resolved_dna_path),
                    spell_data_path=str(resolved_spell_path),
                    verbose=False,
                    board_states=st_boards,
                )
                if verbose and (it % 10 == 0 or it == st_iters):
                    print(f"  * {st_name}: Iteration {it:3d}/{st_iters} complete ({it*50:,}/{st_count:,} matches)")

        # Phase 5: Evaluation & Balancing (Standard unseeded matches from Turn 1)
        if verbose:
            print(f"\n[Evaluation Phase] Simulating {eval_matches:,} unseeded duels across {eval_iters} iterations...")
        tracker.install_hooks()
        for it in range(1, eval_iters + 1):
            simulation.main(
                dna_path=str(resolved_dna_path),
                spell_data_path=str(resolved_spell_path),
                verbose=False,
                board_states=None,
            )
            if verbose and (it % 20 == 0 or it == eval_iters):
                print(f"  * Eval: Iteration {it:3d}/{eval_iters} complete ({it*50:,}/{eval_matches:,} matches recorded)")

    finally:
        project_sorcery.get_registry = orig_get_registry
        json.load = orig_json_load
        json.dump = orig_json_dump
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

    return {
        "status": "success",
        "total_games": total_run_matches,
        "eval_games": len(tracker.recorded_duels),
        "curriculum_games": total_curriculum_matches,
        "modifications_count": len(changelog),
        "changelog": changelog,
        "status_buff_knobs": status_buff_knobs,
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
        "--curriculum",
        type=str,
        default=None,
        help="Path to curriculum_board_states.json",
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
        default=10000,
        help="Total games to simulate in 'games' mode (default: 10000)",
    )
    parser.add_argument(
        "--eval-games",
        type=int,
        default=5000,
        help="Number of games at end to collect aggregate telemetry from (default: 5000)",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=10000,
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

        s1 = 50 if args.quick else args.stage1_matches
        s2 = 50 if args.quick else args.stage2_matches
        s3 = 50 if args.quick else args.stage3_matches
        s4 = 50 if args.quick else args.stage4_matches
        ev = 100 if args.quick else args.eval_matches

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
            sync_interval=args.sync_interval,
            verbose=not args.quiet,
        )


if __name__ == "__main__":
    main()
