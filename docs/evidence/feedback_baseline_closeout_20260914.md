# FB-BASELINE-01 close-out — 3D reconstruction and simplified-2D fidelity

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Date: 2026-09-14  
> Final status: **Resolved at model-fidelity level**  
> Important boundary: this is **not** a claim of exact Sun et al. electrical reproduction.

## 1. Feedback question

The original feedback question was:

> How closely does the simplified 2-D B0 used in the CMP study reproduce the literature 3-D BCAT electrical characteristics, and how should the 2-D model be used if it does not reproduce the absolute device metrics?

The task was therefore split into two parts:

1. construct a literature-consistent 3-D BCAT reference (`3D-Sun-B0`) from the information actually published by Sun et al.;
2. compare the existing simplified 2-D B0 against that stabilized 3-D reconstruction under a controlled electrical-physics / bias parity condition.

## 2. 3D-Sun-B0 reconstruction completed

Literature-explicit nominal inputs used in the reconstruction include:

```text
Lgate      = 20 nm
Drecess    = 120 nm
DBCAT      = 36 nm
Tox        = 5 nm
Wfin       = 17 nm
Hfin       = 48 nm
Rfillet    = 1.0 nominal reference
Gate WF    = 4.8 eV
Body B     = 1e17 cm^-3
S/D As     = 1e20 cm^-3
Djunction  = 48 nm = 0.40 × Drecess
```

The paper does not publish the complete CAD/process deck. Domain dimensions, exact contact faces, exact lateral S/D straggle, exact mesh, and several 3-D process-mapping details therefore remain reconstruction assumptions and are kept separate from literature-explicit facts.

Completed 3-D checkpoints:

```text
Geometry / coordinate system        PASS / frozen
Contacts                            PASS / frozen
Vertical doping / Djunction         PASS / frozen
Source junction zero-crossing       ~48.0 nm
Drain junction zero-crossing        ~48.0 nm
G0 numerical bring-up               PASS
G1 high-Vd ID-VG                    PASS
G2 low-Vd ID-VG                     PASS
Canali / Caughey-Thomas family map  PASS at model-family level
Threshold-width ambiguity check     cannot explain mismatch
H1 Lgate mapping sensitivity        rejected
H2 GaussFactor 0 -> 0.8             rejected as main cause
Electrical mesh convergence         PASS for DC ID-VG metrics
```

## 3. 3-D electrical checkpoint versus the paper

Using the current reconstruction-defined threshold convention (`W=Wfin=17 nm`, `L=Lgate=20 nm`, `Icrit=8.5e-8 A`) gives:

```text
3D-Sun-B0
Vth_high @ Vd=1.20 V  = 1.14659 V
Vth_low  @ Vd=0.05 V  = 1.20610 V
SS_high                 ≈ 91.17 mV/dec
SS_low                  ≈ 92.83 mV/dec
DIBL_reconstruction     ≈ 51.75 mV/V
Id @ Vg=2 V, Vd=1.2 V  = 1.063365e-5 A
```

Sun et al. nominal reported values are:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

Therefore the 3-D reconstruction is **structurally literature-consistent and numerically stable, but not electrically calibrated to the published nominal values**.

The discrepancy was not force-fitted away because the paper does not publish enough process/device-calibration detail to justify arbitrary adjustment of work function, nominal doping, corner shape, or other parameters solely to hit one reported Vth.

## 4. Reconstruction sensitivities checked before stopping calibration attempts

### H1 — alternative Lgate interpretation

Alternative tested:

```text
baseline: W metal = 20 nm, oxide-outer recess = 30 nm
H1:       W metal = 10 nm, oxide-outer recess = 20 nm
```

Result:

```text
Vth_high = 1.24248 V
SS        ≈ 97.39 mV/dec
```

The alternative moved the result farther from the paper nominal values. It was rejected as the mismatch explanation.

### H2 — lateral Gaussian sensitivity

