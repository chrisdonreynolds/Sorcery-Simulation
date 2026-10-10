# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T23:43:40Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 796.2s  
**Total Spells Tuned:** 101 / 125  

## Executive Summary

The automated balancing suite simulated Project Sorcery games, recording granular combat telemetry
over the final 5,000 games to evaluate the stabilized neuroevolutionary meta. Three primary algorithms analyzed
the resulting telemetry:

1. **Conditional Payoff & Setup Engine:** Identified conditional spells where payoffs were under-triggered, widening
   the spread between the unconditional base factor (`b`) and payoff multiplier (`n`) to heavily reward proactive setup.
2. **Group Synergy & Archetype Engine:** Evaluated all 15 spell classes and key synergy loops (e.g., *Frosty* appliers
   vs beneficiaries, *Sunny* weather setups vs payoffs), dampening over-performing archetypes and boosting tempo-loss setups.
3. **Individual Outlier Engine:** Regressed statistical outliers back toward the 50.0% win-rate baseline.

---

## Class Performance Summary

| Class | Casts | Win Rate (Smoothed) | Raw Win Rate | Avg Damage/Cast | Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Poison** | 22,637 | 56.0% | 56.0% | 9.4 | Overtuned ⚠️ |
| **Blood** | 20,642 | 54.4% | 54.4% | 14.0 | Overtuned ⚠️ |
| **Fire** | 10,741 | 52.9% | 52.9% | 13.9 | Balanced ✅ |
| **Plants** | 21,813 | 52.8% | 52.8% | 9.0 | Balanced ✅ |
| **Dark** | 10,144 | 52.3% | 52.3% | 10.7 | Balanced ✅ |
| **Earth** | 10,287 | 51.4% | 51.4% | 20.3 | Balanced ✅ |
| **Light** | 10,917 | 51.2% | 51.2% | 8.5 | Balanced ✅ |
| **Beasts** | 21,987 | 50.3% | 50.3% | 6.7 | Balanced ✅ |
| **Ghostfire** | 21,598 | 50.3% | 50.3% | 15.1 | Balanced ✅ |
| **Cosmic** | 19,442 | 49.6% | 49.6% | 15.9 | Balanced ✅ |
| **Ice** | 22,072 | 47.4% | 47.4% | 11.8 | Balanced ✅ |
| **Water** | 10,748 | 47.2% | 47.2% | 8.4 | Balanced ✅ |
| **Fey** | 20,789 | 47.0% | 47.0% | 10.3 | Balanced ✅ |
| **Wind** | 20,580 | 46.2% | 46.2% | 7.5 | Undertuned ⚠️ |
| **Lightning** | 24,094 | 46.1% | 46.0% | 9.8 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 8,389 (51.2%) | 3,643 (49.8%) | 18.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,816 (49.6%) | 4,831 (53.7%) | 8.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,317 (58.2%) | 5,763 (48.9%) | 11.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,047 (66.4%) | 9,522 (46.3%) | 6.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 16,352 (46.7%) | 4,558 (43.1%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,575 (57.2%) | 6,500 (45.0%) | 2.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,049 (34.7%) | 5,482 (39.7%) | 6.2% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 42.8 -> **41.6** (-2.8%) | - | 42.8 -> **41.6** | Status 'Burning' appliers overtuned on own (WR: 58.2%) |
| `FFE` | Fire | Debuff / Control | 34.0 -> **33.4** (-1.8%) | - | 34.0 -> **33.4** | Individual spell overtuned (WR: 55.1%, Casts: 2596, mult: 0.983) |
| `FFL` | Fire | Debuff / Control | 6.0 -> **5.6** (-6.7%) | - | 6.0 -> **5.6** | Status 'Burning' appliers overtuned on own (WR: 58.2%); Individual spell overtuned (WR: 61.6%, Casts: 2099, mult: 0.958) |
| `FFD` | Fire | Conditional Strike | 4.9 -> **4.2** (-14.3%) | 38.4 -> **49.4** | 193.1 -> **211.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.9% vs 30% floor, Casts: 1995). Increasing spread: b -14.0%, n +28.7% |
| `WWF` | Water | Conditional Strike | 9.8 -> **8.7** (-11.2%) | 30.1 -> **37.2** | 304.8 -> **332.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 16.2% vs 30% floor, Casts: 1875). Increasing spread: b -11.5%, n +23.5% |
| `WWE` | Water | Setup - Weather | 33.4 -> **37.2** (+11.4%) | - | 33.4 -> **37.2** | Weather 'Raining' appliers undertuned (WR: 34.7%, casts: 2049); Individual spell undertuned (WR: 34.7%, Casts: 2049, mult: 1.057) |
| `EEF` | Earth | Conditional Strike | 16.4 -> **14.1** (-14.0%) | 10.1 -> **12.6** | 182.0 -> **191.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.3% vs 30% floor, Casts: 1455). Increasing spread: b -12.3%, n +25.1%; Individual spell overtuned (WR: 55.1%, Casts: 1455, mult: 0.983) |
| `EED` | Earth | Direct Damage | 7.1 -> **7.2** (+1.4%) | - | 7.1 -> **7.2** | Individual spell undertuned (WR: 45.9%, Casts: 2386, mult: 1.013) |
| `LLF` | Light | Conditional Strike | 3.3 -> **3.8** (+15.2%) | 44.4 -> **59.0** | 149.8 -> **228.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.0% vs 30% floor, Casts: 2661). Increasing spread: b -16.0%, n +32.8%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 39.8 -> **40.4** (+1.5%) | - | 39.8 -> **40.4** | Individual spell undertuned (WR: 45.2%, Casts: 2756, mult: 1.016) |
| `LLE` | Light | Setup - Weather | 53.2 -> **61.2** (+15.0%) | - | 53.2 -> **61.2** | Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 24.3 -> **23.3** (-4.1%) | - | 24.3 -> **23.3** | Individual spell overtuned (WR: 61.7%, Casts: 1621, mult: 0.957) |
| `LLD` | Light | Ultimate | 34.9 -> **34.9** (+0.0%) | 16.3 -> **20.9** | 603.8 -> **764.3** | Weather 'Sunny' beneficiaries overtuned (WR: 53.7%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 2063). Shifted tuner focus: protected ultimate base floor at 34.9 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 3.0 -> **2.5** (-16.7%) | 67.9 -> **93.0** | 206.7 -> **235.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1828). Increasing spread: b -18.0%, n +37.0% |
| `DDE` | Dark | Setup - Weather | 54.8 -> **65.5** (+19.5%) | - | 54.8 -> **65.5** | Weather 'Darkness' appliers undertuned (WR: 44.3%, casts: 1792); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 26.5 -> **26.1** (-1.5%) | - | 26.5 -> **26.1** | Individual spell overtuned (WR: 54.1%, Casts: 3141, mult: 0.987) |
| `DDD` | Dark | Debuff / Control | 25.7 -> **25.1** (-2.3%) | - | 25.7 -> **25.1** | Individual spell overtuned (WR: 56.9%, Casts: 1701, mult: 0.976) |
| `FWF` | Ghostfire | Debuff / Control | 30.3 -> **28.2** (-6.9%) | - | 30.3 -> **28.2** | Status 'Burning' appliers overtuned on own (WR: 58.2%); Individual spell overtuned (WR: 61.4%, Casts: 2359, mult: 0.959) |
| `FWE` | Ghostfire | Setup - Location | 67.4 -> **69.8** (+3.6%) | - | 67.4 -> **69.8** | Location 'Graveyard' appliers undertuned (WR: 44.9%, casts: 2226); Individual spell undertuned (WR: 44.9%, Casts: 2226, mult: 1.017) |
| `FWD` | Ghostfire | Ultimate | 44.0 -> **49.0** (+11.4%) | 19.6 -> **19.5** | 906.4 -> **1004.5** | Status 'Cursed' beneficiaries undertuned (WR: 44.6%); Location 'Graveyard' beneficiaries undertuned (WR: 41.4%) |
| `WFF` | Ghostfire | Conditional Strike | 4.9 -> **4.2** (-14.3%) | 40.0 -> **52.8** | 200.9 -> **226.0** | Status 'Bleeding' beneficiaries undertuned (WR: 46.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.4% vs 30% floor, Casts: 2490). Increasing spread: b -14.6%, n +30.0% |
| `WFW` | Ghostfire | Debuff / Control | 27.7 -> **27.2** (-1.8%) | - | 27.7 -> **27.2** | Individual spell overtuned (WR: 55.0%, Casts: 2641, mult: 0.983) |
| `WFE` | Ghostfire | Debuff / Control | 33.7 -> **29.7** (-11.9%) | - | 33.7 -> **29.7** | Status 'Bleeding' appliers overtuned on own (WR: 66.4%); Individual spell overtuned (WR: 67.4%, Casts: 1999, mult: 0.934) |
| `WFL` | Ghostfire | Buff / Sustain | 41.4 -> **42.1** (+1.7%) | - | 41.4 -> **42.1** | Individual spell undertuned (WR: 45.2%, Casts: 1728, mult: 1.016) |
| `WFD` | Ghostfire | Conditional Strike | 5.7 -> **5.0** (-12.3%) | 35.3 -> **46.1** | 206.9 -> **235.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.6% vs 30% floor, Casts: 1609). Increasing spread: b -15.0%, n +30.7%; Individual spell undertuned (WR: 40.5%, Casts: 1609, mult: 1.034) |
| `FEW` | Beasts | Conditional Strike | 3.1 -> **2.6** (-16.1%) | 67.7 -> **94.4** | 213.0 -> **248.0** | Status 'Entangled' beneficiaries undertuned (WR: 45.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1833). Increasing spread: b -17.9%, n +36.7% |
| `FEE` | Beasts | Buff / Sustain | 27.6 -> **28.1** (+1.8%) | - | 27.6 -> **28.1** | Individual spell undertuned (WR: 44.7%, Casts: 3006, mult: 1.018) |
| `FEL` | Beasts | Buff / Sustain | 29.9 -> **31.0** (+3.7%) | - | 29.9 -> **31.0** | Individual spell undertuned (WR: 39.6%, Casts: 2421, mult: 1.037) |
| `EFF` | Beasts | Debuff / Control | 3.9 -> **3.3** (-15.4%) | 61.7 -> **84.1** | 244.5 -> **280.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 2540). Increasing spread: b -17.7%, n +36.3%; Individual spell undertuned (WR: 45.6%, Casts: 2540, mult: 1.014) |
| `EFW` | Beasts | Buff / Sustain | 24.6 -> **24.1** (-2.0%) | - | 24.6 -> **24.1** | Individual spell overtuned (WR: 55.8%, Casts: 1645, mult: 0.980) |
| `EFL` | Beasts | Buff / Sustain | 7.4 -> **6.3** (-14.9%) | - | 7.4 -> **6.3** | Individual spell overtuned (WR: 86.9%, Casts: 1650, mult: 0.850) |
| `EFD` | Beasts | Ultimate | 33.4 -> **37.0** (+10.8%) | 28.9 -> **28.3** | 998.7 -> **1084.1** | Status 'Entangled' beneficiaries undertuned (WR: 45.0%); Location 'Jungle' beneficiaries undertuned (WR: 44.3%) |
| `FLF` | Lightning | Conditional Strike | 3.3 -> **2.8** (-15.2%) | 81.1 -> **113.9** | 270.9 -> **321.7** | Class Lightning undertuned (WR: 46.1%, factor: 1.016); Status 'Stunned' beneficiaries undertuned (WR: 43.1%) |
| `FLW` | Lightning | Debuff / Control | 54.3 -> **55.2** (+1.7%) | - | 54.3 -> **55.2** | Class Lightning undertuned (WR: 46.1%, factor: 1.016) |
| `FLE` | Lightning | Setup - Weather | 30.0 -> **31.3** (+4.3%) | - | 30.0 -> **31.3** | Class Lightning undertuned (WR: 46.1%, factor: 1.016); Weather 'Storming' appliers undertuned (WR: 45.9%, casts: 2614) |
| `FLL` | Lightning | Buff / Sustain | 26.4 -> **26.8** (+1.5%) | - | 26.4 -> **26.8** | Class Lightning undertuned (WR: 46.1%, factor: 1.016) |
| `FLD` | Lightning | Ultimate | 60.8 -> **68.9** (+13.3%) | 8.6 -> **8.6** | 583.7 -> **661.4** | Class Lightning undertuned (WR: 46.1%, factor: 1.016); Status 'Stunned' beneficiaries undertuned (WR: 43.1%) |
| `LFF` | Lightning | Conditional Strike | 3.7 -> **3.1** (-16.2%) | 57.3 -> **77.7** | 215.7 -> **244.0** | Class Lightning undertuned (WR: 46.1%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.7% vs 30% floor, Casts: 1501). Increasing spread: b -17.3%, n +35.6% |
| `LFE` | Lightning | Debuff / Control | 48.2 -> **50.2** (+4.1%) | - | 48.2 -> **50.2** | Class Lightning undertuned (WR: 46.1%, factor: 1.016); Individual spell undertuned (WR: 43.0%, Casts: 2951, mult: 1.024) |
| `LFL` | Lightning | Debuff / Control | 21.5 -> **18.8** (-12.6%) | 31.7 -> **40.7** | 703.1 -> **784.0** | Class Lightning undertuned (WR: 46.1%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.3% vs 30% floor, Casts: 2611). Increasing spread: b -13.9%, n +28.4% |
| `LFD` | Lightning | Conditional Strike | 6.8 -> **6.2** (-8.8%) | 56.1 -> **72.4** | 388.3 -> **455.1** | Class Lightning undertuned (WR: 46.1%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.6% vs 30% floor, Casts: 3714). Increasing spread: b -14.2%, n +29.0% |
| `FDF` | Blood | Conditional Strike | 3.4 -> **2.8** (-17.6%) | 68.0 -> **93.2** | 234.6 -> **263.8** | Class Blood overtuned (WR: 54.4%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2514). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 66.0 -> **64.8** (-1.8%) | - | 66.0 -> **64.8** | Class Blood overtuned (WR: 54.4%, factor: 0.982) |
| `FDE` | Blood | Setup - Weather | 21.9 -> **21.5** (-1.8%) | - | 21.9 -> **21.5** | Class Blood overtuned (WR: 54.4%, factor: 0.982) |
| `FDL` | Blood | Debuff / Control | 25.0 -> **20.9** (-16.4%) | - | 25.0 -> **20.9** | Class Blood overtuned (WR: 54.4%, factor: 0.982); Status 'Bleeding' appliers overtuned on own (WR: 66.4%) |
| `FDD` | Blood | Ultimate | 45.3 -> **49.4** (+9.1%) | 7.5 -> **7.0** | 385.0 -> **395.2** | Class Blood overtuned (WR: 54.4%, factor: 0.982); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.4% vs 16% floor, Casts: 1895, WR: 41.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 4.1 -> **3.4** (-17.1%) | 40.1 -> **52.8** | 168.5 -> **182.9** | Class Blood overtuned (WR: 54.4%, factor: 0.982); Status 'Bleeding' beneficiaries undertuned (WR: 46.3%) |
| `DFW` | Blood | Debuff / Control | 23.1 -> **19.5** (-15.6%) | - | 23.1 -> **19.5** | Class Blood overtuned (WR: 54.4%, factor: 0.982); Status 'Bleeding' appliers overtuned on own (WR: 66.4%) |
| `DFE` | Blood | Buff / Sustain | 39.4 -> **39.9** (+1.3%) | - | 39.4 -> **39.9** | Class Blood overtuned (WR: 54.4%, factor: 0.982); Individual spell undertuned (WR: 41.3%, Casts: 1796, mult: 1.031) |
| `DFL` | Blood | Buff / Sustain | 33.1 -> **32.1** (-3.0%) | - | 33.1 -> **32.1** | Class Blood overtuned (WR: 54.4%, factor: 0.982); Individual spell overtuned (WR: 53.7%, Casts: 1325, mult: 0.988) |
| `DFD` | Blood | Conditional Strike | 97.6 -> **110.7** (+13.4%) | 0.1 -> **0.1** | 107.4 -> **121.8** | Class Blood overtuned (WR: 54.4%, factor: 0.982); Condition triggers excessively (N=1 conditions, Trigger Rate: 96.0% vs 55% ceiling, WR: 53.5%). Compressing spread: b +15.5%, n -24.0% |
| `WEF` | Plants | Conditional Strike | 5.4 -> **4.6** (-14.8%) | 29.9 -> **39.7** | 166.9 -> **187.2** | Location 'Jungle' beneficiaries undertuned (WR: 44.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.6% vs 30% floor, Casts: 1648). Increasing spread: b -14.6%, n +29.9% |
| `WEW` | Plants | Debuff / Control | 112.0 -> **131.0** (+17.0%) | - | 112.0 -> **131.0** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 44.8%, Casts: 2065, mult: 1.017) |
| `WEE` | Plants | Setup - Location | 23.6 -> **23.0** (-2.5%) | - | 23.6 -> **23.0** | Location 'Jungle' appliers overtuned on own (WR: 53.8%); Individual spell overtuned (WR: 53.8%, Casts: 1653, mult: 0.988) |
| `WEL` | Plants | Debuff / Control | 40.4 -> **38.4** (-5.0%) | - | 40.4 -> **38.4** | Status 'Entangled' appliers overtuned on own (WR: 57.2%); Individual spell overtuned (WR: 57.2%, Casts: 2575, mult: 0.975) |
| `WED` | Plants | Conditional Strike | 10.0 -> **8.2** (-18.0%) | 19.2 -> **26.2** | 202.0 -> **223.0** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 2108). Increasing spread: b -17.8%, n +36.6% |
| `EWF` | Plants | Buff / Sustain | 5.3 -> **4.5** (-15.1%) | 25.7 -> **31.6** | 141.5 -> **146.7** | Weather 'Sunny' beneficiaries overtuned (WR: 53.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.4% vs 30% floor, Casts: 2768). Increasing spread: b -12.2%, n +25.0% |
| `EWW` | Plants | Debuff / Control | 9.5 -> **8.0** (-15.8%) | - | 9.5 -> **8.0** | Individual spell overtuned (WR: 87.5%, Casts: 1488, mult: 0.847) |
| `EWL` | Plants | Debuff / Control | 62.9 -> **63.6** (+1.1%) | - | 62.9 -> **63.6** | Individual spell undertuned (WR: 46.5%, Casts: 3440, mult: 1.011) |
| `EWD` | Plants | Conditional Strike | 14.8 -> **11.8** (-20.3%) | 60.6 -> **81.8** | 911.7 -> **977.0** | Status 'Bleeding' appliers overtuned on own (WR: 66.4%); Status 'Entangled' beneficiaries undertuned (WR: 45.0%) |
| `WLF` | Fey | Conditional Strike | 4.8 -> **4.1** (-14.6%) | 53.0 -> **71.4** | 259.2 -> **296.8** | Status 'Cursed' beneficiaries undertuned (WR: 44.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 1870). Increasing spread: b -15.5%, n +31.8% |
| `WLE` | Fey | Setup - Location | 87.5 -> **100.6** (+15.0%) | - | 87.5 -> **100.6** | Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 59.4 -> **58.0** (-2.4%) | - | 59.4 -> **58.0** | Individual spell overtuned (WR: 56.7%, Casts: 1425, mult: 0.977) |
| `WLD` | Fey | Ultimate | 27.8 -> **27.8** (+0.0%) | 55.6 -> **72.3** | 1573.5 -> **2037.7** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1970). Shifted tuner focus: protected ultimate base floor at 27.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 15.8 -> **13.9** (-12.0%) | 23.3 -> **29.5** | 383.9 -> **423.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.2% vs 30% floor, Casts: 3167). Increasing spread: b -13.1%, n +26.8%; Individual spell undertuned (WR: 45.6%, Casts: 3167, mult: 1.014) |
| `LWW` | Fey | Debuff / Control | 43.3 -> **44.1** (+1.8%) | - | 43.3 -> **44.1** | Individual spell undertuned (WR: 44.3%, Casts: 1908, mult: 1.019) |
| `LWD` | Fey | Conditional Strike | 3.7 -> **3.2** (-13.5%) | 68.0 -> **93.2** | 255.3 -> **301.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1750). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 34.2%, Casts: 1750, mult: 1.059) |
| `WDF` | Ice | Conditional Strike | 5.6 -> **5.0** (-10.7%) | 64.4 -> **88.0** | 366.2 -> **445.0** | Weather 'Raining' beneficiaries undertuned (WR: 39.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.0% vs 30% floor, Casts: 2724). Increasing spread: b -15.2%, n +31.2% |
| `WDW` | Ice | Buff / Sustain | 14.5 -> **14.8** (+2.1%) | - | 14.5 -> **14.8** | Individual spell undertuned (WR: 43.1%, Casts: 3125, mult: 1.024) |
| `WDL` | Ice | Debuff / Control | 45.6 -> **44.1** (-3.3%) | - | 45.6 -> **44.1** | Individual spell overtuned (WR: 59.2%, Casts: 1217, mult: 0.968) |
| `WDD` | Ice | Ultimate | 27.9 -> **27.9** (+0.0%) | 39.1 -> **49.8** | 1118.8 -> **1417.3** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 2.1% vs 16% floor, Casts: 2262). Shifted tuner focus: protected ultimate base floor at 27.9 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWF` | Ice | Debuff / Control | 44.0 -> **43.3** (-1.6%) | - | 44.0 -> **43.3** | Individual spell overtuned (WR: 54.8%, Casts: 2176, mult: 0.984) |
| `DWE` | Ice | Setup - Location | 30.1 -> **32.0** (+6.3%) | - | 30.1 -> **32.0** | Location 'Tundra' appliers undertuned (WR: 41.0%, casts: 2936); Individual spell undertuned (WR: 41.0%, Casts: 2936, mult: 1.032) |
| `DWL` | Ice | Debuff / Control | 43.0 -> **42.2** (-1.9%) | - | 43.0 -> **42.2** | Individual spell overtuned (WR: 55.4%, Casts: 1871, mult: 0.982) |
| `DWD` | Ice | Conditional Strike | 10.2 -> **9.3** (-8.8%) | 15.1 -> **18.0** | 164.2 -> **176.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 21.3% vs 30% floor, Casts: 2188). Increasing spread: b -9.5%, n +19.2%; Individual spell undertuned (WR: 46.2%, Casts: 2188, mult: 1.012) |
| `ELF` | Wind | Conditional Strike | 10.3 -> **9.1** (-11.7%) | 41.8 -> **55.6** | 440.8 -> **515.1** | Class Wind undertuned (WR: 46.2%, factor: 1.015); Status 'Bleeding' beneficiaries undertuned (WR: 46.3%) |
| `ELW` | Wind | Debuff / Control | 44.8 -> **45.5** (+1.6%) | - | 44.8 -> **45.5** | Class Wind undertuned (WR: 46.2%, factor: 1.015) |
| `ELE` | Wind | Setup - Weather | 22.0 -> **22.8** (+3.6%) | - | 22.0 -> **22.8** | Class Wind undertuned (WR: 46.2%, factor: 1.015); Individual spell undertuned (WR: 44.1%, Casts: 1657, mult: 1.020) |
| `ELL` | Wind | Buff / Sustain | 36.4 -> **37.0** (+1.6%) | - | 36.4 -> **37.0** | Class Wind undertuned (WR: 46.2%, factor: 1.015) |
| `ELD` | Wind | Conditional Strike | 6.2 -> **5.6** (-9.7%) | 54.7 -> **75.4** | 345.3 -> **427.8** | Class Wind undertuned (WR: 46.2%, factor: 1.015); Weather 'Raining' beneficiaries undertuned (WR: 39.7%) |
| `LEF` | Wind | Conditional Strike | 4.0 -> **3.5** (-12.5%) | 45.4 -> **58.5** | 185.6 -> **208.2** | Class Wind undertuned (WR: 46.2%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.8% vs 30% floor, Casts: 1893). Increasing spread: b -14.1%, n +28.9% |
| `LEW` | Wind | Debuff / Control | 55.6 -> **57.2** (+2.9%) | - | 55.6 -> **57.2** | Class Wind undertuned (WR: 46.2%, factor: 1.015); Individual spell undertuned (WR: 46.1%, Casts: 2664, mult: 1.013) |
| `LEE` | Wind | Setup - Weather | 19.9 -> **20.2** (+1.5%) | - | 19.9 -> **20.2** | Class Wind undertuned (WR: 46.2%, factor: 1.015) |
| `LEL` | Wind | Buff / Sustain | 40.7 -> **41.3** (+1.5%) | - | 40.7 -> **41.3** | Class Wind undertuned (WR: 46.2%, factor: 1.015) |
| `EDF` | Poison | Conditional Strike | 3.8 -> **3.1** (-18.4%) | 46.5 -> **60.0** | 180.5 -> **189.1** | Class Poison overtuned (WR: 56.0%, factor: 0.976); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.6% vs 30% floor, Casts: 1809). Increasing spread: b -14.2%, n +29.0% |
| `EDW` | Poison | Debuff / Control | 19.1 -> **17.5** (-8.4%) | - | 19.1 -> **17.5** | Class Poison overtuned (WR: 56.0%, factor: 0.976); Individual spell overtuned (WR: 65.9%, Casts: 2071, mult: 0.941) |
| `EDE` | Poison | Setup - Location | 50.6 -> **52.0** (+2.8%) | - | 50.6 -> **52.0** | Class Poison overtuned (WR: 56.0%, factor: 0.976); Location 'Swamp' appliers undertuned (WR: 42.5%, casts: 2076) |
| `EDL` | Poison | Debuff / Control | 3.9 -> **3.2** (-17.9%) | - | 3.9 -> **3.2** | Class Poison overtuned (WR: 56.0%, factor: 0.976); Individual spell overtuned (WR: 86.7%, Casts: 2221, mult: 0.851) |
| `EDD` | Poison | Ultimate | 27.0 -> **29.1** (+7.8%) | 28.4 -> **27.8** | 793.8 -> **838.1** | Class Poison overtuned (WR: 56.0%, factor: 0.976); Status 'Bleeding' beneficiaries undertuned (WR: 46.3%) |
| `DEF` | Poison | Conditional Strike | 31.2 -> **32.5** (+4.2%) | 1.7 -> **1.5** | 84.2 -> **81.2** | Class Poison overtuned (WR: 56.0%, factor: 0.976); Condition triggers excessively (N=1 conditions, Trigger Rate: 57.6% vs 55% ceiling, WR: 52.6%). Compressing spread: b +6.6%, n -10.0% |
| `DEW` | Poison | Debuff / Control | 20.4 -> **19.6** (-3.9%) | - | 20.4 -> **19.6** | Class Poison overtuned (WR: 56.0%, factor: 0.976); Individual spell overtuned (WR: 54.1%, Casts: 3782, mult: 0.987) |
| `DEE` | Poison | Debuff / Control | 21.7 -> **21.2** (-2.3%) | - | 21.7 -> **21.2** | Class Poison overtuned (WR: 56.0%, factor: 0.976) |
| `DEL` | Poison | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 42.0 -> **56.6** | 17.2 -> **17.3** | Class Poison overtuned (WR: 56.0%, factor: 0.976); Status 'Bleeding' beneficiaries undertuned (WR: 46.3%) |
| `DED` | Poison | Debuff / Control | 23.6 -> **23.0** (-2.5%) | - | 23.6 -> **23.0** | Class Poison overtuned (WR: 56.0%, factor: 0.976) |
| `LDW` | Cosmic | Debuff / Control | 49.0 -> **47.4** (-3.3%) | - | 49.0 -> **47.4** | Individual spell overtuned (WR: 59.3%, Casts: 3060, mult: 0.967) |
| `LDE` | Cosmic | Setup - Location | 24.6 -> **25.1** (+2.0%) | - | 24.6 -> **25.1** | Individual spell undertuned (WR: 44.4%, Casts: 1739, mult: 1.019) |
| `LDL` | Cosmic | Conditional Strike | 4.8 -> **4.2** (-12.5%) | 46.9 -> **62.1** | 229.9 -> **265.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 1957). Increasing spread: b -15.8%, n +32.4%; Individual spell undertuned (WR: 40.3%, Casts: 1957, mult: 1.035) |
| `LDD` | Cosmic | Ultimate | 57.1 -> **62.4** (+9.3%) | 5.4 -> **5.1** | 365.4 -> **380.6** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2056, WR: 46.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 46.3%, Casts: 2056, mult: 1.012) |
| `DLF` | Cosmic | Conditional Strike | 5.8 -> **5.0** (-13.8%) | 46.6 -> **60.7** | 276.1 -> **308.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 2281). Increasing spread: b -14.8%, n +30.2%; Individual spell undertuned (WR: 46.5%, Casts: 2281, mult: 1.011) |
| `DLW` | Cosmic | Direct Damage | 62.3 -> **61.3** (-1.6%) | - | 62.3 -> **61.3** | Individual spell overtuned (WR: 54.7%, Casts: 2061, mult: 0.984) |
| `DLL` | Cosmic | Conditional Strike | 12.9 -> **11.4** (-11.6%) | 25.3 -> **32.4** | 339.3 -> **380.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.9% vs 30% floor, Casts: 1967). Increasing spread: b -13.6%, n +27.9%; Individual spell undertuned (WR: 44.0%, Casts: 1967, mult: 1.020) |
