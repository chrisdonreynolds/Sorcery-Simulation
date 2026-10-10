# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T18:47:11Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 107.8s  
**Total Spells Tuned:** 109 / 125  

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
| **Earth** | 12,685 | 70.2% | 70.2% | 15.0 | Overtuned ⚠️ |
| **Water** | 8,980 | 69.1% | 69.1% | 5.5 | Overtuned ⚠️ |
| **Ghostfire** | 25,367 | 59.4% | 59.4% | 2.2 | Overtuned ⚠️ |
| **Blood** | 25,207 | 57.6% | 57.6% | 7.8 | Overtuned ⚠️ |
| **Cosmic** | 24,135 | 57.3% | 57.4% | 8.8 | Overtuned ⚠️ |
| **Poison** | 38,777 | 55.1% | 55.1% | 2.9 | Overtuned ⚠️ |
| **Light** | 17,479 | 54.8% | 54.8% | 1.6 | Overtuned ⚠️ |
| **Fire** | 13,609 | 54.5% | 54.5% | 3.2 | Overtuned ⚠️ |
| **Beasts** | 32,901 | 50.6% | 50.6% | 2.7 | Balanced ✅ |
| **Ice** | 40,322 | 50.5% | 50.5% | 3.1 | Balanced ✅ |
| **Dark** | 8,044 | 49.3% | 49.3% | 2.5 | Balanced ✅ |
| **Lightning** | 20,005 | 45.4% | 45.4% | 1.8 | Undertuned ⚠️ |
| **Plants** | 30,457 | 42.8% | 42.8% | 2.0 | Undertuned ⚠️ |
| **Fey** | 31,723 | 39.0% | 39.0% | 2.9 | Undertuned ⚠️ |
| **Wind** | 35,049 | 25.9% | 25.9% | 1.1 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 17,756 (63.7%) | 1,486 (40.7%) | 4.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,989 (69.2%) | 12,671 (45.6%) | 1.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,878 (71.5%) | 10,190 (27.5%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,077 (78.6%) | 20,969 (35.7%) | 2.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 11,566 (56.9%) | 2,496 (29.8%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 4,177 (68.8%) | 5,959 (39.7%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 194 (49.5%) | 3,485 (35.0%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 15.3 -> **13.8** (-9.8%) | - | 15.3 -> **13.8** | Class Fire overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 71.8%, Casts: 2147, mult: 0.916) |
| `FFW` | Fire | Debuff / Control | 6.6 -> **5.9** (-10.6%) | - | 6.6 -> **5.9** | Class Fire overtuned (WR: 54.5%, factor: 0.982); Status 'Burning' appliers overtuned on own (WR: 71.5%) |
| `FFE` | Fire | Debuff / Control | 8.5 -> **7.5** (-11.8%) | - | 8.5 -> **7.5** | Class Fire overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 74.6%, Casts: 1512, mult: 0.904) |
| `FFD` | Fire | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 4778.9 -> **7109.9** | 4301.9 -> **5688.7** | Class Fire overtuned (WR: 54.5%, factor: 0.982); Status 'Burning' beneficiaries undertuned (WR: 27.5%) |
| `WWF` | Water | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 2832.0 -> **3719.6** | 2833.0 -> **3348.5** | Class Water overtuned (WR: 69.1%, factor: 0.924); Status 'Burning' beneficiaries undertuned (WR: 27.5%) |
| `WWE` | Water | Setup - Weather | 315.7 -> **291.6** (-7.6%) | - | 315.7 -> **291.6** | Class Water overtuned (WR: 69.1%, factor: 0.924) |
| `WWL` | Water | Buff / Sustain | 13.7 -> **11.6** (-15.3%) | - | 13.7 -> **11.6** | Class Water overtuned (WR: 69.1%, factor: 0.924); Individual spell overtuned (WR: 71.0%, Casts: 7730, mult: 0.919) |
| `WWD` | Water | Buff / Sustain | 25.6 -> **22.5** (-12.1%) | - | 25.6 -> **22.5** | Class Water overtuned (WR: 69.1%, factor: 0.924); Individual spell overtuned (WR: 73.1%, Casts: 14, mult: 0.953) |
| `EEF` | Earth | Conditional Strike | 0.9 -> **0.7** (-22.2%) | 4193.2 -> **5869.9** | 3774.8 -> **4109.6** | Class Earth overtuned (WR: 70.2%, factor: 0.919); Status 'Frosty' beneficiaries undertuned (WR: 40.7%) |
| `EEW` | Earth | Buff / Sustain | 33.8 -> **29.9** (-11.5%) | - | 33.8 -> **29.9** | Class Earth overtuned (WR: 70.2%, factor: 0.919); Individual spell overtuned (WR: 60.8%, Casts: 1372, mult: 0.961) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 2201.1 -> **2966.7** | 220.2 -> **296.8** | Class Light overtuned (WR: 54.8%, factor: 0.981); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.7% vs 30% floor, Casts: 1730). Increasing spread: b -16.9%, n +34.8% |
| `LLW` | Light | Debuff / Control | 10.0 -> **9.8** (-2.0%) | - | 10.0 -> **9.8** | Class Light overtuned (WR: 54.8%, factor: 0.981) |
| `LLE` | Light | Setup - Weather | 717.8 -> **608.6** (-15.2%) | - | 717.8 -> **608.6** | Class Light overtuned (WR: 54.8%, factor: 0.981); Weather 'Sunny' appliers overtuned on own (WR: 69.2%) |
| `LLL` | Light | Buff / Sustain | 7.4 -> **6.5** (-12.2%) | - | 7.4 -> **6.5** | Class Light overtuned (WR: 54.8%, factor: 0.981); Individual spell overtuned (WR: 76.3%, Casts: 2784, mult: 0.896) |
| `LLD` | Light | Ultimate | 3.9 -> **4.2** (+7.7%) | 570.9 -> **546.2** | 2230.4 -> **2298.2** | Class Light overtuned (WR: 54.8%, factor: 0.981); Weather 'Sunny' beneficiaries undertuned (WR: 45.6%) |
| `DDF` | Dark | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 2974.0 -> **4074.4** | 1190.0 -> **1630.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1947). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 10.6%, Casts: 1947, mult: 1.162) |
| `DDW` | Dark | Debuff / Control | 10.1 -> **10.6** (+5.0%) | - | 10.1 -> **10.6** | Individual spell undertuned (WR: 37.4%, Casts: 520, mult: 1.046) |
| `DDE` | Dark | Setup - Weather | 404.8 -> **433.1** (+7.0%) | - | 404.8 -> **433.1** | Weather 'Darkness' appliers undertuned (WR: 40.3%, casts: 259); Individual spell undertuned (WR: 40.2%, Casts: 259, mult: 1.035) |
| `DDL` | Dark | Debuff / Control | 9.3 -> **8.9** (-4.3%) | - | 9.3 -> **8.9** | Individual spell overtuned (WR: 61.7%, Casts: 2868, mult: 0.958) |
| `DDD` | Dark | Debuff / Control | 3.6 -> **3.3** (-8.3%) | - | 3.6 -> **3.3** | Individual spell overtuned (WR: 69.2%, Casts: 2450, mult: 0.927) |
| `FWW` | Ghostfire | Debuff / Control | 4.9 -> **4.3** (-12.2%) | - | 4.9 -> **4.3** | Class Ghostfire overtuned (WR: 59.4%, factor: 0.963); Status 'Cursed' appliers overtuned on own (WR: 63.0%) |
| `FWE` | Ghostfire | Setup - Location | 130.0 -> **97.3** (-25.2%) | - | 130.0 -> **97.3** | Class Ghostfire overtuned (WR: 59.4%, factor: 0.963); Location 'Graveyard' appliers overtuned on own (WR: 83.0%) |
| `FWL` | Ghostfire | Debuff / Control | 11.6 -> **10.7** (-7.8%) | - | 11.6 -> **10.7** | Class Ghostfire overtuned (WR: 59.4%, factor: 0.963); Status 'Cursed' appliers overtuned on own (WR: 63.0%) |
| `FWD` | Ghostfire | Ultimate | 5.1 -> **3.5** (-31.4%) | 152.5 -> **187.4** | 782.8 -> **659.4** | Class Ghostfire overtuned (WR: 59.4%, factor: 0.963); Status 'Cursed' beneficiaries undertuned (WR: 45.1%) |
| `WFF` | Ghostfire | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 7105.2 -> **10290.5** | 4263.7 -> **5145.8** | Class Ghostfire overtuned (WR: 59.4%, factor: 0.963); Status 'Bleeding' beneficiaries undertuned (WR: 35.7%) |
| `WFW` | Ghostfire | Debuff / Control | 4.2 -> **3.9** (-7.1%) | - | 4.2 -> **3.9** | Class Ghostfire overtuned (WR: 59.4%, factor: 0.963); Individual spell overtuned (WR: 62.9%, Casts: 8843, mult: 0.953) |
| `WFE` | Ghostfire | Debuff / Control | 0.6 -> **0.4** (-33.3%) | - | 0.6 -> **0.4** | Class Ghostfire overtuned (WR: 59.4%, factor: 0.963); Status 'Bleeding' appliers overtuned on own (WR: 78.6%) |
| `WFL` | Ghostfire | Buff / Sustain | 45.7 -> **44.0** (-3.7%) | - | 45.7 -> **44.0** | Class Ghostfire overtuned (WR: 59.4%, factor: 0.963) |
| `WFD` | Ghostfire | Conditional Strike | 0.8 -> **0.6** (-25.0%) | 2462.2 -> **3372.4** | 1970.6 -> **2024.0** | Class Ghostfire overtuned (WR: 59.4%, factor: 0.963); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4973). Increasing spread: b -18.0%, n +37.0% |
| `FEF` | Beasts | Debuff / Control | 10.7 -> **10.0** (-6.5%) | - | 10.7 -> **10.0** | Individual spell overtuned (WR: 66.6%, Casts: 5948, mult: 0.937) |
| `FEW` | Beasts | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 4173.0 -> **5953.0** | 2087.0 -> **2381.6** | Status 'Entangled' beneficiaries undertuned (WR: 39.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 770). Increasing spread: b -18.0%, n +37.0% |
| `FEE` | Beasts | Buff / Sustain | 110.4 -> **127.0** (+15.0%) | - | 110.4 -> **127.0** | Individual spell undertuned (WR: 13.1%, Casts: 4095, mult: 1.151) |
| `FEL` | Beasts | Buff / Sustain | 149.6 -> **152.3** (+1.8%) | - | 149.6 -> **152.3** | Individual spell undertuned (WR: 44.6%, Casts: 3078, mult: 1.018) |
| `FED` | Beasts | Conditional Strike | 2.3 -> **2.1** (-8.7%) | 3.5 -> **3.5** | 10.3 -> **9.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.2% vs 30% floor, Casts: 31). Increasing spread: b -16.7%, n +34.3%; Individual spell undertuned (WR: 16.3%, Casts: 31, mult: 1.107) |
| `EFF` | Beasts | Debuff / Control | 0.5 -> **0.5** (+0.0%) | 2655.6 -> **3638.2** | 1328.3 -> **1819.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4601). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 8.4%, Casts: 4601, mult: 1.171) |
| `EFW` | Beasts | Buff / Sustain | 84.4 -> **80.2** (-5.0%) | - | 84.4 -> **80.2** | Individual spell overtuned (WR: 63.6%, Casts: 139, mult: 0.950) |
| `EFE` | Beasts | Buff / Sustain | 13.1 -> **11.8** (-9.9%) | - | 13.1 -> **11.8** | Individual spell overtuned (WR: 75.5%, Casts: 7229, mult: 0.900) |
| `EFD` | Beasts | Ultimate | 4.0 -> **4.5** (+12.5%) | 516.1 -> **554.1** | 2068.4 -> **2498.0** | Status 'Entangled' beneficiaries undertuned (WR: 39.7%); Location 'Jungle' beneficiaries undertuned (WR: 25.8%) |
| `FLF` | Lightning | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 4699.4 -> **6958.1** | 3290.3 -> **4175.5** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Status 'Stunned' beneficiaries undertuned (WR: 29.8%) |
| `FLW` | Lightning | Debuff / Control | 8.2 -> **7.6** (-7.3%) | - | 8.2 -> **7.6** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Status 'Stunned' appliers overtuned on own (WR: 56.9%) |
| `FLE` | Lightning | Setup - Weather | 253.2 -> **246.7** (-2.6%) | - | 253.2 -> **246.7** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Weather 'Storming' appliers overtuned on own (WR: 56.3%) |
| `FLL` | Lightning | Buff / Sustain | 47.0 -> **42.4** (-9.8%) | - | 47.0 -> **42.4** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Individual spell overtuned (WR: 78.6%, Casts: 952, mult: 0.886) |
| `FLD` | Lightning | Ultimate | 5.9 -> **4.5** (-23.7%) | 347.9 -> **471.8** | 2058.5 -> **2127.6** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Status 'Stunned' beneficiaries undertuned (WR: 29.8%) |
| `LFF` | Lightning | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 2820.3 -> **3863.3** | 2821.3 -> **3477.9** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5021). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 18.6 -> **18.9** (+1.6%) | - | 18.6 -> **18.9** | Class Lightning undertuned (WR: 45.4%, factor: 1.018) |
| `LFE` | Lightning | Debuff / Control | 7.7 -> **7.3** (-5.2%) | - | 7.7 -> **7.3** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Status 'Stunned' appliers overtuned on own (WR: 56.9%) |
| `LFL` | Lightning | Debuff / Control | 1.1 -> **1.0** (-9.1%) | 1958.3 -> **2754.5** | 2155.2 -> **2755.5** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Weather 'Darkness' beneficiaries undertuned (WR: 43.1%) |
| `LFD` | Lightning | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 3342.8 -> **4579.6** | 1671.9 -> **1832.2** | Class Lightning undertuned (WR: 45.4%, factor: 1.018); Status 'Stunned' appliers overtuned on own (WR: 56.9%) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 2974.0 -> **4074.4** | 595.0 -> **815.1** | Class Blood overtuned (WR: 57.6%, factor: 0.969); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 897). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 77.0 -> **80.6** (+4.7%) | - | 77.0 -> **80.6** | Class Blood overtuned (WR: 57.6%, factor: 0.969); Individual spell undertuned (WR: 29.4%, Casts: 1114, mult: 1.079) |
| `FDE` | Blood | Setup - Weather | 57.3 -> **48.3** (-15.7%) | - | 57.3 -> **48.3** | Class Blood overtuned (WR: 57.6%, factor: 0.969); Individual spell overtuned (WR: 82.5%, Casts: 68, mult: 0.869) |
| `FDD` | Blood | Ultimate | 2.4 -> **2.7** (+12.5%) | 200.0 -> **193.2** | 482.4 -> **524.3** | Class Blood overtuned (WR: 57.6%, factor: 0.969); Weather 'Darkness' beneficiaries undertuned (WR: 43.1%) |
| `DFF` | Blood | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 5137.5 -> **7325.3** | 3596.9 -> **4395.8** | Class Blood overtuned (WR: 57.6%, factor: 0.969); Status 'Bleeding' beneficiaries undertuned (WR: 35.7%) |
| `DFE` | Blood | Buff / Sustain | 250.6 -> **286.7** (+14.4%) | - | 250.6 -> **286.7** | Class Blood overtuned (WR: 57.6%, factor: 0.969); Individual spell undertuned (WR: 1.3%, Casts: 1292, mult: 1.180) |
| `DFL` | Blood | Buff / Sustain | 5.5 -> **5.1** (-7.3%) | - | 5.5 -> **5.1** | Class Blood overtuned (WR: 57.6%, factor: 0.969); Individual spell overtuned (WR: 61.0%, Casts: 4342, mult: 0.960) |
| `DFD` | Blood | Conditional Strike | 130.9 -> **134.1** (+2.4%) | 0.1 -> **0.1** | 144.0 -> **147.5** | Class Blood overtuned (WR: 57.6%, factor: 0.969); Condition triggers excessively (N=1 conditions, Trigger Rate: 84.0% vs 55% ceiling, WR: 93.4%). Compressing spread: b +28.8%, n -35.7% |
| `WEF` | Plants | Conditional Strike | 0.6 -> **0.6** (+0.0%) | 3401.4 -> **5040.5** | 2041.4 -> **3024.9** | Class Plants undertuned (WR: 42.8%, factor: 1.029); Location 'Jungle' beneficiaries undertuned (WR: 25.8%) |
| `WEW` | Plants | Debuff / Control | 108.2 -> **120.0** (+10.9%) | - | 108.2 -> **120.0** | Class Plants undertuned (WR: 42.8%, factor: 1.029); Individual spell undertuned (WR: 29.6%, Casts: 3680, mult: 1.078) |
| `WEE` | Plants | Setup - Location | 527.8 -> **706.0** (+33.8%) | - | 527.8 -> **706.0** | Class Plants undertuned (WR: 42.8%, factor: 1.029); Location 'Jungle' appliers undertuned (WR: 10.8%, casts: 3416) |
| `WEL` | Plants | Debuff / Control | 8.4 -> **7.5** (-10.7%) | - | 8.4 -> **7.5** | Class Plants undertuned (WR: 42.8%, factor: 1.029); Status 'Entangled' appliers overtuned on own (WR: 68.8%) |
| `WED` | Plants | Conditional Strike | 6.4 -> **7.1** (+10.9%) | 68.8 -> **64.7** | 446.7 -> **466.5** | Class Plants undertuned (WR: 42.8%, factor: 1.029); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 5126, WR: 47.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 1.6 -> **1.4** (-12.5%) | 4934.2 -> **6710.7** | 7896.3 -> **9396.4** | Class Plants undertuned (WR: 42.8%, factor: 1.029); Weather 'Sunny' beneficiaries undertuned (WR: 45.6%) |
| `EWL` | Plants | Debuff / Control | 14.0 -> **13.2** (-5.7%) | - | 14.0 -> **13.2** | Class Plants undertuned (WR: 42.8%, factor: 1.029); Individual spell overtuned (WR: 72.1%, Casts: 3543, mult: 0.915) |
| `EWD` | Plants | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 4050.1 -> **5777.7** | 405.1 -> **577.9** | Class Plants undertuned (WR: 42.8%, factor: 1.029); Status 'Bleeding' appliers overtuned on own (WR: 78.6%) |
| `WLF` | Fey | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 2349.4 -> **3239.3** | 2350.4 -> **2916.3** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Status 'Cursed' beneficiaries undertuned (WR: 45.1%) |
| `WLW` | Fey | Debuff / Control | 9.5 -> **8.5** (-10.5%) | - | 9.5 -> **8.5** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Status 'Cursed' appliers overtuned on own (WR: 63.0%) |
| `WLE` | Fey | Setup - Location | 1276.9 -> **1542.6** (+20.8%) | - | 1276.9 -> **1542.6** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Location 'Enchanted Forest' appliers undertuned (WR: 29.4%, casts: 908) |
| `WLL` | Fey | Direct Damage | 29.5 -> **26.7** (-9.5%) | - | 29.5 -> **26.7** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Individual spell overtuned (WR: 83.4%, Casts: 2681, mult: 0.865) |
| `WLD` | Fey | Ultimate | 5.9 -> **4.8** (-18.6%) | 433.9 -> **610.7** | 2565.9 -> **2936.2** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Weather 'Darkness' beneficiaries undertuned (WR: 43.1%) |
| `LWF` | Fey | Debuff / Control | 2.0 -> **1.8** (-10.0%) | 3067.7 -> **4149.6** | 6137.4 -> **7471.1** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.1% vs 30% floor, Casts: 6117). Increasing spread: b -17.2%, n +35.3% |
| `LWW` | Fey | Debuff / Control | 85.9 -> **103.5** (+20.5%) | - | 85.9 -> **103.5** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Individual spell undertuned (WR: 12.2%, Casts: 7071, mult: 1.154) |
| `LWL` | Fey | Debuff / Control | 394.3 -> **479.2** (+21.5%) | - | 394.3 -> **479.2** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Individual spell undertuned (WR: 10.0%, Casts: 2603, mult: 1.164) |
| `LWD` | Fey | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 2974.0 -> **4074.4** | 2677.5 -> **3260.3** | Class Fey undertuned (WR: 39.0%, factor: 1.044); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 236). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 6077.6 -> **8826.2** | 3647.2 -> **4413.6** | Status 'Stunned' appliers overtuned on own (WR: 56.9%); Weather 'Raining' beneficiaries undertuned (WR: 35.0%) |
| `WDW` | Ice | Buff / Sustain | 39.8 -> **37.9** (-4.8%) | - | 39.8 -> **37.9** | Status 'Frosty' appliers overtuned on own (WR: 63.7%) |
| `WDE` | Ice | Setup - Weather | 135.3 -> **158.7** (+17.3%) | - | 135.3 -> **158.7** | Individual spell undertuned (WR: 8.1%, Casts: 5138, mult: 1.173) |
| `WDL` | Ice | Debuff / Control | 9.4 -> **8.3** (-11.7%) | - | 9.4 -> **8.3** | Status 'Frosty' appliers overtuned on own (WR: 63.7%); Individual spell overtuned (WR: 68.6%, Casts: 663, mult: 0.929) |
| `WDD` | Ice | Ultimate | 5.6 -> **4.6** (-17.9%) | 91.8 -> **125.8** | 519.7 -> **583.3** | Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 10422). Increasing spread: b -18.0%, n +37.0% |
| `DWF` | Ice | Debuff / Control | 8.4 -> **7.3** (-13.1%) | - | 8.4 -> **7.3** | Status 'Frosty' appliers overtuned on own (WR: 63.7%); Individual spell overtuned (WR: 72.6%, Casts: 7609, mult: 0.912) |
| `DWW` | Ice | Debuff / Control | 10.7 -> **10.2** (-4.7%) | - | 10.7 -> **10.2** | Individual spell overtuned (WR: 62.1%, Casts: 4395, mult: 0.956) |
| `DWE` | Ice | Setup - Location | 260.3 -> **239.5** (-8.0%) | - | 260.3 -> **239.5** | Location 'Tundra' appliers overtuned on own (WR: 61.4%); Individual spell overtuned (WR: 61.5%, Casts: 344, mult: 0.958) |
| `DWL` | Ice | Debuff / Control | 11.6 -> **10.8** (-6.9%) | - | 11.6 -> **10.8** | Status 'Frosty' appliers overtuned on own (WR: 63.7%); Individual spell overtuned (WR: 57.4%, Casts: 8036, mult: 0.974) |
| `DWD` | Ice | Conditional Strike | 0.8 -> **0.8** (+0.0%) | 3161.8 -> **4254.4** | 2530.2 -> **3404.3** | Status 'Frosty' beneficiaries undertuned (WR: 40.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 389). Increasing spread: b -14.5%, n +29.7% |
| `ELF` | Wind | Conditional Strike | 2.0 -> **2.0** (+0.0%) | 6069.6 -> **8358.6** | 12141.2 -> **16719.2** | Class Wind undertuned (WR: 25.9%, factor: 1.096); Status 'Bleeding' beneficiaries undertuned (WR: 35.7%) |
| `ELW` | Wind | Debuff / Control | 18.1 -> **22.0** (+21.5%) | - | 18.1 -> **22.0** | Class Wind undertuned (WR: 25.9%, factor: 1.096); Individual spell undertuned (WR: 22.6%, Casts: 50, mult: 1.108) |
| `ELE` | Wind | Setup - Weather | 120.6 -> **153.0** (+26.9%) | - | 120.6 -> **153.0** | Class Wind undertuned (WR: 25.9%, factor: 1.096); Individual spell undertuned (WR: 11.5%, Casts: 11179, mult: 1.158) |
| `ELL` | Wind | Buff / Sustain | 76.1 -> **82.0** (+7.8%) | - | 76.1 -> **82.0** | Class Wind undertuned (WR: 25.9%, factor: 1.096); Individual spell overtuned (WR: 55.0%, Casts: 819, mult: 0.983) |
| `ELD` | Wind | Conditional Strike | 3.0 -> **2.8** (-6.7%) | 5412.7 -> **7833.8** | 16241.1 -> **21937.4** | Class Wind undertuned (WR: 25.9%, factor: 1.096); Weather 'Raining' beneficiaries undertuned (WR: 35.0%) |
| `LEF` | Wind | Conditional Strike | 1.1 -> **1.1** (+0.0%) | 4956.4 -> **7364.9** | 5453.1 -> **8102.5** | Class Wind undertuned (WR: 25.9%, factor: 1.096); Status 'Burning' beneficiaries undertuned (WR: 27.5%) |
| `LEW` | Wind | Debuff / Control | 20.3 -> **19.7** (-3.0%) | - | 20.3 -> **19.7** | Class Wind undertuned (WR: 25.9%, factor: 1.096); Individual spell overtuned (WR: 78.9%, Casts: 2902, mult: 0.885) |
| `LEE` | Wind | Setup - Weather | 182.8 -> **222.6** (+21.8%) | - | 182.8 -> **222.6** | Class Wind undertuned (WR: 25.9%, factor: 1.096); Individual spell undertuned (WR: 22.0%, Casts: 3048, mult: 1.111) |
| `LEL` | Wind | Buff / Sustain | 231.9 -> **298.1** (+28.5%) | - | 231.9 -> **298.1** | Class Wind undertuned (WR: 25.9%, factor: 1.096); Individual spell undertuned (WR: 8.2%, Casts: 5022, mult: 1.172) |
| `EDF` | Poison | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 1886.5 -> **2580.4** | 566.2 -> **516.3** | Class Poison overtuned (WR: 55.1%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1538). Increasing spread: b -17.9%, n +36.8% |
| `EDW` | Poison | Debuff / Control | 3.7 -> **3.2** (-13.5%) | - | 3.7 -> **3.2** | Class Poison overtuned (WR: 55.1%, factor: 0.979); Individual spell overtuned (WR: 82.4%, Casts: 3935, mult: 0.870) |
| `EDE` | Poison | Setup - Location | 314.8 -> **397.4** (+26.2%) | - | 314.8 -> **397.4** | Class Poison overtuned (WR: 55.1%, factor: 0.979); Location 'Swamp' appliers undertuned (WR: 13.0%, casts: 4257) |
| `EDD` | Poison | Ultimate | 5.5 -> **5.9** (+7.3%) | 417.2 -> **425.0** | 2300.1 -> **2513.4** | Class Poison overtuned (WR: 55.1%, factor: 0.979); Status 'Bleeding' beneficiaries undertuned (WR: 35.7%) |
| `DEF` | Poison | Conditional Strike | 2.9 -> **2.5** (-13.8%) | 26.8 -> **36.7** | 80.6 -> **94.2** | Class Poison overtuned (WR: 55.1%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 35). Increasing spread: b -18.0%, n +37.0% |
| `DEE` | Poison | Debuff / Control | 13.1 -> **11.6** (-11.5%) | - | 13.1 -> **11.6** | Class Poison overtuned (WR: 55.1%, factor: 0.979); Individual spell overtuned (WR: 74.6%, Casts: 8060, mult: 0.904) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 6995.5 -> **10131.6** | 2098.9 -> **3039.8** | Class Poison overtuned (WR: 55.1%, factor: 0.979); Status 'Bleeding' beneficiaries undertuned (WR: 35.7%) |
| `DED` | Poison | Debuff / Control | 13.5 -> **12.3** (-8.9%) | - | 13.5 -> **12.3** | Class Poison overtuned (WR: 55.1%, factor: 0.979); Individual spell overtuned (WR: 68.4%, Casts: 3263, mult: 0.930) |
| `LDF` | Cosmic | Debuff / Control | 22.9 -> **18.7** (-18.3%) | - | 22.9 -> **18.7** | Class Cosmic overtuned (WR: 57.3%, factor: 0.971); Individual spell overtuned (WR: 89.2%, Casts: 3774, mult: 0.839) |
| `LDW` | Cosmic | Debuff / Control | 7.4 -> **7.3** (-1.4%) | - | 7.4 -> **7.3** | Class Cosmic overtuned (WR: 57.3%, factor: 0.971); Status 'Stunned' appliers overtuned on own (WR: 56.9%) |
| `LDE` | Cosmic | Setup - Location | 79.7 -> **72.8** (-8.7%) | - | 79.7 -> **72.8** | Class Cosmic overtuned (WR: 57.3%, factor: 0.971); Individual spell overtuned (WR: 65.8%, Casts: 1532, mult: 0.941) |
| `LDL` | Cosmic | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 2474.9 -> **3390.6** | 1980.7 -> **2374.1** | Class Cosmic overtuned (WR: 57.3%, factor: 0.971); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1076). Increasing spread: b -18.0%, n +37.0% |
| `LDD` | Cosmic | Ultimate | 5.5 -> **6.1** (+10.9%) | 170.6 -> **160.4** | 943.8 -> **984.5** | Class Cosmic overtuned (WR: 57.3%, factor: 0.971); Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 5659, WR: 34.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 2246.3 -> **3077.4** | 1797.8 -> **2154.9** | Class Cosmic overtuned (WR: 57.3%, factor: 0.971); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 523). Increasing spread: b -18.0%, n +37.0% |
| `DLW` | Cosmic | Direct Damage | 12.1 -> **11.1** (-8.3%) | - | 12.1 -> **11.1** | Class Cosmic overtuned (WR: 57.3%, factor: 0.971); Individual spell overtuned (WR: 64.3%, Casts: 1591, mult: 0.947) |
| `DLE` | Cosmic | Direct Damage | 265.2 -> **284.2** (+7.2%) | - | 265.2 -> **284.2** | Class Cosmic overtuned (WR: 57.3%, factor: 0.971); Individual spell undertuned (WR: 23.5%, Casts: 4274, mult: 1.104) |
| `DLL` | Cosmic | Conditional Strike | 1.0 -> **0.7** (-30.0%) | 2308.8 -> **3249.7** | 2309.8 -> **2275.5** | Class Cosmic overtuned (WR: 57.3%, factor: 0.971); Weather 'Darkness' beneficiaries undertuned (WR: 43.1%) |
