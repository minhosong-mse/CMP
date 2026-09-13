# 3D-Sun-B0 electrical mesh-convergence checkpoint

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Date: 2026-09-13  
> Status: **F1C Coarse + F1F Fine launched; results pending**

## 1. Why this step exists

The nominal 3-D reconstruction is numerically operational through G0/G1/G2, but its paper-level electrical values remain far from the Sun et al. nominal baseline. Two controlled reconstruction sensitivities have already been checked:

```text
H1 Lgate-mapping alternative
  Vth_high = 1.24248 V
  result = farther from paper nominal -> reject as mismatch explanation

H2 GaussFactor 0.0 -> 0.8
  Vth_high = 1.14634 V
  result = ~0.25 mV shift -> reject as main mismatch cause
```

Before freezing the literature-consistent 3-D baseline and comparing it with the simplified 2-D B0, the electrical metrics must be shown to be stable against reasonable mesh-spacing changes.

## 2. Controlled comparison

All three branches use the nominal reconstruction geometry and nominal doping mapping:

```text
Lgate = 20 nm
Drecess = 120 nm
DBCAT = 36 nm
Tox = 5 nm
Wfin = 17 nm
Hfin = 48 nm
Djunction = 48 nm
GaussFactor = 0.0
WF = 4.8 eV
```

H1 and H2 changes are **not** carried into the convergence branches.

The same G1 high-drain SDevice conditions are used for every mesh:

```text
T = 300 K
Vs = 0 V
Vsub = 0 V
Vd = 1.2 V
Vg = 0 -> 2.0 V
```

## 3. Mesh branches

| Branch | Relative spacing | Role | Status |
|---|---:|---|---|
| `F1C` Coarse | `1.25 x nominal` | coarse convergence point | RUNNING / result pending |
| `F1` Nominal | `1.00 x` | current reference | PASS / candidate |
| `F1F` Fine | `0.80 x nominal` | fine convergence point | RUNNING / result pending |

Exact refinement values are recorded in:

```text
code/sde/baseline_3d_sun_b0/VARIANTS.md
```

## 4. Result data required

For each of F1C and F1F, retain only the standard lightweight repository evidence unless debugging is necessary:

```text
1. SVisual Points / Elements
2. ID-VG CSV
   X = gate OuterVoltage
   Y = drain TotalCurrent
```

Full SDevice logs and native `.plt` files remain workspace/debug evidence unless the run is abnormal.

## 5. Extraction / comparison after completion

Use the same extraction procedure already used for nominal G1:

```text
Icrit = 1e-7 A x W/L
W = Wfin = 17 nm
L = Lgate = 20 nm
Icrit = 8.5e-8 A
```

For Coarse / Nominal / Fine compare:

```text
Vth_high
SS over the same subthreshold-current interval
Id at Vg = 2.0 V
whole ID-VG horizontal / vertical shift
Points / Elements
```

First-pass acceptance guideline for `Nominal -> Fine` stability:

```text
|Delta Vth| <= ~10 mV
|Delta SS|  <= ~2 mV/dec
```

These are workflow acceptance guidelines for this reconstruction, not universal TCAD standards.

## 6. Decision path

If Nominal and Fine are stable:

```text
F1 electrical mesh -> acceptable baseline mesh for the feedback comparison
absolute Sun electrical mismatch -> not attributable to ordinary mesh-spacing resolution
next -> stabilized 3-D vs simplified 2-D B0 comparison
```

If Nominal and Fine are not stable:

```text
F1 remains unfrozen
inspect local mesh quality / tiny-edge / high-field regions
revise mesh before any 2-D fidelity conclusion
```

## 7. Current baseline claim boundary

Until F1C/F1F results are ingested:

> `3D-Sun-B0` is a literature-consistent and numerically operational reconstruction, but F1 remains a candidate electrical mesh and exact Sun electrical reproduction is not claimed. H1 and H2 do not explain the large threshold mismatch; mesh convergence is now the active numerical validation step.

## 8. Resume point

When the two runs finish, ingest:

```text
F1C: Points, Elements, ID-VG CSV
F1F: Points, Elements, ID-VG CSV
```

Then compute the three-mesh metric table and decide whether F1 can be frozen for the final `3-D vs 2-D B0` feedback comparison.
