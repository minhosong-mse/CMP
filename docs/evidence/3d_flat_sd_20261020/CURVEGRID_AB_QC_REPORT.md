# CMP 3D-Sun-SADDLE-V1 Flat S/D — CurveGrid A/B native QC

**Date:** 2026-10-20. **Status:** CMP-EXECUTED SDE-only, PROVISIONAL mesh; not electrical convergence or final adoption.

## Node map and controlled input

- Baseline CurveGrid=0: `n44`; A CurveGrid=1: `n41`; B CurveGrid=2: `n46`.
- Matched ARgate=6, DBCAT=36 nm, JunctionRatio=0.4, Wfin=17 nm, RfilletFactor=1, MeshCase=0, CadSeamCase=3, GaussFactor=0.
- A/B add only an SDE local refinement window: A max step (x,y,z)=2.2/1.8/2.2 nm, B=1.5/1.2/1.5 nm; no physical CAD or doping/contact changes.
- Source: uploaded original `n44/n41/n46_msh.tdr`, `bnd.tdr`, `msh.log`, `dvs.cmd`, `dvs.log`.

## Computed native results

| Metric | n44 | n41 | n46 |
|---|---:|---:|---:|
| Vertex | 48,531 | 62,396 | 80,788 |
| Tetra | 272,506 | 352,400 | 459,464 |
| Min edge, nm | 0.01438067 | 0.03658883 | 0.03658883 |
| Edges below 0.02 nm | 30 | 0 | 0 |
| Edges below 0.05 nm | 98 | 42 | 74 |
| Edges below 0.1 nm | 132 | 114 | 198 |
| Edges 0.1nm under, depth 73–73.5 nm | 128 | 68 | 120 |
| Gate curve window median edge, nm | 2.652 | 1.875 | 1.406 |
| Min tet dihedral angle, deg | 0.356817 | 0.427801 | 0.855553 |
| Tetra with min dihedral below 1deg | 212 | 78 | 142 |
| Tetra with min dihedral below 5deg | 2150 | 2309 | 2370 |
| non-Delaunay **boundary faces** | 94 | 0 | 0 |
| non-Delaunay **elements** | 0 | 0 | 0 |

Canonical TDR tetra coordinate/connectivity hashes are all distinct; source `CMP_GATE_CURVEGRID_0_1_2_QC_20261020.csv` records exact hashes. Thus A/B provide independent spatial meshes on the same nominal geometry.

## Geometry, contact, doping equivalence

- `n44/n41/n46_bnd.tdr`: exact same ordered BREP vertices **and** per-region boundary connectivity (canonical SHA256 `99dcd37cc29147399451be26648315675057cd097a02e71539b39feb2ce796f8`).
- Material volume from tetra per model: Silicon `0.0009210703431`, Oxide `0.0002626955307`, Nitride `0.0000432` µm³; equality at computed precision.
- Contact areas unchanged: source/drain `0.000816`, gate `0.0107610934156`, substrate `0.0072` µm².
- Three Silicon doping fields (`DopingConcentration`, `ArsenicActiveConcentration`, `BoronActiveConcentration`) compared at coordinate-matched Silicon vertices: n44/n41 35,015 common coords, n44/n46 35,015, n41/n46 43,734; **zero differences**. Newly placed vertices are not pointwise cross-comparable.

## Remaining localized weakness

- All short edges below 0.1nm in A/B remain within |x|<=15nm. 68/114 A and 120/198 B edges reside at depth 73.0–73.5nm.
- Edge material incidence: A Oxide-only 46, Oxide/Silicon 68; B Oxide-only 66, Oxide/Silicon 132. Incidence is not a declaration of a particular BTBT origin.
- Boundary imprint still generates min edge 0.0365888nm; mesh refinement does not eliminate that source. The number of very bad tetra (<1deg) remains 78 A and 142 B. These are serious local quality flags, but 0.1nm edge threshold alone is not a universal physical failure criterion.
- `zero non-Delaunay boundary faces` does not imply E-field/BTBT convergence. Fine curvature representation is a controlled numerical variation, not proof of physical device validity.

## Decision and next bounded action

1. **Keep unchanged nominal physical geometry and CadSeamCase=3**; n41 is the lower-cost, lower-extreme-defect pilot A, n46 is the independent refined pilot B. Neither mesh is frozen/final.
2. Because gross geometry, contacts and shared-vertex doping pass, it is reasonable to consider a **strictly limited 300 K LOWVD diagnostic paired SDevice run** on A/B as a sensitivity test **only after verifying SDevice deck has no stale region references**, e.g. `R.SiSaddle`/`R.SaddleDielectricOuter`, and identical physics/terminal definitions. Do not claim field or BTBT validity solely on successful DC convergence.
3. Review Id–Vg, Vth, SS, KCL and numerical convergence. If stable, advance to a **single matched bias** `Vd=1.2V` OFF-state spatial ElectricField / Band2BandGeneration A/B. Check current partition, hotspot position, integrated generation by physical material/ROI, and sensitivity to residual poor elements; if unstable, stop and address boundary tessellation, not parameter-fit paper Vth.
4. No full DC batch, MEB sweep, temperature, 1T1C or production retention until electrical/spatial independence is demonstrated.

**Research boundary:** 3D-Sun-SADDLE-V1 Flat S/D is still provisional; historical M1 and 2D PAPER-CAL freeze untouched. The present analysis is local file analysis only; no Sentaurus SDevice was executed and no GitHub file was changed.
