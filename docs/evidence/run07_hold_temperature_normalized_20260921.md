# Run 07 — Temperature-Normalized Direct Hold (300 / 340 / 380 K)

Date: 2026-09-21  
Scope: B0=36 nm, Mesh1, AreaFactor=0.017, Ccell=10 fF, direct floating-SN Hold.

## 1. Normalization anchors

Write times were calibrated so each temperature begins Hold near 1 V:

| Temperature | Twrite | actual direct-Hold VSN start | error from 1 V |
|---:|---:|---:|---:|
| 300 K | 667 ns | 1.000017733 V | +0.00177% |
| 340 K | 258 ns | 1.000107421 V | +0.01074% |
| 380 K | 126.54 ns | 1.000272165 V | +0.02722% |

The direct-Hold deck therefore achieves an approximately common 1 V start. The 380 K start is slightly above the standalone calibration result, so final temperature claims should be described as approximately normalized rather than mathematically identical.

## 2. Direct Hold results

| T | 100 ns | 1 us | 10 us | 100 us |
|---:|---:|---:|---:|---:|
| 300 K | 0.270 nV | 2.702 nV | 27.020 nV | 0.270195 uV |
| 340 K | 0.4839 nV | 4.8389 nV | 48.389 nV | 0.483889 uV |
| 380 K | 7.439 nV | 74.390 nV | 0.743900 uV | 7.438961 uV |

At every temperature, DeltaVSN scales approximately with the tested Hold duration over 100 ns–100 us, which is consistent with the nearly constant leakage scale across each short transient window.

## 3. Equivalent leakage scale

Using Ccell*DeltaV/DeltaT only as a transient-equivalent leakage scale:

```text
300 K ≈ 2.70e-17 A
340 K ≈ 4.84e-17 A
380 K ≈ 7.44e-16 A
```

At 100 us:

```text
340 / 300 ≈ 1.79 x
380 / 340 ≈ 15.37 x
380 / 300 ≈ 27.53 x
```

This establishes a clear temperature dependence of the floating-node decay in the tested B0 condition, with a particularly strong increase at 380 K.

## 4. Interpretation boundary

- The result is a temperature-normalized direct-Hold trend, not a measured physical retention time.
- None of the tested transients reaches VSN=0.8 V.
- Do not extrapolate t_1.0→0.8 from the 100 us slope.
- The equivalent leakage scale is derived from capacitor voltage loss and is not a substitute for a full leakage-vs-V integration.
- No MEB-depth comparison is made here; this remains a B0 protocol/result checkpoint.

## 5. Presentation-safe statement

> With the storage node initialized near 1 V at each temperature, the 100 us voltage loss increased from about 0.270 uV at 300 K to 0.484 uV at 340 K and 7.439 uV at 380 K. The corresponding transient-equivalent leakage scale increased by about 27.5x from 300 K to 380 K.

Processed source:
- `data/run07/processed/hold_temp_normalized_300_340_380.csv`
