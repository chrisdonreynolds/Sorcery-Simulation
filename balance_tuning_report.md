# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T00:27:10Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 708.5s  
**Total Spells Tuned:** 99 / 125  

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
| **Blood** | 18,866 | 55.5% | 55.5% | 16.3 | Overtuned ⚠️ |
| **Poison** | 21,313 | 53.8% | 53.8% | 9.0 | Overtuned ⚠️ |
| **Light** | 9,740 | 52.8% | 52.8% | 11.7 | Balanced ✅ |
| **Beasts** | 19,410 | 52.8% | 52.8% | 10.1 | Balanced ✅ |
| **Earth** | 10,260 | 52.3% | 52.3% | 18.5 | Balanced ✅ |
| **Ghostfire** | 21,544 | 51.0% | 51.0% | 15.3 | Balanced ✅ |
| **Plants** | 19,950 | 50.9% | 50.9% | 8.3 | Balanced ✅ |
| **Fire** | 9,443 | 50.3% | 50.3% | 14.3 | Balanced ✅ |
| **Lightning** | 22,038 | 49.2% | 49.2% | 11.9 | Balanced ✅ |
| **Cosmic** | 17,617 | 49.2% | 49.2% | 15.1 | Balanced ✅ |
| **Dark** | 10,393 | 48.7% | 48.7% | 15.4 | Balanced ✅ |
| **Wind** | 18,987 | 48.2% | 48.2% | 7.3 | Balanced ✅ |
| **Water** | 9,515 | 47.4% | 47.4% | 9.8 | Balanced ✅ |
| **Ice** | 19,990 | 46.5% | 46.5% | 12.9 | Balanced ✅ |
| **Fey** | 17,100 | 43.7% | 43.7% | 19.3 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,818 (51.4%) | 3,185 (52.8%) | 20.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,483 (54.6%) | 4,593 (54.6%) | 9.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,668 (52.0%) | 4,239 (48.4%) | 12.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,080 (65.3%) | 8,674 (46.1%) | 5.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,367 (45.7%) | 5,362 (43.0%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,665 (58.6%) | 7,260 (48.3%) | 2.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,577 (44.9%) | 5,581 (39.6%) | 5.3% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 61.0 -> **60.3** (-1.1%) | - | 61.0 -> **60.3** | Individual spell overtuned (WR: 53.7%, Casts: 1689, mult: 0.988) |
| `FFE` | Fire | Debuff / Control | 33.4 -> **33.9** (+1.5%) | - | 33.4 -> **33.9** | Individual spell undertuned (WR: 45.5%, Casts: 2140, mult: 1.015) |
| `FFL` | Fire | Debuff / Control | 4.9 -> **4.8** (-2.0%) | - | 4.9 -> **4.8** | Individual spell overtuned (WR: 58.4%, Casts: 1937, mult: 0.970) |
| `FFD` | Fire | Conditional Strike | 3.1 -> **2.6** (-16.1%) | 84.7 -> **110.6** | 265.7 -> **290.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.7% vs 30% floor, Casts: 1318). Increasing spread: b -14.9%, n +30.6% |
| `WWF` | Water | Conditional Strike | 7.1 -> **6.3** (-11.3%) | 55.6 -> **68.0** | 401.9 -> **434.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.5% vs 30% floor, Casts: 1278). Increasing spread: b -11.0%, n +22.4% |
| `WWE` | Water | Setup - Weather | 45.5 -> **47.1** (+3.5%) | - | 45.5 -> **47.1** | Weather 'Raining' appliers undertuned (WR: 44.9%, casts: 1577); Individual spell undertuned (WR: 44.9%, Casts: 1577, mult: 1.017) |
| `WWD` | Water | Buff / Sustain | 49.4 -> **50.2** (+1.6%) | - | 49.4 -> **50.2** | Individual spell undertuned (WR: 45.4%, Casts: 2354, mult: 1.015) |
| `EEF` | Earth | Conditional Strike | 14.6 -> **13.5** (-7.5%) | 17.8 -> **20.5** | 274.5 -> **290.2** | Status 'Stunned' appliers undertuned (WR: 45.7%, casts: 14367); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 26.1% vs 30% floor, Casts: 1581). Increasing spread: b -7.6%, n +15.3% |
| `EEW` | Earth | Buff / Sustain | 27.6 -> **26.8** (-2.9%) | - | 27.6 -> **26.8** | Individual spell overtuned (WR: 58.7%, Casts: 1771, mult: 0.969) |
| `LLF` | Light | Conditional Strike | 4.9 -> **5.6** (+14.3%) | 104.5 -> **139.6** | 517.0 -> **787.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.1% vs 30% floor, Casts: 3015). Increasing spread: b -16.4%, n +33.6%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 54.0 -> **62.1** (+15.0%) | - | 54.0 -> **62.1** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LLE` | Light | Setup - Weather | 84.7 -> **94.4** (+11.5%) | - | 84.7 -> **94.4** | Weather 'Sunny' appliers overtuned on own (WR: 54.6%); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 21.8 -> **21.5** (-1.4%) | - | 21.8 -> **21.5** | Individual spell overtuned (WR: 54.4%, Casts: 1090, mult: 0.986) |
| `LLD` | Light | Ultimate | 34.9 -> **34.3** (-1.7%) | 35.4 -> **45.1** | 1270.4 -> **1581.2** | Weather 'Sunny' beneficiaries overtuned (WR: 54.6%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1849). Shifted tuner focus: protected ultimate base floor at 34.9 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 1.7 -> **1.4** (-17.6%) | 174.5 -> **239.1** | 298.3 -> **336.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2345). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 41.8%, Casts: 2345, mult: 1.029) |
| `DDW` | Dark | Debuff / Control | 72.1 -> **73.1** (+1.4%) | - | 72.1 -> **73.1** | Individual spell undertuned (WR: 45.9%, Casts: 2061, mult: 1.013) |
| `DDE` | Dark | Setup - Weather | 86.6 -> **96.9** (+11.9%) | - | 86.6 -> **96.9** | Weather 'Darkness' appliers overtuned on own (WR: 54.1%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `DDD` | Dark | Debuff / Control | 23.6 -> **23.0** (-2.5%) | - | 23.6 -> **23.0** | Individual spell overtuned (WR: 57.0%, Casts: 1456, mult: 0.976) |
| `FWW` | Ghostfire | Debuff / Control | 39.6 -> **47.0** (+18.7%) | - | 39.6 -> **47.0** | Status 'Cursed' appliers undertuned (WR: 45.7%, casts: 5225); Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 100.4 -> **115.5** (+15.0%) | - | 100.4 -> **115.5** | Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 100.4 -> **117.2** (+16.7%) | - | 100.4 -> **117.2** | Status 'Cursed' appliers undertuned (WR: 45.7%, casts: 5225); Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 47.8 -> **47.0** (-1.7%) | 31.9 -> **42.2** | 1572.6 -> **2030.4** | Status 'Cursed' beneficiaries undertuned (WR: 40.7%); Location 'Graveyard' beneficiaries overtuned (WR: 54.8%) |
| `WFF` | Ghostfire | Conditional Strike | 3.0 -> **2.5** (-16.7%) | 91.4 -> **121.8** | 277.2 -> **307.0** | Status 'Bleeding' beneficiaries undertuned (WR: 46.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.0% vs 30% floor, Casts: 2056). Increasing spread: b -15.2%, n +31.2% |
| `WFW` | Ghostfire | Debuff / Control | 26.8 -> **26.3** (-1.9%) | - | 26.8 -> **26.3** | Individual spell overtuned (WR: 55.5%, Casts: 2724, mult: 0.982) |
| `WFE` | Ghostfire | Debuff / Control | 22.6 -> **20.0** (-11.5%) | - | 22.6 -> **20.0** | Status 'Bleeding' appliers overtuned on own (WR: 65.3%); Individual spell overtuned (WR: 66.8%, Casts: 1764, mult: 0.937) |
| `WFD` | Ghostfire | Conditional Strike | 3.7 -> **3.3** (-10.8%) | 78.3 -> **101.6** | 293.4 -> **338.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.8% vs 30% floor, Casts: 2081). Increasing spread: b -14.5%, n +29.7%; Individual spell undertuned (WR: 39.0%, Casts: 2081, mult: 1.040) |
| `FEF` | Beasts | Debuff / Control | 42.0 -> **41.2** (-1.9%) | - | 42.0 -> **41.2** | Individual spell overtuned (WR: 55.6%, Casts: 1201, mult: 0.981) |
| `FEW` | Beasts | Conditional Strike | 1.9 -> **1.6** (-15.8%) | 177.9 -> **242.8** | 339.9 -> **390.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 1600). Increasing spread: b -17.7%, n +36.5%; Individual spell undertuned (WR: 44.8%, Casts: 1600, mult: 1.017) |
| `FEE` | Beasts | Buff / Sustain | 30.2 -> **30.8** (+2.0%) | - | 30.2 -> **30.8** | Individual spell undertuned (WR: 44.3%, Casts: 2400, mult: 1.019) |
| `FEL` | Beasts | Buff / Sustain | 34.0 -> **34.6** (+1.8%) | - | 34.0 -> **34.6** | Individual spell undertuned (WR: 44.8%, Casts: 2790, mult: 1.017) |
| `EFF` | Beasts | Debuff / Control | 2.2 -> **1.8** (-18.2%) | 156.5 -> **214.2** | 346.5 -> **387.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1382). Increasing spread: b -17.9%, n +36.9% |
| `EFW` | Beasts | Buff / Sustain | 23.4 -> **22.5** (-3.8%) | - | 23.4 -> **22.5** | Individual spell overtuned (WR: 60.3%, Casts: 1450, mult: 0.963) |
| `EFL` | Beasts | Buff / Sustain | 4.5 -> **3.8** (-15.6%) | - | 4.5 -> **3.8** | Individual spell overtuned (WR: 86.8%, Casts: 1527, mult: 0.850) |
| `EFD` | Beasts | Ultimate | 35.3 -> **34.7** (-1.7%) | 48.7 -> **63.1** | 1754.4 -> **2224.3** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.4% vs 16% floor, Casts: 3000). Shifted tuner focus: protected ultimate base floor at 35.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo.; Individual spell overtuned (WR: 54.9%, Casts: 3000, mult: 0.984) |
| `FLF` | Lightning | Conditional Strike | 1.9 -> **1.6** (-15.8%) | 212.5 -> **298.9** | 405.6 -> **479.8** | Status 'Stunned' beneficiaries undertuned (WR: 43.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 3114). Increasing spread: b -17.9%, n +36.8% |
| `FLW` | Lightning | Debuff / Control | 60.5 -> **60.2** (-0.5%) | - | 60.5 -> **60.2** | Status 'Stunned' appliers undertuned (WR: 45.7%, casts: 14367); Individual spell overtuned (WR: 55.8%, Casts: 2041, mult: 0.980) |
| `FLD` | Lightning | Ultimate | 76.0 -> **82.1** (+8.0%) | 10.8 -> **10.4** | 896.8 -> **935.9** | Status 'Stunned' beneficiaries undertuned (WR: 43.0%); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 2248, WR: 48.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `LFF` | Lightning | Conditional Strike | 2.2 -> **1.8** (-18.2%) | 143.5 -> **195.0** | 317.9 -> **352.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.3% vs 30% floor, Casts: 1128). Increasing spread: b -17.5%, n +35.9%; Individual spell undertuned (WR: 44.5%, Casts: 1128, mult: 1.019) |
| `LFW` | Lightning | Buff / Sustain | 31.3 -> **30.0** (-4.2%) | - | 31.3 -> **30.0** | Individual spell overtuned (WR: 61.4%, Casts: 2608, mult: 0.959) |
| `LFE` | Lightning | Debuff / Control | 51.5 -> **52.3** (+1.6%) | - | 51.5 -> **52.3** | Status 'Stunned' appliers undertuned (WR: 45.7%, casts: 14367) |
| `LFL` | Lightning | Debuff / Control | 24.5 -> **28.2** (+15.1%) | 67.8 -> **87.7** | 1685.6 -> **2501.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.2% vs 30% floor, Casts: 2811). Increasing spread: b -14.3%, n +29.3%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 4.9 -> **4.5** (-8.2%) | 118.1 -> **148.6** | 583.6 -> **673.2** | Status 'Stunned' appliers undertuned (WR: 45.7%, casts: 14367); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.5% vs 30% floor, Casts: 2667). Increasing spread: b -12.6%, n +25.8% |
| `FDF` | Blood | Conditional Strike | 1.9 -> **1.5** (-21.1%) | 174.9 -> **239.6** | 334.2 -> **360.9** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1547). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 71.9 -> **70.3** (-2.2%) | - | 71.9 -> **70.3** | Class Blood overtuned (WR: 55.5%, factor: 0.978) |
| `FDE` | Blood | Setup - Weather | 21.5 -> **21.0** (-2.3%) | - | 21.5 -> **21.0** | Class Blood overtuned (WR: 55.5%, factor: 0.978) |
| `FDL` | Blood | Debuff / Control | 15.9 -> **13.2** (-17.0%) | - | 15.9 -> **13.2** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Status 'Bleeding' appliers overtuned on own (WR: 65.3%) |
| `FDD` | Blood | Ultimate | 57.7 -> **56.4** (-2.3%) | 6.2 -> **8.0** | 415.4 -> **507.6** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.4% vs 16% floor, Casts: 1676). Shifted tuner focus: protected ultimate base floor at 57.7 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 2.5 -> **2.1** (-16.0%) | 89.4 -> **119.2** | 226.0 -> **252.4** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Status 'Bleeding' beneficiaries undertuned (WR: 46.1%) |
| `DFW` | Blood | Debuff / Control | 19.6 -> **16.4** (-16.3%) | - | 19.6 -> **16.4** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Status 'Bleeding' appliers overtuned on own (WR: 65.3%) |
| `DFE` | Blood | Buff / Sustain | 42.4 -> **43.6** (+2.8%) | - | 42.4 -> **43.6** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Individual spell undertuned (WR: 36.2%, Casts: 2145, mult: 1.051) |
| `DFL` | Blood | Buff / Sustain | 33.4 -> **33.8** (+1.2%) | - | 33.4 -> **33.8** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Individual spell undertuned (WR: 40.1%, Casts: 1037, mult: 1.035) |
| `DFD` | Blood | Conditional Strike | 144.0 -> **160.6** (+11.5%) | 0.1 -> **0.1** | 158.4 -> **176.7** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.8% vs 55% ceiling, WR: 50.4%). Compressing spread: b +14.1%, n -22.5% |
| `WEF` | Plants | Conditional Strike | 3.6 -> **3.2** (-11.1%) | 68.0 -> **87.9** | 248.4 -> **284.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.3% vs 30% floor, Casts: 1650). Increasing spread: b -14.3%, n +29.3%; Individual spell undertuned (WR: 38.9%, Casts: 1650, mult: 1.040) |
| `WEW` | Plants | Debuff / Control | 175.3 -> **204.3** (+16.5%) | - | 175.3 -> **204.3** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 45.9%, Casts: 1825, mult: 1.013) |
| `WEL` | Plants | Debuff / Control | 38.4 -> **36.1** (-6.0%) | - | 38.4 -> **36.1** | Status 'Entangled' appliers overtuned on own (WR: 58.6%); Individual spell overtuned (WR: 58.6%, Casts: 2665, mult: 0.970) |
| `WED` | Plants | Conditional Strike | 5.5 -> **6.1** (+10.9%) | 49.2 -> **46.2** | 276.1 -> **287.9** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.7% vs 8% floor, Casts: 1225, WR: 42.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 42.4%, Casts: 1225, mult: 1.027) |
| `EWF` | Plants | Buff / Sustain | 3.5 -> **3.0** (-14.3%) | 48.2 -> **58.6** | 172.2 -> **178.8** | Weather 'Sunny' beneficiaries overtuned (WR: 54.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.7% vs 30% floor, Casts: 2744). Increasing spread: b -11.7%, n +23.9% |
| `EWW` | Plants | Debuff / Control | 5.9 -> **5.2** (-11.9%) | - | 5.9 -> **5.2** | Individual spell overtuned (WR: 80.8%, Casts: 2128, mult: 0.877) |
| `EWL` | Plants | Debuff / Control | 66.5 -> **68.5** (+3.0%) | - | 66.5 -> **68.5** | Individual spell undertuned (WR: 41.3%, Casts: 2563, mult: 1.031) |
| `EWD` | Plants | Conditional Strike | 7.9 -> **6.5** (-17.7%) | 149.1 -> **196.5** | 1185.8 -> **1283.8** | Status 'Bleeding' appliers overtuned on own (WR: 65.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 2660). Increasing spread: b -15.5%, n +31.8% |
| `WLF` | Fey | Conditional Strike | 3.0 -> **2.8** (-6.7%) | 123.5 -> **169.4** | 373.5 -> **477.1** | Class Fey undertuned (WR: 43.7%, factor: 1.025); Status 'Cursed' beneficiaries undertuned (WR: 40.7%) |
| `WLW` | Fey | Debuff / Control | 52.9 -> **56.2** (+6.2%) | - | 52.9 -> **56.2** | Class Fey undertuned (WR: 43.7%, factor: 1.025); Status 'Cursed' appliers undertuned (WR: 45.7%, casts: 5225) |
| `WLE` | Fey | Setup - Location | 133.1 -> **156.9** (+17.9%) | - | 133.1 -> **156.9** | Class Fey undertuned (WR: 43.7%, factor: 1.025); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 55.1 -> **56.5** (+2.5%) | - | 55.1 -> **56.5** | Class Fey undertuned (WR: 43.7%, factor: 1.025) |
| `WLD` | Fey | Ultimate | 27.8 -> **27.7** (-0.4%) | 122.2 -> **155.9** | 3425.0 -> **4346.1** | Class Fey undertuned (WR: 43.7%, factor: 1.025); Location 'Enchanted Forest' beneficiaries overtuned (WR: 54.6%) |
| `LWF` | Fey | Debuff / Control | 18.6 -> **16.7** (-10.2%) | 47.0 -> **57.8** | 892.8 -> **982.0** | Class Fey undertuned (WR: 43.7%, factor: 1.025); Location 'Enchanted Forest' beneficiaries overtuned (WR: 54.6%) |
| `LWW` | Fey | Debuff / Control | 44.9 -> **46.0** (+2.4%) | - | 44.9 -> **46.0** | Class Fey undertuned (WR: 43.7%, factor: 1.025) |
| `LWL` | Fey | Debuff / Control | 42.3 -> **44.7** (+5.7%) | - | 42.3 -> **44.7** | Class Fey undertuned (WR: 43.7%, factor: 1.025); Individual spell undertuned (WR: 41.4%, Casts: 1600, mult: 1.030) |
| `LWD` | Fey | Conditional Strike | 2.2 -> **1.9** (-13.6%) | 174.9 -> **239.6** | 387.0 -> **457.1** | Class Fey undertuned (WR: 43.7%, factor: 1.025); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1493). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 3.9 -> **3.6** (-7.7%) | 158.8 -> **219.5** | 623.2 -> **793.8** | Status 'Stunned' appliers undertuned (WR: 45.7%, casts: 14367); Weather 'Raining' beneficiaries undertuned (WR: 39.6%) |
| `WDW` | Ice | Buff / Sustain | 14.2 -> **14.0** (-1.4%) | - | 14.2 -> **14.0** | Individual spell overtuned (WR: 55.1%, Casts: 3364, mult: 0.983) |
| `WDE` | Ice | Setup - Weather | 25.9 -> **26.9** (+3.9%) | - | 25.9 -> **26.9** | Individual spell undertuned (WR: 39.4%, Casts: 1795, mult: 1.038) |
| `WDD` | Ice | Ultimate | 27.1 -> **29.7** (+9.6%) | 75.4 -> **73.2** | 2070.4 -> **2203.7** | Weather 'Blizzard' beneficiaries undertuned (WR: 45.9%); Location 'Tundra' beneficiaries undertuned (WR: 45.9%) |
| `DWF` | Ice | Debuff / Control | 43.3 -> **42.8** (-1.2%) | - | 43.3 -> **42.8** | Individual spell overtuned (WR: 53.9%, Casts: 1155, mult: 0.987) |
| `DWW` | Ice | Debuff / Control | 54.3 -> **52.9** (-2.6%) | - | 54.3 -> **52.9** | Individual spell overtuned (WR: 57.5%, Casts: 1908, mult: 0.974) |
| `DWE` | Ice | Setup - Location | 33.0 -> **34.0** (+3.0%) | - | 33.0 -> **34.0** | Location 'Tundra' appliers undertuned (WR: 45.6%, casts: 1983); Individual spell undertuned (WR: 45.6%, Casts: 1983, mult: 1.014) |
| `DWL` | Ice | Debuff / Control | 43.9 -> **44.8** (+2.1%) | - | 43.9 -> **44.8** | Individual spell undertuned (WR: 44.0%, Casts: 2031, mult: 1.020) |
| `DWD` | Ice | Conditional Strike | 7.9 -> **7.0** (-11.4%) | 26.6 -> **32.9** | 218.0 -> **237.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.8% vs 30% floor, Casts: 1604). Increasing spread: b -11.7%, n +23.9% |
| `ELF` | Wind | Conditional Strike | 6.9 -> **6.1** (-11.6%) | 97.4 -> **128.7** | 679.0 -> **791.2** | Status 'Bleeding' beneficiaries undertuned (WR: 46.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.3% vs 30% floor, Casts: 1231). Increasing spread: b -14.7%, n +30.1% |
| `ELE` | Wind | Setup - Weather | 23.1 -> **23.8** (+3.0%) | - | 23.1 -> **23.8** | Individual spell undertuned (WR: 41.2%, Casts: 1896, mult: 1.031) |
| `ELD` | Wind | Conditional Strike | 3.9 -> **3.3** (-15.4%) | 139.0 -> **191.7** | 546.0 -> **635.9** | Weather 'Raining' beneficiaries undertuned (WR: 39.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 2576). Increasing spread: b -15.8%, n +32.4% |
| `LEF` | Wind | Conditional Strike | 2.6 -> **2.3** (-11.5%) | 98.5 -> **125.3** | 258.7 -> **290.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.8% vs 30% floor, Casts: 1643). Increasing spread: b -13.3%, n +27.2% |
| `EDF` | Poison | Conditional Strike | 2.1 -> **1.8** (-14.3%) | 98.5 -> **126.4** | 209.0 -> **229.3** | Class Poison overtuned (WR: 53.8%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.5% vs 30% floor, Casts: 2188). Increasing spread: b -13.8%, n +28.3% |
| `EDW` | Poison | Debuff / Control | 15.8 -> **14.9** (-5.7%) | - | 15.8 -> **14.9** | Class Poison overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 61.9%, Casts: 2388, mult: 0.957) |
| `EDE` | Poison | Setup - Location | 50.0 -> **49.2** (-1.6%) | - | 50.0 -> **49.2** | Class Poison overtuned (WR: 53.8%, factor: 0.985) |
| `EDL` | Poison | Debuff / Control | 2.2 -> **1.9** (-13.6%) | - | 2.2 -> **1.9** | Class Poison overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 85.2%, Casts: 2165, mult: 0.857) |
| `EDD` | Poison | Ultimate | 33.3 -> **35.4** (+6.3%) | 25.1 -> **24.0** | 869.1 -> **885.0** | Class Poison overtuned (WR: 53.8%, factor: 0.985); Status 'Bleeding' beneficiaries undertuned (WR: 46.1%) |
| `DEF` | Poison | Conditional Strike | 32.8 -> **32.9** (+0.3%) | 1.4 -> **1.4** | 78.7 -> **79.0** | Class Poison overtuned (WR: 53.8%, factor: 0.985); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 51.3% within [30%-55%] target window, WR: 44.5%). |
| `DEW` | Poison | Debuff / Control | 17.9 -> **17.3** (-3.4%) | - | 17.9 -> **17.3** | Class Poison overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 55.1%, Casts: 2923, mult: 0.983) |
| `DEE` | Poison | Debuff / Control | 26.9 -> **25.8** (-4.1%) | - | 26.9 -> **25.8** | Class Poison overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 57.2%, Casts: 1679, mult: 0.975) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 98.7 -> **132.8** | 19.9 -> **26.8** | Class Poison overtuned (WR: 53.8%, factor: 0.985); Status 'Bleeding' beneficiaries undertuned (WR: 46.1%) |
| `DED` | Poison | Debuff / Control | 22.4 -> **22.1** (-1.3%) | - | 22.4 -> **22.1** | Class Poison overtuned (WR: 53.8%, factor: 0.985) |
| `LDF` | Cosmic | Debuff / Control | 77.9 -> **75.5** (-3.1%) | - | 77.9 -> **75.5** | Individual spell overtuned (WR: 58.7%, Casts: 887, mult: 0.969) |
| `LDW` | Cosmic | Debuff / Control | 44.4 -> **45.1** (+1.6%) | - | 44.4 -> **45.1** | Status 'Stunned' appliers undertuned (WR: 45.7%, casts: 14367) |
| `LDE` | Cosmic | Setup - Location | 25.1 -> **25.6** (+2.0%) | - | 25.1 -> **25.6** | Individual spell undertuned (WR: 44.5%, Casts: 1878, mult: 1.018) |
| `LDL` | Cosmic | Conditional Strike | 3.3 -> **2.8** (-15.2%) | 111.2 -> **149.1** | 370.3 -> **420.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.5% vs 30% floor, Casts: 1943). Increasing spread: b -16.6%, n +34.1%; Individual spell undertuned (WR: 40.6%, Casts: 1943, mult: 1.034) |
| `LDD` | Cosmic | Ultimate | 62.4 -> **67.4** (+8.0%) | 8.6 -> **8.1** | 599.0 -> **613.3** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1469, WR: 47.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 3.7 -> **3.1** (-16.2%) | 104.8 -> **138.9** | 391.5 -> **433.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.4% vs 30% floor, Casts: 2406). Increasing spread: b -15.9%, n +32.5% |
| `DLL` | Cosmic | Conditional Strike | 8.5 -> **7.5** (-11.8%) | 52.8 -> **65.9** | 457.3 -> **501.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.7% vs 30% floor, Casts: 1755). Increasing spread: b -12.1%, n +24.8% |
