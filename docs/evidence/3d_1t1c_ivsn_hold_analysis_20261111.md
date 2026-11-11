# 2026-11-11 independent 3D SN I–V / direct-Hold / retention-integral review

> **Status: CMP-EXECUTED user-provided SDevice outputs / exported-QC PASS for 20 IVSN + 16 short Holds; PHYSICAL RETENTION NOT DEMONSTRATED.** Model: `3D-Sun-SADDLE-V1 / Flat upper S/D`, Hurkx ON. Do not merge with historical 2D NonlocalPath/Run 7 or paper-calibrated 2D.

## 1. Study, provenance and data validity

- User's external SWB: `CMP_3D_Temp_Copy` (SN I–V), `CMP_3D_Temp_Copy_Copy` (direct Hold); source archive `CMP_3D_1T1C_RESULTS_REVIEW.tar.gz`, SHA256 `861104a9aa070b8ba1078d64c056b8f11cc76c8c6415b50e21cce885041dc371`.
- Independent 3D `MEB/DBCAT=36,41,48,54,60 nm` × `233/300/340/380 K`; 20 completed 101-point VSN I–V sweeps, **16** successfully completed `100 ns` Floating Holds, **4** failed Hold runs. None of the 16 reached VSN=0.8 V.
- Input native outputs: **`IVSN_0P8_TO_1P0_n*_ivsn_sys.plt`** and **`DIRECT_HOLD_n*_hold_sys.plt`**. The unprefixed `n*_...sys.plt` may be initialization-only. Prior SVisual wildcard `*_ivsn_sys.plt` found 60 files and aborted; this is an input selection failure, **not** evidence of failed IVSN.
- Constants `Ccell_F=1e-14 F` (10 fF), `VWL_HOLD=-0.7 V`, BL/body=0 V, initial SN=1 V. Current is **signed SN terminal current** from direct device+capacitor circuit, not `GIDL` from drain-based ON−OFF difference.
- 54/60 nm 1T1C SWB depth mapping derived from ordered selected-depth sweep; source SDE preprocessed files for those were not included. Exact binary grid/parent PP, contact identity, mesh, 233 K ionization and capacitance-equivalence remain open.
- Native PLT/TDR/logs remain unmodified **external D-005**; derived `ivsn_all.csv` (2020 rows), `case_metrics.csv`, matrix CSVs are archived under [data](../../data/3d_1t1c_retention_20261111/).

## 2. Retention computation and meaning

A consistent internal `VSN=1.0→0.8 V` comparison is implemented by

```text
t_est = integral(V=0.8..1.0) [ Ccell / |I_SN(V)| ] dV
I_SN(V) < 0 (discharge direction; all 20 tested cases)
Ccell = 10 fF assumed constant (no 3D Ceff validation)
```

101 sampled VSN points per case, numerical trapezoid integration, 20/20 complete SN currents. The committed [recalculation code](../../code/scripts/analysis/3d_retention_20261111/recalculate_ivsn_retention.py) reproduces the archived 20 estimates. Current model's `I_SN` includes all activated transport/leakage contributions; the calculation is a **model-internal 10-fF current-integral retention estimate**, not a measured 0.8-V crossing or a real DRAM refresh specification.

### 20-case retention estimate

| MEB (nm) | 233 K | 300 K | 340 K | 380 K |
|---:|---:|---:|---:|---:|
| 36 | 22.655 s | 67.161 ms | 10.112 ms | 1.660 ms |
| 41 | 27.106 s | 130.476 ms | 14.807 ms | 1.881 ms |
| 48 | 50.747 s | 177.004 ms | 16.435 ms | 1.941 ms |
| 54 | 81.337 s | 202.245 ms | 17.533 ms | 1.986 ms |
| 60 | 97.038 s | 233.837 ms | 18.647 ms | 2.028 ms |

General within-model observation: higher MEB gives higher estimated t for each tested temperature, whereas higher T shortens it. Relative MEB=36→60 improvement is about 4.28× (233K), 3.48× (300K), 1.84× (340K), 1.22× (380K). The apparent high-T compressed benefit is **provisional** pending temperature/physics/mesh and exact current scaling validation.

### Direct 100-ns Hold loss (microvolts)

| MEB (nm) | 233 K | 300 K | 340 K | 380 K |
|---:|---:|---:|---:|---:|
| 36 | 0.00102 | 0.42425 | 2.90384 | FAIL |
| 41 | 0.00089 | 0.22957 | 1.76831 | 11.90454 |
| 48 | 0.00003 | 0.15451 | 1.50211 | 11.16860 |
| 54 | 0.00032 | 0.13528 | 1.35356 | FAIL |
| 60 | 0.00026 | 0.11454 | 1.21112 | FAIL |

