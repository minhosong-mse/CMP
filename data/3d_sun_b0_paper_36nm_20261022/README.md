# 2026-10-22 — 3D Sun Flat S/D, MEB/DBCAT 36 nm: DC paper comparison evidence

**Maturity:** CMP-EXECUTED five DC sweeps, **PROVISIONAL paper-equivalence**. Same provisional `3D-Sun-SADDLE-V1 / Flat upper S/D` parent as 2026-10-20 Mesh A CurveGrid1 (SDE n41 -> SDevice n47). 300 K, gate WF **4.8 eV unchanged**, DBCAT=36 nm, Hurkx ON, nominal Wfin=17 nm, Lgate=20 nm. No geometry, contact, doping, mesh or physics retune from this checkpoint. No new TCAD job was run for postprocessing.

## New tracked figure

[Five executed current curves, viewable SVG](figures/CMP36_five_curves.svg): Id–Vg at Vd=0.05/1.2 V and Id–Vd at Vg=0.1/0.6/1.2 V. Id–Vd appears in both linear and logarithmic scales because smaller-current traces overlap the axis on linear scale. SVG is a **pixel-simplified derived visualization**; not the original numerical series.

## Executed original five PLTs (outside git)

Original uploaded `CMP_36nm_BASELINE_CURVES.tar.gz`, SHA256 **ee954836053426ad0c921c96ce5089b96e8403908c7d4e16d4fbc1a20ae9523f**; contents include byte-preserved native PLTs, `PLOTS/all_curves_raw_and_widthnorm.csv` (779 data rows), derived `*_DERIVED_WIDTH17nm.plt`, and original `PLOTS/PLOT_MANIFEST.json`. The original archive is held as user-supplied evidence, not republished due to size.

| Sweep | Points | Native PLT SHA256 | Bias |
|---|---:|---|---|
| IDVG_VD005 | 60 | `35e87fbf9d698df25822c838e0b5eb2aa23cbc2ee44035963a55884327914675` | Vd=0.05 V; Vg=0..1.5 V |
| IDVG_VD12 | 107 | `2798c9f9ac7ad44f72cfeb43c2f607835b8dd1aa7b8a6e418f77b7a839f00178` | Vd=1.2 V; Vg=0..2.0 V |
| IDVD_VG01 | 204 | `0abd293674f438a734e295a8058cc244a90d6996f650f07cdcce07a52f0fe29c` | Vg=0.1 V; Vd=0.0012..1.2 V |
| IDVD_VG06 | 204 | `c4aeba6e8bfb7abf8e3b572b3e058b913de1a7356afb354b699a507d22616fb7` | Vg=0.6 V; Vd=0.0012..1.2 V |
| IDVD_VG12 | 204 | `047df30866b92a13fcd7ed99b6aa8fd02a4855f02a8de893a7db677e14302e15` | Vg=1.2 V; Vd=0.0012..1.2 V |

Existing Id–Vg sweeps from `/user2/cmp/cmp212/B0_3D_low` and `B0_3D_highpos`; three Id–Vd SWB runs from `/user2/cmp/cmp212/CMP_B0_PAPER_COMPARE_36`. The collection script initially rejected valid Id–Vd because the first recorded Vd=0.0012 V, not 0; user corrected only the collector's first-point tolerance to allow 0..0.002 V and collected all five sweeps. This does not modify the native PLTs, simulation decks, models, or results.

## Numerical reference (native `Idrain / 0.017 µm`, ABS magnitude, DERIVED)

At **Vd=1.2 V**:
- Id–Vd, Vg=0.1 V: **5.295908166897099e-13 A/µm**.
- Id–Vd, Vg=0.6 V: **3.766437779474682e-8 A/µm**.
- Id–Vd, Vg=1.2 V: **2.137791050891e-4 A/µm**.
- Id–Vg, Vg=2.0 V: **9.261749314983e-4 A/µm**.

Existing Mesh A LOWVD Vth=**0.807873 V**, HIGHVD Vth=**0.782709 V** (project's constant-current method); LOWVD SS=**75.887 mV/dec**, DIBL=**21.882 mV/V** (CMP extraction). Do not automatically equate these to paper bias/metric definitions.

The paper states current normalized to channel width (Table 1). Here the normalization divisor 0.017 µm is the *nominal Wfin* only and is **not established to be identical to the paper's active/effective conduction perimeter**. Do not treat normalization-adjusted current as an independently calibrated absolute reproduction.

## Original paper and corrected overlay provenance

Original: Sun, Baac & Shin, *Micromachines* **13**, 1476 (2022), Table 1 DBCAT 36 nm and Figure 3; DOI: https://doi.org/10.3390/mi13091476. Source user PDF SHA256 **de52fa88fe7fd0b57cde39ba8db498b1a87179608386f26a4f5b604f9**. The paper supplies **Vth=0.656 V**, **SS=76 mV/dec**, **Ion/Ioff=3.4e10**, **DIBL=23.6 mV/V** for nominal baseline. The exact output curves are raster figures, not released tabular sweep data.

A corrected *pixel-axis-aligned* background overlay image is preserved in the user delivery as `01_PAPER_CMP_OVERLAY_VERIFIED.png` (SHA256 **0a24072fd34c24581daf572e0be3e5cf524d896a72a264af118d60904c179840**); the externally retained raster is **not** an extracted numeric paper curve. The repository SVG displays solely the five executed CMP curves; it does not synthesize any paper data.

At the paper's graphed Vg=0.1/0.6 V, the CMP Id–Vd is orders below the paper's **visually estimated** output traces. At Vg=1.2 V CMP has a similar rising shape, but different amplitude and saturation slope. Id–Vg broadly similar turn-on/SS trend, yet CMP high-Vd Vth exceeds the paper nominal by ~**0.127 V**. **Full absolute 3D paper baseline replication is NOT demonstrated.**

**User-directed next task:** preserve original WF=4.8 eV and geometry; run matching *24/36/48 nm DBCAT* Id–Vg and Id–Vd sweep comparison against paper; accept as a **qualitative MEB-trend reference only if directions and characteristics are supported**. Gate-Drain GIDL/BTBT/E/Cgd and temperature/1T1C research comes downstream; no premature paper fit, freeze, performance/retention claim or root README change.
