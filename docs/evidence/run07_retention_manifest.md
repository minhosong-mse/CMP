# Run 07 Evidence Manifest — 1T1C / Retention Feasibility

Status: **B0-v1 cell-operation feasibility expanded and processed; 300 K normalized Write/Hold/Read complete at feasibility level; 300/340/380 K approximately 1 V-normalized direct-Hold comparison complete; final retention-time metric still open**.

## 1. Scope and provenance

```text
B0 MEB_Depth = 0.036 um
Mesh_Code = 1
AreaFactor = 0.017
Ccell = 10 fF
Physics = established CMP NonlocalPath chain
```

## 2. Execution evidence table

| Branch | Accepted set | Processed summary | Status |
|---|---|---|---|
| R7B Write screen | AF=0.017 write matrix | `write_screen_af0017.csv` | PASS |
| R7A 300 K 1 V calibration | n409, 667 ns | `write_1v_calibration_af0017.csv` | PASS |
| R7C 100 ns Hold screen | complete 36 cases | `hold100_complete.csv` | PASS |
| R7C direct Hold | 300 K, 100 ns–100 us | `hold_direct_300k.csv` | PASS |
| R7E independent Read | D0/D1 reference | `read_window.csv` | PASS |
| R7E Read transfer | 13 VSN points | `read_transfer_vsn.csv` | PASS |
| Integrated W-H-R | 300 K, 100 ns/1 us/10 us | `whr_300k_norm.csv` | PASS — operation feasibility |
| Temperature Write calibration | 340 K 258 ns / 380 K 126.54 ns | `write_temp_calibration_af0017.csv` | PASS |
| Temperature-normalized direct Hold | 300/340/380 K × 4 Hold windows | `hold_temp_normalized_300_340_380.csv` | PASS — temperature trend |
| T_RET,5% leakage integration | pending | pending | not closed |
| Mesh1 vs Mesh3 | pending | pending | not closed |

## 3. Quantitative checkpoint

### Write normalization

```text
300 K -> 667 ns
340 K -> 258 ns
380 K -> 126.54 ns
```

### Temperature-normalized direct Hold

Actual direct-Hold settled starts:

```text
300 K: 1.000017733 V
340 K: 1.000107421 V
380 K: 1.000272165 V
```

100 us voltage loss:

```text
300 K: 0.270195 uV
340 K: 0.483889 uV
380 K: 7.438961 uV
```

Equivalent leakage scale Ccell*DeltaV/DeltaT:

```text
300 K: ~2.70e-17 A
340 K: ~4.84e-17 A
380 K: ~7.44e-16 A
380 K / 300 K: ~27.53 x
```

### Independent Read transfer

```text
D0 DeltaVBL = -72.12 mV
VSN=0.80 V   -> DeltaVBL = +17.92 mV, separation = 90.04 mV
VSN=0.9481 V -> DeltaVBL = +30.55 mV, separation = 102.67 mV
VSN=1.00 V   -> DeltaVBL = +35.14 mV, separation = 107.26 mV
```

### Integrated 300 K W-H-R

```text
100 ns / 1 us / 10 us Hold
DeltaVBL ≈ +35.6251 mV
```

## 4. Claim boundary

- The direct-Hold temperature comparison is approximately normalized near 1 V, not mathematically identical in starting VSN.
- 100 us stability/decay does not equal a measured retention time.
- 0.8 V is not a CMP read-fail voltage.
- No t_1.0→0.8 is reported from short-window extrapolation.
- No MEB-dependent retention conclusion is entered at this B0 checkpoint.
- AreaFactor=0.017 remains an effective-width proxy, not production calibration.

## 5. Presentation checkpoint

Use these current headline results:

1. 300 K Write: 667 ns -> ~1.000015 V.
2. Direct Hold temperature trend at 100 us: 0.270 uV / 0.484 uV / 7.439 uV for 300/340/380 K.
3. Equivalent leakage scale: ~27.5x increase from 300 K to 380 K.
4. Independent VSN -> DeltaVBL transfer.
5. Integrated 300 K W-H-R: +35.625 mV D1 BL signal for 100 ns–10 us Hold.

Detailed temperature-Hold evidence:
- `docs/evidence/run07_hold_temperature_normalized_20260921.md`

Cell-operation checkpoint:
- `docs/evidence/run07_cell_operation_checkpoint_20260920.md`

## 6. Next required evidence

```text
temperature-normalized integrated Write → Hold → Read at 340/380 K
→ leakage-vs-V integration if direct transient remains far from threshold
→ Mesh1/3 check
→ later MEB-dependent cell translation
```
