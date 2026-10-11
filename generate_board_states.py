#!/usr/bin/env python3
"""
generate_board_states.py
========================
Generates 500 multi-stage board states (125 spells x 4 progressive difficulty stages)
for Reverse Curriculum Learning in Project Sorcery.
Exports: curriculum_board_states.json structured as [stage_1, stage_2, stage_3, stage_4],
each containing 125 entries indexed by target spell recipe.
"""

import json
import random
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from project_sorcery import (
    ALL_RUNES,
    BUFF_CONFIGS,
    STATUS_CONFIGS,
    Location,
    Weather,
    SpellClass,
    MULTI_CONDITION_REQUIREMENTS,
    get_spell_class,
    get_registry,
)

SCRIPT_DIR = Path(__file__).resolve().parent

# Class affinities for favorable weather and locations
CLASS_FAVORABLE_WEATHER: Dict[SpellClass, Weather] = {
    SpellClass.FIRE: Weather.SUNNY,
    SpellClass.WATER: Weather.RAINING,
    SpellClass.EARTH: Weather.SANDSTORM,
    SpellClass.LIGHT: Weather.SUNNY,
    SpellClass.DARK: Weather.DARKNESS,
    SpellClass.GHOSTFIRE: Weather.BLOOD_RAIN,
    SpellClass.BEASTS: Weather.STORMING,
    SpellClass.LIGHTNING: Weather.STORMING,
    SpellClass.BLOOD: Weather.BLOOD_RAIN,
    SpellClass.PLANTS: Weather.SUNNY,
    SpellClass.FEY: Weather.DARKNESS,
    SpellClass.ICE: Weather.BLIZZARD,
    SpellClass.WIND: Weather.WINDY,
    SpellClass.POISON: Weather.RAINING,
    SpellClass.COSMIC: Weather.DARKNESS,
}

CLASS_FAVORABLE_LOCATION: Dict[SpellClass, Location] = {
    SpellClass.FIRE: Location.JUNGLE, # Or Graveyard
    SpellClass.WATER: Location.SWAMP,
    SpellClass.EARTH: Location.JUNGLE,
    SpellClass.LIGHT: Location.ENCHANTED_FOREST,
    SpellClass.DARK: Location.GRAVEYARD,
    SpellClass.GHOSTFIRE: Location.GRAVEYARD,
    SpellClass.BEASTS: Location.JUNGLE,
    SpellClass.LIGHTNING: Location.GRAVEYARD,
    SpellClass.BLOOD: Location.GRAVEYARD,
    SpellClass.PLANTS: Location.JUNGLE,
    SpellClass.FEY: Location.ENCHANTED_FOREST,
    SpellClass.ICE: Location.TUNDRA,
    SpellClass.WIND: Location.JUNGLE,
    SpellClass.POISON: Location.SWAMP,
    SpellClass.COSMIC: Location.SPACE,
}

NON_DEFAULT_WEATHERS = [w for w in Weather if w != Weather.CLEAR]
NON_DEFAULT_LOCATIONS = [l for l in Location if l != Location.NONE]


STAGE_CONFIG: Dict[int, Dict[str, int]] = {
    1: {"turn": 6, "target_pool_size": 5},
    2: {"turn": 5, "target_pool_size": 5},
    3: {"turn": 3, "target_pool_size": 4},
    4: {"turn": 1, "target_pool_size": 3},
}


def make_rune_pools_for_stage(recipe: str, stage: int) -> Tuple[List[str], List[str]]:
    """
    Rune pool guarantee per stage:
    Stage 1 (turn 6): target pool size 5 -> 3 required runes for recipe + 2 random runes for P1; 5 random runes for P2.
    Stage 2 (turn 5): target pool size 5 -> 3 required runes for recipe + 2 random runes for P1; 5 random runes for P2.
    Stage 3 (turn 3): target pool size 4 -> 3 required runes for recipe + 1 random rune for P1; 4 random runes for P2.
    Stage 4 (turn 1): target pool size 3 -> 3 required runes for recipe + 0 random runes for P1; 3 random runes for P2.
    """
    cfg = STAGE_CONFIG[stage]
    pool_size = cfg["target_pool_size"]

    p1_pool = list(recipe.upper())
    if pool_size > 3:
        p1_pool.extend(random.choices(ALL_RUNES, k=pool_size - 3))
    random.shuffle(p1_pool)

    p2_pool = random.choices(ALL_RUNES, k=pool_size)
    return p1_pool, p2_pool


