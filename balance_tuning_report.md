# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T19:02:38Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 131.0s  
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
| **Earth** | 18,172 | 77.2% | 77.3% | 13.6 | Overtuned ⚠️ |
| **Ghostfire** | 28,111 | 61.2% | 61.2% | 2.3 | Overtuned ⚠️ |
| **Water** | 8,036 | 60.5% | 60.5% | 4.2 | Overtuned ⚠️ |
| **Poison** | 45,325 | 58.0% | 58.0% | 3.0 | Overtuned ⚠️ |
| **Fire** | 20,411 | 57.6% | 57.7% | 3.0 | Overtuned ⚠️ |
| **Blood** | 25,332 | 55.3% | 55.3% | 5.7 | Overtuned ⚠️ |
| **Ice** | 39,411 | 52.4% | 52.4% | 3.1 | Balanced ✅ |
| **Cosmic** | 23,826 | 49.4% | 49.4% | 3.1 | Balanced ✅ |
| **Plants** | 22,833 | 48.9% | 48.9% | 2.5 | Balanced ✅ |
| **Lightning** | 18,173 | 47.3% | 47.3% | 1.4 | Balanced ✅ |
| **Light** | 20,583 | 46.9% | 46.9% | 2.1 | Balanced ✅ |
| **Beasts** | 31,707 | 42.8% | 42.8% | 2.2 | Undertuned ⚠️ |
| **Fey** | 24,810 | 40.7% | 40.7% | 2.5 | Undertuned ⚠️ |
| **Dark** | 13,305 | 32.9% | 32.9% | 1.4 | Undertuned ⚠️ |
| **Wind** | 32,297 | 24.0% | 24.0% | 0.8 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 21,058 (57.5%) | 2,629 (60.9%) | 16.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,794 (46.2%) | 13,934 (46.3%) | 0.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 9,468 (76.9%) | 9,414 (23.1%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,100 (89.1%) | 27,885 (37.4%) | 0.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 10,419 (60.1%) | 2,903 (39.8%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 4,277 (50.9%) | 5,611 (43.2%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 130 (23.1%) | 1,845 (24.2%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 13.8 -> **11.8** (-14.5%) | - | 13.8 -> **11.8** | Class Fire overtuned (WR: 57.6%, factor: 0.969); Individual spell overtuned (WR: 78.8%, Casts: 3810, mult: 0.886) |
| `FFW` | Fire | Debuff / Control | 5.9 -> **5.3** (-10.2%) | - | 5.9 -> **5.3** | Class Fire overtuned (WR: 57.6%, factor: 0.969); Status 'Burning' appliers overtuned on own (WR: 76.9%) |
| `FFE` | Fire | Debuff / Control | 7.5 -> **6.6** (-12.0%) | - | 7.5 -> **6.6** | Class Fire overtuned (WR: 57.6%, factor: 0.969); Individual spell overtuned (WR: 72.5%, Casts: 3437, mult: 0.913) |
| `FFD` | Fire | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 7109.9 -> **10789.3** | 5688.7 -> **7553.2** | Class Fire overtuned (WR: 57.6%, factor: 0.969); Status 'Burning' beneficiaries undertuned (WR: 23.1%) |
| `WWF` | Water | Conditional Strike | 0.9 -> **0.7** (-22.2%) | 3719.6 -> **5645.2** | 3348.5 -> **3952.3** | Class Water overtuned (WR: 60.5%, factor: 0.958); Status 'Burning' beneficiaries undertuned (WR: 23.1%) |
| `WWE` | Water | Setup - Weather | 291.6 -> **338.9** (+16.2%) | - | 291.6 -> **338.9** | Class Water overtuned (WR: 60.5%, factor: 0.958); Weather 'Raining' appliers undertuned (WR: 23.1%, casts: 130) |
| `WWL` | Water | Buff / Sustain | 11.6 -> **10.4** (-10.3%) | - | 11.6 -> **10.4** | Class Water overtuned (WR: 60.5%, factor: 0.958); Individual spell overtuned (WR: 66.7%, Casts: 6037, mult: 0.937) |
| `WWD` | Water | Buff / Sustain | 22.5 -> **23.0** (+2.2%) | - | 22.5 -> **23.0** | Class Water overtuned (WR: 60.5%, factor: 0.958); Individual spell undertuned (WR: 31.9%, Casts: 776, mult: 1.069) |
| `EEF` | Earth | Conditional Strike | 0.7 -> **0.5** (-28.6%) | 5869.9 -> **6861.1** | 4109.6 -> **3431.1** | Class Earth overtuned (WR: 77.2%, factor: 0.891); Status 'Frosty' beneficiaries overtuned (WR: 60.9%) |
| `EEW` | Earth | Buff / Sustain | 29.9 -> **24.4** (-18.4%) | - | 29.9 -> **24.4** | Class Earth overtuned (WR: 77.2%, factor: 0.891); Individual spell overtuned (WR: 71.6%, Casts: 1923, mult: 0.917) |
| `EEE` | Earth | Conditional Strike | 10.0 -> **9.7** (-3.0%) | 1.5 -> **1.5** | 25.0 -> **24.2** | Class Earth overtuned (WR: 77.2%, factor: 0.891); Condition triggers excessively (N=1 conditions, Trigger Rate: 93.8% vs 55% ceiling, WR: 89.4%). Compressing spread: b +29.4%, n -37.5% |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 2966.7 -> **4042.4** | 296.8 -> **404.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 1125). Increasing spread: b -17.6%, n +36.3% |
| `LLW` | Light | Debuff / Control | 9.8 -> **9.4** (-4.1%) | - | 9.8 -> **9.4** | Individual spell overtuned (WR: 60.1%, Casts: 4355, mult: 0.964) |
| `LLE` | Light | Setup - Weather | 608.6 -> **624.4** (+2.6%) | - | 608.6 -> **624.4** | Weather 'Sunny' appliers undertuned (WR: 46.2%, casts: 1794); Individual spell undertuned (WR: 46.2%, Casts: 1794, mult: 1.012) |
| `LLL` | Light | Buff / Sustain | 6.5 -> **6.7** (+3.1%) | - | 6.5 -> **6.7** | Individual spell undertuned (WR: 43.2%, Casts: 2413, mult: 1.023) |
| `LLD` | Light | Ultimate | 4.2 -> **4.7** (+11.9%) | 546.2 -> **521.1** | 2298.2 -> **2453.9** | Weather 'Sunny' beneficiaries undertuned (WR: 46.3%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 10896, WR: 42.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 4074.4 -> **5581.9** | 1630.2 -> **2233.2** | Class Dark undertuned (WR: 32.9%, factor: 1.068); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 8536). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 10.6 -> **10.9** (+2.8%) | - | 10.6 -> **10.9** | Class Dark undertuned (WR: 32.9%, factor: 1.068); Individual spell overtuned (WR: 61.4%, Casts: 959, mult: 0.959) |
| `DDE` | Dark | Setup - Weather | 433.1 -> **447.7** (+3.4%) | - | 433.1 -> **447.7** | Class Dark undertuned (WR: 32.9%, factor: 1.068); Weather 'Darkness' appliers overtuned on own (WR: 54.8%) |
| `DDL` | Dark | Debuff / Control | 8.9 -> **9.1** (+2.2%) | - | 8.9 -> **9.1** | Class Dark undertuned (WR: 32.9%, factor: 1.068); Individual spell overtuned (WR: 61.4%, Casts: 2688, mult: 0.959) |
| `DDD` | Dark | Debuff / Control | 3.3 -> **3.4** (+3.0%) | - | 3.3 -> **3.4** | Class Dark undertuned (WR: 32.9%, factor: 1.068); Individual spell overtuned (WR: 59.1%, Casts: 917, mult: 0.968) |
| `FWF` | Ghostfire | Debuff / Control | 0.7 -> **0.5** (-28.6%) | - | 0.7 -> **0.5** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Status 'Burning' appliers overtuned on own (WR: 76.9%) |
| `FWW` | Ghostfire | Debuff / Control | 4.3 -> **4.0** (-7.0%) | - | 4.3 -> **4.0** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Status 'Cursed' appliers overtuned on own (WR: 60.5%) |
| `FWE` | Ghostfire | Setup - Location | 97.3 -> **107.6** (+10.6%) | - | 97.3 -> **107.6** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Location 'Graveyard' appliers undertuned (WR: 29.4%, casts: 313) |
| `FWL` | Ghostfire | Debuff / Control | 10.7 -> **9.5** (-11.2%) | - | 10.7 -> **9.5** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Status 'Cursed' appliers overtuned on own (WR: 60.5%) |
| `FWD` | Ghostfire | Ultimate | 3.5 -> **2.7** (-22.9%) | 187.4 -> **256.7** | 659.4 -> **695.8** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 631). Increasing spread: b -18.0%, n +37.0% |
| `WFF` | Ghostfire | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 10290.5 -> **14322.1** | 5145.8 -> **5729.2** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Status 'Bleeding' beneficiaries undertuned (WR: 37.4%) |
| `WFW` | Ghostfire | Debuff / Control | 3.9 -> **3.5** (-10.3%) | - | 3.9 -> **3.5** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Individual spell overtuned (WR: 63.8%, Casts: 7645, mult: 0.949) |
| `WFE` | Ghostfire | Debuff / Control | 0.4 -> **0.3** (-25.0%) | - | 0.4 -> **0.3** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Status 'Bleeding' appliers overtuned on own (WR: 89.1%) |
| `WFL` | Ghostfire | Buff / Sustain | 44.0 -> **36.5** (-17.0%) | - | 44.0 -> **36.5** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Individual spell overtuned (WR: 82.7%, Casts: 370, mult: 0.868) |
| `WFD` | Ghostfire | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 3372.4 -> **4616.5** | 2024.0 -> **2308.8** | Class Ghostfire overtuned (WR: 61.2%, factor: 0.955); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 3041). Increasing spread: b -17.9%, n +36.9% |
| `FEF` | Beasts | Debuff / Control | 10.0 -> **9.7** (-3.0%) | - | 10.0 -> **9.7** | Class Beasts undertuned (WR: 42.8%, factor: 1.029); Individual spell overtuned (WR: 66.5%, Casts: 4389, mult: 0.938) |
| `FEW` | Beasts | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 5953.0 -> **8378.4** | 2381.6 -> **2513.8** | Class Beasts undertuned (WR: 42.8%, factor: 1.029); Status 'Entangled' beneficiaries undertuned (WR: 43.2%) |
| `FEE` | Beasts | Buff / Sustain | 127.0 -> **153.8** (+21.1%) | - | 127.0 -> **153.8** | Class Beasts undertuned (WR: 42.8%, factor: 1.029); Individual spell undertuned (WR: 7.1%, Casts: 5142, mult: 1.177) |
| `FEL` | Beasts | Buff / Sustain | 152.3 -> **180.4** (+18.5%) | - | 152.3 -> **180.4** | Class Beasts undertuned (WR: 42.8%, factor: 1.029); Individual spell undertuned (WR: 12.8%, Casts: 4683, mult: 1.151) |
| `FED` | Beasts | Conditional Strike | 2.1 -> **2.0** (-4.8%) | 3.5 -> **3.5** | 9.5 -> **9.0** | Class Beasts undertuned (WR: 42.8%, factor: 1.029); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 17). Increasing spread: b -18.0%, n +37.0% |
| `EFF` | Beasts | Debuff / Control | 0.5 -> **0.5** (+0.0%) | 3638.2 -> **4984.3** | 1819.6 -> **2492.7** | Class Beasts undertuned (WR: 42.8%, factor: 1.029); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3297). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 80.2 -> **71.9** (-10.3%) | - | 80.2 -> **71.9** | Class Beasts undertuned (WR: 42.8%, factor: 1.029); Individual spell overtuned (WR: 81.9%, Casts: 93, mult: 0.872) |
| `EFE` | Beasts | Buff / Sustain | 11.8 -> **10.8** (-8.5%) | - | 11.8 -> **10.8** | Class Beasts undertuned (WR: 42.8%, factor: 1.029); Individual spell overtuned (WR: 78.3%, Casts: 5950, mult: 0.888) |
| `EFD` | Beasts | Ultimate | 4.5 -> **5.2** (+15.6%) | 554.1 -> **558.6** | 2498.0 -> **2909.9** | Class Beasts undertuned (WR: 42.8%, factor: 1.029); Status 'Entangled' beneficiaries undertuned (WR: 43.2%) |
| `FLF` | Lightning | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 6958.1 -> **9920.0** | 4175.5 -> **4960.5** | Status 'Stunned' beneficiaries undertuned (WR: 39.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2707). Increasing spread: b -18.0%, n +37.0% |
| `FLW` | Lightning | Debuff / Control | 7.6 -> **6.8** (-10.5%) | - | 7.6 -> **6.8** | Status 'Stunned' appliers overtuned on own (WR: 60.1%); Individual spell overtuned (WR: 67.9%, Casts: 3497, mult: 0.932) |
| `FLD` | Lightning | Ultimate | 4.5 -> **3.3** (-26.7%) | 471.8 -> **598.7** | 2127.6 -> **1979.0** | Status 'Stunned' beneficiaries undertuned (WR: 39.8%); Weather 'Storming' beneficiaries overtuned (WR: 77.5%) |
| `LFF` | Lightning | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 3863.3 -> **5292.7** | 3477.9 -> **4235.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4978). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 36.4%, Casts: 4978, mult: 1.050) |
| `LFW` | Lightning | Buff / Sustain | 18.9 -> **20.2** (+6.9%) | - | 18.9 -> **20.2** | Individual spell undertuned (WR: 31.4%, Casts: 672, mult: 1.071) |
| `LFE` | Lightning | Debuff / Control | 7.3 -> **6.5** (-11.0%) | - | 7.3 -> **6.5** | Status 'Stunned' appliers overtuned on own (WR: 60.1%); Individual spell overtuned (WR: 69.5%, Casts: 2240, mult: 0.926) |
| `LFL` | Lightning | Debuff / Control | 1.0 -> **0.9** (-10.0%) | 2754.5 -> **3987.9** | 2755.5 -> **3590.0** | Weather 'Darkness' beneficiaries undertuned (WR: 35.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1701). Increasing spread: b -18.0%, n +37.0% |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 4074.4 -> **5581.9** | 815.1 -> **1116.6** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3143). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 80.6 -> **90.6** (+12.4%) | - | 80.6 -> **90.6** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Individual spell undertuned (WR: 13.5%, Casts: 778, mult: 1.148) |
| `FDE` | Blood | Setup - Weather | 48.3 -> **51.1** (+5.8%) | - | 48.3 -> **51.1** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Individual spell undertuned (WR: 29.2%, Casts: 546, mult: 1.080) |
| `FDD` | Blood | Ultimate | 2.7 -> **3.0** (+11.1%) | 193.2 -> **191.9** | 524.3 -> **578.7** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Weather 'Darkness' beneficiaries undertuned (WR: 35.8%) |
| `DFF` | Blood | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 7325.3 -> **10390.2** | 4395.8 -> **5195.6** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Status 'Bleeding' beneficiaries undertuned (WR: 37.4%) |
| `DFE` | Blood | Buff / Sustain | 286.7 -> **331.2** (+15.5%) | - | 286.7 -> **331.2** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Individual spell undertuned (WR: 5.7%, Casts: 582, mult: 1.180) |
| `DFL` | Blood | Buff / Sustain | 5.1 -> **4.6** (-9.8%) | - | 5.1 -> **4.6** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Individual spell overtuned (WR: 70.7%, Casts: 2424, mult: 0.920) |
| `DFD` | Blood | Conditional Strike | 134.1 -> **139.6** (+4.1%) | 0.1 -> **0.1** | 147.5 -> **153.6** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Condition triggers excessively (N=1 conditions, Trigger Rate: 87.2% vs 55% ceiling, WR: 92.9%). Compressing spread: b +29.3%, n -36.6% |
| `WEF` | Plants | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 5040.5 -> **7050.9** | 3024.9 -> **3525.9** | Location 'Jungle' beneficiaries undertuned (WR: 39.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.6% vs 30% floor, Casts: 2722). Increasing spread: b -16.6%, n +34.0% |
| `WEW` | Plants | Debuff / Control | 120.0 -> **135.8** (+13.2%) | - | 120.0 -> **135.8** | Individual spell undertuned (WR: 17.2%, Casts: 2680, mult: 1.132) |
| `WEE` | Plants | Setup - Location | 706.0 -> **901.2** (+27.6%) | - | 706.0 -> **901.2** | Location 'Jungle' appliers undertuned (WR: 15.6%, casts: 738); Individual spell undertuned (WR: 15.5%, Casts: 738, mult: 1.140) |
| `WED` | Plants | Conditional Strike | 7.1 -> **5.8** (-18.3%) | 64.7 -> **88.6** | 466.5 -> **519.7** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 6578). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 1.4 -> **1.1** (-21.4%) | 6710.7 -> **9226.8** | 9396.4 -> **10150.6** | Weather 'Sunny' beneficiaries undertuned (WR: 46.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 3038). Increasing spread: b -17.3%, n +35.5% |
| `EWW` | Plants | Debuff / Control | 0.9 -> **0.7** (-22.2%) | - | 0.9 -> **0.7** | Individual spell overtuned (WR: 91.1%, Casts: 662, mult: 0.831) |
| `EWL` | Plants | Debuff / Control | 13.2 -> **12.0** (-9.1%) | - | 13.2 -> **12.0** | Individual spell overtuned (WR: 73.7%, Casts: 2079, mult: 0.908) |
| `EWD` | Plants | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 5777.7 -> **7775.6** | 577.9 -> **777.7** | Status 'Bleeding' appliers overtuned on own (WR: 89.1%); Status 'Entangled' beneficiaries undertuned (WR: 43.2%) |
| `WLF` | Fey | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 3239.3 -> **4437.8** | 2916.3 -> **3551.0** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1122). Increasing spread: b -18.0%, n +37.0% |
| `WLW` | Fey | Debuff / Control | 8.5 -> **8.0** (-5.9%) | - | 8.5 -> **8.0** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Status 'Cursed' appliers overtuned on own (WR: 60.5%) |
| `WLE` | Fey | Setup - Location | 1542.6 -> **1670.0** (+8.3%) | - | 1542.6 -> **1670.0** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Location 'Enchanted Forest' appliers undertuned (WR: 43.8%, casts: 962) |
| `WLL` | Fey | Direct Damage | 26.7 -> **24.3** (-9.0%) | - | 26.7 -> **24.3** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Individual spell overtuned (WR: 80.4%, Casts: 2361, mult: 0.879) |
| `WLD` | Fey | Ultimate | 4.8 -> **5.6** (+16.7%) | 610.7 -> **653.1** | 2936.2 -> **3663.0** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Weather 'Darkness' beneficiaries undertuned (WR: 35.8%) |
| `LWF` | Fey | Debuff / Control | 1.8 -> **1.7** (-5.6%) | 4149.6 -> **6108.7** | 7471.1 -> **10386.5** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Location 'Enchanted Forest' beneficiaries undertuned (WR: 30.9%) |
| `LWW` | Fey | Debuff / Control | 103.5 -> **123.6** (+19.4%) | - | 103.5 -> **123.6** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Individual spell undertuned (WR: 12.9%, Casts: 3340, mult: 1.151) |
| `LWL` | Fey | Debuff / Control | 479.2 -> **531.1** (+10.8%) | - | 479.2 -> **531.1** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Individual spell undertuned (WR: 31.9%, Casts: 1159, mult: 1.068) |
| `LWD` | Fey | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 4074.4 -> **5581.9** | 3260.3 -> **3908.0** | Class Fey undertuned (WR: 40.7%, factor: 1.037); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1134). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 8826.2 -> **13341.2** | 4413.6 -> **5336.9** | Status 'Stunned' appliers overtuned on own (WR: 60.1%); Weather 'Raining' beneficiaries undertuned (WR: 24.2%) |
| `WDW` | Ice | Buff / Sustain | 37.9 -> **37.7** (-0.5%) | - | 37.9 -> **37.7** | Status 'Frosty' appliers overtuned on own (WR: 57.5%); Individual spell undertuned (WR: 43.7%, Casts: 1657, mult: 1.021) |
| `WDE` | Ice | Setup - Weather | 158.7 -> **183.0** (+15.3%) | - | 158.7 -> **183.0** | Individual spell undertuned (WR: 12.5%, Casts: 1100, mult: 1.153) |
| `WDL` | Ice | Debuff / Control | 8.3 -> **7.9** (-4.8%) | - | 8.3 -> **7.9** | Status 'Frosty' appliers overtuned on own (WR: 57.5%); Individual spell overtuned (WR: 57.0%, Casts: 2997, mult: 0.976) |
| `WDD` | Ice | Ultimate | 4.6 -> **5.1** (+10.9%) | 125.8 -> **123.2** | 583.3 -> **633.4** | Weather 'Blizzard' beneficiaries undertuned (WR: 44.8%); Location 'Tundra' beneficiaries undertuned (WR: 44.8%) |
| `DWF` | Ice | Debuff / Control | 7.3 -> **6.9** (-5.5%) | - | 7.3 -> **6.9** | Status 'Frosty' appliers overtuned on own (WR: 57.5%); Individual spell overtuned (WR: 57.7%, Casts: 7892, mult: 0.973) |
| `DWW` | Ice | Debuff / Control | 10.2 -> **9.6** (-5.9%) | - | 10.2 -> **9.6** | Individual spell overtuned (WR: 66.9%, Casts: 4651, mult: 0.936) |
| `DWE` | Ice | Setup - Location | 239.5 -> **277.1** (+15.7%) | - | 239.5 -> **277.1** | Location 'Tundra' appliers undertuned (WR: 29.4%, casts: 1085); Individual spell undertuned (WR: 29.3%, Casts: 1085, mult: 1.079) |
| `DWL` | Ice | Debuff / Control | 10.8 -> **10.1** (-6.5%) | - | 10.8 -> **10.1** | Status 'Frosty' appliers overtuned on own (WR: 57.5%); Individual spell overtuned (WR: 60.2%, Casts: 8512, mult: 0.963) |
| `DWD` | Ice | Conditional Strike | 0.8 -> **0.6** (-25.0%) | 4254.4 -> **5553.4** | 3404.3 -> **3332.6** | Status 'Frosty' beneficiaries overtuned (WR: 60.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 157). Increasing spread: b -17.7%, n +36.5% |
| `ELF` | Wind | Conditional Strike | 2.0 -> **1.9** (-5.0%) | 8358.6 -> **11910.7** | 16719.2 -> **22632.2** | Class Wind undertuned (WR: 24.0%, factor: 1.104); Status 'Bleeding' beneficiaries undertuned (WR: 37.4%) |
| `ELW` | Wind | Debuff / Control | 22.0 -> **23.4** (+6.4%) | - | 22.0 -> **23.4** | Class Wind undertuned (WR: 24.0%, factor: 1.104); Individual spell overtuned (WR: 60.6%, Casts: 130, mult: 0.962) |
| `ELE` | Wind | Setup - Weather | 153.0 -> **195.1** (+27.5%) | - | 153.0 -> **195.1** | Class Wind undertuned (WR: 24.0%, factor: 1.104); Individual spell undertuned (WR: 12.0%, Casts: 8345, mult: 1.155) |
| `ELL` | Wind | Buff / Sustain | 82.0 -> **94.0** (+14.6%) | - | 82.0 -> **94.0** | Class Wind undertuned (WR: 24.0%, factor: 1.104); Individual spell undertuned (WR: 39.4%, Casts: 707, mult: 1.038) |
| `ELD` | Wind | Conditional Strike | 2.8 -> **3.0** (+7.1%) | 7833.8 -> **11841.2** | 21937.4 -> **35526.6** | Class Wind undertuned (WR: 24.0%, factor: 1.104); Weather 'Raining' beneficiaries undertuned (WR: 24.2%) |
| `LEF` | Wind | Conditional Strike | 1.1 -> **1.1** (+0.0%) | 7364.9 -> **11177.6** | 8102.5 -> **12296.5** | Class Wind undertuned (WR: 24.0%, factor: 1.104); Status 'Burning' beneficiaries undertuned (WR: 23.1%) |
| `LEW` | Wind | Debuff / Control | 19.7 -> **19.8** (+0.5%) | - | 19.7 -> **19.8** | Class Wind undertuned (WR: 24.0%, factor: 1.104); Individual spell overtuned (WR: 72.5%, Casts: 1233, mult: 0.913) |
| `LEE` | Wind | Setup - Weather | 222.6 -> **280.8** (+26.1%) | - | 222.6 -> **280.8** | Class Wind undertuned (WR: 24.0%, factor: 1.104); Individual spell undertuned (WR: 14.8%, Casts: 4405, mult: 1.143) |
| `LEL` | Wind | Buff / Sustain | 298.1 -> **385.2** (+29.2%) | - | 298.1 -> **385.2** | Class Wind undertuned (WR: 24.0%, factor: 1.104); Individual spell undertuned (WR: 8.6%, Casts: 4631, mult: 1.170) |
| `EDF` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 2580.4 -> **3528.9** | 516.3 -> **706.0** | Class Poison overtuned (WR: 58.0%, factor: 0.968); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 697). Increasing spread: b -17.9%, n +36.8% |
| `EDW` | Poison | Debuff / Control | 3.2 -> **2.9** (-9.4%) | - | 3.2 -> **2.9** | Class Poison overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 65.6%, Casts: 5442, mult: 0.942) |
| `EDE` | Poison | Setup - Location | 397.4 -> **452.6** (+13.9%) | - | 397.4 -> **452.6** | Class Poison overtuned (WR: 58.0%, factor: 0.968); Location 'Swamp' appliers undertuned (WR: 27.0%, casts: 3027) |
| `EDD` | Poison | Ultimate | 5.9 -> **6.3** (+6.8%) | 425.0 -> **427.8** | 2513.4 -> **2701.4** | Class Poison overtuned (WR: 58.0%, factor: 0.968); Status 'Bleeding' beneficiaries undertuned (WR: 37.4%) |
| `DEF` | Poison | Conditional Strike | 2.5 -> **1.7** (-32.0%) | 36.7 -> **50.2** | 94.2 -> **87.0** | Class Poison overtuned (WR: 58.0%, factor: 0.968); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 349). Increasing spread: b -17.9%, n +36.8% |
| `DEW` | Poison | Debuff / Control | 3.4 -> **3.2** (-5.9%) | - | 3.4 -> **3.2** | Class Poison overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 57.1%, Casts: 3519, mult: 0.975) |
| `DEE` | Poison | Debuff / Control | 11.6 -> **9.9** (-14.7%) | - | 11.6 -> **9.9** | Class Poison overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 79.6%, Casts: 8086, mult: 0.882) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 10131.6 -> **14582.6** | 3039.8 -> **4375.1** | Class Poison overtuned (WR: 58.0%, factor: 0.968); Status 'Bleeding' beneficiaries undertuned (WR: 37.4%) |
| `DED` | Poison | Debuff / Control | 12.3 -> **10.6** (-13.8%) | - | 12.3 -> **10.6** | Class Poison overtuned (WR: 58.0%, factor: 0.968); Individual spell overtuned (WR: 78.5%, Casts: 4117, mult: 0.887) |
| `LDF` | Cosmic | Debuff / Control | 18.7 -> **16.6** (-11.2%) | - | 18.7 -> **16.6** | Individual spell overtuned (WR: 78.6%, Casts: 3840, mult: 0.886) |
| `LDW` | Cosmic | Debuff / Control | 7.3 -> **6.2** (-15.1%) | - | 7.3 -> **6.2** | Status 'Stunned' appliers overtuned on own (WR: 60.1%); Individual spell overtuned (WR: 79.8%, Casts: 645, mult: 0.881) |
| `LDE` | Cosmic | Setup - Location | 72.8 -> **69.8** (-4.1%) | - | 72.8 -> **69.8** | Individual spell overtuned (WR: 61.5%, Casts: 614, mult: 0.958) |
| `LDL` | Cosmic | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 3390.6 -> **4645.1** | 2374.1 -> **2787.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 8538). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 28.1%, Casts: 8538, mult: 1.085) |
| `LDD` | Cosmic | Ultimate | 6.1 -> **5.0** (-18.0%) | 160.4 -> **219.7** | 984.5 -> **1103.5** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 4628). Increasing spread: b -18.0%, n +37.0% |
| `DLF` | Cosmic | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 3077.4 -> **4216.0** | 2154.9 -> **2530.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1772). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 57.0%, Casts: 1772, mult: 0.976) |
| `DLW` | Cosmic | Direct Damage | 11.1 -> **10.6** (-4.5%) | - | 11.1 -> **10.6** | Individual spell overtuned (WR: 63.0%, Casts: 915, mult: 0.952) |
| `DLE` | Cosmic | Direct Damage | 284.2 -> **290.6** (+2.3%) | - | 284.2 -> **290.6** | Individual spell undertuned (WR: 43.5%, Casts: 936, mult: 1.022) |
| `DLL` | Cosmic | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 3249.7 -> **4686.2** | 2275.5 -> **2812.3** | Weather 'Darkness' beneficiaries undertuned (WR: 35.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 1222). Increasing spread: b -17.7%, n +36.5% |
