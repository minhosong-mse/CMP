# CMP TASK HUB

> Purpose: track where cross-chat work is paused, what is completed, and what the next concrete action is.

## 1. Operating rule

- **Chat / local workspace**: exploratory work, raw screenshots, failed attempts, temporary measurements.
- **TASK_HUB**: current task state, frozen method, completed checkpoint, next action.
- **RUN_SHEET**: official research-stage status and exit criteria.
- **DECISIONS**: interpretation / metric / scope decisions.
- **progress / evidence**: finalized scientific results and curated evidence.

## 2. Active / completed feedback tasks

| Task ID | Task | Source | Status | Completed checkpoint | Next action | Final destination |
|---|---|---|---|---|---|---|
| `T-EFIELD-01` | Literature-grounded hotspot E-field / BTBT validation | Run 4–5, 31/36/41 nm, 300 K GIDL ON | **Completed — feedback level** | Phase A + conditional Phase B complete; hotspot coordinates, threshold sensitivity, integrated field / BTBT trend and figures committed | Use the evidence package for presentation; reopen only for thesis-level extension | `docs/evidence/feedback_efield_hotspot_validation_20260911.md` + `data/run05/feedback_efield_20260911/` |
| `T-MESH-01` | Per-MEB mesh-setting / common-ROI feedback evidence | Run 3–4 Mesh-GIDL | **Completed — feedback level** | 31/36/41 nm all use the same Mesh-Code 3 rule; independently extracted BTBT hotspots remain inside the common ROI with ≥9.875 nm nearest-edge margin; 6-panel hotspot/mesh evidence committed | Use for presentation / backup; reopen only if later MEB cases approach/leave the ROI or numerical inconsistency appears | `docs/evidence/feedback_mesh_common_roi_validation_20260911.md` + `data/run04/feedback_mesh_20260911/` + `assets/images/feedback/20260911_mesh/` |
| `T-BASELINE-01` | Baseline recalibration / literature comparison | Run 0–1 | **In Progress elsewhere** | B0 scope / limitations documented | Continue paper vs B0-v1 vs recalibrated B0-v2 comparison | baseline validation slide + progress / decision update |
| `T-RET-01` | 1T1C retention protocol freeze | Run 7 | **Checkpoint reached — feedback-level feasibility** | Write screen quantified; floating-SN 100 ns Hold stable for processed subset; independent D0/D1 Read window = **102.67 mV** | Integrated `Write → Hold → Read`, longer Hold, `T_RET,5%`, final retention-metric freeze | `docs/progress/run07_1t1c_retention_feasibility.md` + `docs/evidence/feedback_retention_operation_checkpoint_20260911.md` + methodology traceability |

## 3. T-EFIELD-01 close-out checkpoint

### Why it existed

```text
MEB 31 → 41 nm
GIDL endpoint decrease          ≈ 60.42%
fixed-cut E_wall,max decrease   ≈ 1.69%
```

The feedback question was whether the terminal-GIDL sensitivity could be interpreted more defensibly from the actual BTBT-critical region rather than one fixed field peak.

This remained a **supporting validation**, not a new main research axis.

### Frozen validation set

```text
MEB       = 31 / 36 / 41 nm
Mesh_Code = 3
T         = 300 K
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
terminal  = |Idrain| @ VG=-0.7 V
```

### Completed protocol

1. full-Si `Band2BandGeneration` maximum localization;
2. hotspot-coordinate / common-ROI coverage check;
3. hotspot-following X-cut at `Y_hot`;
4. export `Band2BandGeneration`, `ElectricField-X`, `Abs(ElectricField-V)`;
5. compare profiles / peaks with old `E_wall,max` and terminal GIDL;
6. activate Phase B because peak-field behavior was insufficient;
7. evaluate 10/20/50% BTBT-active widths and `int(|E| dx)`;
8. retain 1-D `int(G_BTBT dx)` as a spatial-generation trend cross-check only.

