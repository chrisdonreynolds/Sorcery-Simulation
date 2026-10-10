# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T16:17:33Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 131.4s  
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
| **Fire** | 24,996 | 66.0% | 66.0% | 10.8 | Overtuned ⚠️ |
| **Dark** | 11,609 | 61.0% | 61.1% | 8.2 | Overtuned ⚠️ |
| **Earth** | 27,351 | 58.8% | 58.8% | 13.5 | Overtuned ⚠️ |
| **Poison** | 38,581 | 58.8% | 58.8% | 6.6 | Overtuned ⚠️ |
| **Ghostfire** | 17,787 | 55.7% | 55.7% | 3.7 | Overtuned ⚠️ |
| **Blood** | 20,754 | 55.2% | 55.2% | 4.5 | Overtuned ⚠️ |
| **Cosmic** | 40,131 | 52.3% | 52.3% | 10.4 | Balanced ✅ |
| **Lightning** | 22,851 | 50.8% | 50.8% | 6.6 | Balanced ✅ |
| **Light** | 14,765 | 50.1% | 50.1% | 6.6 | Balanced ✅ |
| **Water** | 17,408 | 48.5% | 48.5% | 8.4 | Balanced ✅ |
| **Ice** | 32,702 | 48.2% | 48.2% | 8.4 | Balanced ✅ |
| **Beasts** | 27,700 | 41.1% | 41.1% | 3.7 | Undertuned ⚠️ |
| **Fey** | 22,487 | 36.7% | 36.7% | 4.9 | Undertuned ⚠️ |
| **Plants** | 16,426 | 35.6% | 35.6% | 2.2 | Undertuned ⚠️ |
| **Wind** | 20,225 | 29.1% | 29.1% | 2.9 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 20,096 (48.0%) | 5,872 (26.3%) | 3.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 687 (31.0%) | 11,901 (34.5%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,567 (57.4%) | 8,116 (48.4%) | 3.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,944 (83.6%) | 14,789 (30.5%) | 1.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 21,200 (53.0%) | 5,077 (50.0%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 101 (49.6%) | 11,855 (33.4%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 3,941 (8.2%) | 3,051 (21.0%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 30.3 -> **27.3** (-9.9%) | - | 30.3 -> **27.3** | Class Fire overtuned (WR: 66.0%, factor: 0.936); Individual spell overtuned (WR: 60.5%, Casts: 3333, mult: 0.962) |
| `FFW` | Fire | Debuff / Control | 19.2 -> **17.5** (-8.9%) | - | 19.2 -> **17.5** | Class Fire overtuned (WR: 66.0%, factor: 0.936); Status 'Burning' appliers overtuned on own (WR: 57.4%) |
| `FFE` | Fire | Debuff / Control | 17.3 -> **14.6** (-15.6%) | - | 17.3 -> **14.6** | Class Fire overtuned (WR: 66.0%, factor: 0.936); Individual spell overtuned (WR: 75.4%, Casts: 13745, mult: 0.900) |
| `FFL` | Fire | Debuff / Control | 1.2 -> **1.0** (-16.7%) | - | 1.2 -> **1.0** | Class Fire overtuned (WR: 66.0%, factor: 0.936); Status 'Burning' appliers overtuned on own (WR: 57.4%) |
| `FFD` | Fire | Conditional Strike | 3.8 -> **3.0** (-21.1%) | 85.8 -> **116.5** | 329.8 -> **352.5** | Class Fire overtuned (WR: 66.0%, factor: 0.936); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 1843). Increasing spread: b -17.4%, n +35.8% |
| `WWF` | Water | Conditional Strike | 4.2 -> **3.5** (-16.7%) | 66.0 -> **88.2** | 281.4 -> **312.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.0% vs 30% floor, Casts: 5379). Increasing spread: b -16.4%, n +33.7% |
| `WWE` | Water | Setup - Weather | 94.5 -> **124.1** (+31.3%) | - | 94.5 -> **124.1** | Weather 'Raining' appliers undertuned (WR: 8.2%, casts: 3941); Individual spell undertuned (WR: 8.2%, Casts: 3941, mult: 1.172) |
| `WWL` | Water | Buff / Sustain | 47.2 -> **41.1** (-12.9%) | - | 47.2 -> **41.1** | Individual spell overtuned (WR: 82.4%, Casts: 5994, mult: 0.870) |
| `WWD` | Water | Buff / Sustain | 40.0 -> **46.3** (+15.7%) | - | 40.0 -> **46.3** | Individual spell undertuned (WR: 11.2%, Casts: 1619, mult: 1.159) |
| `EEF` | Earth | Conditional Strike | 4.5 -> **4.0** (-11.1%) | 90.5 -> **133.9** | 411.8 -> **539.6** | Class Earth overtuned (WR: 58.8%, factor: 0.965); Status 'Frosty' beneficiaries undertuned (WR: 26.3%) |
| `EEW` | Earth | Buff / Sustain | 50.0 -> **47.1** (-5.8%) | - | 50.0 -> **47.1** | Class Earth overtuned (WR: 58.8%, factor: 0.965); Individual spell overtuned (WR: 57.1%, Casts: 3331, mult: 0.975) |
| `EED` | Earth | Direct Damage | 3.3 -> **2.9** (-12.1%) | - | 3.3 -> **2.9** | Class Earth overtuned (WR: 58.8%, factor: 0.965); Individual spell overtuned (WR: 70.5%, Casts: 11483, mult: 0.921) |
| `LLF` | Light | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 78.5 -> **104.3** | 15.9 -> **21.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 1520). Increasing spread: b -16.0%, n +32.9%; Individual spell overtuned (WR: 63.4%, Casts: 1520, mult: 0.950) |
| `LLW` | Light | Debuff / Control | 22.8 -> **22.0** (-3.5%) | - | 22.8 -> **22.0** | Individual spell overtuned (WR: 60.2%, Casts: 4699, mult: 0.964) |
| `LLE` | Light | Setup - Weather | 146.8 -> **168.0** (+14.4%) | - | 146.8 -> **168.0** | Weather 'Sunny' appliers undertuned (WR: 31.0%, casts: 687); Individual spell undertuned (WR: 30.9%, Casts: 687, mult: 1.073) |
| `LLL` | Light | Buff / Sustain | 13.1 -> **12.9** (-1.5%) | - | 13.1 -> **12.9** | Individual spell overtuned (WR: 54.2%, Casts: 1387, mult: 0.986) |
| `LLD` | Light | Ultimate | 16.8 -> **18.7** (+11.3%) | 27.4 -> **27.4** | 477.1 -> **531.1** | Weather 'Sunny' beneficiaries undertuned (WR: 34.5%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 6472, WR: 40.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 2.3 -> **1.7** (-26.1%) | 93.2 -> **127.7** | 216.7 -> **218.8** | Class Dark overtuned (WR: 61.0%, factor: 0.956); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 310). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 32.7 -> **30.4** (-7.0%) | - | 32.7 -> **30.4** | Class Dark overtuned (WR: 61.0%, factor: 0.956); Individual spell overtuned (WR: 57.5%, Casts: 5496, mult: 0.974) |
| `DDE` | Dark | Setup - Weather | 70.9 -> **69.4** (-2.1%) | - | 70.9 -> **69.4** | Class Dark overtuned (WR: 61.0%, factor: 0.956); Weather 'Darkness' appliers undertuned (WR: 46.4%, casts: 665) |
| `DDL` | Dark | Debuff / Control | 17.0 -> **16.7** (-1.8%) | - | 17.0 -> **16.7** | Class Dark overtuned (WR: 61.0%, factor: 0.956); Individual spell undertuned (WR: 42.8%, Casts: 2044, mult: 1.025) |
| `DDD` | Dark | Debuff / Control | 9.5 -> **7.9** (-16.8%) | - | 9.5 -> **7.9** | Class Dark overtuned (WR: 61.0%, factor: 0.956); Individual spell overtuned (WR: 81.6%, Casts: 3094, mult: 0.873) |
| `FWF` | Ghostfire | Debuff / Control | 6.3 -> **4.9** (-22.2%) | - | 6.3 -> **4.9** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977); Status 'Burning' appliers overtuned on own (WR: 57.4%) |
| `FWW` | Ghostfire | Debuff / Control | 11.8 -> **11.4** (-3.4%) | - | 11.8 -> **11.4** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977); Status 'Cursed' appliers overtuned on own (WR: 59.9%) |
| `FWE` | Ghostfire | Setup - Location | 75.0 -> **73.7** (-1.7%) | - | 75.0 -> **73.7** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977); Location 'Graveyard' appliers undertuned (WR: 48.4%, casts: 17) |
| `FWL` | Ghostfire | Debuff / Control | 30.3 -> **29.5** (-2.6%) | - | 30.3 -> **29.5** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977); Status 'Cursed' appliers overtuned on own (WR: 59.9%) |
| `FWD` | Ghostfire | Ultimate | 17.1 -> **13.7** (-19.9%) | 21.6 -> **28.9** | 386.5 -> **409.6** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977); Status 'Cursed' beneficiaries overtuned (WR: 55.7%) |
| `WFF` | Ghostfire | Conditional Strike | 2.4 -> **2.1** (-12.5%) | 117.3 -> **173.1** | 283.9 -> **365.6** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977); Status 'Bleeding' beneficiaries undertuned (WR: 30.5%) |
| `WFW` | Ghostfire | Debuff / Control | 11.6 -> **10.2** (-12.1%) | - | 11.6 -> **10.2** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977); Individual spell overtuned (WR: 75.2%, Casts: 2735, mult: 0.901) |
| `WFE` | Ghostfire | Debuff / Control | 3.3 -> **2.5** (-24.2%) | - | 3.3 -> **2.5** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977); Status 'Bleeding' appliers overtuned on own (WR: 83.6%) |
| `WFL` | Ghostfire | Buff / Sustain | 43.7 -> **42.7** (-2.3%) | - | 43.7 -> **42.7** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977) |
| `WFD` | Ghostfire | Conditional Strike | 2.6 -> **2.2** (-15.4%) | 80.7 -> **110.5** | 212.4 -> **245.3** | Class Ghostfire overtuned (WR: 55.7%, factor: 0.977); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 2068). Increasing spread: b -18.0%, n +37.0% |
| `FEF` | Beasts | Debuff / Control | 16.0 -> **16.3** (+1.9%) | - | 16.0 -> **16.3** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell overtuned (WR: 54.3%, Casts: 5648, mult: 0.986) |
| `FEW` | Beasts | Conditional Strike | 3.7 -> **3.5** (-5.4%) | 119.7 -> **174.9** | 446.6 -> **615.6** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Status 'Entangled' beneficiaries undertuned (WR: 33.4%) |
| `FEE` | Beasts | Buff / Sustain | 34.3 -> **39.8** (+16.0%) | - | 34.3 -> **39.8** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell undertuned (WR: 20.1%, Casts: 2965, mult: 1.119) |
| `FEL` | Beasts | Buff / Sustain | 70.5 -> **83.6** (+18.6%) | - | 70.5 -> **83.6** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell undertuned (WR: 14.3%, Casts: 3887, mult: 1.145) |
| `EFF` | Beasts | Debuff / Control | 5.0 -> **4.0** (-20.0%) | 86.1 -> **115.0** | 435.5 -> **464.0** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.1% vs 30% floor, Casts: 957). Increasing spread: b -16.4%, n +33.6% |
| `EFW` | Beasts | Buff / Sustain | 36.7 -> **39.4** (+7.4%) | - | 36.7 -> **39.4** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell undertuned (WR: 40.0%, Casts: 278, mult: 1.036) |
| `EFE` | Beasts | Buff / Sustain | 27.9 -> **26.0** (-6.8%) | - | 27.9 -> **26.0** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell overtuned (WR: 75.6%, Casts: 925, mult: 0.900) |
| `EFL` | Beasts | Buff / Sustain | 4.4 -> **3.7** (-15.9%) | - | 4.4 -> **3.7** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Individual spell overtuned (WR: 95.9%, Casts: 2203, mult: 0.820) |
| `EFD` | Beasts | Ultimate | 14.0 -> **11.9** (-15.0%) | 63.4 -> **92.6** | 901.6 -> **1113.8** | Class Beasts undertuned (WR: 41.1%, factor: 1.036); Status 'Entangled' beneficiaries undertuned (WR: 33.4%) |
| `FLF` | Lightning | Conditional Strike | 3.3 -> **2.7** (-18.2%) | 106.8 -> **146.3** | 355.7 -> **397.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 935). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 54.6%, Casts: 935, mult: 0.985) |
| `FLW` | Lightning | Debuff / Control | 24.3 -> **22.2** (-8.6%) | - | 24.3 -> **22.2** | Individual spell overtuned (WR: 72.8%, Casts: 5960, mult: 0.912) |
| `FLE` | Lightning | Setup - Weather | 31.8 -> **33.5** (+5.3%) | - | 31.8 -> **33.5** | Weather 'Storming' appliers undertuned (WR: 42.4%, casts: 203); Individual spell undertuned (WR: 42.3%, Casts: 203, mult: 1.027) |
| `FLL` | Lightning | Buff / Sustain | 41.2 -> **38.8** (-5.8%) | - | 41.2 -> **38.8** | Individual spell overtuned (WR: 65.6%, Casts: 279, mult: 0.942) |
| `FLD` | Lightning | Ultimate | 20.5 -> **16.8** (-18.0%) | 23.2 -> **31.8** | 496.1 -> **551.0** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4142). Increasing spread: b -18.0%, n +37.0% |
| `LFF` | Lightning | Conditional Strike | 3.7 -> **3.2** (-13.5%) | 88.4 -> **121.1** | 330.8 -> **390.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1785). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 31.4%, Casts: 1785, mult: 1.071) |
| `LFW` | Lightning | Buff / Sustain | 23.4 -> **25.3** (+8.1%) | - | 23.4 -> **25.3** | Individual spell undertuned (WR: 28.5%, Casts: 2988, mult: 1.083) |
| `LFE` | Lightning | Debuff / Control | 19.1 -> **18.2** (-4.7%) | - | 19.1 -> **18.2** | Individual spell overtuned (WR: 62.9%, Casts: 2989, mult: 0.952) |
| `LFL` | Lightning | Debuff / Control | 5.2 -> **4.6** (-11.5%) | 70.1 -> **97.4** | 369.7 -> **452.6** | Weather 'Darkness' beneficiaries undertuned (WR: 45.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.0% vs 30% floor, Casts: 3502). Increasing spread: b -17.6%, n +36.2% |
| `LFD` | Lightning | Conditional Strike | 3.4 -> **2.7** (-20.6%) | 108.2 -> **145.6** | 371.3 -> **395.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.9% vs 30% floor, Casts: 68). Increasing spread: b -16.8%, n +34.6%; Individual spell overtuned (WR: 60.0%, Casts: 68, mult: 0.964) |
| `FDF` | Blood | Conditional Strike | 2.2 -> **2.0** (-9.1%) | 93.2 -> **127.7** | 207.2 -> **257.4** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3449). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 79.1 -> **79.4** (+0.4%) | - | 79.1 -> **79.4** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Individual spell undertuned (WR: 42.9%, Casts: 345, mult: 1.025) |
| `FDE` | Blood | Setup - Weather | 49.5 -> **54.8** (+10.7%) | - | 49.5 -> **54.8** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Individual spell undertuned (WR: 17.8%, Casts: 1574, mult: 1.129) |
| `FDL` | Blood | Debuff / Control | 3.2 -> **2.3** (-28.1%) | - | 3.2 -> **2.3** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Status 'Bleeding' appliers overtuned on own (WR: 83.6%) |
| `FDD` | Blood | Ultimate | 11.5 -> **9.1** (-20.9%) | 25.4 -> **35.5** | 303.6 -> **332.1** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Weather 'Darkness' beneficiaries undertuned (WR: 45.0%) |
| `DFF` | Blood | Conditional Strike | 3.7 -> **3.5** (-5.4%) | 100.3 -> **137.3** | 374.8 -> **484.1** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Status 'Bleeding' beneficiaries undertuned (WR: 30.5%) |
| `DFW` | Blood | Debuff / Control | 2.5 -> **1.8** (-28.0%) | - | 2.5 -> **1.8** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Status 'Bleeding' appliers overtuned on own (WR: 83.6%) |
| `DFE` | Blood | Buff / Sustain | 96.5 -> **109.5** (+13.5%) | - | 96.5 -> **109.5** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Individual spell undertuned (WR: 11.3%, Casts: 1486, mult: 1.158) |
| `DFL` | Blood | Buff / Sustain | 15.3 -> **13.8** (-9.8%) | - | 15.3 -> **13.8** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Individual spell overtuned (WR: 71.3%, Casts: 2458, mult: 0.918) |
| `DFD` | Blood | Conditional Strike | 75.7 -> **82.0** (+8.3%) | 0.1 -> **0.1** | 83.3 -> **90.2** | Class Blood overtuned (WR: 55.2%, factor: 0.979); Condition triggers excessively (N=1 conditions, Trigger Rate: 89.3% vs 55% ceiling, WR: 75.1%). Compressing spread: b +22.6%, n -30.2% |
| `WEF` | Plants | Conditional Strike | 3.4 -> **2.6** (-23.5%) | 105.6 -> **144.3** | 362.4 -> **377.8** | Class Plants undertuned (WR: 35.6%, factor: 1.058); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 257). Increasing spread: b -17.8%, n +36.7% |
| `WEW` | Plants | Debuff / Control | 37.6 -> **43.0** (+14.4%) | - | 37.6 -> **43.0** | Class Plants undertuned (WR: 35.6%, factor: 1.058); Individual spell undertuned (WR: 28.8%, Casts: 2294, mult: 1.082) |
| `WEE` | Plants | Setup - Location | 73.3 -> **88.6** (+20.9%) | - | 73.3 -> **88.6** | Class Plants undertuned (WR: 35.6%, factor: 1.058); Location 'Jungle' appliers undertuned (WR: 31.2%, casts: 419) |
| `WEL` | Plants | Debuff / Control | 27.2 -> **28.8** (+5.9%) | - | 27.2 -> **28.8** | Class Plants undertuned (WR: 35.6%, factor: 1.058) |
| `WED` | Plants | Conditional Strike | 17.0 -> **20.2** (+18.8%) | 9.8 -> **9.2** | 183.6 -> **206.0** | Class Plants undertuned (WR: 35.6%, factor: 1.058); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 3361, WR: 38.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 3.8 -> **3.6** (-5.3%) | 81.5 -> **118.1** | 313.5 -> **428.8** | Class Plants undertuned (WR: 35.6%, factor: 1.058); Weather 'Sunny' beneficiaries undertuned (WR: 34.5%) |
| `EWW` | Plants | Debuff / Control | 4.8 -> **4.2** (-12.5%) | - | 4.8 -> **4.2** | Class Plants undertuned (WR: 35.6%, factor: 1.058); Individual spell overtuned (WR: 90.7%, Casts: 1289, mult: 0.833) |
| `EWL` | Plants | Debuff / Control | 41.9 -> **40.3** (-3.8%) | - | 41.9 -> **40.3** | Class Plants undertuned (WR: 35.6%, factor: 1.058); Individual spell overtuned (WR: 73.4%, Casts: 356, mult: 0.909) |
| `EWD` | Plants | Conditional Strike | 1.1 -> **0.9** (-18.2%) | 117.2 -> **171.2** | 130.0 -> **155.0** | Class Plants undertuned (WR: 35.6%, factor: 1.058); Status 'Bleeding' appliers overtuned on own (WR: 83.6%) |
| `WLF` | Fey | Conditional Strike | 4.1 -> **3.2** (-22.0%) | 71.7 -> **92.9** | 298.1 -> **300.5** | Class Fey undertuned (WR: 36.7%, factor: 1.053); Status 'Cursed' beneficiaries overtuned (WR: 55.7%) |
| `WLW` | Fey | Debuff / Control | 31.6 -> **28.3** (-10.4%) | - | 31.6 -> **28.3** | Class Fey undertuned (WR: 36.7%, factor: 1.053); Status 'Cursed' appliers overtuned on own (WR: 59.9%) |
| `WLE` | Fey | Setup - Location | 110.7 -> **133.5** (+20.6%) | - | 110.7 -> **133.5** | Class Fey undertuned (WR: 36.7%, factor: 1.053); Location 'Enchanted Forest' appliers undertuned (WR: 30.9%, casts: 1108) |
| `WLL` | Fey | Direct Damage | 67.7 -> **82.0** (+21.1%) | - | 67.7 -> **82.0** | Class Fey undertuned (WR: 36.7%, factor: 1.053); Individual spell undertuned (WR: 13.2%, Casts: 56, mult: 1.150) |
| `WLD` | Fey | Ultimate | 20.4 -> **23.2** (+13.7%) | 28.9 -> **30.0** | 610.0 -> **719.2** | Class Fey undertuned (WR: 36.7%, factor: 1.053); Weather 'Darkness' beneficiaries undertuned (WR: 45.0%) |
| `LWF` | Fey | Debuff / Control | 7.4 -> **7.1** (-4.1%) | 78.1 -> **116.0** | 585.3 -> **830.7** | Class Fey undertuned (WR: 36.7%, factor: 1.053); Location 'Enchanted Forest' beneficiaries undertuned (WR: 28.9%) |
| `LWW` | Fey | Debuff / Control | 68.0 -> **58.7** (-13.7%) | - | 68.0 -> **58.7** | Class Fey undertuned (WR: 36.7%, factor: 1.053); Individual spell overtuned (WR: 94.0%, Casts: 121, mult: 0.820) |
| `LWL` | Fey | Debuff / Control | 85.1 -> **102.5** (+20.4%) | - | 85.1 -> **102.5** | Class Fey undertuned (WR: 36.7%, factor: 1.053); Individual spell undertuned (WR: 14.6%, Casts: 386, mult: 1.144) |
| `LWD` | Fey | Conditional Strike | 5.6 -> **5.3** (-5.4%) | 93.2 -> **127.7** | 527.5 -> **682.1** | Class Fey undertuned (WR: 36.7%, factor: 1.053); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5618). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 4.7 -> **4.3** (-8.5%) | 116.3 -> **177.6** | 551.3 -> **768.0** | Weather 'Raining' beneficiaries undertuned (WR: 21.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 2856). Increasing spread: b -17.9%, n +36.8% |
| `WDW` | Ice | Buff / Sustain | 26.4 -> **30.7** (+16.3%) | - | 26.4 -> **30.7** | Individual spell undertuned (WR: 10.4%, Casts: 5740, mult: 1.162) |
| `WDE` | Ice | Setup - Weather | 47.6 -> **46.6** (-2.1%) | - | 47.6 -> **46.6** | Individual spell overtuned (WR: 56.3%, Casts: 459, mult: 0.979) |
| `WDL` | Ice | Debuff / Control | 31.3 -> **28.6** (-8.6%) | - | 31.3 -> **28.6** | Individual spell overtuned (WR: 72.5%, Casts: 177, mult: 0.913) |
| `WDD` | Ice | Ultimate | 23.0 -> **17.3** (-24.8%) | 19.5 -> **22.5** | 471.5 -> **406.6** | Weather 'Blizzard' beneficiaries overtuned (WR: 70.8%); Location 'Tundra' beneficiaries overtuned (WR: 70.8%) |
| `DWF` | Ice | Debuff / Control | 26.7 -> **25.4** (-4.9%) | - | 26.7 -> **25.4** | Individual spell overtuned (WR: 63.0%, Casts: 9436, mult: 0.952) |
| `DWW` | Ice | Debuff / Control | 30.7 -> **29.0** (-5.5%) | - | 30.7 -> **29.0** | Individual spell overtuned (WR: 64.8%, Casts: 6117, mult: 0.945) |
| `DWE` | Ice | Setup - Location | 71.9 -> **85.6** (+19.1%) | - | 71.9 -> **85.6** | Location 'Tundra' appliers undertuned (WR: 25.4%, casts: 1436); Individual spell undertuned (WR: 25.4%, Casts: 1436, mult: 1.096) |
| `DWL` | Ice | Debuff / Control | 29.6 -> **28.2** (-4.7%) | - | 29.6 -> **28.2** | Individual spell overtuned (WR: 62.7%, Casts: 4743, mult: 0.953) |
| `DWD` | Ice | Conditional Strike | 6.6 -> **5.6** (-15.2%) | 82.4 -> **117.1** | 550.4 -> **661.4** | Status 'Frosty' beneficiaries undertuned (WR: 26.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 1409). Increasing spread: b -14.5%, n +29.8% |
| `ELF` | Wind | Conditional Strike | 7.9 -> **7.8** (-1.3%) | 108.5 -> **157.0** | 865.1 -> **1232.4** | Class Wind undertuned (WR: 29.1%, factor: 1.084); Status 'Bleeding' beneficiaries undertuned (WR: 30.5%) |
| `ELW` | Wind | Debuff / Control | 34.7 -> **35.5** (+2.3%) | - | 34.7 -> **35.5** | Class Wind undertuned (WR: 29.1%, factor: 1.084); Individual spell overtuned (WR: 65.1%, Casts: 951, mult: 0.944) |
| `ELE` | Wind | Setup - Weather | 44.4 -> **53.5** (+20.5%) | - | 44.4 -> **53.5** | Class Wind undertuned (WR: 29.1%, factor: 1.084); Individual spell undertuned (WR: 21.9%, Casts: 4304, mult: 1.112) |
| `ELL` | Wind | Buff / Sustain | 64.5 -> **78.1** (+21.1%) | - | 64.5 -> **78.1** | Class Wind undertuned (WR: 29.1%, factor: 1.084); Individual spell undertuned (WR: 20.5%, Casts: 845, mult: 1.117) |
| `ELD` | Wind | Conditional Strike | 5.8 -> **6.8** (+17.2%) | 105.5 -> **159.8** | 617.7 -> **1093.4** | Class Wind undertuned (WR: 29.1%, factor: 1.084); Weather 'Raining' beneficiaries undertuned (WR: 21.0%) |
| `LEF` | Wind | Conditional Strike | 4.5 -> **4.0** (-11.1%) | 88.7 -> **121.3** | 403.7 -> **489.2** | Class Wind undertuned (WR: 29.1%, factor: 1.084); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 894). Increasing spread: b -17.9%, n +36.7% |
| `LEW` | Wind | Debuff / Control | 39.1 -> **37.7** (-3.6%) | - | 39.1 -> **37.7** | Class Wind undertuned (WR: 29.1%, factor: 1.084); Individual spell overtuned (WR: 77.6%, Casts: 1049, mult: 0.891) |
| `LEE` | Wind | Setup - Weather | 44.9 -> **55.6** (+23.8%) | - | 44.9 -> **55.6** | Class Wind undertuned (WR: 29.1%, factor: 1.084); Individual spell undertuned (WR: 14.6%, Casts: 3354, mult: 1.143) |
| `LEL` | Wind | Buff / Sustain | 85.1 -> **83.5** (-1.9%) | - | 85.1 -> **83.5** | Class Wind undertuned (WR: 29.1%, factor: 1.084); Individual spell overtuned (WR: 74.3%, Casts: 552, mult: 0.905) |
| `EDF` | Poison | Conditional Strike | 2.9 -> **2.5** (-13.8%) | 72.3 -> **95.7** | 212.6 -> **241.8** | Class Poison overtuned (WR: 58.8%, factor: 0.965); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 1413). Increasing spread: b -15.8%, n +32.4% |
| `EDW` | Poison | Debuff / Control | 9.4 -> **7.7** (-18.1%) | - | 9.4 -> **7.7** | Class Poison overtuned (WR: 58.8%, factor: 0.965); Individual spell overtuned (WR: 86.1%, Casts: 12609, mult: 0.853) |
| `EDE` | Poison | Setup - Location | 54.6 -> **69.6** (+27.5%) | - | 54.6 -> **69.6** | Class Poison overtuned (WR: 58.8%, factor: 0.965); Location 'Swamp' appliers undertuned (WR: 4.2%, casts: 3438) |
| `EDL` | Poison | Debuff / Control | 2.3 -> **1.8** (-21.7%) | - | 2.3 -> **1.8** | Class Poison overtuned (WR: 58.8%, factor: 0.965); Individual spell overtuned (WR: 92.0%, Casts: 2518, mult: 0.827) |
| `EDD` | Poison | Ultimate | 17.4 -> **18.6** (+6.9%) | 29.4 -> **30.7** | 529.0 -> **589.6** | Class Poison overtuned (WR: 58.8%, factor: 0.965); Status 'Bleeding' beneficiaries undertuned (WR: 30.5%) |
| `DEF` | Poison | Conditional Strike | 11.2 -> **11.7** (+4.5%) | 5.9 -> **3.9** | 77.3 -> **57.3** | Class Poison overtuned (WR: 58.8%, factor: 0.965); Condition triggers excessively (N=1 conditions, Trigger Rate: 86.8% vs 55% ceiling, WR: 85.9%). Compressing spread: b +26.4%, n -33.7% |
| `DEW` | Poison | Debuff / Control | 8.3 -> **7.5** (-9.6%) | - | 8.3 -> **7.5** | Class Poison overtuned (WR: 58.8%, factor: 0.965); Individual spell overtuned (WR: 65.4%, Casts: 1369, mult: 0.943) |
| `DEE` | Poison | Debuff / Control | 18.6 -> **17.6** (-5.4%) | - | 18.6 -> **17.6** | Class Poison overtuned (WR: 58.8%, factor: 0.965); Individual spell overtuned (WR: 55.3%, Casts: 2556, mult: 0.982) |
| `DEL` | Poison | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 107.3 -> **158.0** | 43.3 -> **63.6** | Class Poison overtuned (WR: 58.8%, factor: 0.965); Status 'Bleeding' beneficiaries undertuned (WR: 30.5%) |
| `DED` | Poison | Debuff / Control | 20.2 -> **19.5** (-3.5%) | - | 20.2 -> **19.5** | Class Poison overtuned (WR: 58.8%, factor: 0.965) |
| `LDF` | Cosmic | Debuff / Control | 30.6 -> **28.9** (-5.6%) | - | 30.6 -> **28.9** | Individual spell overtuned (WR: 64.8%, Casts: 5758, mult: 0.945) |
| `LDW` | Cosmic | Debuff / Control | 20.6 -> **18.9** (-8.3%) | - | 20.6 -> **18.9** | Individual spell overtuned (WR: 71.8%, Casts: 4864, mult: 0.916) |
| `LDE` | Cosmic | Setup - Location | 23.4 -> **26.5** (+13.2%) | - | 23.4 -> **26.5** | Individual spell undertuned (WR: 17.4%, Casts: 575, mult: 1.131) |
| `LDL` | Cosmic | Conditional Strike | 4.3 -> **3.9** (-9.3%) | 79.0 -> **108.2** | 344.0 -> **425.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6976). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 21.9%, Casts: 6976, mult: 1.112) |
| `LDD` | Cosmic | Ultimate | 12.1 -> **9.8** (-19.0%) | 35.2 -> **48.2** | 438.0 -> **482.2** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 6512). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 54.4%, Casts: 6512, mult: 0.986) |
| `DLF` | Cosmic | Conditional Strike | 4.6 -> **4.3** (-6.5%) | 70.6 -> **96.6** | 329.4 -> **419.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1545). Increasing spread: b -17.9%, n +36.9%; Individual spell undertuned (WR: 15.7%, Casts: 1545, mult: 1.139) |
| `DLW` | Cosmic | Direct Damage | 32.0 -> **29.8** (-6.9%) | - | 32.0 -> **29.8** | Individual spell overtuned (WR: 68.2%, Casts: 8186, mult: 0.931) |
| `DLE` | Cosmic | Direct Damage | 74.2 -> **85.7** (+15.5%) | - | 74.2 -> **85.7** | Individual spell undertuned (WR: 12.0%, Casts: 2755, mult: 1.155) |
| `DLL` | Cosmic | Conditional Strike | 5.6 -> **4.7** (-16.1%) | 78.2 -> **108.2** | 443.5 -> **513.2** | Weather 'Darkness' beneficiaries undertuned (WR: 45.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 62). Increasing spread: b -17.4%, n +35.7% |
