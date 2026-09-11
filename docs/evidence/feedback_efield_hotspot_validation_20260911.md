# E-field / BTBT Critical-Region Validation — First Presentation Feedback

**Date:** 2026-09-11  
**Feedback ID:** `FB-EFIELD-01`  
**Task:** `T-EFIELD-01`  
**Status:** **Completed — presentation-feedback level**  
**Source:** Run 4–5 formal 31/36/41 nm GIDL data at 300 K

## 1. Why this validation was added

The original Run 5 comparison used a reproducible fixed drain-side wall metric:

```text
Field     = Abs(ElectricField-V)
cutline   = Y = 0.116 um
X range   = 0.032–0.070 um
metric    = E_wall,max
```

Across MEB `31 -> 41 nm`, the terminal GIDL endpoint decreased by about `60.42%`, while the old fixed-cut `E_wall,max` decreased by only about `1.69%`.

The presentation feedback therefore asked whether:

1. the electric field should be checked in the actual GIDL / BTBT critical region;
2. a moving or redistributed hotspot makes the old fixed cut incomplete;
3. a single peak electric-field scalar is enough to interpret the terminal GIDL trend.

This validation was **not** intended to create a new main research axis or to find a field metric whose percentage change must numerically equal the GIDL percentage. It is a supporting mechanism check for the existing MEB–GIDL result.

## 2. Literature-grounded reasoning used before extraction

Five BCAT / DRAM leakage studies were reviewed before fixing the protocol.

| Literature role | Methodological point carried into CMP |
|---|---|
| Lee et al. 2020, Pi-BCAT | E-field and BTBT spatial profiles can provide more information than peak E alone; BTBT-region width / integrated field are useful when peak field is insufficient |
| Lim & Kwon 2022, multi-gate BCAT | Drain-side field redistribution and terminal GIDL are interpreted together rather than by a global-domain Emax |
| Jang & Kim 2026, MEB/PEB variation | MEB/PEB changes can move / reshape field peaks; depth-direction field profiles are examined before reducing to a scalar maximum |
| Kim et al. 2021, retention degradation | Leakage-sensitive drain critical region is identified spatially before linking local physics to leakage / retention |
| Park et al. 2024, DWF-BCAT | GIDL is discussed using a physically defined gate/drain high-field region and vertical field profile |

Common logic used for CMP:

```text
physical GIDL / leakage critical region
→ spatial E-field / BTBT profile
→ representative regional metric if needed
→ terminal leakage comparison
```

CMP-specific additions for reproducibility:

- automatic `Band2BandGeneration` maximum localization;
- common drain-side ROI coverage check;
- case-following X-cut at `Y_hot`;
- 10/20/50% normalized `G/Gmax` sensitivity only if peak-only evidence is insufficient.

The automatic hotspot search and normalized-threshold rule are CMP implementation choices, not claimed as universal literature standards.

## 3. Frozen validation set

```text
MEB       = 31 / 36 / 41 nm
T         = 300 K
Mesh      = Mesh_Code 3
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2Band(Model=NonlocalPath)
terminal  = |Idrain| @ VG=-0.7 V
```

Why these three points:

```text
31 nm = shallow-side reference
36 nm = literature-based nominal B0
41 nm = deeper-side reference
```

This is the original formal shallow / nominal / deeper screening set, not a new design-range optimization sweep.

Coordinate convention:

```text
X = wafer depth
Y = source-to-drain lateral direction
```

Existing common Mesh-GIDL ROI:

```text
X = 0.032–0.070 um
Y = 0.112–0.133 um
```

## 4. Phase A — hotspot-following spatial extraction

For each MEB case:

1. use the final GIDL-ON TDR at `VG=-0.7 V`;
2. search full-Si `Band2BandGeneration` maximum;
3. record `BTBT_max`, `X_hot`, `Y_hot`;
4. verify that the hotspot is inside the existing common Mesh-GIDL ROI;
5. generate an X-direction cut at the extracted `Y_hot`;
6. export `Band2BandGeneration`, `ElectricField-X`, and `Abs(ElectricField-V)`;
7. compare the profile / peak behavior against old `E_wall,max` and terminal GIDL.

All three cases returned:

```text
Y_hot = 0.121875 um
```

### Phase-A quantitative results

| MEB | GIDL (A) | BTBTmax (cm^-3 s^-1) | Xhot (um) | Ex peak (V/cm) | X at Ex peak (um) | Ex at BTBTmax (V/cm) | |E| peak (V/cm) | X at |E| peak (um) | old E_wall,max (V/cm) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | 1.9624468e-14 | 1.1673607e22 | 0.051562496 | 3.6277373e5 | 0.053124998 | 3.6001816e5 | 8.9800452e5 | 0.043749996 | 871969.09 |
| 36 | 1.3777737e-14 | 8.4182472e21 | 0.051562496 | 3.7287684e5 | 0.052343745 | 3.7158875e5 | 8.8695786e5 | 0.044531245 | 867936.60 |
| 41 | 7.7683012e-15 | 5.5526998e21 | 0.052343745 | 3.9235824e5 | 0.051562496 | 3.9195505e5 | 8.6638379e5 | 0.046093747 | 857194.93 |

31 -> 41 nm:

```text
GIDL endpoint                  -60.42%
BTBT_max                       -52.43%
hotspot-cut |E| peak            -3.52%
old fixed E_wall,max            -1.69%
ElectricField-X peak            +8.16%
```

Phase A therefore showed that neither the old fixed peak nor the hotspot-following directional peak alone adequately represents the terminal GIDL sensitivity.

## 5. Phase B — BTBT-active-region spatial check

Phase B was activated because peak-field behavior alone remained insufficient.

