# CMP Research Handoff

## 2026-10-25 — 3D independent working baseline selected; Vg0.6 native TDR source-spatial QC COMPLETE (SESSION CLOSED)

- **User scope decision:** use the independently constructed **`3D-Sun-SADDLE-V1 / Flat upper S/D`** as the **active research WORKING BASELINE** for subsequent MEB→GIDL/BTBT/E→Cgd→temperature→1T1C. No mandatory 2D revalidation or absolute Sun-paper force-fit. Keep the old 2D branches separate, historically valid but not inputs to the new 3D analysis.
- **Baseline selection:** fixed current geometry/physics (`Lg20nm, Wfin17nm, Tox5nm, recess120nm, nominal junction48nm, WF4.8eV, Mesh A CurveGrid1, Hurkx ON`); **WORKING SELECTED / NOT PAPER-CALIBRATED OR FULL MESH-CONVERGED**. It is acceptable that paper and CMP differ in nominal Vth and some MEB current orderings; disclose, do not claim paper reproduction.
- **Executed this session:** 24/36/48nm distinct SDevice reruns at **Vg0.6 Vd1.2 T300 Hurkx ON** from existing meshes, three 3D HDF5 TDRs successfully generated and ZIP-manifest SHA256 verified. Native tetra-interpolated matched-Silicon analysis at x−15nm shows 24→48 mean φ +2.5624mV, sampled eDensity +14.0663%, native drain Id +14.0713% (6.197e−10→7.069e−10 A). These align with a **channel-electrostatic explanation** of the Vg0.6 current inversion, **not proven unique transport saddle or causality**. MEB 36 Mesh A/B Id sensitivity ≈5% is a numerical caveat.
- **Earlier 15/15 DC sweep comparison remains:** general Id–Vg turn-on and high-Vg Id–Vd shapes broadly reasonable, Id–Vd Vg1.2 order agrees paper (24>36>48), Vg0.6 order opposite (48>36>24), low-Vg Id–Vg OFF order opposite; paper Vth~0.656V vs CMP high-Vd ~0.783V. Uniform Vth shift can help explain 0.6V **absolute current amplitude**, not the MEB order reversal by itself. Vg0.1 native 36nm primarily Drain–Body current. Do not label raw drain leakage pure GIDL.
- **Evidence:** [2026-10-25 analysis/selection](docs/progress/3d_vg06_channel_working_baseline_closeout_20261025.md), [raw-TDR hashes and extracted CSV/plots](data/3d_vg06_channel_validation_20261025/README.md). Full source HDF5 TDR, logs and fine-grained CSV/PNG remain immutable externally; Git stores validated summary and SVG trend plots. Previous 2026-10-24 report is historical predecessor, not erased.
- **NEXT FIRST ACTION:** directly continue the **3D** model with matched **24/36/48nm, T300K, Vd1.2V, Vg≈−0.7V** Hurkx ON/OFF, signed four-terminal leakage/KCL plus Gate–Drain/Outer Drain spatial E-field/BTBT. Perform a **bounded** x≈60nm Drain contact/boundary check as part of leakage interpretation, not an open-ended baseline rebuild. Then 3D Cgd → temperature → 1T1C. No root README edit, no geometry/WF retune without new explicit scientific reason.
- **Status:** session CLOSED; no final GIDL/Retention/optimum/production claim; frozen 2D historical data left intact.


## 2026-10-24 — 3D Sun Flat S/D MEB 24/36/48 paper-calibration interim review (EXECUTED / MODEL MECHANISM SUPPORTED / PAPER FIT PARTIAL)

- **Current lineage and status:** `3D-Sun-SADDLE-V1 / Flat upper S/D`, 20nm Lg / Wfin17nm, Mesh A/CurveGrid1 policy, **WF4.8eV frozen**, 300K, Hurkx ON unless deliberate OFF control. **PROVISIONAL; NOT a paper-reproducing calibrated or frozen 3D baseline.** The frozen 2D `B0-2D-PAPER-CAL C7_4` remains separate/untouched.
- **Executed DC:** 15/15 24/36/48-nm five-sweep devices successfully completed; **2,337** original solver-log terminal points. Colliding native current-PLT naming left only 48nm native five sweeps in the archive; all 24/36/48 trend values recovered from independent execution logs (~4 significant digits) and verified against independent native 36/48nm traces. Sun Table1 DBCAT: high-Vg Id–Vd 24>36>48 direction agrees; Vg0.6 Id–Vd opposite; Id–Vg OFF 24>36>48 vs paper raster 48>36>24 opposite. Nominal paper Vth0.656 V vs project 36nm high-Vd ~0.783 V; SS~75.887 vs76, DIBL~21.9 vs23.6 (definitions not fully equivalent); low-Vg output amplitude strongly mismatched.
- **Executed Hurkx ON/OFF:** 24/48nm matched 107-point high-Vd Id–Vg, with only `Recombination(Band2Band(Hurkx))` removed for OFF; 36nm Vg0 uses separately executed 2026-10-21 HIGHNEG historical reference. At Vg0/Vd1.2, ON−OFF excess **18.1073/6.6398/3.6435 fA** for 24/36/48. Removing Hurkx eliminates **99.7524%** of 24−48nm ON depth difference. Vg0.6 reversed depth ordering survives Hurkx removal, indicating a separate channel-electrostatic issue.
- **Executed spatial:** 24/36/48 ON + 24/48 OFF 3D SVisual ROI analysis, **15 ROI entries**; signed/positive/negative integral QC passed after dimension correction. 24→48 Gate–Drain x15..30nm `|E|max` −**43.36%**, positive BTBT qG −**99.9954%**; 24→48 decrease in total three-ROI qG **14.465477 fA**, of which **83.888%** comes from Gate ROI, comparable with terminal model-dependent ON−OFF reduction **14.463770 fA** (difference-of-differences residual **0.0118%**). These are **geometric ROI generation equivalents, not terminal-collected physical GIDL**. Outer Drain x≈60nm field remains ≈3.3MV/cm and is the dominant residual generation at 48nm; full contact/geometry artifact not excluded. Original full TDR binaries were not included in spatial extracted ZIP.
- **Data/progress/visuals:** [interim review](docs/progress/3d_sun_meb_paper_interim_20261024.md) and [CSV/figure index](data/3d_sun_meb_paper_interim_20261024/README.md) with new **4 SVG graphs**, CSVs, original ZIP/file hashes and paper DOI. The paper's raster graphics are referenced, not republished. No root README edit.
- **NEXT FIRST ACTION:** reuse existing full native 3D TDR/SDE/Drain Face91 evidence to verify whether x≈60nm Outer Drain hotspot is contact/boundary-driven; establish geometry/doping/ROI membership before making a pure GIDL or paper-equivalence claim. **Second:** channel barrier/Vth and Vg≈0.6V crossover comparison at fixed geometry and WF. **Third conditional:** negative-Vg (around −0.7V) 24/36/48 spatial BTBT + signed terminal validation after boundary interpretation. Only then consider 3D Cgd/temperature/1T1C. Do not reopen full sweep, force-fit WF/geometry or promote a 3D optimum/retention conclusion.
- **Frozen/do-not-reopen:** 2D C7_4; original 3D source decks/evidence; physical geometry/doping/WF4.8eV; no 3D paper calibration freeze; no root README update or publication claim. **Read next:** new 2026-10-24 progress → new 2026-10-24 data index → earlier 2026-10-21 boundary report only as needed.

