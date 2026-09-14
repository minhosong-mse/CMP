# 3D-Sun-B0 SDE variants

> Baseline source: `F1_nominal.cmd`  
> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Last updated: 2026-09-14  
> Final status: **controlled reconstruction sensitivities and DC mesh convergence completed**

This file records every controlled SDE variant used after the nominal F1 build. Variants are defined relative to the exact committed nominal source so the reconstruction assumptions remain auditable.

Deterministic generator:

```text
code/sde/baseline_3d_sun_b0/generate_variants.py
```

Generated working decks:

```text
H1_Lgate_outer20nm_sensitivity.cmd
H2_GaussFactor_0p8_sensitivity.cmd
F1C_coarse_mesh.cmd
F1F_fine_mesh.cmd
```

## 1. Nominal F1 reference

```text
Geometry:
  Lgate = 20 nm
  Rgate = 10 nm
  Router = 15 nm
  W metal width = 20 nm
  oxide-outer recess width = 30 nm

Doping:
  GaussFactor = 0.0
  Djunction = 48 nm

Electrical mesh:
  Global max/min            = 12 / 3 nm
  Active max                = 3 / 2 / 2 nm
  Active min                = 1 / 0.5 / 0.5 nm
  Gate interface max/min    = 1.5 / 0.3 nm isotropic
  Si/Oxide MaxLenInt        = 0.3 nm
  Junction max              = 1.5 / 1.5 / 0.5 nm
  Junction min              = 0.5 / 0.5 / 0.25 nm
  Gate-edge max             = 1.0 / 1.0 / 0.5 nm
  Gate-edge min             = 0.3 / 0.3 / 0.2 nm
```

Nominal high-Vd electrical checkpoint:

```text
Points   = 473004
Elements = 2902876
Vth_high = 1.14659 V
SS        = 91.170 mV/dec
Id(2 V)   = 1.063365e-5 A
```

## 2. H1 — Lgate mapping sensitivity

Purpose: test the alternative interpretation that the literature `Lgate=20 nm` spans the oxide-outer recess width rather than the tungsten width.

Changed mapping only:

```text
Router = 10 nm
Rgate  = 5 nm
oxide-outer recess width = 20 nm
W metal width            = 10 nm
```

Result:

```text
Vth_high = 1.24248 V
SS        = 97.39 mV/dec
Id(2 V)   ≈ 8.230e-6 A
```

Decision: **REJECTED as an explanation of the paper mismatch**. Vth and SS moved farther from the Sun nominal values.

Evidence:

```text
data/baseline_3d_sun_b0/h1_idvg_highvd_lgate_outer20nm.csv
data/baseline_3d_sun_b0/h1_lgate_mapping_validation_summary.txt
```

## 3. H2 — lateral Gaussian sensitivity

Purpose: test whether unpublished lateral S/D Gaussian spread is the dominant reason for the high reconstructed Vth.

Changed parameter only:

```text
GaussFactor = 0.0 -> 0.8
```

`0.8` is a sensitivity bracket, not a Sun-2022 literature value.

Result:

```text
Vth_high = 1.14634 V
SS        = 91.21 mV/dec
Id(2 V)   = 1.0643355e-5 A

Delta Vth vs nominal     ≈ -0.25 mV
Delta SS vs nominal      ≈ +0.04 mV/dec
Delta Id(2 V) vs nominal ≈ +0.09%
```

Decision: **REJECTED as the main cause of the large electrical mismatch**.

Evidence:

```text
data/baseline_3d_sun_b0/h2_gaussfactor0p8_idvg_highvd.csv
data/baseline_3d_sun_b0/h1_h2_sensitivity_summary_20260913.csv
docs/evidence/baseline_3d_h1_h2_sensitivity_20260913.md
```

## 4. F1C / F1F — electrical mesh convergence

Both branches return to the nominal geometry and `GaussFactor=0.0`. H1/H2 changes are not carried forward.

Common electrical condition:

```text
T = 300 K
Vd = 1.2 V
Vg = 0 -> 2.0 V
Vs = 0 V
Vsub = 0 V
WF = 4.8 eV
```

### F1C Coarse

Nominal mesh dimensions multiplied by `1.25`.

```text
Points   = 325741
Elements = 1998482
Vth_high = 1.14899 V
SS        = 91.251 mV/dec
Id(2 V)   = 1.0686352e-5 A
```

### F1F Fine

Nominal mesh dimensions multiplied by `0.80`.

```text
Points   = 883382
Elements = 5393039
Vth_high = 1.14541 V
SS        = 91.099 mV/dec
Id(2 V)   = 1.0638591e-5 A
```

Nominal -> Fine:

```text
Delta Vth     = -1.18 mV
Delta SS      = -0.071 mV/dec
Delta Id(2 V) = +0.046%
```

Decision:

```text
F1 for baseline DC ID-VG / Vth / SS comparison = FROZEN / ACCEPTED
```

This does not establish universal convergence for local peak-field or BTBT/GIDL hotspot claims.

Evidence:

```text
data/baseline_3d_sun_b0/f1c_coarse_idvg_highvd.csv
data/baseline_3d_sun_b0/g1_idvg_highvd_1p2V_to_2p0V.csv
data/baseline_3d_sun_b0/f1f_fine_idvg_highvd.csv
data/baseline_3d_sun_b0/f1_mesh_convergence_summary_20260914.csv
docs/evidence/baseline_3d_mesh_convergence_result_20260914.md
```

## 5. Final status after 2-D parity comparison

The downstream simplified-2-D-vs-3-D parity comparison is now also complete.

Final modeling decision:

```text
3D-Sun-B0 = literature-consistent higher-fidelity validation anchor
2D B0     = controlled relative-trend / design-space model
```

The simplified 2-D B0 does not quantitatively reproduce the stabilized 3-D electrical baseline. Future broad MEB / temperature / process exploration can remain in 2-D, but final design conclusions should be checked at selected representative points in 3-D.

Primary close-out:

```text
docs/evidence/feedback_baseline_closeout_20260914.md
data/baseline_3d_sun_b0/baseline_2d_3d_fidelity_summary_20260914.csv
data/baseline_3d_sun_b0/baseline_feedback_manifest_20260914.csv
```

## 6. Claim boundary

Do not use these variants to claim exact Sun-2022 process reproduction. H1/H2 are reconstruction sensitivities, not literature values, and F1 mesh acceptance is scoped to the DC baseline metrics tested here.
