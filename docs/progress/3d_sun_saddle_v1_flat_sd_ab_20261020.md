# 3D-Sun-SADDLE-V1 · Flat-S/D two-grid DC / E-field / BTBT verification (2026-10-20)

**CMP-EXECUTED (numeric evidence), PROVISIONAL (physics and absolute GIDL claim).** Current selected-point MEB=DBCAT36nm, T=300K, Hurkx. This is a separate 3D reconstructed geometry, **not** the frozen B0-2D-PAPER-CAL or historical 3D-Sun-B0; D-050 3D selected-point strategy remains applicable.

## 1. Reconstructed geometry and executed diagnostic history

- D-051 selected **flat upper Source/Drain**, lower Silicon saddle still rounded. ARgate6 gives nominal Recess120nm; Wfin17nm; Hsaddle48nm; Si crest -72nm; Tox5nm; W bottom -115nm and oxide outer trench floor -120nm. The saddle base -122nm deliberately overlaps Si substrate by 2nm for Boolean connectivity. The exact Fin base CAD placement remains **CMP-reconstructed**, not paper-explicit.
- **MeshCase 0..6 (SDE n19/n33..n38):** M2D Case0 reproduced, Cases0/4/5 effective mesh duplicate; Outer/Gate placement switches reduce some short edges but not the local z≈-73nm defect; intentionally coarse Case6 not acceptable for device calculations.
- **LocalCase 1,2 (n32,n40):** Source-only / Drain-only OuterCrest disabled; 372 to 348 sub-0.1nm edges each, but 308 edges at depth73.0–73.5nm unchanged.
- **CadSeamCase 0..3 (n39,n42,n43,n44):** same-material Silicon–Silicon and Oxide–Oxide internal seams tested separately and jointly. Case3 both unions reduces sub-0.1nm edges 372→132; non-Delaunay **boundary faces** 278→94. Physical material volumes, electrode areas and common-coordinate dopants matched; this does **not** imply exact paper CAD or absolute field proof.
- **CurveGrid A/B:** Both use CadSeamCase3, MeshCase0, identical geometry/doping/contacts. A=CurveGrid1 SDE n41, 62,396 vertices/352,400 tetra; B=CurveGrid2 SDE n46, 80,788 vertices/459,464 tetra. B has finer local gate window (nominal maximum 1.5/1.2/1.5nm versus A 2.2/1.8/2.2nm). Both have 0 non-Delaunay boundary faces in SnMesh, but short edges A114/B198 (<0.1nm), min edge 0.03659nm and poor minimum angles A0.428°/B0.856°. These are independent discretizations, **not** mesh-free physical truth.

## 2. Six native SDevice runs: matched conditions

Exact project↔mesh mapping: `B0_3D_low`, `B0_3D_highpos`, `B0_3D_highneg`, each SDevice **n47=A** reading `n41_msh.tdr` and **n48=B** reading `n46_msh.tdr`. All 6 runs reached target endpoint; original full native PLT preserved outside Git and extracted sampled raw PLT CSVs archived in [`device/`](../../data/3d_sun_flat_sd_ab_20261020/device/). Four-electrode KCL was checked. Fixed physics: 300K, workfunction4.8eV, Fermi, Silicon PhuMob+Lombardi+high-field and Hurkx; no retuning.

| Sweep | Bias | A final Id (A) | B final Id (A) | Original transfer points each |
|---|---|---:|---:|---:|
| LOWVD | Vd=0.05, Vg0→1.5 | 2.1902846e-6 | 2.1470543e-6 | 60 |
| HIGHPOS | Vd=1.2, Vg0→2 | 1.5744974e-5 | 1.5595101e-5 | 107 |
| HIGHNEG | Vd=1.2, Vg0→-1 | 9.1393007e-14 | 9.1415084e-14 | 205 |

Within-this-lineage extraction: Vth constant-current criterion **|Id|=8.5e-8A**, SS semilog range **1e-12 to 1e-9A**. At LOWVD, Vth A/B=0.8078731/0.8114484V (3.58mV shift), SS=75.8867/76.1950mV/dec. At HIGHPOS, Vth=0.7827093/0.7850354V (2.33mV), SS=76.9048/77.0662mV/dec, DIBL=21.8815/22.9678mV/V. This does **not** share the main 2D Run1 Vth definition. Total 3D terminal currents in A, NOT paper-normalized A/µm.

## 3. All-bias spatial E-field/BTBT A/B analysis (24 snapshots)

12 unique (sweep,Vg) conditions × two grids: LOWVD Vg0/0.6/1.2/1.5V, HIGHPOS 0/0.6/1.2/2.0V, HIGHNEG 0/-0.1/-0.5/-1.0V. HIGHPOS/HIGHNEG Vg0 is a bias-equivalent duplicate, not distinct extra physics. Full-Silicon `ElectricField` vector-norm maximum and positive-clipped nodal `Band2BandGeneration` tetra volume integration were computed. The latter yields **q∫max(G,0)dV**, a *generation-equivalent* current (A) and **not terminal drain GIDL current**. Full per-bias CSVs preserve volume-weighted percentiles, centroids and coordinates.

