# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T19:17:29Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 128.7s  
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
| **Blood** | 21,572 | 63.5% | 63.5% | 10.2 | Overtuned ⚠️ |
| **Poison** | 47,481 | 63.5% | 63.5% | 2.8 | Overtuned ⚠️ |
| **Earth** | 17,813 | 63.1% | 63.1% | 11.9 | Overtuned ⚠️ |
| **Fire** | 18,294 | 62.2% | 62.3% | 3.9 | Overtuned ⚠️ |
| **Water** | 12,823 | 55.2% | 55.2% | 3.0 | Overtuned ⚠️ |
| **Ghostfire** | 28,338 | 53.4% | 53.4% | 2.1 | Balanced ✅ |
| **Dark** | 10,494 | 51.9% | 51.9% | 2.1 | Balanced ✅ |
| **Ice** | 35,496 | 50.4% | 50.4% | 2.9 | Balanced ✅ |
| **Beasts** | 26,226 | 48.6% | 48.6% | 2.4 | Balanced ✅ |
| **Light** | 10,044 | 48.5% | 48.5% | 2.2 | Balanced ✅ |
| **Cosmic** | 32,919 | 45.0% | 45.0% | 3.6 | Undertuned ⚠️ |
| **Fey** | 25,116 | 43.4% | 43.4% | 3.6 | Undertuned ⚠️ |
| **Lightning** | 21,803 | 38.0% | 37.9% | 0.8 | Undertuned ⚠️ |
| **Plants** | 27,639 | 36.3% | 36.3% | 1.9 | Undertuned ⚠️ |
| **Wind** | 35,366 | 32.0% | 32.0% | 2.0 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 14,665 (61.7%) | 6,206 (28.2%) | 15.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,723 (26.7%) | 9,125 (36.6%) | 1.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,405 (50.4%) | 8,921 (30.8%) | 2.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,727 (85.0%) | 26,129 (42.0%) | 1.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 10,725 (64.1%) | 2,190 (38.1%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 4,359 (61.6%) | 3,871 (37.7%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 199 (41.8%) | 1,043 (43.3%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 11.8 -> **9.7** (-17.8%) | - | 11.8 -> **9.7** | Class Fire overtuned (WR: 62.2%, factor: 0.951); Individual spell overtuned (WR: 82.9%, Casts: 6291, mult: 0.868) |
| `FFE` | Fire | Debuff / Control | 6.6 -> **5.9** (-10.6%) | - | 6.6 -> **5.9** | Class Fire overtuned (WR: 62.2%, factor: 0.951); Individual spell overtuned (WR: 65.3%, Casts: 4282, mult: 0.943) |
| `FFD` | Fire | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 10789.3 -> **15372.6** | 7553.2 -> **9224.2** | Class Fire overtuned (WR: 62.2%, factor: 0.951); Status 'Burning' beneficiaries undertuned (WR: 30.8%) |
| `WWF` | Water | Conditional Strike | 0.7 -> **0.7** (+0.0%) | 5645.2 -> **7675.0** | 3952.3 -> **5373.2** | Class Water overtuned (WR: 55.2%, factor: 0.979); Status 'Burning' beneficiaries undertuned (WR: 30.8%) |
| `WWE` | Water | Setup - Weather | 338.9 -> **351.3** (+3.7%) | - | 338.9 -> **351.3** | Class Water overtuned (WR: 55.2%, factor: 0.979); Weather 'Raining' appliers undertuned (WR: 41.8%, casts: 199) |
| `WWL` | Water | Buff / Sustain | 10.4 -> **9.2** (-11.5%) | - | 10.4 -> **9.2** | Class Water overtuned (WR: 55.2%, factor: 0.979); Individual spell overtuned (WR: 73.9%, Casts: 7217, mult: 0.907) |
| `WWD` | Water | Buff / Sustain | 23.0 -> **25.3** (+10.0%) | - | 23.0 -> **25.3** | Class Water overtuned (WR: 55.2%, factor: 0.979); Individual spell undertuned (WR: 18.8%, Casts: 2753, mult: 1.125) |
| `EEF` | Earth | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 6861.1 -> **8634.6** | 3431.1 -> **3454.2** | Class Earth overtuned (WR: 63.1%, factor: 0.948); Status 'Frosty' beneficiaries undertuned (WR: 28.2%) |
| `EEW` | Earth | Buff / Sustain | 24.4 -> **25.3** (+3.7%) | - | 24.4 -> **25.3** | Class Earth overtuned (WR: 63.1%, factor: 0.948); Individual spell undertuned (WR: 25.5%, Casts: 1503, mult: 1.096) |
| `EEE` | Earth | Conditional Strike | 9.7 -> **9.9** (+2.1%) | 1.5 -> **1.5** | 24.2 -> **24.8** | Class Earth overtuned (WR: 63.1%, factor: 0.948); Condition triggers excessively (N=1 conditions, Trigger Rate: 94.7% vs 55% ceiling, WR: 92.6%). Compressing spread: b +30.9%, n -39.2% |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 4042.4 -> **5510.8** | 404.3 -> **551.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 495). Increasing spread: b -17.7%, n +36.3%; Individual spell overtuned (WR: 77.5%, Casts: 495, mult: 0.891) |
| `LLW` | Light | Debuff / Control | 9.4 -> **8.9** (-5.3%) | - | 9.4 -> **8.9** | Individual spell overtuned (WR: 64.4%, Casts: 3183, mult: 0.946) |
| `LLE` | Light | Setup - Weather | 624.4 -> **736.5** (+18.0%) | - | 624.4 -> **736.5** | Weather 'Sunny' appliers undertuned (WR: 26.7%, casts: 1723); Individual spell undertuned (WR: 26.7%, Casts: 1723, mult: 1.091) |
| `LLL` | Light | Buff / Sustain | 6.7 -> **5.6** (-16.4%) | - | 6.7 -> **5.6** | Individual spell overtuned (WR: 89.1%, Casts: 539, mult: 0.840) |
| `LLD` | Light | Ultimate | 4.7 -> **5.3** (+12.8%) | 521.1 -> **516.2** | 2453.9 -> **2741.2** | Weather 'Sunny' beneficiaries undertuned (WR: 36.6%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 4104, WR: 36.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 5581.9 -> **7647.2** | 2233.2 -> **2294.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3549). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 39.9%, Casts: 3549, mult: 1.036) |
| `DDW` | Dark | Debuff / Control | 10.9 -> **10.1** (-7.3%) | - | 10.9 -> **10.1** | Individual spell overtuned (WR: 70.1%, Casts: 808, mult: 0.923) |
| `DDE` | Dark | Setup - Weather | 447.7 -> **560.3** (+25.2%) | - | 447.7 -> **560.3** | Weather 'Darkness' appliers undertuned (WR: 18.4%, casts: 1443); Individual spell undertuned (WR: 18.4%, Casts: 1443, mult: 1.127) |
| `DDL` | Dark | Debuff / Control | 9.1 -> **8.3** (-8.8%) | - | 9.1 -> **8.3** | Individual spell overtuned (WR: 72.4%, Casts: 3859, mult: 0.913) |
| `FWW` | Ghostfire | Debuff / Control | 4.0 -> **4.3** (+7.5%) | - | 4.0 -> **4.3** | Status 'Cursed' appliers overtuned on own (WR: 62.6%); Individual spell undertuned (WR: 20.4%, Casts: 76, mult: 1.118) |
| `FWE` | Ghostfire | Setup - Location | 107.6 -> **133.4** (+24.0%) | - | 107.6 -> **133.4** | Location 'Graveyard' appliers undertuned (WR: 20.0%, casts: 193); Individual spell undertuned (WR: 19.5%, Casts: 193, mult: 1.122) |
| `FWL` | Ghostfire | Debuff / Control | 9.5 -> **8.8** (-7.4%) | - | 9.5 -> **8.8** | Status 'Cursed' appliers overtuned on own (WR: 62.6%); Individual spell overtuned (WR: 58.1%, Casts: 11781, mult: 0.971) |
| `FWD` | Ghostfire | Ultimate | 2.7 -> **2.0** (-25.9%) | 256.7 -> **329.2** | 695.8 -> **660.4** | Status 'Cursed' beneficiaries undertuned (WR: 42.5%); Location 'Graveyard' beneficiaries overtuned (WR: 72.9%) |
| `WFF` | Ghostfire | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 14322.1 -> **20246.0** | 5729.2 -> **6074.1** | Status 'Bleeding' beneficiaries undertuned (WR: 42.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 608). Increasing spread: b -18.0%, n +37.0% |
| `WFW` | Ghostfire | Debuff / Control | 3.5 -> **3.4** (-2.9%) | - | 3.5 -> **3.4** | Individual spell overtuned (WR: 58.4%, Casts: 8225, mult: 0.970) |
| `WFL` | Ghostfire | Buff / Sustain | 36.5 -> **33.3** (-8.8%) | - | 36.5 -> **33.3** | Individual spell overtuned (WR: 72.9%, Casts: 552, mult: 0.911) |
| `WFD` | Ghostfire | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 4616.5 -> **6309.6** | 2308.8 -> **2524.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 5359). Increasing spread: b -17.8%, n +36.7%; Individual spell undertuned (WR: 28.4%, Casts: 5359, mult: 1.083) |
| `FEF` | Beasts | Debuff / Control | 9.7 -> **8.7** (-10.3%) | - | 9.7 -> **8.7** | Individual spell overtuned (WR: 75.6%, Casts: 4657, mult: 0.899) |
| `FEW` | Beasts | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 8378.4 -> **12045.0** | 2513.8 -> **3613.8** | Status 'Entangled' beneficiaries undertuned (WR: 37.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1118). Increasing spread: b -18.0%, n +37.0% |
| `FEE` | Beasts | Buff / Sustain | 153.8 -> **181.5** (+18.0%) | - | 153.8 -> **181.5** | Individual spell undertuned (WR: 3.2%, Casts: 4578, mult: 1.180) |
| `FEL` | Beasts | Buff / Sustain | 180.4 -> **205.1** (+13.7%) | - | 180.4 -> **205.1** | Individual spell undertuned (WR: 16.2%, Casts: 3895, mult: 1.137) |
| `EFF` | Beasts | Debuff / Control | 0.5 -> **0.5** (+0.0%) | 4984.3 -> **6828.5** | 2492.7 -> **3414.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1958). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 18.8%, Casts: 1958, mult: 1.125) |
| `EFW` | Beasts | Buff / Sustain | 71.9 -> **72.3** (+0.6%) | - | 71.9 -> **72.3** | Individual spell undertuned (WR: 43.8%, Casts: 4, mult: 1.006) |
| `EFE` | Beasts | Buff / Sustain | 10.8 -> **9.5** (-12.0%) | - | 10.8 -> **9.5** | Individual spell overtuned (WR: 79.6%, Casts: 5600, mult: 0.882) |
| `EFD` | Beasts | Ultimate | 5.2 -> **4.2** (-19.2%) | 558.6 -> **814.4** | 2909.9 -> **3424.7** | Status 'Entangled' beneficiaries undertuned (WR: 37.7%); Location 'Jungle' beneficiaries undertuned (WR: 46.5%) |
| `FLF` | Lightning | Conditional Strike | 0.5 -> **0.5** (+0.0%) | 9920.0 -> **14238.9** | 4960.5 -> **7119.9** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Status 'Stunned' beneficiaries undertuned (WR: 38.1%) |
| `FLW` | Lightning | Debuff / Control | 6.8 -> **6.2** (-8.8%) | - | 6.8 -> **6.2** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Status 'Stunned' appliers overtuned on own (WR: 64.1%) |
| `FLE` | Lightning | Setup - Weather | 246.7 -> **225.1** (-8.8%) | - | 246.7 -> **225.1** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Weather 'Storming' appliers overtuned on own (WR: 68.1%) |
| `FLL` | Lightning | Buff / Sustain | 42.4 -> **36.4** (-14.2%) | - | 42.4 -> **36.4** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Individual spell overtuned (WR: 95.3%, Casts: 831, mult: 0.820) |
| `FLD` | Lightning | Ultimate | 3.3 -> **2.8** (-15.2%) | 598.7 -> **840.1** | 1979.0 -> **2355.1** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Status 'Stunned' beneficiaries undertuned (WR: 38.1%) |
| `LFF` | Lightning | Conditional Strike | 0.8 -> **0.8** (+0.0%) | 5292.7 -> **7251.0** | 4235.0 -> **5801.6** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 11297). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 20.2 -> **23.1** (+14.4%) | - | 20.2 -> **23.1** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Individual spell undertuned (WR: 26.4%, Casts: 3566, mult: 1.092) |
| `LFE` | Lightning | Debuff / Control | 6.5 -> **5.6** (-13.8%) | - | 6.5 -> **5.6** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Status 'Stunned' appliers overtuned on own (WR: 64.1%) |
| `LFL` | Lightning | Debuff / Control | 0.9 -> **0.8** (-11.1%) | 3987.9 -> **5724.4** | 3590.0 -> **4580.3** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Weather 'Darkness' beneficiaries undertuned (WR: 38.1%) |
| `LFD` | Lightning | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 4579.6 -> **6274.1** | 1832.2 -> **1882.5** | Class Lightning undertuned (WR: 38.0%, factor: 1.048); Status 'Stunned' appliers overtuned on own (WR: 64.1%) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 5581.9 -> **7647.2** | 1116.6 -> **1529.6** | Class Blood overtuned (WR: 63.5%, factor: 0.946); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1537). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 90.6 -> **92.2** (+1.8%) | - | 90.6 -> **92.2** | Class Blood overtuned (WR: 63.5%, factor: 0.946); Individual spell undertuned (WR: 30.3%, Casts: 1707, mult: 1.075) |
| `FDE` | Blood | Setup - Weather | 51.1 -> **53.1** (+3.9%) | - | 51.1 -> **53.1** | Class Blood overtuned (WR: 63.5%, factor: 0.946); Individual spell undertuned (WR: 25.0%, Casts: 729, mult: 1.098) |
| `FDD` | Blood | Ultimate | 3.0 -> **3.1** (+3.3%) | 191.9 -> **189.0** | 578.7 -> **589.0** | Class Blood overtuned (WR: 63.5%, factor: 0.946); Weather 'Darkness' beneficiaries undertuned (WR: 38.1%) |
| `DFF` | Blood | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 10390.2 -> **14617.2** | 5195.6 -> **5847.3** | Class Blood overtuned (WR: 63.5%, factor: 0.946); Status 'Bleeding' beneficiaries undertuned (WR: 42.0%) |
| `DFW` | Blood | Debuff / Control | 0.5 -> **0.3** (-40.0%) | - | 0.5 -> **0.3** | Class Blood overtuned (WR: 63.5%, factor: 0.946); Status 'Bleeding' appliers overtuned on own (WR: 85.0%) |
| `DFE` | Blood | Buff / Sustain | 331.2 -> **369.7** (+11.6%) | - | 331.2 -> **369.7** | Class Blood overtuned (WR: 63.5%, factor: 0.946); Individual spell undertuned (WR: 4.1%, Casts: 1065, mult: 1.180) |
| `DFL` | Blood | Buff / Sustain | 4.6 -> **4.3** (-6.5%) | - | 4.6 -> **4.3** | Class Blood overtuned (WR: 63.5%, factor: 0.946); Individual spell overtuned (WR: 55.2%, Casts: 908, mult: 0.983) |
| `DFD` | Blood | Conditional Strike | 139.6 -> **141.4** (+1.3%) | 0.1 -> **0.1** | 153.6 -> **155.5** | Class Blood overtuned (WR: 63.5%, factor: 0.946); Condition triggers excessively (N=1 conditions, Trigger Rate: 86.3% vs 55% ceiling, WR: 96.5%). Compressing spread: b +30.6%, n -37.7% |
| `WEF` | Plants | Conditional Strike | 0.5 -> **0.5** (+0.0%) | 7050.9 -> **9760.6** | 3525.9 -> **4880.8** | Class Plants undertuned (WR: 36.3%, factor: 1.055); Location 'Jungle' beneficiaries undertuned (WR: 46.5%) |
| `WEW` | Plants | Debuff / Control | 135.8 -> **167.1** (+23.0%) | - | 135.8 -> **167.1** | Class Plants undertuned (WR: 36.3%, factor: 1.055); Individual spell undertuned (WR: 9.5%, Casts: 6746, mult: 1.167) |
| `WEE` | Plants | Setup - Location | 901.2 -> **1092.8** (+21.3%) | - | 901.2 -> **1092.8** | Class Plants undertuned (WR: 36.3%, factor: 1.055); Location 'Jungle' appliers undertuned (WR: 30.3%, casts: 1303) |
| `WEL` | Plants | Debuff / Control | 7.5 -> **7.3** (-2.7%) | - | 7.5 -> **7.3** | Class Plants undertuned (WR: 36.3%, factor: 1.055); Status 'Entangled' appliers overtuned on own (WR: 61.6%) |
| `WED` | Plants | Conditional Strike | 5.8 -> **6.8** (+17.2%) | 88.6 -> **83.3** | 519.7 -> **573.2** | Class Plants undertuned (WR: 36.3%, factor: 1.055); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 6906, WR: 42.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 1.1 -> **1.0** (-9.1%) | 9226.8 -> **13044.0** | 10150.6 -> **13045.0** | Class Plants undertuned (WR: 36.3%, factor: 1.055); Weather 'Sunny' beneficiaries undertuned (WR: 36.6%) |
| `EWL` | Plants | Debuff / Control | 12.0 -> **11.0** (-8.3%) | - | 12.0 -> **11.0** | Class Plants undertuned (WR: 36.3%, factor: 1.055); Individual spell overtuned (WR: 82.7%, Casts: 1368, mult: 0.869) |
| `EWD` | Plants | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 7775.6 -> **11122.6** | 777.7 -> **1112.4** | Class Plants undertuned (WR: 36.3%, factor: 1.055); Status 'Bleeding' appliers overtuned on own (WR: 85.0%) |
| `WLF` | Fey | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 4437.8 -> **6197.6** | 3551.0 -> **4339.0** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Status 'Cursed' beneficiaries undertuned (WR: 42.5%) |
| `WLW` | Fey | Debuff / Control | 8.0 -> **7.1** (-11.3%) | - | 8.0 -> **7.1** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Status 'Cursed' appliers overtuned on own (WR: 62.6%) |
| `WLE` | Fey | Setup - Location | 1670.0 -> **1777.8** (+6.5%) | - | 1670.0 -> **1777.8** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Location 'Enchanted Forest' appliers undertuned (WR: 44.7%, casts: 510) |
| `WLL` | Fey | Direct Damage | 24.3 -> **21.6** (-11.1%) | - | 24.3 -> **21.6** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Individual spell overtuned (WR: 82.8%, Casts: 2628, mult: 0.868) |
| `WLD` | Fey | Ultimate | 5.6 -> **6.3** (+12.5%) | 653.1 -> **688.4** | 3663.0 -> **4343.2** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Weather 'Darkness' beneficiaries undertuned (WR: 38.1%) |
| `LWF` | Fey | Debuff / Control | 1.7 -> **1.6** (-5.9%) | 6108.7 -> **8907.2** | 10386.5 -> **14253.1** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Location 'Enchanted Forest' beneficiaries undertuned (WR: 32.4%) |
| `LWW` | Fey | Debuff / Control | 123.6 -> **140.5** (+13.7%) | - | 123.6 -> **140.5** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Individual spell undertuned (WR: 22.8%, Casts: 3608, mult: 1.108) |
| `LWL` | Fey | Debuff / Control | 531.1 -> **614.5** (+15.7%) | - | 531.1 -> **614.5** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Individual spell undertuned (WR: 18.3%, Casts: 59, mult: 1.127) |
| `LWD` | Fey | Conditional Strike | 0.7 -> **0.7** (+0.0%) | 5581.9 -> **7647.2** | 3908.0 -> **5353.7** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1258). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 13341.2 -> **18764.4** | 5336.9 -> **5629.6** | Status 'Stunned' appliers overtuned on own (WR: 64.1%); Weather 'Raining' beneficiaries undertuned (WR: 43.3%) |
| `WDW` | Ice | Buff / Sustain | 37.7 -> **36.2** (-4.0%) | - | 37.7 -> **36.2** | Status 'Frosty' appliers overtuned on own (WR: 61.7%) |
| `WDL` | Ice | Debuff / Control | 7.9 -> **7.3** (-7.6%) | - | 7.9 -> **7.3** | Status 'Frosty' appliers overtuned on own (WR: 61.7%); Individual spell overtuned (WR: 61.7%, Casts: 2742, mult: 0.958) |
| `WDD` | Ice | Ultimate | 5.1 -> **5.7** (+11.8%) | 123.2 -> **126.7** | 633.4 -> **727.9** | Weather 'Blizzard' beneficiaries undertuned (WR: 38.5%); Location 'Tundra' beneficiaries undertuned (WR: 38.5%) |
| `DWF` | Ice | Debuff / Control | 6.9 -> **6.3** (-8.7%) | - | 6.9 -> **6.3** | Status 'Frosty' appliers overtuned on own (WR: 61.7%); Individual spell overtuned (WR: 64.4%, Casts: 4876, mult: 0.947) |
| `DWW` | Ice | Debuff / Control | 9.6 -> **8.9** (-7.3%) | - | 9.6 -> **8.9** | Individual spell overtuned (WR: 68.4%, Casts: 4765, mult: 0.930) |
| `DWE` | Ice | Setup - Location | 277.1 -> **336.7** (+21.5%) | - | 277.1 -> **336.7** | Location 'Tundra' appliers undertuned (WR: 22.7%, casts: 424); Individual spell undertuned (WR: 22.5%, Casts: 424, mult: 1.109) |
| `DWL` | Ice | Debuff / Control | 10.1 -> **9.3** (-7.9%) | - | 10.1 -> **9.3** | Status 'Frosty' appliers overtuned on own (WR: 61.7%); Individual spell overtuned (WR: 60.1%, Casts: 6840, mult: 0.964) |
| `DWD` | Ice | Conditional Strike | 0.6 -> **0.6** (+0.0%) | 5553.4 -> **8182.9** | 3332.6 -> **4910.3** | Status 'Frosty' beneficiaries undertuned (WR: 28.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 2757). Increasing spread: b -17.3%, n +35.5% |
| `ELF` | Wind | Conditional Strike | 1.9 -> **1.9** (+0.0%) | 11910.7 -> **16428.6** | 22632.2 -> **31216.2** | Class Wind undertuned (WR: 32.0%, factor: 1.072); Status 'Bleeding' beneficiaries undertuned (WR: 42.0%) |
| `ELW` | Wind | Debuff / Control | 23.4 -> **22.2** (-5.1%) | - | 23.4 -> **22.2** | Class Wind undertuned (WR: 32.0%, factor: 1.072); Individual spell overtuned (WR: 78.9%, Casts: 686, mult: 0.885) |
| `ELE` | Wind | Setup - Weather | 195.1 -> **231.5** (+18.7%) | - | 195.1 -> **231.5** | Class Wind undertuned (WR: 32.0%, factor: 1.072); Individual spell undertuned (WR: 22.9%, Casts: 7676, mult: 1.107) |
| `ELL` | Wind | Buff / Sustain | 94.0 -> **106.5** (+13.3%) | - | 94.0 -> **106.5** | Class Wind undertuned (WR: 32.0%, factor: 1.072); Individual spell undertuned (WR: 34.7%, Casts: 539, mult: 1.057) |
| `ELD` | Wind | Conditional Strike | 3.0 -> **2.4** (-20.0%) | 11841.2 -> **16553.3** | 35526.6 -> **39730.3** | Class Wind undertuned (WR: 32.0%, factor: 1.072); Weather 'Raining' beneficiaries undertuned (WR: 43.3%) |
| `LEF` | Wind | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 11177.6 -> **16490.6** | 12296.5 -> **16491.6** | Class Wind undertuned (WR: 32.0%, factor: 1.072); Status 'Burning' beneficiaries undertuned (WR: 30.8%) |
| `LEW` | Wind | Debuff / Control | 19.8 -> **17.6** (-11.1%) | - | 19.8 -> **17.6** | Class Wind undertuned (WR: 32.0%, factor: 1.072); Individual spell overtuned (WR: 91.0%, Casts: 3834, mult: 0.831) |
| `LEE` | Wind | Setup - Weather | 280.8 -> **331.2** (+17.9%) | - | 280.8 -> **331.2** | Class Wind undertuned (WR: 32.0%, factor: 1.072); Individual spell undertuned (WR: 24.4%, Casts: 1261, mult: 1.100) |
| `LEL` | Wind | Buff / Sustain | 385.2 -> **479.5** (+24.5%) | - | 385.2 -> **479.5** | Class Wind undertuned (WR: 32.0%, factor: 1.072); Individual spell undertuned (WR: 10.7%, Casts: 4697, mult: 1.161) |
| `EDF` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 3528.9 -> **4834.6** | 706.0 -> **967.1** | Class Poison overtuned (WR: 63.5%, factor: 0.946); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 874). Increasing spread: b -18.0%, n +37.0% |
| `EDW` | Poison | Debuff / Control | 2.9 -> **2.5** (-13.8%) | - | 2.9 -> **2.5** | Class Poison overtuned (WR: 63.5%, factor: 0.946); Individual spell overtuned (WR: 72.4%, Casts: 7558, mult: 0.913) |
| `EDE` | Poison | Setup - Location | 452.6 -> **428.2** (-5.4%) | - | 452.6 -> **428.2** | Class Poison overtuned (WR: 63.5%, factor: 0.946) |
| `EDL` | Poison | Debuff / Control | 0.7 -> **0.5** (-28.6%) | - | 0.7 -> **0.5** | Class Poison overtuned (WR: 63.5%, factor: 0.946); Individual spell overtuned (WR: 98.3%, Casts: 3112, mult: 0.820) |
| `EDD` | Poison | Ultimate | 6.3 -> **4.9** (-22.2%) | 427.8 -> **604.7** | 2701.4 -> **2967.9** | Class Poison overtuned (WR: 63.5%, factor: 0.946); Status 'Bleeding' beneficiaries undertuned (WR: 42.0%) |
| `DEF` | Poison | Conditional Strike | 1.7 -> **1.3** (-23.5%) | 50.2 -> **68.8** | 87.0 -> **90.7** | Class Poison overtuned (WR: 63.5%, factor: 0.946); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 0). Increasing spread: b -18.0%, n +37.0% |
| `DEW` | Poison | Debuff / Control | 3.2 -> **3.0** (-6.3%) | - | 3.2 -> **3.0** | Class Poison overtuned (WR: 63.5%, factor: 0.946); Individual spell overtuned (WR: 54.1%, Casts: 3468, mult: 0.987) |
| `DEE` | Poison | Debuff / Control | 9.9 -> **8.1** (-18.2%) | - | 9.9 -> **8.1** | Class Poison overtuned (WR: 63.5%, factor: 0.946); Individual spell overtuned (WR: 84.2%, Casts: 8136, mult: 0.862) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 14582.6 -> **20576.6** | 4375.1 -> **6173.3** | Class Poison overtuned (WR: 63.5%, factor: 0.946); Status 'Bleeding' beneficiaries undertuned (WR: 42.0%) |
| `DED` | Poison | Debuff / Control | 10.6 -> **9.6** (-9.4%) | - | 10.6 -> **9.6** | Class Poison overtuned (WR: 63.5%, factor: 0.946); Individual spell overtuned (WR: 61.7%, Casts: 4260, mult: 0.958) |
| `LDF` | Cosmic | Debuff / Control | 16.6 -> **14.9** (-10.2%) | - | 16.6 -> **14.9** | Class Cosmic undertuned (WR: 45.0%, factor: 1.020); Individual spell overtuned (WR: 79.6%, Casts: 4869, mult: 0.882) |
| `LDW` | Cosmic | Debuff / Control | 6.2 -> **5.2** (-16.1%) | - | 6.2 -> **5.2** | Class Cosmic undertuned (WR: 45.0%, factor: 1.020); Status 'Stunned' appliers overtuned on own (WR: 64.1%) |
| `LDE` | Cosmic | Setup - Location | 69.8 -> **83.4** (+19.5%) | - | 69.8 -> **83.4** | Class Cosmic undertuned (WR: 45.0%, factor: 1.020); Individual spell undertuned (WR: 8.5%, Casts: 4166, mult: 1.171) |
| `LDL` | Cosmic | Conditional Strike | 0.6 -> **0.6** (+0.0%) | 4645.1 -> **6363.8** | 2787.7 -> **3818.9** | Class Cosmic undertuned (WR: 45.0%, factor: 1.020); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5131). Increasing spread: b -18.0%, n +37.0% |
| `LDD` | Cosmic | Ultimate | 5.0 -> **5.7** (+14.0%) | 219.7 -> **206.5** | 1103.5 -> **1182.8** | Class Cosmic undertuned (WR: 45.0%, factor: 1.020); Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 4272, WR: 41.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 4216.0 -> **5775.9** | 2530.2 -> **2888.4** | Class Cosmic undertuned (WR: 45.0%, factor: 1.020); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4270). Increasing spread: b -18.0%, n +37.0% |
| `DLW` | Cosmic | Direct Damage | 10.6 -> **10.2** (-3.8%) | - | 10.6 -> **10.2** | Class Cosmic undertuned (WR: 45.0%, factor: 1.020); Individual spell overtuned (WR: 65.0%, Casts: 2588, mult: 0.944) |
| `DLE` | Cosmic | Direct Damage | 290.6 -> **296.4** (+2.0%) | - | 290.6 -> **296.4** | Class Cosmic undertuned (WR: 45.0%, factor: 1.020) |
| `DLL` | Cosmic | Conditional Strike | 0.6 -> **0.6** (+0.0%) | 4686.2 -> **6657.2** | 2812.3 -> **3994.9** | Class Cosmic undertuned (WR: 45.0%, factor: 1.020); Weather 'Darkness' beneficiaries undertuned (WR: 38.1%) |
