# 3D-Sun-B0 baseline evidence manifest — 2026-09-12

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Reconstruction: `3D-Sun-B0`  
> Last synchronized: 2026-09-13  
> Audit status: **G0/G1/G2 PASS; extraction-width and Canali/Caughey-Thomas mapping verification completed**

## 1. Purpose

This manifest records what has actually been committed for the dedicated literature-consistent 3-D BCAT baseline reconstruction and separates repository evidence from artifacts that remain only in the conversation / Sentaurus workspace.

The target is a literature-consistent reconstruction of Sun et al. (Micromachines 2022, 13, 1476), not an undocumented claim of exact reverse engineering.

## 2. Visual evidence now committed

Browsable reconstruction contact sheet:

```text
assets/images/feedback/20260911_baseline/00_baseline_visual_contact_sheet.svg
```

G1/G2 transfer-curve comparison generated from validated CSV data:

```text
assets/images/feedback/20260911_baseline/01_g1_g2_idvg_comparison.svg
```

The contact sheet summarizes the reconstruction checkpoints used for geometry, XZ/YZ sections, contacts, doping / junction cuts, F1 mesh, and source/drain junction-depth verification.

The original higher-resolution screenshots remain workspace evidence and can be re-exported later if needed.

## 3. Directly browsable quantitative data

Repository directory:

```text
data/baseline_3d_sun_b0/
```

Committed curve / junction / extraction data:

```text
g0_idvg_lowvd_0p05V_to_1p2V.csv
g1_idvg_highvd_1p2V_to_2p0V.csv
g2_idvg_lowvd_0p05V_to_2p0V.csv
junction_source_C1.csv
junction_drain_C2.csv
extraction_width_sensitivity_20260913.csv
```

The source and drain vertical net-doping profiles both cross the signed net-doping zero point at approximately:

```text
Distance = 0.048 um = 48.0 nm
```

This validates the nominal **vertical** `Djunction = 0.40 × 120 nm` reconstruction target. It does not validate the unpublished lateral S/D diffusion profile.

## 4. Compact execution / validation evidence

The repository follows the same lightweight pattern already used in the CMP runs: executable source decks, CSV data, compact summaries, and curated figures/docs are committed; full Sentaurus logs and native `.plt` files remain workspace/debug evidence unless a later diagnosis specifically requires them.

Current compact summaries:

```text
data/baseline_3d_sun_b0/f1_sde_build_summary.txt
data/baseline_3d_sun_b0/g0_sdevice_run_summary.txt
data/baseline_3d_sun_b0/g1_sdevice_run_summary.txt
data/baseline_3d_sun_b0/g2_curve_validation_summary.txt
```

Detailed post-G2 verification:

```text
docs/evidence/baseline_3d_extraction_physics_verification_20260913.md
```

### F1 build checkpoint

```text
geometry / contact overlap checks = clean
source / drain / substrate / gate contact assignment = #t
body / source / drain doping definitions and placements = #t
F1 refinement definitions / placements = #t
save-model = #t
build-mesh = #t
SVisual points = 473004
SDevice tetrahedrons = 2773380
```

F1 remains an electrical mesh **candidate**, not a convergence-frozen production mesh.

### G0 checkpoint

```text
T = 300 K
Vd = 0.05 V
Vg = 0 → 1.2 V
Id(Vg=1.2 V) = 7.769e-8 A
G0 = PASS
```

Purpose: numerical / contact / physics / turn-on sanity validation, not final paper-metric extraction.

### G1 checkpoint

```text
T = 300 K
Vd = 1.2 V
Vg = 0 → 2.0 V
Id(Vg=2.0 V) = 1.063365e-5 A
G1 = PASS
```

Current provisional extraction:

```text
SS, 1e-13~1e-10 A fit ≈ 91.17 mV/dec
max(Id)/min(Id)        ≈ 3.04e9
Vth_high*              ≈ 1.14659 V
```

### G2 checkpoint

Returned SVisual/CSV data reach the full `Vg = 2.0 V` endpoint with a smooth ID–VG curve.

```text
T = 300 K
Vd = 0.05 V
Vg = 0 → 2.0 V
Id minimum = 1.0147335e-17 A @ Vg=0.1395599 V
Id(Vg=2.0 V) = 2.48569e-6 A
SS, 1e-13~1e-10 A fit ≈ 92.83 mV/dec
G2 curve ingestion = PASS
```

Using the same **provisional** constant-current convention currently used for G1:

```text
Icrit = 1e-7 A × W/L
W = Wfin = 17 nm
L = Lgate = 20 nm
Icrit = 8.5e-8 A
```

and log-current interpolation between adjacent gate-sweep points:

```text
Vth_low  (Vd=0.05 V) = 1.20610 V
Vth_high (Vd=1.20 V) = 1.14659 V
reconstruction-defined DIBL
= (Vth_low - Vth_high)/(1.20 - 0.05)
= 51.75 mV/V
```

Paper nominal targets remain:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

Important extraction boundary:

- the paper text reports the nominal DIBL value but does **not** explicitly publish the exact low/high drain-bias pair used for DIBL extraction;
- therefore `51.75 mV/V` is a **reconstruction-defined provisional DIBL**, not yet a strict paper-equivalent value;
- the present 3-D deck is numerically operational but electrical reproduction is not yet demonstrated.

## 5. Post-G2 extraction-width verification

The paper states `Icrit = 1e-7 A × W/L` but does not explicitly define the numerical channel-width convention for the 3-D saddle-fin extraction.

A sensitivity check was performed using the same validated G1/G2 curves.

Primary interpretation:

```text
W = Wfin = 17 nm
Vth_high = 1.14659 V
Vth_low  = 1.20610 V
```

Larger three-surface fin-width sensitivity bound:

