# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T15:47:26Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 122.7s  
**Total Spells Tuned:** 117 / 125  

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
| **Dark** | 19,122 | 59.6% | 59.6% | 9.6 | Overtuned ⚠️ |
| **Fire** | 15,074 | 58.1% | 58.1% | 10.7 | Overtuned ⚠️ |
| **Poison** | 23,789 | 57.0% | 57.0% | 6.5 | Overtuned ⚠️ |
| **Light** | 13,673 | 54.7% | 54.7% | 3.8 | Overtuned ⚠️ |
| **Ghostfire** | 31,491 | 54.5% | 54.5% | 5.1 | Overtuned ⚠️ |
| **Ice** | 36,822 | 54.3% | 54.3% | 11.9 | Overtuned ⚠️ |
| **Earth** | 20,179 | 53.8% | 53.8% | 13.5 | Overtuned ⚠️ |
| **Cosmic** | 35,645 | 52.4% | 52.4% | 14.6 | Balanced ✅ |
| **Blood** | 27,781 | 51.8% | 51.8% | 5.5 | Balanced ✅ |
| **Lightning** | 16,743 | 46.7% | 46.7% | 5.2 | Balanced ✅ |
| **Beasts** | 26,496 | 45.4% | 45.4% | 3.9 | Undertuned ⚠️ |
| **Fey** | 22,266 | 42.0% | 42.0% | 6.0 | Undertuned ⚠️ |
| **Plants** | 20,572 | 41.4% | 41.4% | 3.0 | Undertuned ⚠️ |
| **Wind** | 18,806 | 40.0% | 40.0% | 6.0 | Undertuned ⚠️ |
| **Water** | 12,538 | 24.5% | 24.5% | 2.5 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 18,087 (70.2%) | 8,514 (33.1%) | 3.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 479 (11.8%) | 8,825 (28.7%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,594 (64.4%) | 10,582 (32.5%) | 2.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 16,073 (76.5%) | 8,925 (39.8%) | 0.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,711 (46.8%) | 3,755 (43.4%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,100 (59.2%) | 9,325 (37.5%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 4,440 (6.7%) | 2,104 (31.8%) | 1.7% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 37.6 -> **33.8** (-10.1%) | - | 37.6 -> **33.8** | Class Fire overtuned (WR: 58.1%, factor: 0.968); Individual spell overtuned (WR: 68.4%, Casts: 2893, mult: 0.930) |
| `FFW` | Fire | Debuff / Control | 21.6 -> **20.3** (-6.0%) | - | 21.6 -> **20.3** | Class Fire overtuned (WR: 58.1%, factor: 0.968); Status 'Burning' appliers overtuned on own (WR: 64.4%) |
| `FFE` | Fire | Debuff / Control | 23.4 -> **20.4** (-12.8%) | - | 23.4 -> **20.4** | Class Fire overtuned (WR: 58.1%, factor: 0.968); Individual spell overtuned (WR: 75.3%, Casts: 4028, mult: 0.901) |
| `FFL` | Fire | Debuff / Control | 1.9 -> **1.5** (-21.1%) | - | 1.9 -> **1.5** | Class Fire overtuned (WR: 58.1%, factor: 0.968); Status 'Burning' appliers overtuned on own (WR: 64.4%) |
| `FFD` | Fire | Conditional Strike | 4.9 -> **4.3** (-12.2%) | 40.0 -> **58.2** | 200.9 -> **254.6** | Class Fire overtuned (WR: 58.1%, factor: 0.968); Status 'Burning' beneficiaries undertuned (WR: 32.5%) |
| `WWF` | Water | Conditional Strike | 4.7 -> **4.5** (-4.3%) | 31.5 -> **45.0** | 152.8 -> **207.0** | Class Water undertuned (WR: 24.5%, factor: 1.102); Status 'Burning' beneficiaries undertuned (WR: 32.5%) |
| `WWE` | Water | Setup - Weather | 48.2 -> **67.5** (+40.0%) | - | 48.2 -> **67.5** | Class Water undertuned (WR: 24.5%, factor: 1.102); Weather 'Raining' appliers undertuned (WR: 6.7%, casts: 4440) |
| `WWL` | Water | Buff / Sustain | 42.7 -> **45.8** (+7.3%) | - | 42.7 -> **45.8** | Class Water undertuned (WR: 24.5%, factor: 1.102); Individual spell overtuned (WR: 57.5%, Casts: 1109, mult: 0.974) |
| `WWD` | Water | Buff / Sustain | 34.6 -> **38.1** (+10.1%) | - | 34.6 -> **38.1** | Class Water undertuned (WR: 24.5%, factor: 1.102) |
| `EEF` | Earth | Conditional Strike | 5.6 -> **5.0** (-10.7%) | 44.1 -> **63.2** | 252.6 -> **321.0** | Class Earth overtuned (WR: 53.8%, factor: 0.985); Status 'Frosty' beneficiaries undertuned (WR: 33.1%) |
| `EEW` | Earth | Buff / Sustain | 46.6 -> **44.1** (-5.4%) | - | 46.6 -> **44.1** | Class Earth overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 60.7%, Casts: 1148, mult: 0.962) |
| `EED` | Earth | Direct Damage | 3.9 -> **3.5** (-10.3%) | - | 3.9 -> **3.5** | Class Earth overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 73.6%, Casts: 7142, mult: 0.908) |
| `LLF` | Light | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 44.0 -> **59.3** | 18.0 -> **18.1** | Class Light overtuned (WR: 54.7%, factor: 0.981); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.7% vs 30% floor, Casts: 4380). Increasing spread: b -16.9%, n +34.7% |
| `LLW` | Light | Debuff / Control | 21.6 -> **21.5** (-0.5%) | - | 21.6 -> **21.5** | Class Light overtuned (WR: 54.7%, factor: 0.981); Individual spell undertuned (WR: 46.2%, Casts: 3365, mult: 1.012) |
| `LLE` | Light | Setup - Weather | 86.0 -> **109.4** (+27.2%) | - | 86.0 -> **109.4** | Class Light overtuned (WR: 54.7%, factor: 0.981); Weather 'Sunny' appliers undertuned (WR: 11.8%, casts: 479) |
| `LLL` | Light | Buff / Sustain | 16.4 -> **14.0** (-14.6%) | - | 16.4 -> **14.0** | Class Light overtuned (WR: 54.7%, factor: 0.981); Individual spell overtuned (WR: 82.7%, Casts: 2353, mult: 0.869) |
| `LLD` | Light | Ultimate | 13.2 -> **14.8** (+12.1%) | 27.2 -> **27.7** | 372.2 -> **424.8** | Class Light overtuned (WR: 54.7%, factor: 0.981); Weather 'Sunny' beneficiaries undertuned (WR: 28.7%) |
| `DDF` | Dark | Conditional Strike | 3.6 -> **2.8** (-22.2%) | 49.6 -> **68.0** | 182.2 -> **193.2** | Class Dark overtuned (WR: 59.6%, factor: 0.962); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1972). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 39.4 -> **35.8** (-9.1%) | - | 39.4 -> **35.8** | Class Dark overtuned (WR: 59.6%, factor: 0.962); Individual spell overtuned (WR: 64.6%, Casts: 5855, mult: 0.946) |
| `DDE` | Dark | Setup - Weather | 65.1 -> **77.1** (+18.4%) | - | 65.1 -> **77.1** | Class Dark overtuned (WR: 59.6%, factor: 0.962); Weather 'Darkness' appliers undertuned (WR: 20.6%, casts: 1683) |
| `DDL` | Dark | Debuff / Control | 19.1 -> **18.1** (-5.2%) | - | 19.1 -> **18.1** | Class Dark overtuned (WR: 59.6%, factor: 0.962); Individual spell overtuned (WR: 54.7%, Casts: 6778, mult: 0.985) |
| `DDD` | Dark | Debuff / Control | 12.9 -> **10.6** (-17.8%) | - | 12.9 -> **10.6** | Class Dark overtuned (WR: 59.6%, factor: 0.962); Individual spell overtuned (WR: 86.3%, Casts: 2834, mult: 0.852) |
| `FWF` | Ghostfire | Debuff / Control | 9.4 -> **7.8** (-17.0%) | - | 9.4 -> **7.8** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Status 'Burning' appliers overtuned on own (WR: 64.4%) |
| `FWW` | Ghostfire | Debuff / Control | 10.9 -> **11.2** (+2.8%) | - | 10.9 -> **11.2** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Status 'Cursed' appliers overtuned on own (WR: 54.3%) |
| `FWE` | Ghostfire | Setup - Location | 61.8 -> **66.9** (+8.3%) | - | 61.8 -> **66.9** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Location 'Graveyard' appliers undertuned (WR: 36.1%, casts: 277) |
| `FWL` | Ghostfire | Debuff / Control | 29.2 -> **27.9** (-4.5%) | - | 29.2 -> **27.9** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Status 'Cursed' appliers overtuned on own (WR: 54.3%) |
| `FWD` | Ghostfire | Ultimate | 13.6 -> **14.7** (+8.1%) | 20.8 -> **20.5** | 296.5 -> **316.1** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Status 'Cursed' beneficiaries undertuned (WR: 43.6%) |
| `WFF` | Ghostfire | Conditional Strike | 3.8 -> **3.0** (-21.1%) | 57.5 -> **82.0** | 222.3 -> **249.0** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Status 'Bleeding' beneficiaries undertuned (WR: 39.8%) |
| `WFW` | Ghostfire | Debuff / Control | 15.9 -> **13.6** (-14.5%) | - | 15.9 -> **13.6** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 81.8%, Casts: 2654, mult: 0.872) |
| `WFE` | Ghostfire | Debuff / Control | 5.9 -> **4.4** (-25.4%) | - | 5.9 -> **4.4** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Status 'Bleeding' appliers overtuned on own (WR: 76.5%) |
| `WFL` | Ghostfire | Buff / Sustain | 40.0 -> **45.5** (+13.8%) | - | 40.0 -> **45.5** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Individual spell undertuned (WR: 11.2%, Casts: 4441, mult: 1.159) |
| `WFD` | Ghostfire | Conditional Strike | 3.6 -> **2.9** (-19.4%) | 43.0 -> **58.9** | 158.4 -> **173.7** | Class Ghostfire overtuned (WR: 54.5%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 4212). Increasing spread: b -18.0%, n +36.9% |
| `FEF` | Beasts | Debuff / Control | 18.8 -> **17.3** (-8.0%) | - | 18.8 -> **17.3** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Individual spell overtuned (WR: 75.0%, Casts: 2647, mult: 0.902) |
| `FEW` | Beasts | Conditional Strike | 4.5 -> **4.1** (-8.9%) | 57.0 -> **82.0** | 261.0 -> **340.3** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Status 'Entangled' beneficiaries undertuned (WR: 37.5%) |
| `FEE` | Beasts | Buff / Sustain | 30.3 -> **32.2** (+6.3%) | - | 30.3 -> **32.2** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Individual spell undertuned (WR: 38.0%, Casts: 796, mult: 1.044) |
| `FEL` | Beasts | Buff / Sustain | 64.4 -> **68.3** (+6.1%) | - | 64.4 -> **68.3** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Individual spell undertuned (WR: 38.5%, Casts: 2981, mult: 1.042) |
| `FED` | Beasts | Conditional Strike | 4.4 -> **4.2** (-4.5%) | 3.5 -> **3.5** | 19.8 -> **18.9** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.7% vs 30% floor, Casts: 6523). Increasing spread: b -13.7%, n +28.1% |
| `EFF` | Beasts | Debuff / Control | 7.9 -> **6.6** (-16.5%) | 46.4 -> **63.5** | 374.5 -> **425.7** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 2925). Increasing spread: b -17.9%, n +36.9% |
| `EFW` | Beasts | Buff / Sustain | 30.3 -> **33.7** (+11.2%) | - | 30.3 -> **33.7** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Individual spell undertuned (WR: 26.5%, Casts: 399, mult: 1.091) |
| `EFE` | Beasts | Buff / Sustain | 29.7 -> **30.7** (+3.4%) | - | 29.7 -> **30.7** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Individual spell undertuned (WR: 45.9%, Casts: 1903, mult: 1.014) |
| `EFL` | Beasts | Buff / Sustain | 6.5 -> **5.4** (-16.9%) | - | 6.5 -> **5.4** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Individual spell overtuned (WR: 95.4%, Casts: 2809, mult: 0.820) |
| `EFD` | Beasts | Ultimate | 15.0 -> **17.1** (+14.0%) | 42.2 -> **43.4** | 648.0 -> **759.2** | Class Beasts undertuned (WR: 45.4%, factor: 1.018); Status 'Entangled' beneficiaries undertuned (WR: 37.5%) |
| `FLF` | Lightning | Conditional Strike | 4.1 -> **3.4** (-17.1%) | 55.6 -> **78.2** | 232.1 -> **269.3** | Status 'Stunned' beneficiaries undertuned (WR: 43.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 896). Increasing spread: b -18.0%, n +37.0% |
| `FLW` | Lightning | Debuff / Control | 24.4 -> **24.7** (+1.2%) | - | 24.4 -> **24.7** | Individual spell undertuned (WR: 45.7%, Casts: 1567, mult: 1.014) |
| `FLE` | Lightning | Setup - Weather | 27.8 -> **28.7** (+3.2%) | - | 27.8 -> **28.7** | Weather 'Storming' appliers undertuned (WR: 45.4%, casts: 83); Individual spell undertuned (WR: 45.3%, Casts: 83, mult: 1.016) |
| `FLL` | Lightning | Buff / Sustain | 39.6 -> **40.3** (+1.8%) | - | 39.6 -> **40.3** | Individual spell undertuned (WR: 44.8%, Casts: 744, mult: 1.017) |
| `FLD` | Lightning | Ultimate | 22.6 -> **25.0** (+10.6%) | 17.1 -> **16.9** | 409.1 -> **447.5** | Status 'Stunned' beneficiaries undertuned (WR: 43.4%); Weather 'Storming' beneficiaries undertuned (WR: 43.2%) |
| `LFF` | Lightning | Conditional Strike | 4.9 -> **4.5** (-8.2%) | 47.1 -> **64.5** | 235.7 -> **294.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3496). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 21.1%, Casts: 3496, mult: 1.115) |
| `LFW` | Lightning | Buff / Sustain | 24.7 -> **23.8** (-3.6%) | - | 24.7 -> **23.8** | Individual spell overtuned (WR: 60.1%, Casts: 3550, mult: 0.964) |
| `LFE` | Lightning | Debuff / Control | 22.8 -> **20.6** (-9.6%) | - | 22.8 -> **20.6** | Individual spell overtuned (WR: 74.4%, Casts: 1571, mult: 0.905) |
| `LFL` | Lightning | Debuff / Control | 7.2 -> **5.9** (-18.1%) | 35.4 -> **49.4** | 262.1 -> **297.4** | Weather 'Darkness' beneficiaries undertuned (WR: 44.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 1701). Increasing spread: b -17.7%, n +36.5% |
| `LFD` | Lightning | Conditional Strike | 5.0 -> **3.9** (-22.0%) | 57.7 -> **79.0** | 293.5 -> **312.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 276). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 63.9%, Casts: 276, mult: 0.949) |
| `FDF` | Blood | Conditional Strike | 3.2 -> **2.7** (-15.6%) | 49.6 -> **68.0** | 161.9 -> **186.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3250). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 38.2%, Casts: 3250, mult: 1.043) |
| `FDW` | Blood | Direct Damage | 70.4 -> **71.6** (+1.7%) | - | 70.4 -> **71.6** | Individual spell undertuned (WR: 44.9%, Casts: 1337, mult: 1.017) |
| `FDE` | Blood | Setup - Weather | 40.5 -> **45.5** (+12.3%) | - | 40.5 -> **45.5** | Individual spell undertuned (WR: 19.3%, Casts: 1506, mult: 1.123) |
| `FDL` | Blood | Debuff / Control | 5.6 -> **4.4** (-21.4%) | - | 5.6 -> **4.4** | Status 'Bleeding' appliers overtuned on own (WR: 76.5%); Individual spell overtuned (WR: 84.9%, Casts: 3714, mult: 0.859) |
| `FDD` | Blood | Ultimate | 9.7 -> **10.8** (+11.3%) | 26.8 -> **25.8** | 269.7 -> **289.4** | Weather 'Darkness' beneficiaries undertuned (WR: 44.3%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 9957, WR: 41.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 4.8 -> **4.1** (-14.6%) | 51.0 -> **71.4** | 249.6 -> **296.8** | Status 'Bleeding' beneficiaries undertuned (WR: 39.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 2097). Increasing spread: b -16.8%, n +34.5% |
| `DFW` | Blood | Debuff / Control | 4.5 -> **3.4** (-24.4%) | - | 4.5 -> **3.4** | Status 'Bleeding' appliers overtuned on own (WR: 76.5%); Individual spell overtuned (WR: 90.0%, Casts: 2771, mult: 0.836) |
| `DFE` | Blood | Buff / Sustain | 87.1 -> **99.8** (+14.6%) | - | 87.1 -> **99.8** | Individual spell undertuned (WR: 14.0%, Casts: 951, mult: 1.146) |
| `DFL` | Blood | Buff / Sustain | 18.3 -> **17.0** (-7.1%) | - | 18.3 -> **17.0** | Individual spell overtuned (WR: 68.9%, Casts: 1783, mult: 0.928) |
| `DFD` | Blood | Conditional Strike | 64.4 -> **70.4** (+9.3%) | 0.1 -> **0.1** | 70.8 -> **77.4** | Condition triggers excessively (N=1 conditions, Trigger Rate: 74.0% vs 55% ceiling, WR: 55.5%). Compressing spread: b +11.4%, n -16.9%; Individual spell overtuned (WR: 55.5%, Casts: 415, mult: 0.981) |
| `WEF` | Plants | Conditional Strike | 4.9 -> **4.2** (-14.3%) | 55.2 -> **77.1** | 275.4 -> **328.0** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Location 'Jungle' beneficiaries undertuned (WR: 39.8%) |
| `WEW` | Plants | Debuff / Control | 33.7 -> **39.1** (+16.0%) | - | 33.7 -> **39.1** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Individual spell undertuned (WR: 19.4%, Casts: 1222, mult: 1.122) |
| `WEE` | Plants | Setup - Location | 51.0 -> **63.3** (+24.1%) | - | 51.0 -> **63.3** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Location 'Jungle' appliers undertuned (WR: 24.3%, casts: 572) |
| `WEL` | Plants | Debuff / Control | 33.9 -> **32.8** (-3.2%) | - | 33.9 -> **32.8** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Status 'Entangled' appliers overtuned on own (WR: 59.2%) |
| `WED` | Plants | Conditional Strike | 12.8 -> **14.9** (+16.4%) | 11.1 -> **10.4** | 154.9 -> **169.9** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4628, WR: 38.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 4.5 -> **4.2** (-6.7%) | 38.1 -> **56.7** | 176.0 -> **242.3** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Weather 'Sunny' beneficiaries undertuned (WR: 28.7%) |
| `EWW` | Plants | Debuff / Control | 6.6 -> **5.6** (-15.2%) | - | 6.6 -> **5.6** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Individual spell overtuned (WR: 92.0%, Casts: 2125, mult: 0.827) |
| `EWL` | Plants | Debuff / Control | 42.5 -> **40.6** (-4.5%) | - | 42.5 -> **40.6** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Individual spell overtuned (WR: 69.8%, Casts: 190, mult: 0.924) |
| `EWD` | Plants | Conditional Strike | 1.7 -> **1.4** (-17.6%) | 55.8 -> **80.3** | 96.6 -> **113.8** | Class Plants undertuned (WR: 41.4%, factor: 1.034); Status 'Bleeding' appliers overtuned on own (WR: 76.5%) |
| `WLF` | Fey | Conditional Strike | 5.4 -> **5.0** (-7.4%) | 39.6 -> **52.9** | 219.2 -> **269.5** | Class Fey undertuned (WR: 42.0%, factor: 1.032); Status 'Cursed' beneficiaries undertuned (WR: 43.6%) |
| `WLW` | Fey | Debuff / Control | 30.5 -> **29.7** (-2.6%) | - | 30.5 -> **29.7** | Class Fey undertuned (WR: 42.0%, factor: 1.032); Status 'Cursed' appliers overtuned on own (WR: 54.3%) |
| `WLE` | Fey | Setup - Location | 122.0 -> **104.0** (-14.8%) | - | 122.0 -> **104.0** | Class Fey undertuned (WR: 42.0%, factor: 1.032); Location 'Enchanted Forest' appliers overtuned on own (WR: 74.5%) |
| `WLL` | Fey | Direct Damage | 56.3 -> **63.2** (+12.3%) | - | 56.3 -> **63.2** | Class Fey undertuned (WR: 42.0%, factor: 1.032); Individual spell undertuned (WR: 27.4%, Casts: 316, mult: 1.087) |
| `WLD` | Fey | Ultimate | 20.3 -> **17.2** (-15.3%) | 19.8 -> **27.7** | 422.2 -> **493.6** | Class Fey undertuned (WR: 42.0%, factor: 1.032); Weather 'Darkness' beneficiaries undertuned (WR: 44.3%) |
| `LWF` | Fey | Debuff / Control | 9.6 -> **8.0** (-16.7%) | 39.3 -> **53.8** | 386.9 -> **438.4** | Class Fey undertuned (WR: 42.0%, factor: 1.032); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1471). Increasing spread: b -17.9%, n +36.9% |
| `LWW` | Fey | Debuff / Control | 71.7 -> **74.0** (+3.2%) | - | 71.7 -> **74.0** | Class Fey undertuned (WR: 42.0%, factor: 1.032) |
| `LWL` | Fey | Debuff / Control | 56.7 -> **67.7** (+19.4%) | - | 56.7 -> **67.7** | Class Fey undertuned (WR: 42.0%, factor: 1.032); Individual spell undertuned (WR: 11.6%, Casts: 2859, mult: 1.157) |
| `LWD` | Fey | Conditional Strike | 6.6 -> **6.0** (-9.1%) | 49.6 -> **68.0** | 334.0 -> **414.0** | Class Fey undertuned (WR: 42.0%, factor: 1.032); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6087). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 6.0 -> **5.2** (-13.3%) | 52.9 -> **77.0** | 323.4 -> **405.6** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Weather 'Raining' beneficiaries undertuned (WR: 31.8%) |
| `WDW` | Ice | Buff / Sustain | 27.5 -> **26.6** (-3.3%) | - | 27.5 -> **26.6** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 70.2%) |
| `WDE` | Ice | Setup - Weather | 41.3 -> **45.3** (+9.7%) | - | 41.3 -> **45.3** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Individual spell undertuned (WR: 20.7%, Casts: 4304, mult: 1.117) |
| `WDL` | Ice | Debuff / Control | 40.5 -> **36.1** (-10.9%) | - | 40.5 -> **36.1** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 70.2%) |
| `WDD` | Ice | Ultimate | 19.3 -> **21.0** (+8.8%) | 20.3 -> **20.1** | 411.1 -> **443.1** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Weather 'Blizzard' beneficiaries undertuned (WR: 43.2%) |
| `DWF` | Ice | Debuff / Control | 39.5 -> **32.2** (-18.5%) | - | 39.5 -> **32.2** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 70.2%) |
| `DWW` | Ice | Debuff / Control | 33.9 -> **31.6** (-6.8%) | - | 33.9 -> **31.6** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 64.1%, Casts: 6098, mult: 0.948) |
| `DWE` | Ice | Setup - Location | 50.0 -> **61.1** (+22.2%) | - | 50.0 -> **61.1** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Location 'Tundra' appliers undertuned (WR: 19.4%, casts: 3202) |
| `DWL` | Ice | Debuff / Control | 40.5 -> **34.2** (-15.6%) | - | 40.5 -> **34.2** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 70.2%) |
| `DWD` | Ice | Conditional Strike | 8.7 -> **7.4** (-14.9%) | 39.4 -> **56.7** | 351.5 -> **427.0** | Class Ice overtuned (WR: 54.3%, factor: 0.983); Status 'Frosty' beneficiaries undertuned (WR: 33.1%) |
| `ELF` | Wind | Conditional Strike | 9.1 -> **8.1** (-11.0%) | 54.2 -> **77.2** | 502.3 -> **633.4** | Class Wind undertuned (WR: 40.0%, factor: 1.040); Status 'Bleeding' beneficiaries undertuned (WR: 39.8%) |
| `ELW` | Wind | Debuff / Control | 37.9 -> **36.1** (-4.7%) | - | 37.9 -> **36.1** | Class Wind undertuned (WR: 40.0%, factor: 1.040); Individual spell overtuned (WR: 71.7%, Casts: 2709, mult: 0.916) |
| `ELE` | Wind | Setup - Weather | 35.9 -> **38.4** (+7.0%) | - | 35.9 -> **38.4** | Class Wind undertuned (WR: 40.0%, factor: 1.040); Individual spell undertuned (WR: 42.0%, Casts: 1802, mult: 1.028) |
| `ELL` | Wind | Buff / Sustain | 49.8 -> **56.4** (+13.3%) | - | 49.8 -> **56.4** | Class Wind undertuned (WR: 40.0%, factor: 1.040); Individual spell undertuned (WR: 27.1%, Casts: 541, mult: 1.089) |
| `ELD` | Wind | Conditional Strike | 6.5 -> **6.0** (-7.7%) | 49.7 -> **70.0** | 329.6 -> **426.0** | Class Wind undertuned (WR: 40.0%, factor: 1.040); Weather 'Raining' beneficiaries undertuned (WR: 31.8%) |
| `LEF` | Wind | Conditional Strike | 5.7 -> **5.2** (-8.8%) | 41.4 -> **60.5** | 241.7 -> **319.8** | Class Wind undertuned (WR: 40.0%, factor: 1.040); Status 'Burning' beneficiaries undertuned (WR: 32.5%) |
| `LEW` | Wind | Debuff / Control | 39.1 -> **39.9** (+2.0%) | - | 39.1 -> **39.9** | Class Wind undertuned (WR: 40.0%, factor: 1.040); Individual spell overtuned (WR: 55.4%, Casts: 1889, mult: 0.982) |
| `LEE` | Wind | Setup - Weather | 32.8 -> **36.3** (+10.7%) | - | 32.8 -> **36.3** | Class Wind undertuned (WR: 40.0%, factor: 1.040); Individual spell undertuned (WR: 33.0%, Casts: 1206, mult: 1.064) |
| `LEL` | Wind | Buff / Sustain | 66.6 -> **72.5** (+8.9%) | - | 66.6 -> **72.5** | Class Wind undertuned (WR: 40.0%, factor: 1.040); Individual spell undertuned (WR: 37.3%, Casts: 1233, mult: 1.047) |
| `EDF` | Poison | Conditional Strike | 4.1 -> **3.3** (-19.5%) | 40.6 -> **54.6** | 170.6 -> **183.5** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 760). Increasing spread: b -16.8%, n +34.5% |
| `EDW` | Poison | Debuff / Control | 12.2 -> **11.1** (-9.0%) | - | 12.2 -> **11.1** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Individual spell overtuned (WR: 67.8%, Casts: 635, mult: 0.932) |
| `EDE` | Poison | Setup - Location | 36.8 -> **45.7** (+24.2%) | - | 36.8 -> **45.7** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Location 'Swamp' appliers undertuned (WR: 15.0%, casts: 3360) |
| `EDL` | Poison | Debuff / Control | 3.7 -> **2.9** (-21.6%) | - | 3.7 -> **2.9** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Individual spell overtuned (WR: 96.0%, Casts: 2646, mult: 0.820) |
| `EDD` | Poison | Ultimate | 20.2 -> **22.0** (+8.9%) | 20.1 -> **20.5** | 426.2 -> **473.0** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Status 'Bleeding' beneficiaries undertuned (WR: 39.8%) |
| `DEF` | Poison | Conditional Strike | 18.3 -> **16.9** (-7.7%) | 4.4 -> **4.4** | 98.8 -> **91.3** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 31.5% within [30%-55%] target window, WR: 62.8%). |
| `DEW` | Poison | Debuff / Control | 11.4 -> **9.9** (-13.2%) | - | 11.4 -> **9.9** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Individual spell overtuned (WR: 76.0%, Casts: 5152, mult: 0.898) |
| `DEL` | Poison | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 52.5 -> **74.9** | 26.8 -> **30.4** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Status 'Bleeding' beneficiaries undertuned (WR: 39.8%) |
| `DED` | Poison | Debuff / Control | 22.6 -> **21.3** (-5.8%) | - | 22.6 -> **21.3** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Individual spell overtuned (WR: 58.7%, Casts: 6799, mult: 0.969) |
| `LDF` | Cosmic | Debuff / Control | 33.9 -> **33.1** (-2.4%) | - | 33.9 -> **33.1** | Individual spell overtuned (WR: 56.6%, Casts: 5022, mult: 0.977) |
| `LDW` | Cosmic | Debuff / Control | 25.9 -> **23.8** (-8.1%) | - | 25.9 -> **23.8** | Individual spell overtuned (WR: 70.9%, Casts: 3456, mult: 0.920) |
| `LDE` | Cosmic | Setup - Location | 24.0 -> **24.5** (+2.1%) | - | 24.0 -> **24.5** | Individual spell undertuned (WR: 43.9%, Casts: 307, mult: 1.021) |
| `LDL` | Cosmic | Conditional Strike | 5.2 -> **4.8** (-7.7%) | 42.1 -> **57.7** | 224.1 -> **281.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6919). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 16.8%, Casts: 6919, mult: 1.134) |
| `LDD` | Cosmic | Ultimate | 13.3 -> **15.1** (+13.5%) | 27.3 -> **25.7** | 376.4 -> **403.2** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 4192, WR: 35.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 35.3%, Casts: 4192, mult: 1.055) |
| `DLF` | Cosmic | Conditional Strike | 6.1 -> **5.4** (-11.5%) | 38.5 -> **51.8** | 240.9 -> **285.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.8% vs 30% floor, Casts: 1302). Increasing spread: b -16.9%, n +34.6%; Individual spell undertuned (WR: 30.8%, Casts: 1302, mult: 1.073) |
| `DLW` | Cosmic | Direct Damage | 39.2 -> **35.9** (-8.4%) | - | 39.2 -> **35.9** | Individual spell overtuned (WR: 72.0%, Casts: 9447, mult: 0.915) |
| `DLE` | Cosmic | Direct Damage | 61.3 -> **67.6** (+10.3%) | - | 61.3 -> **67.6** | Individual spell undertuned (WR: 23.8%, Casts: 707, mult: 1.103) |
| `DLL` | Cosmic | Conditional Strike | 8.5 -> **7.6** (-10.6%) | 38.9 -> **54.5** | 339.1 -> **421.8** | Weather 'Darkness' beneficiaries undertuned (WR: 44.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 55). Increasing spread: b -18.0%, n +37.0% |
