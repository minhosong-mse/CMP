# 3D-Sun-B0 baseline evidence manifest — synchronized 2026-09-14

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Reconstruction: `3D-Sun-B0`  
> Current stage: **baseline-fidelity feedback closed at model-fidelity level**

## 1. Purpose

This manifest records the committed evidence for the literature-consistent 3-D BCAT reconstruction and the final simplified-2-D-vs-3-D fidelity check.

The target is a defensible reconstruction of Sun et al. (Micromachines 2022, 13, 1476), not an exact reverse-engineered process/CAD deck.

## 2. Completed reconstruction checkpoints

```text
A   literature truth table              DONE
B   coordinate system                   PASS / FROZEN
C   geometry v05                        PASS / FROZEN
D   contacts                            PASS / FROZEN
E   nominal vertical doping             PASS / FROZEN
F0  doping-QA mesh                      PASS
F1  nominal electrical mesh             PASS for DC ID-VG metrics / FROZEN for baseline comparison
G0  low-Vd bring-up                     PASS
G1  high-Vd full ID-VG                  PASS
G2  low-Vd full ID-VG                   PASS
H1  Lgate mapping sensitivity           DONE / rejected as mismatch explanation
H2  lateral Gaussian sensitivity        DONE / rejected as main mismatch explanation
F1C/F1/F1F mesh convergence             PASS
2D B0 parity high/low sweeps            PASS
FB-BASELINE-01                          RESOLVED at model-fidelity level
```

Source and drain vertical net-doping cuts both cross the signed net-doping zero point at approximately `48.0 nm`, matching the nominal vertical `Djunction=48 nm` reconstruction target.

## 3. 3-D electrical checkpoint

Current nominal reconstruction:

```text
Vth_high @ Vd=1.20 V = 1.14659 V
Vth_low  @ Vd=0.05 V = 1.20610 V
SS_high                 ≈ 91.17 mV/dec
SS_low                  ≈ 92.83 mV/dec
reconstruction DIBL     ≈ 51.75 mV/V
Id @ Vg=2 V, Vd=1.2 V  = 1.063365e-5 A
```

Paper nominal targets:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

The exact low/high drain-bias pair used by the paper for DIBL is not explicitly published in the text, so the present `51.75 mV/V` remains a reconstruction-defined comparison rather than a strict paper-equivalent DIBL extraction.

## 4. Interpretation checks completed

### Threshold-width convention

Reasonable 3-D width interpretations do not move the extracted threshold toward the paper `0.656 V`; matching that value on the current curve would require an unphysical equivalent width. Width-definition ambiguity is therefore not treated as the dominant cause of the ~0.49 V mismatch.

### Canali / Caughey-Thomas naming

The active `e/hHighFieldSaturation(GradQuasiFermi)` setup is compatible with the Sentaurus Canali/Caughey-Thomas high-field model family. The naming difference in the T-2022.03 log is not treated as evidence that a different high-field model was selected. Exact paper parameter overrides remain unpublished.

### H1 — Lgate mapping

```text
baseline: W metal = 20 nm, oxide-outer recess = 30 nm
H1:       W metal = 10 nm, oxide-outer recess = 20 nm
Vth_high = 1.24248 V
SS        ≈ 97.39 mV/dec
```

Decision: rejected as an explanation of the paper mismatch because the result moved farther from the reported nominal values.

### H2 — lateral Gaussian spread

```text
GaussFactor = 0.0 -> 0.8
Vth_high = 1.14634 V
SS        ≈ 91.21 mV/dec
Delta Vth vs nominal ≈ -0.25 mV
```

Decision: rejected as the main cause of the large electrical mismatch.

## 5. Electrical mesh convergence — completed

| Mesh | Points | Elements | Vth @ 1.2 V | SS | Id @ Vg=2 V |
|---|---:|---:|---:|---:|---:|
| F1C Coarse | 325741 | 1998482 | 1.14899 V | 91.251 mV/dec | 1.06864e-5 A |
| F1 Nominal | 473004 | 2902876 | 1.14659 V | 91.170 mV/dec | 1.06337e-5 A |
| F1F Fine | 883382 | 5393039 | 1.14541 V | 91.099 mV/dec | 1.06386e-5 A |

Nominal -> Fine:

```text
Delta Vth     ≈ -1.18 mV
Delta SS      ≈ -0.071 mV/dec
Delta Id(2 V) ≈ +0.046%
```

Decision:

> F1 is accepted / frozen for the present **DC ID-VG / Vth / SS baseline-fidelity comparison**.

This does not extend to a universal claim of convergence for every local peak-field or BTBT quantity.

## 6. Simplified 2-D B0 parity comparison — completed

The original Run-0 electrical sanity deck was not used directly because its physics set and sweep range differed from the stabilized 3-D baseline.

Instead, the same simplified 2-D geometry (`MEB_Depth=0.036`) was rerun with the same main SDevice physics family and the same high/low drain-bias sweep used by the 3-D reconstruction.

