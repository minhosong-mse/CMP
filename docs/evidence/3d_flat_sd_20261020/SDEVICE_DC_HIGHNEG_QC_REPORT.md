# CMP 3D-Sun-SADDLE-V1 / Flat-SD / CurveGrid A/B — DC and HIGHNEG spatial QC

**Date:** 2026-10-20  
**Status:** CMP-EXECUTED numerical evidence / PROVISIONAL scientific interpretation; **not** a final adopted GIDL model, not a paper absolute-fit, not a retention proof.  
**Original inputs:** `CMP_3D_AB_DC_CORE.zip`, `CMP_3D_AB_SPATIAL_HIGHNEG.zip`, uploaded by researcher. Original zipped bytes preserved by researcher; this package contains **derived** metrics, plots, and extraction code, not original full TDRs.

## 1. SWB provenance and solver completion

| Project | CurveGrid | SDE | SDevice | Grid in actual `pp*_des.cmd` | Grid matched | Voltage goal reached | Original gate-sweep PLT points |
|---|---|---|---|---|---|---|---:|
| B0_3D_low | 1 / 2 | n41 / n46 | n47 / n48 | n41_msh.tdr / n46_msh.tdr | yes | Vd 0.05, Vg +1.5 | 60 / 60 |
| B0_3D_highpos | 1 / 2 | n41 / n46 | n47 / n48 | n41_msh.tdr / n46_msh.tdr | yes | Vd 1.2, Vg +2.0 | 107 / 107 |
| B0_3D_highneg | 1 / 2 | n41 / n46 | n47 / n48 | n41_msh.tdr / n46_msh.tdr | yes | Vd 1.2, Vg -1.0 | 205 / 205 |

All six logs finish `Curve trace finished` and `simulation finished`; signs/magnitudes of four electrode currents balance to roundoff in the parsed native PLTs. Convergence means numerical endpoint completion, **not** validated physical mechanism.

## 2. Matched extraction — native 3D A units

Definition: Vth at |Id|=8.5e-8 A, linear current interpolation; SS fit log10(|Id|) vs Vg on the 1e-12–1e-9 A span; DIBL = (Vth(0.05V)-Vth(1.2V))/1.15 V. These are CMP conventions and have not been shown identical to the cited Sun et al. definition.

| Metric | A / n41 | B / n46 | Absolute A/B shift |
|---|---:|---:|---:|
| LOWVD Vth (V) | 0.807873 | 0.811448 | 3.575 mV |
| LOWVD SS (mV/dec) | 75.8867 | 76.1950 | 0.3083 |
| HIGHVD Vth (V) | 0.782709 | 0.785035 | 2.326 mV |
| HIGHVD SS (mV/dec) | 76.9048 | 77.0662 | 0.1614 |
| DIBL (mV/V) | 21.8815 | 22.9678 | 1.0863 |
| LOWVD Id @ Vg=1.5 V (A) | 2.190285e-6 | 2.147054e-6 | 1.97% of A |
| HIGHVD Id @ Vg=2 V (A) | 1.574497e-5 | 1.559510e-5 | 0.95% of A |
| HIGHNEG Id @ Vg=-1 V (A) | 9.139301e-14 | 9.141508e-14 | ~0.024% |

LOWVD and HIGHVD DC sensitivity is small in these metrics, especially the negative-gate branch. This **does not validate the original physical contact geometry or bulk BTBT parameterization**.

## 3. HIGHNEG terminal current and KCL mechanism warning

At Vd=1.2V, Vg=-1V, each drain has a positive 9.14e-14 A current; the **substrate** is about -9.14e-14 A while source current is negligible (order 1e-21–1e-20 A) and gate is zero. The leakage path is drain–body, **not source–drain channel current**.

- Mesh A: Drain 9.139300678e-14 A, Substrate about -9.139301e-14 A, Source +3.88e-21 A.
- Mesh B: Drain 9.141508379e-14 A, Substrate about -9.141509e-14 A, Source +1.01e-20 A.
- Terminal sign convention is Sentaurus's inward current convention; sum(4 terminals) at final VG=-1 is numerically about 5.0e-29 A (A) and 2.1e-28 A (B).

Terminals do not label all drain current as GIDL. Hurkx ON/OFF or selective-generation tests are needed to distinguish BTBT-generated current from other leakage components.

## 4. HIGHNEG TDR volume integration

Source: full 3D `Band2BandGeneration` fields, all Silicon bulk regions (after same-material seam consolidation: `R.SiSubstrate`, source and drain `R.SiFin_lump_*`). Region-local nodal arrays were associated with sorted unique global vertex IDs of region tetrahedra; each tetra contributes `(mean of four clipped-positive vertex values) × tetra volume (µm³) × 1e-12 cm³/µm³ × q` to equivalent A. Minor negative interpolated BTBT generation samples were clipped to zero as they cannot represent physical negative pair generation. Results are model-derived total generation **not net collected terminal current**.

