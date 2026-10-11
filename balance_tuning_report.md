# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T01:54:24Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 541.6s  
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
| **Earth** | 9,116 | 56.1% | 56.1% | 17.1 | Overtuned ⚠️ |
| **Poison** | 20,964 | 55.2% | 55.2% | 10.4 | Overtuned ⚠️ |
| **Blood** | 20,329 | 55.0% | 55.0% | 18.4 | Overtuned ⚠️ |
| **Ghostfire** | 19,605 | 52.7% | 52.8% | 25.4 | Balanced ✅ |
| **Light** | 9,248 | 51.5% | 51.5% | 18.9 | Balanced ✅ |
| **Beasts** | 19,656 | 50.7% | 50.7% | 11.8 | Balanced ✅ |
| **Fire** | 7,837 | 50.5% | 50.5% | 17.2 | Balanced ✅ |
| **Ice** | 18,952 | 50.1% | 50.1% | 16.6 | Balanced ✅ |
| **Dark** | 9,781 | 49.1% | 49.1% | 38.9 | Balanced ✅ |
| **Lightning** | 21,011 | 49.0% | 49.0% | 15.9 | Balanced ✅ |
| **Cosmic** | 17,903 | 48.6% | 48.6% | 17.2 | Balanced ✅ |
| **Wind** | 18,272 | 47.0% | 47.0% | 8.4 | Balanced ✅ |
| **Plants** | 19,824 | 46.6% | 46.6% | 8.0 | Balanced ✅ |
| **Water** | 10,340 | 46.6% | 46.6% | 12.3 | Balanced ✅ |
| **Fey** | 17,813 | 45.9% | 45.9% | 42.0 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,313 (55.7%) | 3,924 (42.9%) | 19.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,639 (47.1%) | 4,725 (45.6%) | 5.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,984 (51.9%) | 4,098 (45.7%) | 8.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,754 (63.2%) | 8,819 (44.6%) | 4.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 12,291 (50.1%) | 4,971 (45.0%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,079 (53.4%) | 6,939 (46.3%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,258 (39.4%) | 4,035 (43.0%) | 5.6% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 39.1 -> **39.6** (+1.3%) | - | 39.1 -> **39.6** | Individual spell undertuned (WR: 46.1%, Casts: 2042, mult: 1.013) |
| `FFD` | Fire | Conditional Strike | 1.7 -> **1.5** (-11.8%) | 247.1 -> **326.0** | 421.8 -> **490.5** | Status 'Burning' beneficiaries undertuned (WR: 45.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 824). Increasing spread: b -14.5%, n +29.7% |
| `WWF` | Water | Conditional Strike | 4.1 -> **3.6** (-12.2%) | 136.6 -> **177.5** | 564.2 -> **642.6** | Status 'Burning' beneficiaries undertuned (WR: 45.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.1% vs 30% floor, Casts: 1499). Increasing spread: b -13.6%, n +27.8% |
| `WWE` | Water | Setup - Weather | 59.0 -> **63.5** (+7.6%) | - | 59.0 -> **63.5** | Weather 'Raining' appliers undertuned (WR: 39.4%, casts: 2258); Individual spell undertuned (WR: 39.3%, Casts: 2258, mult: 1.038) |
| `EEF` | Earth | Conditional Strike | 18.9 -> **21.2** (+12.2%) | 27.9 -> **33.1** | 546.2 -> **722.9** | Class Earth overtuned (WR: 56.1%, factor: 0.976); Status 'Frosty' beneficiaries undertuned (WR: 42.9%) |
| `EEW` | Earth | Buff / Sustain | 22.0 -> **20.5** (-6.8%) | - | 22.0 -> **20.5** | Class Earth overtuned (WR: 56.1%, factor: 0.976); Individual spell overtuned (WR: 62.6%, Casts: 1988, mult: 0.954) |
| `EED` | Earth | Direct Damage | 7.3 -> **7.1** (-2.7%) | - | 7.3 -> **7.1** | Class Earth overtuned (WR: 56.1%, factor: 0.976) |
| `LLF` | Light | Conditional Strike | 6.1 -> **7.0** (+14.8%) | 330.4 -> **442.5** | 2021.5 -> **3104.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.7% vs 30% floor, Casts: 2734). Increasing spread: b -16.5%, n +33.9%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 90.0 -> **103.5** (+15.0%) | - | 90.0 -> **103.5** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LLE` | Light | Setup - Weather | 119.4 -> **137.3** (+15.0%) | - | 119.4 -> **137.3** | Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 19.0 -> **18.1** (-4.7%) | - | 19.0 -> **18.1** | Individual spell overtuned (WR: 62.4%, Casts: 1285, mult: 0.955) |
| `LLD` | Light | Ultimate | 36.0 -> **36.0** (+0.0%) | 71.6 -> **94.6** | 2613.6 -> **3441.6** | Weather 'Sunny' beneficiaries undertuned (WR: 45.6%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1985). Shifted tuner focus: protected ultimate base floor at 36.0 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 614.7 -> **842.1** | 492.6 -> **590.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1899). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 41.2%, Casts: 1899, mult: 1.031) |
| `DDW` | Dark | Debuff / Control | 111.2 -> **127.9** (+15.0%) | - | 111.2 -> **127.9** | Buffed setup spell [DDW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DDE` | Dark | Setup - Weather | 151.9 -> **181.7** (+19.6%) | - | 151.9 -> **181.7** | Weather 'Darkness' appliers undertuned (WR: 44.2%, casts: 2021); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `DDL` | Dark | Debuff / Control | 52.9 -> **59.1** (+11.7%) | - | 52.9 -> **59.1** | Buffed setup spell [DDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 58.0%, Casts: 1765, mult: 0.972) |
| `DDD` | Dark | Debuff / Control | 20.6 -> **20.2** (-1.9%) | - | 20.6 -> **20.2** | Individual spell overtuned (WR: 55.8%, Casts: 1566, mult: 0.980) |
| `FWF` | Ghostfire | Debuff / Control | 23.1 -> **22.6** (-2.2%) | - | 23.1 -> **22.6** | Individual spell overtuned (WR: 56.3%, Casts: 1898, mult: 0.978) |
| `FWW` | Ghostfire | Debuff / Control | 64.5 -> **71.8** (+11.3%) | - | 64.5 -> **71.8** | Status 'Cursed' appliers overtuned on own (WR: 54.1%); Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 180.0 -> **207.0** (+15.0%) | - | 180.0 -> **207.0** | Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 155.0 -> **170.9** (+10.3%) | - | 155.0 -> **170.9** | Status 'Cursed' appliers overtuned on own (WR: 54.1%); Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 50.2 -> **49.3** (-1.8%) | 68.2 -> **86.0** | 3473.8 -> **4289.1** | Location 'Graveyard' beneficiaries overtuned (WR: 55.5%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.4% vs 8% floor, Casts: 1140). Shifted tuner focus: protected ultimate base floor at 50.2 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 286.5 -> **392.2** | 460.0 -> **550.5** | Status 'Bleeding' beneficiaries undertuned (WR: 44.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.6% vs 30% floor, Casts: 1943). Increasing spread: b -16.6%, n +34.0% |
| `WFW` | Ghostfire | Debuff / Control | 24.8 -> **24.0** (-3.2%) | - | 24.8 -> **24.0** | Individual spell overtuned (WR: 58.9%, Casts: 2482, mult: 0.969) |
| `WFE` | Ghostfire | Debuff / Control | 15.1 -> **13.0** (-13.9%) | - | 15.1 -> **13.0** | Status 'Bleeding' appliers overtuned on own (WR: 63.2%); Individual spell overtuned (WR: 74.2%, Casts: 1874, mult: 0.906) |
| `WFL` | Ghostfire | Buff / Sustain | 44.2 -> **45.5** (+2.9%) | - | 44.2 -> **45.5** | Individual spell undertuned (WR: 41.6%, Casts: 3365, mult: 1.030) |
| `WFD` | Ghostfire | Conditional Strike | 2.3 -> **2.0** (-13.0%) | 209.3 -> **269.0** | 483.7 -> **540.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.2% vs 30% floor, Casts: 1549). Increasing spread: b -13.9%, n +28.5%; Individual spell undertuned (WR: 43.1%, Casts: 1549, mult: 1.024) |
| `FEF` | Beasts | Debuff / Control | 62.7 -> **72.1** (+15.0%) | - | 62.7 -> **72.1** | Buffed setup spell [FEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `FEW` | Beasts | Conditional Strike | 0.9 -> **0.7** (-22.2%) | 621.2 -> **858.6** | 560.0 -> **601.7** | Status 'Entangled' beneficiaries undertuned (WR: 46.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.0% vs 30% floor, Casts: 2056). Increasing spread: b -17.6%, n +36.2% |
| `FEE` | Beasts | Buff / Sustain | 33.0 -> **33.8** (+2.4%) | - | 33.0 -> **33.8** | Individual spell undertuned (WR: 43.1%, Casts: 2460, mult: 1.024) |
| `EFF` | Beasts | Debuff / Control | 1.0 -> **0.8** (-20.0%) | 547.8 -> **748.1** | 548.8 -> **599.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 1696). Increasing spread: b -17.8%, n +36.6%; Individual spell overtuned (WR: 58.8%, Casts: 1696, mult: 0.969) |
| `EFL` | Beasts | Buff / Sustain | 2.3 -> **2.0** (-13.0%) | - | 2.3 -> **2.0** | Individual spell overtuned (WR: 84.6%, Casts: 1076, mult: 0.860) |
| `EFD` | Beasts | Ultimate | 32.2 -> **32.2** (+0.0%) | 140.0 -> **184.1** | 4540.2 -> **5960.2** | Status 'Entangled' beneficiaries undertuned (WR: 46.3%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.3% vs 16% floor, Casts: 2086). Shifted tuner focus: protected ultimate base floor at 32.2 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo. |
| `FLF` | Lightning | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 835.3 -> **1165.9** | 919.9 -> **1166.9** | Status 'Stunned' beneficiaries undertuned (WR: 45.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 2657). Increasing spread: b -17.9%, n +36.8% |
| `FLW` | Lightning | Debuff / Control | 82.0 -> **91.4** (+11.5%) | - | 82.0 -> **91.4** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 58.6%, Casts: 2128, mult: 0.970) |
| `FLE` | Lightning | Setup - Weather | 65.9 -> **78.0** (+18.4%) | - | 65.9 -> **78.0** | Weather 'Storming' appliers undertuned (WR: 45.8%, casts: 2416); Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLL` | Lightning | Buff / Sustain | 30.4 -> **31.2** (+2.6%) | - | 30.4 -> **31.2** | Individual spell undertuned (WR: 42.4%, Casts: 2038, mult: 1.026) |
| `FLD` | Lightning | Ultimate | 80.5 -> **77.7** (-3.5%) | 24.5 -> **31.2** | 2052.8 -> **2501.9** | Status 'Stunned' beneficiaries undertuned (WR: 45.0%); Weather 'Storming' beneficiaries overtuned (WR: 59.7%) |
| `LFF` | Lightning | Conditional Strike | 1.0 -> **0.8** (-20.0%) | 479.7 -> **649.5** | 480.7 -> **520.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1356). Increasing spread: b -17.2%, n +35.4%; Individual spell undertuned (WR: 45.5%, Casts: 1356, mult: 1.015) |
| `LFW` | Lightning | Buff / Sustain | 28.2 -> **27.6** (-2.1%) | - | 28.2 -> **27.6** | Individual spell overtuned (WR: 55.9%, Casts: 1441, mult: 0.980) |
| `LFE` | Lightning | Debuff / Control | 54.1 -> **54.8** (+1.3%) | - | 54.1 -> **54.8** | Individual spell undertuned (WR: 46.1%, Casts: 2092, mult: 1.013) |
| `LFL` | Lightning | Debuff / Control | 40.0 -> **45.0** (+12.5%) | 184.3 -> **241.6** | 7412.0 -> **10917.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.1% vs 30% floor, Casts: 3061). Increasing spread: b -15.2%, n +31.1%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 2.9 -> **2.4** (-17.2%) | 348.1 -> **462.7** | 1012.4 -> **1112.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 1508). Increasing spread: b -16.0%, n +32.9% |
| `FDF` | Blood | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 616.2 -> **844.2** | 493.8 -> **591.6** | Class Blood overtuned (WR: 55.0%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1783). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 65.1 -> **63.8** (-2.0%) | - | 65.1 -> **63.8** | Class Blood overtuned (WR: 55.0%, factor: 0.980) |
| `FDE` | Blood | Setup - Weather | 18.9 -> **18.1** (-4.2%) | - | 18.9 -> **18.1** | Class Blood overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 57.2%, Casts: 2141, mult: 0.975) |
| `FDL` | Blood | Debuff / Control | 8.9 -> **7.5** (-15.7%) | - | 8.9 -> **7.5** | Class Blood overtuned (WR: 55.0%, factor: 0.980); Status 'Bleeding' appliers overtuned on own (WR: 63.2%) |
| `FDD` | Blood | Ultimate | 51.9 -> **50.9** (-1.9%) | 17.4 -> **22.5** | 955.0 -> **1196.1** | Class Blood overtuned (WR: 55.0%, factor: 0.980); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.5% vs 16% floor, Casts: 1686). Shifted tuner focus: protected ultimate base floor at 51.9 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 264.8 -> **356.0** | 319.0 -> **357.0** | Class Blood overtuned (WR: 55.0%, factor: 0.980); Status 'Bleeding' beneficiaries undertuned (WR: 44.6%) |
| `DFW` | Blood | Debuff / Control | 14.7 -> **14.3** (-2.7%) | - | 14.7 -> **14.3** | Class Blood overtuned (WR: 55.0%, factor: 0.980); Status 'Bleeding' appliers overtuned on own (WR: 63.2%) |
| `DFE` | Blood | Buff / Sustain | 43.2 -> **44.5** (+3.0%) | - | 43.2 -> **44.5** | Class Blood overtuned (WR: 55.0%, factor: 0.980); Individual spell undertuned (WR: 36.2%, Casts: 1960, mult: 1.051) |
| `DFL` | Blood | Buff / Sustain | 31.5 -> **30.9** (-1.9%) | - | 31.5 -> **30.9** | Class Blood overtuned (WR: 55.0%, factor: 0.980) |
| `DFD` | Blood | Conditional Strike | 219.7 -> **244.8** (+11.4%) | 0.1 -> **0.1** | 241.7 -> **269.3** | Class Blood overtuned (WR: 55.0%, factor: 0.980); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.5% vs 55% ceiling, WR: 60.8%). Compressing spread: b +18.3%, n -26.7% |
| `WEF` | Plants | Conditional Strike | 2.3 -> **2.0** (-13.0%) | 187.7 -> **241.2** | 434.0 -> **484.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.2% vs 30% floor, Casts: 1566). Increasing spread: b -13.9%, n +28.5%; Individual spell undertuned (WR: 41.2%, Casts: 1566, mult: 1.031) |
| `WEW` | Plants | Debuff / Control | 327.8 -> **395.7** (+20.7%) | - | 327.8 -> **395.7** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 36.5%, Casts: 2555, mult: 1.050) |
| `WEE` | Plants | Setup - Location | 20.7 -> **19.0** (-8.2%) | - | 20.7 -> **19.0** | Location 'Jungle' appliers overtuned on own (WR: 61.6%); Individual spell overtuned (WR: 61.6%, Casts: 858, mult: 0.958) |
| `WED` | Plants | Conditional Strike | 8.3 -> **9.2** (+10.8%) | 38.4 -> **36.1** | 327.0 -> **341.3** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.8% vs 8% floor, Casts: 1198, WR: 42.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 42.2%, Casts: 1198, mult: 1.027) |
| `EWF` | Plants | Buff / Sustain | 1.9 -> **1.7** (-10.5%) | 121.5 -> **160.4** | 232.8 -> **274.4** | Weather 'Sunny' beneficiaries undertuned (WR: 45.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 2740). Increasing spread: b -14.5%, n +29.7% |
| `EWW` | Plants | Debuff / Control | 3.5 -> **3.1** (-11.4%) | - | 3.5 -> **3.1** | Individual spell overtuned (WR: 81.8%, Casts: 1652, mult: 0.872) |
| `EWD` | Plants | Conditional Strike | 4.9 -> **4.1** (-16.3%) | 493.0 -> **677.4** | 2420.6 -> **2781.4** | Status 'Bleeding' appliers overtuned on own (WR: 63.2%); Status 'Entangled' beneficiaries undertuned (WR: 46.3%) |
| `WLF` | Fey | Conditional Strike | 1.9 -> **1.7** (-10.5%) | 387.2 -> **505.4** | 737.6 -> **860.9** | Class Fey undertuned (WR: 45.9%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 1672). Increasing spread: b -14.9%, n +30.5% |
| `WLW` | Fey | Debuff / Control | 57.4 -> **57.5** (+0.2%) | - | 57.4 -> **57.5** | Class Fey undertuned (WR: 45.9%, factor: 1.016); Status 'Cursed' appliers overtuned on own (WR: 54.1%) |
| `WLE` | Fey | Setup - Location | 218.1 -> **237.2** (+8.8%) | - | 218.1 -> **237.2** | Class Fey undertuned (WR: 45.9%, factor: 1.016); Location 'Enchanted Forest' appliers overtuned on own (WR: 60.0%) |
| `WLL` | Fey | Direct Damage | 57.1 -> **57.0** (-0.2%) | - | 57.1 -> **57.0** | Class Fey undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 55.4%, Casts: 1649, mult: 0.982) |
| `WLD` | Fey | Ultimate | 25.3 -> **24.8** (-2.0%) | 328.2 -> **426.7** | 8328.8 -> **10607.0** | Class Fey undertuned (WR: 45.9%, factor: 1.016); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1405). Shifted tuner focus: protected ultimate base floor at 25.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 25.4 -> **30.2** (+18.9%) | 110.2 -> **138.2** | 2824.5 -> **4203.8** | Class Fey undertuned (WR: 45.9%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.9% vs 30% floor, Casts: 2697). Increasing spread: b -12.5%, n +25.4% |
| `LWW` | Fey | Debuff / Control | 45.1 -> **45.8** (+1.6%) | - | 45.1 -> **45.8** | Class Fey undertuned (WR: 45.9%, factor: 1.016) |
| `LWL` | Fey | Debuff / Control | 48.7 -> **50.3** (+3.3%) | - | 48.7 -> **50.3** | Class Fey undertuned (WR: 45.9%, factor: 1.016); Individual spell undertuned (WR: 44.9%, Casts: 1789, mult: 1.017) |
| `LWD` | Fey | Conditional Strike | 1.1 -> **1.0** (-9.1%) | 616.2 -> **844.2** | 678.9 -> **845.2** | Class Fey undertuned (WR: 45.9%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1849). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 2.6 -> **2.2** (-15.4%) | 594.3 -> **812.7** | 1547.8 -> **1790.1** | Weather 'Raining' beneficiaries undertuned (WR: 43.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.8% vs 30% floor, Casts: 2745). Increasing spread: b -16.1%, n +33.0% |
| `WDW` | Ice | Buff / Sustain | 13.2 -> **12.6** (-4.5%) | - | 13.2 -> **12.6** | Status 'Frosty' appliers overtuned on own (WR: 55.7%); Individual spell overtuned (WR: 58.2%, Casts: 3172, mult: 0.971) |
| `WDL` | Ice | Debuff / Control | 43.4 -> **42.0** (-3.2%) | - | 43.4 -> **42.0** | Status 'Frosty' appliers overtuned on own (WR: 55.7%); Individual spell overtuned (WR: 54.2%, Casts: 752, mult: 0.986) |
| `WDD` | Ice | Ultimate | 32.2 -> **35.2** (+9.3%) | 108.0 -> **104.5** | 3509.8 -> **3713.6** | Weather 'Blizzard' beneficiaries undertuned (WR: 46.3%); Location 'Tundra' beneficiaries undertuned (WR: 46.3%) |
| `DWF` | Ice | Debuff / Control | 40.4 -> **39.6** (-2.0%) | - | 40.4 -> **39.6** | Status 'Frosty' appliers overtuned on own (WR: 55.7%) |
| `DWW` | Ice | Debuff / Control | 80.0 -> **90.1** (+12.6%) | - | 80.0 -> **90.1** | Buffed setup spell [DWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 56.0%, Casts: 1401, mult: 0.980) |
| `DWE` | Ice | Setup - Location | 36.2 -> **35.1** (-3.0%) | - | 36.2 -> **35.1** | Location 'Tundra' appliers overtuned on own (WR: 54.4%); Individual spell overtuned (WR: 54.4%, Casts: 1895, mult: 0.986) |
| `DWL` | Ice | Debuff / Control | 44.8 -> **43.0** (-4.0%) | - | 44.8 -> **43.0** | Status 'Frosty' appliers overtuned on own (WR: 55.7%); Individual spell overtuned (WR: 55.8%, Casts: 2016, mult: 0.980) |
| `DWD` | Ice | Conditional Strike | 5.8 -> **5.4** (-6.9%) | 59.9 -> **76.4** | 353.2 -> **418.0** | Status 'Frosty' beneficiaries undertuned (WR: 42.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.6% vs 30% floor, Casts: 2311). Increasing spread: b -11.8%, n +24.0% |
| `ELF` | Wind | Conditional Strike | 4.0 -> **3.5** (-12.5%) | 286.0 -> **388.0** | 1148.0 -> **1361.5** | Status 'Bleeding' beneficiaries undertuned (WR: 44.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.0% vs 30% floor, Casts: 996). Increasing spread: b -16.0%, n +32.8% |
| `ELW` | Wind | Debuff / Control | 86.1 -> **99.0** (+15.0%) | - | 86.1 -> **99.0** | Buffed setup spell [ELW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `ELE` | Wind | Setup - Weather | 24.2 -> **24.5** (+1.2%) | - | 24.2 -> **24.5** | Individual spell undertuned (WR: 45.9%, Casts: 1438, mult: 1.013) |
| `ELD` | Wind | Conditional Strike | 2.4 -> **2.1** (-12.5%) | 495.3 -> **666.6** | 1191.1 -> **1402.0** | Weather 'Raining' beneficiaries undertuned (WR: 43.0%); Weather 'Blizzard' appliers undertuned (WR: 43.5%, casts: 1290) |
| `LEF` | Wind | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 289.6 -> **389.0** | 465.0 -> **546.0** | Status 'Burning' beneficiaries undertuned (WR: 45.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.9% vs 30% floor, Casts: 1775). Increasing spread: b -15.6%, n +32.1% |
| `LEW` | Wind | Debuff / Control | 53.8 -> **52.6** (-2.2%) | - | 53.8 -> **52.6** | Individual spell overtuned (WR: 56.7%, Casts: 3029, mult: 0.977) |
| `LEE` | Wind | Setup - Weather | 21.5 -> **22.0** (+2.3%) | - | 21.5 -> **22.0** | Individual spell undertuned (WR: 42.9%, Casts: 2861, mult: 1.024) |
| `LEL` | Wind | Buff / Sustain | 84.1 -> **96.7** (+15.0%) | - | 84.1 -> **96.7** | Buffed setup spell [LEL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `EDF` | Poison | Conditional Strike | 1.1 -> **0.9** (-18.2%) | 279.1 -> **363.1** | 308.1 -> **327.7** | Class Poison overtuned (WR: 55.2%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.3% vs 30% floor, Casts: 2722). Increasing spread: b -14.7%, n +30.1% |
| `EDW` | Poison | Debuff / Control | 13.7 -> **12.7** (-7.3%) | - | 13.7 -> **12.7** | Class Poison overtuned (WR: 55.2%, factor: 0.979); Individual spell overtuned (WR: 64.8%, Casts: 1895, mult: 0.945) |
| `EDE` | Poison | Setup - Location | 58.3 -> **54.7** (-6.2%) | - | 58.3 -> **54.7** | Class Poison overtuned (WR: 55.2%, factor: 0.979); Location 'Swamp' appliers overtuned on own (WR: 56.0%) |
| `EDL` | Poison | Debuff / Control | 1.2 -> **1.0** (-16.7%) | - | 1.2 -> **1.0** | Class Poison overtuned (WR: 55.2%, factor: 0.979); Individual spell overtuned (WR: 86.3%, Casts: 2150, mult: 0.852) |
| `EDD` | Poison | Ultimate | 42.0 -> **44.4** (+5.7%) | 28.6 -> **27.5** | 1243.2 -> **1265.4** | Class Poison overtuned (WR: 55.2%, factor: 0.979); Status 'Bleeding' beneficiaries undertuned (WR: 44.6%) |
| `DEW` | Poison | Debuff / Control | 15.6 -> **14.8** (-5.1%) | - | 15.6 -> **14.8** | Class Poison overtuned (WR: 55.2%, factor: 0.979); Individual spell overtuned (WR: 58.6%, Casts: 2271, mult: 0.970) |
| `DEE` | Poison | Debuff / Control | 37.7 -> **42.5** (+12.7%) | - | 37.7 -> **42.5** | Class Poison overtuned (WR: 55.2%, factor: 0.979); Buffed setup spell [DEE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 281.5 -> **383.2** | 56.5 -> **76.8** | Class Poison overtuned (WR: 55.2%, factor: 0.979); Status 'Bleeding' beneficiaries undertuned (WR: 44.6%) |
| `DED` | Poison | Debuff / Control | 22.4 -> **22.2** (-0.9%) | - | 22.4 -> **22.2** | Class Poison overtuned (WR: 55.2%, factor: 0.979); Individual spell undertuned (WR: 45.8%, Casts: 2079, mult: 1.014) |
| `LDF` | Cosmic | Debuff / Control | 108.1 -> **121.0** (+11.9%) | - | 108.1 -> **121.0** | Buffed setup spell [LDF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 57.6%, Casts: 1352, mult: 0.973) |
| `LDW` | Cosmic | Debuff / Control | 46.0 -> **45.2** (-1.7%) | - | 46.0 -> **45.2** | Individual spell overtuned (WR: 55.3%, Casts: 2205, mult: 0.982) |
| `LDE` | Cosmic | Setup - Location | 27.0 -> **27.7** (+2.6%) | - | 27.0 -> **27.7** | Individual spell undertuned (WR: 42.8%, Casts: 1480, mult: 1.025) |
| `LDL` | Cosmic | Conditional Strike | 1.8 -> **1.6** (-11.1%) | 369.8 -> **498.9** | 667.4 -> **799.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.5% vs 30% floor, Casts: 1511). Increasing spread: b -17.0%, n +34.9%; Individual spell undertuned (WR: 38.3%, Casts: 1511, mult: 1.043) |
| `LDD` | Cosmic | Ultimate | 66.6 -> **66.6** (+0.0%) | 17.8 -> **23.1** | 1252.1 -> **1605.1** | Ultimate payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2131). Shifted tuner focus: protected ultimate base floor at 66.6 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDW, DDL, DEE, DFW, DWW, ELW, LEL, DLL, FEF, LWF) with +15% b tempo. |
| `DLF` | Cosmic | Conditional Strike | 1.9 -> **1.6** (-15.8%) | 305.2 -> **405.5** | 581.8 -> **650.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.0% vs 30% floor, Casts: 2317). Increasing spread: b -16.0%, n +32.9%; Individual spell overtuned (WR: 54.4%, Casts: 2317, mult: 0.986) |
| `DLW` | Cosmic | Direct Damage | 59.0 -> **57.5** (-2.5%) | - | 59.0 -> **57.5** | Individual spell overtuned (WR: 57.3%, Casts: 1331, mult: 0.975) |
| `DLE` | Cosmic | Direct Damage | 45.1 -> **46.9** (+4.0%) | - | 45.1 -> **46.9** | Individual spell undertuned (WR: 38.8%, Casts: 1992, mult: 1.040) |
| `DLL` | Cosmic | Conditional Strike | 5.2 -> **4.7** (-9.6%) | 141.1 -> **184.9** | 738.9 -> **873.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.1% vs 30% floor, Casts: 2121). Increasing spread: b -15.2%, n +31.1%; Individual spell undertuned (WR: 35.3%, Casts: 2121, mult: 1.055) |
