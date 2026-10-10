# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T15:02:05Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 99.9s  
**Total Spells Tuned:** 115 / 125  

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
| **Poison** | 24,307 | 66.5% | 66.5% | 9.4 | Overtuned ⚠️ |
| **Water** | 6,185 | 59.8% | 59.8% | 4.7 | Overtuned ⚠️ |
| **Ghostfire** | 26,977 | 55.4% | 55.4% | 7.7 | Overtuned ⚠️ |
| **Light** | 11,567 | 55.2% | 55.2% | 3.9 | Overtuned ⚠️ |
| **Fire** | 8,858 | 54.0% | 54.0% | 9.8 | Overtuned ⚠️ |
| **Plants** | 21,846 | 52.8% | 52.8% | 4.4 | Balanced ✅ |
| **Blood** | 20,637 | 52.2% | 52.2% | 9.8 | Balanced ✅ |
| **Dark** | 13,813 | 51.9% | 51.9% | 11.0 | Balanced ✅ |
| **Cosmic** | 20,636 | 50.8% | 50.8% | 13.0 | Balanced ✅ |
| **Earth** | 20,530 | 50.8% | 50.8% | 16.7 | Balanced ✅ |
| **Wind** | 23,702 | 48.8% | 48.8% | 11.8 | Balanced ✅ |
| **Lightning** | 23,735 | 47.4% | 47.4% | 6.8 | Balanced ✅ |
| **Ice** | 27,490 | 41.7% | 41.7% | 9.6 | Undertuned ⚠️ |
| **Beasts** | 20,613 | 39.9% | 39.9% | 1.5 | Undertuned ⚠️ |
| **Fey** | 27,645 | 38.7% | 38.7% | 7.5 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 8,710 (44.9%) | 9,549 (36.9%) | 2.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,865 (19.1%) | 8,980 (47.9%) | 1.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 7,236 (62.1%) | 10,030 (51.4%) | 2.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,652 (78.9%) | 6,788 (45.0%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,913 (49.4%) | 7,599 (33.8%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,517 (43.0%) | 1,432 (40.0%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 466 (27.3%) | 3,239 (33.0%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 45.1 -> **44.4** (-1.6%) | - | 45.1 -> **44.4** | Class Fire overtuned (WR: 54.0%, factor: 0.984) |
| `FFW` | Fire | Debuff / Control | 28.3 -> **26.7** (-5.7%) | - | 28.3 -> **26.7** | Class Fire overtuned (WR: 54.0%, factor: 0.984); Status 'Burning' appliers overtuned on own (WR: 62.1%) |
| `FFE` | Fire | Debuff / Control | 28.6 -> **26.8** (-6.3%) | - | 28.6 -> **26.8** | Class Fire overtuned (WR: 54.0%, factor: 0.984); Individual spell overtuned (WR: 63.2%, Casts: 1926, mult: 0.952) |
| `FFL` | Fire | Debuff / Control | 3.3 -> **3.0** (-9.1%) | - | 3.3 -> **3.0** | Class Fire overtuned (WR: 54.0%, factor: 0.984); Status 'Burning' appliers overtuned on own (WR: 62.1%) |
| `FFD` | Fire | Conditional Strike | 8.1 -> **6.8** (-16.0%) | 16.0 -> **21.7** | 137.7 -> **154.4** | Class Fire overtuned (WR: 54.0%, factor: 0.984); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1741). Increasing spread: b -17.2%, n +35.4% |
| `WWF` | Water | Conditional Strike | 8.4 -> **6.3** (-25.0%) | 13.3 -> **17.9** | 120.1 -> **119.1** | Class Water overtuned (WR: 59.8%, factor: 0.961); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.1% vs 30% floor, Casts: 4281). Increasing spread: b -16.7%, n +34.4% |
| `WWE` | Water | Setup - Weather | 24.7 -> **27.9** (+13.0%) | - | 24.7 -> **27.9** | Class Water overtuned (WR: 59.8%, factor: 0.961); Weather 'Raining' appliers undertuned (WR: 27.3%, casts: 466) |
| `WWL` | Water | Buff / Sustain | 50.1 -> **46.7** (-6.8%) | - | 50.1 -> **46.7** | Class Water overtuned (WR: 59.8%, factor: 0.961); Individual spell overtuned (WR: 58.4%, Casts: 522, mult: 0.970) |
| `WWD` | Water | Buff / Sustain | 33.3 -> **32.7** (-1.8%) | - | 33.3 -> **32.7** | Class Water overtuned (WR: 59.8%, factor: 0.961); Individual spell undertuned (WR: 43.4%, Casts: 292, mult: 1.023) |
| `EEF` | Earth | Conditional Strike | 9.3 -> **8.0** (-14.0%) | 16.0 -> **22.7** | 158.1 -> **189.6** | Status 'Frosty' beneficiaries undertuned (WR: 36.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.4% vs 30% floor, Casts: 3996). Increasing spread: b -17.0%, n +35.0% |
| `EEE` | Earth | Conditional Strike | 9.0 -> **9.9** (+10.0%) | 1.5 -> **1.5** | 22.5 -> **24.8** | Condition triggers excessively (N=1 conditions, Trigger Rate: 95.5% vs 55% ceiling, WR: 82.2%). Compressing spread: b +26.9%, n -35.3%; Individual spell overtuned (WR: 82.2%, Casts: 3107, mult: 0.870) |
| `EED` | Earth | Direct Damage | 5.3 -> **4.9** (-7.5%) | - | 5.3 -> **4.9** | Individual spell overtuned (WR: 68.8%, Casts: 7037, mult: 0.928) |
| `LLF` | Light | Conditional Strike | 1.1 -> **0.8** (-27.3%) | 17.4 -> **23.7** | 20.2 -> **19.8** | Class Light overtuned (WR: 55.2%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 2571). Increasing spread: b -17.5%, n +36.0% |
| `LLW` | Light | Debuff / Control | 23.6 -> **23.1** (-2.1%) | - | 23.6 -> **23.1** | Class Light overtuned (WR: 55.2%, factor: 0.979) |
| `LLE` | Light | Setup - Weather | 40.6 -> **49.5** (+21.9%) | - | 40.6 -> **49.5** | Class Light overtuned (WR: 55.2%, factor: 0.979); Weather 'Sunny' appliers undertuned (WR: 19.1%, casts: 1865) |
| `LLL` | Light | Buff / Sustain | 22.5 -> **19.8** (-12.0%) | - | 22.5 -> **19.8** | Class Light overtuned (WR: 55.2%, factor: 0.979); Individual spell overtuned (WR: 75.4%, Casts: 2487, mult: 0.900) |
| `LLD` | Light | Ultimate | 12.4 -> **13.3** (+7.3%) | 21.8 -> **20.5** | 282.7 -> **285.9** | Class Light overtuned (WR: 55.2%, factor: 0.979); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 480, WR: 44.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 6.5 -> **5.5** (-15.4%) | 19.3 -> **26.4** | 132.0 -> **150.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1504). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 43.3%, Casts: 1504, mult: 1.023) |
| `DDE` | Dark | Setup - Weather | 34.8 -> **41.7** (+19.8%) | - | 34.8 -> **41.7** | Weather 'Darkness' appliers undertuned (WR: 24.4%, casts: 1735); Individual spell undertuned (WR: 24.3%, Casts: 1735, mult: 1.101) |
| `DDL` | Dark | Debuff / Control | 20.1 -> **18.9** (-6.0%) | - | 20.1 -> **18.9** | Individual spell overtuned (WR: 65.4%, Casts: 1865, mult: 0.943) |
| `DDD` | Dark | Debuff / Control | 18.2 -> **16.3** (-10.4%) | - | 18.2 -> **16.3** | Individual spell overtuned (WR: 76.2%, Casts: 1373, mult: 0.897) |
| `FWF` | Ghostfire | Debuff / Control | 17.5 -> **14.8** (-15.4%) | - | 17.5 -> **14.8** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Status 'Burning' appliers overtuned on own (WR: 62.1%) |
| `FWW` | Ghostfire | Debuff / Control | 14.3 -> **12.2** (-14.7%) | - | 14.3 -> **12.2** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Status 'Cursed' appliers overtuned on own (WR: 61.2%) |
| `FWE` | Ghostfire | Setup - Location | 39.1 -> **46.0** (+17.6%) | - | 39.1 -> **46.0** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Location 'Graveyard' appliers undertuned (WR: 24.3%, casts: 391) |
| `FWL` | Ghostfire | Debuff / Control | 35.4 -> **31.8** (-10.2%) | - | 35.4 -> **31.8** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Status 'Cursed' appliers overtuned on own (WR: 61.2%) |
| `FWD` | Ghostfire | Ultimate | 14.7 -> **11.5** (-21.8%) | 15.6 -> **20.4** | 244.0 -> **246.1** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Status 'Cursed' beneficiaries overtuned (WR: 54.3%) |
| `WFF` | Ghostfire | Conditional Strike | 7.7 -> **6.4** (-16.9%) | 20.5 -> **28.6** | 165.6 -> **189.4** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Status 'Bleeding' beneficiaries undertuned (WR: 45.0%) |
| `WFW` | Ghostfire | Debuff / Control | 25.2 -> **21.1** (-16.3%) | - | 25.2 -> **21.1** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Individual spell overtuned (WR: 85.2%, Casts: 3626, mult: 0.857) |
| `WFE` | Ghostfire | Debuff / Control | 12.4 -> **9.8** (-21.0%) | - | 12.4 -> **9.8** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Status 'Bleeding' appliers overtuned on own (WR: 78.9%) |
| `WFL` | Ghostfire | Buff / Sustain | 33.6 -> **34.3** (+2.1%) | - | 33.6 -> **34.3** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Individual spell undertuned (WR: 37.9%, Casts: 1363, mult: 1.044) |
| `WFD` | Ghostfire | Conditional Strike | 7.0 -> **6.1** (-12.9%) | 16.8 -> **23.0** | 124.6 -> **146.4** | Class Ghostfire overtuned (WR: 55.4%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 7703). Increasing spread: b -18.0%, n +37.0% |
| `FEF` | Beasts | Debuff / Control | 20.2 -> **19.8** (-2.0%) | - | 20.2 -> **19.8** | Class Beasts undertuned (WR: 39.9%, factor: 1.040); Individual spell overtuned (WR: 65.0%, Casts: 1092, mult: 0.944) |
| `FEW` | Beasts | Conditional Strike | 6.8 -> **6.2** (-8.8%) | 20.0 -> **28.0** | 142.8 -> **179.8** | Class Beasts undertuned (WR: 39.9%, factor: 1.040); Status 'Entangled' beneficiaries undertuned (WR: 40.0%) |
| `FEE` | Beasts | Buff / Sustain | 26.5 -> **27.6** (+4.2%) | - | 26.5 -> **27.6** | Class Beasts undertuned (WR: 39.9%, factor: 1.040) |
| `FEL` | Beasts | Buff / Sustain | 36.7 -> **45.1** (+22.9%) | - | 36.7 -> **45.1** | Class Beasts undertuned (WR: 39.9%, factor: 1.040); Individual spell undertuned (WR: 6.4%, Casts: 7057, mult: 1.180) |
| `FED` | Beasts | Conditional Strike | 4.8 -> **4.5** (-6.2%) | 2.5 -> **3.2** | 16.8 -> **18.9** | Class Beasts undertuned (WR: 39.9%, factor: 1.040); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 4299). Increasing spread: b -14.5%, n +29.8% |
| `EFF` | Beasts | Debuff / Control | 8.8 -> **8.4** (-4.5%) | 18.4 -> **25.2** | 170.7 -> **220.1** | Class Beasts undertuned (WR: 39.9%, factor: 1.040); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 237). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 25.6 -> **27.0** (+5.5%) | - | 25.6 -> **27.0** | Class Beasts undertuned (WR: 39.9%, factor: 1.040); Individual spell undertuned (WR: 45.4%, Casts: 440, mult: 1.015) |
| `EFE` | Beasts | Buff / Sustain | 29.7 -> **27.7** (-6.7%) | - | 29.7 -> **27.7** | Class Beasts undertuned (WR: 39.9%, factor: 1.040); Individual spell overtuned (WR: 76.2%, Casts: 236, mult: 0.897) |
| `EFL` | Beasts | Buff / Sustain | 10.2 -> **9.0** (-11.8%) | - | 10.2 -> **9.0** | Class Beasts undertuned (WR: 39.9%, factor: 1.040); Individual spell overtuned (WR: 88.2%, Casts: 4190, mult: 0.844) |
| `EFD` | Beasts | Ultimate | 12.6 -> **10.8** (-14.3%) | 27.1 -> **39.8** | 354.1 -> **440.6** | Class Beasts undertuned (WR: 39.9%, factor: 1.040); Status 'Entangled' beneficiaries undertuned (WR: 40.0%) |
| `FLF` | Lightning | Conditional Strike | 6.8 -> **6.1** (-10.3%) | 19.4 -> **28.2** | 138.7 -> **178.1** | Status 'Stunned' beneficiaries undertuned (WR: 33.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 4414). Increasing spread: b -17.8%, n +36.6% |
| `FLW` | Lightning | Debuff / Control | 33.3 -> **30.4** (-8.7%) | - | 33.3 -> **30.4** | Individual spell overtuned (WR: 72.8%, Casts: 4499, mult: 0.912) |
| `FLE` | Lightning | Setup - Weather | 31.6 -> **25.3** (-19.9%) | - | 31.6 -> **25.3** | Weather 'Storming' appliers overtuned on own (WR: 77.7%); Individual spell overtuned (WR: 78.6%, Casts: 77, mult: 0.886) |
| `FLL` | Lightning | Buff / Sustain | 31.5 -> **33.4** (+6.0%) | - | 31.5 -> **33.4** | Individual spell undertuned (WR: 33.8%, Casts: 1120, mult: 1.061) |
| `FLD` | Lightning | Ultimate | 16.7 -> **18.3** (+9.6%) | 16.8 -> **17.1** | 297.3 -> **331.2** | Status 'Stunned' beneficiaries undertuned (WR: 33.8%); Weather 'Storming' beneficiaries undertuned (WR: 45.2%) |
| `LFF` | Lightning | Conditional Strike | 7.2 -> **6.6** (-8.3%) | 18.4 -> **25.2** | 139.7 -> **172.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1806). Increasing spread: b -18.0%, n +36.9%; Individual spell undertuned (WR: 20.2%, Casts: 1806, mult: 1.119) |
| `LFW` | Lightning | Buff / Sustain | 29.2 -> **28.0** (-4.1%) | - | 29.2 -> **28.0** | Individual spell overtuned (WR: 61.4%, Casts: 2106, mult: 0.959) |
| `LFE` | Lightning | Debuff / Control | 30.7 -> **28.0** (-8.8%) | - | 30.7 -> **28.0** | Individual spell overtuned (WR: 72.6%, Casts: 836, mult: 0.912) |
| `LFL` | Lightning | Debuff / Control | 13.5 -> **11.0** (-18.5%) | 14.2 -> **19.2** | 205.2 -> **222.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.1% vs 30% floor, Casts: 3960). Increasing spread: b -17.2%, n +35.2%; Individual spell overtuned (WR: 55.6%, Casts: 3960, mult: 0.981) |
| `LFD` | Lightning | Conditional Strike | 6.9 -> **6.6** (-4.3%) | 26.4 -> **32.2** | 189.1 -> **219.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.8% vs 30% floor, Casts: 1732). Increasing spread: b -10.9%, n +22.1%; Individual spell undertuned (WR: 29.5%, Casts: 1732, mult: 1.079) |
| `FDF` | Blood | Conditional Strike | 7.3 -> **5.5** (-24.7%) | 19.3 -> **26.4** | 148.2 -> **150.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1511). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 69.3%, Casts: 1511, mult: 0.926) |
| `FDW` | Blood | Direct Damage | 76.6 -> **75.0** (-2.1%) | - | 76.6 -> **75.0** | Individual spell overtuned (WR: 56.1%, Casts: 416, mult: 0.979) |
| `FDE` | Blood | Setup - Weather | 31.2 -> **36.2** (+16.0%) | - | 31.2 -> **36.2** | Individual spell undertuned (WR: 10.7%, Casts: 3623, mult: 1.161) |
| `FDL` | Blood | Debuff / Control | 13.4 -> **10.3** (-23.1%) | - | 13.4 -> **10.3** | Status 'Bleeding' appliers overtuned on own (WR: 78.9%); Individual spell overtuned (WR: 85.6%, Casts: 3649, mult: 0.855) |
| `FDD` | Blood | Ultimate | 15.3 -> **17.5** (+14.4%) | 15.2 -> **14.3** | 247.9 -> **267.8** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1982, WR: 33.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 33.6%, Casts: 1982, mult: 1.062) |
| `DFF` | Blood | Conditional Strike | 7.9 -> **6.8** (-13.9%) | 18.8 -> **26.2** | 156.4 -> **185.0** | Status 'Bleeding' beneficiaries undertuned (WR: 45.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 982). Increasing spread: b -17.8%, n +36.5% |
| `DFW` | Blood | Debuff / Control | 10.3 -> **8.0** (-22.3%) | - | 10.3 -> **8.0** | Status 'Bleeding' appliers overtuned on own (WR: 78.9%); Individual spell overtuned (WR: 85.1%, Casts: 1068, mult: 0.858) |
| `DFE` | Blood | Buff / Sustain | 62.8 -> **71.2** (+13.4%) | - | 62.8 -> **71.2** | Individual spell undertuned (WR: 16.8%, Casts: 1927, mult: 1.134) |
| `DFL` | Blood | Buff / Sustain | 23.3 -> **22.8** (-2.1%) | - | 23.3 -> **22.8** | Individual spell overtuned (WR: 56.7%, Casts: 2121, mult: 0.977) |
| `DFD` | Blood | Conditional Strike | 54.4 -> **59.5** (+9.4%) | 0.3 -> **0.2** | 70.7 -> **71.4** | Condition triggers excessively (N=1 conditions, Trigger Rate: 82.7% vs 55% ceiling, WR: 74.8%). Compressing spread: b +21.1%, n -27.8%; Individual spell overtuned (WR: 74.8%, Casts: 3358, mult: 0.903) |
| `WEF` | Plants | Conditional Strike | 7.4 -> **6.4** (-13.5%) | 18.6 -> **26.5** | 145.0 -> **176.0** | Location 'Jungle' beneficiaries undertuned (WR: 40.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 688). Increasing spread: b -18.0%, n +37.0% |
| `WEW` | Plants | Debuff / Control | 36.0 -> **34.6** (-3.9%) | - | 36.0 -> **34.6** | Individual spell overtuned (WR: 61.0%, Casts: 47, mult: 0.961) |
| `WEE` | Plants | Setup - Location | 36.9 -> **42.2** (+14.4%) | - | 36.9 -> **42.2** | Location 'Jungle' appliers undertuned (WR: 31.1%, casts: 832); Individual spell undertuned (WR: 31.0%, Casts: 832, mult: 1.072) |
| `WEL` | Plants | Debuff / Control | 30.2 -> **31.7** (+5.0%) | - | 30.2 -> **31.7** | Status 'Entangled' appliers undertuned (WR: 43.0%, casts: 3517); Individual spell undertuned (WR: 43.0%, Casts: 3517, mult: 1.024) |
| `WED` | Plants | Conditional Strike | 13.2 -> **14.6** (+10.6%) | 9.1 -> **8.6** | 133.3 -> **140.2** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1749, WR: 43.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 43.0%, Casts: 1749, mult: 1.024) |
| `EWF` | Plants | Buff / Sustain | 7.7 -> **6.4** (-16.9%) | 14.9 -> **20.3** | 122.4 -> **136.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 8500). Increasing spread: b -17.5%, n +36.0% |
| `EWW` | Plants | Debuff / Control | 11.8 -> **9.8** (-16.9%) | - | 11.8 -> **9.8** | Individual spell overtuned (WR: 90.5%, Casts: 4269, mult: 0.834) |
| `EWL` | Plants | Debuff / Control | 48.4 -> **44.8** (-7.4%) | - | 48.4 -> **44.8** | Individual spell overtuned (WR: 69.5%, Casts: 178, mult: 0.926) |
| `EWD` | Plants | Conditional Strike | 3.5 -> **2.7** (-22.9%) | 19.3 -> **27.5** | 71.0 -> **77.0** | Status 'Bleeding' appliers overtuned on own (WR: 78.9%); Status 'Entangled' beneficiaries undertuned (WR: 40.0%) |
| `WLF` | Fey | Conditional Strike | 9.2 -> **7.9** (-14.1%) | 16.6 -> **22.3** | 161.9 -> **184.1** | Class Fey undertuned (WR: 38.7%, factor: 1.045); Status 'Cursed' beneficiaries overtuned (WR: 54.3%) |
| `WLW` | Fey | Debuff / Control | 33.1 -> **32.5** (-1.8%) | - | 33.1 -> **32.5** | Class Fey undertuned (WR: 38.7%, factor: 1.045); Status 'Cursed' appliers overtuned on own (WR: 61.2%) |
| `WLE` | Fey | Setup - Location | 58.6 -> **78.3** (+33.6%) | - | 58.6 -> **78.3** | Class Fey undertuned (WR: 38.7%, factor: 1.045); Location 'Enchanted Forest' appliers undertuned (WR: 15.0%, casts: 3616) |
| `WLL` | Fey | Direct Damage | 56.9 -> **54.5** (-4.2%) | - | 56.9 -> **54.5** | Class Fey undertuned (WR: 38.7%, factor: 1.045); Individual spell overtuned (WR: 71.8%, Casts: 3124, mult: 0.916) |
| `WLD` | Fey | Ultimate | 25.7 -> **21.7** (-15.6%) | 11.5 -> **15.8** | 321.2 -> **364.6** | Class Fey undertuned (WR: 38.7%, factor: 1.045); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 5110). Increasing spread: b -18.0%, n +37.0% |
| `LWF` | Fey | Debuff / Control | 14.1 -> **13.4** (-5.0%) | 16.9 -> **23.0** | 252.4 -> **321.6** | Class Fey undertuned (WR: 38.7%, factor: 1.045); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 498). Increasing spread: b -17.5%, n +36.0% |
| `LWW` | Fey | Debuff / Control | 48.5 -> **57.1** (+17.7%) | - | 48.5 -> **57.1** | Class Fey undertuned (WR: 38.7%, factor: 1.045); Individual spell undertuned (WR: 18.6%, Casts: 5515, mult: 1.126) |
| `LWL` | Fey | Debuff / Control | 47.0 -> **45.6** (-3.0%) | - | 47.0 -> **45.6** | Class Fey undertuned (WR: 38.7%, factor: 1.045); Individual spell overtuned (WR: 68.8%, Casts: 446, mult: 0.929) |
| `LWD` | Fey | Conditional Strike | 8.6 -> **8.4** (-2.3%) | 19.3 -> **26.4** | 174.6 -> **230.2** | Class Fey undertuned (WR: 38.7%, factor: 1.045); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2066). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 9.0 -> **8.1** (-10.0%) | 16.2 -> **23.7** | 154.8 -> **200.1** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Weather 'Raining' beneficiaries undertuned (WR: 33.0%) |
| `WDW` | Ice | Buff / Sustain | 20.9 -> **25.0** (+19.6%) | - | 20.9 -> **25.0** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Status 'Frosty' appliers undertuned (WR: 44.9%, casts: 8710) |
| `WDE` | Ice | Setup - Weather | 39.6 -> **44.0** (+11.1%) | - | 39.6 -> **44.0** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Individual spell undertuned (WR: 30.4%, Casts: 1696, mult: 1.075) |
| `WDL` | Ice | Debuff / Control | 49.4 -> **52.0** (+5.3%) | - | 49.4 -> **52.0** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Status 'Frosty' appliers undertuned (WR: 44.9%, casts: 8710) |
| `WDD` | Ice | Ultimate | 19.4 -> **22.0** (+13.4%) | 15.8 -> **15.4** | 325.9 -> **360.8** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Weather 'Blizzard' beneficiaries undertuned (WR: 45.1%) |
| `DWF` | Ice | Debuff / Control | 50.9 -> **53.5** (+5.1%) | - | 50.9 -> **53.5** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Status 'Frosty' appliers undertuned (WR: 44.9%, casts: 8710) |
| `DWW` | Ice | Debuff / Control | 38.7 -> **38.1** (-1.6%) | - | 38.7 -> **38.1** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Individual spell overtuned (WR: 62.9%, Casts: 4136, mult: 0.952) |
| `DWE` | Ice | Setup - Location | 26.7 -> **33.4** (+25.1%) | - | 26.7 -> **33.4** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Location 'Tundra' appliers undertuned (WR: 23.1%, casts: 2300) |
| `DWL` | Ice | Debuff / Control | 52.4 -> **52.9** (+1.0%) | - | 52.4 -> **52.9** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Status 'Frosty' appliers undertuned (WR: 44.9%, casts: 8710) |
| `DWD` | Ice | Conditional Strike | 12.6 -> **11.4** (-9.5%) | 14.1 -> **20.0** | 190.3 -> **239.4** | Class Ice undertuned (WR: 41.7%, factor: 1.033); Status 'Frosty' beneficiaries undertuned (WR: 36.9%) |
| `ELF` | Wind | Conditional Strike | 14.4 -> **11.7** (-18.8%) | 19.6 -> **27.3** | 296.6 -> **331.1** | Status 'Bleeding' beneficiaries undertuned (WR: 45.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 942). Increasing spread: b -17.8%, n +36.6% |
| `ELE` | Wind | Setup - Weather | 24.4 -> **26.1** (+7.0%) | - | 24.4 -> **26.1** | Individual spell undertuned (WR: 31.6%, Casts: 1076, mult: 1.070) |
| `ELL` | Wind | Buff / Sustain | 44.4 -> **46.8** (+5.4%) | - | 44.4 -> **46.8** | Individual spell undertuned (WR: 35.3%, Casts: 322, mult: 1.054) |
| `ELD` | Wind | Conditional Strike | 6.7 -> **6.3** (-6.0%) | 16.3 -> **23.3** | 115.9 -> **153.1** | Weather 'Raining' beneficiaries undertuned (WR: 33.0%); Weather 'Blizzard' appliers undertuned (WR: 33.8%, casts: 170) |
| `LEF` | Wind | Conditional Strike | 8.1 -> **6.9** (-14.8%) | 16.4 -> **22.3** | 140.9 -> **160.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.0% vs 30% floor, Casts: 4008). Increasing spread: b -17.6%, n +36.2%; Individual spell undertuned (WR: 40.5%, Casts: 4008, mult: 1.034) |
| `LEW` | Wind | Debuff / Control | 46.3 -> **42.3** (-8.6%) | - | 46.3 -> **42.3** | Individual spell overtuned (WR: 72.2%, Casts: 8342, mult: 0.914) |
| `LEE` | Wind | Setup - Weather | 19.9 -> **21.9** (+10.1%) | - | 19.9 -> **21.9** | Individual spell undertuned (WR: 24.3%, Casts: 3384, mult: 1.101) |
| `LEL` | Wind | Buff / Sustain | 48.6 -> **54.4** (+11.9%) | - | 48.6 -> **54.4** | Individual spell undertuned (WR: 20.3%, Casts: 766, mult: 1.118) |
| `EDF` | Poison | Conditional Strike | 8.9 -> **6.8** (-23.6%) | 16.8 -> **22.1** | 158.4 -> **157.1** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.5% vs 30% floor, Casts: 2440). Increasing spread: b -15.4%, n +31.6% |
| `EDW` | Poison | Debuff / Control | 20.5 -> **16.2** (-21.0%) | - | 20.5 -> **16.2** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Individual spell overtuned (WR: 87.7%, Casts: 1829, mult: 0.846) |
| `EDE` | Poison | Setup - Location | 26.7 -> **29.2** (+9.4%) | - | 26.7 -> **29.2** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Location 'Swamp' appliers undertuned (WR: 28.1%, casts: 179) |
| `EDL` | Poison | Debuff / Control | 7.3 -> **5.7** (-21.9%) | - | 7.3 -> **5.7** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Individual spell overtuned (WR: 91.2%, Casts: 3161, mult: 0.830) |
| `EDD` | Poison | Ultimate | 23.0 -> **17.6** (-23.5%) | 14.3 -> **20.0** | 351.9 -> **369.6** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Status 'Bleeding' beneficiaries undertuned (WR: 45.0%) |
| `DEF` | Poison | Conditional Strike | 24.5 -> **21.1** (-13.9%) | 2.7 -> **3.1** | 90.7 -> **86.5** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 25.9% vs 30% floor, Casts: 1770). Increasing spread: b -7.6%, n +15.4% |
| `DEW` | Poison | Debuff / Control | 19.0 -> **15.7** (-17.4%) | - | 19.0 -> **15.7** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Individual spell overtuned (WR: 79.4%, Casts: 6188, mult: 0.883) |
| `DEE` | Poison | Debuff / Control | 21.8 -> **20.9** (-4.1%) | - | 21.8 -> **20.9** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Individual spell undertuned (WR: 42.1%, Casts: 2841, mult: 1.028) |
| `DEL` | Poison | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 18.9 -> **26.2** | 15.9 -> **19.0** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Status 'Bleeding' beneficiaries undertuned (WR: 45.0%) |
| `DED` | Poison | Debuff / Control | 25.8 -> **23.4** (-9.3%) | - | 25.8 -> **23.4** | Class Poison overtuned (WR: 66.5%, factor: 0.934); Individual spell overtuned (WR: 58.7%, Casts: 3140, mult: 0.969) |
| `LDF` | Cosmic | Debuff / Control | 37.9 -> **36.8** (-2.9%) | - | 37.9 -> **36.8** | Individual spell overtuned (WR: 58.3%, Casts: 2392, mult: 0.971) |
| `LDE` | Cosmic | Setup - Location | 20.7 -> **21.0** (+1.4%) | - | 20.7 -> **21.0** | Individual spell undertuned (WR: 46.3%, Casts: 135, mult: 1.012) |
| `LDL` | Cosmic | Conditional Strike | 7.7 -> **6.5** (-15.6%) | 16.4 -> **22.4** | 134.0 -> **152.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 2210). Increasing spread: b -17.9%, n +36.8%; Individual spell undertuned (WR: 42.3%, Casts: 2210, mult: 1.027) |
| `LDD` | Cosmic | Ultimate | 12.6 -> **14.6** (+15.9%) | 22.6 -> **21.2** | 297.4 -> **324.1** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 362, WR: 31.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 31.0%, Casts: 362, mult: 1.072) |
| `DLF` | Cosmic | Conditional Strike | 9.1 -> **7.5** (-17.6%) | 17.3 -> **23.4** | 166.5 -> **183.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 6006). Increasing spread: b -17.3%, n +35.5% |
| `DLW` | Cosmic | Direct Damage | 49.4 -> **44.8** (-9.3%) | - | 49.4 -> **44.8** | Individual spell overtuned (WR: 73.7%, Casts: 4304, mult: 0.908) |
| `DLE` | Cosmic | Direct Damage | 43.8 -> **50.7** (+15.8%) | - | 43.8 -> **50.7** | Individual spell undertuned (WR: 11.3%, Casts: 1622, mult: 1.159) |
| `DLL` | Cosmic | Conditional Strike | 11.9 -> **10.9** (-8.4%) | 15.2 -> **20.7** | 192.8 -> **236.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.0% vs 30% floor, Casts: 821). Increasing spread: b -17.6%, n +36.2%; Individual spell undertuned (WR: 22.3%, Casts: 821, mult: 1.110) |
