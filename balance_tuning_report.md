# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T00:49:30Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 492.9s  
**Total Spells Tuned:** 99 / 125  

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
| **Blood** | 19,274 | 58.0% | 58.1% | 18.8 | Overtuned ⚠️ |
| **Light** | 10,230 | 53.5% | 53.6% | 11.4 | Overtuned ⚠️ |
| **Poison** | 20,057 | 52.5% | 52.5% | 8.7 | Balanced ✅ |
| **Beasts** | 21,164 | 52.5% | 52.5% | 10.6 | Balanced ✅ |
| **Earth** | 10,496 | 52.1% | 52.1% | 16.9 | Balanced ✅ |
| **Ghostfire** | 19,829 | 50.6% | 50.6% | 17.5 | Balanced ✅ |
| **Plants** | 20,151 | 50.4% | 50.4% | 7.9 | Balanced ✅ |
| **Dark** | 10,056 | 50.0% | 50.0% | 14.9 | Balanced ✅ |
| **Water** | 9,725 | 49.5% | 49.5% | 10.4 | Balanced ✅ |
| **Wind** | 19,986 | 49.4% | 49.4% | 7.4 | Balanced ✅ |
| **Fire** | 9,932 | 48.9% | 48.9% | 16.0 | Balanced ✅ |
| **Lightning** | 21,965 | 48.0% | 48.0% | 11.9 | Balanced ✅ |
| **Cosmic** | 18,371 | 46.9% | 46.9% | 15.2 | Balanced ✅ |
| **Fey** | 18,087 | 46.7% | 46.7% | 22.2 | Balanced ✅ |
| **Ice** | 20,150 | 45.6% | 45.6% | 13.3 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,906 (52.4%) | 3,480 (46.7%) | 21.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,934 (48.1%) | 4,670 (51.9%) | 9.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 6,079 (52.8%) | 4,649 (49.5%) | 10.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,413 (65.6%) | 8,585 (47.1%) | 6.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,756 (44.3%) | 4,913 (43.5%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,770 (64.6%) | 8,409 (49.8%) | 1.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,913 (40.4%) | 5,538 (37.2%) | 5.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFE` | Fire | Debuff / Control | 33.9 -> **34.4** (+1.5%) | - | 33.9 -> **34.4** | Individual spell undertuned (WR: 45.5%, Casts: 2494, mult: 1.015) |
| `FFD` | Fire | Conditional Strike | 2.6 -> **2.3** (-11.5%) | 110.6 -> **143.7** | 290.2 -> **332.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.5% vs 30% floor, Casts: 1384). Increasing spread: b -14.6%, n +30.0%; Individual spell undertuned (WR: 44.3%, Casts: 1384, mult: 1.019) |
| `WWF` | Water | Conditional Strike | 6.3 -> **5.5** (-12.7%) | 68.0 -> **84.2** | 434.7 -> **468.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.9% vs 30% floor, Casts: 1406). Increasing spread: b -11.7%, n +23.8%; Individual spell overtuned (WR: 54.9%, Casts: 1406, mult: 0.984) |
| `WWE` | Water | Setup - Weather | 47.1 -> **50.4** (+7.0%) | - | 47.1 -> **50.4** | Weather 'Raining' appliers undertuned (WR: 40.4%, casts: 1913); Individual spell undertuned (WR: 40.4%, Casts: 1913, mult: 1.034) |
| `WWD` | Water | Buff / Sustain | 50.2 -> **49.1** (-2.2%) | - | 50.2 -> **49.1** | Individual spell overtuned (WR: 56.2%, Casts: 1668, mult: 0.979) |
| `EEF` | Earth | Conditional Strike | 13.5 -> **15.8** (+17.0%) | 20.5 -> **23.6** | 290.2 -> **388.7** | Status 'Stunned' appliers undertuned (WR: 44.3%, casts: 14756); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 26.1% vs 30% floor, Casts: 1611). Increasing spread: b -7.5%, n +15.2% |
| `EEW` | Earth | Buff / Sustain | 26.8 -> **25.3** (-5.6%) | - | 26.8 -> **25.3** | Individual spell overtuned (WR: 65.4%, Casts: 1754, mult: 0.943) |
| `LLF` | Light | Conditional Strike | 5.6 -> **6.3** (+12.5%) | 139.6 -> **185.0** | 787.4 -> **1171.8** | Class Light overtuned (WR: 53.5%, factor: 0.986); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.3% vs 30% floor, Casts: 3278). Increasing spread: b -15.9%, n +32.6% |
| `LLW` | Light | Debuff / Control | 62.1 -> **69.2** (+11.4%) | - | 62.1 -> **69.2** | Class Light overtuned (WR: 53.5%, factor: 0.986); Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LLE` | Light | Setup - Weather | 94.4 -> **107.0** (+13.3%) | - | 94.4 -> **107.0** | Class Light overtuned (WR: 53.5%, factor: 0.986); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 21.5 -> **20.6** (-4.2%) | - | 21.5 -> **20.6** | Class Light overtuned (WR: 53.5%, factor: 0.986); Individual spell overtuned (WR: 57.5%, Casts: 1246, mult: 0.974) |
| `LLD` | Light | Ultimate | 34.3 -> **33.3** (-2.9%) | 45.1 -> **58.6** | 1581.2 -> **1984.7** | Class Light overtuned (WR: 53.5%, factor: 0.986); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1683). Shifted tuner focus: protected ultimate base floor at 34.3 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 239.1 -> **327.6** | 336.1 -> **394.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1945). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 38.4%, Casts: 1945, mult: 1.042) |
| `DDW` | Dark | Debuff / Control | 73.1 -> **84.1** (+15.0%) | - | 73.1 -> **84.1** | Buffed setup spell [DDW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DDE` | Dark | Setup - Weather | 96.9 -> **111.4** (+15.0%) | - | 96.9 -> **111.4** | Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD]; Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 35.2 -> **40.5** (+15.1%) | - | 35.2 -> **40.5** | Buffed setup spell [DDL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DDD` | Dark | Debuff / Control | 23.0 -> **22.1** (-3.9%) | - | 23.0 -> **22.1** | Individual spell overtuned (WR: 61.1%, Casts: 1503, mult: 0.960) |
| `FWF` | Ghostfire | Debuff / Control | 25.3 -> **24.7** (-2.4%) | - | 25.3 -> **24.7** | Individual spell overtuned (WR: 57.3%, Casts: 2015, mult: 0.975) |
| `FWW` | Ghostfire | Debuff / Control | 47.0 -> **47.8** (+1.7%) | - | 47.0 -> **47.8** | Individual spell undertuned (WR: 44.9%, Casts: 1482, mult: 1.017) |
| `FWE` | Ghostfire | Setup - Location | 115.5 -> **124.9** (+8.1%) | - | 115.5 -> **124.9** | Location 'Graveyard' appliers undertuned (WR: 38.8%, casts: 1943); Individual spell undertuned (WR: 38.8%, Casts: 1943, mult: 1.041) |
| `FWD` | Ghostfire | Ultimate | 47.0 -> **50.8** (+8.1%) | 42.2 -> **41.0** | 2030.4 -> **2133.6** | Status 'Cursed' beneficiaries undertuned (WR: 41.5%); Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 1811, WR: 48.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `WFF` | Ghostfire | Conditional Strike | 2.5 -> **2.1** (-16.0%) | 121.8 -> **163.4** | 307.0 -> **345.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.5% vs 30% floor, Casts: 1561). Increasing spread: b -16.6%, n +34.1%; Individual spell undertuned (WR: 45.5%, Casts: 1561, mult: 1.015) |
| `WFW` | Ghostfire | Debuff / Control | 26.3 -> **25.9** (-1.5%) | - | 26.3 -> **25.9** | Individual spell overtuned (WR: 54.9%, Casts: 2820, mult: 0.984) |
| `WFE` | Ghostfire | Debuff / Control | 20.0 -> **17.3** (-13.5%) | - | 20.0 -> **17.3** | Status 'Bleeding' appliers overtuned on own (WR: 65.6%); Individual spell overtuned (WR: 71.6%, Casts: 1631, mult: 0.916) |
| `WFD` | Ghostfire | Conditional Strike | 3.3 -> **2.9** (-12.1%) | 101.6 -> **129.6** | 338.6 -> **378.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.3% vs 30% floor, Casts: 1994). Increasing spread: b -13.5%, n +27.6%; Individual spell undertuned (WR: 40.8%, Casts: 1994, mult: 1.033) |
| `FEF` | Beasts | Debuff / Control | 41.2 -> **47.4** (+15.0%) | - | 41.2 -> **47.4** | Buffed setup spell [FEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `FEW` | Beasts | Conditional Strike | 1.6 -> **1.3** (-18.8%) | 242.8 -> **330.5** | 390.1 -> **430.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.1% vs 30% floor, Casts: 1940). Increasing spread: b -17.6%, n +36.1%; Individual spell undertuned (WR: 43.4%, Casts: 1940, mult: 1.022) |
| `FEE` | Beasts | Buff / Sustain | 30.8 -> **31.2** (+1.3%) | - | 30.8 -> **31.2** | Individual spell undertuned (WR: 45.9%, Casts: 2145, mult: 1.014) |
| `EFF` | Beasts | Debuff / Control | 1.8 -> **1.5** (-16.7%) | 214.2 -> **293.1** | 387.4 -> **441.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 1796). Increasing spread: b -17.9%, n +36.8% |
| `EFW` | Beasts | Buff / Sustain | 22.5 -> **22.2** (-1.3%) | - | 22.5 -> **22.2** | Individual spell overtuned (WR: 54.1%, Casts: 1664, mult: 0.987) |
| `EFL` | Beasts | Buff / Sustain | 3.8 -> **3.2** (-15.8%) | - | 3.8 -> **3.2** | Individual spell overtuned (WR: 86.8%, Casts: 1417, mult: 0.850) |
| `EFD` | Beasts | Ultimate | 34.7 -> **33.7** (-2.9%) | 63.1 -> **81.9** | 2224.3 -> **2793.7** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 3388). Shifted tuner focus: protected ultimate base floor at 34.7 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo.; Individual spell overtuned (WR: 58.1%, Casts: 3388, mult: 0.972) |
| `FLF` | Lightning | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 298.9 -> **418.8** | 479.8 -> **587.7** | Status 'Stunned' beneficiaries undertuned (WR: 43.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 2984). Increasing spread: b -17.8%, n +36.6% |
| `FLW` | Lightning | Debuff / Control | 60.2 -> **68.9** (+14.5%) | - | 60.2 -> **68.9** | Status 'Stunned' appliers undertuned (WR: 44.3%, casts: 14756); Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLE` | Lightning | Setup - Weather | 39.1 -> **45.0** (+15.1%) | - | 39.1 -> **45.0** | Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLD` | Lightning | Ultimate | 82.1 -> **82.1** (+0.0%) | 10.4 -> **13.9** | 935.9 -> **1223.3** | Status 'Stunned' beneficiaries undertuned (WR: 43.5%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1929). Shifted tuner focus: protected ultimate base floor at 82.1 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 1.8 -> **1.5** (-16.7%) | 195.0 -> **263.9** | 352.8 -> **397.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.0% vs 30% floor, Casts: 1506). Increasing spread: b -17.2%, n +35.3%; Individual spell undertuned (WR: 42.2%, Casts: 1506, mult: 1.027) |
| `LFW` | Lightning | Buff / Sustain | 30.0 -> **29.3** (-2.3%) | - | 30.0 -> **29.3** | Individual spell overtuned (WR: 57.1%, Casts: 2265, mult: 0.976) |
| `LFE` | Lightning | Debuff / Control | 52.3 -> **54.1** (+3.4%) | - | 52.3 -> **54.1** | Status 'Stunned' appliers undertuned (WR: 44.3%, casts: 14756); Individual spell undertuned (WR: 45.9%, Casts: 2482, mult: 1.014) |
| `LFL` | Lightning | Debuff / Control | 28.2 -> **31.8** (+12.8%) | 87.7 -> **112.0** | 2501.3 -> **3593.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.1% vs 30% floor, Casts: 2847). Increasing spread: b -13.5%, n +27.7%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 4.5 -> **4.0** (-11.1%) | 148.6 -> **195.5** | 673.2 -> **786.0** | Status 'Stunned' appliers undertuned (WR: 44.3%, casts: 14756); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.5% vs 30% floor, Casts: 2806). Increasing spread: b -15.4%, n +31.6% |
| `FDF` | Blood | Conditional Strike | 1.5 -> **1.2** (-20.0%) | 239.6 -> **328.3** | 360.9 -> **395.2** | Class Blood overtuned (WR: 58.0%, factor: 0.968); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1271). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 70.3 -> **68.9** (-2.0%) | - | 70.3 -> **68.9** | Class Blood overtuned (WR: 58.0%, factor: 0.968); Individual spell undertuned (WR: 46.1%, Casts: 1711, mult: 1.013) |
| `FDE` | Blood | Setup - Weather | 21.0 -> **20.3** (-3.3%) | - | 21.0 -> **20.3** | Class Blood overtuned (WR: 58.0%, factor: 0.968) |
| `FDL` | Blood | Debuff / Control | 13.2 -> **10.9** (-17.4%) | - | 13.2 -> **10.9** | Class Blood overtuned (WR: 58.0%, factor: 0.968); Status 'Bleeding' appliers overtuned on own (WR: 65.6%) |
| `FDD` | Blood | Ultimate | 56.4 -> **54.6** (-3.2%) | 8.0 -> **10.3** | 507.6 -> **617.0** | Class Blood overtuned (WR: 58.0%, factor: 0.968); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.7% vs 16% floor, Casts: 1650). Shifted tuner focus: protected ultimate base floor at 56.4 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 2.1 -> **1.7** (-19.0%) | 119.2 -> **155.5** | 252.4 -> **266.1** | Class Blood overtuned (WR: 58.0%, factor: 0.968); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 1965). Increasing spread: b -14.9%, n +30.5% |
| `DFW` | Blood | Debuff / Control | 16.4 -> **15.6** (-4.9%) | - | 16.4 -> **15.6** | Class Blood overtuned (WR: 58.0%, factor: 0.968); Status 'Bleeding' appliers overtuned on own (WR: 65.6%) |
| `DFE` | Blood | Buff / Sustain | 43.6 -> **42.2** (-3.2%) | - | 43.6 -> **42.2** | Class Blood overtuned (WR: 58.0%, factor: 0.968) |
| `DFL` | Blood | Buff / Sustain | 33.8 -> **33.1** (-2.1%) | - | 33.8 -> **33.1** | Class Blood overtuned (WR: 58.0%, factor: 0.968); Individual spell undertuned (WR: 46.2%, Casts: 1288, mult: 1.012) |
| `DFD` | Blood | Conditional Strike | 160.6 -> **177.6** (+10.6%) | 0.1 -> **0.1** | 176.7 -> **195.4** | Class Blood overtuned (WR: 58.0%, factor: 0.968); Condition triggers excessively (N=1 conditions, Trigger Rate: 96.2% vs 55% ceiling, WR: 54.7%). Compressing spread: b +16.0%, n -24.5% |
| `WEF` | Plants | Conditional Strike | 3.2 -> **2.9** (-9.4%) | 87.9 -> **113.5** | 284.5 -> **332.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.4% vs 30% floor, Casts: 1632). Increasing spread: b -14.2%, n +29.1%; Individual spell undertuned (WR: 31.6%, Casts: 1632, mult: 1.070) |
| `WEW` | Plants | Debuff / Control | 204.3 -> **234.9** (+15.0%) | - | 204.3 -> **234.9** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WEL` | Plants | Debuff / Control | 36.1 -> **32.4** (-10.2%) | - | 36.1 -> **32.4** | Status 'Entangled' appliers overtuned on own (WR: 64.6%); Individual spell overtuned (WR: 64.6%, Casts: 1770, mult: 0.946) |
| `WED` | Plants | Conditional Strike | 6.1 -> **6.7** (+9.8%) | 46.2 -> **43.4** | 287.9 -> **297.5** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.4% vs 8% floor, Casts: 1307, WR: 44.5%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 44.5%, Casts: 1307, mult: 1.019) |
| `EWF` | Plants | Buff / Sustain | 3.0 -> **2.6** (-13.3%) | 58.6 -> **73.0** | 178.8 -> **192.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.8% vs 30% floor, Casts: 2987). Increasing spread: b -12.1%, n +24.6% |
| `EWW` | Plants | Debuff / Control | 5.2 -> **4.5** (-13.5%) | - | 5.2 -> **4.5** | Individual spell overtuned (WR: 82.4%, Casts: 1952, mult: 0.870) |
| `EWL` | Plants | Debuff / Control | 68.5 -> **70.2** (+2.5%) | - | 68.5 -> **70.2** | Individual spell undertuned (WR: 42.9%, Casts: 2712, mult: 1.024) |
| `EWD` | Plants | Conditional Strike | 6.5 -> **5.2** (-20.0%) | 196.5 -> **264.8** | 1283.8 -> **1382.2** | Status 'Bleeding' appliers overtuned on own (WR: 65.6%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.7% vs 30% floor, Casts: 3081). Increasing spread: b -16.9%, n +34.8% |
| `WLF` | Fey | Conditional Strike | 2.8 -> **2.5** (-10.7%) | 169.4 -> **230.1** | 477.1 -> **577.8** | Status 'Cursed' beneficiaries undertuned (WR: 41.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 2168). Increasing spread: b -15.3%, n +31.4% |
| `WLE` | Fey | Setup - Location | 156.9 -> **168.9** (+7.6%) | - | 156.9 -> **168.9** | Location 'Enchanted Forest' appliers overtuned on own (WR: 59.2%); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 56.5 -> **57.8** (+2.3%) | - | 56.5 -> **57.8** | Individual spell undertuned (WR: 43.5%, Casts: 1750, mult: 1.022) |
| `WLD` | Fey | Ultimate | 27.7 -> **26.7** (-3.6%) | 155.9 -> **197.4** | 4346.1 -> **5297.3** | Location 'Enchanted Forest' beneficiaries overtuned (WR: 56.4%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1522). Shifted tuner focus: protected ultimate base floor at 27.7 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 16.7 -> **19.2** (+15.0%) | 57.8 -> **71.9** | 982.0 -> **1399.7** | Location 'Enchanted Forest' beneficiaries overtuned (WR: 56.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.2% vs 30% floor, Casts: 2055). Increasing spread: b -13.5%, n +27.7% |
| `LWL` | Fey | Debuff / Control | 44.7 -> **46.2** (+3.4%) | - | 44.7 -> **46.2** | Individual spell undertuned (WR: 40.6%, Casts: 1427, mult: 1.033) |
| `LWD` | Fey | Conditional Strike | 1.9 -> **1.6** (-15.8%) | 239.6 -> **328.3** | 457.1 -> **526.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2222). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 43.0%, Casts: 2222, mult: 1.024) |
| `WDF` | Ice | Conditional Strike | 3.6 -> **3.4** (-5.6%) | 219.5 -> **307.2** | 793.8 -> **1047.9** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Status 'Stunned' appliers undertuned (WR: 44.3%, casts: 14756) |
| `WDW` | Ice | Buff / Sustain | 14.0 -> **14.2** (+1.4%) | - | 14.0 -> **14.2** | Class Ice undertuned (WR: 45.6%, factor: 1.018) |
| `WDE` | Ice | Setup - Weather | 26.9 -> **28.9** (+7.4%) | - | 26.9 -> **28.9** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Individual spell undertuned (WR: 35.2%, Casts: 2226, mult: 1.055) |
| `WDL` | Ice | Debuff / Control | 44.9 -> **45.0** (+0.2%) | - | 44.9 -> **45.0** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Individual spell overtuned (WR: 54.6%, Casts: 1173, mult: 0.985) |
| `WDD` | Ice | Ultimate | 29.7 -> **29.8** (+0.3%) | 73.2 -> **90.6** | 2203.7 -> **2729.7** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Weather 'Blizzard' beneficiaries overtuned (WR: 54.2%) |
| `DWF` | Ice | Debuff / Control | 42.8 -> **42.4** (-0.9%) | - | 42.8 -> **42.4** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Individual spell overtuned (WR: 57.8%, Casts: 908, mult: 0.973) |
| `DWW` | Ice | Debuff / Control | 52.9 -> **61.9** (+17.0%) | - | 52.9 -> **61.9** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Buffed setup spell [DWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD] |
| `DWE` | Ice | Setup - Location | 34.0 -> **36.0** (+5.9%) | - | 34.0 -> **36.0** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Location 'Tundra' appliers undertuned (WR: 44.3%, casts: 2797) |
| `DWL` | Ice | Debuff / Control | 44.8 -> **45.6** (+1.8%) | - | 44.8 -> **45.6** | Class Ice undertuned (WR: 45.6%, factor: 1.018) |
| `DWD` | Ice | Conditional Strike | 7.0 -> **6.4** (-8.6%) | 32.9 -> **40.3** | 237.3 -> **264.3** | Class Ice undertuned (WR: 45.6%, factor: 1.018); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.3% vs 30% floor, Casts: 1869). Increasing spread: b -11.1%, n +22.5% |
| `ELF` | Wind | Conditional Strike | 6.1 -> **5.3** (-13.1%) | 128.7 -> **167.3** | 791.2 -> **892.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.4% vs 30% floor, Casts: 1689). Increasing spread: b -14.6%, n +30.0%; Individual spell undertuned (WR: 46.2%, Casts: 1689, mult: 1.013) |
| `ELW` | Wind | Debuff / Control | 59.4 -> **66.4** (+11.8%) | - | 59.4 -> **66.4** | Buffed setup spell [ELW] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 58.1%, Casts: 2120, mult: 0.972) |
| `ELL` | Wind | Buff / Sustain | 37.5 -> **38.0** (+1.3%) | - | 37.5 -> **38.0** | Individual spell undertuned (WR: 45.9%, Casts: 1476, mult: 1.013) |
| `ELD` | Wind | Conditional Strike | 3.3 -> **2.9** (-12.1%) | 191.7 -> **267.0** | 635.9 -> **777.2** | Weather 'Raining' beneficiaries undertuned (WR: 37.2%); Weather 'Blizzard' appliers undertuned (WR: 45.1%, casts: 2749) |
| `LEF` | Wind | Conditional Strike | 2.3 -> **2.0** (-13.0%) | 125.3 -> **162.3** | 290.5 -> **326.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.9% vs 30% floor, Casts: 1859). Increasing spread: b -14.4%, n +29.6% |
| `LEW` | Wind | Debuff / Control | 56.3 -> **55.1** (-2.1%) | - | 56.3 -> **55.1** | Individual spell overtuned (WR: 56.2%, Casts: 2780, mult: 0.979) |
| `LEL` | Wind | Buff / Sustain | 54.6 -> **63.6** (+16.5%) | - | 54.6 -> **63.6** | Buffed setup spell [LEL] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell undertuned (WR: 46.1%, Casts: 2413, mult: 1.013) |
| `EDF` | Poison | Conditional Strike | 1.8 -> **1.5** (-16.7%) | 126.4 -> **164.7** | 229.3 -> **248.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.0% vs 30% floor, Casts: 2914). Increasing spread: b -14.8%, n +30.3% |
| `EDW` | Poison | Debuff / Control | 14.9 -> **14.5** (-2.7%) | - | 14.9 -> **14.5** | Individual spell overtuned (WR: 57.8%, Casts: 1859, mult: 0.973) |
| `EDE` | Poison | Setup - Location | 49.2 -> **52.0** (+5.7%) | - | 49.2 -> **52.0** | Location 'Swamp' appliers undertuned (WR: 42.0%, casts: 1353); Individual spell undertuned (WR: 42.0%, Casts: 1353, mult: 1.028) |
| `EDL` | Poison | Debuff / Control | 1.9 -> **1.6** (-15.8%) | - | 1.9 -> **1.6** | Individual spell overtuned (WR: 84.2%, Casts: 1892, mult: 0.862) |
| `EDD` | Poison | Ultimate | 35.4 -> **39.5** (+11.6%) | 24.0 -> **23.4** | 885.0 -> **963.8** | Location 'Swamp' beneficiaries undertuned (WR: 40.6%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.8% vs 16% floor, Casts: 1372, WR: 40.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DEW` | Poison | Debuff / Control | 17.3 -> **16.9** (-2.3%) | - | 17.3 -> **16.9** | Individual spell overtuned (WR: 56.3%, Casts: 2813, mult: 0.978) |
| `DEE` | Poison | Debuff / Control | 25.8 -> **29.2** (+13.2%) | - | 25.8 -> **29.2** | Buffed setup spell [DEE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 54.6%, Casts: 1466, mult: 0.985) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 132.8 -> **170.4** | 26.8 -> **34.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.5% vs 30% floor, Casts: 1998). Increasing spread: b -13.8%, n +28.3%; Individual spell undertuned (WR: 45.3%, Casts: 1998, mult: 1.016) |
| `DED` | Poison | Debuff / Control | 22.1 -> **22.4** (+1.4%) | - | 22.1 -> **22.4** | Individual spell undertuned (WR: 45.3%, Casts: 2364, mult: 1.015) |
| `LDF` | Cosmic | Debuff / Control | 75.5 -> **84.0** (+11.3%) | - | 75.5 -> **84.0** | Buffed setup spell [LDF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LDD]; Individual spell overtuned (WR: 59.1%, Casts: 754, mult: 0.968) |
| `LDW` | Cosmic | Debuff / Control | 45.1 -> **46.0** (+2.0%) | - | 45.1 -> **46.0** | Status 'Stunned' appliers undertuned (WR: 44.3%, casts: 14756) |
| `LDL` | Cosmic | Conditional Strike | 2.8 -> **2.4** (-14.3%) | 149.1 -> **201.8** | 420.3 -> **486.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.0% vs 30% floor, Casts: 1539). Increasing spread: b -17.2%, n +35.3%; Individual spell undertuned (WR: 37.1%, Casts: 1539, mult: 1.047) |
| `LDD` | Cosmic | Ultimate | 67.4 -> **67.4** (+0.0%) | 8.1 -> **10.5** | 613.3 -> **775.1** | Ultimate payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 1698). Shifted tuner focus: protected ultimate base floor at 67.4 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDW, DDL, DEE, DFW, DWW, ELW, LEL, DLL, FEF, LWF) with +15% b tempo. |
| `DLF` | Cosmic | Conditional Strike | 3.1 -> **2.7** (-12.9%) | 138.9 -> **177.4** | 433.7 -> **481.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.1% vs 30% floor, Casts: 2489). Increasing spread: b -13.5%, n +27.7%; Individual spell undertuned (WR: 45.8%, Casts: 2489, mult: 1.014) |
| `DLW` | Cosmic | Direct Damage | 60.6 -> **61.8** (+2.0%) | - | 60.6 -> **61.8** | Individual spell undertuned (WR: 44.1%, Casts: 2139, mult: 1.020) |
| `DLL` | Cosmic | Conditional Strike | 7.5 -> **6.8** (-9.3%) | 65.9 -> **83.5** | 501.8 -> **574.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.4% vs 30% floor, Casts: 2189). Increasing spread: b -13.0%, n +26.7%; Individual spell undertuned (WR: 37.9%, Casts: 2189, mult: 1.044) |
