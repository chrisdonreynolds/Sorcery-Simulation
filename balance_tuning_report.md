# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T03:06:58Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 394.4s  
**Total Spells Tuned:** 96 / 125  

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
| **Poison** | 16,836 | 55.9% | 55.9% | 10.5 | Overtuned ⚠️ |
| **Blood** | 17,377 | 53.7% | 53.7% | 27.7 | Overtuned ⚠️ |
| **Ghostfire** | 15,214 | 53.1% | 53.1% | 49.6 | Balanced ✅ |
| **Fire** | 7,050 | 52.9% | 52.9% | 15.4 | Balanced ✅ |
| **Light** | 7,581 | 52.0% | 52.0% | 29.6 | Balanced ✅ |
| **Dark** | 8,019 | 51.9% | 51.9% | 206.1 | Balanced ✅ |
| **Earth** | 8,465 | 51.1% | 51.1% | 17.0 | Balanced ✅ |
| **Lightning** | 18,003 | 51.0% | 51.0% | 30.2 | Balanced ✅ |
| **Plants** | 16,015 | 50.7% | 50.7% | 7.7 | Balanced ✅ |
| **Cosmic** | 15,082 | 48.9% | 48.9% | 21.7 | Balanced ✅ |
| **Beasts** | 15,068 | 48.6% | 48.6% | 23.0 | Balanced ✅ |
| **Wind** | 15,753 | 48.1% | 48.1% | 12.6 | Balanced ✅ |
| **Fey** | 13,846 | 47.0% | 47.0% | 1500.5 | Balanced ✅ |
| **Ice** | 18,008 | 46.5% | 46.5% | 31.9 | Undertuned ⚠️ |
| **Water** | 8,694 | 45.1% | 45.1% | 14.7 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,452 (49.6%) | 3,540 (48.1%) | 18.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 766 (60.1%) | 3,438 (50.3%) | 5.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,420 (52.6%) | 3,469 (48.4%) | 9.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 7,194 (60.0%) | 6,418 (47.6%) | 4.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 11,994 (51.5%) | 3,313 (47.1%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,747 (47.4%) | 5,268 (43.7%) | 0.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,209 (36.0%) | 3,439 (44.8%) | 7.7% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFE` | Fire | Debuff / Control | 32.8 -> **32.2** (-1.8%) | - | 32.8 -> **32.2** | Individual spell overtuned (WR: 55.1%, Casts: 1640, mult: 0.983) |
| `FFL` | Fire | Debuff / Control | 4.7 -> **4.6** (-2.1%) | - | 4.7 -> **4.6** | Individual spell overtuned (WR: 56.2%, Casts: 1367, mult: 0.979) |
| `FFD` | Fire | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1048.5 -> **1369.4** | 839.6 -> **959.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.7% vs 30% floor, Casts: 991). Increasing spread: b -14.9%, n +30.6% |
| `WWF` | Water | Conditional Strike | 2.5 -> **2.3** (-8.0%) | 493.0 -> **620.0** | 1235.0 -> **1428.3** | Class Water undertuned (WR: 45.1%, factor: 1.020); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.5% vs 30% floor, Casts: 1454). Increasing spread: b -12.6%, n +25.8% |
| `WWE` | Water | Setup - Weather | 91.1 -> **102.5** (+12.5%) | - | 91.1 -> **102.5** | Class Water undertuned (WR: 45.1%, factor: 1.020); Weather 'Raining' appliers undertuned (WR: 36.0%, casts: 2209) |
| `WWL` | Water | Buff / Sustain | 75.3 -> **76.8** (+2.0%) | - | 75.3 -> **76.8** | Class Water undertuned (WR: 45.1%, factor: 1.020) |
| `WWD` | Water | Buff / Sustain | 48.0 -> **48.9** (+1.9%) | - | 48.0 -> **48.9** | Class Water undertuned (WR: 45.1%, factor: 1.020) |
| `EEF` | Earth | Conditional Strike | 37.1 -> **42.7** (+15.1%) | 73.1 -> **88.9** | 2749.1 -> **3838.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.5% vs 30% floor, Casts: 1986). Increasing spread: b -10.6%, n +21.6%; Buffed setup spell [EEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `EEW` | Earth | Buff / Sustain | 19.1 -> **18.7** (-2.1%) | - | 19.1 -> **18.7** | Individual spell overtuned (WR: 56.6%, Casts: 1750, mult: 0.977) |
| `LLF` | Light | Conditional Strike | 6.4 -> **7.4** (+15.6%) | 1366.5 -> **1818.2** | 8752.0 -> **13462.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.7% vs 30% floor, Casts: 2198). Increasing spread: b -16.1%, n +33.1%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 168.2 -> **197.2** (+17.2%) | - | 168.2 -> **197.2** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Individual spell undertuned (WR: 44.2%, Casts: 1747, mult: 1.020) |
| `LLE` | Light | Setup - Weather | 150.2 -> **160.6** (+6.9%) | - | 150.2 -> **160.6** | Weather 'Sunny' appliers overtuned on own (WR: 60.1%); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 15.5 -> **15.2** (-1.9%) | - | 15.5 -> **15.2** | Individual spell overtuned (WR: 55.6%, Casts: 1361, mult: 0.981) |
| `LLD` | Light | Ultimate | 43.2 -> **43.2** (+0.0%) | 146.7 -> **190.7** | 6380.6 -> **8281.4** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1509). Shifted tuner focus: protected ultimate base floor at 43.2 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 2966.6 -> **4064.2** | 890.3 -> **813.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2459). Increasing spread: b -18.0%, n +37.0% |
| `DDE` | Dark | Setup - Weather | 303.6 -> **349.1** (+15.0%) | - | 303.6 -> **349.1** | Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDD` | Dark | Debuff / Control | 18.0 -> **17.7** (-1.7%) | - | 18.0 -> **17.7** | Individual spell overtuned (WR: 54.7%, Casts: 1367, mult: 0.984) |
| `FWW` | Ghostfire | Debuff / Control | 119.5 -> **131.2** (+9.8%) | - | 119.5 -> **131.2** | Status 'Cursed' appliers overtuned on own (WR: 54.3%); Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 325.4 -> **355.6** (+9.3%) | - | 325.4 -> **355.6** | Location 'Graveyard' appliers overtuned on own (WR: 57.2%); Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 261.8 -> **281.9** (+7.7%) | - | 261.8 -> **281.9** | Status 'Cursed' appliers overtuned on own (WR: 54.3%); Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 46.3 -> **44.8** (-3.2%) | 247.1 -> **309.1** | 11487.0 -> **13892.5** | Location 'Graveyard' beneficiaries overtuned (WR: 59.0%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 964). Shifted tuner focus: protected ultimate base floor at 46.3 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1360.3 -> **1801.4** | 1089.0 -> **1261.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 1621). Increasing spread: b -15.8%, n +32.4%; Individual spell undertuned (WR: 42.4%, Casts: 1621, mult: 1.026) |
| `WFW` | Ghostfire | Debuff / Control | 19.9 -> **19.3** (-3.0%) | - | 19.9 -> **19.3** | Individual spell overtuned (WR: 58.2%, Casts: 1590, mult: 0.971) |
| `WFE` | Ghostfire | Debuff / Control | 9.1 -> **9.5** (+4.4%) | - | 9.1 -> **9.5** | Status 'Bleeding' appliers overtuned on own (WR: 60.0%); Buffed setup spell [WFE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `WFL` | Ghostfire | Buff / Sustain | 48.8 -> **50.3** (+3.1%) | - | 48.8 -> **50.3** | Individual spell undertuned (WR: 41.5%, Casts: 2173, mult: 1.030) |
| `WFD` | Ghostfire | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 737.6 -> **933.4** | 812.5 -> **934.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.5% vs 30% floor, Casts: 1364). Increasing spread: b -13.0%, n +26.5%; Individual spell undertuned (WR: 38.4%, Casts: 1364, mult: 1.042) |
| `FEW` | Beasts | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 2949.3 -> **4119.1** | 885.1 -> **824.0** | Status 'Entangled' beneficiaries undertuned (WR: 43.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 1538). Increasing spread: b -17.6%, n +36.2% |
| `FEL` | Beasts | Buff / Sustain | 41.6 -> **43.0** (+3.4%) | - | 41.6 -> **43.0** | Individual spell undertuned (WR: 40.6%, Casts: 2840, mult: 1.033) |
| `EFF` | Beasts | Debuff / Control | 0.3 -> **0.2** (-33.3%) | 2586.9 -> **3528.3** | 776.4 -> **705.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 1237). Increasing spread: b -17.7%, n +36.4%; Individual spell overtuned (WR: 55.9%, Casts: 1237, mult: 0.980) |
| `EFW` | Beasts | Buff / Sustain | 20.3 -> **19.4** (-4.4%) | - | 20.3 -> **19.4** | Individual spell overtuned (WR: 62.6%, Casts: 1340, mult: 0.954) |
| `EFE` | Beasts | Buff / Sustain | 33.7 -> **34.7** (+3.0%) | - | 33.7 -> **34.7** | Individual spell undertuned (WR: 41.9%, Casts: 1518, mult: 1.028) |
| `EFL` | Beasts | Buff / Sustain | 1.1 -> **1.0** (-9.1%) | - | 1.1 -> **1.0** | Individual spell overtuned (WR: 77.6%, Casts: 773, mult: 0.891) |
| `EFD` | Beasts | Ultimate | 30.4 -> **33.6** (+10.5%) | 541.1 -> **534.3** | 16479.8 -> **17986.1** | Status 'Entangled' beneficiaries undertuned (WR: 43.7%); Location 'Jungle' beneficiaries undertuned (WR: 43.8%) |
| `FLF` | Lightning | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 4401.6 -> **6026.2** | 2641.6 -> **3013.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1740). Increasing spread: b -18.0%, n +36.9%; Individual spell undertuned (WR: 40.9%, Casts: 1740, mult: 1.032) |
| `FLW` | Lightning | Debuff / Control | 134.0 -> **151.1** (+12.8%) | - | 134.0 -> **151.1** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 55.8%, Casts: 2614, mult: 0.980) |
| `FLE` | Lightning | Setup - Weather | 141.7 -> **156.9** (+10.7%) | - | 141.7 -> **156.9** | Weather 'Storming' appliers overtuned on own (WR: 55.5%); Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLL` | Lightning | Buff / Sustain | 34.9 -> **35.7** (+2.3%) | - | 34.9 -> **35.7** | Individual spell undertuned (WR: 43.1%, Casts: 1466, mult: 1.024) |
| `FLD` | Lightning | Ultimate | 76.5 -> **75.5** (-1.3%) | 94.7 -> **121.1** | 7321.1 -> **9218.5** | Weather 'Storming' beneficiaries overtuned (WR: 54.0%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1573). Shifted tuner focus: protected ultimate base floor at 76.5 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 2135.4 -> **2857.9** | 854.6 -> **857.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.8% vs 30% floor, Casts: 999). Increasing spread: b -16.5%, n +33.8% |
| `LFL` | Lightning | Debuff / Control | 53.4 -> **61.4** (+15.0%) | 675.7 -> **879.6** | 36135.8 -> **54068.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 2296). Increasing spread: b -14.7%, n +30.2%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 1481.8 -> **1983.3** | 1779.4 -> **1984.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.8% vs 30% floor, Casts: 1476). Increasing spread: b -16.5%, n +33.8% |
| `FDF` | Blood | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 2974.0 -> **4074.4** | 892.5 -> **815.1** | Class Blood overtuned (WR: 53.7%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1161). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 58.8 -> **57.9** (-1.5%) | - | 58.8 -> **57.9** | Class Blood overtuned (WR: 53.7%, factor: 0.985) |
| `FDL` | Blood | Debuff / Control | 4.8 -> **4.9** (+2.1%) | - | 4.8 -> **4.9** | Class Blood overtuned (WR: 53.7%, factor: 0.985); Status 'Bleeding' appliers overtuned on own (WR: 60.0%) |
| `FDD` | Blood | Ultimate | 50.6 -> **49.8** (-1.6%) | 46.1 -> **59.9** | 2383.3 -> **3032.8** | Class Blood overtuned (WR: 53.7%, factor: 0.985); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1569). Shifted tuner focus: protected ultimate base floor at 50.6 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 1142.7 -> **1518.6** | 571.9 -> **607.8** | Class Blood overtuned (WR: 53.7%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 1586). Increasing spread: b -16.0%, n +32.9% |
| `DFE` | Blood | Buff / Sustain | 46.5 -> **47.1** (+1.3%) | - | 46.5 -> **47.1** | Class Blood overtuned (WR: 53.7%, factor: 0.985); Individual spell undertuned (WR: 42.0%, Casts: 1445, mult: 1.028) |
| `DFL` | Blood | Buff / Sustain | 29.4 -> **29.0** (-1.4%) | - | 29.4 -> **29.0** | Class Blood overtuned (WR: 53.7%, factor: 0.985) |
| `DFD` | Blood | Conditional Strike | 374.4 -> **418.9** (+11.9%) | 0.1 -> **0.1** | 411.8 -> **460.8** | Class Blood overtuned (WR: 53.7%, factor: 0.985); Condition triggers excessively (N=1 conditions, Trigger Rate: 94.6% vs 55% ceiling, WR: 60.3%). Compressing spread: b +17.9%, n -26.2% |
| `WEF` | Plants | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 656.8 -> **869.1** | 789.4 -> **870.1** | Location 'Jungle' beneficiaries undertuned (WR: 43.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.4% vs 30% floor, Casts: 1556). Increasing spread: b -14.2%, n +29.1% |
| `WEW` | Plants | Debuff / Control | 820.8 -> **943.9** (+15.0%) | - | 820.8 -> **943.9** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WED` | Plants | Conditional Strike | 14.0 -> **15.6** (+11.4%) | 28.2 -> **26.5** | 408.8 -> **429.0** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.4% vs 8% floor, Casts: 1448, WR: 40.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 40.2%, Casts: 1448, mult: 1.035) |
| `EWF` | Plants | Buff / Sustain | 0.9 -> **0.8** (-11.1%) | 486.9 -> **631.1** | 439.1 -> **505.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.9% vs 30% floor, Casts: 1929). Increasing spread: b -14.5%, n +29.6% |
| `EWW` | Plants | Debuff / Control | 1.7 -> **1.5** (-11.8%) | - | 1.7 -> **1.5** | Individual spell overtuned (WR: 80.3%, Casts: 1898, mult: 0.879) |
| `EWL` | Plants | Debuff / Control | 74.9 -> **73.4** (-2.0%) | - | 74.9 -> **73.4** | Individual spell overtuned (WR: 55.9%, Casts: 1988, mult: 0.980) |
| `EWD` | Plants | Conditional Strike | 2.6 -> **3.0** (+15.4%) | 2290.2 -> **3200.2** | 5957.1 -> **9603.6** | Status 'Bleeding' appliers overtuned on own (WR: 60.0%); Status 'Entangled' beneficiaries undertuned (WR: 43.7%) |
| `WLF` | Fey | Conditional Strike | 1.2 -> **1.1** (-8.3%) | 1545.0 -> **2003.2** | 1855.2 -> **2204.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.8% vs 30% floor, Casts: 1146). Increasing spread: b -14.5%, n +29.7%; Individual spell undertuned (WR: 38.2%, Casts: 1146, mult: 1.043) |
| `WLW` | Fey | Debuff / Control | 59.6 -> **60.6** (+1.7%) | - | 59.6 -> **60.6** | Status 'Cursed' appliers overtuned on own (WR: 54.3%); Individual spell undertuned (WR: 40.9%, Casts: 1710, mult: 1.032) |
| `WLE` | Fey | Setup - Location | 372.7 -> **409.5** (+9.9%) | - | 372.7 -> **409.5** | Location 'Enchanted Forest' appliers overtuned on own (WR: 56.5%); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 56.8 -> **55.7** (-1.9%) | - | 56.8 -> **55.7** | Individual spell overtuned (WR: 55.6%, Casts: 1325, mult: 0.981) |
| `WLD` | Fey | Ultimate | 22.0 -> **21.2** (-3.6%) | 1177.4 -> **1559.5** | 25924.8 -> **33082.6** | Location 'Enchanted Forest' beneficiaries undertuned (WR: 45.3%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1052). Shifted tuner focus: protected ultimate base floor at 22.0 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 25.9 -> **23.8** (-8.1%) | 316.9 -> **399.7** | 8233.6 -> **9536.7** | Location 'Enchanted Forest' beneficiaries undertuned (WR: 45.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.8% vs 30% floor, Casts: 2425). Increasing spread: b -11.7%, n +23.8% |
| `LWL` | Fey | Debuff / Control | 54.0 -> **55.0** (+1.9%) | - | 54.0 -> **55.0** | Individual spell undertuned (WR: 44.6%, Casts: 1367, mult: 1.018) |
| `LWD` | Fey | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 2974.0 -> **4074.4** | 1785.0 -> **2037.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 849). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 1.2 -> **1.1** (-8.3%) | 2851.6 -> **3809.7** | 3423.1 -> **4191.8** | Class Ice undertuned (WR: 46.5%, factor: 1.014); Weather 'Raining' beneficiaries undertuned (WR: 44.8%) |
| `WDE` | Ice | Setup - Weather | 34.8 -> **36.9** (+6.0%) | - | 34.8 -> **36.9** | Class Ice undertuned (WR: 46.5%, factor: 1.014); Individual spell undertuned (WR: 37.3%, Casts: 2583, mult: 1.047) |
| `WDL` | Ice | Debuff / Control | 39.0 -> **39.6** (+1.5%) | - | 39.0 -> **39.6** | Class Ice undertuned (WR: 46.5%, factor: 1.014) |
| `WDD` | Ice | Ultimate | 32.7 -> **32.5** (-0.6%) | 238.6 -> **288.8** | 7834.9 -> **9418.5** | Class Ice undertuned (WR: 46.5%, factor: 1.014); Weather 'Blizzard' beneficiaries overtuned (WR: 55.8%) |
| `DWF` | Ice | Debuff / Control | 37.7 -> **38.2** (+1.3%) | - | 37.7 -> **38.2** | Class Ice undertuned (WR: 46.5%, factor: 1.014) |
| `DWW` | Ice | Debuff / Control | 103.9 -> **106.9** (+2.9%) | - | 103.9 -> **106.9** | Class Ice undertuned (WR: 46.5%, factor: 1.014); Individual spell undertuned (WR: 45.5%, Casts: 1466, mult: 1.015) |
| `DWE` | Ice | Setup - Location | 40.4 -> **41.0** (+1.5%) | - | 40.4 -> **41.0** | Class Ice undertuned (WR: 46.5%, factor: 1.014) |
| `DWL` | Ice | Debuff / Control | 39.6 -> **41.4** (+4.5%) | - | 39.6 -> **41.4** | Class Ice undertuned (WR: 46.5%, factor: 1.014); Individual spell undertuned (WR: 41.2%, Casts: 1645, mult: 1.031) |
| `DWD` | Ice | Conditional Strike | 3.7 -> **3.4** (-8.1%) | 196.1 -> **240.2** | 729.3 -> **820.1** | Class Ice undertuned (WR: 46.5%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.4% vs 30% floor, Casts: 1554). Increasing spread: b -11.0%, n +22.5% |
| `ELF` | Wind | Conditional Strike | 2.4 -> **2.1** (-12.5%) | 1220.3 -> **1609.6** | 2931.1 -> **3382.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.1% vs 30% floor, Casts: 866). Increasing spread: b -15.6%, n +31.9%; Individual spell undertuned (WR: 42.5%, Casts: 866, mult: 1.026) |
| `ELW` | Wind | Debuff / Control | 111.0 -> **108.9** (-1.9%) | - | 111.0 -> **108.9** | Individual spell overtuned (WR: 55.7%, Casts: 2354, mult: 0.981) |
| `ELE` | Wind | Setup - Weather | 27.7 -> **28.5** (+2.9%) | - | 27.7 -> **28.5** | Individual spell undertuned (WR: 41.9%, Casts: 1524, mult: 1.029) |
| `ELD` | Wind | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 2257.9 -> **2997.5** | 3162.5 -> **3598.2** | Weather 'Raining' beneficiaries undertuned (WR: 44.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.3% vs 30% floor, Casts: 1139). Increasing spread: b -14.7%, n +30.0% |
| `LEF` | Wind | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1202.6 -> **1579.0** | 962.9 -> **1106.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.8% vs 30% floor, Casts: 1024). Increasing spread: b -15.3%, n +31.3%; Individual spell overtuned (WR: 57.3%, Casts: 1024, mult: 0.975) |
| `LEE` | Wind | Setup - Weather | 25.6 -> **26.2** (+2.3%) | - | 25.6 -> **26.2** | Individual spell undertuned (WR: 43.6%, Casts: 1602, mult: 1.022) |
| `LEL` | Wind | Buff / Sustain | 118.5 -> **121.4** (+2.4%) | - | 118.5 -> **121.4** | Individual spell undertuned (WR: 42.9%, Casts: 1997, mult: 1.025) |
| `EDF` | Poison | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 1050.7 -> **1394.9** | 525.9 -> **558.4** | Class Poison overtuned (WR: 55.9%, factor: 0.977); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.1% vs 30% floor, Casts: 2379). Increasing spread: b -16.0%, n +32.8% |
| `EDW` | Poison | Debuff / Control | 9.9 -> **9.5** (-4.0%) | - | 9.9 -> **9.5** | Class Poison overtuned (WR: 55.9%, factor: 0.977); Individual spell overtuned (WR: 55.8%, Casts: 2094, mult: 0.980) |
| `EDE` | Poison | Setup - Location | 52.0 -> **58.4** (+12.3%) | - | 52.0 -> **58.4** | Class Poison overtuned (WR: 55.9%, factor: 0.977); Buffed setup spell [EDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `EDD` | Poison | Ultimate | 51.7 -> **50.5** (-2.3%) | 31.9 -> **41.2** | 1700.9 -> **2131.1** | Class Poison overtuned (WR: 55.9%, factor: 0.977); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.7% vs 16% floor, Casts: 1384). Shifted tuner focus: protected ultimate base floor at 51.7 (hard-coded floor >= 20.0) and buffed appliers/setups (WFE, FDL, DFW, EWD, EDE) with +15% b tempo. |
| `DEF` | Poison | Conditional Strike | 29.9 -> **29.6** (-1.0%) | 1.4 -> **1.4** | 71.8 -> **71.0** | Class Poison overtuned (WR: 55.9%, factor: 0.977); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 54.0% within [30%-55%] target window, WR: 45.9%). |
| `DEW` | Poison | Debuff / Control | 12.4 -> **11.8** (-4.8%) | - | 12.4 -> **11.8** | Class Poison overtuned (WR: 55.9%, factor: 0.977); Individual spell overtuned (WR: 56.3%, Casts: 1960, mult: 0.979) |
| `DEE` | Poison | Debuff / Control | 39.4 -> **37.7** (-4.3%) | - | 39.4 -> **37.7** | Class Poison overtuned (WR: 55.9%, factor: 0.977); Individual spell overtuned (WR: 56.0%, Casts: 1078, mult: 0.980) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 1222.1 -> **1590.6** | 244.6 -> **318.3** | Class Poison overtuned (WR: 55.9%, factor: 0.977); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 961). Increasing spread: b -14.7%, n +30.1% |
| `DED` | Poison | Debuff / Control | 22.5 -> **22.0** (-2.2%) | - | 22.5 -> **22.0** | Class Poison overtuned (WR: 55.9%, factor: 0.977) |
| `LDW` | Cosmic | Debuff / Control | 43.5 -> **42.4** (-2.5%) | - | 43.5 -> **42.4** | Individual spell overtuned (WR: 57.5%, Casts: 2040, mult: 0.974) |
| `LDL` | Cosmic | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1654.2 -> **2242.8** | 1324.2 -> **1570.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.7% vs 30% floor, Casts: 1119). Increasing spread: b -17.3%, n +35.6%; Individual spell undertuned (WR: 46.2%, Casts: 1119, mult: 1.012) |
| `LDD` | Cosmic | Ultimate | 89.4 -> **97.9** (+9.5%) | 24.9 -> **23.4** | 2315.5 -> **2388.8** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2116, WR: 45.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 45.8%, Casts: 2116, mult: 1.014) |
| `DLF` | Cosmic | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1268.4 -> **1680.4** | 1015.5 -> **1177.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.4% vs 30% floor, Casts: 1604). Increasing spread: b -15.8%, n +32.5% |
| `DLW` | Cosmic | Direct Damage | 55.4 -> **54.1** (-2.3%) | - | 55.4 -> **54.1** | Individual spell overtuned (WR: 57.0%, Casts: 968, mult: 0.976) |
| `DLE` | Cosmic | Direct Damage | 53.9 -> **54.8** (+1.7%) | - | 53.9 -> **54.8** | Individual spell undertuned (WR: 45.2%, Casts: 1264, mult: 1.016) |
| `DLL` | Cosmic | Conditional Strike | 2.9 -> **2.6** (-10.3%) | 535.1 -> **704.0** | 1554.7 -> **1833.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.5% vs 30% floor, Casts: 1686). Increasing spread: b -15.4%, n +31.6%; Individual spell undertuned (WR: 34.0%, Casts: 1686, mult: 1.060) |
