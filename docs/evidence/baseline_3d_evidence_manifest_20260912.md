# 3D-Sun-B0 baseline evidence manifest — synchronized 2026-09-13

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Reconstruction: `3D-Sun-B0`  
> Current stage: **H1/H2 sensitivity closed; electrical mesh convergence running**

## 1. Purpose

This manifest records the committed evidence for the literature-consistent 3-D BCAT reconstruction used to answer the baseline-fidelity feedback. The target is a defensible reconstruction of Sun et al. (Micromachines 2022, 13, 1476), not a claim of exact reverse engineering of unpublished process/CAD details.

## 2. Frozen / validated reconstruction checkpoints

```text
A   literature truth table          DONE
B   coordinate system               PASS / FROZEN
C   geometry v05                    PASS / FROZEN
D   contacts                        PASS / FROZEN
E   nominal vertical doping         PASS / FROZEN
F0  doping-QA mesh                  PASS
F1  nominal electrical mesh         BUILD PASS / CANDIDATE
G0  low-Vd bring-up                 PASS
G1  high-Vd full ID-VG              PASS
G2  low-Vd full ID-VG               PASS
```

Source and drain vertical net-doping cuts both cross the signed net-doping zero point at approximately `48.0 nm`, matching the nominal vertical `Djunction = 0.40 × 120 nm` target.

## 3. Literature-electrical checkpoint

Current nominal reconstruction:

```text
Vth_high @ Vd=1.20 V = 1.14659 V
Vth_low  @ Vd=0.05 V = 1.20610 V
SS_high                 ≈ 91.17 mV/dec
SS_low                  ≈ 92.83 mV/dec
reconstruction DIBL     ≈ 51.75 mV/V
```

Paper nominal targets:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

The paper does not explicitly publish the exact low/high drain-bias pair used for its DIBL value, so the current `51.75 mV/V` remains a reconstruction-defined comparison rather than a strict paper-equivalent DIBL extraction.

## 4. Post-G2 interpretation checks completed

### 4.1 Threshold-width interpretation

The paper gives `Icrit = 1e-7 A × W/L`, but does not fully document the numerical 3-D saddle-fin width convention. The reasonable width-sensitivity checks do not move the reconstructed threshold toward `0.656 V`; matching the paper threshold on the current G1 curve would require an unphysical equivalent width. Therefore width-definition ambiguity is not treated as the dominant cause of the ~0.49 V mismatch.

### 4.2 Canali / Caughey-Thomas naming

The active `e/hHighFieldSaturation(GradQuasiFermi)` setup is compatible with the Sentaurus Canali/Caughey-Thomas high-field model family. The naming difference in the T-2022.03 log is not treated as evidence that a different high-field model was selected. Exact paper parameter overrides remain unpublished.

Detailed evidence:

```text
docs/evidence/baseline_3d_extraction_physics_verification_20260913.md
```

## 5. Reconstruction sensitivities completed

### H1 — Lgate lateral mapping

Alternative tested:

```text
baseline: W metal = 20 nm, oxide-outer recess = 30 nm
H1:       W metal = 10 nm, oxide-outer recess = 20 nm
```

Result:

```text
Vth_high = 1.24248 V
SS        ≈ 97.39 mV/dec
Id(2 V)   ≈ 8.230e-6 A
```

Decision: **reject as an explanation of the paper mismatch** because it moves Vth/SS farther from the paper nominal values.

### H2 — lateral Gaussian spread

Alternative tested:

```text
GaussFactor = 0.0 -> 0.8
```

`0.8` is a sensitivity bracket, not a Sun-2022 literature value.

Result:

```text
Vth_high = 1.14634 V
SS        ≈ 91.21 mV/dec
Id(2 V)   = 1.0643355e-5 A
```

Relative to nominal G1:

```text
Delta Vth     ≈ -0.25 mV
Delta SS      ≈ +0.04 mV/dec
Delta Id(2 V) ≈ +0.09%
```

Decision: **reject as the main cause of the large electrical mismatch**.

Evidence:

