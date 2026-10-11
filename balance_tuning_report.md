# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-11T03:53:32Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 490.4s  
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
| **Blood** | 15,261 | 56.2% | 56.2% | 34.7 | Overtuned ⚠️ |
| **Ghostfire** | 14,524 | 53.1% | 53.1% | 111.7 | Balanced ✅ |
| **Dark** | 8,065 | 52.5% | 52.5% | 68.2 | Balanced ✅ |
| **Light** | 6,987 | 52.2% | 52.2% | 54.7 | Balanced ✅ |
| **Beasts** | 13,118 | 52.0% | 52.0% | 29.1 | Balanced ✅ |
| **Plants** | 14,819 | 51.8% | 51.8% | 8.0 | Balanced ✅ |
| **Poison** | 15,346 | 50.7% | 50.7% | 17.2 | Balanced ✅ |
| **Earth** | 8,074 | 50.7% | 50.7% | 19.1 | Balanced ✅ |
| **Lightning** | 16,494 | 49.9% | 49.9% | 52.3 | Balanced ✅ |
| **Fire** | 6,468 | 48.6% | 48.6% | 13.1 | Balanced ✅ |
| **Cosmic** | 13,494 | 48.6% | 48.6% | 23.3 | Balanced ✅ |
| **Ice** | 14,436 | 48.3% | 48.3% | 42.3 | Balanced ✅ |
| **Water** | 6,722 | 46.8% | 46.8% | 27.5 | Balanced ✅ |
| **Wind** | 13,995 | 46.7% | 46.7% | 9.5 | Balanced ✅ |
| **Fey** | 13,465 | 46.5% | 46.4% | 4910.9 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,312 (50.0%) | 3,254 (50.1%) | 18.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 805 (51.6%) | 2,530 (52.4%) | 4.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,178 (48.9%) | 3,498 (46.0%) | 8.9% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 6,447 (58.9%) | 7,080 (45.8%) | 4.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 10,037 (50.1%) | 2,694 (51.9%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,290 (50.0%) | 4,028 (44.9%) | 0.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,545 (42.5%) | 2,201 (48.8%) | 6.6% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFD` | Fire | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 2353.9 -> **3121.3** | 1177.5 -> **1248.9** | Status 'Burning' beneficiaries undertuned (WR: 46.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 1345). Increasing spread: b -14.9%, n +30.5% |
| `WWF` | Water | Conditional Strike | 1.8 -> **1.6** (-11.1%) | 1009.5 -> **1289.1** | 1818.9 -> **2064.2** | Status 'Burning' beneficiaries undertuned (WR: 46.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.6% vs 30% floor, Casts: 1132). Increasing spread: b -12.6%, n +25.7% |
| `WWE` | Water | Setup - Weather | 109.3 -> **115.1** (+5.3%) | - | 109.3 -> **115.1** | Weather 'Raining' appliers undertuned (WR: 42.5%, casts: 1545); Individual spell undertuned (WR: 42.5%, Casts: 1545, mult: 1.026) |
| `EEF` | Earth | Conditional Strike | 56.5 -> **65.0** (+15.0%) | 130.1 -> **158.8** | 7407.1 -> **10387.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.9% vs 30% floor, Casts: 1887). Increasing spread: b -10.8%, n +22.1%; Buffed setup spell [EEF] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `EEW` | Earth | Buff / Sustain | 17.9 -> **17.6** (-1.7%) | - | 17.9 -> **17.6** | Individual spell overtuned (WR: 55.4%, Casts: 1249, mult: 0.982) |
| `LLF` | Light | Conditional Strike | 9.9 -> **11.4** (+15.2%) | 3171.5 -> **4186.4** | 31407.8 -> **47736.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.0% vs 30% floor, Casts: 1967). Increasing spread: b -15.6%, n +32.0%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 226.8 -> **260.8** (+15.0%) | - | 226.8 -> **260.8** | Buffed setup spell [LLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LLE` | Light | Setup - Weather | 200.0 -> **230.0** (+15.0%) | - | 200.0 -> **230.0** | Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 14.5 -> **14.2** (-2.1%) | - | 14.5 -> **14.2** | Individual spell overtuned (WR: 56.3%, Casts: 1141, mult: 0.979) |
| `LLD` | Light | Ultimate | 43.2 -> **42.3** (-2.1%) | 322.3 -> **419.0** | 13966.6 -> **17766.0** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.0% vs 16% floor, Casts: 1081). Shifted tuner focus: protected ultimate base floor at 43.2 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo.; Individual spell overtuned (WR: 56.3%, Casts: 1081, mult: 0.979) |
| `DDF` | Dark | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 7628.2 -> **10450.6** | 1525.8 -> **2090.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1874). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 46.2%, Casts: 1874, mult: 1.012) |
| `DDE` | Dark | Setup - Weather | 425.8 -> **456.1** (+7.1%) | - | 425.8 -> **456.1** | Weather 'Darkness' appliers overtuned on own (WR: 59.9%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `DDL` | Dark | Debuff / Control | 61.6 -> **60.6** (-1.6%) | - | 61.6 -> **60.6** | Individual spell overtuned (WR: 54.7%, Casts: 1543, mult: 0.984) |
| `DDD` | Dark | Debuff / Control | 17.3 -> **17.1** (-1.2%) | - | 17.3 -> **17.1** | Individual spell overtuned (WR: 53.8%, Casts: 1265, mult: 0.988) |
| `FWW` | Ghostfire | Debuff / Control | 162.0 -> **180.1** (+11.2%) | - | 162.0 -> **180.1** | Status 'Cursed' appliers overtuned on own (WR: 53.7%); Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWE` | Ghostfire | Setup - Location | 359.4 -> **362.6** (+0.9%) | - | 359.4 -> **362.6** | Location 'Graveyard' appliers overtuned on own (WR: 67.4%); Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 333.4 -> **362.3** (+8.7%) | - | 333.4 -> **362.3** | Status 'Cursed' appliers overtuned on own (WR: 53.7%); Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWD` | Ghostfire | Ultimate | 39.4 -> **37.6** (-4.6%) | 462.2 -> **568.3** | 18250.1 -> **21405.7** | Location 'Graveyard' beneficiaries overtuned (WR: 62.7%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.2% vs 8% floor, Casts: 1111). Shifted tuner focus: protected ultimate base floor at 39.4 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 3244.7 -> **4400.6** | 1622.8 -> **1760.6** | Status 'Bleeding' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.4% vs 30% floor, Casts: 1768). Increasing spread: b -16.3%, n +33.4% |
| `WFW` | Ghostfire | Debuff / Control | 17.6 -> **17.4** (-1.1%) | - | 17.6 -> **17.4** | Individual spell overtuned (WR: 54.2%, Casts: 2222, mult: 0.986) |
| `WFE` | Ghostfire | Debuff / Control | 10.4 -> **11.1** (+6.7%) | - | 10.4 -> **11.1** | Status 'Bleeding' appliers overtuned on own (WR: 58.9%); Buffed setup spell [WFE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `WFL` | Ghostfire | Buff / Sustain | 49.7 -> **50.3** (+1.2%) | - | 49.7 -> **50.3** | Individual spell undertuned (WR: 46.3%, Casts: 1448, mult: 1.012) |
| `WFD` | Ghostfire | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1498.0 -> **1946.0** | 1199.2 -> **1362.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.5% vs 30% floor, Casts: 1151). Increasing spread: b -14.6%, n +29.9%; Individual spell undertuned (WR: 41.6%, Casts: 1151, mult: 1.029) |
| `FEF` | Beasts | Debuff / Control | 80.8 -> **79.7** (-1.4%) | - | 80.8 -> **79.7** | Individual spell overtuned (WR: 54.2%, Casts: 1224, mult: 0.986) |
| `FEW` | Beasts | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 8007.3 -> **11183.1** | 1601.7 -> **2236.8** | Status 'Entangled' beneficiaries undertuned (WR: 44.9%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.2% vs 30% floor, Casts: 1184). Increasing spread: b -17.9%, n +36.9% |
| `FEE` | Beasts | Buff / Sustain | 38.8 -> **39.8** (+2.6%) | - | 38.8 -> **39.8** | Individual spell undertuned (WR: 42.7%, Casts: 1243, mult: 1.025) |
| `FEL` | Beasts | Buff / Sustain | 46.0 -> **47.8** (+3.9%) | - | 46.0 -> **47.8** | Individual spell undertuned (WR: 39.3%, Casts: 1414, mult: 1.038) |
| `EFF` | Beasts | Debuff / Control | 0.2 -> **0.2** (+0.0%) | 6524.0 -> **8881.3** | 1305.0 -> **1776.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.0% vs 30% floor, Casts: 958). Increasing spread: b -17.6%, n +36.1%; Individual spell overtuned (WR: 55.4%, Casts: 958, mult: 0.982) |
| `EFW` | Beasts | Buff / Sustain | 18.9 -> **18.0** (-4.8%) | - | 18.9 -> **18.0** | Individual spell overtuned (WR: 62.5%, Casts: 1371, mult: 0.954) |
| `EFD` | Beasts | Ultimate | 36.3 -> **36.3** (+0.0%) | 706.4 -> **936.3** | 25678.6 -> **34024.0** | Status 'Entangled' beneficiaries undertuned (WR: 44.9%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1109). Shifted tuner focus: protected ultimate base floor at 36.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo. |
| `FLF` | Lightning | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 11268.6 -> **15388.2** | 3380.9 -> **3077.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 1509). Increasing spread: b -17.8%, n +36.6% |
| `FLW` | Lightning | Debuff / Control | 181.9 -> **200.5** (+10.2%) | - | 181.9 -> **200.5** | Buffed setup spell [FLW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD]; Individual spell overtuned (WR: 61.5%, Casts: 1999, mult: 0.958) |
| `FLE` | Lightning | Setup - Weather | 207.5 -> **238.6** (+15.0%) | - | 207.5 -> **238.6** | Buffed setup spell [FLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FLD] |
| `FLD` | Lightning | Ultimate | 73.8 -> **71.7** (-2.8%) | 199.1 -> **250.3** | 14767.4 -> **18018.2** | Weather 'Storming' beneficiaries overtuned (WR: 58.2%); Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1185). Shifted tuner focus: protected ultimate base floor at 73.8 (hard-coded floor >= 20.0) and buffed appliers/setups (EEF, FLW, LFE, LFD, WDF, LDW, FLE) with +15% b tempo. |
| `LFF` | Lightning | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 5163.8 -> **6996.9** | 1549.4 -> **2099.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.8% vs 30% floor, Casts: 998). Increasing spread: b -17.3%, n +35.5%; Individual spell undertuned (WR: 43.1%, Casts: 998, mult: 1.024) |
| `LFL` | Lightning | Debuff / Control | 59.2 -> **68.1** (+15.0%) | 1485.7 -> **1939.2** | 88012.6 -> **132127.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 2341). Increasing spread: b -14.9%, n +30.5%; Buffed setup spell [LFL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FDD] |
| `LFD` | Lightning | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 3592.2 -> **4805.8** | 2874.6 -> **3364.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.9% vs 30% floor, Casts: 1838). Increasing spread: b -16.5%, n +33.8%; Individual spell undertuned (WR: 38.6%, Casts: 1838, mult: 1.041) |
| `FDF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 7647.2 -> **10476.7** | 1529.6 -> **2095.5** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 939). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 55.5 -> **53.2** (-4.1%) | - | 55.5 -> **53.2** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Individual spell overtuned (WR: 54.9%, Casts: 1682, mult: 0.984) |
| `FDE` | Blood | Setup - Weather | 16.3 -> **15.9** (-2.5%) | - | 16.3 -> **15.9** | Class Blood overtuned (WR: 56.2%, factor: 0.975) |
| `FDD` | Blood | Ultimate | 51.6 -> **49.3** (-4.5%) | 73.1 -> **94.8** | 3823.6 -> **4722.9** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.3% vs 16% floor, Casts: 1099). Shifted tuner focus: protected ultimate base floor at 51.6 (hard-coded floor >= 20.0) and buffed appliers/setups (LLW, LFL, LDF, DDE) with +15% b tempo. |
| `DFF` | Blood | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 2629.9 -> **3508.8** | 526.2 -> **702.0** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Status 'Bleeding' beneficiaries undertuned (WR: 45.8%) |
| `DFE` | Blood | Buff / Sustain | 45.1 -> **44.0** (-2.4%) | - | 45.1 -> **44.0** | Class Blood overtuned (WR: 56.2%, factor: 0.975) |
| `DFL` | Blood | Buff / Sustain | 27.3 -> **26.6** (-2.6%) | - | 27.3 -> **26.6** | Class Blood overtuned (WR: 56.2%, factor: 0.975) |
| `DFD` | Blood | Conditional Strike | 513.3 -> **565.4** (+10.2%) | 0.1 -> **0.1** | 564.6 -> **621.9** | Class Blood overtuned (WR: 56.2%, factor: 0.975); Condition triggers excessively (N=1 conditions, Trigger Rate: 93.7% vs 55% ceiling, WR: 64.8%). Compressing spread: b +19.5%, n -27.7% |
| `WEF` | Plants | Conditional Strike | 0.8 -> **0.7** (-12.5%) | 1511.1 -> **1922.1** | 1209.7 -> **1346.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.8% vs 30% floor, Casts: 1547). Increasing spread: b -13.3%, n +27.2% |
| `WEW` | Plants | Debuff / Control | 1337.4 -> **1557.9** (+16.5%) | - | 1337.4 -> **1557.9** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD]; Individual spell undertuned (WR: 46.0%, Casts: 998, mult: 1.013) |
| `WEE` | Plants | Setup - Location | 18.4 -> **17.8** (-3.3%) | - | 18.4 -> **17.8** | Location 'Jungle' appliers overtuned on own (WR: 55.0%); Individual spell overtuned (WR: 55.0%, Casts: 1195, mult: 0.983) |
| `WED` | Plants | Conditional Strike | 19.1 -> **15.7** (-17.8%) | 23.4 -> **32.0** | 466.0 -> **518.1** | Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 0.1% vs 8% floor, Casts: 850). Increasing spread: b -17.8%, n +36.6% |
| `EWF` | Plants | Buff / Sustain | 0.6 -> **0.5** (-16.7%) | 1101.3 -> **1435.3** | 661.4 -> **718.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.0% vs 30% floor, Casts: 1449). Increasing spread: b -14.8%, n +30.3% |
| `EWW` | Plants | Debuff / Control | 1.1 -> **1.0** (-9.1%) | - | 1.1 -> **1.0** | Individual spell overtuned (WR: 76.8%, Casts: 1852, mult: 0.894) |
| `EWD` | Plants | Conditional Strike | 4.1 -> **4.7** (+14.6%) | 6210.8 -> **8631.3** | 25468.4 -> **40571.8** | Status 'Bleeding' appliers overtuned on own (WR: 58.9%); Status 'Entangled' beneficiaries undertuned (WR: 44.9%) |
| `WLF` | Fey | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 3353.2 -> **4375.6** | 3018.8 -> **3501.3** | Class Fey undertuned (WR: 46.5%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 1793). Increasing spread: b -14.9%, n +30.5% |
| `WLW` | Fey | Debuff / Control | 63.9 -> **64.9** (+1.6%) | - | 63.9 -> **64.9** | Class Fey undertuned (WR: 46.5%, factor: 1.014); Status 'Cursed' appliers overtuned on own (WR: 53.7%) |
| `WLE` | Fey | Setup - Location | 424.3 -> **457.6** (+7.8%) | - | 424.3 -> **457.6** | Class Fey undertuned (WR: 46.5%, factor: 1.014); Location 'Enchanted Forest' appliers overtuned on own (WR: 60.8%) |
| `WLL` | Fey | Direct Damage | 53.9 -> **54.7** (+1.5%) | - | 53.9 -> **54.7** | Class Fey undertuned (WR: 46.5%, factor: 1.014) |
| `WLD` | Fey | Ultimate | 20.3 -> **20.0** (-1.5%) | 2723.8 -> **3613.2** | 55313.4 -> **72284.0** | Class Fey undertuned (WR: 46.5%, factor: 1.014); Location 'Enchanted Forest' beneficiaries undertuned (WR: 44.9%) |
| `LWF` | Fey | Debuff / Control | 19.5 -> **18.1** (-7.2%) | 643.6 -> **815.4** | 12569.7 -> **14776.8** | Class Fey undertuned (WR: 46.5%, factor: 1.014); Location 'Enchanted Forest' beneficiaries undertuned (WR: 44.9%) |
| `LWW` | Fey | Debuff / Control | 49.6 -> **49.5** (-0.2%) | - | 49.6 -> **49.5** | Class Fey undertuned (WR: 46.5%, factor: 1.014); Individual spell overtuned (WR: 54.9%, Casts: 747, mult: 0.984) |
| `LWL` | Fey | Debuff / Control | 58.9 -> **63.3** (+7.5%) | - | 58.9 -> **63.3** | Class Fey undertuned (WR: 46.5%, factor: 1.014); Individual spell undertuned (WR: 33.9%, Casts: 1574, mult: 1.060) |
| `LWD` | Fey | Conditional Strike | 0.3 -> **0.2** (-33.3%) | 7647.2 -> **10476.7** | 2294.5 -> **2095.5** | Class Fey undertuned (WR: 46.5%, factor: 1.014); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 790). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 6902.3 -> **9097.2** | 6213.0 -> **7278.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.2% vs 30% floor, Casts: 1362). Increasing spread: b -15.5%, n +31.8% |
| `WDW` | Ice | Buff / Sustain | 10.0 -> **9.8** (-2.0%) | - | 10.0 -> **9.8** | Individual spell overtuned (WR: 56.6%, Casts: 1984, mult: 0.977) |
| `WDE` | Ice | Setup - Weather | 39.8 -> **40.8** (+2.5%) | - | 39.8 -> **40.8** | Individual spell undertuned (WR: 42.4%, Casts: 1699, mult: 1.026) |
| `WDL` | Ice | Debuff / Control | 39.6 -> **40.2** (+1.5%) | - | 39.6 -> **40.2** | Individual spell undertuned (WR: 45.4%, Casts: 915, mult: 1.015) |
| `WDD` | Ice | Ultimate | 30.7 -> **29.9** (-2.6%) | 410.7 -> **494.2** | 12639.2 -> **14806.5** | Weather 'Blizzard' beneficiaries overtuned (WR: 57.5%); Location 'Tundra' beneficiaries overtuned (WR: 57.5%) |
| `DWW` | Ice | Debuff / Control | 112.0 -> **113.4** (+1.3%) | - | 112.0 -> **113.4** | Individual spell undertuned (WR: 46.1%, Casts: 717, mult: 1.013) |
| `DWE` | Ice | Setup - Location | 45.3 -> **47.3** (+4.4%) | - | 45.3 -> **47.3** | Location 'Tundra' appliers undertuned (WR: 43.8%, casts: 1898); Individual spell undertuned (WR: 43.8%, Casts: 1898, mult: 1.021) |
| `DWL` | Ice | Debuff / Control | 41.4 -> **41.9** (+1.2%) | - | 41.4 -> **41.9** | Individual spell undertuned (WR: 46.0%, Casts: 2076, mult: 1.013) |
| `DWD` | Ice | Conditional Strike | 2.7 -> **2.4** (-11.1%) | 358.6 -> **436.4** | 970.9 -> **1049.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 18.4% vs 30% floor, Casts: 1367). Increasing spread: b -10.7%, n +21.7% |
| `ELF` | Wind | Conditional Strike | 1.5 -> **1.3** (-13.3%) | 2802.7 -> **3782.3** | 4205.5 -> **4918.3** | Status 'Bleeding' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.1% vs 30% floor, Casts: 1203). Increasing spread: b -15.9%, n +32.7% |
| `ELE` | Wind | Setup - Weather | 29.8 -> **30.5** (+2.3%) | - | 29.8 -> **30.5** | Individual spell undertuned (WR: 42.8%, Casts: 1622, mult: 1.025) |
| `ELD` | Wind | Conditional Strike | 0.9 -> **0.8** (-11.1%) | 5277.2 -> **6910.1** | 4750.4 -> **5528.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.3% vs 30% floor, Casts: 839). Increasing spread: b -15.1%, n +30.9% |
| `LEF` | Wind | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 2705.4 -> **3647.4** | 1353.2 -> **1459.4** | Status 'Burning' beneficiaries undertuned (WR: 46.0%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.2% vs 30% floor, Casts: 1021). Increasing spread: b -15.9%, n +32.7% |
| `LEW` | Wind | Debuff / Control | 56.4 -> **57.9** (+2.7%) | - | 56.4 -> **57.9** | Individual spell undertuned (WR: 42.4%, Casts: 2426, mult: 1.026) |
| `LEE` | Wind | Setup - Weather | 27.3 -> **26.6** (-2.6%) | - | 27.3 -> **26.6** | Individual spell overtuned (WR: 57.2%, Casts: 1282, mult: 0.975) |
| `EDF` | Poison | Conditional Strike | 0.3 -> **0.3** (+0.0%) | 2440.0 -> **3231.8** | 732.3 -> **969.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.5% vs 30% floor, Casts: 1961). Increasing spread: b -15.8%, n +32.5%; Individual spell undertuned (WR: 45.5%, Casts: 1961, mult: 1.015) |
| `EDE` | Poison | Setup - Location | 79.3 -> **96.1** (+21.2%) | - | 79.3 -> **96.1** | Location 'Swamp' appliers undertuned (WR: 42.4%, casts: 1316); Buffed setup spell [EDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `EDD` | Poison | Ultimate | 49.6 -> **49.6** (+0.0%) | 68.6 -> **89.8** | 3452.2 -> **4503.7** | Status 'Bleeding' beneficiaries undertuned (WR: 45.8%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 1.0% vs 16% floor, Casts: 1611). Shifted tuner focus: protected ultimate base floor at 49.6 (hard-coded floor >= 20.0) and buffed appliers/setups (WFE, FDL, DFW, EWD, EDE) with +15% b tempo. |
| `DEF` | Poison | Conditional Strike | 29.1 -> **29.7** (+2.1%) | 1.4 -> **1.4** | 69.8 -> **71.3** | Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 51.9% within [30%-55%] target window, WR: 43.9%).; Individual spell undertuned (WR: 43.9%, Casts: 1827, mult: 1.021) |
| `DEL` | Poison | Conditional Strike | 0.2 -> **0.2** (+0.0%) | 2719.2 -> **3599.6** | 544.0 -> **720.1** | Status 'Bleeding' beneficiaries undertuned (WR: 45.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 903). Increasing spread: b -14.7%, n +30.2% |
| `DED` | Poison | Debuff / Control | 22.8 -> **23.6** (+3.5%) | - | 22.8 -> **23.6** | Individual spell undertuned (WR: 40.0%, Casts: 1479, mult: 1.036) |
| `LDF` | Cosmic | Debuff / Control | 133.0 -> **130.4** (-2.0%) | - | 133.0 -> **130.4** | Individual spell overtuned (WR: 55.7%, Casts: 990, mult: 0.981) |
| `LDE` | Cosmic | Setup - Location | 27.7 -> **27.3** (-1.4%) | - | 27.7 -> **27.3** | Individual spell overtuned (WR: 54.1%, Casts: 1164, mult: 0.987) |
| `LDL` | Cosmic | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 4043.2 -> **5423.6** | 2022.1 -> **2169.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 3.4% vs 30% floor, Casts: 1138). Increasing spread: b -16.6%, n +34.1% |
| `LDD` | Cosmic | Ultimate | 118.2 -> **127.7** (+8.0%) | 20.7 -> **19.5** | 2564.9 -> **2617.8** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2124, WR: 48.1%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DLF` | Cosmic | Conditional Strike | 0.5 -> **0.4** (-20.0%) | 2928.6 -> **3893.8** | 1464.8 -> **1557.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 1216). Increasing spread: b -16.1%, n +33.0%; Individual spell undertuned (WR: 43.7%, Casts: 1216, mult: 1.021) |
| `DLW` | Cosmic | Direct Damage | 54.1 -> **55.5** (+2.6%) | - | 54.1 -> **55.5** | Individual spell undertuned (WR: 42.4%, Casts: 1028, mult: 1.026) |
| `DLL` | Cosmic | Conditional Strike | 2.0 -> **1.7** (-15.0%) | 1209.5 -> **1607.8** | 2421.0 -> **2735.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.9% vs 30% floor, Casts: 1414). Increasing spread: b -16.0%, n +32.9%; Individual spell undertuned (WR: 39.4%, Casts: 1414, mult: 1.038) |
