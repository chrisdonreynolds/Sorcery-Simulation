# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T20:16:18Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 59.8s  
**Total Spells Tuned:** 103 / 125  

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
| **Earth** | 17,514 | 65.5% | 65.5% | 16.0 | Overtuned ⚠️ |
| **Dark** | 12,790 | 64.2% | 64.2% | 2.4 | Overtuned ⚠️ |
| **Ice** | 29,689 | 59.5% | 59.6% | 2.7 | Overtuned ⚠️ |
| **Cosmic** | 25,088 | 56.3% | 56.3% | 3.1 | Overtuned ⚠️ |
| **Poison** | 30,922 | 55.9% | 55.9% | 1.6 | Overtuned ⚠️ |
| **Light** | 10,670 | 55.7% | 55.7% | 2.9 | Overtuned ⚠️ |
| **Beasts** | 24,441 | 54.6% | 54.6% | 2.7 | Overtuned ⚠️ |
| **Fire** | 17,986 | 53.8% | 53.8% | 2.3 | Overtuned ⚠️ |
| **Blood** | 31,698 | 53.3% | 53.3% | 10.6 | Balanced ✅ |
| **Ghostfire** | 30,445 | 48.1% | 48.1% | 1.1 | Balanced ✅ |
| **Fey** | 29,818 | 43.1% | 43.1% | 1.4 | Undertuned ⚠️ |
| **Wind** | 18,662 | 43.0% | 43.0% | 2.0 | Undertuned ⚠️ |
| **Plants** | 30,447 | 33.1% | 33.0% | 1.7 | Undertuned ⚠️ |
| **Lightning** | 16,432 | 33.0% | 33.0% | 0.5 | Undertuned ⚠️ |
| **Water** | 14,406 | 31.7% | 31.6% | 1.1 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 17,243 (60.7%) | 3,681 (23.4%) | 3.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 396 (23.5%) | 4,814 (22.8%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,558 (57.7%) | 6,409 (24.7%) | 1.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,317 (85.0%) | 23,126 (36.5%) | 0.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 9,994 (33.1%) | 1,338 (41.8%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,996 (39.6%) | 10,737 (41.9%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,996 (19.4%) | 6,581 (26.8%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 7.0 -> **6.5** (-7.1%) | - | 7.0 -> **6.5** | Class Fire overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 65.6%, Casts: 4408, mult: 0.942) |
| `FFW` | Fire | Debuff / Control | 4.4 -> **4.2** (-4.5%) | - | 4.4 -> **4.2** | Class Fire overtuned (WR: 53.8%, factor: 0.985); Status 'Burning' appliers overtuned on own (WR: 57.7%) |
| `FFE` | Fire | Debuff / Control | 4.4 -> **4.1** (-6.8%) | - | 4.4 -> **4.1** | Class Fire overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 64.6%, Casts: 4017, mult: 0.946) |
| `FFD` | Fire | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 47378.2 -> **71428.1** | 18951.7 -> **28571.6** | Class Fire overtuned (WR: 53.8%, factor: 0.985); Status 'Burning' beneficiaries undertuned (WR: 24.7%) |
| `WWF` | Water | Conditional Strike | 0.6 -> **0.6** (+0.0%) | 20579.6 -> **29690.8** | 12348.4 -> **17815.1** | Class Water undertuned (WR: 31.7%, factor: 1.073); Status 'Burning' beneficiaries undertuned (WR: 24.7%) |
| `WWE` | Water | Setup - Weather | 650.9 -> **868.1** (+33.4%) | - | 650.9 -> **868.1** | Class Water undertuned (WR: 31.7%, factor: 1.073); Weather 'Raining' appliers undertuned (WR: 19.4%, casts: 1996) |
| `WWD` | Water | Buff / Sustain | 35.1 -> **33.3** (-5.1%) | - | 35.1 -> **33.3** | Class Water undertuned (WR: 31.7%, factor: 1.073); Individual spell overtuned (WR: 79.1%, Casts: 543, mult: 0.884) |
| `EEF` | Earth | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 23122.1 -> **34368.4** | 6936.9 -> **10310.8** | Class Earth overtuned (WR: 65.5%, factor: 0.938); Status 'Frosty' beneficiaries undertuned (WR: 23.4%) |
| `EEW` | Earth | Buff / Sustain | 27.5 -> **28.0** (+1.8%) | - | 27.5 -> **28.0** | Class Earth overtuned (WR: 65.5%, factor: 0.938); Individual spell undertuned (WR: 27.8%, Casts: 2191, mult: 1.086) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 13599.4 -> **18631.2** | 1360.0 -> **1863.2** | Class Light overtuned (WR: 55.7%, factor: 0.977); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1804). Increasing spread: b -18.0%, n +37.0% |
| `LLW` | Light | Debuff / Control | 7.1 -> **6.5** (-8.5%) | - | 7.1 -> **6.5** | Class Light overtuned (WR: 55.7%, factor: 0.977); Individual spell overtuned (WR: 65.6%, Casts: 7049, mult: 0.942) |
| `LLE` | Light | Setup - Weather | 889.7 -> **1050.4** (+18.1%) | - | 889.7 -> **1050.4** | Class Light overtuned (WR: 55.7%, factor: 0.977); Weather 'Sunny' appliers undertuned (WR: 23.5%, casts: 396) |
| `LLL` | Light | Buff / Sustain | 5.3 -> **4.8** (-9.4%) | - | 5.3 -> **4.8** | Class Light overtuned (WR: 55.7%, factor: 0.977); Individual spell overtuned (WR: 69.3%, Casts: 268, mult: 0.926) |
| `LLD` | Light | Ultimate | 5.1 -> **6.2** (+21.6%) | 718.3 -> **748.8** | 3668.4 -> **4648.8** | Class Light overtuned (WR: 55.7%, factor: 0.977); Weather 'Sunny' beneficiaries undertuned (WR: 22.8%) |
| `DDF` | Dark | Conditional Strike | 0.2 -> **0.1** (-50.0%) | 19663.7 -> **26939.3** | 3932.9 -> **2694.0** | Class Dark overtuned (WR: 64.2%, factor: 0.943); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 404). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 7.1 -> **6.2** (-12.7%) | - | 7.1 -> **6.2** | Class Dark overtuned (WR: 64.2%, factor: 0.943); Individual spell overtuned (WR: 67.8%, Casts: 292, mult: 0.933) |
| `DDE` | Dark | Setup - Weather | 465.0 -> **328.5** (-29.4%) | - | 465.0 -> **328.5** | Class Dark overtuned (WR: 64.2%, factor: 0.943); Weather 'Darkness' appliers overtuned on own (WR: 89.0%) |
| `DDL` | Dark | Debuff / Control | 5.3 -> **4.7** (-11.3%) | - | 5.3 -> **4.7** | Class Dark overtuned (WR: 64.2%, factor: 0.943); Individual spell overtuned (WR: 64.0%, Casts: 11788, mult: 0.948) |
| `DDD` | Dark | Debuff / Control | 2.8 -> **2.5** (-10.7%) | - | 2.8 -> **2.5** | Class Dark overtuned (WR: 64.2%, factor: 0.943); Individual spell overtuned (WR: 64.9%, Casts: 253, mult: 0.945) |
| `FWW` | Ghostfire | Debuff / Control | 3.8 -> **3.5** (-7.9%) | - | 3.8 -> **3.5** | Status 'Cursed' appliers overtuned on own (WR: 63.3%); Individual spell overtuned (WR: 59.4%, Casts: 2586, mult: 0.967) |
| `FWE` | Ghostfire | Setup - Location | 120.2 -> **126.3** (+5.1%) | - | 120.2 -> **126.3** | Location 'Graveyard' appliers undertuned (WR: 42.9%, casts: 112); Individual spell undertuned (WR: 42.7%, Casts: 112, mult: 1.025) |
| `FWL` | Ghostfire | Debuff / Control | 8.4 -> **8.2** (-2.4%) | - | 8.4 -> **8.2** | Status 'Cursed' appliers overtuned on own (WR: 63.3%); Individual spell undertuned (WR: 41.6%, Casts: 4385, mult: 1.030) |
| `FWD` | Ghostfire | Ultimate | 0.8 -> **0.9** (+12.5%) | 659.6 -> **719.7** | 528.5 -> **648.6** | Status 'Cursed' beneficiaries undertuned (WR: 27.8%); Location 'Graveyard' beneficiaries undertuned (WR: 33.4%) |
| `WFF` | Ghostfire | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 51189.2 -> **73878.5** | 15357.1 -> **22163.8** | Status 'Bleeding' beneficiaries undertuned (WR: 36.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 2277). Increasing spread: b -18.0%, n +36.9% |
| `WFW` | Ghostfire | Debuff / Control | 2.9 -> **2.7** (-6.9%) | - | 2.9 -> **2.7** | Individual spell overtuned (WR: 69.9%, Casts: 8117, mult: 0.924) |
| `WFL` | Ghostfire | Buff / Sustain | 32.6 -> **28.7** (-12.0%) | - | 32.6 -> **28.7** | Individual spell overtuned (WR: 79.9%, Casts: 625, mult: 0.881) |
| `WFD` | Ghostfire | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 16131.7 -> **22018.4** | 6453.1 -> **8807.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 7984). Increasing spread: b -17.8%, n +36.5%; Individual spell undertuned (WR: 21.7%, Casts: 7984, mult: 1.112) |
| `FEF` | Beasts | Debuff / Control | 6.6 -> **6.4** (-3.0%) | - | 6.6 -> **6.4** | Class Beasts overtuned (WR: 54.6%, factor: 0.982); Individual spell overtuned (WR: 53.5%, Casts: 345, mult: 0.989) |
| `FEW` | Beasts | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 34671.5 -> **49031.4** | 10401.8 -> **9806.5** | Class Beasts overtuned (WR: 54.6%, factor: 0.982); Status 'Entangled' beneficiaries undertuned (WR: 41.9%) |
| `FEE` | Beasts | Buff / Sustain | 243.4 -> **251.2** (+3.2%) | - | 243.4 -> **251.2** | Class Beasts overtuned (WR: 54.6%, factor: 0.982); Individual spell undertuned (WR: 36.1%, Casts: 706, mult: 1.051) |
| `FEL` | Beasts | Buff / Sustain | 209.5 -> **205.7** (-1.8%) | - | 209.5 -> **205.7** | Class Beasts overtuned (WR: 54.6%, factor: 0.982) |
| `EFF` | Beasts | Debuff / Control | 0.4 -> **0.4** (+0.0%) | 17558.5 -> **24055.1** | 7023.8 -> **9622.4** | Class Beasts overtuned (WR: 54.6%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1756). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 69.0 -> **62.3** (-9.7%) | - | 69.0 -> **62.3** | Class Beasts overtuned (WR: 54.6%, factor: 0.982); Individual spell overtuned (WR: 70.9%, Casts: 592, mult: 0.920) |
| `EFE` | Beasts | Buff / Sustain | 6.2 -> **5.2** (-16.1%) | - | 6.2 -> **5.2** | Class Beasts overtuned (WR: 54.6%, factor: 0.982); Individual spell overtuned (WR: 86.6%, Casts: 4018, mult: 0.851) |
| `EFD` | Beasts | Ultimate | 3.0 -> **3.3** (+10.0%) | 1608.0 -> **1613.7** | 4827.0 -> **5328.5** | Class Beasts overtuned (WR: 54.6%, factor: 0.982); Status 'Entangled' beneficiaries undertuned (WR: 41.9%) |
| `FLF` | Lightning | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 38825.1 -> **54935.0** | 15530.4 -> **16480.8** | Class Lightning undertuned (WR: 33.0%, factor: 1.068); Status 'Stunned' beneficiaries undertuned (WR: 41.8%) |
| `FLW` | Lightning | Debuff / Control | 6.2 -> **7.3** (+17.7%) | - | 6.2 -> **7.3** | Class Lightning undertuned (WR: 33.0%, factor: 1.068); Status 'Stunned' appliers undertuned (WR: 33.1%, casts: 9994) |
| `FLE` | Lightning | Setup - Weather | 251.6 -> **346.5** (+37.7%) | - | 251.6 -> **346.5** | Class Lightning undertuned (WR: 33.0%, factor: 1.068); Weather 'Storming' appliers undertuned (WR: 13.7%, casts: 47) |
| `FLL` | Lightning | Buff / Sustain | 28.9 -> **35.5** (+22.8%) | - | 28.9 -> **35.5** | Class Lightning undertuned (WR: 33.0%, factor: 1.068); Individual spell undertuned (WR: 13.2%, Casts: 1644, mult: 1.150) |
| `FLD` | Lightning | Ultimate | 1.7 -> **2.1** (+23.5%) | 2098.7 -> **2139.3** | 3569.5 -> **4494.6** | Class Lightning undertuned (WR: 33.0%, factor: 1.068); Status 'Stunned' beneficiaries undertuned (WR: 41.8%) |
| `LFF` | Lightning | Conditional Strike | 0.6 -> **0.6** (+0.0%) | 18644.9 -> **25543.5** | 11187.5 -> **15326.7** | Class Lightning undertuned (WR: 33.0%, factor: 1.068); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3940). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 27.7 -> **32.2** (+16.2%) | - | 27.7 -> **32.2** | Class Lightning undertuned (WR: 33.0%, factor: 1.068); Individual spell undertuned (WR: 27.6%, Casts: 6685, mult: 1.087) |
| `LFL` | Lightning | Debuff / Control | 0.4 -> **0.3** (-25.0%) | 17192.4 -> **24260.2** | 6877.4 -> **7278.4** | Class Lightning undertuned (WR: 33.0%, factor: 1.068); Weather 'Darkness' beneficiaries undertuned (WR: 42.5%) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 19663.7 -> **26939.3** | 3932.9 -> **5388.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 328). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 92.7 -> **97.5** (+5.2%) | - | 92.7 -> **97.5** | Individual spell undertuned (WR: 35.9%, Casts: 1735, mult: 1.052) |
| `FDE` | Blood | Setup - Weather | 70.1 -> **80.4** (+14.7%) | - | 70.1 -> **80.4** | Individual spell undertuned (WR: 13.9%, Casts: 2134, mult: 1.147) |
| `FDD` | Blood | Ultimate | 4.1 -> **3.4** (-17.1%) | 183.4 -> **258.8** | 756.0 -> **883.3** | Weather 'Darkness' beneficiaries undertuned (WR: 42.5%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 8380). Increasing spread: b -18.0%, n +37.0% |
| `DFF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 40974.0 -> **58772.0** | 8195.0 -> **11754.6** | Status 'Bleeding' beneficiaries undertuned (WR: 36.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.1% vs 30% floor, Casts: 6568). Increasing spread: b -17.6%, n +36.1% |
| `DFE` | Blood | Buff / Sustain | 544.5 -> **642.5** (+18.0%) | - | 544.5 -> **642.5** | Individual spell undertuned (WR: 2.1%, Casts: 321, mult: 1.180) |
| `DFL` | Blood | Buff / Sustain | 3.2 -> **2.9** (-9.4%) | - | 3.2 -> **2.9** | Individual spell overtuned (WR: 77.0%, Casts: 861, mult: 0.893) |
| `DFD` | Blood | Conditional Strike | 155.6 -> **167.1** (+7.4%) | 0.1 -> **0.1** | 171.2 -> **183.8** | Condition triggers excessively (N=1 conditions, Trigger Rate: 84.5% vs 55% ceiling, WR: 86.6%). Compressing spread: b +26.2%, n -33.1%; Individual spell overtuned (WR: 86.6%, Casts: 3199, mult: 0.851) |
| `WEF` | Plants | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 24971.3 -> **35382.1** | 4994.5 -> **7076.6** | Class Plants undertuned (WR: 33.1%, factor: 1.068); Location 'Jungle' beneficiaries undertuned (WR: 41.4%) |
| `WEW` | Plants | Debuff / Control | 254.5 -> **314.5** (+23.6%) | - | 254.5 -> **314.5** | Class Plants undertuned (WR: 33.1%, factor: 1.068); Individual spell undertuned (WR: 11.5%, Casts: 3780, mult: 1.157) |
| `WEE` | Plants | Setup - Location | 1925.3 -> **2618.9** (+36.0%) | - | 1925.3 -> **2618.9** | Class Plants undertuned (WR: 33.1%, factor: 1.068); Location 'Jungle' appliers undertuned (WR: 15.9%, casts: 6968) |
| `WEL` | Plants | Debuff / Control | 5.5 -> **6.3** (+14.5%) | - | 5.5 -> **6.3** | Class Plants undertuned (WR: 33.1%, factor: 1.068); Status 'Entangled' appliers undertuned (WR: 39.6%, casts: 1996) |
| `WED` | Plants | Conditional Strike | 5.2 -> **6.1** (+17.3%) | 147.0 -> **138.2** | 769.6 -> **849.1** | Class Plants undertuned (WR: 33.1%, factor: 1.068); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4393, WR: 46.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 0.7 -> **0.7** (+0.0%) | 37666.8 -> **57096.0** | 26367.5 -> **39967.9** | Class Plants undertuned (WR: 33.1%, factor: 1.068); Weather 'Sunny' beneficiaries undertuned (WR: 22.8%) |
| `EWD` | Plants | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 30895.1 -> **41772.1** | 3089.6 -> **4177.3** | Class Plants undertuned (WR: 33.1%, factor: 1.068); Status 'Bleeding' appliers overtuned on own (WR: 85.0%) |
| `WLF` | Fey | Conditional Strike | 0.5 -> **0.5** (+0.0%) | 16584.3 -> **24735.3** | 8292.6 -> **12368.1** | Class Fey undertuned (WR: 43.1%, factor: 1.028); Status 'Cursed' beneficiaries undertuned (WR: 27.8%) |
| `WLW` | Fey | Debuff / Control | 6.2 -> **5.4** (-12.9%) | - | 6.2 -> **5.4** | Class Fey undertuned (WR: 43.1%, factor: 1.028); Status 'Cursed' appliers overtuned on own (WR: 63.3%) |
| `WLE` | Fey | Setup - Location | 3091.4 -> **4194.4** (+35.7%) | - | 3091.4 -> **4194.4** | Class Fey undertuned (WR: 43.1%, factor: 1.028); Location 'Enchanted Forest' appliers undertuned (WR: 7.7%, casts: 135) |
| `WLL` | Fey | Direct Damage | 18.3 -> **16.9** (-7.7%) | - | 18.3 -> **16.9** | Class Fey undertuned (WR: 43.1%, factor: 1.028); Individual spell overtuned (WR: 76.1%, Casts: 1233, mult: 0.897) |
| `WLD` | Fey | Ultimate | 7.0 -> **5.7** (-18.6%) | 1089.8 -> **1647.2** | 7635.6 -> **9394.7** | Class Fey undertuned (WR: 43.1%, factor: 1.028); Weather 'Darkness' beneficiaries undertuned (WR: 42.5%) |
| `LWF` | Fey | Debuff / Control | 1.1 -> **1.0** (-9.1%) | 25469.8 -> **37365.3** | 28017.9 -> **37366.3** | Class Fey undertuned (WR: 43.1%, factor: 1.028); Location 'Enchanted Forest' beneficiaries undertuned (WR: 32.2%) |
| `LWW` | Fey | Debuff / Control | 187.7 -> **204.5** (+9.0%) | - | 187.7 -> **204.5** | Class Fey undertuned (WR: 43.1%, factor: 1.028); Individual spell undertuned (WR: 34.0%, Casts: 388, mult: 1.060) |
| `LWL` | Fey | Debuff / Control | 649.5 -> **693.2** (+6.7%) | - | 649.5 -> **693.2** | Class Fey undertuned (WR: 43.1%, factor: 1.028); Individual spell undertuned (WR: 39.0%, Casts: 47, mult: 1.039) |
| `LWD` | Fey | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 19663.7 -> **26939.3** | 11798.8 -> **13470.1** | Class Fey undertuned (WR: 43.1%, factor: 1.028); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5797). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 55512.5 -> **83089.5** | 11102.7 -> **16618.1** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Status 'Stunned' appliers undertuned (WR: 33.1%, casts: 9994) |
| `WDW` | Ice | Buff / Sustain | 31.4 -> **30.6** (-2.5%) | - | 31.4 -> **30.6** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Status 'Frosty' appliers overtuned on own (WR: 60.7%) |
| `WDE` | Ice | Setup - Weather | 235.7 -> **267.5** (+13.5%) | - | 235.7 -> **267.5** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Individual spell undertuned (WR: 4.9%, Casts: 151, mult: 1.180) |
| `WDL` | Ice | Debuff / Control | 6.1 -> **5.4** (-11.5%) | - | 6.1 -> **5.4** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Status 'Frosty' appliers overtuned on own (WR: 60.7%) |
| `WDD` | Ice | Ultimate | 7.6 -> **5.5** (-27.6%) | 125.7 -> **141.7** | 962.9 -> **784.8** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Weather 'Blizzard' beneficiaries overtuned (WR: 73.2%) |
| `DWF` | Ice | Debuff / Control | 5.8 -> **5.2** (-10.3%) | - | 5.8 -> **5.2** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Status 'Frosty' appliers overtuned on own (WR: 60.7%) |
| `DWW` | Ice | Debuff / Control | 7.2 -> **6.5** (-9.7%) | - | 7.2 -> **6.5** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Individual spell overtuned (WR: 66.0%, Casts: 3476, mult: 0.940) |
| `DWE` | Ice | Setup - Location | 682.8 -> **652.4** (-4.5%) | - | 682.8 -> **652.4** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Individual spell overtuned (WR: 54.2%, Casts: 12, mult: 0.993) |
| `DWL` | Ice | Debuff / Control | 7.6 -> **6.5** (-14.5%) | - | 7.6 -> **6.5** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Status 'Frosty' appliers overtuned on own (WR: 60.7%) |
| `DWD` | Ice | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 23746.6 -> **35999.5** | 9499.0 -> **10800.1** | Class Ice overtuned (WR: 59.5%, factor: 0.962); Status 'Frosty' beneficiaries undertuned (WR: 23.4%) |
| `ELF` | Wind | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 44407.3 -> **63642.0** | 62171.6 -> **76371.6** | Class Wind undertuned (WR: 43.0%, factor: 1.028); Status 'Bleeding' beneficiaries undertuned (WR: 36.5%) |
| `ELW` | Wind | Debuff / Control | 18.2 -> **16.3** (-10.4%) | - | 18.2 -> **16.3** | Class Wind undertuned (WR: 43.0%, factor: 1.028); Individual spell overtuned (WR: 82.3%, Casts: 3343, mult: 0.870) |
| `ELE` | Wind | Setup - Weather | 386.6 -> **456.1** (+18.0%) | - | 386.6 -> **456.1** | Class Wind undertuned (WR: 43.0%, factor: 1.028); Individual spell undertuned (WR: 13.7%, Casts: 3089, mult: 1.147) |
| `ELL` | Wind | Buff / Sustain | 132.4 -> **141.8** (+7.1%) | - | 132.4 -> **141.8** | Class Wind undertuned (WR: 43.0%, factor: 1.028); Individual spell undertuned (WR: 38.5%, Casts: 378, mult: 1.042) |
| `ELD` | Wind | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 48264.9 -> **72259.1** | 53092.5 -> **72260.1** | Class Wind undertuned (WR: 43.0%, factor: 1.028); Weather 'Raining' beneficiaries undertuned (WR: 26.8%) |
| `LEF` | Wind | Conditional Strike | 0.7 -> **0.7** (+0.0%) | 49499.2 -> **73817.1** | 34650.1 -> **51672.7** | Class Wind undertuned (WR: 43.0%, factor: 1.028); Status 'Burning' beneficiaries undertuned (WR: 24.7%) |
| `LEW` | Wind | Debuff / Control | 14.0 -> **13.0** (-7.1%) | - | 14.0 -> **13.0** | Class Wind undertuned (WR: 43.0%, factor: 1.028); Individual spell overtuned (WR: 75.1%, Casts: 249, mult: 0.902) |
| `LEE` | Wind | Setup - Weather | 487.9 -> **487.4** (-0.1%) | - | 487.9 -> **487.4** | Class Wind undertuned (WR: 43.0%, factor: 1.028); Individual spell overtuned (WR: 58.1%, Casts: 222, mult: 0.972) |
| `LEL` | Wind | Buff / Sustain | 656.3 -> **613.9** (-6.5%) | - | 656.3 -> **613.9** | Class Wind undertuned (WR: 43.0%, factor: 1.028); Individual spell overtuned (WR: 73.2%, Casts: 1477, mult: 0.910) |
| `EDF` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 11510.0 -> **15756.2** | 2302.2 -> **3151.4** | Class Poison overtuned (WR: 55.9%, factor: 0.976); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 3140). Increasing spread: b -17.9%, n +36.9% |
| `EDW` | Poison | Debuff / Control | 2.4 -> **2.5** (+4.2%) | - | 2.4 -> **2.5** | Class Poison overtuned (WR: 55.9%, factor: 0.976); Individual spell undertuned (WR: 37.4%, Casts: 542, mult: 1.046) |
| `EDE` | Poison | Setup - Location | 577.1 -> **657.2** (+13.9%) | - | 577.1 -> **657.2** | Class Poison overtuned (WR: 55.9%, factor: 0.976); Location 'Swamp' appliers undertuned (WR: 28.3%, casts: 2473) |
| `EDD` | Poison | Ultimate | 4.7 -> **5.0** (+6.4%) | 866.6 -> **858.6** | 4077.7 -> **4298.0** | Class Poison overtuned (WR: 55.9%, factor: 0.976); Status 'Bleeding' beneficiaries undertuned (WR: 36.5%) |
| `DEF` | Poison | Conditional Strike | 0.8 -> **0.6** (-25.0%) | 103.5 -> **141.8** | 83.6 -> **85.7** | Class Poison overtuned (WR: 55.9%, factor: 0.976); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2). Increasing spread: b -18.0%, n +37.0% |
| `DEW` | Poison | Debuff / Control | 2.6 -> **2.4** (-7.7%) | - | 2.6 -> **2.4** | Class Poison overtuned (WR: 55.9%, factor: 0.976); Individual spell overtuned (WR: 61.2%, Casts: 5060, mult: 0.959) |
| `DEE` | Poison | Debuff / Control | 5.6 -> **4.6** (-17.9%) | - | 5.6 -> **4.6** | Class Poison overtuned (WR: 55.9%, factor: 0.976); Individual spell overtuned (WR: 89.7%, Casts: 1324, mult: 0.837) |
| `DEL` | Poison | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 58569.0 -> **84544.8** | 5857.0 -> **8454.6** | Class Poison overtuned (WR: 55.9%, factor: 0.976); Status 'Bleeding' beneficiaries undertuned (WR: 36.5%) |
| `DED` | Poison | Debuff / Control | 7.6 -> **6.9** (-9.2%) | - | 7.6 -> **6.9** | Class Poison overtuned (WR: 55.9%, factor: 0.976); Individual spell overtuned (WR: 69.2%, Casts: 4167, mult: 0.927) |
| `LDF` | Cosmic | Debuff / Control | 9.6 -> **8.3** (-13.5%) | - | 9.6 -> **8.3** | Class Cosmic overtuned (WR: 56.3%, factor: 0.975); Individual spell overtuned (WR: 78.0%, Casts: 7238, mult: 0.889) |
| `LDE` | Cosmic | Setup - Location | 108.8 -> **125.1** (+15.0%) | - | 108.8 -> **125.1** | Class Cosmic overtuned (WR: 56.3%, factor: 0.975); Individual spell undertuned (WR: 1.4%, Casts: 425, mult: 1.180) |
| `LDL` | Cosmic | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 16363.6 -> **22418.1** | 4909.4 -> **6725.7** | Class Cosmic overtuned (WR: 56.3%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1298). Increasing spread: b -18.0%, n +37.0% |
| `LDD` | Cosmic | Ultimate | 5.5 -> **4.3** (-21.8%) | 249.9 -> **342.4** | 1380.0 -> **1476.6** | Class Cosmic overtuned (WR: 56.3%, factor: 0.975); Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 3739). Increasing spread: b -18.0%, n +37.0% |
| `DLF` | Cosmic | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 14754.4 -> **20213.5** | 2951.1 -> **4042.9** | Class Cosmic overtuned (WR: 56.3%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1815). Increasing spread: b -18.0%, n +37.0% |
| `DLW` | Cosmic | Direct Damage | 7.0 -> **6.5** (-7.1%) | - | 7.0 -> **6.5** | Class Cosmic overtuned (WR: 56.3%, factor: 0.975); Individual spell overtuned (WR: 62.9%, Casts: 4646, mult: 0.953) |
| `DLE` | Cosmic | Direct Damage | 287.8 -> **293.7** (+2.1%) | - | 287.8 -> **293.7** | Class Cosmic overtuned (WR: 56.3%, factor: 0.975); Individual spell undertuned (WR: 37.2%, Casts: 367, mult: 1.047) |
| `DLL` | Cosmic | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 19994.1 -> **28213.7** | 7998.0 -> **11285.9** | Class Cosmic overtuned (WR: 56.3%, factor: 0.975); Weather 'Darkness' beneficiaries undertuned (WR: 42.5%) |