For the parity comparison, the 3-D total current is divided by `Wfin=0.017 um`; the native 2-D current is retained in its width-normalized basis.

| Metric | simplified 2-D B0 | stabilized 3D-Sun-B0 |
|---|---:|---:|
| Vth, high Vd | 1.51879 V | 1.14659 V |
| SS, high Vd | 112.20 mV/dec | 91.17 mV/dec |
| SS, low Vd | 114.29 mV/dec | 92.83 mV/dec |
| Id @ Vg=2 V, high Vd | 4.93641e-5 A/um | 6.25509e-4 A/um equivalent |
| Id @ Vg=2 V, low Vd | 3.74105e-6 A/um | 1.46217e-4 A/um equivalent |

The 2-D high-Vd threshold criterion is crossed at `1.51879 V`, while the low-Vd curve does not reach the same criterion by `Vg=2.0 V`.

Therefore only a conservative lower bound is frozen for the 2-D DIBL under the same reconstruction bias pair:

```text
DIBL_2D > 418.4 mV/V
```

No formal 2-D Ion/Ioff value is frozen from this parity sweep because the very-low-current 2-D off-state region contains sign changes near the numerical floor.

## 7. Final baseline-feedback conclusion

> The simplified 2-D B0 does not quantitatively reproduce the literature-oriented 3-D BCAT electrical baseline. It remains useful as a controlled comparative model for relative MEB / temperature / process-trend exploration, but not as an absolute device-reproduction model.

`3D-Sun-B0` is retained as a higher-fidelity validation anchor, with the explicit limitation that its absolute electrical calibration to Sun et al. is also incomplete because the paper does not publish all process/device-calibration details.

Adopted downstream workflow:

```text
Literature reference
  -> literature-consistent 3-D reconstruction
  -> broad 2-D design-space / DOE exploration
  -> select baseline + main candidate + boundary/challenger points
  -> selected-point 3-D validation
  -> confirm whether the 2-D trend / design conclusion survives in 3-D
```

The selected-point 3-D validation objective is **trend preservation and design-decision robustness**, not forced matching of one paper Vth value.

## 8. Primary committed source decks

```text
code/sde/baseline_3d_sun_b0/F1_nominal.cmd
code/sde/baseline_3d_sun_b0/VARIANTS.md
code/sdevice/baseline_3d_sun_b0/G0_bringup.cmd
code/sdevice/baseline_3d_sun_b0/G1_highVd_full_idvg.cmd
code/sdevice/baseline_3d_sun_b0/G2_lowVd_full_idvg.cmd
code/sdevice/baseline_3d_sun_b0/B0_2D_parity_highVd.cmd
code/sdevice/baseline_3d_sun_b0/B0_2D_parity_lowVd.cmd
```

## 9. Primary committed data

```text
data/baseline_3d_sun_b0/junction_source_C1.csv
data/baseline_3d_sun_b0/junction_drain_C2.csv
data/baseline_3d_sun_b0/g0_idvg_lowvd_0p05V_to_1p2V.csv
data/baseline_3d_sun_b0/g1_idvg_highvd_1p2V_to_2p0V.csv
data/baseline_3d_sun_b0/g2_idvg_lowvd_0p05V_to_2p0V.csv
data/baseline_3d_sun_b0/h1_idvg_highvd_lgate_outer20nm.csv
data/baseline_3d_sun_b0/h2_gaussfactor0p8_idvg_highvd.csv
data/baseline_3d_sun_b0/f1c_coarse_idvg_highvd.csv
data/baseline_3d_sun_b0/f1f_fine_idvg_highvd.csv
data/baseline_3d_sun_b0/f1_mesh_convergence_summary_20260914.csv
data/baseline_3d_sun_b0/b0_2d_parity_highvd.csv
data/baseline_3d_sun_b0/b0_2d_parity_lowvd.csv
data/baseline_3d_sun_b0/baseline_2d_3d_fidelity_summary_20260914.csv
data/baseline_3d_sun_b0/baseline_feedback_manifest_20260914.csv
```

## 10. Primary documentation

```text
docs/evidence/feedback_baseline_3d_reconstruction_20260911.md
docs/evidence/baseline_3d_extraction_physics_verification_20260913.md
docs/evidence/baseline_3d_h1_h2_sensitivity_20260913.md
docs/evidence/baseline_3d_mesh_convergence_plan_20260913.md
docs/evidence/feedback_baseline_closeout_20260914.md
assets/images/feedback/20260911_baseline/
```

The main `README.md` remains intentionally untouched until the principal presentation-feedback items are synthesized together.

## 11. Repository evidence policy

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

## 12. Claim guardrail

Supported wording:

> `3D-Sun-B0` is a literature-consistent and DC-mesh-stable 3-D reconstruction. It does not exactly reproduce the paper's absolute electrical calibration. The simplified 2-D B0 shows large quantitative differences from the stabilized 3-D reference, so it is retained for relative trend / design-space exploration. Final design conclusions are to be checked with selected-point 3-D validation.
