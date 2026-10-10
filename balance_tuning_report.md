# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T17:17:30Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 126.2s  
**Total Spells Tuned:** 115 / 125  

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
| **Dark** | 8,042 | 71.0% | 71.1% | 11.8 | Overtuned ⚠️ |
| **Blood** | 23,974 | 57.0% | 57.1% | 4.2 | Overtuned ⚠️ |
| **Beasts** | 18,037 | 56.7% | 56.7% | 4.1 | Overtuned ⚠️ |
| **Ghostfire** | 29,348 | 56.4% | 56.4% | 3.1 | Overtuned ⚠️ |
| **Poison** | 31,014 | 56.2% | 56.2% | 3.9 | Overtuned ⚠️ |
| **Fire** | 18,782 | 54.7% | 54.7% | 8.0 | Overtuned ⚠️ |
| **Cosmic** | 34,035 | 52.0% | 52.0% | 8.3 | Balanced ✅ |
| **Lightning** | 25,775 | 50.3% | 50.3% | 3.4 | Balanced ✅ |
| **Water** | 9,016 | 49.5% | 49.5% | 7.1 | Balanced ✅ |
| **Ice** | 54,567 | 48.4% | 48.4% | 7.0 | Balanced ✅ |
| **Plants** | 21,851 | 46.7% | 46.7% | 2.7 | Balanced ✅ |
| **Fey** | 23,467 | 41.3% | 41.3% | 3.7 | Undertuned ⚠️ |
| **Wind** | 24,794 | 41.3% | 41.3% | 5.0 | Undertuned ⚠️ |
| **Light** | 12,546 | 39.7% | 39.7% | 1.7 | Undertuned ⚠️ |
| **Earth** | 12,560 | 36.5% | 36.5% | 6.2 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 28,001 (50.7%) | 11,965 (30.4%) | 1.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 3,848 (21.6%) | 9,585 (20.3%) | 1.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 9,412 (83.8%) | 7,839 (39.5%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,694 (81.7%) | 14,014 (28.6%) | 0.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 25,001 (46.8%) | 6,017 (35.8%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,987 (84.9%) | 5,516 (52.4%) | 0.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,764 (20.1%) | 5,036 (35.8%) | 0.5% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 19.4 -> **18.3** (-5.7%) | - | 19.4 -> **18.3** | Class Fire overtuned (WR: 54.7%, factor: 0.981); Individual spell overtuned (WR: 60.1%, Casts: 1295, mult: 0.964) |
| `FFW` | Fire | Debuff / Control | 14.2 -> **11.3** (-20.4%) | - | 14.2 -> **11.3** | Class Fire overtuned (WR: 54.7%, factor: 0.981); Status 'Burning' appliers overtuned on own (WR: 83.8%) |
| `FFE` | Fire | Debuff / Control | 11.6 -> **11.2** (-3.4%) | - | 11.6 -> **11.2** | Class Fire overtuned (WR: 54.7%, factor: 0.981); Individual spell overtuned (WR: 54.4%, Casts: 10472, mult: 0.986) |
| `FFD` | Fire | Conditional Strike | 2.1 -> **1.7** (-19.0%) | 358.7 -> **511.5** | 755.4 -> **871.2** | Class Fire overtuned (WR: 54.7%, factor: 0.981); Status 'Burning' beneficiaries undertuned (WR: 39.5%) |
| `WWF` | Water | Conditional Strike | 2.2 -> **1.9** (-13.6%) | 264.8 -> **368.8** | 584.8 -> **702.6** | Status 'Burning' beneficiaries undertuned (WR: 39.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.0% vs 30% floor, Casts: 951). Increasing spread: b -16.4%, n +33.7% |
| `WWE` | Water | Setup - Weather | 186.8 -> **231.0** (+23.7%) | - | 186.8 -> **231.0** | Weather 'Raining' appliers undertuned (WR: 20.1%, casts: 1764); Individual spell undertuned (WR: 20.1%, Casts: 1764, mult: 1.119) |
| `WWL` | Water | Buff / Sustain | 26.4 -> **24.2** (-8.3%) | - | 26.4 -> **24.2** | Individual spell overtuned (WR: 71.5%, Casts: 4267, mult: 0.917) |
| `WWD` | Water | Buff / Sustain | 36.3 -> **33.1** (-8.8%) | - | 36.3 -> **33.1** | Individual spell overtuned (WR: 72.8%, Casts: 588, mult: 0.911) |
| `EEF` | Earth | Conditional Strike | 2.9 -> **2.8** (-3.4%) | 404.8 -> **590.4** | 1176.8 -> **1655.9** | Class Earth undertuned (WR: 36.5%, factor: 1.054); Status 'Frosty' beneficiaries undertuned (WR: 30.4%) |
| `EED` | Earth | Direct Damage | 2.2 -> **2.0** (-9.1%) | - | 2.2 -> **2.0** | Class Earth undertuned (WR: 36.5%, factor: 1.054); Individual spell overtuned (WR: 80.1%, Casts: 294, mult: 0.880) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 262.2 -> **351.3** | 26.3 -> **35.2** | Class Light undertuned (WR: 39.7%, factor: 1.041); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.6% vs 30% floor, Casts: 3447). Increasing spread: b -16.6%, n +34.0% |
| `LLW` | Light | Debuff / Control | 17.2 -> **16.3** (-5.2%) | - | 17.2 -> **16.3** | Class Light undertuned (WR: 39.7%, factor: 1.041); Individual spell overtuned (WR: 72.8%, Casts: 1711, mult: 0.911) |
| `LLE` | Light | Setup - Weather | 173.0 -> **220.3** (+27.3%) | - | 173.0 -> **220.3** | Class Light undertuned (WR: 39.7%, factor: 1.041); Weather 'Sunny' appliers undertuned (WR: 21.6%, casts: 3848) |
| `LLL` | Light | Buff / Sustain | 8.4 -> **8.9** (+6.0%) | - | 8.4 -> **8.9** | Class Light undertuned (WR: 39.7%, factor: 1.041); Individual spell undertuned (WR: 44.3%, Casts: 3474, mult: 1.019) |
| `LLD` | Light | Ultimate | 8.2 -> **10.4** (+26.8%) | 86.2 -> **90.7** | 715.0 -> **953.7** | Class Light undertuned (WR: 39.7%, factor: 1.041); Weather 'Sunny' beneficiaries undertuned (WR: 20.3%) |
| `DDF` | Dark | Conditional Strike | 1.0 -> **0.8** (-20.0%) | 328.3 -> **449.8** | 329.3 -> **360.6** | Class Dark overtuned (WR: 71.0%, factor: 0.916); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 162). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 25.5 -> **20.5** (-19.6%) | - | 25.5 -> **20.5** | Class Dark overtuned (WR: 71.0%, factor: 0.916); Individual spell overtuned (WR: 80.4%, Casts: 5149, mult: 0.879) |
| `DDE` | Dark | Setup - Weather | 138.5 -> **161.2** (+16.4%) | - | 138.5 -> **161.2** | Class Dark overtuned (WR: 71.0%, factor: 0.916); Weather 'Darkness' appliers undertuned (WR: 16.4%, casts: 520) |
| `DDL` | Dark | Debuff / Control | 14.8 -> **13.9** (-6.1%) | - | 14.8 -> **13.9** | Class Dark overtuned (WR: 71.0%, factor: 0.916); Individual spell undertuned (WR: 38.7%, Casts: 19, mult: 1.025) |
| `DDD` | Dark | Debuff / Control | 5.3 -> **4.6** (-13.2%) | - | 5.3 -> **4.6** | Class Dark overtuned (WR: 71.0%, factor: 0.916); Individual spell overtuned (WR: 64.9%, Casts: 2192, mult: 0.945) |
| `FWF` | Ghostfire | Debuff / Control | 2.7 -> **1.9** (-29.6%) | - | 2.7 -> **1.9** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974); Status 'Burning' appliers overtuned on own (WR: 83.8%) |
| `FWW` | Ghostfire | Debuff / Control | 9.6 -> **7.6** (-20.8%) | - | 9.6 -> **7.6** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974); Status 'Cursed' appliers overtuned on own (WR: 65.9%) |
| `FWE` | Ghostfire | Setup - Location | 114.7 -> **111.6** (-2.7%) | - | 114.7 -> **111.6** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974); Individual spell overtuned (WR: 53.8%, Casts: 1, mult: 0.998) |
| `FWL` | Ghostfire | Debuff / Control | 21.6 -> **19.9** (-7.9%) | - | 21.6 -> **19.9** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974); Status 'Cursed' appliers overtuned on own (WR: 65.9%) |
| `FWD` | Ghostfire | Ultimate | 13.8 -> **10.5** (-23.9%) | 38.5 -> **47.1** | 545.1 -> **505.1** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974); Status 'Cursed' beneficiaries overtuned (WR: 63.4%) |
| `WFF` | Ghostfire | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 525.1 -> **778.5** | 736.5 -> **935.4** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974); Status 'Bleeding' beneficiaries undertuned (WR: 28.6%) |
| `WFW` | Ghostfire | Debuff / Control | 7.7 -> **7.5** (-2.6%) | - | 7.7 -> **7.5** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974) |
| `WFE` | Ghostfire | Debuff / Control | 1.1 -> **0.8** (-27.3%) | - | 1.1 -> **0.8** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974); Status 'Bleeding' appliers overtuned on own (WR: 81.7%) |
| `WFL` | Ghostfire | Buff / Sustain | 48.1 -> **55.2** (+14.8%) | - | 48.1 -> **55.2** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974); Individual spell undertuned (WR: 6.8%, Casts: 2665, mult: 1.179) |
| `WFD` | Ghostfire | Conditional Strike | 1.8 -> **1.6** (-11.1%) | 282.6 -> **387.2** | 510.5 -> **621.1** | Class Ghostfire overtuned (WR: 56.4%, factor: 0.974); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 5074). Increasing spread: b -18.0%, n +37.0% |
| `FEW` | Beasts | Conditional Strike | 2.3 -> **1.5** (-34.8%) | 493.6 -> **676.2** | 1137.6 -> **1015.8** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 85). Increasing spread: b -18.0%, n +37.0% |
| `FEE` | Beasts | Buff / Sustain | 53.6 -> **50.6** (-5.6%) | - | 53.6 -> **50.6** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 58.6%, Casts: 2342, mult: 0.970) |
| `FEL` | Beasts | Buff / Sustain | 93.3 -> **94.0** (+0.8%) | - | 93.3 -> **94.0** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell undertuned (WR: 40.2%, Casts: 473, mult: 1.035) |
| `FED` | Beasts | Conditional Strike | 2.9 -> **2.5** (-13.8%) | 3.5 -> **3.5** | 13.0 -> **11.2** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 2469). Increasing spread: b -17.1%, n +35.2% |
| `EFF` | Beasts | Debuff / Control | 1.6 -> **1.4** (-12.5%) | 295.8 -> **403.8** | 474.9 -> **566.7** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 170). Increasing spread: b -17.8%, n +36.5% |
| `EFW` | Beasts | Buff / Sustain | 47.0 -> **47.4** (+0.9%) | - | 47.0 -> **47.4** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell undertuned (WR: 39.8%, Casts: 101, mult: 1.036) |
| `EFE` | Beasts | Buff / Sustain | 22.5 -> **22.8** (+1.3%) | - | 22.5 -> **22.8** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell undertuned (WR: 38.5%, Casts: 1213, mult: 1.042) |
| `EFL` | Beasts | Buff / Sustain | 2.1 -> **1.7** (-19.0%) | - | 2.1 -> **1.7** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 89.7%, Casts: 4147, mult: 0.837) |
| `EFD` | Beasts | Ultimate | 10.7 -> **8.3** (-22.4%) | 118.4 -> **156.3** | 1277.6 -> **1305.6** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Location 'Jungle' beneficiaries overtuned (WR: 59.1%) |
| `FLF` | Lightning | Conditional Strike | 1.6 -> **1.5** (-6.3%) | 395.8 -> **573.0** | 634.9 -> **861.0** | Status 'Stunned' beneficiaries undertuned (WR: 35.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2567). Increasing spread: b -18.0%, n +37.0% |
| `FLW` | Lightning | Debuff / Control | 16.5 -> **14.6** (-11.5%) | - | 16.5 -> **14.6** | Individual spell overtuned (WR: 79.3%, Casts: 4195, mult: 0.883) |
| `FLE` | Lightning | Setup - Weather | 79.6 -> **105.2** (+32.2%) | - | 79.6 -> **105.2** | Weather 'Storming' appliers undertuned (WR: 5.9%, casts: 584); Individual spell undertuned (WR: 5.7%, Casts: 584, mult: 1.180) |
| `FLL` | Lightning | Buff / Sustain | 38.6 -> **34.4** (-10.9%) | - | 38.6 -> **34.4** | Individual spell overtuned (WR: 77.7%, Casts: 163, mult: 0.890) |
| `FLD` | Lightning | Ultimate | 17.7 -> **14.5** (-18.1%) | 42.6 -> **61.7** | 771.7 -> **909.2** | Status 'Stunned' beneficiaries undertuned (WR: 35.8%); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 3450). Increasing spread: b -18.0%, n +37.0% |
| `LFF` | Lightning | Conditional Strike | 2.6 -> **2.3** (-11.5%) | 311.4 -> **426.6** | 812.2 -> **983.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1385). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 31.8%, Casts: 1385, mult: 1.069) |
| `LFW` | Lightning | Buff / Sustain | 25.7 -> **23.2** (-9.7%) | - | 25.7 -> **23.2** | Individual spell overtuned (WR: 75.0%, Casts: 4745, mult: 0.902) |
| `LFE` | Lightning | Debuff / Control | 16.8 -> **15.6** (-7.1%) | - | 16.8 -> **15.6** | Individual spell overtuned (WR: 69.2%, Casts: 2204, mult: 0.927) |
| `LFL` | Lightning | Debuff / Control | 3.0 -> **2.7** (-10.0%) | 208.2 -> **297.0** | 627.6 -> **804.6** | Weather 'Darkness' beneficiaries undertuned (WR: 37.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 4878). Increasing spread: b -17.5%, n +36.0% |
| `LFD` | Lightning | Conditional Strike | 1.6 -> **1.4** (-12.5%) | 374.4 -> **512.3** | 600.6 -> **718.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 1604). Increasing spread: b -17.9%, n +36.8%; Individual spell undertuned (WR: 41.9%, Casts: 1604, mult: 1.028) |
| `FDF` | Blood | Conditional Strike | 1.2 -> **1.0** (-16.7%) | 328.3 -> **449.8** | 395.2 -> **450.8** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 825). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 63.0 -> **63.9** (+1.4%) | - | 63.0 -> **63.9** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Individual spell undertuned (WR: 38.0%, Casts: 653, mult: 1.043) |
| `FDE` | Blood | Setup - Weather | 53.8 -> **57.1** (+6.1%) | - | 53.8 -> **57.1** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Individual spell undertuned (WR: 26.5%, Casts: 358, mult: 1.092) |
| `FDL` | Blood | Debuff / Control | 1.0 -> **0.7** (-30.0%) | - | 1.0 -> **0.7** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Status 'Bleeding' appliers overtuned on own (WR: 81.7%) |
| `FDD` | Blood | Ultimate | 7.8 -> **8.4** (+7.7%) | 43.7 -> **43.1** | 348.7 -> **370.4** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Weather 'Darkness' beneficiaries undertuned (WR: 37.7%) |
| `DFF` | Blood | Conditional Strike | 1.8 -> **1.6** (-11.1%) | 406.4 -> **590.5** | 733.3 -> **946.4** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Status 'Bleeding' beneficiaries undertuned (WR: 28.6%) |
| `DFW` | Blood | Debuff / Control | 0.7 -> **0.5** (-28.6%) | - | 0.7 -> **0.5** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Status 'Bleeding' appliers overtuned on own (WR: 81.7%) |
| `DFE` | Blood | Buff / Sustain | 132.4 -> **149.8** (+13.1%) | - | 132.4 -> **149.8** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Individual spell undertuned (WR: 10.1%, Casts: 256, mult: 1.164) |
| `DFL` | Blood | Buff / Sustain | 9.3 -> **8.6** (-7.5%) | - | 9.3 -> **8.6** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Individual spell overtuned (WR: 64.2%, Casts: 8461, mult: 0.947) |
| `DFD` | Blood | Conditional Strike | 96.0 -> **107.1** (+11.6%) | 0.1 -> **0.1** | 105.6 -> **117.8** | Class Blood overtuned (WR: 57.0%, factor: 0.972); Condition triggers excessively (N=1 conditions, Trigger Rate: 100.0% vs 55% ceiling, WR: 60.0%). Compressing spread: b +19.0%, n -28.0% |
| `WEF` | Plants | Conditional Strike | 1.6 -> **1.2** (-25.0%) | 354.8 -> **468.4** | 569.3 -> **563.3** | Location 'Jungle' beneficiaries overtuned (WR: 59.1%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1202). Increasing spread: b -18.0%, n +37.0% |
| `WEW` | Plants | Debuff / Control | 55.7 -> **63.0** (+13.1%) | - | 55.7 -> **63.0** | Individual spell undertuned (WR: 17.4%, Casts: 223, mult: 1.131) |
| `WEE` | Plants | Setup - Location | 175.0 -> **184.4** (+5.4%) | - | 175.0 -> **184.4** | Location 'Jungle' appliers undertuned (WR: 42.4%, casts: 1434); Individual spell undertuned (WR: 42.4%, Casts: 1434, mult: 1.026) |
| `WEL` | Plants | Debuff / Control | 19.1 -> **14.8** (-22.5%) | - | 19.1 -> **14.8** | Status 'Entangled' appliers overtuned on own (WR: 84.9%); Individual spell overtuned (WR: 85.0%, Casts: 1987, mult: 0.858) |
| `WED` | Plants | Conditional Strike | 14.3 -> **15.4** (+7.7%) | 16.2 -> **15.2** | 246.0 -> **249.5** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1532, WR: 47.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 2.7 -> **2.5** (-7.4%) | 368.1 -> **559.0** | 996.6 -> **1400.0** | Weather 'Sunny' beneficiaries undertuned (WR: 20.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.5% vs 30% floor, Casts: 9519). Increasing spread: b -17.4%, n +35.7% |
| `EWW` | Plants | Debuff / Control | 2.5 -> **2.1** (-16.0%) | - | 2.5 -> **2.1** | Individual spell overtuned (WR: 96.0%, Casts: 2505, mult: 0.820) |
| `EWL` | Plants | Debuff / Control | 26.7 -> **23.6** (-11.6%) | - | 26.7 -> **23.6** | Individual spell overtuned (WR: 79.1%, Casts: 1757, mult: 0.884) |
| `EWD` | Plants | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 485.6 -> **656.3** | 243.3 -> **262.9** | Status 'Bleeding' appliers overtuned on own (WR: 81.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.2% vs 30% floor, Casts: 1304). Increasing spread: b -17.1%, n +35.2% |
| `WLF` | Fey | Conditional Strike | 2.2 -> **2.1** (-4.5%) | 251.4 -> **326.0** | 555.3 -> **686.7** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Status 'Cursed' beneficiaries overtuned (WR: 63.4%) |
| `WLW` | Fey | Debuff / Control | 18.6 -> **16.9** (-9.1%) | - | 18.6 -> **16.9** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Status 'Cursed' appliers overtuned on own (WR: 65.9%) |
| `WLE` | Fey | Setup - Location | 204.8 -> **275.5** (+34.5%) | - | 204.8 -> **275.5** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Location 'Enchanted Forest' appliers undertuned (WR: 10.7%, casts: 4589) |
| `WLL` | Fey | Direct Damage | 61.5 -> **59.2** (-3.7%) | - | 61.5 -> **59.2** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Individual spell overtuned (WR: 68.4%, Casts: 257, mult: 0.930) |
| `WLD` | Fey | Ultimate | 12.6 -> **10.7** (-15.1%) | 78.7 -> **116.7** | 1004.2 -> **1259.4** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Weather 'Darkness' beneficiaries undertuned (WR: 37.7%) |
| `LWF` | Fey | Debuff / Control | 4.5 -> **4.1** (-8.9%) | 295.9 -> **412.9** | 1336.0 -> **1697.0** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Location 'Enchanted Forest' beneficiaries undertuned (WR: 42.0%) |
| `LWW` | Fey | Debuff / Control | 56.3 -> **63.0** (+11.9%) | - | 56.3 -> **63.0** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Individual spell undertuned (WR: 28.7%, Casts: 232, mult: 1.082) |
| `LWL` | Fey | Debuff / Control | 151.5 -> **174.6** (+15.2%) | - | 151.5 -> **174.6** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Individual spell undertuned (WR: 21.3%, Casts: 851, mult: 1.114) |
| `LWD` | Fey | Conditional Strike | 3.6 -> **3.1** (-13.9%) | 328.3 -> **449.8** | 1185.5 -> **1397.5** | Class Fey undertuned (WR: 41.3%, factor: 1.035); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4690). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 3.2 -> **2.7** (-15.6%) | 588.6 -> **849.3** | 1886.7 -> **2295.8** | Weather 'Raining' beneficiaries undertuned (WR: 35.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 4401). Increasing spread: b -17.8%, n +36.5% |
| `WDW` | Ice | Buff / Sustain | 41.1 -> **46.6** (+13.4%) | - | 41.1 -> **46.6** | Individual spell undertuned (WR: 16.7%, Casts: 7300, mult: 1.134) |
| `WDE` | Ice | Setup - Weather | 72.5 -> **83.1** (+14.6%) | - | 72.5 -> **83.1** | Individual spell undertuned (WR: 14.0%, Casts: 5631, mult: 1.146) |
| `WDL` | Ice | Debuff / Control | 21.7 -> **20.6** (-5.1%) | - | 21.7 -> **20.6** | Individual spell overtuned (WR: 63.6%, Casts: 2906, mult: 0.950) |
| `WDD` | Ice | Ultimate | 13.2 -> **9.5** (-28.0%) | 41.8 -> **44.5** | 565.0 -> **432.2** | Weather 'Blizzard' beneficiaries overtuned (WR: 79.7%); Location 'Tundra' beneficiaries overtuned (WR: 79.7%) |
| `DWF` | Ice | Debuff / Control | 19.2 -> **18.4** (-4.2%) | - | 19.2 -> **18.4** | Individual spell overtuned (WR: 60.9%, Casts: 8925, mult: 0.961) |
| `DWW` | Ice | Debuff / Control | 23.4 -> **21.2** (-9.4%) | - | 23.4 -> **21.2** | Individual spell overtuned (WR: 74.2%, Casts: 8754, mult: 0.906) |
| `DWE` | Ice | Setup - Location | 144.2 -> **185.8** (+28.8%) | - | 144.2 -> **185.8** | Location 'Tundra' appliers undertuned (WR: 13.1%, casts: 2574); Individual spell undertuned (WR: 13.0%, Casts: 2574, mult: 1.151) |
| `DWL` | Ice | Debuff / Control | 23.0 -> **21.8** (-5.2%) | - | 23.0 -> **21.8** | Individual spell overtuned (WR: 64.3%, Casts: 8870, mult: 0.947) |
| `DWD` | Ice | Conditional Strike | 3.7 -> **3.1** (-16.2%) | 322.3 -> **471.4** | 1196.2 -> **1464.4** | Status 'Frosty' beneficiaries undertuned (WR: 30.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.6% vs 30% floor, Casts: 3956). Increasing spread: b -17.4%, n +35.7% |
| `ELF` | Wind | Conditional Strike | 4.9 -> **4.5** (-8.2%) | 478.1 -> **689.6** | 2347.6 -> **3107.7** | Class Wind undertuned (WR: 41.3%, factor: 1.035); Status 'Bleeding' beneficiaries undertuned (WR: 28.6%) |
| `ELW` | Wind | Debuff / Control | 29.9 -> **29.2** (-2.3%) | - | 29.9 -> **29.2** | Class Wind undertuned (WR: 41.3%, factor: 1.035); Individual spell overtuned (WR: 65.2%, Casts: 2781, mult: 0.944) |
| `ELE` | Wind | Setup - Weather | 63.4 -> **70.9** (+11.8%) | - | 63.4 -> **70.9** | Class Wind undertuned (WR: 41.3%, factor: 1.035); Individual spell undertuned (WR: 29.0%, Casts: 4629, mult: 1.081) |
| `ELL` | Wind | Buff / Sustain | 98.1 -> **94.1** (-4.1%) | - | 98.1 -> **94.1** | Class Wind undertuned (WR: 41.3%, factor: 1.035); Individual spell overtuned (WR: 69.0%, Casts: 495, mult: 0.927) |
| `ELD` | Wind | Conditional Strike | 4.6 -> **5.0** (+8.7%) | 528.3 -> **765.0** | 2434.8 -> **3830.0** | Class Wind undertuned (WR: 41.3%, factor: 1.035); Weather 'Raining' beneficiaries undertuned (WR: 35.8%) |
| `LEF` | Wind | Conditional Strike | 2.8 -> **2.5** (-10.7%) | 368.5 -> **520.8** | 1034.6 -> **1304.5** | Class Wind undertuned (WR: 41.3%, factor: 1.035); Status 'Burning' beneficiaries undertuned (WR: 39.5%) |
| `LEW` | Wind | Debuff / Control | 29.9 -> **27.5** (-8.0%) | - | 29.9 -> **27.5** | Class Wind undertuned (WR: 41.3%, factor: 1.035); Individual spell overtuned (WR: 77.8%, Casts: 5301, mult: 0.890) |
| `LEE` | Wind | Setup - Weather | 66.2 -> **80.7** (+21.9%) | - | 66.2 -> **80.7** | Class Wind undertuned (WR: 41.3%, factor: 1.035); Individual spell undertuned (WR: 6.9%, Casts: 3603, mult: 1.178) |
| `LEL` | Wind | Buff / Sustain | 106.8 -> **119.7** (+12.1%) | - | 106.8 -> **119.7** | Class Wind undertuned (WR: 41.3%, factor: 1.035); Individual spell undertuned (WR: 28.4%, Casts: 150, mult: 1.083) |
| `EDF` | Poison | Conditional Strike | 1.5 -> **1.2** (-20.0%) | 237.0 -> **306.1** | 357.0 -> **368.5** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.4% vs 30% floor, Casts: 447). Increasing spread: b -14.2%, n +29.2% |
| `EDW` | Poison | Debuff / Control | 5.7 -> **5.2** (-8.8%) | - | 5.7 -> **5.2** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 69.1%, Casts: 5460, mult: 0.927) |
| `EDE` | Poison | Setup - Location | 123.9 -> **112.3** (-9.4%) | - | 123.9 -> **112.3** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Location 'Swamp' appliers overtuned on own (WR: 60.1%) |
| `EDL` | Poison | Debuff / Control | 1.0 -> **0.8** (-20.0%) | - | 1.0 -> **0.8** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 90.0%, Casts: 3331, mult: 0.836) |
| `EDD` | Poison | Ultimate | 13.6 -> **15.0** (+10.3%) | 67.3 -> **72.0** | 928.9 -> **1095.0** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Status 'Bleeding' beneficiaries undertuned (WR: 28.6%) |
| `DEF` | Poison | Conditional Strike | 9.5 -> **8.4** (-11.6%) | 3.9 -> **5.0** | 46.6 -> **50.4** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.8% vs 30% floor, Casts: 289). Increasing spread: b -13.3%, n +27.2% |
| `DEW` | Poison | Debuff / Control | 6.0 -> **5.3** (-11.7%) | - | 6.0 -> **5.3** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 72.5%, Casts: 4137, mult: 0.913) |
| `DEE` | Poison | Debuff / Control | 15.6 -> **14.3** (-8.3%) | - | 15.6 -> **14.3** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 65.9%, Casts: 2219, mult: 0.940) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 483.9 -> **719.5** | 145.5 -> **216.2** | Class Poison overtuned (WR: 56.2%, factor: 0.975); Status 'Bleeding' beneficiaries undertuned (WR: 28.6%) |
| `DED` | Poison | Debuff / Control | 17.5 -> **17.1** (-2.3%) | - | 17.5 -> **17.1** | Class Poison overtuned (WR: 56.2%, factor: 0.975) |
| `LDF` | Cosmic | Debuff / Control | 24.0 -> **22.1** (-7.9%) | - | 24.0 -> **22.1** | Individual spell overtuned (WR: 70.5%, Casts: 341, mult: 0.921) |
| `LDW` | Cosmic | Debuff / Control | 14.3 -> **13.8** (-3.5%) | - | 14.3 -> **13.8** | Individual spell overtuned (WR: 59.4%, Casts: 4588, mult: 0.967) |
| `LDE` | Cosmic | Setup - Location | 36.8 -> **42.4** (+15.2%) | - | 36.8 -> **42.4** | Individual spell undertuned (WR: 12.5%, Casts: 3849, mult: 1.153) |
| `LDL` | Cosmic | Conditional Strike | 2.3 -> **2.1** (-8.7%) | 277.6 -> **374.9** | 640.8 -> **789.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.3% vs 30% floor, Casts: 515). Increasing spread: b -17.1%, n +35.1%; Individual spell undertuned (WR: 19.7%, Casts: 515, mult: 1.121) |
| `LDD` | Cosmic | Ultimate | 14.3 -> **15.7** (+9.8%) | 40.0 -> **37.6** | 586.3 -> **606.0** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 4529, WR: 45.8%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 45.8%, Casts: 4529, mult: 1.014) |
| `DLF` | Cosmic | Conditional Strike | 2.7 -> **2.4** (-11.1%) | 248.4 -> **340.2** | 673.4 -> **818.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2451). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 32.1%, Casts: 2451, mult: 1.068) |
| `DLW` | Cosmic | Direct Damage | 23.7 -> **21.5** (-9.3%) | - | 23.7 -> **21.5** | Individual spell overtuned (WR: 73.7%, Casts: 11427, mult: 0.908) |
| `DLE` | Cosmic | Direct Damage | 124.4 -> **138.0** (+10.9%) | - | 124.4 -> **138.0** | Individual spell undertuned (WR: 22.4%, Casts: 2670, mult: 1.109) |
| `DLL` | Cosmic | Conditional Strike | 2.9 -> **2.5** (-13.8%) | 239.6 -> **342.5** | 697.7 -> **858.8** | Weather 'Darkness' beneficiaries undertuned (WR: 37.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 1592). Increasing spread: b -17.6%, n +36.3% |
