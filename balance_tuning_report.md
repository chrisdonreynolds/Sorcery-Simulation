# Project Sorcery - Simulation & Dynamic Spell Balancing Report

**Date:** 2026-10-10T22:54:49Z  
**Simulation Mode:** games  
**Total Games Simulated:** 10,000  
**Evaluated Games Window:** 5,000 matches  
**Simulation Runtime:** 563.5s  
**Total Spells Tuned:** 98 / 125  

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
| **Poison** | 22,487 | 56.3% | 56.3% | 10.8 | Overtuned ⚠️ |
| **Earth** | 9,229 | 52.8% | 52.8% | 18.4 | Balanced ✅ |
| **Blood** | 19,371 | 52.2% | 52.2% | 12.1 | Balanced ✅ |
| **Beasts** | 17,828 | 51.7% | 51.7% | 6.5 | Balanced ✅ |
| **Dark** | 9,795 | 51.2% | 51.2% | 12.0 | Balanced ✅ |
| **Plants** | 21,715 | 51.2% | 51.2% | 8.9 | Balanced ✅ |
| **Fire** | 9,450 | 50.5% | 50.5% | 14.1 | Balanced ✅ |
| **Ghostfire** | 21,142 | 50.3% | 50.3% | 14.7 | Balanced ✅ |
| **Light** | 11,209 | 49.0% | 49.0% | 6.0 | Balanced ✅ |
| **Lightning** | 19,859 | 48.9% | 48.9% | 10.3 | Balanced ✅ |
| **Ice** | 19,758 | 48.1% | 48.1% | 13.0 | Balanced ✅ |
| **Cosmic** | 18,029 | 47.6% | 47.6% | 15.9 | Balanced ✅ |
| **Fey** | 19,563 | 47.4% | 47.4% | 7.7 | Balanced ✅ |
| **Wind** | 18,324 | 46.8% | 46.8% | 7.8 | Balanced ✅ |
| **Water** | 9,619 | 46.4% | 46.4% | 10.2 | Undertuned ⚠️ |

---

## Key Status & Weather Synergy Loops

| Synergy Group | Applier Casts (WR) | Beneficiary Casts (WR) | Trigger Rate | Synergy Pipeline Health |
| :--- | :---: | :---: | :---: | :--- |
| **Frosty** (status) | 6,954 (53.5%) | 3,874 (53.0%) | 22.8% | Under-Triggered ⚠️ (Spread Widened) |
| **Sunny** (weather) | 2,734 (35.9%) | 4,898 (56.5%) | 9.1% | Under-Triggered ⚠️ (Spread Widened) |
| **Burning** (status) | 4,579 (56.0%) | 6,009 (47.8%) | 9.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Bleeding** (status) | 8,929 (65.7%) | 9,475 (49.5%) | 7.3% | Under-Triggered ⚠️ (Spread Widened) |
| **Stunned** (status) | 13,185 (46.1%) | 4,029 (43.4%) | 0.2% | Under-Triggered ⚠️ (Spread Widened) |
| **Entangled** (status) | 2,889 (52.6%) | 4,718 (48.7%) | 2.5% | Under-Triggered ⚠️ (Spread Widened) |
| **Raining** (weather) | 1,371 (47.9%) | 5,542 (37.8%) | 5.0% | Under-Triggered ⚠️ (Spread Widened) |

---

## Detailed Spell Knob Adjustments (Changelog)

