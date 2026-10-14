#!/usr/bin/env python3
"""
Project Sorcery - Mobile Arena UI
==================================
A sleek, touch-optimized, aesthetically rich interface for Project Sorcery.
Runs seamlessly in Pydroid 3 on mobile (Android) as well as desktop browsers.

Features:
- Character & Stat Customization (HP, Potency, Defense, Luck, Speed + Archetype presets)
- AI Opponent Selector: Battle against any of the 100 trained Neural DQN Bots
- Arena Environment Controls: Choose or randomize Weathers & Locations
- Live Rune Pool & Dynamic Spell Weaving (Tap runes or choose from craftable spells)
- Turn Initiative Display, Dynamic Condition Evaluation, and Animated Health Bars
- Rich Turn Breakdown Modal & Combat Log
- Embedded Web Audio API SFX (Cast whoosh, elemental strikes, critical hits, victory chimes)
- Zero external CDN dependencies - 100% self-contained and offline-ready for Pydroid
- Optional Tkinter GUI fallback mode (--tk)
"""

import argparse
import copy
import json
import math
import os
import random
import socket
import sys
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import parse_qs, urlparse

# Ensure local directories are in python path
SCRIPT_DIR = Path(__file__).resolve().parent
for p in [SCRIPT_DIR, SCRIPT_DIR / "downloads", SCRIPT_DIR.parent, Path.cwd()]:
    if p.exists() and str(p) not in sys.path:
        sys.path.insert(0, str(p))

def resolve_file(filename: str) -> Optional[Path]:
    """Finds project data files in common directories."""
    candidates = [
        SCRIPT_DIR / filename,
        Path.cwd() / filename,
        SCRIPT_DIR / "downloads" / filename,
        SCRIPT_DIR.parent / filename,
        SCRIPT_DIR.parent / "downloads" / filename,
    ]
    for c in candidates:
        if c.exists():
            return c.resolve()
    return None

# Attempt to import project_sorcery and simulation
try:
    import project_sorcery
    from project_sorcery import (
        ProjectSorceryGame,
        Wizard,
        Weather,
        Location,
        get_castable_spells_from_pool,
        BUFF_CONFIGS,
        STATUS_CONFIGS,
    )
except ImportError as e:
    raise ImportError(f"Could not import project_sorcery game engine: {e}")

try:
    import simulation
except ImportError:
    simulation = None

# =============================================================================
# GAME DATA LOADER & HEURISTIC FALLBACK POLICY
# =============================================================================

SPELL_DATA_FILE = resolve_file("spell_data.json")
AI_BOTS_DNA_FILE = resolve_file("ai_bots_dna.json")

ALL_SPELLS: Dict[str, Any] = {}
if SPELL_DATA_FILE and SPELL_DATA_FILE.exists():
    with open(SPELL_DATA_FILE, "r", encoding="utf-8") as f:
        ALL_SPELLS = json.load(f)

ALL_BOTS_DATA: List[Dict[str, Any]] = []
ACTION_CATALOG: List[str] = list(ALL_SPELLS.keys())

if AI_BOTS_DNA_FILE and AI_BOTS_DNA_FILE.exists():
    try:
        with open(AI_BOTS_DNA_FILE, "r", encoding="utf-8") as f:
            dna_json = json.load(f)
            ALL_BOTS_DATA = dna_json.get("bots", [])
            cat = dna_json.get("meta", {}).get("action_catalog")
            if cat:
                ACTION_CATALOG = cat
    except Exception as ex:
        print(f"Notice: Could not fully load ai_bots_dna.json: {ex}")

# Fallback bots if ai_bots_dna.json is not present
if not ALL_BOTS_DATA:
    ALL_BOTS_DATA = [
        {
            "bot_id": "bot_001",
            "name": "Ignis Emberstrike",
            "archetype": "Pyromancer",
            "affinity_class": "Fire",
            "tactical_focus": "Direct Damage / Burn Burst",
            "wizard_stats": {
                "starting_hp": 1000.0,
                "base_potency": 100.0,
                "base_defense": 100.0,
                "base_luck": 100.0,
                "base_speed": 100.0,
            },
        },
        {
            "bot_id": "bot_008",
            "name": "Thalassa Deepwave",
            "archetype": "Hydromancer",
            "affinity_class": "Water",
            "tactical_focus": "Sustain / Control",
            "wizard_stats": {
                "starting_hp": 1000.0,
                "base_potency": 100.0,
                "base_defense": 100.0,
                "base_luck": 100.0,
                "base_speed": 100.0,
            },
        },
        {
            "bot_id": "bot_020",
            "name": "Terra Stoneguard",
            "archetype": "Geomancer",
            "affinity_class": "Earth",
            "tactical_focus": "Shields / Heavy Impact",
            "wizard_stats": {
                "starting_hp": 1100.0,
                "base_potency": 90.0,
                "base_defense": 120.0,
                "base_luck": 95.0,
                "base_speed": 95.0,
            },
        },
        {
            "bot_id": "bot_035",
            "name": "Zephyr Skycleaver",
            "archetype": "Aeromancer",
            "affinity_class": "Wind",
            "tactical_focus": "Speed / Multi-strike",
            "wizard_stats": {
                "starting_hp": 950.0,
                "base_potency": 110.0,
                "base_defense": 90.0,
                "base_luck": 100.0,
                "base_speed": 120.0,
            },
        },
        {
            "bot_id": "bot_050",
            "name": "Noctis Voidwalker",
            "archetype": "Shadowcaster",
            "affinity_class": "Dark",
            "tactical_focus": "Debuffs / Execute",
            "wizard_stats": {
                "starting_hp": 980.0,
                "base_potency": 115.0,
                "base_defense": 95.0,
                "base_luck": 110.0,
                "base_speed": 105.0,
            },
        },
    ]

class HeuristicFallbackPolicy:
    """Smart heuristic policy used when a bot does not have neural weights."""
    def __init__(self, bot_dict: Dict[str, Any]):
        self.bot_id = bot_dict.get("bot_id", "fallback")
        self.name = bot_dict.get("name", "AI Wizard")
        self.affinity = bot_dict.get("affinity_class", "Fire")

    def __call__(self, obs: Dict[str, Any]) -> str:
        castable = obs.get("me", {}).get("castable_spells", obs.get("castable_spells", []))
        if not castable:
            return "FFF"
        
        target_debuffs = obs.get("opponent", {}).get("debuffs", {})
        caster_buffs = obs.get("me", {}).get("buffs", {})
        
        best_spell = castable[0]
        best_score = -999.0

        for recipe in castable:
            s_data = ALL_SPELLS.get(recipe, {})
            b = float(s_data.get("b", 30.0))
            n = float(s_data.get("n", 0.0))
            s_class = s_data.get("class", "")
            cond = s_data.get("condition_required", "")

            score = b
            if s_class == self.affinity:
                score += 15.0
            
            if cond and cond != "None":
                cond_lower = cond.lower()
                for debuff in target_debuffs:
                    if debuff.lower() in cond_lower:
                        score += b * (n if n > 0 else 1.5)
                for buff in caster_buffs:
                    if buff.lower() in cond_lower:
                        score += b * (n if n > 0 else 1.5)
            
            opp_hp = obs.get("opponent", {}).get("current_health", 1000)
            if opp_hp < 300 and ("execute" in s_data.get("description", "").lower() or b > 50):
                score += 30.0

            if score > best_score:
                best_score = score
                best_spell = recipe

        return best_spell