Alternative tested:

```text
GaussFactor = 0.0 -> 0.8
```

Result:

```text
Vth_high = 1.14634 V
SS        ≈ 91.21 mV/dec
Delta Vth vs nominal ≈ -0.25 mV
```

The effect was negligible compared with the ~0.49 V paper/reconstruction Vth difference. Lateral Gaussian spread was therefore rejected as the dominant mismatch cause.

## 5. Electrical mesh convergence

The nominal F1 mesh was compared with a controlled coarse and fine branch while geometry, contacts, doping, physics, and G1 bias were fixed.

| Mesh | Points | Elements | Vth @ 1.2 V | SS | Id @ Vg=2 V |
|---|---:|---:|---:|---:|---:|
| F1C Coarse | 325741 | 1998482 | 1.14899 V | 91.251 mV/dec | 1.06864e-5 A |
| F1 Nominal | 473004 | 2902876 | 1.14659 V | 91.170 mV/dec | 1.06337e-5 A |
| F1F Fine | 883382 | 5393039 | 1.14541 V | 91.099 mV/dec | 1.06386e-5 A |

Nominal -> Fine change:

```text
Delta Vth     ≈ -1.18 mV
Delta SS      ≈ -0.071 mV/dec
Delta Id(2 V) ≈ +0.046%
```

Decision:

> F1 is accepted / frozen for the present **DC baseline ID-VG / Vth / SS fidelity comparison**.

This freeze does not automatically prove convergence of every local peak-E-field or BTBT scalar; those quantities retain their own mesh-quality guardrails.

## 6. Simplified 2-D B0 parity comparison

The original Run-0 2-D electrical sanity deck used a different physics set and only `Vd=0.05 V`, `Vg=0->1.5 V`, so it was not used directly for the final fidelity judgement.

Instead, the same 2-D geometry (`MEB_Depth=0.036`) was rerun with the same main SDevice physics family and the same high/low drain-bias sweep used by the 3-D reconstruction:

```text
T       = 300 K
WF      = 4.8 eV
Vs      = 0 V
Vsub    = 0 V
Vd      = 1.2 V or 0.05 V
Vg      = 0 -> 2.0 V
Mobility: PhuMob + Lombardi + high-field saturation
BTBT: Hurkx
```

For current-density comparison, the 3-D total current was divided by `Wfin=0.017 um`; the native 2-D terminal current is kept in its width-normalized basis. This is a parity comparison convention, not a claim that the 2-D cross section reproduces the true 3-D conduction perimeter.

### Extracted comparison

| Metric | simplified 2-D B0 | stabilized 3D-Sun-B0 |
|---|---:|---:|
| Vth, high Vd | 1.51879 V | 1.14659 V |
| SS, high Vd | 112.20 mV/dec | 91.17 mV/dec |
| SS, low Vd | 114.29 mV/dec | 92.83 mV/dec |
| Id @ Vg=2 V, high Vd | 4.93641e-5 A/um | 6.25509e-4 A/um equivalent |
| Id @ Vg=2 V, low Vd | 3.74105e-6 A/um | 1.46217e-4 A/um equivalent |

Thus the 3-D reconstruction produces about:

```text
12.67x higher high-Vd Id at Vg=2 V
39.08x higher low-Vd Id at Vg=2 V
```

than the simplified 2-D B0 on the stated width-normalized parity basis.

For the paper-style constant-current threshold in 2-D:

```text
Icrit,2D = 1e-7 / L(um)
         = 5e-6 A/um  for L=0.020 um
```

The high-Vd curve crosses this criterion at:

```text
Vth_high,2D = 1.51879 V
```

but the low-Vd curve reaches only `3.74105e-6 A/um` at `Vg=2.0 V`, so the low-Vd threshold is outside the simulated range:

```text
Vth_low,2D > 2.0 V
```

