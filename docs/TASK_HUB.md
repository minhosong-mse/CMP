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
| `T-MESH-01` | Per-MEB mesh-setting / common-ROI feedback evidence | Run 3–4 + full Run 6.5 extension | **Completed — full R6.5 coverage / comparison-consistency level** | All 8 R6.5 MEB cases `36/41/43/45/47/48/49/51 nm` use the same Mesh-Code 3 policy; independently extracted BTBT hotspots remain inside the common ROI with ≥9.875 nm nearest-edge margin; full raw/ROI tables and screenshot provenance committed | Use the full-R6.5 evidence package for presentation; reopen only for an absolute mesh-convergence study or if a future geometry leaves the ROI | `docs/evidence/feedback_mesh_run65_full_validation_20260913.md` + `data/run06_5/feedback_mesh_20260913/` + `assets/images/feedback/20260913_mesh/` |
| `T-BASELINE-01` | Literature-consistent 3-D BCAT baseline reconstruction and 2-D fidelity comparison | Run 0–1 + dedicated `3D-Sun-B0` workflow | **Completed — model-fidelity close-out** | Geometry/contact/doping mapping, G0/G1/G2, H1/H2 sensitivities, DC electrical mesh convergence, and controlled 2D↔3D parity comparison completed; exact Sun-et-al. electrical calibration remains intentionally unclaimed | Use 2D for dense DOE and 3D-Sun-B0 as the selected-point validation anchor | `docs/evidence/feedback_baseline_closeout_20260914.md` | Export exact final F1 SDE source CMD → run isolated lateral S/D Gaussian sensitivity → if needed test S/D-side 3-D rounding → mesh convergence → compare stabilized 3-D baseline with simplified 2-D B0 | `docs/evidence/feedback_baseline_3d_reconstruction_20260911.md` + `docs/evidence/baseline_3d_evidence_manifest_20260912.md` + `docs/evidence/baseline_3d_extraction_physics_verification_20260913.md` |
| `T-RET-01` | 1T1C retention protocol freeze | Run 7 | **Advanced checkpoint — final retention metric still open** | 300 K write-to-~1 V, 100 us direct Hold, independent Read, integrated 300 K W→H→R and approximately normalized 300/340/380 K direct-Hold comparison committed | Complete leakage-vs-V / final retention metric, Mesh1/3 retention check, and temperature-integrated W-H-R only if required by the final handoff | `docs/progress/run07_1t1c_retention_feasibility.md` + latest Run-7 evidence | Integrated `Write → Hold → Read`, longer Hold, `T_RET,5%`, final retention-metric freeze | `docs/progress/run07_1t1c_retention_feasibility.md` + `docs/evidence/feedback_retention_operation_checkpoint_20260911.md` + methodology traceability |
| `T-RC-01` | Practical MEB-depth trade-off: W cross-section / normalized RWL proxy | Run 6.5 GIDL + frozen `3D-Sun-B0` geometry branch | **Checkpoint reached — proxy complete; waiting retention synthesis** | `36/41/43/45/47/48/49/51 nm` geometry sweep completed; normalized `1/A_W` proxy quantified; `47–49 nm` shows diminishing GIDL return while RWL proxy continues to rise | Do not add more TCAD to this branch yet; combine with MEB-dependent retention after Run-7 metric freeze. Optional WL-RC MixedMode only if stronger speed evidence becomes necessary | `docs/evidence/feedback_rwl_tradeoff_proxy_20260913.md` + `data/tradeoff/rwl_proxy_tradeoff_20260913.csv` + `assets/images/feedback/20260913_tradeoff/01_gidl_rwl_tradeoff.svg` |

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
3. hotspot-following **Y-cut at `Y_hot`**, with the profile evaluated along X;
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

The initial feedback check used Run-4 `31/36/41 nm`. After the MEB search expanded, the task was reopened and checked against the **complete Run 6.5 MEB set**.

### Full R6.5 validation set

```text
MEB = 36 / 41 / 43 / 45 / 47 / 48 / 49 / 51 nm
T = 300 K
VD = 1.2 V
VG final = -0.7 V
```

