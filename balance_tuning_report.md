# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T17:01:40Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 75.4s  
**Total Spells Tuned:** 114 / 125  

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
| **Blood** | 24,558 | 61.3% | 61.3% | 4.9 | Overtuned ⚠️ |
| **Fire** | 25,961 | 56.5% | 56.5% | 8.6 | Overtuned ⚠️ |
| **Ghostfire** | 28,233 | 55.3% | 55.3% | 3.5 | Overtuned ⚠️ |
| **Earth** | 13,707 | 55.1% | 55.1% | 9.0 | Overtuned ⚠️ |
| **Cosmic** | 33,907 | 53.6% | 53.6% | 10.2 | Overtuned ⚠️ |
| **Water** | 12,324 | 53.6% | 53.6% | 8.5 | Overtuned ⚠️ |
| **Light** | 7,429 | 52.6% | 52.6% | 1.1 | Balanced ✅ |
| **Beasts** | 21,568 | 51.3% | 51.3% | 3.2 | Balanced ✅ |
| **Wind** | 19,197 | 47.9% | 47.9% | 4.8 | Balanced ✅ |
| **Ice** | 43,526 | 47.6% | 47.6% | 6.5 | Balanced ✅ |
| **Dark** | 16,878 | 46.8% | 46.8% | 5.6 | Balanced ✅ |
| **Lightning** | 25,097 | 46.0% | 46.0% | 3.5 | Undertuned ⚠️ |
| **Poison** | 29,517 | 45.9% | 45.9% | 3.9 | Undertuned ⚠️ |
| **Fey** | 25,255 | 44.1% | 44.1% | 6.4 | Undertuned ⚠️ |
| **Plants** | 24,773 | 42.9% | 42.9% | 2.4 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 19,755 (53.9%) | 7,918 (38.5%) | 1.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 1,400 (46.8%) | 9,633 (30.3%) | 1.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 7,250 (65.0%) | 8,882 (33.7%) | 2.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 11,598 (75.3%) | 12,481 (39.0%) | 0.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 16,973 (60.1%) | 4,376 (46.2%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 903 (73.7%) | 6,209 (50.1%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 277 (47.1%) | 3,237 (26.9%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 23.4 -> **19.4** (-17.1%) | - | 23.4 -> **19.4** | Class Fire overtuned (WR: 56.5%, factor: 0.974); Individual spell overtuned (WR: 86.8%, Casts: 3036, mult: 0.850) |
| `FFW` | Fire | Debuff / Control | 15.4 -> **14.2** (-7.8%) | - | 15.4 -> **14.2** | Class Fire overtuned (WR: 56.5%, factor: 0.974); Status 'Burning' appliers overtuned on own (WR: 65.0%) |
| `FFE` | Fire | Debuff / Control | 12.4 -> **11.6** (-6.5%) | - | 12.4 -> **11.6** | Class Fire overtuned (WR: 56.5%, factor: 0.974); Individual spell overtuned (WR: 60.8%, Casts: 13856, mult: 0.961) |
| `FFL` | Fire | Debuff / Control | 0.8 -> **0.7** (-12.5%) | - | 0.8 -> **0.7** | Class Fire overtuned (WR: 56.5%, factor: 0.974); Status 'Burning' appliers overtuned on own (WR: 65.0%) |
| `FFD` | Fire | Conditional Strike | 2.4 -> **2.1** (-12.5%) | 250.8 -> **358.7** | 604.3 -> **755.4** | Class Fire overtuned (WR: 56.5%, factor: 0.974); Status 'Burning' beneficiaries undertuned (WR: 33.7%) |
| `WWF` | Water | Conditional Strike | 2.6 -> **2.2** (-15.4%) | 183.7 -> **264.8** | 480.2 -> **584.8** | Class Water overtuned (WR: 53.6%, factor: 0.986); Status 'Burning' beneficiaries undertuned (WR: 33.7%) |
| `WWE` | Water | Setup - Weather | 189.5 -> **186.8** (-1.4%) | - | 189.5 -> **186.8** | Class Water overtuned (WR: 53.6%, factor: 0.986) |
| `WWL` | Water | Buff / Sustain | 29.8 -> **26.4** (-11.4%) | - | 29.8 -> **26.4** | Class Water overtuned (WR: 53.6%, factor: 0.986); Individual spell overtuned (WR: 75.9%, Casts: 6641, mult: 0.898) |
| `WWD` | Water | Buff / Sustain | 38.0 -> **36.3** (-4.5%) | - | 38.0 -> **36.3** | Class Water overtuned (WR: 53.6%, factor: 0.986); Individual spell overtuned (WR: 58.5%, Casts: 1236, mult: 0.970) |
| `EEF` | Earth | Conditional Strike | 3.5 -> **2.9** (-17.1%) | 285.4 -> **404.8** | 1002.4 -> **1176.8** | Class Earth overtuned (WR: 55.1%, factor: 0.980); Status 'Frosty' beneficiaries undertuned (WR: 38.5%) |
| `EEW` | Earth | Buff / Sustain | 41.3 -> **41.1** (-0.5%) | - | 41.3 -> **41.1** | Class Earth overtuned (WR: 55.1%, factor: 0.980); Individual spell undertuned (WR: 45.0%, Casts: 1910, mult: 1.017) |
| `EED` | Earth | Direct Damage | 2.5 -> **2.2** (-12.0%) | - | 2.5 -> **2.2** | Class Earth overtuned (WR: 55.1%, factor: 0.980); Individual spell overtuned (WR: 78.4%, Casts: 2993, mult: 0.887) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 192.3 -> **262.2** | 19.3 -> **26.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 3431). Increasing spread: b -17.7%, n +36.4%; Individual spell undertuned (WR: 40.1%, Casts: 3431, mult: 1.035) |
| `LLW` | Light | Debuff / Control | 17.9 -> **17.2** (-3.9%) | - | 17.9 -> **17.2** | Individual spell overtuned (WR: 61.3%, Casts: 765, mult: 0.959) |
| `LLL` | Light | Buff / Sustain | 9.4 -> **8.4** (-10.6%) | - | 9.4 -> **8.4** | Individual spell overtuned (WR: 77.3%, Casts: 1715, mult: 0.892) |
| `LLD` | Light | Ultimate | 10.8 -> **8.2** (-24.1%) | 58.3 -> **86.2** | 640.4 -> **715.0** | Weather 'Sunny' beneficiaries undertuned (WR: 30.3%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 118). Increasing spread: b -18.0%, n +37.0% |
| `DDF` | Dark | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 239.6 -> **328.3** | 288.7 -> **329.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 289). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 36.5%, Casts: 289, mult: 1.050) |
| `DDW` | Dark | Debuff / Control | 26.1 -> **25.5** (-2.3%) | - | 26.1 -> **25.5** | Individual spell overtuned (WR: 56.2%, Casts: 7684, mult: 0.979) |
| `DDE` | Dark | Setup - Weather | 105.0 -> **138.5** (+31.9%) | - | 105.0 -> **138.5** | Weather 'Darkness' appliers undertuned (WR: 7.1%, casts: 4470); Individual spell undertuned (WR: 7.0%, Casts: 4470, mult: 1.178) |
| `DDD` | Dark | Debuff / Control | 5.9 -> **5.3** (-10.2%) | - | 5.9 -> **5.3** | Individual spell overtuned (WR: 75.6%, Casts: 3752, mult: 0.900) |
| `FWF` | Ghostfire | Debuff / Control | 3.4 -> **2.7** (-20.6%) | - | 3.4 -> **2.7** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Status 'Burning' appliers overtuned on own (WR: 65.0%) |
| `FWW` | Ghostfire | Debuff / Control | 10.8 -> **9.6** (-11.1%) | - | 10.8 -> **9.6** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Status 'Cursed' appliers overtuned on own (WR: 65.3%) |
| `FWE` | Ghostfire | Setup - Location | 116.0 -> **114.7** (-1.1%) | - | 116.0 -> **114.7** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Individual spell undertuned (WR: 41.2%, Casts: 5, mult: 1.010) |
| `FWL` | Ghostfire | Debuff / Control | 25.8 -> **21.6** (-16.3%) | - | 25.8 -> **21.6** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Status 'Cursed' appliers overtuned on own (WR: 65.3%) |
| `FWD` | Ghostfire | Ultimate | 18.2 -> **13.8** (-24.2%) | 31.8 -> **38.5** | 597.0 -> **545.1** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Status 'Cursed' beneficiaries overtuned (WR: 64.1%) |
| `WFF` | Ghostfire | Conditional Strike | 1.7 -> **1.4** (-17.6%) | 370.1 -> **525.1** | 630.9 -> **736.5** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Status 'Bleeding' beneficiaries undertuned (WR: 39.0%) |
| `WFW` | Ghostfire | Debuff / Control | 8.7 -> **7.7** (-11.5%) | - | 8.7 -> **7.7** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Individual spell overtuned (WR: 74.2%, Casts: 2255, mult: 0.905) |
| `WFE` | Ghostfire | Debuff / Control | 1.5 -> **1.1** (-26.7%) | - | 1.5 -> **1.1** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Status 'Bleeding' appliers overtuned on own (WR: 75.3%) |
| `WFL` | Ghostfire | Buff / Sustain | 42.9 -> **48.1** (+12.1%) | - | 42.9 -> **48.1** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Individual spell undertuned (WR: 14.4%, Casts: 4558, mult: 1.145) |
| `WFD` | Ghostfire | Conditional Strike | 2.0 -> **1.8** (-10.0%) | 206.5 -> **282.6** | 415.0 -> **510.5** | Class Ghostfire overtuned (WR: 55.3%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 5078). Increasing spread: b -17.9%, n +36.9% |
| `FEF` | Beasts | Debuff / Control | 15.8 -> **15.6** (-1.3%) | - | 15.8 -> **15.6** | Individual spell overtuned (WR: 54.4%, Casts: 2168, mult: 0.986) |
| `FEW` | Beasts | Conditional Strike | 3.0 -> **2.3** (-23.3%) | 360.3 -> **493.6** | 1083.9 -> **1137.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 727). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 65.8%, Casts: 727, mult: 0.941) |
| `FEE` | Beasts | Buff / Sustain | 48.0 -> **53.6** (+11.7%) | - | 48.0 -> **53.6** | Individual spell undertuned (WR: 20.8%, Casts: 2190, mult: 1.116) |
| `FEL` | Beasts | Buff / Sustain | 89.1 -> **93.3** (+4.7%) | - | 89.1 -> **93.3** | Individual spell undertuned (WR: 37.0%, Casts: 2593, mult: 1.048) |
| `FED` | Beasts | Conditional Strike | 3.2 -> **2.9** (-9.4%) | 3.5 -> **3.5** | 14.4 -> **13.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.6% vs 30% floor, Casts: 6046). Increasing spread: b -16.6%, n +34.0%; Individual spell undertuned (WR: 27.7%, Casts: 6046, mult: 1.086) |
| `EFF` | Beasts | Debuff / Control | 2.2 -> **1.6** (-27.3%) | 215.9 -> **295.8** | 477.2 -> **474.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 199). Increasing spread: b -18.0%, n +37.0%; Individual spell overtuned (WR: 72.5%, Casts: 199, mult: 0.913) |
| `EFW` | Beasts | Buff / Sustain | 43.0 -> **47.0** (+9.3%) | - | 43.0 -> **47.0** | Individual spell undertuned (WR: 23.5%, Casts: 39, mult: 1.092) |
| `EFE` | Beasts | Buff / Sustain | 24.0 -> **22.5** (-6.2%) | - | 24.0 -> **22.5** | Individual spell overtuned (WR: 66.5%, Casts: 1434, mult: 0.938) |
| `EFL` | Beasts | Buff / Sustain | 2.5 -> **2.1** (-16.0%) | - | 2.5 -> **2.1** | Individual spell overtuned (WR: 95.2%, Casts: 3973, mult: 0.820) |
| `EFD` | Beasts | Ultimate | 13.8 -> **10.7** (-22.5%) | 91.9 -> **118.4** | 1282.0 -> **1277.6** | Location 'Jungle' beneficiaries overtuned (WR: 65.0%); Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 2199). Increasing spread: b -18.0%, n +37.0% |
| `FLF` | Lightning | Conditional Strike | 1.9 -> **1.6** (-15.8%) | 284.5 -> **395.8** | 542.4 -> **634.9** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Status 'Stunned' beneficiaries undertuned (WR: 46.2%) |
| `FLW` | Lightning | Debuff / Control | 19.3 -> **16.5** (-14.5%) | - | 19.3 -> **16.5** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Status 'Stunned' appliers overtuned on own (WR: 60.1%) |
| `FLE` | Lightning | Setup - Weather | 60.5 -> **79.6** (+31.6%) | - | 60.5 -> **79.6** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Weather 'Storming' appliers undertuned (WR: 11.9%, casts: 2427) |
| `FLL` | Lightning | Buff / Sustain | 35.4 -> **38.6** (+9.0%) | - | 35.4 -> **38.6** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Individual spell undertuned (WR: 30.5%, Casts: 1789, mult: 1.074) |
| `FLD` | Lightning | Ultimate | 15.9 -> **17.7** (+11.3%) | 44.0 -> **42.6** | 715.5 -> **771.7** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Status 'Stunned' beneficiaries undertuned (WR: 46.2%) |
| `LFF` | Lightning | Conditional Strike | 2.8 -> **2.6** (-7.1%) | 227.3 -> **311.4** | 639.2 -> **812.2** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5417). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 26.9 -> **25.7** (-4.5%) | - | 26.9 -> **25.7** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Individual spell overtuned (WR: 65.9%, Casts: 2407, mult: 0.940) |
| `LFE` | Lightning | Debuff / Control | 17.1 -> **16.8** (-1.8%) | - | 17.1 -> **16.8** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Status 'Stunned' appliers overtuned on own (WR: 60.1%) |
| `LFL` | Lightning | Debuff / Control | 3.4 -> **3.0** (-11.8%) | 149.9 -> **208.2** | 513.1 -> **627.6** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Weather 'Darkness' beneficiaries undertuned (WR: 41.1%) |
| `LFD` | Lightning | Conditional Strike | 2.2 -> **1.6** (-27.3%) | 273.3 -> **374.4** | 603.5 -> **600.6** | Class Lightning undertuned (WR: 46.0%, factor: 1.016); Status 'Stunned' appliers overtuned on own (WR: 60.1%) |
| `FDF` | Blood | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 239.6 -> **328.3** | 336.8 -> **395.2** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2353). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 67.9 -> **63.0** (-7.2%) | - | 67.9 -> **63.0** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Individual spell overtuned (WR: 58.3%, Casts: 230, mult: 0.971) |
| `FDE` | Blood | Setup - Weather | 52.4 -> **53.8** (+2.7%) | - | 52.4 -> **53.8** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Individual spell undertuned (WR: 30.2%, Casts: 1513, mult: 1.076) |
| `FDL` | Blood | Debuff / Control | 1.3 -> **1.0** (-23.1%) | - | 1.3 -> **1.0** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Status 'Bleeding' appliers overtuned on own (WR: 75.3%) |
| `FDD` | Blood | Ultimate | 10.0 -> **7.8** (-22.0%) | 30.8 -> **43.7** | 318.0 -> **348.7** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Weather 'Darkness' beneficiaries undertuned (WR: 41.1%) |
| `DFF` | Blood | Conditional Strike | 2.4 -> **1.8** (-25.0%) | 289.0 -> **406.4** | 696.0 -> **733.3** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Status 'Bleeding' beneficiaries undertuned (WR: 39.0%) |
| `DFW` | Blood | Debuff / Control | 1.0 -> **0.7** (-30.0%) | - | 1.0 -> **0.7** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Status 'Bleeding' appliers overtuned on own (WR: 75.3%) |
| `DFE` | Blood | Buff / Sustain | 117.5 -> **132.4** (+12.7%) | - | 117.5 -> **132.4** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Individual spell undertuned (WR: 3.8%, Casts: 330, mult: 1.180) |
| `DFL` | Blood | Buff / Sustain | 10.7 -> **9.3** (-13.1%) | - | 10.7 -> **9.3** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Individual spell overtuned (WR: 73.0%, Casts: 8236, mult: 0.911) |
| `DFD` | Blood | Conditional Strike | 93.3 -> **96.0** (+2.9%) | 0.1 -> **0.1** | 102.6 -> **105.6** | Class Blood overtuned (WR: 61.3%, factor: 0.955); Condition triggers excessively (N=1 conditions, Trigger Rate: 79.0% vs 55% ceiling, WR: 79.4%). Compressing spread: b +22.1%, n -28.3% |
| `WEF` | Plants | Conditional Strike | 2.0 -> **1.6** (-20.0%) | 275.8 -> **354.8** | 553.6 -> **569.3** | Class Plants undertuned (WR: 42.9%, factor: 1.028); Location 'Jungle' beneficiaries overtuned (WR: 65.0%) |
| `WEW` | Plants | Debuff / Control | 51.1 -> **55.7** (+9.0%) | - | 51.1 -> **55.7** | Class Plants undertuned (WR: 42.9%, factor: 1.028); Individual spell undertuned (WR: 33.9%, Casts: 935, mult: 1.060) |
| `WEE` | Plants | Setup - Location | 130.6 -> **175.0** (+34.0%) | - | 130.6 -> **175.0** | Class Plants undertuned (WR: 42.9%, factor: 1.028); Location 'Jungle' appliers undertuned (WR: 10.2%, casts: 3327) |
| `WEL` | Plants | Debuff / Control | 22.3 -> **19.1** (-14.3%) | - | 22.3 -> **19.1** | Class Plants undertuned (WR: 42.9%, factor: 1.028); Status 'Entangled' appliers overtuned on own (WR: 73.7%) |
| `WED` | Plants | Conditional Strike | 17.4 -> **14.3** (-17.8%) | 11.8 -> **16.2** | 222.7 -> **246.0** | Class Plants undertuned (WR: 42.9%, factor: 1.028); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1300). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 2.9 -> **2.7** (-6.9%) | 251.3 -> **368.1** | 731.7 -> **996.6** | Class Plants undertuned (WR: 42.9%, factor: 1.028); Weather 'Sunny' beneficiaries undertuned (WR: 30.3%) |
| `EWW` | Plants | Debuff / Control | 2.9 -> **2.5** (-13.8%) | - | 2.9 -> **2.5** | Class Plants undertuned (WR: 42.9%, factor: 1.028); Individual spell overtuned (WR: 90.9%, Casts: 2296, mult: 0.832) |
| `EWL` | Plants | Debuff / Control | 30.0 -> **26.7** (-11.0%) | - | 30.0 -> **26.7** | Class Plants undertuned (WR: 42.9%, factor: 1.028); Individual spell overtuned (WR: 83.1%, Casts: 2396, mult: 0.867) |
| `EWD` | Plants | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 354.5 -> **485.6** | 213.3 -> **243.3** | Class Plants undertuned (WR: 42.9%, factor: 1.028); Status 'Bleeding' appliers overtuned on own (WR: 75.3%) |
| `WLF` | Fey | Conditional Strike | 2.2 -> **2.2** (+0.0%) | 194.5 -> **251.4** | 430.1 -> **555.3** | Class Fey undertuned (WR: 44.1%, factor: 1.024); Status 'Cursed' beneficiaries overtuned (WR: 64.1%) |
| `WLW` | Fey | Debuff / Control | 20.5 -> **18.6** (-9.3%) | - | 20.5 -> **18.6** | Class Fey undertuned (WR: 44.1%, factor: 1.024); Status 'Cursed' appliers overtuned on own (WR: 65.3%) |
| `WLE` | Fey | Setup - Location | 159.0 -> **204.8** (+28.8%) | - | 159.0 -> **204.8** | Class Fey undertuned (WR: 44.1%, factor: 1.024); Location 'Enchanted Forest' appliers undertuned (WR: 17.6%, casts: 1927) |
| `WLL` | Fey | Direct Damage | 71.8 -> **61.5** (-14.3%) | - | 71.8 -> **61.5** | Class Fey undertuned (WR: 44.1%, factor: 1.024); Individual spell overtuned (WR: 89.8%, Casts: 2037, mult: 0.837) |
| `WLD` | Fey | Ultimate | 15.0 -> **12.6** (-16.0%) | 54.0 -> **78.7** | 825.0 -> **1004.2** | Class Fey undertuned (WR: 44.1%, factor: 1.024); Weather 'Darkness' beneficiaries undertuned (WR: 41.1%) |
| `LWF` | Fey | Debuff / Control | 5.0 -> **4.5** (-10.0%) | 212.1 -> **295.9** | 1065.5 -> **1336.0** | Class Fey undertuned (WR: 44.1%, factor: 1.024); Location 'Enchanted Forest' beneficiaries undertuned (WR: 43.2%) |
| `LWW` | Fey | Debuff / Control | 51.4 -> **56.3** (+9.5%) | - | 51.4 -> **56.3** | Class Fey undertuned (WR: 44.1%, factor: 1.024); Individual spell undertuned (WR: 31.8%, Casts: 999, mult: 1.069) |
| `LWL` | Fey | Debuff / Control | 133.8 -> **151.5** (+13.2%) | - | 133.8 -> **151.5** | Class Fey undertuned (WR: 44.1%, factor: 1.024); Individual spell undertuned (WR: 23.1%, Casts: 725, mult: 1.106) |
| `LWD` | Fey | Conditional Strike | 4.2 -> **3.6** (-14.3%) | 239.6 -> **328.3** | 1010.5 -> **1185.5** | Class Fey undertuned (WR: 44.1%, factor: 1.024); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3642). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 3.7 -> **3.2** (-13.5%) | 393.3 -> **588.6** | 1458.9 -> **1886.7** | Status 'Stunned' appliers overtuned on own (WR: 60.1%); Weather 'Raining' beneficiaries undertuned (WR: 26.9%) |
| `WDW` | Ice | Buff / Sustain | 37.2 -> **41.1** (+10.5%) | - | 37.2 -> **41.1** | Status 'Frosty' appliers overtuned on own (WR: 53.9%); Individual spell undertuned (WR: 20.0%, Casts: 5718, mult: 1.120) |
| `WDE` | Ice | Setup - Weather | 62.5 -> **72.5** (+16.0%) | - | 62.5 -> **72.5** | Individual spell undertuned (WR: 11.0%, Casts: 6155, mult: 1.160) |
| `WDL` | Ice | Debuff / Control | 23.4 -> **21.7** (-7.3%) | - | 23.4 -> **21.7** | Status 'Frosty' appliers overtuned on own (WR: 53.9%); Individual spell overtuned (WR: 66.4%, Casts: 3246, mult: 0.939) |
| `WDD` | Ice | Ultimate | 16.1 -> **13.2** (-18.0%) | 30.5 -> **41.8** | 507.2 -> **565.0** | Conditional payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 3876). Increasing spread: b -18.0%, n +37.0% |
| `DWF` | Ice | Debuff / Control | 22.3 -> **19.2** (-13.9%) | - | 22.3 -> **19.2** | Status 'Frosty' appliers overtuned on own (WR: 53.9%); Individual spell overtuned (WR: 81.4%, Casts: 4269, mult: 0.874) |
| `DWW` | Ice | Debuff / Control | 25.9 -> **23.4** (-9.7%) | - | 25.9 -> **23.4** | Individual spell overtuned (WR: 74.2%, Casts: 6949, mult: 0.905) |
| `DWE` | Ice | Setup - Location | 124.1 -> **144.2** (+16.2%) | - | 124.1 -> **144.2** | Location 'Tundra' appliers undertuned (WR: 28.9%, casts: 783); Individual spell undertuned (WR: 28.8%, Casts: 783, mult: 1.082) |
| `DWL` | Ice | Debuff / Control | 24.1 -> **23.0** (-4.6%) | - | 24.1 -> **23.0** | Status 'Frosty' appliers overtuned on own (WR: 53.9%); Individual spell overtuned (WR: 59.5%, Casts: 6522, mult: 0.966) |
| `DWD` | Ice | Conditional Strike | 4.3 -> **3.7** (-14.0%) | 228.0 -> **322.3** | 984.7 -> **1196.2** | Status 'Frosty' beneficiaries undertuned (WR: 38.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 3748). Increasing spread: b -17.1%, n +35.2% |
| `ELF` | Wind | Conditional Strike | 6.3 -> **4.9** (-22.2%) | 335.0 -> **478.1** | 2116.8 -> **2347.6** | Status 'Bleeding' beneficiaries undertuned (WR: 39.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 842). Increasing spread: b -17.9%, n +36.7% |
| `ELW` | Wind | Debuff / Control | 33.4 -> **29.9** (-10.5%) | - | 33.4 -> **29.9** | Individual spell overtuned (WR: 76.3%, Casts: 883, mult: 0.896) |
| `ELE` | Wind | Setup - Weather | 60.7 -> **63.4** (+4.4%) | - | 60.7 -> **63.4** | Individual spell undertuned (WR: 37.9%, Casts: 2110, mult: 1.044) |
| `ELD` | Wind | Conditional Strike | 5.1 -> **4.6** (-9.8%) | 353.0 -> **528.3** | 1805.4 -> **2434.8** | Weather 'Raining' beneficiaries undertuned (WR: 26.9%); Weather 'Blizzard' appliers undertuned (WR: 36.8%, casts: 977) |
| `LEF` | Wind | Conditional Strike | 3.3 -> **2.8** (-15.2%) | 255.5 -> **368.5** | 846.4 -> **1034.6** | Status 'Burning' beneficiaries undertuned (WR: 33.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 3541). Increasing spread: b -17.2%, n +35.4% |
| `LEW` | Wind | Debuff / Control | 33.8 -> **29.9** (-11.5%) | - | 33.8 -> **29.9** | Individual spell overtuned (WR: 78.7%, Casts: 4186, mult: 0.886) |
| `LEL` | Wind | Buff / Sustain | 95.6 -> **106.8** (+11.7%) | - | 95.6 -> **106.8** | Individual spell undertuned (WR: 20.6%, Casts: 1490, mult: 1.117) |
| `EDF` | Poison | Conditional Strike | 1.6 -> **1.5** (-6.3%) | 176.0 -> **237.0** | 283.2 -> **357.0** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.8% vs 30% floor, Casts: 318). Increasing spread: b -16.9%, n +34.6% |
| `EDW` | Poison | Debuff / Control | 5.9 -> **5.7** (-3.4%) | - | 5.9 -> **5.7** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 64.7%, Casts: 3263, mult: 0.946) |
| `EDE` | Poison | Setup - Location | 94.4 -> **123.9** (+31.2%) | - | 94.4 -> **123.9** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Location 'Swamp' appliers undertuned (WR: 12.5%, casts: 5570) |
| `EDL` | Poison | Debuff / Control | 1.2 -> **1.0** (-16.7%) | - | 1.2 -> **1.0** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 91.8%, Casts: 2112, mult: 0.828) |
| `EDD` | Poison | Ultimate | 16.3 -> **13.6** (-16.6%) | 47.1 -> **67.3** | 784.0 -> **928.9** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Status 'Bleeding' beneficiaries undertuned (WR: 39.0%) |
| `DEF` | Poison | Conditional Strike | 11.3 -> **9.5** (-15.9%) | 3.0 -> **3.9** | 45.2 -> **46.6** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.9% vs 30% floor, Casts: 919). Increasing spread: b -14.4%, n +29.6% |
| `DEW` | Poison | Debuff / Control | 6.2 -> **6.0** (-3.2%) | - | 6.2 -> **6.0** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 63.5%, Casts: 3952, mult: 0.950) |
| `DEE` | Poison | Debuff / Control | 16.1 -> **15.6** (-3.1%) | - | 16.1 -> **15.6** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 63.4%, Casts: 3545, mult: 0.951) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 338.3 -> **483.9** | 101.8 -> **145.5** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Status 'Bleeding' beneficiaries undertuned (WR: 39.0%) |
| `DED` | Poison | Debuff / Control | 18.4 -> **17.5** (-4.9%) | - | 18.4 -> **17.5** | Class Poison undertuned (WR: 45.9%, factor: 1.016); Individual spell overtuned (WR: 67.5%, Casts: 1499, mult: 0.934) |
| `LDF` | Cosmic | Debuff / Control | 26.6 -> **24.0** (-9.8%) | - | 26.6 -> **24.0** | Class Cosmic overtuned (WR: 53.6%, factor: 0.986); Individual spell overtuned (WR: 72.0%, Casts: 549, mult: 0.915) |
| `LDW` | Cosmic | Debuff / Control | 17.0 -> **14.3** (-15.9%) | - | 17.0 -> **14.3** | Class Cosmic overtuned (WR: 53.6%, factor: 0.986); Status 'Stunned' appliers overtuned on own (WR: 60.1%) |
| `LDE` | Cosmic | Setup - Location | 35.5 -> **36.8** (+3.7%) | - | 35.5 -> **36.8** | Class Cosmic overtuned (WR: 53.6%, factor: 0.986); Individual spell undertuned (WR: 35.9%, Casts: 600, mult: 1.052) |
| `LDL` | Cosmic | Conditional Strike | 2.9 -> **2.3** (-20.7%) | 202.9 -> **277.6** | 591.3 -> **640.8** | Class Cosmic overtuned (WR: 53.6%, factor: 0.986); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 885). Increasing spread: b -17.9%, n +36.8% |
| `LDD` | Cosmic | Ultimate | 13.2 -> **14.3** (+8.3%) | 42.6 -> **40.0** | 575.5 -> **586.3** | Class Cosmic overtuned (WR: 53.6%, factor: 0.986); Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 6434, WR: 44.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 3.1 -> **2.7** (-12.9%) | 181.3 -> **248.4** | 565.1 -> **673.4** | Class Cosmic overtuned (WR: 53.6%, factor: 0.986); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 3758). Increasing spread: b -18.0%, n +37.0% |
| `DLW` | Cosmic | Direct Damage | 25.9 -> **23.7** (-8.5%) | - | 25.9 -> **23.7** | Class Cosmic overtuned (WR: 53.6%, factor: 0.986); Individual spell overtuned (WR: 69.2%, Casts: 9914, mult: 0.927) |
| `DLE` | Cosmic | Direct Damage | 110.6 -> **124.4** (+12.5%) | - | 110.6 -> **124.4** | Class Cosmic overtuned (WR: 53.6%, factor: 0.986); Individual spell undertuned (WR: 15.2%, Casts: 1974, mult: 1.141) |
| `DLL` | Cosmic | Conditional Strike | 3.1 -> **2.9** (-6.5%) | 172.0 -> **239.6** | 536.3 -> **697.7** | Class Cosmic overtuned (WR: 53.6%, factor: 0.986); Weather 'Darkness' beneficiaries undertuned (WR: 41.1%) |