## 2026-10-22 — Sun 3D 36 nm paper DC overlay + five executed curves (CLOSE-OUT; PAPER FIT PARTIAL, MEB TREND NEXT)

- **Current stage/lineage:** independently **PROVISIONAL** `3D-Sun-SADDLE-V1 / Flat upper S/D`, Mesh A CurveGrid1 (SDE n41, SDevice n47), 300 K, WF 4.8 eV, MEB/DBCAT 36 nm, Hurkx ON. The user's latest explicit direction is **paper-referenced 3D DC comparison followed by MEB 24/36/48 trend test**, not further contact/mesh/Hurkx diagnostic proliferation. Historical 2026-10-21 next-task gate is **superseded as a planning directive**, not erased as evidence.
- **COMPLETED:** T-2022.03 SWB Id–Vd Vg=0.1/0.6/1.2 V (204 valid points EACH; Vd=0.0012..1.2 V); reused native Id–Vg Vd=0.05/1.2 V (60/107 points). All 5 native PLTs collected and displayed in SVisual after Tcl label quote correction and collector's valid first-Vd tolerance fix (no SDevice retune/reexecution). Exact PLT hashes, archive SHA, data locations and visual **5-curve SVG** in [data index](data/3d_sun_b0_paper_36nm_20261022/README.md); interpretation in [close-out progress](docs/progress/3d_sun_b0_paper_36nm_20261022.md).
- **Paper comparison:** uploaded original Sun et al. (2022) PDF, Table 1 DBCAT row (36 nm reference). CMP HIGHVD Vth ~0.782709 V vs nominal paper 0.656 V, SS project ~75.887 mV/dec low-Vd vs paper 76, DIBL ~21.882 mV/V vs 23.6 (conditions not guaranteed identical). With illustrative /0.017-µm current normalization, Id–Vd Vg=1.2 V Vd=1.2 V 2.13779e-4 A/µm is broadly same order as paper, but Vg=0.1/0.6 V results (5.29591e-13/3.76644e-8 A/µm) are orders below paper raster. Paper absolute baseline **NOT reproduced**, qualitative Id–Vg trend partly similar. Original paper-vs-CMP overlay PNG delivered to user; paper data are graphical and not treated as exact numeric samples.
- **Next FIRST TASK:** preserve nominal geometry, contact scheme and WF **4.8 eV** unchanged; generate **MEB/DBCAT 24 and 48 nm** beside executed 36 nm at matched Mesh-A policy, 300 K, Hurkx ON; run **Id–Vg Vd=1.2 V** and **Id–Vd Vg=0.1/0.6/1.2 V**. Compare 24/36/48 direction and curve shape with Sun Table 1 before adopting a **trend-only** provisional 3D baseline. Following supported trend: study MEB→GIDL/BTBT/E-field/Cgd→temperature→1T1C; none of those downstream runs/retention claims are completed in this checkpoint.
- **Frozen/do not reopen:** 2D C7_4 and earlier experiments; no geometry/WF calibration, no extra boundary diagnostic unless a later result *requires* it; no root README, no claim of paper-equivalent current normalization, GIDL absolute collection, 3D production optimum or 1T1C retention.

## 2026-10-21 — Flat S/D boundary and Mesh A Hurkx ON/OFF close-out (NUMERIC QC COMPLETE; GIDL CLAIM PROVISIONAL)

- **New selected-point checkpoint:** [progress](docs/progress/3d_flat_sd_boundary_hurkx_20261021.md), [native-hash/derived evidence](data/3d_sun_flat_sd_hurkx_20261021/README.md), [ON/OFF control code](code/scripts/analysis/3d_flat_sd_hurkx_20261021/README.md). Old 2026-10-20 Flat CurveGrid A/B checkpoint remains historical parent, not overwritten.
- **Executed:** native HIGHNEG Mesh A n41→n47, T300K/DBCAT36nm, Vd1.2V/Vg0→−1V, 205/205 matched original ON vs single-clause Hurkx-OFF, 4-terminal KCL both pass; reproduced ON original Id, no physical/solver retuning. At −1V drain +9.1393006812e−14A ON vs +5.3737137583e−15A OFF; Δ=8.6019293054e−14A, **94.1202% ON-reference reduction**. Substrate counterbalances drain; Source negligible. This demonstrates **Hurkx-model-dependent drain-body current**, NOT pure terminal-collected GIDL.
- **Executed spatial QC:** 12 ON/12 OFF SVisual 3D-TDR cuts, 843 matched coordinate/doping points; E-field differs ≤0.1V/cm at sample positions and x=60nm outer |E|max remains ~3.85967MV/cm with Hurkx OFF, while OFF Band2BandGeneration=0 across samples/three ROI maxima. Previous Mesh A/B 12-cut outer-boundary x-gradient and BTBT-GateDrain mismatch confirmed. Native SDE pp41/n41 face selection returned Drain **Face 91** at x60nm probe z−25nm; **full face extent and hotspot Face91 membership NOT VERIFIED**.
- **Next FIRST TASK:** isolate one drain-domain/contact-placement *boundary sensitivity* preserving model/active core/doping/WF/mesh controls; additionally calculate full 3D **signed** ON/OFF BTBT volume generation (positive, negative, net), distinguish terminal collection, verify face geometry. Only if boundary physically resolved consider selected MEB36↔48 at matched 300K. No global 3D DOE, temperature/retention, root README, public baseline promotion or frozen 2D C7_4 edits.
- **Sources:** 2026-10-21 user native ZIPs and derived CSVs are hash indexed; raw TDR/PLT/log ZIPs external to GitHub, not rewritten. D-050/D-051/D-052 stay in force.


## 2026-10-20 — CURRENT: Flat S/D CurveGrid A/B 300K/36nm DC+spatial QC complete (PROVISIONAL)

