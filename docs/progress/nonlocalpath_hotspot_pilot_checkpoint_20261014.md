# 2026-10-14 — PAPER-CAL NonlocalPath hotspot pilot and conditional validation roadmap

> **Status: PROVISIONAL / pilot IN PROGRESS.** The BTBT-OFF selected six-point run was executed and its received evidence independently QC-reviewed; ON spatial maxima are **SVisual screenshot observations only** at 36 and 39 nm, without the ON source TDR/PP-CMD/log/terminal PLT inventory. **NO mesh convergence, full BTBT integral, model preference, re-freeze, or 1T1C/retention claim.**

## 1. Why this pilot exists

Third-week mentor feedback raised (i) low sensitivity of 2D DC SS/Vth to MEB-depth changes compared with Sun et al. 3D BCAT figures; (ii) a request to compare Hurkx vs NonlocalPath GIDL/BTBT on matched axes; and (iii) the possibility of retaining the DC-matched effective 2D baseline **provided** leakage/BTBT mechanisms and further validation become defensible.

**Proposed, not adopted:** test the existing DC-matched PAPER-CAL geometry/three effective calibration coordinates with NonlocalPath BTBT; identify actual source regions under the *current* SDE mesh; separately converge a common mesh policy; remeasure full MEB spatial BTBT and terminal leakage using a controlled Hurkx/NonlocalPath bridge; evaluate DC structural sensitivity as a separate gate; only then decide whether a NonlocalPath branch can serve as a follow-on conditional research baseline.

Do **not** assume that changing BTBT physics improves Vth/SS MEB sensitivity: existing DC extraction used BTBT OFF, and its structural sensitivity is not resolved by a tunneling-model substitution alone.

## 2. Source / lineage and controlled conditions

- Existing frozen baseline remains **B0-2D-PAPER-CAL C7_4 / B_QF_HALF**, *not* replaced. The new experiment is a separately labeled **PAPER-CAL-derived NonlocalPath SCREENING branch**, not a clean exact-parent Hurkx-to-Nonlocal model-only bridge yet.
- User SWB OFF project: `/user/semi/semi333/MEB_nonlocal_off`. Separate ON project/screen: `/user/semi/semi333/MEB_nonlocal`.
- OFF SDE preprocessing verified: same configured `GateCouplingScale=2.300`, `GateDepthBoost=0.025 um`, `Jdepth=0.048 um`, `MeshLevel=2`, `MEBDepth` per case.
- OFF SDevice preprocessing verified: `Qf_Int=+2.55e12 cm^-2` implemented using `Physics(MaterialInterface="Silicon/SiO2") { Traps((FixedCharge Conc=2.55e12)) }`; `WF=4.8 eV`, 300 K, `Vd=+1.2 V`, `Vg=-0.7 V`, Source/Substrate 0 V, **BTBT OFF**.
- The assembled pilot SDevice command was **not proven byte-for-byte equivalent** to the executed 2026-10-08 PAPER-CAL Hurkx Atlas parent. The OFF-control mismatch below makes this provenance distinction consequential.
- User screenshot selected six depths: **31/36/39/41/46/51 nm**. This selection contains **46 nm, not 48 nm**; 48 nm remains an unscreened boundary point for this new pilot.
- Source ZIP received via chat: `CMP_NONLOCAL_OFF_6_EVIDENCE.zip`, SHA256 `086d50fadc4a271728030b42000aac62015ea77562c3bc1fbcecc3b1f6fe1e92`. The received archive's manifest covered 104 source files with checksum/length PASS; ZIP CRC PASS. **Original ZIP not included in this GitHub commit**; numerical audit is deposited under `data/nonlocalpath_pilot_20261013/`.

## 3. What is actually complete: OFF six selected depths

