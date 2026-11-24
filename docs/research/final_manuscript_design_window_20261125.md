# Final manuscript and MEB design-window analysis — 2026-11-25

**Status:** manuscript-stage analysis completed; numerical DOE complete; scientific conclusions conditional on the specified 3D model and engineering screening criteria. Low-temperature results are provisional. This is a new summary of the final manuscript, not a rewrite of historical evidence.

## Source and scope

- Canonical lineage: `3D-Sun-SADDLE-V1 / Flat upper S/D`, single-WF W gate (4.8 eV), 20 nm gate length.
- Original data/code snapshot: [7973adc](https://github.com/minhosong-mse/CMP/commit/7973adc0afaae4a4d48ca7c67db47fcf6dd2dca2).
- [37-depth canonical dataset](../../data/3d_meb_jedec_37depth_complete_20261123/README.md), [six-metric master](../../data/3d_meb_jedec_37depth_complete_20261123/six_metrics_148_conditions.csv), [node QC](../../data/3d_meb_jedec_37depth_complete_20261123/node_qc_740.csv).
- User-supplied final English manuscript: `BCAT_DRAM_MEB_Manuscript_Final_Submission(1).docx`, SHA-256 `c3b549f2d4443fb93c51c52c7bc33b5d48fa759405995c80584b77943ba10825`. Korean Review6 is the earlier reference; the final English manuscript governs later verified wording. Neither manuscript binary is published by this update.
- The user-supplied independent Codex audit dated 2026-11-24 reported re-extraction of 740/740 exported curves and 1,924/1,924 matching metrics/intermediate values, with direct native-file checks for 28 cases. Its requested current/KCL definitions, numerical precision and citation corrections were subsequently incorporated into the final manuscript. No separate Codex rerun on the revised final file is claimed.

## Design and analysis protocol

The initial 300 K campaign covered 25 depths (24–48 nm) and seven modes, including output curves and spatial field/BTBT analysis. The final DOE covers 37 depths (24–60 nm, 1 nm increments) × four sampled temperatures (233.15, 300, 358.15, 368.15 K) × five modes (0/1/5/6/7). All 740 planned numerical endpoints are complete; 19 initial failed nodes were recovered with numerical-only R1 settings. The final master contains 148 depth–temperature rows. The historical campaigns and final DOE are separately traceable.

Six metrics are Ion, Ioff, SS, DIBL, estimated GIDL current (signed Hurkx ON−OFF drain-current difference at VG = −0.7 V, VD = 1.2 V), and estimated storage-node discharge time. The latter integrates Ccell/Iloss over 0.8–1.0 V using 101 quasistationary IVSN samples, assumed 10 fF, and Iloss = −i(cell,sn). It is not a directly simulated or measured retention time.

| Metric | Initial screening vs 36 nm at 300 K | Same-temperature screening vs 51 nm |
|---|---:|---:|
| Ion | ≥95% | ≥95% |
| Ioff | ≤80% | ≤150% |
| SS | ≤105% | ≤105% |
| DIBL | ≤115% | ≤115% |
| Estimated GIDL | ≤50% | ≤120% |
| Estimated discharge time | ≥200% | ≥90% |

Criteria are study-defined engineering constraints, not manufacturer or JEDEC acceptance limits. Equal-weight min–max ranking of the six metrics gives 45 nm (80.82/100); the initial constraints yield 44–51 nm and maximizing the estimated discharge time within that feasible set selects 51 nm. These are different objectives. Fig. 7 normalizes each constraint boundary to 100; the same-temperature Fig. 8 clips scores to 0–100 with an acceptance boundary of 80 using S = 100 − 20 L/A, where L is nonnegative unfavorable relative degradation and A is allowable degradation. Fig. 9 passes a condition only if all six raw metrics meet their limits.

## Final reported results

At 300 K, 51 nm vs 36 nm retains 95.32% of Ion, lowers Ioff by 29.09% and estimated GIDL by 72.72%, and increases estimated discharge time from 67.16 to 188.86 ms (2.81×). For 24→48 nm at 300 K the Gate–Drain peak field changes from 1.593 to 0.865 MV/cm, charge-weighted positive BTBT generation from 68.32 to 1.31 fA, and estimated GIDL from 89.80 to 19.04 fA. Regional generation is not collected terminal current.

| Sampled temperature | Same-temperature relative window |
|---|---:|
| 233.15 K | 50–56 nm (provisional) |
| 300 K | 47–56 nm |
| 358.15 K | 46–56 nm |
| 368.15 K | 46–56 nm |
| Common, 300/358.15/368.15 K | 47–56 nm |
| Common, all four | 50–56 nm (provisional) |

The additional intersection with initial 300 K constraints is 47–51 nm for the three non-cold sampled temperatures, and 50–51 nm (provisional) for all four. These results were recalculated from the 148-row master during this synchronization; raw data and simulation code were not modified.

## Boundaries and follow-up

- 25 cold (233.15 K) rows have maximum relative IVSN KCL residual above 1%, with maximum 15.57% at 57 nm (51 nm: 10.31%). The relative residual is |i(cell,sn)+i(vsn,sn)| / |i(cell,sn)|, evaluated across the 101 points. No quantitative error bound on discharge time is established.
- The same-temperature design range is relative, not an absolute retention/refresh specification or a continuous-temperature guarantee. The 51 nm discharge estimate decreases to 6.17 ms at 358.15 K and 3.61 ms at 368.15 K.
- SRH and incomplete ionization are omitted. Mesh convergence/equivalence, quantitative paper calibration, actual process tolerance, direct transient retention/read failure and JEDEC product compliance remain unestablished.
- Prior 2D/3D exploratory lineages, original native archives, R1 provenance and all historical research records remain intact. No new simulation or physical calibration was performed for this synchronization.