- **Current lineage:** separately provisional `3D-Sun-SADDLE-V1 / Flat upper S/D` under D-051. Native SDE/SMesh Case 0..6, LocalCase1/2, CadSeamCase0..3 and CurveGrid1/2 were executed and independently checked; data/code/report: [new checkpoint](docs/progress/3d_sun_saddle_v1_flat_sd_ab_20261020.md), [machine-readable evidence](data/3d_sun_flat_sd_ab_20261020/README.md). Older 2026-10-19 SDE-only next steps below are **HISTORICAL/SUPERSEDED by this current section**, not deleted.
- **Numerically executed:** 300K Hurkx/36nm six SDevice sweeps across `B0_3D_low`, `B0_3D_highpos`, `B0_3D_highneg`; Mesh A CurveGrid1 SDE n41 → Device n47, Mesh B CurveGrid2 SDE n46 → Device n48, per project. All six completed 60/107/205 terminal points per mesh and passed KCL check; all 24 full spatial TDR snapshots matched to 12 bias conditions. A 352400 tets, B 459464; 0 SnMesh non-Delaunay boundary faces on both; residual A114/B198 short edges <0.1nm remain.
- **Matched A/B indicators:** LOWVD Vth 0.807873/0.811448V; HIGHVD Vth 0.782709/0.785035V, A/B Vth difference <3.6mV; LOWVD SS 75.887/76.195mV/dec. HIGHNEG Vd1.2/Vg-1 q∫positive-BTBT dV = 8.3979e-14/8.4000e-14A (+0.025%), both drains ~9.14e-14A; 0→-1V positive BTBT grows ~12.88x and x15..30nm fraction 22.48→74.23% (A). This is **generation-equivalent, NOT terminal GIDL**.
- **Blocked physical claim:** global electric-field maximum consistently at x=+60nm finite drain outer boundary; at HIGHNEG -1V, drain→body terminal path dominates, and negative gate-correlated positive BTBT shifts toward gate-drain. Hurkx contribution, domain/contact/implant sensitivity and signed generation-to-terminal collection are **not separately proven**. Short Tetra angles remain; two-grid numerical agreement is NOT full physical mesh convergence or paper-equivalent GIDL. No MEB48/temperature/retention transfer has been executed here.
- **NEXT FIRST ACTION (must run before any larger batch):** use existing 3D PP-SDE/CMD and full native HIGHNEG TDR to audit x=+60nm drain-domain surface/contact, doping and E hotspot against gate-drain x15..30nm at Vd1.2V/Vg-1V. Then one bounded Hurkx ON/OFF counterpart at 300K/36nm on A, comparing signed drain/source/body currents, KCL and positive/negative BTBT integral. If domain peak remains unphysical/unresolved, one isolated domain/contact sensitivity control. Only after mechanism attribution, selected MEB36 vs48nm under matching ROI/bias/model; retention & temperature downstream.
- **Frozen / do-not-reopen:** original B0-2D-PAPER-CAL C7_4, older 3D-Sun-B0 role in D-050, Rounded M1/GaussFactor and 2026-10-19 Flat branch history. No global 3D sweep, no paper-Vth fitting, no 1T1C retention or physical refresh claim, no README/public baseline promotion.
- **Read next:** new 2026-10-20 progress → new `data/` index → exact CurveGrid CMD and all-bias CSV → old 2026-10-19 historical addendum only for provenance.


## 2026-10-19 — D-051 Flat upper S/D selected (STRUCTURAL SELECTION ONLY)

- **Adopted forward geometry:** Flat upper source/drain in 3D-Sun-SADDLE-V1; **lower saddle remains rounded**. Source: Sun et al. Figure 1(b,d) upper S/D profile versus Figure 2(e) saddle fillet, plus user decision D-051. This is figure-consistent reconstruction, not exact paper CAD or validated 3D electrical reproduction. See [D-051](docs/DECISIONS.md) and [Flat S/D progress addendum](docs/progress/3d_sun_saddle_v1_flat_sd_mesh_20261019.md).
- **Boundary:** Geometry choice accepted, but **Flat M1/M2A/M2D mesh and E/BTBT are NOT validated**; M2B/C/D are SDE-only and M2C/M2D are one effective mesh. All historical Rounded M1/GaussFactor evidence, existing 3D-Sun-B0 role under D-050, and frozen 2D PAPER-CAL C7_4 remain unchanged. No new TCAD run was performed to make this selection.
- **NEXT FIRST ACTION:** Isolated **MeshCase=0 SDE-only** run to reproduce M2D, then bounded cases 1–6 and CAD/Si-Ox curved saddle sliver diagnosis. Two genuinely distinct, adequately resolved meshes and matched-bias SDevice E/BTBT checks are required before quantitative adoption. No blanket electrical, thermal or retention run yet.

## 2026-10-19 — 3D-Sun-SADDLE-V1 Flat S/D M1→M2D SDE mesh QA (PAUSED / PROVISIONAL)

