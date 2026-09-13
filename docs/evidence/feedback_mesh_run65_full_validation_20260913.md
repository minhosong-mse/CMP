# FB-MESH-01 Extension — Full Run 6.5 Mesh / BTBT Hotspot Coverage Validation

**Date:** 2026-09-13  
**Feedback ID:** `FB-MESH-01`  
**Task:** `T-MESH-01`  
**Scope:** full Run 6.5 MEB geometry set  
**Status:** **Completed — full R6.5 coverage / comparison-consistency level**

## 1. Why the earlier mesh check was extended

The first feedback package validated only the formal 31/36/41 nm screening set. Because the final transistor-level MEB search was later extended through Run 6.5, the mesh-feedback question was reopened and checked against **every MEB geometry used in R6.5**:

```text
36 / 41 / 43 / 45 / 47 / 48 / 49 / 51 nm
```

The question remains deliberately limited:

> Does the same Mesh-Code 3 drain-side refinement ROI continue to cover the independently extracted BTBT hotspot across the full R6.5 geometry sweep?

This is a hotspot-coverage / comparison-consistency validation, not an absolute mesh-convergence proof.

## 2. Frozen validation conditions

```text
Run       = R6.5
T         = 300 K
Mesh_Code = 3
VD        = 1.2 V
VG final  = -0.7 V
BTBT      = Band2BandGeneration maximum in full Silicon domain
```

Common Mesh-GIDL refinement rule:

```text
Base mesh = Medium
ROI X = 0.032–0.070 um
ROI Y = 0.112–0.133 um
local max/min = 1.0 / 0.25 nm
```

The geometry changes through MEB depth; the local-refinement policy is not relocated case-by-case.

## 3. Full R6.5 raw extraction table

| MEB (nm) | BTBT node | Mesh node | BTBTmax (cm^-3 s^-1) | Xhot (um) | Yhot (um) | Points | Elements |
|---:|---|---|---:|---:|---:|---:|---:|
| 36 | `n119_des` | `n2_msh` | 8.41825e21 | 0.0515625 | 0.121875 | 5789 | 12175 |
| 41 | `n120_des` | `n33_msh` | 5.55270e21 | 0.0523437 | 0.121875 | 5830 | 12273 |
| 43 | `n121_des` | `n108_msh` | 3.92200e21 | 0.0523437 | 0.121875 | 5843 | 12303 |
| 45 | `n122_des` | `n110_msh` | 2.95585e21 | 0.0531250 | 0.121875 | 5856 | 12333 |
| 47 | `n123_des` | `n112_msh` | 1.90750e21 | 0.0531250 | 0.121875 | 5880 | 12385 |
| 48 | `n124_des` | `n114_msh` | 1.42817e21 | 0.0539063 | 0.121875 | 5882 | 12393 |
| 49 | `n125_des` | `n116_msh` | 1.17656e21 | 0.0539063 | 0.121875 | 5895 | 12423 |
| 51 | `n126_des` | `n118_msh` | 5.94400e20 | 0.0539063 | 0.121875 | 5908 | 12453 |

Primary numeric sources:

- `data/run06_5/feedback_mesh_20260913/r65_mesh_raw_extract.csv`
- `data/run06_5/feedback_mesh_20260913/r65_mesh_hotspot_coverage_summary.csv`

## 4. Hotspot-motion audit

Across the complete R6.5 sweep:

```text
Xhot minimum = 0.0515625 um @ 36 nm
Xhot maximum = 0.0539063 um @ 48/49/51 nm
Delta Xhot, 36→51 nm ≈ +0.0023438 um = +2.344 nm
Yhot = 0.121875 um for all eight cases
```

The hotspot moves gradually in wafer-depth X and does not show a lateral Y jump over the R6.5 geometry set.

## 5. Common-ROI margin audit

Common ROI:

```text
X = 0.032–0.070 um
Y = 0.112–0.133 um
```

| MEB | X-low margin (nm) | X-high margin (nm) | Y-low margin (nm) | Y-high margin (nm) | Nearest edge (nm) | Coverage |
|---:|---:|---:|---:|---:|---:|---|
| 36 | 19.5625 | 18.4375 | 9.875 | 11.125 | 9.875 | PASS |
| 41 | 20.3437 | 17.6563 | 9.875 | 11.125 | 9.875 | PASS |
| 43 | 20.3437 | 17.6563 | 9.875 | 11.125 | 9.875 | PASS |
| 45 | 21.1250 | 16.8750 | 9.875 | 11.125 | 9.875 | PASS |
| 47 | 21.1250 | 16.8750 | 9.875 | 11.125 | 9.875 | PASS |
| 48 | 21.9063 | 16.0937 | 9.875 | 11.125 | 9.875 | PASS |
| 49 | 21.9063 | 16.0937 | 9.875 | 11.125 | 9.875 | PASS |
| 51 | 21.9063 | 16.0937 | 9.875 | 11.125 | 9.875 | PASS |

Result:

```text
R6.5 ROI coverage = 8 / 8 PASS
minimum nearest-edge margin = 9.875 nm
```

Even the deepest / boundary case (`51 nm`) remains well inside the same refinement ROI.

## 6. Mesh-size consistency

Points and elements increase gradually as MEB geometry changes:

```text
Points   : 5789 → 5908
Elements : 12175 → 12453
```

Identical element counts are not expected because MEB modifies the geometry and therefore mesher topology. The comparison-control condition is the use of the same `Mesh_Code=3` rule and common local-refinement window.

## 7. Screenshot evidence package

The raw screenshots were captured for all eight R6.5 conditions with three evidence types per MEB:

```text
*_btbt_hotspot.png  = full-Si Band2BandGeneration maximum window + device map
*_mesh_full.png     = full device mesh
*_mesh_zoom.png     = drain-side hotspot-region mesh zoom
```

Canonical names and exact source-node mapping are recorded in:

- `data/run06_5/feedback_mesh_20260913/screenshot_manifest.csv`

The raw image pack preserves the original screenshots without resampling or annotation. For presentation, use a curated subset or make a composite from these originals rather than repeatedly screenshotting compressed figures.

## 8. Supported conclusion

> Across the full Run 6.5 MEB set (36/41/43/45/47/48/49/51 nm), independently extracted BTBT hotspots remain inside the same `Mesh_Code=3` common Mesh-GIDL refinement ROI. The total X-hotspot motion is only about 2.34 nm, Yhot remains 0.121875 um for every case, and every hotspot retains at least 9.875 nm distance to the nearest ROI edge. Therefore, the common refinement policy provides robust hotspot coverage and fair case-to-case comparison consistency throughout R6.5; case-specific ROI relocation is not required by the observed hotspot motion.

## 9. Claim boundary

Do **not** state:

- absolute mesh independence has been proven;
- the numerical mesh error is zero;
- 0.25 nm is a universal converged BTBT spacing;
- this mesh check itself proves the physical GIDL mechanism.

Use:

- full-R6.5 hotspot coverage is verified;
- common mesh policy supports comparison consistency;
- no observed R6.5 hotspot requires case-specific ROI relocation;
- absolute mesh independence would require a separate coarse/medium/fine or spacing-convergence study.

## 10. Relation to earlier evidence

Earlier 31/36/41 feedback package:

- `docs/evidence/feedback_mesh_common_roi_validation_20260911.md`
- `data/run04/feedback_mesh_20260911/`

This 2026-09-13 extension supersedes the earlier limited-range statement when discussing **Run 6.5**. The original evidence remains useful as historical presentation-feedback provenance.
