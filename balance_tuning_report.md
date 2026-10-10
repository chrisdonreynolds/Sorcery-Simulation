# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T18:16:20Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 61.0s  
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
| **Earth** | 12,376 | 79.2% | 79.3% | 27.3 | Overtuned ⚠️ |
| **Blood** | 27,856 | 62.7% | 62.7% | 10.7 | Overtuned ⚠️ |
| **Ice** | 31,962 | 56.0% | 56.0% | 3.5 | Overtuned ⚠️ |
| **Dark** | 12,574 | 52.8% | 52.8% | 3.8 | Balanced ✅ |
| **Poison** | 31,068 | 52.7% | 52.7% | 3.0 | Balanced ✅ |
| **Water** | 8,733 | 52.2% | 52.2% | 4.7 | Balanced ✅ |
| **Ghostfire** | 20,651 | 51.1% | 51.1% | 2.0 | Balanced ✅ |
| **Wind** | 22,496 | 49.1% | 49.1% | 2.1 | Balanced ✅ |
| **Beasts** | 24,714 | 48.7% | 48.7% | 2.2 | Balanced ✅ |
| **Cosmic** | 30,768 | 48.4% | 48.4% | 4.3 | Balanced ✅ |
| **Light** | 16,072 | 45.9% | 45.9% | 1.4 | Undertuned ⚠️ |
| **Fire** | 24,340 | 43.2% | 43.2% | 2.3 | Undertuned ⚠️ |
| **Lightning** | 32,659 | 42.8% | 42.8% | 1.5 | Undertuned ⚠️ |
| **Plants** | 27,120 | 41.7% | 41.7% | 2.1 | Undertuned ⚠️ |
| **Fey** | 24,017 | 40.7% | 40.7% | 5.3 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 12,478 (55.4%) | 3,586 (67.8%) | 4.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,405 (27.5%) | 11,959 (39.8%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,638 (71.0%) | 17,508 (30.9%) | 0.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,996 (86.3%) | 19,370 (30.2%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 16,978 (61.3%) | 6,770 (25.7%) | 0.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,765 (81.8%) | 3,527 (62.6%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 73 (65.3%) | 5,006 (60.1%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 15.8 -> **14.7** (-7.0%) | - | 15.8 -> **14.7** | Class Fire undertuned (WR: 43.2%, factor: 1.027); Individual spell overtuned (WR: 73.8%, Casts: 691, mult: 0.907) |
| `FFW` | Fire | Debuff / Control | 7.7 -> **7.2** (-6.5%) | - | 7.7 -> **7.2** | Class Fire undertuned (WR: 43.2%, factor: 1.027); Status 'Burning' appliers overtuned on own (WR: 71.0%) |
| `FFD` | Fire | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 2300.4 -> **3380.7** | 2531.5 -> **3381.7** | Class Fire undertuned (WR: 43.2%, factor: 1.027); Status 'Burning' beneficiaries undertuned (WR: 30.9%) |
| `WWF` | Water | Conditional Strike | 1.2 -> **1.1** (-8.3%) | 1425.2 -> **2065.3** | 1711.4 -> **2272.9** | Status 'Burning' beneficiaries undertuned (WR: 30.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.9% vs 30% floor, Casts: 316). Increasing spread: b -16.9%, n +34.6% |
| `WWE` | Water | Setup - Weather | 287.1 -> **255.5** (-11.0%) | - | 287.1 -> **255.5** | Weather 'Raining' appliers overtuned on own (WR: 65.3%); Individual spell overtuned (WR: 65.9%, Casts: 73, mult: 0.941) |
| `WWL` | Water | Buff / Sustain | 16.1 -> **15.2** (-5.6%) | - | 16.1 -> **15.2** | Individual spell overtuned (WR: 64.7%, Casts: 5324, mult: 0.945) |
| `WWD` | Water | Buff / Sustain | 28.9 -> **29.5** (+2.1%) | - | 28.9 -> **29.5** | Individual spell undertuned (WR: 33.3%, Casts: 6, mult: 1.022) |
| `EEF` | Earth | Conditional Strike | 1.5 -> **1.0** (-33.3%) | 2289.3 -> **2832.9** | 3435.5 -> **2833.9** | Class Earth overtuned (WR: 79.2%, factor: 0.883); Status 'Frosty' beneficiaries overtuned (WR: 67.8%) |
| `EEW` | Earth | Buff / Sustain | 43.3 -> **35.7** (-17.6%) | - | 43.3 -> **35.7** | Class Earth overtuned (WR: 79.2%, factor: 0.883); Individual spell overtuned (WR: 67.6%, Casts: 834, mult: 0.933) |
| `EEE` | Earth | Conditional Strike | 9.9 -> **9.5** (-4.0%) | 1.5 -> **1.5** | 24.8 -> **23.8** | Class Earth overtuned (WR: 79.2%, factor: 0.883); Condition triggers excessively (N=1 conditions, Trigger Rate: 94.6% vs 55% ceiling, WR: 89.7%). Compressing spread: b +29.7%, n -37.9% |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 1215.2 -> **1645.1** | 121.6 -> **164.6** | Class Light undertuned (WR: 45.9%, factor: 1.017); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 3584). Increasing spread: b -17.2%, n +35.4% |
| `LLW` | Light | Debuff / Control | 13.2 -> **11.8** (-10.6%) | - | 13.2 -> **11.8** | Class Light undertuned (WR: 45.9%, factor: 1.017); Individual spell overtuned (WR: 80.5%, Casts: 281, mult: 0.878) |
| `LLE` | Light | Setup - Weather | 609.8 -> **726.9** (+19.2%) | - | 609.8 -> **726.9** | Class Light undertuned (WR: 45.9%, factor: 1.017); Weather 'Sunny' appliers undertuned (WR: 27.5%, casts: 2405) |
| `LLL` | Light | Buff / Sustain | 8.8 -> **9.1** (+3.4%) | - | 8.8 -> **9.1** | Class Light undertuned (WR: 45.9%, factor: 1.017); Individual spell undertuned (WR: 45.4%, Casts: 4172, mult: 1.015) |
| `LLD` | Light | Ultimate | 6.1 -> **5.1** (-16.4%) | 282.4 -> **402.6** | 1728.7 -> **2058.4** | Class Light undertuned (WR: 45.9%, factor: 1.017); Weather 'Sunny' beneficiaries undertuned (WR: 39.8%) |
| `DDF` | Dark | Conditional Strike | 0.5 -> **0.5** (+0.0%) | 1584.5 -> **2170.8** | 792.8 -> **1085.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4428). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 23.9%, Casts: 4428, mult: 1.103) |
| `DDW` | Dark | Debuff / Control | 12.4 -> **11.3** (-8.9%) | - | 12.4 -> **11.3** | Individual spell overtuned (WR: 72.9%, Casts: 1191, mult: 0.911) |
| `DDE` | Dark | Setup - Weather | 368.4 -> **422.4** (+14.7%) | - | 368.4 -> **422.4** | Weather 'Darkness' appliers undertuned (WR: 30.9%, casts: 103); Individual spell undertuned (WR: 30.4%, Casts: 103, mult: 1.075) |
| `DDL` | Dark | Debuff / Control | 10.9 -> **10.2** (-6.4%) | - | 10.9 -> **10.2** | Individual spell overtuned (WR: 67.8%, Casts: 4111, mult: 0.932) |
| `DDD` | Dark | Debuff / Control | 4.4 -> **4.1** (-6.8%) | - | 4.4 -> **4.1** | Individual spell overtuned (WR: 69.0%, Casts: 2741, mult: 0.927) |
| `FWW` | Ghostfire | Debuff / Control | 5.4 -> **5.2** (-3.7%) | - | 5.4 -> **5.2** | Status 'Cursed' appliers overtuned on own (WR: 61.0%) |
| `FWE` | Ghostfire | Setup - Location | 128.6 -> **132.0** (+2.6%) | - | 128.6 -> **132.0** | Individual spell undertuned (WR: 31.6%, Casts: 7, mult: 1.026) |
| `FWL` | Ghostfire | Debuff / Control | 13.9 -> **12.6** (-9.4%) | - | 13.9 -> **12.6** | Status 'Cursed' appliers overtuned on own (WR: 61.0%); Individual spell overtuned (WR: 64.6%, Casts: 4103, mult: 0.946) |
| `FWD` | Ghostfire | Ultimate | 5.8 -> **4.8** (-17.2%) | 101.5 -> **146.1** | 594.5 -> **706.1** | Status 'Cursed' beneficiaries undertuned (WR: 37.3%); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 279). Increasing spread: b -18.0%, n +37.0% |
| `WFF` | Ghostfire | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 3401.6 -> **4985.0** | 2722.1 -> **3490.2** | Status 'Bleeding' beneficiaries undertuned (WR: 30.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.4% vs 30% floor, Casts: 701). Increasing spread: b -17.4%, n +35.8% |
| `WFW` | Ghostfire | Debuff / Control | 5.0 -> **4.5** (-10.0%) | - | 5.0 -> **4.5** | Individual spell overtuned (WR: 76.5%, Casts: 4668, mult: 0.895) |
| `WFL` | Ghostfire | Buff / Sustain | 47.1 -> **46.4** (-1.5%) | - | 47.1 -> **46.4** | Individual spell overtuned (WR: 54.4%, Casts: 91, mult: 0.986) |
| `WFD` | Ghostfire | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 1311.9 -> **1797.3** | 1312.9 -> **1618.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 7516). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 21.6%, Casts: 7516, mult: 1.113) |
| `FEF` | Beasts | Debuff / Control | 12.4 -> **11.6** (-6.5%) | - | 12.4 -> **11.6** | Individual spell overtuned (WR: 66.8%, Casts: 3748, mult: 0.937) |
| `FEW` | Beasts | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 2291.0 -> **2980.1** | 1604.4 -> **1788.7** | Status 'Entangled' beneficiaries overtuned (WR: 62.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 19). Increasing spread: b -18.0%, n +37.0% |
| `FEE` | Beasts | Buff / Sustain | 86.4 -> **94.0** (+8.8%) | - | 86.4 -> **94.0** | Individual spell undertuned (WR: 27.5%, Casts: 6180, mult: 1.087) |
| `FEL` | Beasts | Buff / Sustain | 127.7 -> **135.5** (+6.1%) | - | 127.7 -> **135.5** | Individual spell undertuned (WR: 33.8%, Casts: 4034, mult: 1.061) |
| `FED` | Beasts | Conditional Strike | 2.7 -> **2.5** (-7.4%) | 3.5 -> **3.5** | 12.2 -> **11.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.9% vs 30% floor, Casts: 2913). Increasing spread: b -16.9%, n +34.6%; Individual spell undertuned (WR: 23.4%, Casts: 2913, mult: 1.105) |
| `EFF` | Beasts | Debuff / Control | 0.7 -> **0.6** (-14.3%) | 1414.9 -> **1938.4** | 991.1 -> **1163.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 47). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 23.7%, Casts: 47, mult: 1.100) |
| `EFW` | Beasts | Buff / Sustain | 85.0 -> **87.4** (+2.8%) | - | 85.0 -> **87.4** | Individual spell undertuned (WR: 41.9%, Casts: 594, mult: 1.028) |
| `EFE` | Beasts | Buff / Sustain | 15.6 -> **13.7** (-12.2%) | - | 15.6 -> **13.7** | Individual spell overtuned (WR: 81.2%, Casts: 1790, mult: 0.875) |
| `EFL` | Beasts | Buff / Sustain | 0.9 -> **0.7** (-22.2%) | - | 0.9 -> **0.7** | Individual spell overtuned (WR: 95.9%, Casts: 1961, mult: 0.820) |
| `EFD` | Beasts | Ultimate | 4.6 -> **3.6** (-21.7%) | 377.7 -> **503.8** | 1742.0 -> **1817.3** | Status 'Entangled' beneficiaries overtuned (WR: 62.6%); Location 'Jungle' beneficiaries undertuned (WR: 43.6%) |
| `FLF` | Lightning | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 2063.5 -> **3090.6** | 1651.6 -> **2164.1** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Status 'Stunned' beneficiaries undertuned (WR: 25.7%) |
| `FLW` | Lightning | Debuff / Control | 9.5 -> **8.9** (-6.3%) | - | 9.5 -> **8.9** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Status 'Stunned' appliers overtuned on own (WR: 61.3%) |
| `FLE` | Lightning | Setup - Weather | 222.5 -> **247.7** (+11.3%) | - | 222.5 -> **247.7** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Weather 'Storming' appliers undertuned (WR: 38.7%, casts: 1255) |
| `FLL` | Lightning | Buff / Sustain | 37.8 -> **42.7** (+13.0%) | - | 37.8 -> **42.7** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Individual spell undertuned (WR: 24.8%, Casts: 2315, mult: 1.099) |
| `FLD` | Lightning | Ultimate | 8.4 -> **7.0** (-16.7%) | 154.5 -> **228.8** | 1306.2 -> **1608.6** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Status 'Stunned' beneficiaries undertuned (WR: 25.7%) |
| `LFF` | Lightning | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 1502.6 -> **2058.6** | 1954.7 -> **2265.6** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5895). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 18.2 -> **17.0** (-6.6%) | - | 18.2 -> **17.0** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Individual spell overtuned (WR: 73.3%, Casts: 1392, mult: 0.909) |
| `LFE` | Lightning | Debuff / Control | 9.0 -> **8.3** (-7.8%) | - | 9.0 -> **8.3** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Status 'Stunned' appliers overtuned on own (WR: 61.3%) |
| `LFL` | Lightning | Debuff / Control | 1.3 -> **1.2** (-7.7%) | 1058.9 -> **1450.7** | 1377.9 -> **1742.0** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4086). Increasing spread: b -18.0%, n +37.0% |
| `LFD` | Lightning | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 1781.0 -> **2440.0** | 1247.4 -> **1464.6** | Class Lightning undertuned (WR: 42.8%, factor: 1.029); Status 'Stunned' appliers overtuned on own (WR: 61.3%) |
| `FDF` | Blood | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 1584.5 -> **2170.8** | 634.2 -> **651.5** | Class Blood overtuned (WR: 62.7%, factor: 0.949); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 561). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 80.0 -> **78.6** (-1.8%) | - | 80.0 -> **78.6** | Class Blood overtuned (WR: 62.7%, factor: 0.949); Individual spell undertuned (WR: 40.1%, Casts: 4486, mult: 1.035) |
| `FDE` | Blood | Setup - Weather | 63.5 -> **59.2** (-6.8%) | - | 63.5 -> **59.2** | Class Blood overtuned (WR: 62.7%, factor: 0.949); Individual spell overtuned (WR: 55.4%, Casts: 566, mult: 0.982) |
| `FDD` | Blood | Ultimate | 4.1 -> **3.1** (-24.4%) | 106.6 -> **146.0** | 441.2 -> **455.7** | Class Blood overtuned (WR: 62.7%, factor: 0.949); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 4077). Increasing spread: b -18.0%, n +37.0% |
| `DFF` | Blood | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 2549.6 -> **3670.8** | 2295.5 -> **2937.4** | Class Blood overtuned (WR: 62.7%, factor: 0.949); Status 'Bleeding' beneficiaries undertuned (WR: 30.2%) |
| `DFE` | Blood | Buff / Sustain | 196.0 -> **219.5** (+12.0%) | - | 196.0 -> **219.5** | Class Blood overtuned (WR: 62.7%, factor: 0.949); Individual spell undertuned (WR: 3.5%, Casts: 721, mult: 1.180) |
| `DFL` | Blood | Buff / Sustain | 6.5 -> **5.8** (-10.8%) | - | 6.5 -> **5.8** | Class Blood overtuned (WR: 62.7%, factor: 0.949); Individual spell overtuned (WR: 65.9%, Casts: 4109, mult: 0.941) |
| `DFD` | Blood | Conditional Strike | 127.8 -> **127.6** (-0.2%) | 0.1 -> **0.1** | 140.6 -> **140.4** | Class Blood overtuned (WR: 62.7%, factor: 0.949); Condition triggers excessively (N=1 conditions, Trigger Rate: 79.3% vs 55% ceiling, WR: 94.8%). Compressing spread: b +28.3%, n -34.6% |
| `WEF` | Plants | Conditional Strike | 0.7 -> **0.7** (+0.0%) | 1676.1 -> **2349.8** | 1174.0 -> **1645.6** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Location 'Jungle' beneficiaries undertuned (WR: 43.6%) |
| `WEW` | Plants | Debuff / Control | 90.8 -> **100.1** (+10.2%) | - | 90.8 -> **100.1** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Individual spell undertuned (WR: 32.2%, Casts: 414, mult: 1.068) |
| `WEE` | Plants | Setup - Location | 294.7 -> **396.2** (+34.4%) | - | 294.7 -> **396.2** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Location 'Jungle' appliers undertuned (WR: 10.6%, casts: 5656) |
| `WEL` | Plants | Debuff / Control | 12.7 -> **10.3** (-18.9%) | - | 12.7 -> **10.3** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Status 'Entangled' appliers overtuned on own (WR: 81.8%) |
| `WED` | Plants | Conditional Strike | 6.8 -> **5.8** (-14.7%) | 53.4 -> **73.2** | 369.9 -> **430.4** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 5553). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 1.9 -> **1.8** (-5.3%) | 2475.4 -> **3480.0** | 4705.2 -> **6265.8** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Weather 'Sunny' beneficiaries undertuned (WR: 39.8%) |
| `EWW` | Plants | Debuff / Control | 1.1 -> **0.9** (-18.2%) | - | 1.1 -> **0.9** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Individual spell overtuned (WR: 92.0%, Casts: 1648, mult: 0.826) |
| `EWL` | Plants | Debuff / Control | 16.2 -> **15.4** (-4.9%) | - | 16.2 -> **15.4** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Individual spell overtuned (WR: 70.7%, Casts: 1121, mult: 0.920) |
| `EWD` | Plants | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 2223.5 -> **2892.3** | 444.9 -> **578.7** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Status 'Bleeding' appliers overtuned on own (WR: 86.3%) |
| `WLF` | Fey | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 1086.5 -> **1557.5** | 1196.2 -> **1558.5** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Status 'Cursed' beneficiaries undertuned (WR: 37.3%) |
| `WLW` | Fey | Debuff / Control | 11.1 -> **10.6** (-4.5%) | - | 11.1 -> **10.6** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Status 'Cursed' appliers overtuned on own (WR: 61.0%) |
| `WLE` | Fey | Setup - Location | 716.2 -> **973.7** (+36.0%) | - | 716.2 -> **973.7** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Location 'Enchanted Forest' appliers undertuned (WR: 8.6%, casts: 4393) |
| `WLL` | Fey | Direct Damage | 36.3 -> **32.1** (-11.6%) | - | 36.3 -> **32.1** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Individual spell overtuned (WR: 86.3%, Casts: 4518, mult: 0.853) |
| `WLD` | Fey | Ultimate | 6.6 -> **8.0** (+21.2%) | 307.5 -> **308.9** | 2036.1 -> **2479.2** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Location 'Enchanted Forest' beneficiaries undertuned (WR: 32.9%) |
| `LWF` | Fey | Debuff / Control | 2.4 -> **2.2** (-8.3%) | 1511.0 -> **2210.5** | 3628.8 -> **4865.3** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Location 'Enchanted Forest' beneficiaries undertuned (WR: 32.9%) |
| `LWW` | Fey | Debuff / Control | 63.2 -> **72.2** (+14.2%) | - | 63.2 -> **72.2** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Individual spell undertuned (WR: 24.1%, Casts: 3161, mult: 1.102) |
| `LWL` | Fey | Debuff / Control | 278.6 -> **336.0** (+20.6%) | - | 278.6 -> **336.0** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Individual spell undertuned (WR: 10.3%, Casts: 1837, mult: 1.163) |
| `LWD` | Fey | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 1584.5 -> **2170.8** | 1902.6 -> **2171.8** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 153). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 1.0 -> **0.7** (-30.0%) | 3204.7 -> **4213.8** | 3205.7 -> **2950.4** | Class Ice overtuned (WR: 56.0%, factor: 0.976); Status 'Stunned' appliers overtuned on own (WR: 61.3%) |
| `WDW` | Ice | Buff / Sustain | 40.3 -> **38.0** (-5.7%) | - | 40.3 -> **38.0** | Class Ice overtuned (WR: 56.0%, factor: 0.976); Status 'Frosty' appliers overtuned on own (WR: 55.4%) |
| `WDE` | Ice | Setup - Weather | 106.8 -> **118.9** (+11.3%) | - | 106.8 -> **118.9** | Class Ice overtuned (WR: 56.0%, factor: 0.976); Individual spell undertuned (WR: 15.3%, Casts: 2565, mult: 1.141) |
| `WDD` | Ice | Ultimate | 6.7 -> **5.2** (-22.4%) | 75.1 -> **97.7** | 509.9 -> **513.2** | Class Ice overtuned (WR: 56.0%, factor: 0.976); Weather 'Blizzard' beneficiaries overtuned (WR: 56.4%) |
| `DWF` | Ice | Debuff / Control | 9.7 -> **8.9** (-8.2%) | - | 9.7 -> **8.9** | Class Ice overtuned (WR: 56.0%, factor: 0.976); Status 'Frosty' appliers overtuned on own (WR: 55.4%) |
| `DWW` | Ice | Debuff / Control | 12.7 -> **11.2** (-11.8%) | - | 12.7 -> **11.2** | Class Ice overtuned (WR: 56.0%, factor: 0.976); Individual spell overtuned (WR: 75.1%, Casts: 4635, mult: 0.902) |
| `DWE` | Ice | Setup - Location | 202.2 -> **202.7** (+0.2%) | - | 202.2 -> **202.7** | Class Ice overtuned (WR: 56.0%, factor: 0.976); Location 'Tundra' appliers undertuned (WR: 46.0%, casts: 975) |
| `DWL` | Ice | Debuff / Control | 12.7 -> **12.5** (-1.6%) | - | 12.7 -> **12.5** | Class Ice overtuned (WR: 56.0%, factor: 0.976); Status 'Frosty' appliers overtuned on own (WR: 55.4%) |
| `DWD` | Ice | Conditional Strike | 1.3 -> **1.0** (-23.1%) | 1783.1 -> **2201.0** | 2319.3 -> **2202.0** | Class Ice overtuned (WR: 56.0%, factor: 0.976); Status 'Frosty' beneficiaries overtuned (WR: 67.8%) |
| `ELF` | Wind | Conditional Strike | 2.7 -> **2.2** (-18.5%) | 3041.2 -> **4435.5** | 8213.9 -> **9760.3** | Status 'Bleeding' beneficiaries undertuned (WR: 30.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 3435). Increasing spread: b -17.1%, n +35.2% |
| `ELW` | Wind | Debuff / Control | 22.3 -> **19.2** (-13.9%) | - | 22.3 -> **19.2** | Individual spell overtuned (WR: 83.9%, Casts: 2847, mult: 0.863) |
| `ELL` | Wind | Buff / Sustain | 82.7 -> **74.6** (-9.8%) | - | 82.7 -> **74.6** | Individual spell overtuned (WR: 74.9%, Casts: 589, mult: 0.903) |
| `ELD` | Wind | Conditional Strike | 3.2 -> **2.6** (-18.8%) | 2853.4 -> **3751.9** | 9134.1 -> **9757.5** | Weather 'Raining' beneficiaries overtuned (WR: 60.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3331). Increasing spread: b -18.0%, n +37.0% |
| `LEF` | Wind | Conditional Strike | 1.6 -> **1.3** (-18.8%) | 2355.1 -> **3468.3** | 3769.8 -> **4510.1** | Status 'Burning' beneficiaries undertuned (WR: 30.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 4335). Increasing spread: b -17.9%, n +36.8% |
| `LEW` | Wind | Debuff / Control | 24.2 -> **21.8** (-9.9%) | - | 24.2 -> **21.8** | Individual spell overtuned (WR: 74.8%, Casts: 143, mult: 0.903) |
| `LEE` | Wind | Setup - Weather | 140.1 -> **149.2** (+6.5%) | - | 140.1 -> **149.2** | Individual spell undertuned (WR: 32.8%, Casts: 348, mult: 1.065) |
| `LEL` | Wind | Buff / Sustain | 171.9 -> **188.2** (+9.5%) | - | 171.9 -> **188.2** | Individual spell undertuned (WR: 25.7%, Casts: 5806, mult: 1.095) |
| `EDF` | Poison | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 1011.9 -> **1386.3** | 506.4 -> **554.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1422). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 29.4%, Casts: 1422, mult: 1.079) |
| `EDW` | Poison | Debuff / Control | 5.0 -> **4.4** (-12.0%) | - | 5.0 -> **4.4** | Individual spell overtuned (WR: 78.9%, Casts: 4573, mult: 0.885) |
| `EDD` | Poison | Ultimate | 8.9 -> **7.1** (-20.2%) | 208.9 -> **300.2** | 1868.1 -> **2138.5** | Status 'Bleeding' beneficiaries undertuned (WR: 30.2%); Location 'Swamp' beneficiaries overtuned (WR: 57.0%) |
| `DEF` | Poison | Conditional Strike | 4.5 -> **3.7** (-17.8%) | 14.9 -> **20.3** | 71.5 -> **78.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 1888). Increasing spread: b -17.8%, n +36.6% |
| `DEW` | Poison | Debuff / Control | 4.3 -> **3.8** (-11.6%) | - | 4.3 -> **3.8** | Individual spell overtuned (WR: 77.5%, Casts: 2326, mult: 0.891) |
| `DEE` | Poison | Debuff / Control | 18.1 -> **16.0** (-11.6%) | - | 18.1 -> **16.0** | Individual spell overtuned (WR: 79.8%, Casts: 1544, mult: 0.881) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 3317.7 -> **4904.7** | 995.6 -> **1471.7** | Status 'Bleeding' beneficiaries undertuned (WR: 30.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 9864). Increasing spread: b -18.0%, n +37.0% |
| `DED` | Poison | Debuff / Control | 17.4 -> **15.8** (-9.2%) | - | 17.4 -> **15.8** | Individual spell overtuned (WR: 73.2%, Casts: 2940, mult: 0.910) |
| `LDF` | Cosmic | Debuff / Control | 19.8 -> **22.9** (+15.7%) | - | 19.8 -> **22.9** | Individual spell undertuned (WR: 11.4%, Casts: 1374, mult: 1.158) |
| `LDW` | Cosmic | Debuff / Control | 9.6 -> **8.2** (-14.6%) | - | 9.6 -> **8.2** | Status 'Stunned' appliers overtuned on own (WR: 61.3%); Individual spell overtuned (WR: 77.2%, Casts: 914, mult: 0.892) |
| `LDE` | Cosmic | Setup - Location | 67.6 -> **76.5** (+13.2%) | - | 67.6 -> **76.5** | Individual spell undertuned (WR: 17.2%, Casts: 5007, mult: 1.132) |
| `LDL` | Cosmic | Conditional Strike | 1.1 -> **0.9** (-18.2%) | 1318.6 -> **1806.5** | 1451.6 -> **1626.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4965). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 40.2%, Casts: 4965, mult: 1.035) |
| `LDD` | Cosmic | Ultimate | 6.3 -> **5.0** (-20.6%) | 132.5 -> **181.5** | 841.0 -> **912.5** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 8300). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 59.0%, Casts: 8300, mult: 0.968) |
| `DLF` | Cosmic | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 1196.8 -> **1639.6** | 1557.1 -> **1804.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 274). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 39.9%, Casts: 274, mult: 1.036) |
| `DLW` | Cosmic | Direct Damage | 14.3 -> **13.4** (-6.3%) | - | 14.3 -> **13.4** | Individual spell overtuned (WR: 66.1%, Casts: 7912, mult: 0.939) |
| `DLE` | Cosmic | Direct Damage | 212.2 -> **236.1** (+11.3%) | - | 212.2 -> **236.1** | Individual spell undertuned (WR: 21.6%, Casts: 881, mult: 1.113) |
| `DLL` | Cosmic | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 1232.0 -> **1687.8** | 1726.2 -> **2026.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 269). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 39.9%, Casts: 269, mult: 1.036) |
