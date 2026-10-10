# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T07:05:51Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 70.7s  
**Total Spells Tuned:** 87 / 125  

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
| **Water** | 9,527 | 55.1% | 55.1% | 10.4 | Overtuned ⚠️ |
| **Beasts** | 19,320 | 54.3% | 54.3% | 6.0 | Overtuned ⚠️ |
| **Plants** | 20,020 | 53.1% | 53.2% | 10.1 | Balanced ✅ |
| **Poison** | 21,129 | 52.5% | 52.5% | 11.1 | Balanced ✅ |
| **Fire** | 11,122 | 51.9% | 51.9% | 18.0 | Balanced ✅ |
| **Dark** | 10,543 | 50.7% | 50.7% | 12.5 | Balanced ✅ |
| **Wind** | 19,187 | 50.4% | 50.4% | 8.5 | Balanced ✅ |
| **Ghostfire** | 20,711 | 50.3% | 50.3% | 12.2 | Balanced ✅ |
| **Lightning** | 21,433 | 50.2% | 50.2% | 11.0 | Balanced ✅ |
| **Light** | 10,263 | 49.7% | 49.7% | 4.1 | Balanced ✅ |
| **Blood** | 19,820 | 49.5% | 49.5% | 13.4 | Balanced ✅ |
| **Earth** | 11,299 | 48.0% | 48.0% | 13.0 | Balanced ✅ |
| **Fey** | 20,567 | 47.6% | 47.6% | 9.6 | Balanced ✅ |
| **Cosmic** | 20,967 | 46.9% | 46.9% | 14.0 | Balanced ✅ |
| **Ice** | 24,476 | 45.6% | 45.6% | 12.2 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 10,275 (45.3%) | 5,222 (46.2%) | 14.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,632 (39.2%) | 4,115 (52.5%) | 4.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,079 (54.0%) | 6,230 (52.4%) | 7.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 7,592 (57.2%) | 9,592 (49.8%) | 3.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 15,448 (45.5%) | 3,966 (49.0%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,632 (52.1%) | 5,992 (50.2%) | 0.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,776 (53.6%) | 5,151 (46.6%) | 5.3% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 60.0 -> **59.3** (-1.2%) | - | 60.0 -> **59.3** | Individual spell overtuned (WR: 53.6%, Casts: 2370, mult: 0.988) |
| `FFW` | Fire | Debuff / Control | 45.0 -> **44.4** (-1.3%) | - | 45.0 -> **44.4** | Status 'Burning' appliers overtuned on own (WR: 54.0%) |
| `FFL` | Fire | Debuff / Control | 8.0 -> **7.8** (-2.5%) | - | 8.0 -> **7.8** | Status 'Burning' appliers overtuned on own (WR: 54.0%); Individual spell overtuned (WR: 54.0%, Casts: 2028, mult: 0.987) |
| `FFD` | Fire | Conditional Strike | 22.6 -> **19.1** (-15.5%) | 2.7 -> **3.6** | 83.6 -> **87.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.5% vs 30% floor, Casts: 1934). Increasing spread: b -15.4%, n +31.6% |
| `WWF` | Water | Conditional Strike | 35.8 -> **29.3** (-18.2%) | 2.7 -> **3.5** | 132.5 -> **131.8** | Class Water overtuned (WR: 55.1%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.5% vs 30% floor, Casts: 2391). Increasing spread: b -14.2%, n +29.0% |
| `WWE` | Water | Setup - Weather | 20.0 -> **19.1** (-4.5%) | - | 20.0 -> **19.1** | Class Water overtuned (WR: 55.1%, factor: 0.980); Weather 'Raining' appliers overtuned on own (WR: 53.6%) |
| `WWL` | Water | Buff / Sustain | 60.0 -> **58.8** (-2.0%) | - | 60.0 -> **58.8** | Class Water overtuned (WR: 55.1%, factor: 0.980) |
| `WWD` | Water | Buff / Sustain | 45.0 -> **43.5** (-3.3%) | - | 45.0 -> **43.5** | Class Water overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 53.9%, Casts: 1801, mult: 0.987) |
| `EEF` | Earth | Conditional Strike | 25.0 -> **22.9** (-8.4%) | 2.8 -> **3.5** | 95.0 -> **103.0** | Status 'Frosty' beneficiaries undertuned (WR: 46.2%); Status 'Stunned' appliers undertuned (WR: 45.5%, casts: 15448) |
| `EEE` | Earth | Conditional Strike | 4.0 -> **4.6** (+15.0%) | 2.0 -> **1.6** | 12.0 -> **12.0** | Condition triggers excessively (N=1 conditions, Trigger Rate: 95.0% vs 55% ceiling, WR: 47.2%). Compressing spread: b +13.9%, n -22.2% |
| `LLF` | Light | Conditional Strike | 4.0 -> **3.3** (-17.5%) | 2.8 -> **3.8** | 15.2 -> **15.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.3% vs 30% floor, Casts: 1986). Increasing spread: b -16.7%, n +34.2% |
| `LLE` | Light | Setup - Weather | 20.0 -> **21.6** (+8.0%) | - | 20.0 -> **21.6** | Weather 'Sunny' appliers undertuned (WR: 39.2%, casts: 2632); Individual spell undertuned (WR: 39.1%, Casts: 2632, mult: 1.039) |
| `LLL` | Light | Buff / Sustain | 33.8 -> **32.7** (-3.3%) | - | 33.8 -> **32.7** | Individual spell overtuned (WR: 58.9%, Casts: 2031, mult: 0.969) |
| `LLD` | Light | Ultimate | 23.4 -> **19.2** (-17.9%) | 7.2 -> **9.9** | 191.9 -> **209.3** | Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1842). Increasing spread: b -18.0%, n +36.9% |
| `DDF` | Dark | Conditional Strike | 21.8 -> **17.9** (-17.9%) | 2.9 -> **4.0** | 85.0 -> **89.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1762). Increasing spread: b -18.0%, n +37.0% |
| `DDD` | Dark | Debuff / Control | 33.8 -> **32.8** (-3.0%) | - | 33.8 -> **32.8** | Individual spell overtuned (WR: 58.1%, Casts: 1746, mult: 0.972) |
| `FWF` | Ghostfire | Debuff / Control | 44.2 -> **42.9** (-2.9%) | - | 44.2 -> **42.9** | Status 'Burning' appliers overtuned on own (WR: 54.0%); Individual spell overtuned (WR: 54.7%, Casts: 2208, mult: 0.984) |
| `FWD` | Ghostfire | Ultimate | 23.4 -> **19.2** (-17.9%) | 7.2 -> **9.9** | 191.9 -> **209.3** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 2194). Increasing spread: b -17.9%, n +36.8% |
| `WFF` | Ghostfire | Conditional Strike | 22.2 -> **18.6** (-16.2%) | 2.8 -> **3.7** | 84.4 -> **87.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.1% vs 30% floor, Casts: 1585). Increasing spread: b -16.4%, n +33.6% |
| `WFE` | Ghostfire | Debuff / Control | 42.7 -> **40.2** (-5.9%) | - | 42.7 -> **40.2** | Status 'Bleeding' appliers overtuned on own (WR: 57.2%); Individual spell overtuned (WR: 59.9%, Casts: 1874, mult: 0.965) |
| `WFL` | Ghostfire | Buff / Sustain | 35.0 -> **36.6** (+4.6%) | - | 35.0 -> **36.6** | Individual spell undertuned (WR: 37.5%, Casts: 2860, mult: 1.046) |
| `WFD` | Ghostfire | Conditional Strike | 22.7 -> **19.0** (-16.3%) | 2.8 -> **3.7** | 86.3 -> **89.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.5% vs 30% floor, Casts: 2199). Increasing spread: b -15.0%, n +30.8%; Individual spell overtuned (WR: 54.0%, Casts: 2199, mult: 0.987) |
| `FEF` | Beasts | Debuff / Control | 25.0 -> **24.6** (-1.6%) | - | 25.0 -> **24.6** | Class Beasts overtuned (WR: 54.3%, factor: 0.983) |
| `FEW` | Beasts | Conditional Strike | 22.1 -> **17.9** (-19.0%) | 2.9 -> **4.0** | 86.2 -> **89.5** | Class Beasts overtuned (WR: 54.3%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 2275). Increasing spread: b -17.8%, n +36.5% |
| `FEE` | Beasts | Buff / Sustain | 25.0 -> **24.6** (-1.6%) | - | 25.0 -> **24.6** | Class Beasts overtuned (WR: 54.3%, factor: 0.983) |
| `FEL` | Beasts | Buff / Sustain | 25.0 -> **24.6** (-1.6%) | - | 25.0 -> **24.6** | Class Beasts overtuned (WR: 54.3%, factor: 0.983) |
| `EFF` | Beasts | Debuff / Control | 27.5 -> **22.3** (-18.9%) | 2.9 -> **3.9** | 107.2 -> **109.3** | Class Beasts overtuned (WR: 54.3%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.3% vs 30% floor, Casts: 1937). Increasing spread: b -17.5%, n +35.9% |
| `EFW` | Beasts | Buff / Sustain | 24.5 -> **24.1** (-1.6%) | - | 24.5 -> **24.1** | Class Beasts overtuned (WR: 54.3%, factor: 0.983) |
| `EFE` | Beasts | Buff / Sustain | 35.0 -> **34.4** (-1.7%) | - | 35.0 -> **34.4** | Class Beasts overtuned (WR: 54.3%, factor: 0.983) |
| `EFL` | Beasts | Buff / Sustain | 30.4 -> **25.8** (-15.1%) | - | 30.4 -> **25.8** | Class Beasts overtuned (WR: 54.3%, factor: 0.983); Individual spell overtuned (WR: 83.9%, Casts: 2151, mult: 0.863) |
| `EFD` | Beasts | Ultimate | 23.4 -> **18.9** (-19.2%) | 7.2 -> **9.9** | 191.9 -> **206.0** | Class Beasts overtuned (WR: 54.3%, factor: 0.983); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1991). Increasing spread: b -17.9%, n +36.8% |
| `FLF` | Lightning | Conditional Strike | 21.9 -> **18.0** (-17.8%) | 2.9 -> **4.0** | 85.4 -> **90.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1895). Increasing spread: b -17.9%, n +36.8% |
| `FLW` | Lightning | Debuff / Control | 45.6 -> **46.3** (+1.5%) | - | 45.6 -> **46.3** | Status 'Stunned' appliers undertuned (WR: 45.5%, casts: 15448) |
| `FLD` | Lightning | Ultimate | 23.7 -> **25.6** (+8.0%) | 7.4 -> **7.0** | 199.1 -> **204.8** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 2071, WR: 46.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `LFF` | Lightning | Conditional Strike | 22.0 -> **18.2** (-17.3%) | 2.9 -> **3.9** | 85.8 -> **89.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1723). Increasing spread: b -17.2%, n +35.4% |
| `LFW` | Lightning | Buff / Sustain | 34.4 -> **33.5** (-2.6%) | - | 34.4 -> **33.5** | Individual spell overtuned (WR: 57.8%, Casts: 2735, mult: 0.973) |
| `LFE` | Lightning | Debuff / Control | 45.6 -> **47.2** (+3.5%) | - | 45.6 -> **47.2** | Status 'Stunned' appliers undertuned (WR: 45.5%, casts: 15448); Individual spell undertuned (WR: 44.4%, Casts: 3294, mult: 1.019) |
| `LFL` | Lightning | Debuff / Control | 36.6 -> **31.8** (-13.1%) | 2.8 -> **3.6** | 139.1 -> **146.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.2% vs 30% floor, Casts: 2311). Increasing spread: b -13.1%, n +26.9% |
| `LFD` | Lightning | Conditional Strike | 23.1 -> **19.8** (-14.3%) | 4.3 -> **5.7** | 122.4 -> **132.7** | Status 'Stunned' appliers undertuned (WR: 45.5%, casts: 15448); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.9% vs 30% floor, Casts: 1418). Increasing spread: b -15.6%, n +32.1% |
| `FDF` | Blood | Conditional Strike | 21.8 -> **17.9** (-17.9%) | 2.9 -> **4.0** | 85.0 -> **89.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1498). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 61.0 -> **62.2** (+2.0%) | - | 61.0 -> **62.2** | Individual spell undertuned (WR: 44.3%, Casts: 2035, mult: 1.019) |
| `FDL` | Blood | Debuff / Control | 41.4 -> **38.7** (-6.5%) | - | 41.4 -> **38.7** | Status 'Bleeding' appliers overtuned on own (WR: 57.2%); Individual spell overtuned (WR: 61.5%, Casts: 1839, mult: 0.958) |
| `FDD` | Blood | Ultimate | 23.5 -> **25.4** (+8.1%) | 7.2 -> **6.8** | 192.7 -> **198.1** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 2178, WR: 46.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 22.4 -> **18.7** (-16.5%) | 2.8 -> **3.7** | 85.1 -> **87.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.8% vs 30% floor, Casts: 1757). Increasing spread: b -16.5%, n +33.9% |
| `DFW` | Blood | Debuff / Control | 32.4 -> **30.4** (-6.2%) | - | 32.4 -> **30.4** | Status 'Bleeding' appliers overtuned on own (WR: 57.2%); Individual spell overtuned (WR: 60.5%, Casts: 2153, mult: 0.962) |
| `DFE` | Blood | Buff / Sustain | 35.5 -> **37.1** (+4.5%) | - | 35.5 -> **37.1** | Individual spell undertuned (WR: 37.7%, Casts: 2409, mult: 1.045) |
| `DFD` | Blood | Conditional Strike | 28.6 -> **32.6** (+14.0%) | 1.8 -> **1.4** | 80.1 -> **78.2** | Condition triggers excessively (N=1 conditions, Trigger Rate: 95.6% vs 55% ceiling, WR: 50.2%). Compressing spread: b +14.0%, n -22.4% |
| `WEF` | Plants | Conditional Strike | 23.1 -> **19.6** (-15.2%) | 2.8 -> **3.7** | 87.8 -> **92.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.2% vs 30% floor, Casts: 2015). Increasing spread: b -15.1%, n +31.0% |
| `WED` | Plants | Conditional Strike | 21.9 -> **24.0** (+9.6%) | 4.3 -> **4.0** | 116.1 -> **120.0** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.2% vs 8% floor, Casts: 2592, WR: 45.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 45.7%, Casts: 2592, mult: 1.014) |
| `EWF` | Plants | Buff / Sustain | 27.5 -> **23.5** (-14.5%) | 2.8 -> **3.6** | 104.5 -> **108.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 2273). Increasing spread: b -14.5%, n +29.7% |
| `EWW` | Plants | Debuff / Control | 38.5 -> **33.6** (-12.7%) | - | 38.5 -> **33.6** | Individual spell overtuned (WR: 81.5%, Casts: 2269, mult: 0.874) |
| `EWD` | Plants | Conditional Strike | 21.3 -> **17.4** (-18.3%) | 2.9 -> **3.9** | 83.1 -> **85.3** | Status 'Bleeding' appliers overtuned on own (WR: 57.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 1726). Increasing spread: b -17.4%, n +35.7% |
| `WLF` | Fey | Conditional Strike | 22.3 -> **18.4** (-17.5%) | 2.8 -> **3.7** | 84.7 -> **86.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.9% vs 30% floor, Casts: 2292). Increasing spread: b -16.4%, n +33.8%; Individual spell overtuned (WR: 53.7%, Casts: 2292, mult: 0.988) |
| `WLE` | Fey | Setup - Location | 20.0 -> **20.7** (+3.5%) | - | 20.0 -> **20.7** | Location 'Enchanted Forest' appliers undertuned (WR: 44.9%, casts: 1828); Individual spell undertuned (WR: 44.9%, Casts: 1828, mult: 1.017) |
| `WLL` | Fey | Direct Damage | 60.0 -> **60.9** (+1.5%) | - | 60.0 -> **60.9** | Individual spell undertuned (WR: 45.5%, Casts: 2104, mult: 1.015) |
| `WLD` | Fey | Ultimate | 23.4 -> **25.3** (+8.1%) | 7.2 -> **6.8** | 191.9 -> **197.3** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1837, WR: 47.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `LWF` | Fey | Debuff / Control | 36.9 -> **31.6** (-14.4%) | 2.7 -> **3.5** | 136.5 -> **142.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.2% vs 30% floor, Casts: 1781). Increasing spread: b -14.3%, n +29.3% |
| `LWD` | Fey | Conditional Strike | 21.8 -> **18.2** (-16.5%) | 2.9 -> **4.0** | 85.0 -> **91.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2245). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 45.0%, Casts: 2245, mult: 1.017) |
| `WDF` | Ice | Conditional Strike | 22.8 -> **20.2** (-11.4%) | 2.8 -> **3.7** | 86.6 -> **94.9** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Status 'Stunned' appliers undertuned (WR: 45.5%, casts: 15448) |
| `WDW` | Ice | Buff / Sustain | 14.7 -> **15.2** (+3.4%) | - | 14.7 -> **15.2** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Status 'Frosty' appliers undertuned (WR: 45.3%, casts: 10275) |
| `WDE` | Ice | Setup - Weather | 20.0 -> **20.4** (+2.0%) | - | 20.0 -> **20.4** | Class Ice undertuned (WR: 45.6%, factor: 1.018) |
| `WDL` | Ice | Debuff / Control | 45.0 -> **46.5** (+3.3%) | - | 45.0 -> **46.5** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Status 'Frosty' appliers undertuned (WR: 45.3%, casts: 10275) |
| `WDD` | Ice | Ultimate | 23.7 -> **26.6** (+12.2%) | 7.1 -> **7.0** | 192.0 -> **212.8** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Weather 'Blizzard' beneficiaries undertuned (WR: 44.1%) |
| `DWF` | Ice | Debuff / Control | 45.0 -> **47.7** (+6.0%) | - | 45.0 -> **47.7** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Status 'Frosty' appliers undertuned (WR: 45.3%, casts: 10275) |
| `DWW` | Ice | Debuff / Control | 35.0 -> **36.6** (+4.6%) | - | 35.0 -> **36.6** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Individual spell undertuned (WR: 42.4%, Casts: 2808, mult: 1.027) |
| `DWE` | Ice | Setup - Location | 20.0 -> **20.4** (+2.0%) | - | 20.0 -> **20.4** | Class Ice undertuned (WR: 45.6%, factor: 1.018) |
| `DWL` | Ice | Debuff / Control | 45.0 -> **48.0** (+6.7%) | - | 45.0 -> **48.0** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Status 'Frosty' appliers undertuned (WR: 45.3%, casts: 10275) |
| `DWD` | Ice | Conditional Strike | 24.1 -> **21.5** (-10.8%) | 2.7 -> **3.4** | 89.2 -> **94.6** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Status 'Frosty' beneficiaries undertuned (WR: 46.2%) |
| `ELF` | Wind | Conditional Strike | 47.8 -> **39.4** (-17.6%) | 2.8 -> **3.7** | 181.6 -> **185.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.7% vs 30% floor, Casts: 1422). Increasing spread: b -16.5%, n +33.9%; Individual spell overtuned (WR: 53.8%, Casts: 1422, mult: 0.988) |
| `ELD` | Wind | Conditional Strike | 23.1 -> **19.5** (-15.6%) | 2.8 -> **3.7** | 87.8 -> **91.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.8% vs 30% floor, Casts: 2115). Increasing spread: b -15.7%, n +32.1% |
| `LEF` | Wind | Conditional Strike | 22.1 -> **18.6** (-15.8%) | 2.8 -> **3.7** | 84.0 -> **87.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.0% vs 30% floor, Casts: 1905). Increasing spread: b -16.0%, n +32.8% |
| `LEW` | Wind | Debuff / Control | 60.0 -> **59.2** (-1.3%) | - | 60.0 -> **59.2** | Individual spell overtuned (WR: 54.1%, Casts: 1990, mult: 0.987) |
| `LEL` | Wind | Buff / Sustain | 35.0 -> **35.4** (+1.1%) | - | 35.0 -> **35.4** | Individual spell undertuned (WR: 46.2%, Casts: 2067, mult: 1.012) |
| `EDF` | Poison | Conditional Strike | 22.5 -> **19.2** (-14.7%) | 2.8 -> **3.8** | 85.5 -> **92.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.6% vs 30% floor, Casts: 2898). Increasing spread: b -16.6%, n +34.0%; Individual spell undertuned (WR: 43.0%, Casts: 2898, mult: 1.024) |
| `EDW` | Poison | Debuff / Control | 34.0 -> **33.0** (-2.9%) | - | 34.0 -> **33.0** | Individual spell overtuned (WR: 58.4%, Casts: 1607, mult: 0.970) |
| `EDL` | Poison | Debuff / Control | 21.6 -> **18.9** (-12.5%) | - | 21.6 -> **18.9** | Individual spell overtuned (WR: 81.7%, Casts: 1810, mult: 0.873) |
| `EDD` | Poison | Ultimate | 24.3 -> **26.6** (+9.5%) | 7.5 -> **7.2** | 206.6 -> **218.1** | Location 'Swamp' beneficiaries undertuned (WR: 46.0%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.4% vs 16% floor, Casts: 2197, WR: 46.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DEW` | Poison | Debuff / Control | 33.9 -> **33.3** (-1.8%) | - | 33.9 -> **33.3** | Individual spell overtuned (WR: 55.3%, Casts: 2049, mult: 0.982) |
| `DEL` | Poison | Conditional Strike | 2.4 -> **2.0** (-16.7%) | 2.8 -> **3.7** | 9.1 -> **9.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.7% vs 30% floor, Casts: 2631). Increasing spread: b -16.5%, n +33.9% |
| `DED` | Poison | Debuff / Control | 28.8 -> **29.4** (+2.1%) | - | 28.8 -> **29.4** | Individual spell undertuned (WR: 43.9%, Casts: 1991, mult: 1.021) |
| `LDW` | Cosmic | Debuff / Control | 45.6 -> **47.2** (+3.5%) | - | 45.6 -> **47.2** | Status 'Stunned' appliers undertuned (WR: 45.5%, casts: 15448); Individual spell undertuned (WR: 44.4%, Casts: 2194, mult: 1.019) |
| `LDL` | Cosmic | Conditional Strike | 22.2 -> **18.4** (-17.1%) | 2.9 -> **3.9** | 86.6 -> **90.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.8% vs 30% floor, Casts: 1983). Increasing spread: b -16.9%, n +34.7% |
| `LDD` | Cosmic | Ultimate | 24.2 -> **19.8** (-18.2%) | 7.2 -> **9.9** | 198.4 -> **215.8** | Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2136). Increasing spread: b -18.0%, n +37.0% |
| `DLF` | Cosmic | Conditional Strike | 28.1 -> **23.6** (-16.0%) | 2.8 -> **3.7** | 106.8 -> **110.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.1% vs 30% floor, Casts: 1959). Increasing spread: b -16.0%, n +32.8% |
| `DLE` | Cosmic | Direct Damage | 35.0 -> **37.0** (+5.7%) | - | 35.0 -> **37.0** | Individual spell undertuned (WR: 35.0%, Casts: 3232, mult: 1.056) |
| `DLL` | Cosmic | Conditional Strike | 36.6 -> **31.5** (-13.9%) | 2.8 -> **3.6** | 139.1 -> **144.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.5% vs 30% floor, Casts: 1616). Increasing spread: b -13.8%, n +28.3% |
| `DLD` | Cosmic | Conditional Strike | 35.0 -> **39.8** (+13.7%) | 2.0 -> **1.6** | 105.0 -> **103.5** | Condition triggers excessively (N=1 conditions, Trigger Rate: 93.6% vs 55% ceiling, WR: 48.5%). Compressing spread: b +13.6%, n -21.7% |
