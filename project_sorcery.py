"""
Project Sorcery - 1v1 Simulation & Game Logic Engine
=====================================================
A fully functional, headless 1v1 spell combat engine for Project Sorcery,
designed for training and evaluating Neural Network Genetic AIs.

Grounding & Specifications:
- Based on 'Project Sorcery - Game Design Notes'
- 125 3-rune spell recipes across 15 pure and hybrid classes
- Environmental buffs/nerfs (9 weathers and 6 locations)
- 6 Buffs & 14 Status Effects with accurate durations, stat alters, DoTs, and CCs
- Real-time dynamic loading of formula knobs (b, n) from spell_data.json
- Modular AI interface supporting state vectors, gym-style stepping, and batch duels
"""

import json
import math
import os
import random
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union


# =============================================================================
# 1. CONSTANTS, RUNES, AND ENUMS
# =============================================================================

class Rune(str, Enum):
    FIRE = "F"
    WATER = "W"
    EARTH = "E"
    LIGHT = "L"
    DARK = "D"


# Association between Runes and Base Stats:
# Fire: Potency | Water: Defense | Earth: Health | Dark: Luck | Light: Speed
RUNE_TO_STAT = {
    Rune.FIRE: "potency",
    Rune.WATER: "defense",
    Rune.EARTH: "health",
    Rune.DARK: "luck",
    Rune.LIGHT: "speed",
}

ALL_RUNES = [Rune.FIRE.value, Rune.WATER.value, Rune.EARTH.value, Rune.LIGHT.value, Rune.DARK.value]


class SpellClass(str, Enum):
    # Pure Classes (First 2 runes identical)
    FIRE = "Fire"          # F+F
    WATER = "Water"        # W+W
    EARTH = "Earth"        # E+E
    LIGHT = "Light"        # L+L
    DARK = "Dark"          # D+D
    
    # Hybrid Classes (First 2 runes combination)
    GHOSTFIRE = "Ghostfire" # F+W, W+F
    BEASTS = "Beasts"       # F+E, E+F
    LIGHTNING = "Lightning" # F+L, L+F
    BLOOD = "Blood"         # F+D, D+F
    PLANTS = "Plants"       # W+E, E+W
    FEY = "Fey"             # W+L, L+W
    ICE = "Ice"             # W+D, D+W
    WIND = "Wind"           # E+L, L+E
    POISON = "Poison"       # E+D, D+E
    COSMIC = "Cosmic"       # L+D, D+L


# Mapping from 2-rune prefix to SpellClass
PREFIX_TO_CLASS: Dict[str, SpellClass] = {
    "FF": SpellClass.FIRE,
    "WW": SpellClass.WATER,
    "EE": SpellClass.EARTH,
    "LL": SpellClass.LIGHT,
    "DD": SpellClass.DARK,
    "FW": SpellClass.GHOSTFIRE,
    "WF": SpellClass.GHOSTFIRE,
    "FE": SpellClass.BEASTS,
    "EF": SpellClass.BEASTS,
    "FL": SpellClass.LIGHTNING,
    "LF": SpellClass.LIGHTNING,
    "FD": SpellClass.BLOOD,
    "DF": SpellClass.BLOOD,
    "WE": SpellClass.PLANTS,
    "EW": SpellClass.PLANTS,
    "WL": SpellClass.FEY,
    "LW": SpellClass.FEY,
    "WD": SpellClass.ICE,
    "DW": SpellClass.ICE,
    "EL": SpellClass.WIND,
    "LE": SpellClass.WIND,
    "ED": SpellClass.POISON,
    "DE": SpellClass.POISON,
    "LD": SpellClass.COSMIC,
    "DL": SpellClass.COSMIC,
}


def get_spell_class(recipe: str) -> SpellClass:
    """Determine the spell's class from the first two runes of its recipe."""
    prefix = recipe[:2].upper()
    if prefix in PREFIX_TO_CLASS:
        return PREFIX_TO_CLASS[prefix]
    raise ValueError(f"Invalid recipe prefix '{prefix}'. Must be composed of F, W, E, L, D.")


# Buff Definitions
# Name, Associated Stat/Element, Base Magnitude (%), Duration (Turns)
BUFF_CONFIGS = {
    "Charged": {"stat": "potency", "magnitude": 0.25, "duration": 3, "desc": "Increases Potency by 25% for 3 rounds."},
    "Honed": {"stat": "luck", "magnitude": 0.25, "duration": 3, "desc": "Increases Luck by 25% for 3 rounds."},
    "Shielded": {"stat": "defense", "magnitude": 0.25, "duration": 3, "desc": "Increases Defense by 25% and grants immunity to negative status effects."},
    "Quickened": {"stat": "speed", "magnitude": 0.30, "duration": 3, "desc": "Increases Speed by 30% for 3 rounds."},
    "Invisible": {"stat": "invulnerable", "magnitude": 0.50, "duration": 1, "desc": "Invulnerable to direct damage & increases Potency by 50% for 1 round."},
    "Blessed": {"stat": "all", "magnitude": 0.20, "duration": 5, "desc": "Increases all stats by 20% and heals 5% max health each turn for 5 rounds."},
}

# Negative Status Effect (Debuff) Definitions
STATUS_CONFIGS = {
    "Burning": {"category": "DoT", "magnitude": 0.05, "duration": 3, "desc": "Deals 5% of target's Current Health each turn."},
    "Poisoned": {"category": "Escalating DoT", "magnitude": 0.03, "duration": -1, "desc": "Deals 3% of target's Maximum Health, increasing by +2% each turn active (Until cleansed)."},
    "Cursed": {"category": "Stat Debuff", "magnitude": 0.15, "duration": 3, "desc": "Decreases all stats by 15% for 3 rounds."},
    "Slowed": {"category": "Stat Debuff", "magnitude": 0.25, "duration": 3, "desc": "Decreases Speed by 25% for 3 rounds."},
    "Vulnerable": {"category": "Stat Debuff", "magnitude": 0.25, "duration": 3, "desc": "Decreases Defense by 25% for 3 rounds (amplifies incoming damage)."},
    "Weakened": {"category": "Stat Debuff", "magnitude": 0.25, "duration": 3, "desc": "Decreases Potency by 25% for 3 rounds."},
    "Blinded": {"category": "Stat Debuff", "magnitude": 0.25, "duration": 3, "desc": "Decreases Luck by 25% for 3 rounds."},
    "Bleeding": {"category": "DoT", "magnitude": 0.06, "duration": 3, "desc": "Deals 6% of target's Maximum Health each turn."},
    "Entangled": {"category": "Crowd Control", "magnitude": 0.30, "duration": 3, "desc": "Decreases Speed by 30% and prevents turn priority."},
    "Frosty": {"category": "Dual Debuff", "magnitude": 0.15, "duration": 3, "desc": "Decreases Speed and Potency each by 15%."},
    "Stunned": {"category": "Hard CC", "magnitude": 0.25, "duration": 1, "desc": "Skips turn; incoming damage increased by 25%."},
    "Asleep": {"category": "Hard CC", "magnitude": 0.30, "duration": 1, "desc": "Skips turn; decreases Defense by 30%; breaks upon taking damage."},
    "Polymorphed": {"category": "Hard CC", "magnitude": 0.25, "duration": 1, "desc": "Skips turn; removes all active buffs and status effects; incoming damage increased by 25%."},
    "Infected": {"category": "Severe DoT", "magnitude": 0.05, "duration": -1, "desc": "Overrides Poisoned; deals 5% of target's Maximum Health, increasing by +3% each turn, halts all stat growth."},
}


class Weather(str, Enum):
    CLEAR = "Clear"
    STORMING = "Storming"
    SNOWING = "Snowing"
    BLOOD_RAIN = "Blood Rain"
    WINDY = "Windy"
    SUNNY = "Sunny"
    DARKNESS = "Darkness"
    SANDSTORM = "Sandstorm"
    RAINING = "Raining"
    BLIZZARD = "Blizzard"


class Location(str, Enum):
    NONE = "None"
    JUNGLE = "Jungle"
    GRAVEYARD = "Graveyard"
    ENCHANTED_FOREST = "Enchanted Forest"
    TUNDRA = "Tundra"
    SWAMP = "Swamp"
    SPACE = "Space"


# Weather buffs and nerfs mapping
WEATHER_AFFINITIES: Dict[Weather, Dict[str, List[SpellClass]]] = {
    Weather.CLEAR: {"buffed": [], "nerfed": []},
    Weather.STORMING: {
        "buffed": [SpellClass.LIGHTNING, SpellClass.WATER],
        "nerfed": [SpellClass.BEASTS, SpellClass.LIGHT],
    },
    Weather.SNOWING: {
        "buffed": [SpellClass.ICE],
        "nerfed": [SpellClass.FIRE, SpellClass.PLANTS],
    },
    Weather.BLOOD_RAIN: {
        "buffed": [SpellClass.BLOOD, SpellClass.GHOSTFIRE],
        "nerfed": [SpellClass.FEY],
    },
    Weather.WINDY: {
        "buffed": [SpellClass.WIND],
        "nerfed": [SpellClass.EARTH],
    },
    Weather.SUNNY: {
        "buffed": [SpellClass.FIRE, SpellClass.LIGHT, SpellClass.PLANTS],
        "nerfed": [SpellClass.DARK, SpellClass.ICE],
    },
    Weather.DARKNESS: {
        "buffed": [SpellClass.DARK, SpellClass.FEY],
        "nerfed": [SpellClass.LIGHT],
    },
    Weather.SANDSTORM: {
        "buffed": [SpellClass.EARTH, SpellClass.WIND],
        "nerfed": [SpellClass.BEASTS],
    },
    Weather.RAINING: {
        "buffed": [SpellClass.WATER, SpellClass.PLANTS],
        "nerfed": [SpellClass.EARTH, SpellClass.FIRE],
    },
    Weather.BLIZZARD: {
        "buffed": [SpellClass.ICE],
        "nerfed": [SpellClass.FIRE, SpellClass.PLANTS],
    },
}

# Location buffs mapping
LOCATION_AFFINITIES: Dict[Location, List[SpellClass]] = {
    Location.NONE: [],
    Location.JUNGLE: [SpellClass.BEASTS, SpellClass.PLANTS],
    Location.GRAVEYARD: [SpellClass.GHOSTFIRE, SpellClass.DARK],
    Location.ENCHANTED_FOREST: [SpellClass.FEY],
    Location.TUNDRA: [SpellClass.ICE],
    Location.SWAMP: [SpellClass.POISON],
    Location.SPACE: [SpellClass.COSMIC],
}


