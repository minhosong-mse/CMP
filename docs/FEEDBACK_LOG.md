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
| `FB-MESH-01` | If MEB changes hotspot position, is the common Mesh-GIDL refinement still valid for each MEB case, and how should the per-MEB mesh-setting evidence be shown? | Run 3–4 + Run 6.5 extension | `T-MESH-01` | **Resolved — full R6.5 coverage / comparison-consistency level** | Full R6.5 set `36/41/43/45/47/48/49/51 nm` independently checked: 8/8 BTBT hotspots remain inside the same Mesh-Code 3 ROI with ≥9.875 nm nearest-edge margin. Evidence: [`feedback_mesh_run65_full_validation_20260913.md`](evidence/feedback_mesh_run65_full_validation_20260913.md) |
| `FB-BASELINE-01` | How closely does the simplified 2-D B0 reproduce the literature 3-D BCAT electrical characteristics? | Run 0–1 + dedicated 3-D reconstruction | `T-BASELINE-01` | **In Progress — post-G2 extraction / model-mapping stage** | `3D-Sun-B0` built through frozen geometry/contact/doping; G0/G1/G2 curves completed; provisional low/high-Vd thresholds and reconstruction-defined DIBL extracted; executable decks, CSVs, compact summaries, and curated visual evidence committed. Evidence: [`feedback_baseline_3d_reconstruction_20260911.md`](evidence/feedback_baseline_3d_reconstruction_20260911.md), [`baseline_3d_evidence_manifest_20260912.md`](evidence/baseline_3d_evidence_manifest_20260912.md) |
| `FB-RET-01` | What exactly is the 1T1C retention measurement definition? | Run 7; downstream Run 8–9 | `T-RET-01` | **Checkpoint reached — feasibility; metric freeze still open** | Write quantified, 100 ns floating-Hold stability verified on processed subset, independent D0/D1 read window = 102.67 mV. Evidence: [`feedback_retention_operation_checkpoint_20260911.md`](evidence/feedback_retention_operation_checkpoint_20260911.md). Next: integrated Write→Hold→Read, longer Hold, `T_RET,5%`, final metric freeze. |
| `FB-RC-01` | Does deeper metal etch-back introduce a practical DRAM trade-off such as increased word-line resistance / RC delay? | Run 6.5 interpretation + `3D-Sun-B0` geometry branch | `T-RC-01` | **Checkpoint reached — geometry proxy; retention synthesis pending** | Frozen 3-D geometry swept over `36/41/43/45/47/48/49/51 nm`; remaining W cross-section and normalized `1/A_W` RWL proxy quantified. `47–49 nm` shows diminishing GIDL return while RWL proxy keeps rising. Evidence: [`feedback_rwl_tradeoff_proxy_20260913.md`](evidence/feedback_rwl_tradeoff_proxy_20260913.md) |

## 3. Resolved feedback — E-field / BTBT critical-region validation

Formal Run 5 originally showed:

```text
MEB 31 → 41 nm
GIDL endpoint decrease          ≈ 60.42%
fixed-cut E_wall,max decrease   ≈ 1.69%
```

The goal was not to force one E-field scalar to reproduce the GIDL percentage, but to determine whether the GIDL trend can be explained more defensibly from the actual BTBT-critical region.

Frozen validation set:

```text
MEB       = 31 / 36 / 41 nm
Mesh_Code = 3
T         = 300 K
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
GIDL      = |Idrain| @ VG=-0.7 V
```

Completed flow:

1. full-Si `BTBT_max`, `X_hot`, `Y_hot` automatically extracted;
2. common Mesh-GIDL ROI coverage checked;
3. hotspot-following Y-cut created at `Y_hot` and profiled along X;
4. `Band2BandGeneration`, `ElectricField-X`, `Abs(ElectricField-V)` profiles exported;
5. profile / peak behavior compared with old `E_wall,max` and terminal GIDL;
6. 10/20/50% BTBT-active widths and `int(|E| dx)` evaluated because peak-only behavior was insufficient;
7. 1-D `int(G_BTBT dx)` retained only as a spatial-generation trend cross-check.

All three cases returned:

```text
Y_hot = 0.121875 um
```

Key result, 31 → 41 nm:

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

Resolved interpretation:

> The MEB-dependent GIDL reduction is better supported by the **critical-region spatial E-field / BTBT distribution** than by one local peak-field scalar.

Scope boundary:

- no direct `Cgd → E-field → GIDL` causal law is proven;
- 1-D BTBT integral is not a terminal-current calculation;
- absolute BTBT calibration is not claimed;
- this remains a supporting validation, not the main research axis.

Evidence:

```text
docs/evidence/feedback_efield_hotspot_validation_20260911.md
data/run05/feedback_efield_20260911/
assets/images/feedback/20260911_efield/
```

## 4. Resolved feedback — per-MEB Mesh / hotspot coverage

### 4.1 Frozen common refinement rule

```text
Mesh_Code = 3
Base mesh = Medium
common ROI:
X = 0.032–0.070 um
Y = 0.112–0.133 um
local max/min = 1.0 / 0.25 nm
```

The first feedback package checked the formal Run-4 `31/36/41 nm` set. Because the final transistor-level MEB sweep was extended in Run 6.5, the mesh check was subsequently repeated across **every R6.5 MEB geometry** rather than leaving the conclusion limited to the earlier three points.

### 4.2 Full Run 6.5 audit

| MEB | BTBT node | Mesh node | Points | Elements | BTBTmax (cm^-3 s^-1) | Xhot (um) | Yhot (um) | Nearest ROI-edge margin (nm) | Result |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 36 | `n119_des` | `n2_msh` | 5789 | 12175 | 8.41825e21 | 0.0515625 | 0.121875 | 9.875 | PASS |
| 41 | `n120_des` | `n33_msh` | 5830 | 12273 | 5.55270e21 | 0.0523437 | 0.121875 | 9.875 | PASS |
| 43 | `n121_des` | `n108_msh` | 5843 | 12303 | 3.92200e21 | 0.0523437 | 0.121875 | 9.875 | PASS |
| 45 | `n122_des` | `n110_msh` | 5856 | 12333 | 2.95585e21 | 0.0531250 | 0.121875 | 9.875 | PASS |
| 47 | `n123_des` | `n112_msh` | 5880 | 12385 | 1.90750e21 | 0.0531250 | 0.121875 | 9.875 | PASS |
| 48 | `n124_des` | `n114_msh` | 5882 | 12393 | 1.42817e21 | 0.0539063 | 0.121875 | 9.875 | PASS |
| 49 | `n125_des` | `n116_msh` | 5895 | 12423 | 1.17656e21 | 0.0539063 | 0.121875 | 9.875 | PASS |
| 51 | `n126_des` | `n118_msh` | 5908 | 12453 | 5.94400e20 | 0.0539063 | 0.121875 | 9.875 | PASS |

Observed motion over the complete R6.5 sweep:

```text
Xhot range              = 0.0515625–0.0539063 um
Delta Xhot, 36→51 nm    ≈ +2.344 nm
Yhot                    = 0.121875 um for 8/8 cases
ROI coverage            = 8/8 PASS
minimum nearest margin  = 9.875 nm
```

The point / element counts increase gradually as geometry changes; identical counts are not required. The comparison-control condition is that the same `Mesh_Code=3` rule and same common local-refinement window are retained.

Resolved interpretation:

> Across the full Run 6.5 MEB set, independently extracted BTBT hotspots remain inside the same `Mesh_Code = 3` common refinement ROI with at least 9.875 nm nearest-edge margin. The total hotspot motion is small relative to the ROI dimensions, so case-specific refinement-window relocation is not required by the observed R6.5 hotspot movement. The common policy therefore supports hotspot coverage and fair case-to-case comparison consistency throughout R6.5.

Scope boundary:

- closes `FB-MESH-01` at the **full-R6.5 coverage / comparison-consistency level**;
- does not prove absolute mesh independence;
- `0.25 nm` is not claimed as a universal converged BTBT mesh size;
- a separate spacing / coarse-medium-fine convergence study would be required for an absolute mesh-independence claim.

Primary evidence:

