# 3D-Sun-B0 baseline evidence manifest — 2026-09-12

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Reconstruction: `3D-Sun-B0`  
> Last synchronized: 2026-09-13  
> Audit status: **G0 PASS / G1 PASS / G2 curve ingested PASS**

## 1. Purpose

This manifest records what has actually been committed for the dedicated literature-consistent 3-D BCAT baseline reconstruction and separates repository evidence from artifacts that remain only in the conversation / Sentaurus workspace.

The target is a literature-consistent reconstruction of Sun et al. (Micromachines 2022, 13, 1476), not an undocumented claim of exact reverse engineering.

## 2. Visual evidence now committed

Browsable contact sheet:

```text
assets/images/feedback/20260911_baseline/00_baseline_visual_contact_sheet.svg
```

It summarizes the reconstruction checkpoints used for geometry, XZ/YZ sections, contacts, doping / junction cuts, F1 mesh, and source/drain junction-depth verification.

The original higher-resolution screenshots remain workspace evidence and can be re-exported later if needed.

## 3. Directly browsable quantitative data

Repository directory:

```text
data/baseline_3d_sun_b0/
```

Committed curve / junction data:

```text
g0_idvg_lowvd_0p05V_to_1p2V.csv
g1_idvg_highvd_1p2V_to_2p0V.csv
g2_idvg_lowvd_0p05V_to_2p0V.csv
junction_source_C1.csv
junction_drain_C2.csv
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

## 5. Executable SDevice decks committed

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

The code README records the current physics-model claim boundary and the fact that current decks require no custom SWB parameters.

## 6. Exact SDE source status

The final F1 SDE build execution evidence is preserved through the compact checkpoint summary, but the exact final standalone SDE source CMD was not available as a separately uploaded artifact during this audit.

It is intentionally **not reconstructed from the execution log and mislabeled as exact source**.

Remaining archival action:

```text
export the original final 3D-Sun-B0 SDE source CMD from the Sentaurus workspace
→ commit it under a dedicated 3-D baseline SDE directory
```

This is the one source artifact still worth adding later because existing CMP runs normally keep the executed SDE/SDevice decks themselves.

## 7. Remaining work before `FB-BASELINE-01` closes

1. freeze the paper-equivalent Vth / Ion-Ioff extraction definitions and document the DIBL bias-pair limitation;
2. verify the paper `Canali` wording against the exact T-2022.03 high-field implementation;
3. test sensitivity to the unpublished lateral S/D Gaussian assumption (`GaussFactor=0.0`) without arbitrary parameter fitting;
4. perform coarse / nominal / fine electrical mesh convergence before freezing F1;
5. compare stabilized `3D-Sun-B0` metrics directly with the simplified 2-D CMP B0;
6. archive the original final SDE source CMD once exported from Sentaurus.

## 8. Resume point

Next session should **not** rerun G2. Resume from the post-G2 interpretation stage:

```text
G2 curve validation                         DONE
provisional low/high Vth + DIBL             DONE
paper-equivalent extraction definition      OPEN
Canali / high-field implementation mapping  OPEN
lateral Gaussian sensitivity                OPEN
mesh convergence                             OPEN
2-D vs stabilized 3-D fidelity comparison   OPEN
```

## 9. Feedback-hub synchronization state

This checkpoint should remain synchronized across:

```text
docs/FEEDBACK_LOG.md
docs/TASK_HUB.md
docs/evidence/feedback_baseline_3d_reconstruction_20260911.md
docs/evidence/baseline_3d_evidence_manifest_20260912.md
assets/images/feedback/20260911_baseline/
data/baseline_3d_sun_b0/
code/sdevice/baseline_3d_sun_b0/
```

The main `README.md` remains intentionally untouched under the existing rule to integrate all principal presentation feedback in one final synthesis.

## 10. Claim guardrail

Current supported wording:

> `3D-Sun-B0` is a literature-consistent 3-D reconstruction with frozen geometry/contact/vertical-doping checkpoints and completed G0/G1/G2 ID–VG operation. Under the current provisional `W=Wfin`, `L=Lgate` constant-current interpretation, the reconstruction gives `Vth_high ≈ 1.1466 V`, `Vth_low ≈ 1.2061 V`, and a reconstruction-defined DIBL of about `51.75 mV/V`. The exact paper-equivalent extraction convention, high-field-model mapping, lateral-doping sensitivity, electrical mesh convergence, and direct 2-D fidelity comparison remain open; therefore exact electrical reproduction is not claimed.
