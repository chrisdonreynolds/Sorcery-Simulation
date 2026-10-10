# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T20:02:24Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 119.2s  
**Total Spells Tuned:** 104 / 125  

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
| **Light** | 6,964 | 65.5% | 65.6% | 1.9 | Overtuned ⚠️ |
| **Dark** | 10,846 | 62.1% | 62.1% | 2.4 | Overtuned ⚠️ |
| **Poison** | 28,653 | 60.1% | 60.1% | 2.1 | Overtuned ⚠️ |
| **Earth** | 18,799 | 59.1% | 59.1% | 13.2 | Overtuned ⚠️ |
| **Blood** | 31,176 | 53.8% | 53.8% | 10.3 | Overtuned ⚠️ |
| **Fire** | 17,984 | 52.3% | 52.4% | 2.3 | Balanced ✅ |
| **Ice** | 22,067 | 51.8% | 51.8% | 3.6 | Balanced ✅ |
| **Cosmic** | 23,505 | 51.4% | 51.4% | 3.4 | Balanced ✅ |
| **Beasts** | 27,446 | 47.7% | 47.7% | 7.8 | Balanced ✅ |
| **Ghostfire** | 35,767 | 47.4% | 47.4% | 1.3 | Balanced ✅ |
| **Wind** | 23,152 | 46.6% | 46.6% | 2.3 | Balanced ✅ |
| **Plants** | 28,770 | 46.3% | 46.3% | 2.3 | Undertuned ⚠️ |
| **Lightning** | 18,030 | 43.0% | 43.0% | 0.8 | Undertuned ⚠️ |
| **Fey** | 27,264 | 41.3% | 41.3% | 1.7 | Undertuned ⚠️ |
| **Water** | 14,316 | 34.4% | 34.4% | 1.2 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 13,490 (54.2%) | 4,313 (38.5%) | 4.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 928 (50.1%) | 3,912 (27.3%) | 2.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,300 (55.9%) | 5,580 (31.5%) | 3.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 12,116 (88.4%) | 19,682 (39.8%) | 0.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 8,846 (44.0%) | 3,062 (49.0%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 968 (83.5%) | 5,631 (53.3%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 6,328 (13.5%) | 3,385 (38.7%) | 1.1% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 7.2 -> **7.0** (-2.8%) | - | 7.2 -> **7.0** | Individual spell overtuned (WR: 57.1%, Casts: 6044, mult: 0.976) |
| `FFE` | Fire | Debuff / Control | 4.6 -> **4.4** (-4.3%) | - | 4.6 -> **4.4** | Individual spell overtuned (WR: 61.9%, Casts: 4540, mult: 0.957) |
| `FFD` | Fire | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 32449.4 -> **47378.2** | 12980.2 -> **18951.7** | Status 'Burning' beneficiaries undertuned (WR: 31.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 2895). Increasing spread: b -17.5%, n +36.0% |
| `WWF` | Water | Conditional Strike | 0.6 -> **0.6** (+0.0%) | 15432.4 -> **20579.6** | 9260.0 -> **12348.4** | Class Water undertuned (WR: 34.4%, factor: 1.063); Status 'Burning' beneficiaries undertuned (WR: 31.5%) |
| `WWE` | Water | Setup - Weather | 476.1 -> **650.9** (+36.7%) | - | 476.1 -> **650.9** | Class Water undertuned (WR: 34.4%, factor: 1.063); Weather 'Raining' appliers undertuned (WR: 13.5%, casts: 6328) |
| `WWL` | Water | Buff / Sustain | 7.7 -> **7.6** (-1.3%) | - | 7.7 -> **7.6** | Class Water undertuned (WR: 34.4%, factor: 1.063); Individual spell overtuned (WR: 68.7%, Casts: 4116, mult: 0.929) |
| `WWD` | Water | Buff / Sustain | 30.1 -> **35.1** (+16.6%) | - | 30.1 -> **35.1** | Class Water undertuned (WR: 34.4%, factor: 1.063); Individual spell undertuned (WR: 25.4%, Casts: 267, mult: 1.096) |
| `EEF` | Earth | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 16534.3 -> **23122.1** | 4960.6 -> **6936.9** | Class Earth overtuned (WR: 59.1%, factor: 0.964); Status 'Frosty' beneficiaries undertuned (WR: 38.5%) |
| `EEW` | Earth | Buff / Sustain | 25.9 -> **27.5** (+6.2%) | - | 25.9 -> **27.5** | Class Earth overtuned (WR: 59.1%, factor: 0.964); Individual spell undertuned (WR: 23.9%, Casts: 1850, mult: 1.103) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 10254.0 -> **13599.4** | 1025.5 -> **1360.0** | Class Light overtuned (WR: 65.5%, factor: 0.938); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.2% vs 30% floor, Casts: 1656). Increasing spread: b -15.9%, n +32.6% |
| `LLW` | Light | Debuff / Control | 8.1 -> **7.1** (-12.3%) | - | 8.1 -> **7.1** | Class Light overtuned (WR: 65.5%, factor: 0.938); Individual spell overtuned (WR: 66.4%, Casts: 3034, mult: 0.938) |
| `LLE` | Light | Setup - Weather | 948.6 -> **889.7** (-6.2%) | - | 948.6 -> **889.7** | Class Light overtuned (WR: 65.5%, factor: 0.938) |
| `LLL` | Light | Buff / Sustain | 6.2 -> **5.3** (-14.5%) | - | 6.2 -> **5.3** | Class Light overtuned (WR: 65.5%, factor: 0.938); Individual spell overtuned (WR: 74.0%, Casts: 1028, mult: 0.906) |
| `LLD` | Light | Ultimate | 6.6 -> **5.1** (-22.7%) | 480.7 -> **718.3** | 3179.2 -> **3668.4** | Class Light overtuned (WR: 65.5%, factor: 0.938); Weather 'Sunny' beneficiaries undertuned (WR: 27.3%) |
| `DDF` | Dark | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 14353.1 -> **19663.7** | 2870.8 -> **3932.9** | Class Dark overtuned (WR: 62.1%, factor: 0.952); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1648). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 8.6 -> **7.1** (-17.4%) | - | 8.6 -> **7.1** | Class Dark overtuned (WR: 62.1%, factor: 0.952); Individual spell overtuned (WR: 84.1%, Casts: 202, mult: 0.862) |
| `DDE` | Dark | Setup - Weather | 376.7 -> **465.0** (+23.4%) | - | 376.7 -> **465.0** | Class Dark overtuned (WR: 62.1%, factor: 0.952); Weather 'Darkness' appliers undertuned (WR: 12.5%, casts: 85) |
| `DDL` | Dark | Debuff / Control | 6.0 -> **5.3** (-11.7%) | - | 6.0 -> **5.3** | Class Dark overtuned (WR: 62.1%, factor: 0.952); Individual spell overtuned (WR: 66.8%, Casts: 8756, mult: 0.937) |
| `FWW` | Ghostfire | Debuff / Control | 4.1 -> **3.8** (-7.3%) | - | 4.1 -> **3.8** | Status 'Cursed' appliers overtuned on own (WR: 61.2%); Individual spell overtuned (WR: 62.1%, Casts: 3947, mult: 0.956) |
| `FWE` | Ghostfire | Setup - Location | 112.2 -> **120.2** (+7.1%) | - | 112.2 -> **120.2** | Location 'Graveyard' appliers undertuned (WR: 40.1%, casts: 198); Individual spell undertuned (WR: 40.0%, Casts: 198, mult: 1.036) |
| `FWL` | Ghostfire | Debuff / Control | 8.6 -> **8.4** (-2.3%) | - | 8.6 -> **8.4** | Status 'Cursed' appliers overtuned on own (WR: 61.2%); Individual spell undertuned (WR: 45.9%, Casts: 5951, mult: 1.014) |
| `FWD` | Ghostfire | Ultimate | 1.1 -> **0.8** (-27.3%) | 550.7 -> **659.6** | 606.9 -> **528.5** | Status 'Cursed' beneficiaries overtuned (WR: 53.6%); Location 'Graveyard' beneficiaries overtuned (WR: 78.2%) |
| `WFF` | Ghostfire | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 35896.9 -> **51189.2** | 10769.4 -> **15357.1** | Status 'Bleeding' beneficiaries undertuned (WR: 39.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3523). Increasing spread: b -18.0%, n +37.0% |
| `WFW` | Ghostfire | Debuff / Control | 3.1 -> **2.9** (-6.5%) | - | 3.1 -> **2.9** | Individual spell overtuned (WR: 65.0%, Casts: 8589, mult: 0.944) |
| `WFL` | Ghostfire | Buff / Sustain | 37.7 -> **32.6** (-13.5%) | - | 37.7 -> **32.6** | Individual spell overtuned (WR: 83.4%, Casts: 622, mult: 0.865) |
| `WFD` | Ghostfire | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 11805.1 -> **16131.7** | 4722.4 -> **6453.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 9888). Increasing spread: b -17.8%, n +36.7%; Individual spell undertuned (WR: 22.3%, Casts: 9888, mult: 1.110) |
| `FEF` | Beasts | Debuff / Control | 7.7 -> **6.6** (-14.3%) | - | 7.7 -> **6.6** | Individual spell overtuned (WR: 84.2%, Casts: 653, mult: 0.862) |
| `FEW` | Beasts | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 25307.7 -> **34671.5** | 7592.6 -> **10401.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 171). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 37.2%, Casts: 171, mult: 1.047) |
| `FEE` | Beasts | Buff / Sustain | 230.5 -> **243.4** (+5.6%) | - | 230.5 -> **243.4** | Individual spell undertuned (WR: 35.0%, Casts: 2863, mult: 1.056) |
| `FEL` | Beasts | Buff / Sustain | 198.0 -> **209.5** (+5.8%) | - | 198.0 -> **209.5** | Individual spell undertuned (WR: 34.5%, Casts: 6024, mult: 1.058) |
| `EFF` | Beasts | Debuff / Control | 0.4 -> **0.4** (+0.0%) | 12816.4 -> **17558.5** | 5127.0 -> **7023.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4728). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 5.9%, Casts: 4728, mult: 1.180) |
| `EFW` | Beasts | Buff / Sustain | 68.0 -> **69.0** (+1.5%) | - | 68.0 -> **69.0** | Individual spell undertuned (WR: 45.5%, Casts: 1311, mult: 1.015) |
| `EFE` | Beasts | Buff / Sustain | 7.2 -> **6.2** (-13.9%) | - | 7.2 -> **6.2** | Individual spell overtuned (WR: 84.1%, Casts: 4536, mult: 0.862) |
| `EFD` | Beasts | Ultimate | 3.6 -> **3.0** (-16.7%) | 1174.0 -> **1608.0** | 4230.0 -> **4827.0** | Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 4790). Increasing spread: b -18.0%, n +37.0% |
| `FLF` | Lightning | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 28365.4 -> **38825.1** | 11346.6 -> **15530.4** | Class Lightning undertuned (WR: 43.0%, factor: 1.028); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 668). Increasing spread: b -17.9%, n +36.9% |
| `FLW` | Lightning | Debuff / Control | 5.9 -> **6.2** (+5.1%) | - | 5.9 -> **6.2** | Class Lightning undertuned (WR: 43.0%, factor: 1.028); Status 'Stunned' appliers undertuned (WR: 44.0%, casts: 8846) |
| `FLE` | Lightning | Setup - Weather | 257.7 -> **251.6** (-2.4%) | - | 257.7 -> **251.6** | Class Lightning undertuned (WR: 43.0%, factor: 1.028); Weather 'Storming' appliers overtuned on own (WR: 57.6%) |
| `FLL` | Lightning | Buff / Sustain | 28.1 -> **28.9** (+2.8%) | - | 28.1 -> **28.9** | Class Lightning undertuned (WR: 43.0%, factor: 1.028) |
| `FLD` | Lightning | Ultimate | 2.0 -> **1.7** (-15.0%) | 1562.8 -> **2098.7** | 3127.6 -> **3569.5** | Class Lightning undertuned (WR: 43.0%, factor: 1.028); Weather 'Storming' beneficiaries overtuned (WR: 54.9%) |
| `LFF` | Lightning | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 13609.4 -> **18644.9** | 9527.3 -> **11187.5** | Class Lightning undertuned (WR: 43.0%, factor: 1.028); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5122). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 26.6 -> **27.7** (+4.1%) | - | 26.6 -> **27.7** | Class Lightning undertuned (WR: 43.0%, factor: 1.028); Individual spell undertuned (WR: 45.7%, Casts: 5216, mult: 1.014) |
| `LFE` | Lightning | Debuff / Control | 4.9 -> **4.6** (-6.1%) | - | 4.9 -> **4.6** | Class Lightning undertuned (WR: 43.0%, factor: 1.028); Status 'Stunned' appliers undertuned (WR: 44.0%, casts: 8846) |
| `LFL` | Lightning | Debuff / Control | 0.5 -> **0.4** (-20.0%) | 11902.2 -> **17192.4** | 5951.6 -> **6877.4** | Class Lightning undertuned (WR: 43.0%, factor: 1.028); Weather 'Darkness' beneficiaries undertuned (WR: 36.4%) |
| `LFD` | Lightning | Conditional Strike | 0.3 -> **0.4** (+33.3%) | 7586.7 -> **6113.9** | 2276.3 -> **2446.0** | Class Lightning undertuned (WR: 43.0%, factor: 1.028); Status 'Stunned' appliers undertuned (WR: 44.0%, casts: 8846) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 14353.1 -> **19663.7** | 2870.8 -> **3932.9** | Class Blood overtuned (WR: 53.8%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 498). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 90.7 -> **92.7** (+2.2%) | - | 90.7 -> **92.7** | Class Blood overtuned (WR: 53.8%, factor: 0.985); Individual spell undertuned (WR: 39.6%, Casts: 2418, mult: 1.038) |
| `FDE` | Blood | Setup - Weather | 60.3 -> **70.1** (+16.3%) | - | 60.3 -> **70.1** | Class Blood overtuned (WR: 53.8%, factor: 0.985); Individual spell undertuned (WR: 6.5%, Casts: 3370, mult: 1.180) |
| `FDD` | Blood | Ultimate | 3.7 -> **4.1** (+10.8%) | 185.0 -> **183.4** | 688.2 -> **756.0** | Class Blood overtuned (WR: 53.8%, factor: 0.985); Weather 'Darkness' beneficiaries undertuned (WR: 36.4%) |
| `DFF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 28800.0 -> **40974.0** | 5760.2 -> **8195.0** | Class Blood overtuned (WR: 53.8%, factor: 0.985); Status 'Bleeding' beneficiaries undertuned (WR: 39.8%) |
| `DFE` | Blood | Buff / Sustain | 468.7 -> **544.5** (+16.2%) | - | 468.7 -> **544.5** | Class Blood overtuned (WR: 53.8%, factor: 0.985); Individual spell undertuned (WR: 3.7%, Casts: 449, mult: 1.180) |
| `DFL` | Blood | Buff / Sustain | 3.4 -> **3.2** (-5.9%) | - | 3.4 -> **3.2** | Class Blood overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 59.8%, Casts: 319, mult: 0.965) |
| `DFD` | Blood | Conditional Strike | 147.0 -> **155.6** (+5.9%) | 0.1 -> **0.1** | 161.7 -> **171.2** | Class Blood overtuned (WR: 53.8%, factor: 0.985); Condition triggers excessively (N=1 conditions, Trigger Rate: 84.9% vs 55% ceiling, WR: 86.5%). Compressing spread: b +26.2%, n -33.2% |
| `WEF` | Plants | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 18227.2 -> **24971.3** | 5468.5 -> **4994.5** | Class Plants undertuned (WR: 46.3%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 342). Increasing spread: b -18.0%, n +37.0% |
| `WEW` | Plants | Debuff / Control | 232.4 -> **254.5** (+9.5%) | - | 232.4 -> **254.5** | Class Plants undertuned (WR: 46.3%, factor: 1.015); Individual spell undertuned (WR: 29.4%, Casts: 2930, mult: 1.079) |
| `WEE` | Plants | Setup - Location | 1562.7 -> **1925.3** (+23.2%) | - | 1562.7 -> **1925.3** | Class Plants undertuned (WR: 46.3%, factor: 1.015); Location 'Jungle' appliers undertuned (WR: 22.7%, casts: 7086) |
| `WEL` | Plants | Debuff / Control | 7.0 -> **5.5** (-21.4%) | - | 7.0 -> **5.5** | Class Plants undertuned (WR: 46.3%, factor: 1.015); Status 'Entangled' appliers overtuned on own (WR: 83.5%) |
| `WED` | Plants | Conditional Strike | 6.3 -> **5.2** (-17.5%) | 107.3 -> **147.0** | 682.3 -> **769.6** | Class Plants undertuned (WR: 46.3%, factor: 1.015); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4724). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 0.8 -> **0.7** (-12.5%) | 25538.7 -> **37666.8** | 20431.8 -> **26367.5** | Class Plants undertuned (WR: 46.3%, factor: 1.015); Weather 'Sunny' beneficiaries undertuned (WR: 27.3%) |
| `EWL` | Plants | Debuff / Control | 8.7 -> **7.9** (-9.2%) | - | 8.7 -> **7.9** | Class Plants undertuned (WR: 46.3%, factor: 1.015); Individual spell overtuned (WR: 76.3%, Casts: 4792, mult: 0.896) |
| `EWD` | Plants | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 22757.4 -> **30895.1** | 2275.8 -> **3089.6** | Class Plants undertuned (WR: 46.3%, factor: 1.015); Status 'Bleeding' appliers overtuned on own (WR: 88.4%) |
| `WLF` | Fey | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 12284.7 -> **16584.3** | 7371.4 -> **8292.6** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Status 'Cursed' beneficiaries overtuned (WR: 53.6%) |
| `WLW` | Fey | Debuff / Control | 6.8 -> **6.2** (-8.8%) | - | 6.8 -> **6.2** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Status 'Cursed' appliers overtuned on own (WR: 61.2%) |
| `WLE` | Fey | Setup - Location | 2406.4 -> **3091.4** (+28.5%) | - | 2406.4 -> **3091.4** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Location 'Enchanted Forest' appliers undertuned (WR: 19.6%, casts: 1127) |
| `WLL` | Fey | Direct Damage | 20.2 -> **18.3** (-9.4%) | - | 20.2 -> **18.3** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Individual spell overtuned (WR: 80.7%, Casts: 1132, mult: 0.877) |
| `WLD` | Fey | Ultimate | 6.2 -> **7.0** (+12.9%) | 1030.1 -> **1089.8** | 6392.8 -> **7635.6** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Weather 'Darkness' beneficiaries undertuned (WR: 36.4%) |
| `LWF` | Fey | Debuff / Control | 1.2 -> **1.1** (-8.3%) | 17534.9 -> **25469.8** | 21043.1 -> **28017.9** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Location 'Enchanted Forest' beneficiaries undertuned (WR: 33.1%) |
| `LWW` | Fey | Debuff / Control | 174.9 -> **187.7** (+7.3%) | - | 174.9 -> **187.7** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Individual spell undertuned (WR: 39.6%, Casts: 326, mult: 1.037) |
| `LWL` | Fey | Debuff / Control | 656.2 -> **649.5** (-1.0%) | - | 656.2 -> **649.5** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Individual spell overtuned (WR: 62.0%, Casts: 59, mult: 0.956) |
| `LWD` | Fey | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 14353.1 -> **19663.7** | 10047.9 -> **11798.8** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 7436). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 38766.3 -> **55512.5** | 7753.5 -> **11102.7** | Status 'Stunned' appliers undertuned (WR: 44.0%, casts: 8846); Weather 'Raining' beneficiaries undertuned (WR: 38.7%) |
| `WDW` | Ice | Buff / Sustain | 29.7 -> **31.4** (+5.7%) | - | 29.7 -> **31.4** | Status 'Frosty' appliers overtuned on own (WR: 54.2%); Individual spell undertuned (WR: 30.5%, Casts: 733, mult: 1.075) |
| `WDE` | Ice | Setup - Weather | 219.9 -> **235.7** (+7.2%) | - | 219.9 -> **235.7** | Individual spell undertuned (WR: 31.2%, Casts: 142, mult: 1.072) |
| `WDL` | Ice | Debuff / Control | 6.3 -> **6.1** (-3.2%) | - | 6.3 -> **6.1** | Status 'Frosty' appliers overtuned on own (WR: 54.2%); Individual spell overtuned (WR: 54.9%, Casts: 6860, mult: 0.984) |
| `WDD` | Ice | Ultimate | 6.7 -> **7.6** (+13.4%) | 119.0 -> **125.7** | 804.0 -> **962.9** | Weather 'Blizzard' beneficiaries undertuned (WR: 35.0%); Location 'Tundra' beneficiaries undertuned (WR: 35.0%) |
| `DWW` | Ice | Debuff / Control | 7.9 -> **7.2** (-8.9%) | - | 7.9 -> **7.2** | Individual spell overtuned (WR: 72.7%, Casts: 3710, mult: 0.912) |
| `DWE` | Ice | Setup - Location | 523.7 -> **682.8** (+30.4%) | - | 523.7 -> **682.8** | Location 'Tundra' appliers undertuned (WR: 10.2%, casts: 846); Individual spell undertuned (WR: 10.0%, Casts: 846, mult: 1.164) |
| `DWL` | Ice | Debuff / Control | 8.0 -> **7.6** (-5.0%) | - | 8.0 -> **7.6** | Status 'Frosty' appliers overtuned on own (WR: 54.2%); Individual spell overtuned (WR: 60.1%, Casts: 3964, mult: 0.964) |
| `DWD` | Ice | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 17098.1 -> **23746.6** | 8549.5 -> **9499.0** | Status 'Frosty' beneficiaries undertuned (WR: 38.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.1% vs 30% floor, Casts: 492). Increasing spread: b -16.0%, n +32.8% |
| `ELF` | Wind | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 31921.6 -> **44407.3** | 51076.2 -> **62171.6** | Status 'Bleeding' beneficiaries undertuned (WR: 39.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.0% vs 30% floor, Casts: 3209). Increasing spread: b -16.4%, n +33.7% |
| `ELW` | Wind | Debuff / Control | 19.9 -> **18.2** (-8.5%) | - | 19.9 -> **18.2** | Individual spell overtuned (WR: 72.0%, Casts: 1858, mult: 0.915) |
| `ELE` | Wind | Setup - Weather | 348.0 -> **386.6** (+11.1%) | - | 348.0 -> **386.6** | Individual spell undertuned (WR: 22.0%, Casts: 4090, mult: 1.111) |
| `ELL` | Wind | Buff / Sustain | 127.8 -> **132.4** (+3.6%) | - | 127.8 -> **132.4** | Individual spell undertuned (WR: 39.9%, Casts: 504, mult: 1.036) |
| `ELD` | Wind | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 33969.5 -> **48264.9** | 44161.7 -> **53092.5** | Weather 'Raining' beneficiaries undertuned (WR: 38.7%); Weather 'Blizzard' appliers undertuned (WR: 40.7%, casts: 2960) |
| `LEF` | Wind | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 34491.9 -> **49499.2** | 27594.3 -> **34650.1** | Status 'Burning' beneficiaries undertuned (WR: 31.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.0% vs 30% floor, Casts: 2360). Increasing spread: b -16.4%, n +33.6% |
| `LEW` | Wind | Debuff / Control | 15.7 -> **14.0** (-10.8%) | - | 15.7 -> **14.0** | Individual spell overtuned (WR: 77.5%, Casts: 3389, mult: 0.891) |
| `LEL` | Wind | Buff / Sustain | 644.4 -> **656.3** (+1.8%) | - | 644.4 -> **656.3** | Individual spell undertuned (WR: 44.5%, Casts: 2979, mult: 1.019) |
| `EDF` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 8841.4 -> **11510.0** | 1768.5 -> **2302.2** | Class Poison overtuned (WR: 60.1%, factor: 0.960); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 672). Increasing spread: b -14.7%, n +30.2% |
| `EDW` | Poison | Debuff / Control | 2.5 -> **2.4** (-4.0%) | - | 2.5 -> **2.4** | Class Poison overtuned (WR: 60.1%, factor: 0.960) |
| `EDE` | Poison | Setup - Location | 533.5 -> **577.1** (+8.2%) | - | 533.5 -> **577.1** | Class Poison overtuned (WR: 60.1%, factor: 0.960); Location 'Swamp' appliers undertuned (WR: 33.0%, casts: 4139) |
| `EDD` | Poison | Ultimate | 6.0 -> **4.7** (-21.7%) | 607.7 -> **866.6** | 3652.2 -> **4077.7** | Class Poison overtuned (WR: 60.1%, factor: 0.960); Status 'Bleeding' beneficiaries undertuned (WR: 39.8%) |
| `DEF` | Poison | Conditional Strike | 1.1 -> **0.8** (-27.3%) | 81.0 -> **103.5** | 90.2 -> **83.6** | Class Poison overtuned (WR: 60.1%, factor: 0.960); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.1% vs 30% floor, Casts: 298). Increasing spread: b -13.6%, n +27.8% |
| `DEW` | Poison | Debuff / Control | 2.9 -> **2.6** (-10.3%) | - | 2.9 -> **2.6** | Class Poison overtuned (WR: 60.1%, factor: 0.960); Individual spell overtuned (WR: 67.8%, Casts: 5274, mult: 0.933) |
| `DEE` | Poison | Debuff / Control | 6.4 -> **5.6** (-12.5%) | - | 6.4 -> **5.6** | Class Poison overtuned (WR: 60.1%, factor: 0.960); Individual spell overtuned (WR: 74.2%, Casts: 1843, mult: 0.905) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.1** (-50.0%) | 41187.3 -> **58569.0** | 8237.7 -> **5857.0** | Class Poison overtuned (WR: 60.1%, factor: 0.960); Status 'Bleeding' beneficiaries undertuned (WR: 39.8%) |
| `DED` | Poison | Debuff / Control | 8.6 -> **7.6** (-11.6%) | - | 8.6 -> **7.6** | Class Poison overtuned (WR: 60.1%, factor: 0.960); Individual spell overtuned (WR: 71.7%, Casts: 3861, mult: 0.916) |
| `LDF` | Cosmic | Debuff / Control | 10.9 -> **9.6** (-11.9%) | - | 10.9 -> **9.6** | Individual spell overtuned (WR: 80.8%, Casts: 6683, mult: 0.877) |
| `LDW` | Cosmic | Debuff / Control | 4.1 -> **4.5** (+9.8%) | - | 4.1 -> **4.5** | Status 'Stunned' appliers undertuned (WR: 44.0%, casts: 8846); Individual spell undertuned (WR: 32.7%, Casts: 660, mult: 1.065) |
| `LDE` | Cosmic | Setup - Location | 92.2 -> **108.8** (+18.0%) | - | 92.2 -> **108.8** | Individual spell undertuned (WR: 1.6%, Casts: 1274, mult: 1.180) |
| `LDL` | Cosmic | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 11944.2 -> **16363.6** | 4778.1 -> **4909.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1241). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 37.8%, Casts: 1241, mult: 1.044) |
| `LDD` | Cosmic | Ultimate | 4.9 -> **5.5** (+12.2%) | 265.9 -> **249.9** | 1307.8 -> **1380.0** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 3652, WR: 38.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 38.0%, Casts: 3652, mult: 1.044) |
| `DLF` | Cosmic | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 10776.2 -> **14754.4** | 3233.2 -> **2951.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 2021). Increasing spread: b -18.0%, n +36.9% |
| `DLW` | Cosmic | Direct Damage | 7.3 -> **7.0** (-4.1%) | - | 7.3 -> **7.0** | Individual spell overtuned (WR: 61.7%, Casts: 4149, mult: 0.958) |
| `DLE` | Cosmic | Direct Damage | 255.6 -> **287.8** (+12.6%) | - | 255.6 -> **287.8** | Individual spell undertuned (WR: 18.6%, Casts: 559, mult: 1.126) |
| `DLL` | Cosmic | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 13841.8 -> **19994.1** | 5537.1 -> **7998.0** | Weather 'Darkness' beneficiaries undertuned (WR: 36.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2778). Increasing spread: b -18.0%, n +37.0% |
