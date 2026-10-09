# CMP Research Handoff

> Canonical session handoff. Read after `AGENTS.md`. Current research authority: live GitHub main + linked underlying evidence.

**Last updated:** 2026-10-09  
**Session state:** **300 K Atlas QC VALIDATED; 45/45 new-T GIDL ON/OFF + spatial DATA QC REVIEWED; 44/45 new-T AC Cgd DATA QC REVIEWED; 36nm × four-temperature DC/GIDL/Cgd/spatial DATA-COMPLETE (new DC source curves QC PASS); remaining 14 new-temperature MEB DC PENDING**. FZ-C↔Atlas L2 mesh numeric equivalence NOT DEMONSTRATED.

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

## 2. Current completed work (2026-10-08, updated 2026-10-09)

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

**2026-10-09 update:** new-temperature 15-MEB GIDL ON/OFF/spatial 45×3 output branches and AC Cgd 44/45 extracted and independently reviewed; 41nm/340K Cgd is missing because the device did not converge. For nominal 36nm, DC005+DC12 at 233, 340, 380 K are newly source-curve QC-validated (six summary + six 6107-point Id-Vg curves, pp deck, SWB graph, bounded device-end log). Together with already validated 300 K this closes the **36nm × four-temperature electrical and spatial baseline**, not the full 15-depth DC thermal matrix. Source ZIP and full curve archive exist in local chat deliverable; six original DC summary CSV and 4-row integrated 36nm master are committed. Read `docs/progress/paper_cal_36nm_temperature_dc_qc_20261009.md` and `data/paper_cal/atlas_temperature_20261009/README.md`.

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
- New temperatures have independently QC-reviewed 45/45 terminal GIDL ON/OFF and spatial extracts, 44/45 Cgd extracts and, at 36nm only, validated six additional DC extractions from original curves. **No** PAPER-CAL 1T1C retention validation yet. Numerical/thermal mesh convergence NOT established.

## 4. Active stage and NEXT FIRST ACTION — 2026-10-09

**Stage:** 36nm four-temperature Atlas DATA-COMPLETE / independent source-extraction QC PASS, while the **other 14 MEB depths at new temperatures remain DC IN-PROGRESS / not ingested**. New 45 GIDL ON/OFF/spatial branches and 44 of 45 AC Cgd branches have been previously independently QC-reviewed. Do NOT treat this as full 60-condition DC completed.

**NEXT FIRST ACTION: let ongoing DC005/DC12 runs for remaining 14 MEB depths finish; collect completed original CSV+Id–Vg curves, actual pp*_des.cmd, SWB gtree, and node logs in batches. QC each row and append to the existing 60-row PARTIAL table. Do not start a blanket new run or re-calibration.**

- Source of 36nm validated four-temperature table: `data/paper_cal/atlas_temperature_20261009/processed/MEB36_4TEMP_INTEGRATED_VALIDATED_DC.csv` (59 fields, 4 rows), six raw DC summaries in `raw_dc36/`. Original user ZIP SHA256 `e680122bcfca924bf60f7320efd39f685e2289bc8b89f963938ccdd5319b8262`. Full ZIP / six Id–Vg raw curves / 60-row partial dataset / workbook / plots and reproducible script are in local downloadable `CMP_DC36_COMPLETE_RESEARCH_BUNDLE_20261009.zip`, NOT fully Git-committed.
- 36nm 233→380K: Vth@Vd1.2 falls 131.635mV; SSquick@Vd1.2 rises 40.228mV/dec; DIBL 22.813→26.786mV/V; Ion@Vg1.2 falls 4.093%; Ion/Ioff 2.5597e12→1.6586e7; **DC** Ioff@Vg0 rises ~148,009×. Total **GIDL-bias** Id_ON rises ~24,627.5×; raw AC |Cgd| falls 11.378%. These are distinct bias currents.
- Known QC watchlist: 36nm/380K ON−OFF vs q∫BTBT mismatch −4.39076%; five higher-temperature/shallow MEB cases are previously flagged in GIDL/Cgd analysis. The 41nm/340K AC is missing due to SDevice Newton failure; it must not be interpolated as measured.
- SWB parameters: SDE `MEBDepth` [0.031,0.033,0.036,0.039,0.041,0.042,0.043,0.044,0.045,0.046,0.047,0.048,0.049,0.050,0.051] um; SDevice `Temp_K=233,340,380` K; existing 300 K reused. Atlas MeshLevel=2; frozen Qf/WF/geometry adjustments unchanged.
- When other new-T MEB DC data are returned, independently check node↔temperature↔MEB, curve endpoint, constant-current Vth (Icrit=5e-6 A/um), SS1/2/quick, Ion/Ioff, DIBL from Vth005/12, then combine with existing GIDL/Cgd/spatial data without filling absent values. Narrow follow-up reruns only if a warning materially affects scientific conclusions.
- Remain within Atlas L2 branch. Avoid presenting frozen FZ-C↔Atlas equivalence, mesh convergence, physical retention/refresh or final effective optimum as proven. A+B 1T1C roadmap remains provisional.

**Read next:** `docs/progress/paper_cal_36nm_temperature_dc_qc_20261009.md` → `data/paper_cal/atlas_temperature_20261009/README.md` → `docs/progress/paper_cal_temperature_atlas_15x4_dispatch_20261009.md`.

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
2. **Resume first:** `docs/progress/paper_cal_36nm_temperature_dc_qc_20261009.md` and `data/paper_cal/atlas_temperature_20261009/README.md`. Then temperature dispatch and, only if relevant, G0 bridge.
3. `docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md` and validated CSV plus source ZIP/QC.
4. Existing authoritative numerical-lineage concerns:
   - `docs/progress/b0_2d_paper_cal_mesh_revalidation_20261007.md`
   - `docs/research/b0_2d_production_revalidation_plan.md`
   - `docs/research/b0_2d_final_freeze_plan.md`
5. `docs/MODEL_SCOPE.md`, `docs/research/CLAIM_EVIDENCE_MATRIX.md` before upgrading claims.
6. Consult manual routing index and official T-2022.03 section **only** for a triggered syntax/solver/physics question.

**Session close-out (2026-10-09):** 36nm four-temperature DC/GIDL/Cgd/spatial BASELINE DATA-COMPLETE / DC source QC PASS; the all-MEB DC thermal validation is IN PROGRESS. First next action: collect remaining-depth DC source curves / logs as SWB jobs finish and incrementally QC/extend the 60-row partial Atlas. No FZ-C recalibration or wholesale reruns.
