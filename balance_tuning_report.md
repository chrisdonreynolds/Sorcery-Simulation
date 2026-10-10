# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T19:47:08Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 106.0s  
**Total Spells Tuned:** 104 / 125  

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
| **Dark** | 11,461 | 71.8% | 71.9% | 3.1 | Overtuned ⚠️ |
| **Cosmic** | 22,820 | 61.9% | 62.0% | 5.0 | Overtuned ⚠️ |
| **Blood** | 27,426 | 61.3% | 61.3% | 10.2 | Overtuned ⚠️ |
| **Earth** | 14,594 | 61.1% | 61.1% | 13.4 | Overtuned ⚠️ |
| **Light** | 10,834 | 58.2% | 58.2% | 2.4 | Overtuned ⚠️ |
| **Fire** | 15,086 | 53.5% | 53.5% | 2.3 | Overtuned ⚠️ |
| **Poison** | 32,590 | 52.8% | 52.8% | 2.0 | Balanced ✅ |
| **Ghostfire** | 27,563 | 52.6% | 52.6% | 1.3 | Balanced ✅ |
| **Water** | 9,339 | 48.3% | 48.3% | 1.8 | Balanced ✅ |
| **Beasts** | 24,279 | 47.6% | 47.6% | 5.3 | Balanced ✅ |
| **Ice** | 38,341 | 47.0% | 47.0% | 2.9 | Balanced ✅ |
| **Lightning** | 14,911 | 41.8% | 41.8% | 0.6 | Undertuned ⚠️ |
| **Plants** | 31,646 | 38.9% | 38.9% | 1.8 | Undertuned ⚠️ |
| **Wind** | 27,342 | 37.0% | 37.0% | 1.8 | Undertuned ⚠️ |
| **Fey** | 26,636 | 37.0% | 37.0% | 2.0 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 21,272 (54.8%) | 4,993 (26.2%) | 3.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 623 (49.0%) | 6,473 (36.5%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,158 (52.3%) | 6,741 (34.8%) | 2.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 11,375 (88.4%) | 17,574 (43.5%) | 0.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 10,417 (42.8%) | 3,174 (44.9%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,737 (53.9%) | 3,630 (29.8%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,852 (34.4%) | 3,477 (24.5%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 8.0 -> **7.2** (-10.0%) | - | 8.0 -> **7.2** | Class Fire overtuned (WR: 53.5%, factor: 0.986); Individual spell overtuned (WR: 73.6%, Casts: 4270, mult: 0.908) |
| `FFE` | Fire | Debuff / Control | 4.7 -> **4.6** (-2.1%) | - | 4.7 -> **4.6** | Class Fire overtuned (WR: 53.5%, factor: 0.986) |
| `FFD` | Fire | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 22461.0 -> **32449.4** | 11231.0 -> **12980.2** | Class Fire overtuned (WR: 53.5%, factor: 0.986); Status 'Burning' beneficiaries undertuned (WR: 34.8%) |
| `WWF` | Water | Conditional Strike | 0.6 -> **0.6** (+0.0%) | 11216.7 -> **15432.4** | 6730.6 -> **9260.0** | Status 'Burning' beneficiaries undertuned (WR: 34.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.8% vs 30% floor, Casts: 343). Increasing spread: b -14.5%, n +29.7% |
| `WWE` | Water | Setup - Weather | 426.6 -> **476.1** (+11.6%) | - | 426.6 -> **476.1** | Weather 'Raining' appliers undertuned (WR: 34.4%, casts: 2852); Individual spell undertuned (WR: 34.4%, Casts: 2852, mult: 1.058) |
| `WWL` | Water | Buff / Sustain | 8.4 -> **7.7** (-8.3%) | - | 8.4 -> **7.7** | Individual spell overtuned (WR: 72.6%, Casts: 3874, mult: 0.912) |
| `WWD` | Water | Buff / Sustain | 27.6 -> **30.1** (+9.1%) | - | 27.6 -> **30.1** | Individual spell undertuned (WR: 26.3%, Casts: 307, mult: 1.092) |
| `EEF` | Earth | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 11489.5 -> **16534.3** | 3447.2 -> **4960.6** | Class Earth overtuned (WR: 61.1%, factor: 0.956); Status 'Frosty' beneficiaries undertuned (WR: 26.2%) |
| `EEW` | Earth | Buff / Sustain | 25.5 -> **25.9** (+1.6%) | - | 25.5 -> **25.9** | Class Earth overtuned (WR: 61.1%, factor: 0.956); Individual spell undertuned (WR: 32.9%, Casts: 1256, mult: 1.065) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 7499.7 -> **10254.0** | 750.1 -> **1025.5** | Class Light overtuned (WR: 58.2%, factor: 0.967); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1526). Increasing spread: b -17.9%, n +36.7% |
| `LLW` | Light | Debuff / Control | 9.1 -> **8.1** (-11.0%) | - | 9.1 -> **8.1** | Class Light overtuned (WR: 58.2%, factor: 0.967); Individual spell overtuned (WR: 70.1%, Casts: 3563, mult: 0.923) |
| `LLE` | Light | Setup - Weather | 980.6 -> **948.6** (-3.3%) | - | 980.6 -> **948.6** | Class Light overtuned (WR: 58.2%, factor: 0.967) |
| `LLL` | Light | Buff / Sustain | 6.7 -> **6.2** (-7.5%) | - | 6.7 -> **6.2** | Class Light overtuned (WR: 58.2%, factor: 0.967); Individual spell overtuned (WR: 63.6%, Casts: 1613, mult: 0.950) |
| `LLD` | Light | Ultimate | 6.3 -> **6.6** (+4.8%) | 485.2 -> **480.7** | 3063.1 -> **3179.2** | Class Light overtuned (WR: 58.2%, factor: 0.967); Weather 'Sunny' beneficiaries undertuned (WR: 36.5%) |
| `DDF` | Dark | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 10476.7 -> **14353.1** | 3143.3 -> **2870.8** | Class Dark overtuned (WR: 71.8%, factor: 0.913); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1008). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 9.4 -> **8.6** (-8.5%) | - | 9.4 -> **8.6** | Class Dark overtuned (WR: 71.8%, factor: 0.913) |
| `DDE` | Dark | Setup - Weather | 549.2 -> **376.7** (-31.4%) | - | 549.2 -> **376.7** | Class Dark overtuned (WR: 71.8%, factor: 0.913); Weather 'Darkness' appliers overtuned on own (WR: 89.2%) |
| `DDL` | Dark | Debuff / Control | 7.4 -> **6.0** (-18.9%) | - | 7.4 -> **6.0** | Class Dark overtuned (WR: 71.8%, factor: 0.913); Individual spell overtuned (WR: 78.5%, Casts: 9081, mult: 0.887) |
| `DDD` | Dark | Debuff / Control | 3.2 -> **2.8** (-12.5%) | - | 3.2 -> **2.8** | Class Dark overtuned (WR: 71.8%, factor: 0.913); Individual spell overtuned (WR: 65.1%, Casts: 486, mult: 0.944) |
| `FWW` | Ghostfire | Debuff / Control | 4.4 -> **4.1** (-6.8%) | - | 4.4 -> **4.1** | Status 'Cursed' appliers overtuned on own (WR: 61.0%); Individual spell overtuned (WR: 59.1%, Casts: 475, mult: 0.968) |
| `FWE` | Ghostfire | Setup - Location | 129.3 -> **112.2** (-13.2%) | - | 129.3 -> **112.2** | Location 'Graveyard' appliers overtuned on own (WR: 68.3%); Individual spell overtuned (WR: 69.1%, Casts: 56, mult: 0.927) |
| `FWL` | Ghostfire | Debuff / Control | 9.1 -> **8.6** (-5.5%) | - | 9.1 -> **8.6** | Status 'Cursed' appliers overtuned on own (WR: 61.0%); Individual spell overtuned (WR: 54.9%, Casts: 5149, mult: 0.984) |
| `FWD` | Ghostfire | Ultimate | 1.4 -> **1.1** (-21.4%) | 419.1 -> **550.7** | 588.1 -> **606.9** | Location 'Graveyard' beneficiaries overtuned (WR: 60.2%); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 539). Increasing spread: b -18.0%, n +37.0% |
| `WFF` | Ghostfire | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 25625.3 -> **35896.9** | 7687.9 -> **10769.4** | Status 'Bleeding' beneficiaries undertuned (WR: 43.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 739). Increasing spread: b -17.8%, n +36.5% |
| `WFW` | Ghostfire | Debuff / Control | 3.2 -> **3.1** (-3.1%) | - | 3.2 -> **3.1** | Individual spell overtuned (WR: 62.8%, Casts: 9731, mult: 0.953) |
| `WFL` | Ghostfire | Buff / Sustain | 37.0 -> **37.7** (+1.9%) | - | 37.0 -> **37.7** | Individual spell undertuned (WR: 44.5%, Casts: 1288, mult: 1.019) |
| `WFD` | Ghostfire | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 8622.1 -> **11805.1** | 3449.2 -> **4722.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 6848). Increasing spread: b -18.0%, n +36.9%; Individual spell undertuned (WR: 24.3%, Casts: 6848, mult: 1.101) |
| `FEF` | Beasts | Debuff / Control | 7.9 -> **7.7** (-2.5%) | - | 7.9 -> **7.7** | Individual spell overtuned (WR: 57.6%, Casts: 398, mult: 0.974) |
| `FEW` | Beasts | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 17092.4 -> **25307.7** | 5128.0 -> **7592.6** | Status 'Entangled' beneficiaries undertuned (WR: 29.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1951). Increasing spread: b -18.0%, n +37.0% |
| `FEE` | Beasts | Buff / Sustain | 203.3 -> **230.5** (+13.4%) | - | 203.3 -> **230.5** | Individual spell undertuned (WR: 16.9%, Casts: 4731, mult: 1.134) |
| `FEL` | Beasts | Buff / Sustain | 194.3 -> **198.0** (+1.9%) | - | 194.3 -> **198.0** | Individual spell undertuned (WR: 44.4%, Casts: 5637, mult: 1.019) |
| `EFF` | Beasts | Debuff / Control | 0.4 -> **0.4** (+0.0%) | 9355.0 -> **12816.4** | 3742.4 -> **5127.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1621). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 11.0%, Casts: 1621, mult: 1.160) |
| `EFW` | Beasts | Buff / Sustain | 69.4 -> **68.0** (-2.0%) | - | 69.4 -> **68.0** | Individual spell overtuned (WR: 56.1%, Casts: 580, mult: 0.979) |
| `EFE` | Beasts | Buff / Sustain | 8.2 -> **7.2** (-12.2%) | - | 8.2 -> **7.2** | Individual spell overtuned (WR: 79.3%, Casts: 5075, mult: 0.883) |
| `EFD` | Beasts | Ultimate | 4.4 -> **3.6** (-18.2%) | 792.9 -> **1174.0** | 3493.2 -> **4230.0** | Status 'Entangled' beneficiaries undertuned (WR: 29.8%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1573). Increasing spread: b -18.0%, n +37.0% |
| `FLF` | Lightning | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 20292.3 -> **28365.4** | 10146.6 -> **11346.6** | Class Lightning undertuned (WR: 41.8%, factor: 1.033); Status 'Stunned' beneficiaries undertuned (WR: 44.9%) |
| `FLW` | Lightning | Debuff / Control | 5.8 -> **5.9** (+1.7%) | - | 5.8 -> **5.9** | Class Lightning undertuned (WR: 41.8%, factor: 1.033); Status 'Stunned' appliers undertuned (WR: 42.8%, casts: 10417) |
| `FLE` | Lightning | Setup - Weather | 250.7 -> **257.7** (+2.8%) | - | 250.7 -> **257.7** | Class Lightning undertuned (WR: 41.8%, factor: 1.033); Individual spell overtuned (WR: 57.1%, Casts: 2, mult: 0.995) |
| `FLL` | Lightning | Buff / Sustain | 32.1 -> **28.1** (-12.5%) | - | 32.1 -> **28.1** | Class Lightning undertuned (WR: 41.8%, factor: 1.033); Individual spell overtuned (WR: 87.5%, Casts: 220, mult: 0.847) |
| `FLD` | Lightning | Ultimate | 2.4 -> **2.0** (-16.7%) | 1169.2 -> **1562.8** | 2808.5 -> **3127.6** | Class Lightning undertuned (WR: 41.8%, factor: 1.033); Status 'Stunned' beneficiaries undertuned (WR: 44.9%) |
| `LFF` | Lightning | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 9933.9 -> **13609.4** | 7947.9 -> **9527.3** | Class Lightning undertuned (WR: 41.8%, factor: 1.033); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5675). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 25.8 -> **26.6** (+3.1%) | - | 25.8 -> **26.6** | Class Lightning undertuned (WR: 41.8%, factor: 1.033) |
| `LFE` | Lightning | Debuff / Control | 5.1 -> **4.9** (-3.9%) | - | 5.1 -> **4.9** | Class Lightning undertuned (WR: 41.8%, factor: 1.033); Status 'Stunned' appliers undertuned (WR: 42.8%, casts: 10417) |
| `LFL` | Lightning | Debuff / Control | 0.6 -> **0.5** (-16.7%) | 8200.0 -> **11902.2** | 4920.6 -> **5951.6** | Class Lightning undertuned (WR: 41.8%, factor: 1.033); Weather 'Darkness' beneficiaries undertuned (WR: 35.1%) |
| `LFD` | Lightning | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 8408.9 -> **7586.7** | 2523.0 -> **2276.3** | Class Lightning undertuned (WR: 41.8%, factor: 1.033); Status 'Stunned' appliers undertuned (WR: 42.8%, casts: 10417) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 10476.7 -> **14353.1** | 2095.5 -> **2870.8** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 308). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 89.5 -> **90.7** (+1.3%) | - | 89.5 -> **90.7** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Individual spell undertuned (WR: 33.6%, Casts: 676, mult: 1.062) |
| `FDE` | Blood | Setup - Weather | 59.3 -> **60.3** (+1.7%) | - | 59.3 -> **60.3** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Individual spell undertuned (WR: 32.8%, Casts: 1694, mult: 1.065) |
| `FDD` | Blood | Ultimate | 3.4 -> **3.7** (+8.8%) | 185.8 -> **185.0** | 635.1 -> **688.2** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Weather 'Darkness' beneficiaries undertuned (WR: 35.1%) |
| `DFF` | Blood | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 20598.1 -> **28800.0** | 6179.7 -> **5760.2** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Status 'Bleeding' beneficiaries undertuned (WR: 43.5%) |
| `DFE` | Blood | Buff / Sustain | 415.9 -> **468.7** (+12.7%) | - | 415.9 -> **468.7** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Individual spell undertuned (WR: 6.4%, Casts: 488, mult: 1.180) |
| `DFL` | Blood | Buff / Sustain | 3.7 -> **3.4** (-8.1%) | - | 3.7 -> **3.4** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Individual spell overtuned (WR: 60.1%, Casts: 2350, mult: 0.964) |
| `DFD` | Blood | Conditional Strike | 145.0 -> **147.0** (+1.4%) | 0.1 -> **0.1** | 159.5 -> **161.7** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Condition triggers excessively (N=1 conditions, Trigger Rate: 79.6% vs 55% ceiling, WR: 88.1%). Compressing spread: b +25.7%, n -32.0% |
| `WEF` | Plants | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 13337.0 -> **18227.2** | 5335.2 -> **5468.5** | Class Plants undertuned (WR: 38.9%, factor: 1.044); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 497). Increasing spread: b -17.8%, n +36.7% |
| `WEW` | Plants | Debuff / Control | 194.8 -> **232.4** (+19.3%) | - | 194.8 -> **232.4** | Class Plants undertuned (WR: 38.9%, factor: 1.044); Individual spell undertuned (WR: 14.9%, Casts: 8158, mult: 1.142) |
| `WEE` | Plants | Setup - Location | 1259.6 -> **1562.7** (+24.1%) | - | 1259.6 -> **1562.7** | Class Plants undertuned (WR: 38.9%, factor: 1.044); Location 'Jungle' appliers undertuned (WR: 25.7%, casts: 5563) |
| `WED` | Plants | Conditional Strike | 5.6 -> **6.3** (+12.5%) | 114.1 -> **107.3** | 644.6 -> **682.3** | Class Plants undertuned (WR: 38.9%, factor: 1.044); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 4925, WR: 47.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 0.8 -> **0.8** (+0.0%) | 17687.7 -> **25538.7** | 14151.0 -> **20431.8** | Class Plants undertuned (WR: 38.9%, factor: 1.044); Weather 'Sunny' beneficiaries undertuned (WR: 36.5%) |
| `EWL` | Plants | Debuff / Control | 9.4 -> **8.7** (-7.4%) | - | 9.4 -> **8.7** | Class Plants undertuned (WR: 38.9%, factor: 1.044); Individual spell overtuned (WR: 78.2%, Casts: 2989, mult: 0.888) |
| `EWD` | Plants | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 15730.7 -> **22757.4** | 1573.2 -> **2275.8** | Class Plants undertuned (WR: 38.9%, factor: 1.044); Status 'Bleeding' appliers overtuned on own (WR: 88.4%) |
| `WLF` | Fey | Conditional Strike | 0.6 -> **0.6** (+0.0%) | 8966.9 -> **12284.7** | 5380.7 -> **7371.4** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 325). Increasing spread: b -18.0%, n +37.0% |
| `WLW` | Fey | Debuff / Control | 7.1 -> **6.8** (-4.2%) | - | 7.1 -> **6.8** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Status 'Cursed' appliers overtuned on own (WR: 61.0%) |
| `WLE` | Fey | Setup - Location | 2040.7 -> **2406.4** (+17.9%) | - | 2040.7 -> **2406.4** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Location 'Enchanted Forest' appliers undertuned (WR: 33.8%, casts: 1606) |
| `WLL` | Fey | Direct Damage | 20.6 -> **20.2** (-1.9%) | - | 20.6 -> **20.2** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Individual spell overtuned (WR: 67.9%, Casts: 2089, mult: 0.932) |
| `WLD` | Fey | Ultimate | 5.2 -> **6.2** (+19.2%) | 965.5 -> **1030.1** | 5025.8 -> **6392.8** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Weather 'Darkness' beneficiaries undertuned (WR: 35.1%) |
| `LWF` | Fey | Debuff / Control | 1.3 -> **1.2** (-7.7%) | 11947.6 -> **17534.9** | 15533.2 -> **21043.1** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Location 'Enchanted Forest' beneficiaries undertuned (WR: 32.2%) |
| `LWW` | Fey | Debuff / Control | 163.8 -> **174.9** (+6.8%) | - | 163.8 -> **174.9** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Individual spell undertuned (WR: 45.6%, Casts: 225, mult: 1.015) |
| `LWL` | Fey | Debuff / Control | 631.0 -> **656.2** (+4.0%) | - | 631.0 -> **656.2** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Individual spell overtuned (WR: 53.6%, Casts: 182, mult: 0.988) |
| `LWD` | Fey | Conditional Strike | 0.7 -> **0.7** (+0.0%) | 10476.7 -> **14353.1** | 7334.4 -> **10047.9** | Class Fey undertuned (WR: 37.0%, factor: 1.052); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2744). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 25707.2 -> **38766.3** | 5141.6 -> **7753.5** | Status 'Stunned' appliers undertuned (WR: 42.8%, casts: 10417); Weather 'Raining' beneficiaries undertuned (WR: 24.5%) |
| `WDE` | Ice | Setup - Weather | 192.9 -> **219.9** (+14.0%) | - | 192.9 -> **219.9** | Individual spell undertuned (WR: 15.4%, Casts: 222, mult: 1.140) |
| `WDL` | Ice | Debuff / Control | 6.5 -> **6.3** (-3.1%) | - | 6.5 -> **6.3** | Status 'Frosty' appliers overtuned on own (WR: 54.8%); Individual spell overtuned (WR: 54.0%, Casts: 6973, mult: 0.987) |
| `WDD` | Ice | Ultimate | 6.1 -> **6.7** (+9.8%) | 123.0 -> **119.0** | 756.4 -> **804.0** | Weather 'Blizzard' beneficiaries undertuned (WR: 46.3%); Location 'Tundra' beneficiaries undertuned (WR: 46.3%) |
| `DWW` | Ice | Debuff / Control | 8.3 -> **7.9** (-4.8%) | - | 8.3 -> **7.9** | Individual spell overtuned (WR: 64.0%, Casts: 4663, mult: 0.948) |
| `DWE` | Ice | Setup - Location | 425.6 -> **523.7** (+23.0%) | - | 425.6 -> **523.7** | Location 'Tundra' appliers undertuned (WR: 20.8%, casts: 3313); Individual spell undertuned (WR: 20.8%, Casts: 3313, mult: 1.116) |
| `DWL` | Ice | Debuff / Control | 8.4 -> **8.0** (-4.8%) | - | 8.4 -> **8.0** | Status 'Frosty' appliers overtuned on own (WR: 54.8%); Individual spell overtuned (WR: 58.4%, Casts: 7816, mult: 0.970) |
| `DWD` | Ice | Conditional Strike | 0.5 -> **0.5** (+0.0%) | 11426.1 -> **17098.1** | 5713.6 -> **8549.5** | Status 'Frosty' beneficiaries undertuned (WR: 26.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 2341). Increasing spread: b -17.8%, n +36.6% |
| `ELF` | Wind | Conditional Strike | 1.8 -> **1.6** (-11.1%) | 22999.4 -> **31921.6** | 41400.7 -> **51076.2** | Class Wind undertuned (WR: 37.0%, factor: 1.052); Status 'Bleeding' beneficiaries undertuned (WR: 43.5%) |
| `ELW` | Wind | Debuff / Control | 21.1 -> **19.9** (-5.7%) | - | 21.1 -> **19.9** | Class Wind undertuned (WR: 37.0%, factor: 1.052); Individual spell overtuned (WR: 76.3%, Casts: 406, mult: 0.896) |
| `ELE` | Wind | Setup - Weather | 285.2 -> **348.0** (+22.0%) | - | 285.2 -> **348.0** | Class Wind undertuned (WR: 37.0%, factor: 1.052); Individual spell undertuned (WR: 10.9%, Casts: 5212, mult: 1.160) |
| `ELL` | Wind | Buff / Sustain | 118.7 -> **127.8** (+7.7%) | - | 118.7 -> **127.8** | Class Wind undertuned (WR: 37.0%, factor: 1.052); Individual spell undertuned (WR: 43.1%, Casts: 719, mult: 1.024) |
| `ELD` | Wind | Conditional Strike | 2.0 -> **1.3** (-35.0%) | 22654.6 -> **33969.5** | 45311.2 -> **44161.7** | Class Wind undertuned (WR: 37.0%, factor: 1.052); Weather 'Raining' beneficiaries undertuned (WR: 24.5%) |
| `LEF` | Wind | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 24100.4 -> **34491.9** | 21691.3 -> **27594.3** | Class Wind undertuned (WR: 37.0%, factor: 1.052); Status 'Burning' beneficiaries undertuned (WR: 34.8%) |
| `LEW` | Wind | Debuff / Control | 16.9 -> **15.7** (-7.1%) | - | 16.9 -> **15.7** | Class Wind undertuned (WR: 37.0%, factor: 1.052); Individual spell overtuned (WR: 79.0%, Casts: 4168, mult: 0.885) |
| `LEE` | Wind | Setup - Weather | 402.8 -> **487.9** (+21.1%) | - | 402.8 -> **487.9** | Class Wind undertuned (WR: 37.0%, factor: 1.052); Individual spell undertuned (WR: 12.8%, Casts: 4618, mult: 1.152) |
| `LEL` | Wind | Buff / Sustain | 572.2 -> **644.4** (+12.6%) | - | 572.2 -> **644.4** | Class Wind undertuned (WR: 37.0%, factor: 1.052); Individual spell undertuned (WR: 31.4%, Casts: 2538, mult: 1.071) |
| `EDF` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 6596.8 -> **8841.4** | 1319.6 -> **1768.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.6% vs 30% floor, Casts: 3586). Increasing spread: b -16.6%, n +34.0%; Individual spell undertuned (WR: 22.5%, Casts: 3586, mult: 1.109) |
| `EDW` | Poison | Debuff / Control | 2.4 -> **2.5** (+4.2%) | - | 2.4 -> **2.5** | Individual spell undertuned (WR: 42.8%, Casts: 1597, mult: 1.025) |
| `EDE` | Poison | Setup - Location | 517.5 -> **533.5** (+3.1%) | - | 517.5 -> **533.5** | Location 'Swamp' appliers undertuned (WR: 45.5%, casts: 1406); Individual spell undertuned (WR: 45.5%, Casts: 1406, mult: 1.015) |
| `EDD` | Poison | Ultimate | 5.4 -> **6.0** (+11.1%) | 611.4 -> **607.7** | 3307.0 -> **3652.2** | Status 'Bleeding' beneficiaries undertuned (WR: 43.5%); Location 'Swamp' beneficiaries undertuned (WR: 42.3%) |
| `DEF` | Poison | Conditional Strike | 1.4 -> **1.1** (-21.4%) | 59.4 -> **81.0** | 84.6 -> **90.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 707). Increasing spread: b -17.7%, n +36.4%; Individual spell overtuned (WR: 61.5%, Casts: 707, mult: 0.958) |
| `DEW` | Poison | Debuff / Control | 3.0 -> **2.9** (-3.3%) | - | 3.0 -> **2.9** | Individual spell overtuned (WR: 57.0%, Casts: 4333, mult: 0.976) |
| `DEE` | Poison | Debuff / Control | 6.9 -> **6.4** (-7.2%) | - | 6.9 -> **6.4** | Individual spell overtuned (WR: 69.7%, Casts: 2042, mult: 0.925) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 29375.0 -> **41187.3** | 8812.8 -> **8237.7** | Status 'Bleeding' beneficiaries undertuned (WR: 43.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 511). Increasing spread: b -17.8%, n +36.7% |
| `DED` | Poison | Debuff / Control | 9.1 -> **8.6** (-5.5%) | - | 9.1 -> **8.6** | Individual spell overtuned (WR: 65.5%, Casts: 5081, mult: 0.942) |
| `LDF` | Cosmic | Debuff / Control | 12.5 -> **10.9** (-12.8%) | - | 12.5 -> **10.9** | Class Cosmic overtuned (WR: 61.9%, factor: 0.952); Individual spell overtuned (WR: 72.5%, Casts: 4979, mult: 0.913) |
| `LDW` | Cosmic | Debuff / Control | 4.5 -> **4.1** (-8.9%) | - | 4.5 -> **4.1** | Class Cosmic overtuned (WR: 61.9%, factor: 0.952); Status 'Stunned' appliers undertuned (WR: 42.8%, casts: 10417) |
| `LDE` | Cosmic | Setup - Location | 94.2 -> **92.2** (-2.1%) | - | 94.2 -> **92.2** | Class Cosmic overtuned (WR: 61.9%, factor: 0.952); Individual spell undertuned (WR: 42.1%, Casts: 318, mult: 1.028) |
| `LDL` | Cosmic | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 8718.4 -> **11944.2** | 4359.7 -> **4778.1** | Class Cosmic overtuned (WR: 61.9%, factor: 0.952); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 733). Increasing spread: b -18.0%, n +37.0% |
| `LDD` | Cosmic | Ultimate | 4.6 -> **4.9** (+6.5%) | 282.9 -> **265.9** | 1305.9 -> **1307.8** | Class Cosmic overtuned (WR: 61.9%, factor: 0.952); Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 4167, WR: 40.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 7888.4 -> **10776.2** | 3155.8 -> **3233.2** | Class Cosmic overtuned (WR: 61.9%, factor: 0.952); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 3401). Increasing spread: b -17.8%, n +36.6% |
| `DLW` | Cosmic | Direct Damage | 8.5 -> **7.3** (-14.1%) | - | 8.5 -> **7.3** | Class Cosmic overtuned (WR: 61.9%, factor: 0.952); Individual spell overtuned (WR: 75.0%, Casts: 2810, mult: 0.902) |
| `DLE` | Cosmic | Direct Damage | 282.2 -> **255.6** (-9.4%) | - | 282.2 -> **255.6** | Class Cosmic overtuned (WR: 61.9%, factor: 0.952); Individual spell overtuned (WR: 63.3%, Casts: 2020, mult: 0.951) |
| `DLL` | Cosmic | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 9536.3 -> **13841.8** | 4768.6 -> **5537.1** | Class Cosmic overtuned (WR: 61.9%, factor: 0.952); Weather 'Darkness' beneficiaries undertuned (WR: 35.1%) |
