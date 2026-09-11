# Post-Presentation E-field / BTBT Validation — 2026-09-11

> **Feedback ID:** `FB-EFIELD-01` + minimal mesh audit `FB-MESH-01`  
> **Source data:** formal Run 4 / Run 5 31–36–41 nm GIDL-ON results, 300 K  
> **Scope:** supporting validation after the first topic presentation. This is **not** a new main research axis and does not reopen the extended 43–51 nm design-range search.

## 1. Why this validation was added

The existing formal Run 5 result showed a large sensitivity mismatch across MEB 31 → 41 nm:

- terminal GIDL endpoint: approximately **60.42% decrease**
- fixed-cut `E_wall,max`: approximately **1.69% decrease**

The presentation feedback asked whether the electric field should be evaluated in the actual GIDL / BTBT critical region, and whether a single peak-field metric is sufficient when the terminal leakage changes much more strongly.

The purpose of this validation is **not** to find an E-field metric that numerically reproduces the GIDL percentage. The purpose is to test whether the GIDL trend can be interpreted more defensibly from the **spatial E-field / BTBT behavior** in the actual critical region.

## 2. Literature-methodology rationale

Five BCAT / DRAM leakage papers were reviewed before the extraction method was frozen.

Common methodological pattern:

```text
physical GIDL / leakage critical region
→ spatial electric-field profile or map
→ representative peak / region metric when useful
→ terminal leakage or retention comparison
```

The two most relevant lessons for this feedback item were:

1. MEB / gate-structure changes can move or redistribute the field peak; therefore a fixed spatial point alone may miss part of the mechanism.
2. In Pi-BCAT literature, cases with similar peak field can still differ in BTBT-active spatial extent and integrated field. Therefore width / integral analysis is a justified conditional follow-up when a peak-only explanation is insufficient.

Important boundary:

- automatic `Band2BandGeneration`-maximum localization is a **CMP reproducibility rule**, not claimed as a universal literature standard;
- the normalized 10/20/50% BTBT threshold sensitivity is also a CMP quantitative implementation, not a threshold directly specified by the reviewed papers.

## 3. Frozen validation set and simulation condition

Validation set:

```text
MEB = 31 / 36 / 41 nm
31 nm = shallow side
36 nm = nominal baseline
41 nm = deeper side
```

Common formal GIDL condition:

```text
Mesh_Code = 3
T         = 300 K
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
GIDL      = |Idrain| @ VG=-0.7 V
```

Coordinate convention:

```text
X = wafer depth
Y = source-to-drain lateral direction
```

Existing common Mesh-GIDL refinement ROI:

```text
X = 0.032–0.070 um
Y = 0.112–0.133 um
local max/min = 1.0 / 0.25 nm
```

## 4. Measurement Protocol v1

### Phase A

For each MEB:

1. inspect `Band2BandGeneration` over the full silicon domain;
2. automatically extract `BTBT_max`, `X_hot`, and `Y_hot`;
3. verify the hotspot lies inside the common Mesh-GIDL ROI;
4. create an X-direction depth cut at the case-specific `Y_hot`;
5. export on the same cut:
   - `Band2BandGeneration`
   - `ElectricField-X`
   - `Abs(ElectricField-V)`
6. compare with:
   - existing fixed-cut `E_wall,max`
   - terminal GIDL endpoint.

All three extracted hotspots produced the same `Y_hot = 0.121875 um`, so the final 31/36/41 profile comparison uses the same Y cut.

### Phase B trigger

Phase B was activated because the hotspot-following directional peak field did **not** decrease with GIDL. Instead, `ElectricField-X` peak slightly increased from 31 to 41 nm.

Conditional Phase-B quantities:

- normalized BTBT-active-region width for `G/Gmax >= 10%, 20%, 50%`;
- `integral(|E| dx)` over each corresponding active region;
- 1-D `integral(G_BTBT dx)` as a spatial-generation trend cross-check.