# =============================================================================
# 2. REAL-TIME SPELL KNOBS LOADER (Reads b and n in real time)
# =============================================================================

@dataclass
class SpellKnob:
    recipe: str
    spell_class: str
    category: str
    b: float
    n: float
    condition_required: str
    description: str
    max_potential: float = 0.0


class SpellKnobsRegistry:
    """
    Manages loading and real-time retrieval of spell formula knobs (b, n)
    from a separate JSON file. Automatically reloads if the file has been modified on disk.
    """
    def __init__(self, json_path: str = "spell_data.json"):
        self.json_path = json_path
        self._last_mtime: float = 0.0
        self._knobs: Dict[str, SpellKnob] = {}
        self.load(force=True)

    def load(self, force: bool = False) -> None:
        """Reads the JSON file from disk if modified or forced."""
        if not os.path.exists(self.json_path):
            raise FileNotFoundError(f"Spell data JSON file not found at: {self.json_path}")
        
        current_mtime = os.path.getmtime(self.json_path)
        if force or current_mtime > self._last_mtime:
            with open(self.json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            new_knobs = {}
            for recipe, info in data.items():
                new_knobs[recipe.upper()] = SpellKnob(
                    recipe=recipe.upper(),
                    spell_class=info.get("class", ""),
                    category=info.get("category", ""),
                    b=float(info.get("b", 0.0)),
                    n=float(info.get("n", 0.0)),
                    condition_required=info.get("condition_required", "None"),
                    description=info.get("description", ""),
                    max_potential=float(info.get("max_potential", 0.0)),
                )
            self._knobs = new_knobs
            self._last_mtime = current_mtime

    def get(self, recipe: str) -> SpellKnob:
        """Fetch current knob values in real-time."""
        self.load(force=False)  # Hot-reload if file updated
        recipe_upper = recipe.upper()
        if recipe_upper not in self._knobs:
            raise KeyError(f"Recipe '{recipe_upper}' not found in spell knobs registry.")
        return self._knobs[recipe_upper]

    def all_recipes(self) -> List[str]:
        self.load(force=False)
        return sorted(list(self._knobs.keys()))


# Global default registry instance
GLOBAL_REGISTRY: Optional[SpellKnobsRegistry] = None

def get_registry(json_path: str = "spell_data.json") -> SpellKnobsRegistry:
    global GLOBAL_REGISTRY
    if GLOBAL_REGISTRY is None or GLOBAL_REGISTRY.json_path != json_path:
        GLOBAL_REGISTRY = SpellKnobsRegistry(json_path)
    return GLOBAL_REGISTRY


# =============================================================================
# 3. WIZARD / COMBATANT STATE
# =============================================================================

@dataclass
class Wizard:
    """
    Represents an AI-controlled wizard in a 1v1 duel.
    Tracks starting HP, current HP, base stats, match-long alterations,
    active buffs, active debuffs, and combat history.
    """
    name: str = "Wizard"
    starting_hp: float = 1000.0
    base_potency: float = 100.0
    base_defense: float = 100.0
    base_luck: float = 50.0
    base_speed: float = 100.0

    # Dynamic match state
    max_health: float = 1000.0
    current_health: float = 1000.0
    match_stat_mods: Dict[str, float] = field(default_factory=lambda: {
        "potency": 0.0,
        "defense": 0.0,
        "luck": 0.0,
        "speed": 0.0,
        "health": 0.0,
    })

    # Active buffs: name -> turns remaining
    buffs: Dict[str, int] = field(default_factory=dict)
    # Active debuffs: name -> turns remaining (-1 = permanent until cleansed)
    debuffs: Dict[str, int] = field(default_factory=dict)

    # Escalating DoT tracking
    poison_turns_active: int = 0
    infected_turns_active: int = 0

    # Turn priority flag (from FLL)
    has_next_turn_priority: bool = False
    # Retaliation flag (WDW: while active, when damaged, applies Frosty to attacker)
    wdw_retaliation_active: bool = False

    # Rune pool (for spells that grant runes to pool)
    rune_pool: List[str] = field(default_factory=list)

    # Analytics / Fitness metrics for Genetic AI
    damage_dealt: float = 0.0
    damage_taken: float = 0.0
    healing_done: float = 0.0
    turns_survived: int = 0

    def __post_init__(self):
        self.max_health = float(self.starting_hp)
        self.current_health = float(self.starting_hp)

    def reset(self):
        """Reset match-specific variables to original starting values."""
        self.max_health = float(self.starting_hp)
        self.current_health = float(self.starting_hp)
        self.match_stat_mods = {"potency": 0.0, "defense": 0.0, "luck": 0.0, "speed": 0.0, "health": 0.0}
        self.buffs.clear()
        self.debuffs.clear()
        self.poison_turns_active = 0
        self.infected_turns_active = 0
        self.has_next_turn_priority = False
        self.wdw_retaliation_active = False
        self.rune_pool.clear()
        self.damage_dealt = 0.0
        self.damage_taken = 0.0
        self.healing_done = 0.0
        self.turns_survived = 0

    @property
    def is_alive(self) -> bool:
        return self.current_health > 0.0

    # -------------------------------------------------------------------------
    # Stat Calculation with Buffs and Debuffs
    # -------------------------------------------------------------------------
    def get_effective_stat(self, stat_name: str) -> float:
        """
        Calculates effective stat:
        1. Base stat + match-duration flat modifications.
        2. Applies percentage multipliers from active buffs and status effects.
        """
        stat_name = stat_name.lower()
        if stat_name == "potency":
            raw = self.base_potency + self.match_stat_mods["potency"]
        elif stat_name == "defense":
            raw = self.base_defense + self.match_stat_mods["defense"]
        elif stat_name == "luck":
            raw = self.base_luck + self.match_stat_mods["luck"]
        elif stat_name == "speed":
            raw = self.base_speed + self.match_stat_mods["speed"]
        elif stat_name == "health":
            return self.max_health
        else:
            raise ValueError(f"Unknown stat name: {stat_name}")

        multiplier = 1.0

        # Buff contributions
        if "Blessed" in self.buffs:
            multiplier += BUFF_CONFIGS["Blessed"]["magnitude"]  # +20% all stats

        if stat_name == "potency":
            if "Charged" in self.buffs:
                multiplier += BUFF_CONFIGS["Charged"]["magnitude"]  # +25%
            if "Invisible" in self.buffs:
                multiplier += BUFF_CONFIGS["Invisible"]["magnitude"]  # +50%
            if "Weakened" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Weakened"]["magnitude"]  # -25%
            if "Frosty" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Frosty"]["magnitude"]  # -15%
            if "Cursed" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Cursed"]["magnitude"]  # -15%

        elif stat_name == "defense":
            if "Shielded" in self.buffs:
                multiplier += BUFF_CONFIGS["Shielded"]["magnitude"]  # +25%
            if "Vulnerable" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Vulnerable"]["magnitude"]  # -25%
            if "Asleep" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Asleep"]["magnitude"]  # -30%
            if "Cursed" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Cursed"]["magnitude"]  # -15%

        elif stat_name == "speed":
            if "Quickened" in self.buffs:
                multiplier += BUFF_CONFIGS["Quickened"]["magnitude"]  # +30%
            if "Slowed" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Slowed"]["magnitude"]  # -25%
            if "Entangled" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Entangled"]["magnitude"]  # -30%
            if "Frosty" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Frosty"]["magnitude"]  # -15%
            if "Cursed" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Cursed"]["magnitude"]  # -15%

        elif stat_name == "luck":
            if "Honed" in self.buffs:
                multiplier += BUFF_CONFIGS["Honed"]["magnitude"]  # +25%
            if "Blinded" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Blinded"]["magnitude"]  # -25%
            if "Cursed" in self.debuffs:
                multiplier -= STATUS_CONFIGS["Cursed"]["magnitude"]  # -15%

        # Floor stat at 1.0 to prevent division by zero or negative effective stats
        effective = max(1.0, raw * max(0.05, multiplier))
        return effective

    # -------------------------------------------------------------------------
    # Buff & Debuff Application and Cleansing
    # -------------------------------------------------------------------------
    def apply_buff(self, buff_name: str, duration: Optional[int] = None) -> bool:
        """Applies or refreshes a positive buff."""
        if buff_name not in BUFF_CONFIGS:
            return False
        dur = duration if duration is not None else BUFF_CONFIGS[buff_name]["duration"]
        self.buffs[buff_name] = dur
        return True

    def remove_buff(self, buff_name: str) -> bool:
        if buff_name in self.buffs:
            del self.buffs[buff_name]
            if buff_name == "Shielded":
                self.wdw_retaliation_active = False
            return True
        return False

    def remove_all_buffs(self) -> int:
        count = len(self.buffs)
        self.buffs.clear()
        self.wdw_retaliation_active = False
        return count

    def apply_debuff(self, debuff_name: str, duration: Optional[int] = None) -> bool:
        """
        Applies a negative status effect to the wizard.
        Respects Shielded immunity: 'Shielded grants immunity to negative status effects'.
        """
        if "Shielded" in self.buffs:
            # Target is immune to negative status effects
            return False

        if debuff_name not in STATUS_CONFIGS:
            return False

        # Polymorphed removes all active buffs and status effects first
        if debuff_name == "Polymorphed":
            self.remove_all_buffs()
            self.debuffs.clear()

        # Infected overrides Poisoned
        if debuff_name == "Infected":
            if "Poisoned" in self.debuffs:
                del self.debuffs["Poisoned"]
            self.infected_turns_active = 0

        if debuff_name == "Poisoned" and "Infected" in self.debuffs:
            # Cannot apply Poisoned if already Infected
            return False

        dur = duration if duration is not None else STATUS_CONFIGS[debuff_name]["duration"]
        self.debuffs[debuff_name] = dur
        if debuff_name == "Poisoned" and self.poison_turns_active == 0:
            self.poison_turns_active = 0
        return True

    def remove_debuff(self, debuff_name: str) -> bool:
        if debuff_name in self.debuffs:
            del self.debuffs[debuff_name]
            if debuff_name == "Poisoned":
                self.poison_turns_active = 0
            if debuff_name == "Infected":
                self.infected_turns_active = 0
            return True
        return False

    def cleanse_all_debuffs(self) -> int:
        """Cleanses all negative status effects from the wizard."""
        count = len(self.debuffs)
        self.debuffs.clear()
        self.poison_turns_active = 0
        self.infected_turns_active = 0
        return count

    def reset_debuff_durations(self) -> None:
        """LEW mechanic: re-applies any debuff on the target, effectively resetting its duration."""
        for debuff_name in list(self.debuffs.keys()):
            default_dur = STATUS_CONFIGS[debuff_name]["duration"]
            self.debuffs[debuff_name] = default_dur

    def alter_stat(self, stat_name: str, amount: float) -> None:
        """
        Permanently modifies a base stat for the remainder of the match.
        If 'Infected' is active, halts all stat growth (only decreases permitted).
        """
        stat_name = stat_name.lower()
        if "Infected" in self.debuffs and amount > 0:
            # Halts all stat growth
            return

        if stat_name in self.match_stat_mods:
            self.match_stat_mods[stat_name] += amount
        elif stat_name == "health":
            self.max_health = max(1.0, self.max_health + amount)
            self.current_health = min(self.max_health, self.current_health + amount)

    # -------------------------------------------------------------------------
    # Direct Damage, Healing, and Hard CC Action Checks
    # -------------------------------------------------------------------------
    def take_damage(self, amount: float, is_direct: bool = True, attacker: Optional["Wizard"] = None) -> float:
        """
        Inflicts damage on this wizard.
        - If Invisible and damage is direct: damage is 0.
        - If Stunned: incoming damage is increased by 25%.
        - If Polymorphed: incoming damage is increased by 25%.
        - If Asleep: waking occurs upon taking damage (Asleep breaks).
        - If wdw_retaliation_active: attacker is afflicted with Frosty.
        """
        if amount <= 0.0 or not self.is_alive:
            return 0.0

        if is_direct and "Invisible" in self.buffs:
            return 0.0

        actual_damage = amount

        # Damage amplification from Hard CCs
        if "Stunned" in self.debuffs:
            actual_damage *= 1.25
        if "Polymorphed" in self.debuffs:
            actual_damage *= 1.25

        # Asleep breaks upon taking damage
        if "Asleep" in self.debuffs:
            self.remove_debuff("Asleep")

        # Shielded retaliatory effect (WDW): while active, applies Frosty to attacker on hit
        if self.wdw_retaliation_active and attacker is not None and attacker is not self:
            attacker.apply_debuff("Frosty")

        self.current_health = max(0.0, self.current_health - actual_damage)
        self.damage_taken += actual_damage
        if attacker is not None:
            attacker.damage_dealt += actual_damage

        return actual_damage

    def heal(self, amount: float) -> float:
        """Heals the wizard up to max_health."""
        if amount <= 0.0 or not self.is_alive:
            return 0.0
        old_hp = self.current_health
        self.current_health = min(self.max_health, self.current_health + amount)
        actual_heal = self.current_health - old_hp
        self.healing_done += actual_heal
        return actual_heal

    def can_act(self) -> Tuple[bool, str]:
        """
        Checks if the wizard can cast a spell this turn.
        Returns (can_act: bool, reason: str).
        Hard CCs (Stunned, Asleep, Polymorphed) cause the wizard to skip turn.
        """
        if not self.is_alive:
            return False, "Defeated"
        if "Stunned" in self.debuffs:
            return False, "Stunned"
        if "Asleep" in self.debuffs:
            return False, "Asleep"
        if "Polymorphed" in self.debuffs:
            return False, "Polymorphed"
        return True, "Ready"


# =============================================================================
# 4. ENVIRONMENT & BATTLEFIELD STATE
# =============================================================================

@dataclass
class Environment:
    """
    Tracks the active Weather, active Location, and their summoned potencies.
    Also tracks the battlefield Seedling state (planted, rained on, sunny).
    """
    weather: Weather = Weather.CLEAR
    weather_potency: float = 0.20  # Default 20% modifier
    location: Location = Location.NONE
    location_potency: float = 0.20  # Default 20% modifier

    # Seedling mechanics (Plant spells: EWE, EWL, WED)
    seedling_active: bool = False
    seedling_rained_on: bool = False
    seedling_sunny_on: bool = False
    seedling_turns_alive: int = 0

    def set_weather(self, weather: Weather, potency_b: Optional[float] = None) -> None:
        """Sets weather. Spells use Base Factor (b) to set environment potency."""
        self.weather = weather
        if potency_b is not None:
            self.weather_potency = float(potency_b) / 100.0 if potency_b > 1.0 else float(potency_b)

    def set_location(self, location: Location, potency_b: Optional[float] = None) -> None:
        """Sets location/terrain. Spells use Base Factor (b) to set environment potency."""
        self.location = location
        if potency_b is not None:
            self.location_potency = float(potency_b) / 100.0 if potency_b > 1.0 else float(potency_b)

    def plant_seedling(self) -> None:
        self.seedling_active = True
        self.seedling_rained_on = (self.weather == Weather.RAINING)
        self.seedling_sunny_on = (self.weather == Weather.SUNNY)
        self.seedling_turns_alive = 0

    def consume_seedling(self) -> bool:
        if self.seedling_active:
            self.seedling_active = False
            self.seedling_rained_on = False
            self.seedling_sunny_on = False
            self.seedling_turns_alive = 0
            return True
        return False

    def update_seedling(self) -> None:
        if self.seedling_active:
            self.seedling_turns_alive += 1
            if self.weather == Weather.RAINING:
                self.seedling_rained_on = True
            if self.weather == Weather.SUNNY:
                self.seedling_sunny_on = True

    def get_class_multiplier(self, spell_class: SpellClass) -> float:
        """
        Calculates the combined environmental damage/healing multiplier for a spell class.
        Math: (1.0 + weather_mod + location_mod)
        """
        mod = 0.0
        # Weather buff / nerf
        weather_aff = WEATHER_AFFINITIES.get(self.weather, {"buffed": [], "nerfed": []})
        if spell_class in weather_aff["buffed"]:
            mod += self.weather_potency
        elif spell_class in weather_aff["nerfed"]:
            mod -= self.weather_potency

        # Location buff
        loc_buffed = LOCATION_AFFINITIES.get(self.location, [])
        if spell_class in loc_buffed:
            mod += self.location_potency

        return max(0.1, 1.0 + mod)


# =============================================================================
# 5. DAMAGE & COMBAT CALCULATION MATH
# =============================================================================

class CombatMath:
    """
    Houses all deterministic math formulas for Project Sorcery:
    - Base Spell Scaling
    - Environmental Multipliers
    - Potency Scaling
    - Defense Mitigation
    - Luck Scaling
    """
    @staticmethod
    def calculate_damage(
        caster: Wizard,
        target: Wizard,
        raw_damage: float,
        spell_class: SpellClass,
        env: Environment,
        is_direct: bool = True
    ) -> float:
        """
        Calculates net damage after all multipliers:
        Net Damage = raw_damage * Environment_Multiplier * Potency_Factor * Defense_Factor
        """
        if raw_damage <= 0.0:
            return 0.0

        # 1. Environment Multiplier (Weather & Location)
        env_mult = env.get_class_multiplier(spell_class)

        # 2. Caster Potency Factor (100 base = 1.0x)
        eff_potency = caster.get_effective_stat("potency")
        potency_factor = max(0.05, eff_potency / 100.0)

        # 3. Target Defense Factor (Standard RPG hyperbolic curve: 100 / (100 + Defense))
        eff_defense = target.get_effective_stat("defense")
        defense_factor = 100.0 / (100.0 + max(0.0, eff_defense))

        total_damage = raw_damage * env_mult * potency_factor * defense_factor
        return total_damage

    @staticmethod
    def check_luck_chance(caster: Wizard, base_chance: float = 0.50) -> bool:
        """
        Calculates chance-based rolls scaling with Luck.
        Base chance (50% at 50 Luck). Scales linearly: chance = min(1.0, base_chance * (Luck / 50.0)).
        """
        eff_luck = caster.get_effective_stat("luck")
        scaling = eff_luck / 50.0
        prob = min(1.0, max(0.0, base_chance * scaling))
        return random.random() < prob


# =============================================================================
# 6. ALL 125 SPELL MECHANICS RESOLVER
# =============================================================================

class SpellResolver:
    """
    Implements the complete mechanical specification for every one of the 125 spells,
    evaluating conditional payoffs, status effects, and environmental summons using real-time b & n knobs.
    """
    def __init__(self, registry: SpellKnobsRegistry):
        self.registry = registry

    def resolve(
        self,
        recipe: str,
        caster: Wizard,
        target: Wizard,
        env: Environment
    ) -> Dict[str, Any]:
        """
        Resolves a spell cast by `caster` against `target` in environment `env`.
        Returns an execution log dictionary.
        """
        knob = self.registry.get(recipe)
        b = knob.b
        n = knob.n
        spell_class = get_spell_class(recipe)

        log = {
            "recipe": recipe,
            "class": spell_class.value,
            "caster": caster.name,
            "target": target.name,
            "damage_dealt": 0.0,
            "healing_done": 0.0,
            "effects_applied": [],
            "ultimate_triggered": False,
            "notes": ""
        }

        # Helper method for dealing damage through the combat math engine
        def deal_damage(amount: float, is_direct: bool = True) -> float:
            calc = CombatMath.calculate_damage(caster, target, amount, spell_class, env, is_direct)
            dmg = target.take_damage(calc, is_direct=is_direct, attacker=caster)
            log["damage_dealt"] += dmg
            return dmg

        # Helper method for self-damage
        def deal_self_damage(amount: float) -> float:
            calc = CombatMath.calculate_damage(caster, caster, amount, spell_class, env, is_direct=False)
            dmg = caster.take_damage(calc, is_direct=False, attacker=caster)
            log["notes"] += f"Self-damage: {dmg:.1f}. "
            return dmg

        # Helper method for healing
        def do_heal(target_wiz: Wizard, amount: float) -> float:
            # Healing also scales with environment and potency
            env_mult = env.get_class_multiplier(spell_class)
            eff_pot = caster.get_effective_stat("potency") / 100.0
            h = target_wiz.heal(amount * env_mult * eff_pot)
            log["healing_done"] += h
            return h

        # ---------------------------------------------------------------------
        # CLASS: FIRE (FFF, FFW, FFE, FFL, FFD)
        # ---------------------------------------------------------------------
        if recipe == "FFF":
            deal_damage(1.0 * b)

        elif recipe == "FFW":
            deal_damage(1.0 * b)
            caster.apply_debuff("Burning")
            target.apply_debuff("Burning")
            log["effects_applied"].extend(["Burning on caster", "Burning on target"])

        elif recipe == "FFE":
            deal_damage(1.0 * b)
            target.alter_stat("defense", -(1.0 * b))
            log["effects_applied"].append(f"Target Defense -{b:.1f}")

        elif recipe == "FFL":
            deal_damage(1.0 * b)
            target.apply_debuff("Burning")
            log["effects_applied"].append("Burning on target")

        elif recipe == "FFD":
            dmg_amount = 1.0 * b
            if "Burning" in target.debuffs:
                dmg_amount += 2.0 * b
                log["notes"] += "Target Burning (+2b bonus). "
            if "Vulnerable" in target.debuffs:
                dmg_amount += 2.0 * b
                log["notes"] += "Target Vulnerable (+2b bonus). "
            deal_damage(dmg_amount)

        # ---------------------------------------------------------------------
        # CLASS: WATER (WWF, WWW, WWE, WWL, WWD)
        # ---------------------------------------------------------------------
        elif recipe == "WWF":
            deal_damage(1.0 * b)
            target.alter_stat("potency", -(1.0 * b))
            log["effects_applied"].append(f"Target Potency -{b:.1f}")
            if "Charged" in target.buffs or "Burning" in target.debuffs:
                target.alter_stat("potency", -(2.0 * b))
                target.remove_buff("Charged")
                target.remove_debuff("Burning")
                log["effects_applied"].append(f"Target Charged/Burning consumed, Potency -{2*b:.1f}")

        elif recipe == "WWW":
            caster.cleanse_all_debuffs()
            caster.rune_pool.append("W")
            log["effects_applied"].append("Cleansed all status effects, +1 Water rune to pool")

        elif recipe == "WWE":
            env.set_weather(Weather.RAINING, b)
            log["effects_applied"].append(f"Weather changed to Raining (potency {b}%)")

        elif recipe == "WWL":
            deal_damage(1.0 * b)
            caster_buffs_removed = target.remove_all_buffs()
            log["effects_applied"].append(f"Removed {caster_buffs_removed} buffs from target")

        elif recipe == "WWD":
            debuffs_affected = []
            if "Weakened" in target.debuffs:
                target.alter_stat("potency", -(2.0 * b))
                debuffs_affected.append("Potency")
            if "Vulnerable" in target.debuffs:
                target.alter_stat("defense", -(2.0 * b))
                debuffs_affected.append("Defense")
            if "Slowed" in target.debuffs:
                target.alter_stat("speed", -(2.0 * b))
                debuffs_affected.append("Speed")
            if "Blinded" in target.debuffs:
                target.alter_stat("luck", -(2.0 * b))
                debuffs_affected.append("Luck")
            if not debuffs_affected:
                stat_choice = random.choice(["potency", "defense", "speed", "luck"])
                target.alter_stat(stat_choice, -(1.0 * b))
                log["effects_applied"].append(f"Decreased random stat {stat_choice} by {b:.1f}")
            else:
                log["effects_applied"].append(f"Decreased {', '.join(debuffs_affected)} by {2*b:.1f}")

        # ---------------------------------------------------------------------
        # CLASS: EARTH (EEF, EEW, EEE, EEL, EED)
        # ---------------------------------------------------------------------
        elif recipe == "EEF":
            bonus = 2.0 * b if "Frosty" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)
            if "Frosty" in target.debuffs:
                target.apply_debuff("Stunned")
                log["effects_applied"].append("Target Stunned (+2b bonus from Frosty)")

        elif recipe == "EEW":
            caster.apply_buff("Shielded")
            caster.alter_stat("defense", 1.0 * b)
            caster.remove_debuff("Vulnerable")
            log["effects_applied"].append(f"Shielded applied, Defense +{b:.1f}, Cured Vulnerable")

        elif recipe == "EEE":
            bonus_max_hp = (b / 100.0) * target.max_health
            deal_damage(1.0 * b + bonus_max_hp)
            log["notes"] += f"Bonus max HP damage: {bonus_max_hp:.1f}. "

        elif recipe == "EEL":
            # Deals damage scaling with caster's Health ((1*b) * Health)
            scaled_dmg = (1.0 * b) * (caster.current_health / 100.0)
            deal_damage(scaled_dmg)

        elif recipe == "EED":
            # 10 instances of (1*b) damage
            total_hits = 10
            for _ in range(total_hits):
                deal_damage(1.0 * b)

        # ---------------------------------------------------------------------
        # CLASS: LIGHT (LLF, LLW, LLE, LLL, LLD)
        # ---------------------------------------------------------------------
        elif recipe == "LLF":
            random_buff = random.choice(list(BUFF_CONFIGS.keys()))
            caster.apply_buff(random_buff)
            log["effects_applied"].append(f"Random buff: {random_buff}")
            if "Cursed" in caster.debuffs:
                caster.remove_debuff("Cursed")
                caster.apply_buff("Blessed")
                log["effects_applied"].append("Cured Cursed -> Granted Blessed!")

        elif recipe == "LLW":
            deal_damage(1.0 * b)
            target.apply_debuff("Blinded")
            log["effects_applied"].append("Target Blinded")

        elif recipe == "LLE":
            env.set_weather(Weather.SUNNY, b)
            log["effects_applied"].append(f"Weather changed to Sunny (potency {b}%)")

        elif recipe == "LLL":
            do_heal(caster, 1.0 * b)
            for s in ["potency", "defense", "luck", "speed"]:
                caster.alter_stat(s, 1.0 * b)
            log["effects_applied"].append(f"Healed {b:.1f}, All stats +{b:.1f}")

        elif recipe == "LLD":
            # Ultimate: Sunny AND Caster is Blessed
            bonus = 0.0
            if env.weather == Weather.SUNNY and "Blessed" in caster.buffs:
                bonus = n * b
                log["ultimate_triggered"] = True
                log["notes"] += "ULTIMATE TRIGGERED! "
            deal_damage(1.0 * b + bonus)

        # ---------------------------------------------------------------------
        # CLASS: DARK (DDF, DDW, DDE, DDL, DDD)
        # ---------------------------------------------------------------------
        elif recipe == "DDF":
            bonus = 2.0 * b if "Asleep" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "DDW":
            deal_damage(1.0 * b)
            caster.apply_debuff("Weakened")
            log["effects_applied"].append("Caster Weakened")

        elif recipe == "DDE":
            env.set_weather(Weather.DARKNESS, b)
            log["effects_applied"].append(f"Weather changed to Darkness (potency {b}%)")

        elif recipe == "DDL":
            deal_damage(1.0 * b)
            target.apply_debuff("Weakened")
            log["effects_applied"].append("Target Weakened")

        elif recipe == "DDD":
            deal_damage(1.0 * b)
            for s in ["potency", "defense", "luck", "speed"]:
                target.alter_stat(s, -(1.0 * b))
            log["effects_applied"].append(f"Decreased all target stats by {b:.1f}")

        # ---------------------------------------------------------------------
        # CLASS: GHOSTFIRE (FWF, FWW, FWE, FWL, FWD, WFF, WFW, WFE, WFL, WFD)
        # ---------------------------------------------------------------------
        elif recipe == "FWF":
            deal_damage(1.0 * b)
            if CombatMath.check_luck_chance(caster):
                target.apply_debuff("Burning")
                log["effects_applied"].append("Burning applied (Luck roll)")

        elif recipe == "FWW":
            deal_damage(1.0 * b)
            target.apply_debuff("Cursed")
            log["effects_applied"].append("Target Cursed")

        elif recipe == "FWE":
            env.set_location(Location.GRAVEYARD, b)
            log["effects_applied"].append(f"Location changed to Graveyard (potency {b}%)")

        elif recipe == "FWL":
            deal_damage(1.0 * b)
            caster.apply_debuff("Cursed")
            log["effects_applied"].append("Caster Cursed")

        elif recipe == "FWD":
            # Ultimate: Target Cursed, Weather Blood Rain, Location Graveyard
            bonus = 0.0
            if "Cursed" in target.debuffs and env.weather == Weather.BLOOD_RAIN and env.location == Location.GRAVEYARD:
                bonus = n * b
                log["ultimate_triggered"] = True
                log["notes"] += "ULTIMATE TRIGGERED! "
            deal_damage(1.0 * b + bonus)

        elif recipe == "WFF":
            bonus = 2.0 * b if "Bleeding" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "WFW":
            deal_damage(1.0 * b)
            target.alter_stat("potency", -(1.0 * b))
            target.alter_stat("luck", -(1.0 * b))
            log["effects_applied"].append(f"Target Potency & Luck -{b:.1f}")

        elif recipe == "WFE":
            deal_damage(1.0 * b)
            if CombatMath.check_luck_chance(caster):
                target.apply_debuff("Bleeding")
                log["effects_applied"].append("Bleeding applied (Luck roll)")

        elif recipe == "WFL":
            caster.apply_buff("Honed")
            caster.alter_stat("luck", 1.0 * b)
            caster.remove_debuff("Blinded")
            log["effects_applied"].append(f"Honed applied, Luck +{b:.1f}, Cured Blinded")

        elif recipe == "WFD":
            bonus = 0.0
            if "Shielded" in caster.buffs:
                caster.remove_buff("Shielded")
                bonus += 2.0 * b * (caster.get_effective_stat("defense") / 100.0)
                log["notes"] += "Consumed Shielded for Defense-scaled bonus. "
            if "Honed" in caster.buffs:
                caster.remove_buff("Honed")
                bonus += 2.0 * b * (caster.get_effective_stat("luck") / 50.0)
                log["notes"] += "Consumed Honed for Luck-scaled bonus. "
            deal_damage(1.0 * b + bonus)

        # ---------------------------------------------------------------------
        # CLASS: BEASTS (FEF, FEW, FEE, FEL, FED, EFF, EFW, EFE, EFL, EFD)
        # ---------------------------------------------------------------------
        elif recipe == "FEF":
            deal_damage(1.0 * b)
            target.apply_debuff("Vulnerable")
            log["effects_applied"].append("Target Vulnerable")

        elif recipe == "FEW":
            bonus = 2.0 * b if "Entangled" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "FEE":
            caster.apply_buff("Charged")
            caster.rune_pool.append("F")
            log["effects_applied"].append("Charged applied, +1 Fire rune")

        elif recipe == "FEL":
            caster.apply_buff("Honed")
            caster.rune_pool.append("W")
            log["effects_applied"].append("Honed applied, +1 Water rune")

        elif recipe == "FED":
            x = len(target.debuffs)
            hits = (x + 1)**2 if x <= 2 else (4 * x if x <= 6 else x + 18)
            for _ in range(hits):
                deal_damage(1.0 * b)
            log["notes"] += f"Hit {hits} times based on {x} debuffs. "

        elif recipe == "EFF":
            target.alter_stat("defense", -(1.0 * b))
            log["effects_applied"].append(f"Target Defense -{b:.1f}")
            if "Vulnerable" in target.debuffs:
                target.remove_debuff("Vulnerable")
                caster.apply_buff("Honed")
                caster.apply_buff("Quickened")
                log["effects_applied"].append("Removed Vulnerable -> Granted Honed & Quickened")

        elif recipe == "EFW":
            caster.apply_buff("Shielded")
            caster.rune_pool.append("E")
            log["effects_applied"].append("Shielded applied, +1 Earth rune")

        elif recipe == "EFE":
            deal_damage(1.0 * b)
            caster.alter_stat("health", 1.0 * b)
            log["effects_applied"].append(f"Caster Max Health +{b:.1f}")

        elif recipe == "EFL":
            do_heal(caster, 1.0 * b)
            target.apply_debuff("Poisoned")
            log["effects_applied"].append("Healed caster, Target Poisoned")

        elif recipe == "EFD":
            # Ultimate: Target Entangled AND Location Jungle
            bonus = 0.0
            if "Entangled" in target.debuffs and env.location == Location.JUNGLE:
                bonus = n * b
                log["ultimate_triggered"] = True
                log["notes"] += "ULTIMATE TRIGGERED! "
            deal_damage(1.0 * b + bonus)

        # ---------------------------------------------------------------------
        # CLASS: LIGHTNING (FLF, FLW, FLE, FLL, FLD, LFF, LFW, LFE, LFL, LFD)
        # ---------------------------------------------------------------------
        elif recipe == "FLF":
            bonus = 2.0 * b if "Stunned" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "FLW":
            deal_damage(1.0 * b)
            if CombatMath.check_luck_chance(caster):
                target.apply_debuff("Stunned")
                log["effects_applied"].append("Stunned applied (Luck roll)")

        elif recipe == "FLE":
            env.set_weather(Weather.STORMING, b)
            log["effects_applied"].append(f"Weather changed to Storming (potency {b}%)")

        elif recipe == "FLL":
            caster.apply_buff("Quickened")
            caster.has_next_turn_priority = True
            log["effects_applied"].append("Quickened applied, Turn Priority on next turn")

        elif recipe == "FLD":
            # Ultimate: Target Stunned, Caster Charged, Weather Storming
            bonus = 0.0
            if "Stunned" in target.debuffs and "Charged" in caster.buffs and env.weather == Weather.STORMING:
                bonus = n * b
                log["ultimate_triggered"] = True
                log["notes"] += "ULTIMATE TRIGGERED! "
            deal_damage(1.0 * b + bonus)

        elif recipe == "LFF":
            bonus = 2.0 * b if "Vulnerable" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "LFW":
            caster.apply_buff("Charged")
            caster.alter_stat("potency", 1.0 * b)
            caster.remove_debuff("Weakened")
            log["effects_applied"].append(f"Charged applied, Potency +{b:.1f}, Cured Weakened")

        elif recipe == "LFE":
            deal_damage(1.0 * b)
            target.apply_debuff("Stunned")
            log["effects_applied"].append("Target Stunned")
            if env.weather == Weather.STORMING:
                caster.apply_debuff("Stunned")
                log["effects_applied"].append("Caster Stunned (Storming effect)")

        elif recipe == "LFL":
            deal_damage(1.0 * b)
            if env.weather == Weather.DARKNESS:
                target.apply_debuff("Blinded")
                log["effects_applied"].append("Target Blinded (Darkness effect)")

        elif recipe == "LFD":
            dmg = 3.0 * b if "Charged" in caster.buffs else 1.0 * b
            deal_damage(dmg)
            caster.apply_debuff("Stunned")
            log["effects_applied"].append("Caster Stunned")

        # ---------------------------------------------------------------------
        # CLASS: BLOOD (FDF, FDW, FDE, FDL, FDD, DFF, DFW, DFE, DFL, DFD)
        # ---------------------------------------------------------------------
        elif recipe == "FDF":
            bonus = 2.0 * b if "Invisible" in caster.buffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "FDW":
            deal_damage(1.0 * b)
            deal_self_damage(1.0 * b)

        elif recipe == "FDE":
            env.set_weather(Weather.BLOOD_RAIN, b)
            log["effects_applied"].append(f"Weather changed to Blood Rain (potency {b}%)")

        elif recipe == "FDL":
            deal_damage(1.0 * b)
            target.apply_debuff("Bleeding")
            log["effects_applied"].append("Target Bleeding")

        elif recipe == "FDD":
            # Ultimate: Target Blinded AND Weather Darkness
            bonus = 0.0
            if "Blinded" in target.debuffs and env.weather == Weather.DARKNESS:
                bonus = n * b
                log["ultimate_triggered"] = True
                log["notes"] += "ULTIMATE TRIGGERED! "
            deal_damage(1.0 * b + bonus)

        elif recipe == "DFF":
            bonus = 0.0
            if "Bleeding" in caster.debuffs:
                bonus += 2.0 * b
            if env.weather == Weather.BLOOD_RAIN:
                bonus += 2.0 * b
            deal_damage(1.0 * b + bonus)

        elif recipe == "DFW":
            deal_damage(1.0 * b)
            target.apply_debuff("Bleeding")
            target.apply_debuff("Slowed")
            log["effects_applied"].append("Target Bleeding and Slowed")

        elif recipe == "DFE":
            deal_self_damage(1.0 * b)
            caster.apply_buff("Charged")
            caster.apply_buff("Honed")
            caster.remove_debuff("Asleep")
            log["effects_applied"].append("Caster Charged & Honed, Cured Asleep")

        elif recipe == "DFL":
            dmg = deal_damage(1.0 * b)
            do_heal(caster, dmg)
            log["effects_applied"].append(f"Healed caster for 100% of damage ({dmg:.1f})")

        elif recipe == "DFD":
            missing_ratio = max(0.0, (caster.max_health - caster.current_health) / caster.max_health)
            bonus = (n * b if n > 0 else 2.0 * b) * missing_ratio
            deal_damage(1.0 * b + bonus)
            log["notes"] += f"Missing HP bonus: +{bonus:.1f}. "

        # ---------------------------------------------------------------------
        # CLASS: PLANTS (WEF, WEW, WEE, WEL, WED, EWF, EWW, EWE, EWL, EWD)
        # ---------------------------------------------------------------------
        elif recipe == "WEF":
            bonus = 2.0 * b if env.location == Location.JUNGLE else 0.0
            deal_damage(1.0 * b + bonus)
            if env.location == Location.JUNGLE:
                env.set_location(Location.NONE)
                log["effects_applied"].append("Location cleared to None")

        elif recipe == "WEW":
            target.apply_debuff("Asleep")
            log["effects_applied"].append("Target Asleep")

        elif recipe == "WEE":
            env.set_location(Location.JUNGLE, b)
            log["effects_applied"].append(f"Location changed to Jungle (potency {b}%)")

        elif recipe == "WEL":
            deal_damage(1.0 * b)
            target.apply_debuff("Entangled")
            log["effects_applied"].append("Target Entangled")

        elif recipe == "WED":
            # (3*b) bonus damage if active seedling has been rained on and sunny
            bonus = 0.0
            if env.seedling_active and env.seedling_rained_on and env.seedling_sunny_on:
                bonus = 3.0 * b
                log["notes"] += "Seedling was rained on and sunny (+3b bonus). "
            deal_damage(1.0 * b + bonus)

        elif recipe == "EWF":
            bonus_heal = 1.0 * b if env.weather == Weather.SUNNY else 0.0
            do_heal(caster, 1.0 * b + bonus_heal)
            caster.alter_stat("potency", 1.0 * b)
            log["effects_applied"].append(f"Healed {1.0*b + bonus_heal:.1f}, Potency +{b:.1f}")

        elif recipe == "EWW":
            deal_damage(1.0 * b)
            target.apply_debuff("Poisoned")
            log["effects_applied"].append("Target Poisoned")

        elif recipe == "EWE":
            env.plant_seedling()
            log["effects_applied"].append("Planted seedling on battlefield")

        elif recipe == "EWL":
            deal_damage(1.0 * b)
            if env.consume_seedling():
                caster.apply_buff("Quickened")
                log["effects_applied"].append("Consumed seedling -> Granted Quickened")

        elif recipe == "EWD":
            deal_damage(1.0 * b)
            if "Entangled" in target.debuffs:
                target.apply_debuff("Bleeding")
                log["effects_applied"].append("Target Bleeding (from Entangled)")

        # ---------------------------------------------------------------------
        # CLASS: FEY (WLF, WLW, WLE, WLL, WLD, LWF, LWW, LWE, LWL, LWD)
        # ---------------------------------------------------------------------
        elif recipe == "WLF":
            bonus = 2.0 * b if "Cursed" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "WLW":
            deal_damage(1.0 * b)
            target.apply_debuff("Cursed")
            log["effects_applied"].append("Target Cursed")

        elif recipe == "WLE":
            env.set_location(Location.ENCHANTED_FOREST, b)
            log["effects_applied"].append(f"Location changed to Enchanted Forest (potency {b}%)")

        elif recipe == "WLL":
            deal_damage(1.0 * b)

        elif recipe == "WLD":
            # Ultimate: Target Asleep, Weather Darkness, Location Enchanted Forest
            bonus = 0.0
            if "Asleep" in target.debuffs and env.weather == Weather.DARKNESS and env.location == Location.ENCHANTED_FOREST:
                bonus = n * b
                log["ultimate_triggered"] = True
                log["notes"] += "ULTIMATE TRIGGERED! "
            deal_damage(1.0 * b + bonus)

        elif recipe == "LWF":
            deal_damage(1.0 * b)
            if env.location == Location.ENCHANTED_FOREST:
                target.apply_debuff("Vulnerable")
                log["effects_applied"].append("Target Vulnerable (Enchanted Forest effect)")

        elif recipe == "LWW":
            caster.apply_debuff("Asleep")
            target.apply_debuff("Asleep")
            log["effects_applied"].append("Caster and Target Asleep")

        elif recipe == "LWE":
            caster.apply_buff("Invisible", duration=1)
            log["effects_applied"].append("Caster Invisible for 1 round")

        elif recipe == "LWL":
            target.apply_debuff("Polymorphed", duration=1)
            log["effects_applied"].append("Target Polymorphed for 1 round")

        elif recipe == "LWD":
            deal_damage(1.0 * b)
            if "Polymorphed" in target.debuffs:
                target.remove_debuff("Polymorphed")
                caster.apply_buff("Invisible", duration=1)
                log["effects_applied"].append("Consumed Polymorphed -> Caster Invisible for 1 round")

        # ---------------------------------------------------------------------
        # CLASS: ICE (WDF, WDW, WDE, WDL, WDD, DWF, DWW, DWE, DWL, DWD)
        # ---------------------------------------------------------------------
        elif recipe == "WDF":
            deal_damage(1.0 * b)
            if env.weather == Weather.RAINING:
                env.set_weather(Weather.SNOWING, b)
                target.apply_debuff("Stunned")
                log["effects_applied"].append("Weather changed to Snowing, Target Stunned")

        elif recipe == "WDW":
            caster.apply_buff("Shielded")
            caster.wdw_retaliation_active = True
            log["effects_applied"].append("Shielded applied with Frosty retaliation on hit")

        elif recipe == "WDE":
            env.set_weather(Weather.SNOWING, b)
            log["effects_applied"].append(f"Weather changed to Snowing (potency {b}%)")

        elif recipe == "WDL":
            deal_damage(1.0 * b)
            target.apply_debuff("Frosty")
            log["effects_applied"].append("Target Frosty")

        elif recipe == "WDD":
            # Ultimate: Weather Blizzard AND Location Tundra
            bonus = 0.0
            if env.weather == Weather.BLIZZARD and env.location == Location.TUNDRA:
                bonus = n * b
                log["ultimate_triggered"] = True
                log["notes"] += "ULTIMATE TRIGGERED! "
            deal_damage(1.0 * b + bonus)

        elif recipe == "DWF":
            deal_damage(1.0 * b)
            if CombatMath.check_luck_chance(caster):
                target.apply_debuff("Frosty")
                log["effects_applied"].append("Frosty applied (Luck roll)")

        elif recipe == "DWW":
            deal_damage(1.0 * b)
            target.apply_debuff("Slowed")
            log["effects_applied"].append("Target Slowed")

        elif recipe == "DWE":
            env.set_location(Location.TUNDRA, b)
            log["effects_applied"].append(f"Location changed to Tundra (potency {b}%)")

        elif recipe == "DWL":
            deal_damage(1.0 * b)
            caster.apply_debuff("Frosty")
            target.apply_debuff("Frosty")
            log["effects_applied"].append("Frosty on Caster and Target")

        elif recipe == "DWD":
            bonus = 0.0
            if "Frosty" in target.debuffs:
                target.remove_debuff("Frosty")
                bonus = 2.0 * b
                target.apply_debuff("Vulnerable")
                log["effects_applied"].append("Consumed Frosty (+2b bonus) -> Target Vulnerable")
            deal_damage(1.0 * b + bonus)

        # ---------------------------------------------------------------------
        # CLASS: WIND (ELF, ELW, ELE, ELL, ELD, LEF, LEW, LEE, LEL, LED)
        # ---------------------------------------------------------------------
        elif recipe == "ELF":
            deal_damage(1.0 * b)
            if "Bleeding" in caster.debuffs:
                caster.remove_debuff("Bleeding")
                env.set_weather(Weather.BLOOD_RAIN, b)
                log["effects_applied"].append("Removed Bleeding -> Weather changed to Blood Rain")

        elif recipe == "ELW":
            deal_damage(1.0 * b)
            target.apply_debuff("Slowed")
            log["effects_applied"].append("Target Slowed")

        elif recipe == "ELE":
            env.set_weather(Weather.WINDY, b)
            log["effects_applied"].append(f"Weather changed to Windy (potency {b}%)")

        elif recipe == "ELL":
            caster.apply_buff("Quickened")
            caster.alter_stat("speed", 1.0 * b)
            caster.remove_debuff("Slowed")
            log["effects_applied"].append(f"Quickened applied, Speed +{b:.1f}, Cured Slowed")

        elif recipe == "ELD":
            bonus = 2.0 * b if env.weather == Weather.RAINING else 0.0
            deal_damage(1.0 * b + bonus)
            env.set_weather(Weather.BLIZZARD, b)
            log["effects_applied"].append("Weather changed to Blizzard")

        elif recipe == "LEF":
            bonus = 2.0 * b if "Burning" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "LEW":
            deal_damage(1.0 * b)
            target.reset_debuff_durations()
            log["effects_applied"].append("Reset durations of all debuffs on target")

        elif recipe == "LEE":
            env.set_weather(Weather.SANDSTORM, b)
            log["effects_applied"].append(f"Weather changed to Sandstorm (potency {b}%)")

        elif recipe == "LEL":
            caster.apply_buff("Quickened")
            target.apply_debuff("Slowed")
            log["effects_applied"].append("Caster Quickened, Target Slowed")

        elif recipe == "LED":
            # Deals damage scaling with caster's Speed ((1*b) * Speed)
            spd = caster.get_effective_stat("speed")
            deal_damage((1.0 * b) * (spd / 100.0))

        # ---------------------------------------------------------------------
        # CLASS: POISON (EDF, EDW, EDE, EDL, EDD, DEF, DEW, DEE, DEL, DED)
        # ---------------------------------------------------------------------
        elif recipe == "EDF":
            bonus = 2.0 * b if "Weakened" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "EDW":
            deal_damage(1.0 * b)
            target.alter_stat("potency", -(1.0 * b))
            target.alter_stat("defense", -(1.0 * b))
            log["effects_applied"].append(f"Target Potency & Defense -{b:.1f}")

        elif recipe == "EDE":
            env.set_location(Location.SWAMP, b)
            log["effects_applied"].append(f"Location changed to Swamp (potency {b}%)")

        elif recipe == "EDL":
            deal_damage(1.0 * b)
            target.apply_debuff("Poisoned")
            log["effects_applied"].append("Target Poisoned")

        elif recipe == "EDD":
            # Ultimate: Target Bleeding AND Location Swamp
            bonus = 0.0
            if "Bleeding" in target.debuffs and env.location == Location.SWAMP:
                bonus = n * b
                log["ultimate_triggered"] = True
                log["notes"] += "ULTIMATE TRIGGERED! "
            deal_damage(1.0 * b + bonus)

        elif recipe == "DEF":
            missing_pot = max(0.0, target.base_potency - target.get_effective_stat("potency"))
            ratio = missing_pot / target.base_potency if target.base_potency > 0 else 0.0
            bonus = (n * b if n > 0 else 2.0 * b) * ratio
            deal_damage(1.0 * b + bonus)
            log["notes"] += f"Missing Potency bonus: +{bonus:.1f}. "

        elif recipe == "DEW":
            deal_damage(1.0 * b)
            target.alter_stat("potency", -(1.0 * b))
            target.alter_stat("luck", -(1.0 * b))
            log["effects_applied"].append(f"Target Potency & Luck -{b:.1f}")

        elif recipe == "DEE":
            deal_damage(1.0 * b)
            target.apply_debuff("Weakened")
            log["effects_applied"].append("Target Weakened")

        elif recipe == "DEL":
            deal_damage(1.0 * b)
            if "Bleeding" in target.debuffs:
                target.apply_debuff("Infected")
                log["effects_applied"].append("Target Infected (from Bleeding)")

        elif recipe == "DED":
            deal_damage(1.0 * b)
            num_debuffs = len(target.debuffs)
            target.cleanse_all_debuffs()
            heal_amount = num_debuffs * (1.0 * b)
            do_heal(caster, heal_amount)
            log["effects_applied"].append(f"Removed {num_debuffs} debuffs on target -> Healed {heal_amount:.1f}")

        # ---------------------------------------------------------------------
        # CLASS: COSMIC (LDF, LDW, LDE, LDL, LDD, DLF, DLW, DLE, DLL, DLD)
        # ---------------------------------------------------------------------
        elif recipe == "LDF":
            deal_damage(1.0 * b)
            target.apply_debuff("Blinded")
            log["effects_applied"].append("Target Blinded")

        elif recipe == "LDW":
            deal_damage(1.0 * b)
            if CombatMath.check_luck_chance(caster):
                target.apply_debuff("Stunned")
                log["effects_applied"].append("Target Stunned (Luck roll)")

        elif recipe == "LDE":
            env.set_location(Location.SPACE, b)
            log["effects_applied"].append(f"Location changed to Space (potency {b}%)")

        elif recipe == "LDL":
            bonus = 2.0 * b if "Blinded" in target.debuffs else 0.0
            deal_damage(1.0 * b + bonus)

        elif recipe == "LDD":
            # Ultimate: Target has Blinded, Weakened, Slowed, AND Vulnerable
            bonus = 0.0
            req = {"Blinded", "Weakened", "Slowed", "Vulnerable"}
            if req.issubset(set(target.debuffs.keys())):
                bonus = n * b
                log["ultimate_triggered"] = True
                log["notes"] += "ULTIMATE TRIGGERED! "
            deal_damage(1.0 * b + bonus)

        elif recipe == "DLF":
            deal_damage(1.0 * b)
            if "Slowed" in target.debuffs:
                target.remove_debuff("Slowed")
                caster.alter_stat("speed", 1.0 * b)
                log["effects_applied"].append(f"Consumed Slowed -> Caster Speed +{b:.1f}")

        elif recipe == "DLW":
            deal_damage(1.0 * b)

        elif recipe == "DLE":
            # Swaps caster and target base Potency and Defense for remainder of match
            c_pot, c_def = caster.base_potency, caster.base_defense
            t_pot, t_def = target.base_potency, target.base_defense
            caster.base_potency, caster.base_defense = t_pot, t_def
            target.base_potency, target.base_defense = c_pot, c_def
            log["effects_applied"].append("Swapped base Potency and Defense between Caster and Target")

        elif recipe == "DLL":
            deal_damage(1.0 * b)
            if env.weather == Weather.DARKNESS:
                caster.apply_buff("Charged")
                caster.apply_buff("Quickened")
                target.apply_debuff("Slowed")
                log["effects_applied"].append("Darkness effect: Caster Charged & Quickened, Target Slowed")

        elif recipe == "DLD":
            # Deals damage scaling with target's missing health
            missing_ratio = max(0.0, (target.max_health - target.current_health) / target.max_health)
            bonus = (n * b if n > 0 else 2.0 * b) * missing_ratio
            deal_damage(1.0 * b + bonus)
            log["notes"] += f"Target missing HP bonus: +{bonus:.1f}. "

        else:
            raise NotImplementedError(f"Spell logic for recipe '{recipe}' is not implemented.")

        return log


