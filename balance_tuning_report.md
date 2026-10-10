# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T20:59:47Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 485.4s  
**Total Spells Tuned:** 74 / 125  

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
| **Poison** | 18,117 | 56.2% | 56.3% | 10.2 | Overtuned ⚠️ |
| **Beasts** | 17,707 | 52.5% | 52.6% | 7.8 | Balanced ✅ |
| **Blood** | 19,277 | 52.1% | 52.1% | 12.3 | Balanced ✅ |
| **Water** | 7,344 | 51.0% | 51.0% | 8.0 | Balanced ✅ |
| **Light** | 16,376 | 50.8% | 50.8% | 4.5 | Balanced ✅ |
| **Ghostfire** | 23,035 | 50.6% | 50.6% | 12.2 | Balanced ✅ |
| **Earth** | 8,316 | 50.5% | 50.5% | 15.8 | Balanced ✅ |
| **Plants** | 20,439 | 49.9% | 49.9% | 9.5 | Balanced ✅ |
| **Fire** | 6,913 | 49.0% | 49.0% | 15.3 | Balanced ✅ |
| **Ice** | 17,513 | 48.9% | 48.9% | 10.8 | Balanced ✅ |
| **Dark** | 15,532 | 48.8% | 48.8% | 9.3 | Balanced ✅ |
| **Wind** | 13,964 | 48.7% | 48.7% | 8.5 | Balanced ✅ |
| **Lightning** | 19,156 | 47.9% | 47.9% | 10.6 | Balanced ✅ |
| **Cosmic** | 15,096 | 47.5% | 47.5% | 14.5 | Balanced ✅ |
| **Fey** | 15,863 | 46.9% | 46.9% | 9.9 | Balanced ✅ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,286 (50.3%) | 3,539 (49.2%) | 31.4% | Healthy ✅ |
| **Sunny** (weather) | 3,420 (50.2%) | 2,397 (48.1%) | 8.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,113 (50.6%) | 3,841 (48.5%) | 10.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 11,685 (56.8%) | 6,671 (48.6%) | 9.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 11,918 (49.5%) | 3,027 (44.8%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,567 (50.4%) | 6,072 (47.7%) | 1.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,609 (49.7%) | 4,794 (49.0%) | 6.7% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 47.9 -> **48.5** (+1.3%) | - | 47.9 -> **48.5** | Individual spell undertuned (WR: 46.2%, Casts: 1261, mult: 1.012) |
| `FFD` | Fire | Conditional Strike | 18.9 -> **16.4** (-13.2%) | 3.8 -> **4.8** | 90.7 -> **95.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.2% vs 30% floor, Casts: 1383). Increasing spread: b -13.1%, n +26.8% |
| `WWF` | Water | Conditional Strike | 31.7 -> **27.4** (-13.6%) | 3.7 -> **4.6** | 149.0 -> **153.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.1% vs 30% floor, Casts: 1132). Increasing spread: b -12.4%, n +25.3%; Individual spell overtuned (WR: 53.8%, Casts: 1132, mult: 0.987) |
| `EEW` | Earth | Buff / Sustain | 36.4 -> **35.7** (-1.9%) | - | 36.4 -> **35.7** | Individual spell overtuned (WR: 55.8%, Casts: 1218, mult: 0.980) |
| `EEE` | Earth | Conditional Strike | 4.8 -> **5.5** (+14.6%) | 1.6 -> **1.5** | 12.5 -> **13.8** | Condition triggers excessively (N=1 conditions, Trigger Rate: 94.6% vs 55% ceiling, WR: 48.9%). Compressing spread: b +13.8%, n -22.1% |
| `LLF` | Light | Conditional Strike | 3.5 -> **3.0** (-14.3%) | 3.7 -> **4.8** | 16.4 -> **17.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.5% vs 30% floor, Casts: 3360). Increasing spread: b -14.2%, n +29.1% |
| `LLW` | Light | Debuff / Control | 28.7 -> **33.0** (+15.0%) | - | 28.7 -> **33.0** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LLL` | Light | Buff / Sustain | 33.1 -> **32.5** (-1.8%) | - | 33.1 -> **32.5** | Individual spell overtuned (WR: 55.3%, Casts: 3022, mult: 0.982) |
| `LLD` | Light | Ultimate | 25.0 -> **27.0** (+8.0%) | 6.5 -> **6.1** | 187.5 -> **191.7** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 1117, WR: 48.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 17.7 -> **14.5** (-18.1%) | 4.0 -> **5.5** | 88.5 -> **94.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3015). Increasing spread: b -18.0%, n +37.0% |
| `DDE` | Dark | Setup - Weather | 21.2 -> **25.0** (+17.9%) | - | 21.2 -> **25.0** | Weather 'Darkness' appliers undertuned (WR: 46.1%, casts: 5977); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `DDD` | Dark | Debuff / Control | 34.3 -> **33.9** (-1.2%) | - | 34.3 -> **33.9** | Individual spell overtuned (WR: 53.8%, Casts: 1602, mult: 0.988) |
| `FWW` | Ghostfire | Debuff / Control | 15.0 -> **17.2** (+14.7%) | - | 15.0 -> **17.2** | Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 22.0 -> **25.3** (+15.0%) | - | 22.0 -> **25.3** | Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 45.0 -> **51.7** (+14.9%) | - | 45.0 -> **51.7** | Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 25.5 -> **25.5** (+0.0%) | 6.8 -> **8.8** | 198.9 -> **249.9** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.5% vs 8% floor, Casts: 1501). Shifted tuner focus: protected ultimate base floor at 25.5 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 18.9 -> **16.3** (-13.8%) | 3.7 -> **4.8** | 88.8 -> **94.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.3% vs 30% floor, Casts: 1540). Increasing spread: b -13.9%, n +28.4% |
| `WFE` | Ghostfire | Debuff / Control | 41.6 -> **39.2** (-5.8%) | - | 41.6 -> **39.2** | Status 'Bleeding' appliers overtuned on own (WR: 56.8%); Individual spell overtuned (WR: 59.7%, Casts: 1261, mult: 0.965) |
| `WFD` | Ghostfire | Conditional Strike | 19.7 -> **17.1** (-13.2%) | 3.6 -> **4.6** | 90.6 -> **95.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.0% vs 30% floor, Casts: 1505). Increasing spread: b -13.2%, n +27.0% |
| `FEW` | Beasts | Conditional Strike | 18.0 -> **14.9** (-17.2%) | 4.0 -> **5.4** | 90.0 -> **95.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.1% vs 30% floor, Casts: 1063). Increasing spread: b -17.2%, n +35.3% |
| `FED` | Beasts | Conditional Strike | 6.0 -> **6.4** (+6.7%) | 2.0 -> **1.8** | 18.0 -> **17.9** | Condition triggers excessively (N=1 conditions, Trigger Rate: 65.1% vs 55% ceiling, WR: 50.9%). Compressing spread: b +7.2%, n -11.6% |
| `EFF` | Beasts | Debuff / Control | 21.9 -> **18.2** (-16.9%) | 4.0 -> **5.4** | 109.5 -> **116.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.4% vs 30% floor, Casts: 2153). Increasing spread: b -17.1%, n +35.0% |
| `EFW` | Beasts | Buff / Sustain | 23.5 -> **23.1** (-1.7%) | - | 23.5 -> **23.1** | Individual spell overtuned (WR: 55.6%, Casts: 906, mult: 0.981) |
| `EFL` | Beasts | Buff / Sustain | 29.3 -> **25.4** (-13.3%) | - | 29.3 -> **25.4** | Individual spell overtuned (WR: 83.2%, Casts: 1026, mult: 0.866) |
| `EFD` | Beasts | Ultimate | 22.3 -> **22.3** (+0.0%) | 9.1 -> **11.8** | 225.2 -> **285.4** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.7% vs 16% floor, Casts: 1460). Shifted tuner focus: protected ultimate base floor at 22.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo. |
| `FLF` | Lightning | Conditional Strike | 18.0 -> **14.8** (-17.8%) | 4.0 -> **5.6** | 90.0 -> **97.7** | Status 'Stunned' beneficiaries undertuned (WR: 44.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.3% vs 30% floor, Casts: 1391). Increasing spread: b -17.9%, n +36.8% |
| `FLE` | Lightning | Setup - Weather | 25.8 -> **26.9** (+4.3%) | - | 25.8 -> **26.9** | Weather 'Storming' appliers undertuned (WR: 44.1%, casts: 2613); Individual spell undertuned (WR: 44.1%, Casts: 2613, mult: 1.020) |
| `FLD` | Lightning | Ultimate | 23.7 -> **26.3** (+11.0%) | 9.6 -> **9.5** | 251.2 -> **276.2** | Status 'Stunned' beneficiaries undertuned (WR: 44.8%); Weather 'Storming' beneficiaries undertuned (WR: 41.8%) |
| `LFF` | Lightning | Conditional Strike | 18.2 -> **15.4** (-15.4%) | 4.0 -> **5.3** | 91.0 -> **97.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 1520). Increasing spread: b -15.4%, n +31.7% |
| `LFL` | Lightning | Debuff / Control | 42.9 -> **50.2** (+17.0%) | 4.0 -> **4.7** | 214.5 -> **286.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 22.2% vs 30% floor, Casts: 1308). Increasing spread: b -9.1%, n +18.5%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 19.7 -> **17.2** (-12.7%) | 5.6 -> **7.2** | 130.0 -> **141.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.1% vs 30% floor, Casts: 1335). Increasing spread: b -14.4%, n +29.4%; Individual spell undertuned (WR: 44.6%, Casts: 1335, mult: 1.018) |
| `FDF` | Blood | Conditional Strike | 17.5 -> **14.8** (-15.4%) | 4.0 -> **5.5** | 87.5 -> **96.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1786). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 42.0%, Casts: 1786, mult: 1.028) |
| `FDL` | Blood | Debuff / Control | 38.4 -> **35.9** (-6.5%) | - | 38.4 -> **35.9** | Status 'Bleeding' appliers overtuned on own (WR: 56.8%); Individual spell overtuned (WR: 61.4%, Casts: 3013, mult: 0.959) |
| `FDD` | Blood | Ultimate | 24.7 -> **24.7** (+0.0%) | 7.0 -> **8.9** | 197.6 -> **244.5** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 1.9% vs 16% floor, Casts: 1369). Shifted tuner focus: protected ultimate base floor at 24.7 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 18.7 -> **16.1** (-13.9%) | 3.7 -> **4.7** | 87.9 -> **91.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.8% vs 30% floor, Casts: 1599). Increasing spread: b -13.7%, n +28.0% |
| `DFW` | Blood | Debuff / Control | 34.7 -> **32.4** (-6.6%) | - | 34.7 -> **32.4** | Status 'Bleeding' appliers overtuned on own (WR: 56.8%); Individual spell overtuned (WR: 61.9%, Casts: 3862, mult: 0.957) |
| `DFE` | Blood | Buff / Sustain | 35.0 -> **35.6** (+1.7%) | - | 35.0 -> **35.6** | Individual spell undertuned (WR: 44.6%, Casts: 1453, mult: 1.018) |
| `DFD` | Blood | Conditional Strike | 31.8 -> **36.2** (+13.8%) | 1.4 -> **1.1** | 76.3 -> **76.0** | Condition triggers excessively (N=1 conditions, Trigger Rate: 94.5% vs 55% ceiling, WR: 48.5%). Compressing spread: b +13.8%, n -22.1% |
| `WEF` | Plants | Conditional Strike | 20.1 -> **17.9** (-10.9%) | 3.4 -> **4.2** | 88.4 -> **93.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.0% vs 30% floor, Casts: 1491). Increasing spread: b -11.2%, n +22.8% |
| `WEW` | Plants | Debuff / Control | 36.0 -> **41.4** (+15.0%) | - | 36.0 -> **41.4** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WED` | Plants | Conditional Strike | 17.8 -> **15.1** (-15.2%) | 5.9 -> **7.7** | 122.8 -> **131.4** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 2.0% vs 8% floor, Casts: 1265). Increasing spread: b -15.0%, n +30.8% |
| `EWF` | Plants | Buff / Sustain | 23.5 -> **20.7** (-11.9%) | 3.5 -> **4.3** | 105.8 -> **109.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.4% vs 30% floor, Casts: 1280). Increasing spread: b -11.8%, n +24.2% |
| `EWW` | Plants | Debuff / Control | 38.2 -> **33.5** (-12.3%) | - | 38.2 -> **33.5** | Individual spell overtuned (WR: 80.9%, Casts: 1352, mult: 0.876) |
| `EWL` | Plants | Debuff / Control | 59.2 -> **60.0** (+1.4%) | - | 59.2 -> **60.0** | Individual spell undertuned (WR: 45.9%, Casts: 2966, mult: 1.014) |
| `EWD` | Plants | Conditional Strike | 17.6 -> **14.4** (-18.2%) | 4.0 -> **5.4** | 88.0 -> **92.2** | Status 'Bleeding' appliers overtuned on own (WR: 56.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 3549). Increasing spread: b -17.1%, n +35.2% |
| `WLF` | Fey | Conditional Strike | 18.2 -> **15.7** (-13.7%) | 3.8 -> **4.9** | 87.4 -> **92.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.1% vs 30% floor, Casts: 1618). Increasing spread: b -13.9%, n +28.5% |
| `WLE` | Fey | Setup - Location | 20.6 -> **24.8** (+20.4%) | - | 20.6 -> **24.8** | Location 'Enchanted Forest' appliers undertuned (WR: 43.6%, casts: 2477); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLD` | Fey | Ultimate | 25.7 -> **25.7** (+0.0%) | 7.0 -> **9.1** | 205.6 -> **259.6** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1549). Shifted tuner focus: protected ultimate base floor at 25.7 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 42.0 -> **37.0** (-11.9%) | 3.4 -> **4.2** | 184.8 -> **192.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.5% vs 30% floor, Casts: 2350). Increasing spread: b -11.8%, n +24.1% |
| `LWL` | Fey | Debuff / Control | 34.8 -> **35.2** (+1.1%) | - | 34.8 -> **35.2** | Individual spell undertuned (WR: 46.2%, Casts: 940, mult: 1.012) |
| `LWD` | Fey | Conditional Strike | 18.1 -> **15.2** (-16.0%) | 4.0 -> **5.5** | 90.5 -> **98.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1685). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 43.0%, Casts: 1685, mult: 1.024) |
| `WDF` | Ice | Conditional Strike | 18.7 -> **15.7** (-16.0%) | 3.9 -> **5.2** | 91.6 -> **97.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 1585). Increasing spread: b -15.8%, n +32.4% |
| `WDW` | Ice | Buff / Sustain | 14.4 -> **14.2** (-1.4%) | - | 14.4 -> **14.2** | Individual spell overtuned (WR: 55.0%, Casts: 1560, mult: 0.983) |
| `WDD` | Ice | Ultimate | 25.2 -> **27.6** (+9.5%) | 6.7 -> **6.5** | 194.0 -> **207.0** | Weather 'Blizzard' beneficiaries undertuned (WR: 45.3%); Location 'Tundra' beneficiaries undertuned (WR: 45.3%) |
| `ELF` | Wind | Conditional Strike | 39.8 -> **34.5** (-13.3%) | 3.8 -> **4.8** | 191.0 -> **200.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.5% vs 30% floor, Casts: 1081). Increasing spread: b -13.4%, n +27.4% |
| `ELW` | Wind | Debuff / Control | 39.8 -> **40.5** (+1.8%) | - | 39.8 -> **40.5** | Individual spell undertuned (WR: 44.5%, Casts: 1149, mult: 1.018) |
| `ELD` | Wind | Conditional Strike | 20.1 -> **17.1** (-14.9%) | 3.6 -> **4.7** | 92.5 -> **97.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.2% vs 30% floor, Casts: 3209). Increasing spread: b -15.1%, n +31.0% |
| `LEF` | Wind | Conditional Strike | 18.2 -> **15.6** (-14.3%) | 4.0 -> **5.3** | 91.0 -> **98.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.3% vs 30% floor, Casts: 1326). Increasing spread: b -15.5%, n +31.8%; Individual spell undertuned (WR: 44.9%, Casts: 1326, mult: 1.017) |
| `EDF` | Poison | Conditional Strike | 18.7 -> **15.3** (-18.2%) | 3.6 -> **4.8** | 86.0 -> **88.7** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.3% vs 30% floor, Casts: 2442). Increasing spread: b -16.3%, n +33.4% |
| `EDW` | Poison | Debuff / Control | 33.0 -> **32.2** (-2.4%) | - | 33.0 -> **32.2** | Class Poison overtuned (WR: 56.2%, factor: 0.975) |
| `EDE` | Poison | Setup - Location | 19.4 -> **18.9** (-2.6%) | - | 19.4 -> **18.9** | Class Poison overtuned (WR: 56.2%, factor: 0.975) |
| `EDL` | Poison | Debuff / Control | 19.7 -> **16.8** (-14.7%) | - | 19.7 -> **16.8** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 80.9%, Casts: 3611, mult: 0.876) |
| `EDD` | Poison | Ultimate | 25.5 -> **27.2** (+6.7%) | 7.0 -> **6.7** | 204.0 -> **209.4** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Location 'Swamp' beneficiaries undertuned (WR: 46.3%) |
| `DEF` | Poison | Conditional Strike | 34.8 -> **36.1** (+3.7%) | 2.1 -> **1.9** | 107.9 -> **104.7** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Condition triggers excessively (N=1 conditions, Trigger Rate: 61.2% vs 55% ceiling, WR: 51.5%). Compressing spread: b +6.4%, n -10.2% |
| `DEW` | Poison | Debuff / Control | 32.9 -> **31.4** (-4.6%) | - | 32.9 -> **31.4** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 55.9%, Casts: 1452, mult: 0.980) |
| `DEE` | Poison | Debuff / Control | 27.9 -> **27.2** (-2.5%) | - | 27.9 -> **27.2** | Class Poison overtuned (WR: 56.2%, factor: 0.975) |
| `DEL` | Poison | Conditional Strike | 1.9 -> **1.6** (-15.8%) | 3.7 -> **4.7** | 8.9 -> **9.1** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.7% vs 30% floor, Casts: 1157). Increasing spread: b -13.7%, n +28.1% |
| `DED` | Poison | Debuff / Control | 28.0 -> **27.3** (-2.5%) | - | 28.0 -> **27.3** | Class Poison overtuned (WR: 56.2%, factor: 0.975) |
| `LDE` | Cosmic | Setup - Location | 20.5 -> **20.9** (+2.0%) | - | 20.5 -> **20.9** | Individual spell undertuned (WR: 43.8%, Casts: 1147, mult: 1.021) |
| `LDL` | Cosmic | Conditional Strike | 19.4 -> **16.6** (-14.4%) | 3.8 -> **4.9** | 93.1 -> **97.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 1361). Increasing spread: b -14.5%, n +29.7% |
| `LDD` | Cosmic | Ultimate | 24.4 -> **26.4** (+8.2%) | 9.4 -> **8.8** | 253.8 -> **258.7** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1566, WR: 46.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 22.9 -> **19.9** (-13.1%) | 3.8 -> **4.9** | 109.9 -> **117.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.2% vs 30% floor, Casts: 2459). Increasing spread: b -14.3%, n +29.3%; Individual spell undertuned (WR: 45.8%, Casts: 2459, mult: 1.014) |
| `DLL` | Cosmic | Conditional Strike | 38.2 -> **34.6** (-9.4%) | 2.9 -> **3.5** | 149.0 -> **155.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 21.2% vs 30% floor, Casts: 2194). Increasing spread: b -9.5%, n +19.3% |
| `DLD` | Cosmic | Conditional Strike | 41.6 -> **47.2** (+13.5%) | 1.5 -> **1.5** | 104.0 -> **118.0** | Condition triggers excessively (N=1 conditions, Trigger Rate: 92.5% vs 55% ceiling, WR: 49.1%). Compressing spread: b +13.3%, n -21.3% |