```text
W = 2Hfin + Wfin = 113 nm
Vth_high = 1.27410 V
Vth_low  = 1.36562 V
```

A larger width raises the constant-current threshold criterion and therefore moves the extracted Vth even farther from the paper nominal `0.656 V`.

At `Vg = 0.656 V`, the G1 current is approximately `9.34e-13 A`. For that current to satisfy the paper constant-current formula with `L=20 nm`, the implied width would be approximately `1.87e-4 nm`, which is not a physically meaningful channel-width interpretation.

Therefore:

> **channel-width extraction ambiguity cannot plausibly explain the present ~0.49 V Vth mismatch.**

The exact paper convention is still unresolved for formal reporting, but it is no longer treated as a leading mismatch cause.

## 6. Canali / Caughey-Thomas high-field mapping checkpoint

Sun et al. explicitly state that the Canali model was used for carrier velocity saturation.

The current T-2022.03 SDevice run log reports the activated electron/hole high-field model as:

```text
Caughey-Thomas saturation model,
using gradient quasi-Fermi potential
```

Sentaurus documentation/training describes the built-in high-field saturation model as the **Canali** model, uses `HighFieldSaturation(GradQuasiFermi)` for it, and documents the carrier-specific `eHighFieldSaturation` / `hHighFieldSaturation` forms used in the current deck. Sentaurus documentation also describes the default Canali implementation as being based on the Caughey-Thomas formulation.

Therefore:

> **the Caughey-Thomas wording in the log is compatible with the Sentaurus Canali high-field model family and is not evidence of a different physics model being selected.**

This item is considered **resolved at model-family / activation level**.

Remaining limitation:

- the paper does not publish its exact Sentaurus release or numerical high-field parameter overrides;
- exact parameter-by-parameter equivalence therefore cannot be proven.

The Canali/Caughey-Thomas naming issue is no longer a leading explanation for the electrical mismatch.

## 7. Executable SDevice decks committed

```text
code/sdevice/baseline_3d_sun_b0/
```

contains:

```text
G0_bringup.cmd
G1_highVd_full_idvg.cmd
G2_lowVd_full_idvg.cmd
README.md
```

Status:

```text
G0 deck = executed / PASS
G1 deck = executed / PASS
G2 deck = executed / returned curve ingested PASS
```

## 8. Exact SDE source status

The final F1 SDE build execution evidence is preserved through the compact checkpoint summary, but the exact final standalone SDE source CMD was not available as a separately uploaded artifact during this audit.

It is intentionally **not reconstructed from the execution log and mislabeled as exact source**.

Remaining archival action:

```text
export the original final 3D-Sun-B0 SDE source CMD from the Sentaurus workspace
→ commit it under a dedicated 3-D baseline SDE directory
```

This source file is now the immediate prerequisite for a controlled S/D reconstruction sensitivity study.

## 9. Revised remaining work before `FB-BASELINE-01` closes

1. archive the exact final F1 SDE source CMD;
2. run a controlled **lateral S/D Gaussian sensitivity** test with geometry, vertical junction target, work function, mesh policy, and SDevice physics otherwise fixed;
3. if lateral spread alone does not resolve the direction/magnitude of mismatch, test source/drain-side **3-D corner rounding / effective-channel geometry** as a separate variable;
4. freeze the final reporting convention for Ion/Ioff and retain the published-DIBL bias-pair limitation explicitly;
5. perform coarse / nominal / fine electrical mesh convergence before freezing F1;
6. compare stabilized `3D-Sun-B0` metrics directly with the simplified 2-D CMP B0.

Do not tune work function or nominal doping merely to force agreement.

Any nonzero `GaussFactor` value is a **reconstruction sensitivity parameter**, not a Sun-2022 literature value. Sentaurus training examples use nonzero lateral diffusion factors (for example 0.8), but those examples are not evidence for the BCAT device under study.

## 10. Resume point

Next session should resume from:

```text
G0/G1/G2 ID-VG                              DONE
provisional low/high Vth + DIBL             DONE
Vth width-artifact check                    DONE — cannot explain mismatch
Canali/Caughey-Thomas model-family mapping  DONE — compatible
exact F1 SDE source archival                OPEN — immediate prerequisite
lateral S/D Gaussian sensitivity            OPEN — next simulation
S/D-side 3-D geometry sensitivity           OPEN — conditional next
mesh convergence                            OPEN
2-D vs stabilized 3-D fidelity comparison   OPEN
```

## 11. Feedback-hub synchronization state

Current baseline evidence is distributed across:

```text
docs/FEEDBACK_LOG.md
docs/TASK_HUB.md
docs/evidence/feedback_baseline_3d_reconstruction_20260911.md
docs/evidence/baseline_3d_evidence_manifest_20260912.md
docs/evidence/baseline_3d_extraction_physics_verification_20260913.md
assets/images/feedback/20260911_baseline/
data/baseline_3d_sun_b0/
code/sdevice/baseline_3d_sun_b0/
```

The main `README.md` remains intentionally untouched under the existing rule to integrate all principal presentation feedback in one final synthesis.

## 12. Claim guardrail

Current supported wording:

> `3D-Sun-B0` is a literature-consistent 3-D reconstruction with frozen geometry/contact/vertical-doping checkpoints and completed G0/G1/G2 ID–VG operation. The current electrical mismatch is real under reasonable threshold-width interpretations: width-convention ambiguity cannot plausibly account for the ~0.49 V threshold shift. The active Sentaurus high-field setup is consistent with the Canali/Caughey-Thomas model family, although exact paper parameterization is unpublished. The next controlled uncertainty to test is the unpublished source/drain lateral profile, followed by source/drain-side 3-D geometry if needed. Exact electrical reproduction is not yet claimed.
