# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T00:10:04Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 575.9s  
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
| **Poison** | 21,389 | 55.5% | 55.5% | 9.3 | Overtuned ⚠️ |
| **Blood** | 19,525 | 53.0% | 53.0% | 15.7 | Balanced ✅ |
| **Earth** | 8,836 | 52.6% | 52.6% | 20.1 | Balanced ✅ |
| **Ghostfire** | 21,037 | 51.4% | 51.4% | 15.1 | Balanced ✅ |
| **Fire** | 9,982 | 50.6% | 50.6% | 12.9 | Balanced ✅ |
| **Light** | 9,639 | 50.6% | 50.6% | 8.8 | Balanced ✅ |
| **Plants** | 21,979 | 50.3% | 50.3% | 9.4 | Balanced ✅ |
| **Wind** | 17,528 | 50.3% | 50.3% | 7.1 | Balanced ✅ |
| **Cosmic** | 17,776 | 49.3% | 49.3% | 15.0 | Balanced ✅ |
| **Lightning** | 21,196 | 48.9% | 48.9% | 11.7 | Balanced ✅ |
| **Beasts** | 20,539 | 48.7% | 48.6% | 7.8 | Balanced ✅ |
| **Dark** | 10,450 | 48.1% | 48.1% | 13.0 | Balanced ✅ |
| **Ice** | 18,914 | 48.1% | 48.1% | 12.8 | Balanced ✅ |
| **Water** | 9,890 | 47.4% | 47.4% | 8.4 | Balanced ✅ |
| **Fey** | 16,488 | 47.2% | 47.2% | 22.3 | Balanced ✅ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,746 (49.2%) | 3,035 (49.7%) | 20.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,488 (43.5%) | 4,428 (51.3%) | 12.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,508 (55.5%) | 4,401 (49.0%) | 11.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,877 (64.7%) | 8,947 (47.4%) | 5.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,580 (49.2%) | 4,925 (46.8%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,811 (50.1%) | 6,060 (47.5%) | 2.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,972 (40.4%) | 5,503 (45.2%) | 6.1% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 40.5 -> **39.7** (-2.0%) | - | 40.5 -> **39.7** | Status 'Burning' appliers overtuned on own (WR: 55.5%) |
| `FFL` | Fire | Debuff / Control | 5.2 -> **4.9** (-5.8%) | - | 5.2 -> **4.9** | Status 'Burning' appliers overtuned on own (WR: 55.5%); Individual spell overtuned (WR: 61.1%, Casts: 2289, mult: 0.960) |
| `FFD` | Fire | Conditional Strike | 3.6 -> **3.1** (-13.9%) | 64.8 -> **84.7** | 236.9 -> **265.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.5% vs 30% floor, Casts: 1681). Increasing spread: b -15.0%, n +30.8%; Individual spell undertuned (WR: 45.0%, Casts: 1681, mult: 1.017) |
| `WWF` | Water | Conditional Strike | 7.9 -> **7.1** (-10.1%) | 45.6 -> **55.6** | 368.1 -> **401.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.1% vs 30% floor, Casts: 1174). Increasing spread: b -10.7%, n +21.9% |
| `WWE` | Water | Setup - Weather | 42.6 -> **45.5** (+6.8%) | - | 42.6 -> **45.5** | Weather 'Raining' appliers undertuned (WR: 40.4%, casts: 1972); Individual spell undertuned (WR: 40.4%, Casts: 1972, mult: 1.034) |
| `WWL` | Water | Buff / Sustain | 70.0 -> **70.8** (+1.1%) | - | 70.0 -> **70.8** | Individual spell undertuned (WR: 46.4%, Casts: 2262, mult: 1.012) |
| `EEF` | Earth | Conditional Strike | 12.9 -> **14.6** (+13.2%) | 15.0 -> **17.8** | 206.4 -> **274.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 22.3% vs 30% floor, Casts: 1390). Increasing spread: b -9.1%, n +18.4%; Buffed setup spell [EEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `EEW` | Earth | Buff / Sustain | 28.5 -> **27.6** (-3.2%) | - | 28.5 -> **27.6** | Individual spell overtuned (WR: 58.7%, Casts: 1415, mult: 0.969) |
| `EED` | Earth | Direct Damage | 7.2 -> **7.4** (+2.8%) | - | 7.2 -> **7.4** | Individual spell undertuned (WR: 43.0%, Casts: 2109, mult: 1.024) |
| `LLF` | Light | Conditional Strike | 4.3 -> **4.9** (+14.0%) | 78.5 -> **104.5** | 341.8 -> **517.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.7% vs 30% floor, Casts: 2903). Increasing spread: b -16.1%, n +33.1%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 47.0 -> **54.0** (+14.9%) | - | 47.0 -> **54.0** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LLE` | Light | Setup - Weather | 70.4 -> **84.7** (+20.3%) | - | 70.4 -> **84.7** | Weather 'Sunny' appliers undertuned (WR: 43.5%, casts: 1488); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 22.5 -> **21.8** (-3.1%) | - | 22.5 -> **21.8** | Individual spell overtuned (WR: 58.7%, Casts: 1456, mult: 0.969) |
| `LLD` | Light | Ultimate | 34.9 -> **34.9** (+0.0%) | 27.2 -> **35.4** | 984.2 -> **1270.4** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1454). Shifted tuner focus: protected ultimate base floor at 34.9 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 2.1 -> **1.7** (-19.0%) | 127.4 -> **174.5** | 269.6 -> **298.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1890). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 60.8 -> **72.1** (+18.6%) | - | 60.8 -> **72.1** | Buffed setup spell [DDW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell undertuned (WR: 41.1%, Casts: 2106, mult: 1.031) |
| `DDE` | Dark | Setup - Weather | 75.3 -> **86.6** (+15.0%) | - | 75.3 -> **86.6** | Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 30.0 -> **35.2** (+17.3%) | - | 30.0 -> **35.2** | Buffed setup spell [DDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell undertuned (WR: 44.3%, Casts: 2835, mult: 1.019) |
| `DDD` | Dark | Debuff / Control | 24.4 -> **23.6** (-3.3%) | - | 24.4 -> **23.6** | Individual spell overtuned (WR: 59.2%, Casts: 1476, mult: 0.967) |
| `FWF` | Ghostfire | Debuff / Control | 26.3 -> **25.3** (-3.8%) | - | 26.3 -> **25.3** | Status 'Burning' appliers overtuned on own (WR: 55.5%); Individual spell overtuned (WR: 56.0%, Casts: 2042, mult: 0.979) |
| `FWW` | Ghostfire | Debuff / Control | 34.4 -> **39.6** (+15.1%) | - | 34.4 -> **39.6** | Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 87.3 -> **100.4** (+15.0%) | - | 87.3 -> **100.4** | Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 87.3 -> **100.4** (+15.0%) | - | 87.3 -> **100.4** | Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 49.0 -> **47.8** (-2.4%) | 25.3 -> **31.9** | 1288.7 -> **1572.6** | Location 'Graveyard' beneficiaries overtuned (WR: 57.2%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1752). Shifted tuner focus: protected ultimate base floor at 49.0 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 3.6 -> **3.0** (-16.7%) | 69.3 -> **91.4** | 253.1 -> **277.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 2191). Increasing spread: b -15.5%, n +31.9% |
| `WFE` | Ghostfire | Debuff / Control | 26.0 -> **22.6** (-13.1%) | - | 26.0 -> **22.6** | Status 'Bleeding' appliers overtuned on own (WR: 64.7%); Individual spell overtuned (WR: 71.7%, Casts: 1605, mult: 0.916) |
| `WFD` | Ghostfire | Conditional Strike | 4.2 -> **3.7** (-11.9%) | 60.4 -> **78.3** | 257.9 -> **293.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.9% vs 30% floor, Casts: 2160). Increasing spread: b -14.4%, n +29.6%; Individual spell undertuned (WR: 44.9%, Casts: 2160, mult: 1.017) |
| `FEF` | Beasts | Debuff / Control | 35.7 -> **42.0** (+17.6%) | - | 35.7 -> **42.0** | Buffed setup spell [FEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell undertuned (WR: 43.6%, Casts: 1222, mult: 1.022) |
| `FEW` | Beasts | Conditional Strike | 2.2 -> **1.9** (-13.6%) | 131.1 -> **177.9** | 290.6 -> **339.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 1555). Increasing spread: b -17.4%, n +35.7%; Individual spell undertuned (WR: 41.7%, Casts: 1555, mult: 1.029) |
| `FEE` | Beasts | Buff / Sustain | 29.1 -> **30.2** (+3.8%) | - | 29.1 -> **30.2** | Individual spell undertuned (WR: 39.6%, Casts: 2688, mult: 1.037) |
| `FEL` | Beasts | Buff / Sustain | 32.1 -> **34.0** (+5.9%) | - | 32.1 -> **34.0** | Individual spell undertuned (WR: 33.9%, Casts: 3204, mult: 1.060) |
| `EFF` | Beasts | Debuff / Control | 2.7 -> **2.2** (-18.5%) | 114.7 -> **156.5** | 312.4 -> **346.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 1750). Increasing spread: b -17.7%, n +36.5% |
| `EFL` | Beasts | Buff / Sustain | 5.3 -> **4.5** (-15.1%) | - | 5.3 -> **4.5** | Individual spell overtuned (WR: 89.0%, Casts: 1727, mult: 0.840) |
| `EFD` | Beasts | Ultimate | 36.3 -> **35.3** (-2.8%) | 37.8 -> **48.7** | 1408.4 -> **1754.4** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.9% vs 16% floor, Casts: 2001). Shifted tuner focus: protected ultimate base floor at 36.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo.; Individual spell overtuned (WR: 57.8%, Casts: 2001, mult: 0.973) |
| `FLF` | Lightning | Conditional Strike | 2.3 -> **1.9** (-17.4%) | 155.6 -> **212.5** | 360.2 -> **405.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 2654). Increasing spread: b -17.8%, n +36.6%; Individual spell undertuned (WR: 44.5%, Casts: 2654, mult: 1.018) |
| `FLW` | Lightning | Debuff / Control | 55.2 -> **60.5** (+9.6%) | - | 55.2 -> **60.5** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 63.0%, Casts: 1517, mult: 0.952) |
| `FLE` | Lightning | Setup - Weather | 33.1 -> **39.1** (+18.1%) | - | 33.1 -> **39.1** | Weather 'Storming' appliers undertuned (WR: 45.8%, casts: 1489); Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLL` | Lightning | Buff / Sustain | 27.5 -> **28.4** (+3.3%) | - | 27.5 -> **28.4** | Individual spell undertuned (WR: 41.1%, Casts: 1663, mult: 1.032) |
| `FLD` | Lightning | Ultimate | 76.0 -> **76.0** (+0.0%) | 8.3 -> **10.8** | 706.8 -> **896.8** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 2271). Shifted tuner focus: protected ultimate base floor at 76.0 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 2.6 -> **2.2** (-15.4%) | 105.6 -> **143.5** | 277.2 -> **317.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.3% vs 30% floor, Casts: 1413). Increasing spread: b -17.5%, n +35.9%; Individual spell undertuned (WR: 44.1%, Casts: 1413, mult: 1.020) |
| `LFW` | Lightning | Buff / Sustain | 32.3 -> **31.3** (-3.1%) | - | 32.3 -> **31.3** | Individual spell overtuned (WR: 59.0%, Casts: 1967, mult: 0.968) |
| `LFL` | Lightning | Debuff / Control | 21.6 -> **24.5** (+13.4%) | 52.9 -> **67.8** | 1164.2 -> **1685.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.7% vs 30% floor, Casts: 2680). Increasing spread: b -13.7%, n +28.1%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LFD` | Lightning | Conditional Strike | 5.4 -> **4.9** (-9.3%) | 94.6 -> **118.1** | 516.2 -> **583.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.6% vs 30% floor, Casts: 2839). Increasing spread: b -12.2%, n +24.8%; Individual spell undertuned (WR: 42.1%, Casts: 2839, mult: 1.028) |
| `FDF` | Blood | Conditional Strike | 2.3 -> **1.9** (-17.4%) | 127.7 -> **174.9** | 296.0 -> **334.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1677). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 43.5%, Casts: 1677, mult: 1.022) |
| `FDW` | Blood | Direct Damage | 69.4 -> **71.9** (+3.6%) | - | 69.4 -> **71.9** | Individual spell undertuned (WR: 40.1%, Casts: 2375, mult: 1.036) |
| `FDL` | Blood | Debuff / Control | 18.5 -> **15.9** (-14.1%) | - | 18.5 -> **15.9** | Status 'Bleeding' appliers overtuned on own (WR: 64.7%); Individual spell overtuned (WR: 73.7%, Casts: 2641, mult: 0.908) |
| `FDD` | Blood | Ultimate | 53.4 -> **57.7** (+8.1%) | 6.6 -> **6.2** | 405.8 -> **415.4** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1860, WR: 47.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 2.9 -> **2.5** (-13.8%) | 68.7 -> **89.4** | 202.1 -> **226.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.3% vs 30% floor, Casts: 1442). Increasing spread: b -14.7%, n +30.1% |
| `DFE` | Blood | Buff / Sustain | 40.6 -> **42.4** (+4.4%) | - | 40.6 -> **42.4** | Individual spell undertuned (WR: 37.9%, Casts: 1930, mult: 1.044) |
| `DFL` | Blood | Buff / Sustain | 32.7 -> **33.4** (+2.1%) | - | 32.7 -> **33.4** | Individual spell undertuned (WR: 43.7%, Casts: 872, mult: 1.022) |
| `DFD` | Blood | Conditional Strike | 126.2 -> **144.0** (+14.1%) | 0.1 -> **0.1** | 138.8 -> **158.4** | Condition triggers excessively (N=1 conditions, Trigger Rate: 96.1% vs 55% ceiling, WR: 50.7%). Compressing spread: b +14.1%, n -22.6% |
| `WEF` | Plants | Conditional Strike | 4.1 -> **3.6** (-12.2%) | 52.6 -> **68.0** | 219.8 -> **248.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.3% vs 30% floor, Casts: 1446). Increasing spread: b -14.3%, n +29.2%; Individual spell undertuned (WR: 41.8%, Casts: 1446, mult: 1.029) |
| `WEW` | Plants | Debuff / Control | 150.6 -> **175.3** (+16.4%) | - | 150.6 -> **175.3** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 46.2%, Casts: 1635, mult: 1.012) |
| `WED` | Plants | Conditional Strike | 6.7 -> **5.5** (-17.9%) | 35.9 -> **49.2** | 247.2 -> **276.1** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1275). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 3.9 -> **3.5** (-10.3%) | 39.6 -> **48.2** | 158.3 -> **172.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.5% vs 30% floor, Casts: 2974). Increasing spread: b -10.6%, n +21.6% |
| `EWW` | Plants | Debuff / Control | 6.9 -> **5.9** (-14.5%) | - | 6.9 -> **5.9** | Individual spell overtuned (WR: 84.4%, Casts: 2095, mult: 0.861) |
| `EWL` | Plants | Debuff / Control | 64.5 -> **66.5** (+3.1%) | - | 64.5 -> **66.5** | Individual spell undertuned (WR: 41.2%, Casts: 3424, mult: 1.031) |
| `EWD` | Plants | Conditional Strike | 9.7 -> **7.9** (-18.6%) | 112.1 -> **149.1** | 1097.1 -> **1185.8** | Status 'Bleeding' appliers overtuned on own (WR: 64.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.8% vs 30% floor, Casts: 2504). Increasing spread: b -16.1%, n +33.0% |
| `WLF` | Fey | Conditional Strike | 3.5 -> **3.0** (-14.3%) | 93.1 -> **123.5** | 329.3 -> **373.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.2% vs 30% floor, Casts: 1285). Increasing spread: b -15.9%, n +32.7%; Individual spell undertuned (WR: 43.2%, Casts: 1285, mult: 1.023) |
| `WLW` | Fey | Debuff / Control | 51.9 -> **52.9** (+1.9%) | - | 51.9 -> **52.9** | Individual spell undertuned (WR: 44.3%, Casts: 1728, mult: 1.019) |
| `WLE` | Fey | Setup - Location | 115.7 -> **133.1** (+15.0%) | - | 115.7 -> **133.1** | Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 56.2 -> **55.1** (-2.0%) | - | 56.2 -> **55.1** | Individual spell overtuned (WR: 55.7%, Casts: 1292, mult: 0.981) |
| `WLD` | Fey | Ultimate | 27.8 -> **27.8** (+0.0%) | 94.0 -> **122.2** | 2641.0 -> **3425.0** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1704). Shifted tuner focus: protected ultimate base floor at 27.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 16.2 -> **18.6** (+14.8%) | 37.5 -> **47.0** | 623.7 -> **892.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.1% vs 30% floor, Casts: 1708). Increasing spread: b -12.4%, n +25.2%; Buffed setup spell [LWF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LWL` | Fey | Debuff / Control | 41.4 -> **42.3** (+2.2%) | - | 41.4 -> **42.3** | Individual spell undertuned (WR: 43.6%, Casts: 1991, mult: 1.022) |
| `LWD` | Fey | Conditional Strike | 2.7 -> **2.2** (-18.5%) | 127.7 -> **174.9** | 347.5 -> **387.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1719). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 45.6%, Casts: 1719, mult: 1.014) |
| `WDF` | Ice | Conditional Strike | 4.4 -> **3.9** (-11.4%) | 118.8 -> **158.8** | 527.1 -> **623.2** | Weather 'Raining' beneficiaries undertuned (WR: 45.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.0% vs 30% floor, Casts: 3062). Increasing spread: b -15.2%, n +31.1% |
| `WDW` | Ice | Buff / Sustain | 14.4 -> **14.2** (-1.4%) | - | 14.4 -> **14.2** | Individual spell overtuned (WR: 53.7%, Casts: 3161, mult: 0.988) |
| `WDL` | Ice | Debuff / Control | 44.1 -> **44.9** (+1.8%) | - | 44.1 -> **44.9** | Individual spell undertuned (WR: 44.9%, Casts: 1314, mult: 1.017) |
| `WDD` | Ice | Ultimate | 27.4 -> **27.1** (-1.1%) | 60.5 -> **75.4** | 1685.1 -> **2070.4** | Weather 'Blizzard' beneficiaries overtuned (WR: 53.6%); Location 'Tundra' beneficiaries overtuned (WR: 53.6%) |
| `DWW` | Ice | Debuff / Control | 48.5 -> **54.3** (+12.0%) | - | 48.5 -> **54.3** | Buffed setup spell [DWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 57.6%, Casts: 1711, mult: 0.974) |
| `DWE` | Ice | Setup - Location | 32.0 -> **33.0** (+3.1%) | - | 32.0 -> **33.0** | Location 'Tundra' appliers undertuned (WR: 45.5%, casts: 1481); Individual spell undertuned (WR: 45.5%, Casts: 1481, mult: 1.015) |
| `DWL` | Ice | Debuff / Control | 42.8 -> **43.9** (+2.6%) | - | 42.8 -> **43.9** | Individual spell undertuned (WR: 42.5%, Casts: 1908, mult: 1.026) |
| `DWD` | Ice | Conditional Strike | 8.7 -> **7.9** (-9.2%) | 21.8 -> **26.6** | 198.4 -> **218.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.2% vs 30% floor, Casts: 1645). Increasing spread: b -10.7%, n +21.8%; Individual spell undertuned (WR: 45.1%, Casts: 1645, mult: 1.016) |
| `ELF` | Wind | Conditional Strike | 7.9 -> **6.9** (-12.7%) | 73.5 -> **97.4** | 588.6 -> **679.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.3% vs 30% floor, Casts: 1225). Increasing spread: b -15.9%, n +32.6%; Individual spell undertuned (WR: 40.7%, Casts: 1225, mult: 1.033) |
| `ELW` | Wind | Debuff / Control | 52.3 -> **59.4** (+13.6%) | - | 52.3 -> **59.4** | Buffed setup spell [ELW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 53.8%, Casts: 2254, mult: 0.988) |
| `ELE` | Wind | Setup - Weather | 22.8 -> **23.1** (+1.3%) | - | 22.8 -> **23.1** | Individual spell undertuned (WR: 45.9%, Casts: 1639, mult: 1.013) |
| `ELD` | Wind | Conditional Strike | 4.7 -> **3.9** (-17.0%) | 102.7 -> **139.0** | 487.4 -> **546.0** | Weather 'Raining' beneficiaries undertuned (WR: 45.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.0% vs 30% floor, Casts: 2441). Increasing spread: b -16.0%, n +32.8% |
| `LEF` | Wind | Conditional Strike | 3.0 -> **2.6** (-13.3%) | 76.2 -> **98.5** | 231.6 -> **258.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.3% vs 30% floor, Casts: 1546). Increasing spread: b -14.3%, n +29.2% |
| `LEL` | Wind | Buff / Sustain | 48.3 -> **54.6** (+13.0%) | - | 48.3 -> **54.6** | Buffed setup spell [LEL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 55.2%, Casts: 1579, mult: 0.983) |
| `EDF` | Poison | Conditional Strike | 2.6 -> **2.1** (-19.2%) | 76.8 -> **98.5** | 202.3 -> **209.0** | Class Poison overtuned (WR: 55.5%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.6% vs 30% floor, Casts: 2046). Increasing spread: b -13.8%, n +28.2% |
| `EDW` | Poison | Debuff / Control | 16.7 -> **15.8** (-5.4%) | - | 16.7 -> **15.8** | Class Poison overtuned (WR: 55.5%, factor: 0.978); Individual spell overtuned (WR: 59.2%, Casts: 1939, mult: 0.968) |
| `EDE` | Poison | Setup - Location | 51.1 -> **50.0** (-2.2%) | - | 51.1 -> **50.0** | Class Poison overtuned (WR: 55.5%, factor: 0.978) |
| `EDL` | Poison | Debuff / Control | 2.7 -> **2.2** (-18.5%) | - | 2.7 -> **2.2** | Class Poison overtuned (WR: 55.5%, factor: 0.978); Individual spell overtuned (WR: 86.4%, Casts: 2495, mult: 0.852) |
| `EDD` | Poison | Ultimate | 31.5 -> **33.3** (+5.7%) | 26.7 -> **25.1** | 872.5 -> **869.1** | Class Poison overtuned (WR: 55.5%, factor: 0.978); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.6% vs 16% floor, Casts: 1718, WR: 48.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DEF` | Poison | Conditional Strike | 33.5 -> **32.8** (-2.1%) | 1.4 -> **1.4** | 80.4 -> **78.7** | Class Poison overtuned (WR: 55.5%, factor: 0.978); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 46.5% within [30%-55%] target window, WR: 48.9%). |
| `DEW` | Poison | Debuff / Control | 18.7 -> **17.9** (-4.3%) | - | 18.7 -> **17.9** | Class Poison overtuned (WR: 55.5%, factor: 0.978); Individual spell overtuned (WR: 56.5%, Casts: 2936, mult: 0.978) |
| `DEE` | Poison | Debuff / Control | 23.9 -> **26.9** (+12.6%) | - | 23.9 -> **26.9** | Class Poison overtuned (WR: 55.5%, factor: 0.978); Buffed setup spell [DEE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 74.2 -> **98.7** | 15.0 -> **19.9** | Class Poison overtuned (WR: 55.5%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.8% vs 30% floor, Casts: 2371). Increasing spread: b -16.1%, n +33.0% |
| `DED` | Poison | Debuff / Control | 22.6 -> **22.4** (-0.9%) | - | 22.6 -> **22.4** | Class Poison overtuned (WR: 55.5%, factor: 0.978); Individual spell undertuned (WR: 45.7%, Casts: 2306, mult: 1.014) |
| `LDF` | Cosmic | Debuff / Control | 67.7 -> **77.9** (+15.1%) | - | 67.7 -> **77.9** | Buffed setup spell [LDF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LDW` | Cosmic | Debuff / Control | 45.5 -> **44.4** (-2.4%) | - | 45.5 -> **44.4** | Individual spell overtuned (WR: 56.8%, Casts: 3069, mult: 0.977) |
| `LDL` | Cosmic | Conditional Strike | 3.7 -> **3.3** (-10.8%) | 82.8 -> **111.2** | 310.1 -> **370.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.3% vs 30% floor, Casts: 2113). Increasing spread: b -16.7%, n +34.2%; Individual spell undertuned (WR: 34.5%, Casts: 2113, mult: 1.058) |
| `LDD` | Cosmic | Ultimate | 62.4 -> **62.4** (+0.0%) | 6.6 -> **8.6** | 474.2 -> **599.0** | Ultimate payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1495). Shifted tuner focus: protected ultimate base floor at 62.4 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDW, DDL, DEE, DFW, DWW, ELW, LEL, DLL, FEF, LWF) with +15% b tempo. |
| `DLF` | Cosmic | Conditional Strike | 4.4 -> **3.7** (-15.9%) | 79.8 -> **104.8** | 355.5 -> **391.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.9% vs 30% floor, Casts: 2360). Increasing spread: b -15.3%, n +31.3% |
| `DLL` | Cosmic | Conditional Strike | 9.9 -> **8.5** (-14.1%) | 41.2 -> **52.8** | 417.8 -> **457.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.6% vs 30% floor, Casts: 1637). Increasing spread: b -13.8%, n +28.2% |
