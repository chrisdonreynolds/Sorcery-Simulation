# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T22:16:10Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 737.0s  
**Total Spells Tuned:** 91 / 125  

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
| **Blood** | 19,052 | 55.4% | 55.4% | 12.6 | Overtuned ⚠️ |
| **Poison** | 21,358 | 54.9% | 54.9% | 10.6 | Overtuned ⚠️ |
| **Earth** | 8,587 | 53.2% | 53.2% | 16.5 | Balanced ✅ |
| **Beasts** | 19,927 | 53.0% | 53.0% | 6.2 | Balanced ✅ |
| **Plants** | 22,374 | 52.2% | 52.2% | 7.4 | Balanced ✅ |
| **Light** | 11,165 | 51.6% | 51.6% | 4.0 | Balanced ✅ |
| **Dark** | 10,453 | 49.6% | 49.6% | 12.0 | Balanced ✅ |
| **Water** | 9,613 | 49.0% | 49.0% | 8.4 | Balanced ✅ |
| **Fire** | 9,289 | 48.3% | 48.2% | 15.1 | Balanced ✅ |
| **Fey** | 17,081 | 48.3% | 48.3% | 7.8 | Balanced ✅ |
| **Lightning** | 23,549 | 48.0% | 48.0% | 10.8 | Balanced ✅ |
| **Ghostfire** | 22,715 | 47.7% | 47.7% | 13.6 | Balanced ✅ |
| **Cosmic** | 19,133 | 47.5% | 47.5% | 16.2 | Balanced ✅ |
| **Wind** | 19,819 | 47.2% | 47.2% | 7.7 | Balanced ✅ |
| **Ice** | 20,403 | 47.1% | 47.1% | 12.8 | Balanced ✅ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,042 (47.6%) | 4,138 (52.4%) | 19.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,831 (43.8%) | 4,477 (55.5%) | 7.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,612 (53.0%) | 6,368 (50.0%) | 9.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,155 (65.9%) | 8,196 (49.5%) | 5.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 13,887 (50.0%) | 5,010 (41.1%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,537 (52.5%) | 5,683 (54.1%) | 1.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,633 (43.8%) | 5,443 (36.4%) | 5.2% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 46.7 -> **47.4** (+1.5%) | - | 46.7 -> **47.4** | Individual spell undertuned (WR: 45.3%, Casts: 1366, mult: 1.016) |
| `FFL` | Fire | Debuff / Control | 7.7 -> **7.5** (-2.6%) | - | 7.7 -> **7.5** | Individual spell overtuned (WR: 56.3%, Casts: 1273, mult: 0.978) |
| `FFD` | Fire | Conditional Strike | 10.4 -> **9.1** (-12.5%) | 10.4 -> **13.5** | 118.6 -> **131.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 2537). Increasing spread: b -14.7%, n +30.2%; Individual spell undertuned (WR: 43.2%, Casts: 2537, mult: 1.023) |
| `WWF` | Water | Conditional Strike | 18.6 -> **16.2** (-12.9%) | 9.2 -> **11.6** | 189.7 -> **204.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.9% vs 30% floor, Casts: 1759). Increasing spread: b -12.8%, n +26.2% |
| `WWE` | Water | Setup - Weather | 24.5 -> **25.6** (+4.5%) | - | 24.5 -> **25.6** | Weather 'Raining' appliers undertuned (WR: 43.8%, casts: 1633); Individual spell undertuned (WR: 43.8%, Casts: 1633, mult: 1.021) |
| `WWL` | Water | Buff / Sustain | 63.0 -> **63.8** (+1.3%) | - | 63.0 -> **63.8** | Individual spell undertuned (WR: 46.0%, Casts: 2291, mult: 1.013) |
| `WWD` | Water | Buff / Sustain | 47.9 -> **47.1** (-1.7%) | - | 47.9 -> **47.1** | Individual spell overtuned (WR: 54.9%, Casts: 1669, mult: 0.984) |
| `EEF` | Earth | Conditional Strike | 28.4 -> **25.0** (-12.0%) | 4.4 -> **5.3** | 153.4 -> **157.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.8% vs 30% floor, Casts: 1785). Increasing spread: b -10.5%, n +21.4%; Individual spell overtuned (WR: 54.7%, Casts: 1785, mult: 0.984) |
| `EEW` | Earth | Buff / Sustain | 34.8 -> **33.7** (-3.2%) | - | 34.8 -> **33.7** | Individual spell overtuned (WR: 59.0%, Casts: 2327, mult: 0.968) |
| `EEE` | Earth | Conditional Strike | 8.1 -> **9.2** (+13.6%) | 1.5 -> **1.5** | 20.2 -> **23.0** | Condition triggers excessively (N=1 conditions, Trigger Rate: 94.1% vs 55% ceiling, WR: 51.5%). Compressing spread: b +13.7%, n -21.9% |
| `LLF` | Light | Conditional Strike | 3.4 -> **3.8** (+11.8%) | 10.8 -> **14.4** | 40.1 -> **58.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.7% vs 30% floor, Casts: 3367). Increasing spread: b -16.1%, n +33.1%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLE` | Light | Setup - Weather | 27.1 -> **32.5** (+19.9%) | - | 27.1 -> **32.5** | Weather 'Sunny' appliers undertuned (WR: 43.8%, casts: 2831); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 29.9 -> **28.9** (-3.3%) | - | 29.9 -> **28.9** | Individual spell overtuned (WR: 59.6%, Casts: 1935, mult: 0.966) |
| `LLD` | Light | Ultimate | 29.5 -> **29.5** (+0.0%) | 9.5 -> **12.1** | 309.8 -> **386.4** | Weather 'Sunny' beneficiaries overtuned (WR: 55.5%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 974). Shifted tuner focus: protected ultimate base floor at 29.5 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 7.6 -> **6.3** (-17.1%) | 14.1 -> **19.3** | 114.8 -> **127.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1845). Increasing spread: b -18.0%, n +36.9%; Individual spell undertuned (WR: 45.3%, Casts: 1845, mult: 1.015) |
| `DDW` | Dark | Debuff / Control | 53.0 -> **53.8** (+1.5%) | - | 53.0 -> **53.8** | Individual spell undertuned (WR: 45.5%, Casts: 2167, mult: 1.015) |
| `DDD` | Dark | Debuff / Control | 30.8 -> **29.5** (-4.2%) | - | 30.8 -> **29.5** | Individual spell overtuned (WR: 61.6%, Casts: 1304, mult: 0.958) |
| `FWF` | Ghostfire | Debuff / Control | 41.4 -> **40.5** (-2.2%) | - | 41.4 -> **40.5** | Individual spell overtuned (WR: 56.2%, Casts: 1973, mult: 0.979) |
| `FWW` | Ghostfire | Debuff / Control | 28.0 -> **29.1** (+3.9%) | - | 28.0 -> **29.1** | Status 'Cursed' appliers undertuned (WR: 45.5%, casts: 5823); Individual spell undertuned (WR: 43.4%, Casts: 1960, mult: 1.023) |
| `FWE` | Ghostfire | Setup - Location | 46.9 -> **51.6** (+10.0%) | - | 46.9 -> **51.6** | Location 'Graveyard' appliers undertuned (WR: 36.4%, casts: 2911); Individual spell undertuned (WR: 36.3%, Casts: 2911, mult: 1.050) |
| `FWL` | Ghostfire | Debuff / Control | 77.6 -> **80.1** (+3.2%) | - | 77.6 -> **80.1** | Status 'Cursed' appliers undertuned (WR: 45.5%, casts: 5823); Individual spell undertuned (WR: 45.0%, Casts: 2920, mult: 1.017) |
| `FWD` | Ghostfire | Ultimate | 25.0 -> **27.5** (+10.0%) | 18.9 -> **18.5** | 497.5 -> **536.2** | Status 'Cursed' beneficiaries undertuned (WR: 46.2%); Location 'Graveyard' beneficiaries undertuned (WR: 44.2%) |
| `WFF` | Ghostfire | Conditional Strike | 10.1 -> **8.5** (-15.8%) | 10.8 -> **14.2** | 119.2 -> **129.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 2038). Increasing spread: b -15.4%, n +31.6% |
| `WFE` | Ghostfire | Debuff / Control | 38.5 -> **33.5** (-13.0%) | - | 38.5 -> **33.5** | Status 'Bleeding' appliers overtuned on own (WR: 65.9%); Individual spell overtuned (WR: 70.4%, Casts: 1250, mult: 0.922) |
| `WFL` | Ghostfire | Buff / Sustain | 36.0 -> **36.5** (+1.4%) | - | 36.0 -> **36.5** | Individual spell undertuned (WR: 46.0%, Casts: 1694, mult: 1.013) |
| `WFD` | Ghostfire | Conditional Strike | 11.9 -> **10.5** (-11.8%) | 9.6 -> **12.6** | 126.1 -> **142.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.4% vs 30% floor, Casts: 2359). Increasing spread: b -15.0%, n +30.8%; Individual spell undertuned (WR: 40.4%, Casts: 2359, mult: 1.034) |
| `FEF` | Beasts | Debuff / Control | 28.9 -> **29.7** (+2.8%) | - | 28.9 -> **29.7** | Individual spell undertuned (WR: 42.5%, Casts: 2321, mult: 1.026) |
| `FEW` | Beasts | Conditional Strike | 8.3 -> **6.6** (-20.5%) | 13.8 -> **18.5** | 122.8 -> **128.7** | Status 'Entangled' beneficiaries overtuned (WR: 54.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 1454). Increasing spread: b -17.7%, n +36.3% |
| `FEE` | Beasts | Buff / Sustain | 25.5 -> **26.3** (+3.1%) | - | 25.5 -> **26.3** | Individual spell undertuned (WR: 41.2%, Casts: 2383, mult: 1.031) |
| `FEL` | Beasts | Buff / Sustain | 25.9 -> **26.9** (+3.9%) | - | 25.9 -> **26.9** | Individual spell undertuned (WR: 38.8%, Casts: 1488, mult: 1.040) |
| `FED` | Beasts | Conditional Strike | 7.8 -> **8.3** (+6.4%) | 1.5 -> **1.5** | 19.5 -> **20.8** | Condition triggers excessively (N=1 conditions, Trigger Rate: 57.6% vs 55% ceiling, WR: 52.1%). Compressing spread: b +6.4%, n -9.8% |
| `EFF` | Beasts | Debuff / Control | 10.4 -> **8.5** (-18.3%) | 13.6 -> **18.4** | 151.8 -> **164.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.3% vs 30% floor, Casts: 2076). Increasing spread: b -17.1%, n +35.1%; Individual spell overtuned (WR: 55.3%, Casts: 2076, mult: 0.982) |
| `EFL` | Beasts | Buff / Sustain | 16.2 -> **14.0** (-13.6%) | - | 16.2 -> **14.0** | Individual spell overtuned (WR: 84.1%, Casts: 2164, mult: 0.862) |
| `EFD` | Beasts | Ultimate | 29.8 -> **29.8** (+0.0%) | 10.5 -> **13.3** | 342.7 -> **426.1** | Status 'Entangled' beneficiaries overtuned (WR: 54.1%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.7% vs 16% floor, Casts: 1329). Shifted tuner focus: protected ultimate base floor at 29.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo. |
| `FLF` | Lightning | Conditional Strike | 8.8 -> **7.2** (-18.2%) | 15.4 -> **21.7** | 144.3 -> **163.4** | Status 'Stunned' beneficiaries undertuned (WR: 41.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 1745). Increasing spread: b -17.7%, n +36.4% |
| `FLD` | Lightning | Ultimate | 36.4 -> **41.1** (+12.9%) | 9.2 -> **9.4** | 371.3 -> **427.4** | Status 'Stunned' beneficiaries undertuned (WR: 41.1%); Weather 'Storming' beneficiaries undertuned (WR: 37.4%) |
| `LFF` | Lightning | Conditional Strike | 9.1 -> **7.5** (-17.6%) | 12.9 -> **17.2** | 126.5 -> **136.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.9% vs 30% floor, Casts: 1521). Increasing spread: b -16.4%, n +33.7%; Individual spell overtuned (WR: 55.8%, Casts: 1521, mult: 0.980) |
| `LFL` | Lightning | Debuff / Control | 34.7 -> **30.4** (-12.4%) | 9.4 -> **11.8** | 360.9 -> **389.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.4% vs 30% floor, Casts: 3139). Increasing spread: b -12.3%, n +25.0% |
| `LFD` | Lightning | Conditional Strike | 12.5 -> **10.7** (-14.4%) | 15.5 -> **20.4** | 206.2 -> **229.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 2607). Increasing spread: b -15.5%, n +31.8%; Individual spell undertuned (WR: 44.9%, Casts: 2607, mult: 1.017) |
| `FDF` | Blood | Conditional Strike | 8.3 -> **6.7** (-19.3%) | 14.1 -> **19.3** | 125.3 -> **136.0** | Class Blood overtuned (WR: 55.4%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1872). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 59.8 -> **58.5** (-2.2%) | - | 59.8 -> **58.5** | Class Blood overtuned (WR: 55.4%, factor: 0.978) |
| `FDE` | Blood | Setup - Weather | 20.0 -> **19.9** (-0.5%) | - | 20.0 -> **19.9** | Class Blood overtuned (WR: 55.4%, factor: 0.978); Individual spell undertuned (WR: 45.0%, Casts: 2049, mult: 1.017) |
| `FDL` | Blood | Debuff / Control | 30.3 -> **25.5** (-15.8%) | - | 30.3 -> **25.5** | Class Blood overtuned (WR: 55.4%, factor: 0.978); Status 'Bleeding' appliers overtuned on own (WR: 65.9%) |
| `FDD` | Blood | Ultimate | 32.4 -> **34.8** (+7.4%) | 7.5 -> **7.0** | 275.4 -> **278.4** | Class Blood overtuned (WR: 55.4%, factor: 0.978); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.9% vs 16% floor, Casts: 1692, WR: 44.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 10.0 -> **8.3** (-17.0%) | 10.1 -> **13.2** | 111.0 -> **117.9** | Class Blood overtuned (WR: 55.4%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.7% vs 30% floor, Casts: 1506). Increasing spread: b -14.9%, n +30.6% |
| `DFW` | Blood | Debuff / Control | 28.9 -> **24.7** (-14.5%) | - | 28.9 -> **24.7** | Class Blood overtuned (WR: 55.4%, factor: 0.978); Status 'Bleeding' appliers overtuned on own (WR: 65.9%) |
| `DFE` | Blood | Buff / Sustain | 35.0 -> **34.2** (-2.3%) | - | 35.0 -> **34.2** | Class Blood overtuned (WR: 55.4%, factor: 0.978) |
| `DFL` | Blood | Buff / Sustain | 33.1 -> **32.4** (-2.1%) | - | 33.1 -> **32.4** | Class Blood overtuned (WR: 55.4%, factor: 0.978) |
| `DFD` | Blood | Conditional Strike | 51.8 -> **57.8** (+11.6%) | 0.5 -> **0.4** | 77.7 -> **80.9** | Class Blood overtuned (WR: 55.4%, factor: 0.978); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.5% vs 55% ceiling, WR: 56.6%). Compressing spread: b +16.6%, n -25.0% |
| `WEF` | Plants | Conditional Strike | 11.5 -> **9.9** (-13.9%) | 9.1 -> **11.7** | 116.1 -> **125.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.3% vs 30% floor, Casts: 1856). Increasing spread: b -13.9%, n +28.4% |
| `WEE` | Plants | Setup - Location | 20.6 -> **22.2** (+7.8%) | - | 20.6 -> **22.2** | Location 'Jungle' appliers undertuned (WR: 39.5%, casts: 2668); Individual spell undertuned (WR: 39.5%, Casts: 2668, mult: 1.038) |
| `WED` | Plants | Conditional Strike | 10.7 -> **9.1** (-15.0%) | 12.9 -> **17.0** | 148.7 -> **163.8** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 1.7% vs 8% floor, Casts: 1617). Increasing spread: b -15.4%, n +31.6% |
| `EWF` | Plants | Buff / Sustain | 13.2 -> **11.1** (-15.9%) | 8.3 -> **10.5** | 122.8 -> **127.6** | Weather 'Sunny' beneficiaries overtuned (WR: 55.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.7% vs 30% floor, Casts: 3503). Increasing spread: b -14.1%, n +28.9% |
| `EWW` | Plants | Debuff / Control | 20.9 -> **18.1** (-13.4%) | - | 20.9 -> **18.1** | Individual spell overtuned (WR: 83.4%, Casts: 1894, mult: 0.865) |
| `EWL` | Plants | Debuff / Control | 58.2 -> **59.3** (+1.9%) | - | 58.2 -> **59.3** | Individual spell undertuned (WR: 44.5%, Casts: 2127, mult: 1.018) |
| `EWD` | Plants | Conditional Strike | 13.2 -> **10.2** (-22.7%) | 13.5 -> **17.9** | 191.4 -> **192.8** | Status 'Bleeding' appliers overtuned on own (WR: 65.9%); Status 'Entangled' beneficiaries overtuned (WR: 54.1%) |
| `WLF` | Fey | Conditional Strike | 10.2 -> **8.6** (-15.7%) | 11.7 -> **15.7** | 129.5 -> **143.6** | Status 'Cursed' beneficiaries undertuned (WR: 46.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.0% vs 30% floor, Casts: 2020). Increasing spread: b -15.6%, n +32.0% |
| `WLW` | Fey | Debuff / Control | 47.1 -> **47.8** (+1.5%) | - | 47.1 -> **47.8** | Status 'Cursed' appliers undertuned (WR: 45.5%, casts: 5823) |
| `WLL` | Fey | Direct Damage | 63.1 -> **61.5** (-2.5%) | - | 63.1 -> **61.5** | Individual spell overtuned (WR: 57.3%, Casts: 1453, mult: 0.975) |
| `WLD` | Fey | Ultimate | 26.2 -> **28.3** (+8.0%) | 20.2 -> **19.0** | 555.4 -> **566.0** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1174, WR: 47.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `LWF` | Fey | Debuff / Control | 26.8 -> **23.7** (-11.6%) | 7.7 -> **9.5** | 233.2 -> **248.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 16.4% vs 30% floor, Casts: 1893). Increasing spread: b -11.4%, n +23.3% |
| `LWW` | Fey | Debuff / Control | 38.9 -> **40.9** (+5.1%) | - | 38.9 -> **40.9** | Individual spell undertuned (WR: 35.9%, Casts: 2641, mult: 1.052) |
| `LWD` | Fey | Conditional Strike | 9.2 -> **7.5** (-18.5%) | 14.1 -> **19.3** | 138.9 -> **152.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1798). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 10.3 -> **9.0** (-12.6%) | 12.7 -> **17.6** | 141.1 -> **167.4** | Weather 'Raining' beneficiaries undertuned (WR: 36.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.8% vs 30% floor, Casts: 2019). Increasing spread: b -15.3%, n +31.3% |
| `WDE` | Ice | Setup - Weather | 21.6 -> **22.4** (+3.7%) | - | 21.6 -> **22.4** | Individual spell undertuned (WR: 39.1%, Casts: 2155, mult: 1.039) |
| `WDD` | Ice | Ultimate | 28.7 -> **28.4** (-1.0%) | 12.7 -> **15.8** | 393.2 -> **477.1** | Weather 'Blizzard' beneficiaries overtuned (WR: 53.6%); Location 'Tundra' beneficiaries overtuned (WR: 53.6%) |
| `DWF` | Ice | Debuff / Control | 45.2 -> **46.3** (+2.4%) | - | 45.2 -> **46.3** | Individual spell undertuned (WR: 43.0%, Casts: 2459, mult: 1.024) |
| `DWE` | Ice | Setup - Location | 25.1 -> **26.3** (+4.8%) | - | 25.1 -> **26.3** | Location 'Tundra' appliers undertuned (WR: 43.2%, casts: 2204); Individual spell undertuned (WR: 43.2%, Casts: 2204, mult: 1.023) |
| `DWD` | Ice | Conditional Strike | 17.2 -> **15.5** (-9.9%) | 5.9 -> **7.1** | 118.7 -> **125.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 20.6% vs 30% floor, Casts: 2353). Increasing spread: b -9.8%, n +19.9% |
| `ELF` | Wind | Conditional Strike | 22.1 -> **18.7** (-15.4%) | 10.5 -> **13.8** | 254.2 -> **276.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 934). Increasing spread: b -15.4%, n +31.6% |
| `ELE` | Wind | Setup - Weather | 19.9 -> **20.2** (+1.5%) | - | 19.9 -> **20.2** | Individual spell undertuned (WR: 45.9%, Casts: 1864, mult: 1.013) |
| `ELL` | Wind | Buff / Sustain | 36.8 -> **37.3** (+1.4%) | - | 36.8 -> **37.3** | Individual spell undertuned (WR: 45.5%, Casts: 1938, mult: 1.015) |
| `ELD` | Wind | Conditional Strike | 11.6 -> **10.9** (-6.0%) | 10.9 -> **15.3** | 138.0 -> **177.7** | Weather 'Raining' beneficiaries undertuned (WR: 36.4%); Weather 'Blizzard' appliers undertuned (WR: 34.1%, casts: 3424) |
| `LEF` | Wind | Conditional Strike | 9.9 -> **8.2** (-17.2%) | 11.8 -> **15.5** | 126.7 -> **135.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.2% vs 30% floor, Casts: 2072). Increasing spread: b -15.1%, n +31.0%; Individual spell overtuned (WR: 58.2%, Casts: 2072, mult: 0.971) |
| `EDF` | Poison | Conditional Strike | 8.5 -> **7.3** (-14.1%) | 11.3 -> **15.0** | 104.6 -> **116.8** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 2372). Increasing spread: b -15.8%, n +32.4% |
| `EDW` | Poison | Debuff / Control | 28.3 -> **26.7** (-5.7%) | - | 28.3 -> **26.7** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 60.3%, Casts: 1716, mult: 0.963) |
| `EDL` | Poison | Debuff / Control | 9.7 -> **8.1** (-16.5%) | - | 9.7 -> **8.1** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 85.8%, Casts: 2542, mult: 0.855) |
| `EDD` | Poison | Ultimate | 27.3 -> **29.5** (+8.1%) | 10.5 -> **10.1** | 313.9 -> **327.4** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Location 'Swamp' beneficiaries undertuned (WR: 44.0%) |
| `DEF` | Poison | Conditional Strike | 35.0 -> **34.3** (-2.0%) | 1.7 -> **1.7** | 94.5 -> **92.6** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 48.1% within [30%-55%] target window, WR: 50.1%). |
| `DEW` | Poison | Debuff / Control | 27.1 -> **25.3** (-6.6%) | - | 27.1 -> **25.3** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 63.4%, Casts: 2853, mult: 0.951) |
| `DEE` | Poison | Debuff / Control | 25.6 -> **25.1** (-2.0%) | - | 25.6 -> **25.1** | Class Poison overtuned (WR: 54.9%, factor: 0.980) |
| `DEL` | Poison | Conditional Strike | 1.0 -> **0.8** (-20.0%) | 10.4 -> **13.6** | 11.4 -> **11.7** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.0% vs 30% floor, Casts: 1716). Increasing spread: b -15.2%, n +31.2% |
| `DED` | Poison | Debuff / Control | 26.2 -> **26.0** (-0.8%) | - | 26.2 -> **26.0** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell undertuned (WR: 46.3%, Casts: 2140, mult: 1.012) |
| `LDF` | Cosmic | Debuff / Control | 58.7 -> **59.4** (+1.2%) | - | 58.7 -> **59.4** | Individual spell undertuned (WR: 46.2%, Casts: 878, mult: 1.012) |
| `LDW` | Cosmic | Debuff / Control | 48.1 -> **46.9** (-2.5%) | - | 48.1 -> **46.9** | Individual spell overtuned (WR: 57.1%, Casts: 2868, mult: 0.975) |
| `LDE` | Cosmic | Setup - Location | 22.7 -> **23.2** (+2.2%) | - | 22.7 -> **23.2** | Individual spell undertuned (WR: 43.1%, Casts: 1944, mult: 1.024) |
| `LDL` | Cosmic | Conditional Strike | 11.0 -> **9.4** (-14.5%) | 11.1 -> **14.9** | 133.1 -> **149.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.9% vs 30% floor, Casts: 2135). Increasing spread: b -16.8%, n +34.5%; Individual spell undertuned (WR: 42.1%, Casts: 2135, mult: 1.027) |
| `LDD` | Cosmic | Ultimate | 36.3 -> **39.7** (+9.4%) | 7.3 -> **6.9** | 301.3 -> **313.6** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1848, WR: 46.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 46.5%, Casts: 1848, mult: 1.011) |
| `DLF` | Cosmic | Conditional Strike | 12.4 -> **10.8** (-12.9%) | 11.4 -> **15.1** | 153.8 -> **173.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.6% vs 30% floor, Casts: 1936). Increasing spread: b -15.8%, n +32.4%; Individual spell undertuned (WR: 41.5%, Casts: 1936, mult: 1.030) |
| `DLE` | Cosmic | Direct Damage | 41.0 -> **42.5** (+3.7%) | - | 41.0 -> **42.5** | Individual spell undertuned (WR: 39.9%, Casts: 1583, mult: 1.036) |
| `DLL` | Cosmic | Conditional Strike | 24.1 -> **20.9** (-13.3%) | 7.1 -> **9.2** | 195.2 -> **213.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.0% vs 30% floor, Casts: 1682). Increasing spread: b -14.4%, n +29.5%; Individual spell undertuned (WR: 46.3%, Casts: 1682, mult: 1.012) |
