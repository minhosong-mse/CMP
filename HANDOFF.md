# CMP Research Handoff

> Canonical session handoff. Read after `AGENTS.md`. Current research authority: live GitHub main + linked underlying evidence.

**Last updated:** 2026-10-14  
**Session state:** **NonlocalPath PAPER-CAL-derived pilot IN PROGRESS / PROVISIONAL**; L1/L2 duplicate effective mesh confirmed from 36/51-nm OFF source; dual-mesh (L1 vs Rough R1) 15-MEB × 2-VD × 2-mesh DC SWB dispatched by user, all 60 DC numerical results/QC still PENDING. Frozen C7_4 and prior Q0 close-out unchanged.

## 2026-10-14 latest checkpoint — L1/L2 duplicate effective mesh; L1 vs Rough R1 dual-mesh DC dispatched (PROVISIONAL)

- **Latest detailed status / first read:** [NonlocalPath dual-mesh DC dispatch and mesh-identity checkpoint](docs/progress/nonlocalpath_mesh_dc_dispatch_20261014.md); [source-verified 36/51-nm OFF QC CSV](data/nonlocalpath_pilot_20261013/off_l1_l2_mesh_equivalence_qc_20261014.csv). This section **supersedes the previous NonlocalPath pilot's immediate task ordering**, without changing the older historical evidence.
- **Source-QC COMPLETE, not mesh-converged:** user archive `CMP_NONLOCAL_OFF_L1_L2_EVIDENCE.zip` (76/76 manifest source entries; 36/51 nm × L1/L2 OFF 4/4 completed). Within each depth the L1 vs L2 SDE intended refinement differs but **actual TDR vertex coordinates, connectivity and numerical datasets match exactly**; PLTs and OFF currents match. L1/L2 are **one effective mesh state**, NOT two mesh-convergence points. 36nm OFF=1.242002286e-12 A/um, 51nm OFF=2.298969895e-16 A/um. Old L0 OFF differs materially; deck lineage needs checking.
- **New independent mesh candidate (screenshot / not physically validated):** Rough R1 at 36nm **12,857 SVisual elements / 6,176 points**, versus L1 **24,327 / 11,835**. Local windows include previously observed electron/hole peaks, but full ON−OFF/BTBT-integral convergence and R1 device performance are still pending. L1 36nm ON log completed; screenshot-only max should not be called a validated integral.
- **User-reported SWB dispatch:** actual projects `MEB_nonlocal_1_DC` and `MEB_nonlocal_1_DC_Copy` show **15 MEB depths × VD_Target 0.05/1.2 V each** = **30 SDevice conditions per project, 60 total**. Intended comparison is L1 vs Rough R1, but *project↔mesh mapping requires actual PP-SDE/TDR confirmation*. All new DC numerical outcomes/60-job completion **NOT YET VERIFIED**. DC deck: 300K, VG0→2 V, BTBT OFF, fixed PAPER-CAL geometry/calibration/positive Qf/WF. No current evidence that model swap fixes MEB DC sensitivity.
- **NEXT FIRST ACTION:** after user's DC outputs arrive, collect and source-QC both project trees with the prepared `collect_cmp_dualmesh_dc.py`, identify true mesh from PP source/TDR, validate 60 endpoints/current curves, extract identical Vth (Icrit=5e-6 A/um), SS, DIBL and Ion/Ioff definitions, compare L1/R1 across 15 MEB and against paper 36/48 trends. **Separately** finish 36/48/51 NonlocalPath ON−OFF carrier-resolved integrated BTBT and mesh-dependence plus Hurkx matched-parent controls before a baseline decision.
- **Preserve:** C7_4 frozen baseline, calibration, original Atlas/Q0, README and DECISIONS; no NonlocalPath promotion, no 3D-equivalence, no retention/optimum claim. This record documents work in progress, not a validated result set.
## 2026-10-14 NonlocalPath pilot (newest session checkpoint, PROVISIONAL)

