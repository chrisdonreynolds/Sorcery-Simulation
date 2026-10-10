# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T16:46:23Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 64.6s  
**Total Spells Tuned:** 117 / 125  

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
| **Light** | 5,460 | 68.2% | 68.3% | 1.8 | Overtuned ⚠️ |
| **Blood** | 19,153 | 64.8% | 64.8% | 8.8 | Overtuned ⚠️ |
| **Dark** | 12,725 | 58.4% | 58.4% | 7.9 | Overtuned ⚠️ |
| **Water** | 15,397 | 57.8% | 57.9% | 8.9 | Overtuned ⚠️ |
| **Beasts** | 26,844 | 56.7% | 56.7% | 5.9 | Overtuned ⚠️ |
| **Fire** | 21,074 | 56.1% | 56.1% | 7.9 | Overtuned ⚠️ |
| **Poison** | 18,826 | 55.1% | 55.1% | 4.4 | Overtuned ⚠️ |
| **Earth** | 20,529 | 55.1% | 55.1% | 10.2 | Overtuned ⚠️ |
| **Wind** | 15,764 | 55.1% | 55.1% | 7.3 | Overtuned ⚠️ |
| **Fey** | 27,302 | 49.2% | 49.2% | 6.9 | Balanced ✅ |
| **Lightning** | 28,436 | 45.6% | 45.6% | 5.0 | Undertuned ⚠️ |
| **Cosmic** | 35,996 | 44.5% | 44.5% | 8.0 | Undertuned ⚠️ |
| **Ghostfire** | 34,935 | 43.6% | 43.6% | 2.4 | Undertuned ⚠️ |
| **Ice** | 38,701 | 43.4% | 43.4% | 5.6 | Undertuned ⚠️ |
| **Plants** | 27,451 | 40.9% | 40.9% | 3.4 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 20,003 (53.6%) | 8,625 (34.5%) | 1.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 37 (47.1%) | 7,525 (27.3%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,051 (62.0%) | 9,384 (29.6%) | 3.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 14,439 (63.6%) | 16,894 (32.6%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 22,029 (54.1%) | 4,269 (48.8%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,672 (72.4%) | 10,208 (31.6%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 360 (19.3%) | 5,165 (37.2%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 25.5 -> **23.4** (-8.2%) | - | 25.5 -> **23.4** | Class Fire overtuned (WR: 56.1%, factor: 0.976); Individual spell overtuned (WR: 66.0%, Casts: 687, mult: 0.940) |
| `FFW` | Fire | Debuff / Control | 16.5 -> **15.4** (-6.7%) | - | 16.5 -> **15.4** | Class Fire overtuned (WR: 56.1%, factor: 0.976); Status 'Burning' appliers overtuned on own (WR: 62.0%) |
| `FFE` | Fire | Debuff / Control | 13.6 -> **12.4** (-8.8%) | - | 13.6 -> **12.4** | Class Fire overtuned (WR: 56.1%, factor: 0.976); Individual spell overtuned (WR: 67.8%, Casts: 10647, mult: 0.933) |
| `FFL` | Fire | Debuff / Control | 1.0 -> **0.8** (-20.0%) | - | 1.0 -> **0.8** | Class Fire overtuned (WR: 56.1%, factor: 0.976); Status 'Burning' appliers overtuned on own (WR: 62.0%) |
| `FFD` | Fire | Conditional Strike | 2.7 -> **2.4** (-11.1%) | 172.0 -> **250.8** | 467.1 -> **604.3** | Class Fire overtuned (WR: 56.1%, factor: 0.976); Status 'Burning' beneficiaries undertuned (WR: 29.6%) |
| `WWF` | Water | Conditional Strike | 3.0 -> **2.6** (-13.3%) | 128.6 -> **183.7** | 388.8 -> **480.2** | Class Water overtuned (WR: 57.8%, factor: 0.969); Status 'Burning' beneficiaries undertuned (WR: 29.6%) |
| `WWE` | Water | Setup - Weather | 157.2 -> **189.5** (+20.5%) | - | 157.2 -> **189.5** | Class Water overtuned (WR: 57.8%, factor: 0.969); Weather 'Raining' appliers undertuned (WR: 19.3%, casts: 360) |
| `WWL` | Water | Buff / Sustain | 34.8 -> **29.8** (-14.4%) | - | 34.8 -> **29.8** | Class Water overtuned (WR: 57.8%, factor: 0.969); Individual spell overtuned (WR: 79.1%, Casts: 8026, mult: 0.884) |
| `WWD` | Water | Buff / Sustain | 43.8 -> **38.0** (-13.2%) | - | 43.8 -> **38.0** | Class Water overtuned (WR: 57.8%, factor: 0.969); Individual spell overtuned (WR: 76.5%, Casts: 1022, mult: 0.896) |
| `EEF` | Earth | Conditional Strike | 4.1 -> **3.5** (-14.6%) | 196.7 -> **285.4** | 810.6 -> **1002.4** | Class Earth overtuned (WR: 55.1%, factor: 0.980); Status 'Frosty' beneficiaries undertuned (WR: 34.5%) |
| `EEW` | Earth | Buff / Sustain | 44.7 -> **41.3** (-7.6%) | - | 44.7 -> **41.3** | Class Earth overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 65.1%, Casts: 2221, mult: 0.944) |
| `EED` | Earth | Direct Damage | 2.8 -> **2.5** (-10.7%) | - | 2.8 -> **2.5** | Class Earth overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 69.4%, Casts: 6804, mult: 0.926) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 142.4 -> **192.3** | 14.3 -> **19.3** | Class Light overtuned (WR: 68.2%, factor: 0.927); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.4% vs 30% floor, Casts: 2355). Increasing spread: b -17.0%, n +35.0% |
| `LLW` | Light | Debuff / Control | 20.8 -> **17.9** (-13.9%) | - | 20.8 -> **17.9** | Class Light overtuned (WR: 68.2%, factor: 0.927); Individual spell overtuned (WR: 69.0%, Casts: 771, mult: 0.928) |
| `LLE` | Light | Setup - Weather | 186.6 -> **173.0** (-7.3%) | - | 186.6 -> **173.0** | Class Light overtuned (WR: 68.2%, factor: 0.927) |
| `LLL` | Light | Buff / Sustain | 10.7 -> **9.4** (-12.1%) | - | 10.7 -> **9.4** | Class Light overtuned (WR: 68.2%, factor: 0.927); Individual spell overtuned (WR: 63.3%, Casts: 1763, mult: 0.951) |
| `LLD` | Light | Ultimate | 14.5 -> **10.8** (-25.5%) | 39.0 -> **58.3** | 580.0 -> **640.4** | Class Light overtuned (WR: 68.2%, factor: 0.927); Weather 'Sunny' beneficiaries undertuned (WR: 27.3%) |
| `DDF` | Dark | Conditional Strike | 1.6 -> **1.2** (-25.0%) | 174.9 -> **239.6** | 281.4 -> **288.7** | Class Dark overtuned (WR: 58.4%, factor: 0.967); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 781). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 28.3 -> **26.1** (-7.8%) | - | 28.3 -> **26.1** | Class Dark overtuned (WR: 58.4%, factor: 0.967); Individual spell overtuned (WR: 62.4%, Casts: 7384, mult: 0.955) |
| `DDE` | Dark | Setup - Weather | 87.1 -> **105.0** (+20.6%) | - | 87.1 -> **105.0** | Class Dark overtuned (WR: 58.4%, factor: 0.967); Weather 'Darkness' appliers undertuned (WR: 18.9%, casts: 1676) |
| `DDL` | Dark | Debuff / Control | 16.1 -> **14.8** (-8.1%) | - | 16.1 -> **14.8** | Class Dark overtuned (WR: 58.4%, factor: 0.967); Individual spell overtuned (WR: 63.1%, Casts: 427, mult: 0.952) |
| `DDD` | Dark | Debuff / Control | 6.7 -> **5.9** (-11.9%) | - | 6.7 -> **5.9** | Class Dark overtuned (WR: 58.4%, factor: 0.967); Individual spell overtuned (WR: 72.5%, Casts: 2457, mult: 0.913) |
| `FWF` | Ghostfire | Debuff / Control | 4.1 -> **3.4** (-17.1%) | - | 4.1 -> **3.4** | Class Ghostfire undertuned (WR: 43.6%, factor: 1.025); Status 'Burning' appliers overtuned on own (WR: 62.0%) |
| `FWE` | Ghostfire | Setup - Location | 89.6 -> **116.0** (+29.5%) | - | 89.6 -> **116.0** | Class Ghostfire undertuned (WR: 43.6%, factor: 1.025); Location 'Graveyard' appliers undertuned (WR: 15.0%, casts: 35) |
| `FWL` | Ghostfire | Debuff / Control | 29.1 -> **25.8** (-11.3%) | - | 29.1 -> **25.8** | Class Ghostfire undertuned (WR: 43.6%, factor: 1.025); Status 'Cursed' appliers overtuned on own (WR: 62.9%) |
| `FWD` | Ghostfire | Ultimate | 15.4 -> **18.2** (+18.2%) | 29.6 -> **31.8** | 471.2 -> **597.0** | Class Ghostfire undertuned (WR: 43.6%, factor: 1.025); Status 'Cursed' beneficiaries undertuned (WR: 32.8%) |
| `WFF` | Ghostfire | Conditional Strike | 1.9 -> **1.7** (-10.5%) | 253.2 -> **370.1** | 483.0 -> **630.9** | Class Ghostfire undertuned (WR: 43.6%, factor: 1.025); Status 'Bleeding' beneficiaries undertuned (WR: 32.6%) |
| `WFW` | Ghostfire | Debuff / Control | 9.1 -> **8.7** (-4.4%) | - | 9.1 -> **8.7** | Class Ghostfire undertuned (WR: 43.6%, factor: 1.025); Individual spell overtuned (WR: 66.6%, Casts: 3787, mult: 0.937) |
| `WFE` | Ghostfire | Debuff / Control | 1.9 -> **1.5** (-21.1%) | - | 1.9 -> **1.5** | Class Ghostfire undertuned (WR: 43.6%, factor: 1.025); Status 'Bleeding' appliers overtuned on own (WR: 63.6%) |
| `WFL` | Ghostfire | Buff / Sustain | 41.3 -> **42.9** (+3.9%) | - | 41.3 -> **42.9** | Class Ghostfire undertuned (WR: 43.6%, factor: 1.025); Individual spell undertuned (WR: 45.9%, Casts: 1693, mult: 1.014) |
| `WFD` | Ghostfire | Conditional Strike | 2.1 -> **2.0** (-4.8%) | 151.2 -> **206.5** | 319.6 -> **415.0** | Class Ghostfire undertuned (WR: 43.6%, factor: 1.025); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 9435). Increasing spread: b -17.8%, n +36.6% |
| `FEF` | Beasts | Debuff / Control | 16.6 -> **15.8** (-4.8%) | - | 16.6 -> **15.8** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 56.9%, Casts: 8632, mult: 0.976) |
| `FEW` | Beasts | Conditional Strike | 3.3 -> **3.0** (-9.1%) | 246.2 -> **360.3** | 815.8 -> **1083.9** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Status 'Entangled' beneficiaries undertuned (WR: 31.6%) |
| `FEE` | Beasts | Buff / Sustain | 44.9 -> **48.0** (+6.9%) | - | 44.9 -> **48.0** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell undertuned (WR: 25.1%, Casts: 2260, mult: 1.098) |
| `FEL` | Beasts | Buff / Sustain | 93.2 -> **89.1** (-4.4%) | - | 93.2 -> **89.1** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 55.4%, Casts: 3144, mult: 0.982) |
| `FED` | Beasts | Conditional Strike | 3.8 -> **3.2** (-15.8%) | 3.5 -> **3.5** | 17.1 -> **14.4** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.7% vs 30% floor, Casts: 1381). Increasing spread: b -16.5%, n +33.9% |
| `EFF` | Beasts | Debuff / Control | 3.1 -> **2.2** (-29.0%) | 157.6 -> **215.9** | 491.7 -> **477.2** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 48). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 42.1 -> **43.0** (+2.1%) | - | 42.1 -> **43.0** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell undertuned (WR: 29.0%, Casts: 19, mult: 1.050) |
| `EFE` | Beasts | Buff / Sustain | 26.5 -> **24.0** (-9.4%) | - | 26.5 -> **24.0** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 68.5%, Casts: 3545, mult: 0.930) |
| `EFL` | Beasts | Buff / Sustain | 3.1 -> **2.5** (-19.4%) | - | 3.1 -> **2.5** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 93.6%, Casts: 3223, mult: 0.820) |
| `EFD` | Beasts | Ultimate | 13.1 -> **13.8** (+5.3%) | 89.4 -> **91.9** | 1184.2 -> **1282.0** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Status 'Entangled' beneficiaries undertuned (WR: 31.6%) |
| `FLF` | Lightning | Conditional Strike | 2.3 -> **1.9** (-17.4%) | 207.7 -> **284.5** | 480.0 -> **542.4** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 89). Increasing spread: b -18.0%, n +37.0% |
| `FLW` | Lightning | Debuff / Control | 21.6 -> **19.3** (-10.6%) | - | 21.6 -> **19.3** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Status 'Stunned' appliers overtuned on own (WR: 54.1%) |
| `FLE` | Lightning | Setup - Weather | 45.1 -> **60.5** (+34.1%) | - | 45.1 -> **60.5** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Weather 'Storming' appliers undertuned (WR: 7.4%, casts: 4045) |
| `FLL` | Lightning | Buff / Sustain | 39.0 -> **35.4** (-9.2%) | - | 39.0 -> **35.4** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Individual spell overtuned (WR: 77.2%, Casts: 707, mult: 0.893) |
| `FLD` | Lightning | Ultimate | 19.1 -> **15.9** (-16.8%) | 32.1 -> **44.0** | 632.2 -> **715.5** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4180). Increasing spread: b -18.0%, n +37.0% |
| `LFF` | Lightning | Conditional Strike | 3.0 -> **2.8** (-6.7%) | 165.9 -> **227.3** | 500.7 -> **639.2** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6322). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 25.8 -> **26.9** (+4.3%) | - | 25.8 -> **26.9** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Individual spell undertuned (WR: 42.4%, Casts: 2562, mult: 1.026) |
| `LFE` | Lightning | Debuff / Control | 19.0 -> **17.1** (-10.0%) | - | 19.0 -> **17.1** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Status 'Stunned' appliers overtuned on own (WR: 54.1%) |
| `LFL` | Lightning | Debuff / Control | 3.8 -> **3.4** (-10.5%) | 114.3 -> **149.9** | 438.1 -> **513.1** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.0% vs 30% floor, Casts: 654). Increasing spread: b -15.2%, n +31.1% |
| `LFD` | Lightning | Conditional Strike | 2.4 -> **2.2** (-8.3%) | 199.5 -> **273.3** | 481.2 -> **603.5** | Class Lightning undertuned (WR: 45.6%, factor: 1.018); Status 'Stunned' appliers overtuned on own (WR: 54.1%) |
| `FDF` | Blood | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 174.9 -> **239.6** | 281.4 -> **336.8** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 203). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 81.7 -> **67.9** (-16.9%) | - | 81.7 -> **67.9** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Individual spell overtuned (WR: 79.3%, Casts: 973, mult: 0.883) |
| `FDE` | Blood | Setup - Weather | 56.4 -> **52.4** (-7.1%) | - | 56.4 -> **52.4** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Individual spell overtuned (WR: 53.8%, Casts: 2087, mult: 0.988) |
| `FDL` | Blood | Debuff / Control | 1.7 -> **1.3** (-23.5%) | - | 1.7 -> **1.3** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Status 'Bleeding' appliers overtuned on own (WR: 63.6%) |
| `FDD` | Blood | Ultimate | 9.6 -> **10.0** (+4.2%) | 32.8 -> **30.8** | 324.5 -> **318.0** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 5045, WR: 43.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 3.1 -> **2.4** (-22.6%) | 197.5 -> **289.0** | 615.4 -> **696.0** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Status 'Bleeding' beneficiaries undertuned (WR: 32.6%) |
| `DFW` | Blood | Debuff / Control | 1.3 -> **1.0** (-23.1%) | - | 1.3 -> **1.0** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Status 'Bleeding' appliers overtuned on own (WR: 63.6%) |
| `DFE` | Blood | Buff / Sustain | 114.1 -> **117.5** (+3.0%) | - | 114.1 -> **117.5** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Individual spell undertuned (WR: 25.8%, Casts: 472, mult: 1.094) |
| `DFL` | Blood | Buff / Sustain | 12.8 -> **10.7** (-16.4%) | - | 12.8 -> **10.7** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Individual spell overtuned (WR: 78.4%, Casts: 4187, mult: 0.887) |
| `DFD` | Blood | Conditional Strike | 88.7 -> **93.3** (+5.2%) | 0.1 -> **0.1** | 97.6 -> **102.6** | Class Blood overtuned (WR: 64.8%, factor: 0.941); Condition triggers excessively (N=1 conditions, Trigger Rate: 90.9% vs 55% ceiling, WR: 69.0%). Compressing spread: b +20.6%, n -28.3% |
| `WEF` | Plants | Conditional Strike | 2.3 -> **2.0** (-13.0%) | 197.7 -> **275.8** | 457.0 -> **553.6** | Class Plants undertuned (WR: 40.9%, factor: 1.036); Location 'Jungle' beneficiaries undertuned (WR: 45.5%) |
| `WEW` | Plants | Debuff / Control | 44.4 -> **51.1** (+15.1%) | - | 44.4 -> **51.1** | Class Plants undertuned (WR: 40.9%, factor: 1.036); Individual spell undertuned (WR: 22.2%, Casts: 1239, mult: 1.110) |
| `WEE` | Plants | Setup - Location | 100.0 -> **130.6** (+30.6%) | - | 100.0 -> **130.6** | Class Plants undertuned (WR: 40.9%, factor: 1.036); Location 'Jungle' appliers undertuned (WR: 17.4%, casts: 2848) |
| `WEL` | Plants | Debuff / Control | 25.6 -> **22.3** (-12.9%) | - | 25.6 -> **22.3** | Class Plants undertuned (WR: 40.9%, factor: 1.036); Status 'Entangled' appliers overtuned on own (WR: 72.4%) |
| `WED` | Plants | Conditional Strike | 21.8 -> **17.4** (-20.2%) | 8.6 -> **11.8** | 209.3 -> **222.7** | Class Plants undertuned (WR: 40.9%, factor: 1.036); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 2340). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 3.1 -> **2.9** (-6.5%) | 168.1 -> **251.3** | 524.2 -> **731.7** | Class Plants undertuned (WR: 40.9%, factor: 1.036); Weather 'Sunny' beneficiaries undertuned (WR: 27.3%) |
| `EWW` | Plants | Debuff / Control | 3.4 -> **2.9** (-14.7%) | - | 3.4 -> **2.9** | Class Plants undertuned (WR: 40.9%, factor: 1.036); Individual spell overtuned (WR: 92.3%, Casts: 2152, mult: 0.825) |
| `EWL` | Plants | Debuff / Control | 33.6 -> **30.0** (-10.7%) | - | 33.6 -> **30.0** | Class Plants undertuned (WR: 40.9%, factor: 1.036); Individual spell overtuned (WR: 84.3%, Casts: 2464, mult: 0.861) |
| `EWD` | Plants | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 241.0 -> **354.5** | 169.4 -> **213.3** | Class Plants undertuned (WR: 40.9%, factor: 1.036); Status 'Bleeding' appliers overtuned on own (WR: 63.6%) |
| `WLF` | Fey | Conditional Strike | 2.6 -> **2.2** (-15.4%) | 132.8 -> **194.5** | 347.9 -> **430.1** | Status 'Cursed' beneficiaries undertuned (WR: 32.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 10). Increasing spread: b -18.0%, n +37.0% |
| `WLW` | Fey | Debuff / Control | 23.7 -> **20.5** (-13.5%) | - | 23.7 -> **20.5** | Status 'Cursed' appliers overtuned on own (WR: 62.9%); Individual spell overtuned (WR: 74.4%, Casts: 6983, mult: 0.905) |
| `WLE` | Fey | Setup - Location | 151.0 -> **159.0** (+5.3%) | - | 151.0 -> **159.0** | Location 'Enchanted Forest' appliers undertuned (WR: 42.5%, casts: 902); Individual spell undertuned (WR: 42.4%, Casts: 902, mult: 1.026) |
| `WLL` | Fey | Direct Damage | 79.1 -> **71.8** (-9.2%) | - | 79.1 -> **71.8** | Individual spell overtuned (WR: 73.8%, Casts: 973, mult: 0.907) |
| `WLD` | Fey | Ultimate | 18.7 -> **15.0** (-19.8%) | 40.4 -> **54.0** | 774.2 -> **825.0** | Location 'Enchanted Forest' beneficiaries overtuned (WR: 56.0%); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 6217). Increasing spread: b -18.0%, n +37.0% |
| `LWF` | Fey | Debuff / Control | 6.1 -> **5.0** (-18.0%) | 158.9 -> **212.1** | 975.4 -> **1065.5** | Location 'Enchanted Forest' beneficiaries overtuned (WR: 56.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 698). Increasing spread: b -17.9%, n +36.8% |
| `LWW` | Fey | Debuff / Control | 57.0 -> **51.4** (-9.8%) | - | 57.0 -> **51.4** | Individual spell overtuned (WR: 75.2%, Casts: 141, mult: 0.901) |
| `LWL` | Fey | Debuff / Control | 115.0 -> **133.8** (+16.3%) | - | 115.0 -> **133.8** | Individual spell undertuned (WR: 10.2%, Casts: 847, mult: 1.163) |
| `LWD` | Fey | Conditional Strike | 4.8 -> **4.2** (-12.5%) | 174.9 -> **239.6** | 844.3 -> **1010.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6302). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 34.8%, Casts: 6302, mult: 1.057) |
| `WDF` | Ice | Conditional Strike | 4.2 -> **3.7** (-11.9%) | 273.1 -> **393.3** | 1151.2 -> **1458.9** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Status 'Stunned' appliers overtuned on own (WR: 54.1%) |
| `WDW` | Ice | Buff / Sustain | 33.4 -> **37.2** (+11.4%) | - | 33.4 -> **37.2** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Status 'Frosty' appliers overtuned on own (WR: 53.6%) |
| `WDE` | Ice | Setup - Weather | 52.6 -> **62.5** (+18.8%) | - | 52.6 -> **62.5** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Individual spell undertuned (WR: 11.5%, Casts: 7080, mult: 1.158) |
| `WDL` | Ice | Debuff / Control | 25.1 -> **23.4** (-6.8%) | - | 25.1 -> **23.4** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Status 'Frosty' appliers overtuned on own (WR: 53.6%) |
| `WDD` | Ice | Ultimate | 19.5 -> **16.1** (-17.4%) | 23.2 -> **30.5** | 471.9 -> **507.2** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Weather 'Blizzard' beneficiaries overtuned (WR: 54.9%) |
| `DWF` | Ice | Debuff / Control | 23.3 -> **22.3** (-4.3%) | - | 23.3 -> **22.3** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Status 'Frosty' appliers overtuned on own (WR: 53.6%) |
| `DWW` | Ice | Debuff / Control | 26.4 -> **25.9** (-1.9%) | - | 26.4 -> **25.9** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Individual spell overtuned (WR: 61.6%, Casts: 2809, mult: 0.958) |
| `DWE` | Ice | Setup - Location | 102.7 -> **124.1** (+20.8%) | - | 102.7 -> **124.1** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Location 'Tundra' appliers undertuned (WR: 27.1%, casts: 212) |
| `DWL` | Ice | Debuff / Control | 25.5 -> **24.1** (-5.5%) | - | 25.5 -> **24.1** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Status 'Frosty' appliers overtuned on own (WR: 53.6%) |
| `DWD` | Ice | Conditional Strike | 4.9 -> **4.3** (-12.2%) | 160.8 -> **228.0** | 792.8 -> **984.7** | Class Ice undertuned (WR: 43.4%, factor: 1.026); Status 'Frosty' beneficiaries undertuned (WR: 34.5%) |
| `ELF` | Wind | Conditional Strike | 7.5 -> **6.3** (-16.0%) | 229.3 -> **335.0** | 1727.2 -> **2116.8** | Class Wind overtuned (WR: 55.1%, factor: 0.980); Status 'Bleeding' beneficiaries undertuned (WR: 32.6%) |
| `ELW` | Wind | Debuff / Control | 35.4 -> **33.4** (-5.6%) | - | 35.4 -> **33.4** | Class Wind overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 60.5%, Casts: 1480, mult: 0.962) |
| `ELE` | Wind | Setup - Weather | 62.0 -> **60.7** (-2.1%) | - | 62.0 -> **60.7** | Class Wind overtuned (WR: 55.1%, factor: 0.980) |
| `ELL` | Wind | Buff / Sustain | 96.0 -> **98.1** (+2.2%) | - | 96.0 -> **98.1** | Class Wind overtuned (WR: 55.1%, factor: 0.980); Individual spell undertuned (WR: 38.0%, Casts: 882, mult: 1.044) |
| `ELD` | Wind | Conditional Strike | 6.3 -> **5.1** (-19.0%) | 245.1 -> **353.0** | 1550.4 -> **1805.4** | Class Wind overtuned (WR: 55.1%, factor: 0.980); Weather 'Raining' beneficiaries undertuned (WR: 37.2%) |
| `LEF` | Wind | Conditional Strike | 4.1 -> **3.3** (-19.5%) | 173.2 -> **255.5** | 714.2 -> **846.4** | Class Wind overtuned (WR: 55.1%, factor: 0.980); Status 'Burning' beneficiaries undertuned (WR: 29.6%) |
| `LEW` | Wind | Debuff / Control | 39.5 -> **33.8** (-14.4%) | - | 39.5 -> **33.8** | Class Wind overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 81.5%, Casts: 3868, mult: 0.873) |
| `LEE` | Wind | Setup - Weather | 67.6 -> **66.2** (-2.1%) | - | 67.6 -> **66.2** | Class Wind overtuned (WR: 55.1%, factor: 0.980) |
| `LEL` | Wind | Buff / Sustain | 93.7 -> **95.6** (+2.0%) | - | 93.7 -> **95.6** | Class Wind overtuned (WR: 55.1%, factor: 0.980); Individual spell undertuned (WR: 38.5%, Casts: 1295, mult: 1.042) |
| `EDF` | Poison | Conditional Strike | 1.9 -> **1.6** (-15.8%) | 128.5 -> **176.0** | 246.0 -> **283.2** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 101). Increasing spread: b -18.0%, n +37.0% |
| `EDW` | Poison | Debuff / Control | 6.7 -> **5.9** (-11.9%) | - | 6.7 -> **5.9** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 74.2%, Casts: 3836, mult: 0.906) |
| `EDE` | Poison | Setup - Location | 75.0 -> **94.4** (+25.9%) | - | 75.0 -> **94.4** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Location 'Swamp' appliers undertuned (WR: 13.8%, casts: 1745) |
| `EDL` | Poison | Debuff / Control | 1.4 -> **1.2** (-14.3%) | - | 1.4 -> **1.2** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 88.3%, Casts: 2070, mult: 0.843) |
| `EDD` | Poison | Ultimate | 14.8 -> **16.3** (+10.1%) | 44.9 -> **47.1** | 679.3 -> **784.0** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Status 'Bleeding' beneficiaries undertuned (WR: 32.6%) |
| `DEF` | Poison | Conditional Strike | 12.8 -> **11.3** (-11.7%) | 3.0 -> **3.0** | 51.2 -> **45.2** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 33.9% within [30%-55%] target window, WR: 75.1%). |
| `DEW` | Poison | Debuff / Control | 7.3 -> **6.2** (-15.1%) | - | 7.3 -> **6.2** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 83.4%, Casts: 2233, mult: 0.865) |
| `DEE` | Poison | Debuff / Control | 15.8 -> **16.1** (+1.9%) | - | 15.8 -> **16.1** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Individual spell undertuned (WR: 38.9%, Casts: 96, mult: 1.040) |
| `DEL` | Poison | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 230.9 -> **338.3** | 92.8 -> **101.8** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Status 'Bleeding' beneficiaries undertuned (WR: 32.6%) |
| `DED` | Poison | Debuff / Control | 19.2 -> **18.4** (-4.2%) | - | 19.2 -> **18.4** | Class Poison overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 56.0%, Casts: 1690, mult: 0.979) |
| `LDF` | Cosmic | Debuff / Control | 27.0 -> **26.6** (-1.5%) | - | 27.0 -> **26.6** | Class Cosmic undertuned (WR: 44.5%, factor: 1.022); Individual spell overtuned (WR: 60.5%, Casts: 1620, mult: 0.962) |
| `LDW` | Cosmic | Debuff / Control | 17.9 -> **17.0** (-5.0%) | - | 17.9 -> **17.0** | Class Cosmic undertuned (WR: 44.5%, factor: 1.022); Status 'Stunned' appliers overtuned on own (WR: 54.1%) |
| `LDE` | Cosmic | Setup - Location | 30.6 -> **35.5** (+16.0%) | - | 30.6 -> **35.5** | Class Cosmic undertuned (WR: 44.5%, factor: 1.022); Individual spell undertuned (WR: 16.6%, Casts: 7899, mult: 1.135) |
| `LDL` | Cosmic | Conditional Strike | 3.5 -> **2.9** (-17.1%) | 148.1 -> **202.9** | 521.9 -> **591.3** | Class Cosmic undertuned (WR: 44.5%, factor: 1.022); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1837). Increasing spread: b -18.0%, n +37.0% |
| `LDD` | Cosmic | Ultimate | 11.5 -> **13.2** (+14.8%) | 45.3 -> **42.6** | 532.4 -> **575.5** | Class Cosmic undertuned (WR: 44.5%, factor: 1.022); Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 7776, WR: 39.1%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 3.4 -> **3.1** (-8.8%) | 132.3 -> **181.3** | 453.2 -> **565.1** | Class Cosmic undertuned (WR: 44.5%, factor: 1.022); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2872). Increasing spread: b -18.0%, n +37.0% |
| `DLW` | Cosmic | Direct Damage | 27.4 -> **25.9** (-5.5%) | - | 27.4 -> **25.9** | Class Cosmic undertuned (WR: 44.5%, factor: 1.022); Individual spell overtuned (WR: 69.8%, Casts: 7517, mult: 0.924) |
| `DLE` | Cosmic | Direct Damage | 93.1 -> **110.6** (+18.8%) | - | 93.1 -> **110.6** | Class Cosmic undertuned (WR: 44.5%, factor: 1.022); Individual spell undertuned (WR: 10.3%, Casts: 1419, mult: 1.163) |
| `DLL` | Cosmic | Conditional Strike | 4.0 -> **3.1** (-22.5%) | 128.4 -> **172.0** | 517.6 -> **536.3** | Class Cosmic undertuned (WR: 44.5%, factor: 1.022); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.7% vs 30% floor, Casts: 325). Increasing spread: b -16.5%, n +33.9% |
