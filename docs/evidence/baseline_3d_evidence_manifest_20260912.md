# 3D-Sun-B0 baseline evidence manifest — 2026-09-12

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Reconstruction: `3D-Sun-B0`  
> Status at audit: **G0 PASS / G1 PASS / G2 launched, result not yet ingested**

## 1. Purpose

This manifest records the evidence already produced for the dedicated literature-consistent 3-D BCAT baseline reconstruction, identifies the repository locations of the curated/raw artifacts, and prevents the feedback hub from overstating work that has not yet been returned and checked.

The reconstruction is intended as a literature-consistent implementation of Sun et al. (Micromachines 2022, 13, 1476), not an exact reverse-engineered paper deck.

## 2. Curated visual evidence

Archive:

```text
assets/images/feedback/20260911_baseline/baseline_visual_evidence_20260911.zip
```

The archive contains eight selected SVisual screenshots covering:

1. 3-D baseline geometry overview;
2. along-channel XZ buried-gate / oxide / nitride cross-section;
3. across-fin YZ saddle-fin cross-section;
4. source / drain / gate / substrate contact-boundary visualization;
5. 3-D doping view with the vertical junction-cut setup;
6. F1 nominal electrical mesh / doping view;
7. source-side junction-depth profile;
8. drain-side junction-depth profile.

Archive SHA-256 recorded at packaging time:

```text
9f641b31e20742bcbfc8a73c90ebd572e440242efc735ceecb016a19f54bf6b1
```

These images document the reconstruction / QA checkpoints; they do not by themselves prove electrical agreement with the paper.

## 3. Raw text / data evidence

### 3.1 Raw log/data archive

```text
data/baseline_3d_sun_b0/baseline_raw_text_data_20260911.zip
```

Contents:

```text
g0_idvg_lowvd_0p05V_to_1p2V.csv
g1_idvg_highvd_1p2V_to_2p0V.csv
junction_source_C1.csv
junction_drain_C2.csv
g0_sdevice_full.log
g1_sdevice_full.log
f1_sde_build_full.log
README.txt
```

Archive SHA-256:

```text
a59388796ce04679c042a7eeed686e1a1c6185e8391c57969b7e1bbbf0b5ecde
```

For direct review without opening the archive, the four principal CSVs are also stored separately:

```text
data/baseline_3d_sun_b0/g0_idvg_lowvd_0p05V_to_1p2V.csv
data/baseline_3d_sun_b0/g1_idvg_highvd_1p2V_to_2p0V.csv
data/baseline_3d_sun_b0/junction_source_C1.csv
data/baseline_3d_sun_b0/junction_drain_C2.csv
```

### 3.2 Native G0/G1 curve output archive

```text
data/baseline_3d_sun_b0/baseline_curve_plt_20260911.zip
```

Contains the original uploaded current-curve outputs:

```text
IdVg_LowVd_n5_des.plt
IdVg_HighVd_n5_des.plt
```

Archive SHA-256:

```text
d094ae4f6f10d1ce61b963d592ccbc6a963879605be24e6b0c528393c5de8d63
```

This preserves the native Sentaurus curve data in addition to the CSV exports.

## 4. Executable SDevice decks now committed

Current reconstruction SDevice decks are stored under:

```text
code/sdevice/baseline_3d_sun_b0/
```

Files:

```text
G0_bringup.cmd
G1_highVd_full_idvg.cmd
G2_lowVd_full_idvg.cmd
README.md
```

Status:

```text
G0 deck  = executed / PASS
G1 deck  = executed / PASS
G2 deck  = launched; completed result not yet ingested
```

The deck README also records the current physics-model claim boundary and SWB placeholder behavior.

### Exact SDE source availability

The final F1 SDE **build log** is preserved in the raw archive, but the exact final standalone SDE source command file was not available as an independently uploaded conversation artifact during this audit. It is therefore intentionally **not reconstructed from the execution log and mislabeled as exact source**.

Remaining repository action when the original file is exported from the Sentaurus workspace:

```text
add exact final 3D-Sun-B0 SDE source CMD
```

Until then, the build log plus visual/doping/mesh evidence are retained as traceability evidence, not as a substitute for the original source file.

## 5. Evidence represented by these files

### Geometry / contact

The curated images preserve the frozen geometry views and the four-terminal contact visualization used during Phase C / D validation.

### Vertical doping QA

Both source and drain cut data place the signed net-doping zero crossing at approximately:

```text
Distance = 0.048 um = 48.0 nm
```

