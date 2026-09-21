# Run 07 Cell-Operation Checkpoint — updated 2026-09-21

Scope: **B0-v1 methodology feasibility / presentation checkpoint**.  
Geometry: **MEB_Depth = 0.036 um (36 nm)**.

## 1. Executed chain

```text
Write to ~1 V
→ 300 K direct floating Hold to 100 us
→ independent Read transfer
→ integrated Write → Hold → Read at 300 K
→ 340/380 K Write normalization
→ 300/340/380 K approximately normalized direct-Hold comparison
```

No physical retention time is frozen yet.

## 2. Write normalization anchors

| Temperature | Twrite | calibration VSN |
|---:|---:|---:|
| 300 K | 667 ns | 1.00001465 V |
| 340 K | 258 ns | 1.00009888 V |
| 380 K | 126.54 ns | 1.00009202 V |

## 3. Temperature-normalized direct Hold

Actual direct-Hold settled starts were 1.000017733 V, 1.000107421 V and 1.000272165 V at 300/340/380 K respectively.

| T | DeltaVSN @ 100 ns | @ 1 us | @ 10 us | @ 100 us |
|---:|---:|---:|---:|---:|
| 300 K | 0.270 nV | 2.702 nV | 27.020 nV | 0.270195 uV |
| 340 K | 0.4839 nV | 4.8389 nV | 48.389 nV | 0.483889 uV |
| 380 K | 7.439 nV | 74.390 nV | 0.743900 uV | 7.438961 uV |

Equivalent leakage scale:

```text
300 K ~ 2.70e-17 A
340 K ~ 4.84e-17 A
380 K ~ 7.44e-16 A
380 / 300 ~ 27.53 x
```

This is the strongest new temperature-dependent Hold evidence for presentation, but it remains a short-window direct-transient result rather than a retention-time extraction.

## 4. Independent Read transfer

| VSN init | Delta VBL | D0/D1 separation |
|---:|---:|---:|
| 0.80 V | +17.92 mV | 90.04 mV |
| 0.9481 V | +30.55 mV | 102.67 mV |
| 1.00 V | +35.14 mV | 107.26 mV |

D0 reference: DeltaVBL = -72.12 mV.

## 5. Integrated 300 K Write → Hold → Read

| Thold | Hold loss | Delta VBL |
|---:|---:|---:|
| 100 ns | 0.261 nV | +35.6251 mV |
| 1 us | 2.701 nV | +35.6251 mV |
| 10 us | 27.01 nV | +35.6251 mV |

300 K integrated operation feasibility is PASS for the tested Hold windows.

## 6. Presentation-safe claims

> With VSN initialized near 1 V, the 100 us floating-node voltage loss increased from about 0.270 uV at 300 K to 0.484 uV at 340 K and 7.439 uV at 380 K, corresponding to about a 27.5x increase in the transient-equivalent leakage scale from 300 K to 380 K.

> At 300 K, an actual Write→Hold→Read sequence retained an approximately +35.6 mV D1 bitline signal for 100 ns–10 us Hold.

Not supported yet:
- Retention time = X
- measured t_1.0→0.8
- final temperature-dependent W-H-R result at 340/380 K
- final MEB-dependent retention conclusion
- production-calibrated retention or refresh improvement
