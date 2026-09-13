# FB-RC-01 — MEB-related gate-top depth / RWL proxy checkpoint

Date: 2026-09-13  
Scope: feedback-level practical trade-off evidence before retention synthesis  
Task: `T-RC-01`

## 1. Feedback question

The practical question is:

> If deeper MEB-related gate-top depth keeps suppressing GIDL, why not simply continue increasing the depth?

Literature motivates a counter-penalty: reducing the remaining lower metal-gate cross-section can increase word-line resistance and WL RC delay. The present CMP checkpoint does **not** directly simulate absolute `RWL` or RC delay. Instead, it quantifies the geometry penalty on the frozen 3-D baseline and compares it with the existing Run 6.5 GIDL benefit.

## 2. Method

A dedicated geometry-only branch was created from frozen `3D-Sun-B0 Geometry v05`.

Fixed geometry inputs include:

```text
Lgate    = 20 nm
Drecess  = 120 nm
Tox      = 5 nm
Wfin     = 17 nm
Rgate    = 10 nm
W bottom geometry = fixed rounded bottom
```

Only the MEB-related gate-top / `DBCAT` depth was swept:

```text
36 / 41 / 43 / 45 / 47 / 48 / 49 / 51 nm
```

The word-line current direction is `y`, so the relevant W conducting cross-section is the `x-z` section. In the current frozen geometry this section is a rectangular W body plus a rounded lower half-circle.

```text
A_W(d) = rectangular W area + rounded-bottom W area
```

With identical W resistivity and word-line length across cases:

```text
R ~ rho L / A
```

Therefore the project-internal normalized resistance proxy is

```text
RWL_proxy(d) = A_W(36 nm) / A_W(d)
```

This is a **geometry-derived normalized RWL proxy**, not an absolute or production-calibrated word-line resistance.

## 3. Results

| Depth | W cross-section [nm^2] | W-area loss vs 36 nm | RWL proxy | RWL proxy penalty | GIDL @300 K [A] | GIDL suppression vs 36 nm |
|---:|---:|---:|---:|---:|---:|---:|
| 36 | 1537.08 | 0.00% | 1.0000 | 0.00% | 1.3777737e-14 | 0.00% |
| 41 | 1437.08 | 6.51% | 1.0696 | 6.96% | 7.7683012e-15 | 43.62% |
| 43 | 1397.08 | 9.11% | 1.1002 | 10.02% | 5.6821000e-15 | 58.76% |
| 45 | 1357.08 | 11.71% | 1.1326 | 13.26% | 3.9345000e-15 | 71.44% |
| 47 | 1317.08 | 14.31% | 1.1670 | 16.70% | 2.0128000e-15 | 85.39% |
| 48 | 1297.08 | 15.61% | 1.1850 | 18.50% | 1.9375000e-15 | 85.94% |
| 49 | 1277.08 | 16.92% | 1.2036 | 20.36% | 1.8860000e-15 | 86.31% |
| 51 | 1237.08 | 19.52% | 1.2425 | 24.25% | 3.2571000e-16 | 97.64%* |

`*` The 51 nm terminal-current point remains a low-current/background-sensitive boundary reference and is excluded from the main ranking interpretation.

## 4. Trade-off interpretation

The key observation is the `47–49 nm` region.

```text
47 -> 48 nm:
  terminal GIDL additional decrease ≈ 3.74%
  normalized RWL proxy additional increase ≈ 1.54%

48 -> 49 nm:
  terminal GIDL additional decrease ≈ 2.66%
  normalized RWL proxy additional increase ≈ 1.57%
```

Thus the existing transistor-level data show a diminishing-return region: deeper gate-top depth continues to reduce GIDL, but the incremental GIDL benefit becomes small while the geometry-derived W-resistance penalty continues to increase.

Presentation-safe interpretation:

> Increasing the MEB-related gate-top depth suppresses GIDL, but the remaining tungsten cross-section simultaneously decreases. Around the 47–49 nm region, the incremental GIDL benefit becomes small while the normalized RWL proxy continues to increase. Therefore minimum GIDL alone is not sufficient to define the final MEB design point.

## 5. What this checkpoint does and does not prove

Supported:

- same frozen 3-D geometry was used for all cases except gate-top depth;
- W conducting cross-section decreases monotonically with depth;
- a normalized `1/A_W` resistance proxy therefore increases monotonically;
- the proxy can be combined with existing Run 6.5 GIDL data to expose a practical trade-off / diminishing-return region.

Not supported yet:

- absolute tungsten word-line resistance;
- distributed array resistance;
- actual WL RC delay;
- read/write delay degradation caused by the proxy;
- a final optimum at 47, 48, or 49 nm;
- a final effective MEB range before cell-level retention evidence is available.

## 6. Next action

No additional TCAD simulation is required for this proxy branch before the retention comparison.

Resume after the retention protocol is frozen and MEB-dependent cell data are available:

```text
GIDL suppression
        +
retention improvement
        +
DC / cell guardrails
        +
geometry-derived RWL penalty
        ↓
effective MEB design range
```

A later MixedMode / circuit-level WL-RC sensitivity study is optional and should be added only if the final design-range conclusion requires stronger read/write-speed evidence.

## 7. Evidence map

```text
code/sde/tradeoff/bcat_3d_rwl_proxy_sweep.cmd
data/tradeoff/rwl_proxy_tradeoff_20260913.csv
assets/images/feedback/20260913_tradeoff/01_gidl_rwl_tradeoff.svg
```

Raw SDE logs and SVisual screenshots remain workspace evidence unless later reproducibility or presentation needs require explicit archival.
