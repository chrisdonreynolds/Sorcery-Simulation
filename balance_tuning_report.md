# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T02:11:56Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 691.1s  
**Total Spells Tuned:** 108 / 125  

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
| **Blood** | 19,042 | 56.2% | 56.2% | 18.2 | Overtuned ⚠️ |
| **Poison** | 20,706 | 55.0% | 55.0% | 10.8 | Overtuned ⚠️ |
| **Ghostfire** | 18,424 | 53.3% | 53.3% | 28.9 | Balanced ✅ |
| **Light** | 9,711 | 53.3% | 53.3% | 20.4 | Balanced ✅ |
| **Beasts** | 20,313 | 51.9% | 51.9% | 14.3 | Balanced ✅ |
| **Earth** | 8,942 | 51.3% | 51.3% | 15.9 | Balanced ✅ |
| **Ice** | 18,346 | 49.8% | 49.8% | 16.4 | Balanced ✅ |
| **Dark** | 10,743 | 49.7% | 49.7% | 35.3 | Balanced ✅ |
| **Fire** | 8,393 | 49.4% | 49.4% | 19.1 | Balanced ✅ |
| **Cosmic** | 17,725 | 49.1% | 49.1% | 18.0 | Balanced ✅ |
| **Lightning** | 21,371 | 49.0% | 49.0% | 16.5 | Balanced ✅ |
| **Plants** | 20,405 | 47.7% | 47.7% | 7.5 | Balanced ✅ |
| **Water** | 9,457 | 46.1% | 46.1% | 13.6 | Undertuned ⚠️ |
| **Wind** | 17,355 | 45.8% | 45.8% | 8.5 | Undertuned ⚠️ |
| **Fey** | 17,380 | 45.4% | 45.4% | 68.0 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,133 (54.2%) | 3,872 (46.0%) | 19.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,787 (53.5%) | 4,938 (45.8%) | 5.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,934 (49.9%) | 4,219 (43.8%) | 9.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,125 (63.4%) | 8,154 (44.4%) | 4.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 12,995 (51.1%) | 5,084 (41.3%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,035 (62.8%) | 6,864 (47.7%) | 1.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,754 (44.2%) | 3,993 (41.5%) | 4.9% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 60.3 -> **59.6** (-1.2%) | - | 60.3 -> **59.6** | Individual spell overtuned (WR: 53.5%, Casts: 1925, mult: 0.989) |
| `FFW` | Fire | Debuff / Control | 39.6 -> **40.5** (+2.3%) | - | 39.6 -> **40.5** | Individual spell undertuned (WR: 43.5%, Casts: 1955, mult: 1.022) |
| `FFD` | Fire | Conditional Strike | 1.5 -> **1.3** (-13.3%) | 326.0 -> **440.6** | 490.5 -> **574.1** | Status 'Burning' beneficiaries undertuned (WR: 43.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 960). Increasing spread: b -15.5%, n +31.9% |
| `WWF` | Water | Conditional Strike | 3.6 -> **3.3** (-8.3%) | 177.5 -> **226.5** | 642.6 -> **750.8** | Class Water undertuned (WR: 46.1%, factor: 1.016); Status 'Burning' beneficiaries undertuned (WR: 43.8%) |
| `WWE` | Water | Setup - Weather | 63.5 -> **67.1** (+5.7%) | - | 63.5 -> **67.1** | Class Water undertuned (WR: 46.1%, factor: 1.016); Weather 'Raining' appliers undertuned (WR: 44.2%, casts: 1754) |
| `WWL` | Water | Buff / Sustain | 70.8 -> **72.7** (+2.7%) | - | 70.8 -> **72.7** | Class Water undertuned (WR: 46.1%, factor: 1.016); Individual spell undertuned (WR: 46.4%, Casts: 2883, mult: 1.012) |
| `WWD` | Water | Buff / Sustain | 47.4 -> **48.8** (+3.0%) | - | 47.4 -> **48.8** | Class Water undertuned (WR: 46.1%, factor: 1.016); Individual spell undertuned (WR: 45.6%, Casts: 1544, mult: 1.015) |
| `EEF` | Earth | Conditional Strike | 21.2 -> **24.4** (+15.1%) | 33.1 -> **39.2** | 722.9 -> **980.9** | Status 'Frosty' beneficiaries undertuned (WR: 46.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 24.4% vs 30% floor, Casts: 1678). Increasing spread: b -8.2%, n +16.6% |
| `EEW` | Earth | Buff / Sustain | 20.5 -> **20.1** (-2.0%) | - | 20.5 -> **20.1** | Individual spell overtuned (WR: 55.3%, Casts: 1891, mult: 0.982) |
| `LLF` | Light | Conditional Strike | 7.0 -> **7.8** (+11.4%) | 442.5 -> **588.2** | 3104.5 -> **4595.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 2400). Increasing spread: b -16.0%, n +32.9%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 103.5 -> **121.8** (+17.7%) | - | 103.5 -> **121.8** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LLE` | Light | Setup - Weather | 137.3 -> **154.2** (+12.3%) | - | 137.3 -> **154.2** | Weather 'Sunny' appliers overtuned on own (WR: 53.5%); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 18.1 -> **17.3** (-4.4%) | - | 18.1 -> **17.3** | Individual spell overtuned (WR: 62.4%, Casts: 1667, mult: 0.955) |
| `LLD` | Light | Ultimate | 36.0 -> **36.0** (+0.0%) | 94.6 -> **125.0** | 3441.6 -> **4536.0** | Weather 'Sunny' beneficiaries undertuned (WR: 45.8%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 2067). Shifted tuner focus: protected ultimate base floor at 36.0 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 842.1 -> **1153.7** | 590.2 -> **692.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2221). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 40.6%, Casts: 2221, mult: 1.033) |
| `DDW` | Dark | Debuff / Control | 127.9 -> **147.1** (+15.0%) | - | 127.9 -> **147.1** | Buffed setup spell [DDW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DDE` | Dark | Setup - Weather | 181.7 -> **209.0** (+15.0%) | - | 181.7 -> **209.0** | Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 59.1 -> **66.5** (+12.5%) | - | 59.1 -> **66.5** | Buffed setup spell [DDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 56.5%, Casts: 1912, mult: 0.978) |
| `DDD` | Dark | Debuff / Control | 20.2 -> **19.7** (-2.5%) | - | 20.2 -> **19.7** | Individual spell overtuned (WR: 57.1%, Casts: 1706, mult: 0.975) |
| `FWF` | Ghostfire | Debuff / Control | 22.6 -> **22.1** (-2.2%) | - | 22.6 -> **22.1** | Individual spell overtuned (WR: 56.3%, Casts: 1757, mult: 0.978) |
| `FWW` | Ghostfire | Debuff / Control | 71.8 -> **82.6** (+15.0%) | - | 71.8 -> **82.6** | Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 207.0 -> **238.0** (+15.0%) | - | 207.0 -> **238.0** | Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 170.9 -> **188.6** (+10.4%) | - | 170.9 -> **188.6** | Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD]; Individual spell overtuned (WR: 61.2%, Casts: 1958, mult: 0.959) |
| `FWD` | Ghostfire | Ultimate | 49.3 -> **49.3** (+0.0%) | 86.0 -> **112.9** | 4289.1 -> **5615.3** | Status 'Cursed' beneficiaries undertuned (WR: 46.2%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.3% vs 8% floor, Casts: 1447). Shifted tuner focus: protected ultimate base floor at 49.3 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 392.2 -> **539.0** | 550.5 -> **648.0** | Status 'Bleeding' beneficiaries undertuned (WR: 44.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.1% vs 30% floor, Casts: 1699). Increasing spread: b -16.8%, n +34.4% |
| `WFW` | Ghostfire | Debuff / Control | 24.0 -> **23.2** (-3.3%) | - | 24.0 -> **23.2** | Individual spell overtuned (WR: 59.7%, Casts: 2118, mult: 0.966) |
| `WFE` | Ghostfire | Debuff / Control | 13.0 -> **11.5** (-11.5%) | - | 13.0 -> **11.5** | Status 'Bleeding' appliers overtuned on own (WR: 63.4%); Individual spell overtuned (WR: 68.8%, Casts: 1581, mult: 0.928) |
| `WFL` | Ghostfire | Buff / Sustain | 45.5 -> **46.3** (+1.8%) | - | 45.5 -> **46.3** | Individual spell undertuned (WR: 45.0%, Casts: 2887, mult: 1.017) |
| `WFD` | Ghostfire | Conditional Strike | 2.0 -> **1.7** (-15.0%) | 269.0 -> **346.1** | 540.0 -> **590.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.0% vs 30% floor, Casts: 1658). Increasing spread: b -14.0%, n +28.7%; Individual spell undertuned (WR: 45.3%, Casts: 1658, mult: 1.015) |
| `FEF` | Beasts | Debuff / Control | 72.1 -> **82.9** (+15.0%) | - | 72.1 -> **82.9** | Buffed setup spell [FEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `FEW` | Beasts | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 858.6 -> **1163.0** | 601.7 -> **698.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 2383). Increasing spread: b -17.3%, n +35.5% |
| `FEE` | Beasts | Buff / Sustain | 33.8 -> **34.3** (+1.5%) | - | 33.8 -> **34.3** | Individual spell undertuned (WR: 45.3%, Casts: 2349, mult: 1.016) |
| `EFF` | Beasts | Debuff / Control | 0.8 -> **0.6** (-25.0%) | 748.1 -> **1022.8** | 599.3 -> **614.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1831). Increasing spread: b -17.9%, n +36.7%; Individual spell overtuned (WR: 54.5%, Casts: 1831, mult: 0.985) |
| `EFL` | Beasts | Buff / Sustain | 2.0 -> **1.7** (-15.0%) | - | 2.0 -> **1.7** | Individual spell overtuned (WR: 81.8%, Casts: 1031, mult: 0.872) |
| `EFD` | Beasts | Ultimate | 32.2 -> **31.3** (-2.8%) | 184.1 -> **238.6** | 5960.2 -> **7499.5** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.3% vs 16% floor, Casts: 1973). Shifted tuner focus: protected ultimate base floor at 32.2 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo.; Individual spell overtuned (WR: 57.9%, Casts: 1973, mult: 0.972) |
| `FLF` | Lightning | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 1165.9 -> **1647.3** | 1166.9 -> **1483.5** | Status 'Stunned' beneficiaries undertuned (WR: 41.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 2797). Increasing spread: b -17.8%, n +36.5% |
| `FLW` | Lightning | Debuff / Control | 91.4 -> **100.9** (+10.4%) | - | 91.4 -> **100.9** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 61.1%, Casts: 2373, mult: 0.960) |
| `FLE` | Lightning | Setup - Weather | 78.0 -> **93.1** (+19.4%) | - | 78.0 -> **93.1** | Weather 'Storming' appliers undertuned (WR: 44.5%, casts: 2812); Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLL` | Lightning | Buff / Sustain | 31.2 -> **32.2** (+3.2%) | - | 31.2 -> **32.2** | Individual spell undertuned (WR: 40.8%, Casts: 2282, mult: 1.033) |
| `FLD` | Lightning | Ultimate | 77.7 -> **77.7** (+0.0%) | 31.2 -> **42.0** | 2501.9 -> **3341.1** | Status 'Stunned' beneficiaries undertuned (WR: 41.3%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 2287). Shifted tuner focus: protected ultimate base floor at 77.7 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 649.5 -> **879.6** | 520.4 -> **616.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1220). Increasing spread: b -17.2%, n +35.4% |
| `LFW` | Lightning | Buff / Sustain | 27.6 -> **26.4** (-4.3%) | - | 27.6 -> **26.4** | Individual spell overtuned (WR: 61.7%, Casts: 1442, mult: 0.958) |
| `LFL` | Lightning | Debuff / Control | 45.0 -> **50.8** (+12.9%) | 241.6 -> **311.9** | 10917.0 -> **15895.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.5% vs 30% floor, Casts: 2602). Increasing spread: b -14.2%, n +29.1%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 2.4 -> **2.0** (-16.7%) | 462.7 -> **613.4** | 1112.9 -> **1228.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.3% vs 30% floor, Casts: 1955). Increasing spread: b -15.9%, n +32.6% |
| `FDF` | Blood | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 844.2 -> **1156.6** | 591.6 -> **694.6** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1329). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 63.8 -> **62.2** (-2.5%) | - | 63.8 -> **62.2** | Class Blood overtuned (WR: 56.2%, factor: 0.975) |
| `FDE` | Blood | Setup - Weather | 18.1 -> **17.3** (-4.4%) | - | 18.1 -> **17.3** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 55.3%, Casts: 2332, mult: 0.982) |
| `FDL` | Blood | Debuff / Control | 7.5 -> **6.3** (-16.0%) | - | 7.5 -> **6.3** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Status 'Bleeding' appliers overtuned on own (WR: 63.4%) |
| `FDD` | Blood | Ultimate | 50.9 -> **49.6** (-2.6%) | 22.5 -> **29.2** | 1196.1 -> **1497.9** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.3% vs 16% floor, Casts: 1435). Shifted tuner focus: protected ultimate base floor at 50.9 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 1.0 -> **0.8** (-20.0%) | 356.0 -> **479.1** | 357.0 -> **384.1** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Status 'Bleeding' beneficiaries undertuned (WR: 44.4%) |
| `DFW` | Blood | Debuff / Control | 14.3 -> **13.7** (-4.2%) | - | 14.3 -> **13.7** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Status 'Bleeding' appliers overtuned on own (WR: 63.4%) |
| `DFE` | Blood | Buff / Sustain | 44.5 -> **46.3** (+4.0%) | - | 44.5 -> **46.3** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Individual spell undertuned (WR: 32.5%, Casts: 1582, mult: 1.066) |
| `DFL` | Blood | Buff / Sustain | 30.9 -> **30.1** (-2.6%) | - | 30.9 -> **30.1** | Class Blood overtuned (WR: 56.2%, factor: 0.975) |
| `DFD` | Blood | Conditional Strike | 244.8 -> **270.1** (+10.3%) | 0.1 -> **0.1** | 269.3 -> **297.1** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Condition triggers excessively (N=1 conditions, Trigger Rate: 94.0% vs 55% ceiling, WR: 63.9%). Compressing spread: b +19.2%, n -27.4% |
| `WEF` | Plants | Conditional Strike | 2.0 -> **1.8** (-10.0%) | 241.2 -> **310.1** | 484.4 -> **560.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.1% vs 30% floor, Casts: 1918). Increasing spread: b -14.0%, n +28.6%; Individual spell undertuned (WR: 38.7%, Casts: 1918, mult: 1.041) |
| `WEW` | Plants | Debuff / Control | 395.7 -> **482.4** (+21.9%) | - | 395.7 -> **482.4** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 33.9%, Casts: 2475, mult: 1.060) |
| `WEE` | Plants | Setup - Location | 19.0 -> **18.4** (-3.2%) | - | 19.0 -> **18.4** | Location 'Jungle' appliers overtuned on own (WR: 54.7%); Individual spell overtuned (WR: 54.7%, Casts: 1399, mult: 0.984) |
| `WEL` | Plants | Debuff / Control | 29.4 -> **26.8** (-8.8%) | - | 29.4 -> **26.8** | Status 'Entangled' appliers overtuned on own (WR: 62.8%); Individual spell overtuned (WR: 62.9%, Casts: 2035, mult: 0.953) |
| `WED` | Plants | Conditional Strike | 9.2 -> **10.1** (+9.8%) | 36.1 -> **33.9** | 341.3 -> **352.5** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1318, WR: 43.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 43.9%, Casts: 1318, mult: 1.021) |
| `EWF` | Plants | Buff / Sustain | 1.7 -> **1.5** (-11.8%) | 160.4 -> **211.5** | 274.4 -> **318.8** | Weather 'Sunny' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.8% vs 30% floor, Casts: 2871). Increasing spread: b -14.5%, n +29.7% |
| `EWW` | Plants | Debuff / Control | 3.1 -> **2.7** (-12.9%) | - | 3.1 -> **2.7** | Individual spell overtuned (WR: 83.9%, Casts: 1717, mult: 0.863) |
| `EWL` | Plants | Debuff / Control | 72.7 -> **73.9** (+1.7%) | - | 72.7 -> **73.9** | Individual spell undertuned (WR: 45.1%, Casts: 2533, mult: 1.016) |
| `EWD` | Plants | Conditional Strike | 4.1 -> **3.4** (-17.1%) | 677.4 -> **914.5** | 2781.4 -> **3112.7** | Status 'Bleeding' appliers overtuned on own (WR: 63.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.4% vs 30% floor, Casts: 2508). Increasing spread: b -17.0%, n +35.0% |
| `WLF` | Fey | Conditional Strike | 1.7 -> **1.5** (-11.8%) | 505.4 -> **682.3** | 860.9 -> **1024.9** | Class Fey undertuned (WR: 45.4%, factor: 1.018); Status 'Cursed' beneficiaries undertuned (WR: 46.2%) |
| `WLW` | Fey | Debuff / Control | 57.5 -> **58.5** (+1.7%) | - | 57.5 -> **58.5** | Class Fey undertuned (WR: 45.4%, factor: 1.018) |
| `WLE` | Fey | Setup - Location | 237.2 -> **277.8** (+17.1%) | - | 237.2 -> **277.8** | Class Fey undertuned (WR: 45.4%, factor: 1.018); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 57.0 -> **58.0** (+1.8%) | - | 57.0 -> **58.0** | Class Fey undertuned (WR: 45.4%, factor: 1.018) |
| `WLD` | Fey | Ultimate | 24.8 -> **24.3** (-2.0%) | 426.7 -> **546.8** | 10607.0 -> **13311.5** | Class Fey undertuned (WR: 45.4%, factor: 1.018); Location 'Enchanted Forest' beneficiaries overtuned (WR: 53.6%) |
| `LWF` | Fey | Debuff / Control | 30.2 -> **35.4** (+17.2%) | 138.2 -> **169.3** | 4203.8 -> **6028.6** | Class Fey undertuned (WR: 45.4%, factor: 1.018); Location 'Enchanted Forest' beneficiaries overtuned (WR: 53.6%) |
| `LWW` | Fey | Debuff / Control | 45.8 -> **46.6** (+1.7%) | - | 45.8 -> **46.6** | Class Fey undertuned (WR: 45.4%, factor: 1.018) |
| `LWL` | Fey | Debuff / Control | 50.3 -> **52.4** (+4.2%) | - | 50.3 -> **52.4** | Class Fey undertuned (WR: 45.4%, factor: 1.018); Individual spell undertuned (WR: 43.5%, Casts: 1601, mult: 1.022) |
| `LWD` | Fey | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 844.2 -> **1156.6** | 845.2 -> **1041.8** | Class Fey undertuned (WR: 45.4%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1817). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 2.2 -> **1.9** (-13.6%) | 812.7 -> **1120.4** | 1790.1 -> **2130.7** | Weather 'Raining' beneficiaries undertuned (WR: 41.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.4% vs 30% floor, Casts: 2664). Increasing spread: b -16.2%, n +33.3% |
| `WDW` | Ice | Buff / Sustain | 12.6 -> **12.2** (-3.2%) | - | 12.6 -> **12.2** | Status 'Frosty' appliers overtuned on own (WR: 54.2%); Individual spell overtuned (WR: 55.4%, Casts: 3785, mult: 0.982) |
| `WDE` | Ice | Setup - Weather | 30.4 -> **31.0** (+2.0%) | - | 30.4 -> **31.0** | Individual spell undertuned (WR: 44.6%, Casts: 1818, mult: 1.018) |
| `WDL` | Ice | Debuff / Control | 42.0 -> **41.4** (-1.4%) | - | 42.0 -> **41.4** | Status 'Frosty' appliers overtuned on own (WR: 54.2%) |
| `WDD` | Ice | Ultimate | 35.2 -> **35.2** (+0.0%) | 104.5 -> **133.2** | 3713.6 -> **4723.8** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 2.0% vs 16% floor, Casts: 1385). Shifted tuner focus: protected ultimate base floor at 35.2 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWF` | Ice | Debuff / Control | 39.6 -> **39.0** (-1.5%) | - | 39.6 -> **39.0** | Status 'Frosty' appliers overtuned on own (WR: 54.2%) |
| `DWW` | Ice | Debuff / Control | 90.1 -> **101.6** (+12.8%) | - | 90.1 -> **101.6** | Buffed setup spell [DWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 55.9%, Casts: 1368, mult: 0.980) |
| `DWL` | Ice | Debuff / Control | 43.0 -> **41.5** (-3.5%) | - | 43.0 -> **41.5** | Status 'Frosty' appliers overtuned on own (WR: 54.2%); Individual spell overtuned (WR: 55.9%, Casts: 1653, mult: 0.980) |
| `DWD` | Ice | Conditional Strike | 5.4 -> **4.9** (-9.3%) | 76.4 -> **95.9** | 418.0 -> **474.8** | Status 'Frosty' beneficiaries undertuned (WR: 46.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 16.1% vs 30% floor, Casts: 2194). Increasing spread: b -11.5%, n +23.6% |
| `ELF` | Wind | Conditional Strike | 3.5 -> **3.2** (-8.6%) | 388.0 -> **518.1** | 1361.5 -> **1661.1** | Class Wind undertuned (WR: 45.8%, factor: 1.017); Status 'Bleeding' beneficiaries undertuned (WR: 44.4%) |
| `ELW` | Wind | Debuff / Control | 99.0 -> **115.8** (+17.0%) | - | 99.0 -> **115.8** | Class Wind undertuned (WR: 45.8%, factor: 1.017); Buffed setup spell [ELW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `ELE` | Wind | Setup - Weather | 24.5 -> **25.3** (+3.3%) | - | 24.5 -> **25.3** | Class Wind undertuned (WR: 45.8%, factor: 1.017); Individual spell undertuned (WR: 45.4%, Casts: 1384, mult: 1.015) |
| `ELL` | Wind | Buff / Sustain | 38.6 -> **39.3** (+1.8%) | - | 38.6 -> **39.3** | Class Wind undertuned (WR: 45.8%, factor: 1.017) |
| `ELD` | Wind | Conditional Strike | 2.1 -> **1.9** (-9.5%) | 666.6 -> **910.9** | 1402.0 -> **1732.6** | Class Wind undertuned (WR: 45.8%, factor: 1.017); Weather 'Raining' beneficiaries undertuned (WR: 41.5%) |
| `LEF` | Wind | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 389.0 -> **528.4** | 546.0 -> **635.3** | Class Wind undertuned (WR: 45.8%, factor: 1.017); Status 'Burning' beneficiaries undertuned (WR: 43.8%) |
| `LEW` | Wind | Debuff / Control | 52.6 -> **53.5** (+1.7%) | - | 52.6 -> **53.5** | Class Wind undertuned (WR: 45.8%, factor: 1.017) |
| `LEE` | Wind | Setup - Weather | 22.0 -> **22.4** (+1.8%) | - | 22.0 -> **22.4** | Class Wind undertuned (WR: 45.8%, factor: 1.017) |
| `LEL` | Wind | Buff / Sustain | 96.7 -> **113.1** (+17.0%) | - | 96.7 -> **113.1** | Class Wind undertuned (WR: 45.8%, factor: 1.017); Buffed setup spell [LEL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `EDF` | Poison | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 363.1 -> **473.0** | 327.7 -> **379.2** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 2849). Increasing spread: b -14.8%, n +30.3% |
| `EDW` | Poison | Debuff / Control | 12.7 -> **11.7** (-7.9%) | - | 12.7 -> **11.7** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 66.2%, Casts: 1822, mult: 0.939) |
| `EDE` | Poison | Setup - Location | 54.7 -> **51.7** (-5.5%) | - | 54.7 -> **51.7** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Location 'Swamp' appliers overtuned on own (WR: 55.1%) |
| `EDL` | Poison | Debuff / Control | 1.0 -> **0.8** (-20.0%) | - | 1.0 -> **0.8** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 85.9%, Casts: 1947, mult: 0.854) |
| `EDD` | Poison | Ultimate | 44.4 -> **47.0** (+5.9%) | 27.5 -> **26.4** | 1265.4 -> **1287.8** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Status 'Bleeding' beneficiaries undertuned (WR: 44.4%) |
| `DEF` | Poison | Conditional Strike | 32.1 -> **31.9** (-0.6%) | 1.4 -> **1.4** | 77.0 -> **76.6** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 52.5% within [30%-55%] target window, WR: 45.4%). |
| `DEW` | Poison | Debuff / Control | 14.8 -> **14.0** (-5.4%) | - | 14.8 -> **14.0** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 58.9%, Casts: 2731, mult: 0.969) |
| `DEE` | Poison | Debuff / Control | 42.5 -> **46.8** (+10.1%) | - | 42.5 -> **46.8** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Buffed setup spell [DEE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 383.2 -> **523.3** | 76.8 -> **104.9** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Status 'Bleeding' beneficiaries undertuned (WR: 44.4%) |
| `DED` | Poison | Debuff / Control | 22.2 -> **22.3** (+0.5%) | - | 22.2 -> **22.3** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Individual spell undertuned (WR: 42.5%, Casts: 1866, mult: 1.026) |
| `LDF` | Cosmic | Debuff / Control | 121.0 -> **139.1** (+15.0%) | - | 121.0 -> **139.1** | Buffed setup spell [LDF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LDW` | Cosmic | Debuff / Control | 45.2 -> **44.6** (-1.3%) | - | 45.2 -> **44.6** | Individual spell overtuned (WR: 54.1%, Casts: 2724, mult: 0.987) |
| `LDL` | Cosmic | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 498.9 -> **674.3** | 799.8 -> **945.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 1359). Increasing spread: b -17.1%, n +35.2%; Individual spell undertuned (WR: 33.1%, Casts: 1359, mult: 1.064) |
| `LDD` | Cosmic | Ultimate | 66.6 -> **66.6** (+0.0%) | 23.1 -> **30.0** | 1605.1 -> **2064.6** | Ultimate payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1912). Shifted tuner focus: protected ultimate base floor at 66.6 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDW, DDL, DEE, DFW, DWW, ELW, LEL, DLL, FEF, LWF) with +15% b tempo. |
| `DLF` | Cosmic | Conditional Strike | 1.6 -> **1.3** (-18.8%) | 405.5 -> **535.6** | 650.4 -> **697.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.9% vs 30% floor, Casts: 2341). Increasing spread: b -15.6%, n +32.1%; Individual spell overtuned (WR: 56.4%, Casts: 2341, mult: 0.978) |
| `DLW` | Cosmic | Direct Damage | 57.5 -> **56.6** (-1.6%) | - | 57.5 -> **56.6** | Individual spell overtuned (WR: 54.6%, Casts: 1722, mult: 0.985) |
| `DLE` | Cosmic | Direct Damage | 46.9 -> **48.9** (+4.3%) | - | 46.9 -> **48.9** | Individual spell undertuned (WR: 38.4%, Casts: 1281, mult: 1.042) |
| `DLL` | Cosmic | Conditional Strike | 4.7 -> **4.1** (-12.8%) | 184.9 -> **243.3** | 873.7 -> **1001.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.5% vs 30% floor, Casts: 2162). Increasing spread: b -15.4%, n +31.6%; Individual spell undertuned (WR: 38.3%, Casts: 2162, mult: 1.042) |
