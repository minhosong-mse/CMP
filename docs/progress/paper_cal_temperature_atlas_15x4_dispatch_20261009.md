# B0-2D-PAPER-CAL: 15-MEB × temperature Atlas dispatch checkpoint

> Session close-out date: 2026-10-09 (Asia/Seoul)
> Current state: PAUSED AFTER USER-REPORTED SWB EXECUTION / EVIDENCE RETURN AND QC PENDING.
> Scope: post-freeze MEB Atlas Level2, NOT FZ-C-equivalent numerical mesh, NOT legacy NonlocalPath.
> Do not treat user-reported run completion as data validation.

## 1. Experiment and lineage

The frozen C7_4 / B_QF_HALF physics coordinates stay unchanged: GateCouplingScale=2.300, GateDepthBoost=0.025 um, Qf_Int=2.55e12 cm^-2 (in SDevice), tungsten WF=4.8 eV, nominal 36 nm, single-WF Hurkx on/off diagnostic. Atlas SDE uses MeshLevel=2.

The 300 K 15-MEB dataset is already complete and independently QC-validated with 1,036 checks. It is the reference plane and must be reused, not rerun by default.

The user extended the original nominal-36-nm temperature package to ALL 15 Atlas MEB depths:
31, 33, 36, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51 nm.
New fixed lattice temperatures: 233 K, 340 K, 380 K; existing 300 K is retained. Target assembled matrix: 15 depths × 4 temperatures = 60 MEB-temperature rows.

SWB user parameters: MEBDepth in um (0.031, 0.033, 0.036, 0.039, 0.041, 0.042, 0.043, 0.044, 0.045, 0.046, 0.047, 0.048, 0.049, 0.050, 0.051); Temp_K in K (233, 340, 380). Parameter placement: MEBDepth upstream in SDE, Temp_K in SDevice; verify actual preprocessing/ancestry in recovered SWB files. Temperature is a prescribed isothermal lattice condition, not a thermal transport simulation.

## 2. Six SVisual outputs and five distinct SDevice calculations

| SDevice branch | Conditions | SVisual branch outputs |
|---|---|---|
| DC005 | Vd=0.05 V, Id-Vg | DC005 |
| DC12 | Vd=1.20 V, Id-Vg | DC12 |
| CGD | Vd=1.2 V, Vg=-0.7 V, 1 MHz, BTBT OFF | CGD |
| GIDL_ON | Vd=1.2 V, Vg=0→-0.7 V, Hurkx ON | GIDL_ON terminal; GIDL_ON spatial (two sibling descendants) |
| GIDL_OFF | Same GIDL bias, Band2Band OFF | GIDL_OFF terminal |

USER-REPORTED: 45 MEB-temperature combinations dispatched/completed across all six SVisual branches. Expected new execution footprint if successfully finished: 45 × 5 = 225 SDevice nodes and 45 × 6 = 270 SVisual extraction nodes. The conversation has not yet received the resulting CSVs, logs, preprocessed decks, or an independent SWB completion inventory. THESE COUNTS ARE EXPECTATIONS, NOT VERIFIED PASS COUNTS.

## 3. Prepared local artifacts and provenance

- CMP_36NM_TEMPERATURE_FULL_CMD_READY_20261008.zip, SHA256 6d53718390b1be33697e103c95ceac616141420eefc7e0091fa7657909684d34. Contains unchanged Atlas SDE, five SDevice temperature-parametric derivatives, six historical validated SVisual extraction files, 36-nm manifest/reference and 300 K regression tools. Original packaging was scoped to 36 nm; user expanded parameter sweeps in SWB.
- CMP_collect_TDEP_45_all_branches.py, SHA256 0e0120aa9e9e0987ccee65f8a0b1f641596b5e9807eba0b80a4baa17494dc5d6. Read-only Python standard-library collector from specified SWB project folders. Copies textual CMD/CSV/log/metadata into an indexed ZIP; excludes TDR/PLT due to size.
- These package SHA256 records identify user-facing local artifacts. Their bytes have NOT been deposited into this GitHub commit; retain original copies on the TCAD server/conversation until committed as provenance-backed code or archived separately. Existing GitHub Atlas SDE is code/sde/paper_cal/atlas_300k/CMP_B0_2D_PAPER_CAL_MEB_ATLAS_SDE.cmd.
- Offline test: temperature package ZIP CRC check PASSED and collector py_compile PASSED. This verifies local artifact format, not current 45-condition SWB execution or scientific results.

