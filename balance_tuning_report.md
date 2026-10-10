# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T14:02:16Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 112.4s  
**Total Spells Tuned:** 114 / 125  

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
| **Ghostfire** | 18,689 | 60.1% | 60.1% | 12.3 | Overtuned ⚠️ |
| **Plants** | 29,576 | 56.6% | 56.6% | 7.6 | Overtuned ⚠️ |
| **Beasts** | 18,916 | 53.0% | 53.0% | 6.2 | Balanced ✅ |
| **Dark** | 13,286 | 52.9% | 52.9% | 10.9 | Balanced ✅ |
| **Blood** | 18,947 | 51.6% | 51.6% | 10.6 | Balanced ✅ |
| **Fire** | 8,782 | 51.5% | 51.5% | 13.9 | Balanced ✅ |
| **Lightning** | 21,382 | 51.2% | 51.2% | 9.8 | Balanced ✅ |
| **Light** | 19,970 | 51.1% | 51.1% | 2.8 | Balanced ✅ |
| **Ice** | 37,013 | 50.2% | 50.2% | 12.6 | Balanced ✅ |
| **Cosmic** | 20,659 | 49.7% | 49.7% | 13.4 | Balanced ✅ |
| **Poison** | 22,992 | 48.7% | 48.7% | 8.6 | Balanced ✅ |
| **Wind** | 26,407 | 47.9% | 47.9% | 11.9 | Balanced ✅ |
| **Fey** | 27,644 | 43.4% | 43.4% | 9.3 | Undertuned ⚠️ |
| **Water** | 12,081 | 42.5% | 42.5% | 4.4 | Undertuned ⚠️ |
| **Earth** | 21,633 | 40.5% | 40.5% | 10.1 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 18,884 (55.1%) | 7,489 (43.6%) | 6.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 3,119 (47.3%) | 11,226 (64.4%) | 3.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,264 (63.6%) | 7,753 (49.2%) | 3.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 4,869 (75.1%) | 11,652 (49.2%) | 1.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 17,097 (48.1%) | 2,948 (54.9%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 4,151 (59.0%) | 6,404 (44.2%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 5,249 (23.0%) | 2,360 (55.8%) | 5.1% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 58.2 -> **55.0** (-5.5%) | - | 58.2 -> **55.0** | Individual spell overtuned (WR: 64.7%, Casts: 1303, mult: 0.945) |
| `FFW` | Fire | Debuff / Control | 43.5 -> **42.3** (-2.8%) | - | 43.5 -> **42.3** | Status 'Burning' appliers overtuned on own (WR: 63.6%); Individual spell undertuned (WR: 43.8%, Casts: 1393, mult: 1.021) |
| `FFE` | Fire | Debuff / Control | 35.0 -> **33.4** (-4.6%) | - | 35.0 -> **33.4** | Individual spell overtuned (WR: 62.5%, Casts: 1710, mult: 0.954) |
| `FFL` | Fire | Debuff / Control | 7.5 -> **6.5** (-13.3%) | - | 7.5 -> **6.5** | Status 'Burning' appliers overtuned on own (WR: 63.6%); Individual spell overtuned (WR: 71.8%, Casts: 1303, mult: 0.916) |
| `FFD` | Fire | Conditional Strike | 16.6 -> **14.5** (-12.7%) | 4.8 -> **6.5** | 96.3 -> **108.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 3073). Increasing spread: b -17.4%, n +35.7%; Individual spell undertuned (WR: 34.5%, Casts: 3073, mult: 1.058) |
| `WWF` | Water | Conditional Strike | 24.1 -> **20.1** (-16.6%) | 4.4 -> **5.8** | 130.1 -> **136.7** | Class Water undertuned (WR: 42.5%, factor: 1.030); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.8% vs 30% floor, Casts: 1307). Increasing spread: b -15.3%, n +31.3% |
| `WWE` | Water | Setup - Weather | 17.6 -> **22.0** (+25.0%) | - | 17.6 -> **22.0** | Class Water undertuned (WR: 42.5%, factor: 1.030); Weather 'Raining' appliers undertuned (WR: 23.0%, casts: 5249) |
| `WWL` | Water | Buff / Sustain | 57.5 -> **57.1** (-0.7%) | - | 57.5 -> **57.1** | Class Water undertuned (WR: 42.5%, factor: 1.030); Individual spell overtuned (WR: 59.9%, Casts: 1511, mult: 0.965) |
| `WWD` | Water | Buff / Sustain | 42.6 -> **39.8** (-6.6%) | - | 42.6 -> **39.8** | Class Water undertuned (WR: 42.5%, factor: 1.030); Individual spell overtuned (WR: 73.9%, Casts: 1030, mult: 0.907) |
| `EEF` | Earth | Conditional Strike | 21.0 -> **18.7** (-11.0%) | 4.4 -> **6.0** | 113.4 -> **130.9** | Class Earth undertuned (WR: 40.5%, factor: 1.038); Status 'Frosty' beneficiaries undertuned (WR: 43.6%) |
| `EEW` | Earth | Buff / Sustain | 35.7 -> **41.0** (+14.8%) | - | 35.7 -> **41.0** | Class Earth undertuned (WR: 40.5%, factor: 1.038); Individual spell undertuned (WR: 23.3%, Casts: 8987, mult: 1.105) |
| `EEE` | Earth | Conditional Strike | 5.4 -> **6.3** (+16.7%) | 1.5 -> **1.5** | 13.5 -> **15.8** | Class Earth undertuned (WR: 40.5%, factor: 1.038); Condition triggers excessively (N=1 conditions, Trigger Rate: 88.3% vs 55% ceiling, WR: 64.7%). Compressing spread: b +18.3%, n -25.7% |
| `EED` | Earth | Direct Damage | 6.2 -> **6.0** (-3.2%) | - | 6.2 -> **6.0** | Class Earth undertuned (WR: 40.5%, factor: 1.038); Individual spell overtuned (WR: 67.0%, Casts: 1937, mult: 0.936) |
| `LLF` | Light | Conditional Strike | 3.0 -> **2.4** (-20.0%) | 5.1 -> **6.9** | 18.3 -> **19.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 5734). Increasing spread: b -17.3%, n +35.4%; Individual spell overtuned (WR: 56.9%, Casts: 5734, mult: 0.976) |
| `LLW` | Light | Debuff / Control | 25.4 -> **24.6** (-3.1%) | - | 25.4 -> **24.6** | Individual spell overtuned (WR: 58.5%, Casts: 1455, mult: 0.970) |
| `LLL` | Light | Buff / Sustain | 31.6 -> **32.5** (+2.8%) | - | 31.6 -> **32.5** | Individual spell undertuned (WR: 42.2%, Casts: 5983, mult: 1.027) |
| `LLD` | Light | Ultimate | 22.6 -> **18.1** (-19.9%) | 9.3 -> **12.0** | 232.8 -> **235.3** | Weather 'Sunny' beneficiaries overtuned (WR: 64.4%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 3679). Increasing spread: b -18.0%, n +37.0% |
| `DDF` | Dark | Conditional Strike | 14.7 -> **11.8** (-19.7%) | 5.5 -> **7.5** | 95.5 -> **100.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1666). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 57.1%, Casts: 1666, mult: 0.976) |
| `DDW` | Dark | Debuff / Control | 48.3 -> **47.6** (-1.4%) | - | 48.3 -> **47.6** | Individual spell overtuned (WR: 54.2%, Casts: 4477, mult: 0.986) |
| `DDE` | Dark | Setup - Weather | 22.5 -> **24.9** (+10.7%) | - | 22.5 -> **24.9** | Weather 'Darkness' appliers undertuned (WR: 35.9%, casts: 3649); Individual spell undertuned (WR: 35.8%, Casts: 3649, mult: 1.052) |
| `DDL` | Dark | Debuff / Control | 24.5 -> **23.6** (-3.7%) | - | 24.5 -> **23.6** | Individual spell overtuned (WR: 60.0%, Casts: 1354, mult: 0.964) |
| `DDD` | Dark | Debuff / Control | 31.3 -> **28.7** (-8.3%) | - | 31.3 -> **28.7** | Individual spell overtuned (WR: 71.5%, Casts: 2140, mult: 0.917) |
| `FWF` | Ghostfire | Debuff / Control | 40.3 -> **34.0** (-15.6%) | - | 40.3 -> **34.0** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960); Status 'Burning' appliers overtuned on own (WR: 63.6%) |
| `FWW` | Ghostfire | Debuff / Control | 14.8 -> **14.4** (-2.7%) | - | 14.8 -> **14.4** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960); Status 'Cursed' appliers overtuned on own (WR: 57.6%) |
| `FWE` | Ghostfire | Setup - Location | 24.8 -> **25.5** (+2.8%) | - | 24.8 -> **25.5** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960); Location 'Graveyard' appliers undertuned (WR: 40.2%, casts: 1570) |
| `FWL` | Ghostfire | Debuff / Control | 45.0 -> **42.0** (-6.7%) | - | 45.0 -> **42.0** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960); Status 'Cursed' appliers overtuned on own (WR: 57.6%) |
| `FWD` | Ghostfire | Ultimate | 20.7 -> **16.0** (-22.7%) | 9.3 -> **11.9** | 213.2 -> **206.4** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960); Status 'Cursed' beneficiaries overtuned (WR: 60.4%) |
| `WFF` | Ghostfire | Conditional Strike | 15.0 -> **11.9** (-20.7%) | 5.2 -> **7.1** | 93.0 -> **96.4** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.3% vs 30% floor, Casts: 1089). Increasing spread: b -17.5%, n +35.9% |
| `WFW` | Ghostfire | Debuff / Control | 32.5 -> **28.6** (-12.0%) | - | 32.5 -> **28.6** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960); Individual spell overtuned (WR: 71.1%, Casts: 2686, mult: 0.919) |
| `WFE` | Ghostfire | Debuff / Control | 34.0 -> **26.2** (-22.9%) | - | 34.0 -> **26.2** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960); Status 'Bleeding' appliers overtuned on own (WR: 75.1%) |
| `WFL` | Ghostfire | Buff / Sustain | 36.6 -> **35.1** (-4.1%) | - | 36.6 -> **35.1** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960) |
| `WFD` | Ghostfire | Conditional Strike | 15.9 -> **11.6** (-27.0%) | 4.9 -> **6.7** | 93.8 -> **89.3** | Class Ghostfire overtuned (WR: 60.1%, factor: 0.960); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.4% vs 30% floor, Casts: 1593). Increasing spread: b -17.4%, n +35.8% |
| `FEF` | Beasts | Debuff / Control | 22.3 -> **21.0** (-5.8%) | - | 22.3 -> **21.0** | Individual spell overtuned (WR: 65.3%, Casts: 1831, mult: 0.943) |
| `FEW` | Beasts | Conditional Strike | 13.9 -> **12.0** (-13.7%) | 5.2 -> **7.3** | 86.2 -> **99.6** | Status 'Entangled' beneficiaries undertuned (WR: 44.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 3754). Increasing spread: b -17.9%, n +36.8% |
| `FEE` | Beasts | Buff / Sustain | 23.5 -> **24.8** (+5.5%) | - | 23.5 -> **24.8** | Individual spell undertuned (WR: 35.3%, Casts: 1973, mult: 1.055) |
| `FEL` | Beasts | Buff / Sustain | 23.8 -> **24.7** (+3.8%) | - | 23.8 -> **24.7** | Individual spell undertuned (WR: 39.0%, Casts: 1721, mult: 1.040) |
| `FED` | Beasts | Conditional Strike | 5.8 -> **5.6** (-3.4%) | 1.8 -> **1.7** | 16.2 -> **15.1** | Condition triggers within target window (46.9%), but combo payoff is warping win rate (66.0%). Compressing spread: b +3.0%, n -8.0%; Individual spell overtuned (WR: 66.0%, Casts: 627, mult: 0.940) |
| `EFF` | Beasts | Debuff / Control | 17.2 -> **13.6** (-20.9%) | 5.3 -> **7.2** | 108.4 -> **111.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.3% vs 30% floor, Casts: 1228). Increasing spread: b -17.1%, n +35.1%; Individual spell overtuned (WR: 62.3%, Casts: 1228, mult: 0.955) |
| `EFW` | Beasts | Buff / Sustain | 22.2 -> **23.1** (+4.1%) | - | 22.2 -> **23.1** | Individual spell undertuned (WR: 38.5%, Casts: 1223, mult: 1.042) |
| `EFL` | Beasts | Buff / Sustain | 20.8 -> **17.1** (-17.8%) | - | 20.8 -> **17.1** | Individual spell overtuned (WR: 93.0%, Casts: 2623, mult: 0.822) |
| `EFD` | Beasts | Ultimate | 14.8 -> **11.9** (-19.6%) | 13.2 -> **18.5** | 210.2 -> **232.1** | Status 'Entangled' beneficiaries undertuned (WR: 44.2%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1800). Increasing spread: b -18.0%, n +36.9% |
| `FLF` | Lightning | Conditional Strike | 14.2 -> **11.2** (-21.1%) | 5.4 -> **7.2** | 90.9 -> **91.8** | Status 'Stunned' beneficiaries overtuned (WR: 54.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 986). Increasing spread: b -17.9%, n +36.8% |
| `FLW` | Lightning | Debuff / Control | 44.4 -> **43.3** (-2.5%) | - | 44.4 -> **43.3** | Individual spell overtuned (WR: 57.2%, Casts: 3545, mult: 0.975) |
| `FLE` | Lightning | Setup - Weather | 22.3 -> **23.0** (+3.1%) | - | 22.3 -> **23.0** | Weather 'Storming' appliers undertuned (WR: 45.2%, casts: 1509); Individual spell undertuned (WR: 45.2%, Casts: 1509, mult: 1.016) |
| `FLL` | Lightning | Buff / Sustain | 24.6 -> **24.0** (-2.4%) | - | 24.6 -> **24.0** | Individual spell overtuned (WR: 56.7%, Casts: 1073, mult: 0.977) |
| `FLD` | Lightning | Ultimate | 20.6 -> **16.9** (-18.0%) | 9.4 -> **12.6** | 214.2 -> **229.8** | Status 'Stunned' beneficiaries overtuned (WR: 54.9%); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1962). Increasing spread: b -18.0%, n +37.0% |
| `LFF` | Lightning | Conditional Strike | 14.8 -> **12.2** (-17.6%) | 5.3 -> **7.2** | 93.2 -> **100.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 1582). Increasing spread: b -17.7%, n +36.5% |
| `LFW` | Lightning | Buff / Sustain | 33.5 -> **32.9** (-1.8%) | - | 33.5 -> **32.9** | Individual spell overtuned (WR: 55.7%, Casts: 3106, mult: 0.981) |
| `LFE` | Lightning | Debuff / Control | 44.5 -> **42.7** (-4.0%) | - | 44.5 -> **42.7** | Individual spell overtuned (WR: 60.9%, Casts: 2154, mult: 0.961) |
| `LFL` | Lightning | Debuff / Control | 25.8 -> **21.7** (-15.9%) | 4.5 -> **6.0** | 141.9 -> **151.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.2% vs 30% floor, Casts: 2411). Increasing spread: b -15.9%, n +32.6% |
| `LFD` | Lightning | Conditional Strike | 15.9 -> **14.0** (-11.9%) | 7.7 -> **10.5** | 138.3 -> **161.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 3054). Increasing spread: b -17.9%, n +36.8%; Individual spell undertuned (WR: 31.5%, Casts: 3054, mult: 1.070) |
| `FDF` | Blood | Conditional Strike | 13.9 -> **11.8** (-15.1%) | 5.5 -> **7.5** | 90.4 -> **100.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 965). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 40.2%, Casts: 965, mult: 1.035) |
| `FDW` | Blood | Direct Damage | 61.8 -> **63.1** (+2.1%) | - | 61.8 -> **63.1** | Individual spell undertuned (WR: 43.8%, Casts: 1747, mult: 1.021) |
| `FDE` | Blood | Setup - Weather | 19.4 -> **21.1** (+8.8%) | - | 19.4 -> **21.1** | Individual spell undertuned (WR: 27.8%, Casts: 4270, mult: 1.086) |
| `FDL` | Blood | Debuff / Control | 32.1 -> **27.3** (-15.0%) | - | 32.1 -> **27.3** | Status 'Bleeding' appliers overtuned on own (WR: 75.1%); Individual spell overtuned (WR: 67.8%, Casts: 603, mult: 0.933) |
| `FDD` | Blood | Ultimate | 19.5 -> **15.6** (-20.0%) | 9.0 -> **12.3** | 195.0 -> **207.5** | Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 2610). Increasing spread: b -17.9%, n +36.9%; Individual spell overtuned (WR: 56.7%, Casts: 2610, mult: 0.977) |
| `DFF` | Blood | Conditional Strike | 15.3 -> **12.6** (-17.6%) | 5.1 -> **6.9** | 93.3 -> **99.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 1622). Increasing spread: b -17.4%, n +35.7% |
| `DFW` | Blood | Debuff / Control | 24.0 -> **19.2** (-20.0%) | - | 24.0 -> **19.2** | Status 'Bleeding' appliers overtuned on own (WR: 75.1%); Individual spell overtuned (WR: 81.1%, Casts: 1315, mult: 0.876) |
| `DFE` | Blood | Buff / Sustain | 38.7 -> **42.1** (+8.8%) | - | 38.7 -> **42.1** | Individual spell undertuned (WR: 27.5%, Casts: 1064, mult: 1.087) |
| `DFL` | Blood | Buff / Sustain | 32.8 -> **29.7** (-9.5%) | - | 32.8 -> **29.7** | Individual spell overtuned (WR: 74.1%, Casts: 2568, mult: 0.906) |
| `DFD` | Blood | Conditional Strike | 35.8 -> **40.0** (+11.7%) | 1.0 -> **0.7** | 71.6 -> **68.0** | Condition triggers excessively (N=1 conditions, Trigger Rate: 90.9% vs 55% ceiling, WR: 69.4%). Compressing spread: b +20.7%, n -28.5%; Individual spell overtuned (WR: 69.4%, Casts: 2183, mult: 0.926) |
| `WEF` | Plants | Conditional Strike | 16.0 -> **13.3** (-16.9%) | 4.9 -> **6.6** | 94.4 -> **101.1** | Class Plants overtuned (WR: 56.6%, factor: 0.974); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.0% vs 30% floor, Casts: 3341). Increasing spread: b -17.2%, n +35.3% |
| `WEW` | Plants | Debuff / Control | 35.3 -> **37.7** (+6.8%) | - | 35.3 -> **37.7** | Class Plants overtuned (WR: 56.6%, factor: 0.974); Individual spell undertuned (WR: 25.2%, Casts: 2127, mult: 1.097) |
| `WEE` | Plants | Setup - Location | 22.2 -> **23.2** (+4.5%) | - | 22.2 -> **23.2** | Class Plants overtuned (WR: 56.6%, factor: 0.974); Location 'Jungle' appliers undertuned (WR: 39.6%, casts: 2840) |
| `WEL` | Plants | Debuff / Control | 43.9 -> **40.1** (-8.7%) | - | 43.9 -> **40.1** | Class Plants overtuned (WR: 56.6%, factor: 0.974); Status 'Entangled' appliers overtuned on own (WR: 59.0%) |
| `WED` | Plants | Conditional Strike | 19.0 -> **15.2** (-20.0%) | 5.5 -> **7.5** | 123.5 -> **129.2** | Class Plants overtuned (WR: 56.6%, factor: 0.974); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 1485). Increasing spread: b -17.8%, n +36.6% |
| `EWF` | Plants | Buff / Sustain | 18.3 -> **13.9** (-24.0%) | 4.7 -> **5.9** | 104.3 -> **95.9** | Class Plants overtuned (WR: 56.6%, factor: 0.974); Weather 'Sunny' beneficiaries overtuned (WR: 64.4%) |
| `EWW` | Plants | Debuff / Control | 27.5 -> **22.3** (-18.9%) | - | 27.5 -> **22.3** | Class Plants overtuned (WR: 56.6%, factor: 0.974); Individual spell overtuned (WR: 91.0%, Casts: 3092, mult: 0.831) |
| `EWL` | Plants | Debuff / Control | 59.4 -> **55.2** (-7.1%) | - | 59.4 -> **55.2** | Class Plants overtuned (WR: 56.6%, factor: 0.974); Individual spell overtuned (WR: 62.6%, Casts: 2135, mult: 0.954) |
| `EWD` | Plants | Conditional Strike | 12.4 -> **8.8** (-29.0%) | 5.0 -> **7.0** | 74.4 -> **70.4** | Class Plants overtuned (WR: 56.6%, factor: 0.974); Status 'Bleeding' appliers overtuned on own (WR: 75.1%) |
| `WLF` | Fey | Conditional Strike | 15.3 -> **12.4** (-19.0%) | 5.0 -> **6.5** | 91.8 -> **93.0** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Status 'Cursed' beneficiaries overtuned (WR: 60.4%) |
| `WLW` | Fey | Debuff / Control | 45.7 -> **43.1** (-5.7%) | - | 45.7 -> **43.1** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Status 'Cursed' appliers overtuned on own (WR: 57.6%) |
| `WLE` | Fey | Setup - Location | 21.0 -> **27.9** (+32.9%) | - | 21.0 -> **27.9** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Location 'Enchanted Forest' appliers undertuned (WR: 12.2%, casts: 2677) |
| `WLL` | Fey | Direct Damage | 61.0 -> **59.7** (-2.1%) | - | 61.0 -> **59.7** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Individual spell overtuned (WR: 62.9%, Casts: 2443, mult: 0.953) |
| `WLD` | Fey | Ultimate | 20.7 -> **17.1** (-17.4%) | 9.0 -> **12.3** | 207.0 -> **227.4** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1618). Increasing spread: b -18.0%, n +37.0% |
| `LWF` | Fey | Debuff / Control | 27.0 -> **23.1** (-14.4%) | 4.6 -> **6.2** | 151.2 -> **166.3** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.1% vs 30% floor, Casts: 1421). Increasing spread: b -16.8%, n +34.4% |
| `LWW` | Fey | Debuff / Control | 37.0 -> **42.1** (+13.8%) | - | 37.0 -> **42.1** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Individual spell undertuned (WR: 22.4%, Casts: 5299, mult: 1.109) |
| `LWL` | Fey | Debuff / Control | 35.5 -> **37.1** (+4.5%) | - | 35.5 -> **37.1** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Individual spell undertuned (WR: 44.8%, Casts: 2091, mult: 1.017) |
| `LWD` | Fey | Conditional Strike | 15.1 -> **14.0** (-7.3%) | 5.5 -> **7.5** | 98.1 -> **119.0** | Class Fey undertuned (WR: 43.4%, factor: 1.027); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2083). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 17.1 -> **14.2** (-17.0%) | 5.1 -> **6.7** | 104.3 -> **109.3** | Weather 'Raining' beneficiaries overtuned (WR: 55.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.6% vs 30% floor, Casts: 1414). Increasing spread: b -17.0%, n +34.8% |
| `WDE` | Ice | Setup - Weather | 21.7 -> **24.5** (+12.9%) | - | 21.7 -> **24.5** | Individual spell undertuned (WR: 17.9%, Casts: 4030, mult: 1.129) |
| `WDL` | Ice | Debuff / Control | 46.5 -> **43.6** (-6.2%) | - | 46.5 -> **43.6** | Status 'Frosty' appliers overtuned on own (WR: 55.1%); Individual spell overtuned (WR: 62.3%, Casts: 1950, mult: 0.955) |
| `WDD` | Ice | Ultimate | 29.2 -> **23.5** (-19.5%) | 6.9 -> **9.0** | 230.7 -> **235.0** | Weather 'Blizzard' beneficiaries overtuned (WR: 56.2%); Location 'Tundra' beneficiaries overtuned (WR: 56.2%) |
| `DWF` | Ice | Debuff / Control | 48.3 -> **45.2** (-6.4%) | - | 48.3 -> **45.2** | Status 'Frosty' appliers overtuned on own (WR: 55.1%); Individual spell overtuned (WR: 62.8%, Casts: 8331, mult: 0.953) |
| `DWW` | Ice | Debuff / Control | 35.5 -> **34.7** (-2.3%) | - | 35.5 -> **34.7** | Individual spell overtuned (WR: 56.9%, Casts: 3912, mult: 0.976) |
| `DWE` | Ice | Setup - Location | 20.4 -> **21.9** (+7.4%) | - | 20.4 -> **21.9** | Location 'Tundra' appliers undertuned (WR: 40.1%, casts: 1112); Individual spell undertuned (WR: 40.0%, Casts: 1112, mult: 1.036) |
| `DWL` | Ice | Debuff / Control | 48.0 -> **47.1** (-1.9%) | - | 48.0 -> **47.1** | Status 'Frosty' appliers overtuned on own (WR: 55.1%) |
| `DWD` | Ice | Conditional Strike | 18.3 -> **16.4** (-10.4%) | 4.2 -> **5.4** | 95.2 -> **105.0** | Status 'Frosty' beneficiaries undertuned (WR: 43.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.2% vs 30% floor, Casts: 1744). Increasing spread: b -12.3%, n +25.1% |
| `ELF` | Wind | Conditional Strike | 32.5 -> **27.0** (-16.9%) | 5.2 -> **7.0** | 201.5 -> **216.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.5% vs 30% floor, Casts: 1677). Increasing spread: b -17.0%, n +34.9% |
| `ELE` | Wind | Setup - Weather | 19.9 -> **20.3** (+2.0%) | - | 19.9 -> **20.3** | Individual spell undertuned (WR: 43.7%, Casts: 1780, mult: 1.022) |
| `ELL` | Wind | Buff / Sustain | 36.0 -> **40.0** (+11.1%) | - | 36.0 -> **40.0** | Individual spell undertuned (WR: 21.8%, Casts: 2415, mult: 1.112) |
| `ELD` | Wind | Conditional Strike | 17.5 -> **13.4** (-23.4%) | 5.1 -> **6.5** | 106.8 -> **100.5** | Weather 'Raining' beneficiaries overtuned (WR: 55.8%); Weather 'Blizzard' appliers overtuned on own (WR: 64.7%) |
| `LEF` | Wind | Conditional Strike | 15.7 -> **12.7** (-19.1%) | 4.9 -> **6.6** | 92.6 -> **96.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.9% vs 30% floor, Casts: 3373). Increasing spread: b -16.9%, n +34.6%; Individual spell overtuned (WR: 57.5%, Casts: 3373, mult: 0.974) |
| `LEW` | Wind | Debuff / Control | 58.6 -> **55.9** (-4.6%) | - | 58.6 -> **55.9** | Individual spell overtuned (WR: 62.6%, Casts: 8628, mult: 0.954) |
| `LEL` | Wind | Buff / Sustain | 38.5 -> **40.0** (+3.9%) | - | 38.5 -> **40.0** | Individual spell undertuned (WR: 39.5%, Casts: 1334, mult: 1.038) |
| `EDF` | Poison | Conditional Strike | 15.6 -> **13.9** (-10.9%) | 5.1 -> **6.8** | 95.2 -> **108.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.4% vs 30% floor, Casts: 3097). Increasing spread: b -16.6%, n +34.2%; Individual spell undertuned (WR: 32.2%, Casts: 3097, mult: 1.068) |
| `EDW` | Poison | Debuff / Control | 31.6 -> **29.2** (-7.6%) | - | 31.6 -> **29.2** | Individual spell overtuned (WR: 69.7%, Casts: 2142, mult: 0.925) |
| `EDE` | Poison | Setup - Location | 20.5 -> **22.6** (+10.2%) | - | 20.5 -> **22.6** | Location 'Swamp' appliers undertuned (WR: 35.9%, casts: 4861); Individual spell undertuned (WR: 35.9%, Casts: 4861, mult: 1.052) |
| `EDL` | Poison | Debuff / Control | 16.3 -> **14.1** (-13.5%) | - | 16.3 -> **14.1** | Individual spell overtuned (WR: 83.4%, Casts: 1042, mult: 0.865) |
| `EDD` | Poison | Ultimate | 31.9 -> **25.1** (-21.3%) | 7.9 -> **10.3** | 283.9 -> **283.6** | Location 'Swamp' beneficiaries overtuned (WR: 61.7%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 3118). Increasing spread: b -18.0%, n +36.9% |
| `DEF` | Poison | Conditional Strike | 32.0 -> **31.9** (-0.3%) | 2.4 -> **2.2** | 108.8 -> **102.1** | Condition triggers within target window (49.2%), but combo payoff is warping win rate (59.0%). Compressing spread: b +3.0%, n -8.0%; Individual spell overtuned (WR: 59.0%, Casts: 724, mult: 0.968) |
| `DEW` | Poison | Debuff / Control | 31.3 -> **30.1** (-3.8%) | - | 31.3 -> **30.1** | Individual spell overtuned (WR: 61.0%, Casts: 1291, mult: 0.960) |
| `DEE` | Poison | Debuff / Control | 25.0 -> **24.5** (-2.0%) | - | 25.0 -> **24.5** | Individual spell overtuned (WR: 56.0%, Casts: 857, mult: 0.979) |
| `DEL` | Poison | Conditional Strike | 1.7 -> **1.5** (-11.8%) | 5.2 -> **7.0** | 10.5 -> **12.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 4146). Increasing spread: b -16.8%, n +34.5%; Individual spell undertuned (WR: 40.5%, Casts: 4146, mult: 1.034) |
| `DED` | Poison | Debuff / Control | 29.4 -> **29.7** (+1.0%) | - | 29.4 -> **29.7** | Individual spell undertuned (WR: 46.5%, Casts: 1714, mult: 1.011) |
| `LDF` | Cosmic | Debuff / Control | 45.9 -> **43.4** (-5.4%) | - | 45.9 -> **43.4** | Individual spell overtuned (WR: 64.5%, Casts: 2474, mult: 0.946) |
| `LDW` | Cosmic | Debuff / Control | 48.7 -> **46.9** (-3.7%) | - | 48.7 -> **46.9** | Individual spell overtuned (WR: 60.3%, Casts: 1185, mult: 0.963) |
| `LDE` | Cosmic | Setup - Location | 19.7 -> **19.2** (-2.5%) | - | 19.7 -> **19.2** | Individual spell overtuned (WR: 57.7%, Casts: 693, mult: 0.973) |
| `LDL` | Cosmic | Conditional Strike | 16.5 -> **14.2** (-13.9%) | 4.9 -> **6.6** | 97.4 -> **107.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 4329). Increasing spread: b -16.8%, n +34.5%; Individual spell undertuned (WR: 40.7%, Casts: 4329, mult: 1.033) |
| `LDD` | Cosmic | Ultimate | 16.2 -> **13.0** (-19.8%) | 13.6 -> **18.6** | 236.5 -> **254.8** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1667). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 55.8%, Casts: 1667, mult: 0.980) |
| `DLF` | Cosmic | Conditional Strike | 19.6 -> **16.4** (-16.3%) | 5.0 -> **6.8** | 117.6 -> **127.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.1% vs 30% floor, Casts: 2097). Increasing spread: b -17.6%, n +36.1%; Individual spell undertuned (WR: 45.5%, Casts: 2097, mult: 1.015) |
| `DLE` | Cosmic | Direct Damage | 38.1 -> **39.7** (+4.2%) | - | 38.1 -> **39.7** | Individual spell undertuned (WR: 38.5%, Casts: 1817, mult: 1.042) |
| `DLL` | Cosmic | Conditional Strike | 26.6 -> **22.9** (-13.9%) | 4.5 -> **6.0** | 146.3 -> **160.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.5% vs 30% floor, Casts: 2886). Increasing spread: b -16.2%, n +33.3%; Individual spell undertuned (WR: 42.5%, Casts: 2886, mult: 1.026) |
| `DLD` | Cosmic | Conditional Strike | 45.0 -> **50.9** (+13.1%) | 1.5 -> **1.5** | 112.5 -> **127.2** | Condition triggers excessively (N=1 conditions, Trigger Rate: 93.7% vs 55% ceiling, WR: 63.9%). Compressing spread: b +19.2%, n -27.3%; Individual spell overtuned (WR: 63.9%, Casts: 1638, mult: 0.948) |
