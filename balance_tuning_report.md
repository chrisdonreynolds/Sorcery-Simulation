# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T15:32:15Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 110.9s  
**Total Spells Tuned:** 116 / 125  

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
| **Earth** | 17,850 | 63.0% | 63.0% | 17.4 | Overtuned ⚠️ |
| **Fire** | 7,710 | 61.6% | 61.6% | 10.1 | Overtuned ⚠️ |
| **Ghostfire** | 24,502 | 57.9% | 57.9% | 6.9 | Overtuned ⚠️ |
| **Blood** | 32,112 | 57.3% | 57.3% | 7.3 | Overtuned ⚠️ |
| **Dark** | 14,350 | 57.3% | 57.3% | 8.9 | Overtuned ⚠️ |
| **Ice** | 34,621 | 54.2% | 54.2% | 11.3 | Overtuned ⚠️ |
| **Poison** | 17,437 | 54.2% | 54.2% | 4.8 | Overtuned ⚠️ |
| **Cosmic** | 34,343 | 51.6% | 51.6% | 14.2 | Balanced ✅ |
| **Light** | 14,470 | 51.1% | 51.1% | 3.1 | Balanced ✅ |
| **Plants** | 16,739 | 46.7% | 46.7% | 3.0 | Balanced ✅ |
| **Lightning** | 21,134 | 45.9% | 45.9% | 4.5 | Undertuned ⚠️ |
| **Fey** | 25,113 | 45.5% | 45.4% | 6.6 | Undertuned ⚠️ |
| **Beasts** | 27,908 | 41.1% | 41.0% | 3.2 | Undertuned ⚠️ |
| **Water** | 19,932 | 39.5% | 39.4% | 2.6 | Undertuned ⚠️ |
| **Wind** | 28,869 | 38.0% | 38.0% | 4.2 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 16,714 (68.4%) | 7,546 (41.3%) | 4.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 3,700 (8.0%) | 5,325 (43.1%) | 2.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,599 (70.6%) | 12,899 (51.6%) | 1.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 12,487 (75.6%) | 9,467 (41.0%) | 1.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 16,353 (56.5%) | 3,586 (41.4%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 900 (38.5%) | 3,574 (34.9%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 3,515 (14.8%) | 3,885 (30.2%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 42.5 -> **37.6** (-11.5%) | - | 42.5 -> **37.6** | Class Fire overtuned (WR: 61.6%, factor: 0.954); Individual spell overtuned (WR: 69.0%, Casts: 1446, mult: 0.928) |
| `FFW` | Fire | Debuff / Control | 23.6 -> **21.6** (-8.5%) | - | 23.6 -> **21.6** | Class Fire overtuned (WR: 61.6%, factor: 0.954); Status 'Burning' appliers overtuned on own (WR: 70.6%) |
| `FFE` | Fire | Debuff / Control | 25.0 -> **23.4** (-6.4%) | - | 25.0 -> **23.4** | Class Fire overtuned (WR: 61.6%, factor: 0.954); Individual spell overtuned (WR: 55.2%, Casts: 1633, mult: 0.983) |
| `FFL` | Fire | Debuff / Control | 2.4 -> **1.9** (-20.8%) | - | 2.4 -> **1.9** | Class Fire overtuned (WR: 61.6%, factor: 0.954); Status 'Burning' appliers overtuned on own (WR: 70.6%) |
| `FFD` | Fire | Conditional Strike | 5.4 -> **4.9** (-9.3%) | 29.5 -> **40.0** | 164.7 -> **200.9** | Class Fire overtuned (WR: 61.6%, factor: 0.954); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 561). Increasing spread: b -17.3%, n +35.5% |
| `WWF` | Water | Conditional Strike | 5.5 -> **4.7** (-14.5%) | 23.3 -> **31.5** | 133.7 -> **152.8** | Class Water undertuned (WR: 39.5%, factor: 1.042); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 9602). Increasing spread: b -17.2%, n +35.4% |
| `WWE` | Water | Setup - Weather | 36.1 -> **48.2** (+33.5%) | - | 36.1 -> **48.2** | Class Water undertuned (WR: 39.5%, factor: 1.042); Weather 'Raining' appliers undertuned (WR: 14.8%, casts: 3515) |
| `WWL` | Water | Buff / Sustain | 43.7 -> **42.7** (-2.3%) | - | 43.7 -> **42.7** | Class Water undertuned (WR: 39.5%, factor: 1.042); Individual spell overtuned (WR: 66.5%, Casts: 1266, mult: 0.938) |
| `WWD` | Water | Buff / Sustain | 36.1 -> **34.6** (-4.2%) | - | 36.1 -> **34.6** | Class Water undertuned (WR: 39.5%, factor: 1.042); Individual spell overtuned (WR: 70.8%, Casts: 289, mult: 0.920) |
| `EEF` | Earth | Conditional Strike | 6.8 -> **5.6** (-17.6%) | 32.9 -> **44.1** | 230.5 -> **252.6** | Class Earth overtuned (WR: 63.0%, factor: 0.948); Status 'Frosty' beneficiaries undertuned (WR: 41.3%) |
| `EEW` | Earth | Buff / Sustain | 50.6 -> **46.6** (-7.9%) | - | 50.6 -> **46.6** | Class Earth overtuned (WR: 63.0%, factor: 0.948); Individual spell overtuned (WR: 57.9%, Casts: 2572, mult: 0.972) |
| `EED` | Earth | Direct Damage | 4.4 -> **3.9** (-11.4%) | - | 4.4 -> **3.9** | Class Earth overtuned (WR: 63.0%, factor: 0.948); Individual spell overtuned (WR: 68.4%, Casts: 5886, mult: 0.930) |
| `LLF` | Light | Conditional Strike | 0.6 -> **0.4** (-33.3%) | 32.3 -> **44.0** | 20.0 -> **18.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.1% vs 30% floor, Casts: 3710). Increasing spread: b -17.6%, n +36.1%; Individual spell overtuned (WR: 73.5%, Casts: 3710, mult: 0.909) |
| `LLW` | Light | Debuff / Control | 22.6 -> **21.6** (-4.4%) | - | 22.6 -> **21.6** | Individual spell overtuned (WR: 62.1%, Casts: 3420, mult: 0.956) |
| `LLE` | Light | Setup - Weather | 65.4 -> **86.0** (+31.5%) | - | 65.4 -> **86.0** | Weather 'Sunny' appliers undertuned (WR: 8.0%, casts: 3700); Individual spell undertuned (WR: 8.0%, Casts: 3700, mult: 1.174) |
| `LLL` | Light | Buff / Sustain | 17.8 -> **16.4** (-7.9%) | - | 17.8 -> **16.4** | Individual spell overtuned (WR: 70.8%, Casts: 2166, mult: 0.920) |
| `LLD` | Light | Ultimate | 16.1 -> **13.2** (-18.0%) | 19.3 -> **27.2** | 326.8 -> **372.2** | Weather 'Sunny' beneficiaries undertuned (WR: 43.1%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1474). Increasing spread: b -18.0%, n +37.0% |
| `DDF` | Dark | Conditional Strike | 4.6 -> **3.6** (-21.7%) | 36.2 -> **49.6** | 171.1 -> **182.2** | Class Dark overtuned (WR: 57.3%, factor: 0.971); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4708). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 42.2 -> **39.4** (-6.6%) | - | 42.2 -> **39.4** | Class Dark overtuned (WR: 57.3%, factor: 0.971); Individual spell overtuned (WR: 60.4%, Casts: 4567, mult: 0.963) |
| `DDE` | Dark | Setup - Weather | 56.0 -> **65.1** (+16.2%) | - | 56.0 -> **65.1** | Class Dark overtuned (WR: 57.3%, factor: 0.971); Weather 'Darkness' appliers undertuned (WR: 24.7%, casts: 838) |
| `DDL` | Dark | Debuff / Control | 19.3 -> **19.1** (-1.0%) | - | 19.3 -> **19.1** | Class Dark overtuned (WR: 57.3%, factor: 0.971); Individual spell undertuned (WR: 44.2%, Casts: 2395, mult: 1.019) |
| `DDD` | Dark | Debuff / Control | 15.5 -> **12.9** (-16.8%) | - | 15.5 -> **12.9** | Class Dark overtuned (WR: 57.3%, factor: 0.971); Individual spell overtuned (WR: 85.5%, Casts: 1842, mult: 0.856) |
| `FWF` | Ghostfire | Debuff / Control | 11.6 -> **9.4** (-19.0%) | - | 11.6 -> **9.4** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Status 'Burning' appliers overtuned on own (WR: 70.6%) |
| `FWW` | Ghostfire | Debuff / Control | 12.2 -> **10.9** (-10.7%) | - | 12.2 -> **10.9** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Status 'Cursed' appliers overtuned on own (WR: 59.7%) |
| `FWE` | Ghostfire | Setup - Location | 54.0 -> **61.8** (+14.4%) | - | 54.0 -> **61.8** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Location 'Graveyard' appliers undertuned (WR: 25.5%, casts: 38) |
| `FWL` | Ghostfire | Debuff / Control | 31.2 -> **29.2** (-6.4%) | - | 31.2 -> **29.2** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Status 'Cursed' appliers overtuned on own (WR: 59.7%) |
| `FWD` | Ghostfire | Ultimate | 12.6 -> **13.6** (+7.9%) | 20.6 -> **20.8** | 272.2 -> **296.5** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Status 'Cursed' beneficiaries undertuned (WR: 41.5%) |
| `WFF` | Ghostfire | Conditional Strike | 5.0 -> **3.8** (-24.0%) | 40.5 -> **57.5** | 207.5 -> **222.3** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Status 'Bleeding' beneficiaries undertuned (WR: 41.0%) |
| `WFW` | Ghostfire | Debuff / Control | 17.4 -> **15.9** (-8.6%) | - | 17.4 -> **15.9** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Individual spell overtuned (WR: 64.9%, Casts: 885, mult: 0.945) |
| `WFE` | Ghostfire | Debuff / Control | 7.7 -> **5.9** (-23.4%) | - | 7.7 -> **5.9** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Status 'Bleeding' appliers overtuned on own (WR: 75.6%) |
| `WFL` | Ghostfire | Buff / Sustain | 38.7 -> **40.0** (+3.4%) | - | 38.7 -> **40.0** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Individual spell undertuned (WR: 32.1%, Casts: 278, mult: 1.068) |
| `WFD` | Ghostfire | Conditional Strike | 4.7 -> **3.6** (-23.4%) | 31.5 -> **43.0** | 152.8 -> **158.4** | Class Ghostfire overtuned (WR: 57.9%, factor: 0.968); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 1978). Increasing spread: b -17.7%, n +36.4% |
| `FEF` | Beasts | Debuff / Control | 20.1 -> **18.8** (-6.5%) | - | 20.1 -> **18.8** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell overtuned (WR: 74.6%, Casts: 5699, mult: 0.904) |
| `FEW` | Beasts | Conditional Strike | 5.3 -> **4.5** (-15.1%) | 39.2 -> **57.0** | 213.1 -> **261.0** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Status 'Entangled' beneficiaries undertuned (WR: 34.9%) |
| `FEE` | Beasts | Buff / Sustain | 28.3 -> **30.3** (+7.1%) | - | 28.3 -> **30.3** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell undertuned (WR: 40.2%, Casts: 617, mult: 1.035) |
| `FEL` | Beasts | Buff / Sustain | 54.1 -> **64.4** (+19.0%) | - | 54.1 -> **64.4** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell undertuned (WR: 13.2%, Casts: 6107, mult: 1.150) |
| `FED` | Beasts | Conditional Strike | 4.6 -> **4.4** (-4.3%) | 3.5 -> **3.5** | 20.7 -> **19.8** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.9% vs 30% floor, Casts: 4407). Increasing spread: b -14.8%, n +30.4% |
| `EFF` | Beasts | Debuff / Control | 8.1 -> **7.9** (-2.5%) | 34.5 -> **46.4** | 287.6 -> **374.5** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 6115). Increasing spread: b -16.8%, n +34.5% |
| `EFW` | Beasts | Buff / Sustain | 28.0 -> **30.3** (+8.2%) | - | 28.0 -> **30.3** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell undertuned (WR: 32.4%, Casts: 22, mult: 1.044) |
| `EFE` | Beasts | Buff / Sustain | 28.7 -> **29.7** (+3.5%) | - | 28.7 -> **29.7** | Class Beasts undertuned (WR: 41.1%, factor: 1.036) |
| `EFL` | Beasts | Buff / Sustain | 7.6 -> **6.5** (-14.5%) | - | 7.6 -> **6.5** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell overtuned (WR: 94.3%, Casts: 3107, mult: 0.820) |
| `EFD` | Beasts | Ultimate | 12.6 -> **15.0** (+19.0%) | 40.4 -> **42.2** | 521.6 -> **648.0** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Status 'Entangled' beneficiaries undertuned (WR: 34.9%) |
| `FLF` | Lightning | Conditional Strike | 4.8 -> **4.1** (-14.6%) | 39.2 -> **55.6** | 193.0 -> **232.1** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Status 'Stunned' beneficiaries undertuned (WR: 41.4%) |
| `FLW` | Lightning | Debuff / Control | 26.8 -> **24.4** (-9.0%) | - | 26.8 -> **24.4** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Status 'Stunned' appliers overtuned on own (WR: 56.5%) |
| `FLE` | Lightning | Setup - Weather | 27.2 -> **27.8** (+2.2%) | - | 27.2 -> **27.8** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Weather 'Storming' appliers undertuned (WR: 48.5%, casts: 19) |
| `FLL` | Lightning | Buff / Sustain | 34.2 -> **39.6** (+15.8%) | - | 34.2 -> **39.6** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Individual spell undertuned (WR: 15.6%, Casts: 4185, mult: 1.139) |
| `FLD` | Lightning | Ultimate | 19.5 -> **22.6** (+15.9%) | 16.6 -> **17.1** | 343.2 -> **409.1** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Status 'Stunned' beneficiaries undertuned (WR: 41.4%) |
| `LFF` | Lightning | Conditional Strike | 5.7 -> **4.9** (-14.0%) | 34.4 -> **47.1** | 201.8 -> **235.7** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2313). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 25.8 -> **24.7** (-4.3%) | - | 25.8 -> **24.7** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 65.7%, Casts: 2941, mult: 0.941) |
| `LFE` | Lightning | Debuff / Control | 24.9 -> **22.8** (-8.4%) | - | 24.9 -> **22.8** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Status 'Stunned' appliers overtuned on own (WR: 56.5%) |
| `LFL` | Lightning | Debuff / Control | 8.6 -> **7.2** (-16.3%) | 25.9 -> **35.4** | 231.3 -> **262.1** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 3921). Increasing spread: b -17.8%, n +36.6% |
| `LFD` | Lightning | Conditional Strike | 5.2 -> **5.0** (-3.8%) | 44.0 -> **57.7** | 234.0 -> **293.5** | Class Lightning undertuned (WR: 45.9%, factor: 1.016); Status 'Stunned' appliers overtuned on own (WR: 56.5%) |
| `FDF` | Blood | Conditional Strike | 4.2 -> **3.2** (-23.8%) | 36.2 -> **49.6** | 156.2 -> **161.9** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2688). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 74.5 -> **70.4** (-5.5%) | - | 74.5 -> **70.4** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Individual spell overtuned (WR: 60.0%, Casts: 28, mult: 0.973) |
| `FDE` | Blood | Setup - Weather | 37.3 -> **40.5** (+8.6%) | - | 37.3 -> **40.5** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Individual spell undertuned (WR: 20.3%, Casts: 3737, mult: 1.118) |
| `FDL` | Blood | Debuff / Control | 7.5 -> **5.6** (-25.3%) | - | 7.5 -> **5.6** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Status 'Bleeding' appliers overtuned on own (WR: 75.6%) |
| `FDD` | Blood | Ultimate | 12.2 -> **9.7** (-20.5%) | 19.6 -> **26.8** | 251.3 -> **269.7** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 7795). Increasing spread: b -18.0%, n +37.0% |
| `DFF` | Blood | Conditional Strike | 5.6 -> **4.8** (-14.3%) | 36.9 -> **51.0** | 212.2 -> **249.6** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Status 'Bleeding' beneficiaries undertuned (WR: 41.0%) |
| `DFW` | Blood | Debuff / Control | 5.9 -> **4.5** (-23.7%) | - | 5.9 -> **4.5** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Status 'Bleeding' appliers overtuned on own (WR: 75.6%) |
| `DFE` | Blood | Buff / Sustain | 77.2 -> **87.1** (+12.8%) | - | 77.2 -> **87.1** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Individual spell undertuned (WR: 10.6%, Casts: 1576, mult: 1.162) |
| `DFL` | Blood | Buff / Sustain | 20.9 -> **18.3** (-12.4%) | - | 20.9 -> **18.3** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Individual spell overtuned (WR: 75.5%, Casts: 3995, mult: 0.900) |
| `DFD` | Blood | Conditional Strike | 62.1 -> **64.4** (+3.7%) | 0.1 -> **0.1** | 68.3 -> **70.8** | Class Blood overtuned (WR: 57.3%, factor: 0.971); Condition triggers excessively (N=1 conditions, Trigger Rate: 71.2% vs 55% ceiling, WR: 76.5%). Compressing spread: b +19.2%, n -24.4% |
| `WEF` | Plants | Conditional Strike | 5.7 -> **4.9** (-14.0%) | 38.4 -> **55.2** | 224.6 -> **275.4** | Location 'Jungle' beneficiaries undertuned (WR: 37.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2936). Increasing spread: b -18.0%, n +37.0% |
| `WEW` | Plants | Debuff / Control | 33.2 -> **33.7** (+1.5%) | - | 33.2 -> **33.7** | Individual spell undertuned (WR: 45.8%, Casts: 1991, mult: 1.014) |
| `WEE` | Plants | Setup - Location | 45.3 -> **51.0** (+12.6%) | - | 45.3 -> **51.0** | Location 'Jungle' appliers undertuned (WR: 33.4%, casts: 154); Individual spell undertuned (WR: 33.1%, Casts: 154, mult: 1.064) |
| `WEL` | Plants | Debuff / Control | 31.3 -> **33.9** (+8.3%) | - | 31.3 -> **33.9** | Status 'Entangled' appliers undertuned (WR: 38.5%, casts: 900); Individual spell undertuned (WR: 38.5%, Casts: 900, mult: 1.042) |
| `WED` | Plants | Conditional Strike | 11.6 -> **12.8** (+10.3%) | 11.8 -> **11.1** | 148.5 -> **154.9** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1977, WR: 43.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 43.9%, Casts: 1977, mult: 1.021) |
| `EWF` | Plants | Buff / Sustain | 5.2 -> **4.5** (-13.5%) | 27.6 -> **38.1** | 148.7 -> **176.0** | Weather 'Sunny' beneficiaries undertuned (WR: 43.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.2% vs 30% floor, Casts: 3851). Increasing spread: b -16.7%, n +34.3% |
| `EWW` | Plants | Debuff / Control | 8.0 -> **6.6** (-17.5%) | - | 8.0 -> **6.6** | Individual spell overtuned (WR: 92.2%, Casts: 1974, mult: 0.826) |
| `EWL` | Plants | Debuff / Control | 46.6 -> **42.5** (-8.8%) | - | 46.6 -> **42.5** | Individual spell overtuned (WR: 72.4%, Casts: 115, mult: 0.913) |
| `EWD` | Plants | Conditional Strike | 2.1 -> **1.7** (-19.0%) | 38.5 -> **55.8** | 83.0 -> **96.6** | Status 'Bleeding' appliers overtuned on own (WR: 75.6%); Status 'Entangled' beneficiaries undertuned (WR: 34.9%) |
| `WLF` | Fey | Conditional Strike | 6.8 -> **5.4** (-20.6%) | 31.5 -> **39.6** | 221.0 -> **219.2** | Class Fey undertuned (WR: 45.5%, factor: 1.018); Status 'Cursed' beneficiaries undertuned (WR: 41.5%) |
| `WLW` | Fey | Debuff / Control | 34.2 -> **30.5** (-10.8%) | - | 34.2 -> **30.5** | Class Fey undertuned (WR: 45.5%, factor: 1.018); Status 'Cursed' appliers overtuned on own (WR: 59.7%) |
| `WLE` | Fey | Setup - Location | 99.9 -> **122.0** (+22.1%) | - | 99.9 -> **122.0** | Class Fey undertuned (WR: 45.5%, factor: 1.018); Location 'Enchanted Forest' appliers undertuned (WR: 24.4%, casts: 3140) |
| `WLL` | Fey | Direct Damage | 56.6 -> **56.3** (-0.5%) | - | 56.6 -> **56.3** | Class Fey undertuned (WR: 45.5%, factor: 1.018); Individual spell overtuned (WR: 56.5%, Casts: 1733, mult: 0.978) |
| `WLD` | Fey | Ultimate | 24.7 -> **20.3** (-17.8%) | 14.9 -> **19.8** | 392.7 -> **422.2** | Class Fey undertuned (WR: 45.5%, factor: 1.018); Location 'Enchanted Forest' beneficiaries overtuned (WR: 57.2%) |
| `LWF` | Fey | Debuff / Control | 11.4 -> **9.6** (-15.8%) | 31.3 -> **39.3** | 368.2 -> **386.9** | Class Fey undertuned (WR: 45.5%, factor: 1.018); Location 'Enchanted Forest' beneficiaries overtuned (WR: 57.2%) |
| `LWW` | Fey | Debuff / Control | 67.4 -> **71.7** (+6.4%) | - | 67.4 -> **71.7** | Class Fey undertuned (WR: 45.5%, factor: 1.018); Individual spell undertuned (WR: 37.5%, Casts: 1823, mult: 1.045) |
| `LWL` | Fey | Debuff / Control | 48.0 -> **56.7** (+18.1%) | - | 48.0 -> **56.7** | Class Fey undertuned (WR: 45.5%, factor: 1.018); Individual spell undertuned (WR: 11.0%, Casts: 2335, mult: 1.160) |
| `LWD` | Fey | Conditional Strike | 7.7 -> **6.6** (-14.3%) | 36.2 -> **49.6** | 286.4 -> **334.0** | Class Fey undertuned (WR: 45.5%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4177). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 7.1 -> **6.0** (-15.5%) | 35.8 -> **52.9** | 261.3 -> **323.4** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Stunned' appliers overtuned on own (WR: 56.5%) |
| `WDW` | Ice | Buff / Sustain | 29.0 -> **27.5** (-5.2%) | - | 29.0 -> **27.5** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 68.4%) |
| `WDE` | Ice | Setup - Weather | 44.0 -> **41.3** (-6.1%) | - | 44.0 -> **41.3** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Individual spell overtuned (WR: 62.6%, Casts: 437, mult: 0.954) |
| `WDL` | Ice | Debuff / Control | 49.5 -> **40.5** (-18.2%) | - | 49.5 -> **40.5** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 68.4%) |
| `WDD` | Ice | Ultimate | 17.7 -> **19.3** (+9.0%) | 20.3 -> **20.3** | 377.0 -> **411.1** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Weather 'Blizzard' beneficiaries undertuned (WR: 42.1%) |
| `DWF` | Ice | Debuff / Control | 48.5 -> **39.5** (-18.6%) | - | 48.5 -> **39.5** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 68.4%) |
| `DWW` | Ice | Debuff / Control | 36.3 -> **33.9** (-6.6%) | - | 36.3 -> **33.9** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Individual spell overtuned (WR: 63.8%, Casts: 4721, mult: 0.949) |
| `DWE` | Ice | Setup - Location | 40.3 -> **50.0** (+24.1%) | - | 40.3 -> **50.0** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Location 'Tundra' appliers undertuned (WR: 17.4%, casts: 3502) |
| `DWL` | Ice | Debuff / Control | 48.9 -> **40.5** (-17.2%) | - | 48.9 -> **40.5** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 68.4%) |
| `DWD` | Ice | Conditional Strike | 10.4 -> **8.7** (-16.3%) | 28.2 -> **39.4** | 303.7 -> **351.5** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' beneficiaries undertuned (WR: 41.3%) |
| `ELF` | Wind | Conditional Strike | 10.3 -> **9.1** (-11.7%) | 38.5 -> **54.2** | 406.9 -> **502.3** | Class Wind undertuned (WR: 38.0%, factor: 1.048); Status 'Bleeding' beneficiaries undertuned (WR: 41.0%) |
| `ELW` | Wind | Debuff / Control | 35.3 -> **37.9** (+7.4%) | - | 35.3 -> **37.9** | Class Wind undertuned (WR: 38.0%, factor: 1.048); Individual spell undertuned (WR: 42.9%, Casts: 179, mult: 1.024) |
| `ELE` | Wind | Setup - Weather | 32.4 -> **35.9** (+10.8%) | - | 32.4 -> **35.9** | Class Wind undertuned (WR: 38.0%, factor: 1.048); Individual spell undertuned (WR: 35.0%, Casts: 6665, mult: 1.056) |
| `ELL` | Wind | Buff / Sustain | 51.4 -> **49.8** (-3.1%) | - | 51.4 -> **49.8** | Class Wind undertuned (WR: 38.0%, factor: 1.048); Individual spell overtuned (WR: 69.8%, Casts: 240, mult: 0.924) |
| `ELD` | Wind | Conditional Strike | 7.3 -> **6.5** (-11.0%) | 33.8 -> **49.7** | 254.0 -> **329.6** | Class Wind undertuned (WR: 38.0%, factor: 1.048); Weather 'Raining' beneficiaries undertuned (WR: 30.2%) |
| `LEF` | Wind | Conditional Strike | 6.5 -> **5.7** (-12.3%) | 30.4 -> **41.4** | 204.1 -> **241.7** | Class Wind undertuned (WR: 38.0%, factor: 1.048); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 2736). Increasing spread: b -17.6%, n +36.3% |
| `LEW` | Wind | Debuff / Control | 41.9 -> **39.1** (-6.7%) | - | 41.9 -> **39.1** | Class Wind undertuned (WR: 38.0%, factor: 1.048); Individual spell overtuned (WR: 77.6%, Casts: 4842, mult: 0.891) |
| `LEE` | Wind | Setup - Weather | 27.1 -> **32.8** (+21.0%) | - | 27.1 -> **32.8** | Class Wind undertuned (WR: 38.0%, factor: 1.048); Individual spell undertuned (WR: 12.0%, Casts: 5839, mult: 1.155) |
| `LEL` | Wind | Buff / Sustain | 59.2 -> **66.6** (+12.5%) | - | 59.2 -> **66.6** | Class Wind undertuned (WR: 38.0%, factor: 1.048); Individual spell undertuned (WR: 30.6%, Casts: 1086, mult: 1.074) |
| `EDF` | Poison | Conditional Strike | 5.5 -> **4.1** (-25.5%) | 29.6 -> **40.6** | 168.3 -> **170.6** | Class Poison overtuned (WR: 54.2%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 787). Increasing spread: b -18.0%, n +37.0% |
| `EDW` | Poison | Debuff / Control | 13.5 -> **12.2** (-9.6%) | - | 13.5 -> **12.2** | Class Poison overtuned (WR: 54.2%, factor: 0.983); Individual spell overtuned (WR: 70.2%, Casts: 323, mult: 0.923) |
| `EDE` | Poison | Setup - Location | 29.4 -> **36.8** (+25.2%) | - | 29.4 -> **36.8** | Class Poison overtuned (WR: 54.2%, factor: 0.983); Location 'Swamp' appliers undertuned (WR: 15.9%, casts: 3520) |
| `EDL` | Poison | Debuff / Control | 4.5 -> **3.7** (-17.8%) | - | 4.5 -> **3.7** | Class Poison overtuned (WR: 54.2%, factor: 0.983); Individual spell overtuned (WR: 90.3%, Casts: 2863, mult: 0.834) |
| `EDD` | Poison | Ultimate | 19.0 -> **20.2** (+6.3%) | 20.6 -> **20.1** | 410.4 -> **426.2** | Class Poison overtuned (WR: 54.2%, factor: 0.983); Status 'Bleeding' beneficiaries undertuned (WR: 41.0%) |
| `DEF` | Poison | Conditional Strike | 18.1 -> **18.3** (+1.1%) | 3.8 -> **4.4** | 86.9 -> **98.8** | Class Poison overtuned (WR: 54.2%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 25.6% vs 30% floor, Casts: 242). Increasing spread: b -7.8%, n +15.7% |
| `DEW` | Poison | Debuff / Control | 13.2 -> **11.4** (-13.6%) | - | 13.2 -> **11.4** | Class Poison overtuned (WR: 54.2%, factor: 0.983); Individual spell overtuned (WR: 80.8%, Casts: 3533, mult: 0.877) |
| `DEL` | Poison | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 37.1 -> **52.5** | 22.9 -> **26.8** | Class Poison overtuned (WR: 54.2%, factor: 0.983); Status 'Bleeding' beneficiaries undertuned (WR: 41.0%) |
| `LDF` | Cosmic | Debuff / Control | 35.5 -> **33.9** (-4.5%) | - | 35.5 -> **33.9** | Individual spell overtuned (WR: 62.1%, Casts: 3060, mult: 0.956) |
| `LDW` | Cosmic | Debuff / Control | 29.1 -> **25.9** (-11.0%) | - | 29.1 -> **25.9** | Status 'Stunned' appliers overtuned on own (WR: 56.5%); Individual spell overtuned (WR: 73.0%, Casts: 6095, mult: 0.911) |
| `LDE` | Cosmic | Setup - Location | 21.3 -> **24.0** (+12.7%) | - | 21.3 -> **24.0** | Individual spell undertuned (WR: 17.9%, Casts: 3811, mult: 1.129) |
| `LDL` | Cosmic | Conditional Strike | 5.8 -> **5.2** (-10.3%) | 30.7 -> **42.1** | 183.9 -> **224.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6778). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 27.0%, Casts: 6778, mult: 1.089) |
| `LDD` | Cosmic | Ultimate | 11.6 -> **13.3** (+14.7%) | 29.0 -> **27.3** | 348.0 -> **376.4** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2269, WR: 33.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 33.9%, Casts: 2269, mult: 1.060) |
| `DLF` | Cosmic | Conditional Strike | 6.7 -> **6.1** (-9.0%) | 30.7 -> **38.5** | 212.4 -> **240.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.1% vs 30% floor, Casts: 1015). Increasing spread: b -12.4%, n +25.3%; Individual spell undertuned (WR: 39.3%, Casts: 1015, mult: 1.038) |
| `DLW` | Cosmic | Direct Damage | 41.6 -> **39.2** (-5.8%) | - | 41.6 -> **39.2** | Individual spell overtuned (WR: 65.7%, Casts: 6259, mult: 0.941) |
| `DLE` | Cosmic | Direct Damage | 58.7 -> **61.3** (+4.4%) | - | 58.7 -> **61.3** | Individual spell undertuned (WR: 37.9%, Casts: 484, mult: 1.044) |
| `DLL` | Cosmic | Conditional Strike | 9.9 -> **8.5** (-14.1%) | 28.4 -> **38.9** | 291.1 -> **339.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 102). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 36.8%, Casts: 102, mult: 1.048) |
