# Run 07 Evidence Manifest — 1T1C / Retention Feasibility

Status: **B0-v1 cell-operation feasibility expanded and processed; 300 K normalized Write/Hold/Read complete at feasibility level; 340/380 K Write normalization complete; temperature-normalized long-Hold currently running and excluded from completed evidence; final retention metric still open**.

This manifest follows the repository evidence rule: GitHub keeps source code where frozen, parameter snapshots, processed summaries and selected evidence; full `.tdr`, `.plt` and solver logs remain in the TCAD/local archive unless a provenance problem requires a specific artifact.

## 1. Scope and provenance

```text
B0 MEB_Depth = 0.036 um
Mesh_Code = 1 for current Run-7 feasibility/normalization work
AreaFactor = 0.017 for normalized checkpoints
Ccell = 10 fF
Physics = established CMP NonlocalPath chain
```

SDE provenance remains the B0 Run-6.5 geometry source.

Local Sentaurus Workbench projects are the execution archive. GitHub stores frozen command decks where available plus processed result tables and evidence summaries.

## 2. Execution evidence table

| Branch | Accepted set | Parameter snapshot | Processed summary | Status |
|---|---|---|---|---|
| R7B Write screen | AF=0.017 nodes 182–185, 194–197, 206–209 | `VBL=1.2 V`, `VWL=1.5–3.0 V`, `Twrite=100/200/300 ns` | `write_screen_af0017.csv` | **PASS — feasibility** |
| R7A 300 K 1 V calibration | n409 | `T=300 K`, `Twrite=667 ns` | `write_1v_calibration_af0017.csv` | **PASS — 300 K anchor frozen** |
| R7C 100 ns Hold screen | complete 36 cases | AF=0.011/0.017/0.023, `Thold=100 ns` | `hold100_complete.csv` | **PASS — complete short-Hold screen** |
| R7C direct Hold | 300 K, 4 windows | `Twrite=667 ns`, `Thold=100 ns/1 us/10 us/100 us` | `hold_direct_300k.csv` | **PASS — tested transient window** |
| R7E independent Read | D0/D1 reference | `Ccell=10 fF`, `CBL=45 fF`, `VBL=0.5 V`, `Tread=10 ns` | `read_window.csv` | **PASS** |
| R7E Read transfer | 13 VSN points | `VSN=0,0.55…1.05 V` | `read_transfer_vsn.csv` | **PASS — monotonic transfer** |
| Integrated W-H-R | 300 K normalized, 3 Hold windows | `Twrite=667 ns`, `Thold=100 ns/1 us/10 us` | `whr_300k_norm.csv` | **PASS — 300 K operation feasibility** |
| Temperature Write calibration | 340/380 K | `Twrite=258 ns / 126.54 ns` final anchors | `write_temp_calibration_af0017.csv` | **PASS — normalized anchors frozen** |
| Temperature-normalized Hold | 340/380 K × 4 Hold windows | ~1 V start | not registered | **RUNNING / excluded from completed checkpoint** |
| `T_RET,5%` leakage integration | pending | Synopsys-compatible integration path | pending | **Not run for closure** |
| Mesh1 vs Mesh3 | pending | final verification | pending | **Not run** |

## 3. Quantitative checkpoint

### 3.1 Write normalization

```text
300 K: Twrite = 667 ns    -> VSN_hold_start = 1.00001464973547 V
340 K: Twrite = 258 ns    -> VSN_hold_start = 1.00009888 V
380 K: Twrite = 126.54 ns -> VSN_hold_start = 1.00009202 V
```

These are comparison anchors, not universal operation voltages.

### 3.2 300 K direct Hold

| Thold | Delta VSN |
|---:|---:|
| 100 ns | 0.270 nV |
| 1 us | 2.702 nV |
| 10 us | 27.020 nV |
| 100 us | 270.195 nV |

The 0.8 V criterion is not reached within 100 us. No physical retention time is extrapolated from this short-window slope.

### 3.3 Independent Read transfer

```text
D0 DeltaVBL = -72.12 mV

VSN=0.80 V   -> DeltaVBL = +17.92 mV, separation = 90.04 mV
VSN=0.9481 V -> DeltaVBL = +30.55 mV, separation = 102.67 mV
VSN=1.00 V   -> DeltaVBL = +35.14 mV, separation = 107.26 mV
```

The 0.8 V point is not a CMP read-fail threshold.

### 3.4 Integrated 300 K Write → Hold → Read

| Thold | Hold loss | VSN before Read | Delta VBL |
|---:|---:|---:|---:|
| 100 ns | 0.261 nV | 1.000044347 V | +35.6251 mV |
| 1 us | 2.701 nV | 1.000044344 V | +35.6251 mV |
| 10 us | 27.01 nV | 1.000044320 V | +35.6251 mV |

This closes **300 K integrated operation feasibility** for the tested windows. It does not close a physical retention-time metric.

## 4. Processed summary files

```text
data/run07/processed/
  write_screen_af0017.csv
  write_1v_calibration_af0017.csv
  write_temp_calibration_af0017.csv
  hold100_partial.csv
  hold100_complete.csv
  hold_direct_300k.csv
  read_window.csv
  read_transfer_vsn.csv
  whr_300k_norm.csv
```

## 5. Selected Run-7A figures already registered

```text
assets/images/run07/06_r7_A_n409_write_hold_overall_667ns.svg
assets/images/run07/07_r7_A_n409_vsn_write_to_1V_667ns.svg
assets/images/run07/08_r7_A_n409_1V_settling_zoom_667ns.svg
```

## 6. Evidence / claim boundary

- 1 V is a literature-compatible normalization benchmark, not a universal operating voltage.
- Direct floating transient `VSN(t)` remains distinct from `T_RET,5%` and `t_1.0→0.8`.
- 100 us stability does not equal a measured retention time.
- `0.8 V` is not automatically a read-fail voltage; the independent Read sweep still shows positive D1 signal there.
- The 300 K W-H-R result is integrated operation feasibility, not final temperature-dependent retention validation.
- Temperature-normalized 340/380 K long-Hold results are not entered until the currently running matrix is processed.
- `AreaFactor=0.017` remains an effective-width proxy, not production calibration.
- No MEB-dependent retention conclusion is entered during this B0 Run-7 checkpoint.

## 7. Presentation checkpoint

For current presentation reinforcement, use:

1. 300 K Write normalization: `667 ns -> ~1.000015 V`.
2. 300 K direct Hold: 100 ns–100 us storage-node decay table/trend.
3. Independent `VSN -> DeltaVBL` transfer to connect stored-voltage degradation to Read margin.
4. Integrated 300 K W-H-R: `DeltaVBL ≈ +35.625 mV` for 100 ns–10 us Hold.
5. 340/380 K Write normalization anchors as setup for the next temperature-Hold result.

Detailed presentation-safe checkpoint:
- `docs/evidence/run07_cell_operation_checkpoint_20260920.md`

## 8. Next required evidence

```text
currently running:
340/380 K temperature-normalized Hold from ~1 V
→ process 100 ns / 1 us / 10 us / 100 us

then:
temperature-normalized integrated Write → Hold → Read
→ leakage-vs-V integration if direct transient remains far from selected threshold
→ Mesh1/3 check
→ later MEB-dependent cell translation
```

Main progress document:
- `docs/progress/run07_1t1c_retention_feasibility.md`

Methodology traceability:
- `docs/methodology/run07_methodology_traceability.md`
