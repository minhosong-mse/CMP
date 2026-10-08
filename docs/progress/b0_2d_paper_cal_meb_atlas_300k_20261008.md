# B0-2D-PAPER-CAL — 300 K 15-point MEB Atlas: Interim Evidence Review
> **Status: DATA-VALIDATED / MODEL-LINEAGE BRIDGE OPEN. Not a final physical optimum or retention conclusion.**
> Date: 2026-10-08. Source: user-exported `CMP_MEB_ATLAS_300K_EVIDENCE.zip` (immutable raw archive).

## 1. Provenance and scope

- Target main lineage: `B0-2D-PAPER-CAL / C7_4 / B_QF_HALF`, 2D simplified BCAT. Current series is a **post-freeze production-mesh branch** (Level 2).
- Frozen calibration inputs: `GateCouplingScale=2.300`, `GateDepthBoost=25 nm`, `Qf_Int=2.55e12 cm^-2`, `WF=4.8 eV`; no retuning in this analysis.
- The exact executed original 2026-10-05 FZ-C parent is **not yet recovered/bridged**. The GitHub `b0_2d_production_revalidation_plan.md` and `b0_2d_paper_cal_mesh_revalidation_20261007.md` preserve this restriction. This 15-point set establishes **within-branch** trends, not proof of mesh-only identity to the historical freeze.
- Biases: GIDL `Vd=1.2 V`, `Vg=-0.7 V`, 300 K, Hurkx ON/OFF; Cgd `1 MHz`, `Vd=1.2 V`, `Vg=-0.7 V`, BTBT OFF; DC `Vd=0.05/1.2 V`.
- MEB: `31/33/36/39/41/42/43/44/45/46/47/48/49/50/51 nm`.
- Imported source summary CSVs: 6 branches × 15 = 90; source curve CSVs: 105 (unchanged archive); independent check count: 1036, all passed.
- `GIDL_End` is **total signed drain leakage at GIDL bias**, not a pure measured BTBT component; `Cgd_abs` is a **project-internal raw AC capacitance-matrix metric**, not a calibrated production-cell overlap capacitance.
- 2D ∫BTBT is per-unit-width model metric. No 3D equivalence, process optimum, physical retention time, or refresh claim is supported.

## 2. Data QC and numerical controls

- All 90 summary files present; exact 15-point MEB coverage for each branch; no duplicates.
- DC endpoints and constant-current Vth reached; GIDL ON/OFF endpoints and signed currents present; AC point bias and 1 MHz verified.
- DC-low summary has no explicit MeshLevel column; mesh Level 2 is supported by SWB/deck lineage and all other extraction branches, not a row-wise assertion from the DC-low CSV itself.
- ON/OFF terminal KCL checked; max relative residual: `4.525e-12`.
- Max Cgd `|c(g,d)|` vs `|c(d,g)|` reciprocity discrepancy: `0.001803%`.
- Relative mismatch of signed ON−OFF vs `q*∫BTBT`: maximum `0.6193%` at 31 nm; 36–51 nm well below 0.01%. This is a **consistency/transport diagnostic** under the tested settings, not an identity guaranteed for other configurations.

## 3. Selected data points (full 15-point values in validated master CSV)

| MEB (nm) | Total Id ON (A/um) | Residual Id OFF (A/um) | ON−OFF (A/um) | q∫BTBT (A/um) | Hurkx-sensitive fraction | Cgd raw | Ion @ Vg=1.2 (A/um) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 31 | 6.3377e-11 | 6.3310e-11 | 6.6617e-14 | 6.7032e-14 | 0.11% | 1.5857e-16 | 2.4456e-04 |
| 33 | 1.1038e-11 | 1.0954e-11 | 8.4369e-14 | 8.4478e-14 | 0.76% | 1.5214e-16 | 2.4433e-04 |
| 36 | 1.0886e-12 | 9.0415e-13 | 1.8440e-13 | 1.8441e-13 | 16.94% | 1.4244e-16 | 2.4396e-04 |
| 39 | 3.6375e-13 | 9.4200e-14 | 2.6955e-13 | 2.6954e-13 | 74.10% | 1.3230e-16 | 2.4355e-04 |
| 41 | 2.7258e-13 | 2.4026e-14 | 2.4855e-13 | 2.4854e-13 | 91.19% | 1.2614e-16 | 2.4325e-04 |
| 42 | 2.3660e-13 | 1.2658e-14 | 2.2394e-13 | 2.2393e-13 | 94.65% | 1.2329e-16 | 2.4311e-04 |
| 43 | 2.0603e-13 | 6.7725e-15 | 1.9925e-13 | 1.9924e-13 | 96.71% | 1.2052e-16 | 2.4293e-04 |
| 44 | 1.8053e-13 | 3.7407e-15 | 1.7679e-13 | 1.7678e-13 | 97.93% | 1.1789e-16 | 2.4277e-04 |
| 45 | 1.5804e-13 | 2.1085e-15 | 1.5593e-13 | 1.5593e-13 | 98.67% | 1.1533e-16 | 2.4259e-04 |
| 46 | 1.3488e-13 | 1.2125e-15 | 1.3367e-13 | 1.3367e-13 | 99.10% | 1.1287e-16 | 2.4241e-04 |
| 47 | 1.1493e-13 | 7.1546e-16 | 1.1422e-13 | 1.1421e-13 | 99.38% | 1.1049e-16 | 2.4223e-04 |
| 48 | 9.9516e-14 | 4.3009e-16 | 9.9086e-14 | 9.9079e-14 | 99.57% | 1.0817e-16 | 2.4202e-04 |
| 49 | 8.2335e-14 | 2.6423e-16 | 8.2071e-14 | 8.2067e-14 | 99.68% | 1.0593e-16 | 2.4183e-04 |
| 50 | 6.7815e-14 | 1.6530e-16 | 6.7650e-14 | 6.7646e-14 | 99.76% | 1.0374e-16 | 2.4160e-04 |
| 51 | 5.5836e-14 | 1.0571e-16 | 5.5731e-14 | 5.5725e-14 | 99.81% | 1.0163e-16 | 2.4140e-04 |

