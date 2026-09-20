# Run 07 Cell-Operation Checkpoint — 2026-09-20

Scope: **B0-v1 methodology feasibility / presentation checkpoint**.  
Geometry: **MEB_Depth = 0.036 um (36 nm)**.  
This checkpoint intentionally excludes the currently running 340/380 K temperature-normalized long-Hold matrix.

## 1. What is now executed

```text
Write to ~1 V
→ floating-SN direct Hold
→ independent Read transfer
→ integrated Write → Hold → Read at 300 K
→ temperature-specific Write-to-1 V normalization at 340/380 K
```

No physical retention time is frozen yet.

## 2. Write normalization anchors

| Temperature | Twrite | settled Hold-start VSN | status |
|---:|---:|---:|---|
| 300 K | 667 ns | 1.00001464973547 V | PASS / reference |
| 340 K | 258 ns | 1.00009888 V | PASS |
| 380 K | 126.54 ns | 1.00009202 V | PASS |

The 1 V state is a literature-compatible normalization benchmark, not a universal DRAM operation voltage.

Processed source:
- `data/run07/processed/write_1v_calibration_af0017.csv`
- `data/run07/processed/write_temp_calibration_af0017.csv`

## 3. 300 K direct floating Hold

Condition:

```text
AF = 0.017
Twrite = 667 ns
Ccell = 10 fF
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

At 100 us, the node remains near 1 V and the 0.8 V criterion is not reached.

Interpretation boundary:
- this is direct transient stability/decay evidence;
- it is **not** a measured `t_1.0→0.8`;
- do not extrapolate a retention time from the near-linear short-window slope.

Processed source:
- `data/run07/processed/hold_direct_300k.csv`

## 4. Independent Read transfer: VSN → BL signal

The Read-B sweep established a monotonic transfer from storage-node voltage to bitline signal.

Selected points:

| VSN init | Delta VBL | D0/D1 final BL separation |
|---:|---:|---:|
| 0.80 V | +17.92 mV | 90.04 mV |
| 0.9481 V | +30.55 mV | 102.67 mV |
| 1.00 V | +35.14 mV | 107.26 mV |

D0 remains the independent reference:

```text
D0 DeltaVBL = -72.12 mV
```

The 0.8 V point still produces a positive D1 read signal in this CMP setup; therefore 0.8 V is a literature-compatible retention criterion, **not an automatically derived read-fail threshold**.

Processed source:
- `data/run07/processed/read_transfer_vsn.csv`

## 5. Integrated 300 K Write → Hold → Read

Normalized 300 K condition:

```text
Twrite = 667 ns
VSN_hold_start ≈ 1.0000284 V
CBL = 45 fF
VBL_PRE = 0.5 V
Tread = 10 ns
```

| Thold | Hold loss | VSN before Read | Delta VBL |
|---:|---:|---:|---:|
| 100 ns | 0.261 nV | 1.000044347 V | +35.6251 mV |
| 1 us | 2.701 nV | 1.000044344 V | +35.6251 mV |
| 10 us | 27.01 nV | 1.000044320 V | +35.6251 mV |

Thus the 300 K integrated sequence is accepted as **operation-feasibility PASS** for the tested Hold windows.

The small Write-off settling from about 1.002 V to about 1.000 V occurs before the settled Hold metric and is not counted as retention loss.

Processed source:
- `data/run07/processed/whr_300k_norm.csv`

## 6. Presentation-safe claims

Supported now:

> At B0=36 nm, the 300 K 1T1C MixedMode cell was normalized to approximately 1 V, remained stable through direct floating Hold up to 100 us in the tested transient window, and completed an integrated Write→Hold→Read sequence with approximately +35.6 mV D1 bitline signal for 100 ns–10 us Hold.

Also supported:

> Independent Read transfer shows that lower VSN reduces the D1 bitline signal and D0/D1 separation, providing a cell-level link between storage-node degradation and read margin.

Not supported yet:

- `Retention time = X`
- measured `t_1.0→0.8`
- final temperature-dependent retention comparison
- final MEB-dependent retention conclusion
- production-calibrated retention or refresh improvement

## 7. Current next step — intentionally excluded from this checkpoint

The following matrix is running and is **not registered as completed evidence here**:

```text
340 K: Twrite = 258 ns
380 K: Twrite = 126.54 ns

Thold = 100 ns / 1 us / 10 us / 100 us
```

After those eight nodes are processed, the 300/340/380 K direct-Hold comparison can be registered on an approximately common 1 V starting state.
