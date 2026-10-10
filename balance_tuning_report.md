# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T21:08:24Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 480.2s  
**Total Spells Tuned:** 93 / 125  

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
| **Poison** | 18,137 | 55.0% | 55.0% | 9.8 | Overtuned ⚠️ |
| **Blood** | 19,254 | 54.0% | 54.1% | 12.1 | Overtuned ⚠️ |
| **Dark** | 12,000 | 52.4% | 52.4% | 10.6 | Balanced ✅ |
| **Beasts** | 16,682 | 52.3% | 52.3% | 7.3 | Balanced ✅ |
| **Water** | 7,221 | 51.5% | 51.5% | 8.7 | Balanced ✅ |
| **Plants** | 21,176 | 51.0% | 51.0% | 8.3 | Balanced ✅ |
| **Earth** | 9,365 | 50.9% | 50.9% | 16.2 | Balanced ✅ |
| **Ghostfire** | 22,678 | 50.8% | 50.8% | 12.0 | Balanced ✅ |
| **Fire** | 6,420 | 50.4% | 50.4% | 14.7 | Balanced ✅ |
| **Light** | 13,435 | 49.8% | 49.8% | 5.1 | Balanced ✅ |
| **Lightning** | 19,490 | 48.1% | 48.1% | 10.9 | Balanced ✅ |
| **Wind** | 14,532 | 48.0% | 48.0% | 8.0 | Balanced ✅ |
| **Cosmic** | 16,895 | 47.7% | 47.7% | 14.2 | Balanced ✅ |
| **Fey** | 17,385 | 46.3% | 46.3% | 9.9 | Undertuned ⚠️ |
| **Ice** | 19,862 | 45.7% | 45.7% | 11.0 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 7,664 (48.7%) | 4,191 (47.9%) | 31.6% | Healthy ✅ |
| **Sunny** (weather) | 2,159 (50.0%) | 3,987 (50.4%) | 8.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 3,697 (52.0%) | 4,053 (47.3%) | 8.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 11,807 (60.8%) | 7,547 (48.9%) | 7.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 12,275 (50.7%) | 3,568 (45.4%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,361 (58.8%) | 5,370 (45.3%) | 1.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,448 (45.6%) | 3,617 (46.4%) | 7.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFD` | Fire | Conditional Strike | 16.4 -> **14.1** (-14.0%) | 4.8 -> **6.2** | 95.1 -> **101.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.7% vs 30% floor, Casts: 1468). Increasing spread: b -14.1%, n +28.9% |
| `WWF` | Water | Conditional Strike | 27.4 -> **23.8** (-13.1%) | 4.6 -> **5.8** | 153.4 -> **161.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.8% vs 30% floor, Casts: 1110). Increasing spread: b -13.3%, n +27.2% |
| `WWE` | Water | Setup - Weather | 20.7 -> **21.3** (+2.9%) | - | 20.7 -> **21.3** | Weather 'Raining' appliers undertuned (WR: 45.6%, casts: 1448); Individual spell undertuned (WR: 45.6%, Casts: 1448, mult: 1.015) |
| `EEW` | Earth | Buff / Sustain | 35.7 -> **34.8** (-2.5%) | - | 35.7 -> **34.8** | Individual spell overtuned (WR: 57.3%, Casts: 1656, mult: 0.975) |
| `EEE` | Earth | Conditional Strike | 5.5 -> **6.3** (+14.5%) | 1.5 -> **1.5** | 13.8 -> **15.8** | Condition triggers excessively (N=1 conditions, Trigger Rate: 94.7% vs 55% ceiling, WR: 47.9%). Compressing spread: b +13.8%, n -22.1% |
| `LLF` | Light | Conditional Strike | 3.0 -> **2.6** (-13.3%) | 4.8 -> **6.3** | 17.4 -> **19.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 3412). Increasing spread: b -14.8%, n +30.3% |
| `LLL` | Light | Buff / Sustain | 32.5 -> **32.0** (-1.5%) | - | 32.5 -> **32.0** | Individual spell overtuned (WR: 55.1%, Casts: 2456, mult: 0.983) |
| `LLD` | Light | Ultimate | 27.0 -> **30.0** (+11.1%) | 6.1 -> **5.7** | 191.7 -> **201.0** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1628, WR: 41.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 41.5%, Casts: 1628, mult: 1.030) |
| `DDF` | Dark | Conditional Strike | 14.5 -> **11.7** (-19.3%) | 5.5 -> **7.5** | 94.2 -> **99.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2499). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 54.3%, Casts: 2499, mult: 0.986) |
| `DDE` | Dark | Setup - Weather | 25.0 -> **28.1** (+12.4%) | - | 25.0 -> **28.1** | Weather 'Darkness' appliers overtuned on own (WR: 53.5%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDD` | Dark | Debuff / Control | 33.9 -> **33.3** (-1.8%) | - | 33.9 -> **33.3** | Individual spell overtuned (WR: 55.0%, Casts: 1441, mult: 0.983) |
| `FWF` | Ghostfire | Debuff / Control | 45.5 -> **45.0** (-1.1%) | - | 45.5 -> **45.0** | Individual spell overtuned (WR: 53.7%, Casts: 1356, mult: 0.988) |
| `FWW` | Ghostfire | Debuff / Control | 17.2 -> **19.8** (+15.1%) | - | 17.2 -> **19.8** | Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 25.3 -> **30.9** (+22.1%) | - | 25.3 -> **30.9** | Location 'Graveyard' appliers undertuned (WR: 41.3%, casts: 2842); Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 51.7 -> **59.5** (+15.1%) | - | 51.7 -> **59.5** | Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 25.5 -> **25.5** (+0.0%) | 8.8 -> **11.4** | 249.9 -> **316.2** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.3% vs 8% floor, Casts: 1503). Shifted tuner focus: protected ultimate base floor at 25.5 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 16.3 -> **14.0** (-14.1%) | 4.8 -> **6.3** | 94.5 -> **102.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.2% vs 30% floor, Casts: 1860). Increasing spread: b -15.1%, n +31.0%; Individual spell undertuned (WR: 45.7%, Casts: 1860, mult: 1.014) |
| `WFW` | Ghostfire | Debuff / Control | 33.3 -> **32.2** (-3.3%) | - | 33.3 -> **32.2** | Individual spell overtuned (WR: 59.1%, Casts: 5094, mult: 0.968) |
| `WFE` | Ghostfire | Debuff / Control | 39.2 -> **41.3** (+5.4%) | - | 39.2 -> **41.3** | Status 'Bleeding' appliers overtuned on own (WR: 60.8%); Buffed setup spell [WFE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `WFL` | Ghostfire | Buff / Sustain | 35.0 -> **36.5** (+4.3%) | - | 35.0 -> **36.5** | Individual spell undertuned (WR: 38.0%, Casts: 1064, mult: 1.044) |
| `WFD` | Ghostfire | Conditional Strike | 17.1 -> **15.0** (-12.3%) | 4.6 -> **5.9** | 95.8 -> **103.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.7% vs 30% floor, Casts: 2566). Increasing spread: b -13.7%, n +28.1%; Individual spell undertuned (WR: 44.3%, Casts: 2566, mult: 1.019) |
| `FEW` | Beasts | Conditional Strike | 14.9 -> **12.1** (-18.8%) | 5.4 -> **7.5** | 95.4 -> **102.8** | Status 'Entangled' beneficiaries undertuned (WR: 45.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 740). Increasing spread: b -17.2%, n +35.4% |
| `FEL` | Beasts | Buff / Sustain | 25.0 -> **25.4** (+1.6%) | - | 25.0 -> **25.4** | Individual spell undertuned (WR: 44.8%, Casts: 911, mult: 1.018) |
| `FED` | Beasts | Conditional Strike | 6.4 -> **6.8** (+6.2%) | 1.8 -> **1.6** | 17.9 -> **17.7** | Condition triggers excessively (N=1 conditions, Trigger Rate: 58.2% vs 55% ceiling, WR: 50.9%). Compressing spread: b +5.7%, n -9.1% |
| `EFF` | Beasts | Debuff / Control | 18.2 -> **15.1** (-17.0%) | 5.4 -> **7.3** | 116.5 -> **125.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.0% vs 30% floor, Casts: 1888). Increasing spread: b -17.2%, n +35.4% |
| `EFL` | Beasts | Buff / Sustain | 25.4 -> **21.9** (-13.8%) | - | 25.4 -> **21.9** | Individual spell overtuned (WR: 84.0%, Casts: 1528, mult: 0.863) |
| `EFD` | Beasts | Ultimate | 22.3 -> **25.1** (+12.6%) | 11.8 -> **11.7** | 285.4 -> **318.8** | Status 'Entangled' beneficiaries undertuned (WR: 45.3%); Location 'Jungle' beneficiaries undertuned (WR: 40.7%) |
| `FLF` | Lightning | Conditional Strike | 14.8 -> **12.4** (-16.2%) | 5.6 -> **7.8** | 97.7 -> **109.1** | Status 'Stunned' beneficiaries undertuned (WR: 45.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 1689). Increasing spread: b -17.9%, n +36.7% |
| `FLE` | Lightning | Setup - Weather | 26.9 -> **28.2** (+4.8%) | - | 26.9 -> **28.2** | Weather 'Storming' appliers undertuned (WR: 43.4%, casts: 2235); Individual spell undertuned (WR: 43.4%, Casts: 2235, mult: 1.023) |
| `FLL` | Lightning | Buff / Sustain | 25.1 -> **25.5** (+1.6%) | - | 25.1 -> **25.5** | Individual spell undertuned (WR: 45.5%, Casts: 2401, mult: 1.015) |
| `FLD` | Lightning | Ultimate | 26.3 -> **28.8** (+9.5%) | 9.5 -> **9.2** | 276.2 -> **293.8** | Status 'Stunned' beneficiaries undertuned (WR: 45.4%); Weather 'Storming' beneficiaries undertuned (WR: 46.1%) |
| `LFF` | Lightning | Conditional Strike | 15.4 -> **12.9** (-16.2%) | 5.3 -> **7.1** | 97.0 -> **104.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.1% vs 30% floor, Casts: 1919). Increasing spread: b -16.4%, n +33.6% |
| `LFE` | Lightning | Debuff / Control | 45.6 -> **44.8** (-1.8%) | - | 45.6 -> **44.8** | Individual spell overtuned (WR: 55.5%, Casts: 2253, mult: 0.982) |
| `LFL` | Lightning | Debuff / Control | 50.2 -> **44.1** (-12.2%) | 4.7 -> **5.9** | 286.1 -> **304.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.7% vs 30% floor, Casts: 1754). Increasing spread: b -12.1%, n +24.7% |
| `LFD` | Lightning | Conditional Strike | 17.2 -> **14.9** (-13.4%) | 7.2 -> **9.4** | 141.0 -> **155.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.0% vs 30% floor, Casts: 1879). Increasing spread: b -14.8%, n +30.3%; Individual spell undertuned (WR: 44.5%, Casts: 1879, mult: 1.018) |
| `FDF` | Blood | Conditional Strike | 14.8 -> **12.2** (-17.6%) | 5.5 -> **7.5** | 96.2 -> **103.7** | Class Blood overtuned (WR: 54.0%, factor: 0.984); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1870). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 60.3 -> **59.3** (-1.7%) | - | 60.3 -> **59.3** | Class Blood overtuned (WR: 54.0%, factor: 0.984) |
| `FDE` | Blood | Setup - Weather | 19.6 -> **20.0** (+2.0%) | - | 19.6 -> **20.0** | Class Blood overtuned (WR: 54.0%, factor: 0.984); Individual spell undertuned (WR: 39.5%, Casts: 2213, mult: 1.038) |
| `FDL` | Blood | Debuff / Control | 35.9 -> **36.1** (+0.6%) | - | 35.9 -> **36.1** | Class Blood overtuned (WR: 54.0%, factor: 0.984); Status 'Bleeding' appliers overtuned on own (WR: 60.8%) |
| `FDD` | Blood | Ultimate | 24.7 -> **26.2** (+6.1%) | 8.9 -> **8.4** | 244.5 -> **246.3** | Class Blood overtuned (WR: 54.0%, factor: 0.984); Multi-condition setup trap (N=2 conditions, Trigger Rate: 1.3% vs 16% floor, Casts: 1373, WR: 47.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 16.1 -> **13.7** (-14.9%) | 4.7 -> **6.0** | 91.8 -> **95.9** | Class Blood overtuned (WR: 54.0%, factor: 0.984); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.5% vs 30% floor, Casts: 1444). Increasing spread: b -13.4%, n +27.4% |
| `DFW` | Blood | Debuff / Control | 32.4 -> **33.1** (+2.2%) | - | 32.4 -> **33.1** | Class Blood overtuned (WR: 54.0%, factor: 0.984); Status 'Bleeding' appliers overtuned on own (WR: 60.8%) |
| `DFL` | Blood | Buff / Sustain | 34.3 -> **33.7** (-1.7%) | - | 34.3 -> **33.7** | Class Blood overtuned (WR: 54.0%, factor: 0.984) |
| `DFD` | Blood | Conditional Strike | 36.2 -> **40.6** (+12.2%) | 1.1 -> **0.9** | 76.0 -> **77.1** | Class Blood overtuned (WR: 54.0%, factor: 0.984); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.2% vs 55% ceiling, WR: 49.0%). Compressing spread: b +13.9%, n -22.3% |
| `WEF` | Plants | Conditional Strike | 17.9 -> **16.1** (-10.1%) | 4.2 -> **5.5** | 93.1 -> **104.7** | Location 'Jungle' beneficiaries undertuned (WR: 40.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.2% vs 30% floor, Casts: 2126). Increasing spread: b -12.3%, n +25.2% |
| `WEW` | Plants | Debuff / Control | 41.4 -> **48.2** (+16.4%) | - | 41.4 -> **48.2** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 46.0%, Casts: 1541, mult: 1.013) |
| `WEE` | Plants | Setup - Location | 19.3 -> **20.2** (+4.7%) | - | 19.3 -> **20.2** | Location 'Jungle' appliers undertuned (WR: 43.2%, casts: 3063); Individual spell undertuned (WR: 43.1%, Casts: 3063, mult: 1.024) |
| `WEL` | Plants | Debuff / Control | 45.0 -> **42.3** (-6.0%) | - | 45.0 -> **42.3** | Status 'Entangled' appliers overtuned on own (WR: 58.8%); Individual spell overtuned (WR: 58.8%, Casts: 1361, mult: 0.969) |
| `WED` | Plants | Conditional Strike | 15.1 -> **12.7** (-15.9%) | 7.7 -> **10.2** | 131.4 -> **142.2** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 1.4% vs 8% floor, Casts: 1112). Increasing spread: b -16.0%, n +32.8% |
| `EWF` | Plants | Buff / Sustain | 20.7 -> **17.7** (-14.5%) | 4.3 -> **5.4** | 109.7 -> **113.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.5% vs 30% floor, Casts: 2359). Increasing spread: b -12.6%, n +25.7%; Individual spell overtuned (WR: 56.5%, Casts: 2359, mult: 0.978) |
| `EWW` | Plants | Debuff / Control | 33.5 -> **29.3** (-12.5%) | - | 33.5 -> **29.3** | Individual spell overtuned (WR: 81.1%, Casts: 1723, mult: 0.875) |
| `EWD` | Plants | Conditional Strike | 14.4 -> **16.2** (+12.5%) | 5.4 -> **7.4** | 92.2 -> **136.1** | Status 'Bleeding' appliers overtuned on own (WR: 60.8%); Status 'Entangled' beneficiaries undertuned (WR: 45.3%) |
| `WLF` | Fey | Conditional Strike | 15.7 -> **13.7** (-12.7%) | 4.9 -> **6.5** | 92.6 -> **102.8** | Class Fey undertuned (WR: 46.3%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.3% vs 30% floor, Casts: 1836). Increasing spread: b -15.5%, n +31.8% |
| `WLW` | Fey | Debuff / Control | 44.4 -> **45.1** (+1.6%) | - | 44.4 -> **45.1** | Class Fey undertuned (WR: 46.3%, factor: 1.015) |
| `WLE` | Fey | Setup - Location | 24.8 -> **28.9** (+16.5%) | - | 24.8 -> **28.9** | Class Fey undertuned (WR: 46.3%, factor: 1.015); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 61.8 -> **62.7** (+1.5%) | - | 61.8 -> **62.7** | Class Fey undertuned (WR: 46.3%, factor: 1.015) |
| `WLD` | Fey | Ultimate | 25.7 -> **26.1** (+1.6%) | 9.1 -> **11.8** | 259.6 -> **334.1** | Class Fey undertuned (WR: 46.3%, factor: 1.015); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 2227). Shifted tuner focus: protected ultimate base floor at 25.7 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 37.0 -> **33.0** (-10.8%) | 4.2 -> **5.2** | 192.4 -> **204.6** | Class Fey undertuned (WR: 46.3%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.0% vs 30% floor, Casts: 2286). Increasing spread: b -12.0%, n +24.5% |
| `LWW` | Fey | Debuff / Control | 35.0 -> **36.2** (+3.4%) | - | 35.0 -> **36.2** | Class Fey undertuned (WR: 46.3%, factor: 1.015); Individual spell undertuned (WR: 43.9%, Casts: 1721, mult: 1.021) |
| `LWL` | Fey | Debuff / Control | 35.2 -> **36.7** (+4.3%) | - | 35.2 -> **36.7** | Class Fey undertuned (WR: 46.3%, factor: 1.015); Individual spell undertuned (WR: 42.0%, Casts: 1530, mult: 1.028) |
| `LWD` | Fey | Conditional Strike | 15.2 -> **12.9** (-15.1%) | 5.5 -> **7.5** | 98.8 -> **109.7** | Class Fey undertuned (WR: 46.3%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1335). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 15.7 -> **13.4** (-14.6%) | 5.2 -> **7.0** | 97.3 -> **107.2** | Class Ice undertuned (WR: 45.7%, factor: 1.017); Weather 'Raining' beneficiaries undertuned (WR: 46.4%) |
| `WDW` | Ice | Buff / Sustain | 14.2 -> **14.4** (+1.4%) | - | 14.2 -> **14.4** | Class Ice undertuned (WR: 45.7%, factor: 1.017) |
| `WDE` | Ice | Setup - Weather | 20.0 -> **20.3** (+1.5%) | - | 20.0 -> **20.3** | Class Ice undertuned (WR: 45.7%, factor: 1.017) |
| `WDL` | Ice | Debuff / Control | 44.4 -> **45.8** (+3.2%) | - | 44.4 -> **45.8** | Class Ice undertuned (WR: 45.7%, factor: 1.017); Individual spell undertuned (WR: 45.7%, Casts: 1514, mult: 1.014) |
| `WDD` | Ice | Ultimate | 27.6 -> **28.1** (+1.8%) | 6.5 -> **8.1** | 207.0 -> **255.7** | Class Ice undertuned (WR: 45.7%, factor: 1.017); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 3.9% vs 16% floor, Casts: 1346). Shifted tuner focus: protected ultimate base floor at 27.6 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWF` | Ice | Debuff / Control | 43.5 -> **44.2** (+1.6%) | - | 43.5 -> **44.2** | Class Ice undertuned (WR: 45.7%, factor: 1.017) |
| `DWW` | Ice | Debuff / Control | 40.5 -> **42.1** (+4.0%) | - | 40.5 -> **42.1** | Class Ice undertuned (WR: 45.7%, factor: 1.017); Individual spell undertuned (WR: 43.9%, Casts: 1874, mult: 1.021) |
| `DWE` | Ice | Setup - Location | 20.0 -> **22.3** (+11.5%) | - | 20.0 -> **22.3** | Class Ice undertuned (WR: 45.7%, factor: 1.017); Location 'Tundra' appliers undertuned (WR: 36.9%, casts: 4337) |
| `DWL` | Ice | Debuff / Control | 43.2 -> **43.9** (+1.6%) | - | 43.2 -> **43.9** | Class Ice undertuned (WR: 45.7%, factor: 1.017) |
| `DWD` | Ice | Conditional Strike | 20.9 -> **20.3** (-2.9%) | 3.7 -> **4.2** | 98.2 -> **105.6** | Class Ice undertuned (WR: 45.7%, factor: 1.017); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 29.1% vs 30% floor, Casts: 1457). Increasing spread: b -6.4%, n +12.8% |
| `ELF` | Wind | Conditional Strike | 34.5 -> **29.7** (-13.9%) | 4.8 -> **6.2** | 200.1 -> **213.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.4% vs 30% floor, Casts: 1288). Increasing spread: b -13.8%, n +28.3% |
| `ELW` | Wind | Debuff / Control | 40.5 -> **41.3** (+2.0%) | - | 40.5 -> **41.3** | Individual spell undertuned (WR: 44.0%, Casts: 1296, mult: 1.021) |
| `ELD` | Wind | Conditional Strike | 17.1 -> **15.0** (-12.3%) | 4.7 -> **6.2** | 97.5 -> **108.0** | Weather 'Raining' beneficiaries undertuned (WR: 46.4%); Weather 'Blizzard' appliers undertuned (WR: 45.3%, casts: 2227) |
| `LEF` | Wind | Conditional Strike | 15.6 -> **13.5** (-13.5%) | 5.3 -> **7.0** | 98.3 -> **108.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.7% vs 30% floor, Casts: 1475). Increasing spread: b -15.7%, n +32.3%; Individual spell undertuned (WR: 41.4%, Casts: 1475, mult: 1.030) |
| `LEW` | Wind | Debuff / Control | 58.9 -> **57.8** (-1.9%) | - | 58.9 -> **57.8** | Individual spell overtuned (WR: 55.5%, Casts: 1629, mult: 0.981) |
| `EDF` | Poison | Conditional Strike | 15.3 -> **12.6** (-17.6%) | 4.8 -> **6.4** | 88.7 -> **93.2** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.8% vs 30% floor, Casts: 2520). Increasing spread: b -16.1%, n +33.0% |
| `EDW` | Poison | Debuff / Control | 32.2 -> **30.9** (-4.0%) | - | 32.2 -> **30.9** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 56.4%, Casts: 1583, mult: 0.978) |
| `EDE` | Poison | Setup - Location | 18.9 -> **21.3** (+12.7%) | - | 18.9 -> **21.3** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Buffed setup spell [EDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `EDL` | Poison | Debuff / Control | 16.8 -> **14.1** (-16.1%) | - | 16.8 -> **14.1** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 85.6%, Casts: 2680, mult: 0.856) |
| `EDD` | Poison | Ultimate | 27.2 -> **26.3** (-3.3%) | 6.7 -> **8.5** | 209.4 -> **249.8** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Location 'Swamp' beneficiaries overtuned (WR: 53.6%) |
| `DEF` | Poison | Conditional Strike | 36.1 -> **37.5** (+3.9%) | 1.9 -> **1.7** | 104.7 -> **101.2** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Condition triggers excessively (N=1 conditions, Trigger Rate: 60.1% vs 55% ceiling, WR: 46.8%). Compressing spread: b +6.1%, n -9.8% |
| `DEW` | Poison | Debuff / Control | 31.4 -> **30.8** (-1.9%) | - | 31.4 -> **30.8** | Class Poison overtuned (WR: 55.0%, factor: 0.980) |
| `DEE` | Poison | Debuff / Control | 27.2 -> **26.7** (-1.8%) | - | 27.2 -> **26.7** | Class Poison overtuned (WR: 55.0%, factor: 0.980) |
| `DEL` | Poison | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 4.7 -> **6.1** | 9.1 -> **9.9** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.5% vs 30% floor, Casts: 1175). Increasing spread: b -15.0%, n +30.8% |
| `DED` | Poison | Debuff / Control | 27.3 -> **27.1** (-0.7%) | - | 27.3 -> **27.1** | Class Poison overtuned (WR: 55.0%, factor: 0.980); Individual spell undertuned (WR: 46.1%, Casts: 1117, mult: 1.013) |
| `LDF` | Cosmic | Debuff / Control | 53.8 -> **54.8** (+1.9%) | - | 53.8 -> **54.8** | Individual spell undertuned (WR: 44.3%, Casts: 1363, mult: 1.019) |
| `LDL` | Cosmic | Conditional Strike | 16.6 -> **14.5** (-12.7%) | 4.9 -> **6.4** | 97.9 -> **107.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.4% vs 30% floor, Casts: 1383). Increasing spread: b -14.6%, n +30.0%; Individual spell undertuned (WR: 44.0%, Casts: 1383, mult: 1.020) |
| `LDD` | Cosmic | Ultimate | 26.4 -> **28.9** (+9.5%) | 8.8 -> **8.3** | 258.7 -> **268.8** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1826, WR: 45.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 45.9%, Casts: 1826, mult: 1.013) |
| `DLF` | Cosmic | Conditional Strike | 19.9 -> **16.8** (-15.6%) | 4.9 -> **6.5** | 117.4 -> **126.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 2723). Increasing spread: b -15.4%, n +31.7% |
| `DLE` | Cosmic | Direct Damage | 36.2 -> **36.8** (+1.7%) | - | 36.2 -> **36.8** | Individual spell undertuned (WR: 45.2%, Casts: 1719, mult: 1.016) |
| `DLL` | Cosmic | Conditional Strike | 34.6 -> **30.7** (-11.3%) | 3.5 -> **4.4** | 155.7 -> **165.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.8% vs 30% floor, Casts: 1810). Increasing spread: b -12.5%, n +25.5%; Individual spell undertuned (WR: 45.9%, Casts: 1810, mult: 1.013) |
| `DLD` | Cosmic | Conditional Strike | 47.2 -> **53.5** (+13.3%) | 1.5 -> **1.5** | 118.0 -> **133.8** | Condition triggers excessively (N=1 conditions, Trigger Rate: 92.3% vs 55% ceiling, WR: 47.7%). Compressing spread: b +13.3%, n -21.3% |