| MEB | BTBT node | Mesh node | Points | Elements | BTBTmax (cm^-3 s^-1) | Xhot (um) | Yhot (um) | nearest ROI-edge margin (nm) | ROI |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| 36 | `n119_des` | `n2_msh` | 5789 | 12175 | 8.41825e21 | 0.0515625 | 0.121875 | 9.875 | PASS |
| 41 | `n120_des` | `n33_msh` | 5830 | 12273 | 5.55270e21 | 0.0523437 | 0.121875 | 9.875 | PASS |
| 43 | `n121_des` | `n108_msh` | 5843 | 12303 | 3.92200e21 | 0.0523437 | 0.121875 | 9.875 | PASS |
| 45 | `n122_des` | `n110_msh` | 5856 | 12333 | 2.95585e21 | 0.0531250 | 0.121875 | 9.875 | PASS |
| 47 | `n123_des` | `n112_msh` | 5880 | 12385 | 1.90750e21 | 0.0531250 | 0.121875 | 9.875 | PASS |
| 48 | `n124_des` | `n114_msh` | 5882 | 12393 | 1.42817e21 | 0.0539063 | 0.121875 | 9.875 | PASS |
| 49 | `n125_des` | `n116_msh` | 5895 | 12423 | 1.17656e21 | 0.0539063 | 0.121875 | 9.875 | PASS |
| 51 | `n126_des` | `n118_msh` | 5908 | 12453 | 5.94400e20 | 0.0539063 | 0.121875 | 9.875 | PASS |

Completed evidence:

1. exact R6.5 Mesh-Code 3 cases identified for all eight MEB geometries;
2. full-Si `Band2BandGeneration` maximum independently extracted per case;
3. `Xhot/Yhot`, `BTBTmax`, points and elements transcribed into a raw-data table;
4. four ROI-edge margins calculated per case;
5. **8/8 cases PASS** the common-ROI coverage audit;
6. `Xhot` moves only about **+2.344 nm** from 36→51 nm;
7. `Yhot = 0.121875 um` for **all 8 cases**;
8. minimum nearest-edge margin remains **9.875 nm** throughout the sweep;
9. screenshot provenance / canonical filename mapping recorded for slide extraction;
10. claim boundary retained as **coverage / comparison consistency**, not absolute mesh-independence proof.

Supported interpretation:

> Across the complete R6.5 MEB geometry sweep, the same `Mesh_Code = 3` policy and common refinement ROI cover the independently extracted BTBT critical region with sufficient margin. The observed hotspot motion does not require case-specific ROI relocation, so the common mesh policy is defensible for fair R6.5 comparison.

Evidence:

- `docs/evidence/feedback_mesh_run65_full_validation_20260913.md`
- `docs/evidence/feedback_mesh_presentation_extract_20260913.md`
- `data/run06_5/feedback_mesh_20260913/r65_mesh_raw_extract.csv`
- `data/run06_5/feedback_mesh_20260913/r65_mesh_hotspot_coverage_summary.csv`
- `data/run06_5/feedback_mesh_20260913/screenshot_manifest.csv`
- `assets/images/feedback/20260913_mesh/`

Historical 31/36/41 package remains at:

- `docs/evidence/feedback_mesh_common_roi_validation_20260911.md`
- `data/run04/feedback_mesh_20260911/`
- `assets/images/feedback/20260911_mesh/`

Reopen conditions:

- a future geometry hotspot approaches or leaves the current ROI;
- numerical inconsistency appears across cases;
- an absolute mesh-independence claim is required, in which case a separate convergence study is needed.

## 5. Cross-chat tasks still open

### T-BASELINE-01

Dedicated `3D-Sun-B0` baseline workflow.

Current checkpoint:

```text
Literature truth table          DONE
Geometry / contacts / doping    PASS / FROZEN
Vertical Djunction              48.0 nm source + drain PASS
F1 electrical mesh             BUILD PASS / CANDIDATE
G0 low-Vd bring-up              PASS
G1 high-Vd full ID-VG           PASS
G2 low-Vd full ID-VG            PASS
Vth-width artifact check        PASS — cannot explain mismatch
Canali / CT model-family map    PASS — compatible
Electrical paper match          NOT YET
```

G1/G2 provide a consistent reconstruction-defined low/high drain comparison. Under the current provisional constant-current interpretation (`W=Wfin=17 nm`, `L=Lgate=20 nm`, `Icrit=8.5e-8 A`) and log-current interpolation:

```text
Vth_high @ Vd=1.20 V = 1.14659 V
Vth_low  @ Vd=0.05 V = 1.20610 V
DIBL_reconstruction     = 51.75 mV/V
SS_high                 ≈ 91.17 mV/dec
SS_low                  ≈ 92.83 mV/dec
```

Paper nominal values remain `Vth=0.656 V`, `SS=76 mV/dec`, `Ion/Ioff=3.4e10`, and `DIBL=23.6 mV/V`.

Post-G2 verification conclusions:

1. **Width convention is not the main Vth problem.** Using a larger saddle-fin width interpretation moves the extracted Vth even higher. Matching the paper `Vth=0.656 V` on the current G1 curve would require an unphysical equivalent width of about `1.87e-4 nm` under the constant-current formula.
2. **Canali vs. Caughey-Thomas naming is not a model-family mismatch.** Sentaurus documentation/training describes the built-in high-field saturation model as Canali and also describes its Caughey-Thomas basis; the current `e/hHighFieldSaturation(GradQuasiFermi)` setup is therefore consistent at model-family/activation level. Exact paper parameter overrides remain unpublished.
3. The paper text still does not explicitly publish the exact low/high drain-bias pair used for its DIBL value, so `51.75 mV/V` remains a **reconstruction-defined provisional DIBL**.

