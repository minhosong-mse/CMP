# REF14 — Kim & Kwon (2026): Saddle-Fin BCAT Fin-Height Optimization

> **Role:** 3D saddle-fin geometry and electrostatic checks; separating fin-height, body-doping and bottom-metal-depth effects; GIJL/PGE/1-row-hammer multi-objective trade-off. **Not** a direct reproduction of CMP MEB-depth GIDL, calibrated retention time or current 3D baseline.
>
> **Source status:** User-provided full eight-page IEEE Access PDF directly checked on 2026-10-27, including Table 1 and Figs. 1, 5, 8, 16–17. Facts below are paper-specific unless marked as CMP interpretation. No paper figures are copied into this repository.

## Bibliographic record

D. Kim and M.-W. Kwon, “Optimization of Fin Height in Saddle-Fin BCAT Structured DRAMs,” *IEEE Access*, vol. 14, pp. 143318–143325, 2026. DOI [10.1109/ACCESS.2026.3733420](https://doi.org/10.1109/ACCESS.2026.3733420).

## Why it is relevant to CMP

- **[LIT-EXPLICIT, PDF pp. 2–3, Fig. 1/Table 1/Fig. 2]** A 1z-nm-class **3D saddle-fin BCAT** is simulated with upper n-poly-Si / lower W gates. Fin height is swept from **19 to 1 nm** in 1-nm increments while body doping is adjusted to compensate Vth. Bottom-metal depth also varies with this geometry.
- **[LIT-EXPLICIT, PDF pp. 3–4, Figs. 3, 5, 8]** The paper distinguishes **GIDL at gate–drain overlap** from **GIJL associated with the lower gate–substrate field**. Its claim that the Hfin change has negligible impact on GIDL is tied to its assumption of unchanged gate–drain overlap; it is **not** a statement that all gate-top/MEB variations leave GIDL unchanged.
- **[LIT-EXPLICIT, PDF pp. 4–7, Figs. 8–17]** The paper separates structural and Nbody contributions to junction leakage/disturbance and evaluates opposing effects across DIBL, GIJL, passing-gate effect and 1-row hammer.
- **[CMP-INFERRED]** Its strongest contribution to CMP is **analysis methodology and spatial/parameter-definition checks**, not transplanting its numerical optimum, leakage percentages or 1-row-hammer results into the CMP 3D MEB study.

## Reusable model facts — do not silently transfer values

| Quantity | Paper source / value | CMP interpretation |
|---|---|---|
| Cell | 3D 6F² saddle-fin BCAT; 1z-nm context (Fig. 1) | Structural comparison only; not identical to the independent CMP CAD |
| Word-line / active / channel widths | 10.6 / 21.2 / 30 nm (Table 1) | Different parameter definitions from CMP Lg=20 nm, Wfin=17 nm; no one-to-one width substitution |
| DBCAT / top metal / bottom metal depths | 132 / 33 / 60.3 nm nominal (Table 1) | Determine reference planes before any geometry comparison |
| Oxide | WL sidewall 7 nm, bottom 5.3 nm (Table 1) | Not equivalent to CMP nominal Tox=5 nm everywhere |
| Hfin | 19 nm nominal; 19→1 nm sweep (Fig. 2) | Silicon saddle-fin protrusion height, **not** CMP MEB/gate-top depth |
| Gate | n-poly-Si top, tungsten bottom; n-poly doping 10²¹ cm⁻³ | Dual-material gate; CMP active 3D is single-WF tungsten (4.8 eV) |
| Doping | BLC/SN 10²⁰ cm⁻³; body baseline 10¹⁷ cm⁻³, varied for Vth compensation | Nominal concentration alone does not define the same 3D junction profile |
| Nominal biases | Vsub=−0.7 V, Vd=1.0 V, Vg,on=3 V, Vg,off=−0.2 V (PDF p. 2) | Do not equate with CMP Vsub=0 V, Vd=1.2 V, Vg≈−0.7 V GIDL protocol |
| Models named | phuMob, high-field saturation, Enormal, SRH, TAT, BTBT | Specific BTBT/TAT implementation, trap details, solver and mesh not sufficiently disclosed |
| Vth calibration | Constant-current criterion Id=100 nA; nominal Vth≈0.54 V at Vd=1 V | Paper-specific metric and Nbody-calibrated family |
| Disturbance cell | 8 fF capacitor; 60-ns neighboring-WL pulse period; 10-pulse SN observation (PDF pp. 5–7) | Row-hammer transient precedent, **not** a demonstrated CMP hold/retention time |

**Reproduction boundary:** Exact 3D CAD/contact geometry, full doping implant profiles, material work-function assignments, BTBT/TAT/trap parameters, solver controls and mesh refinement are not supplied in enough detail for exact absolute reproduction. **[CMP-INFERRED]** Treat this paper as partial structural/physics guidance rather than a calibrated reference device.

## Reported trade-offs (paper-only)

| Result under Hfin reduction | Paper-reported change | Primary evidence / interpretation |
|---|---:|---|
| SS | roughly +10 mV/dec | Fig. 4(a), weaker gate control |
| DIBL | +19% | Fig. 4(b), worsens |
| GIJL | −87% in combined Hfin + Nbody condition | Fig. 8 and body text; lower gate–substrate field |
| Passing-gate effect | +29% | Figs. 7–11, worsens; adjacent WL necessary |
| 1-row-hammer immunity | +92% in data-flip pulse count | Figs. 12–17, improves under the calibrated disturbance model |
| Combined normalized-score best Hfin | 12 nm | Fig. 16, four metric-specific best/worst scores summed with equal weight |

**[LIT-EXPLICIT / CAUTION]** Hfin change, **Nbody re-calibration**, and varying bottom-metal geometry are coupled in the main sweep. The separate Hfin-only, Nbody-only and combined controls in Fig. 8 are especially useful as a methodological precedent. The 12-nm optimum depends on this paper's geometry, metric choices, normalization and weighting; **it is not a CMP MEB optimum**.

**[FIGURE-ESTIMATED / NEEDS VERIFICATION]** Fig. 5(d) labels approximately 3.18×10⁻¹² A and 7.16×10⁻¹³ A at the displayed high-magnitude substrate-bias comparison (simple endpoint reduction ≈77.5%), whereas Fig. 8/text state a combined 87% improvement. The conditions/extraction mapping are not sufficiently established to force those figures into one identical comparison. Fig. 5 uses a **Vsub sweep reaching −12 V**, far from the nominal Vsub=−0.7 V operating condition.

## GIDL versus GIJL — the critical claim boundary

1. **GIDL:** gate–drain overlap-region leakage, commonly associated with BTBT/TAT. The paper argues its particular Hfin variation largely leaves that overlap unchanged (PDF p. 3, Fig. 3 uses an Ion/IGIDL ratio).
2. **GIJL:** gate–substrate/saddle-bottom electric-field-associated junction leakage; modified Hfin and reduced body doping both change this field (Figs. 5 and 8).
3. **CMP:** active structural input is **MEB/gate-top depth**, not Hfin. A gate-top geometry sweep can alter the gate–drain coupling/field differently from this paper's Hfin sweep.
4. **Inference boundary:** The literature does not prove CMP's terminal GIDL collection fraction, or any resulting physical 1T1C retention improvement. Nor does an E-field peak alone quantify a collected terminal current.

## Specific implementation and evidence-extraction hints

1. **[Fig. 1] Verify geometric reference planes.** In the current 3D SDE parent, explicitly mark wafer top, saddle crest, gate top, recess depth, junction target, STI, metal/poly regions and each contact face. Do not invent a mapping Hfin↔DBM↔CMP MEB when one is not supplied.
2. **[Fig. 2/8] Isolate covariates.** Compare fixed-doping structural MEB results first; consider controlled body-doping or other geometry tests only if needed. Do not silently retune the selected CMP working model to reproduce the paper's Vth.
3. **[Fig. 5] Keep spatial and terminal evidence separate.** Plot matched Gate–Drain and Outer Drain ROI electric-field/BTBT with fixed and hotspot-following cuts; compare signed source/drain/body/gate currents and KCL. A spatial q∫GdV is a generation equivalent, not proven collected GIDL.
4. **[Figs. 5/8] Check the known outer-domain risk.** Current CMP has an unresolved x≈60-nm drain contact/boundary hotspot. Confirm face/Si/ROI membership and doping before interpreting it as an intrinsic MEB mechanism.
5. **[Figs. 7–15] Respect topology.** Passing-WL interference and 1-row-hammer require adjacent word lines, traps, pulse calibration and SN conditions; they are not automatically represented by a single-gate CMP GIDL deck.
6. **[Fig. 16] Evaluate a design *range*.** After CMP execution supports GIDL, Cgd, 1T1C and temperature effects, use explicit pass/fail guardrails and disclose any normalization/weighting sensitivity. No current paper-based 12-nm transfer.

## Comparison to current CMP active lineage (2026-10-25)

- **[CMP-EXECUTED / WORKING SELECTED]** 3D-Sun-SADDLE-V1 / Flat upper S/D: Lg20 nm, Wfin17 nm, Tox5 nm, recess120 nm, junction target48 nm, WF4.8 eV, Mesh A/CurveGrid1, Hurkx ON. Selected as an **independent 3D working baseline**, not fully mesh-converged or paper-calibrated. See [close-out](../progress/3d_vg06_channel_working_baseline_closeout_20261025.md).
- **[CMP-EXECUTED]** 24/36/48-nm MEB DC and Vg=0-V 3D Hurkx ON/OFF and spatial ROI comparisons exist. Gate-side |E|max and BTBT generation decrease toward MEB48, but Outer Drain remains sensitive; see [3D interim spatial review](../progress/3d_sun_meb_paper_interim_20261024.md).
- **[PLANNED]** Next step remains matched **MEB 24/36/48 nm, 300 K, Vd1.2 V, Vg≈−0.7 V, Hurkx ON/OFF**, signed four-terminal current/KCL and Gate–Drain/Outer Drain 3D E/BTBT; bounded x≈60-nm boundary check; then 3D Cgd → temperature → 1T1C. This reference note **does not** authorize changing geometry/WF, solver/physics or frozen 2D lineages.

## Non-transferable results / research integrity

- GIJL −87% **≠** CMP GIDL reduction.
- 1-row-hammer +92% pulse endurance **≠** longer physical data retention time or refresh reduction.
- Hfin=12 nm paper optimum **≠** CMP optimal MEB or production process window.
- Paper fin-height/DWFG/body-doping results **≠** validated single-WF MEB parameter transfer.
- Named BTBT/TAT models **≠** identical Hurkx/NonlocalPath parameterization.
- Neither paper figures nor this note establish full paper-to-CMP 3D equivalence.

**Bottom line:** REF14 supports **3D saddle-fin geometry checking, controlled variable isolation, spatial leakage interpretation and explicit multi-metric trade-offs**. It does **not** replace CMP native executed evidence for GIDL/retention or justify changing the frozen/working baseline.

## Primary-source anchors

- Original publication and DOI: [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/11690560/), [DOI](https://doi.org/10.1109/ACCESS.2026.3733420).
- PDF p. 2 (journal p. 143319): Fig. 1 and Table 1 geometry, Fig. 2 Vth/body-doping compensation, simulation physics.
- PDF pp. 3–4 (journal pp. 143320–143321): GIDL/GIJL distinction, Figs. 3/5/8 field and isolation.
- PDF pp. 4–7 (journal pp. 143321–143324): Figs. 7–17 PGE, 1-row hammer, normalized-score optimum.
