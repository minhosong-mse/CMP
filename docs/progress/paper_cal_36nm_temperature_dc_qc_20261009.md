# 36 nm × 233/300/340/380 K: integrated DC / GIDL / Cgd / spatial validation
**2026-10-09 · State: 36-nm temperature baseline DATA-COMPLETE / DC source-curve QC PASS · only within post-freeze Atlas L2**
**Frozen physical calibration preserved: C7_4/B_QF_HALF, GCS=2.3, depth boost 0.025um, Qf=2.55e12cm^-2, WF4.8eV. No mesh convergence, retention, final optimum or FZ-C numerical equality claimed.**

## Provenance
- New user ZIP `CMP_DC36_RESULTS.zip` SHA256 `e680122bcfca924bf60f7320efd39f685e2289bc8b89f963938ccdd5319b8262`. 47 archive members, 44 file-level SHA256 verified; all six new-temperature summary and six corresponding curve CSV available in **user source ZIP**. Six immutable summary CSVs are committed under `data/paper_cal/atlas_temperature_20261009/raw_dc36/`.
- Data extraction: `MEB_DC_0.05`, `MEB_DC_1.2` SWB graph, parent SDE n8=36 nm, SDevice n9/n66/n96 for 233/340/380 K, respective SVisual n10/n67/n97. Actual preprocessed SDevice decks and bounded log excerpts match; actual bias endpoints and constant-current threshold reached (all six). Each curve has 6,107 Id–Vg points. Full ~7MB logs remain on SWB server, not in ZIP.
- **Independent check:** six curve-backed log-interpolated Vth at `Icrit=5e-6 A/um`, SSquick minimum positive local slope on 1e-12..1e-6 A/um, SS1dec/SS2dec, terminal current at Vg=0/1.2/2, and Ion/Ioff reproduced reported SVisual summary values. Source hashes match.
- 300 K DC directly reused from separately validated 2026-10-08 15-depth Atlas, no reruns. Temperature GIDL ON/OFF, P2 spatial BTBT/E hotspot, AC Cgd values are reused from 2026-10-09 previously QC-reviewed 45-case evidence; the ZIP of that work remains a separate local artifact, not part of this commit.

## 36 nm master metrics (full precision in committed CSV)
| Metric | 233 K | 300 K | 340 K | 380 K |
|---|---:|---:|---:|---:|
| `Vth_005_V` | 0.7378157 | 0.6814816 | 0.6463376 | 0.6107495 |
| `Vth_12_V` | 0.7115806 | 0.6547513 | 0.6182390 | 0.5799454 |
| `DIBL_mV_per_V` | 22.81312 | 23.24371 | 24.43357 | 26.78622 |
| `SSquick_005_mV_dec` | 58.47513 | 76.29423 | 87.44551 | 98.93948 |
| `SSquick_12_mV_dec` | 58.02584 | 75.75862 | 86.76888 | 98.25393 |
| `SS1dec_005_mV_dec` | 64.01275 | 81.16548 | 91.75157 | 102.8112 |
| `SS1dec_12_mV_dec` | 61.99119 | 79.20486 | 89.79122 | 100.7973 |
| `SS2dec_005_mV_dec` | 62.22728 | 79.17957 | 89.80335 | 100.9675 |
| `SS2dec_12_mV_dec` | 60.66016 | 77.73553 | 88.39075 | 99.57777 |
| `Id_005_Vg0_A_per_um` | 4.348773e-18 | 1.633483e-14 | 5.094055e-13 | 8.010353e-12 |
| `Id_005_Vg1p2_A_per_um` | 6.993007e-5 | 6.158282e-5 | 5.648570e-5 | 5.172386e-5 |
| `Id_12_Vg0_A_per_um` | 9.626299e-17 | 3.158401e-14 | 9.316713e-13 | 1.424781e-11 |
| `Id_12_Vg1p2_A_per_um` | 2.464055e-4 | 2.439552e-4 | 2.404565e-4 | 2.363192e-4 |
| `Id_12_Vg2_A_per_um` | 6.831725e-4 | 6.440992e-4 | 6.213824e-4 | 5.999545e-4 |
| `IonIoff_12_Vg1p2` | 2.559712e+12 | 7.724012e+9 | 2.580915e+8 | 1.658636e+7 |
| `IonIoff_12_Vg2` | 7.096939e+12 | 2.039321e+10 | 6.669545e+8 | 4.210855e+7 |
| `Cgd_abs` | 1.501431e-16 | 1.424448e-16 | 1.377090e-16 | 1.330596e-16 |
| `Cdg_abs` | 1.501431e-16 | 1.424448e-16 | 1.377084e-16 | 1.330553e-16 |
| `Cgd_reciprocity_pct` | 5.328252e-8 | 2.734182e-5 | 3.805845e-4 | 0.003230414 |
| `Id_ON_signed_A_per_um` | 3.975188e-15 | 1.088559e-12 | 1.261287e-11 | 9.789892e-11 |
| `Id_OFF_signed_A_per_um` | 1.775931e-15 | 9.041544e-13 | 1.215514e-11 | 9.716743e-11 |
| `Hurkx_delta_A_per_um` | 2.199257e-15 | 1.844042e-13 | 4.577241e-13 | 7.314941e-13 |
| `Hurkx_sensitive_pct` | 55.32460 | 16.94021 | 3.629025 | 0.7471932 |
| `qG_BTBT_A_per_um` | 2.199951e-15 | 1.844146e-13 | 4.593123e-13 | 7.650873e-13 |
| `Delta_vs_qG_err_pct` | -0.03157688 | -0.005643860 | -0.3457630 | -4.390760 |
| `BTBTmax_cm3s` | 8.181221e+20 | 2.460872e+23 | 1.111787e+24 | 2.268616e+24 |
| `BTBT_int2D_s_inv_um_inv` | 13731.02 | 1.151025e+6 | 2.866802e+6 | 4.775299e+6 |
| `Ehot_at_BTBT_V_cm` | 9.236992e+5 | 1.040113e+6 | 1.144874e+6 | 1.141760e+6 |
| `Xhot_um` | 0.03867187 | 0.03632813 | 0.03574219 | 0.03574219 |
| `Yhot_um` | 0.2531250 | 0.2528906 | 0.2521740 | 0.2521740 |
| `BTBT20_area_um2` | 2.698514e-5 | 7.055239e-6 | 4.090788e-6 | 3.129488e-6 |

