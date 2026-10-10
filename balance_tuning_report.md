# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T16:01:49Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 82.6s  
**Total Spells Tuned:** 118 / 125  

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
| **Fire** | 22,054 | 60.7% | 60.7% | 11.3 | Overtuned ⚠️ |
| **Dark** | 17,222 | 60.1% | 60.1% | 8.8 | Overtuned ⚠️ |
| **Poison** | 32,368 | 59.0% | 59.0% | 7.2 | Overtuned ⚠️ |
| **Blood** | 22,361 | 58.3% | 58.3% | 6.8 | Overtuned ⚠️ |
| **Cosmic** | 47,755 | 56.5% | 56.5% | 12.6 | Overtuned ⚠️ |
| **Ghostfire** | 14,919 | 54.4% | 54.4% | 3.4 | Overtuned ⚠️ |
| **Ice** | 38,111 | 53.3% | 53.3% | 10.6 | Balanced ✅ |
| **Beasts** | 19,099 | 51.6% | 51.6% | 4.1 | Balanced ✅ |
| **Lightning** | 23,831 | 49.1% | 49.1% | 7.1 | Balanced ✅ |
| **Earth** | 30,600 | 47.6% | 47.6% | 12.6 | Balanced ✅ |
| **Plants** | 17,909 | 41.7% | 41.7% | 2.1 | Undertuned ⚠️ |
| **Light** | 15,768 | 41.2% | 41.2% | 5.5 | Undertuned ⚠️ |
| **Fey** | 16,235 | 33.8% | 33.8% | 4.0 | Undertuned ⚠️ |
| **Wind** | 19,277 | 31.5% | 31.5% | 4.1 | Undertuned ⚠️ |
| **Water** | 11,485 | 30.1% | 30.1% | 3.6 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 12,739 (71.2%) | 8,228 (30.1%) | 4.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 3,541 (11.5%) | 12,429 (36.5%) | 0.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,090 (68.4%) | 9,103 (29.8%) | 1.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 12,906 (85.8%) | 14,166 (38.3%) | 1.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 25,805 (54.7%) | 7,721 (51.3%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 170 (77.6%) | 4,663 (33.6%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 3,573 (7.5%) | 1,715 (24.2%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 33.8 -> **30.3** (-10.4%) | - | 33.8 -> **30.3** | Class Fire overtuned (WR: 60.7%, factor: 0.957); Individual spell overtuned (WR: 67.1%, Casts: 3549, mult: 0.935) |
| `FFW` | Fire | Debuff / Control | 20.3 -> **19.2** (-5.4%) | - | 20.3 -> **19.2** | Class Fire overtuned (WR: 60.7%, factor: 0.957); Status 'Burning' appliers overtuned on own (WR: 68.4%) |
| `FFE` | Fire | Debuff / Control | 20.4 -> **17.3** (-15.2%) | - | 20.4 -> **17.3** | Class Fire overtuned (WR: 60.7%, factor: 0.957); Individual spell overtuned (WR: 79.2%, Casts: 9893, mult: 0.884) |
| `FFL` | Fire | Debuff / Control | 1.5 -> **1.2** (-20.0%) | - | 1.5 -> **1.2** | Class Fire overtuned (WR: 60.7%, factor: 0.957); Status 'Burning' appliers overtuned on own (WR: 68.4%) |
| `FFD` | Fire | Conditional Strike | 4.3 -> **3.8** (-11.6%) | 58.2 -> **85.8** | 254.6 -> **329.8** | Class Fire overtuned (WR: 60.7%, factor: 0.957); Status 'Burning' beneficiaries undertuned (WR: 29.8%) |
| `WWF` | Water | Conditional Strike | 4.5 -> **4.2** (-6.7%) | 45.0 -> **66.0** | 207.0 -> **281.4** | Class Water undertuned (WR: 30.1%, factor: 1.080); Status 'Burning' beneficiaries undertuned (WR: 29.8%) |
| `WWE` | Water | Setup - Weather | 67.5 -> **94.5** (+40.0%) | - | 67.5 -> **94.5** | Class Water undertuned (WR: 30.1%, factor: 1.080); Weather 'Raining' appliers undertuned (WR: 7.5%, casts: 3573) |
| `WWL` | Water | Buff / Sustain | 45.8 -> **47.2** (+3.1%) | - | 45.8 -> **47.2** | Class Water undertuned (WR: 30.1%, factor: 1.080); Individual spell overtuned (WR: 62.2%, Casts: 1852, mult: 0.955) |
| `WWD` | Water | Buff / Sustain | 38.1 -> **40.0** (+5.0%) | - | 38.1 -> **40.0** | Class Water undertuned (WR: 30.1%, factor: 1.080); Individual spell overtuned (WR: 58.2%, Casts: 392, mult: 0.971) |
| `EEF` | Earth | Conditional Strike | 5.0 -> **4.5** (-10.0%) | 63.2 -> **90.5** | 321.0 -> **411.8** | Status 'Frosty' beneficiaries undertuned (WR: 30.1%); Status 'Stunned' appliers overtuned on own (WR: 54.7%) |
| `EEW` | Earth | Buff / Sustain | 44.1 -> **50.0** (+13.4%) | - | 44.1 -> **50.0** | Individual spell undertuned (WR: 17.0%, Casts: 3524, mult: 1.133) |
| `EED` | Earth | Direct Damage | 3.5 -> **3.3** (-5.7%) | - | 3.5 -> **3.3** | Individual spell overtuned (WR: 65.6%, Casts: 8807, mult: 0.942) |
| `LLF` | Light | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 59.3 -> **78.5** | 18.1 -> **15.9** | Class Light undertuned (WR: 41.2%, factor: 1.035); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.6% vs 30% floor, Casts: 449). Increasing spread: b -15.8%, n +32.4% |
| `LLW` | Light | Debuff / Control | 21.5 -> **22.8** (+6.0%) | - | 21.5 -> **22.8** | Class Light undertuned (WR: 41.2%, factor: 1.035); Individual spell undertuned (WR: 42.9%, Casts: 5428, mult: 1.024) |
| `LLE` | Light | Setup - Weather | 109.4 -> **146.8** (+34.2%) | - | 109.4 -> **146.8** | Class Light undertuned (WR: 41.2%, factor: 1.035); Weather 'Sunny' appliers undertuned (WR: 11.5%, casts: 3541) |
| `LLL` | Light | Buff / Sustain | 14.0 -> **13.1** (-6.4%) | - | 14.0 -> **13.1** | Class Light undertuned (WR: 41.2%, factor: 1.035); Individual spell overtuned (WR: 73.9%, Casts: 2068, mult: 0.907) |
| `LLD` | Light | Ultimate | 14.8 -> **16.8** (+13.5%) | 27.7 -> **27.4** | 424.8 -> **477.1** | Class Light undertuned (WR: 41.2%, factor: 1.035); Weather 'Sunny' beneficiaries undertuned (WR: 36.5%) |
| `DDF` | Dark | Conditional Strike | 2.8 -> **2.3** (-17.9%) | 68.0 -> **93.2** | 193.2 -> **216.7** | Class Dark overtuned (WR: 60.1%, factor: 0.960); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1179). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 35.8 -> **32.7** (-8.7%) | - | 35.8 -> **32.7** | Class Dark overtuned (WR: 60.1%, factor: 0.960); Individual spell overtuned (WR: 62.8%, Casts: 5778, mult: 0.953) |
| `DDE` | Dark | Setup - Weather | 77.1 -> **70.9** (-8.0%) | - | 77.1 -> **70.9** | Class Dark overtuned (WR: 60.1%, factor: 0.960); Weather 'Darkness' appliers overtuned on own (WR: 56.2%) |
| `DDL` | Dark | Debuff / Control | 18.1 -> **17.0** (-6.1%) | - | 18.1 -> **17.0** | Class Dark overtuned (WR: 60.1%, factor: 0.960); Individual spell overtuned (WR: 56.8%, Casts: 5303, mult: 0.977) |
| `DDD` | Dark | Debuff / Control | 10.6 -> **9.5** (-10.4%) | - | 10.6 -> **9.5** | Class Dark overtuned (WR: 60.1%, factor: 0.960); Individual spell overtuned (WR: 68.6%, Casts: 3451, mult: 0.929) |
| `FWF` | Ghostfire | Debuff / Control | 7.8 -> **6.3** (-19.2%) | - | 7.8 -> **6.3** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Status 'Burning' appliers overtuned on own (WR: 68.4%) |
| `FWW` | Ghostfire | Debuff / Control | 11.2 -> **11.8** (+5.4%) | - | 11.2 -> **11.8** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Status 'Cursed' appliers undertuned (WR: 40.8%, casts: 4451) |
| `FWE` | Ghostfire | Setup - Location | 66.9 -> **75.0** (+12.1%) | - | 66.9 -> **75.0** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Location 'Graveyard' appliers undertuned (WR: 31.8%, casts: 59) |
| `FWL` | Ghostfire | Debuff / Control | 27.9 -> **30.3** (+8.6%) | - | 27.9 -> **30.3** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Status 'Cursed' appliers undertuned (WR: 40.8%, casts: 4451) |
| `FWD` | Ghostfire | Ultimate | 14.7 -> **17.1** (+16.3%) | 20.5 -> **21.6** | 316.1 -> **386.5** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Status 'Cursed' beneficiaries undertuned (WR: 44.3%) |
| `WFF` | Ghostfire | Conditional Strike | 3.0 -> **2.4** (-20.0%) | 82.0 -> **117.3** | 249.0 -> **283.9** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Status 'Bleeding' beneficiaries undertuned (WR: 38.3%) |
| `WFW` | Ghostfire | Debuff / Control | 13.6 -> **11.6** (-14.7%) | - | 13.6 -> **11.6** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Individual spell overtuned (WR: 81.9%, Casts: 574, mult: 0.872) |
| `WFE` | Ghostfire | Debuff / Control | 4.4 -> **3.3** (-25.0%) | - | 4.4 -> **3.3** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Status 'Bleeding' appliers overtuned on own (WR: 85.8%) |
| `WFL` | Ghostfire | Buff / Sustain | 45.5 -> **43.7** (-4.0%) | - | 45.5 -> **43.7** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Individual spell overtuned (WR: 56.8%, Casts: 835, mult: 0.977) |
| `WFD` | Ghostfire | Conditional Strike | 2.9 -> **2.6** (-10.3%) | 58.9 -> **80.7** | 173.7 -> **212.4** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3766). Increasing spread: b -18.0%, n +37.0% |
| `FEF` | Beasts | Debuff / Control | 17.3 -> **16.0** (-7.5%) | - | 17.3 -> **16.0** | Individual spell overtuned (WR: 69.7%, Casts: 2636, mult: 0.925) |
| `FEW` | Beasts | Conditional Strike | 4.1 -> **3.7** (-9.8%) | 82.0 -> **119.7** | 340.3 -> **446.6** | Status 'Entangled' beneficiaries undertuned (WR: 33.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2400). Increasing spread: b -18.0%, n +37.0% |
| `FEE` | Beasts | Buff / Sustain | 32.2 -> **34.3** (+6.5%) | - | 32.2 -> **34.3** | Individual spell undertuned (WR: 32.6%, Casts: 1515, mult: 1.066) |
| `FEL` | Beasts | Buff / Sustain | 68.3 -> **70.5** (+3.2%) | - | 68.3 -> **70.5** | Individual spell undertuned (WR: 41.1%, Casts: 548, mult: 1.032) |
| `FED` | Beasts | Conditional Strike | 4.2 -> **3.8** (-9.5%) | 3.5 -> **3.5** | 18.9 -> **17.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.2% vs 30% floor, Casts: 4849). Increasing spread: b -16.3%, n +33.5%; Individual spell undertuned (WR: 29.2%, Casts: 4849, mult: 1.080) |
| `EFF` | Beasts | Debuff / Control | 6.6 -> **5.0** (-24.2%) | 63.5 -> **86.1** | 425.7 -> **435.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 1752). Increasing spread: b -17.4%, n +35.7%; Individual spell overtuned (WR: 69.7%, Casts: 1752, mult: 0.925) |
| `EFW` | Beasts | Buff / Sustain | 33.7 -> **36.7** (+8.9%) | - | 33.7 -> **36.7** | Individual spell undertuned (WR: 27.1%, Casts: 58, mult: 1.089) |
| `EFE` | Beasts | Buff / Sustain | 30.7 -> **27.9** (-9.1%) | - | 30.7 -> **27.9** | Individual spell overtuned (WR: 73.3%, Casts: 1971, mult: 0.909) |
| `EFL` | Beasts | Buff / Sustain | 5.4 -> **4.4** (-18.5%) | - | 5.4 -> **4.4** | Individual spell overtuned (WR: 96.8%, Casts: 1969, mult: 0.820) |
| `EFD` | Beasts | Ultimate | 17.1 -> **14.0** (-18.1%) | 43.4 -> **63.4** | 759.2 -> **901.6** | Status 'Entangled' beneficiaries undertuned (WR: 33.6%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1401). Increasing spread: b -18.0%, n +37.0% |
| `FLF` | Lightning | Conditional Strike | 3.4 -> **3.3** (-2.9%) | 78.2 -> **106.8** | 269.3 -> **355.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 180). Increasing spread: b -17.8%, n +36.5%; Individual spell undertuned (WR: 9.4%, Casts: 180, mult: 1.167) |
| `FLW` | Lightning | Debuff / Control | 24.7 -> **24.3** (-1.6%) | - | 24.7 -> **24.3** | Status 'Stunned' appliers overtuned on own (WR: 54.7%) |
| `FLE` | Lightning | Setup - Weather | 28.7 -> **31.8** (+10.8%) | - | 28.7 -> **31.8** | Weather 'Storming' appliers undertuned (WR: 35.7%, casts: 62); Individual spell undertuned (WR: 35.1%, Casts: 62, mult: 1.055) |
| `FLL` | Lightning | Buff / Sustain | 40.3 -> **41.2** (+2.2%) | - | 40.3 -> **41.2** | Individual spell undertuned (WR: 43.8%, Casts: 116, mult: 1.021) |
| `FLD` | Lightning | Ultimate | 25.0 -> **20.5** (-18.0%) | 16.9 -> **23.2** | 447.5 -> **496.1** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 7541). Increasing spread: b -18.0%, n +37.0% |
| `LFF` | Lightning | Conditional Strike | 4.5 -> **3.7** (-17.8%) | 64.5 -> **88.4** | 294.8 -> **330.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1619). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 23.8 -> **23.4** (-1.7%) | - | 23.8 -> **23.4** | Individual spell overtuned (WR: 55.4%, Casts: 2667, mult: 0.982) |
| `LFE` | Lightning | Debuff / Control | 20.6 -> **19.1** (-7.3%) | - | 20.6 -> **19.1** | Status 'Stunned' appliers overtuned on own (WR: 54.7%); Individual spell overtuned (WR: 65.5%, Casts: 4930, mult: 0.942) |
| `LFL` | Lightning | Debuff / Control | 5.9 -> **5.2** (-11.9%) | 49.4 -> **70.1** | 297.4 -> **369.7** | Weather 'Darkness' beneficiaries undertuned (WR: 38.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 4811). Increasing spread: b -17.3%, n +35.5% |
| `LFD` | Lightning | Conditional Strike | 3.9 -> **3.4** (-12.8%) | 79.0 -> **108.2** | 312.0 -> **371.3** | Status 'Stunned' appliers overtuned on own (WR: 54.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1014). Increasing spread: b -18.0%, n +36.9% |
| `FDF` | Blood | Conditional Strike | 2.7 -> **2.2** (-18.5%) | 68.0 -> **93.2** | 186.3 -> **207.2** | Class Blood overtuned (WR: 58.3%, factor: 0.967); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2468). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 71.6 -> **79.1** (+10.5%) | - | 71.6 -> **79.1** | Class Blood overtuned (WR: 58.3%, factor: 0.967); Individual spell undertuned (WR: 14.7%, Casts: 1447, mult: 1.143) |
| `FDE` | Blood | Setup - Weather | 45.5 -> **49.5** (+8.8%) | - | 45.5 -> **49.5** | Class Blood overtuned (WR: 58.3%, factor: 0.967); Individual spell undertuned (WR: 18.8%, Casts: 1106, mult: 1.125) |
| `FDL` | Blood | Debuff / Control | 4.4 -> **3.2** (-27.3%) | - | 4.4 -> **3.2** | Class Blood overtuned (WR: 58.3%, factor: 0.967); Status 'Bleeding' appliers overtuned on own (WR: 85.8%) |
| `FDD` | Blood | Ultimate | 10.8 -> **11.5** (+6.5%) | 25.8 -> **25.4** | 289.4 -> **303.6** | Class Blood overtuned (WR: 58.3%, factor: 0.967); Weather 'Darkness' beneficiaries undertuned (WR: 38.3%) |
| `DFF` | Blood | Conditional Strike | 4.1 -> **3.7** (-9.8%) | 71.4 -> **100.3** | 296.8 -> **374.8** | Class Blood overtuned (WR: 58.3%, factor: 0.967); Status 'Bleeding' beneficiaries undertuned (WR: 38.3%) |
| `DFW` | Blood | Debuff / Control | 3.4 -> **2.5** (-26.5%) | - | 3.4 -> **2.5** | Class Blood overtuned (WR: 58.3%, factor: 0.967); Status 'Bleeding' appliers overtuned on own (WR: 85.8%) |
| `DFE` | Blood | Buff / Sustain | 99.8 -> **96.5** (-3.3%) | - | 99.8 -> **96.5** | Class Blood overtuned (WR: 58.3%, factor: 0.967) |
| `DFL` | Blood | Buff / Sustain | 17.0 -> **15.3** (-10.0%) | - | 17.0 -> **15.3** | Class Blood overtuned (WR: 58.3%, factor: 0.967); Individual spell overtuned (WR: 68.3%, Casts: 2715, mult: 0.930) |
| `DFD` | Blood | Conditional Strike | 70.4 -> **75.7** (+7.5%) | 0.1 -> **0.1** | 77.4 -> **83.3** | Class Blood overtuned (WR: 58.3%, factor: 0.967); Condition triggers excessively (N=1 conditions, Trigger Rate: 91.5% vs 55% ceiling, WR: 74.2%). Compressing spread: b +22.8%, n -30.7% |
| `WEF` | Plants | Conditional Strike | 4.2 -> **3.4** (-19.0%) | 77.1 -> **105.6** | 328.0 -> **362.4** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 237). Increasing spread: b -18.0%, n +37.0% |
| `WEW` | Plants | Debuff / Control | 39.1 -> **37.6** (-3.8%) | - | 39.1 -> **37.6** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Individual spell overtuned (WR: 68.3%, Casts: 133, mult: 0.931) |
| `WEE` | Plants | Setup - Location | 63.3 -> **73.3** (+15.8%) | - | 63.3 -> **73.3** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Location 'Jungle' appliers undertuned (WR: 33.8%, casts: 962) |
| `WEL` | Plants | Debuff / Control | 32.8 -> **27.2** (-17.1%) | - | 32.8 -> **27.2** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Status 'Entangled' appliers overtuned on own (WR: 77.6%) |
| `WED` | Plants | Conditional Strike | 14.9 -> **17.0** (+14.1%) | 10.4 -> **9.8** | 169.9 -> **183.6** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4394, WR: 43.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 4.2 -> **3.8** (-9.5%) | 56.7 -> **81.5** | 242.3 -> **313.5** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Weather 'Sunny' beneficiaries undertuned (WR: 36.5%) |
| `EWW` | Plants | Debuff / Control | 5.6 -> **4.8** (-14.3%) | - | 5.6 -> **4.8** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Individual spell overtuned (WR: 92.3%, Casts: 1757, mult: 0.826) |
| `EWL` | Plants | Debuff / Control | 40.6 -> **41.9** (+3.2%) | - | 40.6 -> **41.9** | Class Plants undertuned (WR: 41.7%, factor: 1.033) |
| `EWD` | Plants | Conditional Strike | 1.4 -> **1.1** (-21.4%) | 80.3 -> **117.2** | 113.8 -> **130.0** | Class Plants undertuned (WR: 41.7%, factor: 1.033); Status 'Bleeding' appliers overtuned on own (WR: 85.8%) |
| `WLF` | Fey | Conditional Strike | 5.0 -> **4.1** (-18.0%) | 52.9 -> **71.7** | 269.5 -> **298.1** | Class Fey undertuned (WR: 33.8%, factor: 1.065); Status 'Cursed' beneficiaries undertuned (WR: 44.3%) |
| `WLW` | Fey | Debuff / Control | 29.7 -> **31.6** (+6.4%) | - | 29.7 -> **31.6** | Class Fey undertuned (WR: 33.8%, factor: 1.065); Status 'Cursed' appliers undertuned (WR: 40.8%, casts: 4451) |
| `WLE` | Fey | Setup - Location | 104.0 -> **110.7** (+6.4%) | - | 104.0 -> **110.7** | Class Fey undertuned (WR: 33.8%, factor: 1.065) |
| `WLL` | Fey | Direct Damage | 63.2 -> **67.7** (+7.1%) | - | 63.2 -> **67.7** | Class Fey undertuned (WR: 33.8%, factor: 1.065); Individual spell undertuned (WR: 44.4%, Casts: 6, mult: 1.006) |
| `WLD` | Fey | Ultimate | 17.2 -> **20.4** (+18.6%) | 27.7 -> **28.9** | 493.6 -> **610.0** | Class Fey undertuned (WR: 33.8%, factor: 1.065); Weather 'Darkness' beneficiaries undertuned (WR: 38.3%) |
| `LWF` | Fey | Debuff / Control | 8.0 -> **7.4** (-7.5%) | 53.8 -> **78.1** | 438.4 -> **585.3** | Class Fey undertuned (WR: 33.8%, factor: 1.065); Location 'Enchanted Forest' beneficiaries undertuned (WR: 35.1%) |
| `LWW` | Fey | Debuff / Control | 74.0 -> **68.0** (-8.1%) | - | 74.0 -> **68.0** | Class Fey undertuned (WR: 33.8%, factor: 1.065); Individual spell overtuned (WR: 84.0%, Casts: 275, mult: 0.863) |
| `LWL` | Fey | Debuff / Control | 67.7 -> **85.1** (+25.7%) | - | 67.7 -> **85.1** | Class Fey undertuned (WR: 33.8%, factor: 1.065); Individual spell undertuned (WR: 6.1%, Casts: 1176, mult: 1.180) |
| `LWD` | Fey | Conditional Strike | 6.0 -> **5.6** (-6.7%) | 68.0 -> **93.2** | 414.0 -> **527.5** | Class Fey undertuned (WR: 33.8%, factor: 1.065); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5154). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 5.2 -> **4.7** (-9.6%) | 77.0 -> **116.3** | 405.6 -> **551.3** | Status 'Stunned' appliers overtuned on own (WR: 54.7%); Weather 'Raining' beneficiaries undertuned (WR: 24.2%) |
| `WDW` | Ice | Buff / Sustain | 26.6 -> **26.4** (-0.8%) | - | 26.6 -> **26.4** | Status 'Frosty' appliers overtuned on own (WR: 71.2%); Individual spell undertuned (WR: 31.1%, Casts: 641, mult: 1.072) |
| `WDE` | Ice | Setup - Weather | 45.3 -> **47.6** (+5.1%) | - | 45.3 -> **47.6** | Individual spell undertuned (WR: 36.1%, Casts: 2007, mult: 1.052) |
| `WDL` | Ice | Debuff / Control | 36.1 -> **31.3** (-13.3%) | - | 36.1 -> **31.3** | Status 'Frosty' appliers overtuned on own (WR: 71.2%); Individual spell overtuned (WR: 66.7%, Casts: 54, mult: 0.937) |
| `WDD` | Ice | Ultimate | 21.0 -> **23.0** (+9.5%) | 20.1 -> **19.5** | 443.1 -> **471.5** | Weather 'Blizzard' beneficiaries undertuned (WR: 46.0%); Location 'Tundra' beneficiaries undertuned (WR: 46.0%) |
| `DWF` | Ice | Debuff / Control | 32.2 -> **26.7** (-17.1%) | - | 32.2 -> **26.7** | Status 'Frosty' appliers overtuned on own (WR: 71.2%); Individual spell overtuned (WR: 76.1%, Casts: 8317, mult: 0.897) |
| `DWW` | Ice | Debuff / Control | 31.6 -> **30.7** (-2.8%) | - | 31.6 -> **30.7** | Individual spell overtuned (WR: 57.8%, Casts: 11850, mult: 0.973) |
| `DWE` | Ice | Setup - Location | 61.1 -> **71.9** (+17.7%) | - | 61.1 -> **71.9** | Location 'Tundra' appliers undertuned (WR: 27.1%, casts: 5848); Individual spell undertuned (WR: 27.1%, Casts: 5848, mult: 1.089) |
| `DWL` | Ice | Debuff / Control | 34.2 -> **29.6** (-13.5%) | - | 34.2 -> **29.6** | Status 'Frosty' appliers overtuned on own (WR: 71.2%); Individual spell overtuned (WR: 67.1%, Casts: 3727, mult: 0.936) |
| `DWD` | Ice | Conditional Strike | 7.4 -> **6.6** (-10.8%) | 56.7 -> **82.4** | 427.0 -> **550.4** | Status 'Frosty' beneficiaries undertuned (WR: 30.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.8% vs 30% floor, Casts: 1101). Increasing spread: b -16.9%, n +34.7% |
| `ELF` | Wind | Conditional Strike | 8.1 -> **7.9** (-2.5%) | 77.2 -> **108.5** | 633.4 -> **865.1** | Class Wind undertuned (WR: 31.5%, factor: 1.074); Status 'Bleeding' beneficiaries undertuned (WR: 38.3%) |
| `ELW` | Wind | Debuff / Control | 36.1 -> **34.7** (-3.9%) | - | 36.1 -> **34.7** | Class Wind undertuned (WR: 31.5%, factor: 1.074); Individual spell overtuned (WR: 76.9%, Casts: 924, mult: 0.894) |
| `ELE` | Wind | Setup - Weather | 38.4 -> **44.4** (+15.6%) | - | 38.4 -> **44.4** | Class Wind undertuned (WR: 31.5%, factor: 1.074); Individual spell undertuned (WR: 30.2%, Casts: 2317, mult: 1.076) |
| `ELL` | Wind | Buff / Sustain | 56.4 -> **64.5** (+14.4%) | - | 56.4 -> **64.5** | Class Wind undertuned (WR: 31.5%, factor: 1.074); Individual spell undertuned (WR: 32.9%, Casts: 1156, mult: 1.065) |
| `ELD` | Wind | Conditional Strike | 6.0 -> **5.8** (-3.3%) | 70.0 -> **105.5** | 426.0 -> **617.7** | Class Wind undertuned (WR: 31.5%, factor: 1.074); Weather 'Raining' beneficiaries undertuned (WR: 24.2%) |
| `LEF` | Wind | Conditional Strike | 5.2 -> **4.5** (-13.5%) | 60.5 -> **88.7** | 319.8 -> **403.7** | Class Wind undertuned (WR: 31.5%, factor: 1.074); Status 'Burning' beneficiaries undertuned (WR: 29.8%) |
| `LEW` | Wind | Debuff / Control | 39.9 -> **39.1** (-2.0%) | - | 39.9 -> **39.1** | Class Wind undertuned (WR: 31.5%, factor: 1.074); Individual spell overtuned (WR: 72.8%, Casts: 1307, mult: 0.912) |
| `LEE` | Wind | Setup - Weather | 36.3 -> **44.9** (+23.7%) | - | 36.3 -> **44.9** | Class Wind undertuned (WR: 31.5%, factor: 1.074); Individual spell undertuned (WR: 13.0%, Casts: 3335, mult: 1.151) |
| `LEL` | Wind | Buff / Sustain | 72.5 -> **85.1** (+17.4%) | - | 72.5 -> **85.1** | Class Wind undertuned (WR: 31.5%, factor: 1.074); Individual spell undertuned (WR: 26.3%, Casts: 1189, mult: 1.092) |
| `EDF` | Poison | Conditional Strike | 3.3 -> **2.9** (-12.1%) | 54.6 -> **72.3** | 183.5 -> **212.6** | Class Poison overtuned (WR: 59.0%, factor: 0.964); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.4% vs 30% floor, Casts: 2568). Increasing spread: b -15.8%, n +32.5% |
| `EDW` | Poison | Debuff / Control | 11.1 -> **9.4** (-15.3%) | - | 11.1 -> **9.4** | Class Poison overtuned (WR: 59.0%, factor: 0.964); Individual spell overtuned (WR: 80.3%, Casts: 2509, mult: 0.879) |
| `EDE` | Poison | Setup - Location | 45.7 -> **54.6** (+19.5%) | - | 45.7 -> **54.6** | Class Poison overtuned (WR: 59.0%, factor: 0.964); Location 'Swamp' appliers undertuned (WR: 19.8%, casts: 1980) |
| `EDL` | Poison | Debuff / Control | 2.9 -> **2.3** (-20.7%) | - | 2.9 -> **2.3** | Class Poison overtuned (WR: 59.0%, factor: 0.964); Individual spell overtuned (WR: 94.5%, Casts: 1884, mult: 0.820) |
| `EDD` | Poison | Ultimate | 22.0 -> **17.4** (-20.9%) | 20.5 -> **29.4** | 473.0 -> **529.0** | Class Poison overtuned (WR: 59.0%, factor: 0.964); Status 'Bleeding' beneficiaries undertuned (WR: 38.3%) |
| `DEF` | Poison | Conditional Strike | 16.9 -> **11.2** (-33.7%) | 4.4 -> **5.9** | 91.3 -> **77.3** | Class Poison overtuned (WR: 59.0%, factor: 0.964); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.4% vs 30% floor, Casts: 83). Increasing spread: b -17.0%, n +35.0% |
| `DEW` | Poison | Debuff / Control | 9.9 -> **8.3** (-16.2%) | - | 9.9 -> **8.3** | Class Poison overtuned (WR: 59.0%, factor: 0.964); Individual spell overtuned (WR: 82.1%, Casts: 6563, mult: 0.871) |
| `DEE` | Poison | Debuff / Control | 19.3 -> **18.6** (-3.6%) | - | 19.3 -> **18.6** | Class Poison overtuned (WR: 59.0%, factor: 0.964) |
| `DEL` | Poison | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 74.9 -> **107.3** | 30.4 -> **43.3** | Class Poison overtuned (WR: 59.0%, factor: 0.964); Status 'Bleeding' beneficiaries undertuned (WR: 38.3%) |
| `DED` | Poison | Debuff / Control | 21.3 -> **20.2** (-5.2%) | - | 21.3 -> **20.2** | Class Poison overtuned (WR: 59.0%, factor: 0.964); Individual spell overtuned (WR: 54.5%, Casts: 7739, mult: 0.985) |
| `LDF` | Cosmic | Debuff / Control | 33.1 -> **30.6** (-7.6%) | - | 33.1 -> **30.6** | Class Cosmic overtuned (WR: 56.5%, factor: 0.974); Individual spell overtuned (WR: 63.7%, Casts: 5470, mult: 0.949) |
| `LDW` | Cosmic | Debuff / Control | 23.8 -> **20.6** (-13.4%) | - | 23.8 -> **20.6** | Class Cosmic overtuned (WR: 56.5%, factor: 0.974); Status 'Stunned' appliers overtuned on own (WR: 54.7%) |
| `LDE` | Cosmic | Setup - Location | 24.5 -> **23.4** (-4.5%) | - | 24.5 -> **23.4** | Class Cosmic overtuned (WR: 56.5%, factor: 0.974); Individual spell overtuned (WR: 58.3%, Casts: 24, mult: 0.980) |
| `LDL` | Cosmic | Conditional Strike | 4.8 -> **4.3** (-10.4%) | 57.7 -> **79.0** | 281.8 -> **344.0** | Class Cosmic overtuned (WR: 56.5%, factor: 0.974); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 7397). Increasing spread: b -18.0%, n +37.0% |
| `LDD` | Cosmic | Ultimate | 15.1 -> **12.1** (-19.9%) | 25.7 -> **35.2** | 403.2 -> **438.0** | Class Cosmic overtuned (WR: 56.5%, factor: 0.974); Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 3844). Increasing spread: b -18.0%, n +37.0% |
| `DLF` | Cosmic | Conditional Strike | 5.4 -> **4.6** (-14.8%) | 51.8 -> **70.6** | 285.1 -> **329.4** | Class Cosmic overtuned (WR: 56.5%, factor: 0.974); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 4018). Increasing spread: b -17.7%, n +36.3% |
| `DLW` | Cosmic | Direct Damage | 35.9 -> **32.0** (-10.9%) | - | 35.9 -> **32.0** | Class Cosmic overtuned (WR: 56.5%, factor: 0.974); Individual spell overtuned (WR: 72.1%, Casts: 10784, mult: 0.914) |
| `DLE` | Cosmic | Direct Damage | 67.6 -> **74.2** (+9.8%) | - | 67.6 -> **74.2** | Class Cosmic overtuned (WR: 56.5%, factor: 0.974); Individual spell undertuned (WR: 18.5%, Casts: 1736, mult: 1.126) |
| `DLL` | Cosmic | Conditional Strike | 7.6 -> **5.6** (-26.3%) | 54.5 -> **78.2** | 421.8 -> **443.5** | Class Cosmic overtuned (WR: 56.5%, factor: 0.974); Weather 'Darkness' beneficiaries undertuned (WR: 38.3%) |
