# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T19:31:43Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 80.2s  
**Total Spells Tuned:** 106 / 125  

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
| **Earth** | 14,233 | 72.3% | 72.4% | 15.3 | Overtuned ⚠️ |
| **Fire** | 16,139 | 71.0% | 71.0% | 3.3 | Overtuned ⚠️ |
| **Blood** | 26,890 | 57.4% | 57.4% | 10.7 | Overtuned ⚠️ |
| **Beasts** | 25,887 | 56.7% | 56.7% | 3.1 | Overtuned ⚠️ |
| **Dark** | 9,190 | 55.0% | 55.0% | 2.3 | Overtuned ⚠️ |
| **Cosmic** | 29,219 | 54.7% | 54.8% | 4.7 | Overtuned ⚠️ |
| **Ice** | 27,930 | 54.5% | 54.5% | 3.1 | Overtuned ⚠️ |
| **Poison** | 45,534 | 50.8% | 50.8% | 2.0 | Balanced ✅ |
| **Plants** | 25,304 | 50.0% | 50.0% | 2.5 | Balanced ✅ |
| **Water** | 7,243 | 49.2% | 49.2% | 2.2 | Balanced ✅ |
| **Ghostfire** | 32,104 | 46.8% | 46.8% | 1.6 | Balanced ✅ |
| **Fey** | 30,027 | 43.3% | 43.3% | 2.3 | Undertuned ⚠️ |
| **Lightning** | 18,628 | 35.8% | 35.7% | 0.6 | Undertuned ⚠️ |
| **Light** | 14,235 | 34.1% | 34.1% | 1.4 | Undertuned ⚠️ |
| **Wind** | 36,211 | 32.2% | 32.2% | 1.7 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 17,607 (61.2%) | 3,317 (40.6%) | 9.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,185 (18.4%) | 6,960 (50.0%) | 0.7% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,020 (77.4%) | 8,005 (33.3%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 9,999 (86.3%) | 22,569 (39.3%) | 1.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 7,205 (57.5%) | 1,108 (39.9%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 4,244 (56.9%) | 3,816 (41.0%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 489 (22.7%) | 1,199 (48.5%) | 0.1% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 9.7 -> **8.0** (-17.5%) | - | 9.7 -> **8.0** | Class Fire overtuned (WR: 71.0%, factor: 0.916); Individual spell overtuned (WR: 75.0%, Casts: 7813, mult: 0.902) |
| `FFW` | Fire | Debuff / Control | 5.3 -> **4.4** (-17.0%) | - | 5.3 -> **4.4** | Class Fire overtuned (WR: 71.0%, factor: 0.916); Status 'Burning' appliers overtuned on own (WR: 77.4%) |
| `FFE` | Fire | Debuff / Control | 5.9 -> **4.7** (-20.3%) | - | 5.9 -> **4.7** | Class Fire overtuned (WR: 71.0%, factor: 0.916); Individual spell overtuned (WR: 84.2%, Casts: 2515, mult: 0.862) |
| `FFD` | Fire | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 15372.6 -> **22461.0** | 9224.2 -> **11231.0** | Class Fire overtuned (WR: 71.0%, factor: 0.916); Status 'Burning' beneficiaries undertuned (WR: 33.3%) |
| `WWF` | Water | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 7675.0 -> **11216.7** | 5373.2 -> **6730.6** | Status 'Burning' beneficiaries undertuned (WR: 33.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 48). Increasing spread: b -18.0%, n +37.0% |
| `WWE` | Water | Setup - Weather | 351.3 -> **426.6** (+21.4%) | - | 351.3 -> **426.6** | Weather 'Raining' appliers undertuned (WR: 22.7%, casts: 489); Individual spell undertuned (WR: 22.6%, Casts: 489, mult: 1.109) |
| `WWL` | Water | Buff / Sustain | 9.2 -> **8.4** (-8.7%) | - | 9.2 -> **8.4** | Individual spell overtuned (WR: 73.4%, Casts: 3769, mult: 0.909) |
| `WWD` | Water | Buff / Sustain | 25.3 -> **27.6** (+9.1%) | - | 25.3 -> **27.6** | Individual spell undertuned (WR: 26.3%, Casts: 1551, mult: 1.092) |
| `EEF` | Earth | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 8634.6 -> **11489.5** | 3454.2 -> **3447.2** | Class Earth overtuned (WR: 72.3%, factor: 0.911); Status 'Frosty' beneficiaries undertuned (WR: 40.6%) |
| `EEW` | Earth | Buff / Sustain | 25.3 -> **25.5** (+0.8%) | - | 25.3 -> **25.5** | Class Earth overtuned (WR: 72.3%, factor: 0.911); Individual spell undertuned (WR: 23.2%, Casts: 1020, mult: 1.106) |
| `LLF` | Light | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 5510.8 -> **7499.7** | 551.2 -> **750.1** | Class Light undertuned (WR: 34.1%, factor: 1.064); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.1% vs 30% floor, Casts: 1656). Increasing spread: b -17.6%, n +36.1% |
| `LLW` | Light | Debuff / Control | 8.9 -> **9.1** (+2.2%) | - | 8.9 -> **9.1** | Class Light undertuned (WR: 34.1%, factor: 1.064); Individual spell overtuned (WR: 60.1%, Casts: 1620, mult: 0.964) |
| `LLE` | Light | Setup - Weather | 736.5 -> **980.6** (+33.1%) | - | 736.5 -> **980.6** | Class Light undertuned (WR: 34.1%, factor: 1.064); Weather 'Sunny' appliers undertuned (WR: 18.4%, casts: 2185) |
| `LLL` | Light | Buff / Sustain | 5.6 -> **6.7** (+19.6%) | - | 5.6 -> **6.7** | Class Light undertuned (WR: 34.1%, factor: 1.064); Individual spell undertuned (WR: 17.5%, Casts: 4485, mult: 1.131) |
| `LLD` | Light | Ultimate | 5.3 -> **6.3** (+18.9%) | 516.2 -> **485.2** | 2741.2 -> **3063.1** | Class Light undertuned (WR: 34.1%, factor: 1.064); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 4289, WR: 40.9%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DDF` | Dark | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 7647.2 -> **10476.7** | 2294.5 -> **3143.3** | Class Dark overtuned (WR: 55.0%, factor: 0.980); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2888). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 10.1 -> **9.4** (-6.9%) | - | 10.1 -> **9.4** | Class Dark overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 63.5%, Casts: 284, mult: 0.950) |
| `DDE` | Dark | Setup - Weather | 560.3 -> **549.2** (-2.0%) | - | 560.3 -> **549.2** | Class Dark overtuned (WR: 55.0%, factor: 0.980) |
| `DDL` | Dark | Debuff / Control | 8.3 -> **7.4** (-10.8%) | - | 8.3 -> **7.4** | Class Dark overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 74.4%, Casts: 4386, mult: 0.905) |
| `DDD` | Dark | Debuff / Control | 3.4 -> **3.2** (-5.9%) | - | 3.4 -> **3.2** | Class Dark overtuned (WR: 55.0%, factor: 0.980); Individual spell overtuned (WR: 63.6%, Casts: 1140, mult: 0.950) |
| `FWW` | Ghostfire | Debuff / Control | 4.3 -> **4.4** (+2.3%) | - | 4.3 -> **4.4** | Individual spell undertuned (WR: 45.3%, Casts: 414, mult: 1.016) |
| `FWE` | Ghostfire | Setup - Location | 133.4 -> **129.3** (-3.1%) | - | 133.4 -> **129.3** | Individual spell overtuned (WR: 70.0%, Casts: 8, mult: 0.969) |
| `FWL` | Ghostfire | Debuff / Control | 8.8 -> **9.1** (+3.4%) | - | 8.8 -> **9.1** | Individual spell undertuned (WR: 39.1%, Casts: 8723, mult: 1.039) |
| `FWD` | Ghostfire | Ultimate | 2.0 -> **1.4** (-30.0%) | 329.2 -> **419.1** | 660.4 -> **588.1** | Status 'Cursed' beneficiaries undertuned (WR: 36.0%); Location 'Graveyard' beneficiaries overtuned (WR: 84.7%) |
| `WFF` | Ghostfire | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 20246.0 -> **25625.3** | 6074.1 -> **7687.9** | Status 'Bleeding' beneficiaries undertuned (WR: 39.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.8% vs 30% floor, Casts: 48). Increasing spread: b -10.5%, n +21.4% |
| `WFW` | Ghostfire | Debuff / Control | 3.4 -> **3.2** (-5.9%) | - | 3.4 -> **3.2** | Individual spell overtuned (WR: 67.7%, Casts: 11129, mult: 0.933) |
| `WFL` | Ghostfire | Buff / Sustain | 33.3 -> **37.0** (+11.1%) | - | 33.3 -> **37.0** | Individual spell undertuned (WR: 21.8%, Casts: 1859, mult: 1.112) |
| `WFD` | Ghostfire | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 6309.6 -> **8622.1** | 2524.2 -> **3449.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 8263). Increasing spread: b -17.8%, n +36.7%; Individual spell undertuned (WR: 25.6%, Casts: 8263, mult: 1.096) |
| `FEF` | Beasts | Debuff / Control | 8.7 -> **7.9** (-9.2%) | - | 8.7 -> **7.9** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 66.7%, Casts: 3275, mult: 0.937) |
| `FEW` | Beasts | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 12045.0 -> **17092.4** | 3613.8 -> **5128.0** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Status 'Entangled' beneficiaries undertuned (WR: 41.0%) |
| `FEE` | Beasts | Buff / Sustain | 181.5 -> **203.3** (+12.0%) | - | 181.5 -> **203.3** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell undertuned (WR: 12.9%, Casts: 4843, mult: 1.151) |
| `FEL` | Beasts | Buff / Sustain | 205.1 -> **194.3** (-5.3%) | - | 205.1 -> **194.3** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 57.6%, Casts: 3858, mult: 0.973) |
| `EFF` | Beasts | Debuff / Control | 0.5 -> **0.4** (-20.0%) | 6828.5 -> **9355.0** | 3414.8 -> **3742.4** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1025). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 72.3 -> **69.4** (-4.0%) | - | 72.3 -> **69.4** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 58.3%, Casts: 12, mult: 0.986) |
| `EFE` | Beasts | Buff / Sustain | 9.5 -> **8.2** (-13.7%) | - | 9.5 -> **8.2** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Individual spell overtuned (WR: 77.7%, Casts: 6218, mult: 0.890) |
| `EFD` | Beasts | Ultimate | 4.2 -> **4.4** (+4.8%) | 814.4 -> **792.9** | 3424.7 -> **3493.2** | Class Beasts overtuned (WR: 56.7%, factor: 0.973); Status 'Entangled' beneficiaries undertuned (WR: 41.0%) |
| `FLF` | Lightning | Conditional Strike | 0.5 -> **0.5** (+0.0%) | 14238.9 -> **20292.3** | 7119.9 -> **10146.6** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Status 'Stunned' beneficiaries undertuned (WR: 39.9%) |
| `FLW` | Lightning | Debuff / Control | 6.2 -> **5.8** (-6.5%) | - | 6.2 -> **5.8** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Status 'Stunned' appliers overtuned on own (WR: 57.5%) |
| `FLE` | Lightning | Setup - Weather | 225.1 -> **250.7** (+11.4%) | - | 225.1 -> **250.7** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Weather 'Storming' appliers undertuned (WR: 42.4%, casts: 144) |
| `FLL` | Lightning | Buff / Sustain | 36.4 -> **32.1** (-11.8%) | - | 36.4 -> **32.1** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Individual spell overtuned (WR: 90.4%, Casts: 767, mult: 0.834) |
| `FLD` | Lightning | Ultimate | 2.8 -> **2.4** (-14.3%) | 840.1 -> **1169.2** | 2355.1 -> **2808.5** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Status 'Stunned' beneficiaries undertuned (WR: 39.9%) |
| `LFF` | Lightning | Conditional Strike | 0.8 -> **0.8** (+0.0%) | 7251.0 -> **9933.9** | 5801.6 -> **7947.9** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 10422). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 23.1 -> **25.8** (+11.7%) | - | 23.1 -> **25.8** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Individual spell undertuned (WR: 34.4%, Casts: 3859, mult: 1.058) |
| `LFE` | Lightning | Debuff / Control | 5.6 -> **5.1** (-8.9%) | - | 5.6 -> **5.1** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Status 'Stunned' appliers overtuned on own (WR: 57.5%) |
| `LFL` | Lightning | Debuff / Control | 0.8 -> **0.6** (-25.0%) | 5724.4 -> **8200.0** | 4580.3 -> **4920.6** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Weather 'Darkness' beneficiaries undertuned (WR: 38.6%) |
| `LFD` | Lightning | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 6274.1 -> **8408.9** | 1882.5 -> **2523.0** | Class Lightning undertuned (WR: 35.8%, factor: 1.057); Status 'Stunned' appliers overtuned on own (WR: 57.5%) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 7647.2 -> **10476.7** | 1529.6 -> **2095.5** | Class Blood overtuned (WR: 57.4%, factor: 0.970); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1628). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 92.2 -> **89.5** (-2.9%) | - | 92.2 -> **89.5** | Class Blood overtuned (WR: 57.4%, factor: 0.970) |
| `FDE` | Blood | Setup - Weather | 53.1 -> **59.3** (+11.7%) | - | 53.1 -> **59.3** | Class Blood overtuned (WR: 57.4%, factor: 0.970); Individual spell undertuned (WR: 13.1%, Casts: 2798, mult: 1.150) |
| `FDD` | Blood | Ultimate | 3.1 -> **3.4** (+9.7%) | 189.0 -> **185.8** | 589.0 -> **635.1** | Class Blood overtuned (WR: 57.4%, factor: 0.970); Weather 'Darkness' beneficiaries undertuned (WR: 38.6%) |
| `DFF` | Blood | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 14617.2 -> **20598.1** | 5847.3 -> **6179.7** | Class Blood overtuned (WR: 57.4%, factor: 0.970); Status 'Bleeding' beneficiaries undertuned (WR: 39.3%) |
| `DFE` | Blood | Buff / Sustain | 369.7 -> **415.9** (+12.5%) | - | 369.7 -> **415.9** | Class Blood overtuned (WR: 57.4%, factor: 0.970); Individual spell undertuned (WR: 11.1%, Casts: 639, mult: 1.159) |
| `DFL` | Blood | Buff / Sustain | 4.3 -> **3.7** (-14.0%) | - | 4.3 -> **3.7** | Class Blood overtuned (WR: 57.4%, factor: 0.970); Individual spell overtuned (WR: 79.6%, Casts: 350, mult: 0.882) |
| `DFD` | Blood | Conditional Strike | 141.4 -> **145.0** (+2.5%) | 0.1 -> **0.1** | 155.5 -> **159.5** | Class Blood overtuned (WR: 57.4%, factor: 0.970); Condition triggers excessively (N=1 conditions, Trigger Rate: 80.2% vs 55% ceiling, WR: 90.5%). Compressing spread: b +26.8%, n -33.2% |
| `WEF` | Plants | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 9760.6 -> **13337.0** | 4880.8 -> **5335.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 702). Increasing spread: b -17.8%, n +36.6% |
| `WEW` | Plants | Debuff / Control | 167.1 -> **194.8** (+16.6%) | - | 167.1 -> **194.8** | Individual spell undertuned (WR: 9.6%, Casts: 3982, mult: 1.166) |
| `WEE` | Plants | Setup - Location | 1092.8 -> **1259.6** (+15.3%) | - | 1092.8 -> **1259.6** | Location 'Jungle' appliers undertuned (WR: 29.9%, casts: 1727); Individual spell undertuned (WR: 29.9%, Casts: 1727, mult: 1.077) |
| `WEL` | Plants | Debuff / Control | 7.3 -> **7.0** (-4.1%) | - | 7.3 -> **7.0** | Status 'Entangled' appliers overtuned on own (WR: 56.9%); Individual spell overtuned (WR: 56.9%, Casts: 4244, mult: 0.976) |
| `WED` | Plants | Conditional Strike | 6.8 -> **5.6** (-17.6%) | 83.3 -> **114.1** | 573.2 -> **644.6** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 8356). Increasing spread: b -18.0%, n +37.0% |
| `EWF` | Plants | Buff / Sustain | 1.0 -> **0.8** (-20.0%) | 13044.0 -> **17687.7** | 13045.0 -> **14151.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.7% vs 30% floor, Casts: 2671). Increasing spread: b -17.3%, n +35.6%; Individual spell overtuned (WR: 64.6%, Casts: 2671, mult: 0.946) |
| `EWL` | Plants | Debuff / Control | 11.0 -> **9.4** (-14.5%) | - | 11.0 -> **9.4** | Individual spell overtuned (WR: 86.0%, Casts: 2702, mult: 0.854) |
| `EWD` | Plants | Conditional Strike | 0.1 -> **0.1** (+0.0%) | 11122.6 -> **15730.7** | 1112.4 -> **1573.2** | Status 'Bleeding' appliers overtuned on own (WR: 86.3%); Status 'Entangled' beneficiaries undertuned (WR: 41.0%) |
| `WLF` | Fey | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 6197.6 -> **8966.9** | 4339.0 -> **5380.7** | Class Fey undertuned (WR: 43.3%, factor: 1.027); Status 'Cursed' beneficiaries undertuned (WR: 36.0%) |
| `WLE` | Fey | Setup - Location | 1777.8 -> **2040.7** (+14.8%) | - | 1777.8 -> **2040.7** | Class Fey undertuned (WR: 43.3%, factor: 1.027); Location 'Enchanted Forest' appliers undertuned (WR: 34.3%, casts: 211) |
| `WLL` | Fey | Direct Damage | 21.6 -> **20.6** (-4.6%) | - | 21.6 -> **20.6** | Class Fey undertuned (WR: 43.3%, factor: 1.027); Individual spell overtuned (WR: 68.7%, Casts: 2282, mult: 0.929) |
| `WLD` | Fey | Ultimate | 6.3 -> **5.2** (-17.5%) | 688.4 -> **965.5** | 4343.2 -> **5025.8** | Class Fey undertuned (WR: 43.3%, factor: 1.027); Weather 'Darkness' beneficiaries undertuned (WR: 38.6%) |
| `LWF` | Fey | Debuff / Control | 1.6 -> **1.3** (-18.8%) | 8907.2 -> **11947.6** | 14253.1 -> **15533.2** | Class Fey undertuned (WR: 43.3%, factor: 1.027); Location 'Enchanted Forest' beneficiaries overtuned (WR: 55.2%) |
| `LWW` | Fey | Debuff / Control | 140.5 -> **163.8** (+16.6%) | - | 140.5 -> **163.8** | Class Fey undertuned (WR: 43.3%, factor: 1.027); Individual spell undertuned (WR: 16.4%, Casts: 2744, mult: 1.136) |
| `LWL` | Fey | Debuff / Control | 614.5 -> **631.0** (+2.7%) | - | 614.5 -> **631.0** | Class Fey undertuned (WR: 43.3%, factor: 1.027) |
| `LWD` | Fey | Conditional Strike | 0.7 -> **0.7** (+0.0%) | 7647.2 -> **10476.7** | 5353.7 -> **7334.4** | Class Fey undertuned (WR: 43.3%, factor: 1.027); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 754). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 18764.4 -> **25707.2** | 5629.6 -> **5141.6** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Status 'Stunned' appliers overtuned on own (WR: 57.5%) |
| `WDW` | Ice | Buff / Sustain | 36.2 -> **29.7** (-18.0%) | - | 36.2 -> **29.7** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Status 'Frosty' appliers overtuned on own (WR: 61.2%) |
| `WDE` | Ice | Setup - Weather | 183.0 -> **192.9** (+5.4%) | - | 183.0 -> **192.9** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Individual spell undertuned (WR: 30.7%, Casts: 284, mult: 1.074) |
| `WDL` | Ice | Debuff / Control | 7.3 -> **6.5** (-11.0%) | - | 7.3 -> **6.5** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Status 'Frosty' appliers overtuned on own (WR: 61.2%) |
| `WDD` | Ice | Ultimate | 5.7 -> **6.1** (+7.0%) | 126.7 -> **123.0** | 727.9 -> **756.4** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Weather 'Blizzard' beneficiaries undertuned (WR: 45.9%) |
| `DWF` | Ice | Debuff / Control | 6.3 -> **5.8** (-7.9%) | - | 6.3 -> **5.8** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Status 'Frosty' appliers overtuned on own (WR: 61.2%) |
| `DWW` | Ice | Debuff / Control | 8.9 -> **8.3** (-6.7%) | - | 8.9 -> **8.3** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Individual spell overtuned (WR: 63.6%, Casts: 4261, mult: 0.950) |
| `DWE` | Ice | Setup - Location | 336.7 -> **425.6** (+26.4%) | - | 336.7 -> **425.6** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Location 'Tundra' appliers undertuned (WR: 13.3%, casts: 2906) |
| `DWL` | Ice | Debuff / Control | 9.3 -> **8.4** (-9.7%) | - | 9.3 -> **8.4** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Status 'Frosty' appliers overtuned on own (WR: 61.2%) |
| `DWD` | Ice | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 8182.9 -> **11426.1** | 4910.3 -> **5713.6** | Class Ice overtuned (WR: 54.5%, factor: 0.982); Status 'Frosty' beneficiaries undertuned (WR: 40.6%) |
| `ELF` | Wind | Conditional Strike | 1.9 -> **1.8** (-5.3%) | 16428.6 -> **22999.4** | 31216.2 -> **41400.7** | Class Wind undertuned (WR: 32.2%, factor: 1.071); Status 'Bleeding' beneficiaries undertuned (WR: 39.3%) |
| `ELW` | Wind | Debuff / Control | 22.2 -> **21.1** (-5.0%) | - | 22.2 -> **21.1** | Class Wind undertuned (WR: 32.2%, factor: 1.071); Individual spell overtuned (WR: 78.1%, Casts: 810, mult: 0.889) |
| `ELE` | Wind | Setup - Weather | 231.5 -> **285.2** (+23.2%) | - | 231.5 -> **285.2** | Class Wind undertuned (WR: 32.2%, factor: 1.071); Individual spell undertuned (WR: 13.1%, Casts: 5488, mult: 1.150) |
| `ELL` | Wind | Buff / Sustain | 106.5 -> **118.7** (+11.5%) | - | 106.5 -> **118.7** | Class Wind undertuned (WR: 32.2%, factor: 1.071); Individual spell undertuned (WR: 38.7%, Casts: 536, mult: 1.041) |
| `ELD` | Wind | Conditional Strike | 2.4 -> **2.0** (-16.7%) | 16553.3 -> **22654.6** | 39730.3 -> **45311.2** | Class Wind undertuned (WR: 32.2%, factor: 1.071); Weather 'Blizzard' appliers overtuned on own (WR: 57.4%) |
| `LEF` | Wind | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 16490.6 -> **24100.4** | 16491.6 -> **21691.3** | Class Wind undertuned (WR: 32.2%, factor: 1.071); Status 'Burning' beneficiaries undertuned (WR: 33.3%) |
| `LEW` | Wind | Debuff / Control | 17.6 -> **16.9** (-4.0%) | - | 17.6 -> **16.9** | Class Wind undertuned (WR: 32.2%, factor: 1.071); Individual spell overtuned (WR: 76.6%, Casts: 4335, mult: 0.895) |
| `LEE` | Wind | Setup - Weather | 331.2 -> **402.8** (+21.6%) | - | 331.2 -> **402.8** | Class Wind undertuned (WR: 32.2%, factor: 1.071); Individual spell undertuned (WR: 16.4%, Casts: 4204, mult: 1.136) |
| `LEL` | Wind | Buff / Sustain | 479.5 -> **572.2** (+19.3%) | - | 479.5 -> **572.2** | Class Wind undertuned (WR: 32.2%, factor: 1.071); Individual spell undertuned (WR: 21.3%, Casts: 5066, mult: 1.114) |
| `EDF` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 4834.6 -> **6596.8** | 967.1 -> **1319.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.7% vs 30% floor, Casts: 4386). Increasing spread: b -17.7%, n +36.4%; Individual spell undertuned (WR: 13.9%, Casts: 4386, mult: 1.147) |
| `EDW` | Poison | Debuff / Control | 2.5 -> **2.4** (-4.0%) | - | 2.5 -> **2.4** | Individual spell overtuned (WR: 64.3%, Casts: 4077, mult: 0.947) |
| `EDE` | Poison | Setup - Location | 428.2 -> **517.5** (+20.9%) | - | 428.2 -> **517.5** | Location 'Swamp' appliers undertuned (WR: 23.3%, casts: 4703); Individual spell undertuned (WR: 23.3%, Casts: 4703, mult: 1.105) |
| `EDD` | Poison | Ultimate | 4.9 -> **5.4** (+10.2%) | 604.7 -> **611.4** | 2967.9 -> **3307.0** | Status 'Bleeding' beneficiaries undertuned (WR: 39.3%); Location 'Swamp' beneficiaries undertuned (WR: 42.1%) |
| `DEF` | Poison | Conditional Strike | 1.3 -> **1.4** (+7.7%) | 68.8 -> **59.4** | 90.7 -> **84.6** | Condition triggers excessively (N=1 conditions, Trigger Rate: 61.7% vs 55% ceiling, WR: 58.1%). Compressing spread: b +9.7%, n -13.6%; Individual spell overtuned (WR: 58.1%, Casts: 81, mult: 0.972) |
| `DEE` | Poison | Debuff / Control | 8.1 -> **6.9** (-14.8%) | - | 8.1 -> **6.9** | Individual spell overtuned (WR: 85.7%, Casts: 5334, mult: 0.855) |
| `DEL` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 20576.6 -> **29375.0** | 6173.3 -> **8812.8** | Status 'Bleeding' beneficiaries undertuned (WR: 39.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 835). Increasing spread: b -18.0%, n +36.9% |
| `DED` | Poison | Debuff / Control | 9.6 -> **9.1** (-5.2%) | - | 9.6 -> **9.1** | Individual spell overtuned (WR: 63.8%, Casts: 4739, mult: 0.949) |
| `LDF` | Cosmic | Debuff / Control | 14.9 -> **12.5** (-16.1%) | - | 14.9 -> **12.5** | Class Cosmic overtuned (WR: 54.7%, factor: 0.981); Individual spell overtuned (WR: 86.1%, Casts: 6853, mult: 0.854) |
| `LDW` | Cosmic | Debuff / Control | 5.2 -> **4.5** (-13.5%) | - | 5.2 -> **4.5** | Class Cosmic overtuned (WR: 54.7%, factor: 0.981); Status 'Stunned' appliers overtuned on own (WR: 57.5%) |
| `LDE` | Cosmic | Setup - Location | 83.4 -> **94.2** (+12.9%) | - | 83.4 -> **94.2** | Class Cosmic overtuned (WR: 54.7%, factor: 0.981); Individual spell undertuned (WR: 12.9%, Casts: 3168, mult: 1.151) |
| `LDL` | Cosmic | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 6363.8 -> **8718.4** | 3818.9 -> **4359.7** | Class Cosmic overtuned (WR: 54.7%, factor: 0.981); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2015). Increasing spread: b -18.0%, n +37.0% |
| `LDD` | Cosmic | Ultimate | 5.7 -> **4.6** (-19.3%) | 206.5 -> **282.9** | 1182.8 -> **1305.9** | Class Cosmic overtuned (WR: 54.7%, factor: 0.981); Conditional payoff under-triggered (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 4199). Increasing spread: b -18.0%, n +37.0% |
| `DLF` | Cosmic | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 5775.9 -> **7888.4** | 2888.4 -> **3155.8** | Class Cosmic overtuned (WR: 54.7%, factor: 0.981); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 3535). Increasing spread: b -17.8%, n +36.6% |
| `DLW` | Cosmic | Direct Damage | 10.2 -> **8.5** (-16.7%) | - | 10.2 -> **8.5** | Class Cosmic overtuned (WR: 54.7%, factor: 0.981); Individual spell overtuned (WR: 87.9%, Casts: 1093, mult: 0.845) |
| `DLE` | Cosmic | Direct Damage | 296.4 -> **282.2** (-4.8%) | - | 296.4 -> **282.2** | Class Cosmic overtuned (WR: 54.7%, factor: 0.981); Individual spell overtuned (WR: 58.4%, Casts: 1188, mult: 0.970) |
| `DLL` | Cosmic | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 6657.2 -> **9536.3** | 3994.9 -> **4768.6** | Class Cosmic overtuned (WR: 54.7%, factor: 0.981); Weather 'Darkness' beneficiaries undertuned (WR: 38.6%) |
