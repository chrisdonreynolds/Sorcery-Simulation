# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T21:49:24Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 692.0s  
**Total Spells Tuned:** 101 / 125  

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
| **Poison** | 18,690 | 57.5% | 57.6% | 10.1 | Overtuned ⚠️ |
| **Plants** | 19,379 | 54.0% | 54.0% | 7.7 | Overtuned ⚠️ |
| **Fire** | 6,806 | 52.8% | 52.9% | 15.8 | Balanced ✅ |
| **Blood** | 20,445 | 52.7% | 52.7% | 13.1 | Balanced ✅ |
| **Beasts** | 18,018 | 51.8% | 51.8% | 6.2 | Balanced ✅ |
| **Dark** | 9,950 | 50.7% | 50.7% | 12.3 | Balanced ✅ |
| **Earth** | 9,590 | 50.4% | 50.4% | 17.7 | Balanced ✅ |
| **Ice** | 16,429 | 49.6% | 49.6% | 12.3 | Balanced ✅ |
| **Ghostfire** | 20,885 | 49.5% | 49.5% | 12.1 | Balanced ✅ |
| **Light** | 11,098 | 49.5% | 49.5% | 4.0 | Balanced ✅ |
| **Lightning** | 20,852 | 49.3% | 49.3% | 10.6 | Balanced ✅ |
| **Wind** | 16,230 | 46.8% | 46.7% | 7.6 | Balanced ✅ |
| **Water** | 8,609 | 46.2% | 46.2% | 7.2 | Undertuned ⚠️ |
| **Fey** | 18,318 | 46.1% | 46.1% | 8.8 | Undertuned ⚠️ |
| **Cosmic** | 19,074 | 44.9% | 44.9% | 14.9 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 5,494 (50.7%) | 3,647 (52.3%) | 21.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,739 (42.1%) | 3,715 (51.9%) | 14.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 3,638 (56.3%) | 5,008 (47.9%) | 9.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,326 (66.7%) | 7,484 (47.4%) | 6.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 12,849 (52.7%) | 3,746 (41.3%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,088 (52.6%) | 4,935 (52.1%) | 1.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,885 (36.8%) | 3,941 (44.0%) | 7.4% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 61.8 -> **61.0** (-1.3%) | - | 61.8 -> **61.0** | Individual spell overtuned (WR: 53.8%, Casts: 1557, mult: 0.988) |
| `FFW` | Fire | Debuff / Control | 47.8 -> **46.7** (-2.3%) | - | 47.8 -> **46.7** | Status 'Burning' appliers overtuned on own (WR: 56.3%) |
| `FFE` | Fire | Debuff / Control | 36.1 -> **34.8** (-3.6%) | - | 36.1 -> **34.8** | Individual spell overtuned (WR: 60.3%, Casts: 1209, mult: 0.963) |
| `FFL` | Fire | Debuff / Control | 8.2 -> **7.7** (-6.1%) | - | 8.2 -> **7.7** | Status 'Burning' appliers overtuned on own (WR: 56.3%); Individual spell overtuned (WR: 60.9%, Casts: 779, mult: 0.961) |
| `FFD` | Fire | Conditional Strike | 12.1 -> **10.4** (-14.0%) | 8.0 -> **10.4** | 108.9 -> **118.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.0% vs 30% floor, Casts: 1975). Increasing spread: b -14.8%, n +30.4%; Individual spell undertuned (WR: 46.1%, Casts: 1975, mult: 1.013) |
| `WWF` | Water | Conditional Strike | 20.7 -> **18.6** (-10.1%) | 7.3 -> **9.2** | 171.8 -> **189.7** | Class Water undertuned (WR: 46.2%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.9% vs 30% floor, Casts: 1571). Increasing spread: b -12.8%, n +26.2% |
| `WWE` | Water | Setup - Weather | 22.0 -> **24.5** (+11.4%) | - | 22.0 -> **24.5** | Class Water undertuned (WR: 46.2%, factor: 1.015); Weather 'Raining' appliers undertuned (WR: 36.8%, casts: 1885) |
| `WWL` | Water | Buff / Sustain | 62.1 -> **63.0** (+1.4%) | - | 62.1 -> **63.0** | Class Water undertuned (WR: 46.2%, factor: 1.015) |
| `WWD` | Water | Buff / Sustain | 47.2 -> **47.9** (+1.5%) | - | 47.2 -> **47.9** | Class Water undertuned (WR: 46.2%, factor: 1.015) |
| `EEF` | Earth | Conditional Strike | 31.4 -> **28.4** (-9.6%) | 3.7 -> **4.4** | 147.6 -> **153.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 21.1% vs 30% floor, Casts: 2247). Increasing spread: b -9.6%, n +19.5% |
| `EEE` | Earth | Conditional Strike | 7.1 -> **8.1** (+14.1%) | 1.5 -> **1.5** | 17.8 -> **20.2** | Condition triggers excessively (N=1 conditions, Trigger Rate: 93.3% vs 55% ceiling, WR: 51.9%). Compressing spread: b +13.5%, n -21.6% |
| `LLF` | Light | Conditional Strike | 3.0 -> **3.4** (+13.3%) | 8.2 -> **10.8** | 27.6 -> **40.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 3132). Increasing spread: b -15.3%, n +31.4%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLE` | Light | Setup - Weather | 22.3 -> **27.1** (+21.5%) | - | 22.3 -> **27.1** | Weather 'Sunny' appliers undertuned (WR: 42.1%, casts: 2739); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 30.5 -> **29.9** (-2.0%) | - | 30.5 -> **29.9** | Individual spell overtuned (WR: 55.9%, Casts: 2141, mult: 0.980) |
| `LLD` | Light | Ultimate | 29.5 -> **29.5** (+0.0%) | 7.3 -> **9.5** | 244.9 -> **309.8** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.3% vs 16% floor, Casts: 1103). Shifted tuner focus: protected ultimate base floor at 29.5 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 9.3 -> **7.6** (-18.3%) | 10.3 -> **14.1** | 105.1 -> **114.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1633). Increasing spread: b -18.0%, n +37.0% |
| `DDE` | Dark | Setup - Weather | 31.8 -> **36.6** (+15.1%) | - | 31.8 -> **36.6** | Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDD` | Dark | Debuff / Control | 31.6 -> **30.8** (-2.5%) | - | 31.6 -> **30.8** | Individual spell overtuned (WR: 57.5%, Casts: 1175, mult: 0.974) |
| `FWF` | Ghostfire | Debuff / Control | 43.7 -> **41.4** (-5.3%) | - | 43.7 -> **41.4** | Status 'Burning' appliers overtuned on own (WR: 56.3%); Individual spell overtuned (WR: 59.0%, Casts: 1573, mult: 0.968) |
| `FWW` | Ghostfire | Debuff / Control | 23.4 -> **28.0** (+19.7%) | - | 23.4 -> **28.0** | Status 'Cursed' appliers undertuned (WR: 46.2%, casts: 5944); Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 38.8 -> **46.9** (+20.9%) | - | 38.8 -> **46.9** | Location 'Graveyard' appliers undertuned (WR: 42.8%, casts: 3258); Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 66.6 -> **77.6** (+16.5%) | - | 66.6 -> **77.6** | Status 'Cursed' appliers undertuned (WR: 46.2%, casts: 5944); Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 25.5 -> **25.0** (-2.0%) | 14.7 -> **18.9** | 400.3 -> **497.5** | Status 'Cursed' beneficiaries undertuned (WR: 45.7%); Location 'Graveyard' beneficiaries overtuned (WR: 55.7%) |
| `WFF` | Ghostfire | Conditional Strike | 11.7 -> **10.1** (-13.7%) | 8.2 -> **10.8** | 107.6 -> **119.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 2161). Increasing spread: b -15.5%, n +31.8%; Individual spell undertuned (WR: 44.8%, Casts: 2161, mult: 1.017) |
| `WFW` | Ghostfire | Debuff / Control | 31.1 -> **30.5** (-1.9%) | - | 31.1 -> **30.5** | Individual spell overtuned (WR: 56.0%, Casts: 3511, mult: 0.980) |
| `WFE` | Ghostfire | Debuff / Control | 43.3 -> **38.5** (-11.1%) | - | 43.3 -> **38.5** | Status 'Bleeding' appliers overtuned on own (WR: 66.7%); Individual spell overtuned (WR: 65.2%, Casts: 1360, mult: 0.943) |
| `WFD` | Ghostfire | Conditional Strike | 13.3 -> **11.9** (-10.5%) | 7.5 -> **9.6** | 113.1 -> **126.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.2% vs 30% floor, Casts: 2061). Increasing spread: b -13.9%, n +28.5%; Individual spell undertuned (WR: 39.6%, Casts: 2061, mult: 1.037) |
| `FEF` | Beasts | Debuff / Control | 28.2 -> **28.9** (+2.5%) | - | 28.2 -> **28.9** | Individual spell undertuned (WR: 43.2%, Casts: 2700, mult: 1.023) |
| `FEW` | Beasts | Conditional Strike | 10.0 -> **8.3** (-17.0%) | 10.2 -> **13.8** | 112.0 -> **122.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 1367). Increasing spread: b -17.3%, n +35.5% |
| `FEE` | Beasts | Buff / Sustain | 25.0 -> **25.5** (+2.0%) | - | 25.0 -> **25.5** | Individual spell undertuned (WR: 44.0%, Casts: 1855, mult: 1.020) |
| `FEL` | Beasts | Buff / Sustain | 25.4 -> **25.9** (+2.0%) | - | 25.4 -> **25.9** | Individual spell undertuned (WR: 44.5%, Casts: 653, mult: 1.018) |
| `FED` | Beasts | Conditional Strike | 7.3 -> **7.8** (+6.8%) | 1.5 -> **1.5** | 18.2 -> **19.5** | Condition triggers excessively (N=1 conditions, Trigger Rate: 57.3% vs 55% ceiling, WR: 52.9%). Compressing spread: b +6.7%, n -10.0% |
| `EFF` | Beasts | Debuff / Control | 12.4 -> **10.4** (-16.1%) | 10.0 -> **13.6** | 136.4 -> **151.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 2322). Increasing spread: b -17.3%, n +35.6%; Individual spell undertuned (WR: 45.7%, Casts: 2322, mult: 1.014) |
| `EFL` | Beasts | Buff / Sustain | 18.9 -> **16.2** (-14.3%) | - | 18.9 -> **16.2** | Individual spell overtuned (WR: 84.9%, Casts: 1991, mult: 0.859) |
| `EFD` | Beasts | Ultimate | 27.6 -> **29.8** (+8.0%) | 11.2 -> **10.5** | 336.7 -> **342.7** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.4% vs 16% floor, Casts: 1086, WR: 48.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `FLF` | Lightning | Conditional Strike | 10.4 -> **8.8** (-15.4%) | 10.9 -> **15.4** | 123.8 -> **144.3** | Status 'Stunned' beneficiaries undertuned (WR: 41.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 1600). Increasing spread: b -17.7%, n +36.4% |
| `FLW` | Lightning | Debuff / Control | 54.9 -> **54.2** (-1.3%) | - | 54.9 -> **54.2** | Individual spell overtuned (WR: 53.7%, Casts: 2250, mult: 0.988) |
| `FLD` | Lightning | Ultimate | 32.7 -> **36.4** (+11.3%) | 9.1 -> **9.2** | 330.3 -> **371.3** | Status 'Stunned' beneficiaries undertuned (WR: 41.3%); Weather 'Storming' beneficiaries undertuned (WR: 41.2%) |
| `LFF` | Lightning | Conditional Strike | 11.0 -> **9.1** (-17.3%) | 9.5 -> **12.9** | 115.5 -> **126.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1599). Increasing spread: b -17.2%, n +35.4% |
| `LFW` | Lightning | Buff / Sustain | 34.2 -> **33.2** (-2.9%) | - | 34.2 -> **33.2** | Individual spell overtuned (WR: 58.1%, Casts: 1665, mult: 0.972) |
| `LFE` | Lightning | Debuff / Control | 46.9 -> **46.1** (-1.7%) | - | 46.9 -> **46.1** | Individual spell overtuned (WR: 55.1%, Casts: 2513, mult: 0.983) |
| `LFL` | Lightning | Debuff / Control | 39.5 -> **34.7** (-12.2%) | 7.4 -> **9.4** | 331.8 -> **360.9** | Weather 'Darkness' beneficiaries undertuned (WR: 46.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.8% vs 30% floor, Casts: 2270). Increasing spread: b -12.1%, n +24.7% |
| `LFD` | Lightning | Conditional Strike | 14.6 -> **12.5** (-14.4%) | 12.0 -> **15.5** | 189.8 -> **206.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.9% vs 30% floor, Casts: 2471). Increasing spread: b -14.4%, n +29.5% |
| `FDF` | Blood | Conditional Strike | 9.8 -> **8.3** (-15.3%) | 10.3 -> **14.1** | 110.7 -> **125.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2047). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 41.6%, Casts: 2047, mult: 1.030) |
| `FDW` | Blood | Direct Damage | 58.2 -> **59.8** (+2.7%) | - | 58.2 -> **59.8** | Individual spell undertuned (WR: 41.9%, Casts: 1780, mult: 1.028) |
| `FDE` | Blood | Setup - Weather | 20.3 -> **20.0** (-1.5%) | - | 20.3 -> **20.0** | Individual spell overtuned (WR: 53.9%, Casts: 1072, mult: 0.987) |
| `FDL` | Blood | Debuff / Control | 35.3 -> **30.3** (-14.2%) | - | 35.3 -> **30.3** | Status 'Bleeding' appliers overtuned on own (WR: 66.7%); Individual spell overtuned (WR: 72.9%, Casts: 3587, mult: 0.911) |
| `FDD` | Blood | Ultimate | 28.4 -> **32.4** (+14.1%) | 7.9 -> **7.5** | 252.8 -> **275.4** | Weather 'Darkness' beneficiaries undertuned (WR: 46.1%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.5% vs 16% floor, Casts: 2086, WR: 35.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 11.7 -> **10.0** (-14.5%) | 7.8 -> **10.1** | 103.0 -> **111.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.0% vs 30% floor, Casts: 1528). Increasing spread: b -14.4%, n +29.5% |
| `DFW` | Blood | Debuff / Control | 33.1 -> **28.9** (-12.7%) | - | 33.1 -> **28.9** | Status 'Bleeding' appliers overtuned on own (WR: 66.7%); Individual spell overtuned (WR: 69.2%, Casts: 1897, mult: 0.927) |
| `DFE` | Blood | Buff / Sustain | 34.5 -> **35.0** (+1.4%) | - | 34.5 -> **35.0** | Individual spell undertuned (WR: 45.4%, Casts: 2402, mult: 1.015) |
| `DFD` | Blood | Conditional Strike | 45.4 -> **51.8** (+14.1%) | 0.7 -> **0.5** | 77.2 -> **77.7** | Condition triggers excessively (N=1 conditions, Trigger Rate: 95.8% vs 55% ceiling, WR: 50.4%). Compressing spread: b +14.1%, n -22.5% |
| `WEF` | Plants | Conditional Strike | 13.8 -> **11.5** (-16.7%) | 7.2 -> **9.1** | 113.2 -> **116.1** | Class Plants overtuned (WR: 54.0%, factor: 0.984); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.8% vs 30% floor, Casts: 1496). Increasing spread: b -12.9%, n +26.4% |
| `WEW` | Plants | Debuff / Control | 56.3 -> **63.7** (+13.1%) | - | 56.3 -> **63.7** | Class Plants overtuned (WR: 54.0%, factor: 0.984); Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WEE` | Plants | Setup - Location | 19.9 -> **20.6** (+3.5%) | - | 19.9 -> **20.6** | Class Plants overtuned (WR: 54.0%, factor: 0.984); Location 'Jungle' appliers undertuned (WR: 42.8%, casts: 2416) |
| `WEL` | Plants | Debuff / Control | 41.7 -> **41.0** (-1.7%) | - | 41.7 -> **41.0** | Class Plants overtuned (WR: 54.0%, factor: 0.984) |
| `WED` | Plants | Conditional Strike | 10.1 -> **10.7** (+5.9%) | 13.7 -> **12.9** | 148.5 -> **148.7** | Class Plants overtuned (WR: 54.0%, factor: 0.984); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.5% vs 8% floor, Casts: 1293, WR: 46.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 14.9 -> **13.2** (-11.4%) | 6.9 -> **8.3** | 117.7 -> **122.8** | Class Plants overtuned (WR: 54.0%, factor: 0.984); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 20.8% vs 30% floor, Casts: 2612). Increasing spread: b -9.7%, n +19.7% |
| `EWW` | Plants | Debuff / Control | 24.7 -> **20.9** (-15.4%) | - | 24.7 -> **20.9** | Class Plants overtuned (WR: 54.0%, factor: 0.984); Individual spell overtuned (WR: 84.2%, Casts: 2050, mult: 0.862) |
| `EWL` | Plants | Debuff / Control | 59.1 -> **58.2** (-1.5%) | - | 59.1 -> **58.2** | Class Plants overtuned (WR: 54.0%, factor: 0.984) |
| `EWD` | Plants | Conditional Strike | 17.5 -> **13.2** (-24.6%) | 10.0 -> **13.5** | 192.5 -> **191.4** | Class Plants overtuned (WR: 54.0%, factor: 0.984); Status 'Bleeding' appliers overtuned on own (WR: 66.7%) |
| `WLF` | Fey | Conditional Strike | 11.7 -> **10.2** (-12.8%) | 8.6 -> **11.7** | 112.3 -> **129.5** | Class Fey undertuned (WR: 46.1%, factor: 1.016); Status 'Cursed' beneficiaries undertuned (WR: 45.7%) |
| `WLW` | Fey | Debuff / Control | 45.1 -> **47.1** (+4.4%) | - | 45.1 -> **47.1** | Class Fey undertuned (WR: 46.1%, factor: 1.016); Status 'Cursed' appliers undertuned (WR: 46.2%, casts: 5944) |
| `WLE` | Fey | Setup - Location | 33.2 -> **41.4** (+24.7%) | - | 33.2 -> **41.4** | Class Fey undertuned (WR: 46.1%, factor: 1.016); Location 'Enchanted Forest' appliers undertuned (WR: 40.5%, casts: 1895) |
| `WLL` | Fey | Direct Damage | 63.4 -> **63.1** (-0.5%) | - | 63.4 -> **63.1** | Class Fey undertuned (WR: 46.1%, factor: 1.016); Individual spell overtuned (WR: 56.1%, Casts: 1432, mult: 0.979) |
| `WLD` | Fey | Ultimate | 26.1 -> **26.2** (+0.4%) | 15.3 -> **20.2** | 425.4 -> **555.4** | Class Fey undertuned (WR: 46.1%, factor: 1.016); Weather 'Darkness' beneficiaries undertuned (WR: 46.1%) |
| `LWF` | Fey | Debuff / Control | 29.6 -> **26.8** (-9.5%) | 6.3 -> **7.7** | 216.1 -> **233.2** | Class Fey undertuned (WR: 46.1%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.7% vs 30% floor, Casts: 2194). Increasing spread: b -10.9%, n +22.3% |
| `LWW` | Fey | Debuff / Control | 36.9 -> **38.9** (+5.4%) | - | 36.9 -> **38.9** | Class Fey undertuned (WR: 46.1%, factor: 1.016); Individual spell undertuned (WR: 39.3%, Casts: 1742, mult: 1.038) |
| `LWL` | Fey | Debuff / Control | 37.5 -> **38.1** (+1.6%) | - | 37.5 -> **38.1** | Class Fey undertuned (WR: 46.1%, factor: 1.016) |
| `LWD` | Fey | Conditional Strike | 10.6 -> **9.2** (-13.2%) | 10.3 -> **14.1** | 119.8 -> **138.9** | Class Fey undertuned (WR: 46.1%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1514). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 12.2 -> **10.3** (-15.6%) | 9.4 -> **12.7** | 126.9 -> **141.1** | Weather 'Raining' beneficiaries undertuned (WR: 44.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.5% vs 30% floor, Casts: 1505). Increasing spread: b -15.4%, n +31.6% |
| `WDL` | Ice | Debuff / Control | 46.8 -> **46.2** (-1.3%) | - | 46.8 -> **46.2** | Individual spell overtuned (WR: 53.8%, Casts: 1275, mult: 0.987) |
| `WDD` | Ice | Ultimate | 28.7 -> **28.7** (+0.0%) | 10.1 -> **12.7** | 318.6 -> **393.2** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 3.3% vs 16% floor, Casts: 1960). Shifted tuner focus: protected ultimate base floor at 28.7 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWW` | Ice | Debuff / Control | 44.2 -> **43.5** (-1.6%) | - | 44.2 -> **43.5** | Individual spell overtuned (WR: 55.0%, Casts: 1829, mult: 0.983) |
| `DWE` | Ice | Setup - Location | 24.2 -> **25.1** (+3.7%) | - | 24.2 -> **25.1** | Location 'Tundra' appliers undertuned (WR: 44.5%, casts: 2595); Individual spell undertuned (WR: 44.5%, Casts: 2595, mult: 1.018) |
| `DWD` | Ice | Conditional Strike | 18.9 -> **17.2** (-9.0%) | 5.0 -> **5.9** | 113.4 -> **118.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 22.8% vs 30% floor, Casts: 1400). Increasing spread: b -8.9%, n +18.0% |
| `ELF` | Wind | Conditional Strike | 25.3 -> **22.1** (-12.6%) | 8.1 -> **10.5** | 230.2 -> **254.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.5% vs 30% floor, Casts: 1035). Increasing spread: b -14.2%, n +29.1%; Individual spell undertuned (WR: 44.7%, Casts: 1035, mult: 1.018) |
| `ELW` | Wind | Debuff / Control | 41.3 -> **42.5** (+2.9%) | - | 41.3 -> **42.5** | Individual spell undertuned (WR: 41.9%, Casts: 1948, mult: 1.028) |
| `ELE` | Wind | Setup - Weather | 20.3 -> **19.9** (-2.0%) | - | 20.3 -> **19.9** | Individual spell overtuned (WR: 56.4%, Casts: 1070, mult: 0.978) |
| `ELL` | Wind | Buff / Sustain | 35.9 -> **36.8** (+2.5%) | - | 35.9 -> **36.8** | Individual spell undertuned (WR: 42.7%, Casts: 1745, mult: 1.025) |
| `ELD` | Wind | Conditional Strike | 12.8 -> **11.6** (-9.4%) | 8.2 -> **10.9** | 117.8 -> **138.0** | Weather 'Raining' beneficiaries undertuned (WR: 44.0%); Weather 'Blizzard' appliers undertuned (WR: 41.6%, casts: 2436) |
| `LEF` | Wind | Conditional Strike | 11.7 -> **9.9** (-15.4%) | 9.0 -> **11.8** | 117.0 -> **126.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 1462). Increasing spread: b -15.4%, n +31.6% |
| `EDF` | Poison | Conditional Strike | 10.3 -> **8.5** (-17.5%) | 8.5 -> **11.3** | 97.9 -> **104.6** | Class Poison overtuned (WR: 57.5%, factor: 0.970); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.7% vs 30% floor, Casts: 2342). Increasing spread: b -16.1%, n +33.1% |
| `EDW` | Poison | Debuff / Control | 29.7 -> **28.3** (-4.7%) | - | 29.7 -> **28.3** | Class Poison overtuned (WR: 57.5%, factor: 0.970); Individual spell overtuned (WR: 54.9%, Casts: 1752, mult: 0.984) |
| `EDE` | Poison | Setup - Location | 24.9 -> **25.1** (+0.8%) | - | 24.9 -> **25.1** | Class Poison overtuned (WR: 57.5%, factor: 0.970); Location 'Swamp' appliers undertuned (WR: 44.5%, casts: 1599) |
| `EDL` | Poison | Debuff / Control | 11.8 -> **9.7** (-17.8%) | - | 11.8 -> **9.7** | Class Poison overtuned (WR: 57.5%, factor: 0.970); Individual spell overtuned (WR: 86.5%, Casts: 2744, mult: 0.851) |
| `EDD` | Poison | Ultimate | 25.7 -> **27.3** (+6.2%) | 11.0 -> **10.5** | 308.4 -> **313.9** | Class Poison overtuned (WR: 57.5%, factor: 0.970); Location 'Swamp' beneficiaries undertuned (WR: 45.6%) |
| `DEF` | Poison | Conditional Strike | 36.6 -> **35.0** (-4.4%) | 1.7 -> **1.7** | 98.8 -> **94.5** | Class Poison overtuned (WR: 57.5%, factor: 0.970); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 43.2% within [30%-55%] target window, WR: 54.1%). |
| `DEW` | Poison | Debuff / Control | 29.4 -> **27.1** (-7.8%) | - | 29.4 -> **27.1** | Class Poison overtuned (WR: 57.5%, factor: 0.970); Individual spell overtuned (WR: 63.2%, Casts: 3152, mult: 0.951) |
| `DEE` | Poison | Debuff / Control | 26.4 -> **25.6** (-3.0%) | - | 26.4 -> **25.6** | Class Poison overtuned (WR: 57.5%, factor: 0.970) |
| `DEL` | Poison | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 8.0 -> **10.4** | 10.8 -> **11.4** | Class Poison overtuned (WR: 57.5%, factor: 0.970); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.5% vs 30% floor, Casts: 1284). Increasing spread: b -14.6%, n +29.9% |
| `DED` | Poison | Debuff / Control | 27.0 -> **26.2** (-3.0%) | - | 27.0 -> **26.2** | Class Poison overtuned (WR: 57.5%, factor: 0.970) |
| `LDF` | Cosmic | Debuff / Control | 56.3 -> **58.7** (+4.3%) | - | 56.3 -> **58.7** | Class Cosmic undertuned (WR: 44.9%, factor: 1.021); Individual spell undertuned (WR: 43.8%, Casts: 1052, mult: 1.021) |
| `LDW` | Cosmic | Debuff / Control | 48.6 -> **48.1** (-1.0%) | - | 48.6 -> **48.1** | Class Cosmic undertuned (WR: 44.9%, factor: 1.021); Individual spell overtuned (WR: 58.7%, Casts: 1863, mult: 0.969) |
| `LDE` | Cosmic | Setup - Location | 21.3 -> **22.7** (+6.6%) | - | 21.3 -> **22.7** | Class Cosmic undertuned (WR: 44.9%, factor: 1.021); Individual spell undertuned (WR: 38.3%, Casts: 2405, mult: 1.042) |
| `LDL` | Cosmic | Conditional Strike | 12.6 -> **11.0** (-12.7%) | 8.3 -> **11.1** | 117.2 -> **133.1** | Class Cosmic undertuned (WR: 44.9%, factor: 1.021); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.0% vs 30% floor, Casts: 1619). Increasing spread: b -16.4%, n +33.7% |
| `LDD` | Cosmic | Ultimate | 32.0 -> **36.3** (+13.4%) | 7.8 -> **7.3** | 281.6 -> **301.3** | Class Cosmic undertuned (WR: 44.9%, factor: 1.021); Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2282, WR: 42.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 14.2 -> **12.4** (-12.7%) | 8.6 -> **11.4** | 136.3 -> **153.8** | Class Cosmic undertuned (WR: 44.9%, factor: 1.021); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 2443). Increasing spread: b -16.0%, n +32.9% |
| `DLW` | Cosmic | Direct Damage | 59.9 -> **61.1** (+2.0%) | - | 59.9 -> **61.1** | Class Cosmic undertuned (WR: 44.9%, factor: 1.021) |
| `DLE` | Cosmic | Direct Damage | 37.5 -> **41.0** (+9.3%) | - | 37.5 -> **41.0** | Class Cosmic undertuned (WR: 44.9%, factor: 1.021); Individual spell undertuned (WR: 31.2%, Casts: 1921, mult: 1.072) |
| `DLL` | Cosmic | Conditional Strike | 27.3 -> **24.1** (-11.7%) | 5.5 -> **7.1** | 177.5 -> **195.2** | Class Cosmic undertuned (WR: 44.9%, factor: 1.021); Weather 'Darkness' beneficiaries undertuned (WR: 46.1%) |