`FAIL` denotes no complete 100ns result; a partial 48nm/233K run reached ~4.9ns but is not counted as completed. Direct vs `I_SN/C` initial slope agrees within ~0.0766% relative for the 16 completed Holds. **No direct VSN=0.8 crossing**: t_est cannot be relabelled measured t_ret.

## 3. Four failed Hold cases (selective recovery only)

| MEB | Temp | Node | Known failure class | Retain |
|---:|---:|---|---|---|
| 36 | 380 K | `n1968` | Initial Coupled iteration limit before transient | full IVSN valid |
| 54 | 380 K | `n2238` | Initial Coupled iteration limit before transient | full IVSN valid |
| 60 | 380 K | `n2328` | Initial Coupled iteration limit before transient | full IVSN valid |
| 48 | 233 K | `n123` | Newton/MinStep at ~4.9ns of transient | partial Hold only, full IVSN valid |

Recovery **PLANNED, NOT EXECUTED**: preserve the 16 good Holds; try a separate high-T ramp/initialization branch for 380K and timestep/continuation checks for 233K, with T-2022.03 manual validation of any new numerical syntax. Do not change geometry/physics or auto-mark repaired until new external logs pass. Historical temperature DC failures `n1979` and `n1686` from Nov-09 are **separate** issues.

## 4. 300 K transistor/DC–Hurkx–retention synthesis (6 independent metrics)

Measurements from pre-existing [3D 140-case metrics](../../data/3d_meb_temp140_partial_20261109/MEB_5x4_TEMPERATURE_METRICS_PARTIAL.csv) at T=300 K joined on MEB with Nov-11 IVSN integral. 300K source case status is `COMPLETE` across five MEB values. Do not reinterpret 2D Run1 bias-extraction definitions as the extraction definition of this independent 3D comparison.

| MEB (nm) | Ion (µA) | Ioff (fA) | SS (mV/dec) | DIBL proxy (mV/V) | Hurkx ON−OFF excess (fA) | t_est (ms) |
|---:|---:|---:|---:|---:|---:|---:|
| 36 | 3.634 | 11.881 | 79.12 | 21.79 | 62.733 | 67.16 |
| 41 | 3.612 | 9.902 | 79.41 | 22.34 | 38.319 | 130.48 |
| 48 | 3.533 | 8.860 | 80.20 | 23.76 | 19.040 | 177.00 |
| 54 | 3.379 | 8.010 | 81.44 | 26.15 | 15.849 | 202.24 |
| 60 | 3.170 | 7.300 | 83.35 | 30.96 | 13.412 | 233.84 |

- **Ion:** 36→60 nm 12.79% decrease; `Vg=1.2V,Vd=1.2V`.
- **Ioff:** 38.56% decrease; `Vg=0,Vd=1.2V`, not the GIDL criterion.
- **SS:** 4.23 mV/dec increase, high-Vd window `1e-10→1e-8 A` (specific 3D extraction proxy).
- **DIBL:** 9.17 mV/V increase.
- **Hurkx-related excess:** 78.62% reduction, computed on **matched transistor** Hurkx ON−OFF at `VG=-0.7V, VD=1.2V`, **not independently proven pure GIDL**.
- **t_est:** 3.482× increase in the separately biased `SN=1.0→0.8V` current-integral **with assumed Ccell=10fF**.
- This is a within-working-model multi-metric **tradeoff**, **not** evidence of real produced-cell performance, causally isolated GIDL-to-retention translation, or a final optimum.
- Six original-data re-rendered [SVGs](../../data/3d_1t1c_retention_20261111/figures/) correspond to these metrics.

## 5. Mandatory claim gates

1. Validate same 3D geometry/mesh/source PP across independent campaigns (especially 54/60nm), four-terminal sign/KCL under storage bias, exact initial condition and SN node wiring.
2. Verify drain outer-boundary x≈60nm Face91/mesh attribution; test representative mesh sensitivity for IVSN, high-T current and `t_est`. Confirm 233K physics.
3. Validate `C_eff(V,T)` / cell geometry and AreaFactor (do not transfer 2D AreaFactor 0.017).
4. Recover the four Hold failures; compare direct Hold to integral across a meaningful longer voltage/time window on representative points. 100ns initial slope does not establish ms/s retention.
5. Only with a credible 3D cell Write/Read check and explicit pass/fail guardrails consider a usable MEB design range.

Related range proposal: [2026-11-11 exploratory screening](3d_meb_exploratory_range_20261111.md). Current-stage close-out: [progress](../progress/3d_1t1c_retention_checkpoint_20261111.md).
