# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T15:16:58Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 98.0s  
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
| **Blood** | 15,372 | 64.5% | 64.5% | 10.9 | Overtuned ⚠️ |
| **Poison** | 24,272 | 62.0% | 62.0% | 6.7 | Overtuned ⚠️ |
| **Earth** | 21,088 | 61.9% | 61.9% | 21.7 | Overtuned ⚠️ |
| **Fire** | 7,903 | 60.8% | 60.8% | 10.7 | Overtuned ⚠️ |
| **Lightning** | 22,233 | 57.6% | 57.6% | 8.4 | Overtuned ⚠️ |
| **Ghostfire** | 33,361 | 54.6% | 54.6% | 6.6 | Overtuned ⚠️ |
| **Plants** | 18,365 | 53.5% | 53.5% | 3.2 | Overtuned ⚠️ |
| **Light** | 9,861 | 50.8% | 50.8% | 3.0 | Balanced ✅ |
| **Ice** | 33,819 | 49.4% | 49.4% | 12.5 | Balanced ✅ |
| **Cosmic** | 26,817 | 48.5% | 48.5% | 14.7 | Balanced ✅ |
| **Dark** | 12,246 | 44.9% | 44.9% | 9.7 | Undertuned ⚠️ |
| **Water** | 10,403 | 42.1% | 42.1% | 2.5 | Undertuned ⚠️ |
| **Beasts** | 30,047 | 40.9% | 40.9% | 3.5 | Undertuned ⚠️ |
| **Fey** | 24,912 | 37.0% | 37.0% | 6.2 | Undertuned ⚠️ |
| **Wind** | 19,024 | 33.7% | 33.6% | 5.9 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 18,803 (53.4%) | 6,222 (29.8%) | 5.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,115 (4.8%) | 9,568 (47.3%) | 1.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 8,376 (76.0%) | 6,920 (48.2%) | 5.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,572 (76.9%) | 5,525 (41.3%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 17,315 (55.4%) | 2,690 (46.4%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,949 (46.6%) | 6,885 (44.6%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,191 (18.0%) | 1,988 (24.6%) | 1.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 44.4 -> **42.5** (-4.3%) | - | 44.4 -> **42.5** | Class Fire overtuned (WR: 60.8%, factor: 0.957) |
| `FFW` | Fire | Debuff / Control | 26.7 -> **23.6** (-11.6%) | - | 26.7 -> **23.6** | Class Fire overtuned (WR: 60.8%, factor: 0.957); Status 'Burning' appliers overtuned on own (WR: 76.0%) |
| `FFE` | Fire | Debuff / Control | 26.8 -> **25.0** (-6.7%) | - | 26.8 -> **25.0** | Class Fire overtuned (WR: 60.8%, factor: 0.957); Individual spell overtuned (WR: 57.7%, Casts: 1724, mult: 0.973) |
| `FFL` | Fire | Debuff / Control | 3.0 -> **2.4** (-20.0%) | - | 3.0 -> **2.4** | Class Fire overtuned (WR: 60.8%, factor: 0.957); Status 'Burning' appliers overtuned on own (WR: 76.0%) |
| `FFD` | Fire | Conditional Strike | 6.8 -> **5.4** (-20.6%) | 21.7 -> **29.5** | 154.4 -> **164.7** | Class Fire overtuned (WR: 60.8%, factor: 0.957); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.4% vs 30% floor, Casts: 288). Increasing spread: b -17.4%, n +35.8% |
| `WWF` | Water | Conditional Strike | 6.3 -> **5.5** (-12.7%) | 17.9 -> **23.3** | 119.1 -> **133.7** | Class Water undertuned (WR: 42.1%, factor: 1.032); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 4690). Increasing spread: b -14.8%, n +30.3% |
| `WWE` | Water | Setup - Weather | 27.9 -> **36.1** (+29.4%) | - | 27.9 -> **36.1** | Class Water undertuned (WR: 42.1%, factor: 1.032); Weather 'Raining' appliers undertuned (WR: 18.0%, casts: 2191) |
| `WWL` | Water | Buff / Sustain | 46.7 -> **43.7** (-6.4%) | - | 46.7 -> **43.7** | Class Water undertuned (WR: 42.1%, factor: 1.032); Individual spell overtuned (WR: 73.9%, Casts: 574, mult: 0.907) |
| `WWD` | Water | Buff / Sustain | 32.7 -> **36.1** (+10.4%) | - | 32.7 -> **36.1** | Class Water undertuned (WR: 42.1%, factor: 1.032); Individual spell undertuned (WR: 31.3%, Casts: 512, mult: 1.071) |
| `EEF` | Earth | Conditional Strike | 8.0 -> **6.8** (-15.0%) | 22.7 -> **32.9** | 189.6 -> **230.5** | Class Earth overtuned (WR: 61.9%, factor: 0.952); Status 'Frosty' beneficiaries undertuned (WR: 29.8%) |
| `EEW` | Earth | Buff / Sustain | 56.9 -> **50.6** (-11.1%) | - | 56.9 -> **50.6** | Class Earth overtuned (WR: 61.9%, factor: 0.952); Individual spell overtuned (WR: 67.7%, Casts: 3153, mult: 0.933) |
| `EED` | Earth | Direct Damage | 4.9 -> **4.4** (-10.2%) | - | 4.9 -> **4.4** | Class Earth overtuned (WR: 61.9%, factor: 0.952); Individual spell overtuned (WR: 63.0%, Casts: 8623, mult: 0.952) |
| `LLF` | Light | Conditional Strike | 0.8 -> **0.6** (-25.0%) | 23.7 -> **32.3** | 19.8 -> **20.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 3195). Increasing spread: b -17.7%, n +36.4%; Individual spell overtuned (WR: 67.0%, Casts: 3195, mult: 0.936) |
| `LLW` | Light | Debuff / Control | 23.1 -> **22.6** (-2.2%) | - | 23.1 -> **22.6** | Individual spell overtuned (WR: 56.2%, Casts: 2414, mult: 0.979) |
| `LLE` | Light | Setup - Weather | 49.5 -> **65.4** (+32.1%) | - | 49.5 -> **65.4** | Weather 'Sunny' appliers undertuned (WR: 4.8%, casts: 2115); Individual spell undertuned (WR: 4.8%, Casts: 2115, mult: 1.180) |
| `LLL` | Light | Buff / Sustain | 19.8 -> **17.8** (-10.1%) | - | 19.8 -> **17.8** | Individual spell overtuned (WR: 76.2%, Casts: 1751, mult: 0.897) |
| `LLD` | Light | Ultimate | 13.3 -> **16.1** (+21.1%) | 20.5 -> **19.3** | 285.9 -> **326.8** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 386, WR: 20.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 20.3%, Casts: 386, mult: 1.118) |
| `DDF` | Dark | Conditional Strike | 5.5 -> **4.6** (-16.4%) | 26.4 -> **36.2** | 150.7 -> **171.1** | Class Dark undertuned (WR: 44.9%, factor: 1.020); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1475). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 41.4 -> **42.2** (+1.9%) | - | 41.4 -> **42.2** | Class Dark undertuned (WR: 44.9%, factor: 1.020) |
| `DDE` | Dark | Setup - Weather | 41.7 -> **56.0** (+34.3%) | - | 41.7 -> **56.0** | Class Dark undertuned (WR: 44.9%, factor: 1.020); Weather 'Darkness' appliers undertuned (WR: 7.6%, casts: 2122) |
| `DDL` | Dark | Debuff / Control | 18.9 -> **19.3** (+2.1%) | - | 18.9 -> **19.3** | Class Dark undertuned (WR: 44.9%, factor: 1.020) |
| `DDD` | Dark | Debuff / Control | 16.3 -> **15.5** (-4.9%) | - | 16.3 -> **15.5** | Class Dark undertuned (WR: 44.9%, factor: 1.020); Individual spell overtuned (WR: 67.9%, Casts: 785, mult: 0.932) |
| `FWF` | Ghostfire | Debuff / Control | 14.8 -> **11.6** (-21.6%) | - | 14.8 -> **11.6** | Class Ghostfire overtuned (WR: 54.6%, factor: 0.982); Status 'Burning' appliers overtuned on own (WR: 76.0%) |
| `FWE` | Ghostfire | Setup - Location | 46.0 -> **54.0** (+17.4%) | - | 46.0 -> **54.0** | Class Ghostfire overtuned (WR: 54.6%, factor: 0.982); Location 'Graveyard' appliers undertuned (WR: 24.8%, casts: 2009) |
| `FWL` | Ghostfire | Debuff / Control | 31.8 -> **31.2** (-1.9%) | - | 31.8 -> **31.2** | Class Ghostfire overtuned (WR: 54.6%, factor: 0.982) |
| `FWD` | Ghostfire | Ultimate | 11.5 -> **12.6** (+9.6%) | 20.4 -> **20.6** | 246.1 -> **272.2** | Class Ghostfire overtuned (WR: 54.6%, factor: 0.982); Status 'Cursed' beneficiaries undertuned (WR: 41.3%) |
| `WFF` | Ghostfire | Conditional Strike | 6.4 -> **5.0** (-21.9%) | 28.6 -> **40.5** | 189.4 -> **207.5** | Class Ghostfire overtuned (WR: 54.6%, factor: 0.982); Status 'Bleeding' beneficiaries undertuned (WR: 41.3%) |
| `WFW` | Ghostfire | Debuff / Control | 21.1 -> **17.4** (-17.5%) | - | 21.1 -> **17.4** | Class Ghostfire overtuned (WR: 54.6%, factor: 0.982); Individual spell overtuned (WR: 88.6%, Casts: 4082, mult: 0.842) |
| `WFE` | Ghostfire | Debuff / Control | 9.8 -> **7.7** (-21.4%) | - | 9.8 -> **7.7** | Class Ghostfire overtuned (WR: 54.6%, factor: 0.982); Status 'Bleeding' appliers overtuned on own (WR: 76.9%) |
| `WFL` | Ghostfire | Buff / Sustain | 34.3 -> **38.7** (+12.8%) | - | 34.3 -> **38.7** | Class Ghostfire overtuned (WR: 54.6%, factor: 0.982); Individual spell undertuned (WR: 13.2%, Casts: 3588, mult: 1.150) |
| `WFD` | Ghostfire | Conditional Strike | 6.1 -> **4.7** (-23.0%) | 23.0 -> **31.5** | 146.4 -> **152.8** | Class Ghostfire overtuned (WR: 54.6%, factor: 0.982); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1797). Increasing spread: b -18.0%, n +37.0% |
| `FEF` | Beasts | Debuff / Control | 19.8 -> **20.1** (+1.5%) | - | 19.8 -> **20.1** | Class Beasts undertuned (WR: 40.9%, factor: 1.037); Individual spell overtuned (WR: 55.5%, Casts: 2798, mult: 0.981) |
| `FEW` | Beasts | Conditional Strike | 6.2 -> **5.3** (-14.5%) | 28.0 -> **39.2** | 179.8 -> **213.1** | Class Beasts undertuned (WR: 40.9%, factor: 1.037); Status 'Entangled' beneficiaries undertuned (WR: 44.6%) |
| `FEE` | Beasts | Buff / Sustain | 27.6 -> **28.3** (+2.5%) | - | 27.6 -> **28.3** | Class Beasts undertuned (WR: 40.9%, factor: 1.037); Individual spell overtuned (WR: 53.7%, Casts: 2142, mult: 0.988) |
| `FEL` | Beasts | Buff / Sustain | 45.1 -> **54.1** (+20.0%) | - | 45.1 -> **54.1** | Class Beasts undertuned (WR: 40.9%, factor: 1.037); Individual spell undertuned (WR: 11.5%, Casts: 7821, mult: 1.157) |
| `FED` | Beasts | Conditional Strike | 4.5 -> **4.6** (+2.2%) | 3.2 -> **3.5** | 18.9 -> **20.7** | Class Beasts undertuned (WR: 40.9%, factor: 1.037); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 20.1% vs 30% floor, Casts: 4773). Increasing spread: b -10.0%, n +20.2% |
| `EFF` | Beasts | Debuff / Control | 8.4 -> **8.1** (-3.6%) | 25.2 -> **34.5** | 220.1 -> **287.6** | Class Beasts undertuned (WR: 40.9%, factor: 1.037); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 389). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 27.0 -> **28.0** (+3.7%) | - | 27.0 -> **28.0** | Class Beasts undertuned (WR: 40.9%, factor: 1.037) |
| `EFE` | Beasts | Buff / Sustain | 27.7 -> **28.7** (+3.6%) | - | 27.7 -> **28.7** | Class Beasts undertuned (WR: 40.9%, factor: 1.037) |
| `EFL` | Beasts | Buff / Sustain | 9.0 -> **7.6** (-15.6%) | - | 9.0 -> **7.6** | Class Beasts undertuned (WR: 40.9%, factor: 1.037); Individual spell overtuned (WR: 93.9%, Casts: 3484, mult: 0.820) |
| `EFD` | Beasts | Ultimate | 10.8 -> **12.6** (+16.7%) | 39.8 -> **40.4** | 440.6 -> **521.6** | Class Beasts undertuned (WR: 40.9%, factor: 1.037); Status 'Entangled' beneficiaries undertuned (WR: 44.6%) |
| `FLF` | Lightning | Conditional Strike | 6.1 -> **4.8** (-21.3%) | 28.2 -> **39.2** | 178.1 -> **193.0** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Status 'Stunned' beneficiaries undertuned (WR: 46.4%) |
| `FLW` | Lightning | Debuff / Control | 30.4 -> **26.8** (-11.8%) | - | 30.4 -> **26.8** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Status 'Stunned' appliers overtuned on own (WR: 55.4%) |
| `FLE` | Lightning | Setup - Weather | 25.3 -> **27.2** (+7.5%) | - | 25.3 -> **27.2** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Weather 'Storming' appliers undertuned (WR: 35.1%, casts: 576) |
| `FLL` | Lightning | Buff / Sustain | 33.4 -> **34.2** (+2.4%) | - | 33.4 -> **34.2** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Individual spell undertuned (WR: 35.0%, Casts: 999, mult: 1.056) |
| `FLD` | Lightning | Ultimate | 18.3 -> **19.5** (+6.6%) | 17.1 -> **16.6** | 331.2 -> **343.2** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Status 'Stunned' beneficiaries undertuned (WR: 46.4%) |
| `LFF` | Lightning | Conditional Strike | 6.6 -> **5.7** (-13.6%) | 25.2 -> **34.4** | 172.9 -> **201.8** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 1511). Increasing spread: b -17.8%, n +36.7% |
| `LFW` | Lightning | Buff / Sustain | 28.0 -> **25.8** (-7.9%) | - | 28.0 -> **25.8** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Individual spell overtuned (WR: 63.1%, Casts: 2782, mult: 0.952) |
| `LFE` | Lightning | Debuff / Control | 28.0 -> **24.9** (-11.1%) | - | 28.0 -> **24.9** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Status 'Stunned' appliers overtuned on own (WR: 55.4%) |
| `LFL` | Lightning | Debuff / Control | 11.0 -> **8.6** (-21.8%) | 19.2 -> **25.9** | 222.2 -> **231.3** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.4% vs 30% floor, Casts: 2670). Increasing spread: b -17.0%, n +35.0% |
| `LFD` | Lightning | Conditional Strike | 6.6 -> **5.2** (-21.2%) | 32.2 -> **44.0** | 219.1 -> **234.0** | Class Lightning overtuned (WR: 57.6%, factor: 0.969); Status 'Stunned' appliers overtuned on own (WR: 55.4%) |
| `FDF` | Blood | Conditional Strike | 5.5 -> **4.2** (-23.6%) | 26.4 -> **36.2** | 150.7 -> **156.2** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 356). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 75.0 -> **74.5** (-0.7%) | - | 75.0 -> **74.5** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Individual spell undertuned (WR: 32.6%, Casts: 34, mult: 1.054) |
| `FDE` | Blood | Setup - Weather | 36.2 -> **37.3** (+3.0%) | - | 36.2 -> **37.3** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Individual spell undertuned (WR: 25.7%, Casts: 1916, mult: 1.095) |
| `FDL` | Blood | Debuff / Control | 10.3 -> **7.5** (-27.2%) | - | 10.3 -> **7.5** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Status 'Bleeding' appliers overtuned on own (WR: 76.9%) |
| `FDD` | Blood | Ultimate | 17.5 -> **12.2** (-30.3%) | 14.3 -> **19.6** | 267.8 -> **251.3** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1520). Increasing spread: b -17.9%, n +36.9% |
| `DFF` | Blood | Conditional Strike | 6.8 -> **5.6** (-17.6%) | 26.2 -> **36.9** | 185.0 -> **212.2** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Status 'Bleeding' beneficiaries undertuned (WR: 41.3%) |
| `DFW` | Blood | Debuff / Control | 8.0 -> **5.9** (-26.2%) | - | 8.0 -> **5.9** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Status 'Bleeding' appliers overtuned on own (WR: 76.9%) |
| `DFE` | Blood | Buff / Sustain | 71.2 -> **77.2** (+8.4%) | - | 71.2 -> **77.2** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Individual spell undertuned (WR: 13.1%, Casts: 469, mult: 1.150) |
| `DFL` | Blood | Buff / Sustain | 22.8 -> **20.9** (-8.3%) | - | 22.8 -> **20.9** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Individual spell overtuned (WR: 58.0%, Casts: 3591, mult: 0.972) |
| `DFD` | Blood | Conditional Strike | 59.5 -> **62.1** (+4.4%) | 0.2 -> **0.1** | 71.4 -> **68.3** | Class Blood overtuned (WR: 64.5%, factor: 0.942); Condition triggers excessively (N=1 conditions, Trigger Rate: 86.9% vs 55% ceiling, WR: 71.1%). Compressing spread: b +20.5%, n -27.8% |
| `WEF` | Plants | Conditional Strike | 6.4 -> **5.7** (-10.9%) | 26.5 -> **38.4** | 176.0 -> **224.6** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Location 'Jungle' beneficiaries undertuned (WR: 35.8%) |
| `WEW` | Plants | Debuff / Control | 34.6 -> **33.2** (-4.0%) | - | 34.6 -> **33.2** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Individual spell overtuned (WR: 58.0%, Casts: 131, mult: 0.972) |
| `WEE` | Plants | Setup - Location | 42.2 -> **45.3** (+7.3%) | - | 42.2 -> **45.3** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Location 'Jungle' appliers undertuned (WR: 38.0%, casts: 252) |
| `WEL` | Plants | Debuff / Control | 31.7 -> **31.3** (-1.3%) | - | 31.7 -> **31.3** | Class Plants overtuned (WR: 53.5%, factor: 0.986) |
| `WED` | Plants | Conditional Strike | 14.6 -> **11.6** (-20.5%) | 8.6 -> **11.8** | 140.2 -> **148.5** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1255). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 6.4 -> **5.2** (-18.8%) | 20.3 -> **27.6** | 136.3 -> **148.7** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.4% vs 30% floor, Casts: 9182). Increasing spread: b -17.4%, n +35.8% |
| `EWW` | Plants | Debuff / Control | 9.8 -> **8.0** (-18.4%) | - | 9.8 -> **8.0** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Individual spell overtuned (WR: 91.7%, Casts: 2818, mult: 0.828) |
| `EWL` | Plants | Debuff / Control | 44.8 -> **46.6** (+4.0%) | - | 44.8 -> **46.6** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Individual spell undertuned (WR: 35.0%, Casts: 385, mult: 1.056) |
| `EWD` | Plants | Conditional Strike | 2.7 -> **2.1** (-22.2%) | 27.5 -> **38.5** | 77.0 -> **83.0** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Status 'Bleeding' appliers overtuned on own (WR: 76.9%) |
| `WLF` | Fey | Conditional Strike | 7.9 -> **6.8** (-13.9%) | 22.3 -> **31.5** | 184.1 -> **221.0** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Status 'Cursed' beneficiaries undertuned (WR: 41.3%) |
| `WLW` | Fey | Debuff / Control | 32.5 -> **34.2** (+5.2%) | - | 32.5 -> **34.2** | Class Fey undertuned (WR: 37.0%, factor: 1.052) |
| `WLE` | Fey | Setup - Location | 78.3 -> **99.9** (+27.6%) | - | 78.3 -> **99.9** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Location 'Enchanted Forest' appliers undertuned (WR: 22.8%, casts: 5883) |
| `WLL` | Fey | Direct Damage | 54.5 -> **56.6** (+3.9%) | - | 54.5 -> **56.6** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Individual spell overtuned (WR: 54.1%, Casts: 927, mult: 0.987) |
| `WLD` | Fey | Ultimate | 21.7 -> **24.7** (+13.8%) | 15.8 -> **14.9** | 364.6 -> **392.7** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 7393, WR: 47.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `LWF` | Fey | Debuff / Control | 13.4 -> **11.4** (-14.9%) | 23.0 -> **31.3** | 321.6 -> **368.2** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.3% vs 30% floor, Casts: 630). Increasing spread: b -17.5%, n +35.9% |
| `LWW` | Fey | Debuff / Control | 57.1 -> **67.4** (+18.0%) | - | 57.1 -> **67.4** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Individual spell undertuned (WR: 19.6%, Casts: 1139, mult: 1.121) |
| `LWL` | Fey | Debuff / Control | 45.6 -> **48.0** (+5.3%) | - | 45.6 -> **48.0** | Class Fey undertuned (WR: 37.0%, factor: 1.052) |
| `LWD` | Fey | Conditional Strike | 8.4 -> **7.7** (-8.3%) | 26.4 -> **36.2** | 230.2 -> **286.4** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4458). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 8.1 -> **7.1** (-12.3%) | 23.7 -> **35.8** | 200.1 -> **261.3** | Status 'Stunned' appliers overtuned on own (WR: 55.4%); Weather 'Raining' beneficiaries undertuned (WR: 24.6%) |
| `WDW` | Ice | Buff / Sustain | 25.0 -> **29.0** (+16.0%) | - | 25.0 -> **29.0** | Individual spell undertuned (WR: 10.7%, Casts: 5282, mult: 1.161) |
| `WDL` | Ice | Debuff / Control | 52.0 -> **49.5** (-4.8%) | - | 52.0 -> **49.5** | Individual spell overtuned (WR: 63.1%, Casts: 1752, mult: 0.952) |
| `WDD` | Ice | Ultimate | 22.0 -> **17.7** (-19.5%) | 15.4 -> **20.3** | 360.8 -> **377.0** | Weather 'Blizzard' beneficiaries overtuned (WR: 55.0%); Location 'Tundra' beneficiaries overtuned (WR: 55.0%) |
| `DWF` | Ice | Debuff / Control | 53.5 -> **48.5** (-9.3%) | - | 53.5 -> **48.5** | Individual spell overtuned (WR: 73.8%, Casts: 3738, mult: 0.907) |
| `DWW` | Ice | Debuff / Control | 38.1 -> **36.3** (-4.7%) | - | 38.1 -> **36.3** | Individual spell overtuned (WR: 62.7%, Casts: 3964, mult: 0.954) |
| `DWE` | Ice | Setup - Location | 33.4 -> **40.3** (+20.7%) | - | 33.4 -> **40.3** | Location 'Tundra' appliers undertuned (WR: 23.6%, casts: 1795); Individual spell undertuned (WR: 23.6%, Casts: 1795, mult: 1.104) |
| `DWL` | Ice | Debuff / Control | 52.9 -> **48.9** (-7.6%) | - | 52.9 -> **48.9** | Individual spell overtuned (WR: 69.9%, Casts: 8031, mult: 0.924) |
| `DWD` | Ice | Conditional Strike | 11.4 -> **10.4** (-8.8%) | 20.0 -> **28.2** | 239.4 -> **303.7** | Status 'Frosty' beneficiaries undertuned (WR: 29.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 3252). Increasing spread: b -14.9%, n +30.5% |
| `ELF` | Wind | Conditional Strike | 11.7 -> **10.3** (-12.0%) | 27.3 -> **38.5** | 331.1 -> **406.9** | Class Wind undertuned (WR: 33.7%, factor: 1.065); Status 'Bleeding' beneficiaries undertuned (WR: 41.3%) |
| `ELW` | Wind | Debuff / Control | 33.1 -> **35.3** (+6.6%) | - | 33.1 -> **35.3** | Class Wind undertuned (WR: 33.7%, factor: 1.065) |
| `ELE` | Wind | Setup - Weather | 26.1 -> **32.4** (+24.1%) | - | 26.1 -> **32.4** | Class Wind undertuned (WR: 33.7%, factor: 1.065); Individual spell undertuned (WR: 9.9%, Casts: 4017, mult: 1.165) |
| `ELL` | Wind | Buff / Sustain | 46.8 -> **51.4** (+9.8%) | - | 46.8 -> **51.4** | Class Wind undertuned (WR: 33.7%, factor: 1.065); Individual spell undertuned (WR: 41.3%, Casts: 682, mult: 1.030) |
| `ELD` | Wind | Conditional Strike | 6.3 -> **7.3** (+15.9%) | 23.3 -> **33.8** | 153.1 -> **254.0** | Class Wind undertuned (WR: 33.7%, factor: 1.065); Weather 'Raining' beneficiaries undertuned (WR: 24.6%) |
| `LEF` | Wind | Conditional Strike | 6.9 -> **6.5** (-5.8%) | 22.3 -> **30.4** | 160.8 -> **204.1** | Class Wind undertuned (WR: 33.7%, factor: 1.065); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 1942). Increasing spread: b -17.7%, n +36.3% |
| `LEW` | Wind | Debuff / Control | 42.3 -> **41.9** (-0.9%) | - | 42.3 -> **41.9** | Class Wind undertuned (WR: 33.7%, factor: 1.065); Individual spell overtuned (WR: 68.3%, Casts: 4464, mult: 0.931) |
| `LEE` | Wind | Setup - Weather | 21.9 -> **27.1** (+23.7%) | - | 21.9 -> **27.1** | Class Wind undertuned (WR: 33.7%, factor: 1.065); Individual spell undertuned (WR: 11.1%, Casts: 2310, mult: 1.159) |
| `LEL` | Wind | Buff / Sustain | 54.4 -> **59.2** (+8.8%) | - | 54.4 -> **59.2** | Class Wind undertuned (WR: 33.7%, factor: 1.065); Individual spell undertuned (WR: 43.7%, Casts: 375, mult: 1.022) |
| `EDF` | Poison | Conditional Strike | 6.8 -> **5.5** (-19.1%) | 22.1 -> **29.6** | 157.1 -> **168.3** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.9% vs 30% floor, Casts: 3677). Increasing spread: b -16.4%, n +33.7% |
| `EDW` | Poison | Debuff / Control | 16.2 -> **13.5** (-16.7%) | - | 16.2 -> **13.5** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Individual spell overtuned (WR: 80.8%, Casts: 279, mult: 0.877) |
| `EDE` | Poison | Setup - Location | 29.2 -> **29.4** (+0.7%) | - | 29.2 -> **29.4** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Location 'Swamp' appliers undertuned (WR: 42.0%, casts: 184) |
| `EDL` | Poison | Debuff / Control | 5.7 -> **4.5** (-21.1%) | - | 5.7 -> **4.5** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Individual spell overtuned (WR: 90.3%, Casts: 3891, mult: 0.834) |
| `EDD` | Poison | Ultimate | 17.6 -> **19.0** (+8.0%) | 20.0 -> **20.6** | 369.6 -> **410.4** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Status 'Bleeding' beneficiaries undertuned (WR: 41.3%) |
| `DEF` | Poison | Conditional Strike | 21.1 -> **18.1** (-14.2%) | 3.1 -> **3.8** | 86.5 -> **86.9** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.0% vs 30% floor, Casts: 666). Increasing spread: b -11.2%, n +22.9% |
| `DEW` | Poison | Debuff / Control | 15.7 -> **13.2** (-15.9%) | - | 15.7 -> **13.2** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Individual spell overtuned (WR: 79.5%, Casts: 5398, mult: 0.883) |
| `DEE` | Poison | Debuff / Control | 20.9 -> **19.3** (-7.7%) | - | 20.9 -> **19.3** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Individual spell overtuned (WR: 58.8%, Casts: 4655, mult: 0.969) |
| `DEL` | Poison | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 26.2 -> **37.1** | 19.0 -> **22.9** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Status 'Bleeding' beneficiaries undertuned (WR: 41.3%) |
| `DED` | Poison | Debuff / Control | 23.4 -> **22.6** (-3.4%) | - | 23.4 -> **22.6** | Class Poison overtuned (WR: 62.0%, factor: 0.952); Individual spell undertuned (WR: 45.1%, Casts: 2532, mult: 1.016) |
| `LDF` | Cosmic | Debuff / Control | 36.8 -> **35.5** (-3.5%) | - | 36.8 -> **35.5** | Individual spell overtuned (WR: 59.6%, Casts: 2704, mult: 0.966) |
| `LDW` | Cosmic | Debuff / Control | 31.1 -> **29.1** (-6.4%) | - | 31.1 -> **29.1** | Status 'Stunned' appliers overtuned on own (WR: 55.4%); Individual spell overtuned (WR: 62.7%, Casts: 1628, mult: 0.954) |
| `LDE` | Cosmic | Setup - Location | 21.0 -> **21.3** (+1.4%) | - | 21.0 -> **21.3** | Individual spell undertuned (WR: 45.9%, Casts: 221, mult: 1.013) |
| `LDL` | Cosmic | Conditional Strike | 6.5 -> **5.8** (-10.8%) | 22.4 -> **30.7** | 152.1 -> **183.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 6575). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 25.7%, Casts: 6575, mult: 1.095) |
| `LDD` | Cosmic | Ultimate | 14.6 -> **11.6** (-20.5%) | 21.2 -> **29.0** | 324.1 -> **348.0** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 937). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 58.3%, Casts: 937, mult: 0.971) |
| `DLF` | Cosmic | Conditional Strike | 7.5 -> **6.7** (-10.7%) | 23.4 -> **30.7** | 183.0 -> **212.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 1921). Increasing spread: b -15.3%, n +31.4%; Individual spell undertuned (WR: 35.8%, Casts: 1921, mult: 1.053) |
| `DLW` | Cosmic | Direct Damage | 44.8 -> **41.6** (-7.1%) | - | 44.8 -> **41.6** | Individual spell overtuned (WR: 69.0%, Casts: 4897, mult: 0.928) |
| `DLE` | Cosmic | Direct Damage | 50.7 -> **58.7** (+15.8%) | - | 50.7 -> **58.7** | Individual spell undertuned (WR: 11.3%, Casts: 2945, mult: 1.158) |
| `DLL` | Cosmic | Conditional Strike | 10.9 -> **9.9** (-9.2%) | 20.7 -> **28.4** | 236.5 -> **291.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 314). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 23.6%, Casts: 314, mult: 1.104) |
