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

The archive contains selected SVisual screenshots covering:

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

## 3. Raw text / data evidence package

Archive:

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

Archive SHA-256 recorded at packaging time:

```text
a59388796ce04679c042a7eeed686e1a1c6185e8391c57969b7e1bbbf0b5ecde
```

For direct review without opening the archive, the four principal CSVs are also stored as separate repository files:

```text
data/baseline_3d_sun_b0/g0_idvg_lowvd_0p05V_to_1p2V.csv
data/baseline_3d_sun_b0/g1_idvg_highvd_1p2V_to_2p0V.csv
data/baseline_3d_sun_b0/junction_source_C1.csv
data/baseline_3d_sun_b0/junction_drain_C2.csv
```

## 4. Evidence represented by these files

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

## 5. G2 status at this audit

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

## 6. Remaining baseline work

Before `FB-BASELINE-01` can be closed:

1. ingest and validate G2, then extract low-/high-Vd thresholds consistently and calculate DIBL;
2. freeze the paper-equivalent Vth and Ion/Ioff extraction definitions;
3. verify the paper `Canali` wording against the exact T-2022.03 high-field implementation currently logged as Caughey-Thomas saturation with gradient quasi-Fermi potential;
4. test the reconstruction sensitivity to the unpublished lateral S/D Gaussian assumption (`GaussFactor=0.0`) without arbitrary parameter fitting;
5. perform coarse / nominal / fine electrical mesh convergence before freezing F1;
6. compare the stabilized `3D-Sun-B0` metrics directly with the simplified 2-D CMP B0 to answer the original feedback question.

## 7. Repository synchronization audit

At this audit, the intended synchronization state is:

```text
docs/FEEDBACK_LOG.md
  → baseline row points to dedicated 3-D reconstruction and should state G2 result pending

docs/TASK_HUB.md
  → baseline task should point to the dedicated 3-D workflow and current next action

docs/evidence/feedback_baseline_3d_reconstruction_20260911.md
  → scientific checkpoint / assumptions / G0-G1 mismatch / G2-pending state

docs/evidence/baseline_3d_evidence_manifest_20260912.md
  → artifact inventory and audit trail
assets/images/feedback/20260911_baseline/
  → curated visual evidence archive
data/baseline_3d_sun_b0/
  → raw logs/data archive + directly browsable CSV evidence
```

The main `README.md` is intentionally **not** updated at this stage. Existing project policy defers final README integration until the principal presentation-feedback set is ready for one consistent synthesis.

## 8. Claim guardrail

Do not state that the Sun 2022 3-D BCAT has already been exactly reproduced. Current supported wording is:

> `3D-Sun-B0` is a literature-consistent 3-D reconstruction with frozen geometry/contact/vertical-doping checkpoints and numerically converged G0/G1 operation. The first electrical comparison remains mismatched to the reported paper nominal metrics, while G2/DIBL, extraction convention, high-field-model mapping, lateral-doping sensitivity, and electrical mesh convergence remain open.
