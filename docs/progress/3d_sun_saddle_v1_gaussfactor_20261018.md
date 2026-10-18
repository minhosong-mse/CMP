# 3D-Sun-SADDLE-V1 / M1: GaussFactor five-point SDE + three-bias DC checkpoint (2026-10-18)

**Status: PROVISIONAL / 12 of 15 SDevice terminal voltage goals reached; 3 partial failures.** This is a controlled lateral-Gaussian-doping implementation-sensitivity study, **not** physical baseline calibration, paper match, numerical mesh convergence, GIDL validation or retention verification. Separate lineage from the frozen `B0-2D-PAPER-CAL` and historical `3D-Sun-B0`.

## Question and controlled setup

The original 3D M1 reconstructed SDE had `(define GaussFactor 0.0)`. Its numerical value was a **CMP reconstruction assumption**, not a Sun et al. paper-provided lateral diffusion parameter. Only this SDE Gaussian lateral factor was split: **0.0 / 0.2 / 0.5 / 1.0 / 1.5**. All nominal geometry, gate material boundary, mesh refinement policy, temperature, and SDevice physical models were held fixed. Parameters: ARgate 6, DBCAT 36 nm, JunctionRatio 0.4 (Gaussian junction ~48 nm), Wfin 17 nm, RfilletFactor 1.0, WF 4.8 eV, T 300 K; Hurkx BTBT, PhuMob, Lombardi and high-field mobility. None of these geometrical variables was newly fitted to a paper target.

SDE: source/drain Gaussian doping with variable lateral `GaussFactor`, unchanged source/drain vertical Gaussian fit (sigma ~12.914 nm and source/drain symmetric 48 nm target depth). All five SDE boundary geometry meshes match topologically; *production volumetric meshes* differ slightly. GF=0.5 and 1.0 have matching vertex/connectivity mesh arrays, allowing paired doping-only comparison. Five SDE mesh sizes: **84,537 / 84,395 / 84,455 / 84,455 / 84,429 vertices** respectively. All retain a pathological **minimum edge 0.000835 nm**, so successful SDevice convergence does **not** demonstrate spatial E/BTBT accuracy or mesh convergence. Source: uploaded SDE QC TDR archive in [data manifest](../../data/3d_sun_saddle_gaussfactor_20261018/SOURCE_MANIFEST.csv).

Three separately executed SDevice decks, each with requested `NumberOfThreads=8`: LOWVD `Vd=0.05,Vg=0→1.5`, HIGHVD POS `Vd=1.2,Vg=0→2`, HIGHVD NEG `Vd=1.2,Vg=0→−1` V. Every case: `Poisson/Electron/Hole`, `Band2Band(Hurkx)`; current output `GF_IDVG_*.plt`. No Id–Vd or retention sweep was performed in this pilot.

## Independent evidence / success gate

User-original `CMP_GAUSS_3BIAS_CORE.zip`: **424 source entries**, SHA256 `39723f0b6f4f8d7091a5254e4f60ef692d4120a2bd718ff447d586ebeb2a740b`. It includes the original preprocessed `pp*_des.cmd`, `n*_des.log`, native PLT and SWB node results. Read only the five `GF_IDVG_...` transfer PLT curves in each project; exclude historical Quick/Drain-prep PLTs. **1,550** gate-sweep PLT points were independently structured for charting and metric extraction. Raw ZIP and full 1,550-point CSV/PNG figure analysis bundle remain separately archived outside public GitHub; this GitHub checkpoint stores verified compact extracted summaries plus source hashes. Absence of full 3D TDR here prevents spatial hotspot claims.

Success requires BOTH SWB/node completion AND actual target gate bias achieved, not merely `Curve trace finished` (that message can indicate that the *drain preparation* completed). Results:
- LOWVD: 5/5 pass.
- HIGHVD POS: 4/5 pass; GF=1.5 stops at **+0.244028 V**.
- HIGHVD NEG: 3/5 pass; GF=0.2 stops at **−0.352749 V**, GF=1.5 stops at **−0.365715 V**.
- All three failed cases first reached `Vd=1.2 V`, then Newton nonconvergence/step below MinStep in gate ramp; failed curves remain **partial**, not completed off/transfer figures. GF 1.5 failed with **8 solver threads**, so nonconvergence cannot be blamed solely on a parallel-license shortage.

## Extraction definitions — reproduce the earlier M1 within-lineage comparison