**CMP-EXECUTED / validated from raw archived PP-CMD, PLT, logs:** six SDevice jobs reached `Vd=+1.2 V, Vg=-0.7 V`; log completion/sweep checks PASS, 141 requested PLT samples each; electron+hole/contact terminal KCL cross-check PASS. Read `data/nonlocalpath_pilot_20261013/off_6_qc.csv` for per-depth signed drain-hole/electron contributions and full QC values.

| MEB (nm) | Pilot BTBT-OFF total drain Id (A/um) | Historical Atlas Hurkx-BTBT-OFF Id (A/um) | Pilot / old |
|---:|---:|---:|---:|
| 31 | 1.51345915e-10 | 6.33104944e-11 | 2.391 |
| 36 | 2.45506744e-12 | 9.04154436e-13 | 2.715 |
| 39 | 2.70913375e-13 | 9.42003909e-14 | 2.876 |
| 41 | 7.18988405e-14 | 2.40259071e-14 | 2.993 |
| 46 | 3.96635632e-15 | 1.21253651e-15 | 3.271 |
| 51 | 4.02075383e-16 | 1.05710774e-16 | 3.804 |

**Critical blocker:** these are both BTBT-OFF drain currents, yet the pilot/old ratios are ~2.39–3.80. Therefore no ON difference may be attributed solely to Hurkx versus NonlocalPath until parent physics, numerical solver, interfaces, source geometry/mesh, electrode carrier channels, units/2D normalization and extraction ancestry have been compared. This is not a demonstration that NonlocalPath lowers leakage. Pilot OFF drain-hole component dominates the total current at most points, and its microscopic residual source is not yet independently resolved.

## 4. ON screenshot observations only: 36/39 nm hotspot

User SVisual screen, full Silicon maximum of **`Band2BandGeneration`**, one plot at each depth, nominal 300 K/GIDL endpoint (precise actual ON deck/terminal condition not yet independently inspected in this new source review):

| MEB (nm) | Max Band2BandGeneration (cm^-3 s^-1) | Xhot (um) | Yhot (um) | Xhot - GateTop (nm) | SVisual node | Status |
|---:|---:|---:|---:|---:|---|---|
| 36 | 6.32186e18 | 0.0369141 | 0.252174 | +0.9141 | ON-project `n49_des` | SCREENSHOT-OBSERVED |
| 39 | 2.01641e18 | 0.0398437 | 0.252174 | +0.8437 | ON-project `n50_des` | SCREENSHOT-OBSERVED |

- 36→39 nm **pointwise plotted maximum** decreases ~68.1%; two points alone do NOT establish monotonic 15-depth trend, total BTBT generation, total GIDL current, or 3D physical correctness.
- Both plotted maxima lie near the **drain-side GateTop** and track it (~0.84–0.91 nm below GateTop). This describes only the shown field. Global maxima and spatial distributions of `eBand2BandGeneration` and `hBand2BandGeneration` must be inspected **separately**, as NonlocalPath may yield distinct electron/hole distributions.
- User-reported SVisual mesh status at 36 nm: 15,279 elements/7,384 points; at 39 nm: 15,253 elements/7,370 points. Global counts are **not local hotspot resolution or convergence evidence**.
- Two screenshots were furnished in the chat but **PNG files are not part of this commit**. Their original PNG SHA256 are respectively `87b7e91dae3419e2826fd483857b048ca8de9767b7631268bb99f64f612d96d2` (36 nm) and `3f7a3448d52a0ee03ec6b287576e2214834b5f750475bca55a6c007ab36eeb4f` (39 nm). The derived text observations are recorded under `data/nonlocalpath_pilot_20261013/on_2_hotspot_svisual.csv`.
- Historical Hurkx Atlas 36/39-nm peak maxima, hotspot positions and whole-Si integrals live in `data/paper_cal/atlas_300k_20261008/processed/MEB_300K_ATLAS_MASTER_VALIDATED.csv`. **Do not treat the old-vs-new peak magnitude or trend as controlled model-only difference**, given the OFF discrepancy and missing ON source audit.

## 5. Next actions: scientific gate sequence, not executed results