def get_ai_policy(bot_dict: Dict[str, Any]):
    """Instantiates a NeuralBotPolicy if available, otherwise heuristic fallback."""
    if simulation and "dna" in bot_dict and bot_dict["dna"]:
        try:
            return simulation.NeuralBotPolicy(bot_dict, ACTION_CATALOG)
        except Exception as e:
            print(f"Falling back to heuristic policy for {bot_dict.get('name')}: {e}")
    return HeuristicFallbackPolicy(bot_dict)

# =============================================================================
# BATTLE MANAGER
# =============================================================================

class BattleManager:
    """Manages active duel state between Human Player and AI."""
    def __init__(self):
        self.game: Optional[ProjectSorceryGame] = None
        self.ai_policy = None
        self.player_wizard: Optional[Wizard] = None
        self.ai_wizard: Optional[Wizard] = None
        self.current_obs_p1: Optional[Dict[str, Any]] = None
        self.current_obs_p2: Optional[Dict[str, Any]] = None
        self.is_active: bool = False
        self.ai_bot_info: Dict[str, Any] = {}
        self.turn_events_history: List[Dict[str, Any]] = []

    def start_game(
        self,
        player_name: str,
        hp: float,
        potency: float,
        defense: float,
        luck: float,
        speed: float,
        bot_id: str,
        weather_name: str = "Random",
        location_name: str = "Random"
    ) -> Dict[str, Any]:
        """Initializes a new duel with chosen stats and environment."""
        # Find AI Bot
        bot_dict = next((b for b in ALL_BOTS_DATA if b["bot_id"] == bot_id), ALL_BOTS_DATA[0])
        self.ai_bot_info = bot_dict

        # Create Player Wizard
        self.player_wizard = Wizard(
            name=player_name.strip() or "Archmage",
            starting_hp=float(hp),
            max_health=float(hp),
            current_health=float(hp),
            base_potency=float(potency),
            base_defense=float(defense),
            base_luck=float(luck),
            base_speed=float(speed),
        )

        # Create AI Wizard
        if simulation:
            self.ai_wizard = simulation.create_wizard_for_bot(bot_dict)
        else:
            w_stats = bot_dict.get("wizard_stats", {})
            self.ai_wizard = Wizard(
                name=bot_dict.get("name", "AI Wizard"),
                starting_hp=float(w_stats.get("starting_hp", 1000.0)),
                max_health=float(w_stats.get("starting_hp", 1000.0)),
                current_health=float(w_stats.get("starting_hp", 1000.0)),
                base_potency=float(w_stats.get("base_potency", 100.0)),
                base_defense=float(w_stats.get("base_defense", 100.0)),
                base_luck=float(w_stats.get("base_luck", 100.0)),
                base_speed=float(w_stats.get("base_speed", 100.0)),
            )

        # AI Policy
        self.ai_policy = get_ai_policy(bot_dict)

        # Initialize Game
        self.game = ProjectSorceryGame(
            player1=self.player_wizard,
            player2=self.ai_wizard,
            spell_data_path=str(SPELL_DATA_FILE) if SPELL_DATA_FILE else None,
            max_turns=50,
        )

        initial_state = {}
        if weather_name and weather_name != "Random":
            initial_state["weather"] = weather_name
        if location_name and location_name != "Random":
            initial_state["location"] = location_name

        self.current_obs_p1, self.current_obs_p2 = self.game.reset(
            initial_board_state=initial_state if initial_state else None
        )
        self.is_active = True
        self.turn_events_history = []

        return self.get_ui_state()

    def cast_turn(self, player_recipe: str) -> Dict[str, Any]:
        """Executes a round where Player and AI cast spells."""
        if not self.is_active or not self.game or self.game.is_over:
            return {"error": "No active match. Please start a duel first."}

        p1_castable = self.current_obs_p1.get("me", {}).get(
            "castable_spells", self.current_obs_p1.get("castable_spells", [])
        )
        if player_recipe not in p1_castable:
            pool = list(self.player_wizard.rune_pool)
            needed = list(player_recipe.upper())
            valid = True
            for r in needed:
                if r in pool:
                    pool.remove(r)
                else:
                    valid = False
                    break
            if not valid:
                return {
                    "error": f"Recipe {player_recipe} cannot be cast with your current rune pool: {self.player_wizard.rune_pool}"
                }

        # Determine AI action
        try:
            ai_recipe = self.ai_policy(self.current_obs_p2)
        except Exception:
            ai_castable = self.current_obs_p2.get("me", {}).get(
                "castable_spells", self.current_obs_p2.get("castable_spells", ["FFF"])
            )
            ai_recipe = ai_castable[0] if ai_castable else "FFF"

        # Step the game
        obs1_next, obs2_next, r1, r2, done, info = self.game.step(player_recipe, ai_recipe)
        self.current_obs_p1 = obs1_next
        self.current_obs_p2 = obs2_next

        last_turn_log = self.game.combat_logs[-1] if self.game.combat_logs else {}
        self.turn_events_history.append(last_turn_log)

        if done or self.game.is_over:
            self.is_active = False

        state = self.get_ui_state()
        state["last_turn_log"] = last_turn_log
        state["player_cast"] = player_recipe
        state["ai_cast"] = ai_recipe
        return state

    def get_ui_state(self) -> Dict[str, Any]:
        """Serializes current match state for the web / mobile UI."""
        if not self.game:
            return {"is_active": False}

        p1 = self.player_wizard
        p2 = self.ai_wizard
        env = self.game.env

        # Enrich castable spells with metadata and condition status
        castable_list = []
        raw_castable = self.current_obs_p1.get("me", {}).get(
            "castable_spells", self.current_obs_p1.get("castable_spells", [])
        )
        for recipe in raw_castable:
            s_data = ALL_SPELLS.get(recipe, {})
            cond_req = s_data.get("condition_required", "None")
            cond_met = False
            cond_text = ""
            if cond_req and cond_req != "None":
                cond_l = cond_req.lower()
                for debuff in p2.debuffs:
                    if debuff.lower() in cond_l:
                        cond_met = True
                        cond_text = f"Target has {debuff}"
                        break
                if not cond_met:
                    for buff in p1.buffs:
                        if buff.lower() in cond_l:
                            cond_met = True
                            cond_text = f"You have {buff}"
                            break
                if not cond_met:
                    if env.weather.value.lower() in cond_l:
                        cond_met = True
                        cond_text = f"Weather is {env.weather.value}"
                    elif env.location.value.lower() in cond_l:
                        cond_met = True
                        cond_text = f"Location is {env.location.value}"

            castable_list.append({
                "recipe": recipe,
                "class": s_data.get("class", "Arcane"),
                "category": s_data.get("category", "Spell"),
                "b": s_data.get("b", 0.0),
                "n": s_data.get("n", 0.0),
                "max_potential": s_data.get("max_potential", 0.0),
                "description": s_data.get("description", ""),
                "condition_required": cond_req,
                "condition_met": cond_met,
                "condition_text": cond_text,
            })

        p1_spd = p1.get_effective_stat("speed")
        p2_spd = p2.get_effective_stat("speed")
        speed_diff = p1_spd - p2_spd
        has_priority = p1.has_next_turn_priority

        return {
            "is_active": self.is_active,
            "is_over": self.game.is_over,
            "winner": self.game.winner,
            "turn": self.game.current_turn,
            "max_turns": self.game.max_turns,
            "player": {
                "name": p1.name,
                "hp": round(p1.current_health, 1),
                "max_hp": round(p1.max_health, 1),
                "hp_percent": max(0.0, min(100.0, round((p1.current_health / p1.max_health) * 100.0, 1))),
                "potency": round(p1.get_effective_stat("potency"), 1),
                "defense": round(p1.get_effective_stat("defense"), 1),
                "luck": round(p1.get_effective_stat("luck"), 1),
                "speed": round(p1_spd, 1),
                "rune_pool": list(p1.rune_pool),
                "buffs": copy.deepcopy(p1.buffs),
                "debuffs": copy.deepcopy(p1.debuffs),
                "has_priority": p1.has_next_turn_priority,
                "damage_dealt": round(p1.damage_dealt, 1),
                "damage_taken": round(p1.damage_taken, 1),
                "healing_done": round(p1.healing_done, 1),
            },
            "opponent": {
                "name": p2.name,
                "archetype": self.ai_bot_info.get("archetype", "Arcane AI"),
                "affinity": self.ai_bot_info.get("affinity_class", "Sorcery"),
                "hp": round(p2.current_health, 1),
                "max_hp": round(p2.max_health, 1),
                "hp_percent": max(0.0, min(100.0, round((p2.current_health / p2.max_health) * 100.0, 1))),
                "potency": round(p2.get_effective_stat("potency"), 1),
                "defense": round(p2.get_effective_stat("defense"), 1),
                "luck": round(p2.get_effective_stat("luck"), 1),
                "speed": round(p2_spd, 1),
                "rune_count": len(p2.rune_pool),
                "buffs": copy.deepcopy(p2.buffs),
                "debuffs": copy.deepcopy(p2.debuffs),
                "has_priority": p2.has_next_turn_priority,
                "damage_dealt": round(p2.damage_dealt, 1),
                "damage_taken": round(p2.damage_taken, 1),
                "healing_done": round(p2.healing_done, 1),
            },
            "environment": {
                "weather": env.weather.value,
                "weather_turns": env.weather_turns_active,
                "location": env.location.value,
                "location_turns": env.location_turns_active,
                "seedling_active": env.seedling_active,
            },
            "initiative": {
                "player_faster": (speed_diff > 0) or has_priority,
                "has_priority": has_priority,
                "speed_diff": round(speed_diff, 1),
            },
            "castable_spells": castable_list,
            "combat_logs": self.turn_events_history[-8:],
        }