A normalized BTBT-active interval was defined for sensitivity testing:

```text
G_BTBT(X) / G_BTBT,max >= alpha
alpha = 0.10 / 0.20 / 0.50
```

The active interval is the continuous peak-containing X-region satisfying the criterion.

### Threshold sensitivity

| MEB | criterion | X-left (um) | X-right (um) | active width (nm) | int(|E| dx) (V) | int(G_BTBT dx) in active region (cm^-2 s^-1) |
|---:|---:|---:|---:|---:|---:|---:|
| 31 | 10% | 0.049308492 | 0.053847740 | 4.539247 | 0.362127 | 2.961689e15 |
| 31 | 20% | 0.049627628 | 0.053534555 | 3.906927 | 0.311751 | 2.850967e15 |
| 31 | 50% | 0.050344014 | 0.052847427 | 2.503414 | 0.199773 | 2.313207e15 |
| 36 | 10% | 0.049627708 | 0.054154571 | 4.526864 | 0.358152 | 2.178084e15 |
| 36 | 20% | 0.050054648 | 0.053760919 | 3.706270 | 0.293199 | 2.082481e15 |
| 36 | 50% | 0.050635819 | 0.053125240 | 2.489421 | 0.197168 | 1.723950e15 |
| 41 | 10% | 0.050313530 | 0.054537949 | 4.224419 | 0.329318 | 1.253714e15 |
| 41 | 20% | 0.050726653 | 0.054138273 | 3.411620 | 0.265998 | 1.186016e15 |
| 41 | 50% | 0.051272803 | 0.053519564 | 2.246761 | 0.175417 | 9.715285e14 |

All 10/20/50% criteria retain the same overall trend: the BTBT-active width and active-region integrated field decrease as MEB increases.

The 20% value is used only as a representative middle criterion:

| MEB | 20% active width (nm) | 20% int(|E| dx) (V) | full-cut 1-D int(G_BTBT dx) (cm^-2 s^-1) |
|---:|---:|---:|---:|
| 31 | 3.906927 | 0.311751 | 3.080611e15 |
| 36 | 3.706270 | 0.293199 | 2.257001e15 |
| 41 | 3.411620 | 0.265998 | 1.301761e15 |

31 -> 41 nm:

```text
20% BTBT-active width          -12.68%
20% active-region int(|E| dx)  -14.68%
1-D integrated BTBT            -57.74%
GIDL endpoint                  -60.42%
```

The 1-D BTBT integral shows a decrease of similar direction and magnitude to terminal GIDL, but it is a spatial-generation trend cross-check only. It is **not** a terminal-current calculation.

## 6. Supported interpretation

> The large MEB-dependent GIDL reduction is not adequately represented by one local electric-field maximum. In the 31/36/41 nm validation set, BTBT-generation amplitude decreases strongly, the BTBT-active spatial extent narrows, and the field integrated over the active BTBT region decreases. The spatially integrated BTBT-generation trend is consistent with the terminal GIDL decrease. The mechanism is therefore more defensibly discussed from the **critical-region spatial E-field / BTBT distribution** than from one peak-field scalar.

This supports the existing MEB-dependent GIDL trend without requiring the field percentage to numerically match the GIDL percentage.

## 7. Preliminary mesh-coverage checkpoint

This work also generated a preliminary checkpoint for the separate mesh-feedback task.

| MEB | Xhot (um) | Yhot (um) | X-low margin (nm) | X-high margin (nm) | Y-low margin (nm) | Y-high margin (nm) |
|---:|---:|---:|---:|---:|---:|---:|
| 31 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 36 | 0.051562496 | 0.121875 | 19.562 | 18.438 | 9.875 | 11.125 |
| 41 | 0.052343745 | 0.121875 | 20.344 | 17.656 | 9.875 | 11.125 |

All three hotspots are comfortably inside the existing common ROI. This is only an ROI-coverage checkpoint and **does not close the separate mesh-setting feedback**. The next task will prepare per-MEB mesh evidence / screenshots and the explanation for why the common refinement remains appropriate.

## 8. Interpretation guardrails

Do not claim:

- the 20% threshold is a universal literature standard;
- 1-D `int(G_BTBT dx)` equals terminal current;
- absolute BTBT calibration;
- absolute mesh independence;
- direct `Cgd -> E-field -> GIDL` causality;
- that this validation is the main research objective.

Allowed wording:

- peak field alone was insufficient to represent the observed GIDL sensitivity;
- BTBT amplitude and spatial extent both decrease over the validation set;
- active-region integrated field decreases consistently across 10/20/50% threshold sensitivity;
- the spatial BTBT trend is consistent with the terminal GIDL decrease;
- this is supporting evidence for the existing MEB-GIDL interpretation.

## 9. Curated evidence files

Numeric data:

```text
data/run05/feedback_efield_20260911/
  README.md
  efield_btbt_validation_summary.csv
  btbt_threshold_sensitivity.csv
  metric_changes_31_to_41.csv
```

Curated figures:

```text
assets/images/feedback/20260911_efield/
  01_btbt_profiles.svg
  02_abse_profiles.svg
  03_normalized_metric_trends.svg
  04_threshold_width_sensitivity.svg
  05_integrated_field_sensitivity.svg
  06_hotspot_roi_coverage.svg
```

The repository figures are regenerated from the extracted numeric data for reproducibility.

## 10. Close-out state

`FB-EFIELD-01` is closed at **presentation-feedback level**.

Reopen only if the later undergraduate-thesis stage requires a broader MEB range, 2-D BTBT-generation integration, additional mesh-convergence quantification, or experimentally calibrated absolute leakage comparison.

The main project now returns to the remaining first-presentation feedback tasks rather than expanding this supporting validation further.
