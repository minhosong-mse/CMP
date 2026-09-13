# Run 07 Evidence Manifest — 1T1C / Retention Feasibility

Status: **first-pass feasibility evidence executed and curated; complete 36-case 100 ns Hold screen processed; final retention metric still open**.

This manifest follows the existing repository evidence rule: GitHub keeps code, conditions, processed summaries and selected evidence; full `.tdr`, `.plt` and solver logs remain in the TCAD/local archive unless a provenance problem requires a specific artifact.

## 1. Source commands

| Branch | Command | Current status |
|---|---|---|
| R7B Write | `code/sdevice/run07/bcat_1t1c_r7_write_screen.cmd` | executed / quantified for AF=0.017 screen |
| R7C Hold | `code/sdevice/run07/bcat_1t1c_r7_hold100_screen.cmd` | executed / complete 36-case matrix processed |
| R7D Retention ON | `code/sdevice/run07/bcat_retention_r7_ivsn_integral_on.cmd` | prepared / not yet executed for current closure |
| R7D Retention OFF | `code/sdevice/run07/bcat_retention_r7_ivsn_integral_off.cmd` | prepared / not yet executed |
| R7E Read | `code/sdevice/run07/bcat_1t1c_r7_read_window.cmd` | executed / D0-D1 independent read accepted |

SDE provenance remains the B0 Run-6.5 geometry source fixed to `MEB_Depth=0.036 um` for Run 7.

## 2. Execution evidence table

| R7 branch | Accepted node(s) / set | Parameter snapshot | Processed summary | Evidence | Status |
|---|---|---|---|---|---|
| R7B Write | AF=0.017 nodes 182–185, 194–197, 206–209 | `VBL=1.2 V`, `VWL=1.5–3.0 V`, `Twrite=100/200/300 ns`, `Ccell=10 fF` | `data/run07/processed/write_screen_af0017.csv` | `docs/evidence/run07_write_screen_20260911.md` | **PASS — feasibility** |
| R7C Hold Mesh1 | complete nodes 178–213 | `AF=0.011/0.017/0.023`, `VWL=1.5–3.0 V`, `Twrite=100/200/300 ns`, `Thold=100 ns`, SN floating after `Unset(sn)` | `data/run07/processed/hold100_complete.csv` | `docs/evidence/run07_hold100_complete_20260913.md` | **PASS — complete 36-case short-Hold screen** |
| R7D Retention ON | Pending | Synopsys-compatible 5% leakage-integration path | Pending | methodology traceability only | **Not run** |
| R7D Retention OFF | Pending | BTBT attribution branch | Pending | Pending | **Not run** |
| R7E Read | n136 D0, n138 D1 | `Ccell=10 fF`, `CBL=45 fF`, `VBL=0.5 V`, `WL=-0.7→3.0 V`, `Tread=10 ns` | `data/run07/processed/read_window.csv` | `docs/evidence/run07_read_window_20260911.md` | **PASS — independent read** |
| Integrated W-H-R | Pending in this manifest checkpoint | representative D1 | Pending | Pending | **Not claimed here** |
| Mesh1 vs Mesh3 | Pending | final verification | Pending | Pending | **Not run** |

## 3. Current quantitative checkpoint

### Write

```text
max screened nominal-width VSN = 0.948118 V
at AreaFactor=0.017, VWL_ON=3.0 V, Twrite=300 ns
```

### Hold

Complete 36-case 100 ns screen:

```text
36 / 36 cases processed
maximum |DeltaVSN_100ns| = 2.465920e-10 V
maximum |fractional change| = 2.548440e-8 %
```

Representative n209:

```text
VSN_hold_start  = 0.948118339190 V
VSN_hold_+100ns = 0.948118339047 V
DeltaVSN        = 1.432444e-10 V
```

Interpretation: numerical-floor-level change; short-Hold stability only.

### Read

```text
D0 DeltaVBL = -72.12 mV
D1 DeltaVBL = +30.55 mV
D0/D1 final BL separation = 102.67 mV
```

## 4. Processed summary files

```text
data/run07/processed/
  write_screen_af0017.csv
  hold100_partial.csv
  hold100_complete.csv
  read_window.csv
```

The partial Hold CSV is retained as historical provenance. `hold100_complete.csv` is the current formal source for the 36-case 100 ns screen.

## 5. Evidence rules / claim boundary

- A graph without the corresponding exported/processed data and parameter snapshot is not a formal Run 7 metric source.
- `T_RET,5%` is kept distinct from direct threshold-crossing time.
- Liu-compatible `t_1.0→0.8` is not reported unless the written state actually begins near 1.0 V.
- Literature read thresholds are context only unless a CMP-specific criterion is derived.
- `AreaFactor=0.017` remains an effective-width proxy, not production calibration.
- The complete 36-case 100 ns Hold result is **stability evidence**, not a retention-time number.
- The n136/n138 test is **independent read feasibility**, not `Read-after-Hold`.
- No MEB-dependent retention conclusion is entered during this B0 Run 7 checkpoint.

## 6. Next required evidence

The following later follow-up work is intentionally not included as a result in this checkpoint:

```text
representative ~1 V write-condition freeze
→ longer Hold window
→ integrated Write → Hold → Read
→ T_RET,5% leakage integration
→ Mesh1/3 check
→ NonlocalPath ON/OFF attribution
```

Main progress documents:

- `docs/progress/run07_1t1c_retention_feasibility.md`
- `docs/progress/run07_hold100_completion_20260913.md`

Methodology traceability:

- `docs/methodology/run07_methodology_traceability.md`
