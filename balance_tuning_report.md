# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T13:05:49Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 103.3s  
**Total Spells Tuned:** 108 / 125  

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
| **Beasts** | 15,809 | 61.6% | 61.6% | 5.7 | Overtuned ⚠️ |
| **Blood** | 19,078 | 56.9% | 57.0% | 12.3 | Overtuned ⚠️ |
| **Plants** | 23,541 | 56.1% | 56.1% | 9.1 | Overtuned ⚠️ |
| **Water** | 8,159 | 55.4% | 55.5% | 9.6 | Overtuned ⚠️ |
| **Lightning** | 18,539 | 54.3% | 54.4% | 11.0 | Overtuned ⚠️ |
| **Fire** | 8,794 | 51.4% | 51.4% | 16.3 | Balanced ✅ |
| **Ghostfire** | 21,375 | 50.9% | 50.9% | 9.9 | Balanced ✅ |
| **Cosmic** | 19,428 | 48.6% | 48.6% | 14.3 | Balanced ✅ |
| **Poison** | 24,668 | 48.6% | 48.6% | 10.9 | Balanced ✅ |
| **Ice** | 31,750 | 47.2% | 47.2% | 13.8 | Balanced ✅ |
| **Dark** | 13,478 | 47.1% | 47.1% | 12.2 | Balanced ✅ |
| **Fey** | 19,377 | 46.4% | 46.4% | 8.1 | Undertuned ⚠️ |
| **Wind** | 21,911 | 46.0% | 46.0% | 9.0 | Undertuned ⚠️ |
| **Earth** | 14,012 | 44.0% | 44.0% | 10.6 | Undertuned ⚠️ |
| **Light** | 15,729 | 40.7% | 40.7% | 3.2 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 16,995 (48.5%) | 3,625 (50.2%) | 13.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 3,078 (34.9%) | 8,944 (53.2%) | 4.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,056 (55.6%) | 4,045 (51.3%) | 8.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 7,928 (73.0%) | 12,435 (38.3%) | 1.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 10,069 (49.8%) | 4,836 (55.1%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,182 (50.0%) | 4,176 (57.3%) | 3.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,467 (58.2%) | 3,676 (43.3%) | 4.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 59.3 -> **58.2** (-1.9%) | - | 59.3 -> **58.2** | Individual spell overtuned (WR: 55.6%, Casts: 1417, mult: 0.981) |
| `FFW` | Fire | Debuff / Control | 44.4 -> **43.5** (-2.0%) | - | 44.4 -> **43.5** | Status 'Burning' appliers overtuned on own (WR: 55.6%) |
| `FFL` | Fire | Debuff / Control | 7.8 -> **7.5** (-3.8%) | - | 7.8 -> **7.5** | Status 'Burning' appliers overtuned on own (WR: 55.6%); Individual spell overtuned (WR: 53.9%, Casts: 1910, mult: 0.987) |
| `FFD` | Fire | Conditional Strike | 19.1 -> **16.6** (-13.1%) | 3.6 -> **4.8** | 87.9 -> **96.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.8% vs 30% floor, Casts: 1408). Increasing spread: b -16.5%, n +33.8%; Individual spell undertuned (WR: 39.2%, Casts: 1408, mult: 1.039) |
| `WWF` | Water | Conditional Strike | 29.3 -> **24.1** (-17.7%) | 3.5 -> **4.4** | 131.8 -> **130.1** | Class Water overtuned (WR: 55.4%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.3% vs 30% floor, Casts: 1693). Increasing spread: b -12.7%, n +25.9% |
| `WWE` | Water | Setup - Weather | 19.1 -> **17.6** (-7.9%) | - | 19.1 -> **17.6** | Class Water overtuned (WR: 55.4%, factor: 0.978); Weather 'Raining' appliers overtuned on own (WR: 58.2%) |
| `WWL` | Water | Buff / Sustain | 58.8 -> **57.5** (-2.2%) | - | 58.8 -> **57.5** | Class Water overtuned (WR: 55.4%, factor: 0.978) |
| `WWD` | Water | Buff / Sustain | 43.5 -> **42.6** (-2.1%) | - | 43.5 -> **42.6** | Class Water overtuned (WR: 55.4%, factor: 0.978) |
| `EEF` | Earth | Conditional Strike | 22.9 -> **21.0** (-8.3%) | 3.5 -> **4.4** | 103.0 -> **113.4** | Class Earth undertuned (WR: 44.0%, factor: 1.024); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.6% vs 30% floor, Casts: 1999). Increasing spread: b -13.0%, n +26.5% |
| `EEW` | Earth | Buff / Sustain | 34.9 -> **35.7** (+2.3%) | - | 34.9 -> **35.7** | Class Earth undertuned (WR: 44.0%, factor: 1.024) |
| `EEE` | Earth | Conditional Strike | 4.6 -> **5.4** (+17.4%) | 1.6 -> **1.5** | 12.0 -> **13.5** | Class Earth undertuned (WR: 44.0%, factor: 1.024); Condition triggers excessively (N=1 conditions, Trigger Rate: 94.2% vs 55% ceiling, WR: 47.1%). Compressing spread: b +13.7%, n -21.9% |
| `LLF` | Light | Conditional Strike | 3.3 -> **3.0** (-9.1%) | 3.8 -> **5.1** | 15.8 -> **18.3** | Class Light undertuned (WR: 40.7%, factor: 1.037); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 5513). Increasing spread: b -17.2%, n +35.4% |
| `LLW` | Light | Debuff / Control | 25.0 -> **25.4** (+1.6%) | - | 25.0 -> **25.4** | Class Light undertuned (WR: 40.7%, factor: 1.037); Individual spell overtuned (WR: 56.2%, Casts: 1784, mult: 0.979) |
| `LLE` | Light | Setup - Weather | 21.6 -> **24.9** (+15.3%) | - | 21.6 -> **24.9** | Class Light undertuned (WR: 40.7%, factor: 1.037); Weather 'Sunny' appliers undertuned (WR: 34.9%, casts: 3078) |
| `LLL` | Light | Buff / Sustain | 32.7 -> **31.6** (-3.4%) | - | 32.7 -> **31.6** | Class Light undertuned (WR: 40.7%, factor: 1.037); Individual spell overtuned (WR: 67.7%, Casts: 1499, mult: 0.933) |
| `LLD` | Light | Ultimate | 19.2 -> **22.6** (+17.7%) | 9.9 -> **9.3** | 209.3 -> **232.8** | Class Light undertuned (WR: 40.7%, factor: 1.037); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 3855, WR: 36.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 17.9 -> **14.7** (-17.9%) | 4.0 -> **5.5** | 89.5 -> **95.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1731). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 46.2 -> **48.3** (+4.5%) | - | 46.2 -> **48.3** | Individual spell undertuned (WR: 37.6%, Casts: 4660, mult: 1.045) |
| `DDE` | Dark | Setup - Weather | 21.2 -> **22.5** (+6.1%) | - | 21.2 -> **22.5** | Weather 'Darkness' appliers undertuned (WR: 41.6%, casts: 2720); Individual spell undertuned (WR: 41.6%, Casts: 2720, mult: 1.029) |
| `DDL` | Dark | Debuff / Control | 25.0 -> **24.5** (-2.0%) | - | 25.0 -> **24.5** | Individual spell overtuned (WR: 55.5%, Casts: 1861, mult: 0.982) |
| `DDD` | Dark | Debuff / Control | 32.8 -> **31.3** (-4.6%) | - | 32.8 -> **31.3** | Individual spell overtuned (WR: 62.7%, Casts: 2506, mult: 0.953) |
| `FWF` | Ghostfire | Debuff / Control | 42.9 -> **40.3** (-6.1%) | - | 42.9 -> **40.3** | Status 'Burning' appliers overtuned on own (WR: 55.6%); Individual spell overtuned (WR: 61.2%, Casts: 1344, mult: 0.959) |
| `FWW` | Ghostfire | Debuff / Control | 15.0 -> **14.8** (-1.3%) | - | 15.0 -> **14.8** | Individual spell overtuned (WR: 53.6%, Casts: 1480, mult: 0.988) |
| `FWE` | Ghostfire | Setup - Location | 21.3 -> **24.8** (+16.4%) | - | 21.3 -> **24.8** | Location 'Graveyard' appliers undertuned (WR: 28.6%, casts: 3325); Individual spell undertuned (WR: 28.6%, Casts: 3325, mult: 1.082) |
| `FWD` | Ghostfire | Ultimate | 19.2 -> **20.7** (+7.8%) | 9.9 -> **9.3** | 209.3 -> **213.2** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4549, WR: 48.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `WFF` | Ghostfire | Conditional Strike | 18.6 -> **15.0** (-19.4%) | 3.7 -> **5.2** | 87.4 -> **93.0** | Status 'Bleeding' beneficiaries undertuned (WR: 38.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.1% vs 30% floor, Casts: 1013). Increasing spread: b -17.2%, n +35.3% |
| `WFW` | Ghostfire | Debuff / Control | 34.0 -> **32.5** (-4.4%) | - | 34.0 -> **32.5** | Individual spell overtuned (WR: 62.4%, Casts: 1231, mult: 0.955) |
| `WFE` | Ghostfire | Debuff / Control | 40.2 -> **34.0** (-15.4%) | - | 40.2 -> **34.0** | Status 'Bleeding' appliers overtuned on own (WR: 73.0%); Individual spell overtuned (WR: 70.7%, Casts: 2444, mult: 0.921) |
| `WFD` | Ghostfire | Conditional Strike | 19.0 -> **15.9** (-16.3%) | 3.7 -> **4.9** | 89.3 -> **93.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.5% vs 30% floor, Casts: 1414). Increasing spread: b -16.2%, n +33.3% |
| `FEF` | Beasts | Debuff / Control | 24.6 -> **22.3** (-9.3%) | - | 24.6 -> **22.3** | Class Beasts overtuned (WR: 61.6%, factor: 0.954); Individual spell overtuned (WR: 63.1%, Casts: 1724, mult: 0.952) |
| `FEW` | Beasts | Conditional Strike | 17.9 -> **13.9** (-22.3%) | 4.0 -> **5.2** | 89.5 -> **86.2** | Class Beasts overtuned (WR: 61.6%, factor: 0.954); Status 'Entangled' beneficiaries overtuned (WR: 57.3%) |
| `FEE` | Beasts | Buff / Sustain | 24.6 -> **23.5** (-4.5%) | - | 24.6 -> **23.5** | Class Beasts overtuned (WR: 61.6%, factor: 0.954) |
| `FEL` | Beasts | Buff / Sustain | 24.6 -> **23.8** (-3.3%) | - | 24.6 -> **23.8** | Class Beasts overtuned (WR: 61.6%, factor: 0.954); Individual spell undertuned (WR: 45.6%, Casts: 1328, mult: 1.014) |
| `FED` | Beasts | Conditional Strike | 6.0 -> **5.8** (-3.3%) | 2.0 -> **1.8** | 18.0 -> **16.2** | Class Beasts overtuned (WR: 61.6%, factor: 0.954); Condition triggers within target window (47.9%), but combo payoff is warping win rate (54.7%). Compressing spread: b +3.0%, n -8.0% |
| `EFF` | Beasts | Debuff / Control | 22.3 -> **17.2** (-22.9%) | 3.9 -> **5.3** | 109.3 -> **108.4** | Class Beasts overtuned (WR: 61.6%, factor: 0.954); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1661). Increasing spread: b -17.2%, n +35.4% |
| `EFW` | Beasts | Buff / Sustain | 24.1 -> **22.2** (-7.9%) | - | 24.1 -> **22.2** | Class Beasts overtuned (WR: 61.6%, factor: 0.954); Individual spell overtuned (WR: 59.3%, Casts: 1016, mult: 0.967) |
| `EFE` | Beasts | Buff / Sustain | 34.4 -> **31.8** (-7.6%) | - | 34.4 -> **31.8** | Class Beasts overtuned (WR: 61.6%, factor: 0.954); Individual spell overtuned (WR: 58.3%, Casts: 2092, mult: 0.971) |
| `EFL` | Beasts | Buff / Sustain | 25.8 -> **20.8** (-19.4%) | - | 25.8 -> **20.8** | Class Beasts overtuned (WR: 61.6%, factor: 0.954); Individual spell overtuned (WR: 87.9%, Casts: 2815, mult: 0.845) |
| `EFD` | Beasts | Ultimate | 18.9 -> **14.8** (-21.7%) | 9.9 -> **13.2** | 206.0 -> **210.2** | Class Beasts overtuned (WR: 61.6%, factor: 0.954); Status 'Entangled' beneficiaries overtuned (WR: 57.3%) |
| `FLF` | Lightning | Conditional Strike | 18.0 -> **14.2** (-21.1%) | 4.0 -> **5.4** | 90.0 -> **90.9** | Class Lightning overtuned (WR: 54.3%, factor: 0.983); Status 'Stunned' beneficiaries overtuned (WR: 55.1%) |
| `FLW` | Lightning | Debuff / Control | 46.3 -> **44.4** (-4.1%) | - | 46.3 -> **44.4** | Class Lightning overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 56.7%, Casts: 1377, mult: 0.977) |
| `FLE` | Lightning | Setup - Weather | 22.0 -> **22.3** (+1.4%) | - | 22.0 -> **22.3** | Class Lightning overtuned (WR: 54.3%, factor: 0.983); Weather 'Storming' appliers undertuned (WR: 45.2%, casts: 1773) |
| `FLL` | Lightning | Buff / Sustain | 25.5 -> **24.6** (-3.5%) | - | 25.5 -> **24.6** | Class Lightning overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 55.0%, Casts: 1277, mult: 0.983) |
| `FLD` | Lightning | Ultimate | 25.6 -> **20.6** (-19.5%) | 7.0 -> **9.4** | 204.8 -> **214.2** | Class Lightning overtuned (WR: 54.3%, factor: 0.983); Status 'Stunned' beneficiaries overtuned (WR: 55.1%) |
| `LFF` | Lightning | Conditional Strike | 18.2 -> **14.8** (-18.7%) | 3.9 -> **5.3** | 89.2 -> **93.2** | Class Lightning overtuned (WR: 54.3%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 1085). Increasing spread: b -17.4%, n +35.8% |
| `LFE` | Lightning | Debuff / Control | 47.2 -> **44.5** (-5.7%) | - | 47.2 -> **44.5** | Class Lightning overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 61.5%, Casts: 2279, mult: 0.958) |
| `LFL` | Lightning | Debuff / Control | 31.8 -> **25.8** (-18.9%) | 3.6 -> **4.5** | 146.3 -> **141.9** | Class Lightning overtuned (WR: 54.3%, factor: 0.983); Weather 'Darkness' beneficiaries overtuned (WR: 58.6%) |
| `LFD` | Lightning | Conditional Strike | 19.8 -> **15.9** (-19.7%) | 5.7 -> **7.7** | 132.7 -> **138.3** | Class Lightning overtuned (WR: 54.3%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.7% vs 30% floor, Casts: 882). Increasing spread: b -16.9%, n +34.7% |
| `FDF` | Blood | Conditional Strike | 17.9 -> **13.9** (-22.3%) | 4.0 -> **5.5** | 89.5 -> **90.4** | Class Blood overtuned (WR: 56.9%, factor: 0.972); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 945). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 62.2 -> **61.8** (-0.6%) | - | 62.2 -> **61.8** | Class Blood overtuned (WR: 56.9%, factor: 0.972); Individual spell undertuned (WR: 43.4%, Casts: 1910, mult: 1.023) |
| `FDE` | Blood | Setup - Weather | 20.0 -> **19.4** (-3.0%) | - | 20.0 -> **19.4** | Class Blood overtuned (WR: 56.9%, factor: 0.972) |
| `FDL` | Blood | Debuff / Control | 38.7 -> **32.1** (-17.1%) | - | 38.7 -> **32.1** | Class Blood overtuned (WR: 56.9%, factor: 0.972); Status 'Bleeding' appliers overtuned on own (WR: 73.0%) |
| `FDD` | Blood | Ultimate | 25.4 -> **19.5** (-23.2%) | 6.8 -> **9.0** | 198.1 -> **195.0** | Class Blood overtuned (WR: 56.9%, factor: 0.972); Weather 'Darkness' beneficiaries overtuned (WR: 58.6%) |
| `DFF` | Blood | Conditional Strike | 18.7 -> **15.3** (-18.2%) | 3.7 -> **5.1** | 87.9 -> **93.3** | Class Blood overtuned (WR: 56.9%, factor: 0.972); Status 'Bleeding' beneficiaries undertuned (WR: 38.3%) |
| `DFW` | Blood | Debuff / Control | 30.4 -> **24.0** (-21.1%) | - | 30.4 -> **24.0** | Class Blood overtuned (WR: 56.9%, factor: 0.972); Status 'Bleeding' appliers overtuned on own (WR: 73.0%) |
| `DFE` | Blood | Buff / Sustain | 37.1 -> **38.7** (+4.3%) | - | 37.1 -> **38.7** | Class Blood overtuned (WR: 56.9%, factor: 0.972); Individual spell undertuned (WR: 30.9%, Casts: 2313, mult: 1.073) |
| `DFL` | Blood | Buff / Sustain | 35.0 -> **32.8** (-6.3%) | - | 35.0 -> **32.8** | Class Blood overtuned (WR: 56.9%, factor: 0.972); Individual spell overtuned (WR: 60.2%, Casts: 1724, mult: 0.963) |
| `DFD` | Blood | Conditional Strike | 32.6 -> **35.8** (+9.8%) | 1.4 -> **1.0** | 78.2 -> **71.6** | Class Blood overtuned (WR: 56.9%, factor: 0.972); Condition triggers excessively (N=1 conditions, Trigger Rate: 92.1% vs 55% ceiling, WR: 62.5%). Compressing spread: b +18.2%, n -26.2% |
| `WEF` | Plants | Conditional Strike | 19.6 -> **16.0** (-18.4%) | 3.7 -> **4.9** | 92.1 -> **94.4** | Class Plants overtuned (WR: 56.1%, factor: 0.976); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.2% vs 30% floor, Casts: 1868). Increasing spread: b -16.3%, n +33.5% |
| `WEW` | Plants | Debuff / Control | 35.6 -> **35.3** (-0.8%) | - | 35.6 -> **35.3** | Class Plants overtuned (WR: 56.1%, factor: 0.976); Individual spell undertuned (WR: 45.1%, Casts: 1893, mult: 1.016) |
| `WEE` | Plants | Setup - Location | 20.0 -> **22.2** (+11.0%) | - | 20.0 -> **22.2** | Class Plants overtuned (WR: 56.1%, factor: 0.976); Location 'Jungle' appliers undertuned (WR: 31.7%, casts: 2598) |
| `WEL` | Plants | Debuff / Control | 45.0 -> **43.9** (-2.4%) | - | 45.0 -> **43.9** | Class Plants overtuned (WR: 56.1%, factor: 0.976) |
| `WED` | Plants | Conditional Strike | 24.0 -> **19.0** (-20.8%) | 4.0 -> **5.5** | 120.0 -> **123.5** | Class Plants overtuned (WR: 56.1%, factor: 0.976); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 1574). Increasing spread: b -17.8%, n +36.6% |
| `EWF` | Plants | Buff / Sustain | 23.5 -> **18.3** (-22.1%) | 3.6 -> **4.7** | 108.1 -> **104.3** | Class Plants overtuned (WR: 56.1%, factor: 0.976); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.5% vs 30% floor, Casts: 5089). Increasing spread: b -15.0%, n +30.7% |
| `EWW` | Plants | Debuff / Control | 33.6 -> **27.5** (-18.2%) | - | 33.6 -> **27.5** | Class Plants overtuned (WR: 56.1%, factor: 0.976); Individual spell overtuned (WR: 89.1%, Casts: 2507, mult: 0.840) |
| `EWL` | Plants | Debuff / Control | 60.0 -> **59.4** (-1.0%) | - | 60.0 -> **59.4** | Class Plants overtuned (WR: 56.1%, factor: 0.976); Individual spell undertuned (WR: 45.4%, Casts: 2724, mult: 1.015) |
| `EWD` | Plants | Conditional Strike | 17.4 -> **12.4** (-28.7%) | 3.9 -> **5.0** | 85.3 -> **74.4** | Class Plants overtuned (WR: 56.1%, factor: 0.976); Status 'Bleeding' appliers overtuned on own (WR: 73.0%) |
| `WLF` | Fey | Conditional Strike | 18.4 -> **15.3** (-16.8%) | 3.7 -> **5.0** | 86.5 -> **91.8** | Class Fey undertuned (WR: 46.4%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.8% vs 30% floor, Casts: 2048). Increasing spread: b -16.9%, n +34.7% |
| `WLW` | Fey | Debuff / Control | 45.0 -> **45.7** (+1.6%) | - | 45.0 -> **45.7** | Class Fey undertuned (WR: 46.4%, factor: 1.014) |
| `WLE` | Fey | Setup - Location | 20.7 -> **21.0** (+1.4%) | - | 20.7 -> **21.0** | Class Fey undertuned (WR: 46.4%, factor: 1.014) |
| `WLL` | Fey | Direct Damage | 60.9 -> **61.0** (+0.2%) | - | 60.9 -> **61.0** | Class Fey undertuned (WR: 46.4%, factor: 1.014); Individual spell overtuned (WR: 53.8%, Casts: 842, mult: 0.988) |
| `WLD` | Fey | Ultimate | 25.3 -> **20.7** (-18.2%) | 6.8 -> **9.0** | 197.3 -> **207.0** | Class Fey undertuned (WR: 46.4%, factor: 1.014); Weather 'Darkness' beneficiaries overtuned (WR: 58.6%) |
| `LWF` | Fey | Debuff / Control | 31.6 -> **27.0** (-14.6%) | 3.5 -> **4.6** | 142.2 -> **151.2** | Class Fey undertuned (WR: 46.4%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.7% vs 30% floor, Casts: 1379). Increasing spread: b -15.7%, n +32.2% |
| `LWW` | Fey | Debuff / Control | 35.0 -> **37.0** (+5.7%) | - | 35.0 -> **37.0** | Class Fey undertuned (WR: 46.4%, factor: 1.014); Individual spell undertuned (WR: 38.5%, Casts: 4672, mult: 1.042) |
| `LWL` | Fey | Debuff / Control | 35.0 -> **35.5** (+1.4%) | - | 35.0 -> **35.5** | Class Fey undertuned (WR: 46.4%, factor: 1.014) |
| `LWD` | Fey | Conditional Strike | 18.2 -> **15.1** (-17.0%) | 4.0 -> **5.5** | 91.0 -> **98.1** | Class Fey undertuned (WR: 46.4%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2394). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 20.2 -> **17.1** (-15.3%) | 3.7 -> **5.1** | 94.9 -> **104.3** | Weather 'Raining' beneficiaries undertuned (WR: 43.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.4% vs 30% floor, Casts: 1433). Increasing spread: b -16.7%, n +34.2% |
| `WDW` | Ice | Buff / Sustain | 15.2 -> **14.9** (-2.0%) | - | 15.2 -> **14.9** | Individual spell overtuned (WR: 55.4%, Casts: 1788, mult: 0.982) |
| `WDE` | Ice | Setup - Weather | 20.4 -> **21.7** (+6.4%) | - | 20.4 -> **21.7** | Individual spell undertuned (WR: 32.7%, Casts: 3444, mult: 1.065) |
| `WDD` | Ice | Ultimate | 26.6 -> **29.2** (+9.8%) | 7.0 -> **6.9** | 212.8 -> **230.7** | Weather 'Blizzard' beneficiaries undertuned (WR: 44.7%); Location 'Tundra' beneficiaries undertuned (WR: 44.7%) |
| `DWF` | Ice | Debuff / Control | 47.7 -> **48.3** (+1.3%) | - | 47.7 -> **48.3** | Individual spell undertuned (WR: 46.4%, Casts: 7442, mult: 1.012) |
| `DWW` | Ice | Debuff / Control | 36.6 -> **35.5** (-3.0%) | - | 36.6 -> **35.5** | Individual spell overtuned (WR: 58.9%, Casts: 1813, mult: 0.969) |
| `DWD` | Ice | Conditional Strike | 21.5 -> **18.3** (-14.9%) | 3.4 -> **4.2** | 94.6 -> **95.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.9% vs 30% floor, Casts: 1626). Increasing spread: b -12.0%, n +24.6%; Individual spell overtuned (WR: 59.7%, Casts: 1626, mult: 0.965) |
| `ELF` | Wind | Conditional Strike | 39.4 -> **32.5** (-17.5%) | 3.7 -> **5.2** | 185.2 -> **201.5** | Class Wind undertuned (WR: 46.0%, factor: 1.016); Status 'Bleeding' beneficiaries undertuned (WR: 38.3%) |
| `ELW` | Wind | Debuff / Control | 35.0 -> **34.9** (-0.3%) | - | 35.0 -> **34.9** | Class Wind undertuned (WR: 46.0%, factor: 1.016); Individual spell overtuned (WR: 55.4%, Casts: 1666, mult: 0.982) |
| `ELE` | Wind | Setup - Weather | 20.5 -> **19.9** (-2.9%) | - | 20.5 -> **19.9** | Class Wind undertuned (WR: 46.0%, factor: 1.016); Individual spell overtuned (WR: 61.7%, Casts: 1185, mult: 0.957) |
| `ELL` | Wind | Buff / Sustain | 34.5 -> **36.0** (+4.3%) | - | 34.5 -> **36.0** | Class Wind undertuned (WR: 46.0%, factor: 1.016); Individual spell undertuned (WR: 42.0%, Casts: 1807, mult: 1.028) |
| `ELD` | Wind | Conditional Strike | 19.5 -> **17.5** (-10.3%) | 3.7 -> **5.1** | 91.7 -> **106.8** | Class Wind undertuned (WR: 46.0%, factor: 1.016); Weather 'Raining' beneficiaries undertuned (WR: 43.3%) |
| `LEF` | Wind | Conditional Strike | 18.6 -> **15.7** (-15.6%) | 3.7 -> **4.9** | 87.4 -> **92.6** | Class Wind undertuned (WR: 46.0%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.1% vs 30% floor, Casts: 944). Increasing spread: b -16.0%, n +32.8% |
| `LEW` | Wind | Debuff / Control | 59.2 -> **58.6** (-1.0%) | - | 59.2 -> **58.6** | Class Wind undertuned (WR: 46.0%, factor: 1.016); Individual spell overtuned (WR: 57.5%, Casts: 4224, mult: 0.974) |
| `LEE` | Wind | Setup - Weather | 20.0 -> **21.3** (+6.5%) | - | 20.0 -> **21.3** | Class Wind undertuned (WR: 46.0%, factor: 1.016); Individual spell undertuned (WR: 37.0%, Casts: 3080, mult: 1.048) |
| `LEL` | Wind | Buff / Sustain | 35.4 -> **38.5** (+8.8%) | - | 35.4 -> **38.5** | Class Wind undertuned (WR: 46.0%, factor: 1.016); Individual spell undertuned (WR: 31.4%, Casts: 4287, mult: 1.071) |
| `EDF` | Poison | Conditional Strike | 19.2 -> **15.6** (-18.8%) | 3.8 -> **5.1** | 92.2 -> **95.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 1691). Increasing spread: b -17.1%, n +35.2%; Individual spell overtuned (WR: 55.9%, Casts: 1691, mult: 0.980) |
| `EDW` | Poison | Debuff / Control | 33.0 -> **31.6** (-4.2%) | - | 33.0 -> **31.6** | Individual spell overtuned (WR: 62.0%, Casts: 1412, mult: 0.956) |
| `EDE` | Poison | Setup - Location | 20.0 -> **20.5** (+2.5%) | - | 20.0 -> **20.5** | Location 'Swamp' appliers undertuned (WR: 46.0%, casts: 2770); Individual spell undertuned (WR: 46.0%, Casts: 2770, mult: 1.013) |
| `EDL` | Poison | Debuff / Control | 18.9 -> **16.3** (-13.8%) | - | 18.9 -> **16.3** | Individual spell overtuned (WR: 84.6%, Casts: 964, mult: 0.860) |
| `EDD` | Poison | Ultimate | 26.6 -> **31.9** (+19.9%) | 7.2 -> **7.9** | 218.1 -> **283.9** | Status 'Bleeding' beneficiaries undertuned (WR: 38.3%); Location 'Swamp' beneficiaries undertuned (WR: 22.0%) |
| `DEF` | Poison | Conditional Strike | 33.3 -> **32.0** (-3.9%) | 2.4 -> **2.4** | 113.2 -> **108.8** | Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 45.9% within [30%-55%] target window, WR: 61.2%).; Individual spell overtuned (WR: 61.2%, Casts: 2125, mult: 0.960) |
| `DEW` | Poison | Debuff / Control | 33.3 -> **31.3** (-6.0%) | - | 33.3 -> **31.3** | Individual spell overtuned (WR: 66.2%, Casts: 3093, mult: 0.939) |
| `DEL` | Poison | Conditional Strike | 2.0 -> **1.7** (-15.0%) | 3.7 -> **5.2** | 9.4 -> **10.5** | Status 'Bleeding' beneficiaries undertuned (WR: 38.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.1% vs 30% floor, Casts: 3905). Increasing spread: b -17.1%, n +35.2% |
| `LDW` | Cosmic | Debuff / Control | 47.2 -> **48.7** (+3.2%) | - | 47.2 -> **48.7** | Individual spell undertuned (WR: 40.8%, Casts: 2099, mult: 1.033) |
| `LDL` | Cosmic | Conditional Strike | 18.4 -> **16.5** (-10.3%) | 3.9 -> **4.9** | 90.2 -> **97.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.4% vs 30% floor, Casts: 2135). Increasing spread: b -13.1%, n +26.7%; Individual spell undertuned (WR: 41.4%, Casts: 2135, mult: 1.030) |
| `LDD` | Cosmic | Ultimate | 19.8 -> **16.2** (-18.2%) | 9.9 -> **13.6** | 215.8 -> **236.5** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1725). Increasing spread: b -18.0%, n +37.0% |
| `DLF` | Cosmic | Conditional Strike | 23.6 -> **19.6** (-16.9%) | 3.7 -> **5.0** | 110.9 -> **117.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.6% vs 30% floor, Casts: 3046). Increasing spread: b -17.0%, n +34.8% |
| `DLW` | Cosmic | Direct Damage | 60.0 -> **58.0** (-3.3%) | - | 60.0 -> **58.0** | Individual spell overtuned (WR: 59.3%, Casts: 1708, mult: 0.967) |
| `DLE` | Cosmic | Direct Damage | 37.0 -> **38.1** (+3.0%) | - | 37.0 -> **38.1** | Individual spell undertuned (WR: 41.3%, Casts: 2252, mult: 1.031) |
| `DLL` | Cosmic | Conditional Strike | 31.5 -> **26.6** (-15.6%) | 3.6 -> **4.5** | 144.9 -> **146.3** | Weather 'Darkness' beneficiaries overtuned (WR: 58.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.4% vs 30% floor, Casts: 1068). Increasing spread: b -14.6%, n +30.0% |
| `DLD` | Cosmic | Conditional Strike | 39.8 -> **45.0** (+13.1%) | 1.6 -> **1.5** | 103.5 -> **112.5** | Condition triggers excessively (N=1 conditions, Trigger Rate: 93.0% vs 55% ceiling, WR: 63.4%). Compressing spread: b +18.8%, n -26.9%; Individual spell overtuned (WR: 63.4%, Casts: 1505, mult: 0.951) |