| Spell | Class | Category | b (Old -> New) | n (Old -> New) | Max Pot. (Old -> New) | Primary Balancing Rationale |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `FFW` | Fire | Debuff / Control | 46.6 -> **45.6** (-2.1%) | - | 46.6 -> **45.6** | Status 'Burning' appliers overtuned on own (WR: 56.0%) |
| `FFL` | Fire | Debuff / Control | 7.2 -> **6.9** (-4.2%) | - | 7.2 -> **6.9** | Status 'Burning' appliers overtuned on own (WR: 56.0%); Individual spell overtuned (WR: 57.9%, Casts: 1820, mult: 0.973) |
| `FFD` | Fire | Conditional Strike | 7.7 -> **6.7** (-13.0%) | 17.8 -> **23.0** | 144.8 -> **160.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 9.6% vs 30% floor, Casts: 2478). Increasing spread: b -14.2%, n +29.0%; Individual spell undertuned (WR: 45.6%, Casts: 2478, mult: 1.014) |
| `WWF` | Water | Conditional Strike | 14.2 -> **12.9** (-9.2%) | 14.9 -> **18.9** | 225.8 -> **256.7** | Class Water undertuned (WR: 46.4%, factor: 1.015); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.3% vs 30% floor, Casts: 1756). Increasing spread: b -13.1%, n +26.7% |
| `WWE` | Water | Setup - Weather | 27.8 -> **28.2** (+1.4%) | - | 27.8 -> **28.2** | Class Water undertuned (WR: 46.4%, factor: 1.015) |
| `WWL` | Water | Buff / Sustain | 64.8 -> **67.6** (+4.3%) | - | 64.8 -> **67.6** | Class Water undertuned (WR: 46.4%, factor: 1.015); Individual spell undertuned (WR: 42.0%, Casts: 2766, mult: 1.028) |
| `WWD` | Water | Buff / Sustain | 47.8 -> **48.5** (+1.5%) | - | 47.8 -> **48.5** | Class Water undertuned (WR: 46.4%, factor: 1.015) |
| `EEF` | Earth | Conditional Strike | 22.5 -> **20.3** (-9.8%) | 6.4 -> **7.5** | 166.5 -> **172.6** | Status 'Stunned' appliers undertuned (WR: 46.1%, casts: 13185); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 23.4% vs 30% floor, Casts: 1944). Increasing spread: b -8.6%, n +17.5% |
| `EEW` | Earth | Buff / Sustain | 32.7 -> **30.9** (-5.5%) | - | 32.7 -> **30.9** | Individual spell overtuned (WR: 64.5%, Casts: 1795, mult: 0.946) |
| `EED` | Earth | Direct Damage | 6.8 -> **6.9** (+1.5%) | - | 6.8 -> **6.9** | Individual spell undertuned (WR: 44.7%, Casts: 1239, mult: 1.018) |
| `LLF` | Light | Conditional Strike | 3.1 -> **3.5** (+12.9%) | 19.1 -> **25.4** | 62.3 -> **92.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.0% vs 30% floor, Casts: 3093). Increasing spread: b -16.0%, n +32.9%; Buffed setup spell [LLF] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLE` | Light | Setup - Weather | 35.2 -> **44.7** (+27.0%) | - | 35.2 -> **44.7** | Weather 'Sunny' appliers undertuned (WR: 35.9%, casts: 2734); Buffed setup spell [LLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [LLD] |
| `LLL` | Light | Buff / Sustain | 27.5 -> **26.6** (-3.3%) | - | 27.5 -> **26.6** | Individual spell overtuned (WR: 59.2%, Casts: 1701, mult: 0.967) |
| `LLD` | Light | Ultimate | 31.9 -> **31.9** (+0.0%) | 11.1 -> **14.0** | 386.0 -> **478.5** | Weather 'Sunny' beneficiaries overtuned (WR: 56.5%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.1% vs 16% floor, Casts: 1574). Shifted tuner focus: protected ultimate base floor at 31.9 (hard-coded floor >= 20.0) and buffed appliers/setups (LLE, LLF) with +15% b tempo. |
| `DDF` | Dark | Conditional Strike | 5.3 -> **4.5** (-15.1%) | 26.4 -> **36.2** | 145.2 -> **167.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2113). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 42.6%, Casts: 2113, mult: 1.026) |
| `DDE` | Dark | Setup - Weather | 40.3 -> **44.9** (+11.4%) | - | 40.3 -> **44.9** | Weather 'Darkness' appliers overtuned on own (WR: 54.7%); Buffed setup spell [DDE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `DDL` | Dark | Debuff / Control | 27.8 -> **27.5** (-1.1%) | - | 27.8 -> **27.5** | Individual spell overtuned (WR: 53.6%, Casts: 2137, mult: 0.989) |
| `DDD` | Dark | Debuff / Control | 28.7 -> **27.9** (-2.8%) | - | 28.7 -> **27.9** | Individual spell overtuned (WR: 57.8%, Casts: 1820, mult: 0.973) |
| `FWF` | Ghostfire | Debuff / Control | 38.4 -> **36.3** (-5.5%) | - | 38.4 -> **36.3** | Status 'Burning' appliers overtuned on own (WR: 56.0%); Individual spell overtuned (WR: 59.5%, Casts: 1498, mult: 0.966) |
| `FWW` | Ghostfire | Debuff / Control | 29.1 -> **29.4** (+1.0%) | - | 29.1 -> **29.4** | Individual spell undertuned (WR: 46.5%, Casts: 2511, mult: 1.011) |
| `FWE` | Ghostfire | Setup - Location | 57.6 -> **60.5** (+5.0%) | - | 57.6 -> **60.5** | Location 'Graveyard' appliers undertuned (WR: 42.8%, casts: 2767); Individual spell undertuned (WR: 42.8%, Casts: 2767, mult: 1.025) |
| `FWD` | Ghostfire | Ultimate | 30.9 -> **34.9** (+12.9%) | 18.9 -> **19.2** | 614.9 -> **705.0** | Status 'Cursed' beneficiaries undertuned (WR: 42.8%); Location 'Graveyard' beneficiaries undertuned (WR: 37.2%) |
| `WFF` | Ghostfire | Conditional Strike | 7.4 -> **6.4** (-13.5%) | 18.3 -> **23.2** | 142.8 -> **154.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 12.6% vs 30% floor, Casts: 2221). Increasing spread: b -13.0%, n +26.5% |
| `WFW` | Ghostfire | Debuff / Control | 29.7 -> **29.0** (-2.4%) | - | 29.7 -> **29.0** | Individual spell overtuned (WR: 56.6%, Casts: 2487, mult: 0.977) |
| `WFE` | Ghostfire | Debuff / Control | 33.4 -> **33.6** (+0.6%) | - | 33.4 -> **33.6** | Status 'Bleeding' appliers overtuned on own (WR: 65.7%); Buffed setup spell [WFE] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `WFL` | Ghostfire | Buff / Sustain | 36.0 -> **38.0** (+5.6%) | - | 36.0 -> **38.0** | Individual spell undertuned (WR: 35.4%, Casts: 1164, mult: 1.054) |
| `WFD` | Ghostfire | Conditional Strike | 9.0 -> **7.7** (-14.4%) | 16.4 -> **21.4** | 156.6 -> **172.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 2179). Increasing spread: b -14.7%, n +30.2% |
| `FEF` | Beasts | Debuff / Control | 29.7 -> **30.1** (+1.3%) | - | 29.7 -> **30.1** | Individual spell undertuned (WR: 45.8%, Casts: 1581, mult: 1.014) |
| `FEW` | Beasts | Conditional Strike | 5.6 -> **4.6** (-17.9%) | 25.3 -> **34.6** | 147.3 -> **163.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.1% vs 30% floor, Casts: 1429). Increasing spread: b -17.9%, n +36.9% |
| `FEE` | Beasts | Buff / Sustain | 26.3 -> **26.6** (+1.1%) | - | 26.3 -> **26.6** | Individual spell undertuned (WR: 46.4%, Casts: 1729, mult: 1.012) |
| `FEL` | Beasts | Buff / Sustain | 27.6 -> **28.2** (+2.2%) | - | 27.6 -> **28.2** | Individual spell undertuned (WR: 43.2%, Casts: 1260, mult: 1.024) |
| `FED` | Beasts | Conditional Strike | 8.8 -> **9.1** (+3.4%) | 1.5 -> **1.5** | 22.0 -> **22.8** | Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 51.0% within [30%-55%] target window, WR: 40.8%).; Individual spell undertuned (WR: 40.8%, Casts: 2009, mult: 1.033) |
| `EFF` | Beasts | Debuff / Control | 7.0 -> **5.8** (-17.1%) | 24.9 -> **33.7** | 181.3 -> **201.3** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 1.9% vs 30% floor, Casts: 2764). Increasing spread: b -17.2%, n +35.4% |
| `EFE` | Beasts | Buff / Sustain | 32.8 -> **33.2** (+1.2%) | - | 32.8 -> **33.2** | Individual spell undertuned (WR: 46.2%, Casts: 2677, mult: 1.013) |
| `EFL` | Beasts | Buff / Sustain | 12.0 -> **10.2** (-15.0%) | - | 12.0 -> **10.2** | Individual spell overtuned (WR: 86.3%, Casts: 2006, mult: 0.852) |
| `EFD` | Beasts | Ultimate | 29.8 -> **29.4** (-1.3%) | 17.2 -> **21.9** | 542.4 -> **673.3** | Location 'Jungle' beneficiaries overtuned (WR: 54.3%); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.5% vs 16% floor, Casts: 1267). Shifted tuner focus: protected ultimate base floor at 29.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WEL, WEE) with +15% b tempo. |
| `FLF` | Lightning | Conditional Strike | 5.9 -> **4.9** (-16.9%) | 30.3 -> **42.5** | 184.7 -> **213.2** | Status 'Stunned' beneficiaries undertuned (WR: 43.4%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.5% vs 30% floor, Casts: 1867). Increasing spread: b -17.8%, n +36.5% |
| `FLW` | Lightning | Debuff / Control | 53.5 -> **53.3** (-0.4%) | - | 53.5 -> **53.3** | Status 'Stunned' appliers undertuned (WR: 46.1%, casts: 13185); Individual spell overtuned (WR: 55.2%, Casts: 1364, mult: 0.983) |
| `FLE` | Lightning | Setup - Weather | 29.9 -> **29.0** (-3.0%) | - | 29.9 -> **29.0** | Weather 'Storming' appliers overtuned on own (WR: 54.4%); Individual spell overtuned (WR: 54.4%, Casts: 1601, mult: 0.986) |
| `FLD` | Lightning | Ultimate | 45.3 -> **50.4** (+11.3%) | 9.2 -> **9.2** | 462.1 -> **514.1** | Status 'Stunned' beneficiaries undertuned (WR: 43.4%); Weather 'Storming' beneficiaries undertuned (WR: 41.6%) |
| `LFF` | Lightning | Conditional Strike | 6.2 -> **5.3** (-14.5%) | 23.3 -> **31.4** | 150.7 -> **171.7** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 2.7% vs 30% floor, Casts: 2110). Increasing spread: b -16.9%, n +34.8%; Individual spell undertuned (WR: 42.8%, Casts: 2110, mult: 1.025) |
| `LFW` | Lightning | Buff / Sustain | 33.2 -> **32.3** (-2.7%) | - | 33.2 -> **32.3** | Individual spell overtuned (WR: 57.7%, Casts: 2058, mult: 0.973) |
| `LFE` | Lightning | Debuff / Control | 46.1 -> **47.3** (+2.6%) | - | 46.1 -> **47.3** | Status 'Stunned' appliers undertuned (WR: 46.1%, casts: 13185); Individual spell undertuned (WR: 46.0%, Casts: 2325, mult: 1.013) |
| `LFL` | Lightning | Debuff / Control | 35.0 -> **29.7** (-15.1%) | 14.8 -> **19.0** | 553.0 -> **594.0** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.3% vs 30% floor, Casts: 2447). Increasing spread: b -13.9%, n +28.4%; Individual spell overtuned (WR: 54.8%, Casts: 2447, mult: 0.984) |
| `LFD` | Lightning | Conditional Strike | 9.2 -> **8.1** (-12.0%) | 26.3 -> **34.5** | 251.2 -> **287.6** | Status 'Stunned' appliers undertuned (WR: 46.1%, casts: 13185); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.0% vs 30% floor, Casts: 1933). Increasing spread: b -15.2%, n +31.2% |
| `FDF` | Blood | Conditional Strike | 5.6 -> **4.7** (-16.1%) | 26.4 -> **36.2** | 153.4 -> **174.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 2360). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 43.0%, Casts: 2360, mult: 1.024) |
| `FDW` | Blood | Direct Damage | 60.1 -> **63.3** (+5.3%) | - | 60.1 -> **63.3** | Individual spell undertuned (WR: 35.7%, Casts: 1661, mult: 1.053) |
| `FDE` | Blood | Setup - Weather | 20.4 -> **20.6** (+1.0%) | - | 20.4 -> **20.6** | Individual spell undertuned (WR: 46.4%, Casts: 1769, mult: 1.012) |
| `FDD` | Blood | Ultimate | 34.8 -> **38.3** (+10.1%) | 9.0 -> **8.5** | 348.0 -> **363.8** | Multi-condition setup trap (N=2 conditions, Trigger Rate: 2.1% vs 16% floor, Casts: 1394, WR: 44.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 44.7%, Casts: 1394, mult: 1.018) |
| `DFF` | Blood | Conditional Strike | 7.0 -> **5.9** (-15.7%) | 17.4 -> **22.8** | 128.8 -> **140.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 7.5% vs 30% floor, Casts: 1341). Increasing spread: b -15.0%, n +30.8% |
| `DFW` | Blood | Debuff / Control | 24.4 -> **24.1** (-1.2%) | - | 24.4 -> **24.1** | Status 'Bleeding' appliers overtuned on own (WR: 65.7%); Buffed setup spell [DFW] (+15.0% b tempo) to facilitate under-triggered Ultimate [EDD] |
| `DFE` | Blood | Buff / Sustain | 35.0 -> **36.5** (+4.3%) | - | 35.0 -> **36.5** | Individual spell undertuned (WR: 38.0%, Casts: 2327, mult: 1.044) |
| `DFD` | Blood | Conditional Strike | 65.8 -> **75.1** (+14.1%) | 0.3 -> **0.2** | 85.5 -> **90.1** | Condition triggers excessively (N=1 conditions, Trigger Rate: 96.4% vs 55% ceiling, WR: 57.8%). Compressing spread: b +17.3%, n -25.9%; Individual spell overtuned (WR: 57.8%, Casts: 2139, mult: 0.973) |
| `WEF` | Plants | Conditional Strike | 8.6 -> **7.6** (-11.6%) | 14.6 -> **17.5** | 134.2 -> **140.6** | Location 'Jungle' beneficiaries overtuned (WR: 54.3%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 17.9% vs 30% floor, Casts: 921). Increasing spread: b -10.8%, n +22.1% |
| `WEW` | Plants | Debuff / Control | 74.7 -> **85.9** (+15.0%) | - | 74.7 -> **85.9** | Buffed setup spell [WEW] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WEE` | Plants | Setup - Location | 22.2 -> **23.2** (+4.5%) | - | 22.2 -> **23.2** | Location 'Jungle' appliers undertuned (WR: 43.6%, casts: 2325); Individual spell undertuned (WR: 43.6%, Casts: 2325, mult: 1.022) |
| `WED` | Plants | Conditional Strike | 10.1 -> **11.4** (+12.9%) | 16.0 -> **15.0** | 171.7 -> **182.4** | Multi-condition setup trap (N=3 conditions, Trigger Rate: 0.5% vs 8% floor, Casts: 2058, WR: 38.7%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 38.7%, Casts: 2058, mult: 1.041) |
| `EWF` | Plants | Buff / Sustain | 9.4 -> **7.9** (-16.0%) | 13.0 -> **15.9** | 131.6 -> **133.5** | Weather 'Sunny' beneficiaries overtuned (WR: 56.5%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 13.4% vs 30% floor, Casts: 3324). Increasing spread: b -12.7%, n +25.9% |
| `EWW` | Plants | Debuff / Control | 15.4 -> **13.3** (-13.6%) | - | 15.4 -> **13.3** | Individual spell overtuned (WR: 83.5%, Casts: 1921, mult: 0.865) |
| `EWL` | Plants | Debuff / Control | 60.4 -> **62.0** (+2.6%) | - | 60.4 -> **62.0** | Individual spell undertuned (WR: 42.5%, Casts: 3033, mult: 1.026) |
| `EWD` | Plants | Conditional Strike | 11.0 -> **12.1** (+10.0%) | 24.1 -> **32.0** | 276.1 -> **399.3** | Status 'Bleeding' appliers overtuned on own (WR: 65.7%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.3% vs 30% floor, Casts: 2022). Increasing spread: b -15.9%, n +32.6% |
| `WLF` | Fey | Conditional Strike | 7.5 -> **6.4** (-14.7%) | 21.5 -> **28.7** | 168.8 -> **190.1** | Status 'Cursed' beneficiaries undertuned (WR: 42.8%); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.5% vs 30% floor, Casts: 1653). Increasing spread: b -14.6%, n +29.9% |
| `WLW` | Fey | Debuff / Control | 47.8 -> **49.0** (+2.5%) | - | 47.8 -> **49.0** | Individual spell undertuned (WR: 42.6%, Casts: 1423, mult: 1.025) |
| `WLE` | Fey | Setup - Location | 50.6 -> **60.9** (+20.4%) | - | 50.6 -> **60.9** | Location 'Enchanted Forest' appliers undertuned (WR: 43.3%, casts: 2473); Buffed setup spell [WLE] (+15.0% b tempo) to facilitate under-triggered Ultimate [WLD] |
| `WLL` | Fey | Direct Damage | 61.5 -> **59.9** (-2.6%) | - | 61.5 -> **59.9** | Individual spell overtuned (WR: 57.5%, Casts: 1433, mult: 0.974) |
| `WLD` | Fey | Ultimate | 27.8 -> **27.4** (-1.4%) | 24.7 -> **32.1** | 714.5 -> **906.9** | Ultimate payoff under-triggered (N=3 conditions, Trigger Rate: 0.0% vs 8% floor, Casts: 1120). Shifted tuner focus: protected ultimate base floor at 27.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WEW, LWW, DDE, WLE) with +15% b tempo.; Individual spell overtuned (WR: 54.2%, Casts: 1120, mult: 0.986) |
| `LWF` | Fey | Debuff / Control | 21.3 -> **19.1** (-10.3%) | 11.7 -> **14.5** | 270.5 -> **296.1** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 15.5% vs 30% floor, Casts: 3474). Increasing spread: b -11.8%, n +24.1%; Individual spell undertuned (WR: 45.4%, Casts: 3474, mult: 1.015) |
| `LWW` | Fey | Debuff / Control | 40.9 -> **41.9** (+2.4%) | - | 40.9 -> **41.9** | Individual spell undertuned (WR: 42.8%, Casts: 2036, mult: 1.025) |
| `LWD` | Fey | Conditional Strike | 6.2 -> **5.2** (-16.1%) | 26.4 -> **36.2** | 169.9 -> **193.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 0.0% vs 30% floor, Casts: 1699). Increasing spread: b -18.0%, n +37.0%; Individual spell undertuned (WR: 44.9%, Casts: 1699, mult: 1.017) |
| `WDF` | Ice | Conditional Strike | 8.0 -> **7.2** (-10.0%) | 24.4 -> **34.1** | 203.2 -> **252.7** | Status 'Stunned' appliers undertuned (WR: 46.1%, casts: 13185); Weather 'Raining' beneficiaries undertuned (WR: 37.8%) |
| `WDE` | Ice | Setup - Weather | 23.6 -> **24.3** (+3.0%) | - | 23.6 -> **24.3** | Individual spell undertuned (WR: 41.9%, Casts: 1157, mult: 1.028) |
| `WDD` | Ice | Ultimate | 28.4 -> **28.4** (+0.0%) | 19.9 -> **25.4** | 593.6 -> **749.8** | Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 1.8% vs 16% floor, Casts: 2063). Shifted tuner focus: protected ultimate base floor at 28.4 (hard-coded floor >= 20.0) and buffed appliers/setups (ELD, DWE) with +15% b tempo. |
| `DWF` | Ice | Debuff / Control | 46.3 -> **45.6** (-1.5%) | - | 46.3 -> **45.6** | Individual spell overtuned (WR: 54.4%, Casts: 1494, mult: 0.986) |
| `DWE` | Ice | Setup - Location | 26.3 -> **27.1** (+3.0%) | - | 26.3 -> **27.1** | Location 'Tundra' appliers undertuned (WR: 45.8%, casts: 2414); Individual spell undertuned (WR: 45.8%, Casts: 2414, mult: 1.014) |
| `DWL` | Ice | Debuff / Control | 46.0 -> **45.0** (-2.2%) | - | 46.0 -> **45.0** | Individual spell overtuned (WR: 56.2%, Casts: 2019, mult: 0.979) |
| `DWD` | Ice | Conditional Strike | 13.6 -> **12.4** (-8.8%) | 8.9 -> **10.5** | 134.6 -> **142.6** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 22.2% vs 30% floor, Casts: 1930). Increasing spread: b -9.1%, n +18.5% |
| `ELF` | Wind | Conditional Strike | 15.8 -> **13.5** (-14.6%) | 18.2 -> **23.7** | 303.4 -> **333.4** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.2% vs 30% floor, Casts: 1722). Increasing spread: b -14.7%, n +30.2% |
| `ELW` | Wind | Debuff / Control | 43.4 -> **44.8** (+3.2%) | - | 43.4 -> **44.8** | Individual spell undertuned (WR: 41.1%, Casts: 1955, mult: 1.032) |
| `ELE` | Wind | Setup - Weather | 20.8 -> **21.1** (+1.4%) | - | 20.8 -> **21.1** | Individual spell undertuned (WR: 45.9%, Casts: 1497, mult: 1.013) |
| `ELD` | Wind | Conditional Strike | 9.9 -> **8.9** (-10.1%) | 21.4 -> **29.8** | 221.8 -> **274.1** | Weather 'Raining' beneficiaries undertuned (WR: 37.8%); Weather 'Blizzard' appliers undertuned (WR: 40.8%, casts: 2599) |
| `LEF` | Wind | Conditional Strike | 6.7 -> **5.5** (-17.9%) | 20.4 -> **26.8** | 143.4 -> **152.9** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.5% vs 30% floor, Casts: 1775). Increasing spread: b -15.4%, n +31.6%; Individual spell overtuned (WR: 58.2%, Casts: 1775, mult: 0.971) |
| `EDF` | Poison | Conditional Strike | 6.2 -> **5.2** (-16.1%) | 20.1 -> **26.6** | 130.8 -> **143.5** | Class Poison overtuned (WR: 56.3%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 5.9% vs 30% floor, Casts: 1430). Increasing spread: b -15.7%, n +32.1% |
| `EDW` | Poison | Debuff / Control | 24.7 -> **22.1** (-10.5%) | - | 24.7 -> **22.1** | Class Poison overtuned (WR: 56.3%, factor: 0.975); Individual spell overtuned (WR: 71.5%, Casts: 2379, mult: 0.917) |
| `EDE` | Poison | Setup - Location | 30.0 -> **35.5** (+18.3%) | - | 30.0 -> **35.5** | Class Poison overtuned (WR: 56.3%, factor: 0.975); Location 'Swamp' appliers undertuned (WR: 42.1%, casts: 1592) |
| `EDL` | Poison | Debuff / Control | 6.8 -> **5.6** (-17.6%) | - | 6.8 -> **5.6** | Class Poison overtuned (WR: 56.3%, factor: 0.975); Individual spell overtuned (WR: 86.4%, Casts: 2797, mult: 0.852) |
| `EDD` | Poison | Ultimate | 28.8 -> **28.1** (-2.4%) | 13.0 -> **16.8** | 403.2 -> **500.2** | Class Poison overtuned (WR: 56.3%, factor: 0.975); Ultimate payoff under-triggered (N=2 conditions, Trigger Rate: 0.4% vs 16% floor, Casts: 2353). Shifted tuner focus: protected ultimate base floor at 28.8 (hard-coded floor >= 20.0) and buffed appliers/setups (WFE, FDL, DFW, EWD, EDE) with +15% b tempo. |
| `DEF` | Poison | Conditional Strike | 33.5 -> **32.7** (-2.4%) | 1.7 -> **1.7** | 90.5 -> **88.3** | Class Poison overtuned (WR: 56.3%, factor: 0.975); Conditional payoff in equilibrium (N=1 conditions, Trigger Rate: 52.3% within [30%-55%] target window, WR: 46.8%). |
| `DEW` | Poison | Debuff / Control | 23.7 -> **22.0** (-7.2%) | - | 23.7 -> **22.0** | Class Poison overtuned (WR: 56.3%, factor: 0.975); Individual spell overtuned (WR: 63.0%, Casts: 2772, mult: 0.952) |
| `DEE` | Poison | Debuff / Control | 23.8 -> **23.2** (-2.5%) | - | 23.8 -> **23.2** | Class Poison overtuned (WR: 56.3%, factor: 0.975) |
| `DEL` | Poison | Conditional Strike | 0.7 -> **0.6** (-14.3%) | 17.9 -> **23.2** | 13.2 -> **14.5** | Class Poison overtuned (WR: 56.3%, factor: 0.975); Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 8.7% vs 30% floor, Casts: 1838). Increasing spread: b -14.5%, n +29.7% |
| `DED` | Poison | Debuff / Control | 25.4 -> **24.8** (-2.4%) | - | 25.4 -> **24.8** | Class Poison overtuned (WR: 56.3%, factor: 0.975) |
| `LDF` | Cosmic | Debuff / Control | 60.7 -> **58.9** (-3.0%) | - | 60.7 -> **58.9** | Individual spell overtuned (WR: 58.5%, Casts: 890, mult: 0.970) |
| `LDW` | Cosmic | Debuff / Control | 46.9 -> **48.1** (+2.6%) | - | 46.9 -> **48.1** | Status 'Stunned' appliers undertuned (WR: 46.1%, casts: 13185); Individual spell undertuned (WR: 46.3%, Casts: 2676, mult: 1.012) |
| `LDL` | Cosmic | Conditional Strike | 7.9 -> **6.6** (-16.5%) | 20.1 -> **26.7** | 166.7 -> **182.8** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 4.8% vs 30% floor, Casts: 1889). Increasing spread: b -16.1%, n +33.0% |
| `LDD` | Cosmic | Ultimate | 43.5 -> **48.1** (+10.6%) | 6.5 -> **6.1** | 326.2 -> **341.5** | Multi-condition setup trap (N=4 conditions, Trigger Rate: 0.0% vs 3% floor, Casts: 2117, WR: 43.3%). Compressing spread to rescue baseline floor: b +8.0%, n -6.0%; Individual spell undertuned (WR: 43.3%, Casts: 2117, mult: 1.023) |
| `DLF` | Cosmic | Conditional Strike | 9.1 -> **7.9** (-13.2%) | 20.1 -> **26.4** | 192.0 -> **216.5** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 6.8% vs 30% floor, Casts: 2384). Increasing spread: b -15.3%, n +31.3%; Individual spell undertuned (WR: 43.4%, Casts: 2384, mult: 1.023) |
| `DLE` | Cosmic | Direct Damage | 43.8 -> **44.8** (+2.3%) | - | 43.8 -> **44.8** | Individual spell undertuned (WR: 43.4%, Casts: 1937, mult: 1.023) |
| `DLL` | Cosmic | Conditional Strike | 18.6 -> **16.8** (-9.7%) | 11.8 -> **15.2** | 238.1 -> **272.2** | Conditional payoff under-triggered (N=1 conditions, Trigger Rate: 10.3% vs 30% floor, Casts: 1522). Increasing spread: b -13.9%, n +28.4%; Individual spell undertuned (WR: 37.2%, Casts: 1522, mult: 1.047) |
