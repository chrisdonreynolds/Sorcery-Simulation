# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T18:02:28Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 122.2s  
**Total Spells Tuned:** 107 / 125  

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
| **Blood** | 31,040 | 60.5% | 60.5% | 12.6 | Overtuned ⚠️ |
| **Earth** | 17,770 | 59.8% | 59.8% | 18.6 | Overtuned ⚠️ |
| **Ice** | 33,579 | 58.0% | 58.1% | 4.3 | Overtuned ⚠️ |
| **Ghostfire** | 18,242 | 52.8% | 52.8% | 2.5 | Balanced ✅ |
| **Plants** | 23,625 | 51.9% | 51.9% | 3.4 | Balanced ✅ |
| **Water** | 15,473 | 51.5% | 51.5% | 4.1 | Balanced ✅ |
| **Poison** | 30,401 | 50.4% | 50.4% | 3.3 | Balanced ✅ |
| **Fire** | 19,833 | 50.0% | 50.0% | 2.2 | Balanced ✅ |
| **Fey** | 13,325 | 49.3% | 49.3% | 4.7 | Balanced ✅ |
| **Cosmic** | 40,885 | 48.4% | 48.4% | 5.4 | Balanced ✅ |
| **Light** | 15,332 | 48.2% | 48.1% | 1.7 | Balanced ✅ |
| **Lightning** | 23,816 | 46.5% | 46.5% | 1.5 | Undertuned ⚠️ |
| **Beasts** | 20,511 | 44.3% | 44.3% | 2.2 | Undertuned ⚠️ |
| **Dark** | 14,021 | 40.0% | 40.0% | 4.8 | Undertuned ⚠️ |
| **Wind** | 28,836 | 38.2% | 38.2% | 0.8 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 20,710 (59.1%) | 9,855 (41.5%) | 3.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 3,335 (28.9%) | 10,378 (39.1%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,385 (75.4%) | 19,619 (32.9%) | 0.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,108 (82.7%) | 20,299 (36.4%) | 1.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 20,829 (55.6%) | 4,671 (30.1%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,649 (85.1%) | 4,678 (39.8%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 41 (83.0%) | 6,071 (53.5%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 15.2 -> **15.8** (+3.9%) | - | 15.2 -> **15.8** | Individual spell undertuned (WR: 38.8%, Casts: 158, mult: 1.040) |
| `FFW` | Fire | Debuff / Control | 8.5 -> **7.7** (-9.4%) | - | 8.5 -> **7.7** | Status 'Burning' appliers overtuned on own (WR: 75.4%) |
| `FFE` | Fire | Debuff / Control | 9.2 -> **8.5** (-7.6%) | - | 9.2 -> **8.5** | Individual spell overtuned (WR: 70.8%, Casts: 4128, mult: 0.920) |
| `FFD` | Fire | Conditional Strike | 1.2 -> **1.1** (-8.3%) | 1579.8 -> **2300.4** | 1897.0 -> **2531.5** | Status 'Burning' beneficiaries undertuned (WR: 32.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 10609). Increasing spread: b -17.7%, n +36.3% |
| `WWF` | Water | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 982.0 -> **1425.2** | 1376.2 -> **1711.4** | Status 'Burning' beneficiaries undertuned (WR: 32.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.4% vs 30% floor, Casts: 2085). Increasing spread: b -17.4%, n +35.8% |
| `WWE` | Water | Setup - Weather | 365.8 -> **287.1** (-21.5%) | - | 365.8 -> **287.1** | Weather 'Raining' appliers overtuned on own (WR: 83.0%); Individual spell overtuned (WR: 84.9%, Casts: 41, mult: 0.872) |
| `WWL` | Water | Buff / Sustain | 18.1 -> **16.1** (-11.0%) | - | 18.1 -> **16.1** | Individual spell overtuned (WR: 77.8%, Casts: 7171, mult: 0.890) |
| `EEF` | Earth | Conditional Strike | 1.9 -> **1.5** (-21.1%) | 1653.6 -> **2289.3** | 3143.7 -> **3435.5** | Class Earth overtuned (WR: 59.8%, factor: 0.961); Status 'Frosty' beneficiaries undertuned (WR: 41.5%) |
| `EEW` | Earth | Buff / Sustain | 47.2 -> **43.3** (-8.3%) | - | 47.2 -> **43.3** | Class Earth overtuned (WR: 59.8%, factor: 0.961); Individual spell overtuned (WR: 62.3%, Casts: 815, mult: 0.955) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 889.3 -> **1215.2** | 89.0 -> **121.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 2810). Increasing spread: b -17.8%, n +36.6%; Individual spell undertuned (WR: 40.9%, Casts: 2810, mult: 1.032) |
| `LLW` | Light | Debuff / Control | 14.2 -> **13.2** (-7.0%) | - | 14.2 -> **13.2** | Individual spell overtuned (WR: 68.4%, Casts: 624, mult: 0.930) |
| `LLE` | Light | Setup - Weather | 525.1 -> **609.8** (+16.1%) | - | 525.1 -> **609.8** | Weather 'Sunny' appliers undertuned (WR: 28.9%, casts: 3335); Individual spell undertuned (WR: 28.9%, Casts: 3335, mult: 1.081) |
| `LLD` | Light | Ultimate | 7.7 -> **6.1** (-20.8%) | 197.5 -> **282.4** | 1528.5 -> **1728.7** | Weather 'Sunny' beneficiaries undertuned (WR: 39.1%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 5669). Increasing spread: b -18.0%, n +37.0% |
| `DDF` | Dark | Conditional Strike | 0.5 -> **0.5** (+0.0%) | 1156.6 -> **1584.5** | 578.8 -> **792.8** | Class Dark undertuned (WR: 40.0%, factor: 1.040); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6630). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 13.8 -> **12.4** (-10.1%) | - | 13.8 -> **12.4** | Class Dark undertuned (WR: 40.0%, factor: 1.040); Individual spell overtuned (WR: 83.9%, Casts: 2862, mult: 0.863) |
| `DDE` | Dark | Setup - Weather | 291.8 -> **368.4** (+26.3%) | - | 291.8 -> **368.4** | Class Dark undertuned (WR: 40.0%, factor: 1.040); Weather 'Darkness' appliers undertuned (WR: 22.9%, casts: 197) |
| `DDL` | Dark | Debuff / Control | 10.5 -> **10.9** (+3.8%) | - | 10.5 -> **10.9** | Class Dark undertuned (WR: 40.0%, factor: 1.040) |
| `DDD` | Dark | Debuff / Control | 4.2 -> **4.4** (+4.8%) | - | 4.2 -> **4.4** | Class Dark undertuned (WR: 40.0%, factor: 1.040) |
| `FWF` | Ghostfire | Debuff / Control | 0.9 -> **0.7** (-22.2%) | - | 0.9 -> **0.7** | Status 'Burning' appliers overtuned on own (WR: 75.4%); Individual spell overtuned (WR: 85.4%, Casts: 447, mult: 0.856) |
| `FWW` | Ghostfire | Debuff / Control | 5.7 -> **5.4** (-5.3%) | - | 5.7 -> **5.4** | Status 'Cursed' appliers overtuned on own (WR: 66.1%); Individual spell undertuned (WR: 40.0%, Casts: 3, mult: 1.009) |
| `FWE` | Ghostfire | Setup - Location | 107.5 -> **128.6** (+19.6%) | - | 107.5 -> **128.6** | Location 'Graveyard' appliers undertuned (WR: 25.3%, casts: 66); Individual spell undertuned (WR: 24.4%, Casts: 66, mult: 1.101) |
| `FWL` | Ghostfire | Debuff / Control | 15.3 -> **13.9** (-9.2%) | - | 15.3 -> **13.9** | Status 'Cursed' appliers overtuned on own (WR: 66.1%); Individual spell overtuned (WR: 59.7%, Casts: 4011, mult: 0.966) |
| `FWD` | Ghostfire | Ultimate | 7.2 -> **5.8** (-19.4%) | 78.5 -> **101.5** | 572.4 -> **594.5** | Status 'Cursed' beneficiaries overtuned (WR: 57.0%); Location 'Graveyard' beneficiaries overtuned (WR: 57.2%) |
| `WFF` | Ghostfire | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 2370.4 -> **3401.6** | 2134.3 -> **2722.1** | Status 'Bleeding' beneficiaries undertuned (WR: 36.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.1% vs 30% floor, Casts: 1272). Increasing spread: b -17.6%, n +36.1% |
| `WFW` | Ghostfire | Debuff / Control | 5.5 -> **5.0** (-9.1%) | - | 5.5 -> **5.0** | Individual spell overtuned (WR: 73.7%, Casts: 5517, mult: 0.908) |
| `WFL` | Ghostfire | Buff / Sustain | 50.7 -> **47.1** (-7.1%) | - | 50.7 -> **47.1** | Individual spell overtuned (WR: 68.7%, Casts: 189, mult: 0.929) |
| `WFD` | Ghostfire | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 957.7 -> **1311.9** | 1054.6 -> **1312.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5571). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 23.8%, Casts: 5571, mult: 1.103) |
| `FEF` | Beasts | Debuff / Control | 13.0 -> **12.4** (-4.6%) | - | 13.0 -> **12.4** | Class Beasts undertuned (WR: 44.3%, factor: 1.023); Individual spell overtuned (WR: 67.2%, Casts: 3727, mult: 0.935) |
| `FEW` | Beasts | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1606.5 -> **2291.0** | 1286.0 -> **1604.4** | Class Beasts undertuned (WR: 44.3%, factor: 1.023); Status 'Entangled' beneficiaries undertuned (WR: 39.8%) |
| `FEE` | Beasts | Buff / Sustain | 73.7 -> **86.4** (+17.2%) | - | 73.7 -> **86.4** | Class Beasts undertuned (WR: 44.3%, factor: 1.023); Individual spell undertuned (WR: 13.9%, Casts: 3674, mult: 1.147) |
| `FEL` | Beasts | Buff / Sustain | 113.9 -> **127.7** (+12.1%) | - | 113.9 -> **127.7** | Class Beasts undertuned (WR: 44.3%, factor: 1.023); Individual spell undertuned (WR: 25.3%, Casts: 4933, mult: 1.097) |
| `EFF` | Beasts | Debuff / Control | 0.7 -> **0.7** (+0.0%) | 1032.8 -> **1414.9** | 723.7 -> **991.1** | Class Beasts undertuned (WR: 44.3%, factor: 1.023); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 181). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 71.5 -> **85.0** (+18.9%) | - | 71.5 -> **85.0** | Class Beasts undertuned (WR: 44.3%, factor: 1.023); Individual spell undertuned (WR: 10.3%, Casts: 336, mult: 1.163) |
| `EFE` | Beasts | Buff / Sustain | 16.7 -> **15.6** (-6.6%) | - | 16.7 -> **15.6** | Class Beasts undertuned (WR: 44.3%, factor: 1.023); Individual spell overtuned (WR: 73.0%, Casts: 1422, mult: 0.911) |
| `EFD` | Beasts | Ultimate | 4.0 -> **4.6** (+15.0%) | 371.3 -> **377.7** | 1489.2 -> **1742.0** | Class Beasts undertuned (WR: 44.3%, factor: 1.023); Status 'Entangled' beneficiaries undertuned (WR: 39.8%) |
| `FLF` | Lightning | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 1396.5 -> **2063.5** | 1257.8 -> **1651.6** | Class Lightning undertuned (WR: 46.5%, factor: 1.014); Status 'Stunned' beneficiaries undertuned (WR: 30.1%) |
| `FLW` | Lightning | Debuff / Control | 10.2 -> **9.5** (-6.9%) | - | 10.2 -> **9.5** | Class Lightning undertuned (WR: 46.5%, factor: 1.014); Status 'Stunned' appliers overtuned on own (WR: 55.6%) |
| `FLE` | Lightning | Setup - Weather | 219.4 -> **222.5** (+1.4%) | - | 219.4 -> **222.5** | Class Lightning undertuned (WR: 46.5%, factor: 1.014) |
| `FLL` | Lightning | Buff / Sustain | 34.4 -> **37.8** (+9.9%) | - | 34.4 -> **37.8** | Class Lightning undertuned (WR: 46.5%, factor: 1.014); Individual spell undertuned (WR: 28.2%, Casts: 537, mult: 1.084) |
| `FLD` | Lightning | Ultimate | 6.9 -> **8.4** (+21.7%) | 136.6 -> **154.5** | 949.4 -> **1306.2** | Class Lightning undertuned (WR: 46.5%, factor: 1.014); Status 'Stunned' beneficiaries undertuned (WR: 30.1%) |
| `LFF` | Lightning | Conditional Strike | 1.5 -> **1.3** (-13.3%) | 1096.8 -> **1502.6** | 1646.7 -> **1954.7** | Class Lightning undertuned (WR: 46.5%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6054). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 19.6 -> **18.2** (-7.1%) | - | 19.6 -> **18.2** | Class Lightning undertuned (WR: 46.5%, factor: 1.014); Individual spell overtuned (WR: 71.5%, Casts: 2835, mult: 0.917) |
| `LFE` | Lightning | Debuff / Control | 9.8 -> **9.0** (-8.2%) | - | 9.8 -> **9.0** | Class Lightning undertuned (WR: 46.5%, factor: 1.014); Status 'Stunned' appliers overtuned on own (WR: 55.6%) |
| `LFL` | Lightning | Debuff / Control | 1.5 -> **1.3** (-13.3%) | 772.9 -> **1058.9** | 1160.8 -> **1377.9** | Class Lightning undertuned (WR: 46.5%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2094). Increasing spread: b -18.0%, n +37.0% |
| `LFD` | Lightning | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1300.0 -> **1781.0** | 1040.8 -> **1247.4** | Class Lightning undertuned (WR: 46.5%, factor: 1.014); Status 'Stunned' appliers overtuned on own (WR: 55.6%) |
| `FDF` | Blood | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 1156.6 -> **1584.5** | 578.8 -> **634.2** | Class Blood overtuned (WR: 60.5%, factor: 0.958); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 652). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 80.8 -> **80.0** (-1.0%) | - | 80.8 -> **80.0** | Class Blood overtuned (WR: 60.5%, factor: 0.958); Individual spell undertuned (WR: 40.7%, Casts: 4555, mult: 1.033) |
| `FDE` | Blood | Setup - Weather | 67.2 -> **63.5** (-5.5%) | - | 67.2 -> **63.5** | Class Blood overtuned (WR: 60.5%, factor: 0.958); Individual spell overtuned (WR: 54.0%, Casts: 881, mult: 0.987) |
| `FDD` | Blood | Ultimate | 5.4 -> **4.1** (-24.1%) | 77.8 -> **106.6** | 425.5 -> **441.2** | Class Blood overtuned (WR: 60.5%, factor: 0.958); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 3940). Increasing spread: b -18.0%, n +37.0% |
| `DFF` | Blood | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 1793.6 -> **2549.6** | 1794.6 -> **2295.5** | Class Blood overtuned (WR: 60.5%, factor: 0.958); Status 'Bleeding' beneficiaries undertuned (WR: 36.4%) |
| `DFE` | Blood | Buff / Sustain | 174.5 -> **196.0** (+12.3%) | - | 174.5 -> **196.0** | Class Blood overtuned (WR: 60.5%, factor: 0.958); Individual spell undertuned (WR: 8.2%, Casts: 632, mult: 1.172) |
| `DFL` | Blood | Buff / Sustain | 7.0 -> **6.5** (-7.1%) | - | 7.0 -> **6.5** | Class Blood overtuned (WR: 60.5%, factor: 0.958); Individual spell overtuned (WR: 58.5%, Casts: 5783, mult: 0.970) |
| `DFD` | Blood | Conditional Strike | 125.0 -> **127.8** (+2.2%) | 0.1 -> **0.1** | 137.5 -> **140.6** | Class Blood overtuned (WR: 60.5%, factor: 0.958); Condition triggers excessively (N=1 conditions, Trigger Rate: 87.6% vs 55% ceiling, WR: 94.7%). Compressing spread: b +30.1%, n -37.5% |
| `WEF` | Plants | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1176.9 -> **1676.1** | 942.3 -> **1174.0** | Location 'Jungle' beneficiaries undertuned (WR: 40.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 414). Increasing spread: b -18.0%, n +37.0% |
| `WEW` | Plants | Debuff / Control | 82.8 -> **90.8** (+9.7%) | - | 82.8 -> **90.8** | Individual spell undertuned (WR: 25.2%, Casts: 384, mult: 1.097) |
| `WEE` | Plants | Setup - Location | 267.5 -> **294.7** (+10.2%) | - | 267.5 -> **294.7** | Location 'Jungle' appliers undertuned (WR: 36.2%, casts: 4755); Individual spell undertuned (WR: 36.2%, Casts: 4755, mult: 1.051) |
| `WEL` | Plants | Debuff / Control | 16.5 -> **12.7** (-23.0%) | - | 16.5 -> **12.7** | Status 'Entangled' appliers overtuned on own (WR: 85.1%); Individual spell overtuned (WR: 85.1%, Casts: 3649, mult: 0.858) |
| `WED` | Plants | Conditional Strike | 8.4 -> **6.8** (-19.0%) | 39.0 -> **53.4** | 336.0 -> **369.9** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4088). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 53.9%, Casts: 4088, mult: 0.987) |
| `EWF` | Plants | Buff / Sustain | 2.0 -> **1.9** (-5.0%) | 1731.4 -> **2475.4** | 3464.8 -> **4705.2** | Weather 'Sunny' beneficiaries undertuned (WR: 39.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4709). Increasing spread: b -18.0%, n +37.0% |
| `EWW` | Plants | Debuff / Control | 1.3 -> **1.1** (-15.4%) | - | 1.3 -> **1.1** | Individual spell overtuned (WR: 90.1%, Casts: 1672, mult: 0.835) |
| `EWL` | Plants | Debuff / Control | 18.6 -> **16.2** (-12.9%) | - | 18.6 -> **16.2** | Individual spell overtuned (WR: 82.5%, Casts: 3141, mult: 0.869) |
| `EWD` | Plants | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 1559.2 -> **2223.5** | 312.0 -> **444.9** | Status 'Bleeding' appliers overtuned on own (WR: 82.7%); Status 'Entangled' beneficiaries undertuned (WR: 39.8%) |
| `WLF` | Fey | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 816.1 -> **1086.5** | 1062.2 -> **1196.2** | Status 'Cursed' beneficiaries overtuned (WR: 57.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1). Increasing spread: b -18.0%, n +37.0% |
| `WLW` | Fey | Debuff / Control | 12.8 -> **11.1** (-13.3%) | - | 12.8 -> **11.1** | Status 'Cursed' appliers overtuned on own (WR: 66.1%); Individual spell overtuned (WR: 71.8%, Casts: 4538, mult: 0.916) |
| `WLE` | Fey | Setup - Location | 546.7 -> **716.2** (+31.0%) | - | 546.7 -> **716.2** | Location 'Enchanted Forest' appliers undertuned (WR: 8.9%, casts: 1635); Individual spell undertuned (WR: 8.8%, Casts: 1635, mult: 1.170) |
| `WLL` | Fey | Direct Damage | 39.0 -> **36.3** (-6.9%) | - | 39.0 -> **36.3** | Individual spell overtuned (WR: 68.5%, Casts: 1300, mult: 0.930) |
| `WLD` | Fey | Ultimate | 6.1 -> **6.6** (+8.2%) | 315.0 -> **307.5** | 1927.6 -> **2036.1** | Location 'Enchanted Forest' beneficiaries undertuned (WR: 40.4%); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1348, WR: 46.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `LWF` | Fey | Debuff / Control | 2.8 -> **2.4** (-14.3%) | 1061.9 -> **1511.0** | 2976.1 -> **3628.8** | Location 'Enchanted Forest' beneficiaries undertuned (WR: 40.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1409). Increasing spread: b -18.0%, n +37.0% |
| `LWW` | Fey | Debuff / Control | 57.7 -> **63.2** (+9.5%) | - | 57.7 -> **63.2** | Individual spell undertuned (WR: 25.5%, Casts: 1157, mult: 1.096) |
| `LWD` | Fey | Conditional Strike | 1.5 -> **1.2** (-20.0%) | 1156.6 -> **1584.5** | 1736.4 -> **1902.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 947). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 1.3 -> **1.0** (-23.1%) | 2340.2 -> **3204.7** | 3043.6 -> **3205.7** | Class Ice overtuned (WR: 58.0%, factor: 0.968); Status 'Stunned' appliers overtuned on own (WR: 55.6%) |
| `WDW` | Ice | Buff / Sustain | 38.7 -> **40.3** (+4.1%) | - | 38.7 -> **40.3** | Class Ice overtuned (WR: 58.0%, factor: 0.968); Status 'Frosty' appliers overtuned on own (WR: 59.1%) |
| `WDE` | Ice | Setup - Weather | 100.8 -> **106.8** (+6.0%) | - | 100.8 -> **106.8** | Class Ice overtuned (WR: 58.0%, factor: 0.968); Individual spell undertuned (WR: 25.6%, Casts: 1630, mult: 1.095) |
| `WDL` | Ice | Debuff / Control | 12.2 -> **10.4** (-14.8%) | - | 12.2 -> **10.4** | Class Ice overtuned (WR: 58.0%, factor: 0.968); Status 'Frosty' appliers overtuned on own (WR: 59.1%) |
| `WDD` | Ice | Ultimate | 6.4 -> **6.7** (+4.7%) | 79.9 -> **75.1** | 517.8 -> **509.9** | Class Ice overtuned (WR: 58.0%, factor: 0.968); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 3765, WR: 47.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DWF` | Ice | Debuff / Control | 10.9 -> **9.7** (-11.0%) | - | 10.9 -> **9.7** | Class Ice overtuned (WR: 58.0%, factor: 0.968); Status 'Frosty' appliers overtuned on own (WR: 59.1%) |
| `DWW` | Ice | Debuff / Control | 14.9 -> **12.7** (-14.8%) | - | 14.9 -> **12.7** | Class Ice overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 80.0%, Casts: 3461, mult: 0.880) |
| `DWE` | Ice | Setup - Location | 208.9 -> **202.2** (-3.2%) | - | 208.9 -> **202.2** | Class Ice overtuned (WR: 58.0%, factor: 0.968) |
| `DWL` | Ice | Debuff / Control | 13.6 -> **12.7** (-6.6%) | - | 13.6 -> **12.7** | Class Ice overtuned (WR: 58.0%, factor: 0.968); Status 'Frosty' appliers overtuned on own (WR: 59.1%) |
| `DWD` | Ice | Conditional Strike | 1.7 -> **1.3** (-23.5%) | 1303.8 -> **1783.1** | 2218.2 -> **2319.3** | Class Ice overtuned (WR: 58.0%, factor: 0.968); Status 'Frosty' beneficiaries undertuned (WR: 41.5%) |
| `ELF` | Wind | Conditional Strike | 3.1 -> **2.7** (-12.9%) | 2131.5 -> **3041.2** | 6610.8 -> **8213.9** | Class Wind undertuned (WR: 38.2%, factor: 1.047); Status 'Bleeding' beneficiaries undertuned (WR: 36.4%) |
| `ELW` | Wind | Debuff / Control | 22.7 -> **22.3** (-1.8%) | - | 22.7 -> **22.3** | Class Wind undertuned (WR: 38.2%, factor: 1.047); Individual spell overtuned (WR: 66.5%, Casts: 263, mult: 0.938) |
| `ELE` | Wind | Setup - Weather | 93.1 -> **105.7** (+13.5%) | - | 93.1 -> **105.7** | Class Wind undertuned (WR: 38.2%, factor: 1.047); Individual spell undertuned (WR: 28.1%, Casts: 4909, mult: 1.085) |
| `ELL` | Wind | Buff / Sustain | 87.4 -> **82.7** (-5.4%) | - | 87.4 -> **82.7** | Class Wind undertuned (WR: 38.2%, factor: 1.047); Individual spell overtuned (WR: 74.7%, Casts: 459, mult: 0.903) |
| `ELD` | Wind | Conditional Strike | 3.7 -> **3.2** (-13.5%) | 2082.8 -> **2853.4** | 7710.1 -> **9134.1** | Class Wind undertuned (WR: 38.2%, factor: 1.047); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4638). Increasing spread: b -18.0%, n +37.0% |
| `LEF` | Wind | Conditional Strike | 1.8 -> **1.6** (-11.1%) | 1616.3 -> **2355.1** | 2911.1 -> **3769.8** | Class Wind undertuned (WR: 38.2%, factor: 1.047); Status 'Burning' beneficiaries undertuned (WR: 32.9%) |
| `LEW` | Wind | Debuff / Control | 26.9 -> **24.2** (-10.0%) | - | 26.9 -> **24.2** | Class Wind undertuned (WR: 38.2%, factor: 1.047); Individual spell overtuned (WR: 84.7%, Casts: 138, mult: 0.860) |
| `LEE` | Wind | Setup - Weather | 141.3 -> **140.1** (-0.8%) | - | 141.3 -> **140.1** | Class Wind undertuned (WR: 38.2%, factor: 1.047); Individual spell overtuned (WR: 64.4%, Casts: 1446, mult: 0.947) |
| `LEL` | Wind | Buff / Sustain | 147.9 -> **171.9** (+16.2%) | - | 147.9 -> **171.9** | Class Wind undertuned (WR: 38.2%, factor: 1.047); Individual spell undertuned (WR: 22.2%, Casts: 6528, mult: 1.110) |
| `EDF` | Poison | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 745.8 -> **1011.9** | 448.1 -> **506.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 632). Increasing spread: b -17.4%, n +35.7% |
| `EDW` | Poison | Debuff / Control | 5.4 -> **5.0** (-7.4%) | - | 5.4 -> **5.0** | Individual spell overtuned (WR: 68.7%, Casts: 3604, mult: 0.929) |
| `EDE` | Poison | Setup - Location | 240.8 -> **314.1** (+30.4%) | - | 240.8 -> **314.1** | Location 'Swamp' appliers undertuned (WR: 10.0%, casts: 4459); Individual spell undertuned (WR: 9.9%, Casts: 4459, mult: 1.165) |
| `EDD` | Poison | Ultimate | 11.2 -> **8.9** (-20.5%) | 150.6 -> **208.9** | 1697.9 -> **1868.1** | Status 'Bleeding' beneficiaries undertuned (WR: 36.4%); Location 'Swamp' beneficiaries overtuned (WR: 59.6%) |
| `DEF` | Poison | Conditional Strike | 5.7 -> **4.5** (-21.1%) | 11.1 -> **14.9** | 69.0 -> **71.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.4% vs 30% floor, Casts: 826). Increasing spread: b -16.6%, n +34.2%; Individual spell overtuned (WR: 64.4%, Casts: 826, mult: 0.946) |
| `DEW` | Poison | Debuff / Control | 4.5 -> **4.3** (-4.4%) | - | 4.5 -> **4.3** | Individual spell overtuned (WR: 64.9%, Casts: 2995, mult: 0.944) |
| `DEE` | Poison | Debuff / Control | 19.0 -> **18.1** (-4.7%) | - | 19.0 -> **18.1** | Individual spell overtuned (WR: 63.4%, Casts: 220, mult: 0.951) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 2296.5 -> **3317.7** | 689.2 -> **995.6** | Status 'Bleeding' beneficiaries undertuned (WR: 36.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 7795). Increasing spread: b -18.0%, n +37.0% |
| `DED` | Poison | Debuff / Control | 18.9 -> **17.4** (-7.9%) | - | 18.9 -> **17.4** | Individual spell overtuned (WR: 71.0%, Casts: 3192, mult: 0.919) |
| `LDF` | Cosmic | Debuff / Control | 19.0 -> **19.8** (+4.2%) | - | 19.0 -> **19.8** | Individual spell undertuned (WR: 37.8%, Casts: 78, mult: 1.045) |
| `LDW` | Cosmic | Debuff / Control | 11.0 -> **9.6** (-12.7%) | - | 11.0 -> **9.6** | Status 'Stunned' appliers overtuned on own (WR: 55.6%); Individual spell overtuned (WR: 77.9%, Casts: 3382, mult: 0.889) |
| `LDE` | Cosmic | Setup - Location | 58.6 -> **67.6** (+15.4%) | - | 58.6 -> **67.6** | Individual spell undertuned (WR: 12.5%, Casts: 4819, mult: 1.153) |
| `LDL` | Cosmic | Conditional Strike | 1.2 -> **1.1** (-8.3%) | 963.9 -> **1318.6** | 1157.9 -> **1451.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 7222). Increasing spread: b -17.9%, n +36.8%; Individual spell undertuned (WR: 20.2%, Casts: 7222, mult: 1.119) |
| `LDD` | Cosmic | Ultimate | 7.8 -> **6.3** (-19.2%) | 96.7 -> **132.5** | 762.1 -> **841.0** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 7431). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 53.7%, Casts: 7431, mult: 0.988) |
| `DLF` | Cosmic | Conditional Strike | 1.5 -> **1.3** (-13.3%) | 873.6 -> **1196.8** | 1311.9 -> **1557.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2359). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 28.5%, Casts: 2359, mult: 1.083) |
| `DLW` | Cosmic | Direct Damage | 15.8 -> **14.3** (-9.5%) | - | 15.8 -> **14.3** | Individual spell overtuned (WR: 74.8%, Casts: 10743, mult: 0.903) |
| `DLE` | Cosmic | Direct Damage | 184.1 -> **212.2** (+15.3%) | - | 184.1 -> **212.2** | Individual spell undertuned (WR: 12.6%, Casts: 1216, mult: 1.152) |
| `DLL` | Cosmic | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 899.6 -> **1232.0** | 1441.0 -> **1726.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1643). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 30.6%, Casts: 1643, mult: 1.074) |
