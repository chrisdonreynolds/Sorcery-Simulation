# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T18:31:33Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 70.9s  
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
| **Light** | 11,719 | 63.3% | 63.3% | 1.3 | Overtuned ⚠️ |
| **Dark** | 10,554 | 60.4% | 60.5% | 3.4 | Overtuned ⚠️ |
| **Poison** | 38,810 | 60.3% | 60.4% | 3.1 | Overtuned ⚠️ |
| **Water** | 10,334 | 58.6% | 58.6% | 4.8 | Overtuned ⚠️ |
| **Blood** | 29,437 | 58.1% | 58.1% | 8.7 | Overtuned ⚠️ |
| **Earth** | 14,887 | 54.5% | 54.5% | 13.9 | Overtuned ⚠️ |
| **Ghostfire** | 27,379 | 53.8% | 53.8% | 1.9 | Overtuned ⚠️ |
| **Fire** | 11,960 | 51.2% | 51.2% | 1.9 | Balanced ✅ |
| **Cosmic** | 34,589 | 50.5% | 50.5% | 5.3 | Balanced ✅ |
| **Ice** | 41,485 | 50.3% | 50.3% | 2.9 | Balanced ✅ |
| **Lightning** | 22,981 | 44.4% | 44.4% | 1.6 | Undertuned ⚠️ |
| **Plants** | 30,990 | 43.8% | 43.8% | 1.9 | Undertuned ⚠️ |
| **Beasts** | 24,472 | 43.8% | 43.8% | 2.1 | Undertuned ⚠️ |
| **Fey** | 27,775 | 39.0% | 39.0% | 3.3 | Undertuned ⚠️ |
| **Wind** | 20,449 | 31.3% | 31.3% | 1.6 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 19,731 (55.4%) | 7,224 (27.9%) | 1.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 971 (43.9%) | 11,358 (41.2%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,002 (68.3%) | 5,409 (38.0%) | 2.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,809 (86.2%) | 25,729 (39.7%) | 1.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 20,752 (53.6%) | 7,046 (22.5%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,880 (79.9%) | 2,653 (44.5%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 809 (15.0%) | 4,545 (36.7%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 14.7 -> **15.3** (+4.1%) | - | 14.7 -> **15.3** | Individual spell undertuned (WR: 38.6%, Casts: 247, mult: 1.041) |
| `FFW` | Fire | Debuff / Control | 7.2 -> **6.6** (-8.3%) | - | 7.2 -> **6.6** | Status 'Burning' appliers overtuned on own (WR: 68.3%); Individual spell overtuned (WR: 56.2%, Casts: 3301, mult: 0.979) |
| `FFD` | Fire | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 3380.7 -> **4778.9** | 3381.7 -> **4301.9** | Status 'Burning' beneficiaries undertuned (WR: 38.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.6% vs 30% floor, Casts: 3734). Increasing spread: b -17.0%, n +34.9% |
| `WWF` | Water | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 2065.3 -> **2832.0** | 2272.9 -> **2833.0** | Class Water overtuned (WR: 58.6%, factor: 0.966); Status 'Burning' beneficiaries undertuned (WR: 38.0%) |
| `WWE` | Water | Setup - Weather | 255.5 -> **315.7** (+23.6%) | - | 255.5 -> **315.7** | Class Water overtuned (WR: 58.6%, factor: 0.966); Weather 'Raining' appliers undertuned (WR: 15.0%, casts: 809) |
| `WWL` | Water | Buff / Sustain | 15.2 -> **13.7** (-9.9%) | - | 15.2 -> **13.7** | Class Water overtuned (WR: 58.6%, factor: 0.966); Individual spell overtuned (WR: 67.8%, Casts: 6833, mult: 0.932) |
| `WWD` | Water | Buff / Sustain | 29.5 -> **25.6** (-13.2%) | - | 29.5 -> **25.6** | Class Water overtuned (WR: 58.6%, factor: 0.966); Individual spell overtuned (WR: 76.3%, Casts: 47, mult: 0.900) |
| `EEF` | Earth | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 2832.9 -> **4193.2** | 2833.9 -> **3774.8** | Class Earth overtuned (WR: 54.5%, factor: 0.982); Status 'Frosty' beneficiaries undertuned (WR: 27.9%) |
| `EEW` | Earth | Buff / Sustain | 35.7 -> **33.8** (-5.3%) | - | 35.7 -> **33.8** | Class Earth overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 59.8%, Casts: 1098, mult: 0.965) |
| `EEE` | Earth | Conditional Strike | 9.5 -> **10.0** (+5.3%) | 1.5 -> **1.5** | 23.8 -> **25.0** | Class Earth overtuned (WR: 54.5%, factor: 0.982); Condition triggers excessively (N=1 conditions, Trigger Rate: 94.7% vs 55% ceiling, WR: 90.9%). Compressing spread: b +30.2%, n -38.5% |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 1645.1 -> **2201.1** | 164.6 -> **220.2** | Class Light overtuned (WR: 63.3%, factor: 0.947); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.8% vs 30% floor, Casts: 2112). Increasing spread: b -16.5%, n +33.8% |
| `LLW` | Light | Debuff / Control | 11.8 -> **10.0** (-15.3%) | - | 11.8 -> **10.0** | Class Light overtuned (WR: 63.3%, factor: 0.947); Individual spell overtuned (WR: 77.5%, Casts: 224, mult: 0.891) |
| `LLE` | Light | Setup - Weather | 726.9 -> **717.8** (-1.3%) | - | 726.9 -> **717.8** | Class Light overtuned (WR: 63.3%, factor: 0.947); Weather 'Sunny' appliers undertuned (WR: 43.9%, casts: 971) |
| `LLL` | Light | Buff / Sustain | 9.1 -> **7.4** (-18.7%) | - | 9.1 -> **7.4** | Class Light overtuned (WR: 63.3%, factor: 0.947); Individual spell overtuned (WR: 84.4%, Casts: 3302, mult: 0.861) |
| `LLD` | Light | Ultimate | 5.1 -> **3.9** (-23.5%) | 402.6 -> **570.9** | 2058.4 -> **2230.4** | Class Light overtuned (WR: 63.3%, factor: 0.947); Weather 'Sunny' beneficiaries undertuned (WR: 41.2%) |
| `DDF` | Dark | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 2170.8 -> **2974.0** | 1085.9 -> **1190.0** | Class Dark overtuned (WR: 60.4%, factor: 0.958); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1876). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 11.3 -> **10.1** (-10.6%) | - | 11.3 -> **10.1** | Class Dark overtuned (WR: 60.4%, factor: 0.958); Individual spell overtuned (WR: 67.9%, Casts: 490, mult: 0.932) |
| `DDE` | Dark | Setup - Weather | 422.4 -> **404.8** (-4.2%) | - | 422.4 -> **404.8** | Class Dark overtuned (WR: 60.4%, factor: 0.958) |
| `DDL` | Dark | Debuff / Control | 10.2 -> **9.3** (-8.8%) | - | 10.2 -> **9.3** | Class Dark overtuned (WR: 60.4%, factor: 0.958); Individual spell overtuned (WR: 62.3%, Casts: 4499, mult: 0.955) |
| `DDD` | Dark | Debuff / Control | 4.1 -> **3.6** (-12.2%) | - | 4.1 -> **3.6** | Class Dark overtuned (WR: 60.4%, factor: 0.958); Individual spell overtuned (WR: 74.2%, Casts: 2925, mult: 0.906) |
| `FWW` | Ghostfire | Debuff / Control | 5.2 -> **4.9** (-5.8%) | - | 5.2 -> **4.9** | Class Ghostfire overtuned (WR: 53.8%, factor: 0.985); Status 'Cursed' appliers overtuned on own (WR: 62.3%) |
| `FWE` | Ghostfire | Setup - Location | 132.0 -> **130.0** (-1.5%) | - | 132.0 -> **130.0** | Class Ghostfire overtuned (WR: 53.8%, factor: 0.985) |
| `FWL` | Ghostfire | Debuff / Control | 12.6 -> **11.6** (-7.9%) | - | 12.6 -> **11.6** | Class Ghostfire overtuned (WR: 53.8%, factor: 0.985); Status 'Cursed' appliers overtuned on own (WR: 62.3%) |
| `FWD` | Ghostfire | Ultimate | 4.8 -> **5.1** (+6.2%) | 146.1 -> **152.5** | 706.1 -> **782.8** | Class Ghostfire overtuned (WR: 53.8%, factor: 0.985); Status 'Cursed' beneficiaries undertuned (WR: 22.3%) |
| `WFF` | Ghostfire | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 4985.0 -> **7105.2** | 3490.2 -> **4263.7** | Class Ghostfire overtuned (WR: 53.8%, factor: 0.985); Status 'Bleeding' beneficiaries undertuned (WR: 39.7%) |
| `WFW` | Ghostfire | Debuff / Control | 4.5 -> **4.2** (-6.7%) | - | 4.5 -> **4.2** | Class Ghostfire overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 66.1%, Casts: 10785, mult: 0.940) |
| `WFL` | Ghostfire | Buff / Sustain | 46.4 -> **45.7** (-1.5%) | - | 46.4 -> **45.7** | Class Ghostfire overtuned (WR: 53.8%, factor: 0.985) |
| `WFD` | Ghostfire | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 1797.3 -> **2462.2** | 1618.5 -> **1970.6** | Class Ghostfire overtuned (WR: 53.8%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6799). Increasing spread: b -18.0%, n +37.0% |
| `FEF` | Beasts | Debuff / Control | 11.6 -> **10.7** (-7.8%) | - | 11.6 -> **10.7** | Class Beasts undertuned (WR: 43.8%, factor: 1.025); Individual spell overtuned (WR: 76.0%, Casts: 2815, mult: 0.898) |
| `FEW` | Beasts | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 2980.1 -> **4173.0** | 1788.7 -> **2087.0** | Class Beasts undertuned (WR: 43.8%, factor: 1.025); Status 'Entangled' beneficiaries undertuned (WR: 44.5%) |
| `FEE` | Beasts | Buff / Sustain | 94.0 -> **110.4** (+17.4%) | - | 94.0 -> **110.4** | Class Beasts undertuned (WR: 43.8%, factor: 1.025); Individual spell undertuned (WR: 14.1%, Casts: 6874, mult: 1.146) |
| `FEL` | Beasts | Buff / Sustain | 135.5 -> **149.6** (+10.4%) | - | 135.5 -> **149.6** | Class Beasts undertuned (WR: 43.8%, factor: 1.025); Individual spell undertuned (WR: 29.9%, Casts: 2809, mult: 1.077) |
| `FED` | Beasts | Conditional Strike | 2.5 -> **2.3** (-8.0%) | 3.5 -> **3.5** | 11.2 -> **10.3** | Class Beasts undertuned (WR: 43.8%, factor: 1.025); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.6% vs 30% floor, Casts: 2939). Increasing spread: b -17.0%, n +34.8% |
| `EFF` | Beasts | Debuff / Control | 0.6 -> **0.5** (-16.7%) | 1938.4 -> **2655.6** | 1163.6 -> **1328.3** | Class Beasts undertuned (WR: 43.8%, factor: 1.025); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 411). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 87.4 -> **84.4** (-3.4%) | - | 87.4 -> **84.4** | Class Beasts undertuned (WR: 43.8%, factor: 1.025); Individual spell overtuned (WR: 65.5%, Casts: 104, mult: 0.942) |
| `EFE` | Beasts | Buff / Sustain | 13.7 -> **13.1** (-4.4%) | - | 13.7 -> **13.1** | Class Beasts undertuned (WR: 43.8%, factor: 1.025); Individual spell overtuned (WR: 68.3%, Casts: 4003, mult: 0.931) |
| `EFD` | Beasts | Ultimate | 3.6 -> **4.0** (+11.1%) | 503.8 -> **516.1** | 1817.3 -> **2068.4** | Class Beasts undertuned (WR: 43.8%, factor: 1.025); Status 'Entangled' beneficiaries undertuned (WR: 44.5%) |
| `FLF` | Lightning | Conditional Strike | 0.7 -> **0.7** (+0.0%) | 3090.6 -> **4699.4** | 2164.1 -> **3290.3** | Class Lightning undertuned (WR: 44.4%, factor: 1.022); Status 'Stunned' beneficiaries undertuned (WR: 22.5%) |
| `FLW` | Lightning | Debuff / Control | 8.9 -> **8.2** (-7.9%) | - | 8.9 -> **8.2** | Class Lightning undertuned (WR: 44.4%, factor: 1.022); Status 'Stunned' appliers overtuned on own (WR: 53.6%) |
| `FLE` | Lightning | Setup - Weather | 247.7 -> **253.2** (+2.2%) | - | 247.7 -> **253.2** | Class Lightning undertuned (WR: 44.4%, factor: 1.022) |
| `FLL` | Lightning | Buff / Sustain | 42.7 -> **47.0** (+10.1%) | - | 42.7 -> **47.0** | Class Lightning undertuned (WR: 44.4%, factor: 1.022); Individual spell undertuned (WR: 29.8%, Casts: 193, mult: 1.078) |
| `FLD` | Lightning | Ultimate | 7.0 -> **5.9** (-15.7%) | 228.8 -> **347.9** | 1608.6 -> **2058.5** | Class Lightning undertuned (WR: 44.4%, factor: 1.022); Status 'Stunned' beneficiaries undertuned (WR: 22.5%) |
| `LFF` | Lightning | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 2058.6 -> **2820.3** | 2265.6 -> **2821.3** | Class Lightning undertuned (WR: 44.4%, factor: 1.022); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4790). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 17.0 -> **18.6** (+9.4%) | - | 17.0 -> **18.6** | Class Lightning undertuned (WR: 44.4%, factor: 1.022); Individual spell undertuned (WR: 31.9%, Casts: 367, mult: 1.069) |
| `LFE` | Lightning | Debuff / Control | 8.3 -> **7.7** (-7.2%) | - | 8.3 -> **7.7** | Class Lightning undertuned (WR: 44.4%, factor: 1.022); Status 'Stunned' appliers overtuned on own (WR: 53.6%) |
| `LFL` | Lightning | Debuff / Control | 1.2 -> **1.1** (-8.3%) | 1450.7 -> **1958.3** | 1742.0 -> **2155.2** | Class Lightning undertuned (WR: 44.4%, factor: 1.022); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.4% vs 30% floor, Casts: 1702). Increasing spread: b -17.0%, n +35.0% |
| `LFD` | Lightning | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 2440.0 -> **3342.8** | 1464.6 -> **1671.9** | Class Lightning undertuned (WR: 44.4%, factor: 1.022); Status 'Stunned' appliers overtuned on own (WR: 53.6%) |
| `FDF` | Blood | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 2170.8 -> **2974.0** | 651.5 -> **595.0** | Class Blood overtuned (WR: 58.1%, factor: 0.968); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 394). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 78.6 -> **77.0** (-2.0%) | - | 78.6 -> **77.0** | Class Blood overtuned (WR: 58.1%, factor: 0.968); Individual spell undertuned (WR: 46.3%, Casts: 2453, mult: 1.012) |
| `FDE` | Blood | Setup - Weather | 59.2 -> **57.3** (-3.2%) | - | 59.2 -> **57.3** | Class Blood overtuned (WR: 58.1%, factor: 0.968) |
| `FDD` | Blood | Ultimate | 3.1 -> **2.4** (-22.6%) | 146.0 -> **200.0** | 455.7 -> **482.4** | Class Blood overtuned (WR: 58.1%, factor: 0.968); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 7170). Increasing spread: b -18.0%, n +37.0% |
| `DFF` | Blood | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 3670.8 -> **5137.5** | 2937.4 -> **3596.9** | Class Blood overtuned (WR: 58.1%, factor: 0.968); Status 'Bleeding' beneficiaries undertuned (WR: 39.7%) |
| `DFE` | Blood | Buff / Sustain | 219.5 -> **250.6** (+14.2%) | - | 219.5 -> **250.6** | Class Blood overtuned (WR: 58.1%, factor: 0.968); Individual spell undertuned (WR: 1.5%, Casts: 2041, mult: 1.180) |
| `DFL` | Blood | Buff / Sustain | 5.8 -> **5.5** (-5.2%) | - | 5.8 -> **5.5** | Class Blood overtuned (WR: 58.1%, factor: 0.968); Individual spell overtuned (WR: 55.4%, Casts: 2265, mult: 0.982) |
| `DFD` | Blood | Conditional Strike | 127.6 -> **130.9** (+2.6%) | 0.1 -> **0.1** | 140.4 -> **144.0** | Class Blood overtuned (WR: 58.1%, factor: 0.968); Condition triggers excessively (N=1 conditions, Trigger Rate: 85.9% vs 55% ceiling, WR: 93.5%). Compressing spread: b +29.3%, n -36.4% |
| `WEF` | Plants | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 2349.8 -> **3401.4** | 1645.6 -> **2041.4** | Class Plants undertuned (WR: 43.8%, factor: 1.025); Location 'Jungle' beneficiaries undertuned (WR: 33.5%) |
| `WEW` | Plants | Debuff / Control | 100.1 -> **108.2** (+8.1%) | - | 100.1 -> **108.2** | Class Plants undertuned (WR: 43.8%, factor: 1.025); Individual spell undertuned (WR: 35.3%, Casts: 2853, mult: 1.055) |
| `WEE` | Plants | Setup - Location | 396.2 -> **527.8** (+33.2%) | - | 396.2 -> **527.8** | Class Plants undertuned (WR: 43.8%, factor: 1.025); Location 'Jungle' appliers undertuned (WR: 10.8%, casts: 3797) |
| `WEL` | Plants | Debuff / Control | 10.3 -> **8.4** (-18.4%) | - | 10.3 -> **8.4** | Class Plants undertuned (WR: 43.8%, factor: 1.025); Status 'Entangled' appliers overtuned on own (WR: 79.9%) |
| `WED` | Plants | Conditional Strike | 5.8 -> **6.4** (+10.3%) | 73.2 -> **68.8** | 430.4 -> **446.7** | Class Plants undertuned (WR: 43.8%, factor: 1.025); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 6414, WR: 48.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 1.8 -> **1.6** (-11.1%) | 3480.0 -> **4934.2** | 6265.8 -> **7896.3** | Class Plants undertuned (WR: 43.8%, factor: 1.025); Weather 'Sunny' beneficiaries undertuned (WR: 41.2%) |
| `EWL` | Plants | Debuff / Control | 15.4 -> **14.0** (-9.1%) | - | 15.4 -> **14.0** | Class Plants undertuned (WR: 43.8%, factor: 1.025); Individual spell overtuned (WR: 78.0%, Casts: 2478, mult: 0.889) |
| `EWD` | Plants | Conditional Strike | 0.2 -> **0.1** (-50.0%) | 2892.3 -> **4050.1** | 578.7 -> **405.1** | Class Plants undertuned (WR: 43.8%, factor: 1.025); Status 'Bleeding' appliers overtuned on own (WR: 86.2%) |
| `WLF` | Fey | Conditional Strike | 1.0 -> **1.0** (+0.0%) | 1557.5 -> **2349.4** | 1558.5 -> **2350.4** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Status 'Cursed' beneficiaries undertuned (WR: 22.3%) |
| `WLW` | Fey | Debuff / Control | 10.6 -> **9.5** (-10.4%) | - | 10.6 -> **9.5** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Status 'Cursed' appliers overtuned on own (WR: 62.3%) |
| `WLE` | Fey | Setup - Location | 973.7 -> **1276.9** (+31.1%) | - | 973.7 -> **1276.9** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Location 'Enchanted Forest' appliers undertuned (WR: 17.9%, casts: 3703) |
| `WLL` | Fey | Direct Damage | 32.1 -> **29.5** (-8.1%) | - | 32.1 -> **29.5** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Individual spell overtuned (WR: 80.1%, Casts: 3175, mult: 0.880) |
| `WLD` | Fey | Ultimate | 8.0 -> **5.9** (-26.2%) | 308.9 -> **433.9** | 2479.2 -> **2565.9** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.6%) |
| `LWF` | Fey | Debuff / Control | 2.2 -> **2.0** (-9.1%) | 2210.5 -> **3067.7** | 4865.3 -> **6137.4** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.6%) |
| `LWW` | Fey | Debuff / Control | 72.2 -> **85.9** (+19.0%) | - | 72.2 -> **85.9** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Individual spell undertuned (WR: 15.4%, Casts: 4394, mult: 1.140) |
| `LWL` | Fey | Debuff / Control | 336.0 -> **394.3** (+17.4%) | - | 336.0 -> **394.3** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Individual spell undertuned (WR: 19.0%, Casts: 88, mult: 1.124) |
| `LWD` | Fey | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 2170.8 -> **2974.0** | 2171.8 -> **2677.5** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 342). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 4213.8 -> **6077.6** | 2950.4 -> **3647.2** | Status 'Stunned' appliers overtuned on own (WR: 53.6%); Weather 'Raining' beneficiaries undertuned (WR: 36.7%) |
| `WDW` | Ice | Buff / Sustain | 38.0 -> **39.8** (+4.7%) | - | 38.0 -> **39.8** | Status 'Frosty' appliers overtuned on own (WR: 55.4%); Individual spell undertuned (WR: 31.9%, Casts: 4342, mult: 1.069) |
| `WDE` | Ice | Setup - Weather | 118.9 -> **135.3** (+13.8%) | - | 118.9 -> **135.3** | Individual spell undertuned (WR: 15.9%, Casts: 4398, mult: 1.138) |
| `WDL` | Ice | Debuff / Control | 10.4 -> **9.4** (-9.6%) | - | 10.4 -> **9.4** | Status 'Frosty' appliers overtuned on own (WR: 55.4%); Individual spell overtuned (WR: 69.4%, Casts: 527, mult: 0.926) |
| `WDD` | Ice | Ultimate | 5.2 -> **5.6** (+7.7%) | 97.7 -> **91.8** | 513.2 -> **519.7** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 9252, WR: 48.1%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DWF` | Ice | Debuff / Control | 8.9 -> **8.4** (-5.6%) | - | 8.9 -> **8.4** | Status 'Frosty' appliers overtuned on own (WR: 55.4%); Individual spell overtuned (WR: 60.1%, Casts: 7704, mult: 0.964) |
| `DWW` | Ice | Debuff / Control | 11.2 -> **10.7** (-4.5%) | - | 11.2 -> **10.7** | Individual spell overtuned (WR: 63.0%, Casts: 4878, mult: 0.952) |
| `DWE` | Ice | Setup - Location | 202.7 -> **260.3** (+28.4%) | - | 202.7 -> **260.3** | Location 'Tundra' appliers undertuned (WR: 15.3%, casts: 60); Individual spell undertuned (WR: 13.9%, Casts: 60, mult: 1.147) |
| `DWL` | Ice | Debuff / Control | 12.5 -> **11.6** (-7.2%) | - | 12.5 -> **11.6** | Status 'Frosty' appliers overtuned on own (WR: 55.4%); Individual spell overtuned (WR: 63.6%, Casts: 7158, mult: 0.950) |
| `DWD` | Ice | Conditional Strike | 1.0 -> **0.8** (-20.0%) | 2201.0 -> **3161.8** | 2202.0 -> **2530.2** | Status 'Frosty' beneficiaries undertuned (WR: 27.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.0% vs 30% floor, Casts: 316). Increasing spread: b -15.6%, n +32.0% |
| `ELF` | Wind | Conditional Strike | 2.2 -> **2.0** (-9.1%) | 4435.5 -> **6069.6** | 9760.3 -> **12141.2** | Class Wind undertuned (WR: 31.3%, factor: 1.075); Status 'Bleeding' beneficiaries undertuned (WR: 39.7%) |
| `ELW` | Wind | Debuff / Control | 19.2 -> **18.1** (-5.7%) | - | 19.2 -> **18.1** | Class Wind undertuned (WR: 31.3%, factor: 1.075); Individual spell overtuned (WR: 81.1%, Casts: 1413, mult: 0.875) |
| `ELE` | Wind | Setup - Weather | 105.7 -> **120.6** (+14.1%) | - | 105.7 -> **120.6** | Class Wind undertuned (WR: 31.3%, factor: 1.075); Individual spell undertuned (WR: 33.6%, Casts: 1616, mult: 1.062) |
| `ELL` | Wind | Buff / Sustain | 74.6 -> **76.1** (+2.0%) | - | 74.6 -> **76.1** | Class Wind undertuned (WR: 31.3%, factor: 1.075); Individual spell overtuned (WR: 63.7%, Casts: 741, mult: 0.949) |
| `ELD` | Wind | Conditional Strike | 2.6 -> **3.0** (+15.4%) | 3751.9 -> **5412.7** | 9757.5 -> **16241.1** | Class Wind undertuned (WR: 31.3%, factor: 1.075); Weather 'Raining' beneficiaries undertuned (WR: 36.7%) |
| `LEF` | Wind | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 3468.3 -> **4956.4** | 4510.1 -> **5453.1** | Class Wind undertuned (WR: 31.3%, factor: 1.075); Status 'Burning' beneficiaries undertuned (WR: 38.0%) |
| `LEW` | Wind | Debuff / Control | 21.8 -> **20.3** (-6.9%) | - | 21.8 -> **20.3** | Class Wind undertuned (WR: 31.3%, factor: 1.075); Individual spell overtuned (WR: 83.5%, Casts: 1014, mult: 0.865) |
| `LEE` | Wind | Setup - Weather | 149.2 -> **182.8** (+22.5%) | - | 149.2 -> **182.8** | Class Wind undertuned (WR: 31.3%, factor: 1.075); Individual spell undertuned (WR: 15.5%, Casts: 2916, mult: 1.140) |
| `LEL` | Wind | Buff / Sustain | 188.2 -> **231.9** (+23.2%) | - | 188.2 -> **231.9** | Class Wind undertuned (WR: 31.3%, factor: 1.075); Individual spell undertuned (WR: 13.9%, Casts: 7290, mult: 1.147) |
| `EDF` | Poison | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 1386.3 -> **1886.5** | 554.9 -> **566.2** | Class Poison overtuned (WR: 60.3%, factor: 0.959); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.1% vs 30% floor, Casts: 1461). Increasing spread: b -17.6%, n +36.1% |
| `EDW` | Poison | Debuff / Control | 4.4 -> **3.7** (-15.9%) | - | 4.4 -> **3.7** | Class Poison overtuned (WR: 60.3%, factor: 0.959); Individual spell overtuned (WR: 83.0%, Casts: 4046, mult: 0.867) |
| `EDE` | Poison | Setup - Location | 314.1 -> **314.8** (+0.2%) | - | 314.1 -> **314.8** | Class Poison overtuned (WR: 60.3%, factor: 0.959); Location 'Swamp' appliers undertuned (WR: 43.5%, casts: 1668) |
| `EDD` | Poison | Ultimate | 7.1 -> **5.5** (-22.5%) | 300.2 -> **417.2** | 2138.5 -> **2300.1** | Class Poison overtuned (WR: 60.3%, factor: 0.959); Status 'Bleeding' beneficiaries undertuned (WR: 39.7%) |
| `DEF` | Poison | Conditional Strike | 3.7 -> **2.9** (-21.6%) | 20.3 -> **26.8** | 78.8 -> **80.6** | Class Poison overtuned (WR: 60.3%, factor: 0.959); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.1% vs 30% floor, Casts: 163). Increasing spread: b -15.5%, n +31.9% |
| `DEW` | Poison | Debuff / Control | 3.8 -> **3.4** (-10.5%) | - | 3.8 -> **3.4** | Class Poison overtuned (WR: 60.3%, factor: 0.959); Individual spell overtuned (WR: 67.6%, Casts: 3273, mult: 0.933) |
| `DEE` | Poison | Debuff / Control | 16.0 -> **13.1** (-18.1%) | - | 16.0 -> **13.1** | Class Poison overtuned (WR: 60.3%, factor: 0.959); Individual spell overtuned (WR: 86.5%, Casts: 4494, mult: 0.851) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 4904.7 -> **6995.5** | 1471.7 -> **2098.9** | Class Poison overtuned (WR: 60.3%, factor: 0.959); Status 'Bleeding' beneficiaries undertuned (WR: 39.7%) |
| `DED` | Poison | Debuff / Control | 15.8 -> **13.5** (-14.6%) | - | 15.8 -> **13.5** | Class Poison overtuned (WR: 60.3%, factor: 0.959); Individual spell overtuned (WR: 77.1%, Casts: 2356, mult: 0.893) |
| `LDW` | Cosmic | Debuff / Control | 8.2 -> **7.4** (-9.8%) | - | 8.2 -> **7.4** | Status 'Stunned' appliers overtuned on own (WR: 53.6%); Individual spell overtuned (WR: 73.1%, Casts: 2475, mult: 0.910) |
| `LDE` | Cosmic | Setup - Location | 76.5 -> **79.7** (+4.2%) | - | 76.5 -> **79.7** | Individual spell undertuned (WR: 38.3%, Casts: 4129, mult: 1.042) |
| `LDL` | Cosmic | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 1806.5 -> **2474.9** | 1626.8 -> **1980.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3051). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 27.8%, Casts: 3051, mult: 1.086) |
| `LDD` | Cosmic | Ultimate | 5.0 -> **5.5** (+10.0%) | 181.5 -> **170.6** | 912.5 -> **943.8** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 8459, WR: 44.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 44.6%, Casts: 8459, mult: 1.018) |
| `DLF` | Cosmic | Conditional Strike | 1.1 -> **0.8** (-27.3%) | 1639.6 -> **2246.3** | 1804.7 -> **1797.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 424). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 68.8%, Casts: 424, mult: 0.928) |
| `DLW` | Cosmic | Direct Damage | 13.4 -> **12.1** (-9.7%) | - | 13.4 -> **12.1** | Individual spell overtuned (WR: 74.2%, Casts: 5663, mult: 0.906) |
| `DLE` | Cosmic | Direct Damage | 236.1 -> **265.2** (+12.3%) | - | 236.1 -> **265.2** | Individual spell undertuned (WR: 19.2%, Casts: 1045, mult: 1.123) |
| `DLL` | Cosmic | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 1687.8 -> **2308.8** | 2026.6 -> **2309.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 3230). Increasing spread: b -17.9%, n +36.8%; Individual spell undertuned (WR: 33.6%, Casts: 3230, mult: 1.062) |