Therefore, using the same 0.05 / 1.20 V reconstruction bias pair, only a conservative lower bound is reported:

```text
DIBL_2D > 418.4 mV/V
```

The low-current 2-D off-state values include sign changes near the numerical floor, so no formal 2-D Ion/Ioff value is frozen from this parity sweep.

## 7. Final answer to the baseline feedback

**The simplified 2-D B0 does not quantitatively reproduce the literature-oriented 3-D BCAT electrical baseline.** Even after matching the main SDevice physics/bias family, substantial differences remain in Vth, SS, on-current and drain-bias sensitivity.

At the same time, the result does **not** invalidate all existing 2-D CMP sweeps. Their scientifically defensible role is narrower:

> the simplified 2-D model is retained as a controlled comparative model for relative MEB / temperature / process-trend exploration, not as an absolute device-reproduction model.

The 3-D reconstruction is retained as the higher-fidelity validation anchor. Because its absolute calibration to Sun et al. is also incomplete, it is described as a **literature-consistent 3-D reconstruction**, not an exact paper replica.

## 8. Workflow decision for the remaining CMP study

The adopted workflow is:

```text
Literature reference
        ->
3D-Sun-B0 literature-consistent reconstruction
        ->
2D simplified model for broad design-space / DOE exploration
        ->
select baseline + main candidate + boundary/challenger points
        ->
selected-point 3-D validation
        ->
check whether the important 2-D trend / design conclusion survives in 3-D
```

Practical implication:

- use 2-D for the dense MEB / temperature / process-window sweep;
- do not present its absolute Vth / SS / current values as literature reproduction;
- after the effective MEB range is chosen, rerun a small representative set in 3-D;
- the 3-D validation question is **trend preservation and design-decision robustness**, not forced matching of one paper Vth value.

A reasonable selected-point set later is:

```text
36 nm  = baseline reference
~48 nm = main candidate
~49 nm = boundary / challenger
```

The exact final set should follow the completed GIDL + retention + process-window decision, not be frozen solely from this baseline task.

## 9. Claim guardrails

Do not claim:

```text
the Sun 2022 device was exactly reproduced;
the 2-D B0 gives quantitatively correct absolute BCAT characteristics;
F1 is proven converged for every local high-field / BTBT quantity;
DIBL_2D was exactly extracted from the present low-Vd sweep;
```

Supported wording:

> `3D-Sun-B0` is a literature-consistent and DC-mesh-stable 3-D reconstruction. It does not exactly reproduce the paper's absolute electrical calibration. The existing simplified 2-D B0 shows large quantitative differences from the stabilized 3-D reference, so it is used for relative trend / design-space exploration. Final design conclusions are to be checked with selected-point 3-D validation.

## 10. Evidence package

Primary source / execution definitions:

```text
code/sde/baseline_3d_sun_b0/F1_nominal.cmd
code/sde/baseline_3d_sun_b0/VARIANTS.md
code/sdevice/baseline_3d_sun_b0/G0_bringup.cmd
code/sdevice/baseline_3d_sun_b0/G1_highVd_full_idvg.cmd
code/sdevice/baseline_3d_sun_b0/G2_lowVd_full_idvg.cmd
code/sdevice/baseline_3d_sun_b0/B0_2D_parity_highVd.cmd
code/sdevice/baseline_3d_sun_b0/B0_2D_parity_lowVd.cmd
```

Primary data:

```text
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

Supporting evidence:

```text
docs/evidence/feedback_baseline_3d_reconstruction_20260911.md
docs/evidence/baseline_3d_extraction_physics_verification_20260913.md
docs/evidence/baseline_3d_h1_h2_sensitivity_20260913.md
docs/evidence/baseline_3d_mesh_convergence_plan_20260913.md
assets/images/feedback/20260911_baseline/
```

Full Sentaurus logs and native `.plt` files remain workspace/debug evidence under the repository's existing lightweight-evidence policy.
