# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T14:17:15Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 113.3s  
**Total Spells Tuned:** 116 / 125  

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
| **Poison** | 21,856 | 59.1% | 59.2% | 9.9 | Overtuned ⚠️ |
| **Plants** | 26,350 | 58.0% | 58.0% | 5.2 | Overtuned ⚠️ |
| **Cosmic** | 18,845 | 55.6% | 55.6% | 13.2 | Overtuned ⚠️ |
| **Lightning** | 20,360 | 55.4% | 55.5% | 9.6 | Overtuned ⚠️ |
| **Water** | 8,706 | 55.0% | 55.1% | 11.2 | Overtuned ⚠️ |
| **Fire** | 10,358 | 55.0% | 55.0% | 19.2 | Overtuned ⚠️ |
| **Ghostfire** | 26,564 | 54.9% | 54.9% | 9.3 | Overtuned ⚠️ |
| **Dark** | 14,557 | 51.2% | 51.2% | 10.9 | Balanced ✅ |
| **Wind** | 22,839 | 50.4% | 50.4% | 10.5 | Balanced ✅ |
| **Beasts** | 21,971 | 46.4% | 46.4% | 3.1 | Undertuned ⚠️ |
| **Light** | 23,385 | 46.1% | 46.1% | 1.3 | Undertuned ⚠️ |
| **Blood** | 20,658 | 45.8% | 45.8% | 8.0 | Undertuned ⚠️ |
| **Ice** | 25,879 | 44.0% | 44.0% | 9.9 | Undertuned ⚠️ |
| **Earth** | 15,964 | 42.1% | 42.0% | 8.4 | Undertuned ⚠️ |
| **Fey** | 24,267 | 38.0% | 38.0% | 5.2 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 12,134 (49.7%) | 4,139 (50.4%) | 4.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 9,004 (16.2%) | 12,275 (50.0%) | 3.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 8,623 (69.2%) | 13,816 (48.4%) | 2.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 7,141 (79.8%) | 10,007 (47.0%) | 1.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 12,302 (66.3%) | 5,355 (42.8%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,261 (65.4%) | 5,625 (40.5%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,696 (39.3%) | 1,309 (50.6%) | 1.6% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 55.0 -> **49.1** (-10.7%) | - | 55.0 -> **49.1** | Class Fire overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 72.9%, Casts: 1543, mult: 0.911) |
| `FFW` | Fire | Debuff / Control | 42.3 -> **39.4** (-6.9%) | - | 42.3 -> **39.4** | Class Fire overtuned (WR: 55.0%, factor: 0.980); Status 'Burning' appliers overtuned on own (WR: 69.2%) |
| `FFE` | Fire | Debuff / Control | 33.4 -> **32.7** (-2.1%) | - | 33.4 -> **32.7** | Class Fire overtuned (WR: 55.0%, factor: 0.980) |
| `FFL` | Fire | Debuff / Control | 6.5 -> **5.5** (-15.4%) | - | 6.5 -> **5.5** | Class Fire overtuned (WR: 55.0%, factor: 0.980); Status 'Burning' appliers overtuned on own (WR: 69.2%) |
| `FFD` | Fire | Conditional Strike | 14.5 -> **11.8** (-18.6%) | 6.5 -> **8.8** | 108.8 -> **115.6** | Class Fire overtuned (WR: 55.0%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.4% vs 30% floor, Casts: 2975). Increasing spread: b -17.1%, n +35.0% |
| `WWF` | Water | Conditional Strike | 20.1 -> **15.5** (-22.9%) | 5.8 -> **7.7** | 136.7 -> **134.8** | Class Water overtuned (WR: 55.0%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 2753). Increasing spread: b -16.0%, n +32.9% |
| `WWE` | Water | Setup - Weather | 22.0 -> **23.2** (+5.5%) | - | 22.0 -> **23.2** | Class Water overtuned (WR: 55.0%, factor: 0.980); Weather 'Raining' appliers undertuned (WR: 39.3%, casts: 1696) |
| `WWL` | Water | Buff / Sustain | 57.1 -> **53.5** (-6.3%) | - | 57.1 -> **53.5** | Class Water overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 62.2%, Casts: 1698, mult: 0.956) |
| `WWD` | Water | Buff / Sustain | 39.8 -> **38.0** (-4.5%) | - | 39.8 -> **38.0** | Class Water overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 57.1%, Casts: 785, mult: 0.976) |
| `EEF` | Earth | Conditional Strike | 18.7 -> **14.3** (-23.5%) | 6.0 -> **8.0** | 130.9 -> **128.7** | Class Earth undertuned (WR: 42.1%, factor: 1.032); Status 'Stunned' appliers overtuned on own (WR: 66.3%) |
| `EEW` | Earth | Buff / Sustain | 41.0 -> **45.3** (+10.5%) | - | 41.0 -> **45.3** | Class Earth undertuned (WR: 42.1%, factor: 1.032); Individual spell undertuned (WR: 31.1%, Casts: 6447, mult: 1.072) |
| `EEE` | Earth | Conditional Strike | 6.3 -> **7.2** (+14.3%) | 1.5 -> **1.5** | 15.8 -> **18.0** | Class Earth undertuned (WR: 42.1%, factor: 1.032); Condition triggers excessively (N=1 conditions, Trigger Rate: 90.2% vs 55% ceiling, WR: 71.0%). Compressing spread: b +21.2%, n -28.9% |
| `EED` | Earth | Direct Damage | 6.0 -> **6.2** (+3.3%) | - | 6.0 -> **6.2** | Class Earth undertuned (WR: 42.1%, factor: 1.032) |
| `LLF` | Light | Conditional Strike | 2.4 -> **1.9** (-20.8%) | 6.9 -> **9.4** | 19.0 -> **19.8** | Class Light undertuned (WR: 46.1%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 6834). Increasing spread: b -17.4%, n +35.7% |
| `LLW` | Light | Debuff / Control | 24.6 -> **25.0** (+1.6%) | - | 24.6 -> **25.0** | Class Light undertuned (WR: 46.1%, factor: 1.016) |
| `LLE` | Light | Setup - Weather | 24.9 -> **32.1** (+28.9%) | - | 24.9 -> **32.1** | Class Light undertuned (WR: 46.1%, factor: 1.016); Weather 'Sunny' appliers undertuned (WR: 16.2%, casts: 9004) |
| `LLL` | Light | Buff / Sustain | 32.5 -> **29.7** (-8.6%) | - | 32.5 -> **29.7** | Class Light undertuned (WR: 46.1%, factor: 1.016); Individual spell overtuned (WR: 75.4%, Casts: 4436, mult: 0.900) |
| `LLD` | Light | Ultimate | 18.1 -> **13.8** (-23.8%) | 12.0 -> **16.4** | 235.3 -> **240.1** | Class Light undertuned (WR: 46.1%, factor: 1.016); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 782). Increasing spread: b -18.0%, n +37.0% |
| `DDF` | Dark | Conditional Strike | 11.8 -> **9.9** (-16.1%) | 7.5 -> **10.3** | 100.3 -> **111.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3204). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 44.4%, Casts: 3204, mult: 1.019) |
| `DDW` | Dark | Debuff / Control | 47.6 -> **46.8** (-1.7%) | - | 47.6 -> **46.8** | Individual spell overtuned (WR: 55.2%, Casts: 3689, mult: 0.983) |
| `DDE` | Dark | Setup - Weather | 24.9 -> **29.1** (+16.9%) | - | 24.9 -> **29.1** | Weather 'Darkness' appliers undertuned (WR: 28.1%, casts: 3564); Individual spell undertuned (WR: 28.1%, Casts: 3564, mult: 1.085) |
| `DDL` | Dark | Debuff / Control | 23.6 -> **23.2** (-1.7%) | - | 23.6 -> **23.2** | Individual spell overtuned (WR: 55.2%, Casts: 649, mult: 0.983) |
| `DDD` | Dark | Debuff / Control | 28.7 -> **25.7** (-10.5%) | - | 28.7 -> **25.7** | Individual spell overtuned (WR: 76.4%, Casts: 3451, mult: 0.896) |
| `FWF` | Ghostfire | Debuff / Control | 34.0 -> **27.7** (-18.5%) | - | 34.0 -> **27.7** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Status 'Burning' appliers overtuned on own (WR: 69.2%) |
| `FWW` | Ghostfire | Debuff / Control | 14.4 -> **13.9** (-3.5%) | - | 14.4 -> **13.9** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Status 'Cursed' appliers overtuned on own (WR: 54.0%) |
| `FWE` | Ghostfire | Setup - Location | 25.5 -> **28.9** (+13.3%) | - | 25.5 -> **28.9** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Location 'Graveyard' appliers undertuned (WR: 29.7%, casts: 1075) |
| `FWL` | Ghostfire | Debuff / Control | 42.0 -> **40.6** (-3.3%) | - | 42.0 -> **40.6** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Status 'Cursed' appliers overtuned on own (WR: 54.0%) |
| `FWD` | Ghostfire | Ultimate | 16.0 -> **17.2** (+7.5%) | 11.9 -> **11.4** | 206.4 -> **213.3** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Location 'Graveyard' beneficiaries undertuned (WR: 46.2%) |
| `WFF` | Ghostfire | Conditional Strike | 11.9 -> **9.7** (-18.5%) | 7.1 -> **9.7** | 96.4 -> **103.8** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 3412). Increasing spread: b -17.9%, n +36.7% |
| `WFW` | Ghostfire | Debuff / Control | 28.6 -> **27.1** (-5.2%) | - | 28.6 -> **27.1** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 59.3%, Casts: 1699, mult: 0.967) |
| `WFE` | Ghostfire | Debuff / Control | 26.2 -> **20.0** (-23.7%) | - | 26.2 -> **20.0** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Status 'Bleeding' appliers overtuned on own (WR: 79.8%) |
| `WFL` | Ghostfire | Buff / Sustain | 35.1 -> **33.7** (-4.0%) | - | 35.1 -> **33.7** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 56.3%, Casts: 1047, mult: 0.979) |
| `WFD` | Ghostfire | Conditional Strike | 11.6 -> **10.0** (-13.8%) | 6.7 -> **9.1** | 89.3 -> **101.0** | Class Ghostfire overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 5133). Increasing spread: b -17.8%, n +36.5% |
| `FEW` | Beasts | Conditional Strike | 12.0 -> **10.7** (-10.8%) | 7.3 -> **10.4** | 99.6 -> **122.0** | Class Beasts undertuned (WR: 46.4%, factor: 1.014); Status 'Entangled' beneficiaries undertuned (WR: 40.5%) |
| `FEE` | Beasts | Buff / Sustain | 24.8 -> **24.5** (-1.2%) | - | 24.8 -> **24.5** | Class Beasts undertuned (WR: 46.4%, factor: 1.014); Individual spell overtuned (WR: 58.0%, Casts: 1968, mult: 0.972) |
| `FEL` | Beasts | Buff / Sustain | 24.7 -> **28.2** (+14.2%) | - | 24.7 -> **28.2** | Class Beasts undertuned (WR: 46.4%, factor: 1.014); Individual spell undertuned (WR: 18.3%, Casts: 3566, mult: 1.127) |
| `FED` | Beasts | Conditional Strike | 5.6 -> **5.8** (+3.6%) | 1.7 -> **1.6** | 15.1 -> **15.1** | Class Beasts undertuned (WR: 46.4%, factor: 1.014); Condition triggers within target window (33.3%), but combo payoff is warping win rate (54.6%). Compressing spread: b +3.0%, n -8.0% |
| `EFF` | Beasts | Debuff / Control | 13.6 -> **11.8** (-13.2%) | 7.2 -> **9.8** | 111.5 -> **127.4** | Class Beasts undertuned (WR: 46.4%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 2064). Increasing spread: b -17.8%, n +36.6% |
| `EFW` | Beasts | Buff / Sustain | 23.1 -> **25.2** (+9.1%) | - | 23.1 -> **25.2** | Class Beasts undertuned (WR: 46.4%, factor: 1.014); Individual spell undertuned (WR: 30.7%, Casts: 2496, mult: 1.074) |
| `EFE` | Beasts | Buff / Sustain | 31.8 -> **30.1** (-5.3%) | - | 31.8 -> **30.1** | Class Beasts undertuned (WR: 46.4%, factor: 1.014); Individual spell overtuned (WR: 67.7%, Casts: 925, mult: 0.933) |
| `EFL` | Beasts | Buff / Sustain | 17.1 -> **14.4** (-15.8%) | - | 17.1 -> **14.4** | Class Beasts undertuned (WR: 46.4%, factor: 1.014); Individual spell overtuned (WR: 91.8%, Casts: 2930, mult: 0.828) |
| `EFD` | Beasts | Ultimate | 11.9 -> **13.4** (+12.6%) | 18.5 -> **18.4** | 232.1 -> **260.0** | Class Beasts undertuned (WR: 46.4%, factor: 1.014); Status 'Entangled' beneficiaries undertuned (WR: 40.5%) |
| `FLF` | Lightning | Conditional Strike | 11.2 -> **9.0** (-19.6%) | 7.2 -> **10.1** | 91.8 -> **99.9** | Class Lightning overtuned (WR: 55.4%, factor: 0.978); Status 'Stunned' beneficiaries undertuned (WR: 42.8%) |
| `FLW` | Lightning | Debuff / Control | 43.3 -> **37.6** (-13.2%) | - | 43.3 -> **37.6** | Class Lightning overtuned (WR: 55.4%, factor: 0.978); Status 'Stunned' appliers overtuned on own (WR: 66.3%) |
| `FLE` | Lightning | Setup - Weather | 23.0 -> **22.5** (-2.2%) | - | 23.0 -> **22.5** | Class Lightning overtuned (WR: 55.4%, factor: 0.978) |
| `FLL` | Lightning | Buff / Sustain | 24.0 -> **24.9** (+3.7%) | - | 24.0 -> **24.9** | Class Lightning overtuned (WR: 55.4%, factor: 0.978); Individual spell undertuned (WR: 33.8%, Casts: 1349, mult: 1.061) |
| `FLD` | Lightning | Ultimate | 16.9 -> **18.5** (+9.5%) | 12.6 -> **12.7** | 229.8 -> **253.4** | Class Lightning overtuned (WR: 55.4%, factor: 0.978); Status 'Stunned' beneficiaries undertuned (WR: 42.8%) |
| `LFF` | Lightning | Conditional Strike | 12.2 -> **9.3** (-23.8%) | 7.2 -> **9.8** | 100.0 -> **100.4** | Class Lightning overtuned (WR: 55.4%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1382). Increasing spread: b -17.2%, n +35.4% |
| `LFW` | Lightning | Buff / Sustain | 32.9 -> **31.6** (-4.0%) | - | 32.9 -> **31.6** | Class Lightning overtuned (WR: 55.4%, factor: 0.978); Individual spell overtuned (WR: 55.6%, Casts: 2066, mult: 0.981) |
| `LFE` | Lightning | Debuff / Control | 42.7 -> **37.0** (-13.3%) | - | 42.7 -> **37.0** | Class Lightning overtuned (WR: 55.4%, factor: 0.978); Status 'Stunned' appliers overtuned on own (WR: 66.3%) |
| `LFL` | Lightning | Debuff / Control | 21.7 -> **17.7** (-18.4%) | 6.0 -> **8.0** | 151.9 -> **159.3** | Class Lightning overtuned (WR: 55.4%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.8% vs 30% floor, Casts: 1171). Increasing spread: b -16.5%, n +33.8% |
| `LFD` | Lightning | Conditional Strike | 14.0 -> **10.0** (-28.6%) | 10.5 -> **14.3** | 161.0 -> **153.0** | Class Lightning overtuned (WR: 55.4%, factor: 0.978); Status 'Stunned' appliers overtuned on own (WR: 66.3%) |
| `FDF` | Blood | Conditional Strike | 11.8 -> **10.0** (-15.3%) | 7.5 -> **10.3** | 100.3 -> **113.0** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1173). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 63.1 -> **66.2** (+4.9%) | - | 63.1 -> **66.2** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Individual spell undertuned (WR: 40.8%, Casts: 686, mult: 1.032) |
| `FDE` | Blood | Setup - Weather | 21.1 -> **24.3** (+15.2%) | - | 21.1 -> **24.3** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Individual spell undertuned (WR: 17.6%, Casts: 3029, mult: 1.130) |
| `FDL` | Blood | Debuff / Control | 27.3 -> **22.0** (-19.4%) | - | 27.3 -> **22.0** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Status 'Bleeding' appliers overtuned on own (WR: 79.8%) |
| `FDD` | Blood | Ultimate | 15.6 -> **17.1** (+9.6%) | 12.3 -> **11.6** | 207.5 -> **215.5** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 3196, WR: 47.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 12.6 -> **11.1** (-11.9%) | 6.9 -> **9.3** | 99.5 -> **114.3** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.1% vs 30% floor, Casts: 2768). Increasing spread: b -16.8%, n +34.4% |
| `DFW` | Blood | Debuff / Control | 19.2 -> **16.2** (-15.6%) | - | 19.2 -> **16.2** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Status 'Bleeding' appliers overtuned on own (WR: 79.8%) |
| `DFE` | Blood | Buff / Sustain | 42.1 -> **47.5** (+12.8%) | - | 42.1 -> **47.5** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Individual spell undertuned (WR: 22.4%, Casts: 2754, mult: 1.109) |
| `DFL` | Blood | Buff / Sustain | 29.7 -> **29.1** (-2.0%) | - | 29.7 -> **29.1** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Individual spell overtuned (WR: 60.5%, Casts: 1847, mult: 0.962) |
| `DFD` | Blood | Conditional Strike | 40.0 -> **45.4** (+13.5%) | 0.7 -> **0.5** | 68.0 -> **68.1** | Class Blood undertuned (WR: 45.8%, factor: 1.017); Condition triggers excessively (N=1 conditions, Trigger Rate: 88.5% vs 55% ceiling, WR: 65.9%). Compressing spread: b +18.8%, n -26.3% |
| `WEF` | Plants | Conditional Strike | 13.3 -> **10.6** (-20.3%) | 6.6 -> **9.1** | 101.1 -> **107.1** | Class Plants overtuned (WR: 58.0%, factor: 0.968); Location 'Jungle' beneficiaries undertuned (WR: 45.4%) |
| `WEW` | Plants | Debuff / Control | 37.7 -> **36.0** (-4.5%) | - | 37.7 -> **36.0** | Class Plants overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 54.3%, Casts: 518, mult: 0.986) |
| `WEL` | Plants | Debuff / Control | 40.1 -> **34.6** (-13.7%) | - | 40.1 -> **34.6** | Class Plants overtuned (WR: 58.0%, factor: 0.968); Status 'Entangled' appliers overtuned on own (WR: 65.4%) |
| `WED` | Plants | Conditional Strike | 15.2 -> **11.2** (-26.3%) | 7.5 -> **10.3** | 129.2 -> **126.6** | Class Plants overtuned (WR: 58.0%, factor: 0.968); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1269). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 13.9 -> **11.2** (-19.4%) | 5.9 -> **7.9** | 95.9 -> **99.7** | Class Plants overtuned (WR: 58.0%, factor: 0.968); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.2% vs 30% floor, Casts: 11493). Increasing spread: b -16.7%, n +34.3% |
| `EWW` | Plants | Debuff / Control | 22.3 -> **17.7** (-20.6%) | - | 22.3 -> **17.7** | Class Plants overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 93.4%, Casts: 3830, mult: 0.820) |
| `EWL` | Plants | Debuff / Control | 55.2 -> **51.1** (-7.4%) | - | 55.2 -> **51.1** | Class Plants overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 61.8%, Casts: 889, mult: 0.957) |
| `EWD` | Plants | Conditional Strike | 8.8 -> **5.8** (-34.1%) | 7.0 -> **9.9** | 70.4 -> **63.2** | Class Plants overtuned (WR: 58.0%, factor: 0.968); Status 'Bleeding' appliers overtuned on own (WR: 79.8%) |
| `WLF` | Fey | Conditional Strike | 12.4 -> **11.0** (-11.3%) | 6.5 -> **8.5** | 93.0 -> **104.5** | Class Fey undertuned (WR: 38.0%, factor: 1.048); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.1% vs 30% floor, Casts: 799). Increasing spread: b -15.1%, n +31.1% |
| `WLW` | Fey | Debuff / Control | 43.1 -> **41.4** (-3.9%) | - | 43.1 -> **41.4** | Class Fey undertuned (WR: 38.0%, factor: 1.048); Status 'Cursed' appliers overtuned on own (WR: 54.0%) |
| `WLE` | Fey | Setup - Location | 27.9 -> **34.2** (+22.6%) | - | 27.9 -> **34.2** | Class Fey undertuned (WR: 38.0%, factor: 1.048); Location 'Enchanted Forest' appliers undertuned (WR: 27.8%, casts: 1106) |
| `WLL` | Fey | Direct Damage | 59.7 -> **61.2** (+2.5%) | - | 59.7 -> **61.2** | Class Fey undertuned (WR: 38.0%, factor: 1.048); Individual spell overtuned (WR: 56.4%, Casts: 648, mult: 0.978) |
| `WLD` | Fey | Ultimate | 17.1 -> **19.9** (+16.4%) | 12.3 -> **11.9** | 227.4 -> **256.7** | Class Fey undertuned (WR: 38.0%, factor: 1.048); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.1%) |
| `LWF` | Fey | Debuff / Control | 23.1 -> **19.6** (-15.2%) | 6.2 -> **8.6** | 166.3 -> **188.2** | Class Fey undertuned (WR: 38.0%, factor: 1.048); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.1%) |
| `LWW` | Fey | Debuff / Control | 42.1 -> **47.2** (+12.1%) | - | 42.1 -> **47.2** | Class Fey undertuned (WR: 38.0%, factor: 1.048); Individual spell undertuned (WR: 31.8%, Casts: 4121, mult: 1.069) |
| `LWL` | Fey | Debuff / Control | 37.1 -> **42.6** (+14.8%) | - | 37.1 -> **42.6** | Class Fey undertuned (WR: 38.0%, factor: 1.048); Individual spell undertuned (WR: 25.6%, Casts: 4105, mult: 1.095) |
| `LWD` | Fey | Conditional Strike | 14.0 -> **12.6** (-10.0%) | 7.5 -> **10.3** | 119.0 -> **142.4** | Class Fey undertuned (WR: 38.0%, factor: 1.048); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3510). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 14.2 -> **11.4** (-19.7%) | 6.7 -> **9.0** | 109.3 -> **114.0** | Class Ice undertuned (WR: 44.0%, factor: 1.024); Status 'Stunned' appliers overtuned on own (WR: 66.3%) |
| `WDW` | Ice | Buff / Sustain | 14.9 -> **15.5** (+4.0%) | - | 14.9 -> **15.5** | Class Ice undertuned (WR: 44.0%, factor: 1.024); Individual spell undertuned (WR: 45.7%, Casts: 4437, mult: 1.014) |
| `WDE` | Ice | Setup - Weather | 24.5 -> **27.2** (+11.0%) | - | 24.5 -> **27.2** | Class Ice undertuned (WR: 44.0%, factor: 1.024); Individual spell undertuned (WR: 28.2%, Casts: 3973, mult: 1.084) |
| `WDL` | Ice | Debuff / Control | 43.6 -> **44.7** (+2.5%) | - | 43.6 -> **44.7** | Class Ice undertuned (WR: 44.0%, factor: 1.024) |
| `WDD` | Ice | Ultimate | 23.5 -> **27.3** (+16.2%) | 9.0 -> **9.4** | 235.0 -> **283.9** | Class Ice undertuned (WR: 44.0%, factor: 1.024); Weather 'Blizzard' beneficiaries undertuned (WR: 36.0%) |
| `DWW` | Ice | Debuff / Control | 34.7 -> **35.5** (+2.3%) | - | 34.7 -> **35.5** | Class Ice undertuned (WR: 44.0%, factor: 1.024) |
| `DWE` | Ice | Setup - Location | 21.9 -> **23.2** (+5.9%) | - | 21.9 -> **23.2** | Class Ice undertuned (WR: 44.0%, factor: 1.024); Location 'Tundra' appliers undertuned (WR: 44.9%, casts: 618) |
| `DWL` | Ice | Debuff / Control | 47.1 -> **48.2** (+2.3%) | - | 47.1 -> **48.2** | Class Ice undertuned (WR: 44.0%, factor: 1.024) |
| `DWD` | Ice | Conditional Strike | 16.4 -> **14.5** (-11.6%) | 5.4 -> **7.2** | 105.0 -> **118.9** | Class Ice undertuned (WR: 44.0%, factor: 1.024); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.9% vs 30% floor, Casts: 2510). Increasing spread: b -16.4%, n +33.8% |
| `ELF` | Wind | Conditional Strike | 27.0 -> **20.2** (-25.2%) | 7.0 -> **9.5** | 216.0 -> **212.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.0% vs 30% floor, Casts: 502). Increasing spread: b -17.2%, n +35.3%; Individual spell overtuned (WR: 74.3%, Casts: 502, mult: 0.905) |
| `ELE` | Wind | Setup - Weather | 20.3 -> **19.4** (-4.4%) | - | 20.3 -> **19.4** | Individual spell overtuned (WR: 62.7%, Casts: 792, mult: 0.954) |
| `ELL` | Wind | Buff / Sustain | 40.0 -> **42.0** (+5.0%) | - | 40.0 -> **42.0** | Individual spell undertuned (WR: 36.4%, Casts: 601, mult: 1.050) |
| `ELD` | Wind | Conditional Strike | 13.4 -> **11.1** (-17.2%) | 6.5 -> **8.8** | 100.5 -> **108.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.4% vs 30% floor, Casts: 1038). Increasing spread: b -17.5%, n +35.9% |
| `LEF` | Wind | Conditional Strike | 12.7 -> **10.8** (-15.0%) | 6.6 -> **9.0** | 96.5 -> **108.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 8088). Increasing spread: b -17.4%, n +35.7%; Individual spell undertuned (WR: 42.6%, Casts: 8088, mult: 1.026) |
| `LEW` | Wind | Debuff / Control | 55.9 -> **53.7** (-3.9%) | - | 55.9 -> **53.7** | Individual spell overtuned (WR: 61.0%, Casts: 5251, mult: 0.960) |
| `LEE` | Wind | Setup - Weather | 21.3 -> **21.1** (-0.9%) | - | 21.3 -> **21.1** | Individual spell overtuned (WR: 53.6%, Casts: 779, mult: 0.988) |
| `LEL` | Wind | Buff / Sustain | 40.0 -> **42.4** (+6.0%) | - | 40.0 -> **42.4** | Individual spell undertuned (WR: 34.2%, Casts: 1229, mult: 1.059) |
| `EDF` | Poison | Conditional Strike | 13.9 -> **11.4** (-18.0%) | 6.8 -> **9.3** | 108.4 -> **117.4** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.1% vs 30% floor, Casts: 5867). Increasing spread: b -17.6%, n +36.1% |
| `EDW` | Poison | Debuff / Control | 29.2 -> **26.1** (-10.6%) | - | 29.2 -> **26.1** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Individual spell overtuned (WR: 69.2%, Casts: 2355, mult: 0.927) |
| `EDE` | Poison | Setup - Location | 22.6 -> **21.2** (-6.2%) | - | 22.6 -> **21.2** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Location 'Swamp' appliers overtuned on own (WR: 53.9%) |
| `EDL` | Poison | Debuff / Control | 14.1 -> **11.1** (-21.3%) | - | 14.1 -> **11.1** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Individual spell overtuned (WR: 93.9%, Casts: 2345, mult: 0.820) |
| `EDD` | Poison | Ultimate | 25.1 -> **19.3** (-23.1%) | 10.3 -> **13.6** | 283.6 -> **281.8** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Location 'Swamp' beneficiaries overtuned (WR: 58.9%) |
| `DEF` | Poison | Conditional Strike | 31.9 -> **29.8** (-6.6%) | 2.2 -> **2.2** | 102.1 -> **95.4** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 45.5% within [30%-55%] target window, WR: 58.3%). |
| `DEW` | Poison | Debuff / Control | 30.1 -> **26.5** (-12.0%) | - | 30.1 -> **26.5** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Individual spell overtuned (WR: 72.0%, Casts: 1241, mult: 0.915) |
| `DEE` | Poison | Debuff / Control | 24.5 -> **22.8** (-6.9%) | - | 24.5 -> **22.8** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Individual spell overtuned (WR: 59.3%, Casts: 2618, mult: 0.967) |
| `DEL` | Poison | Conditional Strike | 1.5 -> **1.3** (-13.3%) | 7.0 -> **9.3** | 12.0 -> **13.4** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.3% vs 30% floor, Casts: 1033). Increasing spread: b -15.9%, n +32.6% |
| `DED` | Poison | Debuff / Control | 29.7 -> **26.9** (-9.4%) | - | 29.7 -> **26.9** | Class Poison overtuned (WR: 59.1%, factor: 0.963); Individual spell overtuned (WR: 65.9%, Casts: 2205, mult: 0.940) |
| `LDF` | Cosmic | Debuff / Control | 43.4 -> **41.4** (-4.6%) | - | 43.4 -> **41.4** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978); Individual spell overtuned (WR: 57.1%, Casts: 1311, mult: 0.975) |
| `LDW` | Cosmic | Debuff / Control | 46.9 -> **40.0** (-14.7%) | - | 46.9 -> **40.0** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978); Status 'Stunned' appliers overtuned on own (WR: 66.3%) |
| `LDE` | Cosmic | Setup - Location | 19.2 -> **18.8** (-2.1%) | - | 19.2 -> **18.8** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978) |
| `LDL` | Cosmic | Conditional Strike | 14.2 -> **11.7** (-17.6%) | 6.6 -> **8.9** | 107.9 -> **115.8** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 1692). Increasing spread: b -16.8%, n +34.5% |
| `LDD` | Cosmic | Ultimate | 13.0 -> **13.7** (+5.4%) | 18.6 -> **17.5** | 254.8 -> **253.4** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978); Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2388, WR: 47.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 16.4 -> **12.9** (-21.3%) | 6.8 -> **9.3** | 127.9 -> **132.9** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 3302). Increasing spread: b -17.8%, n +36.7% |
| `DLW` | Cosmic | Direct Damage | 58.0 -> **53.9** (-7.1%) | - | 58.0 -> **53.9** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978); Individual spell overtuned (WR: 63.5%, Casts: 1085, mult: 0.950) |
| `DLE` | Cosmic | Direct Damage | 39.7 -> **41.2** (+3.8%) | - | 39.7 -> **41.2** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978); Individual spell undertuned (WR: 33.7%, Casts: 1505, mult: 1.061) |
| `DLL` | Cosmic | Conditional Strike | 22.9 -> **17.7** (-22.7%) | 6.0 -> **8.1** | 160.3 -> **161.1** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 2684). Increasing spread: b -17.2%, n +35.4% |
| `DLD` | Cosmic | Conditional Strike | 50.9 -> **56.3** (+10.6%) | 1.5 -> **1.5** | 127.2 -> **140.8** | Class Cosmic overtuned (WR: 55.6%, factor: 0.978); Condition triggers excessively (N=1 conditions, Trigger Rate: 93.0% vs 55% ceiling, WR: 60.1%). Compressing spread: b +17.5%, n -25.6% |
