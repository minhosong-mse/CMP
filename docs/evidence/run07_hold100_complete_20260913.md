# R7 Evidence — 100 ns Floating-Hold Screen (Complete 36-Case Matrix)

Date: 2026-09-13  
Scope: B0-v1 short-Hold feasibility only. This document does **not** claim a physical retention time.

## Purpose

Close the previously partial 100 ns floating-storage-node Hold screen by processing the complete 36-case matrix:

```text
AreaFactor = 0.011 / 0.017 / 0.023
VWL_ON     = 1.5 / 2.0 / 2.5 / 3.0 V
Twrite     = 100 / 200 / 300 ns
Thold      = 100 ns
MEB        = 0.036 um
Mesh_Code  = 1
T          = 300 K
Ccell      = 10 fF
VBL_WRITE  = 1.2 V
VWL_HOLD   = -0.7 V
```

Total:

```text
3 AreaFactor × 4 VWL_ON × 3 Twrite = 36 cases
```

## Method

- `Set(sn=0)` is used only for the initial condition.
- `Unset(sn)` releases the storage node before the transient.
- The Write pulse charges the floating storage node.
- WL and BL return to the Hold biases after Write.
- Switching-settling behavior is excluded from the Hold metric.
- Hold start is evaluated at:

```text
t_hold,start = Twrite + 2 ns
```

- The short-Hold endpoint is:

```text
t_hold,end = t_hold,start + 100 ns
```

- `VSN` values are obtained from the complete MixedMode system waveform by linear interpolation at those two timestamps.

Each accepted waveform contains 1001 saved points.

## Complete-screen result

All 36 cases remain numerically stable over the 100 ns Hold window.

Across the complete matrix:

```text
maximum |DeltaVSN_100ns| = 2.465920e-10 V
maximum |fractional loss| = 2.548440e-08 %
case with largest |DeltaVSN| = n213
```

The largest measured change is therefore far below a physically meaningful storage-voltage decay and is treated as **numerical-floor-level behavior** for this short window.

The sign of the tiny `DeltaVSN` values is not interpreted physically; a few low-signal cases show equally tiny opposite-sign changes at the numerical floor.

## Representative nominal-width case

The strongest 300 ns nominal-width (`AreaFactor=0.017`) case is n209:

```text
AreaFactor       = 0.017
VWL_ON           = 3.0 V
Twrite           = 300 ns
VSN_hold_start   = 0.948118339190 V
VSN_hold_+100ns  = 0.948118339047 V
DeltaVSN_100ns   = 1.432444e-10 V
```

This confirms that the earlier representative D1 candidate also remains stable over the 100 ns short-Hold interval after switching settling is excluded.

## Highest Hold-start state in the 36-case matrix

The highest Hold-start voltage within this complete 36-case screen occurs at n213:

```text
AreaFactor = 0.023
VWL_ON     = 3.0 V
Twrite     = 300 ns
VSN_start  = 0.967619197546 V
```

This is reported only as a matrix endpoint. It does not replace the nominal-width `AreaFactor=0.017` branch or freeze a final Write condition.

## Interpretation

This completed screen establishes:

- floating-SN Hold implementation: **PASS at feasibility level**
- complete 36-case 100 ns short-Hold stability: **PASS**
- switching settling and Hold loss: **kept separate**
- physically resolved retention decay: **not observed within 100 ns**
- retention time: **not extracted**

The result must **not** be phrased as a long retention-time measurement. It only shows that no meaningful storage-node decay is resolved in the tested 100 ns window.

## Processed data

- `data/run07/processed/hold100_complete.csv`

Historical partial snapshot:

- `docs/evidence/run07_hold100_partial_20260911.md`
- `data/run07/processed/hold100_partial.csv`

The partial files are retained for provenance; this 2026-09-13 complete matrix supersedes them for the 100 ns Hold-screen status.

## Claim boundary

Allowed:

> The complete 36-case B0 1T1C short-Hold matrix remained stable over 100 ns after write-edge settling, with the largest absolute storage-node change only about `2.47e-10 V`.

Not allowed:

- `Retention time = X`
- long-term retention is validated
- the final Write condition is frozen
- integrated Write→Hold→Read is complete
- production/calibrated retention behavior is reproduced
