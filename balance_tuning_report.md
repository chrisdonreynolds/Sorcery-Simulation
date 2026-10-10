# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T17:31:25Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 62.8s  
**Total Spells Tuned:** 112 / 125  

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
| **Lightning** | 22,646 | 60.7% | 60.7% | 3.6 | Overtuned ⚠️ |
| **Fire** | 22,599 | 57.3% | 57.3% | 5.2 | Overtuned ⚠️ |
| **Ghostfire** | 27,904 | 56.0% | 56.0% | 2.3 | Overtuned ⚠️ |
| **Ice** | 54,289 | 54.2% | 54.2% | 7.1 | Overtuned ⚠️ |
| **Beasts** | 23,575 | 53.7% | 53.7% | 4.7 | Overtuned ⚠️ |
| **Water** | 10,182 | 53.3% | 53.3% | 6.5 | Balanced ✅ |
| **Cosmic** | 36,420 | 52.5% | 52.5% | 8.2 | Balanced ✅ |
| **Fey** | 14,012 | 51.5% | 51.5% | 5.2 | Balanced ✅ |
| **Blood** | 23,699 | 51.1% | 51.1% | 7.1 | Balanced ✅ |
| **Wind** | 29,187 | 48.6% | 48.6% | 3.5 | Balanced ✅ |
| **Dark** | 8,089 | 47.4% | 47.4% | 7.7 | Balanced ✅ |
| **Poison** | 29,241 | 43.8% | 43.8% | 2.3 | Undertuned ⚠️ |
| **Earth** | 10,249 | 42.8% | 42.8% | 7.4 | Undertuned ⚠️ |
| **Plants** | 24,604 | 39.7% | 39.7% | 2.8 | Undertuned ⚠️ |
| **Light** | 16,009 | 31.2% | 31.1% | 2.0 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 27,411 (68.2%) | 11,206 (37.3%) | 3.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 7,342 (13.1%) | 10,257 (19.7%) | 2.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 11,351 (80.3%) | 17,354 (37.5%) | 0.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 6,362 (78.9%) | 22,948 (26.0%) | 0.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 22,152 (57.6%) | 3,791 (61.2%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,441 (65.2%) | 4,610 (56.1%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 625 (12.4%) | 3,548 (34.0%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 18.3 -> **19.1** (+4.4%) | - | 18.3 -> **19.1** | Class Fire overtuned (WR: 57.3%, factor: 0.971); Individual spell undertuned (WR: 31.0%, Casts: 59, mult: 1.072) |
| `FFW` | Fire | Debuff / Control | 11.3 -> **9.7** (-14.2%) | - | 11.3 -> **9.7** | Class Fire overtuned (WR: 57.3%, factor: 0.971); Status 'Burning' appliers overtuned on own (WR: 80.3%) |
| `FFE` | Fire | Debuff / Control | 11.2 -> **10.2** (-8.9%) | - | 11.2 -> **10.2** | Class Fire overtuned (WR: 57.3%, factor: 0.971); Individual spell overtuned (WR: 66.4%, Casts: 9834, mult: 0.939) |
| `FFL` | Fire | Debuff / Control | 0.7 -> **0.5** (-28.6%) | - | 0.7 -> **0.5** | Class Fire overtuned (WR: 57.3%, factor: 0.971); Status 'Burning' appliers overtuned on own (WR: 80.3%) |
| `FFD` | Fire | Conditional Strike | 1.7 -> **1.4** (-17.6%) | 511.5 -> **735.3** | 871.2 -> **1030.8** | Class Fire overtuned (WR: 57.3%, factor: 0.971); Status 'Burning' beneficiaries undertuned (WR: 37.5%) |
| `WWF` | Water | Conditional Strike | 1.9 -> **1.6** (-15.8%) | 368.8 -> **513.0** | 702.6 -> **822.4** | Status 'Burning' beneficiaries undertuned (WR: 37.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 1412). Increasing spread: b -15.8%, n +32.5% |
| `WWE` | Water | Setup - Weather | 231.0 -> **298.6** (+29.3%) | - | 231.0 -> **298.6** | Weather 'Raining' appliers undertuned (WR: 12.4%, casts: 625); Individual spell undertuned (WR: 12.2%, Casts: 625, mult: 1.154) |
| `WWL` | Water | Buff / Sustain | 24.2 -> **22.0** (-9.1%) | - | 24.2 -> **22.0** | Individual spell overtuned (WR: 72.9%, Casts: 4334, mult: 0.911) |
| `WWD` | Water | Buff / Sustain | 33.1 -> **30.7** (-7.3%) | - | 33.1 -> **30.7** | Individual spell overtuned (WR: 68.8%, Casts: 774, mult: 0.928) |
| `EEF` | Earth | Conditional Strike | 2.8 -> **2.5** (-10.7%) | 590.4 -> **838.1** | 1655.9 -> **2097.8** | Class Earth undertuned (WR: 42.8%, factor: 1.029); Status 'Frosty' beneficiaries undertuned (WR: 37.3%) |
| `EEW` | Earth | Buff / Sustain | 41.1 -> **45.6** (+10.9%) | - | 41.1 -> **45.6** | Class Earth undertuned (WR: 42.8%, factor: 1.029); Individual spell undertuned (WR: 29.4%, Casts: 287, mult: 1.079) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 351.3 -> **479.3** | 35.2 -> **48.0** | Class Light undertuned (WR: 31.2%, factor: 1.075); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 2859). Increasing spread: b -17.7%, n +36.4% |
| `LLW` | Light | Debuff / Control | 16.3 -> **16.6** (+1.8%) | - | 16.3 -> **16.6** | Class Light undertuned (WR: 31.2%, factor: 1.075); Individual spell overtuned (WR: 63.8%, Casts: 3443, mult: 0.949) |
| `LLE` | Light | Setup - Weather | 220.3 -> **305.2** (+38.5%) | - | 220.3 -> **305.2** | Class Light undertuned (WR: 31.2%, factor: 1.075); Weather 'Sunny' appliers undertuned (WR: 13.1%, casts: 7342) |
| `LLL` | Light | Buff / Sustain | 8.9 -> **9.9** (+11.2%) | - | 8.9 -> **9.9** | Class Light undertuned (WR: 31.2%, factor: 1.075); Individual spell undertuned (WR: 41.2%, Casts: 1543, mult: 1.031) |
| `LLD` | Light | Ultimate | 10.4 -> **12.7** (+22.1%) | 90.7 -> **95.6** | 953.7 -> **1226.8** | Class Light undertuned (WR: 31.2%, factor: 1.075); Weather 'Sunny' beneficiaries undertuned (WR: 19.7%) |
| `DDF` | Dark | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 449.8 -> **616.2** | 360.6 -> **432.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4462). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 32.1%, Casts: 4462, mult: 1.068) |
| `DDW` | Dark | Debuff / Control | 20.5 -> **18.6** (-9.3%) | - | 20.5 -> **18.6** | Individual spell overtuned (WR: 74.2%, Casts: 2821, mult: 0.905) |
| `DDE` | Dark | Setup - Weather | 161.2 -> **207.3** (+28.6%) | - | 161.2 -> **207.3** | Weather 'Darkness' appliers undertuned (WR: 14.0%, casts: 232); Individual spell undertuned (WR: 13.5%, Casts: 232, mult: 1.148) |
| `DDL` | Dark | Debuff / Control | 13.9 -> **13.5** (-2.9%) | - | 13.9 -> **13.5** | Individual spell overtuned (WR: 59.6%, Casts: 35, mult: 0.972) |
| `FWF` | Ghostfire | Debuff / Control | 1.9 -> **1.4** (-26.3%) | - | 1.9 -> **1.4** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Status 'Burning' appliers overtuned on own (WR: 80.3%) |
| `FWW` | Ghostfire | Debuff / Control | 7.6 -> **6.2** (-18.4%) | - | 7.6 -> **6.2** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Status 'Cursed' appliers overtuned on own (WR: 73.7%) |
| `FWE` | Ghostfire | Setup - Location | 111.6 -> **108.7** (-2.6%) | - | 111.6 -> **108.7** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Individual spell overtuned (WR: 53.8%, Casts: 1, mult: 0.998) |
| `FWL` | Ghostfire | Debuff / Control | 19.9 -> **17.0** (-14.6%) | - | 19.9 -> **17.0** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Status 'Cursed' appliers overtuned on own (WR: 73.7%) |
| `FWD` | Ghostfire | Ultimate | 10.5 -> **11.2** (+6.7%) | 47.1 -> **45.9** | 505.1 -> **525.3** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Status 'Cursed' beneficiaries undertuned (WR: 45.4%) |
| `WFF` | Ghostfire | Conditional Strike | 1.2 -> **1.1** (-8.3%) | 778.5 -> **1167.9** | 935.4 -> **1285.8** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Status 'Bleeding' beneficiaries undertuned (WR: 26.0%) |
| `WFW` | Ghostfire | Debuff / Control | 7.5 -> **6.6** (-12.0%) | - | 7.5 -> **6.6** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Individual spell overtuned (WR: 74.4%, Casts: 559, mult: 0.905) |
| `WFE` | Ghostfire | Debuff / Control | 0.8 -> **0.6** (-25.0%) | - | 0.8 -> **0.6** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Status 'Bleeding' appliers overtuned on own (WR: 78.9%) |
| `WFL` | Ghostfire | Buff / Sustain | 55.2 -> **52.0** (-5.8%) | - | 55.2 -> **52.0** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Individual spell overtuned (WR: 59.7%, Casts: 1291, mult: 0.965) |
| `WFD` | Ghostfire | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 387.2 -> **530.4** | 621.1 -> **744.0** | Class Ghostfire overtuned (WR: 56.0%, factor: 0.976); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4991). Increasing spread: b -18.0%, n +37.0% |
| `FEF` | Beasts | Debuff / Control | 15.6 -> **15.1** (-3.2%) | - | 15.6 -> **15.1** | Class Beasts overtuned (WR: 53.7%, factor: 0.985); Individual spell overtuned (WR: 55.8%, Casts: 6787, mult: 0.980) |
| `FEW` | Beasts | Conditional Strike | 1.5 -> **1.1** (-26.7%) | 676.2 -> **903.6** | 1015.8 -> **995.1** | Class Beasts overtuned (WR: 53.7%, factor: 0.985); Status 'Entangled' beneficiaries overtuned (WR: 56.1%) |
| `FEE` | Beasts | Buff / Sustain | 50.6 -> **57.1** (+12.8%) | - | 50.6 -> **57.1** | Class Beasts overtuned (WR: 53.7%, factor: 0.985); Individual spell undertuned (WR: 14.0%, Casts: 4915, mult: 1.146) |
| `FEL` | Beasts | Buff / Sustain | 94.0 -> **95.9** (+2.0%) | - | 94.0 -> **95.9** | Class Beasts overtuned (WR: 53.7%, factor: 0.985); Individual spell undertuned (WR: 40.2%, Casts: 1861, mult: 1.035) |
| `EFF` | Beasts | Debuff / Control | 1.4 -> **1.0** (-28.6%) | 403.8 -> **550.3** | 566.7 -> **551.3** | Class Beasts overtuned (WR: 53.7%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 232). Increasing spread: b -17.7%, n +36.3% |
| `EFW` | Beasts | Buff / Sustain | 47.4 -> **53.0** (+11.8%) | - | 47.4 -> **53.0** | Class Beasts overtuned (WR: 53.7%, factor: 0.985); Individual spell undertuned (WR: 16.5%, Casts: 91, mult: 1.135) |
| `EFE` | Beasts | Buff / Sustain | 22.8 -> **21.1** (-7.5%) | - | 22.8 -> **21.1** | Class Beasts overtuned (WR: 53.7%, factor: 0.985); Individual spell overtuned (WR: 65.9%, Casts: 1688, mult: 0.941) |
| `EFL` | Beasts | Buff / Sustain | 1.7 -> **1.4** (-17.6%) | - | 1.7 -> **1.4** | Class Beasts overtuned (WR: 53.7%, factor: 0.985); Individual spell overtuned (WR: 91.3%, Casts: 4024, mult: 0.830) |
| `EFD` | Beasts | Ultimate | 8.3 -> **6.4** (-22.9%) | 156.3 -> **215.9** | 1305.6 -> **1388.2** | Class Beasts overtuned (WR: 53.7%, factor: 0.985); Status 'Entangled' beneficiaries overtuned (WR: 56.1%) |
| `FLF` | Lightning | Conditional Strike | 1.5 -> **1.2** (-20.0%) | 573.0 -> **749.7** | 861.0 -> **900.8** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Status 'Stunned' beneficiaries overtuned (WR: 61.2%) |
| `FLW` | Lightning | Debuff / Control | 14.6 -> **11.9** (-18.5%) | - | 14.6 -> **11.9** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Status 'Stunned' appliers overtuned on own (WR: 57.6%) |
| `FLE` | Lightning | Setup - Weather | 105.2 -> **129.3** (+22.9%) | - | 105.2 -> **129.3** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Weather 'Storming' appliers undertuned (WR: 14.0%, casts: 1618) |
| `FLL` | Lightning | Buff / Sustain | 34.4 -> **35.4** (+2.9%) | - | 34.4 -> **35.4** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Individual spell undertuned (WR: 30.2%, Casts: 2788, mult: 1.076) |
| `FLD` | Lightning | Ultimate | 14.5 -> **10.9** (-24.8%) | 61.7 -> **76.9** | 909.2 -> **849.1** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Status 'Stunned' beneficiaries overtuned (WR: 61.2%) |
| `LFF` | Lightning | Conditional Strike | 2.3 -> **2.0** (-13.0%) | 426.6 -> **584.4** | 983.5 -> **1170.8** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 976). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 23.2 -> **20.3** (-12.5%) | - | 23.2 -> **20.3** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Individual spell overtuned (WR: 71.7%, Casts: 5137, mult: 0.916) |
| `LFE` | Lightning | Debuff / Control | 15.6 -> **12.7** (-18.6%) | - | 15.6 -> **12.7** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Status 'Stunned' appliers overtuned on own (WR: 57.6%) |
| `LFL` | Lightning | Debuff / Control | 2.7 -> **2.2** (-18.5%) | 297.0 -> **406.9** | 804.6 -> **897.4** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 875). Increasing spread: b -18.0%, n +37.0% |
| `LFD` | Lightning | Conditional Strike | 1.4 -> **1.1** (-21.4%) | 512.3 -> **701.9** | 718.6 -> **773.2** | Class Lightning overtuned (WR: 60.7%, factor: 0.957); Status 'Stunned' appliers overtuned on own (WR: 57.6%) |
| `FDF` | Blood | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 449.8 -> **616.2** | 450.8 -> **555.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 264). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 34.8%, Casts: 264, mult: 1.057) |
| `FDW` | Blood | Direct Damage | 63.9 -> **71.0** (+11.1%) | - | 63.9 -> **71.0** | Individual spell undertuned (WR: 21.9%, Casts: 2587, mult: 1.111) |
| `FDE` | Blood | Setup - Weather | 57.1 -> **66.2** (+15.9%) | - | 57.1 -> **66.2** | Individual spell undertuned (WR: 11.1%, Casts: 3294, mult: 1.159) |
| `FDD` | Blood | Ultimate | 8.4 -> **6.7** (-20.2%) | 43.1 -> **59.0** | 370.4 -> **402.0** | Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 3866). Increasing spread: b -18.0%, n +36.9%; Individual spell overtuned (WR: 57.6%, Casts: 3866, mult: 0.973) |
| `DFF` | Blood | Conditional Strike | 1.6 -> **1.3** (-18.8%) | 590.5 -> **878.3** | 946.4 -> **1143.1** | Status 'Bleeding' beneficiaries undertuned (WR: 26.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 2944). Increasing spread: b -17.4%, n +35.7% |
| `DFE` | Blood | Buff / Sustain | 149.8 -> **166.1** (+10.9%) | - | 149.8 -> **166.1** | Individual spell undertuned (WR: 22.5%, Casts: 139, mult: 1.109) |
| `DFL` | Blood | Buff / Sustain | 8.6 -> **8.3** (-3.5%) | - | 8.6 -> **8.3** | Individual spell overtuned (WR: 60.7%, Casts: 6300, mult: 0.962) |
| `DFD` | Blood | Conditional Strike | 107.1 -> **116.5** (+8.8%) | 0.1 -> **0.1** | 117.8 -> **128.2** | Condition triggers excessively (N=1 conditions, Trigger Rate: 91.8% vs 55% ceiling, WR: 86.7%). Compressing spread: b +27.8%, n -35.7%; Individual spell overtuned (WR: 86.7%, Casts: 939, mult: 0.851) |
| `WEF` | Plants | Conditional Strike | 1.2 -> **1.1** (-8.3%) | 468.4 -> **662.7** | 563.3 -> **730.1** | Class Plants undertuned (WR: 39.7%, factor: 1.041); Location 'Jungle' beneficiaries undertuned (WR: 41.6%) |
| `WEW` | Plants | Debuff / Control | 63.0 -> **75.1** (+19.2%) | - | 63.0 -> **75.1** | Class Plants undertuned (WR: 39.7%, factor: 1.041); Individual spell undertuned (WR: 14.4%, Casts: 78, mult: 1.144) |
| `WEE` | Plants | Setup - Location | 184.4 -> **207.8** (+12.7%) | - | 184.4 -> **207.8** | Class Plants undertuned (WR: 39.7%, factor: 1.041); Location 'Jungle' appliers undertuned (WR: 38.7%, casts: 643) |
| `WEL` | Plants | Debuff / Control | 14.8 -> **13.8** (-6.8%) | - | 14.8 -> **13.8** | Class Plants undertuned (WR: 39.7%, factor: 1.041); Status 'Entangled' appliers overtuned on own (WR: 65.2%) |
| `WED` | Plants | Conditional Strike | 15.4 -> **12.3** (-20.1%) | 15.2 -> **20.8** | 249.5 -> **268.1** | Class Plants undertuned (WR: 39.7%, factor: 1.041); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 826). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 2.5 -> **2.4** (-4.0%) | 559.0 -> **846.5** | 1400.0 -> **2034.0** | Class Plants undertuned (WR: 39.7%, factor: 1.041); Weather 'Sunny' beneficiaries undertuned (WR: 19.7%) |
| `EWW` | Plants | Debuff / Control | 2.1 -> **1.8** (-14.3%) | - | 2.1 -> **1.8** | Class Plants undertuned (WR: 39.7%, factor: 1.041); Individual spell overtuned (WR: 93.7%, Casts: 1745, mult: 0.820) |
| `EWL` | Plants | Debuff / Control | 23.6 -> **21.8** (-7.6%) | - | 23.6 -> **21.8** | Class Plants undertuned (WR: 39.7%, factor: 1.041); Individual spell overtuned (WR: 78.2%, Casts: 2837, mult: 0.888) |
| `EWD` | Plants | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 656.3 -> **877.0** | 262.9 -> **263.4** | Class Plants undertuned (WR: 39.7%, factor: 1.041); Status 'Bleeding' appliers overtuned on own (WR: 78.9%) |
| `WLF` | Fey | Conditional Strike | 2.1 -> **1.9** (-9.5%) | 326.0 -> **454.9** | 686.7 -> **866.2** | Status 'Cursed' beneficiaries undertuned (WR: 45.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 48). Increasing spread: b -18.0%, n +37.0% |
| `WLW` | Fey | Debuff / Control | 16.9 -> **13.8** (-18.3%) | - | 16.9 -> **13.8** | Status 'Cursed' appliers overtuned on own (WR: 73.7%); Individual spell overtuned (WR: 77.3%, Casts: 4024, mult: 0.892) |
| `WLE` | Fey | Setup - Location | 275.5 -> **345.3** (+25.3%) | - | 275.5 -> **345.3** | Location 'Enchanted Forest' appliers undertuned (WR: 18.2%, casts: 1997); Individual spell undertuned (WR: 18.2%, Casts: 1997, mult: 1.128) |
| `WLL` | Fey | Direct Damage | 59.2 -> **49.0** (-17.2%) | - | 59.2 -> **49.0** | Individual spell overtuned (WR: 91.6%, Casts: 370, mult: 0.828) |
| `WLD` | Fey | Ultimate | 10.7 -> **8.8** (-17.8%) | 116.7 -> **159.9** | 1259.4 -> **1415.9** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4395). Increasing spread: b -18.0%, n +37.0% |
| `LWF` | Fey | Debuff / Control | 4.1 -> **3.7** (-9.8%) | 412.9 -> **556.8** | 1697.0 -> **2063.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.6% vs 30% floor, Casts: 850). Increasing spread: b -17.0%, n +34.8%; Individual spell undertuned (WR: 30.7%, Casts: 850, mult: 1.074) |
| `LWW` | Fey | Debuff / Control | 63.0 -> **59.7** (-5.2%) | - | 63.0 -> **59.7** | Individual spell overtuned (WR: 64.1%, Casts: 233, mult: 0.948) |
| `LWL` | Fey | Debuff / Control | 174.6 -> **200.3** (+14.7%) | - | 174.6 -> **200.3** | Individual spell undertuned (WR: 13.8%, Casts: 400, mult: 1.147) |
| `LWD` | Fey | Conditional Strike | 3.1 -> **2.4** (-22.6%) | 449.8 -> **616.2** | 1397.5 -> **1481.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 804). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 62.9%, Casts: 804, mult: 0.953) |
| `WDF` | Ice | Conditional Strike | 2.7 -> **2.2** (-18.5%) | 849.3 -> **1238.0** | 2295.8 -> **2725.8** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Stunned' appliers overtuned on own (WR: 57.6%) |
| `WDW` | Ice | Buff / Sustain | 46.6 -> **45.5** (-2.4%) | - | 46.6 -> **45.5** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 68.2%) |
| `WDE` | Ice | Setup - Weather | 83.1 -> **93.4** (+12.4%) | - | 83.1 -> **93.4** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Individual spell undertuned (WR: 14.5%, Casts: 9099, mult: 1.144) |
| `WDL` | Ice | Debuff / Control | 20.6 -> **17.2** (-16.5%) | - | 20.6 -> **17.2** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 68.2%) |
| `WDD` | Ice | Ultimate | 9.5 -> **7.6** (-20.0%) | 44.5 -> **59.1** | 432.2 -> **456.8** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Weather 'Blizzard' beneficiaries overtuned (WR: 53.9%) |
| `DWF` | Ice | Debuff / Control | 18.4 -> **15.5** (-15.8%) | - | 18.4 -> **15.5** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 68.2%) |
| `DWW` | Ice | Debuff / Control | 21.2 -> **19.2** (-9.4%) | - | 21.2 -> **19.2** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Individual spell overtuned (WR: 70.8%, Casts: 8449, mult: 0.920) |
| `DWE` | Ice | Setup - Location | 185.8 -> **217.2** (+16.9%) | - | 185.8 -> **217.2** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Location 'Tundra' appliers undertuned (WR: 25.6%, casts: 2386) |
| `DWL` | Ice | Debuff / Control | 21.8 -> **17.9** (-17.9%) | - | 21.8 -> **17.9** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' appliers overtuned on own (WR: 68.2%) |
| `DWD` | Ice | Conditional Strike | 3.1 -> **2.6** (-16.1%) | 471.4 -> **650.4** | 1464.4 -> **1693.6** | Class Ice overtuned (WR: 54.2%, factor: 0.983); Status 'Frosty' beneficiaries undertuned (WR: 37.3%) |
| `ELF` | Wind | Conditional Strike | 4.5 -> **3.8** (-15.6%) | 689.6 -> **1014.0** | 3107.7 -> **3857.0** | Status 'Bleeding' beneficiaries undertuned (WR: 26.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.4% vs 30% floor, Casts: 1561). Increasing spread: b -16.6%, n +34.2% |
| `ELW` | Wind | Debuff / Control | 29.2 -> **25.6** (-12.3%) | - | 29.2 -> **25.6** | Individual spell overtuned (WR: 80.5%, Casts: 696, mult: 0.878) |
| `ELE` | Wind | Setup - Weather | 70.9 -> **73.9** (+4.2%) | - | 70.9 -> **73.9** | Individual spell undertuned (WR: 38.3%, Casts: 6111, mult: 1.043) |
| `ELL` | Wind | Buff / Sustain | 94.1 -> **85.7** (-8.9%) | - | 94.1 -> **85.7** | Individual spell overtuned (WR: 73.1%, Casts: 508, mult: 0.910) |
| `ELD` | Wind | Conditional Strike | 5.0 -> **4.9** (-2.0%) | 765.0 -> **1115.1** | 3830.0 -> **5468.9** | Weather 'Raining' beneficiaries undertuned (WR: 34.0%); Weather 'Blizzard' appliers undertuned (WR: 23.6%, casts: 596) |
| `LEF` | Wind | Conditional Strike | 2.5 -> **2.2** (-12.0%) | 520.8 -> **746.9** | 1304.5 -> **1645.4** | Status 'Burning' beneficiaries undertuned (WR: 37.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 9040). Increasing spread: b -17.8%, n +36.6% |
| `LEW` | Wind | Debuff / Control | 27.5 -> **23.4** (-14.9%) | - | 27.5 -> **23.4** | Individual spell overtuned (WR: 86.5%, Casts: 5553, mult: 0.851) |
| `LEE` | Wind | Setup - Weather | 80.7 -> **94.1** (+16.6%) | - | 80.7 -> **94.1** | Individual spell undertuned (WR: 9.6%, Casts: 2820, mult: 1.166) |
| `LEL` | Wind | Buff / Sustain | 119.7 -> **121.9** (+1.8%) | - | 119.7 -> **121.9** | Individual spell undertuned (WR: 44.5%, Casts: 692, mult: 1.019) |
| `EDF` | Poison | Conditional Strike | 1.2 -> **0.9** (-25.0%) | 306.1 -> **419.4** | 368.5 -> **378.4** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 478). Increasing spread: b -18.0%, n +37.0% |
| `EDW` | Poison | Debuff / Control | 5.2 -> **4.9** (-5.8%) | - | 5.2 -> **4.9** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Individual spell overtuned (WR: 72.2%, Casts: 2604, mult: 0.914) |
| `EDE` | Poison | Setup - Location | 112.3 -> **139.5** (+24.2%) | - | 112.3 -> **139.5** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Location 'Swamp' appliers undertuned (WR: 22.9%, casts: 3025) |
| `EDL` | Poison | Debuff / Control | 0.8 -> **0.7** (-12.5%) | - | 0.8 -> **0.7** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Individual spell overtuned (WR: 94.1%, Casts: 3247, mult: 0.820) |
| `EDD` | Poison | Ultimate | 15.0 -> **17.3** (+15.3%) | 72.0 -> **77.6** | 1095.0 -> **1359.8** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Status 'Bleeding' beneficiaries undertuned (WR: 26.0%) |
| `DEF` | Poison | Conditional Strike | 8.4 -> **7.2** (-14.3%) | 5.0 -> **6.7** | 50.4 -> **55.4** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.2% vs 30% floor, Casts: 1497). Increasing spread: b -16.3%, n +33.5% |
| `DEW` | Poison | Debuff / Control | 5.3 -> **5.1** (-3.8%) | - | 5.3 -> **5.1** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Individual spell overtuned (WR: 66.3%, Casts: 1665, mult: 0.939) |
| `DEE` | Poison | Debuff / Control | 14.3 -> **14.2** (-0.7%) | - | 14.3 -> **14.2** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Individual spell overtuned (WR: 58.6%, Casts: 99, mult: 0.970) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 719.5 -> **1080.3** | 216.2 -> **324.4** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Status 'Bleeding' beneficiaries undertuned (WR: 26.0%) |
| `DED` | Poison | Debuff / Control | 17.1 -> **16.9** (-1.2%) | - | 17.1 -> **16.9** | Class Poison undertuned (WR: 43.8%, factor: 1.025); Individual spell overtuned (WR: 60.4%, Casts: 3737, mult: 0.963) |
| `LDW` | Cosmic | Debuff / Control | 13.8 -> **12.3** (-10.9%) | - | 13.8 -> **12.3** | Status 'Stunned' appliers overtuned on own (WR: 57.6%); Individual spell overtuned (WR: 72.2%, Casts: 4220, mult: 0.914) |
| `LDE` | Cosmic | Setup - Location | 42.4 -> **50.0** (+17.9%) | - | 42.4 -> **50.0** | Individual spell undertuned (WR: 6.4%, Casts: 4301, mult: 1.180) |
| `LDL` | Cosmic | Conditional Strike | 2.1 -> **1.7** (-19.0%) | 374.9 -> **513.6** | 789.4 -> **874.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2143). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 57.1%, Casts: 2143, mult: 0.975) |
| `LDD` | Cosmic | Ultimate | 15.7 -> **11.9** (-24.2%) | 37.6 -> **51.5** | 606.0 -> **624.8** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 5653). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 69.5%, Casts: 5653, mult: 0.925) |
| `DLF` | Cosmic | Conditional Strike | 2.4 -> **2.2** (-8.3%) | 340.2 -> **465.5** | 818.9 -> **1026.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 2360). Increasing spread: b -17.9%, n +36.8%; Individual spell undertuned (WR: 25.6%, Casts: 2360, mult: 1.096) |
| `DLW` | Cosmic | Direct Damage | 21.5 -> **20.1** (-6.5%) | - | 21.5 -> **20.1** | Individual spell overtuned (WR: 67.7%, Casts: 9816, mult: 0.933) |
| `DLE` | Cosmic | Direct Damage | 138.0 -> **151.5** (+9.8%) | - | 138.0 -> **151.5** | Individual spell undertuned (WR: 25.1%, Casts: 3645, mult: 1.098) |
| `DLL` | Cosmic | Conditional Strike | 2.5 -> **2.3** (-8.0%) | 342.5 -> **469.2** | 858.8 -> **1081.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1437). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 17.2%, Casts: 1437, mult: 1.132) |
