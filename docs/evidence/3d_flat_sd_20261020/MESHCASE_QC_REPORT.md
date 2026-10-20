# CMP 3D-Sun-SADDLE-V1: Flat S/D MeshCase 0–6 native SDE QC (2026-10-20)

**Status: CMP-EXECUTED / SDE-ONLY / MESH-NOT-ACCEPTED.** Separate `B0_3D_mesh_sdflat` project; do not modify frozen 2D PAPER-CAL, previously completed rounded 3D or historical results. No new SDevice, field/BTBT, thermal, retention, paper-fit or GitHub commit performed in this checkpoint.

## Scope and provenance

- Source: `CMP_B0_3D_mesh_sdflat_MeshCase_0to6.zip`, supplied by user. Node map: MeshCase `0=n19`, `1=n33`, `2=n34`, `3=n35`, `4=n36`, `5=n37`, `6=n38`.
- All cases contain native `*_msh.tdr`, `*_bnd.tdr`, `*_msh.log`, runtime `*_dvs.cmd` / `pp*_dvs.cmd`, `*_dvs.log` and `*_W_VIS_bnd.tdr`. All seven SDE mesh outputs are present.
- Nominal structure: ARgate6 / nominal recess 120 nm / DBCAT36 nm / Wfin17 nm / RfilletFactor1 / JunctionRatio0.4 / Flat upper S/D / rounded lower saddle. Fixed source geometry and doping; `MeshCase` alters only mesh settings.
- Tetrahedron edges: take 6 edges per native four-vertex tetrahedron, sort vertex indices, deduplicate globally, compute Euclidean coordinate separation (TDR coordinates in μm, multiplied by 1000 for nm). Region counts separately deduplicated *within* each region and may overlap on shared boundaries.
- 0.1 nm is a **diagnostic cutoff**, not a universal mesh rejection criterion. Non-Delaunay *boundary faces* must not be misreported as non-Delaunay *volume elements*.

## Native QC table

| Case | Node | Vertices | Tetra elements | unique edges < 0.1 nm | < 0.05 nm | min edge (nm) | min tetra angle (°) | Non-Delaunay boundary faces |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0 | n19 | 51,384 | 289,198 | 372 | 262 | 0.014381 | 0.168928 | 278 |
| 1 | n33 | 43,462 | 244,015 | 324 | 262 | 0.014381 | 0.178410 | 266 |
| 2 | n34 | 34,807 | 194,612 | 276 | 190 | 0.014381 | 0.168928 | 208 |
| 3 | n35 | 41,670 | 234,202 | 372 | 262 | 0.014381 | 0.168928 | 276 |
| 4 | n36 | 51,384 | 289,198 | 372 | 262 | 0.014381 | 0.168928 | 278 |
| 5 | n37 | 51,384 | 289,198 | 372 | 262 | 0.014381 | 0.168928 | 278 |
| 6 | n38 | 1,451 | 6,512 | 0 | 0 | 0.104504 | 0.259345 | 0 |

## Reproducibility and identity

1. **Case 0 reproduces the previously uploaded M2D mesh.** Native vertex-array hash and region-wise tetra connectivity signature match the prior `/mnt/data/n19_msh(4).tdr` (binary hashes need not match because metadata differs).
2. **Cases 0, 4, and 5 are effectively identical meshes**, with exactly matching native vertices and tetrahedron connectivity. They are **not** three independent grids. Increasing selected minimum refinement sizes in cases 4 and 5 did not change the output mesh under current overlapping meshing constraints.
3. Native geometric dataset hashes for `*_bnd.tdr` are identical across all seven cases; same for `*_W_VIS_bnd.tdr` separately. This demonstrates identical represented boundary geometry, **not** that the original geometry is free from local near-tangent edges or slivers.

## Controlled findings

- Case 1 disables OuterCrest placement: 372→324 sub-0.1nm edges (−48, −12.9%). Of the edges, 308 in the depth band 73.0–73.5 nm **persist**.
- Case 2 disables Gate placement: 372→276 (−96, −25.8%). Edges in the 73.0–73.5 nm band reduce 308→220, but minimum edge stays 0.014381 nm and Gate/oxide interface resolution is weakened (GateOxide tets 27,910→11,886). **NOT a SDevice candidate.**
- Case 3 disables Active placement: sub-0.1nm count remains 372, despite lower tetra count. Junction, Si fin and saddle resolution are no longer controlled as intended. **NOT a SDevice candidate.**
- Cases 4 and 5: identical effective grid to case 0, no independent comparison.
- Case 6 coarse-only: 6,512 tetra, **0 edges < 0.1 nm**, min edge 0.104504 nm, boundary non-Delaunay faces 0. Nevertheless minimum tetra angle **0.259345°**, initial BREP surface remains sharp (minAngle ≈1.01728°). This is a **control mesh only**. It loses fine oxide, saddle and gate hotspot resolution and is NOT a SDevice candidate or demonstration of accepted mesh.
- Cases 0–5 all maintain the same global minimum edge ≈0.014381 nm near `x≈±56.25 nm`, `y≈±4.248 nm`, `z≈−73.132 nm`. The larger problem includes off-Gate region `|x|>22nm`, so gate-specific refinement tweaks cannot cure the entire distribution.
- Initial BREP quality is preserved across all cases, including acute angle near `(x,y,z)≈(−15, +8.5, −120)nm` and surface imprint sensitivity near `z≈−73.139nm`. The former is a separate local warning and should not be assumed the sole cause of the latter.

## Interpretation and decision boundary

**Evidence supports a local saddle / Si–Ox curved boundary tessellation or imprint × overlapping refinement interaction.** The underlying Boolean geometry also has acute intersections but this experiment does not prove an intrinsic CAD physical sliver. Neither simply removing refinements nor raising nominal minimum sizes yielded two demonstrably adequate, independent grids. Mesh adoption **REMAINS BLOCKED**.

## Shortest next steps (not yet executed)

1. Use SVisual or a read-only native geometry export to inspect the rounded-Saddle Si/Ox surfaces specifically at `z≈−73.13 nm`, near `y≈±4.248nm` across the central and off-Gate X positions; additionally inspect the acute CAD interface at `x≈±15nm, y≈±8.5nm, z≈−120nm`. Record which region interfaces/edges are duplicated or nearly tangent.
2. Prepare a **separate, geometry-preserving SDE-only diagnostic** to vary the local Saddle crest surface sampling, window intersections or overlapping refinements *without changing the actual material geometry or physical dimensions*. Verify any new SDE/SMesh option in official T-2022.03 manuals first; do not reinterpret min-edge cutoff as pass/fail.
3. If issue persists independent of controls, perform a separately labeled controlled CAD-interface reconstruction test; preserve current D-051 geometry selection and historical runs, and compare full boundary topology before considering adoption.
4. Once **two genuinely distinct, adequately resolved grids** survive regional / surface QA, run restricted matched-bias LOWVD, then selected HIGHVD SDevice E-field, BTBT spatial distributions/integrals and terminal-current/KCL comparisons. Do not run broad DC/temperature/retention or publish GIDL causal claims at this point.

## Attached evidence

- `MESHCASE_NATIVE_QC.csv`: log and native mesh summary including effective-grid signatures.
- `MESHCASE_REGIONS_NATIVE.csv`: per-region tetra and short-edge statistics (shared-region edges overlap).
- `MESHCASE_SHORTEST_EDGES.csv`: minimum 15 short-edge midpoints and vertex IDs per case (Case6 has none below 0.1nm).
- `MESHCASE_SHORT_EDGE_COUNTS.png`: short-edge diagnostic chart, not a validation score.
