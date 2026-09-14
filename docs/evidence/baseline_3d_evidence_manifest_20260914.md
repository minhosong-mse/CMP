# 3D-Sun-B0 baseline evidence manifest — 2026-09-14

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Reconstruction: `3D-Sun-B0`  
> Current stage: **baseline DC mesh convergence closed; 2-D fidelity comparison next**

## Validated / frozen checkpoints

```text
Literature truth table                  DONE
Coordinate / geometry / contacts        PASS / FROZEN
Nominal vertical doping                 PASS / FROZEN
Source + drain Djunction                48.0 nm PASS
G0 low-Vd bring-up                      PASS
G1 high-Vd full ID-VG                   PASS
G2 low-Vd full ID-VG                    PASS
Threshold-width ambiguity check         DONE — not main cause
Canali / Caughey-Thomas model map       DONE — compatible at model-family level
H1 Lgate mapping sensitivity            DONE — rejected
H2 GaussFactor 0.8 sensitivity          DONE — rejected as main cause
F1 Coarse/Nominal/Fine DC convergence   PASS
F1 nominal mesh for DC baseline         FROZEN / ACCEPTED
Exact Sun electrical reproduction       NOT CLAIMED
```

## Nominal electrical checkpoint

```text
Vth_high @ Vd=1.20 V = 1.14659 V
Vth_low  @ Vd=0.05 V = 1.20610 V
SS_high                 ≈ 91.17 mV/dec
SS_low                  ≈ 92.83 mV/dec
reconstruction DIBL     ≈ 51.75 mV/V
```

Sun et al. nominal values:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

The reconstruction remains literature-consistent but not electrically calibrated to the unpublished original deck.

## DC mesh convergence

| Mesh | Relative spacing | Points | Elements | Vth_high (V) | SS (mV/dec) | Id @ 2 V (A) |
|---|---:|---:|---:|---:|---:|---:|
| F1C Coarse | 1.25x | 325741 | 1998482 | 1.14899 | 91.251 | 1.0686352e-5 |
| F1 Nominal | 1.00x | 473004 | 2902876 | 1.14659 | 91.170 | 1.0633650e-5 |
| F1F Fine | 0.80x | 883382 | 5393039 | 1.14541 | 91.099 | 1.0638591e-5 |

Nominal -> Fine:

```text
Delta Vth     = -1.18 mV
Delta SS      = -0.071 mV/dec
Delta Id(2 V) = +0.046%
```

This passes the predefined first-pass DC guideline and freezes F1 for the present baseline transfer-characteristic comparison. It does not prove universal convergence for local peak-field or BTBT/GIDL hotspot quantities.

## Repository evidence

```text
code/sde/baseline_3d_sun_b0/F1_nominal.cmd
code/sde/baseline_3d_sun_b0/generate_variants.py
code/sde/baseline_3d_sun_b0/VARIANTS.md
code/sdevice/baseline_3d_sun_b0/

data/baseline_3d_sun_b0/g1_idvg_highvd_1p2V_to_2p0V.csv
data/baseline_3d_sun_b0/g2_idvg_lowvd_0p05V_to_2p0V.csv
data/baseline_3d_sun_b0/h1_idvg_highvd_lgate_outer20nm.csv
data/baseline_3d_sun_b0/h2_gaussfactor0p8_idvg_highvd.csv
data/baseline_3d_sun_b0/f1c_coarse_idvg_highvd.csv
data/baseline_3d_sun_b0/f1f_fine_idvg_highvd.csv
data/baseline_3d_sun_b0/f1_mesh_convergence_summary_20260914.csv

docs/evidence/baseline_3d_h1_h2_sensitivity_20260913.md
docs/evidence/baseline_3d_mesh_convergence_result_20260914.md
docs/evidence/baseline_3d_resume_checkpoint_20260914.md
```

## Next step / resume point

The next rigorous task is no longer 3-D parameter tuning. It is the original feedback question:

```text
stabilized literature-consistent 3D-Sun-B0
vs
simplified 2-D CMP B0
```

Before making a quantitative fidelity claim, ensure the 2-D electrical run uses a physics/bias protocol that is comparable to the stabilized 3-D run. The historical Run-0 2-D ID-VG deck was a low-Vd sanity deck and used a different mobility/recombination model set, so its raw curve should not be treated as a strict apples-to-apples electrical comparison without a parity run.

Main README remains intentionally untouched until the principal feedback set is synthesized.