## 4. Next session — FIRST ACTION (no new TCAD calculations)

1. Identify the exact SWB project folder(s) and collect existing evidence using:
   python3 CMP_collect_TDEP_45_all_branches.py --out /user/semi/semi333/CMP_TDEP_45_EVIDENCE.zip /user/semi/semi333/ACTUAL_PROJECT_DIRECTORY
   If branches occupy multiple projects, append EACH exact directory. Never point it at the entire home directory.
2. Upload the resulting CMP_TDEP_45_EVIDENCE.zip. Preserve original SWB project and raw TDR/PLT on server; do not overwrite/scrub source results.
3. Independently verify 45 (MEB,T) keys, all five SDevice/6 SVisual branches, each actual execution-complete log, the SDE MEB substitution and all five preprocessed SDevice Temp_K substitutions, solver endpoints, sweep biases and curve availability. Mapping by filename alone is not sufficient.
4. Assemble 45 new rows using existing validated 300 K extraction definitions; join the 15 existing 300 K rows to get a 60-row temperature–MEB master ONLY if keys/branch outputs validate. Missing/failed rows must be explicitly marked.
5. Run analytical QC: signed current and KCL, Hurkx ON−OFF versus q∫BTBT (diagnostic and sign-aware), AC reciprocity, DC Vth/SS/DIBL/Ion/Ioff and Ion/Ioff, spatial BTBT hotspot/E-field/whole-Si integral/20% active area/fixed Y-cut. Do not claim ON−OFF always equals BTBT in every temperature without checking.
6. Plot 36-nm vs temperature first, then 15 MEB vs temperature comparisons, anomaly review and candidate guardrails. Only then discuss targeted reruns or selected-point mesh checks, not blanket FZ-C bridge or recalibration.
7. When real results are audited, deposit provenance-backed CSV/QC/figures, and update HANDOFF; do not label 1T1C retention improvement before new PAPER-CAL mixed-mode validation.

## 5. Scientific claim limits and frozen items

This step does not establish physical retention/refresh, absolute FZ-C numerical equivalence, a global optimum, or a robust process range. GIDL-condition total terminal current is not BTBT-only current. Common fixed Y-cut can miss shallow MEB hotspots; whole-Silicon BTBT is prioritized. Keep original FZ-A/B/C records and 300 K master unchanged. Do not modify calibration knobs or retune to match historical absolute leakage.

Related: docs/evidence/paper_cal_g0_parent_spatial_bridge_20261008.md; docs/research/MEB_2D_TO_1T1C_VALIDATION_ROADMAP_PROVISIONAL.md.

## 2026-10-09 36nm evidence-based update (supersedes earlier execution-only status for completed branches)

- Actual GIDL ON terminal, OFF terminal and ON spatial CSVs are independently QC-reviewed for **45/45 new-temperature MEB cases each**. AC Cgd extracts for **44/45** cases, missing 41nm/340K as a SDevice numerical-failure result. These facts supersede the earlier 'only user-reported' statement for those branches; see standalone 2026-10-09 GIDL/Cgd analysis artifact. Five shallow/high-temperature ON−OFF-vs-qG relative discrepancies remain QC flags.
- Actual **36nm new-temperature DC005/DC12** original summaries+curves (233/340/380 K, 6+6 CSVs) were subsequently ingested and curve-recomputed; all six PASS. Combined 233/300/340/380 K complete 36nm baseline is committed under `data/paper_cal/atlas_temperature_20261009/` with report `docs/progress/paper_cal_36nm_temperature_dc_qc_20261009.md`.
- All 60 MEB×T slots retain GIDL/Cgd/spatial where measured, but **42 non-36nm new-temperature DC rows are still unverified/unfilled here**. Full 60-row partial CSV and large curve/plot evidence are preserved in local download bundle, not claimed committed to Git.
- **Next immediate action:** collect other-depth DC005/DC12 completed original CSV/curves and pp CMD/log evidence in batches, then incrementally QC; do not globally retune or rerun due to one missing Cgd point.
