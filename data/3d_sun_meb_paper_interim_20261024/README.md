# 2026-10-24 3D Sun MEB three-depth / paper interim review data

**State:** executed DC / Hurkx / spatial source evidence with a **PROVISIONAL** physical-calibration claim. Progress interpretation: [interim review](../../docs/progress/3d_sun_meb_paper_interim_20261024.md). Selected SVG visuals under [figures](figures/).

## Indexed numerical evidence

- [`dc_15_case_endpoints.csv`](dc_15_case_endpoints.csv): all 15 executed sweep endpoints, signed drain A and provisional /0.017µm illustrative width normalization.
- [`dc_3depth_metrics.csv`](dc_3depth_metrics.csv): internal Vth, DIBL, OFF and three Id–Vd values reconstructed from printed solver log. 
- [`idvg_highvd_sample21.csv`](idvg_highvd_sample21.csv): 21 **actual printed** Id–Vg samples per depth (63 sampled points in figure), Vd1.2 V; **downsampled from 107 logs per depth**, no interpolation/synthesis, not complete sweep.
- [`hurkx_vg0_components.csv`](hurkx_vg0_components.csv): 24/36/48 nm Hurkx ON/OFF comparison at Vg0,Vd1.2; 36nm from separately executed 2026-10-21 HIGHNEG history.
- [`spatial_3depth_roi.csv`](spatial_3depth_roi.csv): 3D Silicon Gate/Mid/Outer Emax and signed/positive generation-equivalent rates.
- [`paper_trend_matrix.csv`](paper_trend_matrix.csv): categorical reading of Sun et al. (2022) Table 1 DBCAT row vs executed CMP; no invented paper numeric points.

## Figures (GitHub-native SVG, based on CSVs)

- [24/36/48 Id–Vg actual sampled curves](figures/01_idvg_highvd_meb.svg)
- [Id–Vd selected-bias endpoints](figures/02_idvd_endpoint_meb.svg)
- [Hurkx ON/OFF OFF-current decomposition](figures/03_hurkx_vg0.svg)
- [Gate vs Outer Drain E and BTBT](figures/04_spatial_field_generation.svg)

All SVG plots are **new original visualizations of executed CMP data**, not copied paper figures. Figure 2 is endpoint-only at Vd1.2 V, not a full Id–Vd line tracing. Figure 1 uses 21 original sampled points per depth, not 107/curve, and is therefore a visualization sample.

## External original archives / traceability (not uploaded to Git)

| Original archive | SHA256 | Contains |
|---|---|---|
| `CMP_MEB_15_RESULT_AUDIT.zip` | `c0ce6c975f0c9253cd086591d57a02a5013927ef39438e4bc413bd0508010345` | 15 SWB source/log, 48nm surviving native PLTs |
| `CMP_MEB_HURKX_24_48_RESULTS_20261024.zip` | `857845ddf74ca771e554c4061c6e57facde1a704382db09dcab85c57dff84b8f` | ON/OFF logs, 24/48 OFF native PLTs |
| `CMP_MEB_SPATIAL_GATE_DRAIN_RECOVERED_20261024.zip` | `1876959733883ec27de5182cb5f04a897f14ee9f706f0b857f943a9e1aeeeb7f` | original SVisual logs, extracted 5 conditions ×3 ROIs; no native TDR |
| `CMP_36nm_BASELINE_CURVES.tar.gz` | `ee954836053426ad0c921c96ce5089b96e8403908c7d4e16d4fbc1a20ae9523f` | five 36nm native 2026-10-22 PLTs |
| `all_15_log_rounded_curves.csv` | `f7516f5e682b0a9739d50fecd1a0300a76745ad90f22674288bc4e2a99f740f4` | 2337 printed solver records (external, full CSV) |
| `CROSSCHECK_3DEPTH.csv` | `8b3525f14f973ba15b94a85d320bf510f42077434565997b13a704c65d9a1ea9` | spatial derived review source |

Original Sun reference: Sun, Baac & Shin, *Micromachines* 13, 1476 (2022), [DOI](https://doi.org/10.3390/mi13091476). Graph readings are original paper raster observations; **no full paper images are republished to GitHub**.

**Caveats**: The exact TDR binaries were not in supplied spatial ZIP and cannot be independently rehashed here (reported manifest hashes only). The normal `integrate_field Band2BandGeneration` integral is already in [s^-1]; a separate derived positive/negative ROI integration required conversion from um³ numeric measure. The 36nm positive-sweep history is not numerically identical in provenance to 24/48 new ON/OFF runs; always disclose this mix. Do not mistake three-ROI generation equivalent for pure collected GIDL, or 17nm nominal width scaling for validated paper W.
