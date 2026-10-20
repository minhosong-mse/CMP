# CMP 3D-Sun-SADDLE-V1 — CAD seam SDE-only QC (2026-10-20)

**Source**: Uploaded user-executed `B0_3D_mesh_sdflat` native TDR/BND, CMD and SDE/Mesh logs. Case 0=n39; Silicon–Silicon same-material internal seam union Case 1=n42; Oxide–Oxide union Case 2=n43. 300 K/36 nm nominal geometry fixed. **No SDevice run.**

## Results

| Diagnostic | n39 Case 0 | n42 Case 1 | n43 Case 2 |
|---|---:|---:|---:|
| Points | 51,384 | 48,951 | 50,971 |
| Tets | 289,198 | 275,073 | 286,668 |
| Unique tet edges <0.1 nm | 372 | **164** | 340 |
| Unique tet edges <0.05 nm | 262 | **102** | 258 |
| Minimum edge | 0.01438067094 nm | 0.01438067094 nm | 0.01438067094 nm |
| Minimum tetra angle | 0.168928° | **0.356817°** | 0.168928° |
| Non-Delaunay boundary faces (not elements) | 278 | **95** | 277 |
| Edges with midpoint depth 73.0–73.5 nm | 308 | 148 | 288 |
| Edges at x < −22 nm | 84 | **0** | 84 |
| Edges at −22 ≤ x ≤ 22 nm | 204 | 164 | 172 |
| Edges at x > 22 nm | 84 | **0** | 84 |

Si merge decreases sub-0.1-nm edges by 208 (**55.9%**); all 168 outside-Gate (abs(x)>22nm) short edges disappear. Oxide-only union decreases edge count by 32 (**8.6%**). This is compelling evidence that a same-Silicon internal CAD region interface is a contributor to short-edge meshing, **not** proof that the remaining mesh is acceptable, or that CAD has no physical slivers. The minimum edge remains 0.01438 nm and angle 0.357° remains extremely poor. Remaining n42 164 edges lie inside Gate-window; 148 lie near depth 73 nm; many touch curved oxides `R.SaddleDielectricOuter` or `R.GateOxide`.

## Physical geometry and profile controls

Native tetrahedron material volumes match identically to printed precision in three meshes (μm³): Silicon **0.0009210703431**, Oxide **0.0002626955307**, Nitride **0.0000432** (total **0.0012269658738**). Native contact triangle areas match: Source/Drain **0.000816 μm²** each; Gate **0.0107610934156 μm²**; Substrate **0.0072 μm²**. Each contact's spatial bounds unchanged. Gate contact triangle count differs n39 4770 vs n42 4774; equal area. Reconciled common-coordinates Silicon vertices retain identical B/As/Net Doping values: n39↔n42 **35,134 common vertices** (all identical), n39↔n43 **37,450** (all identical). New/regridded vertex positions have not undergone interpolated concentration-error integration.

The merged `R.SiSaddle` disappears as its separate region name in Case 1, and `R.SaddleDielectricOuter` disappears separately in Case 2. Downstream region-specific physics, plots and spatial BTBT integrations must be adjusted if a merged candidate is later adopted. Matching volumes/areas does not alone prove complete physical interface shape or field convergence.

## Next bounded experiment

**Only SDE-run `CadSeamCase=3`** (both same-material seams merged) using the existing `SDE_FLAT_SD_CAD_SEAMCASE_0to3_SWB.cmd`, in a test project, all other parameters unchanged. Provide its node ID, `n*_msh.tdr`, `n*_bnd.tdr`, `n*_msh.log`, `n*_dvs.cmd`, `n*_dvs.log`. Check material volumes, contacts, doping, min edge/angle, actual remaining short-edge positions; Case 1+2 improvements **must not** be assumed additive. If the bottom ~73 nm cluster persists, stop mesh-knob sweeps and isolate CAD-curved physical Si/Ox junction/facet imprint in a separate targeted geometry reconstruction experiment. No broad SDevice runs or freeze until two distinct, physically well resolved meshes and matched-bias E-field/BTBT/KCL comparisons.

**Status: PROVISIONAL.** No GitHub modification or production adoption.
