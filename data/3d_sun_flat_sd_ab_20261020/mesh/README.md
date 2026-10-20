# SDE / mesh diagnostic archival, 2026-10-20

Status: CMP-EXECUTED mesh-only controls, NOT physically converged / production accepted.
Lineage: 3D-Sun-SADDLE-V1 Flat upper S/D, nominal ARgate6 DBCAT36nm Wfin17nm JunctionRatio0.4 Rfillet1 Hsaddle48nm Tox5nm GaussFactor0.

| Series | Actual nodes | Purpose / finding |
|---|---|---|
| MeshCase 0..6 | 19, 33..38 | Case0 repeats M2D; Cases0/4/5 have identical effective vertex/connectivity; Case6 is intentionally coarse, not a SDevice candidate. |
| LocalCase 1,2 | 32,40 | Each disabled source/drain outer-crest refinement independently, removing 24 sub-0.1nm edges; 73nm cluster persisted. |
| CadSeamCase 0..3 | 39,42,43,44 | Same-material Si and oxide unions; Case3 short edges 372->132, non-Delaunay boundary faces 278->94; 0.01438nm min edge remains. |
| CurveGrid 1,2 | 41,46 | CadSeamCase3, independently finer gate-curve windows; A 352400 tetra, B 459464 tetra; 0 non-Delaunay boundary faces in both; sub-0.1nm edges remain. |

Candidate A=n41 (CurveGrid1) and independent finer comparator B=n46 (CurveGrid2) are LIMITED research grids; device suitability depends on matched-bias DC/E/BTBT evidence archived separately. No absolute mesh-convergence claim.

**Executed source GitHub paths:** `code/sde/3d_sun_saddle_v1/flat_sd_mesh_20261020/` (LocalCase, CadSeamCase, CurveGrid source deck). Each is a research diagnostic branch of the previously archived M2D source; T-2022.03 SDE. Actual SWB preprocessed commands checked in user-provided bundles. Never silently mix the removed region labels `R.SiSaddle`, `R.SaddleDielectricOuter` into device-region selectors after union.

## Native source archive locations (external to GitHub)
- `CMP_B0_3D_mesh_sdflat_MeshCase_0to6.zip` — SHA256 `36d5443b8868d1dbbb21cee1079727405f38b0aa4b1056696dae456b87cf9ba1`.
- Follow-on LocalCase, CadSeamCase and CurveGrid native n*_msh.tdr/n*_bnd.tdr/n*_msh.log/n*_dvs.cmd were provided in current CMP conversation; Git stores derived tables, QC reports and executed source, not giant TDR binaries.

Run `CurveGrid=1 2`, `CadSeamCase=3` in SDE only for mesh regeneration; the final SDevice source meshes are n41 and n46 only by their respective SWB projects. Never treat **node ID alone** as an immutable TDR identity without project context.
