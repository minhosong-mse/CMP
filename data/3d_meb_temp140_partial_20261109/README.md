# 3D BCAT MEB × Temperature: 140-condition screening (2026-11-09)

**Status:** `CMP-EXECUTED / EXTRACTION-PARTIAL-QC-PASSED (138/140) / SCIENTIFIC-PROVISIONAL`. This directory archives the previously executed 3D `3D-Sun-SADDLE-V1 / Flat upper S/D` *working* lineage. **Not** a calibrated paper reproduction, a mesh-converged result, an optimized design, or 1T1C retention evidence.

## Scope and provenance

- Five MEB depths `36, 41, 48, 54, 60` nm × four temperatures `233, 300, 340, 380` K × seven modes `0..6` = **140 target combinations**.
- `233/340/380 K` results (105 nodes) came from the independent SWB project `CMP_3D_Temp`; `300 K` baseline comparison (35 nodes) came from `CMP_3D_COMPETITION_DBCAT24_48`.
- The two source projects were read-only during extraction: no SDevice reruns or upstream deck changes. Public mapping uses node numbers, source roles, original PP SHA-256 and size metadata; machine absolute paths were reduced to basenames.
- Uploaded review ZIP: `CMP_3D_MEB_TEMP140_PARTIAL_REVIEW.zip`, **SHA-256 `b022ead99cc75626044bf043c7d1703f0a1dcb384927ded310d9bce338337183`**. The original complete ZIP, native TDR/PLT, full PP decks and logs remain in external user storage under D-005. Only exported CSV, field inventory, bounded run status, extracted code and derived figures are committed.
- Models and geometry comparison remain **provisional**. The supplied analytical QC reports identical SDE preprocessed SHA-256 per depth across T and normalized SDevice PP similarity for corresponding modes; native mesh TDR byte equivalence and mesh convergence are still unverified. The 300-K fallback comes from a separate source project.

## Numerical extraction QC

- Preprocessed SWB node mapping **140/140 unique**.
- Target-bias endpoint **138/140**; 2 incomplete native SDevice sweeps. All 140 raw DC curves are preserved, including the two partial curves, but **target-bias metrics exclude the two incomplete sweeps**.
- `SPATIAL_ROI_AVAILABLE.csv`: **552 rows = 138 valid device cases × four ROIs**. `SPATIAL_RAW_AVAILABLE.csv`: **3864 scalar records = 138×28**. Four Cutlines per valid case, **552** total.
- Per-case `CASE_DONE/` statuses: **138** independently verified cases. `CASE_QC_140.csv` covers all 140 attempted cases.
- `HURKX_SPATIAL_ON_OFF_DELTA_PARTIAL.csv`: mode-5/mode-6 spatial paired comparisons, excluding incomplete pairs. Values are model-dependent BTBT volume-generation equivalents, not necessarily current collected at the drain.
- Max KCL relative mismatch from the accompanying analysis: **4.873e-8**. This is a numerical-consistency check, not proof of convergence or contact attribution.

### Two incomplete native SDevice cases (do not interpolate to requested endpoint)

| MEB | T | RunMode | Node | Required Vg | Achieved Vg | Impact |
|---:|---:|---:|---:|---:|---:|---|
| 36 nm | 380 K | 5 (Hurkx ON negative-gate) | 1979 | −0.7 V | −0.66372928 V | No valid −0.7 V ON−OFF terminal comparison |
| 54 nm | 340 K | 1 (Id–Vg high Vd) | 1686 | +2.0 V | +0.108366 V | No valid high-Vd target-endpoint Id–Vg/DC metric |

The first node's native log states `Newton didn't converge`, followed by `Step-size less than MinStep (7.8735e−07)`. The second node's *numerical failure mechanism* has not yet been checked against its native solver log; only the incomplete exported curve is established. Do not treat either case as completed or attach a physical GIDL/retention conclusion to the missing endpoint.

## GitHub retained artifacts

| Location | Description |
|---|---|
| `DC_curves/` | 140 native-exported sweep CSVs, including two flagged partial-endpoint sweeps; do not misuse them as target-bias results |
| `SPATIAL_cutlines/` | 552 original exported cutline CSVs and 138 field inventories (four cutlines/case) |
| `SPATIAL_RAW_AVAILABLE.csv` | All 3864 model-internal ROI scalar records |
| `SPATIAL_ROI_AVAILABLE.csv` | All 552 four-ROI summaries, signed/positive/negative BTBT and Emax |
| `TERMINAL_AVAILABLE_QC.csv` | 138 complete-target sweep metrics and KCL QC |
| `CASE_QC_140.csv`, `CASE_DONE/`, `INCOMPLETE_CASES.csv` | Node mapping/endpoint/case state and incomplete-case evidence |
| `MEB_5x4_TEMPERATURE_METRICS_PARTIAL.csv`, `METRICS_DELTA_vs_300K_PARTIAL.csv` | 20 MEB–temperature comparisons and 300K-difference table; missing values left blank |
| `SOURCE_MAPPING_140_PUBLIC.csv`, `SOURCE_QC.json`, `EXTRACTION_STATUS.json` | Sanitized source provenance, immutable original hashes and original status |
| `HURKX_SPATIAL_ON_OFF_DELTA_PARTIAL.csv`, `CMP_3D_TEMP140_ANALYSIS_TABLE.csv`, `figures/` | Model-specific GIDL/BTBT comparison and derived charts |
| `ARTIFACT_MANIFEST_SHA256.csv` | SHA-256 hashes for exported files retained in this Git checkpoint |

Extraction code: [`code/scripts/analysis/3d_temp140_20261109/`](../../code/scripts/analysis/3d_temp140_20261109/) (use code from repo root). Findings: [`docs/evidence/3d_meb_temp140_analysis_20261109.md`](../../docs/evidence/3d_meb_temp140_analysis_20261109.md).

## Interpretation guardrails

- `Hurkx ON−OFF` terminal current is model-dependent excess, **not separately demonstrated pure collected GIDL**. `q·∫max(Band2BandGeneration,0)dV` is a BTBT **generation-equivalent** current; do not identify it as a measured terminal collection current.
- Region boundaries: Gate–Drain x=15–30 nm, Mid Drain x=30–45 nm, Outer Drain x=45–60 nm, Full Silicon separately. Outer Drain Emax repeatedly near x≈60 nm; contact/geometry Face91 and mesh sensitivity remain unresolved.
- The 233 K physics model, low-temperature incomplete ionization assumptions, junction/geometry consistency and selected-point mesh convergence are **not validated**. No 1T1C Write/Hold/Read or VSN=1→0.8 V retention time is claimed.
- The point of this dataset is **relative within-lineage** depth/temperature screening. The high-T Ioff and Hurkx-vs-Id differences cannot be mapped automatically to a DRAM retention improvement.
