# 3D-Sun-B0 SDE variants

> Baseline source: `F1_nominal.cmd`  
> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Last updated: 2026-09-13

This file records every controlled SDE variant used after the nominal F1 build. The variants are defined relative to `F1_nominal.cmd` so the reconstruction assumptions remain auditable even when the complete working CMD is kept in the Sentaurus workspace during execution.

The deterministic generator used to reproduce the working sensitivity / convergence decks from the committed nominal source is:

```text
code/sde/baseline_3d_sun_b0/generate_variants.py
```

Running it beside `F1_nominal.cmd` generates:

```text
H1_Lgate_outer20nm_sensitivity.cmd
H2_GaussFactor_0p8_sensitivity.cmd
F1C_coarse_mesh.cmd
F1F_fine_mesh.cmd
```

## Nominal F1 reference

```text
Geometry mapping:
  Lgate = 20 nm
  Rgate = Lgate/2 = 10 nm
  Router = Rgate + Tox = 15 nm
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

## H1 — Lgate mapping sensitivity

Purpose: test the alternative interpretation that literature `Lgate=20 nm` spans the oxide-outer recess width rather than the tungsten width.

Only the lateral gate/recess mapping was changed:

```text
Router = Lgate/2 = 10 nm
Rgate  = Router - Tox = 5 nm

oxide-outer recess width = 20 nm
W metal width            = 10 nm
```

Contacts, nominal doping targets, `GaussFactor=0.0`, mesh policy and the G1 SDevice physics/bias deck were retained.

Electrical result:

```text
Vth_high = 1.24248 V
SS        = 97.39 mV/dec
Id(2 V)   ≈ 8.230e-6 A
```

Decision: **rejected as an explanation of the paper mismatch** because Vth and SS move farther from the Sun nominal values.

Evidence:

```text
data/baseline_3d_sun_b0/h1_idvg_highvd_lgate_outer20nm.csv
data/baseline_3d_sun_b0/h1_lgate_mapping_validation_summary.txt
```

## H2 — lateral Gaussian sensitivity

Purpose: test whether the unpublished lateral S/D Gaussian spread is the dominant reason for the high reconstructed Vth.

Only the analytical-profile lateral factor was changed:

```text
GaussFactor = 0.0  ->  0.8
```

`0.8` is a sensitivity bracket and **not** a Sun-2022 literature value.

Electrical result:

```text
Vth_high = 1.14634 V
SS        = 91.21 mV/dec
Id(2 V)   = 1.0643355e-5 A
```

Relative to nominal G1:

```text
Delta Vth     ≈ -0.25 mV
Delta SS      ≈ +0.04 mV/dec
Delta Id(2 V) ≈ +0.09%
```

Decision: **rejected as the main cause of the large electrical mismatch**.

Evidence:

```text
data/baseline_3d_sun_b0/h2_gaussfactor0p8_idvg_highvd.csv
data/baseline_3d_sun_b0/h1_h2_sensitivity_summary_20260913.csv
docs/evidence/baseline_3d_h1_h2_sensitivity_20260913.md
```

## F1C / F1F — electrical mesh-convergence branches

These branches return to the **nominal geometry/doping mapping**. H1 and H2 changes are not carried forward.

The geometry, contacts, `GaussFactor=0.0`, `Djunction=48 nm`, gate work function, and G1 SDevice physics/bias conditions are fixed. Only mesh spacing changes.

### F1C — Coarse

Nominal mesh dimensions are multiplied by `1.25`:

```text
Global max/min            = 15 / 3.75 nm
Active max                = 3.75 / 2.5 / 2.5 nm
Active min                = 1.25 / 0.625 / 0.625 nm
Gate interface max/min    = 1.875 / 0.375 nm isotropic
Si/Oxide MaxLenInt        = 0.375 nm
Junction max              = 1.875 / 1.875 / 0.625 nm
Junction min              = 0.625 / 0.625 / 0.3125 nm
Gate-edge max             = 1.25 / 1.25 / 0.625 nm
Gate-edge min             = 0.375 / 0.375 / 0.25 nm
```

### F1F — Fine

Nominal mesh dimensions are multiplied by `0.80`:

```text
Global max/min            = 9.6 / 2.4 nm
Active max                = 2.4 / 1.6 / 1.6 nm
Active min                = 0.8 / 0.4 / 0.4 nm
Gate interface max/min    = 1.2 / 0.24 nm isotropic
Si/Oxide MaxLenInt        = 0.24 nm
Junction max              = 1.2 / 1.2 / 0.4 nm
Junction min              = 0.4 / 0.4 / 0.2 nm
Gate-edge max             = 0.8 / 0.8 / 0.4 nm
Gate-edge min             = 0.24 / 0.24 / 0.16 nm
```

Both use the unchanged G1 electrical run:

```text
T = 300 K
Vd = 1.2 V
Vg = 0 -> 2.0 V
Vs = 0 V
Vsub = 0 V
WF = 4.8 eV
```

Status as of 2026-09-13:

```text
F1C Coarse  = launched / result pending
F1 Nominal  = completed / reference
F1F Fine    = launched / result pending
```

Required result package per new branch:

```text
1) SVisual Points / Elements
2) gate OuterVoltage vs drain TotalCurrent CSV
```

No full Sentaurus log or native `.plt` is required unless the curve or convergence is abnormal.