# =============================================================================
# 7. GAME ENGINE & 1V1 TURN RESOLUTION
# =============================================================================

class ProjectSorceryGame:
    """
    Main 1v1 turn-based game engine for Project Sorcery.
    Simulates battles between two AI agents, handling:
    - Speed & Priority-based Turn Initiative
    - Sequential Spell Resolution
    - Hard CC & Turn Skipping
    - End-of-Turn DoT / HoT / Status Decay Phase
    - Observation Vector generation for Neural Networks
    """
    def __init__(
        self,
        player1: Wizard,
        player2: Wizard,
        spell_data_path: str = "spell_data.json",
        max_turns: int = 50
    ):
        self.player1 = player1
        self.player2 = player2
        self.registry = get_registry(spell_data_path)
        self.resolver = SpellResolver(self.registry)
        self.env = Environment()
        self.current_turn: int = 0
        self.max_turns: int = max_turns
        self.is_over: bool = False
        self.winner: Optional[str] = None
        self.combat_logs: List[Dict[str, Any]] = []

    def reset(self) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Resets the match to the initial state."""
        self.player1.reset()
        self.player2.reset()
        self.env = Environment()
        self.current_turn = 0
        self.is_over = False
        self.winner = None
        self.combat_logs.clear()
        return self.get_state(0), self.get_state(1)

    def determine_initiative(self) -> Tuple[Wizard, Wizard]:
        """
        Determines which wizard acts first this turn.
        Priority rules:
        1. 'next_turn_priority' from FLL guarantees first action.
        2. 'Entangled' status prevents turn priority.
        3. Higher effective Speed goes first.
        4. Tie broken randomly.
        """
        p1 = self.player1
        p2 = self.player2

        # 1. FLL Priority check
        if p1.has_next_turn_priority and not p2.has_next_turn_priority:
            p1.has_next_turn_priority = False
            return p1, p2
        elif p2.has_next_turn_priority and not p1.has_next_turn_priority:
            p2.has_next_turn_priority = False
            return p2, p1
        elif p1.has_next_turn_priority and p2.has_next_turn_priority:
            p1.has_next_turn_priority = False
            p2.has_next_turn_priority = False

        # 2. Entangled check (Entangled prevents turn priority)
        p1_entangled = "Entangled" in p1.debuffs
        p2_entangled = "Entangled" in p2.debuffs
        if not p1_entangled and p2_entangled:
            return p1, p2
        elif p1_entangled and not p2_entangled:
            return p2, p1

        # 3. Speed check
        spd1 = p1.get_effective_stat("speed")
        spd2 = p2.get_effective_stat("speed")

        if spd1 > spd2:
            return p1, p2
        elif spd2 > spd1:
            return p2, p1
        else:
            # 50/50 tie-breaker
            return (p1, p2) if random.random() < 0.5 else (p2, p1)

    def step(
        self,
        action_p1: Union[str, int, List[str]],
        action_p2: Union[str, int, List[str]]
    ) -> Tuple[Dict[str, Any], Dict[str, Any], float, float, bool, Dict[str, Any]]:
        """
        Executes one full turn of the 1v1 duel.
        Actions can be:
        - Recipe string: e.g. "FFF"
        - Integer index: 0..124
        - Rune list: e.g. ["F", "F", "F"]

        Returns:
            (obs_p1, obs_p2, reward_p1, reward_p2, done, info)
        """
        if self.is_over:
            raise RuntimeError("Match is already over. Call reset() to start a new match.")

        self.current_turn += 1
        self.player1.turns_survived += 1
        self.player2.turns_survived += 1

        # Format action strings
        recipe1 = self._parse_action(action_p1)
        recipe2 = self._parse_action(action_p2)

        turn_log = {
            "turn": self.current_turn,
            "weather": self.env.weather.value,
            "location": self.env.location.value,
            "events": []
        }

        # 1. Determine Turn Initiative
        first, second = self.determine_initiative()
        first_recipe = recipe1 if first is self.player1 else recipe2
        second_recipe = recipe2 if second is self.player2 else recipe1

        # 2. First Caster Resolves
        can_first_act, reason1 = first.can_act()
        if can_first_act:
            first_log = self.resolver.resolve(first_recipe, first, second, self.env)
            turn_log["events"].append(first_log)
        else:
            turn_log["events"].append({"actor": first.name, "action": "skipped", "reason": reason1})

        # Check if second wizard is defeated
        if not second.is_alive:
            self._conclude_match(winner=first.name)
            self.combat_logs.append(turn_log)
            r1, r2 = self._calculate_rewards()
            return self.get_state(0), self.get_state(1), r1, r2, True, {"winner": self.winner}

        # 3. Second Caster Resolves (if still alive)
        can_second_act, reason2 = second.can_act()
        if can_second_act:
            second_log = self.resolver.resolve(second_recipe, second, first, self.env)
            turn_log["events"].append(second_log)
        else:
            turn_log["events"].append({"actor": second.name, "action": "skipped", "reason": reason2})

        # Check if first wizard is defeated
        if not first.is_alive:
            self._conclude_match(winner=second.name)
            self.combat_logs.append(turn_log)
            r1, r2 = self._calculate_rewards()
            return self.get_state(0), self.get_state(1), r1, r2, True, {"winner": self.winner}

        # 4. End-of-Turn Phase (Status Effects & DoTs)
        self._resolve_end_of_turn_effects(turn_log)

        # Check for defeat after DoTs
        if not self.player1.is_alive and not self.player2.is_alive:
            self._conclude_match(winner="Draw")
        elif not self.player1.is_alive:
            self._conclude_match(winner=self.player2.name)
        elif not self.player2.is_alive:
            self._conclude_match(winner=self.player1.name)
        elif self.current_turn >= self.max_turns:
            # Turn limit reached: tiebreaker on HP percentage
            p1_ratio = self.player1.current_health / self.player1.max_health
            p2_ratio = self.player2.current_health / self.player2.max_health
            if p1_ratio > p2_ratio:
                self._conclude_match(winner=self.player1.name)
            elif p2_ratio > p1_ratio:
                self._conclude_match(winner=self.player2.name)
            else:
                self._conclude_match(winner="Draw")

        self.combat_logs.append(turn_log)
        r1, r2 = self._calculate_rewards()
        return self.get_state(0), self.get_state(1), r1, r2, self.is_over, {"winner": self.winner}

    def _resolve_end_of_turn_effects(self, turn_log: Dict[str, Any]) -> None:
        """
        Handles:
        - DoT Damage: Burning, Bleeding, Poisoned, Infected, Blizzard
        - HoT: Blessed
        - Seedling status progression
        - Status duration decrements
        """
        for wiz in [self.player1, self.player2]:
            if not wiz.is_alive:
                continue

            # HoT: Blessed (heals 5% max health each turn)
            if "Blessed" in wiz.buffs:
                heal_amt = 0.05 * wiz.max_health
                actual_heal = wiz.heal(heal_amt)
                turn_log["events"].append({"actor": wiz.name, "effect": "Blessed HoT", "heal": actual_heal})

            # DoT: Burning (5% of Current Health)
            if "Burning" in wiz.debuffs:
                burn_dmg = 0.05 * wiz.current_health
                actual_burn = wiz.take_damage(burn_dmg, is_direct=False)
                turn_log["events"].append({"actor": wiz.name, "effect": "Burning DoT", "damage": actual_burn})

            # DoT: Bleeding (6% of Maximum Health)
            if "Bleeding" in wiz.debuffs:
                bleed_dmg = 0.06 * wiz.max_health
                actual_bleed = wiz.take_damage(bleed_dmg, is_direct=False)
                turn_log["events"].append({"actor": wiz.name, "effect": "Bleeding DoT", "damage": actual_bleed})

            # Escalating DoT: Poisoned (3% max HP + 2% per turn active)
            if "Poisoned" in wiz.debuffs:
                pct = 0.03 + (0.02 * wiz.poison_turns_active)
                poison_dmg = pct * wiz.max_health
                actual_poison = wiz.take_damage(poison_dmg, is_direct=False)
                wiz.poison_turns_active += 1
                turn_log["events"].append({"actor": wiz.name, "effect": "Poisoned DoT", "damage": actual_poison, "pct": pct})

            # Severe Escalating DoT: Infected (5% max HP + 3% per turn active)
            if "Infected" in wiz.debuffs:
                pct = 0.05 + (0.03 * wiz.infected_turns_active)
                inf_dmg = pct * wiz.max_health
                actual_inf = wiz.take_damage(inf_dmg, is_direct=False)
                wiz.infected_turns_active += 1
                turn_log["events"].append({"actor": wiz.name, "effect": "Infected DoT", "damage": actual_inf, "pct": pct})

            # Blizzard Weather Effect: applies Frosty each turn
            if self.env.weather == Weather.BLIZZARD:
                wiz.apply_debuff("Frosty")

            # Status Duration Decrements
            self._decrement_durations(wiz)

        # Update environment seedling
        self.env.update_seedling()

    def _decrement_durations(self, wiz: Wizard) -> None:
        """Ticks down durations of active buffs and status effects."""
        # Buffs
        for buff in list(wiz.buffs.keys()):
            wiz.buffs[buff] -= 1
            if wiz.buffs[buff] <= 0:
                wiz.remove_buff(buff)

        # Debuffs (duration -1 means until cleansed, e.g. Poisoned & Infected)
        for debuff in list(wiz.debuffs.keys()):
            if wiz.debuffs[debuff] > 0:
                wiz.debuffs[debuff] -= 1
                if wiz.debuffs[debuff] <= 0:
                    wiz.remove_debuff(debuff)

    def _parse_action(self, action: Union[str, int, List[str]]) -> str:
        """Standardizes action input into a 3-character uppercase recipe string."""
        recipes = self.registry.all_recipes()
        if isinstance(action, int):
            if 0 <= action < len(recipes):
                return recipes[action]
            raise IndexError(f"Action index {action} out of bounds (0..{len(recipes)-1}).")
        elif isinstance(action, (list, tuple)):
            recipe = "".join(str(r).upper() for r in action)
            if recipe in recipes:
                return recipe
            raise ValueError(f"Invalid recipe list {action} -> '{recipe}'.")
        elif isinstance(action, str):
            recipe = action.strip().upper()
            if recipe in recipes:
                return recipe
            raise ValueError(f"Unknown recipe '{recipe}'. Must be one of 125 valid spell recipes.")
        raise TypeError(f"Unsupported action type: {type(action)}")

    def _conclude_match(self, winner: str) -> None:
        self.is_over = True
        self.winner = winner

    def _calculate_rewards(self) -> Tuple[float, float]:
        """Reward function suitable for Genetic Algorithm fitness or RL training."""
        p1_hp_ratio = self.player1.current_health / self.player1.max_health
        p2_hp_ratio = self.player2.current_health / self.player2.max_health

        base_r1 = p1_hp_ratio - p2_hp_ratio
        base_r2 = p2_hp_ratio - p1_hp_ratio

        if self.is_over:
            if self.winner == self.player1.name:
                base_r1 += 10.0
                base_r2 -= 10.0
            elif self.winner == self.player2.name:
                base_r1 -= 10.0
                base_r2 += 10.0

        return base_r1, base_r2

    # -------------------------------------------------------------------------
    # State & Neural Network Observation Vector Extraction
    # -------------------------------------------------------------------------
    def get_state(self, player_idx: int) -> Dict[str, Any]:
        """
        Returns rich structured state representation for an AI player.
        Contains:
        - player & opponent HP, max HP, and effective stats
        - active buffs and debuffs with durations
        - environment weather, location, and seedling status
        - numeric feature vector for direct neural network input
        """
        me = self.player1 if player_idx == 0 else self.player2
        opp = self.player2 if player_idx == 0 else self.player1

        return {
            "turn": self.current_turn,
            "is_over": self.is_over,
            "winner": self.winner,
            "me": {
                "name": me.name,
                "current_health": me.current_health,
                "max_health": me.max_health,
                "potency": me.get_effective_stat("potency"),
                "defense": me.get_effective_stat("defense"),
                "luck": me.get_effective_stat("luck"),
                "speed": me.get_effective_stat("speed"),
                "buffs": dict(me.buffs),
                "debuffs": dict(me.debuffs),
                "has_priority": me.has_next_turn_priority,
            },
            "opponent": {
                "name": opp.name,
                "current_health": opp.current_health,
                "max_health": opp.max_health,
                "potency": opp.get_effective_stat("potency"),
                "defense": opp.get_effective_stat("defense"),
                "luck": opp.get_effective_stat("luck"),
                "speed": opp.get_effective_stat("speed"),
                "buffs": dict(opp.buffs),
                "debuffs": dict(opp.debuffs),
                "has_priority": opp.has_next_turn_priority,
            },
            "environment": {
                "weather": self.env.weather.value,
                "weather_potency": self.env.weather_potency,
                "location": self.env.location.value,
                "location_potency": self.env.location_potency,
                "seedling_active": self.env.seedling_active,
                "seedling_rained_on": self.env.seedling_rained_on,
                "seedling_sunny_on": self.env.seedling_sunny_on,
            },
            "feature_vector": self.get_observation_vector(player_idx)
        }

    def get_observation_vector(self, player_idx: int) -> List[float]:
        """
        Vectorized numerical representation of the game state for Neural Networks.
        Length: 54 normalized float features.
        """
        me = self.player1 if player_idx == 0 else self.player2
        opp = self.player2 if player_idx == 0 else self.player1

        vec: List[float] = []

        # 1. Turn progress
        vec.append(min(1.0, self.current_turn / float(self.max_turns)))

        # 2. Player health and stats (normalized relative to 100/1000 baselines)
        vec.append(me.current_health / max(1.0, me.max_health))
        vec.append(me.max_health / 1000.0)
        vec.append(me.get_effective_stat("potency") / 100.0)
        vec.append(me.get_effective_stat("defense") / 100.0)
        vec.append(me.get_effective_stat("luck") / 50.0)
        vec.append(me.get_effective_stat("speed") / 100.0)
        vec.append(1.0 if me.has_next_turn_priority else 0.0)

        # 3. Opponent health and stats
        vec.append(opp.current_health / max(1.0, opp.max_health))
        vec.append(opp.max_health / 1000.0)
        vec.append(opp.get_effective_stat("potency") / 100.0)
        vec.append(opp.get_effective_stat("defense") / 100.0)
        vec.append(opp.get_effective_stat("luck") / 50.0)
        vec.append(opp.get_effective_stat("speed") / 100.0)
        vec.append(1.0 if opp.has_next_turn_priority else 0.0)

        # 4. Player active buffs (6 flags)
        for b_name in ["Charged", "Honed", "Shielded", "Quickened", "Invisible", "Blessed"]:
            vec.append(1.0 if b_name in me.buffs else 0.0)

        # 5. Player active debuffs (14 flags)
        for d_name in [
            "Burning", "Poisoned", "Cursed", "Slowed", "Vulnerable", "Weakened", "Blinded",
            "Bleeding", "Entangled", "Frosty", "Stunned", "Asleep", "Polymorphed", "Infected"
        ]:
            vec.append(1.0 if d_name in me.debuffs else 0.0)

        # 6. Opponent active buffs (6 flags)
        for b_name in ["Charged", "Honed", "Shielded", "Quickened", "Invisible", "Blessed"]:
            vec.append(1.0 if b_name in opp.buffs else 0.0)

        # 7. Opponent active debuffs (14 flags)
        for d_name in [
            "Burning", "Poisoned", "Cursed", "Slowed", "Vulnerable", "Weakened", "Blinded",
            "Bleeding", "Entangled", "Frosty", "Stunned", "Asleep", "Polymorphed", "Infected"
        ]:
            vec.append(1.0 if d_name in opp.debuffs else 0.0)

        # 8. Environment features
        # One-hot Weather (10 categories)
        weather_list = [
            Weather.CLEAR, Weather.STORMING, Weather.SNOWING, Weather.BLOOD_RAIN,
            Weather.WINDY, Weather.SUNNY, Weather.DARKNESS, Weather.SANDSTORM,
            Weather.RAINING, Weather.BLIZZARD
        ]
        for w in weather_list:
            vec.append(1.0 if self.env.weather == w else 0.0)

        # One-hot Location (7 categories)
        location_list = [
            Location.NONE, Location.JUNGLE, Location.GRAVEYARD, Location.ENCHANTED_FOREST,
            Location.TUNDRA, Location.SWAMP, Location.SPACE
        ]
        for loc in location_list:
            vec.append(1.0 if self.env.location == loc else 0.0)

        # Seedling features (3 flags)
        vec.append(1.0 if self.env.seedling_active else 0.0)
        vec.append(1.0 if self.env.seedling_rained_on else 0.0)
        vec.append(1.0 if self.env.seedling_sunny_on else 0.0)

        return vec


# =============================================================================
# 8. CONVENIENCE RUNNER FOR 1V1 DUELS & GENETIC AI TESTING
# =============================================================================

def run_duel(
    p1: Wizard,
    p2: Wizard,
    policy_p1: Callable[[Dict[str, Any]], Union[str, int, List[str]]],
    policy_p2: Callable[[Dict[str, Any]], Union[str, int, List[str]]],
    spell_data_path: str = "spell_data.json",
    max_turns: int = 50,
    verbose: bool = False
) -> Dict[str, Any]:
    """
    Simulates a full 1v1 match between two policy agents.
    policy_p1 and policy_p2 are callables that take the game state dictionary and return an action.
    """
    game = ProjectSorceryGame(p1, p2, spell_data_path=spell_data_path, max_turns=max_turns)
    obs1, obs2 = game.reset()

    while not game.is_over:
        action1 = policy_p1(obs1)
        action2 = policy_p2(obs2)
        obs1, obs2, r1, r2, done, info = game.step(action1, action2)
        if verbose:
            last_turn = game.combat_logs[-1]
            print(f"--- Turn {last_turn['turn']} (Weather: {last_turn['weather']}, Loc: {last_turn['location']}) ---")
            for evt in last_turn["events"]:
                print(f"  {evt}")
            print(f"  HP -> {p1.name}: {p1.current_health:.1f}/{p1.max_health:.1f} | {p2.name}: {p2.current_health:.1f}/{p2.max_health:.1f}")

    return {
        "winner": game.winner,
        "turns": game.current_turn,
        "p1_final_hp": p1.current_health,
        "p2_final_hp": p2.current_health,
        "p1_damage_dealt": p1.damage_dealt,
        "p2_damage_dealt": p2.damage_dealt,
        "combat_logs": game.combat_logs,
    }


if __name__ == "__main__":
    print("Project Sorcery Engine loaded successfully.")
    # Quick self-test
    w1 = Wizard(name="Pyromancer_AI", starting_hp=1000.0, base_potency=120.0, base_defense=80.0, base_luck=60.0, base_speed=110.0)
    w2 = Wizard(name="Cryomancer_AI", starting_hp=1000.0, base_potency=90.0, base_defense=120.0, base_luck=70.0, base_speed=95.0)

    # Simple random policy test
    recipes = get_registry("spell_data.json").all_recipes()
    p_rand = lambda obs: random.choice(recipes)

    res = run_duel(w1, w2, p_rand, p_rand, verbose=True)
    print(f"Self-Test Duel Result: {res['winner']} in {res['turns']} turns!")
