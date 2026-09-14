# 3D-Sun-B0 electrical mesh-convergence result

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Date: 2026-09-14  
> Status: **PASS for baseline DC ID–VG comparison**

## 1. Controlled setup

The Coarse / Nominal / Fine branches use the same nominal `3D-Sun-B0` geometry, contacts, doping mapping, work function, and SDevice physics/bias conditions. H1 and H2 reconstruction changes are not carried into this comparison.

```text
T = 300 K
Vs = 0 V
Vsub = 0 V
Vd = 1.2 V
Vg = 0 -> 2.0 V
WF = 4.8 eV
GaussFactor = 0.0
```

Only the mesh spacing is changed:

```text
F1C Coarse  = 1.25 x nominal spacing
F1 Nominal  = 1.00 x
F1F Fine    = 0.80 x nominal spacing
```

## 2. Mesh sizes and extracted electrical metrics

The same provisional threshold extraction used for G1 is retained:

```text
Icrit = 1e-7 A x W/L
W = Wfin = 17 nm
L = Lgate = 20 nm
Icrit = 8.5e-8 A
```

Threshold is obtained by log-current interpolation, and SS is fitted over the same `1e-13` to `1e-10 A` rising-current interval.

| Mesh | Points | Elements | Vth_high (V) | SS (mV/dec) | Id @ Vg=2 V (A) |
|---|---:|---:|---:|---:|---:|
| F1C Coarse | 325,741 | 1,998,482 | 1.14899 | 91.251 | 1.06864e-5 |
| F1 Nominal | 473,004 | 2,902,876 | 1.14659 | 91.170 | 1.06337e-5 |
| F1F Fine | 883,382 | 5,393,039 | 1.14541 | 91.099 | 1.06386e-5 |

Relative to Nominal:

```text
Coarse - Nominal
  Delta Vth = +2.40 mV
  Delta SS  = +0.081 mV/dec
  Delta Id(2V) = +0.496%

Fine - Nominal
  Delta Vth = -1.18 mV
  Delta SS  = -0.071 mV/dec
  Delta Id(2V) = +0.046%

Fine - Coarse
  Delta Vth = -3.57 mV
  Delta SS  = -0.152 mV/dec
  Delta Id(2V) = -0.447%
```

## 3. Decision

The predeclared first-pass acceptance guideline was:

```text
|Delta Vth| Nominal -> Fine <= ~10 mV
|Delta SS|  Nominal -> Fine <= ~2 mV/dec
```

Observed values are much smaller:

```text
|Delta Vth| = 1.18 mV
|Delta SS|  = 0.071 mV/dec
```

Therefore:

> **F1 Nominal is mesh-stable for the present baseline DC ID–VG comparison and can be frozen for the `3D-Sun-B0` vs simplified 2-D B0 fidelity comparison.**

The large absolute mismatch with the Sun et al. nominal electrical values is therefore not attributable to ordinary mesh-spacing resolution over the tested range.

## 4. Important scope boundary

This convergence result applies to the reported **DC transfer metrics** (`Vth`, SS, high-Vd `Id-Vg`, and `Id@2V`) under the current baseline reconstruction.

It does **not** prove that the same mesh is universally converged for local peak electric field, BTBT/GIDL hotspot magnitude, or every future high-field extraction. The previously observed nominal-mesh quality caveat (including very small local edges / obtuse tetrahedra in SDevice diagnostics) remains relevant if later claims depend on local peak-field accuracy.

Therefore the correct status is:

```text
F1 for baseline DC electrical comparison  = FROZEN / ACCEPTED
F1 for universal local-field/BTBT claims  = NOT ESTABLISHED by this test
```

## 5. Committed data

```text
data/baseline_3d_sun_b0/f1c_coarse_idvg_highvd.csv
data/baseline_3d_sun_b0/g1_idvg_highvd_1p2V_to_2p0V.csv
data/baseline_3d_sun_b0/f1f_fine_idvg_highvd.csv
data/baseline_3d_sun_b0/f1_mesh_convergence_summary_20260914.csv
```

## 6. Baseline-feedback implication

Completed root-cause / numerical checks now include:

```text
threshold-width interpretation          ruled out as main cause
Canali / Caughey-Thomas naming          compatible at model-family level
H1 Lgate mapping alternative            rejected
H2 lateral Gaussian factor sensitivity  rejected as main cause
F1 electrical mesh-spacing sensitivity  PASS / stable
```

The remaining absolute electrical-calibration difference should be documented as a reconstruction limitation tied to unpublished process/device-calibration and 3-D mapping details, rather than fitted away with arbitrary nominal-parameter tuning.

## 7. Next step

Proceed to the original feedback question:

```text
stabilized literature-consistent 3D-Sun-B0
vs
simplified 2-D CMP B0
```

Compare the electrical metrics that can be extracted under a transparent common convention, then state explicitly which aspects of the 2-D baseline are suitable for relative MEB-trend work and which absolute 3-D characteristics it does not reproduce.