## 4. Main within-branch observations

- **Total current:** 31→51 nm falls 1135.0×; nominal 36→51 nm falls 19.50×. All 15 ON currents decrease monotonically.
- **Cgd:** 31→51 nm decreases 35.91% without sharp break at 48 nm. This indicates global coupling reduction, not direct local-field causality.
- **DC penalty:** Id @Vg1.2 decreases 1.30%; Id @Vg2.0 decreases 6.46%. DIBL rises 0.459 mV/V and SSquick@Vd1.2 rises 0.069 mV/dec.
- **Peak/spatial split:** E@BTBT peaks at 39 nm; BTBTmax at 41 nm; ∫BTBT peaks at 39 nm, whereas terminal leakage falls throughout. The 20%-threshold active area decreases strongly. Peak or spatial area alone therefore cannot explain terminal leakage across all MEB.
- **Hurkx activation:** shallow 31–33 nm current is mostly BTBT-OFF residual; the ON−OFF fraction increases through 36 nm (16.94%), 39 nm (74.10%), 41 nm (91.19%), and 51 nm (99.81%). These fractions are *sensitivity to enabling the model*, not a decomposition proven independent of self-consistent electrostatics.
- **Conversion check:** ON−OFF ≈ `q∫G_BTBT dA` across all 15 points, within max 0.62% (worst 31 nm: subtraction of nearly equal currents).
- **48-nm model boundary:** 47→48 reduction 13.4%, 48→49 17.3%, 49→50 17.6%, 50→51 17.7%. No positive evidence of an electrical knee at 48 from terminal leakage or Cgd. `GateTop≈Jdepth=48 nm` remains a geometry/model-internal marker.
- **Fixed Y-cut caution:** Y=0.252174 um captures only ~5.9% of global peak at 31 nm, ~16.6% at 33 nm, and ~62.6% at 36 nm. It becomes representative for the deep side. Use the 2D silicon integral and threshold area to compare all points; fixed cut is a common location descriptor, not universal hotspot-following measure.

## 5. Figures (one chart per file)

1. `figures/01_terminal_current_components`: semilog total, residual, ON−OFF and q∫BTBT.
2. `figures/02_hurkx_sensitive_fraction`: fraction vs MEB.
3. `figures/03_cgd_coupling`: raw AC coupling.
4. `figures/04_btbt_spatial`: integrated BTBT nonmonotonicity.
5. `figures/05_btbt_active_area`: 20%-active area.
6. `figures/06_dc_ion`, `07_dc_dibl`: DC guardrails.
7. `figures/08_peak_btbt`, `09_ehot`: spatial peaks.
8. `figures/10_selected_fixedcut_profiles`: 31/36/39/48/51 nm profiles (shallow cut limitation).

## 6. Unresolved gate before interpreting this as official PAPER-CAL replacement

1. Reconcile 2026-10-05 executed C7_4/FZ-C parent SDE/device/extraction with current working mesh branch. Old documents explicitly classify this bridge as open. **Do not rewrite the old FZ-C freeze**.
2. Compare nominal (36 nm) low/high Vth, GIDL and spatial E against frozen reference under identical decks; avoid treating any absolute differences as mesh-only effects until controlled.
3. Residual OFF leakage at shallow MEB still lacks mechanism-resolved spatial current evidence; the ON/OFF diagnostic identifies the residual current, not its microscopic mechanism.
4. The current series ends at 51 nm with continued total leakage improvement; no globally optimal depth, robust window, or local 0.5/0.1 nm sweep decision is established.
5. Temperature and new PAPER-CAL 1T1C Write/Hold/Read/retention have not been performed on this branch. Decide selected temperature points **after** documentation/lineage gate is addressed.

## 7. Evidence/close-out status

- **DATA:** completed and independently QC-validated; raw user ZIP is immutable source with SHA256 manifest.
- **WITHIN-BRANCH MECHANISM:** strong terminal–spatial numerical consistency; separate ON vs OFF diagnostic; global Cgd correlation not asserted causal.
- **FZ-C EXACT-PARENT IDENTITY:** not demonstrated; explicitly open.
- **NEXT:** synchronize derived evidence to GitHub with this caveat; keep historical freeze unchanged; then plan temperature and 1T1C under an explicitly approved numerical lineage.