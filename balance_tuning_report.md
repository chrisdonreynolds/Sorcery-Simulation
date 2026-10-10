# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T16:32:28Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 123.7s  
**Total Spells Tuned:** 116 / 125  

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
| **Light** | 14,089 | 63.8% | 63.8% | 4.4 | Overtuned ⚠️ |
| **Blood** | 17,920 | 60.7% | 60.7% | 5.3 | Overtuned ⚠️ |
| **Water** | 16,451 | 60.4% | 60.4% | 12.3 | Overtuned ⚠️ |
| **Poison** | 22,418 | 57.0% | 57.0% | 5.7 | Overtuned ⚠️ |
| **Fire** | 30,126 | 56.1% | 56.1% | 9.8 | Overtuned ⚠️ |
| **Dark** | 16,378 | 55.8% | 55.9% | 7.3 | Overtuned ⚠️ |
| **Ghostfire** | 21,226 | 53.4% | 53.4% | 3.6 | Balanced ✅ |
| **Fey** | 24,424 | 50.1% | 50.1% | 8.9 | Balanced ✅ |
| **Cosmic** | 30,102 | 48.3% | 48.3% | 9.2 | Balanced ✅ |
| **Ice** | 43,716 | 47.3% | 47.3% | 7.6 | Balanced ✅ |
| **Plants** | 16,230 | 46.9% | 46.9% | 4.4 | Balanced ✅ |
| **Lightning** | 22,052 | 45.2% | 45.2% | 5.0 | Undertuned ⚠️ |
| **Beasts** | 28,938 | 44.9% | 44.9% | 6.0 | Undertuned ⚠️ |
| **Earth** | 25,472 | 42.8% | 42.8% | 8.0 | Undertuned ⚠️ |
| **Wind** | 18,007 | 33.9% | 33.8% | 5.5 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 21,738 (58.5%) | 10,019 (22.3%) | 7.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 464 (27.2%) | 10,373 (40.3%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 7,330 (58.8%) | 8,857 (26.3%) | 3.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 11,792 (84.1%) | 13,567 (32.8%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 25,075 (36.7%) | 5,361 (41.0%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,842 (65.7%) | 7,967 (43.2%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 818 (1.9%) | 7,884 (19.4%) | 0.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFF` | Fire | Direct Damage | 27.3 -> **25.5** (-6.6%) | - | 27.3 -> **25.5** | Class Fire overtuned (WR: 56.1%, factor: 0.976); Individual spell overtuned (WR: 61.7%, Casts: 5899, mult: 0.958) |
| `FFW` | Fire | Debuff / Control | 17.5 -> **16.5** (-5.7%) | - | 17.5 -> **16.5** | Class Fire overtuned (WR: 56.1%, factor: 0.976); Status 'Burning' appliers overtuned on own (WR: 58.8%) |
| `FFE` | Fire | Debuff / Control | 14.6 -> **13.6** (-6.8%) | - | 14.6 -> **13.6** | Class Fire overtuned (WR: 56.1%, factor: 0.976); Individual spell overtuned (WR: 63.1%, Casts: 13590, mult: 0.952) |
| `FFD` | Fire | Conditional Strike | 3.0 -> **2.7** (-10.0%) | 116.5 -> **172.0** | 352.5 -> **467.1** | Class Fire overtuned (WR: 56.1%, factor: 0.976); Status 'Burning' beneficiaries undertuned (WR: 26.3%) |
| `WWF` | Water | Conditional Strike | 3.5 -> **3.0** (-14.3%) | 88.2 -> **128.6** | 312.2 -> **388.8** | Class Water overtuned (WR: 60.4%, factor: 0.959); Status 'Burning' beneficiaries undertuned (WR: 26.3%) |
| `WWE` | Water | Setup - Weather | 124.1 -> **157.2** (+26.7%) | - | 124.1 -> **157.2** | Class Water overtuned (WR: 60.4%, factor: 0.959); Weather 'Raining' appliers undertuned (WR: 1.9%, casts: 818) |
| `WWL` | Water | Buff / Sustain | 41.1 -> **34.8** (-15.3%) | - | 41.1 -> **34.8** | Class Water overtuned (WR: 60.4%, factor: 0.959); Individual spell overtuned (WR: 79.3%, Casts: 10183, mult: 0.884) |
| `WWD` | Water | Buff / Sustain | 46.3 -> **43.8** (-5.4%) | - | 46.3 -> **43.8** | Class Water overtuned (WR: 60.4%, factor: 0.959); Individual spell overtuned (WR: 54.0%, Casts: 778, mult: 0.987) |
| `EEF` | Earth | Conditional Strike | 4.0 -> **4.1** (+2.5%) | 133.9 -> **196.7** | 539.6 -> **810.6** | Class Earth undertuned (WR: 42.8%, factor: 1.029); Status 'Frosty' beneficiaries undertuned (WR: 22.3%) |
| `EEW` | Earth | Buff / Sustain | 47.1 -> **44.7** (-5.1%) | - | 47.1 -> **44.7** | Class Earth undertuned (WR: 42.8%, factor: 1.029); Individual spell overtuned (WR: 70.4%, Casts: 1026, mult: 0.922) |
| `EED` | Earth | Direct Damage | 2.9 -> **2.8** (-3.4%) | - | 2.9 -> **2.8** | Class Earth undertuned (WR: 42.8%, factor: 1.029); Individual spell overtuned (WR: 68.5%, Casts: 7464, mult: 0.929) |
| `LLF` | Light | Conditional Strike | 0.2 -> **0.1** (-50.0%) | 104.3 -> **142.4** | 21.1 -> **14.3** | Class Light overtuned (WR: 63.8%, factor: 0.945); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 4848). Increasing spread: b -17.8%, n +36.5% |
| `LLW` | Light | Debuff / Control | 22.0 -> **20.8** (-5.5%) | - | 22.0 -> **20.8** | Class Light overtuned (WR: 63.8%, factor: 0.945) |
| `LLE` | Light | Setup - Weather | 168.0 -> **186.6** (+11.1%) | - | 168.0 -> **186.6** | Class Light overtuned (WR: 63.8%, factor: 0.945); Weather 'Sunny' appliers undertuned (WR: 27.2%, casts: 464) |
| `LLL` | Light | Buff / Sustain | 12.9 -> **10.7** (-17.1%) | - | 12.9 -> **10.7** | Class Light overtuned (WR: 63.8%, factor: 0.945); Individual spell overtuned (WR: 81.4%, Casts: 2267, mult: 0.874) |
| `LLD` | Light | Ultimate | 18.7 -> **14.5** (-22.5%) | 27.4 -> **39.0** | 531.1 -> **580.0** | Class Light overtuned (WR: 63.8%, factor: 0.945); Weather 'Sunny' beneficiaries undertuned (WR: 40.3%) |
| `DDF` | Dark | Conditional Strike | 1.7 -> **1.6** (-5.9%) | 127.7 -> **174.9** | 218.8 -> **281.4** | Class Dark overtuned (WR: 55.8%, factor: 0.977); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 199). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 30.4 -> **28.3** (-6.9%) | - | 30.4 -> **28.3** | Class Dark overtuned (WR: 55.8%, factor: 0.977); Individual spell overtuned (WR: 62.8%, Casts: 7218, mult: 0.953) |
| `DDE` | Dark | Setup - Weather | 69.4 -> **87.1** (+25.5%) | - | 69.4 -> **87.1** | Class Dark overtuned (WR: 55.8%, factor: 0.977); Weather 'Darkness' appliers undertuned (WR: 13.7%, casts: 3856) |
| `DDL` | Dark | Debuff / Control | 16.7 -> **16.1** (-3.6%) | - | 16.7 -> **16.1** | Class Dark overtuned (WR: 55.8%, factor: 0.977); Individual spell overtuned (WR: 54.2%, Casts: 309, mult: 0.986) |
| `DDD` | Dark | Debuff / Control | 7.9 -> **6.7** (-15.2%) | - | 7.9 -> **6.7** | Class Dark overtuned (WR: 55.8%, factor: 0.977); Individual spell overtuned (WR: 81.4%, Casts: 4796, mult: 0.874) |
| `FWF` | Ghostfire | Debuff / Control | 4.9 -> **4.1** (-16.3%) | - | 4.9 -> **4.1** | Status 'Burning' appliers overtuned on own (WR: 58.8%); Individual spell overtuned (WR: 86.2%, Casts: 653, mult: 0.853) |
| `FWW` | Ghostfire | Debuff / Control | 11.4 -> **10.8** (-5.3%) | - | 11.4 -> **10.8** | Status 'Cursed' appliers overtuned on own (WR: 66.1%) |
| `FWE` | Ghostfire | Setup - Location | 73.7 -> **89.6** (+21.6%) | - | 73.7 -> **89.6** | Location 'Graveyard' appliers undertuned (WR: 22.6%, casts: 270); Individual spell undertuned (WR: 22.3%, Casts: 270, mult: 1.109) |
| `FWL` | Ghostfire | Debuff / Control | 29.5 -> **29.1** (-1.4%) | - | 29.5 -> **29.1** | Status 'Cursed' appliers overtuned on own (WR: 66.1%); Individual spell undertuned (WR: 37.9%, Casts: 619, mult: 1.044) |
| `FWD` | Ghostfire | Ultimate | 13.7 -> **15.4** (+12.4%) | 28.9 -> **29.6** | 409.6 -> **471.2** | Status 'Cursed' beneficiaries undertuned (WR: 39.2%); Location 'Graveyard' beneficiaries undertuned (WR: 39.0%) |
| `WFF` | Ghostfire | Conditional Strike | 2.1 -> **1.9** (-9.5%) | 173.1 -> **253.2** | 365.6 -> **483.0** | Status 'Bleeding' beneficiaries undertuned (WR: 32.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1709). Increasing spread: b -18.0%, n +36.9% |
| `WFW` | Ghostfire | Debuff / Control | 10.2 -> **9.1** (-10.8%) | - | 10.2 -> **9.1** | Individual spell overtuned (WR: 76.8%, Casts: 3779, mult: 0.894) |
| `WFE` | Ghostfire | Debuff / Control | 2.5 -> **1.9** (-24.0%) | - | 2.5 -> **1.9** | Status 'Bleeding' appliers overtuned on own (WR: 84.1%); Individual spell overtuned (WR: 88.8%, Casts: 4220, mult: 0.841) |
| `WFL` | Ghostfire | Buff / Sustain | 42.7 -> **41.3** (-3.3%) | - | 42.7 -> **41.3** | Individual spell overtuned (WR: 59.4%, Casts: 185, mult: 0.967) |
| `WFD` | Ghostfire | Conditional Strike | 2.2 -> **2.1** (-4.5%) | 110.5 -> **151.2** | 245.3 -> **319.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 3659). Increasing spread: b -17.9%, n +36.8%; Individual spell undertuned (WR: 14.4%, Casts: 3659, mult: 1.145) |
| `FEF` | Beasts | Debuff / Control | 16.3 -> **16.6** (+1.8%) | - | 16.3 -> **16.6** | Class Beasts undertuned (WR: 44.9%, factor: 1.020) |
| `FEW` | Beasts | Conditional Strike | 3.5 -> **3.3** (-5.7%) | 174.9 -> **246.2** | 615.6 -> **815.8** | Class Beasts undertuned (WR: 44.9%, factor: 1.020); Status 'Entangled' beneficiaries undertuned (WR: 43.2%) |
| `FEE` | Beasts | Buff / Sustain | 39.8 -> **44.9** (+12.8%) | - | 39.8 -> **44.9** | Class Beasts undertuned (WR: 44.9%, factor: 1.020); Individual spell undertuned (WR: 23.3%, Casts: 2485, mult: 1.105) |
| `FEL` | Beasts | Buff / Sustain | 83.6 -> **93.2** (+11.5%) | - | 83.6 -> **93.2** | Class Beasts undertuned (WR: 44.9%, factor: 1.020); Individual spell undertuned (WR: 26.2%, Casts: 2515, mult: 1.093) |
| `EFF` | Beasts | Debuff / Control | 4.0 -> **3.1** (-22.5%) | 115.0 -> **157.6** | 464.0 -> **491.7** | Class Beasts undertuned (WR: 44.9%, factor: 1.020); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 64). Increasing spread: b -18.0%, n +37.0% |
| `EFW` | Beasts | Buff / Sustain | 39.4 -> **42.1** (+6.9%) | - | 39.4 -> **42.1** | Class Beasts undertuned (WR: 44.9%, factor: 1.020); Individual spell undertuned (WR: 30.0%, Casts: 18, mult: 1.046) |
| `EFE` | Beasts | Buff / Sustain | 26.0 -> **26.5** (+1.9%) | - | 26.0 -> **26.5** | Class Beasts undertuned (WR: 44.9%, factor: 1.020) |
| `EFL` | Beasts | Buff / Sustain | 3.7 -> **3.1** (-16.2%) | - | 3.7 -> **3.1** | Class Beasts undertuned (WR: 44.9%, factor: 1.020); Individual spell overtuned (WR: 91.2%, Casts: 2967, mult: 0.830) |
| `EFD` | Beasts | Ultimate | 11.9 -> **13.1** (+10.1%) | 92.6 -> **89.4** | 1113.8 -> **1184.2** | Class Beasts undertuned (WR: 44.9%, factor: 1.020); Status 'Entangled' beneficiaries undertuned (WR: 43.2%) |
| `FLF` | Lightning | Conditional Strike | 2.7 -> **2.3** (-14.8%) | 146.3 -> **207.7** | 397.7 -> **480.0** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' beneficiaries undertuned (WR: 41.0%) |
| `FLW` | Lightning | Debuff / Control | 22.2 -> **21.6** (-2.7%) | - | 22.2 -> **21.6** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' appliers undertuned (WR: 36.7%, casts: 25075) |
| `FLE` | Lightning | Setup - Weather | 33.5 -> **45.1** (+34.6%) | - | 33.5 -> **45.1** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Weather 'Storming' appliers undertuned (WR: 5.0%, casts: 3490) |
| `FLL` | Lightning | Buff / Sustain | 38.8 -> **39.0** (+0.5%) | - | 38.8 -> **39.0** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Individual spell overtuned (WR: 54.1%, Casts: 280, mult: 0.987) |
| `FLD` | Lightning | Ultimate | 16.8 -> **19.1** (+13.7%) | 31.8 -> **32.1** | 551.0 -> **632.2** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' beneficiaries undertuned (WR: 41.0%) |
| `LFF` | Lightning | Conditional Strike | 3.2 -> **3.0** (-6.3%) | 121.1 -> **165.9** | 390.7 -> **500.7** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1510). Increasing spread: b -18.0%, n +37.0% |
| `LFW` | Lightning | Buff / Sustain | 25.3 -> **25.8** (+2.0%) | - | 25.3 -> **25.8** | Class Lightning undertuned (WR: 45.2%, factor: 1.019) |
| `LFE` | Lightning | Debuff / Control | 18.2 -> **19.0** (+4.4%) | - | 18.2 -> **19.0** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' appliers undertuned (WR: 36.7%, casts: 25075) |
| `LFL` | Lightning | Debuff / Control | 4.6 -> **3.8** (-17.4%) | 97.4 -> **114.3** | 452.6 -> **438.1** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Weather 'Darkness' beneficiaries overtuned (WR: 54.3%) |
| `LFD` | Lightning | Conditional Strike | 2.7 -> **2.4** (-11.1%) | 145.6 -> **199.5** | 395.8 -> **481.2** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' appliers undertuned (WR: 36.7%, casts: 25075) |
| `FDF` | Blood | Conditional Strike | 2.0 -> **1.6** (-20.0%) | 127.7 -> **174.9** | 257.4 -> **281.4** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 263). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 79.4 -> **81.7** (+2.9%) | - | 79.4 -> **81.7** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Individual spell undertuned (WR: 30.4%, Casts: 471, mult: 1.075) |
| `FDE` | Blood | Setup - Weather | 54.8 -> **56.4** (+2.9%) | - | 54.8 -> **56.4** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Individual spell undertuned (WR: 30.4%, Casts: 2302, mult: 1.075) |
| `FDL` | Blood | Debuff / Control | 2.3 -> **1.7** (-26.1%) | - | 2.3 -> **1.7** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Status 'Bleeding' appliers overtuned on own (WR: 84.1%) |
| `FDD` | Blood | Ultimate | 9.1 -> **9.6** (+5.5%) | 35.5 -> **32.8** | 332.1 -> **324.5** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Weather 'Darkness' beneficiaries overtuned (WR: 54.3%) |
| `DFF` | Blood | Conditional Strike | 3.5 -> **3.1** (-11.4%) | 137.3 -> **197.5** | 484.1 -> **615.4** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Status 'Bleeding' beneficiaries undertuned (WR: 32.8%) |
| `DFW` | Blood | Debuff / Control | 1.8 -> **1.3** (-27.8%) | - | 1.8 -> **1.3** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Status 'Bleeding' appliers overtuned on own (WR: 84.1%) |
| `DFE` | Blood | Buff / Sustain | 109.5 -> **114.1** (+4.2%) | - | 109.5 -> **114.1** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Individual spell undertuned (WR: 27.2%, Casts: 779, mult: 1.089) |
| `DFL` | Blood | Buff / Sustain | 13.8 -> **12.8** (-7.2%) | - | 13.8 -> **12.8** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Individual spell overtuned (WR: 58.5%, Casts: 4736, mult: 0.970) |
| `DFD` | Blood | Conditional Strike | 82.0 -> **88.7** (+8.2%) | 0.1 -> **0.1** | 90.2 -> **97.6** | Class Blood overtuned (WR: 60.7%, factor: 0.957); Condition triggers excessively (N=1 conditions, Trigger Rate: 93.0% vs 55% ceiling, WR: 62.3%). Compressing spread: b +18.3%, n -26.4% |
| `WEF` | Plants | Conditional Strike | 2.6 -> **2.3** (-11.5%) | 144.3 -> **197.7** | 377.8 -> **457.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 253). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 34.3%, Casts: 253, mult: 1.059) |
| `WEW` | Plants | Debuff / Control | 43.0 -> **44.4** (+3.3%) | - | 43.0 -> **44.4** | Individual spell undertuned (WR: 40.6%, Casts: 456, mult: 1.033) |
| `WEE` | Plants | Setup - Location | 88.6 -> **100.0** (+12.9%) | - | 88.6 -> **100.0** | Location 'Jungle' appliers undertuned (WR: 32.9%, casts: 409); Individual spell undertuned (WR: 32.8%, Casts: 409, mult: 1.065) |
| `WEL` | Plants | Debuff / Control | 28.8 -> **25.6** (-11.1%) | - | 28.8 -> **25.6** | Status 'Entangled' appliers overtuned on own (WR: 65.7%); Individual spell overtuned (WR: 65.8%, Casts: 1842, mult: 0.941) |
| `WED` | Plants | Conditional Strike | 20.2 -> **21.8** (+7.9%) | 9.2 -> **8.6** | 206.0 -> **209.3** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1391, WR: 48.2%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `EWF` | Plants | Buff / Sustain | 3.6 -> **3.1** (-13.9%) | 118.1 -> **168.1** | 428.8 -> **524.2** | Weather 'Sunny' beneficiaries undertuned (WR: 40.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 6341). Increasing spread: b -18.0%, n +37.0% |
| `EWW` | Plants | Debuff / Control | 4.2 -> **3.4** (-19.0%) | - | 4.2 -> **3.4** | Individual spell overtuned (WR: 94.2%, Casts: 1812, mult: 0.820) |
| `EWL` | Plants | Debuff / Control | 40.3 -> **33.6** (-16.6%) | - | 40.3 -> **33.6** | Individual spell overtuned (WR: 90.5%, Casts: 839, mult: 0.834) |
| `EWD` | Plants | Conditional Strike | 0.9 -> **0.7** (-22.2%) | 171.2 -> **241.0** | 155.0 -> **169.4** | Status 'Bleeding' appliers overtuned on own (WR: 84.1%); Status 'Entangled' beneficiaries undertuned (WR: 43.2%) |
| `WLF` | Fey | Conditional Strike | 3.2 -> **2.6** (-18.8%) | 92.9 -> **132.8** | 300.5 -> **347.9** | Status 'Cursed' beneficiaries undertuned (WR: 39.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 12). Increasing spread: b -18.0%, n +37.0% |
| `WLW` | Fey | Debuff / Control | 28.3 -> **23.7** (-16.3%) | - | 28.3 -> **23.7** | Status 'Cursed' appliers overtuned on own (WR: 66.1%); Individual spell overtuned (WR: 78.3%, Casts: 6415, mult: 0.888) |
| `WLE` | Fey | Setup - Location | 133.5 -> **151.0** (+13.1%) | - | 133.5 -> **151.0** | Location 'Enchanted Forest' appliers undertuned (WR: 32.6%, casts: 1003); Individual spell undertuned (WR: 32.5%, Casts: 1003, mult: 1.066) |
| `WLL` | Fey | Direct Damage | 82.0 -> **79.1** (-3.5%) | - | 82.0 -> **79.1** | Individual spell overtuned (WR: 59.8%, Casts: 802, mult: 0.965) |
| `WLD` | Fey | Ultimate | 23.2 -> **18.7** (-19.4%) | 30.0 -> **40.4** | 719.2 -> **774.2** | Weather 'Darkness' beneficiaries overtuned (WR: 54.3%); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 7497). Increasing spread: b -18.0%, n +37.0% |
| `LWF` | Fey | Debuff / Control | 7.1 -> **6.1** (-14.1%) | 116.0 -> **158.9** | 830.7 -> **975.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1913). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 35.0%, Casts: 1913, mult: 1.056) |
| `LWW` | Fey | Debuff / Control | 58.7 -> **57.0** (-2.9%) | - | 58.7 -> **57.0** | Individual spell overtuned (WR: 58.5%, Casts: 106, mult: 0.970) |
| `LWL` | Fey | Debuff / Control | 102.5 -> **115.0** (+12.2%) | - | 102.5 -> **115.0** | Individual spell undertuned (WR: 18.6%, Casts: 47, mult: 1.122) |
| `LWD` | Fey | Conditional Strike | 5.3 -> **4.8** (-9.4%) | 127.7 -> **174.9** | 682.1 -> **844.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 4122). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 23.7%, Casts: 4122, mult: 1.103) |
| `WDF` | Ice | Conditional Strike | 4.3 -> **4.2** (-2.3%) | 177.6 -> **273.1** | 768.0 -> **1151.2** | Status 'Stunned' appliers undertuned (WR: 36.7%, casts: 25075); Weather 'Raining' beneficiaries undertuned (WR: 19.4%) |
| `WDW` | Ice | Buff / Sustain | 30.7 -> **33.4** (+8.8%) | - | 30.7 -> **33.4** | Status 'Frosty' appliers overtuned on own (WR: 58.5%); Individual spell undertuned (WR: 19.8%, Casts: 4064, mult: 1.120) |
| `WDE` | Ice | Setup - Weather | 46.6 -> **52.6** (+12.9%) | - | 46.6 -> **52.6** | Individual spell undertuned (WR: 17.9%, Casts: 5489, mult: 1.129) |
| `WDL` | Ice | Debuff / Control | 28.6 -> **25.1** (-12.2%) | - | 28.6 -> **25.1** | Status 'Frosty' appliers overtuned on own (WR: 58.5%); Individual spell overtuned (WR: 74.6%, Casts: 2185, mult: 0.904) |
| `WDD` | Ice | Ultimate | 17.3 -> **19.5** (+12.7%) | 22.5 -> **23.2** | 406.6 -> **471.9** | Weather 'Blizzard' beneficiaries undertuned (WR: 38.1%); Location 'Tundra' beneficiaries undertuned (WR: 38.1%) |
| `DWF` | Ice | Debuff / Control | 25.4 -> **23.3** (-8.3%) | - | 25.4 -> **23.3** | Status 'Frosty' appliers overtuned on own (WR: 58.5%); Individual spell overtuned (WR: 65.0%, Casts: 8241, mult: 0.944) |
| `DWW` | Ice | Debuff / Control | 29.0 -> **26.4** (-9.0%) | - | 29.0 -> **26.4** | Individual spell overtuned (WR: 72.8%, Casts: 5874, mult: 0.912) |
| `DWE` | Ice | Setup - Location | 85.6 -> **102.7** (+20.0%) | - | 85.6 -> **102.7** | Location 'Tundra' appliers undertuned (WR: 24.4%, casts: 597); Individual spell undertuned (WR: 24.3%, Casts: 597, mult: 1.101) |
| `DWL` | Ice | Debuff / Control | 28.2 -> **25.5** (-9.6%) | - | 28.2 -> **25.5** | Status 'Frosty' appliers overtuned on own (WR: 58.5%); Individual spell overtuned (WR: 67.9%, Casts: 7248, mult: 0.932) |
| `DWD` | Ice | Conditional Strike | 5.6 -> **4.9** (-12.5%) | 117.1 -> **160.8** | 661.4 -> **792.8** | Status 'Frosty' beneficiaries undertuned (WR: 22.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 16.1% vs 30% floor, Casts: 1375). Increasing spread: b -11.6%, n +23.6% |
| `ELF` | Wind | Conditional Strike | 7.8 -> **7.5** (-3.8%) | 157.0 -> **229.3** | 1232.4 -> **1727.2** | Class Wind undertuned (WR: 33.9%, factor: 1.065); Status 'Bleeding' beneficiaries undertuned (WR: 32.8%) |
| `ELW` | Wind | Debuff / Control | 35.5 -> **35.4** (-0.3%) | - | 35.5 -> **35.4** | Class Wind undertuned (WR: 33.9%, factor: 1.065); Individual spell overtuned (WR: 66.9%, Casts: 4397, mult: 0.936) |
| `ELE` | Wind | Setup - Weather | 53.5 -> **62.0** (+15.9%) | - | 53.5 -> **62.0** | Class Wind undertuned (WR: 33.9%, factor: 1.065); Individual spell undertuned (WR: 27.0%, Casts: 4082, mult: 1.089) |
| `ELL` | Wind | Buff / Sustain | 78.1 -> **96.0** (+22.9%) | - | 78.1 -> **96.0** | Class Wind undertuned (WR: 33.9%, factor: 1.065); Individual spell undertuned (WR: 12.1%, Casts: 1602, mult: 1.155) |
| `ELD` | Wind | Conditional Strike | 6.8 -> **6.3** (-7.4%) | 159.8 -> **245.1** | 1093.4 -> **1550.4** | Class Wind undertuned (WR: 33.9%, factor: 1.065); Weather 'Raining' beneficiaries undertuned (WR: 19.4%) |
| `LEF` | Wind | Conditional Strike | 4.0 -> **4.1** (+2.5%) | 121.3 -> **173.2** | 489.2 -> **714.2** | Class Wind undertuned (WR: 33.9%, factor: 1.065); Status 'Burning' beneficiaries undertuned (WR: 26.3%) |
| `LEW` | Wind | Debuff / Control | 37.7 -> **39.5** (+4.8%) | - | 37.7 -> **39.5** | Class Wind undertuned (WR: 33.9%, factor: 1.065); Individual spell overtuned (WR: 54.9%, Casts: 542, mult: 0.984) |
| `LEE` | Wind | Setup - Weather | 55.6 -> **67.6** (+21.6%) | - | 55.6 -> **67.6** | Class Wind undertuned (WR: 33.9%, factor: 1.065); Individual spell undertuned (WR: 15.0%, Casts: 1574, mult: 1.142) |
| `LEL` | Wind | Buff / Sustain | 83.5 -> **93.7** (+12.2%) | - | 83.5 -> **93.7** | Class Wind undertuned (WR: 33.9%, factor: 1.065); Individual spell undertuned (WR: 35.3%, Casts: 356, mult: 1.054) |
| `EDF` | Poison | Conditional Strike | 2.5 -> **1.9** (-24.0%) | 95.7 -> **128.5** | 241.8 -> **246.0** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.3% vs 30% floor, Casts: 90). Increasing spread: b -16.7%, n +34.2% |
| `EDW` | Poison | Debuff / Control | 7.7 -> **6.7** (-13.0%) | - | 7.7 -> **6.7** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Individual spell overtuned (WR: 77.0%, Casts: 5567, mult: 0.893) |
| `EDE` | Poison | Setup - Location | 69.6 -> **75.0** (+7.8%) | - | 69.6 -> **75.0** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Location 'Swamp' appliers undertuned (WR: 35.4%, casts: 1137) |
| `EDL` | Poison | Debuff / Control | 1.8 -> **1.4** (-22.2%) | - | 1.8 -> **1.4** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Individual spell overtuned (WR: 92.0%, Casts: 1677, mult: 0.827) |
| `EDD` | Poison | Ultimate | 18.6 -> **14.8** (-20.4%) | 30.7 -> **44.9** | 589.6 -> **679.3** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Status 'Bleeding' beneficiaries undertuned (WR: 32.8%) |
| `DEF` | Poison | Conditional Strike | 11.7 -> **12.8** (+9.4%) | 3.9 -> **3.0** | 57.3 -> **51.2** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Condition triggers excessively (N=1 conditions, Trigger Rate: 90.2% vs 55% ceiling, WR: 56.1%). Compressing spread: b +15.3%, n -23.0% |
| `DEW` | Poison | Debuff / Control | 7.5 -> **7.3** (-2.7%) | - | 7.5 -> **7.3** | Class Poison overtuned (WR: 57.0%, factor: 0.972) |
| `DEE` | Poison | Debuff / Control | 17.6 -> **15.8** (-10.2%) | - | 17.6 -> **15.8** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Individual spell overtuned (WR: 70.5%, Casts: 3010, mult: 0.921) |
| `DEL` | Poison | Conditional Strike | 0.4 -> **0.4** (+0.0%) | 158.0 -> **230.9** | 63.6 -> **92.8** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Status 'Bleeding' beneficiaries undertuned (WR: 32.8%) |
| `DED` | Poison | Debuff / Control | 19.5 -> **19.2** (-1.5%) | - | 19.5 -> **19.2** | Class Poison overtuned (WR: 57.0%, factor: 0.972); Individual spell undertuned (WR: 45.8%, Casts: 1746, mult: 1.014) |
| `LDF` | Cosmic | Debuff / Control | 28.9 -> **27.0** (-6.6%) | - | 28.9 -> **27.0** | Individual spell overtuned (WR: 67.7%, Casts: 1484, mult: 0.933) |
| `LDW` | Cosmic | Debuff / Control | 18.9 -> **17.9** (-5.3%) | - | 18.9 -> **17.9** | Status 'Stunned' appliers undertuned (WR: 36.7%, casts: 25075); Individual spell overtuned (WR: 73.9%, Casts: 2887, mult: 0.907) |
| `LDE` | Cosmic | Setup - Location | 26.5 -> **30.6** (+15.5%) | - | 26.5 -> **30.6** | Individual spell undertuned (WR: 11.7%, Casts: 3816, mult: 1.157) |
| `LDL` | Cosmic | Conditional Strike | 3.9 -> **3.5** (-10.3%) | 108.2 -> **148.1** | 425.9 -> **521.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 5753). Increasing spread: b -18.0%, n +36.9%; Individual spell undertuned (WR: 29.0%, Casts: 5753, mult: 1.081) |
| `LDD` | Cosmic | Ultimate | 9.8 -> **11.5** (+17.3%) | 48.2 -> **45.3** | 482.2 -> **532.4** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 4022, WR: 27.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 27.6%, Casts: 4022, mult: 1.087) |
| `DLF` | Cosmic | Conditional Strike | 4.3 -> **3.4** (-20.9%) | 96.6 -> **132.3** | 419.7 -> **453.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 974). Increasing spread: b -18.0%, n +36.9%; Individual spell overtuned (WR: 56.9%, Casts: 974, mult: 0.976) |
| `DLW` | Cosmic | Direct Damage | 29.8 -> **27.4** (-8.1%) | - | 29.8 -> **27.4** | Individual spell overtuned (WR: 70.6%, Casts: 7136, mult: 0.921) |
| `DLE` | Cosmic | Direct Damage | 85.7 -> **93.1** (+8.6%) | - | 85.7 -> **93.1** | Individual spell undertuned (WR: 27.7%, Casts: 1206, mult: 1.086) |
| `DLL` | Cosmic | Conditional Strike | 4.7 -> **4.0** (-14.9%) | 108.2 -> **128.4** | 513.2 -> **517.6** | Weather 'Darkness' beneficiaries overtuned (WR: 54.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 19.5% vs 30% floor, Casts: 205). Increasing spread: b -10.2%, n +20.7% |
