# CMP FEEDBACK LOG

> Purpose: track mentor / presentation / review feedback that cuts across multiple Runs.
> Feedback is **not forced into Run chronology**. Each item links to the affected Run(s), task(s), and final evidence location.

## 1. Feedback lifecycle

```text
Feedback received
→ FEEDBACK_LOG entry
→ TASK_HUB action item
→ analysis / simulation / post-processing
→ curated evidence
→ final interpretation / slide update
→ feedback item closed
```

## 2. First-topic-presentation feedback matrix

| Feedback ID | Feedback / question | Affected Run(s) | Task | Status | Resolution / target |
|---|---|---|---|---|---|
| `FB-EFIELD-01` | Should the E-field be evaluated in the actual BTBT/GIDL critical region, and can spatial E-field / BTBT behavior explain the large GIDL-vs-field sensitivity mismatch? | Run 3–5 | `T-EFIELD-01` | **Resolved — feedback level** | 31/36/41 hotspot-following Phase A + conditional Phase B completed. Evidence: [`feedback_efield_hotspot_validation_20260911.md`](evidence/feedback_efield_hotspot_validation_20260911.md) |
| `FB-MESH-01` | If MEB changes hotspot position, is the common Mesh-GIDL refinement still valid for each MEB case, and how should the per-MEB mesh-setting evidence be shown? | Run 3–4 | `T-MESH-01` | **Resolved — feedback level** | 31/36/41 nm independently extracted BTBT hotspots are all covered by the same Mesh-Code 3 ROI with ≥9.875 nm nearest-edge margin; Run-4 per-MEB mesh / hotspot 6-panel evidence committed. Evidence: [`feedback_mesh_common_roi_validation_20260911.md`](evidence/feedback_mesh_common_roi_validation_20260911.md) |
| `FB-BASELINE-01` | How closely does the simplified 2-D B0 reproduce the literature 3-D BCAT electrical characteristics? | Run 0–1 + dedicated 3-D reconstruction | `T-BASELINE-01` | **In Progress — G2 result pending ingestion** | Literature-consistent `3D-Sun-B0` built through frozen geometry/contact/doping; G0/G1 PASS; curated visual archive, raw log/data archive, and browsable G0/G1/junction CSV evidence committed. G2 was launched but no completed G2 result has yet been ingested. Evidence: [`feedback_baseline_3d_reconstruction_20260911.md`](evidence/feedback_baseline_3d_reconstruction_20260911.md), [`baseline_3d_evidence_manifest_20260912.md`](evidence/baseline_3d_evidence_manifest_20260912.md) |
| `FB-RET-01` | What exactly is the 1T1C retention measurement definition? | Run 7; downstream Run 8–9 | `T-RET-01` | **Checkpoint reached — feasibility; metric freeze still open** | Write quantified, 100 ns floating-Hold stability verified on processed subset, independent D0/D1 read window = 102.67 mV. Evidence: [`feedback_retention_operation_checkpoint_20260911.md`](evidence/feedback_retention_operation_checkpoint_20260911.md). Next: integrated Write→Hold→Read, longer Hold, `T_RET,5%`, final metric freeze. |
| `FB-RC-01` | Does deeper metal etch-back introduce a practical DRAM trade-off such as increased word-line resistance / RC delay? | Run 6.5 interpretation; downstream synthesis | future synthesis | **Open / literature-supported consideration** | keep as an unmodeled practical trade-off unless directly simulated |

## 3. Resolved feedback — E-field / BTBT critical-region validation

### Original issue

Formal Run 5 showed:

```text
MEB 31 → 41 nm
GIDL endpoint decrease          ≈ 60.42%
fixed-cut E_wall,max decrease   ≈ 1.69%
```

The goal was **not** to force a new E-field metric to reproduce the GIDL percentage. The goal was to determine whether the GIDL trend can be explained more defensibly using spatial E-field / BTBT behavior in the actual critical region.

### Literature-grounded logic

Before extraction, five BCAT / DRAM leakage papers were reviewed. The common logic was:

```text
physical GIDL / leakage critical region
→ spatial E-field profile or map
→ representative peak / region metric when useful
→ terminal leakage / retention comparison
```

CMP-specific reproducibility additions:

- automatic `Band2BandGeneration` maximum localization;
- common ROI + hotspot-following X-cut;
- conditional `G/Gmax = 10/20/50%` sensitivity when peak-only evidence is insufficient.

These implementation choices are not claimed as universal literature standards.

### Validation set

```text
MEB       = 31 / 36 / 41 nm
Mesh_Code = 3
T         = 300 K
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
GIDL      = |Idrain| @ VG=-0.7 V
```

### Completed flow

For all three cases:

1. full-Si `BTBT_max`, `X_hot`, `Y_hot` automatically extracted;
2. common Mesh-GIDL ROI coverage checked;
3. X-direction cut created at `Y_hot`;
4. `Band2BandGeneration`, `ElectricField-X`, `Abs(ElectricField-V)` profiles exported;
5. profile / peak behavior compared with old `E_wall,max` and terminal GIDL;
6. because directional peak field did not decrease with GIDL, Phase B was activated;
7. 10/20/50% normalized BTBT-active-region width and `int(|E| dx)` were checked;
8. 1-D `int(G_BTBT dx)` was used only as a spatial-generation trend cross-check.

All three cases returned:

```text
Y_hot = 0.121875 um
```

### Close-out result: 31 → 41 nm

```text
GIDL endpoint                  -60.42%
BTBT_max                       -52.43%
1-D integrated BTBT            -57.74%
20% BTBT-active width          -12.68%
20% active-region int(|E| dx)  -14.68%
hotspot-cut |E| peak            -3.52%
old fixed E_wall,max            -1.69%
ElectricField-X peak            +8.16%
```

Threshold sensitivity:

- 10%, 20%, and 50% criteria all preserve the decreasing active-width and integrated-field trend;
- 20% is retained only as a representative middle criterion.

### Resolved interpretation

> The MEB-dependent GIDL reduction is not adequately represented by one local E-field maximum. Across 31/36/41 nm, BTBT-generation amplitude decreases, the BTBT-active spatial extent narrows, and the field integrated over the active region also decreases. The spatially integrated BTBT-generation trend is consistent with terminal GIDL reduction. Therefore the supporting mechanism is better discussed from the **critical-region spatial E-field / BTBT distribution** than from one peak-field scalar.

Interpretation boundaries:

- no direct `Cgd → E-field → GIDL` causal law is proven;
- 1-D BTBT integral is not a terminal-current calculation;
- absolute BTBT calibration is not claimed;
- this remains a supporting validation, not the main research axis.

Evidence and reusable data:

```text
docs/evidence/feedback_efield_hotspot_validation_20260911.md
data/run05/feedback_efield_20260911/
assets/images/feedback/20260911_efield/
```

## 4. Resolved feedback — per-MEB Mesh / hotspot coverage

The E-field validation supplied the independently extracted BTBT hotspot coordinates, and Run 4 supplied the formal 31/36/41 nm meshes used for comparison.

Frozen common Mesh-GIDL rule:

```text
Mesh_Code = 3
Base mesh = Medium
common Mesh-GIDL ROI
X = 0.032–0.070 um
Y = 0.112–0.133 um
local max/min = 1.0 / 0.25 nm
```

| MEB | Run-4 mesh node | Points | Elements | Xhot (um) | Yhot (um) | Nearest ROI-edge margin (nm) |
|---:|---|---:|---:|---:|---:|---:|
| 31 | `n53_msh` | 5739 | 12063 | 0.051562496 | 0.121875 | 9.875 |
| 36 | `n29_msh` | 5789 | 12175 | 0.051562496 | 0.121875 | 9.875 |
| 41 | `n58_msh` | 5830 | 12273 | 0.052343745 | 0.121875 | 9.875 |

Observed hotspot motion over 31→41 nm is only about `+0.781 nm` in X and `0 nm` in Y at the extracted mesh-node resolution. All three hotspots remain comfortably inside the same common refinement ROI.

Visual evidence is organized as the 2×3 presentation / backup layout:

```text
              31 nm                 36 nm                 41 nm
Top row   BTBT hotspot map      BTBT hotspot map      BTBT hotspot map
Bottom    Run-4 mesh zoom       Run-4 mesh zoom       Run-4 mesh zoom
```

Primary evidence:

```text
docs/evidence/feedback_mesh_common_roi_validation_20260911.md
data/run04/feedback_mesh_20260911/
assets/images/feedback/20260911_mesh/01_mesh_feedback_6panel.jpg
```

Resolved interpretation:

> The same `Mesh_Code = 3` policy and common drain-side refinement ROI cover the independently extracted BTBT hotspot for 31/36/41 nm with comfortable margin. The Run-4 images confirm that the corresponding physical region is locally refined in every formal case. Therefore the common ROI is a defensible and fair comparison rule for this feedback-validation set, and the observed hotspot motion does not require case-specific ROI relocation.

Scope boundary:

- this closes `FB-MESH-01` at the **feedback / comparison-consistency level**;
- it does **not** prove absolute mesh independence;
- `0.25 nm` is not claimed as a universal converged BTBT mesh size;
- mesh strategy should be reopened if later MEB cases approach / leave the ROI or show numerical inconsistency.

## 5. Baseline-feedback checkpoint — literature-consistent 3-D reconstruction

A separate `3D-Sun-B0` workflow is now being used to answer `FB-BASELINE-01` before judging the simplified 2-D CMP baseline.

Detailed evidence:

```text
docs/evidence/feedback_baseline_3d_reconstruction_20260911.md
docs/evidence/baseline_3d_evidence_manifest_20260912.md
assets/images/feedback/20260911_baseline/
data/baseline_3d_sun_b0/
```

### 5.1 What has been completed

The Sun et al. 2022 baseline was reconstructed in 3-D Sentaurus with an explicit distinction between literature facts and reconstruction assumptions.

Literature-explicit nominal inputs currently carried into the deck include:

```text
Lgate    = 20 nm
Drecess  = 120 nm
DBCAT    = 36 nm
Tox      = 5 nm
Wfin     = 17 nm
Hfin     = 48 nm
Rfillet  = 1.0
W gate WF = 4.8 eV
Body B    = 1e17 cm^-3
S/D As    = 1e20 cm^-3
Gaussian doping
Djunction = 0.40 × Drecess = 48 nm
```

Current phase status:

```text
A   literature truth table          DONE
B   coordinate system               PASS / FROZEN
C   geometry v05                    PASS / FROZEN
D   contacts                        PASS / FROZEN
E   doping                          PASS / FROZEN
F0  doping-QA mesh                  PASS
F1  nominal electrical mesh         BUILD PASS / CANDIDATE
G0  low-Vd SDevice bring-up         PASS
G1  high-Vd full ID-VG              PASS
G2  low-Vd full ID-VG               LAUNCHED / RESULT PENDING INGESTION
```

### 5.2 Quantitative reconstruction checks already passed

The source and drain vertical net-doping cuts both cross zero at approximately 48.0 nm, matching the nominal vertical `Djunction` target.

The nominal electrical mesh also successfully runs the 3-D SDevice deck. SDevice recognizes all four contacts and the 4.8 eV gate work function, and the current model set activates Philips unified mobility, Lombardi interface mobility degradation, Hurkx tunneling, and a high-field saturation model.

### 5.3 First electrical comparison

The high-drain G1 sweep completed at:

```text
T    = 300 K
Vd   = 1.2 V
Vg   = 0 → 2.0 V
Vs   = 0 V
Vsub = 0 V
```

Key current checkpoint:

```text
Id @ Vg=2.0 V = 1.063e-5 A
provisional SS ≈ 91.2 mV/dec
provisional max(Id)/min(Id) ≈ 3.04e9
```

If the paper’s constant-current threshold expression is provisionally evaluated with `W=Wfin=17 nm` and `L=Lgate=20 nm`, the high-Vd threshold is approximately 1.147 V. This is **not frozen as a paper-equivalent Vth** because the exact 3-D channel-width convention used by the paper still needs to be fixed.

Paper nominal targets remain:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

Therefore the current conclusion is **not** that the paper has been reproduced. The current conclusion is that the 3-D reconstruction is numerically stable but still electrically mismatched.

### 5.4 Open baseline issues

The main unresolved items are:

- ingestion of the launched G2 low-Vd full ID–VG result and consistent DIBL extraction;
- freezing the paper-equivalent Vth / Ion-Ioff extraction convention;
- verifying the paper’s Canali wording against the exact Sentaurus T-2022.03 high-field implementation (the current log reports Caughey-Thomas saturation with gradient quasi-Fermi potential);
- evaluating whether the assumed `GaussFactor=0.0` lateral S/D profile is contributing to the high Vth / degraded SS;
- electrical coarse / nominal / fine mesh convergence before F1 is frozen.

No work-function or doping tuning should be used merely to force agreement before those checks are completed.

### 5.5 Feedback-level interpretation

> The literature-consistent 3-D baseline has now been rebuilt far enough to separate “numerically working reconstruction” from “electrical reproduction.” Geometry, contacts, and vertical doping are validated and frozen, while the first high-Vd ID–VG result shows that the current reconstruction does not yet reproduce the reported Sun et al. nominal electrical metrics. DIBL remains pending ingestion of the launched G2 result. This discrepancy is being retained as evidence and investigated through extraction-definition, physics-mapping, lateral-doping, and mesh-convergence checks rather than hidden by parameter fitting.

The final answer to `FB-BASELINE-01` will compare:

```text
literature nominal 3-D metrics
↔ stabilized 3D-Sun-B0 reconstruction
↔ simplified 2-D CMP baseline
```

Only then should the role and limits of the simplified 2-D model be stated in the final presentation / README.

## 6. Retention-feedback checkpoint — Run 7

The prior wording was limited to MixedMode / write feasibility. The current checkpoint has now advanced to:

```text
Write feasibility
→ floating-SN 100 ns Hold stability
→ independent D0/D1 charge-sharing Read
```

Quantitative checkpoint:

```text
strongest screened write VSN = 0.948118 V
100 ns Hold DeltaVSN         ≈ 1e-13 ~ 1e-12 V (processed subset)
D0 DeltaVBL                  = -72.12 mV
D1 DeltaVBL                  = +30.55 mV
D0/D1 final BL separation    = 102.67 mV
```

This supports the presentation-safe statement:

> **B0 1T1C MixedMode에서 Write 후 floating storage node의 100 ns 단기 유지 안정성을 확인했고, 별도 D0/D1 read test에서 약 102.7 mV의 bitline separation을 확보하여 1차 retention-operation feasibility를 검증하였다.**

Still open before `FB-RET-01` is fully resolved:

1. integrated `Write → Hold → Read`;
2. Hold extension beyond 100 ns;
3. Synopsys-compatible `T_RET,5% = ∫ C/|I| dV` extraction;
4. final retention criterion / standby-bias freeze;
5. Mesh1/3 and BTBT attribution before formal Run-7 close-out.

Primary evidence:

- `docs/evidence/feedback_retention_operation_checkpoint_20260911.md`
- `docs/progress/run07_1t1c_retention_feasibility.md`
- `docs/methodology/run07_methodology_traceability.md`

### Practical WL resistance / RC trade-off
Keep as a literature-supported practical consideration unless directly simulated.

## 7. Current guardrails

Avoid:

```text
48 nm is the global optimum MEB.
51 nm is physically bad.
Cgd reduction directly proves GIDL reduction causality.
Final retention time / full integrated retention has already been validated.
Word-line resistance increase was directly simulated.
The literature 3-D BCAT was fully reproduced electrically.
The current 3-D baseline already matches Sun et al.
GaussFactor = 0 is a literature value.
The F1 3-D mesh is convergence-frozen.
```

Use scoped wording:

- current simplified 2-D baseline supports relative MEB-trend analysis under a common model, but its absolute fidelity must be judged against the stabilized 3-D reconstruction;
- `3D-Sun-B0` is a literature-consistent reconstruction with explicit assumptions, not an exact reverse-engineered CAD/process deck;
- completed E-field validation supports critical-region spatial E-field / BTBT interpretation rather than one peak-field scalar;
- completed mesh feedback verifies common-ROI hotspot coverage / comparison consistency for 31/36/41 nm, not absolute mesh independence;
- Run 7 currently supports **first-pass retention-operation feasibility**, not a final retention-time claim;
- the final objective remains an effective / defensible MEB design range.

## 8. README integration rule

Do **not** rewrite the main README after each individual feedback item. Final README integration is deferred until the principal first-presentation feedback set is complete so baseline, E-field/mesh, retention, and practical-trade-off wording can be synthesized consistently in one pass.