| VG (V) | q ∫ G_BTBT+ dV Mesh A (A) | Mesh B (A) | relative A/B discrepancy |
|---|---:|---:|---:|
| 0 | 6.520367e-15 | 6.517173e-15 | ~0.049% |
| -0.1 | 1.116581e-14 | 1.116089e-14 | ~0.044% |
| -0.5 | 4.354295e-14 | 4.353354e-14 | ~0.022% |
| -1.0 | 8.397883e-14 | 8.399970e-14 | ~0.025% |

This BTBT generation is approximately 91.9% of the final drain terminal current in current units. Similarity is suggestive but not proof of collection fraction or mechanism.

## 5. Critical spatial result: two distinct high-field / generation locations

**Maximum silicon E-field, not maximum BTBT,** at Vg=-1V:
- Mesh A: |E|max = 3.85967e6 V/cm, (x,y,z)=(+60,+7.5,-48) nm.
- Mesh B: |E|max = 3.86005e6 V/cm, same coordinates. **This position is on the finite drain-side X boundary**, near the upper fin's z=-48 nm bottom/transition. Boundary/contact-sensitive peak cannot be assumed a physical BCAT gate-edge GIDL hotspot.

**Largest nodal BTBT rate** at Vg=-1V:
- A: 1.155522e24 cm^-3 s^-1 at (+15,-7.5,-25.3125) nm.
- B: 1.155606e24 cm^-3 s^-1 at the same coordinates.
- This is close to the *outer* X extent of the nominal 15-nm gate oxide envelope, **not** the old z=-73nm short-edge cluster. A nodal maximum is not the same as the largest volume-integrated region.

**Volume-integrated spatial location shifts with VG**:
- At VG=0V, about **77.5%** of BTBT generation is in x=45–60nm drain outer region, versus **22.5%** in x=15–30nm.
- At VG=-1V, about **74.2%** is in x=15–30nm (near gate/drain side), versus **25.7%** in x=45–60nm (outer drain boundary).
- Comparing VG=-1V minus VG=0V integrated generation, about **78.6% of the *increase*** originates in x=15–30nm. Both meshes agree closely on these spatial fractions.
- The former extreme mesh defect at z≈-73nm contributes negligibly to the **BTBT volume integral for these four bias points**. **This does not mean the local mesh defect is validated electrically at other conditions.**

**Interpretation boundary**: A negative gate enhances localized drain-side BTBT near the gate oxide edge, consistent with a gate-induced component, **but** another strong region is present at the finite drain contact/body-boundary corner. Source/drain lateral Gaussian factor is currently `GaussFactor=0` (CMP reconstruction, not a calibrated physical doping profile). Do not promote this result to verified pure GIDL or retention prediction until a bounded control checks boundary sensitivity and Hurkx contribution.

## 6. Decision and minimal next gate

1. **DC A/B**: numerically acceptable sensitivity for this isolated 300K/36nm geometry, but keep scientific status **PROVISIONAL**. Stop endless re-meshing to drive all <0.1nm edges to zero.
2. **HIGHNEG BTBT A/B**: selected-point integrated generation, terminal KCL, E peak and source/drain spatial distribution are **numerically stable across two distinct meshes**. This is stronger than LOWVD-only agreement, but it remains a *within-model two-mesh check*, not a full asymptotic convergence study.
3. **Mechanism blocker**: finite x=60nm drain-edge extreme E and ~25.7% of VG=-1 BTBT in outer drain region. For physical claim, inspect contact/junction/doping/field near x=60nm and x=15nm in existing TDR, then if still ambiguous run one bounded Hurkx ON/OFF and one controlled finite-domain/contact sensitivity test. Do not tune recess/fin/saddle geometry or 2D frozen parameters to force fit.
4. **More TDR**: HIGHNEG spatial source is already sufficient for the above. LOW and HIGHPOS TDR ZIPs are optional to extend spatial diagnosis, **not required to prove 6 DC endpoints**.
5. **Not tested**: 48nm MEB 3D trend, temperature dependence, 1T1C retention transfer, matched paper effective width, independent doping/contact verification. These cannot be inferred from the present six runs.

## Machine-readable files and scripts

- `CORE_RUN_QC.csv`: six-run metric and bias/end-point QC
- `B0_3D_*_CurveGrid{1,2}_raw_plt.csv`: source-preserving native PLT numeric rows after field extraction
- `B0_3D_*_AB_INTERPOLATED.csv`: chart-only interpolated points for cross-grid visual comparison (clearly NOT original PLT points)
- `SPATIAL_SILICON_FULL_TDR_METRICS.csv`: native TDR E-field/BTBT summary, 0/−0.1/−0.5/−1 V
- `BTBT_INTEGRAL_SPATIAL_ROI.csv`, `BTBT_SPATIAL_BINS.csv`, `HOTSPOT_LOCALIZATION_ROI.csv`: volume-integrated spatial checks
- `Grid*_*_TOP300_GEN_NODES.csv`: top nodal BTBT points with native coordinate and field
- `analyze_core.py`, `analyze_spatial.py`, `analyze_hotspot_roi.py`, `xdepth_bins.py`, `create_plots.py`: replayable python extraction and visualization; require the original ZIPs beside this analysis directory.

**No simulation was run by the assistant.** Original user's live execution evidence was inspected without modifying SWB, SDE/SDevice files, or GitHub main. 