- **Current stopping classification: IN PROGRESS / PROVISIONAL; no re-freeze.** [Pilot progress & staged model-validation gates](docs/progress/nonlocalpath_hotspot_pilot_checkpoint_20261014.md), [numerical/QC tables](data/nonlocalpath_pilot_20261013/README.md). User plans NonlocalPath hotspot screening → new mesh validation → controlled 15-MEB Hurkx/NonlocalPath GIDL/BTBT → independent DC sensitivity gate → conditional future baseline adoption (NOT an adopted model/parameter change).
- `MEB_nonlocal_off`: six MEB = **31/36/39/41/46/51 nm** (46, not 48); 300K, Vd=1.2,Vg=-0.7, current L2; 6/6 SDevice endpoints and OFF terminal PLT source-QC PASS; original ZIP SHA256 `086d50fadc4a271728030b42000aac62015ea77562c3bc1fbcecc3b1f6fe1e92`. OFF differs from historical Hurkx Atlas OFF by **2.39–3.80x**, so clean physics-model comparison is **NOT** established.
- `MEB_nonlocal`: ON SVisual `Band2BandGeneration` **screenshot-only** at 36nm peak `6.32186e18` at (X,Y)=`(0.0369141,0.252174) um`, 39nm peak `2.01641e18` at `(0.0398437,0.252174) um`. GateTop-adjacent; no carrier-resolved maps/integrals or source-QC of ON TDR/PP-CMD/PLT. No mesh convergence/optimum/model preference.
- **NEXT FIRST ACTION:** collect/verify remaining ON actual PP-CMD/log/terminal PLT/final TDR, 36/39 carrier-specific BTBT and all-region/local-surface hotspots, and complete representative depth screening (including missing **48 nm** boundary); then plan/common-source mesh convergence and run controlled Hurkx↔NonlocalPath comparisons. DC extraction was previously BTBT-OFF, so swapping the BTBT model does NOT itself solve the SS/Vth MEB-sensitivity issue. Frozen PAPER-CAL GCS2.3/GDB25nm/Qf2.55e12, older evidence, Q0 obligations and outstanding temperature DC follow-through remain intact.
- No README update; no `DECISIONS.md` model decision; no 1T1C retention claim. This new section supersedes prior immediate task ordering for **this user-selected Nonlocal pilot** but does not close older Q0/SDE ROI evidence gates.

## 2026-10-12 BTBT 공간/메시 관찰 기록 (non-decision checkpoint)

- New evidence-only checkpoint: [docs/evidence/btbt_roi_hotspot_mesh_checkpoint_20261012.md](docs/evidence/btbt_roi_hotspot_mesh_checkpoint_20261012.md). Q0 Surface-L1 300 K 31/36/41/48 nm TDR signed ROI fractions, PAPER-CAL Atlas 300 K whole-Si 15 MEB reference, 340 K screen-only hotspots, observed SDE mesh coverage, pending 300 K PAPER-CAL region split are now indexed. CSVs / redrawable SVGs under `data/btbt_roi_20261012/` and `assets/images/paper_cal/btbt_roi_20261012/`.
- Q0 TDR-based Surface signed shares at 31/36/41/48 nm = 10.545/10.872/17.712/57.926%; original whole-Si SVisual integration cross-check |error| < 0.0003%. Specific to existing Q0 Surface-L1 mesh; no model/mesh convergence claim.
- PAPER-CAL 300 K 36/39/41 nm whole-Si archived values = 1.151025e6 / 1.682352e6 / 1.551265e6. **PAPER-CAL same-temperature Surface/Gate ROI split not yet obtained.**
- Next: receive and audit prepared independent 300 K Atlas L2 36/39/41 nm TDRs and ROI CSV; measure Surface-side local hotspot; only then design/check separate common Surface refinement across MEB. No README/freeze/model-decision or retention claim changes.

## 0. 2026-10-11 Faithful-Q0 source-based execution close-out — authoritative new checkpoint

> **Completion status:** User-executed 300K Faithful-Q0 ×15 and surface-hotspot-refined Faithful-Q0 ×15 ON/OFF/spatial **DATA + SOURCE QC COMPLETE**; numerical mesh convergence, 2D model selection and GIDL/retention mechanism **NOT DEMONSTRATED**. This update supersedes the previous planned-Q0-run handoff. No new TCAD was run *during the archival close-out*.