1. **Finish the pilot evidence**: collect per-point ON actual preprocessed SDevice CMD, log, terminal PLT, final spatial TDR and exact SDE mesh mappings for the chosen six depths. Include **48 nm** at the mechanism-critical Jdepth crossing before freezing a mesh policy. Validate applied voltage, fixed Qf, 300 K, and whether ON and OFF are same parent apart from `Band2Band`. Preserve the prior OFF source ZIP untouched.
2. **Full-domain spatial map before local mesh design**: at 31/36/39/41/46/**48**/51 nm, find whole-Si maxima, coordinates, charge carrier-specific e/h BTBT maps, integrated e/h BTBT generation, and surface-side local maxima. Identify active GateTop and Surface regions independently; do not assume only one hotspot.
3. **Separate new numerical mesh family**: keep the frozen physical geometry/calibration/48-nm junction, change only SDE refinement policy in an explicitly new mesh branch. Refine **both** GateTop-following and all observed surface-side ROIs as needed, use common coverage across models/depths; test selected-point refinement levels until terminal current, spatial integrals, maximum coordinates/regions and extraction become acceptably stable. A single new mesh is NOT convergence.
4. **Controlled BTBT/GIDL model bridge, then full 15 MEB**: run same new parent geometry, mesh, bias, temperature, traps, mobility, Math/Solve/extraction and unit normalization with NonlocalPath ON, Hurkx ON and common BTBT OFF; first test representative cases, then 15 MEB. Compare signed total drain current, electron/hole decomposition, ON−OFF current sensitivity, whole-Si signed/positive-integrated e/h generation, hotspot/active area, local E-field and Cgd/DC guardrails where mesh changes affect them. Avoid calling total GIDL-bias drain leakage pure BTBT.
5. **DC sensitivity separate gate**: compare paper's `D_BCAT`/MEB trend with 2D `Vth`, SS, DIBL, Ion on matched extraction conditions, paying attention to 36 and 48 nm and paper 3D geometry. The current PAPER-CAL Atlas 36→48 nm nominal `SSquick@Vd1.2` changes only +0.043 mV/dec and `Vth@Vd1.2` -0.362 mV. Nonlocal BTBT substitution does not by itself prove improved sensitivity for DC calculations performed with BTBT OFF. If the sensitivity remains different, document 2D limitation or independently justified geometry/physics changes rather than depth-wise Qf fitting.
6. **Conditional baseline decision**: only after converged numerical comparison, source-matched Hurkx/NonlocalPath evidence, credible leakage/BTBT mechanism and separate DC sensitivity acceptance consider a distinct NonlocalPath-based 2D research baseline. Do not silently reassign `B0-2D-PAPER-CAL` or replace its frozen evidence; a selected-point 3D comparison remains an important credibility cross-check before causal GIDL→Retention claims.

**Immediate next first action:** receive/audit the **remaining NonlocalPath ON source files** (including initial 36/39 TDRs), and inspect their full Silicon carrier-resolved BTBT maps with the existing MeshLevel2; **do not yet design/freeze the new mesh solely from screenshots**.

## 6. Freeze / preservation / links

- **No change** to `B0-2D-PAPER-CAL` frozen GCS/GDB/Qf, 2026-10-08 Hurkx Atlas, historical Faithful-Q0, old FZ-C, README, official model-selection decision or result claims.
- **Parallel work remains open**: pending other-depth thermal DC source collection, PAPER-CAL Surface/Gate ROI, Q0 Surface-L1 numerical validation and later selected-point 3D checks; this NonlocalPath screen does not automatically close or supersede those requirements.
- References: [model-selection gate](../research/faithful_q0_model_selection_gate_20261011.md); [2026-10-12 ROI/mesh checkpoint](../evidence/btbt_roi_hotspot_mesh_checkpoint_20261012.md); [Atlas QC and lineage](b0_2d_paper_cal_meb_atlas_300k_20261008.md); [live handoff](../../HANDOFF.md).
