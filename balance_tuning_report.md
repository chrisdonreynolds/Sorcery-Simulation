# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T23:54:24Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 542.0s  
**Total Spells Tuned:** 99 / 125  

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
| **Poison** | 23,451 | 54.5% | 54.5% | 10.0 | Overtuned ⚠️ |
| **Fire** | 10,208 | 52.9% | 52.9% | 14.1 | Balanced ✅ |
| **Earth** | 9,631 | 52.8% | 52.8% | 20.6 | Balanced ✅ |
| **Light** | 10,006 | 52.6% | 52.6% | 9.1 | Balanced ✅ |
| **Blood** | 21,217 | 52.4% | 52.4% | 14.2 | Balanced ✅ |
| **Beasts** | 22,914 | 51.8% | 51.8% | 6.7 | Balanced ✅ |
| **Ghostfire** | 21,359 | 50.4% | 50.4% | 14.6 | Balanced ✅ |
| **Plants** | 21,927 | 50.0% | 50.0% | 9.1 | Balanced ✅ |
| **Cosmic** | 19,792 | 49.9% | 49.9% | 16.0 | Balanced ✅ |
| **Ice** | 19,490 | 49.6% | 49.6% | 12.9 | Balanced ✅ |
| **Dark** | 10,049 | 48.8% | 48.8% | 10.5 | Balanced ✅ |
| **Wind** | 19,682 | 48.2% | 48.2% | 7.0 | Balanced ✅ |
| **Fey** | 18,268 | 46.9% | 46.9% | 12.8 | Balanced ✅ |
| **Lightning** | 21,428 | 46.9% | 46.9% | 9.8 | Balanced ✅ |
| **Water** | 10,092 | 45.1% | 45.1% | 6.6 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 8,103 (51.6%) | 3,138 (44.8%) | 23.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,429 (52.5%) | 4,547 (49.8%) | 8.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,304 (57.6%) | 3,925 (52.4%) | 10.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,432 (62.9%) | 9,316 (46.9%) | 5.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 13,107 (47.5%) | 4,624 (46.6%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,640 (53.0%) | 7,105 (45.4%) | 1.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,149 (33.5%) | 5,644 (44.8%) | 4.9% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 41.6 -> **40.5** (-2.6%) | - | 41.6 -> **40.5** | Status 'Burning' appliers overtuned on own (WR: 57.6%) |
| `FFL` | Fire | Debuff / Control | 5.6 -> **5.2** (-7.1%) | - | 5.6 -> **5.2** | Status 'Burning' appliers overtuned on own (WR: 57.6%); Individual spell overtuned (WR: 62.7%, Casts: 2084, mult: 0.953) |
| `FFD` | Fire | Conditional Strike | 4.2 -> **3.6** (-14.3%) | 49.4 -> **64.8** | 211.7 -> **236.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.9% vs 30% floor, Casts: 1598). Increasing spread: b -15.2%, n +31.3% |
| `WWF` | Water | Conditional Strike | 8.7 -> **7.9** (-9.2%) | 37.2 -> **45.6** | 332.3 -> **368.1** | Class Water undertuned (WR: 45.1%, factor: 1.019); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.2% vs 30% floor, Casts: 1067). Increasing spread: b -11.1%, n +22.6% |
| `WWE` | Water | Setup - Weather | 37.2 -> **42.6** (+14.5%) | - | 37.2 -> **42.6** | Class Water undertuned (WR: 45.1%, factor: 1.019); Weather 'Raining' appliers undertuned (WR: 33.5%, casts: 2149) |
| `WWL` | Water | Buff / Sustain | 68.7 -> **70.0** (+1.9%) | - | 68.7 -> **70.0** | Class Water undertuned (WR: 45.1%, factor: 1.019) |
| `WWD` | Water | Buff / Sustain | 48.5 -> **49.4** (+1.9%) | - | 48.5 -> **49.4** | Class Water undertuned (WR: 45.1%, factor: 1.019) |
| `EEF` | Earth | Conditional Strike | 14.1 -> **12.9** (-8.5%) | 12.6 -> **15.0** | 191.8 -> **206.4** | Status 'Frosty' beneficiaries undertuned (WR: 44.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 24.4% vs 30% floor, Casts: 1375). Increasing spread: b -8.3%, n +16.7% |
| `EEW` | Earth | Buff / Sustain | 29.4 -> **28.5** (-3.1%) | - | 29.4 -> **28.5** | Individual spell overtuned (WR: 58.3%, Casts: 1679, mult: 0.971) |
| `LLF` | Light | Conditional Strike | 3.8 -> **4.3** (+13.2%) | 59.0 -> **78.5** | 228.0 -> **341.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.7% vs 30% floor, Casts: 2712). Increasing spread: b -16.1%, n +33.1%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 40.4 -> **47.0** (+16.3%) | - | 40.4 -> **47.0** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell undertuned (WR: 46.5%, Casts: 2422, mult: 1.011) |
| `LLE` | Light | Setup - Weather | 61.2 -> **70.4** (+15.0%) | - | 61.2 -> **70.4** | Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 23.3 -> **22.5** (-3.4%) | - | 23.3 -> **22.5** | Individual spell overtuned (WR: 60.0%, Casts: 1588, mult: 0.964) |
| `LLD` | Light | Ultimate | 34.9 -> **34.9** (+0.0%) | 20.9 -> **27.2** | 764.3 -> **984.2** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1855). Shifted tuner focus: protected ultimate base floor at 34.9 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 2.5 -> **2.1** (-16.0%) | 93.0 -> **127.4** | 235.0 -> **269.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2212). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 46.0%, Casts: 2212, mult: 1.013) |
| `DDW` | Dark | Debuff / Control | 52.9 -> **60.8** (+14.9%) | - | 52.9 -> **60.8** | Buffed setup spell [DDW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DDE` | Dark | Setup - Weather | 65.5 -> **75.3** (+15.0%) | - | 65.5 -> **75.3** | Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 26.1 -> **30.0** (+14.9%) | - | 26.1 -> **30.0** | Buffed setup spell [DDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DDD` | Dark | Debuff / Control | 25.1 -> **24.4** (-2.8%) | - | 25.1 -> **24.4** | Individual spell overtuned (WR: 58.1%, Casts: 1273, mult: 0.972) |
| `FWF` | Ghostfire | Debuff / Control | 28.2 -> **26.3** (-6.7%) | - | 28.2 -> **26.3** | Status 'Burning' appliers overtuned on own (WR: 57.6%); Individual spell overtuned (WR: 61.2%, Casts: 2035, mult: 0.959) |
| `FWW` | Ghostfire | Debuff / Control | 29.9 -> **34.4** (+15.1%) | - | 29.9 -> **34.4** | Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 69.8 -> **87.3** (+25.1%) | - | 69.8 -> **87.3** | Location 'Graveyard' appliers undertuned (WR: 38.0%, casts: 2583); Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 75.9 -> **87.3** (+15.0%) | - | 75.9 -> **87.3** | Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 49.0 -> **49.0** (+0.0%) | 19.5 -> **25.3** | 1004.5 -> **1288.7** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 1545). Shifted tuner focus: protected ultimate base floor at 49.0 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 4.2 -> **3.6** (-14.3%) | 52.8 -> **69.3** | 226.0 -> **253.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.9% vs 30% floor, Casts: 2305). Increasing spread: b -15.2%, n +31.2%; Individual spell undertuned (WR: 46.0%, Casts: 2305, mult: 1.013) |
| `WFW` | Ghostfire | Debuff / Control | 27.2 -> **26.8** (-1.5%) | - | 27.2 -> **26.8** | Individual spell overtuned (WR: 54.4%, Casts: 2576, mult: 0.985) |
| `WFE` | Ghostfire | Debuff / Control | 29.7 -> **26.0** (-12.5%) | - | 29.7 -> **26.0** | Status 'Bleeding' appliers overtuned on own (WR: 62.9%); Individual spell overtuned (WR: 71.6%, Casts: 1835, mult: 0.916) |
| `WFL` | Ghostfire | Buff / Sustain | 42.1 -> **42.9** (+1.9%) | - | 42.1 -> **42.9** | Individual spell undertuned (WR: 44.2%, Casts: 2375, mult: 1.019) |
| `WFD` | Ghostfire | Conditional Strike | 5.0 -> **4.2** (-16.0%) | 46.1 -> **60.4** | 235.5 -> **257.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.1% vs 30% floor, Casts: 1658). Increasing spread: b -15.2%, n +31.1% |
| `FEF` | Beasts | Debuff / Control | 30.5 -> **35.7** (+17.0%) | - | 30.5 -> **35.7** | Buffed setup spell [FEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell undertuned (WR: 44.8%, Casts: 1290, mult: 1.017) |
| `FEW` | Beasts | Conditional Strike | 2.6 -> **2.2** (-15.4%) | 94.4 -> **131.1** | 248.0 -> **290.6** | Status 'Entangled' beneficiaries undertuned (WR: 45.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 2267). Increasing spread: b -17.7%, n +36.4% |
| `FEE` | Beasts | Buff / Sustain | 28.1 -> **29.1** (+3.6%) | - | 28.1 -> **29.1** | Individual spell undertuned (WR: 40.4%, Casts: 2540, mult: 1.034) |
| `FEL` | Beasts | Buff / Sustain | 31.0 -> **32.1** (+3.5%) | - | 31.0 -> **32.1** | Individual spell undertuned (WR: 39.9%, Casts: 2821, mult: 1.036) |
| `EFF` | Beasts | Debuff / Control | 3.3 -> **2.7** (-18.2%) | 84.1 -> **114.7** | 280.8 -> **312.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 2493). Increasing spread: b -17.7%, n +36.4% |
| `EFW` | Beasts | Buff / Sustain | 24.1 -> **23.4** (-2.9%) | - | 24.1 -> **23.4** | Individual spell overtuned (WR: 58.4%, Casts: 2391, mult: 0.970) |
| `EFL` | Beasts | Buff / Sustain | 6.3 -> **5.3** (-15.9%) | - | 6.3 -> **5.3** | Individual spell overtuned (WR: 87.0%, Casts: 1970, mult: 0.849) |
| `EFD` | Beasts | Ultimate | 37.0 -> **36.3** (-1.9%) | 28.3 -> **37.8** | 1084.1 -> **1408.4** | Status 'Entangled' beneficiaries undertuned (WR: 45.4%); Location 'Jungle' beneficiaries undertuned (WR: 46.5%) |
| `FLF` | Lightning | Conditional Strike | 2.8 -> **2.3** (-17.9%) | 113.9 -> **155.6** | 321.7 -> **360.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 2637). Increasing spread: b -17.8%, n +36.7% |
| `FLE` | Lightning | Setup - Weather | 31.3 -> **33.1** (+5.8%) | - | 31.3 -> **33.1** | Weather 'Storming' appliers undertuned (WR: 42.0%, casts: 1575); Individual spell undertuned (WR: 42.0%, Casts: 1575, mult: 1.028) |
| `FLL` | Lightning | Buff / Sustain | 26.8 -> **27.5** (+2.6%) | - | 26.8 -> **27.5** | Individual spell undertuned (WR: 42.8%, Casts: 1734, mult: 1.025) |
| `FLD` | Lightning | Ultimate | 68.9 -> **76.0** (+10.3%) | 8.6 -> **8.3** | 661.4 -> **706.8** | Weather 'Storming' beneficiaries undertuned (WR: 43.7%); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1987, WR: 43.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `LFF` | Lightning | Conditional Strike | 3.1 -> **2.6** (-16.1%) | 77.7 -> **105.6** | 244.0 -> **277.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.3% vs 30% floor, Casts: 1442). Increasing spread: b -17.5%, n +35.9% |
| `LFE` | Lightning | Debuff / Control | 50.2 -> **51.5** (+2.6%) | - | 50.2 -> **51.5** | Individual spell undertuned (WR: 42.7%, Casts: 2609, mult: 1.025) |
| `LFL` | Lightning | Debuff / Control | 18.8 -> **21.6** (+14.9%) | 40.7 -> **52.9** | 784.0 -> **1164.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.4% vs 30% floor, Casts: 3163). Increasing spread: b -14.6%, n +30.0%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LFD` | Lightning | Conditional Strike | 6.2 -> **5.4** (-12.9%) | 72.4 -> **94.6** | 455.1 -> **516.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.6% vs 30% floor, Casts: 2517). Increasing spread: b -14.9%, n +30.6%; Individual spell undertuned (WR: 42.3%, Casts: 2517, mult: 1.027) |
| `FDF` | Blood | Conditional Strike | 2.8 -> **2.3** (-17.9%) | 93.2 -> **127.7** | 263.8 -> **296.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1962). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 43.5%, Casts: 1962, mult: 1.022) |
| `FDW` | Blood | Direct Damage | 64.8 -> **69.4** (+7.1%) | - | 64.8 -> **69.4** | Individual spell undertuned (WR: 31.2%, Casts: 2259, mult: 1.072) |
| `FDL` | Blood | Debuff / Control | 20.9 -> **18.5** (-11.5%) | - | 20.9 -> **18.5** | Status 'Bleeding' appliers overtuned on own (WR: 62.9%); Individual spell overtuned (WR: 68.8%, Casts: 2855, mult: 0.929) |
| `FDD` | Blood | Ultimate | 49.4 -> **53.4** (+8.1%) | 7.0 -> **6.6** | 395.2 -> **405.8** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 2372, WR: 47.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 3.4 -> **2.9** (-14.7%) | 52.8 -> **68.7** | 182.9 -> **202.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.3% vs 30% floor, Casts: 1996). Increasing spread: b -14.7%, n +30.1% |
| `DFW` | Blood | Debuff / Control | 19.5 -> **19.6** (+0.5%) | - | 19.5 -> **19.6** | Status 'Bleeding' appliers overtuned on own (WR: 62.9%); Buffed setup spell [DFW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DFE` | Blood | Buff / Sustain | 39.9 -> **40.6** (+1.8%) | - | 39.9 -> **40.6** | Individual spell undertuned (WR: 44.6%, Casts: 1450, mult: 1.018) |
| `DFL` | Blood | Buff / Sustain | 32.1 -> **32.7** (+1.9%) | - | 32.1 -> **32.7** | Individual spell undertuned (WR: 44.8%, Casts: 870, mult: 1.017) |
| `DFD` | Blood | Conditional Strike | 110.7 -> **126.2** (+14.0%) | 0.1 -> **0.1** | 121.8 -> **138.8** | Condition triggers excessively (N=1 conditions, Trigger Rate: 95.7% vs 55% ceiling, WR: 48.0%). Compressing spread: b +14.0%, n -22.5% |
| `WEF` | Plants | Conditional Strike | 4.6 -> **4.1** (-10.9%) | 39.7 -> **52.6** | 187.2 -> **219.8** | Location 'Jungle' beneficiaries undertuned (WR: 46.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.7% vs 30% floor, Casts: 2109). Increasing spread: b -14.9%, n +30.6% |
| `WEW` | Plants | Debuff / Control | 131.0 -> **150.6** (+15.0%) | - | 131.0 -> **150.6** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WED` | Plants | Conditional Strike | 8.2 -> **6.7** (-18.3%) | 26.2 -> **35.9** | 223.0 -> **247.2** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1372). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 4.5 -> **3.9** (-13.3%) | 31.6 -> **39.6** | 146.7 -> **158.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.9% vs 30% floor, Casts: 2692). Increasing spread: b -12.4%, n +25.4% |
| `EWW` | Plants | Debuff / Control | 8.0 -> **6.9** (-13.7%) | - | 8.0 -> **6.9** | Individual spell overtuned (WR: 82.9%, Casts: 1830, mult: 0.868) |
| `EWL` | Plants | Debuff / Control | 63.6 -> **64.5** (+1.4%) | - | 63.6 -> **64.5** | Individual spell undertuned (WR: 45.6%, Casts: 3298, mult: 1.014) |
| `EWD` | Plants | Conditional Strike | 11.8 -> **9.7** (-17.8%) | 81.8 -> **112.1** | 977.0 -> **1097.1** | Status 'Bleeding' appliers overtuned on own (WR: 62.9%); Status 'Entangled' beneficiaries undertuned (WR: 45.4%) |
| `WLF` | Fey | Conditional Strike | 4.1 -> **3.5** (-14.6%) | 71.4 -> **93.1** | 296.8 -> **329.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.9% vs 30% floor, Casts: 1877). Increasing spread: b -14.8%, n +30.4% |
| `WLE` | Fey | Setup - Location | 100.6 -> **115.7** (+15.0%) | - | 100.6 -> **115.7** | Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 58.0 -> **56.2** (-3.1%) | - | 58.0 -> **56.2** | Individual spell overtuned (WR: 58.8%, Casts: 1522, mult: 0.969) |
| `WLD` | Fey | Ultimate | 27.8 -> **27.8** (+0.0%) | 72.3 -> **94.0** | 2037.7 -> **2641.0** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1935). Shifted tuner focus: protected ultimate base floor at 27.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 13.9 -> **16.2** (+16.5%) | 29.5 -> **37.5** | 423.9 -> **623.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.8% vs 30% floor, Casts: 1955). Increasing spread: b -13.3%, n +27.1%; Buffed setup spell [LWF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LWW` | Fey | Debuff / Control | 44.1 -> **44.9** (+1.8%) | - | 44.1 -> **44.9** | Individual spell undertuned (WR: 44.3%, Casts: 1788, mult: 1.019) |
| `LWD` | Fey | Conditional Strike | 3.2 -> **2.7** (-15.6%) | 93.2 -> **127.7** | 301.4 -> **347.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1605). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 37.7%, Casts: 1605, mult: 1.045) |
| `WDF` | Ice | Conditional Strike | 5.0 -> **4.4** (-12.0%) | 88.0 -> **118.8** | 445.0 -> **527.1** | Weather 'Raining' beneficiaries undertuned (WR: 44.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.7% vs 30% floor, Casts: 2430). Increasing spread: b -15.7%, n +32.2% |
| `WDW` | Ice | Buff / Sustain | 14.8 -> **14.4** (-2.7%) | - | 14.8 -> **14.4** | Individual spell overtuned (WR: 56.9%, Casts: 3134, mult: 0.976) |
| `WDD` | Ice | Ultimate | 27.9 -> **27.4** (-1.8%) | 49.8 -> **60.5** | 1417.3 -> **1685.1** | Weather 'Blizzard' beneficiaries overtuned (WR: 55.0%); Location 'Tundra' beneficiaries overtuned (WR: 55.0%) |
| `DWW` | Ice | Debuff / Control | 42.2 -> **48.5** (+14.9%) | - | 42.2 -> **48.5** | Buffed setup spell [DWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DWL` | Ice | Debuff / Control | 42.2 -> **42.8** (+1.4%) | - | 42.2 -> **42.8** | Individual spell undertuned (WR: 45.9%, Casts: 2424, mult: 1.014) |
| `DWD` | Ice | Conditional Strike | 9.3 -> **8.7** (-6.5%) | 18.0 -> **21.8** | 176.7 -> **198.4** | Status 'Frosty' beneficiaries undertuned (WR: 44.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 22.0% vs 30% floor, Casts: 1763). Increasing spread: b -9.2%, n +18.7% |
| `ELF` | Wind | Conditional Strike | 9.1 -> **7.9** (-13.2%) | 55.6 -> **73.5** | 515.1 -> **588.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.7% vs 30% floor, Casts: 1658). Increasing spread: b -15.7%, n +32.3%; Individual spell undertuned (WR: 43.0%, Casts: 1658, mult: 1.024) |
| `ELW` | Wind | Debuff / Control | 45.5 -> **52.3** (+14.9%) | - | 45.5 -> **52.3** | Buffed setup spell [ELW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `ELL` | Wind | Buff / Sustain | 37.0 -> **37.5** (+1.4%) | - | 37.0 -> **37.5** | Individual spell undertuned (WR: 45.9%, Casts: 1584, mult: 1.013) |
| `ELD` | Wind | Conditional Strike | 5.6 -> **4.7** (-16.1%) | 75.4 -> **102.7** | 427.8 -> **487.4** | Weather 'Raining' beneficiaries undertuned (WR: 44.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.3% vs 30% floor, Casts: 3214). Increasing spread: b -16.3%, n +33.4% |
| `LEF` | Wind | Conditional Strike | 3.5 -> **3.0** (-14.3%) | 58.5 -> **76.2** | 208.2 -> **231.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 1260). Increasing spread: b -14.8%, n +30.2% |
| `LEW` | Wind | Debuff / Control | 57.2 -> **56.3** (-1.6%) | - | 57.2 -> **56.3** | Individual spell overtuned (WR: 54.8%, Casts: 2207, mult: 0.984) |
| `LEL` | Wind | Buff / Sustain | 41.3 -> **48.3** (+16.9%) | - | 41.3 -> **48.3** | Buffed setup spell [LEL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell undertuned (WR: 45.2%, Casts: 1806, mult: 1.016) |
| `EDF` | Poison | Conditional Strike | 3.1 -> **2.6** (-16.1%) | 60.0 -> **76.8** | 189.1 -> **202.3** | Class Poison overtuned (WR: 54.5%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.7% vs 30% floor, Casts: 1782). Increasing spread: b -13.7%, n +28.1% |
| `EDW` | Poison | Debuff / Control | 17.5 -> **16.7** (-4.6%) | - | 17.5 -> **16.7** | Class Poison overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 58.3%, Casts: 2481, mult: 0.971) |
| `EDE` | Poison | Setup - Location | 52.0 -> **51.1** (-1.7%) | - | 52.0 -> **51.1** | Class Poison overtuned (WR: 54.5%, factor: 0.982) |
| `EDL` | Poison | Debuff / Control | 3.2 -> **2.7** (-15.6%) | - | 3.2 -> **2.7** | Class Poison overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 83.7%, Casts: 2219, mult: 0.864) |
| `EDD` | Poison | Ultimate | 29.1 -> **31.5** (+8.2%) | 27.8 -> **26.7** | 838.1 -> **872.5** | Class Poison overtuned (WR: 54.5%, factor: 0.982); Location 'Swamp' beneficiaries undertuned (WR: 44.3%) |
| `DEF` | Poison | Conditional Strike | 32.5 -> **33.5** (+3.1%) | 1.5 -> **1.4** | 81.2 -> **80.4** | Class Poison overtuned (WR: 54.5%, factor: 0.982); Condition triggers excessively (N=1 conditions, Trigger Rate: 55.3% vs 55% ceiling, WR: 47.1%). Compressing spread: b +5.1%, n -8.1% |
| `DEW` | Poison | Debuff / Control | 19.6 -> **18.7** (-4.6%) | - | 19.6 -> **18.7** | Class Poison overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 58.3%, Casts: 3646, mult: 0.971) |
| `DEE` | Poison | Debuff / Control | 21.2 -> **23.9** (+12.7%) | - | 21.2 -> **23.9** | Class Poison overtuned (WR: 54.5%, factor: 0.982); Buffed setup spell [DEE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 56.6 -> **74.2** | 17.3 -> **15.0** | Class Poison overtuned (WR: 54.5%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.1% vs 30% floor, Casts: 1600). Increasing spread: b -15.2%, n +31.1% |
| `DED` | Poison | Debuff / Control | 23.0 -> **22.6** (-1.7%) | - | 23.0 -> **22.6** | Class Poison overtuned (WR: 54.5%, factor: 0.982) |
| `LDF` | Cosmic | Debuff / Control | 57.5 -> **67.7** (+17.7%) | - | 57.5 -> **67.7** | Buffed setup spell [LDF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell undertuned (WR: 43.1%, Casts: 969, mult: 1.024) |
| `LDW` | Cosmic | Debuff / Control | 47.4 -> **45.5** (-4.0%) | - | 47.4 -> **45.5** | Individual spell overtuned (WR: 61.2%, Casts: 2634, mult: 0.960) |
| `LDL` | Cosmic | Conditional Strike | 4.2 -> **3.7** (-11.9%) | 62.1 -> **82.8** | 265.0 -> **310.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.4% vs 30% floor, Casts: 2196). Increasing spread: b -16.3%, n +33.4%; Individual spell undertuned (WR: 38.4%, Casts: 2196, mult: 1.042) |
| `LDD` | Cosmic | Ultimate | 62.4 -> **62.4** (+0.0%) | 5.1 -> **6.6** | 380.6 -> **474.2** | Ultimate payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1618). Shifted tuner focus: protected ultimate base floor at 62.4 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDW, DDL, DEE, DFW, DWW, ELW, LEL, DLL, FEF, LWF) with +15% b tempo. |
| `DLF` | Cosmic | Conditional Strike | 5.0 -> **4.4** (-12.0%) | 60.7 -> **79.8** | 308.5 -> **355.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 2523). Increasing spread: b -15.3%, n +31.4%; Individual spell undertuned (WR: 40.4%, Casts: 2523, mult: 1.034) |
| `DLW` | Cosmic | Direct Damage | 61.3 -> **60.6** (-1.1%) | - | 61.3 -> **60.6** | Individual spell overtuned (WR: 53.7%, Casts: 2431, mult: 0.988) |
| `DLE` | Cosmic | Direct Damage | 44.8 -> **44.2** (-1.3%) | - | 44.8 -> **44.2** | Individual spell overtuned (WR: 54.0%, Casts: 1677, mult: 0.987) |
| `DLL` | Cosmic | Conditional Strike | 11.4 -> **9.9** (-13.2%) | 32.4 -> **41.2** | 380.8 -> **417.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.7% vs 30% floor, Casts: 1504). Increasing spread: b -13.3%, n +27.2% |
