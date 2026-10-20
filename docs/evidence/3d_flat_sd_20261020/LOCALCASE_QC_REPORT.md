# CMP — 3D-Sun-SADDLE-V1 Flat-SD LocalCase 1/2 native TDR audit

Date: 2026-10-20
Status: CMP-EXECUTED SDE-only / PROVISIONAL, no SDevice validation.

## Input provenance
- Source previous SWB MeshCase experiment `CMP_B0_3D_mesh_sdflat_MeshCase_0to6.zip` (Case 0 n19, Case 1 n33; selected supplementary Case 2 n34 and Case 6 n38).
- New `n32` LocalCase 1: source-side OuterCrest placement off, `MeshCase=0`; source CMD `n32_dvs.cmd`, native HDF5 `n32_msh.tdr`, `n32_bnd.tdr`, SDE log `n32_dvs.log`.
- New `n40` LocalCase 2: drain-side OuterCrest placement off, `MeshCase=0`; CMD `n40_dvs.cmd`, native HDF5 `n40_msh.tdr`, `n40_bnd.tdr`, SDE log `n40_dvs.log`.
- Physical parameters: nominal Recess=120 nm, DBCAT=36 nm, JunctionRatio=0.4, Wfin=17 nm, RfilletFactor=1, Tox=5 nm; same geometry/contact/doping setup. `GaussFactor=0`.

## Quantitative results (unique tetrahedral edges, TDR connectivity)

| Case | Tetra | <0.1 nm | Min edge (nm) | x<-22 nm | |x|<=22 nm | x>22 nm | z depth 73.0–73.5 nm |
|---|---:|---:|---:|---:|---:|---:|---:|
| MC0_n19 | 289,198 | 372 | 0.01438067 | 84 | 204 | 84 | 308 |
| LC1_n32 | 266,585 | 348 | 0.01438067 | 62 | 202 | 84 | 308 |
| LC2_n40 | 266,604 | 348 | 0.01438067 | 84 | 202 | 62 | 308 |
| MC1_n33 | 244,015 | 324 | 0.01438067 | 62 | 200 | 62 | 308 |
| MC2_n34 | 194,612 | 276 | 0.01438067 | 84 | 108 | 84 | 220 |
| MC6_n38 | 6,512 | 0 | 0.10450383 | 0 | 0 | 0 | 0 |

- All 348 sub-0.1 nm edges retained by LC1/LC2 are geometrically the same as baseline Case 0 to 0.001 nm endpoint quantization: each single-side disable removes **24** baseline edges; creates **zero** new sub-0.1 nm edges.
- Source-off: source x<-22 nm: 84→62; gate |x|<=22 nm: 204→202; drain x>22 nm 84 unchanged.
- Drain-off: drain x>22 nm: 84→62; gate |x|<=22 nm: 204→202; source x<-22 nm 84 unchanged.
- Both-off historical Case1 removes 48 edges, giving 324. This agrees with independent one-side removal.
- **The 308 edges at depth 73–73.5 nm are unchanged across Case 0, LC1, LC2, historical Case 1.** Breakdown of that persistent band: 62 source outer + 184 gate window + 62 drain outer.
- Outer-Gate source/drain examples contain edge lengths as short as **0.01438067 nm** around x ±56.25 nm, y ±4.248357 nm, z −73.132 nm.

## Geometry boundary sanity checks
- Each baseline `n19_bnd.tdr`, both local BND files, and both-off `n33_bnd.tdr` has **286 CAD BREP vertices / 808 BREP faces / 15 regions**.
- The native HDF5 BREP *vertex coordinate* and *face connectivity* data compare identically across four files. Whole binary-file SHA may differ due to metadata.
- Each new SDE trace `n32_dvs.log` and `n40_dvs.log` finishes without error and executes `(sde:build-mesh "snmesh" "" "nXX")`. Do not infer SDevice numerical convergence.

## Interpretation / claim boundaries
1. LocalCase left and right refine windows act largely independently and cause exactly 24 minor edge differences per side.
2. The persistent hotspot is NOT cured by disabling outer-crest placement; hence further size sweeps of that same setting have low diagnostic priority.
3. Beyond the actual Gate/Oxide region, the tiny edges occur in/along the boundary between `R.SiSaddle` and `R.SiSubstrate` — both are Silicon — and the adjacent mesher-generated `R.SiSubstrate` tets. This is consistent with **same-material CAD region-seam/cylindrical-cap segmentation** interacting with SMesh imprint.
4. Inside the Gate, additional edges involve `R.SaddleDielectricOuter` and `R.GateOxide`; therefore a Si–Si union test alone would not prove the full 3D mesh fixed.
5. Whether these extreme slivers materially corrupt simulated fields/BTBT is NOT established; a <0.1 nm edge cutoff is diagnostic, not universal physical failure standard.

## Next bounded action
- **Stop LocalCase window toggle experiments**; preserve original 3D model, D-051 selection, frozen 2D.
- If taking a geometry-oriented diagnostic branch: test *merging same-material silicon regions without changing outer material boundaries* (must independently verify final geometry, contacts, doping, region mapping against baseline after Boolean operation). Changes are diagnostic only until validated; SDE syntax/Boolean behavior should be checked against official Sentaurus T-2022.03 SDE Ch.4 before authoring executable deck.
- Separately probe 3D gate/oxide/cylindrical-Saddle intersection and its surface discretization. Do not assume the Si–Si seam is the sole cause; the 184 persistent short edges in gate-zone remain.
- Current user upload contains `n32_dvs.log`, `n40_dvs.log` (SDE traces) but **not** `n32_msh.log`, `n40_msh.log` (SnMesh quality reports). Request those logs to compare min tetra angles / non-Delaunay faces without rerunning SDE.
- Do not run bulk SDevice/DC/GIDL/thermal until two genuinely different, adequately resolved meshes achieve matched-bias electrical + E/BTBT verification.

Data attachments: `LOCALCASE_SUMMARY.csv`, `LOCALCASE_EDGES.csv`, `LOCALCASE_BOUNDARY_CHECK.json`.
