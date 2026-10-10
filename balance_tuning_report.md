# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T17:53:59Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 123.3s  
**Total Spells Tuned:** 108 / 125  

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
| **Blood** | 27,278 | 63.9% | 63.9% | 9.4 | Overtuned ⚠️ |
| **Ice** | 37,940 | 63.3% | 63.3% | 5.1 | Overtuned ⚠️ |
| **Cosmic** | 33,633 | 57.6% | 57.6% | 7.4 | Overtuned ⚠️ |
| **Dark** | 10,149 | 56.3% | 56.3% | 6.5 | Overtuned ⚠️ |
| **Earth** | 13,304 | 50.2% | 50.2% | 12.0 | Balanced ✅ |
| **Fire** | 30,896 | 50.1% | 50.1% | 3.2 | Balanced ✅ |
| **Ghostfire** | 21,062 | 48.4% | 48.4% | 2.2 | Balanced ✅ |
| **Light** | 15,620 | 48.3% | 48.3% | 1.8 | Balanced ✅ |
| **Water** | 14,049 | 47.9% | 47.9% | 4.6 | Balanced ✅ |
| **Lightning** | 26,829 | 45.4% | 45.4% | 2.0 | Undertuned ⚠️ |
| **Poison** | 29,361 | 45.2% | 45.2% | 2.0 | Undertuned ⚠️ |
| **Beasts** | 22,335 | 44.5% | 44.5% | 2.4 | Undertuned ⚠️ |
| **Plants** | 23,589 | 41.4% | 41.4% | 3.0 | Undertuned ⚠️ |
| **Fey** | 22,729 | 39.0% | 39.0% | 3.6 | Undertuned ⚠️ |
| **Wind** | 24,377 | 38.4% | 38.4% | 1.7 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 21,517 (68.4%) | 12,157 (41.9%) | 1.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 3,870 (7.0%) | 9,226 (32.5%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 12,236 (69.7%) | 18,231 (30.4%) | 2.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,754 (84.0%) | 32,887 (34.6%) | 0.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 20,874 (50.7%) | 4,932 (51.6%) | 0.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 720 (34.6%) | 4,622 (50.4%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 37 (33.7%) | 5,187 (59.7%) | 0.6% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 17.1 -> **15.2** (-11.1%) | - | 17.1 -> **15.2** | Individual spell overtuned (WR: 78.3%, Casts: 149, mult: 0.888) |
| `FFW` | Fire | Debuff / Control | 9.1 -> **8.5** (-6.6%) | - | 9.1 -> **8.5** | Status 'Burning' appliers overtuned on own (WR: 69.7%) |
| `FFE` | Fire | Debuff / Control | 9.5 -> **9.2** (-3.2%) | - | 9.5 -> **9.2** | Individual spell overtuned (WR: 59.7%, Casts: 7797, mult: 0.966) |
| `FFD` | Fire | Conditional Strike | 1.3 -> **1.2** (-7.7%) | 1080.3 -> **1579.8** | 1405.7 -> **1897.0** | Status 'Burning' beneficiaries undertuned (WR: 30.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.7% vs 30% floor, Casts: 11673). Increasing spread: b -17.3%, n +35.6% |
| `WWF` | Water | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 692.9 -> **982.0** | 1110.2 -> **1376.2** | Status 'Burning' beneficiaries undertuned (WR: 30.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 1707). Increasing spread: b -15.3%, n +31.4% |
| `WWE` | Water | Setup - Weather | 327.5 -> **365.8** (+11.7%) | - | 327.5 -> **365.8** | Weather 'Raining' appliers undertuned (WR: 33.7%, casts: 37); Individual spell undertuned (WR: 32.6%, Casts: 37, mult: 1.056) |
| `WWL` | Water | Buff / Sustain | 20.5 -> **18.1** (-11.7%) | - | 20.5 -> **18.1** | Individual spell overtuned (WR: 79.3%, Casts: 6488, mult: 0.883) |
| `WWD` | Water | Buff / Sustain | 31.0 -> **28.9** (-6.8%) | - | 31.0 -> **28.9** | Individual spell overtuned (WR: 67.5%, Casts: 376, mult: 0.934) |
| `EEF` | Earth | Conditional Strike | 2.2 -> **1.9** (-13.6%) | 1180.2 -> **1653.6** | 2598.6 -> **3143.7** | Status 'Frosty' beneficiaries undertuned (WR: 41.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 9210). Increasing spread: b -17.4%, n +35.7% |
| `EEW` | Earth | Buff / Sustain | 44.9 -> **47.2** (+5.1%) | - | 44.9 -> **47.2** | Individual spell undertuned (WR: 36.0%, Casts: 430, mult: 1.052) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 653.0 -> **889.3** | 65.4 -> **89.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.0% vs 30% floor, Casts: 1857). Increasing spread: b -17.6%, n +36.2%; Individual spell overtuned (WR: 54.5%, Casts: 1857, mult: 0.985) |
| `LLW` | Light | Debuff / Control | 14.9 -> **14.2** (-4.7%) | - | 14.9 -> **14.2** | Individual spell overtuned (WR: 62.6%, Casts: 1402, mult: 0.954) |
| `LLE` | Light | Setup - Weather | 398.0 -> **525.1** (+31.9%) | - | 398.0 -> **525.1** | Weather 'Sunny' appliers undertuned (WR: 7.0%, casts: 3870); Individual spell undertuned (WR: 7.0%, Casts: 3870, mult: 1.178) |
| `LLL` | Light | Buff / Sustain | 9.4 -> **8.8** (-6.4%) | - | 9.4 -> **8.8** | Individual spell overtuned (WR: 67.8%, Casts: 4593, mult: 0.933) |
| `LLD` | Light | Ultimate | 9.7 -> **7.7** (-20.6%) | 134.7 -> **197.5** | 1316.3 -> **1528.5** | Weather 'Sunny' beneficiaries undertuned (WR: 32.5%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 3898). Increasing spread: b -18.0%, n +37.0% |
| `DDF` | Dark | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 844.2 -> **1156.6** | 507.1 -> **578.8** | Class Dark overtuned (WR: 56.3%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4173). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 16.6 -> **13.8** (-16.9%) | - | 16.6 -> **13.8** | Class Dark overtuned (WR: 56.3%, factor: 0.975); Individual spell overtuned (WR: 86.8%, Casts: 3938, mult: 0.850) |
| `DDE` | Dark | Setup - Weather | 244.1 -> **291.8** (+19.5%) | - | 244.1 -> **291.8** | Class Dark overtuned (WR: 56.3%, factor: 0.975); Weather 'Darkness' appliers undertuned (WR: 21.3%, casts: 559) |
| `DDL` | Dark | Debuff / Control | 12.3 -> **10.5** (-14.6%) | - | 12.3 -> **10.5** | Class Dark overtuned (WR: 56.3%, factor: 0.975); Individual spell overtuned (WR: 81.5%, Casts: 1294, mult: 0.873) |
| `FWF` | Ghostfire | Debuff / Control | 1.1 -> **0.9** (-18.2%) | - | 1.1 -> **0.9** | Status 'Burning' appliers overtuned on own (WR: 69.7%); Individual spell overtuned (WR: 80.8%, Casts: 959, mult: 0.877) |
| `FWW` | Ghostfire | Debuff / Control | 6.2 -> **5.7** (-8.1%) | - | 6.2 -> **5.7** | Status 'Cursed' appliers overtuned on own (WR: 62.1%); Individual spell overtuned (WR: 69.0%, Casts: 17, mult: 0.958) |
| `FWE` | Ghostfire | Setup - Location | 108.2 -> **107.5** (-0.6%) | - | 108.2 -> **107.5** | Individual spell overtuned (WR: 56.2%, Casts: 4, mult: 0.994) |
| `FWL` | Ghostfire | Debuff / Control | 16.3 -> **15.3** (-6.1%) | - | 16.3 -> **15.3** | Status 'Cursed' appliers overtuned on own (WR: 62.1%); Individual spell overtuned (WR: 55.9%, Casts: 3388, mult: 0.980) |
| `FWD` | Ghostfire | Ultimate | 8.8 -> **7.2** (-18.2%) | 57.3 -> **78.5** | 513.0 -> **572.4** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 859). Increasing spread: b -18.0%, n +37.0% |
| `WFF` | Ghostfire | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 1636.1 -> **2370.4** | 1637.1 -> **2134.3** | Status 'Bleeding' beneficiaries undertuned (WR: 34.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 4475). Increasing spread: b -17.7%, n +36.5% |
| `WFW` | Ghostfire | Debuff / Control | 5.9 -> **5.5** (-6.8%) | - | 5.9 -> **5.5** | Individual spell overtuned (WR: 68.4%, Casts: 4275, mult: 0.930) |
| `WFD` | Ghostfire | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 718.6 -> **957.7** | 935.5 -> **1054.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.5% vs 30% floor, Casts: 6251). Increasing spread: b -16.2%, n +33.3%; Individual spell undertuned (WR: 37.5%, Casts: 6251, mult: 1.046) |
| `FEF` | Beasts | Debuff / Control | 13.9 -> **13.0** (-6.5%) | - | 13.9 -> **13.0** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Individual spell overtuned (WR: 71.6%, Casts: 2281, mult: 0.917) |
| `FEW` | Beasts | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 1172.6 -> **1606.5** | 1056.2 -> **1286.0** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 487). Increasing spread: b -18.0%, n +37.0% |
| `FEE` | Beasts | Buff / Sustain | 63.0 -> **73.7** (+17.0%) | - | 63.0 -> **73.7** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Individual spell undertuned (WR: 14.5%, Casts: 3593, mult: 1.144) |
| `FEL` | Beasts | Buff / Sustain | 103.2 -> **113.9** (+10.4%) | - | 103.2 -> **113.9** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Individual spell undertuned (WR: 29.3%, Casts: 5062, mult: 1.080) |
| `FED` | Beasts | Conditional Strike | 2.6 -> **2.7** (+3.8%) | 3.5 -> **3.5** | 11.7 -> **12.2** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.5% vs 30% floor, Casts: 114). Increasing spread: b -13.8%, n +28.2% |
| `EFF` | Beasts | Debuff / Control | 0.8 -> **0.7** (-12.5%) | 753.9 -> **1032.8** | 603.9 -> **723.7** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 493). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 60.3 -> **71.5** (+18.6%) | - | 60.3 -> **71.5** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Individual spell undertuned (WR: 11.0%, Casts: 2646, mult: 1.160) |
| `EFE` | Beasts | Buff / Sustain | 18.5 -> **16.7** (-9.7%) | - | 18.5 -> **16.7** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Individual spell overtuned (WR: 79.3%, Casts: 1887, mult: 0.883) |
| `EFL` | Beasts | Buff / Sustain | 1.1 -> **0.9** (-18.2%) | - | 1.1 -> **0.9** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Individual spell overtuned (WR: 92.1%, Casts: 2550, mult: 0.826) |
| `EFD` | Beasts | Ultimate | 4.9 -> **4.0** (-18.4%) | 271.0 -> **371.3** | 1332.8 -> **1489.2** | Class Beasts undertuned (WR: 44.5%, factor: 1.022); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 3222). Increasing spread: b -18.0%, n +37.0% |
| `FLF` | Lightning | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 1027.1 -> **1396.5** | 1028.1 -> **1257.8** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 1768). Increasing spread: b -17.5%, n +36.0% |
| `FLE` | Lightning | Setup - Weather | 164.0 -> **219.4** (+33.8%) | - | 164.0 -> **219.4** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Weather 'Storming' appliers undertuned (WR: 8.1%, casts: 4006) |
| `FLL` | Lightning | Buff / Sustain | 33.8 -> **34.4** (+1.8%) | - | 33.8 -> **34.4** | Class Lightning undertuned (WR: 45.4%, factor: 1.018) |
| `FLD` | Lightning | Ultimate | 8.5 -> **6.9** (-18.8%) | 102.3 -> **136.6** | 878.0 -> **949.4** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Weather 'Storming' beneficiaries overtuned (WR: 56.4%) |
| `LFF` | Lightning | Conditional Strike | 1.7 -> **1.5** (-11.8%) | 800.6 -> **1096.8** | 1362.7 -> **1646.7** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4437). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 19.9 -> **19.6** (-1.5%) | - | 19.9 -> **19.6** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Individual spell overtuned (WR: 59.0%, Casts: 4630, mult: 0.968) |
| `LFE` | Lightning | Debuff / Control | 11.3 -> **9.8** (-13.3%) | - | 11.3 -> **9.8** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Individual spell overtuned (WR: 87.2%, Casts: 1010, mult: 0.848) |
| `LFL` | Lightning | Debuff / Control | 1.8 -> **1.5** (-16.7%) | 570.5 -> **772.9** | 1028.7 -> **1160.8** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 1698). Increasing spread: b -17.3%, n +35.5% |
| `LFD` | Lightning | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 953.0 -> **1300.0** | 858.6 -> **1040.8** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 283). Increasing spread: b -17.7%, n +36.4% |
| `FDF` | Blood | Conditional Strike | 0.7 -> **0.5** (-28.6%) | 844.2 -> **1156.6** | 591.6 -> **578.8** | Class Blood overtuned (WR: 63.9%, factor: 0.945); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1309). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 76.2 -> **80.8** (+6.0%) | - | 76.2 -> **80.8** | Class Blood overtuned (WR: 63.9%, factor: 0.945); Individual spell undertuned (WR: 19.2%, Casts: 2376, mult: 1.123) |
| `FDE` | Blood | Setup - Weather | 69.2 -> **67.2** (-2.9%) | - | 69.2 -> **67.2** | Class Blood overtuned (WR: 63.9%, factor: 0.945); Individual spell undertuned (WR: 42.0%, Casts: 88, mult: 1.028) |
| `FDD` | Blood | Ultimate | 7.2 -> **5.4** (-25.0%) | 56.8 -> **77.8** | 416.2 -> **425.5** | Class Blood overtuned (WR: 63.9%, factor: 0.945); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1563). Increasing spread: b -18.0%, n +37.0% |
| `DFF` | Blood | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 1251.1 -> **1793.6** | 1377.3 -> **1794.6** | Class Blood overtuned (WR: 63.9%, factor: 0.945); Status 'Bleeding' beneficiaries undertuned (WR: 34.6%) |
| `DFE` | Blood | Buff / Sustain | 170.2 -> **174.5** (+2.5%) | - | 170.2 -> **174.5** | Class Blood overtuned (WR: 63.9%, factor: 0.945); Individual spell undertuned (WR: 28.0%, Casts: 174, mult: 1.085) |
| `DFL` | Blood | Buff / Sustain | 8.0 -> **7.0** (-12.5%) | - | 8.0 -> **7.0** | Class Blood overtuned (WR: 63.9%, factor: 0.945); Individual spell overtuned (WR: 69.0%, Casts: 8602, mult: 0.927) |
| `DFD` | Blood | Conditional Strike | 122.9 -> **125.0** (+1.7%) | 0.1 -> **0.1** | 135.2 -> **137.5** | Class Blood overtuned (WR: 63.9%, factor: 0.945); Condition triggers excessively (N=1 conditions, Trigger Rate: 85.9% vs 55% ceiling, WR: 86.5%). Compressing spread: b +26.5%, n -33.6% |
| `WEF` | Plants | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 864.2 -> **1176.9** | 778.7 -> **942.3** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.0% vs 30% floor, Casts: 1531). Increasing spread: b -17.6%, n +36.2% |
| `WEW` | Plants | Debuff / Control | 72.1 -> **82.8** (+14.8%) | - | 72.1 -> **82.8** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Individual spell undertuned (WR: 22.1%, Casts: 391, mult: 1.111) |
| `WEE` | Plants | Setup - Location | 216.4 -> **267.5** (+23.6%) | - | 216.4 -> **267.5** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Location 'Jungle' appliers undertuned (WR: 24.9%, casts: 5377) |
| `WEL` | Plants | Debuff / Control | 14.3 -> **16.5** (+15.4%) | - | 14.3 -> **16.5** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Status 'Entangled' appliers undertuned (WR: 34.6%, casts: 720) |
| `WED` | Plants | Conditional Strike | 10.0 -> **8.4** (-16.0%) | 28.5 -> **39.0** | 295.0 -> **336.0** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1795). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 2.1 -> **2.0** (-4.8%) | 1183.2 -> **1731.4** | 2486.8 -> **3464.8** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Weather 'Sunny' beneficiaries undertuned (WR: 32.5%) |
| `EWW` | Plants | Debuff / Control | 1.5 -> **1.3** (-13.3%) | - | 1.5 -> **1.3** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Individual spell overtuned (WR: 91.7%, Casts: 2066, mult: 0.828) |
| `EWL` | Plants | Debuff / Control | 20.0 -> **18.6** (-7.0%) | - | 20.0 -> **18.6** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Individual spell overtuned (WR: 75.7%, Casts: 4903, mult: 0.899) |
| `EWD` | Plants | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 1138.1 -> **1559.2** | 341.7 -> **312.0** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Status 'Bleeding' appliers overtuned on own (WR: 84.0%) |
| `WLF` | Fey | Conditional Strike | 1.5 -> **1.3** (-13.3%) | 595.7 -> **816.1** | 895.1 -> **1062.2** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 11). Increasing spread: b -18.0%, n +37.0% |
| `WLW` | Fey | Debuff / Control | 13.6 -> **12.8** (-5.9%) | - | 13.6 -> **12.8** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Status 'Cursed' appliers overtuned on own (WR: 62.1%) |
| `WLE` | Fey | Setup - Location | 405.7 -> **546.7** (+34.8%) | - | 405.7 -> **546.7** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Location 'Enchanted Forest' appliers undertuned (WR: 12.6%, casts: 4197) |
| `WLL` | Fey | Direct Damage | 41.0 -> **39.0** (-4.9%) | - | 41.0 -> **39.0** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Individual spell overtuned (WR: 72.9%, Casts: 1103, mult: 0.911) |
| `WLD` | Fey | Ultimate | 7.1 -> **6.1** (-14.1%) | 229.9 -> **315.0** | 1639.4 -> **1927.6** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4355). Increasing spread: b -18.0%, n +37.0% |
| `LWF` | Fey | Debuff / Control | 3.2 -> **2.8** (-12.5%) | 778.5 -> **1061.9** | 2494.4 -> **2976.1** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 1113). Increasing spread: b -17.7%, n +36.4% |
| `LWW` | Fey | Debuff / Control | 53.8 -> **57.7** (+7.2%) | - | 53.8 -> **57.7** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Individual spell undertuned (WR: 42.1%, Casts: 584, mult: 1.028) |
| `LWL` | Fey | Debuff / Control | 229.0 -> **278.6** (+21.7%) | - | 229.0 -> **278.6** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Individual spell undertuned (WR: 9.8%, Casts: 4089, mult: 1.165) |
| `LWD` | Fey | Conditional Strike | 2.0 -> **1.5** (-25.0%) | 844.2 -> **1156.6** | 1690.4 -> **1736.4** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 485). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 1.8 -> **1.3** (-27.8%) | 1776.8 -> **2340.2** | 3200.0 -> **3043.6** | Class Ice overtuned (WR: 63.3%, factor: 0.947); Weather 'Raining' beneficiaries overtuned (WR: 59.7%) |
| `WDW` | Ice | Buff / Sustain | 45.6 -> **38.7** (-15.1%) | - | 45.6 -> **38.7** | Class Ice overtuned (WR: 63.3%, factor: 0.947); Status 'Frosty' appliers overtuned on own (WR: 68.4%) |
| `WDE` | Ice | Setup - Weather | 100.1 -> **100.8** (+0.7%) | - | 100.1 -> **100.8** | Class Ice overtuned (WR: 63.3%, factor: 0.947); Individual spell undertuned (WR: 33.1%, Casts: 1876, mult: 1.064) |
| `WDL` | Ice | Debuff / Control | 14.8 -> **12.2** (-17.6%) | - | 14.8 -> **12.2** | Class Ice overtuned (WR: 63.3%, factor: 0.947); Status 'Frosty' appliers overtuned on own (WR: 68.4%) |
| `WDD` | Ice | Ultimate | 8.5 -> **6.4** (-24.7%) | 61.6 -> **79.9** | 532.1 -> **517.8** | Class Ice overtuned (WR: 63.3%, factor: 0.947); Weather 'Blizzard' beneficiaries overtuned (WR: 56.7%) |
| `DWF` | Ice | Debuff / Control | 13.4 -> **10.9** (-18.7%) | - | 13.4 -> **10.9** | Class Ice overtuned (WR: 63.3%, factor: 0.947); Status 'Frosty' appliers overtuned on own (WR: 68.4%) |
| `DWW` | Ice | Debuff / Control | 17.0 -> **14.9** (-12.4%) | - | 17.0 -> **14.9** | Class Ice overtuned (WR: 63.3%, factor: 0.947); Individual spell overtuned (WR: 69.0%, Casts: 4080, mult: 0.928) |
| `DWE` | Ice | Setup - Location | 220.6 -> **208.9** (-5.3%) | - | 220.6 -> **208.9** | Class Ice overtuned (WR: 63.3%, factor: 0.947) |
| `DWL` | Ice | Debuff / Control | 16.2 -> **13.6** (-16.0%) | - | 16.2 -> **13.6** | Class Ice overtuned (WR: 63.3%, factor: 0.947); Status 'Frosty' appliers overtuned on own (WR: 68.4%) |
| `DWD` | Ice | Conditional Strike | 2.1 -> **1.7** (-19.0%) | 940.6 -> **1303.8** | 1977.4 -> **2218.2** | Class Ice overtuned (WR: 63.3%, factor: 0.947); Status 'Frosty' beneficiaries undertuned (WR: 41.9%) |
| `ELF` | Wind | Conditional Strike | 3.5 -> **3.1** (-11.4%) | 1477.2 -> **2131.5** | 5173.7 -> **6610.8** | Class Wind undertuned (WR: 38.4%, factor: 1.046); Status 'Bleeding' beneficiaries undertuned (WR: 34.6%) |
| `ELW` | Wind | Debuff / Control | 23.8 -> **22.7** (-4.6%) | - | 23.8 -> **22.7** | Class Wind undertuned (WR: 38.4%, factor: 1.046); Individual spell overtuned (WR: 72.8%, Casts: 942, mult: 0.912) |
| `ELE` | Wind | Setup - Weather | 80.0 -> **93.1** (+16.4%) | - | 80.0 -> **93.1** | Class Wind undertuned (WR: 38.4%, factor: 1.046); Individual spell undertuned (WR: 21.8%, Casts: 3464, mult: 1.112) |
| `ELL` | Wind | Buff / Sustain | 86.9 -> **87.4** (+0.6%) | - | 86.9 -> **87.4** | Class Wind undertuned (WR: 38.4%, factor: 1.046); Individual spell overtuned (WR: 60.7%, Casts: 665, mult: 0.961) |
| `ELD` | Wind | Conditional Strike | 4.5 -> **3.7** (-17.8%) | 1600.2 -> **2082.8** | 7205.4 -> **7710.1** | Class Wind undertuned (WR: 38.4%, factor: 1.046); Weather 'Raining' beneficiaries overtuned (WR: 59.7%) |
| `LEF` | Wind | Conditional Strike | 2.0 -> **1.8** (-10.0%) | 1103.5 -> **1616.3** | 2209.0 -> **2911.1** | Class Wind undertuned (WR: 38.4%, factor: 1.046); Status 'Burning' beneficiaries undertuned (WR: 30.4%) |
| `LEW` | Wind | Debuff / Control | 26.6 -> **26.9** (+1.1%) | - | 26.6 -> **26.9** | Class Wind undertuned (WR: 38.4%, factor: 1.046); Individual spell overtuned (WR: 59.2%, Casts: 255, mult: 0.967) |
| `LEE` | Wind | Setup - Weather | 116.2 -> **141.3** (+21.6%) | - | 116.2 -> **141.3** | Class Wind undertuned (WR: 38.4%, factor: 1.046); Individual spell undertuned (WR: 10.5%, Casts: 3071, mult: 1.162) |
| `LEL` | Wind | Buff / Sustain | 134.2 -> **147.9** (+10.2%) | - | 134.2 -> **147.9** | Class Wind undertuned (WR: 38.4%, factor: 1.046); Individual spell undertuned (WR: 35.6%, Casts: 1644, mult: 1.054) |
| `EDF` | Poison | Conditional Strike | 0.8 -> **0.6** (-25.0%) | 554.4 -> **745.8** | 444.3 -> **448.1** | Class Poison undertuned (WR: 45.2%, factor: 1.019); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 1511). Increasing spread: b -16.8%, n +34.5% |
| `EDW` | Poison | Debuff / Control | 5.3 -> **5.4** (+1.9%) | - | 5.3 -> **5.4** | Class Poison undertuned (WR: 45.2%, factor: 1.019) |
| `EDE` | Poison | Setup - Location | 185.3 -> **240.8** (+30.0%) | - | 185.3 -> **240.8** | Class Poison undertuned (WR: 45.2%, factor: 1.019); Location 'Swamp' appliers undertuned (WR: 15.8%, casts: 2876) |
| `EDD` | Poison | Ultimate | 14.0 -> **11.2** (-20.0%) | 108.4 -> **150.6** | 1531.6 -> **1697.9** | Class Poison undertuned (WR: 45.2%, factor: 1.019); Status 'Bleeding' beneficiaries undertuned (WR: 34.6%) |
| `DEF` | Poison | Conditional Strike | 6.8 -> **5.7** (-16.2%) | 8.1 -> **11.1** | 61.9 -> **69.0** | Class Poison undertuned (WR: 45.2%, factor: 1.019); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 288). Increasing spread: b -17.9%, n +36.7% |
| `DEW` | Poison | Debuff / Control | 5.1 -> **4.5** (-11.8%) | - | 5.1 -> **4.5** | Class Poison undertuned (WR: 45.2%, factor: 1.019); Individual spell overtuned (WR: 81.5%, Casts: 3621, mult: 0.874) |
| `DEE` | Poison | Debuff / Control | 15.8 -> **19.0** (+20.3%) | - | 15.8 -> **19.0** | Class Poison undertuned (WR: 45.2%, factor: 1.019); Individual spell undertuned (WR: 5.6%, Casts: 132, mult: 1.180) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 1578.8 -> **2296.5** | 473.9 -> **689.2** | Class Poison undertuned (WR: 45.2%, factor: 1.019); Status 'Bleeding' beneficiaries undertuned (WR: 34.6%) |
| `DED` | Poison | Debuff / Control | 16.6 -> **18.9** (+13.9%) | - | 16.6 -> **18.9** | Class Poison undertuned (WR: 45.2%, factor: 1.019); Individual spell undertuned (WR: 19.3%, Casts: 45, mult: 1.116) |
| `LDF` | Cosmic | Debuff / Control | 21.3 -> **19.0** (-10.8%) | - | 21.3 -> **19.0** | Class Cosmic overtuned (WR: 57.6%, factor: 0.970); Individual spell overtuned (WR: 71.3%, Casts: 2387, mult: 0.918) |
| `LDE` | Cosmic | Setup - Location | 56.4 -> **58.6** (+3.9%) | - | 56.4 -> **58.6** | Class Cosmic overtuned (WR: 57.6%, factor: 0.970); Individual spell undertuned (WR: 31.2%, Casts: 3588, mult: 1.072) |
| `LDL` | Cosmic | Conditional Strike | 1.5 -> **1.2** (-20.0%) | 703.6 -> **963.9** | 1056.9 -> **1157.9** | Class Cosmic overtuned (WR: 57.6%, factor: 0.970); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3810). Increasing spread: b -18.0%, n +37.0% |
| `LDD` | Cosmic | Ultimate | 9.8 -> **7.8** (-20.4%) | 70.6 -> **96.7** | 701.7 -> **762.1** | Class Cosmic overtuned (WR: 57.6%, factor: 0.970); Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 7280). Increasing spread: b -18.0%, n +37.0% |
| `DLF` | Cosmic | Conditional Strike | 1.9 -> **1.5** (-21.1%) | 637.7 -> **873.6** | 1213.5 -> **1311.9** | Class Cosmic overtuned (WR: 57.6%, factor: 0.970); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1938). Increasing spread: b -18.0%, n +37.0% |
| `DLW` | Cosmic | Direct Damage | 18.4 -> **15.8** (-14.1%) | - | 18.4 -> **15.8** | Class Cosmic overtuned (WR: 57.6%, factor: 0.970); Individual spell overtuned (WR: 78.6%, Casts: 9090, mult: 0.886) |
| `DLE` | Cosmic | Direct Damage | 175.4 -> **184.1** (+5.0%) | - | 175.4 -> **184.1** | Class Cosmic overtuned (WR: 57.6%, factor: 0.970); Individual spell undertuned (WR: 28.6%, Casts: 862, mult: 1.083) |
| `DLL` | Cosmic | Conditional Strike | 2.0 -> **1.6** (-20.0%) | 657.2 -> **899.6** | 1316.4 -> **1441.0** | Class Cosmic overtuned (WR: 57.6%, factor: 0.970); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1444). Increasing spread: b -17.9%, n +36.9% |
