# CMP Run 7 — 1T1C Retention Feasibility: Updated Checkpoint

Date: 2026-09-20  
Scope: **B0-v1 methodology feasibility** only. This document does **not** freeze a production baseline or a final retention time.

## 1. Executive status

The executed Run-7 chain is now:

```text
Write feasibility
→ 300 K Write-to-~1 V normalization
→ floating-SN direct Hold to 100 us
→ independent D0/D1 Read
→ VSN-to-Read-margin transfer
→ integrated 300 K Write → Hold → Read
→ 340/380 K Write-to-~1 V normalization
```

This supports a stronger but still scoped statement:

> **B0=36 nm에서 300 K의 normalized 1T1C Write→floating Hold→Read operation feasibility를 확인했고, storage-node voltage와 Read margin의 전달 관계를 독립 Read sweep으로 확인했다.**

The currently running 340/380 K normalized long-Hold matrix is intentionally excluded from completed evidence.

## 2. Fixed feasibility scope

```text
B0 MEB depth = 36 nm
Mesh_Code    = 1
AreaFactor   = 0.017 for normalized checkpoints
Ccell        = 10 fF
Physics      = established CMP NonlocalPath chain
```

Mainline physics:

```text
Fermi
EffectiveIntrinsicDensity(OldSlotboom)
Mobility(DopingDep HighFieldSaturation Enormal)
SRH(DopingDep)
Auger
Band2Band(Model=NonlocalPath)
```

## 3. Write normalization

The original 300 K calibration is frozen:

```text
300 K
Twrite = 667 ns
VSN_hold_start = 1.00001464973547 V
```

Temperature-specific Write calibration is also complete:

| Temperature | Twrite | VSN_hold_start |
|---:|---:|---:|
| 300 K | 667 ns | 1.00001464973547 V |
| 340 K | 258 ns | 1.00009888 V |
| 380 K | 126.54 ns | 1.00009202 V |

These values are normalization anchors for later same-start-voltage comparison. They do not imply that 1 V is a universal DRAM operating voltage.

Processed data:
- `data/run07/processed/write_1v_calibration_af0017.csv`
- `data/run07/processed/write_temp_calibration_af0017.csv`

## 4. 300 K direct floating Hold

Normalized direct-Hold condition:

```text
T = 300 K
Twrite = 667 ns
WL_HOLD = -0.7 V
BL = 0 V
SN = floating
```

| Thold | Delta VSN |
|---:|---:|
| 100 ns | 0.270 nV |
| 1 us | 2.702 nV |
| 10 us | 27.020 nV |
| 100 us | 270.195 nV |

The 0.8 V criterion is not reached within 100 us.

Therefore:
- direct floating-Hold transient: **PASS for tested window**
- resolved `t_1.0→0.8`: **not measured**
- precise retention time from short-window slope extrapolation: **not allowed**

Processed data:
- `data/run07/processed/hold_direct_300k.csv`

## 5. Independent Read and transfer

Independent D0/D1 reference:

```text
D0 DeltaVBL = -72.12 mV
D1 at VSN=0.9481 V: DeltaVBL = +30.55 mV
final BL separation = 102.67 mV
```

Read-B transfer selected points:

| VSN init | Delta VBL | D0/D1 separation |
|---:|---:|---:|
| 0.80 V | +17.92 mV | 90.04 mV |
| 0.9481 V | +30.55 mV | 102.67 mV |
| 1.00 V | +35.14 mV | 107.26 mV |

The transfer is monotonic over the executed sweep. In this setup, 0.8 V still produces a positive D1 Read signal and substantial D0/D1 separation, so 0.8 V must not be described as a read-fail threshold.

Processed data:
- `data/run07/processed/read_window.csv`
- `data/run07/processed/read_transfer_vsn.csv`

## 6. Integrated 300 K Write → Hold → Read

Normalized integrated condition uses the executed 667 ns Write anchor.

| Thold | VSN hold-start | Hold loss | VSN before Read | Delta VBL |
|---:|---:|---:|---:|---:|
| 100 ns | 1.000028401 V | 0.261 nV | 1.000044347 V | +35.6251 mV |
| 1 us | 1.000028401 V | 2.701 nV | 1.000044344 V | +35.6251 mV |
| 10 us | 1.000028401 V | 27.01 nV | 1.000044320 V | +35.6251 mV |

Result:

> **300 K normalized integrated Write→floating Hold→Read feasibility = PASS for 100 ns / 1 us / 10 us Hold.**

The Write-off settling before the settled Hold metric is not counted as retention loss.

Processed data:
- `data/run07/processed/whr_300k_norm.csv`

## 7. Current metric boundary

The project keeps these definitions separate:

- direct floating transient: `VSN(t)`, `DeltaVSN(t)`
- Synopsys-compatible secondary metric: `T_RET,5%` from leakage-vs-voltage integration
- Liu-compatible metric: `t_1.0→0.8` only when a genuine ~1 V start is used
- Read transfer: `VSN → DeltaVBL`
- integrated operation: Write → Hold → Read

No direct-retention result is relabeled as another metric.

## 8. Presentation-safe wording

Supported now:

> **B0=36 nm, 300 K에서 약 1 V의 D1 state를 실제 Write로 형성한 뒤 floating Hold와 Read를 연속 수행했으며, 100 ns–10 us Hold 조건에서 약 +35.6 mV의 D1 bitline signal을 유지했다.**

Also supported:

> **300 K direct floating-Hold transient에서는 100 us까지 storage-node voltage가 약 1 V 부근에 유지되었고, 독립 Read sweep에서는 VSN 감소에 따라 Read signal과 D0/D1 separation이 감소하는 전달 특성을 확인했다.**

Do not claim yet:

- `Retention time = X`
- measured `t_1.0→0.8`
- final temperature-dependent retention result
- final MEB-dependent retention result
- production/calibrated retention or refresh reduction

## 9. Next closure

Currently running, not yet registered as completed evidence:

```text
340 K: Twrite = 258 ns
380 K: Twrite = 126.54 ns
Thold = 100 ns / 1 us / 10 us / 100 us
```

After that matrix is processed:

```text
temperature-normalized Hold
→ temperature-normalized integrated W-H-R
→ leakage-vs-V integration if direct transient still does not reach the selected threshold
→ later MEB-dependent cell translation
```

## 10. Documentation map

- presentation/evidence checkpoint: `docs/evidence/run07_cell_operation_checkpoint_20260920.md`
- formal manifest: `docs/evidence/run07_retention_manifest.md`
- methodology: `docs/methodology/run07_methodology_traceability.md`
- source/deck index: `code/sdevice/run07/README.md`

## 11. README integration state

**Do not update the main README yet.**

Main README integration remains deferred until the current feedback/retention block is closed consistently.
