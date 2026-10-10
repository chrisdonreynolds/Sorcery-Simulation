# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T14:31:22Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 60.4s  
**Total Spells Tuned:** 118 / 125  

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
| **Fire** | 12,814 | 65.5% | 65.5% | 17.3 | Overtuned ⚠️ |
| **Water** | 7,605 | 60.8% | 60.9% | 10.5 | Overtuned ⚠️ |
| **Dark** | 9,982 | 58.0% | 58.0% | 13.7 | Overtuned ⚠️ |
| **Poison** | 21,993 | 56.8% | 56.8% | 10.1 | Overtuned ⚠️ |
| **Lightning** | 21,559 | 55.3% | 55.3% | 9.5 | Overtuned ⚠️ |
| **Plants** | 22,014 | 54.9% | 54.9% | 5.3 | Overtuned ⚠️ |
| **Cosmic** | 26,655 | 54.9% | 54.9% | 14.9 | Overtuned ⚠️ |
| **Wind** | 21,065 | 51.9% | 51.9% | 10.8 | Balanced ✅ |
| **Light** | 12,010 | 50.0% | 50.0% | 2.3 | Balanced ✅ |
| **Ghostfire** | 26,152 | 49.6% | 49.6% | 9.3 | Balanced ✅ |
| **Earth** | 13,578 | 48.7% | 48.7% | 15.5 | Balanced ✅ |
| **Beasts** | 22,070 | 48.1% | 48.1% | 2.9 | Balanced ✅ |
| **Blood** | 25,356 | 46.6% | 46.6% | 9.1 | Balanced ✅ |
| **Fey** | 24,194 | 37.0% | 37.0% | 7.0 | Undertuned ⚠️ |
| **Ice** | 20,470 | 32.5% | 32.4% | 6.8 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,560 (45.4%) | 2,614 (50.6%) | 3.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,847 (25.2%) | 12,431 (41.6%) | 2.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 7,129 (75.9%) | 12,036 (48.1%) | 2.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 6,441 (73.1%) | 12,420 (35.7%) | 0.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,833 (65.5%) | 2,863 (57.2%) | 0.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,517 (59.7%) | 5,177 (40.0%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,653 (38.3%) | 1,229 (66.4%) | 2.9% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 49.1 -> **42.2** (-14.1%) | - | 49.1 -> **42.2** | Class Fire overtuned (WR: 65.5%, factor: 0.938); Individual spell overtuned (WR: 71.8%, Casts: 3099, mult: 0.916) |
| `FFW` | Fire | Debuff / Control | 39.4 -> **32.0** (-18.8%) | - | 39.4 -> **32.0** | Class Fire overtuned (WR: 65.5%, factor: 0.938); Status 'Burning' appliers overtuned on own (WR: 75.9%) |
| `FFE` | Fire | Debuff / Control | 32.7 -> **29.5** (-9.8%) | - | 32.7 -> **29.5** | Class Fire overtuned (WR: 65.5%, factor: 0.938); Individual spell overtuned (WR: 60.9%, Casts: 3788, mult: 0.961) |
| `FFL` | Fire | Debuff / Control | 5.5 -> **4.2** (-23.6%) | - | 5.5 -> **4.2** | Class Fire overtuned (WR: 65.5%, factor: 0.938); Status 'Burning' appliers overtuned on own (WR: 75.9%) |
| `FFD` | Fire | Conditional Strike | 11.8 -> **9.2** (-22.0%) | 8.8 -> **11.9** | 115.6 -> **118.7** | Class Fire overtuned (WR: 65.5%, factor: 0.938); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 1918). Increasing spread: b -17.1%, n +35.1% |
| `WWF` | Water | Conditional Strike | 15.5 -> **11.4** (-26.5%) | 7.7 -> **10.3** | 134.8 -> **128.8** | Class Water overtuned (WR: 60.8%, factor: 0.957); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.2% vs 30% floor, Casts: 2595). Increasing spread: b -16.3%, n +33.5% |
| `WWE` | Water | Setup - Weather | 23.2 -> **24.1** (+3.9%) | - | 23.2 -> **24.1** | Class Water overtuned (WR: 60.8%, factor: 0.957); Weather 'Raining' appliers undertuned (WR: 38.3%, casts: 1653) |
| `WWL` | Water | Buff / Sustain | 53.5 -> **49.0** (-8.4%) | - | 53.5 -> **49.0** | Class Water overtuned (WR: 60.8%, factor: 0.957); Individual spell overtuned (WR: 61.5%, Casts: 2491, mult: 0.958) |
| `WWD` | Water | Buff / Sustain | 38.0 -> **35.6** (-6.3%) | - | 38.0 -> **35.6** | Class Water overtuned (WR: 60.8%, factor: 0.957); Individual spell overtuned (WR: 56.0%, Casts: 445, mult: 0.980) |
| `EEF` | Earth | Conditional Strike | 14.3 -> **10.9** (-23.8%) | 8.0 -> **10.9** | 128.7 -> **129.7** | Status 'Stunned' appliers overtuned on own (WR: 65.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 1209). Increasing spread: b -17.4%, n +35.8% |
| `EEW` | Earth | Buff / Sustain | 45.3 -> **48.2** (+6.4%) | - | 45.3 -> **48.2** | Individual spell undertuned (WR: 33.0%, Casts: 2763, mult: 1.064) |
| `EEE` | Earth | Conditional Strike | 7.2 -> **8.1** (+12.5%) | 1.5 -> **1.5** | 18.0 -> **20.2** | Condition triggers excessively (N=1 conditions, Trigger Rate: 94.6% vs 55% ceiling, WR: 70.2%). Compressing spread: b +21.9%, n -30.1%; Individual spell overtuned (WR: 70.2%, Casts: 3772, mult: 0.923) |
| `EED` | Earth | Direct Damage | 6.2 -> **5.8** (-6.5%) | - | 6.2 -> **5.8** | Individual spell overtuned (WR: 68.7%, Casts: 1781, mult: 0.929) |
| `LLF` | Light | Conditional Strike | 1.9 -> **1.5** (-21.1%) | 9.4 -> **12.8** | 19.8 -> **20.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 3938). Increasing spread: b -17.8%, n +36.6%; Individual spell overtuned (WR: 66.7%, Casts: 3938, mult: 0.937) |
| `LLW` | Light | Debuff / Control | 25.0 -> **23.8** (-4.8%) | - | 25.0 -> **23.8** | Individual spell overtuned (WR: 63.2%, Casts: 763, mult: 0.951) |
| `LLE` | Light | Setup - Weather | 32.1 -> **38.3** (+19.3%) | - | 32.1 -> **38.3** | Weather 'Sunny' appliers undertuned (WR: 25.2%, casts: 2847); Individual spell undertuned (WR: 25.2%, Casts: 2847, mult: 1.097) |
| `LLL` | Light | Buff / Sustain | 29.7 -> **25.9** (-12.8%) | - | 29.7 -> **25.9** | Individual spell overtuned (WR: 82.0%, Casts: 1303, mult: 0.871) |
| `LLD` | Light | Ultimate | 13.8 -> **15.7** (+13.8%) | 16.4 -> **15.9** | 240.1 -> **265.3** | Weather 'Sunny' beneficiaries undertuned (WR: 41.6%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 3159, WR: 34.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 9.9 -> **7.8** (-21.2%) | 10.3 -> **14.1** | 111.9 -> **117.8** | Class Dark overtuned (WR: 58.0%, factor: 0.968); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 875). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 46.8 -> **44.2** (-5.6%) | - | 46.8 -> **44.2** | Class Dark overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 57.0%, Casts: 5344, mult: 0.976) |
| `DDE` | Dark | Setup - Weather | 29.1 -> **31.2** (+7.2%) | - | 29.1 -> **31.2** | Class Dark overtuned (WR: 58.0%, factor: 0.968); Weather 'Darkness' appliers undertuned (WR: 35.5%, casts: 1468) |
| `DDL` | Dark | Debuff / Control | 23.2 -> **22.0** (-5.2%) | - | 23.2 -> **22.0** | Class Dark overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 56.1%, Casts: 118, mult: 0.979) |
| `DDD` | Dark | Debuff / Control | 25.7 -> **22.2** (-13.6%) | - | 25.7 -> **22.2** | Class Dark overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 77.1%, Casts: 2177, mult: 0.893) |
| `FWF` | Ghostfire | Debuff / Control | 27.7 -> **22.1** (-20.2%) | - | 27.7 -> **22.1** | Status 'Burning' appliers overtuned on own (WR: 75.9%); Individual spell overtuned (WR: 80.7%, Casts: 3120, mult: 0.877) |
| `FWW` | Ghostfire | Debuff / Control | 13.9 -> **14.3** (+2.9%) | - | 13.9 -> **14.3** | Status 'Cursed' appliers overtuned on own (WR: 61.0%); Individual spell undertuned (WR: 31.7%, Casts: 612, mult: 1.069) |
| `FWE` | Ghostfire | Setup - Location | 28.9 -> **31.1** (+7.6%) | - | 28.9 -> **31.1** | Location 'Graveyard' appliers undertuned (WR: 39.4%, casts: 532); Individual spell undertuned (WR: 39.3%, Casts: 532, mult: 1.038) |
| `FWL` | Ghostfire | Debuff / Control | 40.6 -> **37.9** (-6.7%) | - | 40.6 -> **37.9** | Status 'Cursed' appliers overtuned on own (WR: 61.0%); Individual spell overtuned (WR: 58.2%, Casts: 4890, mult: 0.971) |
| `FWD` | Ghostfire | Ultimate | 17.2 -> **13.8** (-19.8%) | 11.4 -> **15.7** | 213.3 -> **230.5** | Status 'Cursed' beneficiaries undertuned (WR: 43.5%); Location 'Graveyard' beneficiaries overtuned (WR: 55.5%) |
| `WFF` | Ghostfire | Conditional Strike | 9.7 -> **8.7** (-10.3%) | 9.7 -> **14.0** | 103.8 -> **130.5** | Status 'Bleeding' beneficiaries undertuned (WR: 35.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 7573). Increasing spread: b -18.0%, n +37.0% |
| `WFW` | Ghostfire | Debuff / Control | 27.1 -> **25.3** (-6.6%) | - | 27.1 -> **25.3** | Individual spell overtuned (WR: 67.7%, Casts: 675, mult: 0.933) |
| `WFE` | Ghostfire | Debuff / Control | 20.0 -> **16.2** (-19.0%) | - | 20.0 -> **16.2** | Status 'Bleeding' appliers overtuned on own (WR: 73.1%); Individual spell overtuned (WR: 79.9%, Casts: 2568, mult: 0.881) |
| `WFL` | Ghostfire | Buff / Sustain | 33.7 -> **34.2** (+1.5%) | - | 33.7 -> **34.2** | Individual spell undertuned (WR: 45.8%, Casts: 1406, mult: 1.014) |
| `WFD` | Ghostfire | Conditional Strike | 10.0 -> **8.7** (-13.0%) | 9.1 -> **12.3** | 101.0 -> **115.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.0% vs 30% floor, Casts: 3414). Increasing spread: b -17.2%, n +35.3%; Individual spell undertuned (WR: 37.5%, Casts: 3414, mult: 1.046) |
| `FEF` | Beasts | Debuff / Control | 21.0 -> **19.4** (-7.6%) | - | 21.0 -> **19.4** | Individual spell overtuned (WR: 69.4%, Casts: 693, mult: 0.926) |
| `FEW` | Beasts | Conditional Strike | 10.7 -> **8.5** (-20.6%) | 10.4 -> **14.8** | 122.0 -> **134.3** | Status 'Entangled' beneficiaries undertuned (WR: 40.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 492). Increasing spread: b -17.9%, n +36.8% |
| `FEE` | Beasts | Buff / Sustain | 24.5 -> **23.2** (-5.3%) | - | 24.5 -> **23.2** | Individual spell overtuned (WR: 64.1%, Casts: 1259, mult: 0.948) |
| `FEL` | Beasts | Buff / Sustain | 28.2 -> **31.6** (+12.1%) | - | 28.2 -> **31.6** | Individual spell undertuned (WR: 20.1%, Casts: 5513, mult: 1.119) |
| `FED` | Beasts | Conditional Strike | 5.8 -> **5.1** (-12.1%) | 1.6 -> **2.0** | 15.1 -> **15.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.8% vs 30% floor, Casts: 2662). Increasing spread: b -12.1%, n +24.7% |
| `EFF` | Beasts | Debuff / Control | 11.8 -> **10.2** (-13.6%) | 9.8 -> **13.4** | 127.4 -> **146.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 2285). Increasing spread: b -17.7%, n +36.3%; Individual spell undertuned (WR: 35.3%, Casts: 2285, mult: 1.055) |
| `EFW` | Beasts | Buff / Sustain | 25.2 -> **25.9** (+2.8%) | - | 25.2 -> **25.9** | Individual spell undertuned (WR: 42.4%, Casts: 460, mult: 1.027) |
| `EFL` | Beasts | Buff / Sustain | 14.4 -> **12.0** (-16.7%) | - | 14.4 -> **12.0** | Individual spell overtuned (WR: 91.2%, Casts: 4032, mult: 0.830) |
| `EFD` | Beasts | Ultimate | 13.4 -> **15.1** (+12.7%) | 18.4 -> **18.6** | 260.0 -> **296.0** | Status 'Entangled' beneficiaries undertuned (WR: 40.0%); Location 'Jungle' beneficiaries undertuned (WR: 42.1%) |
| `FLF` | Lightning | Conditional Strike | 9.0 -> **7.3** (-18.9%) | 10.1 -> **13.3** | 99.9 -> **104.4** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Status 'Stunned' beneficiaries overtuned (WR: 57.2%) |
| `FLW` | Lightning | Debuff / Control | 37.6 -> **34.8** (-7.4%) | - | 37.6 -> **34.8** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Status 'Stunned' appliers overtuned on own (WR: 65.5%) |
| `FLE` | Lightning | Setup - Weather | 22.5 -> **26.5** (+17.8%) | - | 22.5 -> **26.5** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Weather 'Storming' appliers undertuned (WR: 24.0%, casts: 2357) |
| `FLL` | Lightning | Buff / Sustain | 24.9 -> **26.3** (+5.6%) | - | 24.9 -> **26.3** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Individual spell undertuned (WR: 29.3%, Casts: 697, mult: 1.079) |
| `FLD` | Lightning | Ultimate | 18.5 -> **14.2** (-23.2%) | 12.7 -> **16.1** | 253.4 -> **242.8** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Status 'Stunned' beneficiaries overtuned (WR: 57.2%) |
| `LFF` | Lightning | Conditional Strike | 9.3 -> **7.5** (-19.4%) | 9.8 -> **13.4** | 100.4 -> **108.0** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 3483). Increasing spread: b -17.9%, n +36.9% |
| `LFW` | Lightning | Buff / Sustain | 31.6 -> **28.9** (-8.5%) | - | 31.6 -> **28.9** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Individual spell overtuned (WR: 67.0%, Casts: 952, mult: 0.936) |
| `LFE` | Lightning | Debuff / Control | 37.0 -> **31.4** (-15.1%) | - | 37.0 -> **31.4** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Status 'Stunned' appliers overtuned on own (WR: 65.5%) |
| `LFL` | Lightning | Debuff / Control | 17.7 -> **15.5** (-12.4%) | 8.0 -> **10.5** | 159.3 -> **178.2** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Weather 'Darkness' beneficiaries undertuned (WR: 43.8%) |
| `LFD` | Lightning | Conditional Strike | 10.0 -> **7.6** (-24.0%) | 14.3 -> **19.4** | 153.0 -> **155.0** | Class Lightning overtuned (WR: 55.3%, factor: 0.979); Status 'Stunned' appliers overtuned on own (WR: 65.5%) |
| `FDF` | Blood | Conditional Strike | 10.0 -> **9.2** (-8.0%) | 10.3 -> **14.1** | 113.0 -> **138.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1535). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 20.5%, Casts: 1535, mult: 1.118) |
| `FDW` | Blood | Direct Damage | 66.2 -> **71.4** (+7.9%) | - | 66.2 -> **71.4** | Individual spell undertuned (WR: 29.5%, Casts: 154, mult: 1.079) |
| `FDE` | Blood | Setup - Weather | 24.3 -> **27.5** (+13.2%) | - | 24.3 -> **27.5** | Individual spell undertuned (WR: 17.4%, Casts: 1388, mult: 1.131) |
| `FDL` | Blood | Debuff / Control | 22.0 -> **17.9** (-18.6%) | - | 22.0 -> **17.9** | Status 'Bleeding' appliers overtuned on own (WR: 73.1%); Individual spell overtuned (WR: 79.3%, Casts: 2235, mult: 0.884) |
| `FDD` | Blood | Ultimate | 17.1 -> **18.9** (+10.5%) | 11.6 -> **11.2** | 215.5 -> **230.6** | Weather 'Darkness' beneficiaries undertuned (WR: 43.8%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 5296, WR: 43.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 11.1 -> **9.2** (-17.1%) | 9.3 -> **13.2** | 114.3 -> **130.6** | Status 'Bleeding' beneficiaries undertuned (WR: 35.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 1842). Increasing spread: b -16.8%, n +34.5% |
| `DFW` | Blood | Debuff / Control | 16.2 -> **13.3** (-17.9%) | - | 16.2 -> **13.3** | Status 'Bleeding' appliers overtuned on own (WR: 73.1%); Individual spell overtuned (WR: 76.3%, Casts: 698, mult: 0.896) |
| `DFE` | Blood | Buff / Sustain | 47.5 -> **55.6** (+17.1%) | - | 47.5 -> **55.6** | Individual spell undertuned (WR: 8.5%, Casts: 4722, mult: 1.171) |
| `DFL` | Blood | Buff / Sustain | 29.1 -> **27.0** (-7.2%) | - | 29.1 -> **27.0** | Individual spell overtuned (WR: 69.3%, Casts: 3665, mult: 0.926) |
| `DFD` | Blood | Conditional Strike | 45.4 -> **49.9** (+9.9%) | 0.5 -> **0.4** | 68.1 -> **69.9** | Condition triggers excessively (N=1 conditions, Trigger Rate: 83.5% vs 55% ceiling, WR: 71.8%). Compressing spread: b +20.1%, n -26.9%; Individual spell overtuned (WR: 71.8%, Casts: 3821, mult: 0.916) |
| `WEF` | Plants | Conditional Strike | 10.6 -> **8.2** (-22.6%) | 9.1 -> **12.8** | 107.1 -> **113.2** | Class Plants overtuned (WR: 54.9%, factor: 0.980); Location 'Jungle' beneficiaries undertuned (WR: 42.1%) |
| `WEW` | Plants | Debuff / Control | 36.0 -> **35.3** (-1.9%) | - | 36.0 -> **35.3** | Class Plants overtuned (WR: 54.9%, factor: 0.980) |
| `WEE` | Plants | Setup - Location | 23.2 -> **28.4** (+22.4%) | - | 23.2 -> **28.4** | Class Plants overtuned (WR: 54.9%, factor: 0.980); Location 'Jungle' appliers undertuned (WR: 18.6%, casts: 1074) |
| `WEL` | Plants | Debuff / Control | 34.6 -> **31.6** (-8.7%) | - | 34.6 -> **31.6** | Class Plants overtuned (WR: 54.9%, factor: 0.980); Status 'Entangled' appliers overtuned on own (WR: 59.7%) |
| `WED` | Plants | Conditional Strike | 11.2 -> **12.1** (+8.0%) | 10.3 -> **9.7** | 126.6 -> **129.5** | Class Plants overtuned (WR: 54.9%, factor: 0.980); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 638, WR: 44.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 11.2 -> **9.3** (-17.0%) | 7.9 -> **11.0** | 99.7 -> **111.6** | Class Plants overtuned (WR: 54.9%, factor: 0.980); Weather 'Sunny' beneficiaries undertuned (WR: 41.6%) |
| `EWW` | Plants | Debuff / Control | 17.7 -> **14.3** (-19.2%) | - | 17.7 -> **14.3** | Class Plants overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 92.2%, Casts: 3677, mult: 0.826) |
| `EWL` | Plants | Debuff / Control | 51.1 -> **49.0** (-4.1%) | - | 51.1 -> **49.0** | Class Plants overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 56.6%, Casts: 751, mult: 0.977) |
| `EWD` | Plants | Conditional Strike | 5.8 -> **4.5** (-22.4%) | 9.9 -> **14.1** | 63.2 -> **68.0** | Class Plants overtuned (WR: 54.9%, factor: 0.980); Status 'Bleeding' appliers overtuned on own (WR: 73.1%) |
| `WLF` | Fey | Conditional Strike | 11.0 -> **10.5** (-4.5%) | 8.5 -> **11.5** | 104.5 -> **131.2** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Status 'Cursed' beneficiaries undertuned (WR: 43.5%) |
| `WLW` | Fey | Debuff / Control | 41.4 -> **38.7** (-6.5%) | - | 41.4 -> **38.7** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Status 'Cursed' appliers overtuned on own (WR: 61.0%) |
| `WLE` | Fey | Setup - Location | 34.2 -> **46.4** (+35.7%) | - | 34.2 -> **46.4** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Location 'Enchanted Forest' appliers undertuned (WR: 12.9%, casts: 2671) |
| `WLL` | Fey | Direct Damage | 61.2 -> **61.5** (+0.5%) | - | 61.2 -> **61.5** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Individual spell overtuned (WR: 62.1%, Casts: 1268, mult: 0.956) |
| `WLD` | Fey | Ultimate | 19.9 -> **23.6** (+18.6%) | 11.9 -> **11.9** | 256.7 -> **304.4** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Weather 'Darkness' beneficiaries undertuned (WR: 43.8%) |
| `LWF` | Fey | Debuff / Control | 19.6 -> **17.0** (-13.3%) | 8.6 -> **12.2** | 188.2 -> **224.4** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Location 'Enchanted Forest' beneficiaries undertuned (WR: 39.4%) |
| `LWW` | Fey | Debuff / Control | 47.2 -> **55.3** (+17.2%) | - | 47.2 -> **55.3** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Individual spell undertuned (WR: 21.4%, Casts: 4778, mult: 1.113) |
| `LWL` | Fey | Debuff / Control | 42.6 -> **48.6** (+14.1%) | - | 42.6 -> **48.6** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Individual spell undertuned (WR: 28.2%, Casts: 1474, mult: 1.084) |
| `LWD` | Fey | Conditional Strike | 12.6 -> **11.8** (-6.3%) | 10.3 -> **14.1** | 142.4 -> **178.2** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3910). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 11.4 -> **9.7** (-14.9%) | 9.0 -> **11.1** | 114.0 -> **117.4** | Class Ice undertuned (WR: 32.5%, factor: 1.070); Status 'Stunned' appliers overtuned on own (WR: 65.5%) |
| `WDW` | Ice | Buff / Sustain | 15.5 -> **17.6** (+13.5%) | - | 15.5 -> **17.6** | Class Ice undertuned (WR: 32.5%, factor: 1.070); Status 'Frosty' appliers undertuned (WR: 45.4%, casts: 6560) |
| `WDE` | Ice | Setup - Weather | 27.2 -> **34.3** (+26.1%) | - | 27.2 -> **34.3** | Class Ice undertuned (WR: 32.5%, factor: 1.070); Individual spell undertuned (WR: 6.6%, Casts: 7311, mult: 1.180) |
| `WDL` | Ice | Debuff / Control | 44.7 -> **45.9** (+2.7%) | - | 44.7 -> **45.9** | Class Ice undertuned (WR: 32.5%, factor: 1.070); Status 'Frosty' appliers undertuned (WR: 45.4%, casts: 6560) |
| `WDD` | Ice | Ultimate | 27.3 -> **24.0** (-12.1%) | 9.4 -> **12.9** | 283.9 -> **333.6** | Class Ice undertuned (WR: 32.5%, factor: 1.070); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1644). Increasing spread: b -18.0%, n +36.9% |
| `DWF` | Ice | Debuff / Control | 45.2 -> **50.4** (+11.5%) | - | 45.2 -> **50.4** | Class Ice undertuned (WR: 32.5%, factor: 1.070); Status 'Frosty' appliers undertuned (WR: 45.4%, casts: 6560) |
| `DWW` | Ice | Debuff / Control | 35.5 -> **38.0** (+7.0%) | - | 35.5 -> **38.0** | Class Ice undertuned (WR: 32.5%, factor: 1.070) |
| `DWE` | Ice | Setup - Location | 23.2 -> **23.3** (+0.4%) | - | 23.2 -> **23.3** | Class Ice undertuned (WR: 32.5%, factor: 1.070); Location 'Tundra' appliers overtuned on own (WR: 59.1%) |
| `DWL` | Ice | Debuff / Control | 48.2 -> **51.2** (+6.2%) | - | 48.2 -> **51.2** | Class Ice undertuned (WR: 32.5%, factor: 1.070); Status 'Frosty' appliers undertuned (WR: 45.4%, casts: 6560) |
| `DWD` | Ice | Conditional Strike | 14.5 -> **13.2** (-9.0%) | 7.2 -> **9.6** | 118.9 -> **139.9** | Class Ice undertuned (WR: 32.5%, factor: 1.070); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.1% vs 30% floor, Casts: 1405). Increasing spread: b -16.0%, n +32.7% |
| `ELF` | Wind | Conditional Strike | 20.2 -> **15.8** (-21.8%) | 9.5 -> **13.7** | 212.1 -> **232.3** | Status 'Bleeding' beneficiaries undertuned (WR: 35.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 271). Increasing spread: b -17.7%, n +36.4% |
| `ELW` | Wind | Debuff / Control | 34.9 -> **34.2** (-2.0%) | - | 34.9 -> **34.2** | Individual spell overtuned (WR: 55.9%, Casts: 4097, mult: 0.980) |
| `ELE` | Wind | Setup - Weather | 19.4 -> **21.0** (+8.2%) | - | 19.4 -> **21.0** | Individual spell undertuned (WR: 28.6%, Casts: 843, mult: 1.082) |
| `ELL` | Wind | Buff / Sustain | 42.0 -> **43.7** (+4.0%) | - | 42.0 -> **43.7** | Individual spell undertuned (WR: 38.6%, Casts: 247, mult: 1.041) |
| `ELD` | Wind | Conditional Strike | 11.1 -> **7.6** (-31.5%) | 8.8 -> **11.2** | 108.8 -> **92.7** | Weather 'Raining' beneficiaries overtuned (WR: 66.4%); Weather 'Blizzard' appliers overtuned on own (WR: 74.6%) |
| `LEF` | Wind | Conditional Strike | 10.8 -> **9.2** (-14.8%) | 9.0 -> **12.2** | 108.0 -> **121.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 7523). Increasing spread: b -17.4%, n +35.7%; Individual spell undertuned (WR: 39.8%, Casts: 7523, mult: 1.037) |
| `LEW` | Wind | Debuff / Control | 53.7 -> **49.5** (-7.8%) | - | 53.7 -> **49.5** | Individual spell overtuned (WR: 70.6%, Casts: 4150, mult: 0.921) |
| `LEE` | Wind | Setup - Weather | 21.1 -> **20.4** (-3.3%) | - | 21.1 -> **20.4** | Individual spell overtuned (WR: 58.8%, Casts: 1659, mult: 0.969) |
| `EDF` | Poison | Conditional Strike | 11.4 -> **10.1** (-11.4%) | 9.3 -> **12.6** | 117.4 -> **137.4** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.7% vs 30% floor, Casts: 6104). Increasing spread: b -17.3%, n +35.6% |
| `EDW` | Poison | Debuff / Control | 26.1 -> **22.0** (-15.7%) | - | 26.1 -> **22.0** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Individual spell overtuned (WR: 83.2%, Casts: 2674, mult: 0.866) |
| `EDE` | Poison | Setup - Location | 21.2 -> **22.5** (+6.1%) | - | 21.2 -> **22.5** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Location 'Swamp' appliers undertuned (WR: 37.9%, casts: 150) |
| `EDL` | Poison | Debuff / Control | 11.1 -> **8.9** (-19.8%) | - | 11.1 -> **8.9** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Individual spell overtuned (WR: 94.5%, Casts: 2347, mult: 0.820) |
| `EDD` | Poison | Ultimate | 19.3 -> **20.3** (+5.2%) | 13.6 -> **13.5** | 281.8 -> **294.4** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Status 'Bleeding' beneficiaries undertuned (WR: 35.7%) |
| `DEF` | Poison | Conditional Strike | 29.8 -> **29.0** (-2.7%) | 2.2 -> **2.2** | 95.4 -> **92.8** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 52.7% within [30%-55%] target window, WR: 52.7%). |
| `DEW` | Poison | Debuff / Control | 26.5 -> **23.0** (-13.2%) | - | 26.5 -> **23.0** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Individual spell overtuned (WR: 77.5%, Casts: 3340, mult: 0.891) |
| `DEE` | Poison | Debuff / Control | 22.8 -> **21.8** (-4.4%) | - | 22.8 -> **21.8** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Individual spell overtuned (WR: 55.2%, Casts: 1503, mult: 0.982) |
| `DEL` | Poison | Conditional Strike | 1.3 -> **1.0** (-23.1%) | 9.3 -> **12.9** | 13.4 -> **13.9** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Status 'Bleeding' beneficiaries undertuned (WR: 35.7%) |
| `DED` | Poison | Debuff / Control | 26.9 -> **25.8** (-4.1%) | - | 26.9 -> **25.8** | Class Poison overtuned (WR: 56.8%, factor: 0.973); Individual spell overtuned (WR: 54.1%, Casts: 2665, mult: 0.986) |
| `LDF` | Cosmic | Debuff / Control | 41.4 -> **39.1** (-5.6%) | - | 41.4 -> **39.1** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 60.5%, Casts: 4567, mult: 0.962) |
| `LDW` | Cosmic | Debuff / Control | 40.0 -> **32.7** (-18.2%) | - | 40.0 -> **32.7** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Status 'Stunned' appliers overtuned on own (WR: 65.5%) |
| `LDE` | Cosmic | Setup - Location | 18.8 -> **20.7** (+10.1%) | - | 18.8 -> **20.7** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Individual spell undertuned (WR: 19.1%, Casts: 266, mult: 1.124) |
| `LDL` | Cosmic | Conditional Strike | 11.7 -> **9.3** (-20.5%) | 8.9 -> **12.1** | 115.8 -> **121.8** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.4% vs 30% floor, Casts: 2872). Increasing spread: b -17.5%, n +35.9% |
| `LDD` | Cosmic | Ultimate | 13.7 -> **11.0** (-19.7%) | 17.5 -> **24.0** | 253.4 -> **275.0** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 3740). Increasing spread: b -18.0%, n +37.0% |
| `DLF` | Cosmic | Conditional Strike | 12.9 -> **11.1** (-14.0%) | 9.3 -> **12.7** | 132.9 -> **152.1** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 3912). Increasing spread: b -17.9%, n +36.9% |
| `DLW` | Cosmic | Direct Damage | 53.9 -> **50.5** (-6.3%) | - | 53.9 -> **50.5** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 62.2%, Casts: 2550, mult: 0.956) |
| `DLE` | Cosmic | Direct Damage | 41.2 -> **41.6** (+1.0%) | - | 41.2 -> **41.6** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Individual spell undertuned (WR: 41.7%, Casts: 1062, mult: 1.029) |
| `DLL` | Cosmic | Conditional Strike | 17.7 -> **14.4** (-18.6%) | 8.1 -> **11.2** | 161.1 -> **175.7** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Weather 'Darkness' beneficiaries undertuned (WR: 43.8%) |
| `DLD` | Cosmic | Conditional Strike | 56.3 -> **60.0** (+6.6%) | 1.5 -> **1.5** | 140.8 -> **150.0** | Class Cosmic overtuned (WR: 54.9%, factor: 0.980); Condition triggers excessively (N=1 conditions, Trigger Rate: 92.1% vs 55% ceiling, WR: 68.1%). Compressing spread: b +20.5%, n -28.4% |