**Lineage and controlled comparison**
- `B0-2D-PAPER-CAL = C7_4/B_QF_HALF` stays **FROZEN**: DC-calibrated reduced-order 2D surrogate (GCS2.3, GDB25nm, Qf2.55e12cm^-2). Literature DC benchmark agreement alone cannot establish predictive GIDL/BTBT validity or real fabricated oxide/recess/Qf.
- `B0-2D-FAITHFUL-Q0` remains a **CONDITIONAL** paper-dimension 2D control (GCS1, GDB0, modeled Tox5nm/recess120nm, Qf=0 assumption). Both Q0 and PAPER-CAL use **Hurkx**; no single-variable calibration causality has been isolated.
- Existing `3D-Sun-B0` is literature-consistent but itself DC-mismatched, hence a **proposed 3D mechanism cross-check**, not ground-truth paper calibration.

**Original Q0 15-depth 300K audit:** user original ZIP `CMP_FAITHFUL_Q0_ALL15_4PROJECTS_EVIDENCE.zip` 1,513/1,513 source hash+length PASS; 60/60 SDevice done; 15 ON terminal, 15 OFF terminal, 15 ON spatial, **14/15 Cgd** (31nm SVisual extract absent). MEB↑→both total drain current and original Q0 Cgd↓, also observed for PAPER-CAL, but **BTBT spatial generation and Hurkx-sensitive fraction diverge**. PAPER-CAL BTBT integral peaks39nm and BTBTmax41nm with GateTop-tracking hotspot; Q0 BTBT integral decreases with MEB, near-surface hotspot ~X2.34nm for 33–51nm. Do not call total drain current “pure BTBT.”

**Q0 Phase1 surface hotspot experiment (actually executed):** user ZIP `CMP_Q0_PHASE1_SPLIT6_15MEB_EVIDENCE.zip`: 8+7 split SWB projects for GIDL ON/OFF/spatial, 45/45 SDevice done; 1,197/1,197 original source hashes PASS. Same Q0 geometry/physics/300K (`Vd1.2,Vg-0.7`), same GateTop-following GIDL Core; only new local SDE mesh windows around near-surface hotspot (Outer X0–15nm/Y258–276nm; Core X0–8nm/Y263–270nm) `SurfaceRefineLevel=1`.
- Q0 before→after: 36nm total Id **+47.66%**, whole-Si BTBT integral **−17.68%**; 48nm **+37.79%/−75.81%**, 51nm **+36.01%/−83.47%**. At 31nm global BTBT Xhot switches **29.30→2.34nm**. All 15 retain decreasing *total Id* MEB ranking, while spatial generation remains strongly **mesh-sensitive**.
- 36nm Q0 Surface-L1 total drain Id ≈1.4652936e-9 A/um vs PAPER-CAL Atlas ≈1.0885586e-12; Hurkx ON−OFF fraction ≈0.000069% vs 16.94%. In Q0 Surface-L1 the log-reported drain *electron* ON−OFF tracks `q∫BTBT` within ~1.6% across 15 MEB at displayed precision; drain *hole* current dominates total. Microscopic OFF-hole source, full terminal collection and very small ON−OFF numerical precision **NOT RESOLVED**. Selected Level1 spatial TDR/PLT exist at 31/36/41/48nm. **No Surface-L1 Cgd/DC re-sweep**.
- Two meshes (L2 original and added Surface-L1) demonstrate **sensitivity**, NOT convergence or physical truth. PAPER-CAL historical FZ-C→Atlas L2 numerical mismatch remains a separate outstanding risk.

**Data preservation complete on live GitHub main:**
- `data/faithful_q0/20261011_300k/README.md` gives three 15-depth CSV datasets, exact SDE edit, source-QC reports.
- `PUBLIC_ARCHIVES_MANIFEST.json` + `restore_public_archives.py` reconstruct and SHA256-verify **three public source archives**, stored as 8+14+2 Git binary chunks: original Q0 (source CMD/log/CSV); surface-L1 (CMD/log/CSV and selected TDR/PLT); graphs, full QC tables/collector scripts/plots. Server paths anonymized and job/out/sta intermediates excluded; **original user-uploaded ZIP hashes remain separately recorded**, not overwritten.
- `docs/research/faithful_q0_model_selection_gate_20261011.md` records academic self-audit and **PROPOSED** model-selection strategy. Relevant archive commits `f2c4f515`, `61b64a33`, `557f13f4`.

**Stopping classification:** **PAUSED / PROVISIONAL model-selection stage** after successful source-evidence archival; no PAPER-CAL recalibration, Q0 replacement-baseline adoption, proven retention improvement or final optimum.

