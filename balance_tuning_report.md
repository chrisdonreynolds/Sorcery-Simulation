# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T01:40:34Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 567.7s  
**Total Spells Tuned:** 107 / 125  

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
| **Blood** | 20,317 | 57.1% | 57.1% | 17.9 | Overtuned ⚠️ |
| **Poison** | 19,518 | 56.2% | 56.3% | 9.9 | Overtuned ⚠️ |
| **Earth** | 9,517 | 54.9% | 54.9% | 16.7 | Overtuned ⚠️ |
| **Light** | 10,193 | 52.0% | 52.0% | 14.2 | Balanced ✅ |
| **Fire** | 8,228 | 51.6% | 51.6% | 15.6 | Balanced ✅ |
| **Ghostfire** | 19,910 | 51.1% | 51.1% | 18.8 | Balanced ✅ |
| **Cosmic** | 17,374 | 50.5% | 50.5% | 16.8 | Balanced ✅ |
| **Beasts** | 20,704 | 50.0% | 50.0% | 10.7 | Balanced ✅ |
| **Dark** | 9,862 | 49.4% | 49.4% | 32.4 | Balanced ✅ |
| **Plants** | 20,029 | 48.7% | 48.7% | 7.7 | Balanced ✅ |
| **Ice** | 20,330 | 47.6% | 47.6% | 17.1 | Balanced ✅ |
| **Lightning** | 21,522 | 47.5% | 47.5% | 14.3 | Balanced ✅ |
| **Fey** | 18,082 | 46.6% | 46.6% | 29.5 | Balanced ✅ |
| **Water** | 9,930 | 46.5% | 46.5% | 10.8 | Balanced ✅ |
| **Wind** | 19,274 | 46.3% | 46.3% | 6.6 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,292 (55.1%) | 3,951 (42.1%) | 23.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,639 (46.7%) | 4,932 (52.2%) | 5.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,369 (54.6%) | 4,330 (45.7%) | 9.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,841 (61.6%) | 7,822 (48.4%) | 6.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 13,561 (49.7%) | 5,227 (41.0%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,537 (63.2%) | 8,168 (45.7%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,994 (37.7%) | 5,330 (39.2%) | 6.1% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 39.7 -> **39.1** (-1.5%) | - | 39.7 -> **39.1** | Status 'Burning' appliers overtuned on own (WR: 54.6%) |
| `FFE` | Fire | Debuff / Control | 33.8 -> **33.2** (-1.8%) | - | 33.8 -> **33.2** | Individual spell overtuned (WR: 55.0%, Casts: 2309, mult: 0.983) |
| `FFL` | Fire | Debuff / Control | 4.8 -> **4.6** (-4.2%) | - | 4.8 -> **4.6** | Status 'Burning' appliers overtuned on own (WR: 54.6%); Individual spell overtuned (WR: 56.4%, Casts: 1171, mult: 0.978) |
| `FFD` | Fire | Conditional Strike | 2.0 -> **1.7** (-15.0%) | 185.2 -> **247.1** | 372.4 -> **421.8** | Status 'Burning' beneficiaries undertuned (WR: 45.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.0% vs 30% floor, Casts: 1172). Increasing spread: b -15.2%, n +31.2% |
| `WWF` | Water | Conditional Strike | 4.7 -> **4.1** (-12.8%) | 107.4 -> **136.6** | 509.5 -> **564.2** | Status 'Burning' beneficiaries undertuned (WR: 45.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.4% vs 30% floor, Casts: 1544). Increasing spread: b -12.2%, n +25.0% |
| `WWE` | Water | Setup - Weather | 54.1 -> **59.0** (+9.1%) | - | 54.1 -> **59.0** | Weather 'Raining' appliers undertuned (WR: 37.7%, casts: 1994); Individual spell undertuned (WR: 37.6%, Casts: 1994, mult: 1.045) |
| `EEF` | Earth | Conditional Strike | 17.4 -> **18.9** (+8.6%) | 23.6 -> **27.9** | 428.0 -> **546.2** | Class Earth overtuned (WR: 54.9%, factor: 0.980); Status 'Frosty' beneficiaries undertuned (WR: 42.1%) |
| `EEW` | Earth | Buff / Sustain | 23.3 -> **22.0** (-5.6%) | - | 23.3 -> **22.0** | Class Earth overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 60.8%, Casts: 2361, mult: 0.961) |
| `LLF` | Light | Conditional Strike | 5.3 -> **6.1** (+15.1%) | 246.9 -> **330.4** | 1313.9 -> **2021.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.8% vs 30% floor, Casts: 3415). Increasing spread: b -16.5%, n +33.8%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 78.3 -> **90.0** (+14.9%) | - | 78.3 -> **90.0** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LLE` | Light | Setup - Weather | 103.8 -> **119.4** (+15.0%) | - | 103.8 -> **119.4** | Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 19.9 -> **19.0** (-4.5%) | - | 19.9 -> **19.0** | Individual spell overtuned (WR: 62.5%, Casts: 1487, mult: 0.954) |
| `LLD` | Light | Ultimate | 36.0 -> **36.0** (+0.0%) | 55.1 -> **71.6** | 2019.6 -> **2613.6** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1824). Shifted tuner focus: protected ultimate base floor at 36.0 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 1.0 -> **0.8** (-20.0%) | 448.8 -> **614.7** | 449.8 -> **492.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1834). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 44.0%, Casts: 1834, mult: 1.020) |
| `DDW` | Dark | Debuff / Control | 96.7 -> **111.2** (+15.0%) | - | 96.7 -> **111.2** | Buffed setup spell [DDW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DDE` | Dark | Setup - Weather | 128.1 -> **151.9** (+18.6%) | - | 128.1 -> **151.9** | Weather 'Darkness' appliers undertuned (WR: 45.4%, casts: 1993); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `DDL` | Dark | Debuff / Control | 46.6 -> **52.9** (+13.5%) | - | 46.6 -> **52.9** | Buffed setup spell [DDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 54.0%, Casts: 2252, mult: 0.987) |
| `DDD` | Dark | Debuff / Control | 21.2 -> **20.6** (-2.8%) | - | 21.2 -> **20.6** | Individual spell overtuned (WR: 57.6%, Casts: 1437, mult: 0.973) |
| `FWF` | Ghostfire | Debuff / Control | 24.3 -> **23.1** (-4.9%) | - | 24.3 -> **23.1** | Status 'Burning' appliers overtuned on own (WR: 54.6%); Individual spell overtuned (WR: 59.4%, Casts: 2259, mult: 0.967) |
| `FWW` | Ghostfire | Debuff / Control | 56.1 -> **64.5** (+15.0%) | - | 56.1 -> **64.5** | Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 150.5 -> **180.0** (+19.6%) | - | 150.5 -> **180.0** | Location 'Graveyard' appliers undertuned (WR: 44.2%, casts: 1918); Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 134.8 -> **155.0** (+15.0%) | - | 134.8 -> **155.0** | Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 50.8 -> **50.2** (-1.2%) | 53.3 -> **68.2** | 2758.4 -> **3473.8** | Location 'Graveyard' beneficiaries overtuned (WR: 53.5%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 1318). Shifted tuner focus: protected ultimate base floor at 50.8 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 1.8 -> **1.6** (-11.1%) | 215.0 -> **286.5** | 388.8 -> **460.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.5% vs 30% floor, Casts: 1724). Increasing spread: b -16.2%, n +33.3%; Individual spell undertuned (WR: 40.3%, Casts: 1724, mult: 1.034) |
| `WFW` | Ghostfire | Debuff / Control | 25.3 -> **24.8** (-2.0%) | - | 25.3 -> **24.8** | Individual spell overtuned (WR: 55.8%, Casts: 2148, mult: 0.980) |
| `WFL` | Ghostfire | Buff / Sustain | 43.4 -> **44.2** (+1.8%) | - | 43.4 -> **44.2** | Individual spell undertuned (WR: 44.8%, Casts: 4035, mult: 1.017) |
| `WFD` | Ghostfire | Conditional Strike | 2.6 -> **2.3** (-11.5%) | 164.4 -> **209.3** | 430.0 -> **483.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.7% vs 30% floor, Casts: 1329). Increasing spread: b -13.3%, n +27.3%; Individual spell undertuned (WR: 38.7%, Casts: 1329, mult: 1.041) |
| `FEF` | Beasts | Debuff / Control | 54.5 -> **62.7** (+15.0%) | - | 54.5 -> **62.7** | Buffed setup spell [FEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `FEW` | Beasts | Conditional Strike | 1.1 -> **0.9** (-18.2%) | 449.0 -> **621.2** | 495.0 -> **560.0** | Status 'Entangled' beneficiaries undertuned (WR: 45.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 2583). Increasing spread: b -17.5%, n +36.0% |
| `FEE` | Beasts | Buff / Sustain | 32.1 -> **33.0** (+2.8%) | - | 32.1 -> **33.0** | Individual spell undertuned (WR: 41.6%, Casts: 2281, mult: 1.029) |
| `FEL` | Beasts | Buff / Sustain | 35.8 -> **36.8** (+2.8%) | - | 35.8 -> **36.8** | Individual spell undertuned (WR: 42.2%, Casts: 2302, mult: 1.027) |
| `EFF` | Beasts | Debuff / Control | 1.2 -> **1.0** (-16.7%) | 400.5 -> **547.8** | 481.8 -> **548.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1841). Increasing spread: b -17.9%, n +36.8%; Individual spell overtuned (WR: 53.9%, Casts: 1841, mult: 0.987) |
| `EFW` | Beasts | Buff / Sustain | 22.2 -> **22.5** (+1.4%) | - | 22.2 -> **22.5** | Individual spell undertuned (WR: 46.2%, Casts: 2510, mult: 1.013) |
| `EFL` | Beasts | Buff / Sustain | 2.7 -> **2.3** (-14.8%) | - | 2.7 -> **2.3** | Individual spell overtuned (WR: 84.8%, Casts: 1336, mult: 0.859) |
| `EFD` | Beasts | Ultimate | 32.7 -> **32.2** (-1.5%) | 106.2 -> **140.0** | 3505.4 -> **4540.2** | Status 'Entangled' beneficiaries undertuned (WR: 45.7%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.3% vs 16% floor, Casts: 2348). Shifted tuner focus: protected ultimate base floor at 32.7 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo. |
| `FLF` | Lightning | Conditional Strike | 1.2 -> **1.1** (-8.3%) | 588.9 -> **835.3** | 707.9 -> **919.9** | Status 'Stunned' beneficiaries undertuned (WR: 41.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 2836). Increasing spread: b -18.0%, n +36.9% |
| `FLW` | Lightning | Debuff / Control | 74.4 -> **82.0** (+10.2%) | - | 74.4 -> **82.0** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 61.6%, Casts: 2104, mult: 0.958) |
| `FLE` | Lightning | Setup - Weather | 53.5 -> **65.9** (+23.2%) | - | 53.5 -> **65.9** | Weather 'Storming' appliers undertuned (WR: 40.2%, casts: 2055); Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLL` | Lightning | Buff / Sustain | 29.4 -> **30.4** (+3.4%) | - | 29.4 -> **30.4** | Individual spell undertuned (WR: 40.5%, Casts: 1871, mult: 1.034) |
| `FLD` | Lightning | Ultimate | 82.1 -> **80.5** (-1.9%) | 18.6 -> **24.5** | 1609.2 -> **2052.8** | Status 'Stunned' beneficiaries undertuned (WR: 41.0%); Weather 'Storming' beneficiaries overtuned (WR: 55.6%) |
| `LFF` | Lightning | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 354.6 -> **479.7** | 426.7 -> **480.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.1% vs 30% floor, Casts: 1411). Increasing spread: b -17.2%, n +35.3%; Individual spell undertuned (WR: 39.4%, Casts: 1411, mult: 1.038) |
| `LFW` | Lightning | Buff / Sustain | 29.0 -> **28.2** (-2.8%) | - | 29.0 -> **28.2** | Individual spell overtuned (WR: 57.6%, Casts: 1700, mult: 0.973) |
| `LFL` | Lightning | Debuff / Control | 36.0 -> **40.0** (+11.1%) | 142.9 -> **184.3** | 5180.4 -> **7412.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.7% vs 30% floor, Casts: 2558). Increasing spread: b -14.1%, n +28.9%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 3.4 -> **2.9** (-14.7%) | 260.0 -> **348.1** | 887.4 -> **1012.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.8% vs 30% floor, Casts: 2027). Increasing spread: b -16.5%, n +33.9%; Individual spell undertuned (WR: 46.0%, Casts: 2027, mult: 1.013) |
| `FDF` | Blood | Conditional Strike | 1.0 -> **0.8** (-20.0%) | 449.8 -> **616.2** | 450.8 -> **493.8** | Class Blood overtuned (WR: 57.1%, factor: 0.972); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1756). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 68.2 -> **65.1** (-4.5%) | - | 68.2 -> **65.1** | Class Blood overtuned (WR: 57.1%, factor: 0.972); Individual spell overtuned (WR: 55.1%, Casts: 2069, mult: 0.983) |
| `FDE` | Blood | Setup - Weather | 19.8 -> **18.9** (-4.5%) | - | 19.8 -> **18.9** | Class Blood overtuned (WR: 57.1%, factor: 0.972); Individual spell overtuned (WR: 55.8%, Casts: 2038, mult: 0.980) |
| `FDL` | Blood | Debuff / Control | 9.1 -> **8.9** (-2.2%) | - | 9.1 -> **8.9** | Class Blood overtuned (WR: 57.1%, factor: 0.972); Status 'Bleeding' appliers overtuned on own (WR: 61.6%) |
| `FDD` | Blood | Ultimate | 53.4 -> **51.9** (-2.8%) | 13.4 -> **17.4** | 769.0 -> **955.0** | Class Blood overtuned (WR: 57.1%, factor: 0.972); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.4% vs 16% floor, Casts: 1270). Shifted tuner focus: protected ultimate base floor at 53.4 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 203.3 -> **264.8** | 286.0 -> **319.0** | Class Blood overtuned (WR: 57.1%, factor: 0.972); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 2121). Increasing spread: b -14.8%, n +30.2% |
| `DFW` | Blood | Debuff / Control | 15.1 -> **14.7** (-2.6%) | - | 15.1 -> **14.7** | Class Blood overtuned (WR: 57.1%, factor: 0.972); Status 'Bleeding' appliers overtuned on own (WR: 61.6%) |
| `DFE` | Blood | Buff / Sustain | 42.7 -> **43.2** (+1.2%) | - | 42.7 -> **43.2** | Class Blood overtuned (WR: 57.1%, factor: 0.972); Individual spell undertuned (WR: 38.7%, Casts: 1992, mult: 1.041) |
| `DFL` | Blood | Buff / Sustain | 32.4 -> **31.5** (-2.8%) | - | 32.4 -> **31.5** | Class Blood overtuned (WR: 57.1%, factor: 0.972) |
| `DFD` | Blood | Conditional Strike | 198.2 -> **219.7** (+10.8%) | 0.1 -> **0.1** | 218.0 -> **241.7** | Class Blood overtuned (WR: 57.1%, factor: 0.972); Condition triggers excessively (N=1 conditions, Trigger Rate: 96.0% vs 55% ceiling, WR: 56.7%). Compressing spread: b +16.8%, n -25.2% |
| `WEF` | Plants | Conditional Strike | 2.6 -> **2.3** (-11.5%) | 145.8 -> **187.7** | 381.7 -> **434.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.9% vs 30% floor, Casts: 1335). Increasing spread: b -14.0%, n +28.8%; Individual spell undertuned (WR: 41.0%, Casts: 1335, mult: 1.032) |
| `WEW` | Plants | Debuff / Control | 277.5 -> **327.8** (+18.1%) | - | 277.5 -> **327.8** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 42.2%, Casts: 2249, mult: 1.027) |
| `WEE` | Plants | Setup - Location | 22.1 -> **20.7** (-6.3%) | - | 22.1 -> **20.7** | Location 'Jungle' appliers overtuned on own (WR: 59.2%); Individual spell overtuned (WR: 59.3%, Casts: 921, mult: 0.967) |
| `WEL` | Plants | Debuff / Control | 32.4 -> **29.4** (-9.3%) | - | 32.4 -> **29.4** | Status 'Entangled' appliers overtuned on own (WR: 63.2%); Individual spell overtuned (WR: 63.2%, Casts: 1537, mult: 0.951) |
| `WED` | Plants | Conditional Strike | 7.3 -> **8.3** (+13.7%) | 40.8 -> **38.4** | 305.1 -> **327.0** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 1357, WR: 36.1%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 36.1%, Casts: 1357, mult: 1.051) |
| `EWF` | Plants | Buff / Sustain | 2.2 -> **1.9** (-13.6%) | 93.8 -> **121.5** | 208.6 -> **232.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.0% vs 30% floor, Casts: 3108). Increasing spread: b -14.4%, n +29.5% |
| `EWW` | Plants | Debuff / Control | 4.0 -> **3.5** (-12.5%) | - | 4.0 -> **3.5** | Individual spell overtuned (WR: 82.0%, Casts: 1841, mult: 0.871) |
| `EWL` | Plants | Debuff / Control | 71.2 -> **72.7** (+2.1%) | - | 71.2 -> **72.7** | Individual spell undertuned (WR: 43.9%, Casts: 2992, mult: 1.021) |
| `EWD` | Plants | Conditional Strike | 4.2 -> **4.9** (+16.7%) | 357.8 -> **493.0** | 1507.0 -> **2420.6** | Status 'Bleeding' appliers overtuned on own (WR: 61.6%); Status 'Entangled' beneficiaries undertuned (WR: 45.7%) |
| `WLF` | Fey | Conditional Strike | 2.2 -> **1.9** (-13.6%) | 295.0 -> **387.2** | 651.2 -> **737.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.9% vs 30% floor, Casts: 1682). Increasing spread: b -15.2%, n +31.2%; Individual spell undertuned (WR: 44.6%, Casts: 1682, mult: 1.018) |
| `WLE` | Fey | Setup - Location | 194.2 -> **218.1** (+12.3%) | - | 194.2 -> **218.1** | Location 'Enchanted Forest' appliers overtuned on own (WR: 53.5%); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 57.8 -> **57.1** (-1.2%) | - | 57.8 -> **57.1** | Individual spell overtuned (WR: 53.9%, Casts: 1786, mult: 0.987) |
| `WLD` | Fey | Ultimate | 25.7 -> **25.3** (-1.6%) | 252.5 -> **328.2** | 6514.9 -> **8328.8** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1435). Shifted tuner focus: protected ultimate base floor at 25.7 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo.; Individual spell overtuned (WR: 54.7%, Casts: 1435, mult: 0.984) |
| `LWF` | Fey | Debuff / Control | 22.1 -> **25.4** (+14.9%) | 89.1 -> **110.2** | 1991.2 -> **2824.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 16.0% vs 30% floor, Casts: 2349). Increasing spread: b -11.6%, n +23.7%; Buffed setup spell [LWF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LWL` | Fey | Debuff / Control | 47.4 -> **48.7** (+2.7%) | - | 47.4 -> **48.7** | Individual spell undertuned (WR: 42.3%, Casts: 1538, mult: 1.027) |
| `LWD` | Fey | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 449.8 -> **616.2** | 586.0 -> **678.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1905). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 34.7%, Casts: 1905, mult: 1.057) |
| `WDF` | Ice | Conditional Strike | 3.0 -> **2.6** (-13.3%) | 426.2 -> **594.3** | 1281.6 -> **1547.8** | Weather 'Raining' beneficiaries undertuned (WR: 39.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.0% vs 30% floor, Casts: 2915). Increasing spread: b -16.4%, n +33.7% |
| `WDW` | Ice | Buff / Sustain | 14.0 -> **13.2** (-5.7%) | - | 14.0 -> **13.2** | Status 'Frosty' appliers overtuned on own (WR: 55.1%); Individual spell overtuned (WR: 60.2%, Casts: 2737, mult: 0.963) |
| `WDE` | Ice | Setup - Weather | 29.4 -> **30.4** (+3.4%) | - | 29.4 -> **30.4** | Individual spell undertuned (WR: 40.7%, Casts: 2382, mult: 1.033) |
| `WDL` | Ice | Debuff / Control | 45.0 -> **43.4** (-3.6%) | - | 45.0 -> **43.4** | Status 'Frosty' appliers overtuned on own (WR: 55.1%); Individual spell overtuned (WR: 55.3%, Casts: 762, mult: 0.982) |
| `WDD` | Ice | Ultimate | 32.2 -> **32.2** (+0.0%) | 85.2 -> **108.0** | 2775.6 -> **3509.8** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 2.6% vs 16% floor, Casts: 1875). Shifted tuner focus: protected ultimate base floor at 32.2 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWF` | Ice | Debuff / Control | 41.7 -> **40.4** (-3.1%) | - | 41.7 -> **40.4** | Status 'Frosty' appliers overtuned on own (WR: 55.1%); Individual spell overtuned (WR: 54.4%, Casts: 1279, mult: 0.986) |
| `DWW` | Ice | Debuff / Control | 71.2 -> **80.0** (+12.4%) | - | 71.2 -> **80.0** | Buffed setup spell [DWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 56.6%, Casts: 1179, mult: 0.977) |
| `DWE` | Ice | Setup - Location | 37.1 -> **36.2** (-2.4%) | - | 37.1 -> **36.2** | Location 'Tundra' appliers overtuned on own (WR: 53.6%); Individual spell overtuned (WR: 53.6%, Casts: 2175, mult: 0.988) |
| `DWL` | Ice | Debuff / Control | 45.6 -> **44.8** (-1.8%) | - | 45.6 -> **44.8** | Status 'Frosty' appliers overtuned on own (WR: 55.1%) |
| `DWD` | Ice | Conditional Strike | 6.0 -> **5.8** (-3.3%) | 48.9 -> **59.9** | 299.4 -> **353.2** | Status 'Frosty' beneficiaries undertuned (WR: 42.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 21.8% vs 30% floor, Casts: 2512). Increasing spread: b -9.3%, n +18.9% |
| `ELF` | Wind | Conditional Strike | 4.5 -> **4.0** (-11.1%) | 218.8 -> **286.0** | 989.1 -> **1148.0** | Class Wind undertuned (WR: 46.3%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.6% vs 30% floor, Casts: 952). Increasing spread: b -15.0%, n +30.7% |
| `ELW` | Wind | Debuff / Control | 75.4 -> **86.1** (+14.2%) | - | 75.4 -> **86.1** | Class Wind undertuned (WR: 46.3%, factor: 1.015); Buffed setup spell [ELW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `ELE` | Wind | Setup - Weather | 23.8 -> **24.2** (+1.7%) | - | 23.8 -> **24.2** | Class Wind undertuned (WR: 46.3%, factor: 1.015) |
| `ELL` | Wind | Buff / Sustain | 38.0 -> **38.6** (+1.6%) | - | 38.0 -> **38.6** | Class Wind undertuned (WR: 46.3%, factor: 1.015) |
| `ELD` | Wind | Conditional Strike | 2.6 -> **2.4** (-7.7%) | 365.6 -> **495.3** | 953.2 -> **1191.1** | Class Wind undertuned (WR: 46.3%, factor: 1.015); Weather 'Raining' beneficiaries undertuned (WR: 39.2%) |
| `LEF` | Wind | Conditional Strike | 1.8 -> **1.6** (-11.1%) | 216.0 -> **289.6** | 390.6 -> **465.0** | Class Wind undertuned (WR: 46.3%, factor: 1.015); Status 'Burning' beneficiaries undertuned (WR: 45.7%) |
| `LEW` | Wind | Debuff / Control | 53.0 -> **53.8** (+1.5%) | - | 53.0 -> **53.8** | Class Wind undertuned (WR: 46.3%, factor: 1.015) |
| `LEE` | Wind | Setup - Weather | 20.6 -> **21.5** (+4.4%) | - | 20.6 -> **21.5** | Class Wind undertuned (WR: 46.3%, factor: 1.015); Individual spell undertuned (WR: 41.8%, Casts: 3370, mult: 1.029) |
| `LEL` | Wind | Buff / Sustain | 73.1 -> **84.1** (+15.0%) | - | 73.1 -> **84.1** | Class Wind undertuned (WR: 46.3%, factor: 1.015); Buffed setup spell [LEL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `EDF` | Poison | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 214.4 -> **279.1** | 280.0 -> **308.1** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 3083). Increasing spread: b -14.7%, n +30.2% |
| `EDW` | Poison | Debuff / Control | 14.5 -> **13.7** (-5.5%) | - | 14.5 -> **13.7** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 59.7%, Casts: 1654, mult: 0.966) |
| `EDE` | Poison | Setup - Location | 52.0 -> **58.3** (+12.1%) | - | 52.0 -> **58.3** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Buffed setup spell [EDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `EDL` | Poison | Debuff / Control | 1.4 -> **1.2** (-14.3%) | - | 1.4 -> **1.2** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 85.8%, Casts: 1971, mult: 0.854) |
| `EDD` | Poison | Ultimate | 43.6 -> **42.0** (-3.7%) | 22.6 -> **28.6** | 1029.0 -> **1243.2** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Location 'Swamp' beneficiaries overtuned (WR: 53.7%) |
| `DEF` | Poison | Conditional Strike | 32.9 -> **32.1** (-2.4%) | 1.4 -> **1.4** | 79.0 -> **77.0** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 48.9% within [30%-55%] target window, WR: 51.7%). |
| `DEW` | Poison | Debuff / Control | 16.7 -> **15.6** (-6.6%) | - | 16.7 -> **15.6** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 61.0%, Casts: 1951, mult: 0.960) |
| `DEE` | Poison | Debuff / Control | 33.6 -> **37.7** (+12.2%) | - | 33.6 -> **37.7** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Buffed setup spell [DEE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 222.3 -> **281.5** | 44.7 -> **56.5** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.5% vs 30% floor, Casts: 1572). Increasing spread: b -13.0%, n +26.6% |
| `DED` | Poison | Debuff / Control | 23.0 -> **22.4** (-2.6%) | - | 23.0 -> **22.4** | Class Poison overtuned (WR: 56.2%, factor: 0.975) |
| `LDF` | Cosmic | Debuff / Control | 96.6 -> **108.1** (+11.9%) | - | 96.6 -> **108.1** | Buffed setup spell [LDF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 57.8%, Casts: 872, mult: 0.973) |
| `LDE` | Cosmic | Setup - Location | 26.4 -> **27.0** (+2.3%) | - | 26.4 -> **27.0** | Individual spell undertuned (WR: 43.7%, Casts: 1131, mult: 1.021) |
| `LDL` | Cosmic | Conditional Strike | 2.1 -> **1.8** (-14.3%) | 273.3 -> **369.8** | 576.0 -> **667.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.0% vs 30% floor, Casts: 1672). Increasing spread: b -17.2%, n +35.3%; Individual spell undertuned (WR: 43.9%, Casts: 1672, mult: 1.021) |
| `LDD` | Cosmic | Ultimate | 66.6 -> **66.6** (+0.0%) | 13.7 -> **17.8** | 979.0 -> **1252.1** | Ultimate payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2073). Shifted tuner focus: protected ultimate base floor at 66.6 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDW, DDL, DEE, DFW, DWW, ELW, LEL, DLL, FEF, LWF) with +15% b tempo. |
| `DLF` | Cosmic | Conditional Strike | 2.3 -> **1.9** (-17.4%) | 229.1 -> **305.2** | 529.2 -> **581.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.5% vs 30% floor, Casts: 2440). Increasing spread: b -16.2%, n +33.2% |
| `DLW` | Cosmic | Direct Damage | 61.8 -> **59.0** (-4.5%) | - | 61.8 -> **59.0** | Individual spell overtuned (WR: 62.3%, Casts: 1642, mult: 0.955) |
| `DLE` | Cosmic | Direct Damage | 44.2 -> **45.1** (+2.0%) | - | 44.2 -> **45.1** | Individual spell undertuned (WR: 43.8%, Casts: 1467, mult: 1.021) |
| `DLL` | Cosmic | Conditional Strike | 6.0 -> **5.2** (-13.3%) | 107.0 -> **141.1** | 648.0 -> **738.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 2065). Increasing spread: b -15.5%, n +31.8%; Individual spell undertuned (WR: 41.3%, Casts: 2065, mult: 1.031) |
