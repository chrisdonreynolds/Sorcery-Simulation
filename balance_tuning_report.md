# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T03:38:59Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 516.0s  
**Total Spells Tuned:** 92 / 125  

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
| **Blood** | 15,725 | 55.3% | 55.3% | 35.3 | Overtuned ⚠️ |
| **Ghostfire** | 14,307 | 53.9% | 53.9% | 110.4 | Overtuned ⚠️ |
| **Poison** | 15,861 | 53.1% | 53.1% | 14.2 | Balanced ✅ |
| **Earth** | 8,184 | 52.1% | 52.1% | 18.0 | Balanced ✅ |
| **Dark** | 7,363 | 51.6% | 51.6% | 60.7 | Balanced ✅ |
| **Cosmic** | 14,035 | 50.8% | 50.8% | 23.2 | Balanced ✅ |
| **Beasts** | 12,654 | 50.5% | 50.5% | 27.9 | Balanced ✅ |
| **Light** | 7,105 | 50.3% | 50.3% | 41.5 | Balanced ✅ |
| **Lightning** | 17,389 | 50.1% | 50.1% | 42.4 | Balanced ✅ |
| **Plants** | 14,529 | 50.1% | 50.1% | 6.6 | Balanced ✅ |
| **Fire** | 6,901 | 49.0% | 49.0% | 13.4 | Balanced ✅ |
| **Fey** | 13,546 | 48.1% | 48.1% | 9760.8 | Balanced ✅ |
| **Ice** | 15,087 | 47.0% | 47.0% | 43.9 | Balanced ✅ |
| **Wind** | 14,233 | 46.6% | 46.6% | 9.5 | Balanced ✅ |
| **Water** | 7,804 | 46.4% | 46.4% | 28.3 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,094 (50.8%) | 3,087 (48.4%) | 18.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 773 (52.7%) | 2,620 (48.2%) | 3.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,029 (50.1%) | 3,593 (48.4%) | 8.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 6,385 (56.5%) | 6,891 (47.4%) | 4.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 11,154 (51.4%) | 3,190 (48.2%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,937 (52.2%) | 4,631 (43.3%) | 0.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 2,007 (42.8%) | 2,163 (45.8%) | 7.4% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFD` | Fire | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 1805.4 -> **2353.9** | 1083.8 -> **1177.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.9% vs 30% floor, Casts: 1209). Increasing spread: b -14.8%, n +30.4%; Individual spell undertuned (WR: 43.6%, Casts: 1209, mult: 1.022) |
| `WWF` | Water | Conditional Strike | 2.0 -> **1.8** (-10.0%) | 788.0 -> **1009.5** | 1578.0 -> **1818.9** | Class Water undertuned (WR: 46.4%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.7% vs 30% floor, Casts: 1097). Increasing spread: b -13.7%, n +28.1% |
| `WWE` | Water | Setup - Weather | 102.5 -> **109.3** (+6.6%) | - | 102.5 -> **109.3** | Class Water undertuned (WR: 46.4%, factor: 1.014); Weather 'Raining' appliers undertuned (WR: 42.8%, casts: 2007) |
| `WWL` | Water | Buff / Sustain | 76.8 -> **77.9** (+1.4%) | - | 76.8 -> **77.9** | Class Water undertuned (WR: 46.4%, factor: 1.014) |
| `WWD` | Water | Buff / Sustain | 48.9 -> **49.6** (+1.4%) | - | 48.9 -> **49.6** | Class Water undertuned (WR: 46.4%, factor: 1.014) |
| `EEF` | Earth | Conditional Strike | 49.1 -> **56.5** (+15.1%) | 107.1 -> **130.1** | 5307.7 -> **7407.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.6% vs 30% floor, Casts: 1927). Increasing spread: b -10.6%, n +21.5%; Buffed setup spell [EEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `EEW` | Earth | Buff / Sustain | 18.3 -> **17.9** (-2.2%) | - | 18.3 -> **17.9** | Individual spell overtuned (WR: 56.6%, Casts: 1185, mult: 0.978) |
| `LLF` | Light | Conditional Strike | 8.5 -> **9.9** (+16.5%) | 2393.4 -> **3171.5** | 20352.4 -> **31407.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.4% vs 30% floor, Casts: 2225). Increasing spread: b -15.8%, n +32.5%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 197.2 -> **226.8** (+15.0%) | - | 197.2 -> **226.8** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LLE` | Light | Setup - Weather | 173.9 -> **200.0** (+15.0%) | - | 173.9 -> **200.0** | Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 14.8 -> **14.5** (-2.0%) | - | 14.8 -> **14.5** | Individual spell overtuned (WR: 55.4%, Casts: 1054, mult: 0.982) |
| `LLD` | Light | Ultimate | 43.2 -> **43.2** (+0.0%) | 247.9 -> **322.3** | 10752.5 -> **13966.6** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1163). Shifted tuner focus: protected ultimate base floor at 43.2 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 5568.0 -> **7628.2** | 1113.8 -> **1525.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2113). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 44.3%, Casts: 2113, mult: 1.019) |
| `DDW` | Dark | Debuff / Control | 145.4 -> **142.7** (-1.9%) | - | 145.4 -> **142.7** | Individual spell overtuned (WR: 55.5%, Casts: 1572, mult: 0.982) |
| `DDE` | Dark | Setup - Weather | 382.0 -> **425.8** (+11.5%) | - | 382.0 -> **425.8** | Weather 'Darkness' appliers overtuned on own (WR: 54.6%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `DDL` | Dark | Debuff / Control | 62.4 -> **61.6** (-1.3%) | - | 62.4 -> **61.6** | Individual spell overtuned (WR: 53.9%, Casts: 1352, mult: 0.987) |
| `DDD` | Dark | Debuff / Control | 17.5 -> **17.3** (-1.1%) | - | 17.5 -> **17.3** | Individual spell overtuned (WR: 54.1%, Casts: 1255, mult: 0.987) |
| `FWF` | Ghostfire | Debuff / Control | 21.4 -> **21.1** (-1.4%) | - | 21.4 -> **21.1** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985) |
| `FWW` | Ghostfire | Debuff / Control | 144.9 -> **162.0** (+11.8%) | - | 144.9 -> **162.0** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985); Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 360.2 -> **359.4** (-0.2%) | - | 360.2 -> **359.4** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985); Location 'Graveyard' appliers overtuned on own (WR: 66.8%) |
| `FWL` | Ghostfire | Debuff / Control | 308.1 -> **333.4** (+8.2%) | - | 308.1 -> **333.4** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985); Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 41.6 -> **39.4** (-5.3%) | 372.4 -> **462.2** | 15533.4 -> **18250.1** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985); Location 'Graveyard' beneficiaries overtuned (WR: 60.3%) |
| `WFF` | Ghostfire | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 2409.7 -> **3244.7** | 1446.4 -> **1622.8** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.8% vs 30% floor, Casts: 1770). Increasing spread: b -16.9%, n +34.7% |
| `WFW` | Ghostfire | Debuff / Control | 18.4 -> **17.6** (-4.3%) | - | 18.4 -> **17.6** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985); Individual spell overtuned (WR: 58.6%, Casts: 1794, mult: 0.970) |
| `WFE` | Ghostfire | Debuff / Control | 10.0 -> **10.4** (+4.0%) | - | 10.0 -> **10.4** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985); Status 'Bleeding' appliers overtuned on own (WR: 56.5%) |
| `WFL` | Ghostfire | Buff / Sustain | 49.4 -> **49.7** (+0.6%) | - | 49.4 -> **49.7** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985); Individual spell undertuned (WR: 43.8%, Casts: 1578, mult: 1.021) |
| `WFD` | Ghostfire | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 1186.6 -> **1498.0** | 1068.8 -> **1199.2** | Class Ghostfire overtuned (WR: 53.9%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.9% vs 30% floor, Casts: 1115). Increasing spread: b -12.8%, n +26.2% |
| `FEW` | Beasts | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 5712.7 -> **8007.3** | 1142.7 -> **1601.7** | Status 'Entangled' beneficiaries undertuned (WR: 43.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.6% vs 30% floor, Casts: 1351). Increasing spread: b -17.8%, n +36.5% |
| `FEE` | Beasts | Buff / Sustain | 37.6 -> **38.8** (+3.2%) | - | 37.6 -> **38.8** | Individual spell undertuned (WR: 40.8%, Casts: 1048, mult: 1.032) |
| `FEL` | Beasts | Buff / Sustain | 44.2 -> **46.0** (+4.1%) | - | 44.2 -> **46.0** | Individual spell undertuned (WR: 39.0%, Casts: 1874, mult: 1.040) |
| `EFF` | Beasts | Debuff / Control | 0.2 -> **0.2** (+0.0%) | 4798.5 -> **6524.0** | 959.9 -> **1305.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.2% vs 30% floor, Casts: 1200). Increasing spread: b -17.5%, n +36.0%; Individual spell overtuned (WR: 56.2%, Casts: 1200, mult: 0.979) |
| `EFW` | Beasts | Buff / Sustain | 19.4 -> **18.9** (-2.6%) | - | 19.4 -> **18.9** | Individual spell overtuned (WR: 57.0%, Casts: 1087, mult: 0.976) |
| `EFD` | Beasts | Ultimate | 33.6 -> **36.3** (+8.0%) | 715.4 -> **706.4** | 24071.0 -> **25678.6** | Status 'Entangled' beneficiaries undertuned (WR: 43.3%); Location 'Jungle' beneficiaries undertuned (WR: 44.2%) |
| `FLF` | Lightning | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 8242.8 -> **11268.6** | 3297.5 -> **3380.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.4% vs 30% floor, Casts: 1707). Increasing spread: b -17.9%, n +36.7%; Individual spell undertuned (WR: 40.9%, Casts: 1707, mult: 1.032) |
| `FLW` | Lightning | Debuff / Control | 165.7 -> **181.9** (+9.8%) | - | 165.7 -> **181.9** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 62.4%, Casts: 2438, mult: 0.955) |
| `FLE` | Lightning | Setup - Weather | 180.4 -> **207.5** (+15.0%) | - | 180.4 -> **207.5** | Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLD` | Lightning | Ultimate | 75.5 -> **73.8** (-2.3%) | 157.4 -> **199.1** | 11959.2 -> **14767.4** | Weather 'Storming' beneficiaries overtuned (WR: 56.7%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1483). Shifted tuner focus: protected ultimate base floor at 75.5 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 3817.7 -> **5163.8** | 1145.6 -> **1549.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.1% vs 30% floor, Casts: 1005). Increasing spread: b -17.2%, n +35.3%; Individual spell undertuned (WR: 46.3%, Casts: 1005, mult: 1.012) |
| `LFW` | Lightning | Buff / Sustain | 24.4 -> **23.8** (-2.5%) | - | 24.4 -> **23.8** | Individual spell overtuned (WR: 57.5%, Casts: 839, mult: 0.974) |
| `LFL` | Lightning | Debuff / Control | 51.5 -> **59.2** (+15.0%) | 1148.5 -> **1485.7** | 59199.2 -> **88012.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.2% vs 30% floor, Casts: 2202). Increasing spread: b -14.3%, n +29.4%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 2667.0 -> **3592.2** | 2401.2 -> **2874.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.8% vs 30% floor, Casts: 1808). Increasing spread: b -16.9%, n +34.7%; Individual spell undertuned (WR: 37.7%, Casts: 1808, mult: 1.045) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 5581.9 -> **7647.2** | 1116.6 -> **1529.6** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 978). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 56.7 -> **55.5** (-2.1%) | - | 56.7 -> **55.5** | Class Blood overtuned (WR: 55.3%, factor: 0.979) |
| `FDE` | Blood | Setup - Weather | 16.7 -> **16.3** (-2.4%) | - | 16.7 -> **16.3** | Class Blood overtuned (WR: 55.3%, factor: 0.979) |
| `FDD` | Blood | Ultimate | 52.7 -> **51.6** (-2.1%) | 56.3 -> **73.1** | 3019.7 -> **3823.6** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 1174). Shifted tuner focus: protected ultimate base floor at 52.7 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 2001.3 -> **2629.9** | 600.7 -> **526.2** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.7% vs 30% floor, Casts: 1580). Increasing spread: b -15.3%, n +31.4% |
| `DFW` | Blood | Debuff / Control | 10.1 -> **10.5** (+4.0%) | - | 10.1 -> **10.5** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Status 'Bleeding' appliers overtuned on own (WR: 56.5%) |
| `DFE` | Blood | Buff / Sustain | 46.1 -> **45.1** (-2.2%) | - | 46.1 -> **45.1** | Class Blood overtuned (WR: 55.3%, factor: 0.979) |
| `DFL` | Blood | Buff / Sustain | 27.9 -> **27.3** (-2.2%) | - | 27.9 -> **27.3** | Class Blood overtuned (WR: 55.3%, factor: 0.979) |
| `DFD` | Blood | Conditional Strike | 463.2 -> **513.3** (+10.8%) | 0.1 -> **0.1** | 509.5 -> **564.6** | Class Blood overtuned (WR: 55.3%, factor: 0.979); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.0% vs 55% ceiling, WR: 64.8%). Compressing spread: b +19.8%, n -28.2% |
| `WEF` | Plants | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 1144.3 -> **1511.1** | 1030.8 -> **1209.7** | Location 'Jungle' beneficiaries undertuned (WR: 44.2%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.5% vs 30% floor, Casts: 1682). Increasing spread: b -14.2%, n +29.1% |
| `WEW` | Plants | Debuff / Control | 1133.7 -> **1337.4** (+18.0%) | - | 1133.7 -> **1337.4** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 42.6%, Casts: 1184, mult: 1.026) |
| `WED` | Plants | Conditional Strike | 17.3 -> **19.1** (+10.4%) | 24.9 -> **23.4** | 448.1 -> **466.0** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 996, WR: 44.0%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 44.0%, Casts: 996, mult: 1.020) |
| `EWF` | Plants | Buff / Sustain | 0.7 -> **0.6** (-14.3%) | 830.9 -> **1101.3** | 582.3 -> **661.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.3% vs 30% floor, Casts: 1457). Increasing spread: b -15.9%, n +32.5%; Individual spell undertuned (WR: 44.9%, Casts: 1457, mult: 1.017) |
| `EWW` | Plants | Debuff / Control | 1.3 -> **1.1** (-15.4%) | - | 1.3 -> **1.1** | Individual spell overtuned (WR: 80.6%, Casts: 1974, mult: 0.878) |
| `EWD` | Plants | Conditional Strike | 3.5 -> **4.1** (+17.1%) | 4429.9 -> **6210.8** | 15508.1 -> **25468.4** | Status 'Bleeding' appliers overtuned on own (WR: 56.5%); Status 'Entangled' beneficiaries undertuned (WR: 43.3%) |
| `WLF` | Fey | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 2577.4 -> **3353.2** | 2578.4 -> **3018.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.3% vs 30% floor, Casts: 1352). Increasing spread: b -14.7%, n +30.1%; Individual spell undertuned (WR: 40.5%, Casts: 1352, mult: 1.034) |
| `WLW` | Fey | Debuff / Control | 62.9 -> **63.9** (+1.6%) | - | 62.9 -> **63.9** | Individual spell undertuned (WR: 45.1%, Casts: 2085, mult: 1.016) |
| `WLE` | Fey | Setup - Location | 413.9 -> **424.3** (+2.5%) | - | 413.9 -> **424.3** | Location 'Enchanted Forest' appliers overtuned on own (WR: 65.4%); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 55.0 -> **53.9** (-2.0%) | - | 55.0 -> **53.9** | Individual spell overtuned (WR: 55.7%, Casts: 934, mult: 0.981) |
| `WLD` | Fey | Ultimate | 20.5 -> **20.3** (-1.0%) | 2057.3 -> **2723.8** | 42195.2 -> **55313.4** | Location 'Enchanted Forest' beneficiaries undertuned (WR: 45.4%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1138). Shifted tuner focus: protected ultimate base floor at 20.5 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 21.4 -> **19.5** (-8.9%) | 512.9 -> **643.6** | 10997.5 -> **12569.7** | Location 'Enchanted Forest' beneficiaries undertuned (WR: 45.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 16.5% vs 30% floor, Casts: 2461). Increasing spread: b -11.4%, n +23.2% |
| `LWL` | Fey | Debuff / Control | 56.4 -> **58.9** (+4.4%) | - | 56.4 -> **58.9** | Individual spell undertuned (WR: 37.6%, Casts: 1351, mult: 1.045) |
| `LWD` | Fey | Conditional Strike | 0.4 -> **0.3** (-25.0%) | 5581.9 -> **7647.2** | 2233.2 -> **2294.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 766). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 5155.8 -> **6902.3** | 5156.8 -> **6213.0** | Weather 'Raining' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 1488). Increasing spread: b -15.4%, n +31.7% |
| `WDW` | Ice | Buff / Sustain | 10.2 -> **10.0** (-2.0%) | - | 10.2 -> **10.0** | Individual spell overtuned (WR: 55.4%, Casts: 1970, mult: 0.982) |
| `WDE` | Ice | Setup - Weather | 38.2 -> **39.8** (+4.2%) | - | 38.2 -> **39.8** | Individual spell undertuned (WR: 38.5%, Casts: 2310, mult: 1.042) |
| `WDD` | Ice | Ultimate | 31.4 -> **30.7** (-2.2%) | 339.9 -> **410.7** | 10704.3 -> **12639.2** | Weather 'Blizzard' beneficiaries overtuned (WR: 56.3%); Location 'Tundra' beneficiaries overtuned (WR: 56.3%) |
| `DWW` | Ice | Debuff / Control | 110.1 -> **112.0** (+1.7%) | - | 110.1 -> **112.0** | Individual spell undertuned (WR: 44.8%, Casts: 1275, mult: 1.018) |
| `DWE` | Ice | Setup - Location | 43.3 -> **45.3** (+4.6%) | - | 43.3 -> **45.3** | Location 'Tundra' appliers undertuned (WR: 43.4%, casts: 1611); Individual spell undertuned (WR: 43.4%, Casts: 1611, mult: 1.023) |
| `DWD` | Ice | Conditional Strike | 3.0 -> **2.7** (-10.0%) | 292.1 -> **358.6** | 879.3 -> **970.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.1% vs 30% floor, Casts: 1160). Increasing spread: b -11.2%, n +22.8%; Individual spell undertuned (WR: 44.5%, Casts: 1160, mult: 1.018) |
| `ELF` | Wind | Conditional Strike | 1.8 -> **1.5** (-16.7%) | 2121.9 -> **2802.7** | 3821.2 -> **4205.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.9% vs 30% floor, Casts: 1101). Increasing spread: b -15.6%, n +32.1% |
| `ELW` | Wind | Debuff / Control | 104.7 -> **102.2** (-2.4%) | - | 104.7 -> **102.2** | Individual spell overtuned (WR: 56.9%, Casts: 1335, mult: 0.976) |
| `ELE` | Wind | Setup - Weather | 29.2 -> **29.8** (+2.1%) | - | 29.2 -> **29.8** | Individual spell undertuned (WR: 43.8%, Casts: 1635, mult: 1.021) |
| `ELL` | Wind | Buff / Sustain | 45.6 -> **46.5** (+2.0%) | - | 45.6 -> **46.5** | Individual spell undertuned (WR: 44.0%, Casts: 1624, mult: 1.021) |
| `ELD` | Wind | Conditional Strike | 1.0 -> **0.9** (-10.0%) | 4028.6 -> **5277.2** | 4029.6 -> **4750.4** | Weather 'Raining' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.8% vs 30% floor, Casts: 675). Increasing spread: b -14.1%, n +28.8% |
| `LEF` | Wind | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 2076.8 -> **2705.4** | 1246.7 -> **1353.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 1287). Increasing spread: b -14.8%, n +30.3% |
| `LEW` | Wind | Debuff / Control | 55.2 -> **56.4** (+2.2%) | - | 55.2 -> **56.4** | Individual spell undertuned (WR: 43.6%, Casts: 2419, mult: 1.022) |
| `LEE` | Wind | Setup - Weather | 27.0 -> **27.3** (+1.1%) | - | 27.0 -> **27.3** | Individual spell undertuned (WR: 46.2%, Casts: 1166, mult: 1.012) |
| `LEL` | Wind | Buff / Sustain | 123.6 -> **126.0** (+1.9%) | - | 123.6 -> **126.0** | Individual spell undertuned (WR: 44.2%, Casts: 1713, mult: 1.020) |
| `EDF` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 1843.0 -> **2440.0** | 553.2 -> **732.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 2495). Increasing spread: b -15.8%, n +32.4%; Individual spell undertuned (WR: 44.2%, Casts: 2495, mult: 1.020) |
| `EDE` | Poison | Setup - Location | 65.9 -> **79.3** (+20.3%) | - | 65.9 -> **79.3** | Location 'Swamp' appliers undertuned (WR: 43.4%, casts: 1494); Buffed setup spell [EDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `EDD` | Poison | Ultimate | 49.6 -> **49.6** (+0.0%) | 53.4 -> **68.6** | 2698.2 -> **3452.2** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 1.2% vs 16% floor, Casts: 1531). Shifted tuner focus: protected ultimate base floor at 49.6 (hard-coded floor >= 20.0) and buffed appliers/setups (WFE, FDL, DFW, EWD, EDE) with +15% b tempo. |
| `DEW` | Poison | Debuff / Control | 11.6 -> **11.4** (-1.7%) | - | 11.6 -> **11.4** | Individual spell overtuned (WR: 56.0%, Casts: 1562, mult: 0.980) |
| `DEE` | Poison | Debuff / Control | 37.0 -> **36.3** (-1.9%) | - | 37.0 -> **36.3** | Individual spell overtuned (WR: 55.9%, Casts: 922, mult: 0.980) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 2063.5 -> **2719.2** | 412.9 -> **544.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.3% vs 30% floor, Casts: 909). Increasing spread: b -15.5%, n +31.8% |
| `DED` | Poison | Debuff / Control | 22.1 -> **22.8** (+3.2%) | - | 22.1 -> **22.8** | Individual spell undertuned (WR: 40.8%, Casts: 1372, mult: 1.033) |
| `LDW` | Cosmic | Debuff / Control | 41.0 -> **39.9** (-2.7%) | - | 41.0 -> **39.9** | Individual spell overtuned (WR: 57.8%, Casts: 2085, mult: 0.973) |
| `LDL` | Cosmic | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 3036.8 -> **4043.2** | 1822.7 -> **2022.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.6% vs 30% floor, Casts: 1101). Increasing spread: b -16.1%, n +33.1% |
| `LDD` | Cosmic | Ultimate | 109.4 -> **118.2** (+8.0%) | 22.0 -> **20.7** | 2516.2 -> **2564.9** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2249, WR: 47.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 0.6 -> **0.5** (-16.7%) | 2226.5 -> **2928.6** | 1336.5 -> **1464.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.6% vs 30% floor, Casts: 991). Increasing spread: b -15.4%, n +31.5% |
| `DLL` | Cosmic | Conditional Strike | 2.3 -> **2.0** (-13.0%) | 921.2 -> **1209.5** | 2121.1 -> **2421.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.8% vs 30% floor, Casts: 1505). Increasing spread: b -15.3%, n +31.3%; Individual spell undertuned (WR: 39.2%, Casts: 1505, mult: 1.039) |