```text
docs/evidence/baseline_3d_h1_h2_sensitivity_20260913.md
data/baseline_3d_sun_b0/h1_idvg_highvd_lgate_outer20nm.csv
data/baseline_3d_sun_b0/h1_lgate_mapping_validation_summary.txt
data/baseline_3d_sun_b0/h2_gaussfactor0p8_idvg_highvd.csv
data/baseline_3d_sun_b0/h1_h2_sensitivity_summary_20260913.csv
code/sde/baseline_3d_sun_b0/VARIANTS.md
```

## 6. Exact SDE-source archival status

The exact final nominal F1 source is now archived at:

```text
code/sde/baseline_3d_sun_b0/F1_nominal.cmd
```

The controlled H1/H2 and mesh-branch changes are recorded relative to that exact nominal source at:

```text
code/sde/baseline_3d_sun_b0/VARIANTS.md
```

This avoids reconstructing unpublished or executed settings from logs alone.

## 7. Active step — Coarse / Nominal / Fine electrical mesh convergence

The active convergence comparison returns to the nominal reconstruction (`GaussFactor=0.0`; H1/H2 changes are not carried forward).

```text
F1C Coarse  = 1.25 × nominal spacing  -> launched / result pending
F1 Nominal  = 1.00 ×                  -> completed / candidate reference
F1F Fine    = 0.80 × nominal spacing  -> launched / result pending
```

All branches use the unchanged G1 electrical condition:

```text
T = 300 K
Vd = 1.2 V
Vg = 0 -> 2.0 V
Vs = 0 V
Vsub = 0 V
WF = 4.8 eV
```

Result package required for F1C and F1F:

```text
Points / Elements
ID-VG CSV: gate OuterVoltage vs drain TotalCurrent
```

Full SDevice logs and native `.plt` files remain workspace/debug evidence unless the run is abnormal.

Detailed plan:

```text
docs/evidence/baseline_3d_mesh_convergence_plan_20260913.md
```

## 8. Repository evidence policy

Commit by default:

```text
executed / controlled source definitions
validated CSV data
compact build/run summaries
curated figures used as evidence
feedback / evidence documentation
```

Keep in chat/workspace unless specifically needed:

```text
full Sentaurus logs
native .plt files
temporary screenshots
failed attempts
```

## 9. Primary repository locations

```text
code/sde/baseline_3d_sun_b0/
code/sdevice/baseline_3d_sun_b0/
data/baseline_3d_sun_b0/
assets/images/feedback/20260911_baseline/
docs/evidence/feedback_baseline_3d_reconstruction_20260911.md
docs/evidence/baseline_3d_extraction_physics_verification_20260913.md
docs/evidence/baseline_3d_h1_h2_sensitivity_20260913.md
docs/evidence/baseline_3d_mesh_convergence_plan_20260913.md
```

The main `README.md` remains intentionally untouched until the principal presentation-feedback items are synthesized together.

## 10. Resume point

```text
G0/G1/G2                               DONE
threshold-width check                  DONE
Canali/CT model-family check           DONE
H1 Lgate mapping sensitivity           DONE — rejected as mismatch explanation
H2 lateral Gaussian sensitivity        DONE — rejected as main mismatch cause
F1C Coarse electrical mesh             RUNNING / result pending
F1 Nominal electrical mesh             candidate reference
F1F Fine electrical mesh               RUNNING / result pending
3-D baseline mesh freeze               PENDING convergence result
2-D vs stabilized 3-D comparison       PENDING
FB-BASELINE-01 close                   PENDING
```

When F1C/F1F finish, ingest Points/Elements and the two ID-VG CSVs, compute the three-mesh `Vth / SS / Id(2V)` table, then decide whether F1 can be frozen for the final simplified-2D-vs-3D fidelity comparison.

## 11. Current claim guardrail

Supported wording:

> `3D-Sun-B0` is a literature-consistent 3-D reconstruction with validated geometry/contact/vertical-doping checkpoints and completed G0/G1/G2 electrical operation. Reasonable threshold-width interpretation, an alternative Lgate mapping, and a large lateral-Gaussian sensitivity do not explain the large absolute Vth mismatch with Sun et al. Electrical mesh convergence is now being checked before the reconstruction is frozen and compared directly with the simplified 2-D B0. Exact paper electrical reproduction is not claimed.
