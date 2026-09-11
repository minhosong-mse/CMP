# R7 Evidence — 100 ns Floating-Hold Screen (Partial Snapshot)

## Purpose
Verify that the storage node remains genuinely floating after write and inspect short-time VSN stability before attempting longer retention windows.

## Method
- `Set(sn=0)` is used only for initial condition.
- `Unset(sn)` releases the storage node before transient.
- Write pulse is applied.
- After WL/BL falling-edge settling, Hold is evaluated.
- Hold metric start is defined near `Twrite + 2 ns`.
- Short-hold endpoint is approximately +100 ns from that reference.

## Processed subset

| node | AF | VWL_ON [V] | Twrite [ns] | VSN hold-start [V] | VSN +100 ns [V] | Delta VSN [V] |
|---:|---:|---:|---:|---:|---:|---:|
| 179 | 0.011 | 2.0 | 100 | 0.400957143 | 0.400957143 | 5.860e-13 |
| 191 | 0.011 | 2.0 | 200 | 0.444792564 | 0.444792564 | 6.500e-13 |
| 203 | 0.011 | 2.0 | 300 | 0.468481043 | 0.468481043 | 6.470e-13 |
| 183 | 0.017 | 2.0 | 100 | 0.428387852 | 0.428387852 | 9.720e-13 |
| 194 | 0.017 | 1.5 | 200 | 0.190978612 | 0.190978612 | 5.970e-13 |
| 195 | 0.017 | 2.0 | 200 | 0.469644635 | 0.469644635 | 1.054e-12 |

## Interpretation
All processed cases show 100 ns VSN changes of only about `1e-13 ~ 1e-12 V`. This is treated as **numerical-floor-level change**, not a physically resolved retention decay.

Therefore:
- floating-node Hold implementation: **feasibility PASS**
- 100 ns short-hold stability: **PASS**
- retention time: **not extracted**

The full 36-case screen should be added later; this file intentionally records the currently processed snapshot without inventing missing cases.

Processed source:

- `data/run07/processed/hold100_partial.csv`