| Vd, Vg | q∫max(G,0)dV A / B (A) | Note |
|---|---|---|
| 1.2V, -1.0V | 8.3979e-14 / 8.4000e-14 | HIGHNEG, B-A ≈ +0.025%; max E≈3.860MV/cm |
| 1.2V, -0.5V | 4.354e-14 / 4.353e-14 | HIGHNEG, ≈-0.022% |
| 1.2V, 0V | 6.520e-15 / 6.517e-15 | HIGHNEG/HIGHPOS common start |
| 1.2V, +2.0V | 2.308e-17 / 2.225e-17 | positive-gate Source-boundary weighted generation |
| 0.05V, +1.5V | 1.174e-19 / 1.143e-19 | very small vs ON conduction, signed generation relevant |

- For HIGHNEG A, lowering Vg **0→-1V** increases positive BTBT equivalent current **6.5204e-15→8.3979e-14A = 12.88×**. Fraction in x=15..30nm Gate–Drain ROI rises **22.48%→74.23%**, x=45..60nm outer-Drain ROI decreases **77.52%→25.67%**. Positive-generation centroid x moves **+47.50→+28.43nm**. B reproduces these fractions nearly identically. At Vg=-1, peak generation node is x=+15nm, y=-7.5nm, z=-25.3125nm, whereas global |E| peak remains x=+60nm near Drain **outer simulation boundary**, z≈-48nm.
- The negative-gate Drain terminal current ~9.14e-14A is balanced predominantly by Substrate rather than Source: this is strong **Drain-to-Body leakage**. The **gate-correlated drain-side BTBT component** is promising, but the entire |Id| is **not proven pure GIDL**; boundary/contact/implant effects are unresolved.
- At LOWVD and high-positive-gate biases, the positive clipped generation can be near Source outer x≈-60nm. In LOWVD Vg1.2V, positive=+4.778e-20A but negative=-4.776e-19A (signed net negative); at HIGHPOS Vg0.6V positive=+1.236e-19A, negative=-1.358e-18A. **Keep signed/positive integrals separate; do not combine LOW/HIGHPOS positives with HIGHNEG as if all were drain GIDL**.
- Under matched HIGHNEG conditions, global peak |E| A/B differs ≤0.01% and positive BTBT integral ≤0.05%; some tiny LOW/HIGHPOS positive-source integrals differ ≤4.52%. A/B agreement is a **limited selected-point sensitivity result**, not full grid asymptotic convergence or physical validation.

## 4. Evidence, reproducibility and boundaries

- Machine-readable [`device/`](../../data/3d_sun_flat_sd_ab_20261020/device/) has parsed-original PLT series and interpolated **DERIVED** A/B overlays, plus actual node/current/KCL QC. [`spatial/`](../../data/3d_sun_flat_sd_ab_20261020/spatial/) has all 12 pairs/24 snapshots, signed-rate integration, full-Si ROI/region bins and hotspot coordinates. [`mesh/`](../../data/3d_sun_flat_sd_ab_20261020/mesh/) has SDE and native TDR mesh diagnostics.
- Archive SHA256s and archive filenames are recorded in [`data/README.md`](../../data/3d_sun_flat_sd_ab_20261020/README.md); full original SWB TDR/PLT/log/PP-CMD ZIPs are not stored in GitHub because of size. The original code for DC biases is in `code/sdevice/3d_sun_saddle_v1/D0,D1,D2...`, but PP-CMD with corrected n41/n46 Grid has to be preserved with the external source archives.
- Remaining extreme small tetra edges (A114/B198 <0.1nm), two-grid rather than 3-grid convergence, non-paper CAD assumptions, outer X=+60nm field peak, unknown model contribution to terminal current, and unresolved current-width/published extraction mapping prevent a validated absolute GIDL, Retention, or MEB optimum claim.

## 5. Next actions (ORDERED, not yet executed)

1. **First action — Drain X=+60nm finite-domain/contact/doping boundary audit, from existing TDR/CMD.** Inspect exact contact face, As/Boron profiles, drain junction and max-|E| point on fixed x/y/z cuts, classify edge/corner effects vs true junction field, compare Gate–Drain x15..30 nm and Drain outer x45..60 nm in matched bias. Keep n41/n46 identical physical controls.
2. **One bounded Hurkx ON/OFF contrast** at representative Vd=1.2V, Vg=-1.0V, 300K, MEB36nm starting with A, B only for confirmation if needed. Preserve all other physics/bias/geometry/mesh; compare Δ terminal currents signed Source/Drain/Body, KCL and spatial **signed** BTBT. Do not equate q∫max(G,0)dV with collected drain current.
3. **If unresolved boundary artifacts:** one isolated domain/contact-placement sensitivity control (distinct branch, identical physical device core and dopants), NOT broad geometry recalibration. Quantify field and leakage impact before accept/reject mechanism.
4. **Conditional MEB-depth bridge:** only after mechanism/QC gate, MEB=36 vs 48nm selected-point 300K with matched DC bias, surface geometry and ROI definitions, analyze hotspot relocation and BTBT/terminal leakage relative changes. Do not launch 15-point × 3T × retention 3D DOE.
5. **Downstream:** hand off mechanism-qualified leakage to existing 2D 1T1C Write/Hold/Read and 300/340/380K translation; no retention-time/refresh claim from the historical 100µs Hold pilot alone.

**Status at close-out:** electrical A/B sensitivity at one 36nm point verified numerically; absolute GIDL identity, domain-boundary independence, temperature and retention transfer remain **PROVISIONAL/NOT-DEMONSTRATED**. Keep historical Rounded M1, earlier 3D-Sun-B0 and frozen C7_4 intact; no root README/promotional headline update.
