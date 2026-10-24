# 2026-10-24 — Sun 2022 3D baseline / MEB-depth paper calibration interim review

> **Status: PROVISIONAL / PARTIAL PAPER REPRODUCTION; NOT FROZEN.** This is a scientific checkpoint in the independent `3D-Sun-SADDLE-V1 / Flat upper S/D` lineage, not a revision of the frozen `B0-2D-PAPER-CAL C7_4`.

## 1. Question and fixed comparison framework

How well does the present 3D BCAT model reproduce Sun, Baac & Shin, *Micromachines* **13**, 1476 (2022), [DOI:10.3390/mi13091476](https://doi.org/10.3390/mi13091476), and can MEB depth explain the model's internally observed OFF current reduction?

Fixed across 24/36/48 nm: nominal gate length 20 nm, fin width 17 nm, oxide 5 nm, nominal recess 120 nm, metal gate work function **4.8 eV**, nominal junction depth 48 nm, selected 3D-Sun Flat-upper-S/D geometry, T=300 K, CurveGrid1 mesh policy and original Hurkx-model physics (except deliberate ON/OFF isolation). **No geometry, WF, doping, contact, or solver retuning** was performed to fit the paper.

The current structure is figure-consistent rather than the paper's original 3D CAD. Matching *nominal* junction depth does not establish matching 3D implant profile or contact geometry. Selected MEB varies geometrical gate-top depth; the simulation does not simulate a full physical etch process.

## 2. Simulation coverage and confidence

**CMP-EXECUTED:** 15/15 distinct SDevice DC cases in five sweeps: Id–Vg Vd=0.05 V (60 samples ×3) and Vd=1.2 V (107 ×3); Id–Vd Vg=0.1/0.6/1.2 V (204 samples ×3 per bias). Total **2,337** logged terminal-current samples. DBCAT↔SDE/SDevice mesh mapping and successful end markers audited.

**Source limitation:** current PLT output names collided across depth nodes; only 48 nm final native PLT for each sweep survived in the 15-run archive. All 15 independently named SDevice logs retained per-step values at roughly four significant digits. Full 36 nm independent native PLTs and five 48 nm native PLTs cross-check the log recovery (median relative error 0.00606%/0.00562%, maxima <0.047% for compared magnitudes >1e-18 A). Do **not** imply 24 nm has full-precision native current sweep or report extra meaningful digits from log-based numbers.

Raw files are retained outside Git; SHA256 and provenance are indexed under `data/3d_sun_meb_paper_interim_20261024/README.md`. SVG plots under `figures/` are **derived graphics** with their source numbers in CSV, not original paper raster art.

## 3. Nominal paper DC comparison (36 nm)

| Quantity | Sun 2022 nominal | CMP 3D 36 nm | Evidentiary boundary |
|---|---:|---:|---|
| Vth | 0.656 V | ~0.783 V | +~0.127 V; bias/effective W/extraction equivalence not fully proven |
| SS | 76 mV/dec | ~75.887 mV/dec | similar numerical slope; CMP low-Vd fit definition |
| DIBL | 23.6 mV/V | ~21.9 mV/V | similar order; different extraction conventions possible |
| Ion/Ioff | 3.4e10 | not aligned | don't compare until paper-equivalent ON/OFF definitions |
| Id–Vd at Vg=0.1/0.6 V | paper plotted far higher | CMP several orders smaller using nominal Wfin | wide amplitude mismatch; paper curves only raster |
| Id–Vd at Vg=1.2 V | similar rising trend | broadly same order, different slope/amplitude | partial |

Paper states a constant-current Vth criterion `1e-7 A × W/L`; inserting **nominal** W=17 nm, L=20 nm gives 8.5e-8 A, close to the current *numerical* criterion used by the 2026-10-24 three-depth comparison. It **does not prove** paper-effective conducting width and bias definitions are equivalent. The earlier 2026-10-22 36-nm high-Vd Vth ~0.782709 V and the new 15-log estimate ~0.783237 V use separate extractions and should not be silently merged as if identical.

## 4. MEB trend against Sun Table 1 raster

| Bias / observable | Sun DBCAT raster direction | CMP 24/36/48 direction | Assessment |
|---|---|---|---|
| Id–Vg, low Vg, Vd=1.2 V | 48 > 36 > 24 | **24 > 36 > 48** | **opposite** |
| Id–Vg, turn-on | steep subthreshold rise | broadly similar turn-on | **partial** |
| Id–Vd, Vg=1.2 V | 24 > 36 > 48 | **24 > 36 > 48** | **ordering agrees** |
| Id–Vd, Vg=0.6 V | 24 > 36 > 48 | **48 > 36 > 24** | **opposite** |
| Id–Vd, Vg=0.1 V | paper far larger | CMP tiny; 24 > 36 > 48 at Vd1.2 | **quantitative mismatch** |

Paper Id–Vd extends to Vd=2 V while CMP comparison stops at 1.2 V. The paper does not supply raw Table 1 sweep arrays, so these are **visual ordering observations**, not digitized exact error statistics. Figure 3's plotted Vth/DIBL versus DBCAT direction also differs from some adjacent textual description: keep figure-based observations and paper narrative distinct instead of inventing a reconciliation.

CMP high-Vd Vth at 24/36/48 nm: **0.783786/0.783237/0.782060 V**, using 8.5e-8 A semilog interpolation from printed values; low-Vd Vth **0.808181/0.808341/0.809375 V**. Derived DIBL **21.214/21.829/23.752 mV/V**. All three are internal estimates, not calibrated paper metrics.

## 5. Hurkx isolation: model-causal OFF-depth effect

At Vd=1.2 V, Vg=0 V, T=300 K:

| MEB | Hurkx ON drain (fA) | Hurkx OFF drain (fA) | ON−OFF drain (fA) |
|---:|---:|---:|---:|
| 24 | 23.360 | 5.252716 | 18.107284 |
| 36 | 11.881301 | 5.241500 | 6.639801 |
| 48 | 8.860327 | 5.216813 | 3.643514 |

24/48 ON-versus-OFF decks differ only by removal of the `Recombination(Band2Band(Hurkx))` clause; fixed grid/WF/bias and 107-point Id–Vg. The 36-nm ON/OFF point reuses the 2026-10-21 executed HIGHNEG Mesh A history at **Vg=0**; it is not claimed to be a newly generated 36-nm positive sweep.

24−48 ON depth difference = 14.499673 fA; OFF difference = 0.035903 fA; therefore **99.7524% of the observed ON depth difference vanishes upon removal of Hurkx**. 24→48 ON−OFF excess falls **79.878%**. At Vg=0.6 V, 48 nm > 24 nm remains when Hurkx is removed; this crossover is channel/electrostatic rather than caused by the toggled Hurkx contribution (microscopic channel cause unproven).

This is a **model-dependent drain/substrate excess current**, **NOT** a directly measured pure terminal GIDL current.

## 6. Spatial |E| and 3D BTBT Generation at Vd=1.2 V, Vg=0 V

Common proxy ROI windows along x: Gate–Drain `x=15..30 nm`, Mid `x=30..45 nm`, Outer Drain `x=45..60 nm`, over selected 3D silicon. These geometric slabs are *not yet individually verified contact/interface membership*. Spatial calculations are from original SVisual T-2022.03 logs, following fixed 24/36/48 ON and 24/48 OFF runs.

| MEB | Gate ROI Emax (MV/cm) | Outer ROI Emax (MV/cm) | Gate q∫G+ dV (fA) | Outer q∫G+ dV (fA) | Three-ROI sum (fA) |
|---:|---:|---:|---:|---:|---:|
| 24 | 1.211862 | 3.358850 | 12.135413 | 5.874389 | 18.009811 |
| 36 | 0.945208 | 3.332147 | 1.465518 | 5.054846 | 6.520369 |
| 48 | 0.686433 | 3.275221 | 0.000556 | 3.543777 | 3.544334 |

Hurkx OFF yields zero reported `Band2BandGeneration` under the extraction protocol. Signed/positive/negative identity checks passed for all 15 ROI records; the recovered extraction uses the proper **um³↔cm³ factor of 1e-12** when applying it to separately derived positive/negative integrated fields. **q∫G dV is a generation-equivalent rate, not collected terminal current**.

Between 24 and 48 nm: Gate maximum field **−43.36%**, Outer maximum field **−2.49%**, Gate BTBT positive generation **−99.9954%**, Outer generation **−39.67%**. Across all three ROIs, 24→48 qG reduction **14.465477 fA**, of which **83.888%** comes from Gate slab and **16.112%** from Outer slab. 24→48 change in terminal ON−OFF = **14.463770 fA**, agreeing in *difference* within **0.0118%**; this is **not a collection-efficiency measurement or proof of pure gate GIDL**. At 48 nm nearly all remaining generated BTBT in these ROIs is at the external Drain boundary, not the Gate slab.

## 7. Calibration gate and next actions

**Status: PROVISIONAL / NO FREEZE / PAPER FIT INCOMPLETE.** This fixed-WF 3D construction reproduces selected paper features and has strong internal MEB→Gate-side field→Hurkx-BTBT depth-sensitivity evidence, but it does **not** reproduce all Table 1 trend directions or nominal absolute metrics. It does **not** substantiate production equivalence, GIDL absolute collection, physical retention, or a 3D optimum.

**First priority:** verify external Drain hotspot around x≈60 nm against existing TDR plus Face91 contact shape/doping/E map, separating gate-adjacent mechanism from possible finite-domain boundary influence; use already executed data first. If needed, one bounded boundary sensitivity control without changing frozen physics/WF is appropriate.

**Second:** examine 36-nm channel barrier and 24/48-nm Vg≈0.6 V electrostatics to distinguish current crossover and ~127 mV paper Vth offset; do not fit WF/geometry solely to force agreement.

**Third:** once boundary issue is qualified, compare selected 24/36/48 nm negative gate, Vd=1.2 V, Vg≈−0.7 V, under identical 3D ROI extraction and signed terminal currents. Then consider 3D Cgd, temperature, and 1T1C as downstream tasks **after** a scientifically bounded baseline decision.

**Frozen:** 2D `B0-2D-PAPER-CAL C7_4`, original 3D evidence/history, model geometry/WF4.8eV, root README. This review itself makes **no new physical model calibration freeze**.