def generate_board_state_for_spell(
    recipe: str,
    spell_info: Dict[str, Any],
    stage: int,
) -> Dict[str, Any]:
    """Generates a board state dict for a given spell and stage (1..4)."""
    s_class = get_spell_class(recipe)
    fav_weather = CLASS_FAVORABLE_WEATHER.get(s_class, Weather.SUNNY)
    fav_location = CLASS_FAVORABLE_LOCATION.get(s_class, Location.JUNGLE)

    cfg = STAGE_CONFIG[stage]
    turn_num = cfg["turn"]
    p1_rune_pool, p2_rune_pool = make_rune_pools_for_stage(recipe, stage)

    # Defaults
    weather = random.choice(NON_DEFAULT_WEATHERS).value
    location = random.choice(NON_DEFAULT_LOCATIONS).value
    p1_buffs: Dict[str, int] = {}
    p1_debuffs: Dict[str, int] = {}
    p1_class_mults: Dict[str, float] = {}

    p2_buffs: Dict[str, int] = {}
    p2_debuffs: Dict[str, int] = {}
    p2_class_mults: Dict[str, float] = {}

    seedling_active = False
    seedling_rained_on = False
    seedling_sunny_on = False

    cond_req = spell_info.get("condition_required", "None")

    if stage == 4:
        # Stage 4: Baseline / Natural Start
        # Random non-default weather & location, no active debuffs on target, standard stats
        weather = random.choice(NON_DEFAULT_WEATHERS).value
        location = random.choice(NON_DEFAULT_LOCATIONS).value

    elif recipe in MULTI_CONDITION_REQUIREMENTS:
        # Multi-Condition Spells (LLD, FWD, FLD, FDD, EFD, EDD, WDD, WED, WLD, LDD)
        reqs = MULTI_CONDITION_REQUIREMENTS[recipe]
        n_reqs = len(reqs)

        if stage == 1:
            # Stage 1: Ideal / Payoff State (100% of conditions fulfilled)
            weather = fav_weather.value
            location = fav_location.value
            p1_buffs["Charged"] = 6
            p1_buffs["Quickened"] = 6
            p1_class_mults[s_class.value] = 1.25

            for req_type, req_val in reqs:
                if req_type == "weather":
                    weather = req_val.value if hasattr(req_val, "value") else str(req_val)
                elif req_type == "location":
                    location = req_val.value if hasattr(req_val, "value") else str(req_val)
                elif req_type == "caster_buff":
                    p1_buffs[req_val] = 6
                elif req_type == "target_debuff":
                    dur = STATUS_CONFIGS[req_val]["duration"]
                    p2_debuffs[req_val] = dur if dur > 0 else 6
                elif req_type == "seedling":
                    if req_val == "active": seedling_active = True
                    elif req_val == "rained_on": seedling_rained_on = True
                    elif req_val == "sunny_on": seedling_sunny_on = True

        elif stage == 2:
            # Stage 2: High Synergy (~75% setup complete)
            # 3 of 4 for 4-cond; 2 of 3 for 3-cond; 1-2 for 2-cond
            num_to_meet = max(1, int(round(n_reqs * 0.75)))
            chosen_reqs = reqs[:num_to_meet]

            for req_type, req_val in chosen_reqs:
                if req_type == "weather":
                    weather = req_val.value if hasattr(req_val, "value") else str(req_val)
                elif req_type == "location":
                    location = req_val.value if hasattr(req_val, "value") else str(req_val)
                elif req_type == "caster_buff":
                    p1_buffs[req_val] = 6
                elif req_type == "target_debuff":
                    dur = STATUS_CONFIGS[req_val]["duration"]
                    p2_debuffs[req_val] = dur if dur > 0 else 6
                elif req_type == "seedling":
                    if req_val == "active": seedling_active = True
                    elif req_val == "rained_on": seedling_rained_on = True
                    elif req_val == "sunny_on": seedling_sunny_on = True

            p1_buffs["Charged"] = 6

        elif stage == 3:
            # Stage 3: Low Synergy (only 1 prerequisite condition active)
            first_req = reqs[0]
            req_type, req_val = first_req
            if req_type == "weather":
                weather = req_val.value if hasattr(req_val, "value") else str(req_val)
            elif req_type == "location":
                location = req_val.value if hasattr(req_val, "value") else str(req_val)
            elif req_type == "caster_buff":
                p1_buffs[req_val] = 6
            elif req_type == "target_debuff":
                dur = STATUS_CONFIGS[req_val]["duration"]
                p2_debuffs[req_val] = dur if dur > 0 else 6
            elif req_type == "seedling":
                seedling_active = True

    elif cond_req != "None" or spell_info.get("n", 0) > 0:
        # Single-Condition Spells
        # Extract required condition
        cond_text = cond_req.lower()

        if stage == 1:
            weather = fav_weather.value
            location = fav_location.value
            p1_buffs["Charged"] = 6
            p1_buffs["Quickened"] = 6
            p1_class_mults[s_class.value] = 1.25

            # Find matching status or environment
            applied_cond = False
            for st in STATUS_CONFIGS:
                if st.lower() in cond_text:
                    dur = STATUS_CONFIGS[st]["duration"]
                    p2_debuffs[st] = dur if dur > 0 else 6
                    applied_cond = True
                    break
            for bf in BUFF_CONFIGS:
                if bf.lower() in cond_text:
                    p1_buffs[bf] = BUFF_CONFIGS[bf]["duration"]
                    applied_cond = True
                    break
            for w in Weather:
                if w.value.lower() in cond_text:
                    weather = w.value
                    applied_cond = True
                    break
            for loc in Location:
                if loc.value.lower() in cond_text:
                    location = loc.value
                    applied_cond = True
                    break

            # Add Vulnerable to target if not already present to maximize payoff
            if "Vulnerable" not in p2_debuffs:
                p2_debuffs["Vulnerable"] = 6

        elif stage == 2:
            weather = fav_weather.value
            p1_buffs["Charged"] = 6
            for st in STATUS_CONFIGS:
                if st.lower() in cond_text:
                    dur = STATUS_CONFIGS[st]["duration"]
                    p2_debuffs[st] = dur if dur > 0 else 6
                    break
            for bf in BUFF_CONFIGS:
                if bf.lower() in cond_text:
                    p1_buffs[bf] = BUFF_CONFIGS[bf]["duration"]
                    break
            for w in Weather:
                if w.value.lower() in cond_text:
                    weather = w.value
                    break
            for loc in Location:
                if loc.value.lower() in cond_text:
                    location = loc.value
                    break

        elif stage == 3:
            # 1 condition active
            for st in STATUS_CONFIGS:
                if st.lower() in cond_text:
                    dur = STATUS_CONFIGS[st]["duration"]
                    p2_debuffs[st] = dur if dur > 0 else 6
                    break
            for bf in BUFF_CONFIGS:
                if bf.lower() in cond_text:
                    p1_buffs[bf] = BUFF_CONFIGS[bf]["duration"]
                    break

    else:
        # Direct Damage, Buff/Sustain, Debuff/Control, Setup
        if stage == 1:
            weather = fav_weather.value
            location = fav_location.value
            p2_debuffs["Vulnerable"] = 6
            p1_buffs["Charged"] = 6
            p1_buffs["Quickened"] = 6
            p1_class_mults[s_class.value] = 1.25

        elif stage == 2:
            weather = fav_weather.value
            p2_debuffs["Vulnerable"] = 6
            p1_buffs["Charged"] = 6

        elif stage == 3:
            weather = fav_weather.value

    return {
        "recipe": recipe,
        "class": s_class.value,
        "stage": stage,
        "turn": turn_num,
        "weather": weather,
        "location": location,
        "weather_turns_active": 3 if stage <= 2 else 1,
        "location_turns_active": 3 if stage <= 2 else 1,
        "seedling_active": seedling_active,
        "seedling_rained_on": seedling_rained_on,
        "seedling_sunny_on": seedling_sunny_on,
        "player1": {
            "current_health": 1000.0,
            "max_health": 1000.0,
            "rune_pool": p1_rune_pool,
            "buffs": p1_buffs,
            "debuffs": p1_debuffs,
            "class_multipliers": p1_class_mults,
        },
        "player2": {
            "current_health": 1000.0,
            "max_health": 1000.0,
            "rune_pool": p2_rune_pool,
            "buffs": p2_buffs,
            "debuffs": p2_debuffs,
            "class_multipliers": p2_class_mults,
        },
    }


def generate_curriculum(
    spell_data_path: str = "spell_data.json",
    output_path: str = "curriculum_board_states.json"
) -> List[Dict[str, Any]]:
    """Generates all 500 board states and saves them to json."""
    with open(spell_data_path, "r", encoding="utf-8") as f:
        spell_data = json.load(f)

    stages: List[Dict[str, Any]] = [{}, {}, {}, {}]

    for stage_idx in range(4):
        stage_num = stage_idx + 1
        for recipe, s_info in spell_data.items():
            state = generate_board_state_for_spell(recipe, s_info, stage_num)
            stages[stage_idx][recipe] = state

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(stages, f, indent=2)

    total_states = sum(len(st) for st in stages)
    print(f"Generated {total_states} board states across 4 stages to {output_path}")
    return stages


if __name__ == "__main__":
    generate_curriculum()
