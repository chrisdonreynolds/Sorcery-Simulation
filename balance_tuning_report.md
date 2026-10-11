# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T01:16:39Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 744.4s  
**Total Spells Tuned:** 98 / 125  

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
| **Blood** | 21,160 | 55.6% | 55.6% | 17.4 | Overtuned ⚠️ |
| **Earth** | 10,038 | 55.5% | 55.5% | 16.7 | Overtuned ⚠️ |
| **Poison** | 20,709 | 53.3% | 53.3% | 9.0 | Balanced ✅ |
| **Light** | 9,891 | 52.9% | 52.9% | 14.5 | Balanced ✅ |
| **Ghostfire** | 19,658 | 51.0% | 51.0% | 19.9 | Balanced ✅ |
| **Dark** | 9,738 | 50.7% | 50.7% | 19.1 | Balanced ✅ |
| **Fire** | 8,309 | 50.4% | 50.4% | 16.0 | Balanced ✅ |
| **Water** | 10,140 | 50.1% | 50.1% | 11.9 | Balanced ✅ |
| **Plants** | 18,465 | 49.3% | 49.3% | 8.2 | Balanced ✅ |
| **Cosmic** | 17,344 | 48.9% | 48.9% | 16.2 | Balanced ✅ |
| **Beasts** | 22,263 | 48.9% | 48.9% | 9.3 | Balanced ✅ |
| **Wind** | 19,150 | 48.7% | 48.7% | 6.7 | Balanced ✅ |
| **Lightning** | 21,691 | 48.5% | 48.5% | 12.7 | Balanced ✅ |
| **Fey** | 17,254 | 47.2% | 47.2% | 28.4 | Balanced ✅ |
| **Ice** | 20,057 | 46.6% | 46.6% | 16.6 | Balanced ✅ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,419 (52.0%) | 3,384 (47.1%) | 27.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,617 (54.4%) | 4,398 (50.2%) | 5.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,341 (51.3%) | 4,191 (46.4%) | 10.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,557 (65.5%) | 9,114 (48.2%) | 6.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,169 (48.4%) | 5,106 (42.6%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,850 (53.3%) | 8,017 (46.6%) | 1.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,017 (39.7%) | 5,321 (39.3%) | 5.7% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFE` | Fire | Debuff / Control | 34.4 -> **33.8** (-1.7%) | - | 34.4 -> **33.8** | Individual spell overtuned (WR: 55.2%, Casts: 2218, mult: 0.982) |
| `FFD` | Fire | Conditional Strike | 2.3 -> **2.0** (-13.0%) | 143.7 -> **185.2** | 332.8 -> **372.4** | Status 'Burning' beneficiaries undertuned (WR: 46.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.9% vs 30% floor, Casts: 1064). Increasing spread: b -13.2%, n +27.0% |
| `WWF` | Water | Conditional Strike | 5.5 -> **4.7** (-14.5%) | 84.2 -> **107.4** | 468.6 -> **509.5** | Status 'Burning' beneficiaries undertuned (WR: 46.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.6% vs 30% floor, Casts: 1541). Increasing spread: b -12.6%, n +25.7% |
| `WWE` | Water | Setup - Weather | 50.4 -> **54.1** (+7.3%) | - | 50.4 -> **54.1** | Weather 'Raining' appliers undertuned (WR: 39.7%, casts: 2017); Individual spell undertuned (WR: 39.7%, Casts: 2017, mult: 1.037) |
| `WWD` | Water | Buff / Sustain | 49.1 -> **47.4** (-3.5%) | - | 49.1 -> **47.4** | Individual spell overtuned (WR: 59.6%, Casts: 1744, mult: 0.966) |
| `EEF` | Earth | Conditional Strike | 15.8 -> **17.4** (+10.1%) | 23.6 -> **23.6** | 388.7 -> **428.0** | Class Earth overtuned (WR: 55.5%, factor: 0.978); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 36.0% within [30%-55%] target window, WR: 55.8%). |
| `EEW` | Earth | Buff / Sustain | 25.3 -> **23.3** (-7.9%) | - | 25.3 -> **23.3** | Class Earth overtuned (WR: 55.5%, factor: 0.978); Individual spell overtuned (WR: 65.2%, Casts: 2382, mult: 0.943) |
| `EED` | Earth | Direct Damage | 7.4 -> **7.3** (-1.4%) | - | 7.4 -> **7.3** | Class Earth overtuned (WR: 55.5%, factor: 0.978); Individual spell undertuned (WR: 45.9%, Casts: 1922, mult: 1.014) |
| `LLF` | Light | Conditional Strike | 6.3 -> **5.3** (-15.9%) | 185.0 -> **246.9** | 1171.8 -> **1313.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.2% vs 30% floor, Casts: 2973). Increasing spread: b -16.3%, n +33.5% |
| `LLW` | Light | Debuff / Control | 69.2 -> **78.3** (+13.2%) | - | 69.2 -> **78.3** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LLE` | Light | Setup - Weather | 107.0 -> **103.8** (-3.0%) | - | 107.0 -> **103.8** | Weather 'Sunny' appliers overtuned on own (WR: 54.4%); Individual spell overtuned (WR: 54.4%, Casts: 1617, mult: 0.986) |
| `LLL` | Light | Buff / Sustain | 20.6 -> **19.9** (-3.4%) | - | 20.6 -> **19.9** | Individual spell overtuned (WR: 59.7%, Casts: 1237, mult: 0.966) |
| `LLD` | Light | Ultimate | 33.3 -> **36.0** (+8.1%) | 58.6 -> **55.1** | 1984.7 -> **2019.6** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1923, WR: 48.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 327.6 -> **448.8** | 394.3 -> **449.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2226). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 46.3%, Casts: 2226, mult: 1.012) |
| `DDW` | Dark | Debuff / Control | 84.1 -> **96.7** (+15.0%) | - | 84.1 -> **96.7** | Buffed setup spell [DDW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DDE` | Dark | Setup - Weather | 111.4 -> **128.1** (+15.0%) | - | 111.4 -> **128.1** | Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 40.5 -> **46.6** (+15.1%) | - | 40.5 -> **46.6** | Buffed setup spell [DDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DDD` | Dark | Debuff / Control | 22.1 -> **21.2** (-4.1%) | - | 22.1 -> **21.2** | Individual spell overtuned (WR: 61.3%, Casts: 1348, mult: 0.959) |
| `FWF` | Ghostfire | Debuff / Control | 24.7 -> **24.3** (-1.6%) | - | 24.7 -> **24.3** | Individual spell overtuned (WR: 54.4%, Casts: 2127, mult: 0.985) |
| `FWW` | Ghostfire | Debuff / Control | 47.8 -> **56.1** (+17.4%) | - | 47.8 -> **56.1** | Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD]; Individual spell undertuned (WR: 44.0%, Casts: 1711, mult: 1.020) |
| `FWE` | Ghostfire | Setup - Location | 124.9 -> **150.5** (+20.5%) | - | 124.9 -> **150.5** | Location 'Graveyard' appliers undertuned (WR: 43.2%, casts: 1898); Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 117.2 -> **134.8** (+15.0%) | - | 117.2 -> **134.8** | Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 50.8 -> **50.8** (+0.0%) | 41.0 -> **53.3** | 2133.6 -> **2758.4** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1845). Shifted tuner focus: protected ultimate base floor at 50.8 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 2.1 -> **1.8** (-14.3%) | 163.4 -> **215.0** | 345.2 -> **388.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.5% vs 30% floor, Casts: 1489). Increasing spread: b -15.4%, n +31.6%; Individual spell undertuned (WR: 43.8%, Casts: 1489, mult: 1.021) |
| `WFW` | Ghostfire | Debuff / Control | 25.9 -> **25.3** (-2.3%) | - | 25.9 -> **25.3** | Individual spell overtuned (WR: 57.1%, Casts: 2399, mult: 0.975) |
| `WFE` | Ghostfire | Debuff / Control | 17.3 -> **15.1** (-12.7%) | - | 17.3 -> **15.1** | Status 'Bleeding' appliers overtuned on own (WR: 65.5%); Individual spell overtuned (WR: 70.0%, Casts: 1735, mult: 0.923) |
| `WFL` | Ghostfire | Buff / Sustain | 42.9 -> **43.4** (+1.2%) | - | 42.9 -> **43.4** | Individual spell undertuned (WR: 46.5%, Casts: 2987, mult: 1.011) |
| `WFD` | Ghostfire | Conditional Strike | 2.9 -> **2.6** (-10.3%) | 129.6 -> **164.4** | 378.7 -> **430.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.2% vs 30% floor, Casts: 1412). Increasing spread: b -13.1%, n +26.8%; Individual spell undertuned (WR: 44.0%, Casts: 1412, mult: 1.020) |
| `FEF` | Beasts | Debuff / Control | 47.4 -> **54.5** (+15.0%) | - | 47.4 -> **54.5** | Buffed setup spell [FEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `FEW` | Beasts | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 330.5 -> **449.0** | 430.9 -> **495.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.4% vs 30% floor, Casts: 2859). Increasing spread: b -17.5%, n +35.9%; Individual spell undertuned (WR: 40.2%, Casts: 2859, mult: 1.035) |
| `FEE` | Beasts | Buff / Sustain | 31.2 -> **32.1** (+2.9%) | - | 31.2 -> **32.1** | Individual spell undertuned (WR: 42.1%, Casts: 2426, mult: 1.028) |
| `FEL` | Beasts | Buff / Sustain | 34.6 -> **35.8** (+3.5%) | - | 34.6 -> **35.8** | Individual spell undertuned (WR: 40.5%, Casts: 2930, mult: 1.034) |
| `EFF` | Beasts | Debuff / Control | 1.5 -> **1.2** (-20.0%) | 293.1 -> **400.5** | 441.2 -> **481.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 1671). Increasing spread: b -17.8%, n +36.7% |
| `EFL` | Beasts | Buff / Sustain | 3.2 -> **2.7** (-15.6%) | - | 3.2 -> **2.7** | Individual spell overtuned (WR: 85.6%, Casts: 1421, mult: 0.855) |
| `EFD` | Beasts | Ultimate | 33.7 -> **32.7** (-3.0%) | 81.9 -> **106.2** | 2793.7 -> **3505.4** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 2493). Shifted tuner focus: protected ultimate base floor at 33.7 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo.; Individual spell overtuned (WR: 58.2%, Casts: 2493, mult: 0.971) |
| `FLF` | Lightning | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 418.8 -> **588.9** | 587.7 -> **707.9** | Status 'Stunned' beneficiaries undertuned (WR: 42.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 2913). Increasing spread: b -17.8%, n +36.6% |
| `FLW` | Lightning | Debuff / Control | 68.9 -> **74.4** (+8.0%) | - | 68.9 -> **74.4** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 66.2%, Casts: 2012, mult: 0.939) |
| `FLE` | Lightning | Setup - Weather | 45.0 -> **53.5** (+18.9%) | - | 45.0 -> **53.5** | Weather 'Storming' appliers undertuned (WR: 45.0%, casts: 1713); Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLL` | Lightning | Buff / Sustain | 28.4 -> **29.4** (+3.5%) | - | 28.4 -> **29.4** | Individual spell undertuned (WR: 40.1%, Casts: 1857, mult: 1.035) |
| `FLD` | Lightning | Ultimate | 82.1 -> **82.1** (+0.0%) | 13.9 -> **18.6** | 1223.3 -> **1609.2** | Status 'Stunned' beneficiaries undertuned (WR: 42.6%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 2193). Shifted tuner focus: protected ultimate base floor at 82.1 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 1.5 -> **1.2** (-20.0%) | 263.9 -> **354.6** | 397.3 -> **426.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.2% vs 30% floor, Casts: 1360). Increasing spread: b -16.7%, n +34.4% |
| `LFW` | Lightning | Buff / Sustain | 29.3 -> **29.0** (-1.0%) | - | 29.3 -> **29.0** | Individual spell overtuned (WR: 53.6%, Casts: 2254, mult: 0.988) |
| `LFL` | Lightning | Debuff / Control | 31.8 -> **36.0** (+13.2%) | 112.0 -> **142.9** | 3593.4 -> **5180.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.3% vs 30% floor, Casts: 2513). Increasing spread: b -13.5%, n +27.6%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 4.0 -> **3.4** (-15.0%) | 195.5 -> **260.0** | 786.0 -> **887.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.8% vs 30% floor, Casts: 2700). Increasing spread: b -16.1%, n +33.0%; Individual spell undertuned (WR: 43.2%, Casts: 2700, mult: 1.023) |
| `FDF` | Blood | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 328.3 -> **449.8** | 395.2 -> **450.8** | Class Blood overtuned (WR: 55.6%, factor: 0.977); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1498). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 68.9 -> **68.2** (-1.0%) | - | 68.9 -> **68.2** | Class Blood overtuned (WR: 55.6%, factor: 0.977); Individual spell undertuned (WR: 46.1%, Casts: 1932, mult: 1.013) |
| `FDE` | Blood | Setup - Weather | 20.3 -> **19.8** (-2.5%) | - | 20.3 -> **19.8** | Class Blood overtuned (WR: 55.6%, factor: 0.977) |
| `FDL` | Blood | Debuff / Control | 10.9 -> **9.1** (-16.5%) | - | 10.9 -> **9.1** | Class Blood overtuned (WR: 55.6%, factor: 0.977); Status 'Bleeding' appliers overtuned on own (WR: 65.5%) |
| `FDD` | Blood | Ultimate | 54.6 -> **53.4** (-2.2%) | 10.3 -> **13.4** | 617.0 -> **769.0** | Class Blood overtuned (WR: 55.6%, factor: 0.977); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 1424). Shifted tuner focus: protected ultimate base floor at 54.6 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 1.7 -> **1.4** (-17.6%) | 155.5 -> **203.3** | 266.1 -> **286.0** | Class Blood overtuned (WR: 55.6%, factor: 0.977); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.5% vs 30% floor, Casts: 2168). Increasing spread: b -15.0%, n +30.7% |
| `DFW` | Blood | Debuff / Control | 15.6 -> **15.1** (-3.2%) | - | 15.6 -> **15.1** | Class Blood overtuned (WR: 55.6%, factor: 0.977); Status 'Bleeding' appliers overtuned on own (WR: 65.5%) |
| `DFE` | Blood | Buff / Sustain | 42.2 -> **42.7** (+1.2%) | - | 42.2 -> **42.7** | Class Blood overtuned (WR: 55.6%, factor: 0.977); Individual spell undertuned (WR: 40.1%, Casts: 2240, mult: 1.035) |
| `DFL` | Blood | Buff / Sustain | 33.1 -> **32.4** (-2.1%) | - | 33.1 -> **32.4** | Class Blood overtuned (WR: 55.6%, factor: 0.977) |
| `DFD` | Blood | Conditional Strike | 177.6 -> **198.2** (+11.6%) | 0.1 -> **0.1** | 195.4 -> **218.0** | Class Blood overtuned (WR: 55.6%, factor: 0.977); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.9% vs 55% ceiling, WR: 54.0%). Compressing spread: b +15.7%, n -24.2% |
| `WEF` | Plants | Conditional Strike | 2.9 -> **2.6** (-10.3%) | 113.5 -> **145.8** | 332.1 -> **381.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.3% vs 30% floor, Casts: 993). Increasing spread: b -13.9%, n +28.4%; Individual spell undertuned (WR: 40.0%, Casts: 993, mult: 1.036) |
| `WEW` | Plants | Debuff / Control | 234.9 -> **277.5** (+18.1%) | - | 234.9 -> **277.5** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 42.2%, Casts: 2252, mult: 1.027) |
| `WEE` | Plants | Setup - Location | 23.0 -> **22.1** (-3.9%) | - | 23.0 -> **22.1** | Location 'Jungle' appliers overtuned on own (WR: 55.5%); Individual spell overtuned (WR: 55.6%, Casts: 904, mult: 0.981) |
| `WED` | Plants | Conditional Strike | 6.7 -> **7.3** (+9.0%) | 43.4 -> **40.8** | 297.5 -> **305.1** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 1432, WR: 45.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 45.5%, Casts: 1432, mult: 1.015) |
| `EWF` | Plants | Buff / Sustain | 2.6 -> **2.2** (-15.4%) | 73.0 -> **93.8** | 192.4 -> **208.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.2% vs 30% floor, Casts: 2475). Increasing spread: b -13.9%, n +28.5% |
| `EWW` | Plants | Debuff / Control | 4.5 -> **4.0** (-11.1%) | - | 4.5 -> **4.0** | Individual spell overtuned (WR: 79.6%, Casts: 1785, mult: 0.882) |
| `EWL` | Plants | Debuff / Control | 70.2 -> **71.2** (+1.4%) | - | 70.2 -> **71.2** | Individual spell undertuned (WR: 45.5%, Casts: 2670, mult: 1.015) |
| `EWD` | Plants | Conditional Strike | 5.2 -> **4.2** (-19.2%) | 264.8 -> **357.8** | 1382.2 -> **1507.0** | Status 'Bleeding' appliers overtuned on own (WR: 65.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 2665). Increasing spread: b -17.1%, n +35.1% |
| `WLF` | Fey | Conditional Strike | 2.5 -> **2.2** (-12.0%) | 230.1 -> **295.0** | 577.8 -> **651.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.5% vs 30% floor, Casts: 1729). Increasing spread: b -13.8%, n +28.2%; Individual spell undertuned (WR: 41.6%, Casts: 1729, mult: 1.029) |
| `WLW` | Fey | Debuff / Control | 56.2 -> **57.4** (+2.1%) | - | 56.2 -> **57.4** | Individual spell undertuned (WR: 43.8%, Casts: 2487, mult: 1.021) |
| `WLE` | Fey | Setup - Location | 168.9 -> **194.2** (+15.0%) | - | 168.9 -> **194.2** | Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLD` | Fey | Ultimate | 26.7 -> **25.7** (-3.7%) | 197.4 -> **252.5** | 5297.3 -> **6514.9** | Location 'Enchanted Forest' beneficiaries overtuned (WR: 54.1%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1329). Shifted tuner focus: protected ultimate base floor at 26.7 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 19.2 -> **22.1** (+15.1%) | 71.9 -> **89.1** | 1399.7 -> **1991.2** | Location 'Enchanted Forest' beneficiaries overtuned (WR: 54.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.3% vs 30% floor, Casts: 1848). Increasing spread: b -12.7%, n +25.9% |
| `LWW` | Fey | Debuff / Control | 46.0 -> **45.1** (-2.0%) | - | 46.0 -> **45.1** | Individual spell overtuned (WR: 55.8%, Casts: 735, mult: 0.980) |
| `LWL` | Fey | Debuff / Control | 46.2 -> **47.4** (+2.6%) | - | 46.2 -> **47.4** | Individual spell undertuned (WR: 42.3%, Casts: 1569, mult: 1.027) |
| `LWD` | Fey | Conditional Strike | 1.6 -> **1.3** (-18.8%) | 328.3 -> **449.8** | 526.9 -> **586.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1600). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 41.9%, Casts: 1600, mult: 1.028) |
| `WDF` | Ice | Conditional Strike | 3.4 -> **3.0** (-11.8%) | 307.2 -> **426.2** | 1047.9 -> **1281.6** | Weather 'Raining' beneficiaries undertuned (WR: 39.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.7% vs 30% floor, Casts: 2785). Increasing spread: b -16.1%, n +33.1% |
| `WDW` | Ice | Buff / Sustain | 14.2 -> **14.0** (-1.4%) | - | 14.2 -> **14.0** | Individual spell overtuned (WR: 54.8%, Casts: 3010, mult: 0.984) |
| `WDE` | Ice | Setup - Weather | 28.9 -> **29.4** (+1.7%) | - | 28.9 -> **29.4** | Individual spell undertuned (WR: 45.2%, Casts: 2399, mult: 1.016) |
| `WDD` | Ice | Ultimate | 29.8 -> **32.2** (+8.1%) | 90.6 -> **85.2** | 2729.7 -> **2775.6** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 2.3% vs 16% floor, Casts: 1851, WR: 48.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DWF` | Ice | Debuff / Control | 42.4 -> **41.7** (-1.7%) | - | 42.4 -> **41.7** | Individual spell overtuned (WR: 55.1%, Casts: 1144, mult: 0.983) |
| `DWW` | Ice | Debuff / Control | 61.9 -> **71.2** (+15.0%) | - | 61.9 -> **71.2** | Buffed setup spell [DWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DWE` | Ice | Setup - Location | 36.0 -> **37.1** (+3.1%) | - | 36.0 -> **37.1** | Location 'Tundra' appliers undertuned (WR: 45.6%, casts: 2455); Individual spell undertuned (WR: 45.6%, Casts: 2455, mult: 1.015) |
| `DWD` | Ice | Conditional Strike | 6.4 -> **6.0** (-6.3%) | 40.3 -> **48.9** | 264.3 -> **299.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.7% vs 30% floor, Casts: 1722). Increasing spread: b -10.5%, n +21.4%; Individual spell undertuned (WR: 38.8%, Casts: 1722, mult: 1.041) |
| `ELF` | Wind | Conditional Strike | 5.3 -> **4.5** (-15.1%) | 167.3 -> **218.8** | 892.0 -> **989.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.4% vs 30% floor, Casts: 1585). Increasing spread: b -15.0%, n +30.8% |
| `ELW` | Wind | Debuff / Control | 66.4 -> **75.4** (+13.6%) | - | 66.4 -> **75.4** | Buffed setup spell [ELW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 54.0%, Casts: 1622, mult: 0.987) |
| `ELD` | Wind | Conditional Strike | 2.9 -> **2.6** (-10.3%) | 267.0 -> **365.6** | 777.2 -> **953.2** | Weather 'Raining' beneficiaries undertuned (WR: 39.3%); Weather 'Blizzard' appliers undertuned (WR: 43.3%, casts: 2536) |
| `LEF` | Wind | Conditional Strike | 2.0 -> **1.8** (-10.0%) | 162.3 -> **216.0** | 326.6 -> **390.6** | Status 'Burning' beneficiaries undertuned (WR: 46.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.9% vs 30% floor, Casts: 1586). Increasing spread: b -15.2%, n +31.2% |
| `LEW` | Wind | Debuff / Control | 55.1 -> **53.0** (-3.8%) | - | 55.1 -> **53.0** | Individual spell overtuned (WR: 60.8%, Casts: 2507, mult: 0.961) |
| `LEE` | Wind | Setup - Weather | 20.2 -> **20.6** (+2.0%) | - | 20.2 -> **20.6** | Individual spell undertuned (WR: 44.1%, Casts: 2892, mult: 1.020) |
| `LEL` | Wind | Buff / Sustain | 63.6 -> **73.1** (+14.9%) | - | 63.6 -> **73.1** | Buffed setup spell [LEL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `EDF` | Poison | Conditional Strike | 1.5 -> **1.3** (-13.3%) | 164.7 -> **214.4** | 248.5 -> **280.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 3164). Increasing spread: b -14.7%, n +30.2%; Individual spell overtuned (WR: 54.6%, Casts: 3164, mult: 0.985) |
| `EDL` | Poison | Debuff / Control | 1.6 -> **1.4** (-12.5%) | - | 1.6 -> **1.4** | Individual spell overtuned (WR: 84.0%, Casts: 2138, mult: 0.863) |
| `EDD` | Poison | Ultimate | 39.5 -> **43.6** (+10.4%) | 23.4 -> **22.6** | 963.8 -> **1029.0** | Location 'Swamp' beneficiaries undertuned (WR: 43.6%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 1.2% vs 16% floor, Casts: 1565, WR: 43.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DEW` | Poison | Debuff / Control | 16.9 -> **16.7** (-1.2%) | - | 16.9 -> **16.7** | Individual spell overtuned (WR: 54.4%, Casts: 1953, mult: 0.986) |
| `DEE` | Poison | Debuff / Control | 29.2 -> **33.6** (+15.1%) | - | 29.2 -> **33.6** | Buffed setup spell [DEE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 170.4 -> **222.3** | 34.3 -> **44.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 2307). Increasing spread: b -14.9%, n +30.5% |
| `DED` | Poison | Debuff / Control | 22.4 -> **23.0** (+2.7%) | - | 22.4 -> **23.0** | Individual spell undertuned (WR: 42.9%, Casts: 2929, mult: 1.025) |
| `LDF` | Cosmic | Debuff / Control | 84.0 -> **96.6** (+15.0%) | - | 84.0 -> **96.6** | Buffed setup spell [LDF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LDE` | Cosmic | Setup - Location | 25.6 -> **26.4** (+3.1%) | - | 25.6 -> **26.4** | Individual spell undertuned (WR: 41.2%, Casts: 1285, mult: 1.031) |
| `LDL` | Cosmic | Conditional Strike | 2.4 -> **2.1** (-12.5%) | 201.8 -> **273.3** | 486.7 -> **576.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1665). Increasing spread: b -17.3%, n +35.4%; Individual spell undertuned (WR: 37.8%, Casts: 1665, mult: 1.045) |
| `LDD` | Cosmic | Ultimate | 67.4 -> **66.6** (-1.2%) | 10.5 -> **13.7** | 775.1 -> **979.0** | Ultimate payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1593). Shifted tuner focus: protected ultimate base floor at 67.4 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDW, DDL, DEE, DFW, DWW, ELW, LEL, DLL, FEF, LWF) with +15% b tempo.; Individual spell overtuned (WR: 53.6%, Casts: 1593, mult: 0.988) |
| `DLF` | Cosmic | Conditional Strike | 2.7 -> **2.3** (-14.8%) | 177.4 -> **229.1** | 481.7 -> **529.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.4% vs 30% floor, Casts: 2740). Increasing spread: b -14.2%, n +29.1%; Individual spell overtuned (WR: 53.9%, Casts: 2740, mult: 0.987) |
| `DLL` | Cosmic | Conditional Strike | 6.8 -> **6.0** (-11.8%) | 83.5 -> **107.0** | 574.6 -> **648.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.6% vs 30% floor, Casts: 1884). Increasing spread: b -13.8%, n +28.2%; Individual spell undertuned (WR: 43.8%, Casts: 1884, mult: 1.021) |
