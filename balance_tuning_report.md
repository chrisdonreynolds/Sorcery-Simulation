# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T22:42:19Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 715.0s  
**Total Spells Tuned:** 92 / 125  

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
| **Poison** | 20,837 | 55.6% | 55.6% | 10.1 | Overtuned ⚠️ |
| **Blood** | 18,209 | 53.2% | 53.2% | 12.1 | Balanced ✅ |
| **Plants** | 21,818 | 52.8% | 52.8% | 8.8 | Balanced ✅ |
| **Beasts** | 18,884 | 52.2% | 52.2% | 6.8 | Balanced ✅ |
| **Dark** | 10,544 | 51.4% | 51.4% | 11.9 | Balanced ✅ |
| **Ghostfire** | 20,310 | 51.1% | 51.1% | 14.5 | Balanced ✅ |
| **Earth** | 9,030 | 50.6% | 50.6% | 17.1 | Balanced ✅ |
| **Light** | 11,429 | 50.2% | 50.2% | 5.1 | Balanced ✅ |
| **Fire** | 9,309 | 49.3% | 49.3% | 15.3 | Balanced ✅ |
| **Lightning** | 20,554 | 48.4% | 48.4% | 10.6 | Balanced ✅ |
| **Wind** | 18,235 | 47.9% | 47.9% | 8.2 | Balanced ✅ |
| **Ice** | 20,094 | 47.6% | 47.6% | 12.8 | Balanced ✅ |
| **Fey** | 18,364 | 47.0% | 47.0% | 7.8 | Balanced ✅ |
| **Cosmic** | 17,872 | 46.6% | 46.6% | 15.7 | Balanced ✅ |
| **Water** | 9,494 | 46.2% | 46.2% | 9.5 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,612 (50.8%) | 4,306 (51.7%) | 17.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,765 (38.6%) | 5,324 (55.0%) | 9.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,489 (55.0%) | 5,683 (51.6%) | 7.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 7,772 (67.0%) | 10,130 (48.1%) | 5.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 13,625 (47.5%) | 4,385 (44.9%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 3,082 (51.3%) | 4,311 (47.0%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,511 (40.3%) | 5,567 (36.7%) | 5.4% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 47.4 -> **46.6** (-1.7%) | - | 47.4 -> **46.6** | Status 'Burning' appliers overtuned on own (WR: 55.0%) |
| `FFL` | Fire | Debuff / Control | 7.5 -> **7.2** (-4.0%) | - | 7.5 -> **7.2** | Status 'Burning' appliers overtuned on own (WR: 55.0%); Individual spell overtuned (WR: 55.6%, Casts: 1235, mult: 0.981) |
| `FFD` | Fire | Conditional Strike | 9.1 -> **7.7** (-15.4%) | 13.5 -> **17.8** | 131.9 -> **144.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.5% vs 30% floor, Casts: 2408). Increasing spread: b -15.4%, n +31.6% |
| `WWF` | Water | Conditional Strike | 16.2 -> **14.2** (-12.3%) | 11.6 -> **14.9** | 204.1 -> **225.8** | Class Water undertuned (WR: 46.2%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.5% vs 30% floor, Casts: 1615). Increasing spread: b -13.8%, n +28.3% |
| `WWE` | Water | Setup - Weather | 25.6 -> **27.8** (+8.6%) | - | 25.6 -> **27.8** | Class Water undertuned (WR: 46.2%, factor: 1.015); Weather 'Raining' appliers undertuned (WR: 40.3%, casts: 1511) |
| `WWL` | Water | Buff / Sustain | 63.8 -> **64.8** (+1.6%) | - | 63.8 -> **64.8** | Class Water undertuned (WR: 46.2%, factor: 1.015) |
| `WWD` | Water | Buff / Sustain | 47.1 -> **47.8** (+1.5%) | - | 47.1 -> **47.8** | Class Water undertuned (WR: 46.2%, factor: 1.015) |
| `EEF` | Earth | Conditional Strike | 25.0 -> **22.5** (-10.0%) | 5.3 -> **6.4** | 157.5 -> **166.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 20.2% vs 30% floor, Casts: 2277). Increasing spread: b -9.9%, n +20.2% |
| `EEW` | Earth | Buff / Sustain | 33.7 -> **32.7** (-3.0%) | - | 33.7 -> **32.7** | Individual spell overtuned (WR: 58.2%, Casts: 1643, mult: 0.971) |
| `EEE` | Earth | Conditional Strike | 9.2 -> **10.0** (+8.7%) | 1.5 -> **1.5** | 23.0 -> **25.0** | Condition triggers excessively (N=1 conditions, Trigger Rate: 92.4% vs 55% ceiling, WR: 53.1%). Compressing spread: b +14.5%, n -22.5% |
| `EED` | Earth | Direct Damage | 6.6 -> **6.8** (+3.0%) | - | 6.6 -> **6.8** | Individual spell undertuned (WR: 42.8%, Casts: 1439, mult: 1.025) |
| `LLF` | Light | Conditional Strike | 3.8 -> **3.1** (-18.4%) | 14.4 -> **19.1** | 58.5 -> **62.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 3093). Increasing spread: b -15.8%, n +32.5%; Individual spell overtuned (WR: 57.4%, Casts: 3093, mult: 0.974) |
| `LLW` | Light | Debuff / Control | 34.1 -> **39.2** (+15.0%) | - | 34.1 -> **39.2** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LLE` | Light | Setup - Weather | 32.5 -> **35.2** (+8.3%) | - | 32.5 -> **35.2** | Weather 'Sunny' appliers undertuned (WR: 38.6%, casts: 2765); Individual spell undertuned (WR: 38.6%, Casts: 2765, mult: 1.041) |
| `LLL` | Light | Buff / Sustain | 28.9 -> **27.5** (-4.8%) | - | 28.9 -> **27.5** | Individual spell overtuned (WR: 63.1%, Casts: 1681, mult: 0.952) |
| `LLD` | Light | Ultimate | 29.5 -> **31.9** (+8.1%) | 12.1 -> **11.1** | 386.4 -> **386.0** | Weather 'Sunny' beneficiaries overtuned (WR: 55.0%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1536, WR: 47.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 6.3 -> **5.3** (-15.9%) | 19.3 -> **26.4** | 127.9 -> **145.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1931). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 43.1%, Casts: 1931, mult: 1.024) |
| `DDE` | Dark | Setup - Weather | 36.6 -> **40.3** (+10.1%) | - | 36.6 -> **40.3** | Weather 'Darkness' appliers overtuned on own (WR: 56.3%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `DDD` | Dark | Debuff / Control | 29.5 -> **28.7** (-2.7%) | - | 29.5 -> **28.7** | Individual spell overtuned (WR: 57.8%, Casts: 1929, mult: 0.973) |
| `FWF` | Ghostfire | Debuff / Control | 40.5 -> **38.4** (-5.2%) | - | 40.5 -> **38.4** | Status 'Burning' appliers overtuned on own (WR: 55.0%); Individual spell overtuned (WR: 60.0%, Casts: 1900, mult: 0.964) |
| `FWE` | Ghostfire | Setup - Location | 51.6 -> **57.6** (+11.6%) | - | 51.6 -> **57.6** | Location 'Graveyard' appliers undertuned (WR: 34.3%, casts: 2203); Individual spell undertuned (WR: 34.3%, Casts: 2203, mult: 1.059) |
| `FWD` | Ghostfire | Ultimate | 27.5 -> **30.9** (+12.4%) | 18.5 -> **18.9** | 536.2 -> **614.9** | Status 'Cursed' beneficiaries undertuned (WR: 39.8%); Location 'Graveyard' beneficiaries undertuned (WR: 39.2%) |
| `WFF` | Ghostfire | Conditional Strike | 8.5 -> **7.4** (-12.9%) | 14.2 -> **18.3** | 129.2 -> **142.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.7% vs 30% floor, Casts: 2201). Increasing spread: b -14.1%, n +28.9%; Individual spell undertuned (WR: 46.3%, Casts: 2201, mult: 1.012) |
| `WFW` | Ghostfire | Debuff / Control | 30.5 -> **29.7** (-2.6%) | - | 30.5 -> **29.7** | Individual spell overtuned (WR: 57.5%, Casts: 2780, mult: 0.974) |
| `WFE` | Ghostfire | Debuff / Control | 33.5 -> **33.4** (-0.3%) | - | 33.5 -> **33.4** | Status 'Bleeding' appliers overtuned on own (WR: 67.0%); Buffed setup spell [WFE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `WFL` | Ghostfire | Buff / Sustain | 36.5 -> **36.0** (-1.4%) | - | 36.5 -> **36.0** | Individual spell overtuned (WR: 54.2%, Casts: 942, mult: 0.986) |
| `WFD` | Ghostfire | Conditional Strike | 10.5 -> **9.0** (-14.3%) | 12.6 -> **16.4** | 142.8 -> **156.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.3% vs 30% floor, Casts: 1859). Increasing spread: b -14.7%, n +30.1% |
| `FEW` | Beasts | Conditional Strike | 6.6 -> **5.6** (-15.2%) | 18.5 -> **25.3** | 128.7 -> **147.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 1155). Increasing spread: b -17.8%, n +36.6%; Individual spell undertuned (WR: 40.3%, Casts: 1155, mult: 1.035) |
| `FEL` | Beasts | Buff / Sustain | 26.9 -> **27.6** (+2.6%) | - | 26.9 -> **27.6** | Individual spell undertuned (WR: 42.6%, Casts: 1219, mult: 1.026) |
| `FED` | Beasts | Conditional Strike | 8.3 -> **8.8** (+6.0%) | 1.5 -> **1.5** | 20.8 -> **22.0** | Condition triggers excessively (N=1 conditions, Trigger Rate: 57.8% vs 55% ceiling, WR: 51.8%). Compressing spread: b +5.6%, n -9.0% |
| `EFF` | Beasts | Debuff / Control | 8.5 -> **7.0** (-17.6%) | 18.4 -> **24.9** | 164.9 -> **181.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 2181). Increasing spread: b -17.3%, n +35.5% |
| `EFW` | Beasts | Buff / Sustain | 24.3 -> **25.0** (+2.9%) | - | 24.3 -> **25.0** | Individual spell undertuned (WR: 41.6%, Casts: 1808, mult: 1.030) |
| `EFL` | Beasts | Buff / Sustain | 14.0 -> **12.0** (-14.3%) | - | 14.0 -> **12.0** | Individual spell overtuned (WR: 85.4%, Casts: 2115, mult: 0.857) |
| `EFD` | Beasts | Ultimate | 29.8 -> **29.8** (+0.0%) | 13.3 -> **17.2** | 426.1 -> **542.4** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.3% vs 16% floor, Casts: 1514). Shifted tuner focus: protected ultimate base floor at 29.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo. |
| `FLF` | Lightning | Conditional Strike | 7.2 -> **5.9** (-18.1%) | 21.7 -> **30.3** | 163.4 -> **184.7** | Status 'Stunned' beneficiaries undertuned (WR: 44.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1844). Increasing spread: b -17.9%, n +36.7% |
| `FLW` | Lightning | Debuff / Control | 54.2 -> **53.5** (-1.3%) | - | 54.2 -> **53.5** | Individual spell overtuned (WR: 54.0%, Casts: 1311, mult: 0.987) |
| `FLL` | Lightning | Buff / Sustain | 26.0 -> **26.4** (+1.5%) | - | 26.0 -> **26.4** | Individual spell undertuned (WR: 45.0%, Casts: 1753, mult: 1.017) |
| `FLD` | Lightning | Ultimate | 41.1 -> **45.3** (+10.2%) | 9.4 -> **9.2** | 427.4 -> **462.1** | Status 'Stunned' beneficiaries undertuned (WR: 44.9%); Weather 'Storming' beneficiaries undertuned (WR: 43.7%) |
| `LFF` | Lightning | Conditional Strike | 7.5 -> **6.2** (-17.3%) | 17.2 -> **23.3** | 136.5 -> **150.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 1593). Increasing spread: b -17.3%, n +35.6% |
| `LFL` | Lightning | Debuff / Control | 30.4 -> **35.0** (+15.1%) | 11.8 -> **14.8** | 389.1 -> **553.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.6% vs 30% floor, Casts: 2735). Increasing spread: b -12.5%, n +25.6%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 10.7 -> **9.2** (-14.0%) | 20.4 -> **26.3** | 229.0 -> **251.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.5% vs 30% floor, Casts: 1716). Increasing spread: b -14.2%, n +29.1% |
| `FDF` | Blood | Conditional Strike | 6.7 -> **5.6** (-16.4%) | 19.3 -> **26.4** | 136.0 -> **153.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1703). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 46.0%, Casts: 1703, mult: 1.013) |
| `FDW` | Blood | Direct Damage | 58.5 -> **60.1** (+2.7%) | - | 58.5 -> **60.1** | Individual spell undertuned (WR: 42.2%, Casts: 1650, mult: 1.027) |
| `FDE` | Blood | Setup - Weather | 19.9 -> **20.4** (+2.5%) | - | 19.9 -> **20.4** | Individual spell undertuned (WR: 43.4%, Casts: 2253, mult: 1.023) |
| `FDL` | Blood | Debuff / Control | 25.5 -> **25.0** (-2.0%) | - | 25.5 -> **25.0** | Status 'Bleeding' appliers overtuned on own (WR: 67.0%); Buffed setup spell [FDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `FDD` | Blood | Ultimate | 34.8 -> **34.8** (+0.0%) | 7.0 -> **9.0** | 278.4 -> **348.0** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.7% vs 16% floor, Casts: 1399). Shifted tuner focus: protected ultimate base floor at 34.8 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 8.3 -> **7.0** (-15.7%) | 13.2 -> **17.4** | 117.9 -> **128.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.0% vs 30% floor, Casts: 1622). Increasing spread: b -15.6%, n +32.0% |
| `DFW` | Blood | Debuff / Control | 24.7 -> **24.4** (-1.2%) | - | 24.7 -> **24.4** | Status 'Bleeding' appliers overtuned on own (WR: 67.0%); Buffed setup spell [DFW] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `DFE` | Blood | Buff / Sustain | 34.2 -> **35.0** (+2.3%) | - | 34.2 -> **35.0** | Individual spell undertuned (WR: 42.9%, Casts: 1619, mult: 1.025) |
| `DFL` | Blood | Buff / Sustain | 32.4 -> **33.1** (+2.2%) | - | 32.4 -> **33.1** | Individual spell undertuned (WR: 43.4%, Casts: 1316, mult: 1.023) |
| `DFD` | Blood | Conditional Strike | 57.8 -> **65.8** (+13.8%) | 0.4 -> **0.3** | 80.9 -> **85.5** | Condition triggers excessively (N=1 conditions, Trigger Rate: 94.8% vs 55% ceiling, WR: 50.9%). Compressing spread: b +13.8%, n -22.1% |
| `WEF` | Plants | Conditional Strike | 9.9 -> **8.6** (-13.1%) | 11.7 -> **14.6** | 125.7 -> **134.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.0% vs 30% floor, Casts: 858). Increasing spread: b -12.0%, n +24.5%; Individual spell overtuned (WR: 54.1%, Casts: 858, mult: 0.986) |
| `WEW` | Plants | Debuff / Control | 63.7 -> **74.7** (+17.3%) | - | 63.7 -> **74.7** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 44.0%, Casts: 1534, mult: 1.020) |
| `WED` | Plants | Conditional Strike | 9.1 -> **10.1** (+11.0%) | 17.0 -> **16.0** | 163.8 -> **171.7** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.9% vs 8% floor, Casts: 1948, WR: 43.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 43.2%, Casts: 1948, mult: 1.024) |
| `EWF` | Plants | Buff / Sustain | 11.1 -> **9.4** (-15.3%) | 10.5 -> **13.0** | 127.6 -> **131.6** | Weather 'Sunny' beneficiaries overtuned (WR: 55.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.6% vs 30% floor, Casts: 3788). Increasing spread: b -13.0%, n +26.5% |
| `EWW` | Plants | Debuff / Control | 18.1 -> **15.4** (-14.9%) | - | 18.1 -> **15.4** | Individual spell overtuned (WR: 87.1%, Casts: 2255, mult: 0.849) |
| `EWL` | Plants | Debuff / Control | 59.3 -> **60.4** (+1.9%) | - | 59.3 -> **60.4** | Individual spell undertuned (WR: 44.3%, Casts: 2942, mult: 1.019) |
| `EWD` | Plants | Conditional Strike | 10.2 -> **11.0** (+7.8%) | 17.9 -> **24.1** | 192.8 -> **276.1** | Status 'Bleeding' appliers overtuned on own (WR: 67.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.7% vs 30% floor, Casts: 1642). Increasing spread: b -16.9%, n +34.8% |
| `WLF` | Fey | Conditional Strike | 8.6 -> **7.5** (-12.8%) | 15.7 -> **21.5** | 143.6 -> **168.8** | Status 'Cursed' beneficiaries undertuned (WR: 39.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 2343). Increasing spread: b -15.3%, n +31.4% |
| `WLE` | Fey | Setup - Location | 41.4 -> **50.6** (+22.2%) | - | 41.4 -> **50.6** | Location 'Enchanted Forest' appliers undertuned (WR: 41.1%, casts: 1671); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLD` | Fey | Ultimate | 28.3 -> **27.8** (-1.8%) | 19.0 -> **24.7** | 566.0 -> **714.5** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 976). Shifted tuner focus: protected ultimate base floor at 28.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo.; Individual spell overtuned (WR: 54.9%, Casts: 976, mult: 0.984) |
| `LWF` | Fey | Debuff / Control | 23.7 -> **21.3** (-10.1%) | 9.5 -> **11.7** | 248.8 -> **270.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 16.6% vs 30% floor, Casts: 2768). Increasing spread: b -11.4%, n +23.2%; Individual spell undertuned (WR: 45.9%, Casts: 2768, mult: 1.013) |
| `LWD` | Fey | Conditional Strike | 7.5 -> **6.2** (-17.3%) | 19.3 -> **26.4** | 152.2 -> **169.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1505). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 9.0 -> **8.0** (-11.1%) | 17.6 -> **24.4** | 167.4 -> **203.2** | Weather 'Raining' beneficiaries undertuned (WR: 36.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.3% vs 30% floor, Casts: 2564). Increasing spread: b -15.5%, n +31.7% |
| `WDE` | Ice | Setup - Weather | 22.4 -> **23.6** (+5.4%) | - | 22.4 -> **23.6** | Individual spell undertuned (WR: 35.8%, Casts: 1407, mult: 1.053) |
| `WDD` | Ice | Ultimate | 28.4 -> **28.4** (+0.0%) | 15.8 -> **19.9** | 477.1 -> **593.6** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 3.4% vs 16% floor, Casts: 2068). Shifted tuner focus: protected ultimate base floor at 28.4 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWW` | Ice | Debuff / Control | 43.5 -> **42.8** (-1.6%) | - | 43.5 -> **42.8** | Individual spell overtuned (WR: 55.1%, Casts: 1708, mult: 0.983) |
| `DWD` | Ice | Conditional Strike | 15.5 -> **13.6** (-12.3%) | 7.1 -> **8.9** | 125.5 -> **134.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.8% vs 30% floor, Casts: 2029). Increasing spread: b -12.1%, n +24.7% |
| `ELF` | Wind | Conditional Strike | 18.7 -> **15.8** (-15.5%) | 13.8 -> **18.2** | 276.8 -> **303.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.3% vs 30% floor, Casts: 1156). Increasing spread: b -15.5%, n +31.7% |
| `ELW` | Wind | Debuff / Control | 42.5 -> **43.4** (+2.1%) | - | 42.5 -> **43.4** | Individual spell undertuned (WR: 44.1%, Casts: 1666, mult: 1.020) |
| `ELE` | Wind | Setup - Weather | 20.2 -> **20.8** (+3.0%) | - | 20.2 -> **20.8** | Individual spell undertuned (WR: 41.5%, Casts: 1548, mult: 1.030) |
| `ELD` | Wind | Conditional Strike | 10.9 -> **9.9** (-9.2%) | 15.3 -> **21.4** | 177.7 -> **221.8** | Weather 'Raining' beneficiaries undertuned (WR: 36.7%); Weather 'Blizzard' appliers undertuned (WR: 38.3%, casts: 3003) |
| `LEF` | Wind | Conditional Strike | 8.2 -> **6.7** (-18.3%) | 15.5 -> **20.4** | 135.3 -> **143.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 1660). Increasing spread: b -15.4%, n +31.7%; Individual spell overtuned (WR: 59.5%, Casts: 1660, mult: 0.966) |
| `LEW` | Wind | Debuff / Control | 56.7 -> **55.6** (-1.9%) | - | 56.7 -> **55.6** | Individual spell overtuned (WR: 55.5%, Casts: 3033, mult: 0.981) |
| `LEL` | Wind | Buff / Sustain | 39.7 -> **40.2** (+1.3%) | - | 39.7 -> **40.2** | Individual spell undertuned (WR: 46.5%, Casts: 1090, mult: 1.011) |
| `EDF` | Poison | Conditional Strike | 7.3 -> **6.2** (-15.1%) | 15.0 -> **20.1** | 116.8 -> **130.8** | Class Poison overtuned (WR: 55.6%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.6% vs 30% floor, Casts: 1541). Increasing spread: b -16.6%, n +34.0% |
| `EDW` | Poison | Debuff / Control | 26.7 -> **24.7** (-7.5%) | - | 26.7 -> **24.7** | Class Poison overtuned (WR: 55.6%, factor: 0.978); Individual spell overtuned (WR: 64.5%, Casts: 1941, mult: 0.946) |
| `EDE` | Poison | Setup - Location | 25.1 -> **30.0** (+19.5%) | - | 25.1 -> **30.0** | Class Poison overtuned (WR: 55.6%, factor: 0.978); Location 'Swamp' appliers undertuned (WR: 41.1%, casts: 1321) |
| `EDL` | Poison | Debuff / Control | 8.1 -> **6.8** (-16.0%) | - | 8.1 -> **6.8** | Class Poison overtuned (WR: 55.6%, factor: 0.978); Individual spell overtuned (WR: 85.2%, Casts: 2584, mult: 0.857) |
| `EDD` | Poison | Ultimate | 29.5 -> **28.8** (-2.4%) | 10.1 -> **13.0** | 327.4 -> **403.2** | Class Poison overtuned (WR: 55.6%, factor: 0.978); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.8% vs 16% floor, Casts: 2689). Shifted tuner focus: protected ultimate base floor at 29.5 (hard-coded floor >= 20.0) and buffed appliers/setups (WFE, FDL, DFW, EWD, EDE) with +15% b tempo. |
| `DEF` | Poison | Conditional Strike | 34.3 -> **33.5** (-2.3%) | 1.7 -> **1.7** | 92.6 -> **90.5** | Class Poison overtuned (WR: 55.6%, factor: 0.978); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 47.9% within [30%-55%] target window, WR: 48.2%). |
| `DEW` | Poison | Debuff / Control | 25.3 -> **23.7** (-6.3%) | - | 25.3 -> **23.7** | Class Poison overtuned (WR: 55.6%, factor: 0.978); Individual spell overtuned (WR: 61.2%, Casts: 2937, mult: 0.960) |
| `DEE` | Poison | Debuff / Control | 25.1 -> **23.8** (-5.2%) | - | 25.1 -> **23.8** | Class Poison overtuned (WR: 55.6%, factor: 0.978); Individual spell overtuned (WR: 58.2%, Casts: 1320, mult: 0.971) |
| `DEL` | Poison | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 13.6 -> **17.9** | 11.7 -> **13.2** | Class Poison overtuned (WR: 55.6%, factor: 0.978); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.3% vs 30% floor, Casts: 2462). Increasing spread: b -15.5%, n +31.8% |
| `DED` | Poison | Debuff / Control | 26.0 -> **25.4** (-2.3%) | - | 26.0 -> **25.4** | Class Poison overtuned (WR: 55.6%, factor: 0.978) |
| `LDF` | Cosmic | Debuff / Control | 59.4 -> **60.7** (+2.2%) | - | 59.4 -> **60.7** | Individual spell undertuned (WR: 43.8%, Casts: 934, mult: 1.021) |
| `LDE` | Cosmic | Setup - Location | 23.2 -> **24.1** (+3.9%) | - | 23.2 -> **24.1** | Individual spell undertuned (WR: 39.8%, Casts: 1764, mult: 1.037) |
| `LDL` | Cosmic | Conditional Strike | 9.4 -> **7.9** (-16.0%) | 14.9 -> **20.1** | 149.5 -> **166.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.9% vs 30% floor, Casts: 2172). Increasing spread: b -16.8%, n +34.6%; Individual spell undertuned (WR: 45.5%, Casts: 2172, mult: 1.015) |
| `LDD` | Cosmic | Ultimate | 39.7 -> **43.5** (+9.6%) | 6.9 -> **6.5** | 313.6 -> **326.2** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1675, WR: 45.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 45.6%, Casts: 1675, mult: 1.014) |
| `DLF` | Cosmic | Conditional Strike | 10.8 -> **9.1** (-15.7%) | 15.1 -> **20.1** | 173.9 -> **192.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 1521). Increasing spread: b -16.0%, n +32.9% |
| `DLE` | Cosmic | Direct Damage | 42.5 -> **43.8** (+3.1%) | - | 42.5 -> **43.8** | Individual spell undertuned (WR: 41.3%, Casts: 2145, mult: 1.030) |
| `DLL` | Cosmic | Conditional Strike | 20.9 -> **18.6** (-11.0%) | 9.2 -> **11.8** | 213.2 -> **238.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.2% vs 30% floor, Casts: 1300). Increasing spread: b -13.9%, n +28.5%; Individual spell undertuned (WR: 40.5%, Casts: 1300, mult: 1.034) |
