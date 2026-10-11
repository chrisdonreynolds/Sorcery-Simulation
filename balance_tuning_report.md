# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T02:35:59Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 337.1s  
**Total Spells Tuned:** 98 / 125  

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
| **Blood** | 17,909 | 54.9% | 54.9% | 25.7 | Overtuned ⚠️ |
| **Poison** | 18,336 | 54.8% | 54.8% | 12.2 | Overtuned ⚠️ |
| **Earth** | 8,592 | 53.0% | 53.0% | 17.9 | Balanced ✅ |
| **Lightning** | 17,174 | 52.6% | 52.6% | 23.6 | Balanced ✅ |
| **Light** | 8,496 | 51.6% | 51.6% | 26.1 | Balanced ✅ |
| **Dark** | 8,520 | 51.3% | 51.3% | 56.8 | Balanced ✅ |
| **Ghostfire** | 18,263 | 51.1% | 51.1% | 46.7 | Balanced ✅ |
| **Plants** | 18,096 | 49.9% | 49.9% | 7.8 | Balanced ✅ |
| **Fire** | 8,196 | 49.9% | 49.9% | 17.0 | Balanced ✅ |
| **Beasts** | 17,154 | 49.6% | 49.6% | 20.7 | Balanced ✅ |
| **Ice** | 16,107 | 49.0% | 49.0% | 23.8 | Balanced ✅ |
| **Cosmic** | 18,513 | 47.6% | 47.6% | 18.3 | Balanced ✅ |
| **Fey** | 15,203 | 47.6% | 47.6% | 1970.6 | Balanced ✅ |
| **Water** | 9,198 | 46.4% | 46.4% | 12.8 | Undertuned ⚠️ |
| **Wind** | 17,304 | 46.1% | 46.1% | 11.1 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,090 (55.0%) | 4,178 (45.7%) | 17.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,286 (56.5%) | 3,982 (46.9%) | 4.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 5,497 (46.5%) | 4,066 (44.5%) | 10.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,283 (62.9%) | 7,456 (48.5%) | 3.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 11,672 (53.1%) | 3,822 (46.0%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,194 (51.8%) | 5,938 (47.4%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,138 (35.5%) | 3,216 (41.8%) | 6.1% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 59.6 -> **58.5** (-1.8%) | - | 59.6 -> **58.5** | Individual spell overtuned (WR: 55.5%, Casts: 1488, mult: 0.981) |
| `FFW` | Fire | Debuff / Control | 41.4 -> **42.7** (+3.1%) | - | 41.4 -> **42.7** | Individual spell undertuned (WR: 40.9%, Casts: 1928, mult: 1.032) |
| `FFE` | Fire | Debuff / Control | 33.2 -> **32.8** (-1.2%) | - | 33.2 -> **32.8** | Individual spell overtuned (WR: 53.6%, Casts: 2264, mult: 0.988) |
| `FFD` | Fire | Conditional Strike | 1.1 -> **0.9** (-18.2%) | 591.1 -> **786.1** | 651.3 -> **708.4** | Status 'Burning' beneficiaries undertuned (WR: 44.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.3% vs 30% floor, Casts: 919). Increasing spread: b -14.7%, n +30.1% |
| `WWF` | Water | Conditional Strike | 3.0 -> **2.7** (-10.0%) | 294.4 -> **382.8** | 886.2 -> **1036.3** | Class Water undertuned (WR: 46.4%, factor: 1.014); Status 'Burning' beneficiaries undertuned (WR: 44.5%) |
| `WWE` | Water | Setup - Weather | 72.3 -> **81.2** (+12.3%) | - | 72.3 -> **81.2** | Class Water undertuned (WR: 46.4%, factor: 1.014); Weather 'Raining' appliers undertuned (WR: 35.5%, casts: 2138) |
| `WWL` | Water | Buff / Sustain | 72.7 -> **73.7** (+1.4%) | - | 72.7 -> **73.7** | Class Water undertuned (WR: 46.4%, factor: 1.014) |
| `WWD` | Water | Buff / Sustain | 47.4 -> **47.0** (-0.8%) | - | 47.4 -> **47.0** | Class Water undertuned (WR: 46.4%, factor: 1.014); Individual spell overtuned (WR: 56.6%, Casts: 1389, mult: 0.977) |
| `EEF` | Earth | Conditional Strike | 28.1 -> **32.3** (+14.9%) | 48.2 -> **59.4** | 1382.5 -> **1950.9** | Status 'Frosty' beneficiaries undertuned (WR: 45.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 19.1% vs 30% floor, Casts: 2257). Increasing spread: b -10.3%, n +21.1% |
| `LLF` | Light | Conditional Strike | 6.6 -> **7.6** (+15.2%) | 777.6 -> **1031.6** | 5138.8 -> **7847.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.2% vs 30% floor, Casts: 2212). Increasing spread: b -15.9%, n +32.7%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 140.1 -> **142.9** (+2.0%) | - | 140.1 -> **142.9** | Individual spell undertuned (WR: 44.1%, Casts: 1944, mult: 1.020) |
| `LLE` | Light | Setup - Weather | 145.3 -> **159.7** (+9.9%) | - | 145.3 -> **159.7** | Weather 'Sunny' appliers overtuned on own (WR: 56.5%); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 16.7 -> **16.0** (-4.2%) | - | 16.7 -> **16.0** | Individual spell overtuned (WR: 61.7%, Casts: 1282, mult: 0.958) |
| `LLD` | Light | Ultimate | 40.0 -> **40.0** (+0.0%) | 120.1 -> **156.1** | 4844.0 -> **6284.0** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1772). Shifted tuner focus: protected ultimate base floor at 40.0 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 1580.6 -> **2165.4** | 790.8 -> **866.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2103). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 46.0%, Casts: 2103, mult: 1.013) |
| `DDE` | Dark | Setup - Weather | 240.3 -> **276.3** (+15.0%) | - | 240.3 -> **276.3** | Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 65.2 -> **63.7** (-2.3%) | - | 65.2 -> **63.7** | Individual spell overtuned (WR: 56.7%, Casts: 1620, mult: 0.977) |
| `DDD` | Dark | Debuff / Control | 18.9 -> **18.6** (-1.6%) | - | 18.9 -> **18.6** | Individual spell overtuned (WR: 55.1%, Casts: 1450, mult: 0.983) |
| `FWW` | Ghostfire | Debuff / Control | 93.6 -> **107.6** (+15.0%) | - | 93.6 -> **107.6** | Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 262.4 -> **301.8** (+15.0%) | - | 262.4 -> **301.8** | Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 210.4 -> **237.9** (+13.1%) | - | 210.4 -> **237.9** | Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD]; Individual spell overtuned (WR: 55.0%, Casts: 2311, mult: 0.983) |
| `FWD` | Ghostfire | Ultimate | 46.9 -> **46.9** (+0.0%) | 144.2 -> **189.4** | 6809.9 -> **8929.8** | Status 'Cursed' beneficiaries undertuned (WR: 45.6%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.4% vs 8% floor, Casts: 1333). Shifted tuner focus: protected ultimate base floor at 46.9 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 738.6 -> **997.7** | 739.6 -> **898.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.3% vs 30% floor, Casts: 1730). Increasing spread: b -17.1%, n +35.1%; Individual spell undertuned (WR: 40.8%, Casts: 1730, mult: 1.033) |
| `WFW` | Ghostfire | Debuff / Control | 22.1 -> **21.0** (-5.0%) | - | 22.1 -> **21.0** | Individual spell overtuned (WR: 63.6%, Casts: 1830, mult: 0.950) |
| `WFE` | Ghostfire | Debuff / Control | 9.9 -> **10.1** (+2.0%) | - | 9.9 -> **10.1** | Status 'Bleeding' appliers overtuned on own (WR: 62.9%); Buffed setup spell [WFE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `WFL` | Ghostfire | Buff / Sustain | 46.5 -> **47.8** (+2.8%) | - | 46.5 -> **47.8** | Individual spell undertuned (WR: 41.8%, Casts: 2217, mult: 1.029) |
| `WFD` | Ghostfire | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 444.7 -> **572.5** | 624.0 -> **688.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.9% vs 30% floor, Casts: 1433). Increasing spread: b -14.0%, n +28.7%; Individual spell undertuned (WR: 39.9%, Casts: 1433, mult: 1.036) |
| `FEW` | Beasts | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 1598.2 -> **2164.9** | 799.6 -> **866.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 1626). Increasing spread: b -17.3%, n +35.5% |
| `FEE` | Beasts | Buff / Sustain | 35.5 -> **36.1** (+1.7%) | - | 35.5 -> **36.1** | Individual spell undertuned (WR: 44.7%, Casts: 1826, mult: 1.018) |
| `FEL` | Beasts | Buff / Sustain | 38.3 -> **40.2** (+5.0%) | - | 38.3 -> **40.2** | Individual spell undertuned (WR: 36.7%, Casts: 2647, mult: 1.049) |
| `EFF` | Beasts | Debuff / Control | 0.5 -> **0.4** (-20.0%) | 1395.2 -> **1902.7** | 698.1 -> **761.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 1461). Increasing spread: b -17.7%, n +36.4%; Individual spell overtuned (WR: 60.0%, Casts: 1461, mult: 0.964) |
| `EFW` | Beasts | Buff / Sustain | 21.8 -> **21.2** (-2.8%) | - | 21.8 -> **21.2** | Individual spell overtuned (WR: 57.4%, Casts: 1877, mult: 0.974) |
| `EFL` | Beasts | Buff / Sustain | 1.5 -> **1.3** (-13.3%) | - | 1.5 -> **1.3** | Individual spell overtuned (WR: 84.2%, Casts: 977, mult: 0.862) |
| `EFD` | Beasts | Ultimate | 31.3 -> **30.9** (-1.3%) | 321.1 -> **416.8** | 10081.7 -> **12910.0** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 2040). Shifted tuner focus: protected ultimate base floor at 31.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo.; Individual spell overtuned (WR: 53.7%, Casts: 2040, mult: 0.988) |
| `FLF` | Lightning | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 2316.3 -> **3219.7** | 1853.8 -> **2254.5** | Status 'Stunned' beneficiaries undertuned (WR: 46.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 2260). Increasing spread: b -17.9%, n +36.8% |
| `FLW` | Lightning | Debuff / Control | 110.6 -> **121.9** (+10.2%) | - | 110.6 -> **121.9** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 61.5%, Casts: 2170, mult: 0.958) |
| `FLE` | Lightning | Setup - Weather | 107.1 -> **123.2** (+15.0%) | - | 107.1 -> **123.2** | Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLL` | Lightning | Buff / Sustain | 34.0 -> **34.9** (+2.6%) | - | 34.0 -> **34.9** | Individual spell undertuned (WR: 42.6%, Casts: 1638, mult: 1.026) |
| `FLD` | Lightning | Ultimate | 77.7 -> **77.7** (+0.0%) | 56.2 -> **74.2** | 4444.4 -> **5843.0** | Status 'Stunned' beneficiaries undertuned (WR: 46.0%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1562). Shifted tuner focus: protected ultimate base floor at 77.7 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 1193.8 -> **1607.1** | 716.9 -> **804.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.9% vs 30% floor, Casts: 943). Increasing spread: b -16.9%, n +34.6%; Individual spell overtuned (WR: 53.9%, Casts: 943, mult: 0.987) |
| `LFE` | Lightning | Debuff / Control | 54.8 -> **54.0** (-1.5%) | - | 54.8 -> **54.0** | Individual spell overtuned (WR: 54.7%, Casts: 1462, mult: 0.984) |
| `LFL` | Lightning | Debuff / Control | 56.9 -> **46.4** (-18.5%) | 398.3 -> **519.0** | 22720.2 -> **24128.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.0% vs 30% floor, Casts: 2229). Increasing spread: b -14.8%, n +30.3%; Individual spell overtuned (WR: 61.7%, Casts: 2229, mult: 0.958) |
| `LFD` | Lightning | Conditional Strike | 1.7 -> **1.4** (-17.6%) | 823.8 -> **1106.6** | 1402.2 -> **1550.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.2% vs 30% floor, Casts: 1374). Increasing spread: b -16.7%, n +34.3%; Individual spell overtuned (WR: 54.5%, Casts: 1374, mult: 0.985) |
| `FDF` | Blood | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 1584.5 -> **2170.8** | 792.8 -> **868.7** | Class Blood overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1770). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 60.8 -> **59.6** (-2.0%) | - | 60.8 -> **59.6** | Class Blood overtuned (WR: 54.9%, factor: 0.980) |
| `FDD` | Blood | Ultimate | 48.5 -> **51.3** (+5.8%) | 37.8 -> **35.5** | 1881.8 -> **1872.4** | Class Blood overtuned (WR: 54.9%, factor: 0.980); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1194, WR: 47.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 647.6 -> **856.8** | 454.0 -> **514.7** | Class Blood overtuned (WR: 54.9%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.6% vs 30% floor, Casts: 1896). Increasing spread: b -15.7%, n +32.3% |
| `DFW` | Blood | Debuff / Control | 11.7 -> **11.3** (-3.4%) | - | 11.7 -> **11.3** | Class Blood overtuned (WR: 54.9%, factor: 0.980); Status 'Bleeding' appliers overtuned on own (WR: 62.9%) |
| `DFE` | Blood | Buff / Sustain | 46.5 -> **45.6** (-1.9%) | - | 46.5 -> **45.6** | Class Blood overtuned (WR: 54.9%, factor: 0.980) |
| `DFL` | Blood | Buff / Sustain | 29.4 -> **29.8** (+1.4%) | - | 29.4 -> **29.8** | Class Blood overtuned (WR: 54.9%, factor: 0.980); Individual spell undertuned (WR: 40.2%, Casts: 1149, mult: 1.035) |
| `DFD` | Blood | Conditional Strike | 300.3 -> **334.1** (+11.3%) | 0.1 -> **0.1** | 330.3 -> **367.5** | Class Blood overtuned (WR: 54.9%, factor: 0.980); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.8% vs 55% ceiling, WR: 63.7%). Compressing spread: b +19.6%, n -28.0% |
| `WEF` | Plants | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 405.1 -> **517.1** | 649.8 -> **725.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.2% vs 30% floor, Casts: 1718). Increasing spread: b -13.5%, n +27.6% |
| `WEW` | Plants | Debuff / Control | 575.1 -> **699.6** (+21.6%) | - | 575.1 -> **699.6** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 34.5%, Casts: 1782, mult: 1.058) |
| `WED` | Plants | Conditional Strike | 11.4 -> **12.6** (+10.5%) | 31.9 -> **30.0** | 375.1 -> **390.6** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1374, WR: 43.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 43.2%, Casts: 1374, mult: 1.023) |
| `EWF` | Plants | Buff / Sustain | 1.3 -> **1.1** (-15.4%) | 283.7 -> **369.3** | 370.1 -> **407.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 2210). Increasing spread: b -14.7%, n +30.2%; Individual spell undertuned (WR: 45.5%, Casts: 2210, mult: 1.015) |
| `EWW` | Plants | Debuff / Control | 2.3 -> **2.0** (-13.0%) | - | 2.3 -> **2.0** | Individual spell overtuned (WR: 84.1%, Casts: 1589, mult: 0.862) |
| `EWD` | Plants | Conditional Strike | 2.8 -> **3.2** (+14.3%) | 1249.0 -> **1693.2** | 3500.0 -> **5421.4** | Status 'Bleeding' appliers overtuned on own (WR: 62.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.7% vs 30% floor, Casts: 2272). Increasing spread: b -17.3%, n +35.6% |
| `WLF` | Fey | Conditional Strike | 1.4 -> **1.3** (-7.1%) | 920.4 -> **1185.3** | 1290.0 -> **1542.2** | Status 'Cursed' beneficiaries undertuned (WR: 45.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.5% vs 30% floor, Casts: 1349). Increasing spread: b -13.0%, n +26.6% |
| `WLW` | Fey | Debuff / Control | 59.4 -> **60.6** (+2.0%) | - | 59.4 -> **60.6** | Individual spell undertuned (WR: 43.9%, Casts: 2143, mult: 1.021) |
| `WLE` | Fey | Setup - Location | 310.6 -> **336.9** (+8.5%) | - | 310.6 -> **336.9** | Location 'Enchanted Forest' appliers overtuned on own (WR: 58.2%); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 58.9 -> **57.9** (-1.7%) | - | 58.9 -> **57.9** | Individual spell overtuned (WR: 55.1%, Casts: 1686, mult: 0.983) |
| `WLD` | Fey | Ultimate | 23.8 -> **22.8** (-4.2%) | 696.7 -> **905.7** | 16605.3 -> **20672.8** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1404). Shifted tuner focus: protected ultimate base floor at 23.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo.; Individual spell overtuned (WR: 62.0%, Casts: 1404, mult: 0.956) |
| `LWF` | Fey | Debuff / Control | 31.7 -> **28.4** (-10.4%) | 205.9 -> **256.0** | 6558.7 -> **7298.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.2% vs 30% floor, Casts: 1862). Increasing spread: b -11.9%, n +24.3%; Individual spell undertuned (WR: 44.5%, Casts: 1862, mult: 1.019) |
| `LWW` | Fey | Debuff / Control | 48.8 -> **49.6** (+1.6%) | - | 48.8 -> **49.6** | Individual spell undertuned (WR: 45.0%, Casts: 1020, mult: 1.017) |
| `LWD` | Fey | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1584.5 -> **2170.8** | 1268.4 -> **1520.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1016). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 34.3%, Casts: 1016, mult: 1.059) |
| `WDF` | Ice | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 1528.8 -> **2087.7** | 2447.7 -> **2924.2** | Weather 'Raining' beneficiaries undertuned (WR: 41.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.8% vs 30% floor, Casts: 2000). Increasing spread: b -15.7%, n +32.2% |
| `WDW` | Ice | Buff / Sustain | 11.6 -> **11.1** (-4.3%) | - | 11.6 -> **11.1** | Status 'Frosty' appliers overtuned on own (WR: 55.0%); Individual spell overtuned (WR: 58.6%, Casts: 2735, mult: 0.970) |
| `WDE` | Ice | Setup - Weather | 32.3 -> **33.0** (+2.2%) | - | 32.3 -> **33.0** | Individual spell undertuned (WR: 43.8%, Casts: 2034, mult: 1.021) |
| `WDL` | Ice | Debuff / Control | 40.8 -> **39.5** (-3.2%) | - | 40.8 -> **39.5** | Status 'Frosty' appliers overtuned on own (WR: 55.0%); Individual spell overtuned (WR: 54.4%, Casts: 803, mult: 0.986) |
| `WDD` | Ice | Ultimate | 35.2 -> **34.0** (-3.4%) | 171.0 -> **202.4** | 6054.4 -> **6915.6** | Weather 'Blizzard' beneficiaries overtuned (WR: 59.3%); Location 'Tundra' beneficiaries overtuned (WR: 59.3%) |
| `DWF` | Ice | Debuff / Control | 38.4 -> **37.7** (-1.8%) | - | 38.4 -> **37.7** | Status 'Frosty' appliers overtuned on own (WR: 55.0%) |
| `DWE` | Ice | Setup - Location | 37.0 -> **38.6** (+4.3%) | - | 37.0 -> **38.6** | Location 'Tundra' appliers undertuned (WR: 43.9%, casts: 1424); Individual spell undertuned (WR: 43.9%, Casts: 1424, mult: 1.021) |
| `DWL` | Ice | Debuff / Control | 40.9 -> **40.2** (-1.7%) | - | 40.9 -> **40.2** | Status 'Frosty' appliers overtuned on own (WR: 55.0%) |
| `DWD` | Ice | Conditional Strike | 4.5 -> **4.1** (-8.9%) | 122.9 -> **156.1** | 557.6 -> **644.1** | Status 'Frosty' beneficiaries undertuned (WR: 45.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.6% vs 30% floor, Casts: 1921). Increasing spread: b -12.2%, n +24.8% |
| `ELF` | Wind | Conditional Strike | 2.9 -> **2.6** (-10.3%) | 697.1 -> **918.1** | 2024.5 -> **2389.7** | Class Wind undertuned (WR: 46.1%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 723). Increasing spread: b -15.5%, n +31.7% |
| `ELW` | Wind | Debuff / Control | 116.3 -> **114.0** (-2.0%) | - | 116.3 -> **114.0** | Class Wind undertuned (WR: 46.1%, factor: 1.015); Individual spell overtuned (WR: 59.6%, Casts: 1653, mult: 0.966) |
| `ELE` | Wind | Setup - Weather | 25.7 -> **26.7** (+3.9%) | - | 25.7 -> **26.7** | Class Wind undertuned (WR: 46.1%, factor: 1.015); Individual spell undertuned (WR: 43.4%, Casts: 1412, mult: 1.023) |
| `ELL` | Wind | Buff / Sustain | 40.6 -> **41.7** (+2.7%) | - | 40.6 -> **41.7** | Class Wind undertuned (WR: 46.1%, factor: 1.015); Individual spell undertuned (WR: 46.3%, Casts: 1808, mult: 1.012) |
| `ELD` | Wind | Conditional Strike | 1.7 -> **1.6** (-5.9%) | 1238.3 -> **1681.3** | 2106.8 -> **2691.7** | Class Wind undertuned (WR: 46.1%, factor: 1.015); Weather 'Raining' beneficiaries undertuned (WR: 41.8%) |
| `LEF` | Wind | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 697.6 -> **909.3** | 698.6 -> **819.3** | Class Wind undertuned (WR: 46.1%, factor: 1.015); Status 'Burning' beneficiaries undertuned (WR: 44.5%) |
| `LEW` | Wind | Debuff / Control | 53.6 -> **54.4** (+1.5%) | - | 53.6 -> **54.4** | Class Wind undertuned (WR: 46.1%, factor: 1.015) |
| `LEE` | Wind | Setup - Weather | 23.4 -> **24.4** (+4.3%) | - | 23.4 -> **24.4** | Class Wind undertuned (WR: 46.1%, factor: 1.015); Individual spell undertuned (WR: 42.7%, Casts: 1881, mult: 1.025) |
| `LEL` | Wind | Buff / Sustain | 115.0 -> **116.8** (+1.6%) | - | 115.0 -> **116.8** | Class Wind undertuned (WR: 46.1%, factor: 1.015) |
| `EDF` | Poison | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 613.6 -> **806.9** | 430.2 -> **484.7** | Class Poison overtuned (WR: 54.8%, factor: 0.981); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.6% vs 30% floor, Casts: 2608). Increasing spread: b -15.4%, n +31.5% |
| `EDW` | Poison | Debuff / Control | 10.9 -> **10.3** (-5.5%) | - | 10.9 -> **10.3** | Class Poison overtuned (WR: 54.8%, factor: 0.981); Individual spell overtuned (WR: 59.7%, Casts: 1932, mult: 0.966) |
| `EDE` | Poison | Setup - Location | 48.5 -> **53.0** (+9.3%) | - | 48.5 -> **53.0** | Class Poison overtuned (WR: 54.8%, factor: 0.981); Location 'Swamp' appliers overtuned on own (WR: 54.7%) |
| `EDD` | Poison | Ultimate | 50.3 -> **48.8** (-3.0%) | 25.8 -> **33.3** | 1348.0 -> **1673.8** | Class Poison overtuned (WR: 54.8%, factor: 0.981); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.6% vs 16% floor, Casts: 2048). Shifted tuner focus: protected ultimate base floor at 50.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WFE, FDL, DFW, EWD, EDE) with +15% b tempo. |
| `DEF` | Poison | Conditional Strike | 31.1 -> **30.5** (-1.9%) | 1.4 -> **1.4** | 74.6 -> **73.2** | Class Poison overtuned (WR: 54.8%, factor: 0.981); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 52.5% within [30%-55%] target window, WR: 48.7%). |
| `DEW` | Poison | Debuff / Control | 13.1 -> **12.6** (-3.8%) | - | 13.1 -> **12.6** | Class Poison overtuned (WR: 54.8%, factor: 0.981); Individual spell overtuned (WR: 54.8%, Casts: 2024, mult: 0.984) |
| `DEE` | Poison | Debuff / Control | 44.2 -> **41.9** (-5.2%) | - | 44.2 -> **41.9** | Class Poison overtuned (WR: 54.8%, factor: 0.981); Individual spell overtuned (WR: 59.7%, Casts: 1129, mult: 0.966) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 703.7 -> **921.4** | 140.9 -> **184.5** | Class Poison overtuned (WR: 54.8%, factor: 0.981); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.3% vs 30% floor, Casts: 1059). Increasing spread: b -15.1%, n +30.9% |
| `DED` | Poison | Debuff / Control | 22.0 -> **22.4** (+1.8%) | - | 22.0 -> **22.4** | Class Poison overtuned (WR: 54.8%, factor: 0.981); Individual spell undertuned (WR: 39.2%, Casts: 1379, mult: 1.039) |
| `LDF` | Cosmic | Debuff / Control | 137.1 -> **134.6** (-1.8%) | - | 137.1 -> **134.6** | Individual spell overtuned (WR: 55.5%, Casts: 984, mult: 0.981) |
| `LDL` | Cosmic | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 908.7 -> **1222.5** | 1091.6 -> **1223.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.0% vs 30% floor, Casts: 1387). Increasing spread: b -16.8%, n +34.5%; Individual spell undertuned (WR: 46.5%, Casts: 1387, mult: 1.011) |
| `LDD` | Cosmic | Ultimate | 73.4 -> **81.7** (+11.3%) | 28.2 -> **26.5** | 2143.3 -> **2246.8** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2686, WR: 41.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 41.3%, Casts: 2686, mult: 1.031) |
| `DLF` | Cosmic | Conditional Strike | 1.1 -> **0.9** (-18.2%) | 714.9 -> **952.1** | 787.5 -> **857.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.6% vs 30% floor, Casts: 2311). Increasing spread: b -16.2%, n +33.2% |
| `DLE` | Cosmic | Direct Damage | 50.5 -> **52.5** (+4.0%) | - | 50.5 -> **52.5** | Individual spell undertuned (WR: 39.0%, Casts: 1655, mult: 1.040) |
| `DLL` | Cosmic | Conditional Strike | 3.6 -> **3.2** (-11.1%) | 313.0 -> **411.6** | 1130.4 -> **1320.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.6% vs 30% floor, Casts: 2271). Increasing spread: b -15.4%, n +31.5%; Individual spell undertuned (WR: 37.8%, Casts: 2271, mult: 1.045) |
