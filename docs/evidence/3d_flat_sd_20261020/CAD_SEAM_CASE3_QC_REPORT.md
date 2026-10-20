# CMP 3D-Sun-SADDLE-V1 Flat S/D — CadSeamCase 3 QC (2026-10-20)

**State: CMP-EXECUTED / structural & mesh QC only; PROVISIONAL, NOT an adopted device mesh.**

## Source and lineage
- User-executed SDE/SMesh T-2022.03, nodes n39=CadSeamCase0, n42=Case1 (Si union), n43=Case2 (Oxide union), n44=Case3 (both unions).
- n44 input `n44_dvs.cmd` contains `CadSeamCase=3`, `MeshCase=0`; execution and native `n44_msh.log` completed. Same Recess 120 nm, MEB/DBCAT 36 nm, Hsaddle 48 nm, Wfin 17 nm, Tox 5 nm, ARgate6, JunctionRatio0.4, RfilletFactor1, GaussFactor0.
- This variant does not modify frozen 2D PAPER-CAL, historical 3D-Sun-B0 or rounded M1.

## Native tetra QC

| Case,node | tetra | points | Unique edges <0.1 nm | <0.05 nm | minimum edge (nm) | minimum tet angle (deg) | non-Delaunay boundary faces |
|---|---:|---:|---:|---:|---:|---:|---:|
| 0 n39 | 289,198 | 51,384 | 372 | 262 | 0.014380671 | 0.168928 | 278 |
| 1 n42 | 275,073 | 48,951 | 164 | 102 | 0.014380671 | 0.356817 | 95 |
| 2 n43 | 286,668 | 50,971 | 340 | 258 | 0.014380671 | 0.168928 | 277 |
| 3 n44 | **272,506** | **48,531** | **132** | **98** | **0.014380671** | **0.356817** | **94** |

Case3 reduces unique <0.1 nm edges by 64.52% (372→132), and non-Delaunay **boundary faces** by 66.19% (278→94) compared with original Case0. Case1→3 extra gain: 32 short edges and one non-Delaunay boundary face; minimum edge and tet angle do not improve. This diagnostic <0.1 nm threshold is **not** a universal physics pass/fail specification. `Found 0 non-Delaunay elements` in logs does not imply zero non-Delaunay *boundary faces*.

## Location of surviving issue in n44
- All 132 edges <0.1nm lie within **|x| ≤ 15nm**; none are in x<-22nm or x>22nm outer areas.
- 128/132 (96.97%) are at depth 73.0–73.5nm; the remaining 4 are at other nearby crest locations.
- Edge-region memberships: `R.GateOxide` 132, `R.SiSubstrate` 34 (shared-interface edges can be counted in both). The old `R.SiSaddle` and `R.SaddleDielectricOuter` region names were removed by same-material Boolean union; their material is still present.
- Shortest edges occur around (x=0nm, y=±4.2484nm, depth≈73.132nm) and repeat across the gate. This strongly supports a **local curved physical Si/Ox boundary imprint/surface triangulation interaction** as the next hypothesis to test; not proof of a CAD physical-shape error.
- n44 mesh log initial BREP min edge 2.21874nm, after boundary imprint 0.0365888nm, final tet minimum 0.0143807nm. Severe minimum tet angle ~0.357deg persists.

## Physical-preservation checks
- Native tetra-volume summation across all four nodes gives identical totals (um³, numerical precision): Silicon 0.0009210703431; Oxide 0.0002626955307; Nitride 0.0000432000000.
- Source, drain, gate, substrate *contact surface areas* match original Case0: 0.000816, 0.000816, 0.010761093, 0.007200 um², respectively, and their coordinate ranges match. Gate contact triangle counts can differ from surface re-triangulation.
- From n44 vs n39, 35,015 common Silicon coordinates match identically for `BoronActiveConcentration`, `ArsenicActiveConcentration`, and `DopingConcentration` (maximum absolute delta zero). The full continuous doping functions at newly meshed points were not independently proven identical beyond the already unchanged input definitions.
- These checks support preserved material volumes and contacts, but **do not prove exact pointwise equality of the full physical Si/Ox interface** or a device-independent high-field solution. The `R.SiSaddle`/`R.SaddleDielectricOuter` region labels cease to exist; region-specific SDevice/SVisual commands must be audited before electrical simulation.

## Decision boundary / bounded next experiment
1. **Recommend Case3 as preferred *structural cleanup hypothesis*, not a frozen electrical mesh**. Case1 remains a legitimate comparator if Oxide union introduces later region-name or field/extraction complications; Case3's quality gain vs Case1 is modest.
2. Stop doing broad global mesh size changes and repetitive outer crest switches. The residual 128-edge z≈−73.13nm cluster is localized at physically relevant curved Si/Ox boundary near the gate.
3. Next **SDE-only** step: inspect this interface's CAD face intersections and boundary tessellation / conformality at fixed coordinates, remove only a demonstrable nonphysical sliver or redundant CAD segmentation without changing Recess120nm, Rfillet1, Wfin17nm, Tox5nm, doping or contacts. Compare baseline Case3 before/after identical physical material geometry & dopants.
4. Produce independent meshes A/B with **same candidate CAD** and distinct **adequately resolved** local Si/Ox and gate–drain refinement, verify they differ in vertex/connectivity as well as local resolution, with improved element quality. *Do not take two variants of Case0/4/5 as independent grids (identical meshes).*
5. Only after this gate, run selected 300K / MEB36nm SDevice 0.05V and 1.2V Id–Vg plus a common selected high-Vd OFF-bias 3D `ElectricField` and `Band2BandGeneration`, compare terminal electron/hole/total currents and KCL, fixed-coordinate hotspot profiles and BTBT spatial integration. Do not call total off-current GIDL, or claim paper-equivalent numerical calibration.

**Next first action:** one bounded local physical Si/Ox curved surface/imprint diagnosis (no production SDevice yet). No GitHub files were modified or committed in this analysis.