**NEXT FIRST ACTION (bounded validation; planning, not yet executed):**
1. At **36 and 48nm first**, inspect source TDR/hotspot grid, actual electrode electron/hole currents, ON−OFF subtraction precision, q∫BTBT/AreaFactor; if required run Q0 SurfaceRefineLevel1→2 for selected points. Add 31nm if hotspot switch remains consequential. Avoid automatic full 15-depth rerun; target PAPER-CAL Atlas mesh comparability separately.
2. At **36nm**, isolate GCS/GDB/Qf effect on spatial BTBT and ON/OFF with controlled comparisons (full 2³ only if interactions matter), **without** retroactive changes to frozen baseline.
3. **PROPOSED:** move selected **3D-Sun-B0 36/48nm** physical-mechanism comparison ahead of further broad 1T1C/temperature studies, then decide which 2D surrogate's relative MEB ranking is defensible. The current 3D anchor is not exact paper-calibrated truth.
4. Concurrently collect/QC pending **14 new-T Atlas DC depths** when source files become available. No new all-MEB/temperature mass execution as default.

**Claim guardrail:** Good DC benchmark fitting != experimentally verified GIDL physics. Paper dimensions != measured process details. Q0 validates shared relative Cgd and total Id directions only conditionally; the spatial BTBT and Hurkx-sensitive mechanism, 3D equivalence, retention translation and 48nm optimum remain unproven.

---

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

## 4. Concurrent original Atlas DC source collection — 2026-10-11

**Concurrent Atlas DC stage:** 36nm four-temperature Atlas DATA-COMPLETE / independent source-extraction QC PASS, while the **other 14 MEB depths at new temperatures remain DC IN-PROGRESS / not ingested**. New 45 GIDL ON/OFF/spatial branches and 44 of 45 AC Cgd branches have been previously independently QC-reviewed. Do NOT treat this as full 60-condition DC completed.

**Concurrent Atlas DC follow-through:** let ongoing DC005/DC12 runs for remaining 14 MEB depths finish; collect completed original CSV+Id–Vg curves, actual pp*_des.cmd, SWB gtree, and node logs in batches. QC each row and append to the existing 60-row PARTIAL table. Do not start a blanket new run or re-calibration. **The new primary research validation gate is in §0; it does not cancel pending DC source collection.**

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

1. `AGENTS.md` then this file; read **§0 for completed Q0 original + Surface-L1 data/QC archive, model uncertainty and next selective checks**. Source manifest/restore: `data/faithful_q0/20261011_300k/README.md`; proposed decision gate: `docs/research/faithful_q0_model_selection_gate_20261011.md`.
2. **Concurrent Atlas DC follow-through:** `docs/progress/paper_cal_36nm_temperature_dc_qc_20261009.md` and `data/paper_cal/atlas_temperature_20261009/README.md`. Then temperature dispatch and, only if relevant, G0 bridge.
3. `docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md` and validated CSV plus source ZIP/QC.
4. Existing authoritative numerical-lineage concerns:
   - `docs/progress/b0_2d_paper_cal_mesh_revalidation_20261007.md`
   - `docs/research/b0_2d_production_revalidation_plan.md`
   - `docs/research/b0_2d_final_freeze_plan.md`
5. `docs/MODEL_SCOPE.md`, `docs/research/CLAIM_EVIDENCE_MATRIX.md` before upgrading claims.
6. Consult manual routing index and official T-2022.03 section **only** for a triggered syntax/solver/physics question.

**Session close-out (2026-10-09):** 36nm four-temperature DC/GIDL/Cgd/spatial BASELINE DATA-COMPLETE / DC source QC PASS; the all-MEB DC thermal validation is IN PROGRESS. First next action: collect remaining-depth DC source curves / logs as SWB jobs finish and incrementally QC/extend the 60-row partial Atlas. No FZ-C recalibration or wholesale reruns.

**Session close-out (2026-10-11):** Q0 original + surface-hotspot Level1 (15 MEB) source evidence, QC, SDE and reproducible public GitHub archival **COMMITTED**. Model-selection, mesh convergence, electron/hole leakage origin and retention validation **OPEN**. Next first action is the bounded numerical + calibration/3D selection gate in §0. Frozen PAPER-CAL and historical runs unchanged.
