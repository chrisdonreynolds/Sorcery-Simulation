# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T23:23:10Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 469.1s  
**Total Spells Tuned:** 94 / 125  

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
| **Dark** | 9,958 | 54.4% | 54.4% | 12.3 | Overtuned ⚠️ |
| **Poison** | 22,519 | 54.3% | 54.3% | 9.2 | Overtuned ⚠️ |
| **Plants** | 21,473 | 53.8% | 53.8% | 9.3 | Overtuned ⚠️ |
| **Blood** | 22,119 | 53.5% | 53.5% | 12.3 | Balanced ✅ |
| **Earth** | 9,957 | 52.5% | 52.5% | 19.4 | Balanced ✅ |
| **Light** | 10,657 | 51.8% | 51.8% | 7.0 | Balanced ✅ |
| **Fire** | 10,109 | 51.3% | 51.3% | 14.0 | Balanced ✅ |
| **Ghostfire** | 22,879 | 50.7% | 50.7% | 15.2 | Balanced ✅ |
| **Beasts** | 19,520 | 49.3% | 49.3% | 7.4 | Balanced ✅ |
| **Wind** | 20,247 | 49.0% | 49.0% | 7.5 | Balanced ✅ |
| **Cosmic** | 18,809 | 48.7% | 48.7% | 14.8 | Balanced ✅ |
| **Water** | 11,048 | 47.3% | 47.3% | 9.3 | Balanced ✅ |
| **Lightning** | 23,757 | 46.9% | 46.9% | 9.8 | Balanced ✅ |
| **Ice** | 21,346 | 46.6% | 46.6% | 12.3 | Balanced ✅ |
| **Fey** | 20,996 | 46.2% | 46.2% | 8.4 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 8,399 (48.3%) | 3,530 (52.7%) | 22.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,659 (49.1%) | 4,382 (54.6%) | 5.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,426 (59.6%) | 6,189 (49.6%) | 11.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,959 (68.0%) | 10,151 (45.8%) | 4.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,561 (48.3%) | 5,177 (44.7%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,362 (51.4%) | 5,733 (42.4%) | 1.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,007 (33.7%) | 5,329 (44.3%) | 5.1% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 44.3 -> **42.8** (-3.4%) | - | 44.3 -> **42.8** | Status 'Burning' appliers overtuned on own (WR: 59.6%) |
| `FFL` | Fire | Debuff / Control | 6.5 -> **6.0** (-7.7%) | - | 6.5 -> **6.0** | Status 'Burning' appliers overtuned on own (WR: 59.6%); Individual spell overtuned (WR: 63.0%, Casts: 1747, mult: 0.952) |
| `FFD` | Fire | Conditional Strike | 5.7 -> **4.9** (-14.0%) | 29.8 -> **38.4** | 175.6 -> **193.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.9% vs 30% floor, Casts: 2216). Increasing spread: b -14.0%, n +28.8% |
| `WWF` | Water | Conditional Strike | 11.3 -> **9.8** (-13.3%) | 23.8 -> **30.1** | 280.2 -> **304.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.8% vs 30% floor, Casts: 2434). Increasing spread: b -12.9%, n +26.3% |
| `WWE` | Water | Setup - Weather | 29.8 -> **33.4** (+12.1%) | - | 29.8 -> **33.4** | Weather 'Raining' appliers undertuned (WR: 33.7%, casts: 2007); Individual spell undertuned (WR: 33.6%, Casts: 2007, mult: 1.061) |
| `EEF` | Earth | Conditional Strike | 18.7 -> **16.4** (-12.3%) | 8.6 -> **10.1** | 179.5 -> **182.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 23.1% vs 30% floor, Casts: 1531). Increasing spread: b -8.8%, n +17.7%; Individual spell overtuned (WR: 61.5%, Casts: 1531, mult: 0.958) |
| `EEW` | Earth | Buff / Sustain | 30.0 -> **29.4** (-2.0%) | - | 30.0 -> **29.4** | Individual spell overtuned (WR: 56.1%, Casts: 1730, mult: 0.979) |
| `EED` | Earth | Direct Damage | 6.9 -> **7.1** (+2.9%) | - | 6.9 -> **7.1** | Individual spell undertuned (WR: 41.4%, Casts: 1741, mult: 1.030) |
| `LLF` | Light | Conditional Strike | 4.0 -> **3.3** (-17.5%) | 33.5 -> **44.4** | 138.0 -> **149.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.3% vs 30% floor, Casts: 3351). Increasing spread: b -15.9%, n +32.6%; Individual spell overtuned (WR: 55.8%, Casts: 3351, mult: 0.980) |
| `LLW` | Light | Debuff / Control | 39.2 -> **39.8** (+1.5%) | - | 39.2 -> **39.8** | Individual spell undertuned (WR: 45.1%, Casts: 2482, mult: 1.016) |
| `LLL` | Light | Buff / Sustain | 25.6 -> **24.3** (-5.1%) | - | 25.6 -> **24.3** | Individual spell overtuned (WR: 63.3%, Casts: 1493, mult: 0.951) |
| `LLD` | Light | Ultimate | 31.9 -> **34.9** (+9.4%) | 17.7 -> **16.3** | 596.5 -> **603.8** | Weather 'Sunny' beneficiaries overtuned (WR: 54.6%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1672, WR: 46.1%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 3.7 -> **3.0** (-18.9%) | 49.6 -> **67.9** | 187.2 -> **206.7** | Class Dark overtuned (WR: 54.4%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1337). Increasing spread: b -18.0%, n +36.9% |
| `DDW` | Dark | Debuff / Control | 53.8 -> **52.9** (-1.7%) | - | 53.8 -> **52.9** | Class Dark overtuned (WR: 54.4%, factor: 0.983) |
| `DDE` | Dark | Setup - Weather | 50.1 -> **54.8** (+9.4%) | - | 50.1 -> **54.8** | Class Dark overtuned (WR: 54.4%, factor: 0.983); Weather 'Darkness' appliers overtuned on own (WR: 54.8%) |
| `DDL` | Dark | Debuff / Control | 27.5 -> **26.5** (-3.6%) | - | 27.5 -> **26.5** | Class Dark overtuned (WR: 54.4%, factor: 0.983); Individual spell overtuned (WR: 55.7%, Casts: 3503, mult: 0.981) |
| `DDD` | Dark | Debuff / Control | 27.0 -> **25.7** (-4.8%) | - | 27.0 -> **25.7** | Class Dark overtuned (WR: 54.4%, factor: 0.983); Individual spell overtuned (WR: 59.2%, Casts: 1754, mult: 0.967) |
| `FWF` | Ghostfire | Debuff / Control | 33.2 -> **30.3** (-8.7%) | - | 33.2 -> **30.3** | Status 'Burning' appliers overtuned on own (WR: 59.6%); Individual spell overtuned (WR: 64.6%, Casts: 2128, mult: 0.946) |
| `FWW` | Ghostfire | Debuff / Control | 29.4 -> **29.9** (+1.7%) | - | 29.4 -> **29.9** | Individual spell undertuned (WR: 44.7%, Casts: 2116, mult: 1.018) |
| `FWE` | Ghostfire | Setup - Location | 65.1 -> **67.4** (+3.5%) | - | 65.1 -> **67.4** | Location 'Graveyard' appliers undertuned (WR: 44.9%, casts: 2868); Individual spell undertuned (WR: 44.9%, Casts: 2868, mult: 1.017) |
| `FWL` | Ghostfire | Debuff / Control | 77.4 -> **75.9** (-1.9%) | - | 77.4 -> **75.9** | Individual spell overtuned (WR: 55.6%, Casts: 2588, mult: 0.981) |
| `FWD` | Ghostfire | Ultimate | 38.8 -> **44.0** (+13.4%) | 19.3 -> **19.6** | 787.6 -> **906.4** | Status 'Cursed' beneficiaries undertuned (WR: 43.3%); Location 'Graveyard' beneficiaries undertuned (WR: 36.5%) |
| `WFF` | Ghostfire | Conditional Strike | 5.6 -> **4.9** (-12.5%) | 30.1 -> **40.0** | 174.2 -> **200.9** | Status 'Bleeding' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.5% vs 30% floor, Casts: 2716). Increasing spread: b -15.0%, n +30.8% |
| `WFW` | Ghostfire | Debuff / Control | 28.6 -> **27.7** (-3.1%) | - | 28.6 -> **27.7** | Individual spell overtuned (WR: 58.7%, Casts: 2790, mult: 0.969) |
| `WFE` | Ghostfire | Debuff / Control | 34.2 -> **33.7** (-1.5%) | - | 34.2 -> **33.7** | Status 'Bleeding' appliers overtuned on own (WR: 68.0%); Buffed setup spell [WFE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `WFL` | Ghostfire | Buff / Sustain | 39.1 -> **41.4** (+5.9%) | - | 39.1 -> **41.4** | Individual spell undertuned (WR: 34.2%, Casts: 986, mult: 1.059) |
| `WFD` | Ghostfire | Conditional Strike | 6.6 -> **5.7** (-13.6%) | 27.5 -> **35.3** | 188.1 -> **206.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.2% vs 30% floor, Casts: 2189). Increasing spread: b -13.9%, n +28.5% |
| `FEW` | Beasts | Conditional Strike | 3.8 -> **3.1** (-18.4%) | 48.2 -> **67.7** | 187.0 -> **213.0** | Status 'Entangled' beneficiaries undertuned (WR: 42.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 1124). Increasing spread: b -17.6%, n +36.3% |
| `FEE` | Beasts | Buff / Sustain | 27.1 -> **27.6** (+1.8%) | - | 27.1 -> **27.6** | Individual spell undertuned (WR: 44.1%, Casts: 2322, mult: 1.020) |
| `FEL` | Beasts | Buff / Sustain | 29.2 -> **29.9** (+2.4%) | - | 29.2 -> **29.9** | Individual spell undertuned (WR: 42.8%, Casts: 2248, mult: 1.025) |
| `FED` | Beasts | Conditional Strike | 9.7 -> **10.0** (+3.1%) | 1.5 -> **1.5** | 24.2 -> **25.0** | Condition triggers excessively (N=1 conditions, Trigger Rate: 57.6% vs 55% ceiling, WR: 52.4%). Compressing spread: b +6.6%, n -9.9% |
| `EFF` | Beasts | Debuff / Control | 4.7 -> **3.9** (-17.0%) | 45.6 -> **61.7** | 219.0 -> **244.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 2112). Increasing spread: b -17.2%, n +35.4% |
| `EFL` | Beasts | Buff / Sustain | 8.7 -> **7.4** (-14.9%) | - | 8.7 -> **7.4** | Individual spell overtuned (WR: 86.1%, Casts: 1590, mult: 0.853) |
| `EFD` | Beasts | Ultimate | 29.4 -> **33.4** (+13.6%) | 28.9 -> **28.9** | 879.1 -> **998.7** | Status 'Entangled' beneficiaries undertuned (WR: 42.4%); Location 'Jungle' beneficiaries undertuned (WR: 41.9%) |
| `FLF` | Lightning | Conditional Strike | 4.0 -> **3.3** (-17.5%) | 58.1 -> **81.1** | 236.4 -> **270.9** | Status 'Stunned' beneficiaries undertuned (WR: 44.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 2627). Increasing spread: b -17.8%, n +36.6% |
| `FLE` | Lightning | Setup - Weather | 29.0 -> **30.0** (+3.4%) | - | 29.0 -> **30.0** | Weather 'Storming' appliers undertuned (WR: 45.1%, casts: 2666); Individual spell undertuned (WR: 45.1%, Casts: 2666, mult: 1.016) |
| `FLD` | Lightning | Ultimate | 55.3 -> **60.8** (+9.9%) | 8.8 -> **8.6** | 541.9 -> **583.7** | Status 'Stunned' beneficiaries undertuned (WR: 44.7%); Weather 'Storming' beneficiaries undertuned (WR: 44.7%) |
| `LFF` | Lightning | Conditional Strike | 4.5 -> **3.7** (-17.8%) | 42.4 -> **57.3** | 195.3 -> **215.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.1% vs 30% floor, Casts: 1913). Increasing spread: b -17.2%, n +35.3% |
| `LFL` | Lightning | Debuff / Control | 25.1 -> **21.5** (-14.3%) | 24.5 -> **31.7** | 640.1 -> **703.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.0% vs 30% floor, Casts: 2303). Increasing spread: b -14.4%, n +29.5% |
| `LFD` | Lightning | Conditional Strike | 7.7 -> **6.8** (-11.7%) | 43.1 -> **56.1** | 339.6 -> **388.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 3300). Increasing spread: b -14.7%, n +30.2%; Individual spell undertuned (WR: 40.1%, Casts: 3300, mult: 1.035) |
| `FDF` | Blood | Conditional Strike | 4.0 -> **3.4** (-15.0%) | 49.6 -> **68.0** | 202.4 -> **234.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2486). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 43.5%, Casts: 2486, mult: 1.022) |
| `FDW` | Blood | Direct Damage | 63.3 -> **66.0** (+4.3%) | - | 63.3 -> **66.0** | Individual spell undertuned (WR: 38.4%, Casts: 1148, mult: 1.042) |
| `FDE` | Blood | Setup - Weather | 21.1 -> **21.9** (+3.8%) | - | 21.1 -> **21.9** | Individual spell undertuned (WR: 40.1%, Casts: 2657, mult: 1.036) |
| `FDL` | Blood | Debuff / Control | 25.4 -> **25.0** (-1.6%) | - | 25.4 -> **25.0** | Status 'Bleeding' appliers overtuned on own (WR: 68.0%); Buffed setup spell [FDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `FDD` | Blood | Ultimate | 41.9 -> **45.3** (+8.1%) | 8.0 -> **7.5** | 377.1 -> **385.0** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 1756, WR: 47.1%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 4.9 -> **4.1** (-16.3%) | 30.0 -> **40.1** | 151.9 -> **168.5** | Status 'Bleeding' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 1722). Increasing spread: b -15.3%, n +31.4% |
| `DFW` | Blood | Debuff / Control | 23.9 -> **23.1** (-3.3%) | - | 23.9 -> **23.1** | Status 'Bleeding' appliers overtuned on own (WR: 68.0%); Buffed setup spell [DFW] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `DFE` | Blood | Buff / Sustain | 37.8 -> **39.4** (+4.2%) | - | 37.8 -> **39.4** | Individual spell undertuned (WR: 38.6%, Casts: 2344, mult: 1.041) |
| `DFD` | Blood | Conditional Strike | 85.5 -> **97.6** (+14.2%) | 0.2 -> **0.1** | 102.6 -> **107.4** | Condition triggers excessively (N=1 conditions, Trigger Rate: 96.3% vs 55% ceiling, WR: 57.1%). Compressing spread: b +17.0%, n -25.5%; Individual spell overtuned (WR: 57.1%, Casts: 2190, mult: 0.976) |
| `WEF` | Plants | Conditional Strike | 6.4 -> **5.4** (-15.6%) | 22.5 -> **29.9** | 150.4 -> **166.9** | Class Plants overtuned (WR: 53.8%, factor: 0.985); Location 'Jungle' beneficiaries undertuned (WR: 41.9%) |
| `WEW` | Plants | Debuff / Control | 100.2 -> **112.0** (+11.8%) | - | 100.2 -> **112.0** | Class Plants overtuned (WR: 53.8%, factor: 0.985); Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WEE` | Plants | Setup - Location | 23.2 -> **23.6** (+1.7%) | - | 23.2 -> **23.6** | Class Plants overtuned (WR: 53.8%, factor: 0.985); Location 'Jungle' appliers undertuned (WR: 45.2%, casts: 2445) |
| `WEL` | Plants | Debuff / Control | 41.0 -> **40.4** (-1.5%) | - | 41.0 -> **40.4** | Class Plants overtuned (WR: 53.8%, factor: 0.985) |
| `WED` | Plants | Conditional Strike | 9.4 -> **10.0** (+6.4%) | 20.4 -> **19.2** | 201.2 -> **202.0** | Class Plants overtuned (WR: 53.8%, factor: 0.985); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.6% vs 8% floor, Casts: 1736, WR: 46.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 6.5 -> **5.3** (-18.5%) | 20.1 -> **25.7** | 137.2 -> **141.5** | Class Plants overtuned (WR: 53.8%, factor: 0.985); Weather 'Sunny' beneficiaries overtuned (WR: 54.6%) |
| `EWW` | Plants | Debuff / Control | 11.4 -> **9.5** (-16.7%) | - | 11.4 -> **9.5** | Class Plants overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 86.7%, Casts: 1862, mult: 0.851) |
| `EWL` | Plants | Debuff / Control | 63.9 -> **62.9** (-1.6%) | - | 63.9 -> **62.9** | Class Plants overtuned (WR: 53.8%, factor: 0.985) |
| `EWD` | Plants | Conditional Strike | 13.8 -> **14.8** (+7.2%) | 44.1 -> **60.6** | 622.4 -> **911.7** | Class Plants overtuned (WR: 53.8%, factor: 0.985); Status 'Bleeding' appliers overtuned on own (WR: 68.0%) |
| `WLF` | Fey | Conditional Strike | 5.6 -> **4.8** (-14.3%) | 39.1 -> **53.0** | 224.6 -> **259.2** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Status 'Cursed' beneficiaries undertuned (WR: 43.3%) |
| `WLW` | Fey | Debuff / Control | 51.1 -> **51.9** (+1.6%) | - | 51.1 -> **51.9** | Class Fey undertuned (WR: 46.2%, factor: 1.015) |
| `WLE` | Fey | Setup - Location | 75.0 -> **87.5** (+16.7%) | - | 75.0 -> **87.5** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 59.8 -> **59.4** (-0.7%) | - | 59.8 -> **59.4** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Individual spell overtuned (WR: 56.0%, Casts: 1178, mult: 0.979) |
| `WLD` | Fey | Ultimate | 27.4 -> **27.8** (+1.5%) | 41.7 -> **55.6** | 1170.0 -> **1573.5** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.6%) |
| `LWF` | Fey | Debuff / Control | 17.0 -> **15.8** (-7.1%) | 18.3 -> **23.3** | 328.1 -> **383.9** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.6%) |
| `LWW` | Fey | Debuff / Control | 42.7 -> **43.3** (+1.4%) | - | 42.7 -> **43.3** | Class Fey undertuned (WR: 46.2%, factor: 1.015) |
| `LWL` | Fey | Debuff / Control | 39.8 -> **41.4** (+4.0%) | - | 39.8 -> **41.4** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Individual spell undertuned (WR: 42.7%, Casts: 2214, mult: 1.025) |
| `LWD` | Fey | Conditional Strike | 4.3 -> **3.7** (-14.0%) | 49.6 -> **68.0** | 217.6 -> **255.3** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1500). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 6.5 -> **5.6** (-13.8%) | 47.1 -> **64.4** | 312.7 -> **366.2** | Weather 'Raining' beneficiaries undertuned (WR: 44.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.0% vs 30% floor, Casts: 2888). Increasing spread: b -16.4%, n +33.6% |
| `WDW` | Ice | Buff / Sustain | 14.2 -> **14.5** (+2.1%) | - | 14.2 -> **14.5** | Individual spell undertuned (WR: 43.9%, Casts: 2793, mult: 1.021) |
| `WDE` | Ice | Setup - Weather | 25.2 -> **25.9** (+2.8%) | - | 25.2 -> **25.9** | Individual spell undertuned (WR: 42.3%, Casts: 1060, mult: 1.027) |
| `WDD` | Ice | Ultimate | 27.9 -> **27.9** (+0.0%) | 30.8 -> **39.1** | 887.2 -> **1118.8** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 2.5% vs 16% floor, Casts: 1958). Shifted tuner focus: protected ultimate base floor at 27.9 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWE` | Ice | Setup - Location | 28.5 -> **30.1** (+5.6%) | - | 28.5 -> **30.1** | Location 'Tundra' appliers undertuned (WR: 42.1%, casts: 3207); Individual spell undertuned (WR: 42.1%, Casts: 3207, mult: 1.028) |
| `DWD` | Ice | Conditional Strike | 11.1 -> **10.2** (-8.1%) | 12.8 -> **15.1** | 153.2 -> **164.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 22.5% vs 30% floor, Casts: 1999). Increasing spread: b -9.0%, n +18.3%; Individual spell undertuned (WR: 46.0%, Casts: 1999, mult: 1.013) |
| `ELF` | Wind | Conditional Strike | 11.8 -> **10.3** (-12.7%) | 31.3 -> **41.8** | 381.1 -> **440.8** | Status 'Bleeding' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.9% vs 30% floor, Casts: 1468). Increasing spread: b -15.2%, n +31.3% |
| `ELE` | Wind | Setup - Weather | 21.5 -> **22.0** (+2.3%) | - | 21.5 -> **22.0** | Individual spell undertuned (WR: 43.8%, Casts: 1592, mult: 1.021) |
| `ELL` | Wind | Buff / Sustain | 37.3 -> **36.4** (-2.4%) | - | 37.3 -> **36.4** | Individual spell overtuned (WR: 56.8%, Casts: 1681, mult: 0.977) |
| `ELD` | Wind | Conditional Strike | 7.3 -> **6.2** (-15.1%) | 40.6 -> **54.7** | 303.7 -> **345.3** | Weather 'Raining' beneficiaries undertuned (WR: 44.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 2441). Increasing spread: b -15.4%, n +31.7% |
| `LEF` | Wind | Conditional Strike | 4.7 -> **4.0** (-14.9%) | 35.2 -> **45.4** | 170.1 -> **185.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.7% vs 30% floor, Casts: 1539). Increasing spread: b -14.1%, n +28.9% |
| `EDF` | Poison | Conditional Strike | 4.5 -> **3.8** (-15.6%) | 35.6 -> **46.5** | 164.7 -> **180.5** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.6% vs 30% floor, Casts: 1585). Increasing spread: b -14.9%, n +30.6% |
| `EDW` | Poison | Debuff / Control | 20.2 -> **19.1** (-5.4%) | - | 20.2 -> **19.1** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 60.2%, Casts: 1479, mult: 0.963) |
| `EDE` | Poison | Setup - Location | 42.4 -> **50.6** (+19.3%) | - | 42.4 -> **50.6** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Location 'Swamp' appliers undertuned (WR: 42.2%, casts: 2339) |
| `EDL` | Poison | Debuff / Control | 4.7 -> **3.9** (-17.0%) | - | 4.7 -> **3.9** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 86.3%, Casts: 2277, mult: 0.852) |
| `EDD` | Poison | Ultimate | 27.5 -> **27.0** (-1.8%) | 21.6 -> **28.4** | 621.5 -> **793.8** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Status 'Bleeding' beneficiaries undertuned (WR: 45.8%) |
| `DEF` | Poison | Conditional Strike | 32.1 -> **31.2** (-2.8%) | 1.7 -> **1.7** | 86.7 -> **84.2** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 50.8% within [30%-55%] target window, WR: 53.9%). |
| `DEW` | Poison | Debuff / Control | 21.1 -> **20.4** (-3.3%) | - | 21.1 -> **20.4** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 55.6%, Casts: 3450, mult: 0.981) |
| `DEE` | Poison | Debuff / Control | 22.4 -> **21.7** (-3.1%) | - | 22.4 -> **21.7** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 54.7%, Casts: 1571, mult: 0.984) |
| `DEL` | Poison | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 30.8 -> **42.0** | 15.9 -> **17.2** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Status 'Bleeding' beneficiaries undertuned (WR: 45.8%) |
| `DED` | Poison | Debuff / Control | 24.3 -> **23.6** (-2.9%) | - | 24.3 -> **23.6** | Class Poison overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 53.6%, Casts: 3308, mult: 0.988) |
| `LDF` | Cosmic | Debuff / Control | 58.9 -> **57.5** (-2.4%) | - | 58.9 -> **57.5** | Individual spell overtuned (WR: 56.8%, Casts: 1202, mult: 0.977) |
| `LDL` | Cosmic | Conditional Strike | 5.6 -> **4.8** (-14.3%) | 35.1 -> **46.9** | 202.2 -> **229.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.9% vs 30% floor, Casts: 2024). Increasing spread: b -16.4%, n +33.8%; Individual spell undertuned (WR: 43.6%, Casts: 2024, mult: 1.022) |
| `LDD` | Cosmic | Ultimate | 52.9 -> **57.1** (+7.9%) | 5.7 -> **5.4** | 354.4 -> **365.4** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2366, WR: 47.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 6.8 -> **5.8** (-14.7%) | 35.1 -> **46.6** | 245.5 -> **276.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.0% vs 30% floor, Casts: 1769). Increasing spread: b -16.0%, n +32.9%; Individual spell undertuned (WR: 46.1%, Casts: 1769, mult: 1.013) |
| `DLW` | Cosmic | Direct Damage | 61.1 -> **62.3** (+2.0%) | - | 61.1 -> **62.3** | Individual spell undertuned (WR: 44.2%, Casts: 2009, mult: 1.019) |
| `DLL` | Cosmic | Conditional Strike | 14.6 -> **12.9** (-11.6%) | 19.8 -> **25.3** | 303.7 -> **339.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.8% vs 30% floor, Casts: 1698). Increasing spread: b -13.7%, n +28.0%; Individual spell undertuned (WR: 42.2%, Casts: 1698, mult: 1.027) |
