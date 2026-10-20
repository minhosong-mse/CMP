# 3D-Sun-SADDLE-V1 Flat S/D — drain-boundary + Hurkx ON/OFF close-out (2026-10-21)

**CMP-EXECUTED / selected-point numerical QC complete; physical GIDL attribution PROVISIONAL.** This checkpoint extends [2026-10-20 Flat-S/D A/B](3d_sun_saddle_v1_flat_sd_ab_20261020.md) and D-050/D-051/D-052 without replacing them.

## Conditions / controlled lineage

- Separate provisional 3D-Sun-SADDLE-V1 **flat upper Source/Drain** reconstruction; lower silicon saddle remains rounded. No changes to frozen 2D B0-2D-PAPER-CAL C7_4 or historical 3D-Sun-B0.
- 300 K; MEB/DBCAT=36 nm; Mesh A CurveGrid1 SDE n41 -> SDevice n47; same native `n41_msh.tdr` with verified matching SHA256; gate WF 4.8 eV; Fermi and existing Silicon mobility models; Vd=1.2 V, Vg=0 -> -1 V; 205 matched transfer points.
- Experimental ON: executed HIGHNEG `pp47_des.cmd` with `Recombination(Band2Band(Hurkx))`. Experimental OFF: **only that single Hurkx clause removed**. For independent execution, `File/Grid` is resolved to the original Mesh A absolute path. Output paths isolated; original SWB node/decks unchanged. The source+OFF CMD diff and grid/source hashes were reviewed. Both runs exited successfully and reached target.
- Raw native PLT/TDR/CMD/log ZIPs are retained outside GitHub. Hashes in [data manifest](../../data/3d_sun_flat_sd_hurkx_20261021/README.md).

## A. Drain boundary and CAD contact audit

- Executed `B0_3D_highneg/pp41_dvs.cmd` has `Xhalf=0.060 um`; `P.Drain=(Xhalf,0,-0.025) um`; `sdegeo:set-contact (find-face-id P.Drain) "drain"`. `n41_dvs.out` returned **Drain Face ID 91** (Source 89, Substrate 82); user opened real `n41_bnd.tdr` in SVisual.
- Upper flat silicon fin spans z=0..-48 nm and y=+-8.5 nm. Full-Si global E-field maximum from native TDR occurs at approximately (x,y,z)=(60,+7.5,-48) nm near the external drain-plane/corner at the nominal implant depth.
- **LIMIT:** point `P.Drain` and peak both lie on x=60nm, but Face 91 polygon/element membership of the peak has **not been proven**. Do not label it a definitively contacted corner or physical/unphysical contact artifact.
- Mesh A/B 12-cut/3-ROI field extraction both had 12/12 cuts, valid `Abs(ElectricField-V)` and zero extraction errors. ROI max |E| (A/B V/cm): GateDrain x15..30nm = 1,276,027.57 / 1,276,051.16; MidDrain x30..45nm = 764,077.70 / 764,172.10; OuterDrain x45..60nm = 3,859,669.65 / 3,860,049.75. Field peak is on outer finite boundary. Fixed z=-48nm, y~6.5nm A cut: E(x=45/55/59/59.8nm) = 0.59969 / 0.97606 / 3.04186 / 3.63128 MV/cm. Strong outer-x growth requires domain/contact test; same-point Donor and Acceptor ~1e17 cm^-3 on this cut is a sampled profile, not proof of no junction elsewhere.
- BTBT ROI peak `Band2BandGeneration` A: GateDrain 7.90858e23 at (18.75,7.5,-28.125)nm; OuterDrain 6.37882e23 cm^-3 s^-1 at (56.25,0,-47.8125)nm. Global hotspot from native full-silicon analysis is not identical to these ROI-local maxima. **E peak != BTBT peak**.

## B. Native Hurkx ON/OFF terminal attribution

Both runs completed 205 matching bias steps and reached Vd=1.2 V, Vg=-1.0 V. Original n47 HIGHNEG final drain current = 9.13930067836956e-14 A; reproduced ON = 9.13930068118819e-14 A (endpoint repeatability ~3.08e-8% relative). Final signed terminal currents:

| Terminal / metric | Hurkx ON | Hurkx OFF |
|:--|--:|--:|
| Drain TotalCurrent (A) | +9.13930068118819e-14 | +5.37371375833755e-15 |
| Drain eCurrent (A) | +8.60241285526872e-14 | +9.34658584575121e-21 |
| Drain hCurrent (A) | +5.36887825919469e-15 | +5.37370441175170e-15 |
| Substrate TotalCurrent (A) | -9.13930101906246e-14 | -5.37371962255262e-15 |
| Source TotalCurrent (A) | +3.37874279344865e-21 | +5.86421507309632e-21 |
| Gate TotalCurrent (A) | 0 | 0 |
| |sum(Iterminal)| (A) | 8.83524e-29 | 3.15544e-30 |

- `ΔId = Id_ON-Id_OFF = +8.601929305354435e-14 A`; OFF reduces positive drain current **94.1202134% relative to ON**, ON/OFF ratio 17.00742.
- OFF reduction vs ON for Vg=0/-0.1/-0.5/-1.0 V: **55.8845% / 68.2334% / 89.1738% / 94.1202%**. The dependence rises as gate bias becomes more negative; the drain-to-substrate path dominates, not source-to-drain channel conduction.
- **This is a bounded model-dependent terminal current difference, NOT an independently collected pure-GIDL current or a calibrated retention result.** Background current and terminal carrier partition must remain signed.

## C. ON/OFF spatial audit (same Mesh A)

- Each 3D SVisual extraction exported 12/12 cuts plus 3 ROI extrema; **843 matched sampled points** have identical coordinates and doping.
- ON/OFF `Abs(ElectricField-V)` remains numerically indistinguishable on those 843 sampled locations: maximum absolute change **0.1 V/cm**, relative difference **5.1976211e-8**; global outer ROI maximum remains ~3.85967 MV/cm. Field hotspot therefore survives model toggle.
- OFF `Band2BandGeneration` = **0 for all sampled points and three ROIs**; ON GateDrain/OuterDrain ROI maxima remain 7.90858e23/6.37882e23 cm^-3s^-1.
- The ON/OFF 1D-cut comparison does **not** establish full 3D signed generation integration, surface-face membership, or contact collection partition. Prior ON positive-only `q∫max(G,0)dV≈8.3978834e-14 A` is *generation-equivalent*, not drain collected GIDL and must not be subtracted blindly from terminal Id.

## Execution/provenance and strict claim boundary

Results use user-executed native T-2022.03 Sentaurus data, archived with SHA256 provenance under [data/](../../data/3d_sun_flat_sd_hurkx_20261021/). Curated CSVs and SVGs are **derived**; raw files remain outside GitHub. Selection of A as working mesh is diagnostic under D-052, **not** proof of absolute mesh convergence (remaining short edges and poor tet angles).

**Next FIRST action:** bounded finite-drain-domain/contact-face extent sensitivity: classify Face 91 geometry and boundary-element membership at (60,7.5,-48)nm; then vary only one external drain-boundary / contact-placement control in a separately named diagnostic branch while preserving gate, junction target, doping, material, biases, mesh-quality controls and Hurkx model. Repeat matched bias and signed terminal/KCL plus gate-drain/outer ROIs. A full-Si signed BTBT q∫G dV / positive / negative independent integration for ON and OFF remains a separate required source-to-terminal check. No MEB48/thermal/1T1C DOE or README/mainline baseline promotion until boundary attribution is resolved.
