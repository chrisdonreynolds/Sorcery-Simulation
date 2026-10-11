# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T04:08:29Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 480.8s  
**Total Spells Tuned:** 89 / 125  

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
| **Blood** | 14,701 | 54.2% | 54.2% | 35.2 | Overtuned ⚠️ |
| **Ghostfire** | 14,002 | 54.1% | 54.1% | 306.7 | Overtuned ⚠️ |
| **Light** | 6,978 | 53.8% | 53.8% | 61.0 | Overtuned ⚠️ |
| **Dark** | 7,670 | 52.3% | 52.3% | 68.1 | Balanced ✅ |
| **Beasts** | 12,507 | 51.9% | 51.9% | 31.7 | Balanced ✅ |
| **Poison** | 14,640 | 51.7% | 51.7% | 20.1 | Balanced ✅ |
| **Plants** | 14,081 | 51.4% | 51.4% | 7.3 | Balanced ✅ |
| **Earth** | 7,413 | 51.1% | 51.1% | 20.9 | Balanced ✅ |
| **Fire** | 6,209 | 50.8% | 50.8% | 14.8 | Balanced ✅ |
| **Lightning** | 15,331 | 49.6% | 49.6% | 138.8 | Balanced ✅ |
| **Cosmic** | 12,411 | 48.5% | 48.5% | 21.9 | Balanced ✅ |
| **Water** | 6,169 | 47.9% | 47.9% | 136.4 | Balanced ✅ |
| **Ice** | 14,104 | 47.3% | 47.3% | 47.3 | Balanced ✅ |
| **Wind** | 13,516 | 47.0% | 47.0% | 9.4 | Balanced ✅ |
| **Fey** | 12,762 | 45.8% | 45.8% | 3436.0 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 5,826 (49.5%) | 2,972 (45.8%) | 17.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 862 (45.1%) | 2,943 (47.7%) | 5.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,054 (52.6%) | 3,518 (48.3%) | 8.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 6,045 (59.3%) | 7,445 (44.1%) | 5.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 9,355 (49.2%) | 2,600 (49.9%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,873 (51.0%) | 3,719 (43.4%) | 0.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,495 (42.0%) | 2,216 (49.5%) | 5.8% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFD` | Fire | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 3121.3 -> **4046.8** | 1248.9 -> **1214.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.8% vs 30% floor, Casts: 1088). Increasing spread: b -14.5%, n +29.6% |
| `WWF` | Water | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 1289.1 -> **1627.2** | 2064.2 -> **2279.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.9% vs 30% floor, Casts: 1145). Increasing spread: b -12.8%, n +26.2%; Individual spell undertuned (WR: 44.9%, Casts: 1145, mult: 1.017) |
| `WWE` | Water | Setup - Weather | 115.1 -> **121.6** (+5.6%) | - | 115.1 -> **121.6** | Weather 'Raining' appliers undertuned (WR: 42.0%, casts: 1495); Individual spell undertuned (WR: 42.0%, Casts: 1495, mult: 1.028) |
| `EEF` | Earth | Conditional Strike | 65.0 -> **74.8** (+15.1%) | 158.8 -> **197.4** | 10387.0 -> **14840.3** | Status 'Frosty' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.7% vs 30% floor, Casts: 1702). Increasing spread: b -10.9%, n +22.2% |
| `EEW` | Earth | Buff / Sustain | 17.6 -> **17.1** (-2.8%) | - | 17.6 -> **17.1** | Individual spell overtuned (WR: 57.8%, Casts: 1008, mult: 0.973) |
| `LLF` | Light | Conditional Strike | 11.4 -> **12.9** (+13.2%) | 4186.4 -> **5553.3** | 47736.4 -> **71650.5** | Class Light overtuned (WR: 53.8%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.2% vs 30% floor, Casts: 1761). Increasing spread: b -15.9%, n +32.6% |
| `LLW` | Light | Debuff / Control | 260.8 -> **286.3** (+9.8%) | - | 260.8 -> **286.3** | Class Light overtuned (WR: 53.8%, factor: 0.985); Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LLE` | Light | Setup - Weather | 230.0 -> **269.3** (+17.1%) | - | 230.0 -> **269.3** | Class Light overtuned (WR: 53.8%, factor: 0.985); Weather 'Sunny' appliers undertuned (WR: 45.1%, casts: 862) |
| `LLL` | Light | Buff / Sustain | 14.2 -> **13.5** (-4.9%) | - | 14.2 -> **13.5** | Class Light overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 59.6%, Casts: 1075, mult: 0.966) |
| `LLD` | Light | Ultimate | 42.3 -> **41.7** (-1.4%) | 419.0 -> **544.7** | 17766.0 -> **22755.7** | Class Light overtuned (WR: 53.8%, factor: 0.985); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1223). Shifted tuner focus: protected ultimate base floor at 42.3 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 10450.6 -> **14317.3** | 2090.3 -> **2863.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1506). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 44.8%, Casts: 1506, mult: 1.017) |
| `DDW` | Dark | Debuff / Control | 142.7 -> **162.0** (+13.5%) | - | 142.7 -> **162.0** | Buffed setup spell [DDW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 53.9%, Casts: 2314, mult: 0.987) |
| `DDE` | Dark | Setup - Weather | 456.1 -> **489.7** (+7.4%) | - | 456.1 -> **489.7** | Weather 'Darkness' appliers overtuned on own (WR: 59.6%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `DDL` | Dark | Debuff / Control | 60.6 -> **69.7** (+15.0%) | - | 60.6 -> **69.7** | Buffed setup spell [DDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `FWF` | Ghostfire | Debuff / Control | 21.1 -> **20.8** (-1.4%) | - | 21.1 -> **20.8** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983) |
| `FWW` | Ghostfire | Debuff / Control | 180.1 -> **195.5** (+8.6%) | - | 180.1 -> **195.5** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983); Status 'Cursed' appliers overtuned on own (WR: 56.0%) |
| `FWE` | Ghostfire | Setup - Location | 362.6 -> **374.0** (+3.1%) | - | 362.6 -> **374.0** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983); Location 'Graveyard' appliers overtuned on own (WR: 62.6%) |
| `FWL` | Ghostfire | Debuff / Control | 362.3 -> **377.7** (+4.3%) | - | 362.3 -> **377.7** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983); Status 'Cursed' appliers overtuned on own (WR: 56.0%) |
| `FWD` | Ghostfire | Ultimate | 37.6 -> **35.5** (-5.6%) | 568.3 -> **694.3** | 21405.7 -> **24683.1** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983); Status 'Cursed' beneficiaries overtuned (WR: 53.6%) |
| `WFF` | Ghostfire | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 4400.6 -> **5970.4** | 1760.6 -> **1791.4** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983); Status 'Bleeding' beneficiaries undertuned (WR: 44.1%) |
| `WFW` | Ghostfire | Debuff / Control | 17.4 -> **16.7** (-4.0%) | - | 17.4 -> **16.7** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983); Individual spell overtuned (WR: 56.3%, Casts: 1986, mult: 0.979) |
| `WFE` | Ghostfire | Debuff / Control | 11.1 -> **10.1** (-9.0%) | - | 11.1 -> **10.1** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983); Status 'Bleeding' appliers overtuned on own (WR: 59.3%) |
| `WFL` | Ghostfire | Buff / Sustain | 50.3 -> **50.7** (+0.8%) | - | 50.3 -> **50.7** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983); Individual spell undertuned (WR: 42.8%, Casts: 1617, mult: 1.025) |
| `WFD` | Ghostfire | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 1946.0 -> **2535.0** | 1362.9 -> **1521.6** | Class Ghostfire overtuned (WR: 54.1%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 891). Increasing spread: b -14.8%, n +30.3% |
| `FEF` | Beasts | Debuff / Control | 79.7 -> **90.1** (+13.0%) | - | 79.7 -> **90.1** | Buffed setup spell [FEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 55.0%, Casts: 1388, mult: 0.983) |
| `FEW` | Beasts | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 11183.1 -> **15681.3** | 2236.8 -> **3136.5** | Status 'Entangled' beneficiaries undertuned (WR: 43.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 1088). Increasing spread: b -17.8%, n +36.6% |
| `FEE` | Beasts | Buff / Sustain | 39.8 -> **40.3** (+1.3%) | - | 39.8 -> **40.3** | Individual spell undertuned (WR: 46.1%, Casts: 1294, mult: 1.013) |
| `EFF` | Beasts | Debuff / Control | 0.2 -> **0.2** (+0.0%) | 8881.3 -> **12114.8** | 1776.5 -> **2423.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 840). Increasing spread: b -17.7%, n +36.4%; Individual spell overtuned (WR: 56.6%, Casts: 840, mult: 0.977) |
| `EFW` | Beasts | Buff / Sustain | 18.0 -> **17.6** (-2.2%) | - | 18.0 -> **17.6** | Individual spell overtuned (WR: 57.1%, Casts: 1185, mult: 0.976) |
| `EFD` | Beasts | Ultimate | 36.3 -> **36.3** (+0.0%) | 936.3 -> **1248.1** | 34024.0 -> **45342.3** | Status 'Entangled' beneficiaries undertuned (WR: 43.4%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 987). Shifted tuner focus: protected ultimate base floor at 36.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo. |
| `FLF` | Lightning | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 15388.2 -> **21034.4** | 3077.8 -> **4207.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 1356). Increasing spread: b -17.9%, n +36.7%; Individual spell undertuned (WR: 42.8%, Casts: 1356, mult: 1.025) |
| `FLW` | Lightning | Debuff / Control | 200.5 -> **222.1** (+10.8%) | - | 200.5 -> **222.1** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 60.3%, Casts: 1692, mult: 0.963) |
| `FLE` | Lightning | Setup - Weather | 238.6 -> **274.4** (+15.0%) | - | 238.6 -> **274.4** | Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLD` | Lightning | Ultimate | 71.7 -> **69.8** (-2.6%) | 250.3 -> **315.7** | 18018.2 -> **22105.7** | Weather 'Storming' beneficiaries overtuned (WR: 57.5%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1244). Shifted tuner focus: protected ultimate base floor at 71.7 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 6996.9 -> **9374.7** | 2099.4 -> **2812.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.6% vs 30% floor, Casts: 940). Increasing spread: b -16.6%, n +34.0%; Individual spell undertuned (WR: 43.8%, Casts: 940, mult: 1.021) |
| `LFW` | Lightning | Buff / Sustain | 23.8 -> **23.3** (-2.1%) | - | 23.8 -> **23.3** | Individual spell overtuned (WR: 56.0%, Casts: 1003, mult: 0.980) |
| `LFL` | Lightning | Debuff / Control | 68.1 -> **78.3** (+15.0%) | 1939.2 -> **2521.4** | 132127.6 -> **197503.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.4% vs 30% floor, Casts: 2318). Increasing spread: b -14.7%, n +30.0%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 4805.8 -> **6361.3** | 3364.8 -> **3817.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.6% vs 30% floor, Casts: 1512). Increasing spread: b -15.8%, n +32.4%; Individual spell undertuned (WR: 41.9%, Casts: 1512, mult: 1.028) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 10476.7 -> **14353.1** | 2095.5 -> **2870.8** | Class Blood overtuned (WR: 54.2%, factor: 0.983); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1111). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 53.2 -> **53.1** (-0.2%) | - | 53.2 -> **53.1** | Class Blood overtuned (WR: 54.2%, factor: 0.983); Individual spell undertuned (WR: 45.1%, Casts: 1591, mult: 1.016) |
| `FDL` | Blood | Debuff / Control | 4.9 -> **4.4** (-10.2%) | - | 4.9 -> **4.4** | Class Blood overtuned (WR: 54.2%, factor: 0.983); Status 'Bleeding' appliers overtuned on own (WR: 59.3%) |
| `FDD` | Blood | Ultimate | 49.3 -> **47.2** (-4.3%) | 94.8 -> **122.7** | 4722.9 -> **5838.6** | Class Blood overtuned (WR: 54.2%, factor: 0.983); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.5% vs 16% floor, Casts: 1017). Shifted tuner focus: protected ultimate base floor at 49.3 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 3508.8 -> **4749.4** | 702.0 -> **950.1** | Class Blood overtuned (WR: 54.2%, factor: 0.983); Status 'Bleeding' beneficiaries undertuned (WR: 44.1%) |
| `DFE` | Blood | Buff / Sustain | 44.0 -> **43.3** (-1.6%) | - | 44.0 -> **43.3** | Class Blood overtuned (WR: 54.2%, factor: 0.983) |
| `DFL` | Blood | Buff / Sustain | 26.6 -> **26.1** (-1.9%) | - | 26.6 -> **26.1** | Class Blood overtuned (WR: 54.2%, factor: 0.983) |
| `DFD` | Blood | Conditional Strike | 565.4 -> **625.5** (+10.6%) | 0.1 -> **0.1** | 621.9 -> **688.1** | Class Blood overtuned (WR: 54.2%, factor: 0.983); Condition triggers excessively (N=1 conditions, Trigger Rate: 92.7% vs 55% ceiling, WR: 66.4%). Compressing spread: b +19.9%, n -28.0% |
| `WEF` | Plants | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 1922.1 -> **2443.1** | 1346.2 -> **1466.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.9% vs 30% floor, Casts: 1373). Increasing spread: b -13.3%, n +27.1%; Individual spell undertuned (WR: 44.4%, Casts: 1373, mult: 1.019) |
| `WEW` | Plants | Debuff / Control | 1557.9 -> **1791.6** (+15.0%) | - | 1557.9 -> **1791.6** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WED` | Plants | Conditional Strike | 15.7 -> **17.2** (+9.6%) | 32.0 -> **30.1** | 518.1 -> **534.9** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 895, WR: 46.1%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 46.1%, Casts: 895, mult: 1.013) |
| `EWF` | Plants | Buff / Sustain | 0.5 -> **0.4** (-20.0%) | 1435.3 -> **1853.7** | 718.1 -> **741.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.4% vs 30% floor, Casts: 1720). Increasing spread: b -14.2%, n +29.1%; Individual spell undertuned (WR: 45.7%, Casts: 1720, mult: 1.014) |
| `EWD` | Plants | Conditional Strike | 4.7 -> **3.9** (-17.0%) | 8631.3 -> **12042.6** | 40571.8 -> **46970.0** | Status 'Bleeding' appliers overtuned on own (WR: 59.3%); Status 'Entangled' beneficiaries undertuned (WR: 43.4%) |
| `WLF` | Fey | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 4375.6 -> **5564.4** | 3501.3 -> **3895.8** | Class Fey undertuned (WR: 45.8%, factor: 1.017); Status 'Cursed' beneficiaries overtuned (WR: 53.6%) |
| `WLW` | Fey | Debuff / Control | 64.9 -> **65.5** (+0.9%) | - | 64.9 -> **65.5** | Class Fey undertuned (WR: 45.8%, factor: 1.017); Status 'Cursed' appliers overtuned on own (WR: 56.0%) |
| `WLE` | Fey | Setup - Location | 457.6 -> **520.3** (+13.7%) | - | 457.6 -> **520.3** | Class Fey undertuned (WR: 45.8%, factor: 1.017); Location 'Enchanted Forest' appliers overtuned on own (WR: 54.1%) |
| `WLL` | Fey | Direct Damage | 54.7 -> **55.6** (+1.6%) | - | 54.7 -> **55.6** | Class Fey undertuned (WR: 45.8%, factor: 1.017) |
| `WLD` | Fey | Ultimate | 20.0 -> **20.0** (+0.0%) | 3613.2 -> **4823.0** | 72284.0 -> **96480.0** | Class Fey undertuned (WR: 45.8%, factor: 1.017); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.3%) |
| `LWF` | Fey | Debuff / Control | 18.1 -> **22.1** (+22.1%) | 815.4 -> **1046.6** | 14776.8 -> **23152.0** | Class Fey undertuned (WR: 45.8%, factor: 1.017); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.3%) |
| `LWW` | Fey | Debuff / Control | 49.5 -> **50.3** (+1.6%) | - | 49.5 -> **50.3** | Class Fey undertuned (WR: 45.8%, factor: 1.017) |
| `LWL` | Fey | Debuff / Control | 63.3 -> **67.9** (+7.3%) | - | 63.3 -> **67.9** | Class Fey undertuned (WR: 45.8%, factor: 1.017); Individual spell undertuned (WR: 35.3%, Casts: 1529, mult: 1.055) |
| `LWD` | Fey | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 10476.7 -> **14353.1** | 2095.5 -> **2870.8** | Class Fey undertuned (WR: 45.8%, factor: 1.017); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 438). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 9097.2 -> **11990.1** | 7278.6 -> **8393.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 1426). Increasing spread: b -15.5%, n +31.8% |
| `WDW` | Ice | Buff / Sustain | 9.8 -> **9.5** (-3.1%) | - | 9.8 -> **9.5** | Individual spell overtuned (WR: 58.0%, Casts: 1739, mult: 0.972) |
| `WDE` | Ice | Setup - Weather | 40.8 -> **41.6** (+2.0%) | - | 40.8 -> **41.6** | Individual spell undertuned (WR: 44.5%, Casts: 1780, mult: 1.019) |
| `WDD` | Ice | Ultimate | 29.9 -> **29.2** (-2.3%) | 494.2 -> **598.9** | 14806.5 -> **17517.1** | Weather 'Blizzard' beneficiaries overtuned (WR: 56.4%); Location 'Tundra' beneficiaries overtuned (WR: 56.4%) |
| `DWW` | Ice | Debuff / Control | 113.4 -> **130.4** (+15.0%) | - | 113.4 -> **130.4** | Buffed setup spell [DWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DWE` | Ice | Setup - Location | 47.3 -> **51.0** (+7.8%) | - | 47.3 -> **51.0** | Location 'Tundra' appliers undertuned (WR: 39.3%, casts: 2013); Individual spell undertuned (WR: 39.3%, Casts: 2013, mult: 1.039) |
| `DWL` | Ice | Debuff / Control | 41.9 -> **43.0** (+2.6%) | - | 41.9 -> **43.0** | Individual spell undertuned (WR: 42.6%, Casts: 2005, mult: 1.026) |
| `DWD` | Ice | Conditional Strike | 2.4 -> **2.2** (-8.3%) | 436.4 -> **545.4** | 1049.8 -> **1202.1** | Status 'Frosty' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 16.9% vs 30% floor, Casts: 1270). Increasing spread: b -11.2%, n +22.9% |
| `ELF` | Wind | Conditional Strike | 1.3 -> **1.1** (-15.4%) | 3782.3 -> **5080.9** | 4918.3 -> **5590.1** | Status 'Bleeding' beneficiaries undertuned (WR: 44.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.9% vs 30% floor, Casts: 1390). Increasing spread: b -15.2%, n +31.2% |
| `ELW` | Wind | Debuff / Control | 102.2 -> **114.2** (+11.7%) | - | 102.2 -> **114.2** | Buffed setup spell [ELW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 58.2%, Casts: 1535, mult: 0.971) |
| `ELE` | Wind | Setup - Weather | 30.5 -> **30.9** (+1.3%) | - | 30.5 -> **30.9** | Individual spell undertuned (WR: 46.0%, Casts: 1702, mult: 1.013) |
| `ELD` | Wind | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 6910.1 -> **9182.4** | 5528.9 -> **6428.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 790). Increasing spread: b -16.0%, n +32.9% |
| `LEF` | Wind | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 3647.4 -> **4850.4** | 1459.4 -> **1455.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.8% vs 30% floor, Casts: 1285). Increasing spread: b -16.1%, n +33.0% |
| `LEW` | Wind | Debuff / Control | 57.9 -> **58.9** (+1.7%) | - | 57.9 -> **58.9** | Individual spell undertuned (WR: 44.7%, Casts: 1727, mult: 1.018) |
| `LEL` | Wind | Buff / Sustain | 126.0 -> **146.8** (+16.5%) | - | 126.0 -> **146.8** | Buffed setup spell [LEL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell undertuned (WR: 46.0%, Casts: 1498, mult: 1.013) |
| `EDF` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 3231.8 -> **4284.6** | 969.8 -> **1285.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.3% vs 30% floor, Casts: 1581). Increasing spread: b -15.9%, n +32.6% |
| `EDW` | Poison | Debuff / Control | 9.1 -> **8.9** (-2.2%) | - | 9.1 -> **8.9** | Individual spell overtuned (WR: 57.8%, Casts: 1591, mult: 0.973) |
| `EDE` | Poison | Setup - Location | 96.1 -> **102.3** (+6.5%) | - | 96.1 -> **102.3** | Location 'Swamp' appliers undertuned (WR: 41.0%, casts: 812); Individual spell undertuned (WR: 41.0%, Casts: 812, mult: 1.032) |
| `EDD` | Poison | Ultimate | 49.6 -> **54.3** (+9.5%) | 89.8 -> **87.8** | 4503.7 -> **4821.8** | Status 'Bleeding' beneficiaries undertuned (WR: 44.1%); Location 'Swamp' beneficiaries undertuned (WR: 46.1%) |
| `DEF` | Poison | Conditional Strike | 29.7 -> **30.4** (+2.4%) | 1.4 -> **1.4** | 71.3 -> **73.0** | Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 49.0% within [30%-55%] target window, WR: 42.8%).; Individual spell undertuned (WR: 42.8%, Casts: 1575, mult: 1.025) |
| `DEE` | Poison | Debuff / Control | 36.3 -> **41.7** (+14.9%) | - | 36.3 -> **41.7** | Buffed setup spell [DEE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 3599.6 -> **4837.0** | 720.1 -> **967.6** | Status 'Bleeding' beneficiaries undertuned (WR: 44.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.9% vs 30% floor, Casts: 1180). Increasing spread: b -15.3%, n +31.3% |
| `LDF` | Cosmic | Debuff / Control | 130.4 -> **150.0** (+15.0%) | - | 130.4 -> **150.0** | Buffed setup spell [LDF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `LDE` | Cosmic | Setup - Location | 27.3 -> **26.9** (-1.5%) | - | 27.3 -> **26.9** | Individual spell overtuned (WR: 54.8%, Casts: 928, mult: 0.984) |
| `LDL` | Cosmic | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 5423.6 -> **7346.3** | 2169.8 -> **2204.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 1024). Increasing spread: b -17.3%, n +35.4%; Individual spell overtuned (WR: 55.1%, Casts: 1024, mult: 0.983) |
| `LDD` | Cosmic | Ultimate | 127.7 -> **127.7** (+0.0%) | 19.5 -> **25.4** | 2617.8 -> **3371.3** | Ultimate payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1542). Shifted tuner focus: protected ultimate base floor at 127.7 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDW, DDL, DEE, DFW, DWW, ELW, LEL, DLL, FEF, LWF) with +15% b tempo. |
| `DLF` | Cosmic | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 3893.8 -> **5066.2** | 1557.9 -> **2026.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.3% vs 30% floor, Casts: 1415). Increasing spread: b -14.7%, n +30.1%; Individual spell undertuned (WR: 38.9%, Casts: 1415, mult: 1.040) |
| `DLW` | Cosmic | Direct Damage | 55.5 -> **56.7** (+2.2%) | - | 55.5 -> **56.7** | Individual spell undertuned (WR: 43.4%, Casts: 888, mult: 1.022) |
| `DLL` | Cosmic | Conditional Strike | 1.7 -> **1.5** (-11.8%) | 1607.8 -> **2100.1** | 2735.0 -> **3151.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.7% vs 30% floor, Casts: 1280). Increasing spread: b -14.9%, n +30.6%; Individual spell undertuned (WR: 41.7%, Casts: 1280, mult: 1.029) |