```text
docs/evidence/feedback_mesh_run65_full_validation_20260913.md
docs/evidence/feedback_mesh_presentation_extract_20260913.md
data/run06_5/feedback_mesh_20260913/
assets/images/feedback/20260913_mesh/
```

Historical 31/36/41 evidence remains available at:

```text
docs/evidence/feedback_mesh_common_roi_validation_20260911.md
data/run04/feedback_mesh_20260911/
assets/images/feedback/20260911_mesh/
```

## 5. Baseline-feedback checkpoint — literature-consistent 3-D reconstruction

A separate `3D-Sun-B0` workflow is being used to answer `FB-BASELINE-01` before judging the simplified 2-D CMP baseline.

Detailed evidence:

```text
docs/evidence/feedback_baseline_3d_reconstruction_20260911.md
docs/evidence/baseline_3d_evidence_manifest_20260912.md
assets/images/feedback/20260911_baseline/
data/baseline_3d_sun_b0/
code/sdevice/baseline_3d_sun_b0/
```

### 5.1 Reconstruction status

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
G2  low-Vd full ID-VG               PASS — curve ingested
```

Source and drain vertical net-doping cuts both cross zero at approximately `48.0 nm`, matching the nominal vertical `Djunction` target.

The nominal electrical mesh runs the 3-D SDevice deck and recognizes all four contacts and the 4.8 eV gate work function. The current model set activates Philips unified mobility, Lombardi interface mobility degradation, Hurkx tunneling, and a high-field saturation model.

### 5.2 G1 / G2 electrical checkpoint

High-drain G1:

```text
T = 300 K
Vd = 1.2 V
Vg = 0 → 2.0 V
Id @ Vg=2.0 V = 1.063365e-5 A
SS, 1e-13~1e-10 A fit ≈ 91.17 mV/dec
max(Id)/min(Id) ≈ 3.04e9
```

Low-drain G2:

```text
T = 300 K
Vd = 0.05 V
Vg = 0 → 2.0 V
Id @ Vg=2.0 V = 2.48569e-6 A
SS, 1e-13~1e-10 A fit ≈ 92.83 mV/dec
```

Using the current provisional paper-threshold interpretation:

```text
Icrit = 1e-7 A × W/L
W = Wfin = 17 nm
L = Lgate = 20 nm
Icrit = 8.5e-8 A
```

with log-current interpolation:

```text
Vth_high @ Vd=1.20 V = 1.14659 V
Vth_low  @ Vd=0.05 V = 1.20610 V
DIBL_reconstruction     = 51.75 mV/V
```

Paper nominal targets:

```text
Vth       = 0.656 V
SS        = 76 mV/dec
Ion/Ioff  = 3.4e10
DIBL      = 23.6 mV/V
```

The exact low/high drain-bias pair used by the paper for DIBL is not explicitly published in the text. Therefore `51.75 mV/V` is a **reconstruction-defined provisional DIBL**, not a strict paper-equivalent extraction.

Current conclusion:

> `3D-Sun-B0` is numerically operational through G2, but the reported Sun et al. electrical baseline has **not** yet been reproduced.

### 5.3 Open baseline issues

- freeze / document the paper-equivalent Vth and Ion/Ioff extraction definitions and DIBL bias limitation;
- verify the paper’s Canali wording against the exact Sentaurus T-2022.03 high-field implementation; current logs report Caughey-Thomas saturation with gradient quasi-Fermi potential;
- test whether the assumed `GaussFactor=0.0` lateral S/D reconstruction contributes to the high Vth / degraded SS, without arbitrary parameter fitting;
- perform coarse / nominal / fine electrical mesh convergence before freezing F1;
- compare the stabilized 3-D reconstruction directly with the simplified 2-D CMP B0.

No work-function or doping tuning should be used merely to force agreement before those checks are completed.

## 6. Retention-feedback checkpoint — Run 7

Current checkpoint:

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

Presentation-safe wording:

> **B0 1T1C MixedMode에서 Write 후 floating storage node의 100 ns 단기 유지 안정성을 확인했고, 별도 D0/D1 read test에서 약 102.7 mV의 bitline separation을 확보하여 1차 retention-operation feasibility를 검증하였다.**

Still open before `FB-RET-01` is fully resolved:

1. integrated `Write → Hold → Read`;
2. Hold extension beyond 100 ns;
3. Synopsys-compatible `T_RET,5% = ∫ C/|I| dV` extraction;
4. final retention criterion / standby-bias freeze;
5. Mesh1/3 and BTBT attribution before formal Run-7 close-out.

Primary evidence:

```text
docs/evidence/feedback_retention_operation_checkpoint_20260911.md
docs/progress/run07_1t1c_retention_feasibility.md
docs/methodology/run07_methodology_traceability.md
```

### Practical WL resistance / RC trade-off — checkpoint

A dedicated `T-RC-01` geometry-only branch now quantifies the practical penalty using the frozen `3D-Sun-B0` geometry. Only the MEB-related gate-top / `DBCAT` depth is swept over `36/41/43/45/47/48/49/51 nm`.

With the word-line direction along `y`, the tungsten `x-z` conducting cross-section is used to define

```text
RWL_proxy(d) = A_W(36 nm) / A_W(d)
```

under the controlled assumption of identical W resistivity and WL length.

Key checkpoint:

```text
Depth    GIDL suppression vs 36 nm    RWL proxy penalty
47 nm          85.39%                       16.70%
48 nm          85.94%                       18.50%
49 nm          86.31%                       20.36%
```

The `47–49 nm` region therefore shows diminishing incremental GIDL benefit while the geometry-derived RWL proxy continues to rise. This supports the design argument that `minimum GIDL != final optimum`.

Important scope boundary:

- the proxy is geometry-derived, not an absolute resistance extraction;
- actual distributed WL resistance / RC delay was not directly simulated;
- no final optimum depth is claimed before MEB-dependent retention evidence is available;
- 51 nm remains a background-sensitive boundary reference and is excluded from the main ranking interpretation.

Evidence:

```text
docs/evidence/feedback_rwl_tradeoff_proxy_20260913.md
code/sde/tradeoff/bcat_3d_rwl_proxy_sweep.cmd
data/tradeoff/rwl_proxy_tradeoff_20260913.csv
assets/images/feedback/20260913_tradeoff/01_gidl_rwl_tradeoff.svg
```

No additional TCAD work is required on this proxy branch before retention synthesis. A circuit/MixedMode WL-RC sensitivity study remains optional if later needed to support a stronger read/write-delay claim.

## 7. Current guardrails

Avoid:

```text
48 nm is the global optimum MEB.
51 nm is physically bad.
Cgd reduction directly proves GIDL reduction causality.
Final retention time / full integrated retention has already been validated.
Absolute word-line resistance or WL RC delay was directly simulated.
The literature 3-D BCAT was fully reproduced electrically.
The current 3-D baseline already matches Sun et al.
GaussFactor = 0 is a literature value.
51.75 mV/V is necessarily the paper-equivalent DIBL.
The F1 3-D mesh is convergence-frozen.
```

Use scoped wording:

- current simplified 2-D baseline supports relative MEB-trend analysis under a common model, but its absolute fidelity must be judged against the stabilized 3-D reconstruction;
- `3D-Sun-B0` is a literature-consistent reconstruction with explicit assumptions, not an exact reverse-engineered CAD/process deck;
- G0/G1/G2 show numerically operational ID–VG behavior, not complete electrical reproduction;
- completed E-field validation supports critical-region spatial E-field / BTBT interpretation rather than one peak-field scalar;
- completed mesh feedback verifies common-ROI hotspot coverage / comparison consistency across the full R6.5 MEB set, not absolute mesh independence;
- Run 7 currently supports first-pass retention-operation feasibility, not a final retention-time claim;
- the RWL result is a geometry-derived normalized `1/A_W` proxy and supports a practical trade-off argument, not an absolute RC-delay claim;
- the final objective remains an effective / defensible MEB design range.

## 8. README integration rule

Do **not** rewrite the main README after each individual feedback item. Final README integration is deferred until the principal first-presentation feedback set is complete so baseline, E-field/mesh, retention, and practical-trade-off wording can be synthesized consistently in one pass.