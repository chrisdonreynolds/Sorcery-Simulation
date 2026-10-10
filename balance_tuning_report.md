# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T14:47:15Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 114.1s  
**Total Spells Tuned:** 115 / 125  

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
| **Dark** | 17,514 | 59.2% | 59.2% | 15.1 | Overtuned ⚠️ |
| **Light** | 14,802 | 58.3% | 58.3% | 3.1 | Overtuned ⚠️ |
| **Blood** | 22,007 | 54.9% | 54.9% | 11.7 | Overtuned ⚠️ |
| **Ghostfire** | 20,785 | 54.0% | 54.0% | 7.3 | Overtuned ⚠️ |
| **Fey** | 21,156 | 53.9% | 53.9% | 9.7 | Overtuned ⚠️ |
| **Poison** | 33,507 | 53.0% | 53.0% | 10.3 | Balanced ✅ |
| **Cosmic** | 20,093 | 52.6% | 52.6% | 14.5 | Balanced ✅ |
| **Fire** | 9,595 | 52.3% | 52.3% | 10.5 | Balanced ✅ |
| **Earth** | 15,598 | 51.6% | 51.6% | 17.9 | Balanced ✅ |
| **Plants** | 26,980 | 50.7% | 50.7% | 4.7 | Balanced ✅ |
| **Water** | 9,793 | 49.3% | 49.3% | 4.6 | Balanced ✅ |
| **Wind** | 22,071 | 45.9% | 45.9% | 11.3 | Undertuned ⚠️ |
| **Beasts** | 22,951 | 45.9% | 45.8% | 4.4 | Undertuned ⚠️ |
| **Ice** | 21,760 | 41.0% | 41.0% | 9.5 | Undertuned ⚠️ |
| **Lightning** | 21,094 | 38.5% | 38.5% | 6.1 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,533 (38.7%) | 6,313 (31.8%) | 0.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,128 (37.0%) | 11,060 (49.0%) | 2.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 8,322 (76.2%) | 11,067 (53.6%) | 3.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,764 (80.2%) | 14,116 (32.5%) | 2.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,897 (51.1%) | 5,256 (33.6%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 5,228 (56.3%) | 2,177 (46.6%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 443 (46.2%) | 1,234 (31.8%) | 1.5% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 42.2 -> **45.1** (+6.9%) | - | 42.2 -> **45.1** | Individual spell undertuned (WR: 32.0%, Casts: 282, mult: 1.068) |
| `FFW` | Fire | Debuff / Control | 32.0 -> **28.3** (-11.6%) | - | 32.0 -> **28.3** | Status 'Burning' appliers overtuned on own (WR: 76.2%); Individual spell overtuned (WR: 57.3%, Casts: 1046, mult: 0.975) |
| `FFE` | Fire | Debuff / Control | 29.5 -> **28.6** (-3.1%) | - | 29.5 -> **28.6** | Individual spell overtuned (WR: 59.0%, Casts: 2858, mult: 0.968) |
| `FFL` | Fire | Debuff / Control | 4.2 -> **3.3** (-21.4%) | - | 4.2 -> **3.3** | Status 'Burning' appliers overtuned on own (WR: 76.2%); Individual spell overtuned (WR: 81.0%, Casts: 1810, mult: 0.876) |
| `FFD` | Fire | Conditional Strike | 9.2 -> **8.1** (-12.0%) | 11.9 -> **16.0** | 118.7 -> **137.7** | Status 'Burning' beneficiaries overtuned (WR: 53.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 3599). Increasing spread: b -17.7%, n +36.4% |
| `WWF` | Water | Conditional Strike | 11.4 -> **8.4** (-26.3%) | 10.3 -> **13.3** | 128.8 -> **120.1** | Status 'Burning' beneficiaries overtuned (WR: 53.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.4% vs 30% floor, Casts: 4532). Increasing spread: b -15.0%, n +30.8% |
| `WWE` | Water | Setup - Weather | 24.1 -> **24.7** (+2.5%) | - | 24.1 -> **24.7** | Weather 'Raining' appliers undertuned (WR: 46.2%, casts: 443); Individual spell undertuned (WR: 46.2%, Casts: 443, mult: 1.013) |
| `WWL` | Water | Buff / Sustain | 49.0 -> **50.1** (+2.2%) | - | 49.0 -> **50.1** | Individual spell undertuned (WR: 43.7%, Casts: 942, mult: 1.021) |
| `WWD` | Water | Buff / Sustain | 35.6 -> **33.3** (-6.5%) | - | 35.6 -> **33.3** | Individual spell overtuned (WR: 67.0%, Casts: 203, mult: 0.936) |
| `EEF` | Earth | Conditional Strike | 10.9 -> **9.3** (-14.7%) | 10.9 -> **16.0** | 129.7 -> **158.1** | Status 'Frosty' beneficiaries undertuned (WR: 31.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 4069). Increasing spread: b -17.7%, n +36.5% |
| `EEW` | Earth | Buff / Sustain | 48.2 -> **56.9** (+18.0%) | - | 48.2 -> **56.9** | Individual spell undertuned (WR: 3.7%, Casts: 1404, mult: 1.180) |
| `EEE` | Earth | Conditional Strike | 8.1 -> **9.0** (+11.1%) | 1.5 -> **1.5** | 20.2 -> **22.5** | Condition triggers excessively (N=1 conditions, Trigger Rate: 95.0% vs 55% ceiling, WR: 80.0%). Compressing spread: b +25.9%, n -34.2%; Individual spell overtuned (WR: 80.0%, Casts: 2612, mult: 0.881) |
| `EED` | Earth | Direct Damage | 5.8 -> **5.3** (-8.6%) | - | 5.8 -> **5.3** | Individual spell overtuned (WR: 71.5%, Casts: 4966, mult: 0.917) |
| `LLF` | Light | Conditional Strike | 1.5 -> **1.1** (-26.7%) | 12.8 -> **17.4** | 20.7 -> **20.2** | Class Light overtuned (WR: 58.3%, factor: 0.967); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 7882). Increasing spread: b -17.6%, n +36.2% |
| `LLW` | Light | Debuff / Control | 23.8 -> **23.6** (-0.8%) | - | 23.8 -> **23.6** | Class Light overtuned (WR: 58.3%, factor: 0.967); Individual spell undertuned (WR: 42.6%, Casts: 3524, mult: 1.025) |
| `LLE` | Light | Setup - Weather | 38.3 -> **40.6** (+6.0%) | - | 38.3 -> **40.6** | Class Light overtuned (WR: 58.3%, factor: 0.967); Weather 'Sunny' appliers undertuned (WR: 37.0%, casts: 1128) |
| `LLL` | Light | Buff / Sustain | 25.9 -> **22.5** (-13.1%) | - | 25.9 -> **22.5** | Class Light overtuned (WR: 58.3%, factor: 0.967); Individual spell overtuned (WR: 75.7%, Casts: 1093, mult: 0.899) |
| `LLD` | Light | Ultimate | 15.7 -> **12.4** (-21.0%) | 15.9 -> **21.8** | 265.3 -> **282.7** | Class Light overtuned (WR: 58.3%, factor: 0.967); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1175). Increasing spread: b -18.0%, n +37.0% |
| `DDF` | Dark | Conditional Strike | 7.8 -> **6.5** (-16.7%) | 14.1 -> **19.3** | 117.8 -> **132.0** | Class Dark overtuned (WR: 59.2%, factor: 0.963); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 649). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 44.2 -> **41.4** (-6.3%) | - | 44.2 -> **41.4** | Class Dark overtuned (WR: 59.2%, factor: 0.963); Individual spell overtuned (WR: 58.0%, Casts: 11006, mult: 0.972) |
| `DDE` | Dark | Setup - Weather | 31.2 -> **34.8** (+11.5%) | - | 31.2 -> **34.8** | Class Dark overtuned (WR: 59.2%, factor: 0.963); Weather 'Darkness' appliers undertuned (WR: 29.3%, casts: 2032) |
| `DDL` | Dark | Debuff / Control | 22.0 -> **20.1** (-8.6%) | - | 22.0 -> **20.1** | Class Dark overtuned (WR: 59.2%, factor: 0.963); Individual spell overtuned (WR: 64.5%, Casts: 784, mult: 0.946) |
| `DDD` | Dark | Debuff / Control | 22.2 -> **18.2** (-18.0%) | - | 22.2 -> **18.2** | Class Dark overtuned (WR: 59.2%, factor: 0.963); Individual spell overtuned (WR: 86.6%, Casts: 3043, mult: 0.851) |
| `FWF` | Ghostfire | Debuff / Control | 22.1 -> **17.5** (-20.8%) | - | 22.1 -> **17.5** | Class Ghostfire overtuned (WR: 54.0%, factor: 0.984); Status 'Burning' appliers overtuned on own (WR: 76.2%) |
| `FWE` | Ghostfire | Setup - Location | 31.1 -> **39.1** (+25.7%) | - | 31.1 -> **39.1** | Class Ghostfire overtuned (WR: 54.0%, factor: 0.984); Location 'Graveyard' appliers undertuned (WR: 15.4%, casts: 1135) |
| `FWL` | Ghostfire | Debuff / Control | 37.9 -> **35.4** (-6.6%) | - | 37.9 -> **35.4** | Class Ghostfire overtuned (WR: 54.0%, factor: 0.984); Status 'Cursed' appliers overtuned on own (WR: 64.6%) |
| `FWD` | Ghostfire | Ultimate | 13.8 -> **14.7** (+6.5%) | 15.7 -> **15.6** | 230.5 -> **244.0** | Class Ghostfire overtuned (WR: 54.0%, factor: 0.984); Status 'Cursed' beneficiaries undertuned (WR: 35.6%) |
| `WFF` | Ghostfire | Conditional Strike | 8.7 -> **7.7** (-11.5%) | 14.0 -> **20.5** | 130.5 -> **165.6** | Class Ghostfire overtuned (WR: 54.0%, factor: 0.984); Status 'Bleeding' beneficiaries undertuned (WR: 32.5%) |
| `WFW` | Ghostfire | Debuff / Control | 25.3 -> **25.2** (-0.4%) | - | 25.3 -> **25.2** | Class Ghostfire overtuned (WR: 54.0%, factor: 0.984); Individual spell undertuned (WR: 46.1%, Casts: 413, mult: 1.013) |
| `WFE` | Ghostfire | Debuff / Control | 16.2 -> **12.4** (-23.5%) | - | 16.2 -> **12.4** | Class Ghostfire overtuned (WR: 54.0%, factor: 0.984); Status 'Bleeding' appliers overtuned on own (WR: 80.2%) |
| `WFL` | Ghostfire | Buff / Sustain | 34.2 -> **33.6** (-1.8%) | - | 34.2 -> **33.6** | Class Ghostfire overtuned (WR: 54.0%, factor: 0.984) |
| `WFD` | Ghostfire | Conditional Strike | 8.7 -> **7.0** (-19.5%) | 12.3 -> **16.8** | 115.7 -> **124.6** | Class Ghostfire overtuned (WR: 54.0%, factor: 0.984); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 2962). Increasing spread: b -17.8%, n +36.5% |
| `FEF` | Beasts | Debuff / Control | 19.4 -> **20.2** (+4.1%) | - | 19.4 -> **20.2** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Individual spell undertuned (WR: 42.8%, Casts: 1269, mult: 1.025) |
| `FEW` | Beasts | Conditional Strike | 8.5 -> **6.8** (-20.0%) | 14.8 -> **20.0** | 134.3 -> **142.8** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 258). Increasing spread: b -17.2%, n +35.4% |
| `FEE` | Beasts | Buff / Sustain | 23.2 -> **26.5** (+14.2%) | - | 23.2 -> **26.5** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Individual spell undertuned (WR: 19.2%, Casts: 2387, mult: 1.123) |
| `FEL` | Beasts | Buff / Sustain | 31.6 -> **36.7** (+16.1%) | - | 31.6 -> **36.7** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Individual spell undertuned (WR: 14.9%, Casts: 4059, mult: 1.142) |
| `FED` | Beasts | Conditional Strike | 5.1 -> **4.8** (-5.9%) | 2.0 -> **2.5** | 15.3 -> **16.8** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.1% vs 30% floor, Casts: 3599). Increasing spread: b -12.0%, n +24.4% |
| `EFF` | Beasts | Debuff / Control | 10.2 -> **8.8** (-13.7%) | 13.4 -> **18.4** | 146.9 -> **170.7** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1932). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 25.9 -> **25.6** (-1.2%) | - | 25.9 -> **25.6** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Individual spell overtuned (WR: 58.4%, Casts: 113, mult: 0.970) |
| `EFE` | Beasts | Buff / Sustain | 30.1 -> **29.7** (-1.3%) | - | 30.1 -> **29.7** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Individual spell overtuned (WR: 58.7%, Casts: 4228, mult: 0.969) |
| `EFL` | Beasts | Buff / Sustain | 12.0 -> **10.2** (-15.0%) | - | 12.0 -> **10.2** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Individual spell overtuned (WR: 90.5%, Casts: 4077, mult: 0.834) |
| `EFD` | Beasts | Ultimate | 15.1 -> **12.6** (-16.6%) | 18.6 -> **27.1** | 296.0 -> **354.1** | Class Beasts undertuned (WR: 45.9%, factor: 1.017); Location 'Jungle' beneficiaries undertuned (WR: 33.8%) |
| `FLF` | Lightning | Conditional Strike | 7.3 -> **6.8** (-6.8%) | 13.3 -> **19.4** | 104.4 -> **138.7** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Status 'Stunned' beneficiaries undertuned (WR: 33.6%) |
| `FLW` | Lightning | Debuff / Control | 34.8 -> **33.3** (-4.3%) | - | 34.8 -> **33.3** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Individual spell overtuned (WR: 71.9%, Casts: 2347, mult: 0.915) |
| `FLE` | Lightning | Setup - Weather | 26.5 -> **31.6** (+19.2%) | - | 26.5 -> **31.6** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Weather 'Storming' appliers undertuned (WR: 31.4%, casts: 624) |
| `FLL` | Lightning | Buff / Sustain | 26.3 -> **31.5** (+19.8%) | - | 26.3 -> **31.5** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Individual spell undertuned (WR: 14.0%, Casts: 2703, mult: 1.146) |
| `FLD` | Lightning | Ultimate | 14.2 -> **16.7** (+17.6%) | 16.1 -> **16.8** | 242.8 -> **297.3** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Status 'Stunned' beneficiaries undertuned (WR: 33.6%) |
| `LFF` | Lightning | Conditional Strike | 7.5 -> **7.2** (-4.0%) | 13.4 -> **18.4** | 108.0 -> **139.7** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3024). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 28.9 -> **29.2** (+1.0%) | - | 28.9 -> **29.2** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Individual spell overtuned (WR: 59.2%, Casts: 329, mult: 0.967) |
| `LFE` | Lightning | Debuff / Control | 31.4 -> **30.7** (-2.2%) | - | 31.4 -> **30.7** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Individual spell overtuned (WR: 67.0%, Casts: 1214, mult: 0.936) |
| `LFL` | Lightning | Debuff / Control | 15.5 -> **13.5** (-12.9%) | 10.5 -> **14.2** | 178.2 -> **205.2** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.7% vs 30% floor, Casts: 2954). Increasing spread: b -16.9%, n +34.8% |
| `LFD` | Lightning | Conditional Strike | 7.6 -> **6.9** (-9.2%) | 19.4 -> **26.4** | 155.0 -> **189.1** | Class Lightning undertuned (WR: 38.5%, factor: 1.046); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 2643). Increasing spread: b -17.5%, n +36.0% |
| `FDF` | Blood | Conditional Strike | 9.2 -> **7.3** (-20.7%) | 14.1 -> **19.3** | 138.9 -> **148.2** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 722). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 71.4 -> **76.6** (+7.3%) | - | 71.4 -> **76.6** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Individual spell undertuned (WR: 25.8%, Casts: 832, mult: 1.094) |
| `FDE` | Blood | Setup - Weather | 27.5 -> **31.2** (+13.5%) | - | 27.5 -> **31.2** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Individual spell undertuned (WR: 11.3%, Casts: 3525, mult: 1.158) |
| `FDL` | Blood | Debuff / Control | 17.9 -> **13.4** (-25.1%) | - | 17.9 -> **13.4** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Status 'Bleeding' appliers overtuned on own (WR: 80.2%) |
| `FDD` | Blood | Ultimate | 18.9 -> **15.3** (-19.0%) | 11.2 -> **15.2** | 230.6 -> **247.9** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.7% vs 16% floor, Casts: 450). Increasing spread: b -17.5%, n +36.0% |
| `DFF` | Blood | Conditional Strike | 9.2 -> **7.9** (-14.1%) | 13.2 -> **18.8** | 130.6 -> **156.4** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Status 'Bleeding' beneficiaries undertuned (WR: 32.5%) |
| `DFW` | Blood | Debuff / Control | 13.3 -> **10.3** (-22.6%) | - | 13.3 -> **10.3** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Status 'Bleeding' appliers overtuned on own (WR: 80.2%) |
| `DFE` | Blood | Buff / Sustain | 55.6 -> **62.8** (+12.9%) | - | 55.6 -> **62.8** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Individual spell undertuned (WR: 12.7%, Casts: 589, mult: 1.152) |
| `DFL` | Blood | Buff / Sustain | 27.0 -> **23.3** (-13.7%) | - | 27.0 -> **23.3** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Individual spell overtuned (WR: 79.7%, Casts: 678, mult: 0.882) |
| `DFD` | Blood | Conditional Strike | 49.9 -> **54.4** (+9.0%) | 0.4 -> **0.3** | 69.9 -> **70.7** | Class Blood overtuned (WR: 54.9%, factor: 0.981); Condition triggers excessively (N=1 conditions, Trigger Rate: 89.8% vs 55% ceiling, WR: 71.9%). Compressing spread: b +21.5%, n -29.1% |
| `WEF` | Plants | Conditional Strike | 8.2 -> **7.4** (-9.8%) | 12.8 -> **18.6** | 113.2 -> **145.0** | Location 'Jungle' beneficiaries undertuned (WR: 33.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 2501). Increasing spread: b -17.9%, n +36.8% |
| `WEW` | Plants | Debuff / Control | 35.3 -> **36.0** (+2.0%) | - | 35.3 -> **36.0** | Individual spell undertuned (WR: 44.0%, Casts: 220, mult: 1.020) |
| `WEE` | Plants | Setup - Location | 28.4 -> **36.9** (+29.9%) | - | 28.4 -> **36.9** | Location 'Jungle' appliers undertuned (WR: 11.2%, casts: 1280); Individual spell undertuned (WR: 11.2%, Casts: 1280, mult: 1.159) |
| `WEL` | Plants | Debuff / Control | 31.6 -> **30.2** (-4.4%) | - | 31.6 -> **30.2** | Status 'Entangled' appliers overtuned on own (WR: 56.3%); Individual spell overtuned (WR: 56.3%, Casts: 5228, mult: 0.978) |
| `WED` | Plants | Conditional Strike | 12.1 -> **13.2** (+9.1%) | 9.7 -> **9.1** | 129.5 -> **133.3** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1405, WR: 46.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 46.4%, Casts: 1405, mult: 1.012) |
| `EWF` | Plants | Buff / Sustain | 9.3 -> **7.7** (-17.2%) | 11.0 -> **14.9** | 111.6 -> **122.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.4% vs 30% floor, Casts: 9885). Increasing spread: b -17.0%, n +35.0% |
| `EWW` | Plants | Debuff / Control | 14.3 -> **11.8** (-17.5%) | - | 14.3 -> **11.8** | Individual spell overtuned (WR: 92.5%, Casts: 3621, mult: 0.824) |
| `EWL` | Plants | Debuff / Control | 49.0 -> **48.4** (-1.2%) | - | 49.0 -> **48.4** | Individual spell overtuned (WR: 53.9%, Casts: 142, mult: 0.987) |
| `EWD` | Plants | Conditional Strike | 4.5 -> **3.5** (-22.2%) | 14.1 -> **19.3** | 68.0 -> **71.0** | Status 'Bleeding' appliers overtuned on own (WR: 80.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 890). Increasing spread: b -18.0%, n +36.9% |
| `WLF` | Fey | Conditional Strike | 10.5 -> **9.2** (-12.4%) | 11.5 -> **16.6** | 131.2 -> **161.9** | Class Fey overtuned (WR: 53.9%, factor: 0.984); Status 'Cursed' beneficiaries undertuned (WR: 35.6%) |
| `WLW` | Fey | Debuff / Control | 38.7 -> **33.1** (-14.5%) | - | 38.7 -> **33.1** | Class Fey overtuned (WR: 53.9%, factor: 0.984); Status 'Cursed' appliers overtuned on own (WR: 64.6%) |
| `WLE` | Fey | Setup - Location | 46.4 -> **58.6** (+26.3%) | - | 46.4 -> **58.6** | Class Fey overtuned (WR: 53.9%, factor: 0.984); Location 'Enchanted Forest' appliers undertuned (WR: 14.4%, casts: 1103) |
| `WLL` | Fey | Direct Damage | 61.5 -> **56.9** (-7.5%) | - | 61.5 -> **56.9** | Class Fey overtuned (WR: 53.9%, factor: 0.984); Individual spell overtuned (WR: 65.9%, Casts: 794, mult: 0.941) |
| `WLD` | Fey | Ultimate | 23.6 -> **25.7** (+8.9%) | 11.9 -> **11.5** | 304.4 -> **321.2** | Class Fey overtuned (WR: 53.9%, factor: 0.984); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.5%) |
| `LWF` | Fey | Debuff / Control | 17.0 -> **14.1** (-17.1%) | 12.2 -> **16.9** | 224.4 -> **252.4** | Class Fey overtuned (WR: 53.9%, factor: 0.984); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.5%) |
| `LWW` | Fey | Debuff / Control | 55.3 -> **48.5** (-12.3%) | - | 55.3 -> **48.5** | Class Fey overtuned (WR: 53.9%, factor: 0.984); Individual spell overtuned (WR: 77.8%, Casts: 3559, mult: 0.890) |
| `LWL` | Fey | Debuff / Control | 48.6 -> **47.0** (-3.3%) | - | 48.6 -> **47.0** | Class Fey overtuned (WR: 53.9%, factor: 0.984); Individual spell overtuned (WR: 55.4%, Casts: 973, mult: 0.982) |
| `LWD` | Fey | Conditional Strike | 11.8 -> **8.6** (-27.1%) | 14.1 -> **19.3** | 178.2 -> **174.6** | Class Fey overtuned (WR: 53.9%, factor: 0.984); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 153). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 9.7 -> **9.0** (-7.2%) | 11.1 -> **16.2** | 117.4 -> **154.8** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Weather 'Raining' beneficiaries undertuned (WR: 31.8%) |
| `WDW` | Ice | Buff / Sustain | 17.6 -> **20.9** (+18.7%) | - | 17.6 -> **20.9** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Status 'Frosty' appliers undertuned (WR: 38.7%, casts: 6533) |
| `WDE` | Ice | Setup - Weather | 34.3 -> **39.6** (+15.5%) | - | 34.3 -> **39.6** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Individual spell undertuned (WR: 21.0%, Casts: 2993, mult: 1.115) |
| `WDL` | Ice | Debuff / Control | 45.9 -> **49.4** (+7.6%) | - | 45.9 -> **49.4** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Status 'Frosty' appliers undertuned (WR: 38.7%, casts: 6533) |
| `WDD` | Ice | Ultimate | 24.0 -> **19.4** (-19.2%) | 12.9 -> **15.8** | 333.6 -> **325.9** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Weather 'Blizzard' beneficiaries overtuned (WR: 63.6%) |
| `DWF` | Ice | Debuff / Control | 50.4 -> **50.9** (+1.0%) | - | 50.4 -> **50.9** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Status 'Frosty' appliers undertuned (WR: 38.7%, casts: 6533) |
| `DWW` | Ice | Debuff / Control | 38.0 -> **38.7** (+1.8%) | - | 38.0 -> **38.7** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Individual spell overtuned (WR: 55.2%, Casts: 6182, mult: 0.983) |
| `DWE` | Ice | Setup - Location | 23.3 -> **26.7** (+14.6%) | - | 23.3 -> **26.7** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Location 'Tundra' appliers undertuned (WR: 35.9%, casts: 695) |
| `DWL` | Ice | Debuff / Control | 51.2 -> **52.4** (+2.3%) | - | 51.2 -> **52.4** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Status 'Frosty' appliers undertuned (WR: 38.7%, casts: 6533) |
| `DWD` | Ice | Conditional Strike | 13.2 -> **12.6** (-4.5%) | 9.6 -> **14.1** | 139.9 -> **190.3** | Class Ice undertuned (WR: 41.0%, factor: 1.036); Status 'Frosty' beneficiaries undertuned (WR: 31.8%) |
| `ELF` | Wind | Conditional Strike | 15.8 -> **14.4** (-8.9%) | 13.7 -> **19.6** | 232.3 -> **296.6** | Class Wind undertuned (WR: 45.9%, factor: 1.016); Status 'Bleeding' beneficiaries undertuned (WR: 32.5%) |
| `ELW` | Wind | Debuff / Control | 34.2 -> **33.1** (-3.2%) | - | 34.2 -> **33.1** | Class Wind undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 63.1%, Casts: 1527, mult: 0.952) |
| `ELE` | Wind | Setup - Weather | 21.0 -> **24.4** (+16.2%) | - | 21.0 -> **24.4** | Class Wind undertuned (WR: 45.9%, factor: 1.016); Individual spell undertuned (WR: 14.4%, Casts: 1318, mult: 1.144) |
| `ELL` | Wind | Buff / Sustain | 43.7 -> **44.4** (+1.6%) | - | 43.7 -> **44.4** | Class Wind undertuned (WR: 45.9%, factor: 1.016) |
| `ELD` | Wind | Conditional Strike | 7.6 -> **6.7** (-11.8%) | 11.2 -> **16.3** | 92.7 -> **115.9** | Class Wind undertuned (WR: 45.9%, factor: 1.016); Weather 'Raining' beneficiaries undertuned (WR: 31.8%) |
| `LEF` | Wind | Conditional Strike | 9.2 -> **8.1** (-12.0%) | 12.2 -> **16.4** | 121.4 -> **140.9** | Class Wind undertuned (WR: 45.9%, factor: 1.016); Status 'Burning' beneficiaries overtuned (WR: 53.6%) |
| `LEW` | Wind | Debuff / Control | 49.5 -> **46.3** (-6.5%) | - | 49.5 -> **46.3** | Class Wind undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 70.7%, Casts: 7979, mult: 0.921) |
| `LEE` | Wind | Setup - Weather | 20.4 -> **19.9** (-2.5%) | - | 20.4 -> **19.9** | Class Wind undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 60.7%, Casts: 808, mult: 0.961) |
| `LEL` | Wind | Buff / Sustain | 42.4 -> **48.6** (+14.6%) | - | 42.4 -> **48.6** | Class Wind undertuned (WR: 45.9%, factor: 1.016); Individual spell undertuned (WR: 18.1%, Casts: 3757, mult: 1.128) |
| `EDF` | Poison | Conditional Strike | 10.1 -> **8.9** (-11.9%) | 12.6 -> **16.8** | 137.4 -> **158.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.1% vs 30% floor, Casts: 6888). Increasing spread: b -16.4%, n +33.6%; Individual spell undertuned (WR: 36.4%, Casts: 6888, mult: 1.050) |
| `EDW` | Poison | Debuff / Control | 22.0 -> **20.5** (-6.8%) | - | 22.0 -> **20.5** | Individual spell overtuned (WR: 67.9%, Casts: 593, mult: 0.932) |
| `EDE` | Poison | Setup - Location | 22.5 -> **26.7** (+18.7%) | - | 22.5 -> **26.7** | Location 'Swamp' appliers undertuned (WR: 25.7%, casts: 586); Individual spell undertuned (WR: 25.6%, Casts: 586, mult: 1.095) |
| `EDL` | Poison | Debuff / Control | 8.9 -> **7.3** (-18.0%) | - | 8.9 -> **7.3** | Individual spell overtuned (WR: 95.6%, Casts: 2044, mult: 0.820) |
| `EDD` | Poison | Ultimate | 20.3 -> **23.0** (+13.3%) | 13.5 -> **14.3** | 294.4 -> **351.9** | Status 'Bleeding' beneficiaries undertuned (WR: 32.5%); Location 'Swamp' beneficiaries undertuned (WR: 36.5%) |
| `DEF` | Poison | Conditional Strike | 29.0 -> **24.5** (-15.5%) | 2.2 -> **2.7** | 92.8 -> **90.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.9% vs 30% floor, Casts: 5755). Increasing spread: b -12.1%, n +24.6%; Individual spell overtuned (WR: 61.2%, Casts: 5755, mult: 0.960) |
| `DEW` | Poison | Debuff / Control | 23.0 -> **19.0** (-17.4%) | - | 23.0 -> **19.0** | Individual spell overtuned (WR: 92.0%, Casts: 1791, mult: 0.827) |
| `DEL` | Poison | Conditional Strike | 1.0 -> **0.8** (-20.0%) | 12.9 -> **18.9** | 13.9 -> **15.9** | Status 'Bleeding' beneficiaries undertuned (WR: 32.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 600). Increasing spread: b -17.9%, n +36.7% |
| `LDF` | Cosmic | Debuff / Control | 39.1 -> **37.9** (-3.1%) | - | 39.1 -> **37.9** | Individual spell overtuned (WR: 58.6%, Casts: 3885, mult: 0.970) |
| `LDW` | Cosmic | Debuff / Control | 32.7 -> **31.1** (-4.9%) | - | 32.7 -> **31.1** | Individual spell overtuned (WR: 63.1%, Casts: 3733, mult: 0.952) |
| `LDL` | Cosmic | Conditional Strike | 9.3 -> **7.7** (-17.2%) | 12.1 -> **16.4** | 121.8 -> **134.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1729). Increasing spread: b -17.2%, n +35.4% |
| `LDD` | Cosmic | Ultimate | 11.0 -> **12.6** (+14.5%) | 24.0 -> **22.6** | 275.0 -> **297.4** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1977, WR: 34.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 34.7%, Casts: 1977, mult: 1.057) |
| `DLF` | Cosmic | Conditional Strike | 11.1 -> **9.1** (-18.0%) | 12.7 -> **17.3** | 152.1 -> **166.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 1678). Increasing spread: b -17.8%, n +36.6% |
| `DLW` | Cosmic | Direct Damage | 50.5 -> **49.4** (-2.2%) | - | 50.5 -> **49.4** | Individual spell overtuned (WR: 56.6%, Casts: 2361, mult: 0.977) |
| `DLE` | Cosmic | Direct Damage | 41.6 -> **43.8** (+5.3%) | - | 41.6 -> **43.8** | Individual spell undertuned (WR: 35.7%, Casts: 1899, mult: 1.053) |
| `DLL` | Cosmic | Conditional Strike | 14.4 -> **11.9** (-17.4%) | 11.2 -> **15.2** | 175.7 -> **192.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 812). Increasing spread: b -17.4%, n +35.8% |
