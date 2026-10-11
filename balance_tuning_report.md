# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T02:26:08Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 642.6s  
**Total Spells Tuned:** 104 / 125  

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
| **Poison** | 18,778 | 56.2% | 56.2% | 11.1 | Overtuned ⚠️ |
| **Blood** | 17,807 | 55.5% | 55.6% | 21.4 | Overtuned ⚠️ |
| **Ghostfire** | 17,508 | 53.5% | 53.5% | 40.7 | Overtuned ⚠️ |
| **Dark** | 8,705 | 51.9% | 51.9% | 73.9 | Balanced ✅ |
| **Earth** | 9,064 | 51.2% | 51.2% | 17.5 | Balanced ✅ |
| **Light** | 8,728 | 50.9% | 50.9% | 26.9 | Balanced ✅ |
| **Cosmic** | 17,727 | 49.9% | 49.9% | 18.9 | Balanced ✅ |
| **Lightning** | 18,157 | 49.9% | 49.9% | 18.2 | Balanced ✅ |
| **Fire** | 7,813 | 49.6% | 49.6% | 16.2 | Balanced ✅ |
| **Plants** | 19,586 | 48.8% | 48.8% | 8.3 | Balanced ✅ |
| **Beasts** | 17,707 | 48.5% | 48.5% | 16.6 | Balanced ✅ |
| **Ice** | 17,334 | 47.6% | 47.5% | 19.4 | Balanced ✅ |
| **Water** | 8,354 | 47.5% | 47.5% | 14.2 | Balanced ✅ |
| **Fey** | 15,042 | 46.2% | 46.2% | 566.0 | Undertuned ⚠️ |
| **Wind** | 15,550 | 45.7% | 45.7% | 9.9 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,172 (54.3%) | 4,187 (42.5%) | 18.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,075 (58.3%) | 4,472 (44.6%) | 3.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,800 (50.4%) | 3,924 (44.6%) | 9.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,672 (63.2%) | 7,433 (44.8%) | 4.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 11,698 (50.5%) | 4,115 (42.8%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,370 (54.6%) | 5,806 (44.7%) | 2.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,655 (39.2%) | 3,224 (43.8%) | 4.8% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 40.5 -> **41.4** (+2.2%) | - | 40.5 -> **41.4** | Individual spell undertuned (WR: 43.2%, Casts: 1597, mult: 1.023) |
| `FFD` | Fire | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 440.6 -> **591.1** | 574.1 -> **651.3** | Status 'Burning' beneficiaries undertuned (WR: 44.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.8% vs 30% floor, Casts: 1118). Increasing spread: b -15.3%, n +31.3% |
| `WWF` | Water | Conditional Strike | 3.3 -> **3.0** (-9.1%) | 226.5 -> **294.4** | 750.8 -> **886.2** | Status 'Burning' beneficiaries undertuned (WR: 44.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.7% vs 30% floor, Casts: 1299). Increasing spread: b -13.3%, n +27.2% |
| `WWE` | Water | Setup - Weather | 67.1 -> **72.3** (+7.7%) | - | 67.1 -> **72.3** | Weather 'Raining' appliers undertuned (WR: 39.2%, casts: 1655); Individual spell undertuned (WR: 39.2%, Casts: 1655, mult: 1.039) |
| `WWD` | Water | Buff / Sustain | 48.8 -> **47.4** (-2.9%) | - | 48.8 -> **47.4** | Individual spell overtuned (WR: 58.0%, Casts: 1292, mult: 0.972) |
| `EEF` | Earth | Conditional Strike | 24.4 -> **28.1** (+15.2%) | 39.2 -> **48.2** | 980.9 -> **1382.5** | Status 'Frosty' beneficiaries undertuned (WR: 42.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 21.3% vs 30% floor, Casts: 1941). Increasing spread: b -9.5%, n +19.3% |
| `EEW` | Earth | Buff / Sustain | 20.1 -> **19.7** (-2.0%) | - | 20.1 -> **19.7** | Individual spell overtuned (WR: 56.2%, Casts: 1833, mult: 0.979) |
| `LLF` | Light | Conditional Strike | 7.8 -> **6.6** (-15.4%) | 588.2 -> **777.6** | 4595.8 -> **5138.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.8% vs 30% floor, Casts: 2104). Increasing spread: b -15.7%, n +32.2% |
| `LLW` | Light | Debuff / Control | 121.8 -> **140.1** (+15.0%) | - | 121.8 -> **140.1** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LLE` | Light | Setup - Weather | 154.2 -> **145.3** (-5.8%) | - | 154.2 -> **145.3** | Weather 'Sunny' appliers overtuned on own (WR: 58.3%); Individual spell overtuned (WR: 58.3%, Casts: 1075, mult: 0.971) |
| `LLL` | Light | Buff / Sustain | 17.3 -> **16.7** (-3.5%) | - | 17.3 -> **16.7** | Individual spell overtuned (WR: 59.0%, Casts: 1387, mult: 0.968) |
| `LLD` | Light | Ultimate | 36.0 -> **40.0** (+11.1%) | 125.0 -> **120.1** | 4536.0 -> **4844.0** | Weather 'Sunny' beneficiaries undertuned (WR: 44.6%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 2040, WR: 41.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 1153.7 -> **1580.6** | 692.8 -> **790.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2087). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 42.5%, Casts: 2087, mult: 1.026) |
| `DDE` | Dark | Setup - Weather | 209.0 -> **240.3** (+15.0%) | - | 209.0 -> **240.3** | Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 66.5 -> **65.2** (-2.0%) | - | 66.5 -> **65.2** | Individual spell overtuned (WR: 56.0%, Casts: 1866, mult: 0.980) |
| `DDD` | Dark | Debuff / Control | 19.7 -> **18.9** (-4.1%) | - | 19.7 -> **18.9** | Individual spell overtuned (WR: 61.0%, Casts: 1436, mult: 0.960) |
| `FWF` | Ghostfire | Debuff / Control | 22.1 -> **21.4** (-3.2%) | - | 22.1 -> **21.4** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Individual spell overtuned (WR: 55.3%, Casts: 1645, mult: 0.982) |
| `FWW` | Ghostfire | Debuff / Control | 82.6 -> **93.6** (+13.3%) | - | 82.6 -> **93.6** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 238.0 -> **262.4** (+10.3%) | - | 238.0 -> **262.4** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Location 'Graveyard' appliers overtuned on own (WR: 54.1%) |
| `FWL` | Ghostfire | Debuff / Control | 188.6 -> **210.4** (+11.6%) | - | 188.6 -> **210.4** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 49.3 -> **46.9** (-4.9%) | 112.9 -> **144.2** | 5615.3 -> **6809.9** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Status 'Cursed' beneficiaries undertuned (WR: 44.2%) |
| `WFF` | Ghostfire | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 539.0 -> **738.6** | 648.0 -> **739.6** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Status 'Bleeding' beneficiaries undertuned (WR: 44.8%) |
| `WFW` | Ghostfire | Debuff / Control | 23.2 -> **22.1** (-4.7%) | - | 23.2 -> **22.1** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Individual spell overtuned (WR: 59.0%, Casts: 2118, mult: 0.968) |
| `WFE` | Ghostfire | Debuff / Control | 11.5 -> **9.9** (-13.9%) | - | 11.5 -> **9.9** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Status 'Bleeding' appliers overtuned on own (WR: 63.2%) |
| `WFL` | Ghostfire | Buff / Sustain | 46.3 -> **46.5** (+0.4%) | - | 46.3 -> **46.5** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Individual spell undertuned (WR: 44.6%, Casts: 2217, mult: 1.018) |
| `WFD` | Ghostfire | Conditional Strike | 1.7 -> **1.4** (-17.6%) | 346.1 -> **444.7** | 590.1 -> **624.0** | Class Ghostfire overtuned (WR: 53.5%, factor: 0.986); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.2% vs 30% floor, Casts: 1359). Increasing spread: b -13.9%, n +28.5% |
| `FEF` | Beasts | Debuff / Control | 82.9 -> **82.0** (-1.1%) | - | 82.9 -> **82.0** | Individual spell overtuned (WR: 53.5%, Casts: 1555, mult: 0.989) |
| `FEW` | Beasts | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 1163.0 -> **1598.2** | 698.4 -> **799.6** | Status 'Entangled' beneficiaries undertuned (WR: 44.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.9% vs 30% floor, Casts: 1874). Increasing spread: b -16.8%, n +34.6% |
| `FEE` | Beasts | Buff / Sustain | 34.3 -> **35.5** (+3.5%) | - | 34.3 -> **35.5** | Individual spell undertuned (WR: 40.5%, Casts: 1827, mult: 1.034) |
| `FEL` | Beasts | Buff / Sustain | 36.8 -> **38.3** (+4.1%) | - | 36.8 -> **38.3** | Individual spell undertuned (WR: 39.0%, Casts: 2360, mult: 1.040) |
| `EFF` | Beasts | Debuff / Control | 0.6 -> **0.5** (-16.7%) | 1022.8 -> **1395.2** | 614.3 -> **698.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 1838). Increasing spread: b -17.7%, n +36.4%; Individual spell overtuned (WR: 55.7%, Casts: 1838, mult: 0.981) |
| `EFW` | Beasts | Buff / Sustain | 22.5 -> **21.8** (-3.1%) | - | 22.5 -> **21.8** | Individual spell overtuned (WR: 59.0%, Casts: 1347, mult: 0.968) |
| `EFL` | Beasts | Buff / Sustain | 1.7 -> **1.5** (-11.8%) | - | 1.7 -> **1.5** | Individual spell overtuned (WR: 81.9%, Casts: 1116, mult: 0.872) |
| `EFD` | Beasts | Ultimate | 31.3 -> **31.3** (+0.0%) | 238.6 -> **321.1** | 7499.5 -> **10081.7** | Status 'Entangled' beneficiaries undertuned (WR: 44.7%); Location 'Jungle' beneficiaries undertuned (WR: 46.0%) |
| `FLF` | Lightning | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 1647.3 -> **2316.3** | 1483.5 -> **1853.8** | Status 'Stunned' beneficiaries undertuned (WR: 42.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 2386). Increasing spread: b -17.8%, n +36.7% |
| `FLW` | Lightning | Debuff / Control | 100.9 -> **110.6** (+9.6%) | - | 100.9 -> **110.6** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 62.8%, Casts: 1940, mult: 0.953) |
| `FLE` | Lightning | Setup - Weather | 93.1 -> **107.1** (+15.0%) | - | 93.1 -> **107.1** | Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLL` | Lightning | Buff / Sustain | 32.2 -> **34.0** (+5.6%) | - | 32.2 -> **34.0** | Individual spell undertuned (WR: 35.1%, Casts: 2054, mult: 1.055) |
| `FLD` | Lightning | Ultimate | 77.7 -> **77.7** (+0.0%) | 42.0 -> **56.2** | 3341.1 -> **4444.4** | Status 'Stunned' beneficiaries undertuned (WR: 42.8%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1729). Shifted tuner focus: protected ultimate base floor at 77.7 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 879.6 -> **1193.8** | 616.4 -> **716.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 974). Increasing spread: b -17.4%, n +35.7% |
| `LFW` | Lightning | Buff / Sustain | 26.4 -> **25.6** (-3.0%) | - | 26.4 -> **25.6** | Individual spell overtuned (WR: 59.1%, Casts: 1276, mult: 0.968) |
| `LFL` | Lightning | Debuff / Control | 50.8 -> **56.9** (+12.0%) | 311.9 -> **398.3** | 15895.3 -> **22720.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.2% vs 30% floor, Casts: 2779). Increasing spread: b -13.5%, n +27.7%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 2.0 -> **1.7** (-15.0%) | 613.4 -> **823.8** | 1228.8 -> **1402.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.2% vs 30% floor, Casts: 1736). Increasing spread: b -16.7%, n +34.3% |
| `FDF` | Blood | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 1156.6 -> **1584.5** | 694.6 -> **792.8** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1617). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 62.2 -> **60.8** (-2.3%) | - | 62.2 -> **60.8** | Class Blood overtuned (WR: 55.5%, factor: 0.978) |
| `FDE` | Blood | Setup - Weather | 17.3 -> **16.9** (-2.3%) | - | 17.3 -> **16.9** | Class Blood overtuned (WR: 55.5%, factor: 0.978) |
| `FDL` | Blood | Debuff / Control | 6.3 -> **5.4** (-14.3%) | - | 6.3 -> **5.4** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Status 'Bleeding' appliers overtuned on own (WR: 63.2%) |
| `FDD` | Blood | Ultimate | 49.6 -> **48.5** (-2.2%) | 29.2 -> **37.8** | 1497.9 -> **1881.8** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.4% vs 16% floor, Casts: 1225). Shifted tuner focus: protected ultimate base floor at 49.6 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 479.1 -> **647.6** | 384.1 -> **454.0** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Status 'Bleeding' beneficiaries undertuned (WR: 44.8%) |
| `DFW` | Blood | Debuff / Control | 13.7 -> **11.7** (-14.6%) | - | 13.7 -> **11.7** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Status 'Bleeding' appliers overtuned on own (WR: 63.2%) |
| `DFE` | Blood | Buff / Sustain | 46.3 -> **46.5** (+0.4%) | - | 46.3 -> **46.5** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Individual spell undertuned (WR: 42.3%, Casts: 1288, mult: 1.027) |
| `DFL` | Blood | Buff / Sustain | 30.1 -> **29.4** (-2.3%) | - | 30.1 -> **29.4** | Class Blood overtuned (WR: 55.5%, factor: 0.978) |
| `DFD` | Blood | Conditional Strike | 270.1 -> **300.3** (+11.2%) | 0.1 -> **0.1** | 297.1 -> **330.3** | Class Blood overtuned (WR: 55.5%, factor: 0.978); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.2% vs 55% ceiling, WR: 60.3%). Compressing spread: b +18.1%, n -26.4% |
| `WEF` | Plants | Conditional Strike | 1.8 -> **1.6** (-11.1%) | 310.1 -> **405.1** | 560.0 -> **649.8** | Location 'Jungle' beneficiaries undertuned (WR: 46.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.1% vs 30% floor, Casts: 1974). Increasing spread: b -14.0%, n +28.6% |
| `WEW` | Plants | Debuff / Control | 482.4 -> **575.1** (+19.2%) | - | 482.4 -> **575.1** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 39.8%, Casts: 1818, mult: 1.037) |
| `WEL` | Plants | Debuff / Control | 26.8 -> **26.0** (-3.0%) | - | 26.8 -> **26.0** | Status 'Entangled' appliers overtuned on own (WR: 54.6%); Individual spell overtuned (WR: 54.6%, Casts: 2370, mult: 0.985) |
| `WED` | Plants | Conditional Strike | 10.1 -> **11.4** (+12.9%) | 33.9 -> **31.9** | 352.5 -> **375.1** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1418, WR: 37.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 37.8%, Casts: 1418, mult: 1.044) |
| `EWF` | Plants | Buff / Sustain | 1.5 -> **1.3** (-13.3%) | 211.5 -> **283.7** | 318.8 -> **370.1** | Weather 'Sunny' beneficiaries undertuned (WR: 44.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.9% vs 30% floor, Casts: 2432). Increasing spread: b -15.3%, n +31.3% |
| `EWW` | Plants | Debuff / Control | 2.7 -> **2.3** (-14.8%) | - | 2.7 -> **2.3** | Individual spell overtuned (WR: 83.5%, Casts: 1690, mult: 0.865) |
| `EWL` | Plants | Debuff / Control | 73.9 -> **74.9** (+1.4%) | - | 73.9 -> **74.9** | Individual spell undertuned (WR: 45.7%, Casts: 2778, mult: 1.014) |
| `EWD` | Plants | Conditional Strike | 3.4 -> **2.8** (-17.6%) | 914.5 -> **1249.0** | 3112.7 -> **3500.0** | Status 'Bleeding' appliers overtuned on own (WR: 63.2%); Status 'Entangled' beneficiaries undertuned (WR: 44.7%) |
| `WLF` | Fey | Conditional Strike | 1.5 -> **1.4** (-6.7%) | 682.3 -> **920.4** | 1024.9 -> **1290.0** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Status 'Cursed' beneficiaries undertuned (WR: 44.2%) |
| `WLW` | Fey | Debuff / Control | 58.5 -> **59.4** (+1.5%) | - | 58.5 -> **59.4** | Class Fey undertuned (WR: 46.2%, factor: 1.015) |
| `WLE` | Fey | Setup - Location | 277.8 -> **310.6** (+11.8%) | - | 277.8 -> **310.6** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Location 'Enchanted Forest' appliers overtuned on own (WR: 56.2%) |
| `WLL` | Fey | Direct Damage | 58.0 -> **58.9** (+1.6%) | - | 58.0 -> **58.9** | Class Fey undertuned (WR: 46.2%, factor: 1.015) |
| `WLD` | Fey | Ultimate | 24.3 -> **23.8** (-2.1%) | 546.8 -> **696.7** | 13311.5 -> **16605.3** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Location 'Enchanted Forest' beneficiaries overtuned (WR: 55.0%) |
| `LWF` | Fey | Debuff / Control | 35.4 -> **31.7** (-10.5%) | 169.3 -> **205.9** | 6028.6 -> **6558.7** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Location 'Enchanted Forest' beneficiaries overtuned (WR: 55.0%) |
| `LWW` | Fey | Debuff / Control | 46.6 -> **48.8** (+4.7%) | - | 46.6 -> **48.8** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Individual spell undertuned (WR: 41.3%, Casts: 1081, mult: 1.031) |
| `LWL` | Fey | Debuff / Control | 52.4 -> **54.0** (+3.1%) | - | 52.4 -> **54.0** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Individual spell undertuned (WR: 45.5%, Casts: 1213, mult: 1.015) |
| `LWD` | Fey | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 1156.6 -> **1584.5** | 1041.8 -> **1268.4** | Class Fey undertuned (WR: 46.2%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1352). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 1.9 -> **1.6** (-15.8%) | 1120.4 -> **1528.8** | 2130.7 -> **2447.7** | Weather 'Raining' beneficiaries undertuned (WR: 43.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.7% vs 30% floor, Casts: 2346). Increasing spread: b -16.1%, n +33.1% |
| `WDW` | Ice | Buff / Sustain | 12.2 -> **11.6** (-4.9%) | - | 12.2 -> **11.6** | Status 'Frosty' appliers overtuned on own (WR: 54.3%); Individual spell overtuned (WR: 59.9%, Casts: 2782, mult: 0.965) |
| `WDE` | Ice | Setup - Weather | 31.0 -> **32.3** (+4.2%) | - | 31.0 -> **32.3** | Individual spell undertuned (WR: 38.1%, Casts: 1844, mult: 1.043) |
| `WDL` | Ice | Debuff / Control | 41.4 -> **40.8** (-1.4%) | - | 41.4 -> **40.8** | Status 'Frosty' appliers overtuned on own (WR: 54.3%) |
| `WDD` | Ice | Ultimate | 35.2 -> **35.2** (+0.0%) | 133.2 -> **171.0** | 4723.8 -> **6054.4** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 1.3% vs 16% floor, Casts: 1698). Shifted tuner focus: protected ultimate base floor at 35.2 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWF` | Ice | Debuff / Control | 39.0 -> **38.4** (-1.5%) | - | 39.0 -> **38.4** | Status 'Frosty' appliers overtuned on own (WR: 54.3%) |
| `DWE` | Ice | Setup - Location | 35.1 -> **37.0** (+5.4%) | - | 35.1 -> **37.0** | Location 'Tundra' appliers undertuned (WR: 42.4%, casts: 1519); Individual spell undertuned (WR: 42.4%, Casts: 1519, mult: 1.026) |
| `DWL` | Ice | Debuff / Control | 41.5 -> **40.9** (-1.4%) | - | 41.5 -> **40.9** | Status 'Frosty' appliers overtuned on own (WR: 54.3%) |
| `DWD` | Ice | Conditional Strike | 4.9 -> **4.5** (-8.2%) | 95.9 -> **122.9** | 474.8 -> **557.6** | Status 'Frosty' beneficiaries undertuned (WR: 42.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.1% vs 30% floor, Casts: 2246). Increasing spread: b -11.9%, n +24.4% |
| `ELF` | Wind | Conditional Strike | 3.2 -> **2.9** (-9.4%) | 518.1 -> **697.1** | 1661.1 -> **2024.5** | Class Wind undertuned (WR: 45.7%, factor: 1.017); Status 'Bleeding' beneficiaries undertuned (WR: 44.8%) |
| `ELW` | Wind | Debuff / Control | 115.8 -> **116.3** (+0.4%) | - | 115.8 -> **116.3** | Class Wind undertuned (WR: 45.7%, factor: 1.017); Individual spell overtuned (WR: 53.8%, Casts: 1253, mult: 0.988) |
| `ELE` | Wind | Setup - Weather | 25.3 -> **25.7** (+1.6%) | - | 25.3 -> **25.7** | Class Wind undertuned (WR: 45.7%, factor: 1.017) |
| `ELL` | Wind | Buff / Sustain | 39.3 -> **40.6** (+3.3%) | - | 39.3 -> **40.6** | Class Wind undertuned (WR: 45.7%, factor: 1.017); Individual spell undertuned (WR: 45.2%, Casts: 1773, mult: 1.016) |
| `ELD` | Wind | Conditional Strike | 1.9 -> **1.7** (-10.5%) | 910.9 -> **1238.3** | 1732.6 -> **2106.8** | Class Wind undertuned (WR: 45.7%, factor: 1.017); Weather 'Raining' beneficiaries undertuned (WR: 43.8%) |
| `LEF` | Wind | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 528.4 -> **697.6** | 635.3 -> **698.6** | Class Wind undertuned (WR: 45.7%, factor: 1.017); Status 'Burning' beneficiaries undertuned (WR: 44.6%) |
| `LEW` | Wind | Debuff / Control | 53.5 -> **53.6** (+0.2%) | - | 53.5 -> **53.6** | Class Wind undertuned (WR: 45.7%, factor: 1.017); Individual spell overtuned (WR: 54.3%, Casts: 3040, mult: 0.986) |
| `LEE` | Wind | Setup - Weather | 22.4 -> **23.4** (+4.5%) | - | 22.4 -> **23.4** | Class Wind undertuned (WR: 45.7%, factor: 1.017); Individual spell undertuned (WR: 41.9%, Casts: 1679, mult: 1.028) |
| `LEL` | Wind | Buff / Sustain | 113.1 -> **115.0** (+1.7%) | - | 113.1 -> **115.0** | Class Wind undertuned (WR: 45.7%, factor: 1.017) |
| `EDF` | Poison | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 473.0 -> **613.6** | 379.2 -> **430.2** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 2558). Increasing spread: b -14.5%, n +29.7% |
| `EDW` | Poison | Debuff / Control | 11.7 -> **10.9** (-6.8%) | - | 11.7 -> **10.9** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 61.3%, Casts: 1627, mult: 0.959) |
| `EDE` | Poison | Setup - Location | 51.7 -> **48.5** (-6.2%) | - | 51.7 -> **48.5** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Location 'Swamp' appliers overtuned on own (WR: 55.5%) |
| `EDL` | Poison | Debuff / Control | 0.8 -> **0.7** (-12.5%) | - | 0.8 -> **0.7** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 84.7%, Casts: 2022, mult: 0.859) |
| `EDD` | Poison | Ultimate | 47.0 -> **50.3** (+7.0%) | 26.4 -> **25.8** | 1287.8 -> **1348.0** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Status 'Bleeding' beneficiaries undertuned (WR: 44.8%) |
| `DEF` | Poison | Conditional Strike | 31.9 -> **31.1** (-2.5%) | 1.4 -> **1.4** | 76.6 -> **74.6** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 51.7% within [30%-55%] target window, WR: 49.4%). |
| `DEW` | Poison | Debuff / Control | 14.0 -> **13.1** (-6.4%) | - | 14.0 -> **13.1** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 60.9%, Casts: 2302, mult: 0.961) |
| `DEE` | Poison | Debuff / Control | 46.8 -> **44.2** (-5.6%) | - | 46.8 -> **44.2** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 58.8%, Casts: 1329, mult: 0.969) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 523.3 -> **703.7** | 104.9 -> **140.9** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Status 'Bleeding' beneficiaries undertuned (WR: 44.8%) |
| `DED` | Poison | Debuff / Control | 22.3 -> **22.0** (-1.3%) | - | 22.3 -> **22.0** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell undertuned (WR: 46.2%, Casts: 1686, mult: 1.012) |
| `LDF` | Cosmic | Debuff / Control | 139.1 -> **137.1** (-1.4%) | - | 139.1 -> **137.1** | Individual spell overtuned (WR: 54.3%, Casts: 1137, mult: 0.986) |
| `LDL` | Cosmic | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 674.3 -> **908.7** | 945.4 -> **1091.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.7% vs 30% floor, Casts: 1155). Increasing spread: b -16.9%, n +34.8% |
| `LDD` | Cosmic | Ultimate | 66.6 -> **73.4** (+10.2%) | 30.0 -> **28.2** | 2064.6 -> **2143.3** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2410, WR: 44.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 44.0%, Casts: 2410, mult: 1.020) |
| `DLF` | Cosmic | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 535.6 -> **714.9** | 697.6 -> **787.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.2% vs 30% floor, Casts: 1914). Increasing spread: b -16.3%, n +33.5%; Individual spell overtuned (WR: 57.1%, Casts: 1914, mult: 0.976) |
| `DLE` | Cosmic | Direct Damage | 48.9 -> **50.5** (+3.3%) | - | 48.9 -> **50.5** | Individual spell undertuned (WR: 40.6%, Casts: 1554, mult: 1.034) |
| `DLL` | Cosmic | Conditional Strike | 4.1 -> **3.6** (-12.2%) | 243.3 -> **313.0** | 1001.6 -> **1130.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.0% vs 30% floor, Casts: 2219). Increasing spread: b -14.0%, n +28.7%; Individual spell undertuned (WR: 45.0%, Casts: 2219, mult: 1.017) |
