# 2026-10-14 — NonlocalPath L1/L2 mesh identity, Rough R1, and 15×2×2 DC dispatch

> **Research checkpoint / IN PROGRESS / PROVISIONAL.** This is a user-observed SWB dispatch and prior-source-QC record, **not** a 60-run DC results report. No new baseline freeze, model selection, validated mesh convergence, retention claim, or README change.

## 1. Lineage and why this dispatch was chosen

- The **frozen** `B0-2D-PAPER-CAL = C7_4/B_QF_HALF` is preserved. This is a distinct **PAPER-CAL-derived NonlocalPath pilot** using GCS=2.300, GDB=25 nm, Qf_Int=+2.55e12 cm^-2, WF=4.8 eV, Jdepth=48 nm, and nominal MEB=36 nm. These are effective 2D calibration coordinates, not fabricated geometry or known experimental Qf.
- Main purpose: assess whether a numerically controlled NonlocalPath GIDL/BTBT branch can support a follow-on research baseline, **separately** from paper-matched DC characteristic and MEB sensitivity. DC checks deliberately run **BTBT OFF** to keep the historical extraction role and distinguish channel DC from tunneling leakage.
- Existing pilot OFF six depths (31/36/39/41/46/51 nm) passed source QC on 2026-10-14. Earlier ON six-depth analysis indicated distinct e/h generation endpoints; whole-Si carrier-resolved spatial-integration and ON−OFF validation on the proposed final mesh remain open. Do not infer GIDL/BTBT mesh convergence from hotspot screenshots.

## 2. Evidence obtained before the DC dispatch

| Evidence | 36 nm | 51 nm | Interpretation |
|---|---:|---:|---|
| L1/L2 effective SMesh points | 11,835 each | 11,727 each | SDE refinement numbers differ, but actual spatial vertex positions, connectivity, and all TDR numerical datasets are identical within each depth |
| L1/L2 effective SMesh elements | 23,190 each | 22,998 each | Thus **L1 vs L2 is NOT an independent mesh refinement convergence comparison** |
| L1 and L2 OFF Id (A/um) | 1.24200228624524e-12 | 2.29896989465834e-16 | identical paired OFF PLT curves at a depth; actual OFF jobs completed |
| Original L0 OFF Id (A/um) | 2.45506744220364e-12 | 4.02075383210065e-16 | comparison is provisional until common-source PP-deck audit; large residual-current sensitivity |
| L1/L2 36 nm SVisual elements / points | 24,327 / 11,835 | — | SVisual element count differs from SDevice internal triangulation accounting |
| New Rough R1 36 nm SVisual elements / points | **12,857 / 6,176** | — | observed on SDE mesh screenshot only; no R1 ON/OFF numerical convergence result yet |

- The L1/L2 OFF user evidence archive, `CMP_NONLOCAL_OFF_L1_L2_EVIDENCE.zip` (SHA256 `2688fc15b29a90ce599b4c08a3b96ff45d0e745771cfe1dfc28ef5ae1407d054`), was checked: 76/76 source manifest entries, 4/4 executed 36/51-nm OFF jobs. Independent HDF5 comparison found geometrically/data-identical meshes despite differing full-file SHA256 values (metadata paths/timestamps). Condensed CSV deposited under `data/nonlocalpath_pilot_20261013/off_l1_l2_mesh_equivalence_qc_20261014.csv`.
- ON L1 nominal 36-nm SDevice log ended normally, with final drain current approximately 1.242e-12 A/um and SVisual Band2BandGeneration max approximately 1.14771e19 cm^-3 s^-1. The latter is **screen-only**, and log current rounding does not resolve the ~1e-17 A/um ON−OFF contribution. Final TDR and source-current precision are needed; do not call it converged.
- L1 36-nm log reported min mesh angle approximately **0.33002°** and an extremely short minimum edge around **0.002165 nm**. Treat as a mesh-quality watch item, not automatic solver failure.
- Rough R1: same 2D geometry/doping/calibration, softened body/gate/junction/GIDL and NonlocalPath local refinement, preserving observed h/e-hotspot-containing windows. R1 coverage of already observed peak *coordinates* does **not** prove integrated BTBT convergence.

## 3. 300-K two-mesh DC dispatch (2026-10-14 screenshot/user report)