BATTLE = BattleManager()

# =============================================================================
# EMBEDDED MOBILE WEB UI
# =============================================================================

HTML_APP = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<title>Project Sorcery - Mobile Arena</title>
<style>
:root {
  --bg-deep: #07090e;
  --bg-card: rgba(18, 24, 38, 0.85);
  --border-glass: rgba(255, 255, 255, 0.08);
  --accent-purple: #9333ea;
  --accent-cyan: #06b6d4;
  --accent-gold: #f59e0b;
  --accent-red: #ef4444;
  --accent-green: #10b981;
  --text-main: #f8fafc;
  --text-dim: #94a3b8;
  --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif;
  --rune-f: #ef4444;
  --rune-w: #0284c7;
  --rune-e: #10b981;
  --rune-l: #eab308;
  --rune-d: #8b5cf6;
}

* { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }

body {
  background: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-family);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  background-image: 
    radial-gradient(circle at 10% 20%, rgba(147, 51, 234, 0.12) 0%, transparent 40%),
    radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.12) 0%, transparent 40%);
}

header {
  padding: 12px 16px;
  background: rgba(11, 15, 25, 0.9);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-glass);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
}

.logo-area { display: flex; align-items: center; gap: 8px; }
.logo-icon { font-size: 22px; filter: drop-shadow(0 0 8px rgba(147, 51, 234, 0.6)); }
.logo-title {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: 1px;
  background: linear-gradient(135deg, #a855f7, #38bdf8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.header-controls { display: flex; gap: 8px; align-items: center; }
.btn-icon {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-glass);
  color: var(--text-main);
  border-radius: 8px;
  padding: 6px 10px;
  font-size: 13px;
  cursor: pointer;
}
.btn-icon:hover { background: rgba(255, 255, 255, 0.1); }

main { flex: 1; padding: 14px; max-width: 600px; margin: 0 auto; width: 100%; }

.card {
  background: var(--bg-card);
  border: 1px solid var(--border-glass);
  border-radius: 16px;
  padding: 16px;
  margin-bottom: 14px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(12px);
}

.card-title {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.5px;
  color: var(--text-dim);
  text-transform: uppercase;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.stat-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.stat-label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 600;
  min-width: 110px;
}

.stat-val-badge {
  background: rgba(255, 255, 255, 0.08);
  padding: 2px 8px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: bold;
  color: var(--accent-cyan);
}

.slider-container { flex: 1; margin: 0 12px; }
input[type=range] { width: 100%; accent-color: var(--accent-purple); height: 6px; }

.presets-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin-top: 10px;
}

.btn-preset {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-glass);
  color: var(--text-main);
  padding: 8px 10px;
  border-radius: 10px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  text-align: left;
}

select, input[type=text] {
  width: 100%;
  padding: 10px 12px;
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid var(--border-glass);
  border-radius: 10px;
  color: var(--text-main);
  font-size: 14px;
  outline: none;
  margin-bottom: 10px;
}

select:focus, input[type=text]:focus { border-color: var(--accent-purple); }

.btn-primary {
  width: 100%;
  padding: 14px;
  background: linear-gradient(135deg, #7c3aed, #0284c7);
  border: none;
  border-radius: 12px;
  color: #fff;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(124, 58, 237, 0.4);
}

.btn-primary:active { transform: scale(0.98); }

.arena-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(0, 0, 0, 0.3);
  padding: 8px 12px;
  border-radius: 10px;
  margin-bottom: 12px;
  font-size: 12px;
}

.env-pill {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(255, 255, 255, 0.06);
  padding: 4px 8px;
  border-radius: 6px;
  font-weight: 600;
}

.duelists-container { display: flex; flex-direction: column; gap: 10px; margin-bottom: 12px; }

.duelist-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-glass);
  border-radius: 12px;
  padding: 12px;
}

.duelist-card.player { border-left: 4px solid var(--accent-cyan); }
.duelist-card.opponent { border-left: 4px solid var(--accent-red); }

.duelist-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}

.duelist-name { font-size: 15px; font-weight: 700; }
.duelist-archetype {
  font-size: 11px;
  color: var(--text-dim);
  background: rgba(255, 255, 255, 0.05);
  padding: 2px 6px;
  border-radius: 4px;
}

