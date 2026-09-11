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
| `T-MESH-01` | Per-MEB mesh-setting / common-ROI feedback evidence | Run 3–4 Mesh-GIDL | **In Progress — next task** | E-field work confirmed 31/36/41 BTBT hotspots are inside the common ROI with comfortable margins; 41 nm X shift ≈ 0.781 nm | Collect per-MEB mesh screenshots / refinement settings, confirm same rule and prepare backup-slide proof | mesh-feedback evidence document + selected mesh figures |
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

## 4. T-MESH-01 current checkpoint and next action

Preliminary ROI-coverage evidence already obtained:

```text
common ROI:
X = 0.032–0.070 um
Y = 0.112–0.133 um
```

| MEB | Xhot (um) | Yhot (um) | nearest X margin (nm) | nearest Y margin (nm) |
|---:|---:|---:|---:|---:|
| 31 | 0.051562496 | 0.121875 | 18.438 | 9.875 |
| 36 | 0.051562496 | 0.121875 | 18.438 | 9.875 |
| 41 | 0.052343745 | 0.121875 | 17.656 | 9.875 |

This is **not the final mesh-feedback closure**. Next work starts from:

1. identify the exact 31/36/41 Mesh-Code 3 geometry / node;
2. capture comparable full-view and hotspot-zoom mesh images with the same framing;
3. document the common ROI and local max/min mesh setting (`1.0 / 0.25 nm`);
4. confirm the hotspot stays inside the refined region for each MEB;
5. prepare the presentation explanation and backup evidence;
6. only consider re-meshing if a hotspot approaches/exits the ROI or if numerical inconsistency appears.

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
