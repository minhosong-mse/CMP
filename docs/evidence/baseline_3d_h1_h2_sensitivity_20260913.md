# 3D-Sun-B0 H1/H2 reconstruction-sensitivity checkpoint

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Date: 2026-09-13  
> Purpose: test two unpublished reconstruction assumptions before any arbitrary calibration.

## 1. Reference electrical checkpoint

Current nominal 3-D reconstruction (`G1`, Vd=1.2 V, Vg=0→2 V):

```text
Vth_high = 1.14659 V   [provisional W=Wfin, L=Lgate constant-current criterion]
SS_high  ≈ 91.17 mV/dec
Id(2 V)  = 1.063365e-5 A
```

Sun et al. nominal targets:

```text
Vth      = 0.656 V
SS       = 76 mV/dec
Ion/Ioff = 3.4e10
DIBL     = 23.6 mV/V
```

The goal of H1/H2 was not parameter fitting. Each test changed one ambiguous reconstruction assumption while retaining the remaining baseline settings.

## 2. H1 — `Lgate` lateral mapping sensitivity

### Variant

Baseline interpretation:

```text
W-metal width       = 20 nm
oxide-outer width   = 30 nm
```

H1 alternative:

```text
oxide-outer width   = 20 nm
W-metal width       = 10 nm
```

All other nominal inputs and the same high-Vd SDevice deck were retained.

### Result

```text
Vth_high = 1.24248 V
SS        ≈ 97.39 mV/dec
Id(2 V)   ≈ 8.230e-6 A
```

Compared with nominal G1:

```text
ΔVth ≈ +95.9 mV
ΔSS  ≈ +6.2 mV/dec
Id(2 V) ≈ -22.6%
```

### Decision

**H1 rejected as an explanation of the paper mismatch.** The alternative mapping moves Vth and SS farther away from the reported nominal values. This does not prove the nominal CAD mapping is exact; it only shows that this specific alternative interpretation is not an improvement.

Evidence:

```text
data/baseline_3d_sun_b0/h1_idvg_highvd_lgate_outer20nm.csv
data/baseline_3d_sun_b0/h1_lgate_mapping_validation_summary.txt
```

## 3. H2 — lateral S/D Gaussian sensitivity

### Variant

Nominal:

```text
GaussFactor = 0.0
```

H2 screening value:

```text
GaussFactor = 0.8
```

`0.8` is a sensitivity bracket, not a literature value. Geometry, contacts, peak S/D doping, vertical `Djunction=48 nm`, gate work function, mesh policy, and SDevice physics were retained.

H2 mesh observed in SVisual:

```text
Points   = 473153
Elements = 2903662
```

This is essentially the same numerical scale as the nominal F1 mesh.

### Result

Using the same extraction procedure as G1:

```text
Vth_high = 1.14634 V
SS        ≈ 91.21 mV/dec
Id(2 V)   = 1.0643355e-5 A
Id_min    = 3.38024e-15 A @ Vg≈0.37956 V
```

Compared with nominal G1:

```text
ΔVth      ≈ -0.25 mV
ΔSS       ≈ +0.04 mV/dec
ΔId(2 V)  ≈ +0.09%
```

### Decision

**H2 rejected as the main cause of the large electrical mismatch.** A substantial nonzero lateral Gaussian factor produces an almost indistinguishable high-Vd ID–VG curve under the present reconstruction.

Evidence:

```text
data/baseline_3d_sun_b0/h2_gaussfactor0p8_idvg_highvd.csv
data/baseline_3d_sun_b0/h1_h2_sensitivity_summary_20260913.csv
```

## 4. What these checks imply

The remaining Vth gap is approximately 0.49 V, far larger than the H1/H2 shifts that improve the result. Sun et al. also report that even ±33% variation of `Djunction` changes Vth only from about 0.664 V to 0.641 V, and that the baseline `Rfillet` variation has <5% influence on device performance. Therefore the present discrepancy should not be chased by arbitrary tuning of published nominal parameters.

Current supported interpretation:

> The 3D-Sun-B0 deck is a numerically stable, literature-consistent reconstruction, but the paper's absolute electrical calibration is not reproduced. H1 and H2 show that two plausible unpublished mapping assumptions do not account for the discrepancy. Unpublished process/device-calibration details or a more fundamental 3-D geometry/process mapping difference remain possible.

## 5. Active next step — electrical mesh convergence

Do **not** start another parameter-fitting sweep yet.

The active validation has now moved to Coarse / Nominal / Fine electrical mesh convergence using the nominal geometry and nominal `GaussFactor=0.0` reconstruction.

```text
F1C Coarse = 1.25 × nominal spacing  -> launched / result pending
F1  Nominal = current reference       -> completed / candidate
F1F Fine   = 0.80 × nominal spacing  -> launched / result pending
```

Both new branches use the unchanged G1 high-drain electrical run:

```text
T = 300 K
Vd = 1.2 V
Vg = 0 → 2.0 V
WF = 4.8 eV
```

Exact variant definitions and the result-ingestion protocol are recorded at:

```text
code/sde/baseline_3d_sun_b0/VARIANTS.md
docs/evidence/baseline_3d_mesh_convergence_plan_20260913.md
```

After both runs finish, compare `Vth`, `SS`, `Id@2V`, full ID–VG shift, and Points/Elements. If Nominal and Fine are stable, freeze the literature-consistent 3-D baseline with an explicit absolute-calibration limitation and proceed to the simplified 2-D B0 fidelity comparison.

This sequence avoids turning unpublished geometry/process assumptions into fitted parameters merely to force agreement with one reported Vth value.
