# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T03:20:39Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 320.3s  
**Total Spells Tuned:** 91 / 125  

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
| **Blood** | 16,689 | 55.1% | 55.2% | 31.6 | Overtuned ⚠️ |
| **Poison** | 16,134 | 54.6% | 54.6% | 12.1 | Overtuned ⚠️ |
| **Ghostfire** | 14,335 | 54.4% | 54.4% | 63.1 | Overtuned ⚠️ |
| **Light** | 7,784 | 52.6% | 52.6% | 36.1 | Balanced ✅ |
| **Earth** | 8,254 | 51.9% | 51.9% | 17.8 | Balanced ✅ |
| **Dark** | 6,869 | 51.8% | 51.8% | 49.3 | Balanced ✅ |
| **Lightning** | 18,453 | 50.9% | 50.9% | 40.1 | Balanced ✅ |
| **Fire** | 6,708 | 50.7% | 50.7% | 16.8 | Balanced ✅ |
| **Beasts** | 14,192 | 49.3% | 49.3% | 23.0 | Balanced ✅ |
| **Plants** | 15,725 | 48.8% | 48.7% | 7.2 | Balanced ✅ |
| **Cosmic** | 14,391 | 48.3% | 48.3% | 23.4 | Balanced ✅ |
| **Water** | 8,352 | 48.0% | 47.9% | 24.9 | Balanced ✅ |
| **Fey** | 13,916 | 47.5% | 47.5% | 106396.6 | Balanced ✅ |
| **Ice** | 16,667 | 47.2% | 47.2% | 38.6 | Balanced ✅ |
| **Wind** | 15,647 | 47.0% | 46.9% | 11.1 | Balanced ✅ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,438 (50.6%) | 3,414 (51.4%) | 19.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 893 (58.4%) | 3,585 (49.3%) | 3.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,103 (52.5%) | 3,904 (49.1%) | 8.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 6,577 (58.5%) | 6,548 (46.9%) | 4.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 11,827 (52.0%) | 3,738 (46.9%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,665 (50.3%) | 5,107 (46.0%) | 0.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,015 (47.5%) | 3,023 (43.1%) | 6.8% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFD` | Fire | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 1369.4 -> **1805.4** | 959.3 -> **1083.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 1066). Increasing spread: b -15.5%, n +31.8% |
| `WWF` | Water | Conditional Strike | 2.3 -> **2.0** (-13.0%) | 620.0 -> **788.0** | 1428.3 -> **1578.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.9% vs 30% floor, Casts: 1422). Increasing spread: b -13.2%, n +27.1%; Individual spell undertuned (WR: 46.2%, Casts: 1422, mult: 1.012) |
| `EEF` | Earth | Conditional Strike | 42.7 -> **49.1** (+15.0%) | 88.9 -> **107.1** | 3838.7 -> **5307.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 19.8% vs 30% floor, Casts: 2081). Increasing spread: b -10.1%, n +20.5%; Buffed setup spell [EEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `EEW` | Earth | Buff / Sustain | 18.7 -> **18.3** (-2.1%) | - | 18.7 -> **18.3** | Individual spell overtuned (WR: 56.0%, Casts: 1354, mult: 0.980) |
| `EED` | Earth | Direct Damage | 7.1 -> **6.9** (-2.8%) | - | 7.1 -> **6.9** | Individual spell overtuned (WR: 56.4%, Casts: 1679, mult: 0.978) |
| `LLF` | Light | Conditional Strike | 7.4 -> **8.5** (+14.9%) | 1818.2 -> **2393.4** | 13462.1 -> **20352.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 2486). Increasing spread: b -15.4%, n +31.6%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLE` | Light | Setup - Weather | 160.6 -> **173.9** (+8.3%) | - | 160.6 -> **173.9** | Weather 'Sunny' appliers overtuned on own (WR: 58.4%); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 15.2 -> **14.8** (-2.6%) | - | 15.2 -> **14.8** | Individual spell overtuned (WR: 56.9%, Casts: 1091, mult: 0.976) |
| `LLD` | Light | Ultimate | 43.2 -> **43.2** (+0.0%) | 190.7 -> **247.9** | 8281.4 -> **10752.5** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1541). Shifted tuner focus: protected ultimate base floor at 43.2 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 4064.2 -> **5568.0** | 813.0 -> **1113.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2048). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 44.6%, Casts: 2048, mult: 1.018) |
| `DDE` | Dark | Setup - Weather | 349.1 -> **382.0** (+9.4%) | - | 349.1 -> **382.0** | Weather 'Darkness' appliers overtuned on own (WR: 57.0%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 63.7 -> **62.4** (-2.0%) | - | 63.7 -> **62.4** | Individual spell overtuned (WR: 56.2%, Casts: 1190, mult: 0.979) |
| `DDD` | Dark | Debuff / Control | 17.7 -> **17.5** (-1.1%) | - | 17.7 -> **17.5** | Individual spell overtuned (WR: 53.5%, Casts: 1199, mult: 0.989) |
| `FWF` | Ghostfire | Debuff / Control | 22.1 -> **21.4** (-3.2%) | - | 22.1 -> **21.4** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Individual spell overtuned (WR: 54.9%, Casts: 1363, mult: 0.984) |
| `FWW` | Ghostfire | Debuff / Control | 131.2 -> **144.9** (+10.4%) | - | 131.2 -> **144.9** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 355.6 -> **360.2** (+1.3%) | - | 355.6 -> **360.2** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Location 'Graveyard' appliers overtuned on own (WR: 64.7%) |
| `FWL` | Ghostfire | Debuff / Control | 281.9 -> **308.1** (+9.3%) | - | 281.9 -> **308.1** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 44.8 -> **41.6** (-7.1%) | 309.1 -> **372.4** | 13892.5 -> **15533.4** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Status 'Cursed' beneficiaries overtuned (WR: 53.5%) |
| `WFF` | Ghostfire | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 1801.4 -> **2409.7** | 1261.7 -> **1446.4** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.9% vs 30% floor, Casts: 1805). Increasing spread: b -16.4%, n +33.8% |
| `WFW` | Ghostfire | Debuff / Control | 19.3 -> **18.4** (-4.7%) | - | 19.3 -> **18.4** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Individual spell overtuned (WR: 59.0%, Casts: 1662, mult: 0.968) |
| `WFE` | Ghostfire | Debuff / Control | 9.5 -> **10.0** (+5.3%) | - | 9.5 -> **10.0** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Status 'Bleeding' appliers overtuned on own (WR: 58.5%) |
| `WFL` | Ghostfire | Buff / Sustain | 50.3 -> **49.4** (-1.8%) | - | 50.3 -> **49.4** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982) |
| `WFD` | Ghostfire | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 933.4 -> **1186.6** | 934.4 -> **1068.8** | Class Ghostfire overtuned (WR: 54.4%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.8% vs 30% floor, Casts: 1240). Increasing spread: b -13.3%, n +27.1% |
| `FEW` | Beasts | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 4119.1 -> **5712.7** | 824.0 -> **1142.7** | Status 'Entangled' beneficiaries undertuned (WR: 46.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 1515). Increasing spread: b -17.8%, n +36.5% |
| `FEE` | Beasts | Buff / Sustain | 36.1 -> **37.6** (+4.2%) | - | 36.1 -> **37.6** | Individual spell undertuned (WR: 38.9%, Casts: 1225, mult: 1.040) |
| `FEL` | Beasts | Buff / Sustain | 43.0 -> **44.2** (+2.8%) | - | 43.0 -> **44.2** | Individual spell undertuned (WR: 41.8%, Casts: 2191, mult: 1.029) |
| `EFF` | Beasts | Debuff / Control | 0.2 -> **0.2** (+0.0%) | 3528.3 -> **4798.5** | 705.9 -> **959.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 1162). Increasing spread: b -17.5%, n +36.0% |
| `EFE` | Beasts | Buff / Sustain | 34.7 -> **35.1** (+1.2%) | - | 34.7 -> **35.1** | Individual spell undertuned (WR: 46.5%, Casts: 1578, mult: 1.011) |
| `EFD` | Beasts | Ultimate | 33.6 -> **33.6** (+0.0%) | 534.3 -> **715.4** | 17986.1 -> **24071.0** | Status 'Entangled' beneficiaries undertuned (WR: 46.0%); Location 'Jungle' beneficiaries undertuned (WR: 46.1%) |
| `FLF` | Lightning | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 6026.2 -> **8242.8** | 3013.6 -> **3297.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1958). Increasing spread: b -17.9%, n +36.8%; Individual spell undertuned (WR: 41.5%, Casts: 1958, mult: 1.030) |
| `FLW` | Lightning | Debuff / Control | 151.1 -> **165.7** (+9.7%) | - | 151.1 -> **165.7** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 62.6%, Casts: 2605, mult: 0.954) |
| `FLE` | Lightning | Setup - Weather | 156.9 -> **180.4** (+15.0%) | - | 156.9 -> **180.4** | Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLD` | Lightning | Ultimate | 75.5 -> **75.5** (+0.0%) | 121.1 -> **157.4** | 9218.5 -> **11959.2** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1780). Shifted tuner focus: protected ultimate base floor at 75.5 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 2857.9 -> **3817.7** | 857.7 -> **1145.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.1% vs 30% floor, Casts: 1221). Increasing spread: b -16.4%, n +33.6%; Individual spell undertuned (WR: 44.0%, Casts: 1221, mult: 1.020) |
| `LFW` | Lightning | Buff / Sustain | 25.3 -> **24.4** (-3.6%) | - | 25.3 -> **24.4** | Individual spell overtuned (WR: 59.5%, Casts: 891, mult: 0.966) |
| `LFL` | Lightning | Debuff / Control | 61.4 -> **51.5** (-16.1%) | 879.6 -> **1148.5** | 54068.8 -> **59199.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.7% vs 30% floor, Casts: 2204). Increasing spread: b -14.9%, n +30.6%; Individual spell overtuned (WR: 54.5%, Casts: 2204, mult: 0.985) |
| `LFD` | Lightning | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 1983.3 -> **2667.0** | 1984.3 -> **2401.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 1487). Increasing spread: b -16.8%, n +34.5%; Individual spell undertuned (WR: 36.0%, Casts: 1487, mult: 1.052) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 4074.4 -> **5581.9** | 815.1 -> **1116.6** | Class Blood overtuned (WR: 55.1%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1011). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 57.9 -> **56.7** (-2.1%) | - | 57.9 -> **56.7** | Class Blood overtuned (WR: 55.1%, factor: 0.979) |
| `FDE` | Blood | Setup - Weather | 17.1 -> **16.7** (-2.3%) | - | 17.1 -> **16.7** | Class Blood overtuned (WR: 55.1%, factor: 0.979) |
| `FDD` | Blood | Ultimate | 49.8 -> **52.7** (+5.8%) | 59.9 -> **56.3** | 3032.8 -> **3019.7** | Class Blood overtuned (WR: 55.1%, factor: 0.979); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.3% vs 16% floor, Casts: 1373, WR: 46.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 1518.6 -> **2001.3** | 607.8 -> **600.7** | Class Blood overtuned (WR: 55.1%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.3% vs 30% floor, Casts: 1454). Increasing spread: b -15.5%, n +31.8% |
| `DFW` | Blood | Debuff / Control | 9.9 -> **10.1** (+2.0%) | - | 9.9 -> **10.1** | Class Blood overtuned (WR: 55.1%, factor: 0.979); Status 'Bleeding' appliers overtuned on own (WR: 58.5%) |
| `DFE` | Blood | Buff / Sustain | 47.1 -> **46.1** (-2.1%) | - | 47.1 -> **46.1** | Class Blood overtuned (WR: 55.1%, factor: 0.979) |
| `DFL` | Blood | Buff / Sustain | 29.0 -> **27.9** (-3.8%) | - | 29.0 -> **27.9** | Class Blood overtuned (WR: 55.1%, factor: 0.979); Individual spell overtuned (WR: 54.9%, Casts: 1126, mult: 0.984) |
| `DFD` | Blood | Conditional Strike | 418.9 -> **463.2** (+10.6%) | 0.1 -> **0.1** | 460.8 -> **509.5** | Class Blood overtuned (WR: 55.1%, factor: 0.979); Condition triggers excessively (N=1 conditions, Trigger Rate: 93.3% vs 55% ceiling, WR: 64.5%). Compressing spread: b +19.3%, n -27.4% |
| `WEF` | Plants | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 869.1 -> **1144.3** | 870.1 -> **1030.8** | Location 'Jungle' beneficiaries undertuned (WR: 46.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.8% vs 30% floor, Casts: 1800). Increasing spread: b -14.5%, n +29.6% |
| `WEW` | Plants | Debuff / Control | 943.9 -> **1133.7** (+20.1%) | - | 943.9 -> **1133.7** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 37.8%, Casts: 1173, mult: 1.044) |
| `WED` | Plants | Conditional Strike | 15.6 -> **17.3** (+10.9%) | 26.5 -> **24.9** | 429.0 -> **448.1** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1187, WR: 43.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 43.0%, Casts: 1187, mult: 1.024) |
| `EWF` | Plants | Buff / Sustain | 0.8 -> **0.7** (-12.5%) | 631.1 -> **830.9** | 505.7 -> **582.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 2044). Increasing spread: b -15.4%, n +31.7% |
| `EWW` | Plants | Debuff / Control | 1.5 -> **1.3** (-13.3%) | - | 1.5 -> **1.3** | Individual spell overtuned (WR: 78.0%, Casts: 1816, mult: 0.889) |
| `EWD` | Plants | Conditional Strike | 3.0 -> **3.5** (+16.7%) | 3200.2 -> **4429.9** | 9603.6 -> **15508.1** | Status 'Bleeding' appliers overtuned on own (WR: 58.5%); Status 'Entangled' beneficiaries undertuned (WR: 46.0%) |
| `WLF` | Fey | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 2003.2 -> **2577.4** | 2204.6 -> **2578.4** | Status 'Cursed' beneficiaries overtuned (WR: 53.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 1093). Increasing spread: b -14.9%, n +30.5% |
| `WLW` | Fey | Debuff / Control | 60.6 -> **62.9** (+3.8%) | - | 60.6 -> **62.9** | Individual spell undertuned (WR: 39.5%, Casts: 1881, mult: 1.038) |
| `WLE` | Fey | Setup - Location | 409.5 -> **413.9** (+1.1%) | - | 409.5 -> **413.9** | Location 'Enchanted Forest' appliers overtuned on own (WR: 67.2%); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 55.7 -> **55.0** (-1.3%) | - | 55.7 -> **55.0** | Individual spell overtuned (WR: 54.0%, Casts: 1214, mult: 0.987) |
| `WLD` | Fey | Ultimate | 21.2 -> **20.5** (-3.3%) | 1559.5 -> **2057.3** | 33082.6 -> **42195.2** | Location 'Enchanted Forest' beneficiaries undertuned (WR: 46.3%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1223). Shifted tuner focus: protected ultimate base floor at 21.2 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 23.8 -> **21.4** (-10.1%) | 399.7 -> **512.9** | 9536.7 -> **10997.5** | Location 'Enchanted Forest' beneficiaries undertuned (WR: 46.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.7% vs 30% floor, Casts: 2624). Increasing spread: b -12.9%, n +26.5% |
| `LWL` | Fey | Debuff / Control | 55.0 -> **56.4** (+2.5%) | - | 55.0 -> **56.4** | Individual spell undertuned (WR: 42.8%, Casts: 1379, mult: 1.025) |
| `LWD` | Fey | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 4074.4 -> **5581.9** | 2037.7 -> **2233.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 764). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 3809.7 -> **5155.8** | 4191.8 -> **5156.8** | Weather 'Raining' beneficiaries undertuned (WR: 43.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 1898). Increasing spread: b -15.4%, n +31.7% |
| `WDW` | Ice | Buff / Sustain | 10.5 -> **10.2** (-2.9%) | - | 10.5 -> **10.2** | Individual spell overtuned (WR: 59.1%, Casts: 2167, mult: 0.968) |
| `WDE` | Ice | Setup - Weather | 36.9 -> **38.2** (+3.5%) | - | 36.9 -> **38.2** | Individual spell undertuned (WR: 40.3%, Casts: 2044, mult: 1.034) |
| `WDD` | Ice | Ultimate | 32.5 -> **31.4** (-3.4%) | 288.8 -> **339.9** | 9418.5 -> **10704.3** | Weather 'Blizzard' beneficiaries overtuned (WR: 59.2%); Location 'Tundra' beneficiaries overtuned (WR: 59.2%) |
| `DWF` | Ice | Debuff / Control | 38.2 -> **39.0** (+2.1%) | - | 38.2 -> **39.0** | Individual spell undertuned (WR: 44.0%, Casts: 1571, mult: 1.020) |
| `DWW` | Ice | Debuff / Control | 106.9 -> **110.1** (+3.0%) | - | 106.9 -> **110.1** | Individual spell undertuned (WR: 41.6%, Casts: 1462, mult: 1.030) |
| `DWE` | Ice | Setup - Location | 41.0 -> **43.3** (+5.6%) | - | 41.0 -> **43.3** | Location 'Tundra' appliers undertuned (WR: 42.1%, casts: 2052); Individual spell undertuned (WR: 42.0%, Casts: 2052, mult: 1.028) |
| `DWD` | Ice | Conditional Strike | 3.4 -> **3.0** (-11.8%) | 240.2 -> **292.1** | 820.1 -> **879.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.4% vs 30% floor, Casts: 1333). Increasing spread: b -10.6%, n +21.6% |
| `ELF` | Wind | Conditional Strike | 2.1 -> **1.8** (-14.3%) | 1609.6 -> **2121.9** | 3382.3 -> **3821.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 870). Increasing spread: b -15.5%, n +31.8%; Individual spell undertuned (WR: 43.9%, Casts: 870, mult: 1.021) |
| `ELW` | Wind | Debuff / Control | 108.9 -> **104.7** (-3.9%) | - | 108.9 -> **104.7** | Individual spell overtuned (WR: 60.8%, Casts: 1913, mult: 0.961) |
| `ELE` | Wind | Setup - Weather | 28.5 -> **29.2** (+2.5%) | - | 28.5 -> **29.2** | Individual spell undertuned (WR: 42.8%, Casts: 1607, mult: 1.025) |
| `ELL` | Wind | Buff / Sustain | 43.9 -> **45.6** (+3.9%) | - | 43.9 -> **45.6** | Individual spell undertuned (WR: 39.5%, Casts: 1665, mult: 1.038) |
| `ELD` | Wind | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 2997.5 -> **4028.6** | 3598.2 -> **4029.6** | Weather 'Raining' beneficiaries undertuned (WR: 43.1%); Weather 'Blizzard' appliers undertuned (WR: 45.8%, casts: 1125) |
| `LEF` | Wind | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 1579.0 -> **2076.8** | 1106.0 -> **1246.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.6% vs 30% floor, Casts: 1416). Increasing spread: b -15.4%, n +31.5% |
| `LEE` | Wind | Setup - Weather | 26.2 -> **27.0** (+3.1%) | - | 26.2 -> **27.0** | Individual spell undertuned (WR: 41.7%, Casts: 1410, mult: 1.029) |
| `LEL` | Wind | Buff / Sustain | 121.4 -> **123.6** (+1.8%) | - | 121.4 -> **123.6** | Individual spell undertuned (WR: 44.5%, Casts: 1605, mult: 1.018) |
| `EDF` | Poison | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 1394.9 -> **1843.0** | 558.4 -> **553.2** | Class Poison overtuned (WR: 54.6%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.9% vs 30% floor, Casts: 2050). Increasing spread: b -15.7%, n +32.1% |
| `EDW` | Poison | Debuff / Control | 9.5 -> **9.1** (-4.2%) | - | 9.5 -> **9.1** | Class Poison overtuned (WR: 54.6%, factor: 0.982); Individual spell overtuned (WR: 57.5%, Casts: 2254, mult: 0.974) |
| `EDE` | Poison | Setup - Location | 58.4 -> **65.9** (+12.8%) | - | 58.4 -> **65.9** | Class Poison overtuned (WR: 54.6%, factor: 0.982); Buffed setup spell [EDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `EDD` | Poison | Ultimate | 50.5 -> **49.6** (-1.8%) | 41.2 -> **53.4** | 2131.1 -> **2698.2** | Class Poison overtuned (WR: 54.6%, factor: 0.982); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.4% vs 16% floor, Casts: 1547). Shifted tuner focus: protected ultimate base floor at 50.5 (hard-coded floor >= 20.0) and buffed appliers/setups (WFE, FDL, DFW, EWD, EDE) with +15% b tempo. |
| `DEF` | Poison | Conditional Strike | 29.6 -> **29.1** (-1.7%) | 1.4 -> **1.4** | 71.0 -> **69.8** | Class Poison overtuned (WR: 54.6%, factor: 0.982); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 53.7% within [30%-55%] target window, WR: 51.8%). |
| `DEW` | Poison | Debuff / Control | 11.8 -> **11.6** (-1.7%) | - | 11.8 -> **11.6** | Class Poison overtuned (WR: 54.6%, factor: 0.982) |
| `DEE` | Poison | Debuff / Control | 37.7 -> **37.0** (-1.9%) | - | 37.7 -> **37.0** | Class Poison overtuned (WR: 54.6%, factor: 0.982) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 1590.6 -> **2063.5** | 318.3 -> **412.9** | Class Poison overtuned (WR: 54.6%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 872). Increasing spread: b -14.5%, n +29.7% |
| `DED` | Poison | Debuff / Control | 22.0 -> **22.1** (+0.5%) | - | 22.0 -> **22.1** | Class Poison overtuned (WR: 54.6%, factor: 0.982); Individual spell undertuned (WR: 43.8%, Casts: 1618, mult: 1.021) |
| `LDW` | Cosmic | Debuff / Control | 42.4 -> **41.0** (-3.3%) | - | 42.4 -> **41.0** | Individual spell overtuned (WR: 59.1%, Casts: 2112, mult: 0.968) |
| `LDL` | Cosmic | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 2242.8 -> **3036.8** | 1570.7 -> **1822.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1143). Increasing spread: b -17.2%, n +35.4%; Individual spell undertuned (WR: 46.3%, Casts: 1143, mult: 1.012) |
| `LDD` | Cosmic | Ultimate | 97.9 -> **109.4** (+11.7%) | 23.4 -> **22.0** | 2388.8 -> **2516.2** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2621, WR: 40.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 40.2%, Casts: 2621, mult: 1.035) |
| `DLF` | Cosmic | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 1680.4 -> **2226.5** | 1177.0 -> **1336.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.4% vs 30% floor, Casts: 1185). Increasing spread: b -15.8%, n +32.5%; Individual spell overtuned (WR: 54.8%, Casts: 1185, mult: 0.984) |
| `DLE` | Cosmic | Direct Damage | 54.8 -> **56.5** (+3.1%) | - | 54.8 -> **56.5** | Individual spell undertuned (WR: 41.0%, Casts: 1580, mult: 1.032) |
| `DLL` | Cosmic | Conditional Strike | 2.6 -> **2.3** (-11.5%) | 704.0 -> **921.2** | 1833.0 -> **2121.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.4% vs 30% floor, Casts: 1398). Increasing spread: b -15.1%, n +30.9%; Individual spell undertuned (WR: 36.3%, Casts: 1398, mult: 1.050) |
