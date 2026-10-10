# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T21:24:28Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 697.2s  
**Total Spells Tuned:** 107 / 125  

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
| **Poison** | 18,231 | 55.7% | 55.7% | 10.6 | Overtuned ⚠️ |
| **Blood** | 19,247 | 54.8% | 54.8% | 12.1 | Overtuned ⚠️ |
| **Dark** | 11,001 | 53.8% | 53.8% | 11.5 | Overtuned ⚠️ |
| **Plants** | 19,981 | 53.5% | 53.6% | 8.6 | Overtuned ⚠️ |
| **Beasts** | 17,406 | 52.3% | 52.3% | 6.8 | Balanced ✅ |
| **Light** | 11,651 | 51.7% | 51.8% | 4.5 | Balanced ✅ |
| **Water** | 8,133 | 50.9% | 50.9% | 10.2 | Balanced ✅ |
| **Ghostfire** | 24,253 | 50.5% | 50.5% | 12.2 | Balanced ✅ |
| **Fire** | 7,919 | 49.2% | 49.2% | 14.7 | Balanced ✅ |
| **Wind** | 17,660 | 48.5% | 48.5% | 7.5 | Balanced ✅ |
| **Fey** | 17,556 | 47.2% | 47.2% | 8.8 | Balanced ✅ |
| **Cosmic** | 19,526 | 47.2% | 47.2% | 14.8 | Balanced ✅ |
| **Earth** | 9,392 | 47.1% | 47.1% | 16.9 | Balanced ✅ |
| **Lightning** | 21,205 | 45.2% | 45.2% | 10.0 | Undertuned ⚠️ |
| **Ice** | 18,943 | 44.6% | 44.6% | 10.6 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 5,668 (48.3%) | 3,873 (46.5%) | 29.6% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,084 (53.3%) | 3,677 (53.5%) | 6.0% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,667 (54.3%) | 4,794 (48.8%) | 10.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 10,683 (62.8%) | 7,755 (50.5%) | 6.4% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 14,867 (42.1%) | 3,295 (45.0%) | 0.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 1,703 (52.7%) | 6,061 (48.2%) | 1.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,595 (45.0%) | 4,556 (45.5%) | 6.8% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 48.5 -> **47.8** (-1.4%) | - | 48.5 -> **47.8** | Status 'Burning' appliers overtuned on own (WR: 54.3%) |
| `FFE` | Fire | Debuff / Control | 35.7 -> **36.1** (+1.1%) | - | 35.7 -> **36.1** | Individual spell undertuned (WR: 46.3%, Casts: 1391, mult: 1.012) |
| `FFL` | Fire | Debuff / Control | 8.5 -> **8.2** (-3.5%) | - | 8.5 -> **8.2** | Status 'Burning' appliers overtuned on own (WR: 54.3%); Individual spell overtuned (WR: 57.6%, Casts: 1477, mult: 0.974) |
| `FFD` | Fire | Conditional Strike | 14.1 -> **12.1** (-14.2%) | 6.2 -> **8.0** | 101.5 -> **108.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.1% vs 30% floor, Casts: 1752). Increasing spread: b -14.4%, n +29.4% |
| `WWF` | Water | Conditional Strike | 23.8 -> **20.7** (-13.0%) | 5.8 -> **7.3** | 161.8 -> **171.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.7% vs 30% floor, Casts: 1365). Increasing spread: b -12.9%, n +26.4% |
| `WWE` | Water | Setup - Weather | 21.3 -> **22.0** (+3.3%) | - | 21.3 -> **22.0** | Weather 'Raining' appliers undertuned (WR: 45.0%, casts: 1595); Individual spell undertuned (WR: 45.0%, Casts: 1595, mult: 1.017) |
| `EEF` | Earth | Conditional Strike | 30.0 -> **31.4** (+4.7%) | 3.7 -> **3.7** | 141.0 -> **147.6** | Status 'Stunned' appliers undertuned (WR: 42.1%, casts: 14867); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 32.2% within [30%-55%] target window, WR: 44.5%). |
| `EEE` | Earth | Conditional Strike | 6.3 -> **7.1** (+12.7%) | 1.5 -> **1.5** | 15.8 -> **17.8** | Condition triggers excessively (N=1 conditions, Trigger Rate: 92.0% vs 55% ceiling, WR: 49.4%). Compressing spread: b +13.2%, n -21.2% |
| `LLF` | Light | Conditional Strike | 2.6 -> **3.0** (+15.4%) | 6.3 -> **8.2** | 19.0 -> **27.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.6% vs 30% floor, Casts: 2910). Increasing spread: b -14.5%, n +29.8%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLW` | Light | Debuff / Control | 33.0 -> **34.1** (+3.3%) | - | 33.0 -> **34.1** | Individual spell undertuned (WR: 40.7%, Casts: 2726, mult: 1.033) |
| `LLE` | Light | Setup - Weather | 19.4 -> **22.3** (+14.9%) | - | 19.4 -> **22.3** | Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 32.0 -> **30.5** (-4.7%) | - | 32.0 -> **30.5** | Individual spell overtuned (WR: 62.4%, Casts: 2704, mult: 0.955) |
| `LLD` | Light | Ultimate | 30.0 -> **29.5** (-1.7%) | 5.7 -> **7.3** | 201.0 -> **244.9** | Weather 'Sunny' beneficiaries overtuned (WR: 53.5%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.2% vs 16% floor, Casts: 1227). Shifted tuner focus: protected ultimate base floor at 30.0 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 11.7 -> **9.3** (-20.5%) | 7.5 -> **10.3** | 99.4 -> **105.1** | Class Dark overtuned (WR: 53.8%, factor: 0.985); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2271). Increasing spread: b -18.0%, n +37.0% |
| `DDW` | Dark | Debuff / Control | 53.8 -> **53.0** (-1.5%) | - | 53.8 -> **53.0** | Class Dark overtuned (WR: 53.8%, factor: 0.985) |
| `DDE` | Dark | Setup - Weather | 28.1 -> **31.8** (+13.2%) | - | 28.1 -> **31.8** | Class Dark overtuned (WR: 53.8%, factor: 0.985); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 28.7 -> **27.8** (-3.1%) | - | 28.7 -> **27.8** | Class Dark overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 54.5%, Casts: 2060, mult: 0.985) |
| `DDD` | Dark | Debuff / Control | 33.3 -> **31.6** (-5.1%) | - | 33.3 -> **31.6** | Class Dark overtuned (WR: 53.8%, factor: 0.985); Individual spell overtuned (WR: 60.3%, Casts: 1301, mult: 0.963) |
| `FWF` | Ghostfire | Debuff / Control | 45.0 -> **43.7** (-2.9%) | - | 45.0 -> **43.7** | Status 'Burning' appliers overtuned on own (WR: 54.3%); Individual spell overtuned (WR: 54.5%, Casts: 1954, mult: 0.985) |
| `FWW` | Ghostfire | Debuff / Control | 19.8 -> **23.4** (+18.2%) | - | 19.8 -> **23.4** | Buffed setup spell [FWW] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD]; Individual spell undertuned (WR: 42.2%, Casts: 2962, mult: 1.027) |
| `FWE` | Ghostfire | Setup - Location | 30.9 -> **38.8** (+25.6%) | - | 30.9 -> **38.8** | Location 'Graveyard' appliers undertuned (WR: 37.5%, casts: 4286); Buffed setup spell [FWE] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD] |
| `FWL` | Ghostfire | Debuff / Control | 59.5 -> **66.6** (+11.9%) | - | 59.5 -> **66.6** | Buffed setup spell [FWL] (+15.0% b tempo) to facilitate under-triggered Ultimate [FWD]; Individual spell overtuned (WR: 57.8%, Casts: 2136, mult: 0.973) |
| `FWD` | Ghostfire | Ultimate | 25.5 -> **25.5** (+0.0%) | 11.4 -> **14.7** | 316.2 -> **400.3** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.3% vs 8% floor, Casts: 1011). Shifted tuner focus: protected ultimate base floor at 25.5 (hard-coded floor >= 20.0) and buffed appliers/setups (FWW, FWL, WLW, FDE, ELF, FWE) with +15% b tempo. |
| `WFF` | Ghostfire | Conditional Strike | 14.0 -> **11.7** (-16.4%) | 6.3 -> **8.2** | 102.2 -> **107.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 1879). Increasing spread: b -14.8%, n +30.3%; Individual spell overtuned (WR: 55.5%, Casts: 1879, mult: 0.982) |
| `WFW` | Ghostfire | Debuff / Control | 32.2 -> **31.1** (-3.4%) | - | 32.2 -> **31.1** | Individual spell overtuned (WR: 59.2%, Casts: 4668, mult: 0.967) |
| `WFE` | Ghostfire | Debuff / Control | 41.3 -> **43.3** (+4.8%) | - | 41.3 -> **43.3** | Status 'Bleeding' appliers overtuned on own (WR: 62.8%); Buffed setup spell [WFE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `WFL` | Ghostfire | Buff / Sustain | 36.5 -> **36.0** (-1.4%) | - | 36.5 -> **36.0** | Individual spell overtuned (WR: 54.1%, Casts: 862, mult: 0.987) |
| `WFD` | Ghostfire | Conditional Strike | 15.0 -> **13.3** (-11.3%) | 5.9 -> **7.5** | 103.5 -> **113.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.6% vs 30% floor, Casts: 2779). Increasing spread: b -13.4%, n +27.3%; Individual spell undertuned (WR: 43.6%, Casts: 2779, mult: 1.022) |
| `FEW` | Beasts | Conditional Strike | 12.1 -> **10.0** (-17.4%) | 7.5 -> **10.2** | 102.8 -> **112.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.9% vs 30% floor, Casts: 1206). Increasing spread: b -17.6%, n +36.2% |
| `FEE` | Beasts | Buff / Sustain | 24.5 -> **25.0** (+2.0%) | - | 24.5 -> **25.0** | Individual spell undertuned (WR: 44.4%, Casts: 1714, mult: 1.019) |
| `FED` | Beasts | Conditional Strike | 6.8 -> **7.3** (+7.4%) | 1.6 -> **1.5** | 17.7 -> **18.2** | Condition triggers excessively (N=1 conditions, Trigger Rate: 60.5% vs 55% ceiling, WR: 52.7%). Compressing spread: b +7.3%, n -11.0% |
| `EFF` | Beasts | Debuff / Control | 15.1 -> **12.4** (-17.9%) | 7.3 -> **10.0** | 125.3 -> **136.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.8% vs 30% floor, Casts: 1806). Increasing spread: b -17.7%, n +36.4% |
| `EFW` | Beasts | Buff / Sustain | 23.1 -> **24.3** (+5.2%) | - | 23.1 -> **24.3** | Individual spell undertuned (WR: 35.7%, Casts: 1594, mult: 1.053) |
| `EFE` | Beasts | Buff / Sustain | 33.5 -> **32.8** (-2.1%) | - | 33.5 -> **32.8** | Individual spell overtuned (WR: 56.2%, Casts: 3022, mult: 0.979) |
| `EFL` | Beasts | Buff / Sustain | 21.9 -> **18.9** (-13.7%) | - | 21.9 -> **18.9** | Individual spell overtuned (WR: 84.0%, Casts: 1405, mult: 0.862) |
| `EFD` | Beasts | Ultimate | 25.1 -> **27.6** (+10.0%) | 11.7 -> **11.2** | 318.8 -> **336.7** | Location 'Jungle' beneficiaries undertuned (WR: 45.4%); Multi-condition setup trap (N=2 conditions, Trigger Rate: 0.5% vs 16% floor, Casts: 1325, WR: 44.4%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `FLF` | Lightning | Conditional Strike | 12.4 -> **10.4** (-16.1%) | 7.8 -> **10.9** | 109.1 -> **123.8** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' beneficiaries undertuned (WR: 45.0%) |
| `FLW` | Lightning | Debuff / Control | 52.4 -> **54.9** (+4.8%) | - | 52.4 -> **54.9** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' appliers undertuned (WR: 42.1%, casts: 14867) |
| `FLE` | Lightning | Setup - Weather | 28.2 -> **29.9** (+6.0%) | - | 28.2 -> **29.9** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Weather 'Storming' appliers undertuned (WR: 44.3%, casts: 2445) |
| `FLL` | Lightning | Buff / Sustain | 25.5 -> **26.0** (+2.0%) | - | 25.5 -> **26.0** | Class Lightning undertuned (WR: 45.2%, factor: 1.019) |
| `FLD` | Lightning | Ultimate | 28.8 -> **32.7** (+13.5%) | 9.2 -> **9.1** | 293.8 -> **330.3** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' beneficiaries undertuned (WR: 45.0%) |
| `LFF` | Lightning | Conditional Strike | 12.9 -> **11.0** (-14.7%) | 7.1 -> **9.5** | 104.5 -> **115.5** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.3% vs 30% floor, Casts: 2066). Increasing spread: b -16.3%, n +33.4% |
| `LFE` | Lightning | Debuff / Control | 44.8 -> **46.9** (+4.7%) | - | 44.8 -> **46.9** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' appliers undertuned (WR: 42.1%, casts: 14867) |
| `LFL` | Lightning | Debuff / Control | 44.1 -> **39.5** (-10.4%) | 5.9 -> **7.4** | 304.3 -> **331.8** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 14.5% vs 30% floor, Casts: 2417). Increasing spread: b -12.2%, n +24.9% |
| `LFD` | Lightning | Conditional Strike | 14.9 -> **14.6** (-2.0%) | 9.4 -> **12.0** | 155.0 -> **189.8** | Class Lightning undertuned (WR: 45.2%, factor: 1.019); Status 'Stunned' appliers undertuned (WR: 42.1%, casts: 14867) |
| `FDF` | Blood | Conditional Strike | 12.2 -> **9.8** (-19.7%) | 7.5 -> **10.3** | 103.7 -> **110.7** | Class Blood overtuned (WR: 54.8%, factor: 0.981); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1562). Increasing spread: b -18.0%, n +37.0% |
| `FDW` | Blood | Direct Damage | 59.3 -> **58.2** (-1.9%) | - | 59.3 -> **58.2** | Class Blood overtuned (WR: 54.8%, factor: 0.981) |
| `FDE` | Blood | Setup - Weather | 20.0 -> **20.3** (+1.5%) | - | 20.0 -> **20.3** | Class Blood overtuned (WR: 54.8%, factor: 0.981); Individual spell undertuned (WR: 40.1%, Casts: 2599, mult: 1.036) |
| `FDL` | Blood | Debuff / Control | 36.1 -> **35.3** (-2.2%) | - | 36.1 -> **35.3** | Class Blood overtuned (WR: 54.8%, factor: 0.981); Status 'Bleeding' appliers overtuned on own (WR: 62.8%) |
| `FDD` | Blood | Ultimate | 26.2 -> **28.4** (+8.4%) | 8.4 -> **7.9** | 246.3 -> **252.8** | Class Blood overtuned (WR: 54.8%, factor: 0.981); Multi-condition setup trap (N=2 conditions, Trigger Rate: 1.9% vs 16% floor, Casts: 1689, WR: 43.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0% |
| `DFF` | Blood | Conditional Strike | 13.7 -> **11.7** (-14.6%) | 6.0 -> **7.8** | 95.9 -> **103.0** | Class Blood overtuned (WR: 54.8%, factor: 0.981); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.9% vs 30% floor, Casts: 1609). Increasing spread: b -14.4%, n +29.6% |
| `DFE` | Blood | Buff / Sustain | 35.6 -> **34.5** (-3.1%) | - | 35.6 -> **34.5** | Class Blood overtuned (WR: 54.8%, factor: 0.981); Individual spell overtuned (WR: 53.6%, Casts: 1681, mult: 0.988) |
| `DFL` | Blood | Buff / Sustain | 33.7 -> **33.1** (-1.8%) | - | 33.7 -> **33.1** | Class Blood overtuned (WR: 54.8%, factor: 0.981) |
| `DFD` | Blood | Conditional Strike | 40.6 -> **45.4** (+11.8%) | 0.9 -> **0.7** | 77.1 -> **77.2** | Class Blood overtuned (WR: 54.8%, factor: 0.981); Condition triggers excessively (N=1 conditions, Trigger Rate: 95.7% vs 55% ceiling, WR: 51.6%). Compressing spread: b +14.0%, n -22.5% |
| `WEF` | Plants | Conditional Strike | 16.1 -> **13.8** (-14.3%) | 5.5 -> **7.2** | 104.7 -> **113.2** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Location 'Jungle' beneficiaries undertuned (WR: 45.4%) |
| `WEW` | Plants | Debuff / Control | 48.2 -> **56.3** (+16.8%) | - | 48.2 -> **56.3** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WEE` | Plants | Setup - Location | 20.2 -> **19.9** (-1.5%) | - | 20.2 -> **19.9** | Class Plants overtuned (WR: 53.5%, factor: 0.986) |
| `WEL` | Plants | Debuff / Control | 42.3 -> **41.7** (-1.4%) | - | 42.3 -> **41.7** | Class Plants overtuned (WR: 53.5%, factor: 0.986) |
| `WED` | Plants | Conditional Strike | 12.7 -> **10.1** (-20.5%) | 10.2 -> **13.7** | 142.2 -> **148.5** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Conditional payoff under-triggered (N=3 conditions, Trigger Rate: 1.0% vs 8% floor, Casts: 1129). Increasing spread: b -16.5%, n +34.0% |
| `EWF` | Plants | Buff / Sustain | 17.7 -> **14.9** (-15.8%) | 5.4 -> **6.9** | 113.3 -> **117.7** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Weather 'Sunny' beneficiaries overtuned (WR: 53.5%) |
| `EWW` | Plants | Debuff / Control | 29.3 -> **24.7** (-15.7%) | - | 29.3 -> **24.7** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Individual spell overtuned (WR: 85.5%, Casts: 2111, mult: 0.856) |
| `EWL` | Plants | Debuff / Control | 60.0 -> **59.1** (-1.5%) | - | 60.0 -> **59.1** | Class Plants overtuned (WR: 53.5%, factor: 0.986) |
| `EWD` | Plants | Conditional Strike | 16.2 -> **17.5** (+8.0%) | 7.4 -> **10.0** | 136.1 -> **192.5** | Class Plants overtuned (WR: 53.5%, factor: 0.986); Status 'Bleeding' appliers overtuned on own (WR: 62.8%) |
| `WLF` | Fey | Conditional Strike | 13.7 -> **11.7** (-14.6%) | 6.5 -> **8.6** | 102.8 -> **112.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.4% vs 30% floor, Casts: 1845). Increasing spread: b -15.4%, n +31.7%; Individual spell undertuned (WR: 46.1%, Casts: 1845, mult: 1.013) |
| `WLE` | Fey | Setup - Location | 28.9 -> **33.2** (+14.9%) | - | 28.9 -> **33.2** | Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 62.7 -> **63.4** (+1.1%) | - | 62.7 -> **63.4** | Individual spell undertuned (WR: 46.4%, Casts: 1565, mult: 1.012) |
| `WLD` | Fey | Ultimate | 26.1 -> **26.1** (+0.0%) | 11.8 -> **15.3** | 334.1 -> **425.4** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 2011). Shifted tuner focus: protected ultimate base floor at 26.1 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo. |
| `LWF` | Fey | Debuff / Control | 33.0 -> **29.6** (-10.3%) | 5.2 -> **6.3** | 204.6 -> **216.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 19.6% vs 30% floor, Casts: 1815). Increasing spread: b -10.2%, n +20.7% |
| `LWW` | Fey | Debuff / Control | 36.2 -> **36.9** (+1.9%) | - | 36.2 -> **36.9** | Individual spell undertuned (WR: 44.5%, Casts: 1422, mult: 1.019) |
| `LWL` | Fey | Debuff / Control | 36.7 -> **37.5** (+2.2%) | - | 36.7 -> **37.5** | Individual spell undertuned (WR: 43.8%, Casts: 1992, mult: 1.021) |
| `LWD` | Fey | Conditional Strike | 12.9 -> **10.6** (-17.8%) | 7.5 -> **10.3** | 109.7 -> **119.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1796). Increasing spread: b -18.0%, n +37.0% |
| `WDF` | Ice | Conditional Strike | 13.4 -> **12.2** (-9.0%) | 7.0 -> **9.4** | 107.2 -> **126.9** | Class Ice undertuned (WR: 44.6%, factor: 1.022); Status 'Stunned' appliers undertuned (WR: 42.1%, casts: 14867) |
| `WDE` | Ice | Setup - Weather | 20.3 -> **21.6** (+6.4%) | - | 20.3 -> **21.6** | Class Ice undertuned (WR: 44.6%, factor: 1.022); Individual spell undertuned (WR: 39.0%, Casts: 2596, mult: 1.040) |
| `WDL` | Ice | Debuff / Control | 45.8 -> **46.8** (+2.2%) | - | 45.8 -> **46.8** | Class Ice undertuned (WR: 44.6%, factor: 1.022) |
| `WDD` | Ice | Ultimate | 28.1 -> **28.7** (+2.1%) | 8.1 -> **10.1** | 255.7 -> **318.6** | Class Ice undertuned (WR: 44.6%, factor: 1.022); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 4.1% vs 16% floor, Casts: 1836). Shifted tuner focus: protected ultimate base floor at 28.1 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWF` | Ice | Debuff / Control | 44.2 -> **45.2** (+2.3%) | - | 44.2 -> **45.2** | Class Ice undertuned (WR: 44.6%, factor: 1.022) |
| `DWW` | Ice | Debuff / Control | 42.1 -> **44.2** (+5.0%) | - | 42.1 -> **44.2** | Class Ice undertuned (WR: 44.6%, factor: 1.022); Individual spell undertuned (WR: 42.4%, Casts: 1657, mult: 1.027) |
| `DWE` | Ice | Setup - Location | 22.3 -> **24.2** (+8.5%) | - | 22.3 -> **24.2** | Class Ice undertuned (WR: 44.6%, factor: 1.022); Location 'Tundra' appliers undertuned (WR: 41.1%, casts: 3958) |
| `DWL` | Ice | Debuff / Control | 43.9 -> **46.0** (+4.8%) | - | 43.9 -> **46.0** | Class Ice undertuned (WR: 44.6%, factor: 1.022); Individual spell undertuned (WR: 42.9%, Casts: 1738, mult: 1.025) |
| `DWD` | Ice | Conditional Strike | 20.3 -> **18.9** (-6.9%) | 4.2 -> **5.0** | 105.6 -> **113.4** | Class Ice undertuned (WR: 44.6%, factor: 1.022); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 22.7% vs 30% floor, Casts: 1053). Increasing spread: b -8.9%, n +18.1% |
| `ELF` | Wind | Conditional Strike | 29.7 -> **25.3** (-14.8%) | 6.2 -> **8.1** | 213.8 -> **230.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.1% vs 30% floor, Casts: 1449). Increasing spread: b -14.7%, n +30.2% |
| `ELE` | Wind | Setup - Weather | 20.6 -> **20.3** (-1.5%) | - | 20.6 -> **20.3** | Individual spell overtuned (WR: 54.2%, Casts: 1269, mult: 0.986) |
| `ELL` | Wind | Buff / Sustain | 34.5 -> **35.9** (+4.1%) | - | 34.5 -> **35.9** | Individual spell undertuned (WR: 39.0%, Casts: 1773, mult: 1.040) |
| `ELD` | Wind | Conditional Strike | 15.0 -> **12.8** (-14.7%) | 6.2 -> **8.2** | 108.0 -> **117.8** | Weather 'Raining' beneficiaries undertuned (WR: 45.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.8% vs 30% floor, Casts: 2381). Increasing spread: b -14.9%, n +30.5% |
| `LEF` | Wind | Conditional Strike | 13.5 -> **11.7** (-13.3%) | 7.0 -> **9.0** | 108.0 -> **117.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 11.0% vs 30% floor, Casts: 1677). Increasing spread: b -13.6%, n +27.9% |
| `LEW` | Wind | Debuff / Control | 57.8 -> **56.7** (-1.9%) | - | 57.8 -> **56.7** | Individual spell overtuned (WR: 55.8%, Casts: 2010, mult: 0.980) |
| `LEE` | Wind | Setup - Weather | 20.0 -> **20.3** (+1.5%) | - | 20.0 -> **20.3** | Individual spell undertuned (WR: 45.7%, Casts: 2300, mult: 1.014) |
| `EDF` | Poison | Conditional Strike | 12.6 -> **10.3** (-18.3%) | 6.4 -> **8.5** | 93.2 -> **97.9** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.5% vs 30% floor, Casts: 1995). Increasing spread: b -16.2%, n +33.2% |
| `EDW` | Poison | Debuff / Control | 30.9 -> **29.7** (-3.9%) | - | 30.9 -> **29.7** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Individual spell overtuned (WR: 55.2%, Casts: 1257, mult: 0.983) |
| `EDE` | Poison | Setup - Location | 21.3 -> **24.9** (+16.9%) | - | 21.3 -> **24.9** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Location 'Swamp' appliers undertuned (WR: 44.4%, casts: 1679) |
| `EDL` | Poison | Debuff / Control | 14.1 -> **11.8** (-16.3%) | - | 14.1 -> **11.8** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Individual spell overtuned (WR: 85.4%, Casts: 2678, mult: 0.856) |
| `EDD` | Poison | Ultimate | 26.3 -> **25.7** (-2.3%) | 8.5 -> **11.0** | 249.8 -> **308.4** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.7% vs 16% floor, Casts: 1821). Shifted tuner focus: protected ultimate base floor at 26.3 (hard-coded floor >= 20.0) and buffed appliers/setups (WFE, FDL, DFW, EWD, EDE) with +15% b tempo. |
| `DEF` | Poison | Conditional Strike | 37.5 -> **36.6** (-2.4%) | 1.7 -> **1.7** | 101.2 -> **98.8** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 50.7% within [30%-55%] target window, WR: 47.0%). |
| `DEW` | Poison | Debuff / Control | 30.8 -> **29.4** (-4.5%) | - | 30.8 -> **29.4** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Individual spell overtuned (WR: 56.8%, Casts: 3500, mult: 0.977) |
| `DEE` | Poison | Debuff / Control | 26.7 -> **26.4** (-1.1%) | - | 26.7 -> **26.4** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Individual spell undertuned (WR: 46.2%, Casts: 1507, mult: 1.012) |
| `DEL` | Poison | Conditional Strike | 1.4 -> **1.2** (-14.3%) | 6.1 -> **8.0** | 9.9 -> **10.8** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.3% vs 30% floor, Casts: 997). Increasing spread: b -15.1%, n +30.9% |
| `DED` | Poison | Debuff / Control | 27.1 -> **27.0** (-0.4%) | - | 27.1 -> **27.0** | Class Poison overtuned (WR: 55.7%, factor: 0.977); Individual spell undertuned (WR: 44.3%, Casts: 1666, mult: 1.019) |
| `LDF` | Cosmic | Debuff / Control | 54.8 -> **56.3** (+2.7%) | - | 54.8 -> **56.3** | Individual spell undertuned (WR: 42.2%, Casts: 1667, mult: 1.027) |
| `LDW` | Cosmic | Debuff / Control | 46.5 -> **48.6** (+4.5%) | - | 46.5 -> **48.6** | Status 'Stunned' appliers undertuned (WR: 42.1%, casts: 14867); Individual spell undertuned (WR: 44.8%, Casts: 2304, mult: 1.017) |
| `LDE` | Cosmic | Setup - Location | 20.9 -> **21.3** (+1.9%) | - | 20.9 -> **21.3** | Individual spell undertuned (WR: 44.5%, Casts: 1537, mult: 1.019) |
| `LDL` | Cosmic | Conditional Strike | 14.5 -> **12.6** (-13.1%) | 6.4 -> **8.3** | 107.3 -> **117.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.5% vs 30% floor, Casts: 1826). Increasing spread: b -14.6%, n +29.9%; Individual spell undertuned (WR: 44.1%, Casts: 1826, mult: 1.020) |
| `LDD` | Cosmic | Ultimate | 28.9 -> **32.0** (+10.7%) | 8.3 -> **7.8** | 268.8 -> **281.6** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2432, WR: 42.6%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 42.6%, Casts: 2432, mult: 1.026) |
| `DLF` | Cosmic | Conditional Strike | 16.8 -> **14.2** (-15.5%) | 6.5 -> **8.6** | 126.0 -> **136.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.8% vs 30% floor, Casts: 2219). Increasing spread: b -15.7%, n +32.2% |
| `DLW` | Cosmic | Direct Damage | 62.1 -> **59.9** (-3.5%) | - | 62.1 -> **59.9** | Individual spell overtuned (WR: 60.1%, Casts: 1848, mult: 0.964) |
| `DLE` | Cosmic | Direct Damage | 36.8 -> **37.5** (+1.9%) | - | 36.8 -> **37.5** | Individual spell undertuned (WR: 44.6%, Casts: 2113, mult: 1.018) |
| `DLL` | Cosmic | Conditional Strike | 30.7 -> **27.3** (-11.1%) | 4.4 -> **5.5** | 165.8 -> **177.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.7% vs 30% floor, Casts: 1821). Increasing spread: b -12.5%, n +25.6%; Individual spell undertuned (WR: 44.8%, Casts: 1821, mult: 1.017) |
| `DLD` | Cosmic | Conditional Strike | 53.5 -> **60.0** (+12.1%) | 1.5 -> **1.5** | 133.8 -> **150.0** | Condition triggers excessively (N=1 conditions, Trigger Rate: 94.7% vs 55% ceiling, WR: 51.9%). Compressing spread: b +13.8%, n -22.1% |