Resume from:

1. **export the exact final F1 SDE source CMD from Sentaurus** — do not reconstruct it from a log;
2. create an isolated **lateral S/D Gaussian sensitivity** variant while keeping geometry, vertical `Djunction`, work function, mesh policy, and SDevice physics fixed;
3. treat any nonzero `GaussFactor` as a sensitivity bracket, not as a literature value;
4. if lateral spread does not explain the direction/magnitude of mismatch, separately test S/D-side 3-D rounding / effective-channel geometry;
5. perform coarse / nominal / fine electrical mesh convergence;
6. compare stabilized `3D-Sun-B0` directly with simplified 2-D B0 and close the original feedback question.

Repository evidence policy for this task:

```text
COMMIT by default:
  executed source CMDs
  validated CSV data
  compact run/build summaries
  curated figures used as evidence
  feedback / evidence documentation

KEEP in chat/workspace unless specifically needed:
  full Sentaurus logs
  native .plt files
  temporary screenshots / failed attempts
```

Primary links:

- `docs/evidence/feedback_baseline_3d_reconstruction_20260911.md`
- `docs/evidence/baseline_3d_evidence_manifest_20260912.md`
- `docs/evidence/baseline_3d_extraction_physics_verification_20260913.md`
- `assets/images/feedback/20260911_baseline/01_g1_g2_idvg_comparison.svg`
- `data/baseline_3d_sun_b0/extraction_width_sensitivity_20260913.csv`
- `code/sdevice/baseline_3d_sun_b0/`

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

### T-RC-01
Dedicated practical trade-off branch.

Current checkpoint:

```text
36/41/43/45/47/48/49/51 nm geometry sweep   PASS
W x-z conducting cross-section extraction    PASS
normalized RWL proxy = A_W(36)/A_W(d)         PASS
GIDL + RWL-proxy synthesis                    PASS
actual distributed WL resistance              NOT SIMULATED
actual WL RC delay                             NOT SIMULATED
final optimum / effective range                PENDING RETENTION
```

Key result:

```text
Depth    GIDL suppression vs 36 nm    RWL proxy penalty
47 nm          85.39%                       16.70%
48 nm          85.94%                       18.50%
49 nm          86.31%                       20.36%
```

Supported interpretation:

> The 47–49 nm region is a diminishing-return candidate: incremental GIDL benefit becomes small while the geometry-derived normalized RWL penalty continues to rise. This is sufficient for the current feedback-level trade-off argument, but not sufficient to declare a final optimum.

Resume from:

1. wait for Run-7 retention metric freeze;
2. add MEB-dependent retention results for `36/41/48` and `49` if challenger evidence is needed;
3. combine `GIDL + retention + DC/cell guardrails + RWL proxy` into the effective MEB-range decision;
4. add MixedMode/circuit WL-RC sensitivity only if the final conclusion requires stronger speed evidence.

Primary links:

- `docs/evidence/feedback_rwl_tradeoff_proxy_20260913.md`
- `data/tradeoff/rwl_proxy_tradeoff_20260913.csv`
- `assets/images/feedback/20260913_tradeoff/01_gidl_rwl_tradeoff.svg`
- `code/sde/tradeoff/bcat_3d_rwl_proxy_sweep.cmd`

## 6. README integration rule

Do not update the main README after each individual feedback item. Integrate the major feedback set together after baseline, E-field/mesh, retention, and practical-trade-off wording are ready.

---

## 6. Post-Turn-02 validation tasks

| Task ID | Task | Status | Dependency | Completion condition |
|---|---|---|---|---|
| `T-WRITE-02` | High-WL-bias / write-transfer guardrail | **Planned** | Run-7 B0 protocol | `VWL→VSN` and write-time behavior quantified; MEB dependence tested at selected points; “1 V reached” no longer the only success condition |
| `T-TEMP-COLD-02` | `233 K (-40 °C)` cold extension | **Planned** | SG candidate + stable cell protocol | selected MEB candidates compared across cold-to-hot conditions without mixing planned 233 K with completed 300/340/380 K results |
| `T-DWFG-02` | DWFG transferability of SG-selected MEB range | **Planned / downstream** | Phase-1 SG MEB range | same candidate MEBs implemented under a literature-grounded DWFG extension; hotspot/ROI revalidated; GIDL/retention transferability assessed |
| `T-3D-SELECT-02` | Selected-point 3D validation | **Planned / downstream** | final or near-final candidate set | baseline / candidate / boundary points checked in 3D for trend preservation and design-decision robustness |

See `docs/research/post_turn02_validation_roadmap.md`.
