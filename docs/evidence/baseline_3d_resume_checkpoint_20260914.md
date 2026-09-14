# 3D-Sun-B0 latest resume checkpoint — 2026-09-14

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`

## Current state

```text
Literature truth table              DONE
Geometry / contacts / vertical doping PASS / FROZEN
Djunction source/drain              48.0 nm PASS
G0 bring-up                         PASS
G1 high-Vd full ID-VG               PASS
G2 low-Vd full ID-VG                PASS
Threshold-width ambiguity check     DONE — not main cause
Canali / Caughey-Thomas mapping      DONE — compatible at model-family level
H1 Lgate mapping sensitivity         DONE — rejected
H2 lateral Gaussian sensitivity      DONE — rejected as main cause
F1 Coarse/Nominal/Fine convergence   DONE — PASS for baseline DC
F1 nominal mesh                      FROZEN for baseline DC comparison
Exact Sun electrical reproduction    NOT CLAIMED
```

## Mesh-convergence result

```text
F1C Coarse:  Points 325741, Elements 1998482
  Vth_high = 1.14899 V
  SS       = 91.251 mV/dec
  Id(2V)   = 1.0686352e-5 A

F1 Nominal: Points 473004, Elements 2902876
  Vth_high = 1.14659 V
  SS       = 91.170 mV/dec
  Id(2V)   = 1.063365e-5 A

F1F Fine:   Points 883382, Elements 5393039
  Vth_high = 1.14541 V
  SS       = 91.099 mV/dec
  Id(2V)   = 1.0638591e-5 A
```

Nominal -> Fine:

```text
Delta Vth     = -1.18 mV
Delta SS      = -0.071 mV/dec
Delta Id(2 V) = +0.046%
```

Decision: the nominal F1 mesh is sufficiently stable for the present **DC baseline ID–VG fidelity comparison**. This does not establish universal convergence for local peak-field or BTBT/GIDL hotspot quantities.

## Active next step

Do not continue fitting unpublished 3-D parameters merely to force Sun's absolute Vth.

Next task is the original feedback question:

```text
stabilized literature-consistent 3D-Sun-B0
vs
simplified 2-D CMP B0
```

Compare, under transparent/common extraction where possible:

```text
Vth
SS
Ion/Ioff or clearly defined current-ratio proxy
DIBL where bias definitions are compatible
ID-VG shape / turn-on
key geometry/model differences relevant to MEB trend interpretation
```

Goal: state which properties of the simplified 2-D B0 are defensible for **relative MEB-trend analysis**, and which absolute 3-D BCAT characteristics are not reproduced.

## Primary evidence

```text
docs/evidence/baseline_3d_mesh_convergence_result_20260914.md
data/baseline_3d_sun_b0/f1_mesh_convergence_summary_20260914.csv
code/sde/baseline_3d_sun_b0/VARIANTS.md
docs/evidence/baseline_3d_h1_h2_sensitivity_20260913.md
```