## Key trends / boundaries
- From 233→380 K: Vth at Vd=1.2 drops **131.635 mV**, SSquick increases **40.228 mV/dec**, DIBL grows **22.8131→26.7862 mV/V**. Ion@Vg1.2,Vd1.2 falls **4.093%** while Ion/Ioff collapses **2.5597e12→1.6586e7**.
- DC Ioff is **Id(Vg=0,Vd=1.2)** (233→380 K grows ~148,009×); the **GIDL-bias** total drain current is **Id(Vg=-0.7,Vd=1.2)** (rises ~24,627.5×). These must not be conflated. Raw AC Cgd magnitude decreases 11.378% across 233→380 K.
- 36nm/380K ON−OFF-vs-spatial qIntegralBTBT mismatch **−4.39076%** remains flagged; ON drain current is *total* leakage, not directly pure BTBT.
- Fixed Y-cut under-samples shallow hotspots; use whole-Si spatial integral and moving BTBT hotspots for comparisons. No mathematical inference of physical cell retention or production optimum.
- 41nm/340K Cgd is missing (Newton DC nonconvergence before AC); leave null, no blanket rerun. Other 14 new-temperature MEB DC depths remain running/not-yet-ingested.

## Next
**FIRST:** collect DC005+DC12 source CSV/Id–Vg curves + SWB graph/preprocessed temperature/log evidence for remaining depths, independently QC, and extend 60-row temperature Master incrementally. Avoid unconditional solver/mesh retunes, old FZ-C refreeze or paper-parameter recalibration. Then jointly assess MEB–temperature range; PAPER-CAL 1T1C Write/Hold/Read remains subsequent work.

## Local files not physically stored in this Git commit
Full user ZIP (818661 bytes), original 6 long Id–Vg curves, 60-row **partial** temperature Master CSV, xlsx, charts and the reproduced Python audit script are in `CMP_DC36_COMPLETE_RESEARCH_BUNDLE_20261009.zip` (downloadable from the chat). GitHub contains the complete **36nm four-temperature numeric master**, six original DC summaries, independent QC metadata and this report, but **not those binaries / long curves**; the SHA256 source identifier is recorded for eventual archival. The 60×MEB/T table is NOT fully DC-validated yet.