- `Vth`: first `|Id|=8.5e−8 A` crossing with **linear interpolation in log10(|Id|) versus Vg**. Previous one-bias LOWVD study used current-linear interpolation; values are not identical. Both definitions are tabulated in the metrics CSV; **LOG** is the reported benchmark basis.
- `SS`: linear least-squares `log10(|Id|)` versus `Vg` on valid monotonic `|Id|∈[1e−12,1e−9] A`; 1000/slope in mV/dec.
- `DIBL`: `[Vth(0.05V)−Vth(1.2V)]/1.15 ×1000` mV/V, only if both transfer scans reached thresholds.
- **Illustrative** `Ion/Ioff`: `|Id(Vd1.2,Vg+2)| / |Id(Vd1.2,Vg−1)|`, only with **both full endpoints**. **Not** independently matched to Sun-paper bias/width convention. Raw three-dimensional total terminal current is **A**, not `A/µm`.
- For a failed HIGHVD POS, do **not** report full-high-bias threshold/DIBL/SS; for failed NEG, do **not** report `−1 V` Ioff or Ion/Ioff. No interpolation/extrapolation of missing high-bias endpoints.

| GF | Vth Low (V) | Vth High (V) | SS Low / High (mV/dec) | DIBL (mV/V) | Ion/Ioff illustrative |
|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.812283 | 0.786046 | 76.212 / 77.079 | 22.814 | 1.6725e8 |
| 0.2 | 0.812613 | 0.786299 | 76.239 / 77.112 | 22.882 | — (NEG incomplete) |
| 0.5 | 0.812141 | 0.785896 | 76.235 / 77.113 | 22.822 | 1.6625e8 |
| 1.0 | 0.811311 | 0.785178 | 76.240 / 77.119 | 22.724 | 1.6790e8 |
| 1.5 | 0.806134 | — | 76.135 / — | — | — (both HIGHVD incomplete) |

**GF=0** repeats original 3D M1 values `Vth_High=0.786046`, `SS_High=77.079`, `DIBL=22.814 mV/V` and `Ion/Ioff≈1.6725e8` under exactly the same CMP-defined extraction. It is a **regression anchor** only, not paper reproduction. GF=0.5/1.0 have all three sweeps completed and show small DC differences; they are **comparison candidates, not an adopted factor**.

At `Vd=1.2,Vg=−1`, GF0 `Id≈+9.103689e−14 A` and `Isub≈−9.103690e−14 A` with negligible source current: mainly **drain-to-body terminal balance**, not independently proven BTBT. Signed KCL check succeeds (computed max absolute error ~9.61e−20 A), but KCL is not proof of microscopic GIDL. Across all five curves at common `Vg=−0.3 V`, `Id` is approximately 3.009–3.115e−14 A; these are *only common-bias partial-curve data*, not `Ioff@−1 V`.

## Runtime diagnosis

The nominal decks request 8 threads. A subset acquired no `sparallel` license and explicitly fell back to 1 solver thread. For LOWVD, GF0 1-thread **56.36 min** versus the four 8-thread values **11.65–11.99 min**. HIGHVD POS GF0/0.2/0.5/1.0 ran serial 96–107 min; HIGHVD NEG GF0 serial 122 min vs GF0.5/1.0 at 8 threads 24–25 min. A licensing fallback explains the large runtime disparity; **Newton/MinStep failures must be handled separately**. Subsequent experiments should record actual solver threads per node, and do not assume `NumberOfThreads=8` implies 8 threads acquired.

## Decision boundary / next immediate work (PROPOSED validation sequence)

1. **Read existing representative OFF-bias 3D TDR**, preferably `Vd=1.2 V, Vg=-1 V` at GF0 then GF0.5/1.0; compare a common physical 3D ROI in Silicon with SVisual cuts through fin center and fin sidewall. Inspect `ElectricField` vectors/magnitude, `Band2BandGeneration`, locations of maxima, fixed-cut profiles and spatial extent; use matched color/scale and report geometry-relative coordinates. LOWVD alone was never the GIDL diagnostic bias.
2. **Geometry/topology and mesh gate first before quantitative physics claim**: diagnose gate–saddle/oxide Boolean sliver and the persistent 0.000835 nm minimum edge, inspect mesh at apparent hotspot. Build an independently repaired mesh with identical intended physical geometry/doping/physics. Repeat select bias points and compare `Id`, field maximum/coordinate, local BTBT map, region-integrated `Band2BandGeneration`, current components and KCL. An apparent hotspot may be a mesh artifact.
3. **Separate mechanisms:** quantify `q∫G_BTBT dV` and ON/OFF Hurkx controls on same mesh where meaningful; account for electron/hole current collection and body current. The source-to-drain current and drain-to-substrate leakage must not be mislabeled GIDL.
4. Only after a spatially defensible 3D nominal baseline and matched extraction/current-width convention: revisit paper nominal `Vth=0.656 V` and reported `Ion/Ioff=3.4e10`, then consider MEB/DBCAT sweeps and later 1T1C retention. **Do not tune Gaussian factor, workfunction or doping just to hit paper metrics before this gate.**

No published Sun-paper curve source extraction/normalization equality is asserted. No frozen 2D files, historical M1 results, public root README or `DECISIONS.md` altered. **Keep 3D-Sun-SADDLE-V1 nominal PROVISIONAL.**
