# CMP Research Handoff

> Canonical session handoff. Read after `AGENTS.md`. Current research authority: live GitHub main + linked underlying evidence.

**Last updated:** 2026-10-08  
**Session state:** **300 K Atlas DATA-COMPLETE / QC-VALIDATED; exact FZ-C parent lineage bridge OPEN**.

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
- **Unresolved:** the exact 2026-10-05 executed FZ-C parent deck has not been canonically recovered/bridged to the new SDE. Accordingly, do **not** call the atlas a proven mesh-only restatement of frozen C7_4, despite coherent within-branch data.
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
- No current-branch temperature/1T1C retention validation yet.

## 4. Active gates and next immediate actions

**Next first task:** decide the **exact-parent/lineage bridge** to the 2026-10-05 FZ-C freeze before promoting the new 15-point atlas as a fully controlled physical-parameter/mesh-only production validation.

**Downstream study-design roadmap (approved direction, not numeric freeze):** A+B 1T1C Retention evaluation has been approved as the research framework — A: common 1.0→0.8 V initial-state retention; B: actual common-pulse Write→Hold→Read. The provisional 2D-to-cell handoff gates, measurement roles, and unresolved circuit/bias conditions are recorded in [`docs/research/MEB_2D_TO_1T1C_VALIDATION_ROADMAP_PROVISIONAL.md`](docs/research/MEB_2D_TO_1T1C_VALIDATION_ROADMAP_PROVISIONAL.md). This **does not supersede G0 exact-parent lineage verification** or freeze a new write/read/retention threshold.

1. Recover / map the executed C7_4/FZ-C SDE, SDevice, SVisual, extracted nominal DC/GIDL, and compare with current SDE/physics/geometry/bias under a documented controlled bridge.
2. If an exact bridge is unavailable, make an **explicit user decision** whether to proceed with this self-consistent post-freeze numerical branch as a **separately labeled** working atlas. Do not quietly retroactively re-freeze the physical calibration.
3. The current atlas already has enough 300 K DC/Cgd/GIDL/spatial/ON-OFF data; do **not** rerun this entire suite by default.
4. After lineage gate: plan selected temperature series (`233/300/340/380 K` only as justified by the active protocol), then PAPER-CAL 1T1C Write/Hold/Read and validated retention metric. Legacy Run-7 cell results are historical only.
5. Optional 0.5/0.1 nm sweep near 48 nm is **conditional on observed evidence / design question**, not automatic.

No new scientific optimum/final retention claim is frozen here.

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
2. New `docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md` and validated CSV plus source ZIP/QC.
3. Existing authoritative numerical-lineage concerns:
   - `docs/progress/b0_2d_paper_cal_mesh_revalidation_20261007.md`
   - `docs/research/b0_2d_production_revalidation_plan.md`
   - `docs/research/b0_2d_final_freeze_plan.md`
4. `docs/MODEL_SCOPE.md`, `docs/research/CLAIM_EVIDENCE_MATRIX.md` before upgrading claims.
5. Consult manual routing index and official T-2022.03 section **only** for a triggered syntax/solver/physics question.

**Session close-out:** DATA-COMPLETED / ANALYSIS PROVISIONAL on controlled FZ-C identity. First next action is provenance bridge, not a fresh MEB scan.
