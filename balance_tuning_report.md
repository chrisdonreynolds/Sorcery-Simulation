# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T23:12:45Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 738.0s  
**Total Spells Tuned:** 97 / 125  

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
| **Poison** | 21,554 | 54.9% | 54.9% | 9.2 | Overtuned ⚠️ |
| **Beasts** | 17,504 | 53.1% | 53.1% | 7.5 | Balanced ✅ |
| **Blood** | 19,780 | 52.7% | 52.7% | 11.4 | Balanced ✅ |
| **Fire** | 10,508 | 52.2% | 52.2% | 14.9 | Balanced ✅ |
| **Plants** | 21,296 | 51.8% | 51.8% | 9.4 | Balanced ✅ |
| **Earth** | 9,876 | 51.4% | 51.5% | 22.8 | Balanced ✅ |
| **Dark** | 9,230 | 51.4% | 51.4% | 13.1 | Balanced ✅ |
| **Light** | 11,024 | 51.0% | 51.0% | 6.6 | Balanced ✅ |
| **Ghostfire** | 23,255 | 50.8% | 50.8% | 15.1 | Balanced ✅ |
| **Water** | 9,835 | 48.5% | 48.5% | 10.0 | Balanced ✅ |
| **Wind** | 20,125 | 48.4% | 48.4% | 7.6 | Balanced ✅ |
| **Ice** | 22,505 | 47.9% | 47.9% | 12.1 | Balanced ✅ |
| **Cosmic** | 19,186 | 47.8% | 47.8% | 15.8 | Balanced ✅ |
| **Lightning** | 22,518 | 47.7% | 47.7% | 10.8 | Balanced ✅ |
| **Fey** | 19,077 | 45.3% | 45.3% | 8.3 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,077 (53.8%) | 4,033 (52.9%) | 21.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,780 (44.9%) | 4,610 (56.5%) | 5.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,654 (58.4%) | 6,493 (48.0%) | 9.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,375 (63.3%) | 10,099 (47.4%) | 5.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 15,047 (44.6%) | 4,050 (47.2%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,886 (52.4%) | 5,550 (44.9%) | 1.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,532 (41.9%) | 5,114 (41.1%) | 5.1% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 45.6 -> **44.3** (-2.9%) | - | 45.6 -> **44.3** | Status 'Burning' appliers overtuned on own (WR: 58.4%) |
| `FFE` | Fire | Debuff / Control | 34.8 -> **34.0** (-2.3%) | - | 34.8 -> **34.0** | Individual spell overtuned (WR: 56.7%, Casts: 2801, mult: 0.977) |
| `FFL` | Fire | Debuff / Control | 6.9 -> **6.5** (-5.8%) | - | 6.9 -> **6.5** | Status 'Burning' appliers overtuned on own (WR: 58.4%); Individual spell overtuned (WR: 59.8%, Casts: 1634, mult: 0.965) |
| `FFD` | Fire | Conditional Strike | 6.7 -> **5.7** (-14.9%) | 23.0 -> **29.8** | 160.8 -> **175.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.9% vs 30% floor, Casts: 2687). Increasing spread: b -14.4%, n +29.6% |
| `WWF` | Water | Conditional Strike | 12.9 -> **11.3** (-12.4%) | 18.9 -> **23.8** | 256.7 -> **280.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.1% vs 30% floor, Casts: 1523). Increasing spread: b -12.8%, n +26.1% |
| `WWE` | Water | Setup - Weather | 28.2 -> **29.8** (+5.7%) | - | 28.2 -> **29.8** | Weather 'Raining' appliers undertuned (WR: 41.9%, casts: 1532); Individual spell undertuned (WR: 41.9%, Casts: 1532, mult: 1.028) |
| `WWL` | Water | Buff / Sustain | 67.6 -> **68.7** (+1.6%) | - | 67.6 -> **68.7** | Individual spell undertuned (WR: 45.1%, Casts: 2596, mult: 1.016) |
| `EEF` | Earth | Conditional Strike | 20.3 -> **18.7** (-7.9%) | 7.5 -> **8.6** | 172.6 -> **179.5** | Status 'Stunned' appliers undertuned (WR: 44.6%, casts: 15047); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 26.5% vs 30% floor, Casts: 1665). Increasing spread: b -7.4%, n +14.9% |
| `EEW` | Earth | Buff / Sustain | 30.9 -> **30.0** (-2.9%) | - | 30.9 -> **30.0** | Individual spell overtuned (WR: 58.3%, Casts: 1576, mult: 0.971) |
| `LLF` | Light | Conditional Strike | 3.5 -> **4.0** (+14.3%) | 25.4 -> **33.5** | 92.4 -> **138.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 3497). Increasing spread: b -15.5%, n +31.8%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLE` | Light | Setup - Weather | 44.7 -> **53.2** (+19.0%) | - | 44.7 -> **53.2** | Weather 'Sunny' appliers undertuned (WR: 44.9%, casts: 1780); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 26.6 -> **25.6** (-3.8%) | - | 26.6 -> **25.6** | Individual spell overtuned (WR: 60.6%, Casts: 1875, mult: 0.962) |
| `LLD` | Light | Ultimate | 31.9 -> **31.9** (+0.0%) | 14.0 -> **17.7** | 478.5 -> **596.5** | Weather 'Sunny' beneficiaries overtuned (WR: 56.5%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1852). Shifted tuner focus: protected ultimate base floor at 31.9 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 4.5 -> **3.7** (-17.8%) | 36.2 -> **49.6** | 167.4 -> **187.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1786). Increasing spread: b -18.0%, n +37.0% |
| `DDE` | Dark | Setup - Weather | 44.9 -> **50.1** (+11.6%) | - | 44.9 -> **50.1** | Weather 'Darkness' appliers overtuned on own (WR: 54.3%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDD` | Dark | Debuff / Control | 27.9 -> **27.0** (-3.2%) | - | 27.9 -> **27.0** | Individual spell overtuned (WR: 58.8%, Casts: 1921, mult: 0.969) |
| `FWF` | Ghostfire | Debuff / Control | 36.3 -> **33.2** (-8.5%) | - | 36.3 -> **33.2** | Status 'Burning' appliers overtuned on own (WR: 58.4%); Individual spell overtuned (WR: 65.5%, Casts: 1688, mult: 0.942) |
| `FWE` | Ghostfire | Setup - Location | 60.5 -> **65.1** (+7.6%) | - | 60.5 -> **65.1** | Location 'Graveyard' appliers undertuned (WR: 39.5%, casts: 2944); Individual spell undertuned (WR: 39.5%, Casts: 2944, mult: 1.038) |
| `FWL` | Ghostfire | Debuff / Control | 80.1 -> **77.4** (-3.4%) | - | 80.1 -> **77.4** | Individual spell overtuned (WR: 59.5%, Casts: 2977, mult: 0.966) |
| `FWD` | Ghostfire | Ultimate | 34.9 -> **38.8** (+11.2%) | 19.2 -> **19.3** | 705.0 -> **787.6** | Status 'Cursed' beneficiaries undertuned (WR: 42.1%); Location 'Graveyard' beneficiaries undertuned (WR: 41.4%) |
| `WFF` | Ghostfire | Conditional Strike | 6.4 -> **5.6** (-12.5%) | 23.2 -> **30.1** | 154.9 -> **174.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.6% vs 30% floor, Casts: 3005). Increasing spread: b -14.6%, n +29.9%; Individual spell undertuned (WR: 43.2%, Casts: 3005, mult: 1.023) |
| `WFW` | Ghostfire | Debuff / Control | 29.0 -> **28.6** (-1.4%) | - | 29.0 -> **28.6** | Individual spell overtuned (WR: 54.2%, Casts: 2414, mult: 0.986) |
| `WFE` | Ghostfire | Debuff / Control | 33.6 -> **34.2** (+1.8%) | - | 33.6 -> **34.2** | Status 'Bleeding' appliers overtuned on own (WR: 63.3%); Buffed setup spell [WFE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `WFL` | Ghostfire | Buff / Sustain | 38.0 -> **39.1** (+2.9%) | - | 38.0 -> **39.1** | Individual spell undertuned (WR: 42.0%, Casts: 731, mult: 1.028) |
| `WFD` | Ghostfire | Conditional Strike | 7.7 -> **6.6** (-14.3%) | 21.4 -> **27.5** | 172.5 -> **188.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.0% vs 30% floor, Casts: 2431). Increasing spread: b -14.0%, n +28.6% |
| `FEF` | Beasts | Debuff / Control | 30.1 -> **30.5** (+1.3%) | - | 30.1 -> **30.5** | Individual spell undertuned (WR: 46.3%, Casts: 1503, mult: 1.012) |
| `FEW` | Beasts | Conditional Strike | 4.6 -> **3.8** (-17.4%) | 34.6 -> **48.2** | 163.8 -> **187.0** | Status 'Entangled' beneficiaries undertuned (WR: 44.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 1129). Increasing spread: b -17.8%, n +36.6% |
| `FEE` | Beasts | Buff / Sustain | 26.6 -> **27.1** (+1.9%) | - | 26.6 -> **27.1** | Individual spell undertuned (WR: 44.7%, Casts: 2144, mult: 1.018) |
| `FEL` | Beasts | Buff / Sustain | 28.2 -> **29.2** (+3.5%) | - | 28.2 -> **29.2** | Individual spell undertuned (WR: 39.7%, Casts: 1612, mult: 1.037) |
| `FED` | Beasts | Conditional Strike | 9.1 -> **9.7** (+6.6%) | 1.5 -> **1.5** | 22.8 -> **24.2** | Condition triggers excessively (N=1 conditions, Trigger Rate: 59.1% vs 55% ceiling, WR: 54.0%). Compressing spread: b +7.5%, n -11.1%; Individual spell overtuned (WR: 54.0%, Casts: 1783, mult: 0.987) |
| `EFF` | Beasts | Debuff / Control | 5.8 -> **4.7** (-19.0%) | 33.7 -> **45.6** | 201.3 -> **219.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1868). Increasing spread: b -17.3%, n +35.4%; Individual spell overtuned (WR: 58.0%, Casts: 1868, mult: 0.972) |
| `EFW` | Beasts | Buff / Sustain | 25.0 -> **24.6** (-1.6%) | - | 25.0 -> **24.6** | Individual spell overtuned (WR: 55.2%, Casts: 1100, mult: 0.983) |
| `EFL` | Beasts | Buff / Sustain | 10.2 -> **8.7** (-14.7%) | - | 10.2 -> **8.7** | Individual spell overtuned (WR: 85.5%, Casts: 1942, mult: 0.856) |
| `EFD` | Beasts | Ultimate | 29.4 -> **29.4** (+0.0%) | 21.9 -> **28.9** | 673.3 -> **879.1** | Status 'Entangled' beneficiaries undertuned (WR: 44.9%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.7% vs 16% floor, Casts: 2136). Shifted tuner focus: protected ultimate base floor at 29.4 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo. |
| `FLF` | Lightning | Conditional Strike | 4.9 -> **4.0** (-18.4%) | 42.5 -> **58.1** | 213.2 -> **236.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1452). Increasing spread: b -17.9%, n +36.7% |
| `FLW` | Lightning | Debuff / Control | 53.3 -> **54.3** (+1.9%) | - | 53.3 -> **54.3** | Status 'Stunned' appliers undertuned (WR: 44.6%, casts: 15047) |
| `FLD` | Lightning | Ultimate | 50.4 -> **55.3** (+9.7%) | 9.2 -> **8.8** | 514.1 -> **541.9** | Weather 'Storming' beneficiaries undertuned (WR: 45.4%); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 2598, WR: 45.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `LFF` | Lightning | Conditional Strike | 5.3 -> **4.5** (-15.1%) | 31.4 -> **42.4** | 171.7 -> **195.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 2956). Increasing spread: b -17.1%, n +35.2%; Individual spell undertuned (WR: 43.8%, Casts: 2956, mult: 1.021) |
| `LFE` | Lightning | Debuff / Control | 47.3 -> **48.2** (+1.9%) | - | 47.3 -> **48.2** | Status 'Stunned' appliers undertuned (WR: 44.6%, casts: 15047) |
| `LFL` | Lightning | Debuff / Control | 29.7 -> **25.1** (-15.5%) | 19.0 -> **24.5** | 594.0 -> **640.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.8% vs 30% floor, Casts: 2098). Increasing spread: b -14.1%, n +28.9%; Individual spell overtuned (WR: 54.4%, Casts: 2098, mult: 0.986) |
| `LFD` | Lightning | Conditional Strike | 8.1 -> **7.7** (-4.9%) | 34.5 -> **43.1** | 287.6 -> **339.6** | Status 'Stunned' appliers undertuned (WR: 44.6%, casts: 15047); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.5% vs 30% floor, Casts: 2380). Increasing spread: b -12.2%, n +24.9% |
| `FDF` | Blood | Conditional Strike | 4.7 -> **4.0** (-14.9%) | 36.2 -> **49.6** | 174.8 -> **202.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2096). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 41.8%, Casts: 2096, mult: 1.029) |
| `FDE` | Blood | Setup - Weather | 20.6 -> **21.1** (+2.4%) | - | 20.6 -> **21.1** | Individual spell undertuned (WR: 43.5%, Casts: 1941, mult: 1.022) |
| `FDL` | Blood | Debuff / Control | 25.0 -> **25.4** (+1.6%) | - | 25.0 -> **25.4** | Status 'Bleeding' appliers overtuned on own (WR: 63.3%); Buffed setup spell [FDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `FDD` | Blood | Ultimate | 38.3 -> **41.9** (+9.4%) | 8.5 -> **8.0** | 363.8 -> **377.1** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 1632, WR: 46.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 46.4%, Casts: 1632, mult: 1.012) |
| `DFF` | Blood | Conditional Strike | 5.9 -> **4.9** (-16.9%) | 22.8 -> **30.0** | 140.4 -> **151.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 1468). Increasing spread: b -15.3%, n +31.4%; Individual spell overtuned (WR: 56.0%, Casts: 1468, mult: 0.980) |
| `DFW` | Blood | Debuff / Control | 24.1 -> **23.9** (-0.8%) | - | 24.1 -> **23.9** | Status 'Bleeding' appliers overtuned on own (WR: 63.3%); Buffed setup spell [DFW] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `DFE` | Blood | Buff / Sustain | 36.5 -> **37.8** (+3.6%) | - | 36.5 -> **37.8** | Individual spell undertuned (WR: 39.8%, Casts: 3107, mult: 1.037) |
| `DFD` | Blood | Conditional Strike | 75.1 -> **85.5** (+13.8%) | 0.2 -> **0.2** | 90.1 -> **102.6** | Condition triggers excessively (N=1 conditions, Trigger Rate: 95.0% vs 55% ceiling, WR: 51.6%). Compressing spread: b +13.9%, n -22.2% |
| `WEF` | Plants | Conditional Strike | 7.6 -> **6.4** (-15.8%) | 17.5 -> **22.5** | 140.6 -> **150.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.2% vs 30% floor, Casts: 1427). Increasing spread: b -13.9%, n +28.5%; Individual spell overtuned (WR: 54.5%, Casts: 1427, mult: 0.985) |
| `WEW` | Plants | Debuff / Control | 85.9 -> **100.2** (+16.6%) | - | 85.9 -> **100.2** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 45.7%, Casts: 1637, mult: 1.014) |
| `WED` | Plants | Conditional Strike | 11.4 -> **9.4** (-17.5%) | 15.0 -> **20.4** | 182.4 -> **201.2** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.3% vs 8% floor, Casts: 2084). Increasing spread: b -17.5%, n +35.9% |
| `EWF` | Plants | Buff / Sustain | 7.9 -> **6.5** (-17.7%) | 15.9 -> **20.1** | 133.5 -> **137.2** | Weather 'Sunny' beneficiaries overtuned (WR: 56.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.9% vs 30% floor, Casts: 2758). Increasing spread: b -14.4%, n +29.6% |
| `EWW` | Plants | Debuff / Control | 13.3 -> **11.4** (-14.3%) | - | 13.3 -> **11.4** | Individual spell overtuned (WR: 86.0%, Casts: 1738, mult: 0.854) |
| `EWL` | Plants | Debuff / Control | 62.0 -> **63.9** (+3.1%) | - | 62.0 -> **63.9** | Individual spell undertuned (WR: 41.4%, Casts: 2908, mult: 1.030) |
| `EWD` | Plants | Conditional Strike | 12.1 -> **13.8** (+14.0%) | 32.0 -> **44.1** | 399.3 -> **622.4** | Status 'Bleeding' appliers overtuned on own (WR: 63.3%); Status 'Entangled' beneficiaries undertuned (WR: 44.9%) |
| `WLF` | Fey | Conditional Strike | 6.4 -> **5.6** (-12.5%) | 28.7 -> **39.1** | 190.1 -> **224.6** | Class Fey undertuned (WR: 45.3%, factor: 1.019); Status 'Cursed' beneficiaries undertuned (WR: 42.1%) |
| `WLW` | Fey | Debuff / Control | 49.0 -> **51.1** (+4.3%) | - | 49.0 -> **51.1** | Class Fey undertuned (WR: 45.3%, factor: 1.019); Individual spell undertuned (WR: 43.4%, Casts: 1838, mult: 1.023) |
| `WLE` | Fey | Setup - Location | 60.9 -> **75.0** (+23.2%) | - | 60.9 -> **75.0** | Class Fey undertuned (WR: 45.3%, factor: 1.019); Location 'Enchanted Forest' appliers undertuned (WR: 42.8%, casts: 2570) |
| `WLL` | Fey | Direct Damage | 59.9 -> **59.8** (-0.2%) | - | 59.9 -> **59.8** | Class Fey undertuned (WR: 45.3%, factor: 1.019); Individual spell overtuned (WR: 56.0%, Casts: 1326, mult: 0.980) |
| `WLD` | Fey | Ultimate | 27.4 -> **27.4** (+0.0%) | 32.1 -> **41.7** | 906.9 -> **1170.0** | Class Fey undertuned (WR: 45.3%, factor: 1.019); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 864). Shifted tuner focus: protected ultimate base floor at 27.4 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 19.1 -> **17.0** (-11.0%) | 14.5 -> **18.3** | 296.1 -> **328.1** | Class Fey undertuned (WR: 45.3%, factor: 1.019); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.8% vs 30% floor, Casts: 3023). Increasing spread: b -12.9%, n +26.3% |
| `LWW` | Fey | Debuff / Control | 41.9 -> **42.7** (+1.9%) | - | 41.9 -> **42.7** | Class Fey undertuned (WR: 45.3%, factor: 1.019) |
| `LWL` | Fey | Debuff / Control | 38.1 -> **39.8** (+4.5%) | - | 38.1 -> **39.8** | Class Fey undertuned (WR: 45.3%, factor: 1.019); Individual spell undertuned (WR: 42.9%, Casts: 1616, mult: 1.025) |
| `LWD` | Fey | Conditional Strike | 5.2 -> **4.3** (-17.3%) | 36.2 -> **49.6** | 193.4 -> **217.6** | Class Fey undertuned (WR: 45.3%, factor: 1.019); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1561). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 7.2 -> **6.5** (-9.7%) | 34.1 -> **47.1** | 252.7 -> **312.7** | Status 'Stunned' appliers undertuned (WR: 44.6%, casts: 15047); Weather 'Raining' beneficiaries undertuned (WR: 41.1%) |
| `WDW` | Ice | Buff / Sustain | 14.4 -> **14.2** (-1.4%) | - | 14.4 -> **14.2** | Status 'Frosty' appliers overtuned on own (WR: 53.8%) |
| `WDE` | Ice | Setup - Weather | 24.3 -> **25.2** (+3.7%) | - | 24.3 -> **25.2** | Individual spell undertuned (WR: 40.1%, Casts: 1278, mult: 1.035) |
| `WDL` | Ice | Debuff / Control | 46.2 -> **45.6** (-1.3%) | - | 46.2 -> **45.6** | Status 'Frosty' appliers overtuned on own (WR: 53.8%) |
| `WDD` | Ice | Ultimate | 28.4 -> **27.9** (-1.8%) | 25.4 -> **30.8** | 749.8 -> **887.2** | Weather 'Blizzard' beneficiaries overtuned (WR: 55.6%); Location 'Tundra' beneficiaries overtuned (WR: 55.6%) |
| `DWF` | Ice | Debuff / Control | 45.6 -> **44.0** (-3.5%) | - | 45.6 -> **44.0** | Status 'Frosty' appliers overtuned on own (WR: 53.8%); Individual spell overtuned (WR: 56.3%, Casts: 1147, mult: 0.978) |
| `DWW` | Ice | Debuff / Control | 42.8 -> **42.2** (-1.4%) | - | 42.8 -> **42.2** | Individual spell overtuned (WR: 54.3%, Casts: 1925, mult: 0.986) |
| `DWE` | Ice | Setup - Location | 27.1 -> **28.5** (+5.2%) | - | 27.1 -> **28.5** | Location 'Tundra' appliers undertuned (WR: 42.6%, casts: 3984); Individual spell undertuned (WR: 42.6%, Casts: 3984, mult: 1.026) |
| `DWL` | Ice | Debuff / Control | 45.0 -> **43.0** (-4.4%) | - | 45.0 -> **43.0** | Status 'Frosty' appliers overtuned on own (WR: 53.8%); Individual spell overtuned (WR: 58.8%, Casts: 2330, mult: 0.969) |
| `DWD` | Ice | Conditional Strike | 12.4 -> **11.1** (-10.5%) | 10.5 -> **12.8** | 142.6 -> **153.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.4% vs 30% floor, Casts: 2368). Increasing spread: b -10.6%, n +21.7% |
| `ELF` | Wind | Conditional Strike | 13.5 -> **11.8** (-12.6%) | 23.7 -> **31.3** | 333.4 -> **381.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.9% vs 30% floor, Casts: 1899). Increasing spread: b -15.7%, n +32.1%; Individual spell undertuned (WR: 40.8%, Casts: 1899, mult: 1.033) |
| `ELE` | Wind | Setup - Weather | 21.1 -> **21.5** (+1.9%) | - | 21.1 -> **21.5** | Individual spell undertuned (WR: 44.4%, Casts: 1370, mult: 1.019) |
| `ELD` | Wind | Conditional Strike | 8.9 -> **7.3** (-18.0%) | 29.8 -> **40.6** | 274.1 -> **303.7** | Weather 'Raining' beneficiaries undertuned (WR: 41.1%); Weather 'Blizzard' appliers overtuned on own (WR: 55.2%) |
| `LEF` | Wind | Conditional Strike | 5.5 -> **4.7** (-14.5%) | 26.8 -> **35.2** | 152.9 -> **170.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.8% vs 30% floor, Casts: 2283). Increasing spread: b -15.3%, n +31.3% |
| `LEE` | Wind | Setup - Weather | 20.3 -> **19.9** (-2.0%) | - | 20.3 -> **19.9** | Individual spell overtuned (WR: 56.2%, Casts: 2077, mult: 0.979) |
| `LEL` | Wind | Buff / Sustain | 40.2 -> **40.7** (+1.2%) | - | 40.2 -> **40.7** | Individual spell undertuned (WR: 46.0%, Casts: 938, mult: 1.013) |
| `EDF` | Poison | Conditional Strike | 5.2 -> **4.5** (-13.5%) | 26.6 -> **35.6** | 143.5 -> **164.7** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.9% vs 30% floor, Casts: 2006). Increasing spread: b -16.4%, n +33.8% |
| `EDW` | Poison | Debuff / Control | 22.1 -> **20.2** (-8.6%) | - | 22.1 -> **20.2** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 67.9%, Casts: 1898, mult: 0.932) |
| `EDE` | Poison | Setup - Location | 35.5 -> **42.4** (+19.4%) | - | 35.5 -> **42.4** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Location 'Swamp' appliers undertuned (WR: 41.6%, casts: 2322) |
| `EDL` | Poison | Debuff / Control | 5.6 -> **4.7** (-16.1%) | - | 5.6 -> **4.7** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 85.0%, Casts: 2607, mult: 0.858) |
| `EDD` | Poison | Ultimate | 28.1 -> **27.5** (-2.1%) | 16.8 -> **21.6** | 500.2 -> **621.5** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 1.1% vs 16% floor, Casts: 1736). Shifted tuner focus: protected ultimate base floor at 28.1 (hard-coded floor >= 20.0) and buffed appliers/setups (WFE, FDL, DFW, EWD, EDE) with +15% b tempo. |
| `DEF` | Poison | Conditional Strike | 32.7 -> **32.1** (-1.8%) | 1.7 -> **1.7** | 88.3 -> **86.7** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 46.9% within [30%-55%] target window, WR: 52.7%). |
| `DEW` | Poison | Debuff / Control | 22.0 -> **21.1** (-4.1%) | - | 22.0 -> **21.1** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 56.6%, Casts: 2389, mult: 0.977) |
| `DEE` | Poison | Debuff / Control | 23.2 -> **22.4** (-3.4%) | - | 23.2 -> **22.4** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 53.9%, Casts: 1660, mult: 0.987) |
| `DEL` | Poison | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 23.2 -> **30.8** | 14.5 -> **15.9** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.3% vs 30% floor, Casts: 1991). Increasing spread: b -15.9%, n +32.6% |
| `DED` | Poison | Debuff / Control | 24.8 -> **24.3** (-2.0%) | - | 24.8 -> **24.3** | Class Poison overtuned (WR: 54.9%, factor: 0.980) |
| `LDW` | Cosmic | Debuff / Control | 48.1 -> **49.0** (+1.9%) | - | 48.1 -> **49.0** | Status 'Stunned' appliers undertuned (WR: 44.6%, casts: 15047) |
| `LDE` | Cosmic | Setup - Location | 24.1 -> **24.6** (+2.1%) | - | 24.1 -> **24.6** | Individual spell undertuned (WR: 43.7%, Casts: 1973, mult: 1.021) |
| `LDL` | Cosmic | Conditional Strike | 6.6 -> **5.6** (-15.2%) | 26.7 -> **35.1** | 182.8 -> **202.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.6% vs 30% floor, Casts: 1663). Increasing spread: b -15.4%, n +31.5% |
| `LDD` | Cosmic | Ultimate | 48.1 -> **52.9** (+10.0%) | 6.1 -> **5.7** | 341.5 -> **354.4** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2207, WR: 44.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 44.7%, Casts: 2207, mult: 1.018) |
| `DLF` | Cosmic | Conditional Strike | 7.9 -> **6.8** (-13.9%) | 26.4 -> **35.1** | 216.5 -> **245.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.1% vs 30% floor, Casts: 2333). Increasing spread: b -16.0%, n +32.8%; Individual spell undertuned (WR: 44.7%, Casts: 2333, mult: 1.018) |
| `DLL` | Cosmic | Conditional Strike | 16.8 -> **14.6** (-13.1%) | 15.2 -> **19.8** | 272.2 -> **303.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 1707). Increasing spread: b -14.9%, n +30.5%; Individual spell undertuned (WR: 44.0%, Casts: 1707, mult: 1.020) |