.hp-bar-bg {
  width: 100%;
  height: 14px;
  background: rgba(0, 0, 0, 0.5);
  border-radius: 7px;
  overflow: hidden;
  position: relative;
  margin-bottom: 6px;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.hp-bar-fill {
  height: 100%;
  border-radius: 7px;
  transition: width 0.4s ease-out;
}

.hp-bar-fill.high { background: linear-gradient(90deg, #10b981, #34d399); }
.hp-bar-fill.mid { background: linear-gradient(90deg, #f59e0b, #fbbf24); }
.hp-bar-fill.low { background: linear-gradient(90deg, #ef4444, #f87171); }

.hp-text {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 800;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.9);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 4px;
  font-size: 11px;
  margin-top: 6px;
}

.stat-pill {
  background: rgba(0, 0, 0, 0.25);
  padding: 3px 4px;
  border-radius: 4px;
  text-align: center;
  color: var(--text-dim);
}
.stat-pill b { color: var(--text-main); }

.status-chips { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 6px; }
.status-chip {
  font-size: 10px;
  padding: 2px 6px;
  border-radius: 4px;
  background: rgba(239, 68, 68, 0.2);
  border: 1px solid rgba(239, 68, 68, 0.4);
  color: #fca5a5;
  font-weight: 600;
}
.status-chip.buff {
  background: rgba(16, 185, 129, 0.2);
  border-color: rgba(16, 185, 129, 0.4);
  color: #6ee7b7;
}

.rune-pool-area {
  display: flex;
  gap: 8px;
  align-items: center;
  justify-content: center;
  padding: 10px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 12px;
  margin-bottom: 12px;
}

.rune-badge {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 15px;
  cursor: pointer;
  border: 2px solid transparent;
  user-select: none;
}
.rune-badge:active { transform: scale(0.92); }

.rune-F { background: rgba(239, 68, 68, 0.2); border-color: var(--rune-f); color: #fca5a5; }
.rune-W { background: rgba(2, 132, 199, 0.2); border-color: var(--rune-w); color: #7dd3fc; }
.rune-E { background: rgba(16, 185, 129, 0.2); border-color: var(--rune-e); color: #6ee7b7; }
.rune-L { background: rgba(234, 179, 8, 0.2); border-color: var(--rune-l); color: #fde047; }
.rune-D { background: rgba(139, 92, 246, 0.2); border-color: var(--rune-d); color: #c4b5fd; }

.rune-sub { font-size: 8px; font-weight: normal; margin-top: -2px; opacity: 0.8; }

.weaver-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-glass);
  padding: 8px 12px;
  border-radius: 10px;
  margin-bottom: 12px;
}

.weaver-slots { display: flex; gap: 6px; }
.weaver-slot {
  width: 34px;
  height: 34px;
  border-radius: 6px;
  border: 1px dashed rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 14px;
  background: rgba(0, 0, 0, 0.2);
}

.btn-small {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-glass);
  color: var(--text-main);
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 12px;
  cursor: pointer;
  font-weight: 600;
}
.btn-cast-weaver {
  background: linear-gradient(135deg, #7c3aed, #06b6d4);
  border: none;
  color: white;
}

.spell-filter-bar {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding-bottom: 6px;
  margin-bottom: 8px;
}

.spell-filter-chip {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-glass);
  color: var(--text-dim);
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 11px;
  white-space: nowrap;
  cursor: pointer;
}
.spell-filter-chip.active {
  background: var(--accent-purple);
  color: white;
  border-color: var(--accent-purple);
}

.spell-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: 280px;
  overflow-y: auto;
  padding-right: 4px;
}

.spell-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-glass);
  border-radius: 10px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.spell-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.spell-recipe-badges { display: flex; gap: 3px; }
.spell-recipe-letter {
  font-size: 11px;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 4px;
}

.spell-class-tag {
  font-size: 10px;
  padding: 2px 6px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.07);
  color: var(--text-dim);
}

.spell-desc { font-size: 12px; color: #cbd5e1; line-height: 1.35; }

.spell-condition-badge {
  font-size: 10px;
  padding: 2px 6px;
  border-radius: 4px;
  background: rgba(234, 179, 8, 0.15);
  color: #fde047;
  border: 1px solid rgba(234, 179, 8, 0.3);
  display: inline-flex;
  align-items: center;
  gap: 4px;
  width: fit-content;
}

.spell-condition-badge.active {
  background: rgba(16, 185, 129, 0.2);
  color: #6ee7b7;
  border-color: rgba(16, 185, 129, 0.4);
  font-weight: 700;
}

.spell-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 2px;
}

.spell-formula { font-size: 10px; color: var(--text-dim); }

.btn-cast {
  background: linear-gradient(135deg, #9333ea, #0284c7);
  border: none;
  color: white;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
}

.btn-cast:active { transform: scale(0.95); }

.log-modal {
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(8px);
  z-index: 200;
  padding: 20px;
  align-items: center;
  justify-content: center;
}

.log-box {
  background: #111827;
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 16px;
  max-width: 480px;
  width: 100%;
  max-height: 80vh;
  overflow-y: auto;
  padding: 18px;
}

.log-title {
  font-size: 16px;
  font-weight: 800;
  margin-bottom: 12px;
  color: var(--accent-cyan);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.turn-event-item {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  padding: 8px 10px;
  margin-bottom: 6px;
  font-size: 12px;
  line-height: 1.4;
  border-left: 3px solid var(--accent-purple);
}

.turn-event-item.dmg { border-left-color: var(--accent-red); }
.turn-event-item.dot { border-left-color: #f97316; }
.turn-event-item.buff { border-left-color: var(--accent-green); }

.end-banner {
  text-align: center;
  padding: 16px;
  border-radius: 12px;
  margin-bottom: 14px;
}

.end-banner.win {
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid var(--accent-green);
}

.end-banner.loss {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid var(--accent-red);
}

.end-title { font-size: 20px; font-weight: 900; letter-spacing: 1px; }
</style>
</head>
<body>

<header>
  <div class="logo-area">
    <span class="logo-icon">🔮</span>
    <span class="logo-title">PROJECT SORCERY</span>
  </div>
  <div class="header-controls">
    <button class="btn-icon" id="btn-sound" onclick="toggleSound()">🔊 Sound: ON</button>
    <button class="btn-icon" id="btn-view-toggle" onclick="toggleSetupView()">⚙️ Stats</button>
  </div>
</header>

<main>
  <!-- STATS & SETUP SCREEN -->
  <section id="setup-screen" class="card">
    <div class="card-title">
      <span>Wizard Attribute Matrix</span>
      <span class="stat-val-badge">Points: <span id="pts-count">Free Allocation</span></span>
    </div>

    <input type="text" id="wizard-name" value="Archmage Christopher" placeholder="Enter Wizard Name">

    <div class="stat-row">
      <div class="stat-label">❤️ Health (HP)</div>
      <div class="slider-container">
        <input type="range" id="stat-hp" min="500" max="2000" step="50" value="1000" oninput="updateStatDisplays()">
      </div>
      <span class="stat-val-badge" id="val-hp">1000</span>
    </div>

    <div class="stat-row">
      <div class="stat-label">🔥 Potency</div>
      <div class="slider-container">
        <input type="range" id="stat-potency" min="50" max="200" step="5" value="100" oninput="updateStatDisplays()">
      </div>
      <span class="stat-val-badge" id="val-potency">100</span>
    </div>

    <div class="stat-row">
      <div class="stat-label">🛡️ Defense</div>
      <div class="slider-container">
        <input type="range" id="stat-defense" min="50" max="200" step="5" value="100" oninput="updateStatDisplays()">
      </div>
      <span class="stat-val-badge" id="val-defense">100</span>
    </div>

    <div class="stat-row">
      <div class="stat-label">🎲 Luck</div>
      <div class="slider-container">
        <input type="range" id="stat-luck" min="50" max="200" step="5" value="100" oninput="updateStatDisplays()">
      </div>
      <span class="stat-val-badge" id="val-luck">100</span>
    </div>

    <div class="stat-row">
      <div class="stat-label">⚡ Speed</div>
      <div class="slider-container">
        <input type="range" id="stat-speed" min="50" max="200" step="5" value="100" oninput="updateStatDisplays()">
      </div>
      <span class="stat-val-badge" id="val-speed">100</span>
    </div>

    <div class="card-title" style="margin-top: 14px;">Quick Archetypes</div>
    <div class="presets-container">
      <button class="btn-preset" onclick="setPreset(1000, 100, 100, 100, 100)">⚖️ Balanced (100 all)</button>
      <button class="btn-preset" onclick="setPreset(800, 150, 70, 90, 130)">🔥 Pyromancer Burst</button>
      <button class="btn-preset" onclick="setPreset(1400, 80, 140, 80, 80)">🛡️ Titan Juggernaut</button>
      <button class="btn-preset" onclick="setPreset(900, 110, 80, 150, 120)">🎲 Chaos Gambler</button>
    </div>

    <div class="card-title" style="margin-top: 16px;">AI Opponent (DQN Bot)</div>
    <select id="select-bot"></select>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
      <div>
        <label style="font-size: 11px; color: var(--text-dim);">Weather</label>
        <select id="select-weather">
          <option value="Random">🎲 Random Weather</option>
          <option value="Sunny">☀️ Sunny</option>
          <option value="Raining">🌧️ Raining</option>
          <option value="Blizzard">❄️ Blizzard</option>
          <option value="Darkness">🌑 Darkness</option>
          <option value="Storming">⛈️ Storming</option>
          <option value="Blood Rain">🩸 Blood Rain</option>
          <option value="Snowing">🌨️ Snowing</option>
          <option value="Windy">💨 Windy</option>
          <option value="Sandstorm">🏜️ Sandstorm</option>
          <option value="Clear">✨ Clear</option>
        </select>
      </div>
      <div>
        <label style="font-size: 11px; color: var(--text-dim);">Location</label>
        <select id="select-location">
          <option value="Random">🎲 Random Location</option>
          <option value="Jungle">🌴 Jungle</option>
          <option value="Enchanted Forest">🌲 Enchanted Forest</option>
          <option value="Tundra">🏔️ Tundra</option>
          <option value="Swamp">🌿 Swamp</option>
          <option value="Graveyard">🪦 Graveyard</option>
          <option value="Space">🌌 Space</option>
        </select>
      </div>
    </div>

    <button class="btn-primary" style="margin-top: 10px;" onclick="startDuel()">⚔️ ENTER ARENA & DUEL AI</button>
  </section>

  <!-- BATTLE SCREEN -->
  <section id="battle-screen" style="display: none;">
    <div id="end-banner" class="end-banner" style="display: none;">
      <div id="end-title" class="end-title">VICTORY</div>
      <div id="end-sub" style="font-size: 13px; color: var(--text-dim); margin-top: 4px;">You have triumphed in arcane combat!</div>
      <button class="btn-small" style="margin-top: 10px; background: var(--accent-purple);" onclick="rematch()">⚔️ Rematch</button>
      <button class="btn-small" style="margin-top: 10px; margin-left: 6px;" onclick="toggleSetupView()">⚙️ Adjust Stats</button>
    </div>

    <div class="arena-header">
      <span style="font-weight: 800; color: var(--accent-cyan);" id="battle-turn">TURN 1 / 50</span>
      <div style="display: flex; gap: 6px;">
        <span class="env-pill" id="env-weather">☀️ Sunny</span>
        <span class="env-pill" id="env-location">🌴 Jungle</span>
      </div>
      <span class="env-pill" id="initiative-badge" style="color: var(--accent-gold);">⚡ Initiative</span>
    </div>

    <div class="duelists-container">
      <!-- Player -->
      <div class="duelist-card player">
        <div class="duelist-top">
          <span class="duelist-name">🧙‍♂️ <span id="p1-name">Player</span></span>
          <span class="duelist-archetype" id="p1-priority-badge" style="display: none; color: var(--accent-gold);">Priority</span>
        </div>
        <div class="hp-bar-bg">
          <div class="hp-bar-fill high" id="p1-hp-fill" style="width: 100%;"></div>
          <div class="hp-text" id="p1-hp-text">1000 / 1000 HP</div>
        </div>
        <div class="stats-grid">
          <div class="stat-pill">Pot: <b id="p1-pot">100</b></div>
          <div class="stat-pill">Def: <b id="p1-def">100</b></div>
          <div class="stat-pill">Lck: <b id="p1-lck">100</b></div>
          <div class="stat-pill">Spd: <b id="p1-spd">100</b></div>
        </div>
        <div class="status-chips" id="p1-statuses"></div>
      </div>

      <!-- Opponent -->
      <div class="duelist-card opponent">
        <div class="duelist-top">
          <span class="duelist-name">🤖 <span id="p2-name">AI Bot</span></span>
          <span class="duelist-archetype" id="p2-archetype">Pyromancer</span>
        </div>
        <div class="hp-bar-bg">
          <div class="hp-bar-fill high" id="p2-hp-fill" style="width: 100%;"></div>
          <div class="hp-text" id="p2-hp-text">1000 / 1000 HP</div>
        </div>
        <div class="stats-grid">
          <div class="stat-pill">Pot: <b id="p2-pot">100</b></div>
          <div class="stat-pill">Def: <b id="p2-def">100</b></div>
          <div class="stat-pill">Lck: <b id="p2-lck">100</b></div>
          <div class="stat-pill">Spd: <b id="p2-spd">100</b></div>
        </div>
        <div class="status-chips" id="p2-statuses"></div>
      </div>
    </div>

    <!-- Rune Pool -->
    <div class="card" style="padding: 12px; margin-bottom: 10px;">
      <div class="card-title" style="margin-bottom: 8px;">
        <span>Active Rune Pool</span>
        <span style="font-size: 11px; text-transform: none; color: var(--text-dim);" id="rune-count-text">3 Runes</span>
      </div>
      <div class="rune-pool-area" id="rune-pool-container"></div>

      <div class="weaver-bar">
        <div class="weaver-slots">
          <div class="weaver-slot" id="slot-0">-</div>
          <div class="weaver-slot" id="slot-1">-</div>
          <div class="weaver-slot" id="slot-2">-</div>
        </div>
        <div style="display: flex; gap: 6px;">
          <button class="btn-small" onclick="clearWeaver()">Clear</button>
          <button class="btn-small btn-cast-weaver" onclick="castWeaver()">Cast Recipe</button>
        </div>
      </div>
    </div>

    <!-- Craftable Spells -->
    <div class="card" style="padding: 12px;">
      <div class="card-title" style="margin-bottom: 8px;">
        <span>Craftable Spells</span>
        <span id="castable-count-badge" class="stat-val-badge">0 available</span>
      </div>

      <div class="spell-filter-bar" id="filter-bar">
        <button class="spell-filter-chip active" onclick="setSpellFilter('All', this)">All</button>
        <button class="spell-filter-chip" onclick="setSpellFilter('Direct Damage', this)">Direct Damage</button>
        <button class="spell-filter-chip" onclick="setSpellFilter('Conditional Strike', this)">Combos</button>
        <button class="spell-filter-chip" onclick="setSpellFilter('Debuff / Control', this)">Control</button>
        <button class="spell-filter-chip" onclick="setSpellFilter('Buff / Sustain', this)">Buffs</button>
        <button class="spell-filter-chip" onclick="setSpellFilter('Setup - Weather', this)">Weather</button>
      </div>

      <div class="spell-list" id="spell-list-container"></div>
    </div>

    <button class="btn-small" style="width: 100%; margin-top: 10px; padding: 10px;" onclick="openLogModal()">📜 View Combat Log & Breakdown</button>
  </section>
</main>

<!-- COMBAT LOG MODAL -->
<div class="log-modal" id="log-modal" onclick="closeLogModal(event)">
  <div class="log-box" onclick="event.stopPropagation()">
    <div class="log-title">
      <span>Turn Resolution Log</span>
      <button class="btn-small" onclick="document.getElementById('log-modal').style.display='none'">✕ Close</button>
    </div>
    <div id="modal-log-entries"></div>
  </div>
</div>

<script>
let audioCtx = null;
let soundEnabled = true;

function initAudio() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
}

function playSound(type) {
  if (!soundEnabled) return;
  try {
    initAudio();
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const now = audioCtx.currentTime;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);

    if (type === 'cast') {
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(220, now);
      osc.frequency.exponentialRampToValueAtTime(880, now + 0.18);
      gain.gain.setValueAtTime(0.3, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
      osc.start(now);
      osc.stop(now + 0.22);
    } else if (type === 'hit') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(140, now);
      osc.frequency.linearRampToValueAtTime(40, now + 0.25);
      gain.gain.setValueAtTime(0.4, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
      osc.start(now);
      osc.stop(now + 0.26);
    } else if (type === 'win') {
      [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
        const o = audioCtx.createOscillator();
        const g = audioCtx.createGain();
        o.connect(g); g.connect(audioCtx.destination);
        o.frequency.value = freq;
        g.gain.setValueAtTime(0.2, now + i * 0.12);
        g.gain.exponentialRampToValueAtTime(0.001, now + i * 0.12 + 0.35);
        o.start(now + i * 0.12);
        o.stop(now + i * 0.12 + 0.4);
      });
    }
  } catch(e) {}
}

function toggleSound() {
  soundEnabled = !soundEnabled;
  document.getElementById('btn-sound').innerText = soundEnabled ? '🔊 Sound: ON' : '🔈 Sound: OFF';
}

let appConfig = null;
let currentGameState = null;
let activeFilter = 'All';
let weaverSlots = [];

async function fetchInit() {
  const res = await fetch('/api/init');
  appConfig = await res.json();
  populateBots(appConfig.bots);
}

function populateBots(bots) {
  const sel = document.getElementById('select-bot');
  sel.innerHTML = '';
  bots.forEach(b => {
    const opt = document.createElement('option');
    opt.value = b.bot_id;
    opt.innerText = `${b.name} (${b.archetype} • ${b.affinity_class})`;
    sel.appendChild(opt);
  });
}

function updateStatDisplays() {
  document.getElementById('val-hp').innerText = document.getElementById('stat-hp').value;
  document.getElementById('val-potency').innerText = document.getElementById('stat-potency').value;
  document.getElementById('val-defense').innerText = document.getElementById('stat-defense').value;
  document.getElementById('val-luck').innerText = document.getElementById('stat-luck').value;
  document.getElementById('val-speed').innerText = document.getElementById('stat-speed').value;
}

function setPreset(hp, pot, def, lck, spd) {
  document.getElementById('stat-hp').value = hp;
  document.getElementById('stat-potency').value = pot;
  document.getElementById('stat-defense').value = def;
  document.getElementById('stat-luck').value = lck;
  document.getElementById('stat-speed').value = spd;
  updateStatDisplays();
}

function toggleSetupView() {
  const setup = document.getElementById('setup-screen');
  const battle = document.getElementById('battle-screen');
  if (setup.style.display === 'none') {
    setup.style.display = 'block';
    battle.style.display = 'none';
  } else {
    if (currentGameState && currentGameState.is_active) {
      setup.style.display = 'none';
      battle.style.display = 'block';
    }
  }
}

async function startDuel() {
  initAudio();
  const name = document.getElementById('wizard-name').value;
  const hp = document.getElementById('stat-hp').value;
  const pot = document.getElementById('stat-potency').value;
  const def = document.getElementById('stat-defense').value;
  const lck = document.getElementById('stat-luck').value;
  const spd = document.getElementById('stat-speed').value;
  const botId = document.getElementById('select-bot').value;
  const weather = document.getElementById('select-weather').value;
  const location = document.getElementById('select-location').value;

  const payload = {
    name, hp, potency: pot, defense: def, luck: lck, speed: spd,
    bot_id: botId, weather, location
  };

  const res = await fetch('/api/start', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  currentGameState = await res.json();
  renderGameState(currentGameState);

  document.getElementById('setup-screen').style.display = 'none';
  document.getElementById('battle-screen').style.display = 'block';
  clearWeaver();
  playSound('cast');
}

function rematch() {
  startDuel();
}

function renderGameState(state) {
  if (!state || (!state.is_active && !state.is_over)) return;
  currentGameState = state;

  document.getElementById('battle-turn').innerText = `TURN ${state.turn} / ${state.max_turns}`;
  document.getElementById('env-weather').innerText = `☀️ ${state.environment.weather} (${state.environment.weather_turns}t)`;
  document.getElementById('env-location').innerText = `📍 ${state.environment.location}`;

  const initBadge = document.getElementById('initiative-badge');
  if (state.initiative.player_faster) {
    initBadge.innerText = '⚡ You Strike First';
    initBadge.style.color = 'var(--accent-green)';
  } else {
    initBadge.innerText = '⚠️ AI Strikes First';
    initBadge.style.color = 'var(--accent-red)';
  }

  const p1 = state.player;
  document.getElementById('p1-name').innerText = p1.name;
  document.getElementById('p1-hp-text').innerText = `${p1.hp} / ${p1.max_hp} HP`;
  const p1Fill = document.getElementById('p1-hp-fill');
  p1Fill.style.width = `${p1.hp_percent}%`;
  p1Fill.className = `hp-bar-fill ${p1.hp_percent > 50 ? 'high' : p1.hp_percent > 25 ? 'mid' : 'low'}`;
  document.getElementById('p1-pot').innerText = p1.potency;
  document.getElementById('p1-def').innerText = p1.defense;
  document.getElementById('p1-lck').innerText = p1.luck;
  document.getElementById('p1-spd').innerText = p1.speed;

  renderStatusChips('p1-statuses', p1.buffs, p1.debuffs);

  const p2 = state.opponent;
  document.getElementById('p2-name').innerText = p2.name;
  document.getElementById('p2-archetype').innerText = `${p2.archetype} • ${p2.affinity}`;
  document.getElementById('p2-hp-text').innerText = `${p2.hp} / ${p2.max_hp} HP`;
  const p2Fill = document.getElementById('p2-hp-fill');
  p2Fill.style.width = `${p2.hp_percent}%`;
  p2Fill.className = `hp-bar-fill ${p2.hp_percent > 50 ? 'high' : p2.hp_percent > 25 ? 'mid' : 'low'}`;
  document.getElementById('p2-pot').innerText = p2.potency;
  document.getElementById('p2-def').innerText = p2.defense;
  document.getElementById('p2-lck').innerText = p2.luck;
  document.getElementById('p2-spd').innerText = p2.speed;

  renderStatusChips('p2-statuses', p2.buffs, p2.debuffs);

  renderRunePool(p1.rune_pool);
  renderSpellList(state.castable_spells);

  const endBanner = document.getElementById('end-banner');
  if (state.is_over) {
    endBanner.style.display = 'block';
    if (state.winner === p1.name) {
      endBanner.className = 'end-banner win';
      document.getElementById('end-title').innerText = '🏆 VICTORY!';
      document.getElementById('end-sub').innerText = `You defeated ${p2.name}! Damage dealt: ${p1.damage_dealt}`;
      playSound('win');
    } else if (state.winner === 'Draw') {
      endBanner.className = 'end-banner';
      document.getElementById('end-title').innerText = '🤝 DRAW MATCH';
      document.getElementById('end-sub').innerText = 'Both wizards collapsed in arcane exhaustion!';
    } else {
      endBanner.className = 'end-banner loss';
      document.getElementById('end-title').innerText = '💀 DEFEAT';
      document.getElementById('end-sub').innerText = `${p2.name} overcame your defenses!`;
      playSound('hit');
    }
  } else {
    endBanner.style.display = 'none';
  }
}

function renderStatusChips(containerId, buffs, debuffs) {
  const container = document.getElementById(containerId);
  container.innerHTML = '';
  for (const [buff, turns] of Object.entries(buffs || {})) {
    const chip = document.createElement('span');
    chip.className = 'status-chip buff';
    chip.innerText = `🛡️ ${buff} (${turns})`;
    container.appendChild(chip);
  }
  for (const [debuff, turns] of Object.entries(debuffs || {})) {
    const chip = document.createElement('span');
    chip.className = 'status-chip';
    chip.innerText = `🔥 ${debuff} (${turns})`;
    container.appendChild(chip);
  }
}

function renderRunePool(pool) {
  const container = document.getElementById('rune-pool-container');
  container.innerHTML = '';
  document.getElementById('rune-count-text').innerText = `${pool.length} Runes Available`;

  const counts = {};
  pool.forEach(r => counts[r] = (counts[r] || 0) + 1);

  ['F', 'W', 'E', 'L', 'D'].forEach(r => {
    const count = counts[r] || 0;
    if (count > 0) {
      const b = document.createElement('div');
      b.className = `rune-badge rune-${r}`;
      b.innerHTML = `<div>${r}</div><div class="rune-sub">${count}x</div>`;
      b.onclick = () => addRuneToWeaver(r);
      container.appendChild(b);
    }
  });
}

function addRuneToWeaver(rune) {
  if (weaverSlots.length < 3) {
    const curCount = weaverSlots.filter(r => r === rune).length;
    const pool = currentGameState.player.rune_pool;
    const poolCount = pool.filter(r => r === rune).length;
    if (curCount < poolCount) {
      weaverSlots.push(rune);
      updateWeaverSlots();
      playSound('cast');
    }
  }
}

function clearWeaver() {
  weaverSlots = [];
  updateWeaverSlots();
}

function updateWeaverSlots() {
  document.getElementById('slot-0').innerText = weaverSlots[0] || '-';
  document.getElementById('slot-1').innerText = weaverSlots[1] || '-';
  document.getElementById('slot-2').innerText = weaverSlots[2] || '-';
}

function castWeaver() {
  if (weaverSlots.length === 3) {
    const recipe = weaverSlots.join('');
    castSpell(recipe);
    clearWeaver();
  }
}

function setSpellFilter(filter, el) {
  activeFilter = filter;
  document.querySelectorAll('.spell-filter-chip').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
  if (currentGameState) {
    renderSpellList(currentGameState.castable_spells);
  }
}

function renderSpellList(spells) {
  const container = document.getElementById('spell-list-container');
  container.innerHTML = '';
  document.getElementById('castable-count-badge').innerText = `${spells.length} craftable`;

  const filtered = activeFilter === 'All' 
    ? spells 
    : spells.filter(s => s.category.toLowerCase().includes(activeFilter.toLowerCase()));

  filtered.forEach(s => {
    const card = document.createElement('div');
    card.className = 'spell-card';

    const rBadges = s.recipe.split('').map(r => 
      `<span class="spell-recipe-letter rune-${r}">${r}</span>`
    ).join('');

    const condHtml = s.condition_required && s.condition_required !== 'None'
      ? `<div class="spell-condition-badge ${s.condition_met ? 'active' : ''}">
          ${s.condition_met ? '✨ ' + s.condition_text : '⚠️ ' + s.condition_required}
        </div>`
      : '';

    card.innerHTML = `
      <div class="spell-card-header">
        <div class="spell-recipe-badges">${rBadges}</div>
        <span class="spell-class-tag">${s.class} • ${s.category}</span>
      </div>
      <div class="spell-desc">${s.description}</div>
      ${condHtml}
      <div class="spell-bottom">
        <span class="spell-formula">Base: ${s.b} | Pot: ${s.max_potential}</span>
        <button class="btn-cast" onclick="castSpell('${s.recipe}')">CAST</button>
      </div>
    `;
    container.appendChild(card);
  });
}

async function castSpell(recipe) {
  if (!currentGameState || !currentGameState.is_active) return;
  playSound('cast');

  const res = await fetch('/api/cast', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ recipe })
  });
  const data = await res.json();
  if (data.error) {
    alert(data.error);
    return;
  }
  renderGameState(data);
  playSound('hit');

  if (data.last_turn_log) {
    renderTurnLogModal(data.last_turn_log);
  }
}

function renderTurnLogModal(log) {
  const container = document.getElementById('modal-log-entries');
  container.innerHTML = '';
  (log.events || []).forEach(ev => {
    const item = document.createElement('div');
    if (ev.damage_dealt && ev.damage_dealt > 0) {
      item.className = 'turn-event-item dmg';
      item.innerHTML = `💥 <b>${ev.caster}</b> cast <b>${ev.recipe}</b> dealing <b>${Math.round(ev.damage_dealt)} damage</b> to ${ev.target}!`;
    } else if (ev.effect) {
      item.className = 'turn-event-item dot';
      item.innerHTML = `⏳ <b>${ev.actor}</b> suffered ${Math.round(ev.damage || 0)} damage from <b>${ev.effect}</b>!`;
    } else {
      item.className = 'turn-event-item buff';
      item.innerHTML = `✨ <b>${ev.caster || ev.actor}</b> cast <b>${ev.recipe || ev.action}</b> (${(ev.effects_applied || []).join(', ')})`;
    }
    container.appendChild(item);
  });
}

function openLogModal() {
  const modal = document.getElementById('log-modal');
  modal.style.display = 'flex';
  if (currentGameState && currentGameState.combat_logs) {
    const container = document.getElementById('modal-log-entries');
    container.innerHTML = '';
    currentGameState.combat_logs.slice().reverse().forEach(log => {
      const turnHdr = document.createElement('div');
      turnHdr.style = 'font-weight: 800; color: var(--accent-cyan); margin-top: 10px; margin-bottom: 4px;';
      turnHdr.innerText = `TURN ${log.turn} • ${log.weather} in ${log.location}`;
      container.appendChild(turnHdr);
      (log.events || []).forEach(ev => {
        const item = document.createElement('div');
        item.className = 'turn-event-item';
        if (ev.damage_dealt) {
          item.innerHTML = `💥 <b>${ev.caster}</b> cast <b>${ev.recipe}</b>: ${Math.round(ev.damage_dealt)} damage to ${ev.target}`;
        } else if (ev.effect) {
          item.innerHTML = `⏳ <b>${ev.actor}</b>: ${Math.round(ev.damage || 0)} from ${ev.effect}`;
        } else {
          item.innerHTML = `✨ <b>${ev.caster || ev.actor}</b>: ${ev.recipe || ev.action} ${(ev.effects_applied || []).join(', ')}`;
        }
        container.appendChild(item);
      });
    });
  }
}

function closeLogModal(e) {
  document.getElementById('log-modal').style.display = 'none';
}

fetchInit();
updateStatDisplays();
</script>
</body>
</html>
"""

# =============================================================================
# HTTP REQUEST HANDLER & SERVER
# =============================================================================

class ArenaRequestHandler(BaseHTTPRequestHandler):
    """Serves the SPA frontend and JSON API endpoints."""
    def log_message(self, format, *args):
        pass

    def send_json(self, data: Any, status: int = 200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in ["/", "/index.html"]:
            body = HTML_APP.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif parsed.path == "/api/init":
            self.send_json({
                "bots": [
                    {
                        "bot_id": b.get("bot_id", f"bot_{i:03d}"),
                        "name": b.get("name", f"Bot {i}"),
                        "archetype": b.get("archetype", "Sorcerer"),
                        "affinity_class": b.get("affinity_class", "Arcane"),
                    }
                    for i, b in enumerate(ALL_BOTS_DATA)
                ],
                "weathers": [w.value for w in Weather] if Weather else [],
                "locations": [loc.value for loc in Location] if Location else [],
            })
        elif parsed.path == "/api/state":
            self.send_json(BATTLE.get_ui_state())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        content_len = int(self.headers.get("Content-Length", 0))
        post_body = self.rfile.read(content_len) if content_len > 0 else b"{}"
        try:
            req_data = json.loads(post_body.decode("utf-8"))
        except Exception:
            req_data = {}

        if parsed.path == "/api/start":
            state = BATTLE.start_game(
                player_name=req_data.get("name", "Archmage"),
                hp=float(req_data.get("hp", 1000)),
                potency=float(req_data.get("potency", 100)),
                defense=float(req_data.get("defense", 100)),
                luck=float(req_data.get("luck", 100)),
                speed=float(req_data.get("speed", 100)),
                bot_id=req_data.get("bot_id", "bot_001"),
                weather_name=req_data.get("weather", "Random"),
                location_name=req_data.get("location", "Random"),
            )
            self.send_json(state)
        elif parsed.path == "/api/cast":
            recipe = req_data.get("recipe", "")
            state = BATTLE.cast_turn(recipe)
            self.send_json(state)
        elif parsed.path == "/api/reset":
            state = BATTLE.get_ui_state()
            self.send_json(state)
        else:
            self.send_response(404)
            self.end_headers()

def find_available_port(start_port: int = 8080, max_attempts: int = 20) -> int:
    """Finds an unused local TCP port."""
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return start_port

def run_web_server(port: int = 8080, host: str = "127.0.0.1", open_browser: bool = True):
    """Starts the touch-friendly mobile Web UI server."""
    actual_port = find_available_port(port)
    server_address = (host, actual_port)
    httpd = HTTPServer(server_address, ArenaRequestHandler)
    url = f"http://{host}:{actual_port}"

    print("=" * 64)
    print("🔮 PROJECT SORCERY - MOBILE ARENA UI")
    print("=" * 64)
    print(f"Server active at: {url}")
    print("Pydroid 3 Mobile Instructions:")
    print(" 1. The mobile browser will launch automatically.")
    print(" 2. If it does not, tap or open this link:")
    print(f"    👉 {url}")
    print(" 3. Set your custom stats and enter the arena against the DQN AI!")
    print("=" * 64)
    print("Press Ctrl+C to stop the arena server.\n")

    if open_browser:
        def _open():
            time.sleep(0.5)
            try:
                webbrowser.open_new_tab(url)
            except Exception as e:
                print(f"Browser auto-launch notice: {e}")
        t = threading.Thread(target=_open, daemon=True)
        t.start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nArena server shutting down. Farewell, Archmage!")
        httpd.server_close()

# =============================================================================
# OPTIONAL TKINTER GUI FALLBACK
# =============================================================================

def run_tkinter_ui():
    """Optional native desktop/X11 GUI using Tkinter."""
    try:
        import tkinter as tk
        from tkinter import ttk, messagebox
    except ImportError:
        print("Tkinter is not installed in this environment.")
        print("Launching the sleek Web UI instead...")
        run_web_server()
        return

    root = tk.Tk()
    root.title("Project Sorcery - Arena")
    root.geometry("480x700")
    root.configure(bg="#0b0f19")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", background="#0b0f19", foreground="#f8fafc", font=("Helvetica", 11))
    style.configure("TButton", font=("Helvetica", 11, "bold"), padding=6)

    hdr = tk.Label(root, text="🔮 PROJECT SORCERY", font=("Helvetica", 16, "bold"), fg="#38bdf8", bg="#0b0f19")
    hdr.pack(pady=10)

    lbl_info = tk.Label(
        root,
        text="Native Tkinter Arena Launcher\nFor the premier touch-optimized mobile experience,\nrun without --tk to launch the mobile browser UI.",
        fg="#94a3b8",
        bg="#0b0f19"
    )
    lbl_info.pack(pady=5)

    btn_launch_web = tk.Button(
        root,
        text="🚀 Open Mobile Touch UI",
        font=("Helvetica", 12, "bold"),
        bg="#7c3aed",
        fg="#ffffff",
        padx=10,
        pady=8,
        command=lambda: threading.Thread(target=run_web_server, daemon=True).start()
    )
    btn_launch_web.pack(pady=20)

    root.mainloop()

# =============================================================================
# CLI ENTRY POINT
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Project Sorcery Mobile Arena UI")
    parser.add_argument("--port", type=int, default=8080, help="Port to bind the web server (default: 8080)")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host address (default: 127.0.0.1)")
    parser.add_argument("--no-browser", action="store_true", help="Do not automatically open the browser")
    parser.add_argument("--tk", action="store_true", help="Launch native Tkinter GUI window")

    args = parser.parse_args()

    if args.tk:
        run_tkinter_ui()
    else:
        run_web_server(port=args.port, host=args.host, open_browser=not args.no_browser)

if __name__ == "__main__":
    main()
