# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T02:55:04Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 583.2s  
**Total Spells Tuned:** 102 / 125  

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
| **Poison** | 16,568 | 54.9% | 55.0% | 10.7 | Overtuned ⚠️ |
| **Blood** | 16,789 | 53.5% | 53.5% | 25.7 | Balanced ✅ |
| **Earth** | 8,336 | 52.8% | 52.8% | 19.0 | Balanced ✅ |
| **Lightning** | 17,526 | 52.6% | 52.6% | 27.9 | Balanced ✅ |
| **Ghostfire** | 16,506 | 52.4% | 52.4% | 47.4 | Balanced ✅ |
| **Plants** | 16,527 | 51.3% | 51.3% | 7.9 | Balanced ✅ |
| **Beasts** | 16,440 | 50.8% | 50.8% | 23.9 | Balanced ✅ |
| **Dark** | 8,566 | 50.8% | 50.8% | 96.5 | Balanced ✅ |
| **Light** | 7,926 | 50.7% | 50.7% | 26.1 | Balanced ✅ |
| **Cosmic** | 16,324 | 49.5% | 49.5% | 20.6 | Balanced ✅ |
| **Fire** | 7,394 | 49.1% | 49.1% | 16.2 | Balanced ✅ |
| **Fey** | 14,733 | 47.7% | 47.7% | 4833.7 | Balanced ✅ |
| **Ice** | 17,264 | 47.3% | 47.3% | 21.9 | Balanced ✅ |
| **Wind** | 15,125 | 46.4% | 46.4% | 11.0 | Undertuned ⚠️ |
| **Water** | 9,246 | 44.7% | 44.7% | 13.6 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,384 (54.0%) | 3,386 (47.6%) | 15.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 902 (58.6%) | 3,951 (47.5%) | 3.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,858 (45.0%) | 3,436 (46.3%) | 9.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 7,519 (61.8%) | 6,394 (45.4%) | 5.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 11,609 (53.1%) | 3,559 (48.2%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,184 (52.5%) | 5,292 (48.7%) | 1.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,151 (36.5%) | 3,194 (42.9%) | 5.8% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 42.7 -> **44.6** (+4.4%) | - | 42.7 -> **44.6** | Status 'Burning' appliers undertuned (WR: 45.0%, casts: 4858); Individual spell undertuned (WR: 42.5%, Casts: 1790, mult: 1.026) |
| `FFL` | Fire | Debuff / Control | 4.6 -> **4.7** (+2.2%) | - | 4.6 -> **4.7** | Status 'Burning' appliers undertuned (WR: 45.0%, casts: 4858) |
| `FFD` | Fire | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 786.1 -> **1048.5** | 708.4 -> **839.6** | Status 'Burning' beneficiaries undertuned (WR: 46.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 733). Increasing spread: b -15.3%, n +31.4% |
| `WWF` | Water | Conditional Strike | 2.7 -> **2.5** (-7.4%) | 382.8 -> **493.0** | 1036.3 -> **1235.0** | Class Water undertuned (WR: 44.7%, factor: 1.021); Status 'Burning' beneficiaries undertuned (WR: 46.3%) |
| `WWE` | Water | Setup - Weather | 81.2 -> **91.1** (+12.2%) | - | 81.2 -> **91.1** | Class Water undertuned (WR: 44.7%, factor: 1.021); Weather 'Raining' appliers undertuned (WR: 36.5%, casts: 2151) |
| `WWL` | Water | Buff / Sustain | 73.7 -> **75.3** (+2.2%) | - | 73.7 -> **75.3** | Class Water undertuned (WR: 44.7%, factor: 1.021) |
| `WWD` | Water | Buff / Sustain | 47.0 -> **48.0** (+2.1%) | - | 47.0 -> **48.0** | Class Water undertuned (WR: 44.7%, factor: 1.021) |
| `EEF` | Earth | Conditional Strike | 32.3 -> **37.1** (+14.9%) | 59.4 -> **73.1** | 1950.9 -> **2749.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 16.7% vs 30% floor, Casts: 2029). Increasing spread: b -11.3%, n +23.1%; Buffed setup spell [EEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `EEW` | Earth | Buff / Sustain | 19.7 -> **19.1** (-3.0%) | - | 19.7 -> **19.1** | Individual spell overtuned (WR: 58.7%, Casts: 1462, mult: 0.969) |
| `LLF` | Light | Conditional Strike | 7.6 -> **6.4** (-15.8%) | 1031.6 -> **1366.5** | 7847.8 -> **8752.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.4% vs 30% floor, Casts: 2204). Increasing spread: b -15.8%, n +32.5% |
| `LLW` | Light | Debuff / Control | 142.9 -> **168.2** (+17.7%) | - | 142.9 -> **168.2** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Individual spell undertuned (WR: 43.1%, Casts: 1861, mult: 1.024) |
| `LLE` | Light | Setup - Weather | 159.7 -> **150.2** (-5.9%) | - | 159.7 -> **150.2** | Weather 'Sunny' appliers overtuned on own (WR: 58.6%); Individual spell overtuned (WR: 58.6%, Casts: 902, mult: 0.970) |
| `LLL` | Light | Buff / Sustain | 16.0 -> **15.5** (-3.1%) | - | 16.0 -> **15.5** | Individual spell overtuned (WR: 59.4%, Casts: 1307, mult: 0.966) |
| `LLD` | Light | Ultimate | 40.0 -> **43.2** (+8.0%) | 156.1 -> **146.7** | 6284.0 -> **6380.6** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1652, WR: 47.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 2165.4 -> **2966.6** | 866.6 -> **890.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2249). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 40.8%, Casts: 2249, mult: 1.033) |
| `DDW` | Dark | Debuff / Control | 147.1 -> **145.4** (-1.2%) | - | 147.1 -> **145.4** | Individual spell overtuned (WR: 53.5%, Casts: 1880, mult: 0.989) |
| `DDE` | Dark | Setup - Weather | 276.3 -> **303.6** (+9.9%) | - | 276.3 -> **303.6** | Weather 'Darkness' appliers overtuned on own (WR: 56.5%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `DDD` | Dark | Debuff / Control | 18.6 -> **18.0** (-3.2%) | - | 18.6 -> **18.0** | Individual spell overtuned (WR: 58.6%, Casts: 1429, mult: 0.970) |
| `FWF` | Ghostfire | Debuff / Control | 21.4 -> **22.1** (+3.3%) | - | 21.4 -> **22.1** | Status 'Burning' appliers undertuned (WR: 45.0%, casts: 4858); Individual spell undertuned (WR: 45.2%, Casts: 1701, mult: 1.016) |
| `FWW` | Ghostfire | Debuff / Control | 107.6 -> **119.5** (+11.1%) | - | 107.6 -> **119.5** | Status 'Cursed' appliers overtuned on own (WR: 54.5%); Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 301.8 -> **325.4** (+7.8%) | - | 301.8 -> **325.4** | Location 'Graveyard' appliers overtuned on own (WR: 59.0%); Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 237.9 -> **261.8** (+10.0%) | - | 237.9 -> **261.8** | Status 'Cursed' appliers overtuned on own (WR: 54.5%); Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 46.9 -> **46.3** (-1.3%) | 189.4 -> **247.1** | 8929.8 -> **11487.0** | Status 'Cursed' beneficiaries undertuned (WR: 44.8%); Location 'Graveyard' beneficiaries overtuned (WR: 53.8%) |
| `WFF` | Ghostfire | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 997.7 -> **1360.3** | 898.8 -> **1089.0** | Status 'Bleeding' beneficiaries undertuned (WR: 45.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.8% vs 30% floor, Casts: 1302). Increasing spread: b -16.5%, n +33.9% |
| `WFW` | Ghostfire | Debuff / Control | 21.0 -> **19.9** (-5.2%) | - | 21.0 -> **19.9** | Individual spell overtuned (WR: 64.7%, Casts: 1750, mult: 0.945) |
| `WFE` | Ghostfire | Debuff / Control | 10.1 -> **9.1** (-9.9%) | - | 10.1 -> **9.1** | Status 'Bleeding' appliers overtuned on own (WR: 61.8%); Individual spell overtuned (WR: 66.7%, Casts: 1484, mult: 0.937) |
| `WFL` | Ghostfire | Buff / Sustain | 47.8 -> **48.8** (+2.1%) | - | 47.8 -> **48.8** | Individual spell undertuned (WR: 43.9%, Casts: 2144, mult: 1.021) |
| `WFD` | Ghostfire | Conditional Strike | 1.2 -> **1.1** (-8.3%) | 572.5 -> **737.6** | 688.2 -> **812.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.8% vs 30% floor, Casts: 1848). Increasing spread: b -14.1%, n +28.8%; Individual spell undertuned (WR: 36.9%, Casts: 1848, mult: 1.048) |
| `FEF` | Beasts | Debuff / Control | 82.0 -> **80.8** (-1.5%) | - | 82.0 -> **80.8** | Individual spell overtuned (WR: 54.3%, Casts: 1375, mult: 0.986) |
| `FEW` | Beasts | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 2164.9 -> **2949.3** | 866.4 -> **885.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 1417). Increasing spread: b -17.6%, n +36.2%; Individual spell undertuned (WR: 46.1%, Casts: 1417, mult: 1.013) |
| `FEL` | Beasts | Buff / Sustain | 40.2 -> **41.6** (+3.5%) | - | 40.2 -> **41.6** | Individual spell undertuned (WR: 40.5%, Casts: 2587, mult: 1.034) |
| `EFF` | Beasts | Debuff / Control | 0.4 -> **0.3** (-25.0%) | 1902.7 -> **2586.9** | 761.5 -> **776.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 1275). Increasing spread: b -17.5%, n +36.0%; Individual spell overtuned (WR: 60.3%, Casts: 1275, mult: 0.963) |
| `EFW` | Beasts | Buff / Sustain | 21.2 -> **20.3** (-4.2%) | - | 21.2 -> **20.3** | Individual spell overtuned (WR: 62.0%, Casts: 1669, mult: 0.956) |
| `EFE` | Beasts | Buff / Sustain | 33.2 -> **33.7** (+1.5%) | - | 33.2 -> **33.7** | Individual spell undertuned (WR: 45.6%, Casts: 1652, mult: 1.015) |
| `EFL` | Beasts | Buff / Sustain | 1.3 -> **1.1** (-15.4%) | - | 1.3 -> **1.1** | Individual spell overtuned (WR: 81.0%, Casts: 967, mult: 0.876) |
| `EFD` | Beasts | Ultimate | 30.9 -> **30.4** (-1.6%) | 416.8 -> **541.1** | 12910.0 -> **16479.8** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1960). Shifted tuner focus: protected ultimate base floor at 30.9 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo.; Individual spell overtuned (WR: 54.9%, Casts: 1960, mult: 0.984) |
| `FLF` | Lightning | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 3219.7 -> **4401.6** | 2254.5 -> **2641.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 2019). Increasing spread: b -17.9%, n +36.7%; Individual spell undertuned (WR: 43.3%, Casts: 2019, mult: 1.023) |
| `FLW` | Lightning | Debuff / Control | 121.9 -> **134.0** (+9.9%) | - | 121.9 -> **134.0** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 62.1%, Casts: 2349, mult: 0.956) |
| `FLE` | Lightning | Setup - Weather | 123.2 -> **141.7** (+15.0%) | - | 123.2 -> **141.7** | Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLD` | Lightning | Ultimate | 77.7 -> **76.5** (-1.5%) | 74.2 -> **94.7** | 5843.0 -> **7321.1** | Weather 'Storming' beneficiaries overtuned (WR: 54.6%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1540). Shifted tuner focus: protected ultimate base floor at 77.7 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 1607.1 -> **2135.4** | 804.0 -> **854.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.0% vs 30% floor, Casts: 1110). Increasing spread: b -16.0%, n +32.9%; Individual spell overtuned (WR: 54.1%, Casts: 1110, mult: 0.987) |
| `LFW` | Lightning | Buff / Sustain | 25.6 -> **25.3** (-1.2%) | - | 25.6 -> **25.3** | Individual spell overtuned (WR: 53.8%, Casts: 935, mult: 0.987) |
| `LFL` | Lightning | Debuff / Control | 46.4 -> **53.4** (+15.1%) | 519.0 -> **675.7** | 24128.0 -> **36135.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 2524). Increasing spread: b -14.7%, n +30.2%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 1106.6 -> **1481.8** | 1550.6 -> **1779.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.7% vs 30% floor, Casts: 1376). Increasing spread: b -16.5%, n +33.9%; Individual spell overtuned (WR: 53.8%, Casts: 1376, mult: 0.988) |
| `FDF` | Blood | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 2170.8 -> **2974.0** | 868.7 -> **892.5** | Class Blood overtuned (WR: 53.5%, factor: 0.986); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1313). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 59.6 -> **58.8** (-1.3%) | - | 59.6 -> **58.8** | Class Blood overtuned (WR: 53.5%, factor: 0.986) |
| `FDE` | Blood | Setup - Weather | 16.9 -> **17.1** (+1.2%) | - | 16.9 -> **17.1** | Class Blood overtuned (WR: 53.5%, factor: 0.986); Individual spell undertuned (WR: 41.9%, Casts: 2324, mult: 1.028) |
| `FDL` | Blood | Debuff / Control | 5.4 -> **4.8** (-11.1%) | - | 5.4 -> **4.8** | Class Blood overtuned (WR: 53.5%, factor: 0.986); Status 'Bleeding' appliers overtuned on own (WR: 61.8%) |
| `FDD` | Blood | Ultimate | 51.3 -> **50.6** (-1.4%) | 35.5 -> **46.1** | 1872.4 -> **2383.3** | Class Blood overtuned (WR: 53.5%, factor: 0.986); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 1280). Shifted tuner focus: protected ultimate base floor at 51.3 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 856.8 -> **1142.7** | 514.7 -> **571.9** | Class Blood overtuned (WR: 53.5%, factor: 0.986); Status 'Bleeding' beneficiaries undertuned (WR: 45.4%) |
| `DFW` | Blood | Debuff / Control | 11.3 -> **9.9** (-12.4%) | - | 11.3 -> **9.9** | Class Blood overtuned (WR: 53.5%, factor: 0.986); Status 'Bleeding' appliers overtuned on own (WR: 61.8%) |
| `DFE` | Blood | Buff / Sustain | 45.6 -> **46.5** (+2.0%) | - | 45.6 -> **46.5** | Class Blood overtuned (WR: 53.5%, factor: 0.986); Individual spell undertuned (WR: 40.2%, Casts: 1464, mult: 1.035) |
| `DFL` | Blood | Buff / Sustain | 29.8 -> **29.4** (-1.3%) | - | 29.8 -> **29.4** | Class Blood overtuned (WR: 53.5%, factor: 0.986) |
| `DFD` | Blood | Conditional Strike | 334.1 -> **374.4** (+12.1%) | 0.1 -> **0.1** | 367.5 -> **411.8** | Class Blood overtuned (WR: 53.5%, factor: 0.986); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.1% vs 55% ceiling, WR: 60.7%). Compressing spread: b +18.2%, n -26.5% |
| `WEF` | Plants | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 517.1 -> **656.8** | 725.3 -> **789.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.0% vs 30% floor, Casts: 1318). Increasing spread: b -13.2%, n +27.0% |
| `WEW` | Plants | Debuff / Control | 699.6 -> **820.8** (+17.3%) | - | 699.6 -> **820.8** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 44.0%, Casts: 1446, mult: 1.020) |
| `WED` | Plants | Conditional Strike | 12.6 -> **14.0** (+11.1%) | 30.0 -> **28.2** | 390.6 -> **408.8** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 1200, WR: 41.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 41.5%, Casts: 1200, mult: 1.030) |
| `EWF` | Plants | Buff / Sustain | 1.1 -> **0.9** (-18.2%) | 369.3 -> **486.9** | 407.3 -> **439.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 2299). Increasing spread: b -15.5%, n +31.9% |
| `EWW` | Plants | Debuff / Control | 2.0 -> **1.7** (-15.0%) | - | 2.0 -> **1.7** | Individual spell overtuned (WR: 81.6%, Casts: 1640, mult: 0.873) |
| `EWD` | Plants | Conditional Strike | 3.2 -> **2.6** (-18.8%) | 1693.2 -> **2290.2** | 5421.4 -> **5957.1** | Status 'Bleeding' appliers overtuned on own (WR: 61.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.1% vs 30% floor, Casts: 1915). Increasing spread: b -17.2%, n +35.3% |
| `WLF` | Fey | Conditional Strike | 1.3 -> **1.2** (-7.7%) | 1185.3 -> **1545.0** | 1542.2 -> **1855.2** | Status 'Cursed' beneficiaries undertuned (WR: 44.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.2% vs 30% floor, Casts: 1381). Increasing spread: b -13.5%, n +27.7% |
| `WLW` | Fey | Debuff / Control | 60.6 -> **59.6** (-1.7%) | - | 60.6 -> **59.6** | Status 'Cursed' appliers overtuned on own (WR: 54.5%) |
| `WLE` | Fey | Setup - Location | 336.9 -> **372.7** (+10.6%) | - | 336.9 -> **372.7** | Location 'Enchanted Forest' appliers overtuned on own (WR: 55.6%); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 57.9 -> **56.8** (-1.9%) | - | 57.9 -> **56.8** | Individual spell overtuned (WR: 55.6%, Casts: 1431, mult: 0.981) |
| `WLD` | Fey | Ultimate | 22.8 -> **22.0** (-3.5%) | 905.7 -> **1177.4** | 20672.8 -> **25924.8** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1558). Shifted tuner focus: protected ultimate base floor at 22.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo.; Individual spell overtuned (WR: 59.3%, Casts: 1558, mult: 0.967) |
| `LWF` | Fey | Debuff / Control | 28.4 -> **25.9** (-8.8%) | 256.0 -> **316.9** | 7298.8 -> **8233.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.9% vs 30% floor, Casts: 1993). Increasing spread: b -11.7%, n +23.8%; Individual spell undertuned (WR: 40.8%, Casts: 1993, mult: 1.032) |
| `LWD` | Fey | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 2170.8 -> **2974.0** | 1520.3 -> **1785.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 939). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 39.8%, Casts: 939, mult: 1.037) |
| `WDF` | Ice | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 2087.7 -> **2851.6** | 2924.2 -> **3423.1** | Weather 'Raining' beneficiaries undertuned (WR: 42.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.0% vs 30% floor, Casts: 2282). Increasing spread: b -16.0%, n +32.8% |
| `WDW` | Ice | Buff / Sustain | 11.1 -> **10.5** (-5.4%) | - | 11.1 -> **10.5** | Status 'Frosty' appliers overtuned on own (WR: 54.0%); Individual spell overtuned (WR: 62.1%, Casts: 2497, mult: 0.956) |
| `WDE` | Ice | Setup - Weather | 33.0 -> **34.8** (+5.5%) | - | 33.0 -> **34.8** | Individual spell undertuned (WR: 35.7%, Casts: 2713, mult: 1.053) |
| `WDL` | Ice | Debuff / Control | 39.5 -> **39.0** (-1.3%) | - | 39.5 -> **39.0** | Status 'Frosty' appliers overtuned on own (WR: 54.0%) |
| `WDD` | Ice | Ultimate | 34.0 -> **32.7** (-3.8%) | 202.4 -> **238.6** | 6915.6 -> **7834.9** | Weather 'Blizzard' beneficiaries overtuned (WR: 60.7%); Location 'Tundra' beneficiaries overtuned (WR: 60.7%) |
| `DWW` | Ice | Debuff / Control | 101.6 -> **103.9** (+2.3%) | - | 101.6 -> **103.9** | Individual spell undertuned (WR: 43.4%, Casts: 1149, mult: 1.023) |
| `DWE` | Ice | Setup - Location | 38.6 -> **40.4** (+4.7%) | - | 38.6 -> **40.4** | Location 'Tundra' appliers undertuned (WR: 43.4%, casts: 2096); Individual spell undertuned (WR: 43.4%, Casts: 2096, mult: 1.023) |
| `DWL` | Ice | Debuff / Control | 40.2 -> **39.6** (-1.5%) | - | 40.2 -> **39.6** | Status 'Frosty' appliers overtuned on own (WR: 54.0%) |
| `DWD` | Ice | Conditional Strike | 4.1 -> **3.7** (-9.8%) | 156.1 -> **196.1** | 644.1 -> **729.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.6% vs 30% floor, Casts: 1357). Increasing spread: b -12.5%, n +25.6%; Individual spell undertuned (WR: 43.9%, Casts: 1357, mult: 1.021) |
| `ELF` | Wind | Conditional Strike | 2.6 -> **2.4** (-7.7%) | 918.1 -> **1220.3** | 2389.7 -> **2931.1** | Class Wind undertuned (WR: 46.4%, factor: 1.014); Status 'Bleeding' beneficiaries undertuned (WR: 45.4%) |
| `ELW` | Wind | Debuff / Control | 114.0 -> **111.0** (-2.6%) | - | 114.0 -> **111.0** | Class Wind undertuned (WR: 46.4%, factor: 1.014); Individual spell overtuned (WR: 61.0%, Casts: 1717, mult: 0.960) |
| `ELE` | Wind | Setup - Weather | 26.7 -> **27.7** (+3.7%) | - | 26.7 -> **27.7** | Class Wind undertuned (WR: 46.4%, factor: 1.014); Individual spell undertuned (WR: 43.7%, Casts: 1149, mult: 1.022) |
| `ELL` | Wind | Buff / Sustain | 41.7 -> **43.9** (+5.3%) | - | 41.7 -> **43.9** | Class Wind undertuned (WR: 46.4%, factor: 1.014); Individual spell undertuned (WR: 39.6%, Casts: 1796, mult: 1.037) |
| `ELD` | Wind | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 1681.3 -> **2257.9** | 2691.7 -> **3162.5** | Class Wind undertuned (WR: 46.4%, factor: 1.014); Weather 'Raining' beneficiaries undertuned (WR: 42.9%) |
| `LEF` | Wind | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 909.3 -> **1202.6** | 819.3 -> **962.9** | Class Wind undertuned (WR: 46.4%, factor: 1.014); Status 'Burning' beneficiaries undertuned (WR: 46.3%) |
| `LEW` | Wind | Debuff / Control | 54.4 -> **55.2** (+1.5%) | - | 54.4 -> **55.2** | Class Wind undertuned (WR: 46.4%, factor: 1.014) |
| `LEE` | Wind | Setup - Weather | 24.4 -> **25.6** (+4.9%) | - | 24.4 -> **25.6** | Class Wind undertuned (WR: 46.4%, factor: 1.014); Individual spell undertuned (WR: 40.8%, Casts: 1951, mult: 1.033) |
| `LEL` | Wind | Buff / Sustain | 116.8 -> **118.5** (+1.5%) | - | 116.8 -> **118.5** | Class Wind undertuned (WR: 46.4%, factor: 1.014) |
| `EDF` | Poison | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 806.9 -> **1050.7** | 484.7 -> **525.9** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 2199). Increasing spread: b -14.7%, n +30.2% |
| `EDW` | Poison | Debuff / Control | 10.3 -> **9.9** (-3.9%) | - | 10.3 -> **9.9** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 55.9%, Casts: 1585, mult: 0.980) |
| `EDE` | Poison | Setup - Location | 53.0 -> **52.0** (-1.9%) | - | 53.0 -> **52.0** | Class Poison overtuned (WR: 54.9%, factor: 0.980) |
| `EDD` | Poison | Ultimate | 48.8 -> **51.7** (+5.9%) | 33.3 -> **31.9** | 1673.8 -> **1700.9** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Status 'Bleeding' beneficiaries undertuned (WR: 45.4%) |
| `DEF` | Poison | Conditional Strike | 30.5 -> **29.9** (-2.0%) | 1.4 -> **1.4** | 73.2 -> **71.8** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 50.3% within [30%-55%] target window, WR: 46.5%). |
| `DEW` | Poison | Debuff / Control | 12.6 -> **12.4** (-1.6%) | - | 12.6 -> **12.4** | Class Poison overtuned (WR: 54.9%, factor: 0.980) |
| `DEE` | Poison | Debuff / Control | 41.9 -> **39.4** (-6.0%) | - | 41.9 -> **39.4** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell overtuned (WR: 61.0%, Casts: 1195, mult: 0.960) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 921.4 -> **1222.1** | 184.5 -> **244.6** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Status 'Bleeding' beneficiaries undertuned (WR: 45.4%) |
| `DED` | Poison | Debuff / Control | 22.4 -> **22.5** (+0.4%) | - | 22.4 -> **22.5** | Class Poison overtuned (WR: 54.9%, factor: 0.980); Individual spell undertuned (WR: 43.0%, Casts: 1507, mult: 1.024) |
| `LDF` | Cosmic | Debuff / Control | 134.6 -> **133.0** (-1.2%) | - | 134.6 -> **133.0** | Individual spell overtuned (WR: 53.6%, Casts: 1330, mult: 0.988) |
| `LDW` | Cosmic | Debuff / Control | 44.6 -> **43.5** (-2.5%) | - | 44.6 -> **43.5** | Individual spell overtuned (WR: 57.4%, Casts: 2319, mult: 0.974) |
| `LDL` | Cosmic | Conditional Strike | 1.0 -> **0.8** (-20.0%) | 1222.5 -> **1654.2** | 1223.5 -> **1324.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.0% vs 30% floor, Casts: 1337). Increasing spread: b -17.2%, n +35.3% |
| `LDD` | Cosmic | Ultimate | 81.7 -> **89.4** (+9.4%) | 26.5 -> **24.9** | 2246.8 -> **2315.5** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2400, WR: 46.1%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 46.1%, Casts: 2400, mult: 1.013) |
| `DLF` | Cosmic | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 952.1 -> **1268.4** | 857.8 -> **1015.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.5% vs 30% floor, Casts: 1783). Increasing spread: b -16.2%, n +33.2% |
| `DLW` | Cosmic | Direct Damage | 56.6 -> **55.4** (-2.1%) | - | 56.6 -> **55.4** | Individual spell overtuned (WR: 56.3%, Casts: 1091, mult: 0.978) |
| `DLE` | Cosmic | Direct Damage | 52.5 -> **53.9** (+2.7%) | - | 52.5 -> **53.9** | Individual spell undertuned (WR: 42.2%, Casts: 1341, mult: 1.027) |
| `DLL` | Cosmic | Conditional Strike | 3.2 -> **2.9** (-9.4%) | 411.6 -> **535.1** | 1320.3 -> **1554.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.4% vs 30% floor, Casts: 1872). Increasing spread: b -14.6%, n +30.0%; Individual spell undertuned (WR: 36.0%, Casts: 1872, mult: 1.052) |
