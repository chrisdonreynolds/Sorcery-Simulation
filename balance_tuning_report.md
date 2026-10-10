# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T17:47:25Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 123.7s  
**Total Spells Tuned:** 111 / 125  

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
| **Blood** | 22,520 | 57.6% | 57.6% | 10.5 | Overtuned ⚠️ |
| **Dark** | 8,216 | 56.9% | 57.0% | 8.1 | Overtuned ⚠️ |
| **Lightning** | 23,255 | 54.9% | 55.0% | 2.6 | Overtuned ⚠️ |
| **Beasts** | 22,109 | 54.5% | 54.5% | 3.3 | Overtuned ⚠️ |
| **Fey** | 16,149 | 54.2% | 54.2% | 8.5 | Overtuned ⚠️ |
| **Ice** | 42,629 | 54.1% | 54.1% | 5.1 | Overtuned ⚠️ |
| **Plants** | 25,424 | 53.2% | 53.2% | 4.4 | Balanced ✅ |
| **Cosmic** | 36,385 | 52.8% | 52.8% | 7.6 | Balanced ✅ |
| **Fire** | 21,151 | 50.9% | 50.9% | 3.5 | Balanced ✅ |
| **Earth** | 12,257 | 50.3% | 50.3% | 12.6 | Balanced ✅ |
| **Ghostfire** | 20,075 | 49.7% | 49.7% | 2.2 | Balanced ✅ |
| **Light** | 16,899 | 48.1% | 48.1% | 1.5 | Balanced ✅ |
| **Poison** | 29,887 | 42.5% | 42.5% | 2.5 | Undertuned ⚠️ |
| **Water** | 10,888 | 39.9% | 39.8% | 3.5 | Undertuned ⚠️ |
| **Wind** | 24,560 | 37.3% | 37.3% | 1.6 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 21,661 (62.2%) | 8,671 (35.4%) | 3.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 4,038 (10.0%) | 9,101 (42.9%) | 1.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 8,704 (68.6%) | 13,699 (29.8%) | 1.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 6,858 (86.7%) | 21,705 (33.3%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 23,924 (55.8%) | 1,775 (51.8%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,632 (44.9%) | 5,514 (63.2%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 18 (40.9%) | 8,123 (38.1%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 19.1 -> **17.1** (-10.5%) | - | 19.1 -> **17.1** | Individual spell overtuned (WR: 76.8%, Casts: 156, mult: 0.894) |
| `FFW` | Fire | Debuff / Control | 9.7 -> **9.1** (-6.2%) | - | 9.7 -> **9.1** | Status 'Burning' appliers overtuned on own (WR: 68.6%) |
| `FFE` | Fire | Debuff / Control | 10.2 -> **9.5** (-6.9%) | - | 10.2 -> **9.5** | Individual spell overtuned (WR: 69.2%, Casts: 5131, mult: 0.927) |
| `FFD` | Fire | Conditional Strike | 1.4 -> **1.3** (-7.1%) | 735.3 -> **1080.3** | 1030.8 -> **1405.7** | Status 'Burning' beneficiaries undertuned (WR: 29.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.3% vs 30% floor, Casts: 8374). Increasing spread: b -17.5%, n +35.9% |
| `WWF` | Water | Conditional Strike | 1.6 -> **1.6** (+0.0%) | 513.0 -> **692.9** | 822.4 -> **1110.2** | Class Water undertuned (WR: 39.9%, factor: 1.041); Status 'Burning' beneficiaries undertuned (WR: 29.8%) |
| `WWE` | Water | Setup - Weather | 298.6 -> **327.5** (+9.7%) | - | 298.6 -> **327.5** | Class Water undertuned (WR: 39.9%, factor: 1.041); Weather 'Raining' appliers undertuned (WR: 40.9%, casts: 18) |
| `WWL` | Water | Buff / Sustain | 22.0 -> **20.5** (-6.8%) | - | 22.0 -> **20.5** | Class Water undertuned (WR: 39.9%, factor: 1.041); Individual spell overtuned (WR: 76.5%, Casts: 3686, mult: 0.895) |
| `WWD` | Water | Buff / Sustain | 30.7 -> **31.0** (+1.0%) | - | 30.7 -> **31.0** | Class Water undertuned (WR: 39.9%, factor: 1.041); Individual spell overtuned (WR: 58.1%, Casts: 1046, mult: 0.972) |
| `EEF` | Earth | Conditional Strike | 2.5 -> **2.2** (-12.0%) | 838.1 -> **1180.2** | 2097.8 -> **2598.6** | Status 'Frosty' beneficiaries undertuned (WR: 35.4%); Status 'Stunned' appliers overtuned on own (WR: 55.8%) |
| `EEW` | Earth | Buff / Sustain | 45.6 -> **44.9** (-1.5%) | - | 45.6 -> **44.9** | Individual spell overtuned (WR: 54.4%, Casts: 1794, mult: 0.985) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 479.3 -> **653.0** | 48.0 -> **65.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 3192). Increasing spread: b -17.6%, n +36.2%; Individual spell undertuned (WR: 40.9%, Casts: 3192, mult: 1.032) |
| `LLW` | Light | Debuff / Control | 16.6 -> **14.9** (-10.2%) | - | 16.6 -> **14.9** | Individual spell overtuned (WR: 75.7%, Casts: 1322, mult: 0.899) |
| `LLE` | Light | Setup - Weather | 305.2 -> **398.0** (+30.4%) | - | 305.2 -> **398.0** | Weather 'Sunny' appliers undertuned (WR: 10.0%, casts: 4038); Individual spell undertuned (WR: 10.0%, Casts: 4038, mult: 1.164) |
| `LLL` | Light | Buff / Sustain | 9.9 -> **9.4** (-5.1%) | - | 9.9 -> **9.4** | Individual spell overtuned (WR: 63.9%, Casts: 6176, mult: 0.949) |
| `LLD` | Light | Ultimate | 12.7 -> **9.7** (-23.6%) | 95.6 -> **134.7** | 1226.8 -> **1316.3** | Weather 'Sunny' beneficiaries undertuned (WR: 42.9%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 2171). Increasing spread: b -18.0%, n +37.0% |
| `DDF` | Dark | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 616.2 -> **844.2** | 432.0 -> **507.1** | Class Dark overtuned (WR: 56.9%, factor: 0.972); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2357). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 18.6 -> **16.6** (-10.8%) | - | 18.6 -> **16.6** | Class Dark overtuned (WR: 56.9%, factor: 0.972); Individual spell overtuned (WR: 71.3%, Casts: 3982, mult: 0.918) |
| `DDE` | Dark | Setup - Weather | 207.3 -> **244.1** (+17.8%) | - | 207.3 -> **244.1** | Class Dark overtuned (WR: 56.9%, factor: 0.972); Weather 'Darkness' appliers undertuned (WR: 23.1%, casts: 576) |
| `DDL` | Dark | Debuff / Control | 13.5 -> **12.3** (-8.9%) | - | 13.5 -> **12.3** | Class Dark overtuned (WR: 56.9%, factor: 0.972); Individual spell overtuned (WR: 67.0%, Casts: 466, mult: 0.936) |
| `DDD` | Dark | Debuff / Control | 4.6 -> **4.2** (-8.7%) | - | 4.6 -> **4.2** | Class Dark overtuned (WR: 56.9%, factor: 0.972); Individual spell overtuned (WR: 66.3%, Casts: 835, mult: 0.939) |
| `FWF` | Ghostfire | Debuff / Control | 1.4 -> **1.1** (-21.4%) | - | 1.4 -> **1.1** | Status 'Burning' appliers overtuned on own (WR: 68.6%); Individual spell overtuned (WR: 83.9%, Casts: 1214, mult: 0.863) |
| `FWE` | Ghostfire | Setup - Location | 108.7 -> **108.2** (-0.5%) | - | 108.7 -> **108.2** | Individual spell overtuned (WR: 57.1%, Casts: 2, mult: 0.995) |
| `FWL` | Ghostfire | Debuff / Control | 17.0 -> **16.3** (-4.1%) | - | 17.0 -> **16.3** | Individual spell overtuned (WR: 62.0%, Casts: 2073, mult: 0.956) |
| `FWD` | Ghostfire | Ultimate | 11.2 -> **8.8** (-21.4%) | 45.9 -> **57.3** | 525.3 -> **513.0** | Status 'Cursed' beneficiaries overtuned (WR: 61.0%); Location 'Graveyard' beneficiaries overtuned (WR: 61.6%) |
| `WFF` | Ghostfire | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 1167.9 -> **1636.1** | 1285.8 -> **1637.1** | Status 'Bleeding' beneficiaries undertuned (WR: 33.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.8% vs 30% floor, Casts: 2085). Increasing spread: b -15.3%, n +31.3% |
| `WFW` | Ghostfire | Debuff / Control | 6.6 -> **5.9** (-10.6%) | - | 6.6 -> **5.9** | Individual spell overtuned (WR: 75.7%, Casts: 2482, mult: 0.899) |
| `WFL` | Ghostfire | Buff / Sustain | 52.0 -> **50.7** (-2.5%) | - | 52.0 -> **50.7** | Individual spell overtuned (WR: 57.3%, Casts: 405, mult: 0.975) |
| `WFD` | Ghostfire | Conditional Strike | 1.4 -> **1.3** (-7.1%) | 530.4 -> **718.6** | 744.0 -> **935.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 7266). Increasing spread: b -17.3%, n +35.5%; Individual spell undertuned (WR: 23.9%, Casts: 7266, mult: 1.103) |
| `FEF` | Beasts | Debuff / Control | 15.1 -> **13.9** (-7.9%) | - | 15.1 -> **13.9** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 66.6%, Casts: 2820, mult: 0.938) |
| `FEW` | Beasts | Conditional Strike | 1.1 -> **0.9** (-18.2%) | 903.6 -> **1172.6** | 995.1 -> **1056.2** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Status 'Entangled' beneficiaries overtuned (WR: 63.2%) |
| `FEE` | Beasts | Buff / Sustain | 57.1 -> **63.0** (+10.3%) | - | 57.1 -> **63.0** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Individual spell undertuned (WR: 19.1%, Casts: 4527, mult: 1.124) |
| `FEL` | Beasts | Buff / Sustain | 95.9 -> **103.2** (+7.6%) | - | 95.9 -> **103.2** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Individual spell undertuned (WR: 25.4%, Casts: 3442, mult: 1.096) |
| `FED` | Beasts | Conditional Strike | 2.5 -> **2.6** (+4.0%) | 3.5 -> **3.5** | 11.2 -> **11.7** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 31.7% within [30%-55%] target window, WR: 31.9%). |
| `EFF` | Beasts | Debuff / Control | 1.0 -> **0.8** (-20.0%) | 550.3 -> **753.9** | 551.3 -> **603.9** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 428). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 53.0 -> **60.3** (+13.8%) | - | 53.0 -> **60.3** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Individual spell undertuned (WR: 11.2%, Casts: 157, mult: 1.159) |
| `EFE` | Beasts | Buff / Sustain | 21.1 -> **18.5** (-12.3%) | - | 21.1 -> **18.5** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 76.7%, Casts: 1298, mult: 0.895) |
| `EFL` | Beasts | Buff / Sustain | 1.4 -> **1.1** (-21.4%) | - | 1.4 -> **1.1** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 92.3%, Casts: 4004, mult: 0.826) |
| `EFD` | Beasts | Ultimate | 6.4 -> **4.9** (-23.4%) | 215.9 -> **271.0** | 1388.2 -> **1332.8** | Class Beasts overtuned (WR: 54.5%, factor: 0.982); Status 'Entangled' beneficiaries overtuned (WR: 63.2%) |
| `FLF` | Lightning | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 749.7 -> **1027.1** | 900.8 -> **1028.1** | Class Lightning overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1007). Increasing spread: b -18.0%, n +37.0% |
| `FLW` | Lightning | Debuff / Control | 11.9 -> **10.2** (-14.3%) | - | 11.9 -> **10.2** | Class Lightning overtuned (WR: 54.9%, factor: 0.980); Status 'Stunned' appliers overtuned on own (WR: 55.8%) |
| `FLE` | Lightning | Setup - Weather | 129.3 -> **164.0** (+26.8%) | - | 129.3 -> **164.0** | Class Lightning overtuned (WR: 54.9%, factor: 0.980); Weather 'Storming' appliers undertuned (WR: 12.0%, casts: 2464) |
| `FLL` | Lightning | Buff / Sustain | 35.4 -> **33.8** (-4.5%) | - | 35.4 -> **33.8** | Class Lightning overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 57.1%, Casts: 522, mult: 0.975) |
| `FLD` | Lightning | Ultimate | 10.9 -> **8.5** (-22.0%) | 76.9 -> **102.3** | 849.1 -> **878.0** | Class Lightning overtuned (WR: 54.9%, factor: 0.980); Weather 'Storming' beneficiaries overtuned (WR: 57.3%) |
| `LFF` | Lightning | Conditional Strike | 2.0 -> **1.7** (-15.0%) | 584.4 -> **800.6** | 1170.8 -> **1362.7** | Class Lightning overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1669). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 20.3 -> **19.9** (-2.0%) | - | 20.3 -> **19.9** | Class Lightning overtuned (WR: 54.9%, factor: 0.980) |
| `LFE` | Lightning | Debuff / Control | 12.7 -> **11.3** (-11.0%) | - | 12.7 -> **11.3** | Class Lightning overtuned (WR: 54.9%, factor: 0.980); Status 'Stunned' appliers overtuned on own (WR: 55.8%) |
| `LFL` | Lightning | Debuff / Control | 2.2 -> **1.8** (-18.2%) | 406.9 -> **570.5** | 897.4 -> **1028.7** | Class Lightning overtuned (WR: 54.9%, factor: 0.980); Weather 'Darkness' beneficiaries undertuned (WR: 44.2%) |
| `LFD` | Lightning | Conditional Strike | 1.1 -> **0.9** (-18.2%) | 701.9 -> **953.0** | 773.2 -> **858.6** | Class Lightning overtuned (WR: 54.9%, factor: 0.980); Status 'Stunned' appliers overtuned on own (WR: 55.8%) |
| `FDF` | Blood | Conditional Strike | 0.9 -> **0.7** (-22.2%) | 616.2 -> **844.2** | 555.5 -> **591.6** | Class Blood overtuned (WR: 57.6%, factor: 0.970); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1107). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 71.0 -> **76.2** (+7.3%) | - | 71.0 -> **76.2** | Class Blood overtuned (WR: 57.6%, factor: 0.970); Individual spell undertuned (WR: 22.8%, Casts: 2895, mult: 1.107) |
| `FDE` | Blood | Setup - Weather | 66.2 -> **69.2** (+4.5%) | - | 66.2 -> **69.2** | Class Blood overtuned (WR: 57.6%, factor: 0.970); Individual spell undertuned (WR: 29.5%, Casts: 412, mult: 1.079) |
| `FDL` | Blood | Debuff / Control | 0.7 -> **0.5** (-28.6%) | - | 0.7 -> **0.5** | Class Blood overtuned (WR: 57.6%, factor: 0.970); Status 'Bleeding' appliers overtuned on own (WR: 86.7%) |
| `FDD` | Blood | Ultimate | 6.7 -> **7.2** (+7.5%) | 59.0 -> **56.8** | 402.0 -> **416.2** | Class Blood overtuned (WR: 57.6%, factor: 0.970); Weather 'Darkness' beneficiaries undertuned (WR: 44.2%) |
| `DFF` | Blood | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 878.3 -> **1251.1** | 1143.1 -> **1377.3** | Class Blood overtuned (WR: 57.6%, factor: 0.970); Status 'Bleeding' beneficiaries undertuned (WR: 33.3%) |
| `DFE` | Blood | Buff / Sustain | 166.1 -> **170.2** (+2.5%) | - | 166.1 -> **170.2** | Class Blood overtuned (WR: 57.6%, factor: 0.970); Individual spell undertuned (WR: 34.8%, Casts: 152, mult: 1.057) |
| `DFL` | Blood | Buff / Sustain | 8.3 -> **8.0** (-3.6%) | - | 8.3 -> **8.0** | Class Blood overtuned (WR: 57.6%, factor: 0.970) |
| `DFD` | Blood | Conditional Strike | 116.5 -> **122.9** (+5.5%) | 0.1 -> **0.1** | 128.2 -> **135.2** | Class Blood overtuned (WR: 57.6%, factor: 0.970); Condition triggers excessively (N=1 conditions, Trigger Rate: 93.9% vs 55% ceiling, WR: 88.0%). Compressing spread: b +28.8%, n -37.0% |
| `WEF` | Plants | Conditional Strike | 1.1 -> **0.9** (-18.2%) | 662.7 -> **864.2** | 730.1 -> **778.7** | Location 'Jungle' beneficiaries overtuned (WR: 58.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.6% vs 30% floor, Casts: 2039). Increasing spread: b -17.0%, n +34.8% |
| `WEW` | Plants | Debuff / Control | 75.1 -> **72.1** (-4.0%) | - | 75.1 -> **72.1** | Individual spell overtuned (WR: 61.0%, Casts: 604, mult: 0.960) |
| `WEE` | Plants | Setup - Location | 207.8 -> **216.4** (+4.1%) | - | 207.8 -> **216.4** | Location 'Jungle' appliers undertuned (WR: 44.0%, casts: 2649); Individual spell undertuned (WR: 44.0%, Casts: 2649, mult: 1.020) |
| `WEL` | Plants | Debuff / Control | 13.8 -> **14.3** (+3.6%) | - | 13.8 -> **14.3** | Status 'Entangled' appliers undertuned (WR: 44.9%, casts: 2632); Individual spell undertuned (WR: 44.9%, Casts: 2632, mult: 1.017) |
| `WED` | Plants | Conditional Strike | 12.3 -> **10.0** (-18.7%) | 20.8 -> **28.5** | 268.1 -> **295.0** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 529). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 54.0%, Casts: 529, mult: 0.987) |
| `EWF` | Plants | Buff / Sustain | 2.4 -> **2.1** (-12.5%) | 846.5 -> **1183.2** | 2034.0 -> **2486.8** | Weather 'Sunny' beneficiaries undertuned (WR: 42.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.3% vs 30% floor, Casts: 6930). Increasing spread: b -17.5%, n +35.9% |
| `EWW` | Plants | Debuff / Control | 1.8 -> **1.5** (-16.7%) | - | 1.8 -> **1.5** | Individual spell overtuned (WR: 91.7%, Casts: 1458, mult: 0.828) |
| `EWL` | Plants | Debuff / Control | 21.8 -> **20.0** (-8.3%) | - | 21.8 -> **20.0** | Individual spell overtuned (WR: 71.3%, Casts: 8246, mult: 0.918) |
| `EWD` | Plants | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 877.0 -> **1138.1** | 263.4 -> **341.7** | Status 'Bleeding' appliers overtuned on own (WR: 86.7%); Status 'Entangled' beneficiaries overtuned (WR: 63.2%) |
| `WLF` | Fey | Conditional Strike | 1.9 -> **1.5** (-21.1%) | 454.9 -> **595.7** | 866.2 -> **895.1** | Class Fey overtuned (WR: 54.2%, factor: 0.983); Status 'Cursed' beneficiaries overtuned (WR: 61.0%) |
| `WLW` | Fey | Debuff / Control | 13.8 -> **13.6** (-1.4%) | - | 13.8 -> **13.6** | Class Fey overtuned (WR: 54.2%, factor: 0.983) |
| `WLE` | Fey | Setup - Location | 345.3 -> **405.7** (+17.5%) | - | 345.3 -> **405.7** | Class Fey overtuned (WR: 54.2%, factor: 0.983); Location 'Enchanted Forest' appliers undertuned (WR: 24.9%, casts: 1038) |
| `WLL` | Fey | Direct Damage | 49.0 -> **41.0** (-16.3%) | - | 49.0 -> **41.0** | Class Fey overtuned (WR: 54.2%, factor: 0.983); Individual spell overtuned (WR: 86.6%, Casts: 3825, mult: 0.851) |
| `WLD` | Fey | Ultimate | 8.8 -> **7.1** (-19.3%) | 159.9 -> **229.9** | 1415.9 -> **1639.4** | Class Fey overtuned (WR: 54.2%, factor: 0.983); Weather 'Darkness' beneficiaries undertuned (WR: 44.2%) |
| `LWF` | Fey | Debuff / Control | 3.7 -> **3.2** (-13.5%) | 556.8 -> **778.5** | 2063.9 -> **2494.4** | Class Fey overtuned (WR: 54.2%, factor: 0.983); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.6%) |
| `LWW` | Fey | Debuff / Control | 59.7 -> **53.8** (-9.9%) | - | 59.7 -> **53.8** | Class Fey overtuned (WR: 54.2%, factor: 0.983); Individual spell overtuned (WR: 71.6%, Casts: 199, mult: 0.917) |
| `LWL` | Fey | Debuff / Control | 200.3 -> **229.0** (+14.3%) | - | 200.3 -> **229.0** | Class Fey overtuned (WR: 54.2%, factor: 0.983); Individual spell undertuned (WR: 10.3%, Casts: 416, mult: 1.163) |
| `LWD` | Fey | Conditional Strike | 2.4 -> **2.0** (-16.7%) | 616.2 -> **844.2** | 1481.3 -> **1690.4** | Class Fey overtuned (WR: 54.2%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 469). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 2.2 -> **1.8** (-18.2%) | 1238.0 -> **1776.8** | 2725.8 -> **3200.0** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Status 'Stunned' appliers overtuned on own (WR: 55.8%) |
| `WDW` | Ice | Buff / Sustain | 45.5 -> **45.6** (+0.2%) | - | 45.5 -> **45.6** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 62.2%) |
| `WDE` | Ice | Setup - Weather | 93.4 -> **100.1** (+7.2%) | - | 93.4 -> **100.1** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Individual spell undertuned (WR: 26.9%, Casts: 4335, mult: 1.090) |
| `WDL` | Ice | Debuff / Control | 17.2 -> **14.8** (-14.0%) | - | 17.2 -> **14.8** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 62.2%) |
| `WDD` | Ice | Ultimate | 7.6 -> **8.5** (+11.8%) | 59.1 -> **61.6** | 456.8 -> **532.1** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Weather 'Blizzard' beneficiaries undertuned (WR: 36.8%) |
| `DWF` | Ice | Debuff / Control | 15.5 -> **13.4** (-13.5%) | - | 15.5 -> **13.4** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 62.2%) |
| `DWW` | Ice | Debuff / Control | 19.2 -> **17.0** (-11.5%) | - | 19.2 -> **17.0** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Individual spell overtuned (WR: 75.9%, Casts: 4532, mult: 0.898) |
| `DWE` | Ice | Setup - Location | 217.2 -> **220.6** (+1.6%) | - | 217.2 -> **220.6** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Location 'Tundra' appliers undertuned (WR: 45.3%, casts: 2750) |
| `DWL` | Ice | Debuff / Control | 17.9 -> **16.2** (-9.5%) | - | 17.9 -> **16.2** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 62.2%) |
| `DWD` | Ice | Conditional Strike | 2.6 -> **2.1** (-19.2%) | 650.4 -> **940.6** | 1693.6 -> **1977.4** | Class Ice overtuned (WR: 54.1%, factor: 0.983); Status 'Frosty' beneficiaries undertuned (WR: 35.4%) |
| `ELF` | Wind | Conditional Strike | 3.8 -> **3.5** (-7.9%) | 1014.0 -> **1477.2** | 3857.0 -> **5173.7** | Class Wind undertuned (WR: 37.3%, factor: 1.051); Status 'Bleeding' beneficiaries undertuned (WR: 33.3%) |
| `ELW` | Wind | Debuff / Control | 25.6 -> **23.8** (-7.0%) | - | 25.6 -> **23.8** | Class Wind undertuned (WR: 37.3%, factor: 1.051); Individual spell overtuned (WR: 78.9%, Casts: 1019, mult: 0.885) |
| `ELE` | Wind | Setup - Weather | 73.9 -> **80.0** (+8.3%) | - | 73.9 -> **80.0** | Class Wind undertuned (WR: 37.3%, factor: 1.051); Individual spell undertuned (WR: 41.3%, Casts: 4165, mult: 1.031) |
| `ELL` | Wind | Buff / Sustain | 85.7 -> **86.9** (+1.4%) | - | 85.7 -> **86.9** | Class Wind undertuned (WR: 37.3%, factor: 1.051); Individual spell overtuned (WR: 59.8%, Casts: 558, mult: 0.965) |
| `ELD` | Wind | Conditional Strike | 4.9 -> **4.5** (-8.2%) | 1115.1 -> **1600.2** | 5468.9 -> **7205.4** | Class Wind undertuned (WR: 37.3%, factor: 1.051); Weather 'Raining' beneficiaries undertuned (WR: 38.1%) |
| `LEF` | Wind | Conditional Strike | 2.2 -> **2.0** (-9.1%) | 746.9 -> **1103.5** | 1645.4 -> **2209.0** | Class Wind undertuned (WR: 37.3%, factor: 1.051); Status 'Burning' beneficiaries undertuned (WR: 29.8%) |
| `LEW` | Wind | Debuff / Control | 23.4 -> **26.6** (+13.7%) | - | 23.4 -> **26.6** | Class Wind undertuned (WR: 37.3%, factor: 1.051); Individual spell undertuned (WR: 28.3%, Casts: 501, mult: 1.084) |
| `LEE` | Wind | Setup - Weather | 94.1 -> **116.2** (+23.5%) | - | 94.1 -> **116.2** | Class Wind undertuned (WR: 37.3%, factor: 1.051); Individual spell undertuned (WR: 7.5%, Casts: 3427, mult: 1.176) |
| `LEL` | Wind | Buff / Sustain | 121.9 -> **134.2** (+10.1%) | - | 121.9 -> **134.2** | Class Wind undertuned (WR: 37.3%, factor: 1.051); Individual spell undertuned (WR: 37.0%, Casts: 652, mult: 1.048) |
| `EDF` | Poison | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 419.4 -> **554.4** | 378.4 -> **444.3** | Class Poison undertuned (WR: 42.5%, factor: 1.030); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.8% vs 30% floor, Casts: 536). Increasing spread: b -15.7%, n +32.2% |
| `EDW` | Poison | Debuff / Control | 4.9 -> **5.3** (+8.2%) | - | 4.9 -> **5.3** | Class Poison undertuned (WR: 42.5%, factor: 1.030); Individual spell undertuned (WR: 37.0%, Casts: 1174, mult: 1.048) |
| `EDE` | Poison | Setup - Location | 139.5 -> **185.3** (+32.8%) | - | 139.5 -> **185.3** | Class Poison undertuned (WR: 42.5%, factor: 1.030); Location 'Swamp' appliers undertuned (WR: 12.8%, casts: 4126) |
| `EDD` | Poison | Ultimate | 17.3 -> **14.0** (-19.1%) | 77.6 -> **108.4** | 1359.8 -> **1531.6** | Class Poison undertuned (WR: 42.5%, factor: 1.030); Status 'Bleeding' beneficiaries undertuned (WR: 33.3%) |
| `DEF` | Poison | Conditional Strike | 7.2 -> **6.8** (-5.6%) | 6.7 -> **8.1** | 55.4 -> **61.9** | Class Poison undertuned (WR: 42.5%, factor: 1.030); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 19.7% vs 30% floor, Casts: 1421). Increasing spread: b -10.1%, n +20.6% |
| `DEE` | Poison | Debuff / Control | 14.2 -> **15.8** (+11.3%) | - | 14.2 -> **15.8** | Class Poison undertuned (WR: 42.5%, factor: 1.030); Individual spell undertuned (WR: 29.8%, Casts: 72, mult: 1.078) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 1080.3 -> **1578.8** | 324.4 -> **473.9** | Class Poison undertuned (WR: 42.5%, factor: 1.030); Status 'Bleeding' beneficiaries undertuned (WR: 33.3%) |
| `DED` | Poison | Debuff / Control | 16.9 -> **16.6** (-1.8%) | - | 16.9 -> **16.6** | Class Poison undertuned (WR: 42.5%, factor: 1.030); Individual spell overtuned (WR: 62.5%, Casts: 2570, mult: 0.954) |
| `LDF` | Cosmic | Debuff / Control | 22.1 -> **21.3** (-3.6%) | - | 22.1 -> **21.3** | Individual spell overtuned (WR: 60.1%, Casts: 1734, mult: 0.964) |
| `LDW` | Cosmic | Debuff / Control | 12.3 -> **11.0** (-10.6%) | - | 12.3 -> **11.0** | Status 'Stunned' appliers overtuned on own (WR: 55.8%); Individual spell overtuned (WR: 72.1%, Casts: 4127, mult: 0.914) |
| `LDE` | Cosmic | Setup - Location | 50.0 -> **56.4** (+12.8%) | - | 50.0 -> **56.4** | Individual spell undertuned (WR: 18.3%, Casts: 1060, mult: 1.127) |
| `LDL` | Cosmic | Conditional Strike | 1.7 -> **1.5** (-11.8%) | 513.6 -> **703.6** | 874.8 -> **1056.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5565). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 33.7%, Casts: 5565, mult: 1.061) |
| `LDD` | Cosmic | Ultimate | 11.9 -> **9.8** (-17.6%) | 51.5 -> **70.6** | 624.8 -> **701.7** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 5129). Increasing spread: b -18.0%, n +37.0% |
| `DLF` | Cosmic | Conditional Strike | 2.2 -> **1.9** (-13.6%) | 465.5 -> **637.7** | 1026.3 -> **1213.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2021). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 34.8%, Casts: 2021, mult: 1.057) |
| `DLW` | Cosmic | Direct Damage | 20.1 -> **18.4** (-8.5%) | - | 20.1 -> **18.4** | Individual spell overtuned (WR: 71.6%, Casts: 9819, mult: 0.917) |
| `DLE` | Cosmic | Direct Damage | 151.5 -> **175.4** (+15.8%) | - | 151.5 -> **175.4** | Individual spell undertuned (WR: 11.4%, Casts: 3031, mult: 1.158) |
| `DLL` | Cosmic | Conditional Strike | 2.3 -> **2.0** (-13.0%) | 469.2 -> **657.2** | 1081.5 -> **1316.4** | Weather 'Darkness' beneficiaries undertuned (WR: 44.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1318). Increasing spread: b -17.9%, n +36.9% |