The threshold is **not** selected to maximize correlation with GIDL. All three thresholds are retained as a sensitivity check. The 20% criterion may be used as a representative middle value in presentation tables, with the sensitivity results shown or retained as backup evidence.

## 5. Primary extracted results

| MEB (nm) | GIDL (A) | BTBTmax (cm^-3 s^-1) | Xhot (um) | Yhot (um) | Ex,peak (V/cm) | X at Ex peak (um) | Ex @ BTBTmax (V/cm) | hotspot-cut |E| peak (V/cm) | old E_wall,max (V/cm) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | 1.9624468e-14 | 1.1673607e22 | 0.051562496 | 0.121875 | 3.6277373e5 | 0.053124998 | 3.6001816e5 | 8.9800452e5 | 871969.09 |
| 36 | 1.3777737e-14 | 8.4182472e21 | 0.051562496 | 0.121875 | 3.7287684e5 | 0.052343745 | 3.7158875e5 | 8.8695786e5 | 867936.60 |
| 41 | 7.7683012e-15 | 5.5526998e21 | 0.052343745 | 0.121875 | 3.9235824e5 | 0.051562496 | 3.9195505e5 | 8.6638379e5 | 857194.93 |

31 → 41 nm change:

| Metric | Change |
|---|---:|
| GIDL endpoint | **-60.42%** |
| BTBTmax | **-52.43%** |
| hotspot-following `ElectricField-X` peak | **+8.16%** |
| `Ex @ BTBTmax` | **+8.87%** |
| hotspot-following `|E|` peak | **-3.52%** |
| old fixed-cut `E_wall,max` | **-1.69%** |

### Immediate Phase-A interpretation

A single local directional field peak is **not** a sufficient explanation for the GIDL trend in this validation set. `Ex,peak` slightly increases while GIDL decreases strongly.

The field-magnitude peak decreases, but only by a few percent. This confirms the original concern that peak field alone does not capture the full terminal-GIDL sensitivity.

## 6. Hotspot movement and mesh-ROI audit

| MEB (nm) | Xhot (um) | Yhot (um) | X-low margin (nm) | X-high margin (nm) | Y-low margin (nm) | Y-high margin (nm) |
|---:|---:|---:|---:|---:|---:|---:|
| 31 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 36 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 41 | 0.052343745 | 0.121875 | 20.344 | 17.656 | 9.875 | 11.125 |

Result:

- all three hotspots are comfortably inside the common Mesh-GIDL ROI;
- the 41 nm hotspot moves only about `0.781 nm` deeper in X relative to 31/36 nm;
- no re-mesh is required for this **feedback-level 31/36/41 coverage check**.

This does **not** prove absolute mesh-independent BTBT accuracy.

## 7. BTBT-active-region threshold sensitivity

Definition:

```text
BTBT-active region = contiguous X interval around the main BTBT peak
where G_BTBT(X) / G_BTBT,max >= threshold
```

### Active width

| Criterion | 31 nm | 36 nm | 41 nm | 31→41 change |
|---|---:|---:|---:|---:|
| 10% | 4.539 nm | 4.527 nm | 4.224 nm | -6.94% |
| 20% | 3.907 nm | 3.706 nm | 3.412 nm | -12.68% |
| 50% | 2.503 nm | 2.489 nm | 2.247 nm | -10.25% |

### Integrated field magnitude over the active region

| Criterion | 31 nm | 36 nm | 41 nm | 31→41 change |
|---|---:|---:|---:|---:|
| 10% | 0.36213 V | 0.35815 V | 0.32932 V | -9.06% |
| 20% | 0.31175 V | 0.29320 V | 0.26600 V | -14.68% |
| 50% | 0.19977 V | 0.19717 V | 0.17542 V | -12.19% |

The direction remains the same for all tested thresholds. Therefore the decreasing spatial extent / integrated-field trend is not an artifact of choosing only one threshold.

## 8. 1-D integrated BTBT generation

