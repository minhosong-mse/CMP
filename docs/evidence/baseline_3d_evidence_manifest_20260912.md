# 3D-Sun-B0 baseline evidence manifest — 2026-09-12

> Scope: `FB-BASELINE-01` / `T-BASELINE-01`  
> Reconstruction: `3D-Sun-B0`  
> Audit status: **G0 PASS / G1 PASS / G2 launched, result not yet ingested**

## 1. Purpose

This manifest records what has actually been committed for the dedicated literature-consistent 3-D BCAT baseline reconstruction and separates repository evidence from artifacts that still exist only in the conversation / Sentaurus workspace.

The target is a literature-consistent reconstruction of Sun et al. (Micromachines 2022, 13, 1476), not an undocumented claim of exact reverse engineering.

## 2. Visual evidence now committed

Browsable contact sheet:

```text
assets/images/feedback/20260911_baseline/00_baseline_visual_contact_sheet.svg
```

It summarizes the eight visual checkpoints collected during the reconstruction:

1. 3-D geometry overview;
2. along-channel XZ gate / oxide / nitride cut;
3. across-fin YZ saddle-fin cut;
4. four-terminal contact visualization;
5. 3-D doping + vertical junction-cut setup;
6. F1 nominal electrical mesh view;
7. source junction-depth profile;
8. drain junction-depth profile.

The contact sheet is presentation / audit evidence. The original higher-resolution screenshots remain preserved in the conversation/workspace evidence and can be re-exported later if a full-resolution image archive is needed.

## 3. Directly browsable quantitative data

Repository directory:

```text
data/baseline_3d_sun_b0/
```

Committed curve / junction data:

```text
g0_idvg_lowvd_0p05V_to_1p2V.csv
g1_idvg_highvd_1p2V_to_2p0V.csv
junction_source_C1.csv
junction_drain_C2.csv
```

The source and drain vertical net-doping profiles both cross the signed net-doping zero point at approximately:

```text
Distance = 0.048 um = 48.0 nm
```

This validates the nominal **vertical** `Djunction = 0.40 × 120 nm` reconstruction target. It does not validate the unpublished lateral S/D diffusion profile.

## 4. Compact execution / log evidence

Because the original SDE/SDevice logs are large, the repository stores compact audit-relevant summaries while the full originals remain preserved in the conversation/workspace evidence:

```text
data/baseline_3d_sun_b0/f1_sde_build_summary.txt
data/baseline_3d_sun_b0/g0_sdevice_run_summary.txt
data/baseline_3d_sun_b0/g1_sdevice_run_summary.txt
```

The repository audit removed incomplete archive-transfer attempts instead of leaving truncated binary ZIP/PLT artifacts as if they were authoritative evidence.

### F1 build checkpoint

The execution evidence records:

```text
geometry / contact overlap checks = clean
source / drain / substrate / gate contact assignment = #t
body / source / drain doping definitions and placements = #t
F1 refinement definitions / placements = #t
save-model = #t
build-mesh = #t
SVisual points = 473004
SDevice tetrahedrons = 2773380
SDE execution time = 183 s
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

The G0 log confirms the four contacts, 4.8 eV gate work function, Hurkx BTBT, Philips unified mobility, Lombardi normal-field degradation, and the current T-2022.03 high-field implementation reported as Caughey-Thomas saturation using gradient quasi-Fermi potential.

### G1 checkpoint

```text
T = 300 K
Vd = 1.2 V
Vg = 0 → 2.0 V
Id(Vg=2.0 V) = 1.063e-5 A
G1 = PASS
```

Current provisional extraction:

```text
SS                    ≈ 91.2 mV/dec
max(Id)/min(Id)        ≈ 3.04e9
Vth_high*              ≈ 1.147 V
```

`*` uses the provisional `W=Wfin=17 nm`, `L=Lgate=20 nm` interpretation of the paper constant-current criterion. It is not yet frozen as the paper-equivalent threshold definition.

Paper nominal targets remain:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

Therefore the current 3-D deck is numerically operational but electrical reproduction is not yet demonstrated.

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
G2 deck = launched / result pending ingestion
```

The code README records the current physics-model claim boundary and the fact that current decks require no custom SWB parameters.

## 6. Exact SDE source status

The final F1 SDE build **execution evidence** is preserved, but the exact final standalone SDE source CMD was not available as a separately uploaded artifact during this audit.

It is intentionally **not reconstructed from the execution log and mislabeled as exact source**.

Remaining archival action:

```text
export the original final 3D-Sun-B0 SDE source CMD from the Sentaurus workspace
→ commit it under a dedicated 3-D baseline SDE directory
```

## 7. G2 status

A full low-drain run has been launched with:

```text
T = 300 K
Vd = 0.05 V
Vg = 0 → 2.0 V
```

No completed G2 log / PLT / CSV has yet been returned to the baseline workflow for validation. The only correct current repository wording is:

```text
G2 = LAUNCHED / RESULT PENDING INGESTION
```

Do not mark G2 PASS or publish a DIBL value before the returned data are checked.

Required G2 return set:

```text
full SDevice log
IdVg_LowVd_Full_*.plt
gate OuterVoltage vs drain TotalCurrent CSV
```

## 8. Remaining work before `FB-BASELINE-01` closes

1. ingest / validate G2 and calculate DIBL with one consistent low-/high-Vd threshold rule;
2. freeze the paper-equivalent Vth and Ion/Ioff extraction definitions;
3. verify the paper `Canali` wording against the exact T-2022.03 high-field implementation;
4. test sensitivity to the unpublished lateral S/D Gaussian assumption (`GaussFactor=0.0`) without arbitrary parameter fitting;
5. perform coarse / nominal / fine electrical mesh convergence before freezing F1;
6. compare stabilized `3D-Sun-B0` metrics directly with the simplified 2-D CMP B0;
7. archive the original final SDE source CMD once exported from Sentaurus.

## 9. Feedback-hub synchronization state

The latest intended state is now synchronized across:

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

> `3D-Sun-B0` is a literature-consistent 3-D reconstruction with frozen geometry/contact/vertical-doping checkpoints and numerically converged G0/G1 operation. The first electrical comparison remains mismatched to the reported Sun et al. nominal metrics. G2/DIBL, extraction convention, high-field-model mapping, lateral-doping sensitivity, electrical mesh convergence, direct 2-D fidelity comparison, and final exact-SDE-source archival remain open.