- **Two actual SWB project names** in screenshots: `MEB_nonlocal_1_DC` and `MEB_nonlocal_1_DC_Copy`. They are user-designated dual-mesh DC comparisons. **Which project contains L1 vs Rough R1 is NOT verified by preprocessed SDE source yet**; check `pp*_dvs.cmd`, mesh counts or actual TDR before labeling results.
- Each SWB project screenshot shows **15 distinct `MEBDepth` values** in um: `0.031 0.033 0.036 0.039 0.041 0.042 0.043 0.044 0.045 0.046 0.047 0.048 0.049 0.050 0.051`.
- Each depth is branched into **`VD_Target=0.05 V` and `1.2 V`** using the parameterized SDevice tool (SDE → SDevice → SVisual shown). Per project: 15 SDE conditions and 30 SDevice bias conditions. Across the pair: **60 SDevice conditions / 30 SDE mesh conditions intended**.
- User stated simulations were launched. Screenshot colors and node IDs alone **cannot certify completion, physically correct deck processing, or values**. Actual `.cmd`, `.log`, `.plt`, `.tdr` source outputs and node-status records have **not** been received for this DC dispatch. All 60 final results and PP/source checks remain **PENDING**.
- Prepared DC deck (`SDEVICE_DC_300K_VD_PARAMETER.cmd`, SHA256 `0a8337f181292c5de6e58991b3d3bdd1ef554234c83180c65cbd0fdd4ab481cd`): 300 K; Vg=0→2.0 V; drain=0.05 or 1.2 V; source/substrate=0; Fermi, OldSlotboom, DopingDep/HighFieldSaturation/Enormal, SRH(DopingDep), Auger, fixed positive Qf and WF=4.8 eV; **BTBT OFF**. `CurrentPlot Intervals=400` requests 401 Vg output points, not solver steps.
- Prepared source-deck SHA256: L1 SDE `9d3cbc7634ef4826da9da07016697a1f0a3d8218d6c38e5bb0c06250cfc7cf02`; R1 SDE `231921e9a044bd2e7cbcda8fcaee2f49c41b453e58d852b47a4f4e8d76c1393f`. The supplied deliverable ZIP `CMP_NONLOCAL_DUAL_MESH_DC_15MEB_20261014.zip` SHA256 `c3fd63c5cec49b7792f308a34f60ffa5a926c964e6e60b3c10f254e85349bd7c` contains both source decks, parametric/fixed-VD SDevice options, collector, 60-run matrix and SWB instructions. **ZIP contents are referenced by checksum only and have not been deposited into GitHub**.
- Screenshot provenance (originals retained in user conversation, not in this Git commit): SWB project-view image 1 SHA256 `6068089c6a2464ae323d36467730f3ad4ee14353aa429340063fccac8b2e91b3`; image 2 SHA256 `986ffb08fc577611a931ff1503f3cb8a2f11caeec20a9ab472188c78a3dfd196`.
- This comparison deck was assembled from an executed family pattern, **not demonstrated byte-identical to 2026-10-08 Atlas SDevice PP deck**. Review source differences before attributing an absolute DC current/Vth difference to mesh alone.

## 4. Extraction and paper comparison policy (planned, not yet measured)

1. Map MEB→SDE node→0.05/1.2 V SDevice nodes for each mesh; verify SDE PP source, effective mesh, SDevice actual bias, 300 K, fixed Qf, BTBT OFF, solver completion and nonempty Id–Vg terminal plots. Do not assume SWB color equals status.
2. Extract the **same** current-bias protocol for both meshes: nominal Vth via logarithmic crossing of |Id| at paper constant-current reference `1e-7×W/L A` → `5e-6 A/um` with L=20 nm; SSquick, SS1dec, SS2dec; Vth at both VD; DIBL `(Vth@0.05−Vth@1.20)/1.15×1000` mV/V; Id@Vg0,1.2,2.0; Ion/Ioff using explicitly noted CMP bias conventions.
3. At each MEB, compute L1−R1 absolute and relative differences (Vth/SS/DIBL/Ion/Ioff), including 36 nm nominal and 48 nm GateTop≈Jdepth boundary. Compare DC trend over all 15 points against validated October Atlas **only after** checking PP-deck/extraction lineage.
4. Nominal 36-nm paper headline reference: Vth≈0.656 V, SS≈76 mV/dec, DIBL≈23.6 mV/V and Ion/Ioff≈3.4e10. Literature paper `D_BCAT` sweep includes 24/36/48 nm; these two 15-depth CMP runs overlap at 36/48 but not 24 nm. SS slope-fit and DIBL bias-pair details are not fully established identical, so do not claim exact paper-to-paper extraction match. Paper uses 3D geometry; CMP uses effective 2D.
5. Do **not** infer from BTBT-OFF DC that enabling NonlocalPath has improved GIDL mechanism. Carry the ON−OFF electron/hole generation, whole-Si integrals, peak positions, edge mesh quality, Hurkx-versus-NonlocalPath **same-parent** comparison and (where needed) 3D cross-check as independent gates.

## 5. NEXT FIRST ACTION and freeze boundary

**Next first action once SWB DC outputs are available**: run the prepared `collect_cmp_dualmesh_dc.py` against the two actual project paths, explicitly map `MEB_nonlocal_1_DC`/`_Copy` to L1/R1 from PP SDE + TDR, and ingest complete 60 SDevice jobs with raw PP-CMD/log/Id–Vg PLT/mesh TDR and node mapping. Independent QC before any Vth/SS/DIBL or baseline selection; prioritize mismatched, missing or failed nodes.

**Parallel unfinished work**: R1 ON/OFF and L1 ON original source TDR/PLT, 36/48/51 mesh-bridge and carrier-integral validation, common-source Hurkx/NonlocalPath and background leakage attribution, earlier Q0/3D mechanism gates. 300/340/380 K GIDL/retention and final design range are downstream.

**Unchanged/frozen**: `B0-2D-PAPER-CAL C7_4`, legacy Atlas/Q0 numerical evidence, calibration variables, `DECISIONS.md`, repository `README.md`, existing project files. **No acceptance thresholds, mesh convergence, selected NonlocalPath baseline, retention improvement or optimum are declared by this checkpoint.**

**Previous state:** [NonlocalPath pilot checkpoint](nonlocalpath_hotspot_pilot_checkpoint_20261014.md); [model-selection credibility gate](../research/faithful_q0_model_selection_gate_20261011.md); [Atlas results](b0_2d_paper_cal_meb_atlas_300k_20261008.md).