- **Current lineage and stage:** isolated Flat-upper-S/D variant of the separately provisional 3D-Sun-SADDLE-V1. Gate/Si saddle/oxide/contacts/doping unchanged through M2A–M2D (ARgate=6, DBCAT=36nm, Wfin=17nm, Hsaddle=48nm, JunctionRatio0.4, RfilletFactor1, GaussFactor0). This is **mesh-diagnostic work**, not an accepted geometry, mesh, GIDL field solution, paper fit or retention validation.
- **Actually executed:** Flat M1 DC checked; M2A LOWVD native PLT (Vth0.811597935648V, SS76.177117944mV/dec) checked; M2B, M2C and M2D SDE meshes generated and native tetra connectivity QC'd. <0.1nm edges: M2A 937 → M2B 422 → M2C 372 → M2D **372**. Worst min edge M2A 0.000835nm; M2B–D 0.014381nm. **M2C and M2D effective meshes identical** (vertex coords/connectivity), although binary TDR hashes differ. No SDevice was run for M2B/C/D; **no overnight MeshCase job was started**.
- **What remains blocked:** extreme Saddle curved Si/Ox sub-0.1nm edges still cluster around z≈−73nm, including Gate-exterior x≈±56nm; M2C/M2D minimum tet angle 0.168928° and 278 non-Delaunay boundary faces in SnMesh. CAD Boolean sliver vs mesh imprint/refinement interaction NOT distinguished; no independent spatial E/BTBT convergence or acceptable Gate–Drain interface resolution established.
- **NEXT FIRST ACTION (tomorrow, user deferred tonight's run):** use separate SWB test project, run **MeshCase=0 SDE-only smoke check** from archived [7-case source](code/sde/3d_sun_saddle_v1/flat_sd_mesh_20261019/SDE_FLAT_SD_M2D_MESHCASE_0to6_SWB.cmd). Verify 0 reproduces M2D mesh. Then run remaining cases 1–6 **SDE ONLY** if appropriate; upload per-case TDR/boundary/log/preprocessed SDE CMD with exact node↔MeshCase mapping; evaluate min/short edges, quality, CAD, contacts, doping and local Gate–Drain resolution. In parallel/if needed inspect curved Saddle Boolean imprint. Cases 2/3/6 are intentionally coarse controls and NOT SDevice candidates.
- **Do not run yet:** LOWVD/HIGHVD electrical batch, 300/340/380K or retention batch, until physically resolved two-mesh QC and selected-point DC/field/BTBT independence test. SDE mesh improvements alone do not establish spatial accuracy. A <0.1nm edge threshold is a **diagnostic counter, not universal failure criterion**.
- **Archive committed:** [new scientific progress](docs/progress/3d_sun_saddle_v1_flat_sd_mesh_20261019.md) and [curated numerical evidence/sha256 index](data/3d_sun_flat_sd_mesh_20261019/README.md), exact Git blob-matched Flat M1/M2A/M2B/M2C/M2D CMDs and unexecuted seven-case deck. Large native TDR and PLT evidence not republished; SHA256 identifiers preserved. FROZEN `B0-2D-PAPER-CAL` C7_4 and older 3D rounded/Nonlocal/GaussFactor findings unchanged; no README/RUN_SHEET/PROJECT_TIMELINE/DECISIONS update.
- **Read next:** this new progress page → data index → exact M2D and 7-case CMD → earlier [2026-10-18 GaussFactor checkpoint](docs/progress/3d_sun_saddle_v1_gaussfactor_20261018.md) only when numerical lineage context needed. Manual T-2022.03 only if a genuinely new SDE/SMesh syntax/option/solver behavior is proposed; use manual index first.

## 2026-10-18 — 3D-Sun-SADDLE-V1 GaussFactor SDE + three-bias DC checkpoint (PROVISIONAL)

- **User-executed source audit:** five GaussFactor values (0/0.2/0.5/1/1.5) at unchanged nominal M1 geometry, 300K, Hurkx. Five SDE meshes have identical intended boundary geometry, but the **0.000835 nm minimum-edge defect persists**. Three Id–Vg bias sweeps per factor (LOWVD Vd0.05 Vg0→1.5; HIGHVD POS Vd1.2 Vg0→2; HIGHVD NEG Vd1.2 Vg0→−1) delivered **12/15 full endpoints, 3 MinStep/Newton gate-ramp failures** (NEG GF0.2 at −0.35275V; POS GF1.5 at +0.24403V; NEG GF1.5 at −0.36572V). Actual native PLT points 1550.
- **Within-lineage result:** GF0 recreates nominal M1 high-Vd Vth0.786046V, SS77.079mV/dec, DIBL22.814mV/V, illustrative Ion/Ioff1.6725e8; GF0.5/1.0 complete comparable pilots with very small DC differences. **No Gaussian factor adopted/frozen**; GF0 is reference. Failed factors are not assigned fabricated OFF or high-Vd data. Several high-Vd runs fell back to 1 thread due to `sparallel` checkout failure; GF1.5 failed on 8 threads too, so license slowness and numerical failure are separate.
- **Next FIRST action for this 3D branch:** inspect selected existing high-Vd negative-gate **3D TDR** on common center/sidewall sections for spatial `ElectricField` and `Band2BandGeneration`; immediately examine gate/saddle/oxide topology and pathological sliver, then compare an independently repaired mesh at matched bias with regional BTBT integration, electron/hole terminal currents/KCL and optional Hurkx ON/OFF control. **Only after spatial/mesh validation and width/extraction matching** should paper Vth(0.656V)/Ion/Ioff(3.4e10) reproduction/fitting or DBCAT/MEB DOE be reconsidered.
- Evidence: [new progress record](docs/progress/3d_sun_saddle_v1_gaussfactor_20261018.md) and [data index](data/3d_sun_saddle_gaussfactor_20261018/README.md). Source original and derived ZIP hashes in `SOURCE_MANIFEST.csv`; no full TDR on GitHub. **FROZEN 2D C7_4, historical models and public root README untouched**. This new section supersedes the earlier 3D M1 *immediate next action* while retaining its provisional model/mesh limitations.

## 2026-10-17 — Parallel 3D-Sun-SADDLE-V1 M1 nominal DC six-sweep checkpoint (PROVISIONAL)

- **Separate 3D lineage; no existing freezes replaced.** User-executed 300 K explicit lower-Si-saddle M1 reconstruction at ARgate6, DBCAT36nm, JunctionRatio0.4, Wfin17nm, RfilletFactor1.0. D0 (Vd0.05 IdVg), D1 (Vd1.2 positive IdVg), D2 (Vd1.2 negative IdVg), and three D3 (Vg0.1/0.6/1.2, Vd0→2) **all 6/6 numerically complete** and source-current QC reviewed. Six n1 TDR meshes are byte-identical. See [3D-Sun-SADDLE-V1 M1 validation page](docs/validation/3d_sun_saddle_v1_20261017/README.md) and [progress checkpoint](docs/progress/3d_sun_saddle_v1_m1_nominal_dc_20261017.md).
- **Key provisional findings:** at high Vd Vth0.7860V vs paper0.656; SS77.08 vs76 mV/dec; DIBL22.81 vs23.6 mV/V under CMP-specific extraction; illustrative Ion/Ioff1.67e8 vs paper3.4e10 (not definition matched). At Vd2, D3 drain currents [8.32e-14,7.13e-10,3.93e-6] A for Vg0.1/0.6/1.2. Lower-gate IdVd markedly mismatches published Table1 trend; Vg0.1 Id is largely balanced by substrate, not source.
- **Do not freeze:** M1 numerical success is NOT spatial or DC mesh convergence. M1 has minimum edge 0.000835nm and worst R/H3.23e8; electrical effective width, published extraction biases and low-gate discrepancy remain unresolved. D1-D3 mutual current overlap QC supports only within-lineage numerical consistency. No MEB 5-variable split, absolute GIDL mechanism or retention improvement claimed.
- **3D NEXT FIRST ACTION:** validate physical gate/saddle interface topology and repair pathological sliver; independent representative M1↔repaired-grid DC/field test, resolve channel-width and published curve extraction, THEN decide if geometry DOE is justified. **Existing 2D L1 23/24 status and frozen C7_4 remain unchanged.** Do not update public README yet.

## 2026-10-16 — L1 paper-figure model comparison: 23/24 curves QC; 2D→3D bridge PROPOSED (not adopted)

- **Last updated 2026-10-16. Current stage: PROVISIONAL / no new freeze.** User-executed 300-K PAPER-CAL-derived L1 Table-1 figure replication: NonlocalPath 12/12 IDVG+IDVD conditions (3,612 PLT points); Hurkx 11/12 (3,011 points); **Hurkx MEB24nm IDVG failed Newton/MinStep near gate +0.0395 V after negative-gate sweep**. Full source archives were collected, hashes/conditions and 23 completed curves QC-reviewed; original full source ZIPs remain conversation artifacts, not in GitHub. Checkpoint CSV and exact source SHA: [progress evidence](docs/progress/dbcat_paper_compare_l1_hurkx_nonlocal_20261016.md), [numeric checkpoint data](data/dbcat_figure_2d_20261016/README.md).
- **Main finding:** both 2D BTBT model choices nearly coincide in channel-on current; substantial MEB sensitivity differences occur in low-current/off regions and several paper D_BCAT trends are not reproduced. Paper 3-way overlay plots from synthetic hand-picked anchors were illustrative, **not systematic quantitative digitization**, and have NOT been accepted as literature measurements. No baseline selection/model winner or effective MEB range.
- **Decision boundary:** existing frozen `B0-2D-PAPER-CAL C7_4/B_QF_HALF` remains unchanged, as do earlier Q0/Run Sheet/3D results. Do **not** silently label L1 as converged or paper-validated, or equate terminal leakage to BTBT/Retention.
- **NEXT FIRST ACTION (user confirmation needed for direction):** evaluate **faster 2D screening + already existing 3D-Sun-B0 selected-point bridge** rather than attempting exact paper-3D absolute transfer/output fit with 2D; inventory existing 3D parent F1/current decks and 36nm high-Vd state, benchmark runtime and apples-to-apples width normalization/model/bias, then selected 24/48 nm sensitivity or candidate/boundary points. This is a research path PROPOSAL, not an executed 3D extension or an adopted freeze.
- **Do not reopen:** calibrated knobs (GCS2.3/GDB25nm/Qf2.55e12), earlier historical findings, README/public claims, 1T1C physical-retention claims. **Read next:** checkpoint doc; `data/baseline_3d_sun_b0/README.md`; `docs/MODEL_SCOPE.md`; `docs/RUN_SHEET.md`; original Sun 2022 only for benchmark ambiguity.


> Canonical session handoff. Read after `AGENTS.md`. Current research authority: live GitHub main + linked underlying evidence.

**Last updated:** 2026-10-16  
**Session state:** **PAPER-CAL-derived L1 figure-QC 23/24 complete / research direction review PROVISIONAL**; L1/L2 duplicate effective mesh confirmed from 36/51-nm OFF source; dual-mesh (L1 vs Rough R1) 15-MEB × 2-VD × 2-mesh DC SWB dispatched by user, all 60 DC numerical results/QC still PENDING. Frozen C7_4 and prior Q0 close-out unchanged.

## 2026-10-14 latest checkpoint — L1/L2 duplicate effective mesh; L1 vs Rough R1 dual-mesh DC dispatched (PROVISIONAL)

- **Latest detailed status / first read:** [NonlocalPath dual-mesh DC dispatch and mesh-identity checkpoint](docs/progress/nonlocalpath_mesh_dc_dispatch_20261014.md); [source-verified 36/51-nm OFF QC CSV](data/nonlocalpath_pilot_20261013/off_l1_l2_mesh_equivalence_qc_20261014.csv). This section **supersedes the previous NonlocalPath pilot's immediate task ordering**, without changing the older historical evidence.
- **Source-QC COMPLETE, not mesh-converged:** user archive `CMP_NONLOCAL_OFF_L1_L2_EVIDENCE.zip` (76/76 manifest source entries; 36/51 nm × L1/L2 OFF 4/4 completed). Within each depth the L1 vs L2 SDE intended refinement differs but **actual TDR vertex coordinates, connectivity and numerical datasets match exactly**; PLTs and OFF currents match. L1/L2 are **one effective mesh state**, NOT two mesh-convergence points. 36nm OFF=1.242002286e-12 A/um, 51nm OFF=2.298969895e-16 A/um. Old L0 OFF differs materially; deck lineage needs checking.
- **New independent mesh candidate (screenshot / not physically validated):** Rough R1 at 36nm **12,857 SVisual elements / 6,176 points**, versus L1 **24,327 / 11,835**. Local windows include previously observed electron/hole peaks, but full ON−OFF/BTBT-integral convergence and R1 device performance are still pending. L1 36nm ON log completed; screenshot-only max should not be called a validated integral.
- **User-reported SWB dispatch:** actual projects `MEB_nonlocal_1_DC` and `MEB_nonlocal_1_DC_Copy` show **15 MEB depths × VD_Target 0.05/1.2 V each** = **30 SDevice conditions per project, 60 total**. Intended comparison is L1 vs Rough R1, but *project↔mesh mapping requires actual PP-SDE/TDR confirmation*. All new DC numerical outcomes/60-job completion **NOT YET VERIFIED**. DC deck: 300K, VG0→2 V, BTBT OFF, fixed PAPER-CAL geometry/calibration/positive Qf/WF. No current evidence that model swap fixes MEB DC sensitivity.
- **NEXT FIRST ACTION:** after user's DC outputs arrive, collect and source-QC both project trees with the prepared `collect_cmp_dualmesh_dc.py`, identify true mesh from PP source/TDR, validate 60 endpoints/current curves, extract identical Vth (Icrit=5e-6 A/um), SS, DIBL and Ion/Ioff definitions, compare L1/R1 across 15 MEB and against paper 36/48 trends. **Separately** finish 36/48/51 NonlocalPath ON−OFF carrier-resolved integrated BTBT and mesh-dependence plus Hurkx matched-parent controls before a baseline decision.
- **Preserve:** C7_4 frozen baseline, calibration, original Atlas/Q0, README and DECISIONS; no NonlocalPath promotion, no 3D-equivalence, no retention/optimum claim. This record documents work in progress, not a validated result set.
## 2026-10-14 NonlocalPath pilot (newest session checkpoint, PROVISIONAL)

- **Current stopping classification: IN PROGRESS / PROVISIONAL; no re-freeze.** [Pilot progress & staged model-validation gates](docs/progress/nonlocalpath_hotspot_pilot_checkpoint_20261014.md), [numerical/QC tables](data/nonlocalpath_pilot_20261013/README.md). User plans NonlocalPath hotspot screening → new mesh validation → controlled 15-MEB Hurkx/NonlocalPath GIDL/BTBT → independent DC sensitivity gate → conditional future baseline adoption (NOT an adopted model/parameter change).
- `MEB_nonlocal_off`: six MEB = **31/36/39/41/46/51 nm** (46, not 48); 300K, Vd=1.2,Vg=-0.7, current L2; 6/6 SDevice endpoints and OFF terminal PLT source-QC PASS; original ZIP SHA256 `086d50fadc4a271728030b42000aac62015ea77562c3bc1fbcecc3b1f6fe1e92`. OFF differs from historical Hurkx Atlas OFF by **2.39–3.80x**, so clean physics-model comparison is **NOT** established.
- `MEB_nonlocal`: ON SVisual `Band2BandGeneration` **screenshot-only** at 36nm peak `6.32186e18` at (X,Y)=`(0.0369141,0.252174) um`, 39nm peak `2.01641e18` at `(0.0398437,0.252174) um`. GateTop-adjacent; no carrier-resolved maps/integrals or source-QC of ON TDR/PP-CMD/PLT. No mesh convergence/optimum/model preference.
- **NEXT FIRST ACTION:** collect/verify remaining ON actual PP-CMD/log/terminal PLT/final TDR, 36/39 carrier-specific BTBT and all-region/local-surface hotspots, and complete representative depth screening (including missing **48 nm** boundary); then plan/common-source mesh convergence and run controlled Hurkx↔NonlocalPath comparisons. DC extraction was previously BTBT-OFF, so swapping the BTBT model does NOT itself solve the SS/Vth MEB-sensitivity issue. Frozen PAPER-CAL GCS2.3/GDB25nm/Qf2.55e12, older evidence, Q0 obligations and outstanding temperature DC follow-through remain intact.
- No README update; no `DECISIONS.md` model decision; no 1T1C retention claim. This new section supersedes prior immediate task ordering for **this user-selected Nonlocal pilot** but does not close older Q0/SDE ROI evidence gates.

## 2026-10-12 BTBT 공간/메시 관찰 기록 (non-decision checkpoint)

- New evidence-only checkpoint: [docs/evidence/btbt_roi_hotspot_mesh_checkpoint_20261012.md](docs/evidence/btbt_roi_hotspot_mesh_checkpoint_20261012.md). Q0 Surface-L1 300 K 31/36/41/48 nm TDR signed ROI fractions, PAPER-CAL Atlas 300 K whole-Si 15 MEB reference, 340 K screen-only hotspots, observed SDE mesh coverage, pending 300 K PAPER-CAL region split are now indexed. CSVs / redrawable SVGs under `data/btbt_roi_20261012/` and `assets/images/paper_cal/btbt_roi_20261012/`.
- Q0 TDR-based Surface signed shares at 31/36/41/48 nm = 10.545/10.872/17.712/57.926%; original whole-Si SVisual integration cross-check |error| < 0.0003%. Specific to existing Q0 Surface-L1 mesh; no model/mesh convergence claim.
- PAPER-CAL 300 K 36/39/41 nm whole-Si archived values = 1.151025e6 / 1.682352e6 / 1.551265e6. **PAPER-CAL same-temperature Surface/Gate ROI split not yet obtained.**
- Next: receive and audit prepared independent 300 K Atlas L2 36/39/41 nm TDRs and ROI CSV; measure Surface-side local hotspot; only then design/check separate common Surface refinement across MEB. No README/freeze/model-decision or retention claim changes.

## 0. 2026-10-11 Faithful-Q0 source-based execution close-out — authoritative new checkpoint

> **Completion status:** User-executed 300K Faithful-Q0 ×15 and surface-hotspot-refined Faithful-Q0 ×15 ON/OFF/spatial **DATA + SOURCE QC COMPLETE**; numerical mesh convergence, 2D model selection and GIDL/retention mechanism **NOT DEMONSTRATED**. This update supersedes the previous planned-Q0-run handoff. No new TCAD was run *during the archival close-out*.

**Lineage and controlled comparison**
- `B0-2D-PAPER-CAL = C7_4/B_QF_HALF` stays **FROZEN**: DC-calibrated reduced-order 2D surrogate (GCS2.3, GDB25nm, Qf2.55e12cm^-2). Literature DC benchmark agreement alone cannot establish predictive GIDL/BTBT validity or real fabricated oxide/recess/Qf.
- `B0-2D-FAITHFUL-Q0` remains a **CONDITIONAL** paper-dimension 2D control (GCS1, GDB0, modeled Tox5nm/recess120nm, Qf=0 assumption). Both Q0 and PAPER-CAL use **Hurkx**; no single-variable calibration causality has been isolated.
- Existing `3D-Sun-B0` is literature-consistent but itself DC-mismatched, hence a **proposed 3D mechanism cross-check**, not ground-truth paper calibration.

**Original Q0 15-depth 300K audit:** user original ZIP `CMP_FAITHFUL_Q0_ALL15_4PROJECTS_EVIDENCE.zip` 1,513/1,513 source hash+length PASS; 60/60 SDevice done; 15 ON terminal, 15 OFF terminal, 15 ON spatial, **14/15 Cgd** (31nm SVisual extract absent). MEB↑→both total drain current and original Q0 Cgd↓, also observed for PAPER-CAL, but **BTBT spatial generation and Hurkx-sensitive fraction diverge**. PAPER-CAL BTBT integral peaks39nm and BTBTmax41nm with GateTop-tracking hotspot; Q0 BTBT integral decreases with MEB, near-surface hotspot ~X2.34nm for 33–51nm. Do not call total drain current “pure BTBT.”

**Q0 Phase1 surface hotspot experiment (actually executed):** user ZIP `CMP_Q0_PHASE1_SPLIT6_15MEB_EVIDENCE.zip`: 8+7 split SWB projects for GIDL ON/OFF/spatial, 45/45 SDevice done; 1,197/1,197 original source hashes PASS. Same Q0 geometry/physics/300K (`Vd1.2,Vg-0.7`), same GateTop-following GIDL Core; only new local SDE mesh windows around near-surface hotspot (Outer X0–15nm/Y258–276nm; Core X0–8nm/Y263–270nm) `SurfaceRefineLevel=1`.
- Q0 before→after: 36nm total Id **+47.66%**, whole-Si BTBT integral **−17.68%**; 48nm **+37.79%/−75.81%**, 51nm **+36.01%/−83.47%**. At 31nm global BTBT Xhot switches **29.30→2.34nm**. All 15 retain decreasing *total Id* MEB ranking, while spatial generation remains strongly **mesh-sensitive**.
- 36nm Q0 Surface-L1 total drain Id ≈1.4652936e-9 A/um vs PAPER-CAL Atlas ≈1.0885586e-12; Hurkx ON−OFF fraction ≈0.000069% vs 16.94%. In Q0 Surface-L1 the log-reported drain *electron* ON−OFF tracks `q∫BTBT` within ~1.6% across 15 MEB at displayed precision; drain *hole* current dominates total. Microscopic OFF-hole source, full terminal collection and very small ON−OFF numerical precision **NOT RESOLVED**. Selected Level1 spatial TDR/PLT exist at 31/36/41/48nm. **No Surface-L1 Cgd/DC re-sweep**.
- Two meshes (L2 original and added Surface-L1) demonstrate **sensitivity**, NOT convergence or physical truth. PAPER-CAL historical FZ-C→Atlas L2 numerical mismatch remains a separate outstanding risk.

**Data preservation complete on live GitHub main:**
- `data/faithful_q0/20261011_300k/README.md` gives three 15-depth CSV datasets, exact SDE edit, source-QC reports.
- `PUBLIC_ARCHIVES_MANIFEST.json` + `restore_public_archives.py` reconstruct and SHA256-verify **three public source archives**, stored as 8+14+2 Git binary chunks: original Q0 (source CMD/log/CSV); surface-L1 (CMD/log/CSV and selected TDR/PLT); graphs, full QC tables/collector scripts/plots. Server paths anonymized and job/out/sta intermediates excluded; **original user-uploaded ZIP hashes remain separately recorded**, not overwritten.
- `docs/research/faithful_q0_model_selection_gate_20261011.md` records academic self-audit and **PROPOSED** model-selection strategy. Relevant archive commits `f2c4f515`, `61b64a33`, `557f13f4`.

**Stopping classification:** **PAUSED / PROVISIONAL model-selection stage** after successful source-evidence archival; no PAPER-CAL recalibration, Q0 replacement-baseline adoption, proven retention improvement or final optimum.

**NEXT FIRST ACTION (bounded validation; planning, not yet executed):**
1. At **36 and 48nm first**, inspect source TDR/hotspot grid, actual electrode electron/hole currents, ON−OFF subtraction precision, q∫BTBT/AreaFactor; if required run Q0 SurfaceRefineLevel1→2 for selected points. Add 31nm if hotspot switch remains consequential. Avoid automatic full 15-depth rerun; target PAPER-CAL Atlas mesh comparability separately.
2. At **36nm**, isolate GCS/GDB/Qf effect on spatial BTBT and ON/OFF with controlled comparisons (full 2³ only if interactions matter), **without** retroactive changes to frozen baseline.
3. **PROPOSED:** move selected **3D-Sun-B0 36/48nm** physical-mechanism comparison ahead of further broad 1T1C/temperature studies, then decide which 2D surrogate's relative MEB ranking is defensible. The current 3D anchor is not exact paper-calibrated truth.
4. Concurrently collect/QC pending **14 new-T Atlas DC depths** when source files become available. No new all-MEB/temperature mass execution as default.

**Claim guardrail:** Good DC benchmark fitting != experimentally verified GIDL physics. Paper dimensions != measured process details. Q0 validates shared relative Cgd and total Id directions only conditionally; the spatial BTBT and Hurkx-sensitive mechanism, 3D equivalence, retention translation and 48nm optimum remain unproven.

---

## 1. Current research objective and lineage

**20 nm급 BCAT DRAM에서 MEB 깊이에 따른 GIDL–Retention 전달 특성 및 온도 의존적 유효 설계 범위 도출**

Current causal-evidence sequence to test (not assume):

```text
MEB depth → project-internal Cgd / electrostatic redistribution
→ drain-side E + spatial BTBT → total drain leakage at GIDL bias
→ ON/OFF Hurkx sensitivity → temperature
→ PAPER-CAL 1T1C Write/Hold/Read → retention translation
→ effective MEB range
```

- **Physical baseline still frozen:** `B0-2D-PAPER-CAL = C7_4 / B_QF_HALF`.
- Frozen calibration inputs: `GateCouplingScale=2.300`, `GateDepthBoost=25 nm`, `Qf_Int=2.55e12 cm^-2`, `WF=4.8 eV`, nominal 36 nm, reference 300 K.
- **New numerical branch:** post-freeze 2D MEB atlas, **MeshLevel 2 working production**; MeshLevel 3 convergence reference. No physics retuning.
- **2026-10-08 G0 update:** exact FZ-C SWB parent CMD, logs/CSV and original n14 TDR were recovered; nominal 36-nm static physical/solver association and TDR spatial comparisons were completed. FZ-C↔Atlas numerical interchangeability was NOT demonstrated (+86.86% Atlas total drain current, -64.64% Atlas integrated BTBT). User explicitly chose to continue the post-freeze Atlas L2 as a **separately labeled within-branch research model**, without FZ-C equality/recalibration claims. Read docs/evidence/paper_cal_g0_parent_spatial_bridge_20261008.md.
- Do not mix this branch's absolute currents with `B0-2D-Legacy / NonlocalPath`, old FZ-C, or `3D-Sun-B0` without an explicit bridge.

## 2. Current completed work (2026-10-08, updated 2026-10-09)

Full **15-point 300 K MEB Atlas** completed from user's TCAD runs:

```text
MEB = 31 / 33 / 36 / 39 /
      41 / 42 / 43 / 44 / 45 /
      46 / 47 / 48 / 49 / 50 / 51 nm
```

- DC @ `Vd=0.05`, DC @ `Vd=1.20`, Cgd AC @ `Vd=1.2,Vg=-0.7,1 MHz, BTBT OFF`, GIDL-ON @ `Vd=1.2,Vg=-0.7,Hurkx`.
- P2 spatial post-processing completed: `BTBTmax`, `E@BTBT`, hotspot, `∫BTBT`, 20%-active Si area, common fixed-cut `Y=0.252174 um` E/BTBT profiles and 20% width.
- Additional diagnostic: BTBT-OFF controlled 15 points, plus signed terminal ON/OFF re-extractions and KCL checks.
- `DC005` SVisual extractor originally misconfigured; corrected and confirmed `BiasReached=1, Vd=0.05`.
- `Cgd` SVisual path corrected for actual `Cgd_AC_n*_ac_des.plt` output.
- P2 SVisual cutline/Tcl bugs corrected in v3 and 15-point results returned.

**2026-10-09 update:** new-temperature 15-MEB GIDL ON/OFF/spatial 45×3 output branches and AC Cgd 44/45 extracted and independently reviewed; 41nm/340K Cgd is missing because the device did not converge. For nominal 36nm, DC005+DC12 at 233, 340, 380 K are newly source-curve QC-validated (six summary + six 6107-point Id-Vg curves, pp deck, SWB graph, bounded device-end log). Together with already validated 300 K this closes the **36nm × four-temperature electrical and spatial baseline**, not the full 15-depth DC thermal matrix. Source ZIP and full curve archive exist in local chat deliverable; six original DC summary CSV and 4-row integrated 36nm master are committed. Read `docs/progress/paper_cal_36nm_temperature_dc_qc_20261009.md` and `data/paper_cal/atlas_temperature_20261009/README.md`.

**Raw data ingestion/independent audit:**

- 201 archived entries: **90 summary CSV + 105 curve CSV + collector QC/manifest/metadata**.
- **1,036 independent checks passed** for coverage, checksum, endpoint, bias, KCL, AC reciprocity, ON/OFF versus spatial integral, and computed master consistency.
- Public GitHub archive has only TCAD absolute-path metadata sanitized; all 195 numerical CSV byte sequences preserved.
- GitHub evidence commit: `b40c63299917419e789ac41f2f87c637ff3ebcdb` (2026-10-08).

Evidence paths:

- `data/paper_cal/atlas_300k_20261008/CMP_MEB_ATLAS_300K_EVIDENCE_PUBLIC.zip`
- `data/paper_cal/atlas_300k_20261008/processed/MEB_300K_ATLAS_MASTER_VALIDATED.csv`
- `data/paper_cal/atlas_300k_20261008/qc/`
- `docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md`
- `assets/images/paper_cal/atlas_300k/01..10.svg`
- `code/scripts/analysis/validate_paper_cal_meb_atlas_300k.py`

## 3. Results established *within this numerical branch*

At 300 K and GIDL bias `Vd=1.2,Vg=-0.7`:

- Terminal **total drain leakage**, not pure BTBT current, decreases monotonically from 31→51 nm by **1,135.0×** (36→51 by **19.5×**).
- Project-internal `|c(g,d)|` decreases **35.91%** (31→51); it is **not** calibrated production overlap `Cov` nor a proof of direct `Cgd→local-E→GIDL` causality.
- DC: `Id@Vg1.2,Vd1.2` decreases **1.30%** and `Id@Vg2,Vd1.2` decreases **6.46%** (31→51); DIBL increases **0.459 mV/V**, `SSquick@Vd1.2` increases **0.069 mV/dec**.
- BTBT integral and `E@BTBT` peak at **39 nm**, `BTBTmax` at **41 nm**, while total drain leakage continues decreasing.
- Signed `Id(ON)-Id(OFF)` matches `q∫G_BTBT,dA` within **0.62% max** (31 nm; near-cancellation) and within approximately **0.01%** for 36–51 nm.
- Hurkx-sensitive percentage: **31 nm 0.105%; 36 nm 16.94%; 39 nm 74.10%; 41 nm 91.19%; 48 nm 99.57%; 51 nm 99.81%**. It is a controlled ON/OFF sensitivity, not a separately proven microscopic contribution under arbitrary conditions.
- Shallow total leakage is predominantly **BTBT-OFF residual drain–substrate current**; residual microscopic mechanism remains **unresolved**. Do not call all GIDL-condition terminal current BTBT current.
- Common fixed cut under-samples shallow hotspots (31/33/36 nm); use whole-Si BTBT area/integral for comparisons across the full 15 points.
- `GateTop≈Jdepth=48 nm` is a **model structural boundary**; there is no sharp electrical plateau/knee at 48 from this atlas. The 51-nm endpoint is **not** a final optimum.
- New temperatures have independently QC-reviewed 45/45 terminal GIDL ON/OFF and spatial extracts, 44/45 Cgd extracts and, at 36nm only, validated six additional DC extractions from original curves. **No** PAPER-CAL 1T1C retention validation yet. Numerical/thermal mesh convergence NOT established.

## 4. Concurrent original Atlas DC source collection — 2026-10-11

**Concurrent Atlas DC stage:** 36nm four-temperature Atlas DATA-COMPLETE / independent source-extraction QC PASS, while the **other 14 MEB depths at new temperatures remain DC IN-PROGRESS / not ingested**. New 45 GIDL ON/OFF/spatial branches and 44 of 45 AC Cgd branches have been previously independently QC-reviewed. Do NOT treat this as full 60-condition DC completed.

**Concurrent Atlas DC follow-through:** let ongoing DC005/DC12 runs for remaining 14 MEB depths finish; collect completed original CSV+Id–Vg curves, actual pp*_des.cmd, SWB gtree, and node logs in batches. QC each row and append to the existing 60-row PARTIAL table. Do not start a blanket new run or re-calibration. **The new primary research validation gate is in §0; it does not cancel pending DC source collection.**

- Source of 36nm validated four-temperature table: `data/paper_cal/atlas_temperature_20261009/processed/MEB36_4TEMP_INTEGRATED_VALIDATED_DC.csv` (59 fields, 4 rows), six raw DC summaries in `raw_dc36/`. Original user ZIP SHA256 `e680122bcfca924bf60f7320efd39f685e2289bc8b89f963938ccdd5319b8262`. Full ZIP / six Id–Vg raw curves / 60-row partial dataset / workbook / plots and reproducible script are in local downloadable `CMP_DC36_COMPLETE_RESEARCH_BUNDLE_20261009.zip`, NOT fully Git-committed.
- 36nm 233→380K: Vth@Vd1.2 falls 131.635mV; SSquick@Vd1.2 rises 40.228mV/dec; DIBL 22.813→26.786mV/V; Ion@Vg1.2 falls 4.093%; Ion/Ioff 2.5597e12→1.6586e7; **DC** Ioff@Vg0 rises ~148,009×. Total **GIDL-bias** Id_ON rises ~24,627.5×; raw AC |Cgd| falls 11.378%. These are distinct bias currents.
- Known QC watchlist: 36nm/380K ON−OFF vs q∫BTBT mismatch −4.39076%; five higher-temperature/shallow MEB cases are previously flagged in GIDL/Cgd analysis. The 41nm/340K AC is missing due to SDevice Newton failure; it must not be interpolated as measured.
- SWB parameters: SDE `MEBDepth` [0.031,0.033,0.036,0.039,0.041,0.042,0.043,0.044,0.045,0.046,0.047,0.048,0.049,0.050,0.051] um; SDevice `Temp_K=233,340,380` K; existing 300 K reused. Atlas MeshLevel=2; frozen Qf/WF/geometry adjustments unchanged.
- When other new-T MEB DC data are returned, independently check node↔temperature↔MEB, curve endpoint, constant-current Vth (Icrit=5e-6 A/um), SS1/2/quick, Ion/Ioff, DIBL from Vth005/12, then combine with existing GIDL/Cgd/spatial data without filling absent values. Narrow follow-up reruns only if a warning materially affects scientific conclusions.
- Remain within Atlas L2 branch. Avoid presenting frozen FZ-C↔Atlas equivalence, mesh convergence, physical retention/refresh or final effective optimum as proven. A+B 1T1C roadmap remains provisional.

**Read next:** `docs/progress/paper_cal_36nm_temperature_dc_qc_20261009.md` → `data/paper_cal/atlas_temperature_20261009/README.md` → `docs/progress/paper_cal_temperature_atlas_15x4_dispatch_20261009.md`.

## 5. Do not reopen by default

- C6/C7 physical calibration DOE or C8 fitting;
- model retuning to make old and new GIDL match;
- Hurkx→NonlocalPath replacement without a bridge;
- MeshLevel 4 or global over-refinement;
- historical FZ-C freeze rewritten as if newer mesh had been used then;
- Legacy absolute-value/1T1C relabeling;
- 3D production equivalence, physical retention/refresh or DWFG claims without execution;
- `48 nm = final optimum`.

## 6. Read next

1. `AGENTS.md` then this file; read **§0 for completed Q0 original + Surface-L1 data/QC archive, model uncertainty and next selective checks**. Source manifest/restore: `data/faithful_q0/20261011_300k/README.md`; proposed decision gate: `docs/research/faithful_q0_model_selection_gate_20261011.md`.
2. **Concurrent Atlas DC follow-through:** `docs/progress/paper_cal_36nm_temperature_dc_qc_20261009.md` and `data/paper_cal/atlas_temperature_20261009/README.md`. Then temperature dispatch and, only if relevant, G0 bridge.
3. `docs/progress/b0_2d_paper_cal_meb_atlas_300k_20261008.md` and validated CSV plus source ZIP/QC.
4. Existing authoritative numerical-lineage concerns:
   - `docs/progress/b0_2d_paper_cal_mesh_revalidation_20261007.md`
   - `docs/research/b0_2d_production_revalidation_plan.md`
   - `docs/research/b0_2d_final_freeze_plan.md`
5. `docs/MODEL_SCOPE.md`, `docs/research/CLAIM_EVIDENCE_MATRIX.md` before upgrading claims.
6. Consult manual routing index and official T-2022.03 section **only** for a triggered syntax/solver/physics question.

**Session close-out (2026-10-09):** 36nm four-temperature DC/GIDL/Cgd/spatial BASELINE DATA-COMPLETE / DC source QC PASS; the all-MEB DC thermal validation is IN PROGRESS. First next action: collect remaining-depth DC source curves / logs as SWB jobs finish and incrementally QC/extend the 60-row partial Atlas. No FZ-C recalibration or wholesale reruns.

**Session close-out (2026-10-11):** Q0 original + surface-hotspot Level1 (15 MEB) source evidence, QC, SDE and reproducible public GitHub archival **COMMITTED**. Model-selection, mesh convergence, electron/hole leakage origin and retention validation **OPEN**. Next first action is the bounded numerical + calibration/3D selection gate in §0. Frozen PAPER-CAL and historical runs unchanged.
