# Run 07 — Temperature-Normalized Integrated Write → Hold → Read

Date: 2026-09-23  
Scope: B0=36 nm, Mesh1, AreaFactor=0.017, Ccell=10 fF, CBL=45 fF.

All 300/340/380 K cases were rerun with the same ramped high-temperature-convergence deck so the temperature comparison does not mix old abrupt-step and new ramped sequences.

## 1. Matrix

```text
300 K: Twrite = 667 ns
340 K: Twrite = 258 ns
380 K: Twrite = 126.54 ns

Thold = 100 ns / 1 us / 10 us
```

## 2. Integrated results

| T | Thold | VSN hold-start | Hold loss | VSN before Read | DeltaVBL |
|---:|---:|---:|---:|---:|---:|
| 300 K | 100 ns | 1.000026514 V | 0.270 nV | 1.000042460 V | +35.841458 mV |
| 300 K | 1 us | 1.000026514 V | 2.702 nV | 1.000042458 V | +35.841458 mV |
| 300 K | 10 us | 1.000026514 V | 27.022 nV | 1.000042434 V | +35.841456 mV |
| 340 K | 100 ns | 1.000170588 V | 0.484 nV | 1.000186678 V | +45.004795 mV |
| 340 K | 1 us | 1.000170588 V | 4.842 nV | 1.000186673 V | +45.004794 mV |
| 340 K | 10 us | 1.000170588 V | 48.418 nV | 1.000186630 V | +45.004790 mV |
| 380 K | 100 ns | 1.000372782 V | 7.440 nV | 1.000389042 V | +53.187687 mV |
| 380 K | 1 us | 1.000372782 V | 74.400 nV | 1.000388975 V | +53.187680 mV |
| 380 K | 10 us | 1.000372782 V | 0.744004 uV | 1.000388306 V | +53.187607 mV |

## 3. Main observations

- Integrated Write→Hold→Read completes successfully at all three temperatures and all tested Hold windows.
- The Hold-loss trend reproduces the direct-Hold temperature dependence: 380 K has the largest storage-node decay.
- Within 100 ns–10 us, the Hold-induced change in DeltaVBL is extremely small because the storage-node loss remains very small.
- The absolute D1 DeltaVBL increases with temperature in this ramped integrated sequence: about 35.84 mV at 300 K, 45.00 mV at 340 K and 53.19 mV at 380 K.
- This temperature dependence of the Read signal must not be interpreted as improved retention. It reflects the temperature dependence of the full read operation/transistor response under the current setup.

Relative to the 300 K 100 ns case:

```text
340 K DeltaVBL: +25.57 %
380 K DeltaVBL: +48.40 %
```

## 4. Claim boundary

- The result closes temperature-normalized integrated operation feasibility, not a physical retention-time metric.
- The three Hold-start values are approximately 1 V-normalized, not mathematically identical.
- No t_1.0→0.8 is extracted from these short windows.
- No MEB-depth retention improvement is claimed here.
- Because DeltaVBL itself is temperature dependent, retention-induced Read degradation should be separated from intrinsic temperature-dependent Read response before using Read margin as a retention metric across temperatures.

Processed source:
- `data/run07/processed/whr_temp_normalized_300_340_380.csv`