This validates the nominal vertical `Djunction = 0.40 × 120 nm` reconstruction target. It does **not** validate the unpublished lateral S/D diffusion profile.

### F1 mesh

The curated F1 screenshot records approximately:

```text
SVisual elements ≈ 2.90 M
SVisual points   = 473,004
```

The mesh is a nominal electrical **candidate**, not yet a convergence-frozen production mesh.

### G0

The G0 package preserves the low-drain numerical bring-up run:

```text
T = 300 K
Vd = 0.05 V
Vg = 0 → 1.2 V
Id(Vg=1.2 V) = 7.769e-8 A
```

Purpose: numerical / contact / physics / turn-on sanity validation, not final paper-metric reproduction.

### G1

The G1 package preserves the first high-drain paper-condition comparison sweep:

```text
T = 300 K
Vd = 1.2 V
Vg = 0 → 2.0 V
Id(Vg=2.0 V) = 1.063e-5 A
```

Current provisional extraction remains approximately:

```text
SS                    ≈ 91.2 mV/dec
max(Id)/min(Id)        ≈ 3.04e9
Vth_high*              ≈ 1.147 V
```

`*` uses the provisional `W=Wfin=17 nm`, `L=Lgate=20 nm` interpretation of the paper constant-current criterion and is not yet frozen as paper-equivalent Vth.

Paper nominal targets remain:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

Therefore the current 3-D deck is numerically operational but electrical reproduction is not yet demonstrated.

## 6. G2 status at this audit

A full low-drain G2 run was launched with:

```text
T = 300 K
Vd = 0.05 V
Vg = 0 → 2.0 V
```

However, no completed G2 log / PLT / CSV has yet been returned to the baseline workflow for ingestion and validation. Therefore repository status must be written as:

```text
G2 = LAUNCHED / RESULT PENDING INGESTION
```

and not as `PASS`, `completed`, or a final DIBL result.

Required G2 evidence when available:

```text
full SDevice log
IdVg_LowVd_Full_*.plt
gate OuterVoltage vs drain TotalCurrent CSV
```

## 7. Remaining baseline work

Before `FB-BASELINE-01` can be closed:

1. ingest and validate G2, then extract low-/high-Vd thresholds consistently and calculate DIBL;
2. freeze the paper-equivalent Vth and Ion/Ioff extraction definitions;
3. verify the paper `Canali` wording against the exact T-2022.03 high-field implementation currently logged as Caughey-Thomas saturation with gradient quasi-Fermi potential;
4. test the reconstruction sensitivity to the unpublished lateral S/D Gaussian assumption (`GaussFactor=0.0`) without arbitrary parameter fitting;
5. perform coarse / nominal / fine electrical mesh convergence before freezing F1;
6. compare the stabilized `3D-Sun-B0` metrics directly with the simplified 2-D CMP B0 to answer the original feedback question;
7. add the original final SDE source CMD once exported from the Sentaurus workspace.

## 8. Repository synchronization audit

At this audit, the synchronized state is:

```text
docs/FEEDBACK_LOG.md
  → dedicated 3-D reconstruction; G2 result pending ingestion

docs/TASK_HUB.md
  → dedicated 3-D task, latest checkpoint and next actions

docs/evidence/feedback_baseline_3d_reconstruction_20260911.md
  → assumptions / validation / G0-G1 mismatch / G2-pending scientific checkpoint

docs/evidence/baseline_3d_evidence_manifest_20260912.md
  → artifact inventory, source-availability audit and repository traceability
assets/images/feedback/20260911_baseline/
  → curated visual evidence archive
data/baseline_3d_sun_b0/
  → raw log/data archive + native PLT archive + directly browsable CSV evidence
code/sdevice/baseline_3d_sun_b0/
  → exact G0/G1/G2 SDevice decks used in the workflow
```

The main `README.md` is intentionally **not** updated at this stage. Existing project policy defers final README integration until the principal presentation-feedback set is ready for one consistent synthesis.

## 9. Claim guardrail

Do not state that the Sun 2022 3-D BCAT has already been exactly reproduced. Current supported wording is:

> `3D-Sun-B0` is a literature-consistent 3-D reconstruction with frozen geometry/contact/vertical-doping checkpoints and numerically converged G0/G1 operation. The first electrical comparison remains mismatched to the reported paper nominal metrics, while G2/DIBL, extraction convention, high-field-model mapping, lateral-doping sensitivity, electrical mesh convergence, and final exact-SDE-source archival remain open.