All three cases:

```text
Y_hot = 0.121875 um
```

### Key result: 31 → 41 nm

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

Supported interpretation:

> The terminal GIDL trend is better supported by the critical-region spatial E-field / BTBT distribution than by one local peak-field scalar.

Evidence:

- `docs/evidence/feedback_efield_hotspot_validation_20260911.md`
- `data/run05/feedback_efield_20260911/`
- `assets/images/feedback/20260911_efield/`

## 4. T-MESH-01 close-out checkpoint

Frozen common refinement rule:

```text
Mesh_Code = 3
Base mesh = Medium
common ROI:
X = 0.032–0.070 um
Y = 0.112–0.133 um
local max/min = 1.0 / 0.25 nm
```

| MEB | Run-4 node | Points | Elements | Xhot (um) | Yhot (um) | nearest ROI-edge margin (nm) |
|---:|---|---:|---:|---:|---:|---:|
| 31 | `n53_msh` | 5739 | 12063 | 0.051562496 | 0.121875 | 9.875 |
| 36 | `n29_msh` | 5789 | 12175 | 0.051562496 | 0.121875 | 9.875 |
| 41 | `n58_msh` | 5830 | 12273 | 0.052343745 | 0.121875 | 9.875 |

Completed evidence:

1. exact Run-4 Mesh-Code 3 cases identified for 31/36/41 nm;
2. common refinement rule and local max/min spacing documented;
3. independently extracted BTBT hotspot coordinates compared against the common ROI;
4. all hotspots verified to remain comfortably inside the ROI;
5. per-MEB hotspot / mesh evidence arranged in the 2×3 comparison layout;
6. primary 6-panel image committed to the repository;
7. claim boundary frozen as **coverage / comparison consistency**, not absolute mesh-independence proof.

Supported interpretation:

> For the present 31/36/41 nm validation set, the same `Mesh_Code = 3` policy and common refinement ROI cover the BTBT critical region with sufficient margin. The observed hotspot motion does not require case-specific ROI relocation, so the common mesh policy is defensible for fair comparison.

Evidence:

- `docs/evidence/feedback_mesh_common_roi_validation_20260911.md`
- `data/run04/feedback_mesh_20260911/`
- `assets/images/feedback/20260911_mesh/01_mesh_feedback_6panel.jpg`

Reopen conditions:

- a later MEB hotspot approaches or leaves the current ROI;
- numerical inconsistency appears across cases;
- an absolute mesh-independence claim is required, in which case a separate convergence study is needed.

## 5. Cross-chat tasks still open

### T-BASELINE-01
Dedicated baseline workflow.

### T-RET-01
Dedicated Run-7 workflow.

Current feedback-level checkpoint:

```text
Write screen                      PASS — feasibility
100 ns floating-SN Hold subset    PASS — stability
Independent D0/D1 read            PASS
D0/D1 BL separation               102.67 mV
physical retention time           NOT YET
integrated Write→Hold→Read         NOT YET
```

Presentation-safe wording:

> B0 1T1C MixedMode에서 Write 후 floating storage node의 100 ns 단기 유지 안정성을 확인했고, 별도 D0/D1 read test에서 약 102.7 mV의 bitline separation을 확보하여 1차 retention-operation feasibility를 검증하였다.

Resume from:

1. integrated `Write → Hold → Read`;
2. longer Hold;
3. Synopsys-compatible `T_RET,5%`;
4. final metric / bias freeze;
5. Mesh1/3 and BTBT attribution before formal Run-7 close-out.

Primary links:

- `docs/progress/run07_1t1c_retention_feasibility.md`
- `docs/evidence/feedback_retention_operation_checkpoint_20260911.md`
- `docs/methodology/run07_methodology_traceability.md`

## 6. README integration rule

Do not update the main README after each individual feedback item. Integrate the major feedback set together after baseline, E-field/mesh, retention, and practical-trade-off wording are ready.