The full hotspot-following X-cut integral is:

| MEB (nm) | `integral(G_BTBT dx)` (cm^-2 s^-1) |
|---:|---:|
| 31 | 3.0806114e15 |
| 36 | 2.2570013e15 |
| 41 | 1.3017612e15 |

31 → 41 change:

```text
1-D integrated BTBT generation: -57.74%
terminal GIDL endpoint:         -60.42%
```

For the representative 20% active region:

| MEB (nm) | `integral(G_BTBT dx)` in 20% region (cm^-2 s^-1) |
|---:|---:|
| 31 | 2.8509672e15 |
| 36 | 2.0824812e15 |
| 41 | 1.1860155e15 |

31 → 41 change: **-58.40%**.

Interpretation boundary:

> The 1-D generation integral is **not** a direct calculation of terminal current. It is supporting evidence that the spatially integrated BTBT-generation trend is consistent with the terminal GIDL direction and has a similar reduction scale.

Do not present `integral(G_BTBT dx) = terminal GIDL`.

## 9. Consolidated interpretation

The validation supports the following limited statement:

> The large MEB-dependent GIDL reduction cannot be explained by a single local E-field maximum alone. Across 31/36/41 nm, the BTBT-generation amplitude and active spatial extent both decrease, while the integrated field over the BTBT-active region also decreases. The spatially integrated BTBT-generation trend is consistent with the terminal GIDL reduction. Therefore the GIDL trend is more defensibly interpreted from the **critical-region spatial E-field / BTBT distribution** than from one peak-field scalar.

This is a **mechanism-supporting interpretation**, not proof of a direct `Cgd → E-field → GIDL` causal law.

## 10. Claim guardrails

Supported:

- 31/36/41 nm all use the same formal GIDL condition.
- dominant BTBT hotspot remains inside the common Mesh-GIDL refinement ROI.
- hotspot movement is small over 31–41 nm.
- local `Ex` peak does not track the GIDL reduction.
- BTBT peak generation, active-region width, integrated active-region field, and 1-D integrated BTBT generation all decrease toward 41 nm.
- threshold sensitivity at 10/20/50% preserves the same spatial trend.

Not supported:

- the 20% threshold is a universal literature standard;
- the 1-D BTBT integral equals terminal current;
- the current validation proves absolute BTBT calibration;
- the current mesh audit proves full BTBT mesh independence;
- this feedback validation establishes the final MEB optimum or process window.

## 11. Data and figure index

Raw exported profiles:

```text
data/run05/feedback_efield_20260911/raw/
  31_BTBT.csv
  36_BTBT.csv
  41_BTBT.csv
  31_AbsE.csv
  36_AbsE.csv
  41_AbsE.csv
  31_Ex.csv
  36_Ex.csv
  41_Ex.csv
```

Processed data:

```text
data/run05/feedback_efield_20260911/processed/
  efield_btbt_validation_summary.csv
  btbt_threshold_sensitivity.csv
  btbt_profiles_31_36_41.csv
  abse_profiles_31_36_41.csv
  ex_profiles_31_36_41.csv
```

Curated plots:

```text
assets/images/feedback/20260911_efield/
  01_btbt_profiles.svg
  02_abse_profiles.svg
  03_ex_profiles.svg
  04_normalized_metric_trends.svg
  05_threshold_width_sensitivity.svg
  06_hotspot_roi_coverage.svg
```

Raw SVisual screenshots are stored in the same image folder under `raw_svisual/` for audit / backup use.

## 12. Presentation use

Recommended main/backup split:

- **Main or core backup:** normalized metric trend + hotspot-following BTBT profile.
- **Method backup:** hotspot ROI coverage and the 31/36/41 extraction protocol.
- **Deep Q&A backup:** 10/20/50% threshold sensitivity.
- **Do not center the entire presentation around this validation.** It exists to strengthen one interpretation link inside the larger MEB → GIDL → retention research flow.
