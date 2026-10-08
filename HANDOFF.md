# CMP Research Handoff

> Canonical session handoff. Read after `AGENTS.md`. Current research authority: live GitHub main + linked underlying evidence.

**Last updated:** 2026-10-09  
**Session state:** **300 K Atlas QC-VALIDATED; G0 executed-parent recovered / cross-mesh equivalence NOT DEMONSTRATED; 15-MEB × 3-new-temperature user-reported SWB runs / EVIDENCE RETURN PENDING**.

## 1. Current research objective and lineage

**20 nm급 BCAT DRAM에서 MEB 깊이에 따른 GIDL–Retention 전달 특성 및 온도 의존적 유효 설계 범위 도출**

Current causal-evidence sequence to test (not assume):

```text
MEB depth → project-internal Cgd / electrostatic redistribution
→ drain-side E + spatial BTBT → total drain leakage at GIDL bias
→ ON/OFF Hurkx sensitivity → temperature
→ PAPER-CAL 1T1C Write/Hold/Read → retention translation
→ effective MEB range
```

- **Physical baseline still frozen:** `B0-2D-PAPER-CAL = C7_4 / B_QF_HALF`.
- Frozen calibration inputs: `GateCouplingScale=2.300`, `GateDepthBoost=25 nm`, `Qf_Int=2.55e12 cm^-2`, `WF=4.8 eV`, nominal 36 nm, reference 300 K.
- **New numerical branch:** post-freeze 2D MEB atlas, **MeshLevel 2 working production**; MeshLevel 3 convergence reference. No physics retuning.
- **2026-10-08 G0 update:** exact FZ-C SWB parent CMD, logs/CSV and original n14 TDR were recovered; nominal 36-nm static physical/solver association and TDR spatial comparisons were completed. FZ-C↔Atlas numerical interchangeability was NOT demonstrated (+86.86% Atlas total drain current, -64.64% Atlas integrated BTBT). User explicitly chose to continue the post-freeze Atlas L2 as a **separately labeled within-branch research model**, without FZ-C equality/recalibration claims. Read docs/evidence/paper_cal_g0_parent_spatial_bridge_20261008.md.
- Do not mix this branch's absolute currents with `B0-2D-Legacy / NonlocalPath`, old FZ-C, or `3D-Sun-B0` without an explicit bridge.

## 2. Current completed work (2026-10-08)

Full **15-point 300 K MEB Atlas** completed from user's TCAD runs:

```text
MEB = 31 / 33 / 36 / 39 /
      41 / 42 / 43 / 44 / 45 /
      46 / 47 / 48 / 49 / 50 / 51 nm
```

- DC @ `Vd=0.05`, DC @ `Vd=1.20`, Cgd AC @ `Vd=1.2,Vg=-0.7,1 MHz, BTBT OFF`, GIDL-ON @ `Vd=1.2,Vg=-0.7,Hurkx`.
- P2 spatial post-processing completed: `BTBTmax`, `E@BTBT`, hotspot, `∫BTBT`, 20%-active Si area, common fixed-cut `Y=0.252174 um` E/BTBT profiles and 20% width.
- Additional diagnostic: BTBT-OFF controlled 15 points, plus signed terminal ON/OFF re-extractions and KCL checks.
- `DC005` SVisual extractor originally misconfigured; corrected and confirmed `BiasReached=1, Vd=0.05`.
- `Cgd` SVisual path corrected for actual `Cgd_AC_n*_ac_des.plt` output.
- P2 SVisual cutline/Tcl bugs corrected in v3 and 15-point results returned.

**Raw data ingestion/independent audit:**

- 201 archived entries: **90 summary CSV + 105 curve CSV + collector QC/manifest/metadata**.
- **1,036 independent checks passed** for coverage, checksum, endpoint, bias, KCL, AC reciprocity, ON/OFF versus spatial integral, and computed master consistency.
- Public GitHub archive has only TCAD absolute-path metadata sanitized; all 195 numerical CSV byte sequences preserved.
- GitHub evidence commit: `b40c63299917419e789ac41f2f87c637ff3ebcdb` (2026-10-08).

Evidence paths:

- `data/paper_cal/atlas_300k_20261008/CMP_MEB_ATLAS_300K_EVIDENCE_PUBLIC.zip`
- `data/paper_cal/atlas_300k_20261008/processed/MEB_300K_ATLAS_MASTER_VALIDATED.csv`
- `data/paper_cal/atlas_300k_20261008/qc/`
- `docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md`
- `assets/images/paper_cal/atlas_300k/01..10.svg`
- `code/scripts/analysis/validate_paper_cal_meb_atlas_300k.py`

## 3. Results established *within this numerical branch*

At 300 K and GIDL bias `Vd=1.2,Vg=-0.7`:

- Terminal **total drain leakage**, not pure BTBT current, decreases monotonically from 31→51 nm by **1,135.0×** (36→51 by **19.5×**).
- Project-internal `|c(g,d)|` decreases **35.91%** (31→51); it is **not** calibrated production overlap `Cov` nor a proof of direct `Cgd→local-E→GIDL` causality.
- DC: `Id@Vg1.2,Vd1.2` decreases **1.30%** and `Id@Vg2,Vd1.2` decreases **6.46%** (31→51); DIBL increases **0.459 mV/V**, `SSquick@Vd1.2` increases **0.069 mV/dec**.
- BTBT integral and `E@BTBT` peak at **39 nm**, `BTBTmax` at **41 nm**, while total drain leakage continues decreasing.
- Signed `Id(ON)-Id(OFF)` matches `q∫G_BTBT,dA` within **0.62% max** (31 nm; near-cancellation) and within approximately **0.01%** for 36–51 nm.
- Hurkx-sensitive percentage: **31 nm 0.105%; 36 nm 16.94%; 39 nm 74.10%; 41 nm 91.19%; 48 nm 99.57%; 51 nm 99.81%**. It is a controlled ON/OFF sensitivity, not a separately proven microscopic contribution under arbitrary conditions.
- Shallow total leakage is predominantly **BTBT-OFF residual drain–substrate current**; residual microscopic mechanism remains **unresolved**. Do not call all GIDL-condition terminal current BTBT current.
- Common fixed cut under-samples shallow hotspots (31/33/36 nm); use whole-Si BTBT area/integral for comparisons across the full 15 points.
- `GateTop≈Jdepth=48 nm` is a **model structural boundary**; there is no sharp electrical plateau/knee at 48 from this atlas. The 51-nm endpoint is **not** a final optimum.
- No independently validated current-branch temperature dataset or PAPER-CAL 1T1C retention validation yet. New-temperature SWB runs are **user-reported**, not QC verified.

## 4. Active stage and NEXT FIRST ACTION — 2026-10-09

**Stage:** 15-MEB × 3-new-temperature Atlas SWB execution is **USER-REPORTED**, not yet evidence-validated. Source CMD preparation and offline preflight completed. Session is **PAUSED AWAITING DATA**, not a numerical failure.

**Next FIRST ACTION:** collect user-run temperature SWB evidence (CSV, actual pp*_des.cmd, SDE CMD, logs, project mapping) into ONE indexed ZIP using the read-only CMP_collect_TDEP_45_all_branches.py already supplied to the user. Request exact SWB project folder(s), run collector, upload CMP_TDEP_45_EVIDENCE.zip. **Do not dispatch new TCAD simulations first.**

- New matrix: 15 MEB [31,33,36,39,41,42,43,44,45,46,47,48,49,50,51] nm × [233,340,380] K = **45 new (MEB,T) cases**. User reports six SVisual output branches attempted for all 45 combinations (five SDevice branches: DC005/DC12/CGD/GIDL_ON/GIDL_OFF; ON has terminal+spatial SVisual siblings). **Expected** 225 device runs and 270 visual extractions, **verified completed** count remains UNKNOWN until logs inspected.
- 300 K already QC-validated across all 15 MEB; reuse unchanged. Final target = **60 (MEB,T) rows**.
- SWB parameters: SDE MEBDepth = 0.031/0.033/0.036/0.039/0.041/0.042/0.043/0.044/0.045/0.046/0.047/0.048/0.049/0.050/0.051 (um); SDevice Temp_K = 233/340/380 (K). SDE Atlas MeshLevel 2; frozen GCS=2.300, GateDepthBoost=0.025 um, Qf_Int=2.55e12 cm^-2, WF=4.8 eV. Temperature is prescribed isothermal; do not retune physics.
- After upload, verify correct MEB↔Temp↔node mapping, executable temperature/geometry preprocessing, completed solver and endpoint flags, current sign/KCL, AC reciprocity, DC metrics, ON/OFF vs integrated BTBT, spatial hotspot/E/20% area and missing records. Distinguish terminal total drain current from BTBT-only generation.
- Build 45-row audited temperature result, merge with existing 15 300 K rows, plot 36-nm temperature dependencies first then MEB-vs-temperature, investigate anomalies, and only then decide narrow follow-up numerical runs if needed. No blanket FZ-C re-comparison or full 300 K rerun.
- User-approved downstream A+B PAPER-CAL 1T1C framework remains **PROVISIONAL**; no retention gain/refresh/effective optimum is proven.
- **Detailed checkpoint and commands:** docs/progress/paper_cal_temperature_atlas_15x4_dispatch_20261009.md. **G0 audit:** docs/evidence/paper_cal_g0_parent_spatial_bridge_20261008.md.

## 5. Do not reopen by default

- C6/C7 physical calibration DOE or C8 fitting;
- model retuning to make old and new GIDL match;
- Hurkx→NonlocalPath replacement without a bridge;
- MeshLevel 4 or global over-refinement;
- historical FZ-C freeze rewritten as if newer mesh had been used then;
- Legacy absolute-value/1T1C relabeling;
- 3D production equivalence, physical retention/refresh or DWFG claims without execution;
- `48 nm = final optimum`.

## 6. Read next

1. `AGENTS.md` then this file.
2. **Resume first:** `docs/progress/paper_cal_temperature_atlas_15x4_dispatch_20261009.md`, then `docs/evidence/paper_cal_g0_parent_spatial_bridge_20261008.md`.
3. `docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md` and validated CSV plus source ZIP/QC.
4. Existing authoritative numerical-lineage concerns:
   - `docs/progress/b0_2d_paper_cal_mesh_revalidation_20261007.md`
   - `docs/research/b0_2d_production_revalidation_plan.md`
   - `docs/research/b0_2d_final_freeze_plan.md`
5. `docs/MODEL_SCOPE.md`, `docs/research/CLAIM_EVIDENCE_MATRIX.md` before upgrading claims.
6. Consult manual routing index and official T-2022.03 section **only** for a triggered syntax/solver/physics question.

**Session close-out (2026-10-09):** PAUSED / awaiting evidence from user-reported 45 MEB×T executions. First next action: collect and inspect actual SWB result ZIP, not FZ-C recalibration or new simulation.
