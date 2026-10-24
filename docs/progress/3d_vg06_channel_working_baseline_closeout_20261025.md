# 2026-10-25 — 3D-Sun-SADDLE-V1 24/36/48 nm: Vg=0.6 V channel analysis and working-baseline handoff

> **Session: CLOSED / validation evidence EXECUTED / 3D working baseline SELECTED for the next CMP research stage.**
> The selection is a **research-use working baseline**, **not** a paper-calibrated absolute device, mesh-converged physical model, or final production/retention claim. The full native 3D TDR evidence remains in the user-provided external source ZIP, indexed in [data manifest](../../data/3d_vg06_channel_validation_20261025/README.md). No root README edit.

## User's explicit scope decision (2026-10-25)

- Prioritize **the newly constructed independent 3D** model, not historical 2D results, for the next **MEB → E-field/BTBT/GIDL → Cgd → temperature → 1T1C retention** studies.
- Matching **every absolute Vth/Id and every paper-specific depth ranking** is **not required** for adopting an internally coherent 3D working reference. Record disagreements openly rather than force-fitting.
- Keep current nominal physical model fixed for the next stage: `3D-Sun-SADDLE-V1 / Flat upper S/D`, nominal `Lg=20 nm`, `Wfin=17 nm`, `Tox=5 nm`, `Drecess=120 nm`, nominal junction target `48 nm`, `WF=4.8 eV`, `Mesh A / CurveGrid1`, `Hurkx ON`, `300 K` for the baseline checkpoint.
- Preserve completed 2D branches strictly as historical, separate evidence, **not as prerequisite validation or a source for mixing absolute values** into the new 3D chain.

## Executed inputs and QC

- **Earlier full DC**: 24/36/48 nm × 5 sweeps (Id–Vg Vd=0.05/1.2 V; Id–Vd Vg=0.1/0.6/1.2 V), **15/15 simulations**, **2,337 solver-log points**; 24/36/48 DC trends reconstructed from distinct logs. Native current PLT names collided across nodes; 36 and 48 independently cross-checked. See [2026-10-24 review](3d_sun_meb_paper_interim_20261024.md).
- **New three-depth SDevice TDR recovery**: separate 24/36/48 nm `Vg=0.6 V`, `Vd=1.2 V`, Hurkx ON, 300 K; SDE parent nodes 1/4/6 → SDevice nodes 2/5/7. Original physical geometry/mesh was reused; this was **new SDevice execution**, not an unchanged historical snapshot.
- All three executed successfully and generated their own final 3D HDF5 TDR, console log, executed SDE source, run deck and source manifest. The three TDR SHA256 values match the external ZIP manifest, and all three decode with HDF5 `collection` data. **The archived `run_des.cmd` has a generic comment mentioning 36 nm even in other folders: the authoritative depth mapping is each executed SDE `DBCAT_nm`, mesh, HDF5 tag, and individual manifest, not this inherited comment.**
- Native Silicon `R.SiSubstrate` tetra fields were interpolated at common coordinates rather than matching unrelated vertices. Sampled `ElectrostaticPotential`, `eDensity` and `DopingConcentration`. Other fields (`ElectricField`, `Band2BandGeneration`) are available in the TDR for future analysis.

## Reproduced terminal and electrostatic evidence

| MEB (nm) | Id at Vg=0.6 V, Vd=1.2 V (A; log rounded) | Id relative to 24 | mean φ at x=−15 nm, common Y–Z Silicon section (V) | sampled eDensity sum, relative to 24 |
|---:|---:|---:|---:|---:|
| 24 | 6.197e−10 | 1.00000 | 0.229327 | 1.00000 |
| 36 | 6.403e−10 | 1.03324 | 0.230000 | 1.03338 |
| 48 | 7.069e−10 | 1.14071 | 0.231889 | 1.14066 |

- Common Y–Z section is **x=−15 nm**, `y=−8…8 nm`, `z=−100…−75 nm`, 1 nm pitch, **442 shared valid Silicon samples**. The `eDensity` sum is **a sampled concentration proxy**, not a current integral or charge density integrated with exact tetra volumes.
- 24→48 nm: section mean φ **+2.5624 mV**, sampled electron density **+14.0663%**, terminal Id **+14.0713%**. Common-section doping does not change. Source-contact Si potential near `x=−55,y=0,z=−25 nm` remains ≈0.53818 V; at `x≈−14.5,y=0,z=−75 nm`, potential ≈0.28804/0.28881/0.29112 V. This corresponds to **≈3.07 meV source-to-channel electrostatic barrier proxy decrease** (24→48), **not** a directly extracted conduction-band minimum or proof of the unique transport saddle.
- The terminal 48/24 ratio corresponds to ≈3.4 meV through a simple `kT ln(I48/I24)` exponential estimate at 300 K. The proximity to the electrostatic proxy is a **qualitative interpretation**, not independent mechanistic proof.
- Existing 36-nm native PLT separates bias regimes: at `Vg≈0.1 V`, ≈97.8% of the absolute source+substrate terminal-current sum is substrate current (drain/body leakage dominated); at `Vg=0.6 V`, ≈99.9993% is source current (source/drain channel-current dominated). These are terminal path ratios, not BTBT collection fractions.
- Hurkx-OFF controls previously showed the `Vg≈0.6 V` depth-order inversion persists without the Hurkx model. Together, this supports a **channel-electrostatics hypothesis** rather than Hurkx as the sole cause.

## Paper comparison and baseline-selection scope

Reference: Sun, Baac and Shin, *Micromachines* **13**, 1476 (2022), DOI [10.3390/mi13091476](https://doi.org/10.3390/mi13091476). The paper's Table 1 is a raster plot; visual depth-order readings are not exact digitized measurements.

| Characteristic | CMP 3D finding | Paper comparison / status |
|---|---|---|
| 36 nm nominal high-Vd Vth | ≈0.783 V | paper nominal 0.656 V; ≈+0.127 V, extraction/current-width equivalence not proven |
| 36 nm SS, DIBL | ≈75.887 mV/dec, ≈21.9 mV/V | similar to paper nominal 76 and 23.6, definitions not identical |
| Id–Vg | subthreshold-to-ON turn-on qualitatively plausible | paper-like broad shape; low-Vg MEB OFF ordering is **opposite** (paper visually 48>36>24 vs CMP 24>36>48) |
| Id–Vd, Vg=1.2 V | high-current rise, depth order **24>36>48** | order agrees; shape and amplitude not exact |
| Id–Vd, Vg=0.6 V | depth order **48>36>24** | opposite paper visual 24>36>48; deep MEB has ~14.1% higher Id at Vd1.2 |
| Id–Vd, Vg=0.1 V | extremely low current, drain/body dominated for 36nm | paper raster shows much higher current; normalization, junction/outer boundary and Vth may contribute; **unresolved** |

**Vth-offset distinction:** at `Vg=0.6 V`, `Vg−Vth≈−0.183 V` in CMP vs ≈`−0.056 V` from paper nominal Vth. Using ~76 mV/dec gives an **illustrative ~47× current sensitivity** for an approximately 127 mV shift under a uniform-subthreshold-slope assumption. This can explain part of the absolute current-level discrepancy, **not** the per-MEB ordering reversal by itself. CMP high-Vd Vth slightly falls with MEB (≈0.783786/0.783237/0.782060 V); that trend is consistent with higher `Vg=0.6` Id at deep MEB in its own model.

**Decision:** accept `3D-Sun-SADDLE-V1 / Flat upper S/D` as a fixed-parameter **independent 3D WORKING BASELINE** for next-stage CMP research, not as an exact Sun-paper-reproducing or production-calibrated baseline. Do not change WF/geometry solely to force paper absolute current or ranking. A different paper ranking must remain explicitly disclosed.

## Scientific/numerical limitations to carry forward

1. Historical 36nm Mesh A versus Mesh B at Vg0.6, Vd1.2: `Id(A)=6.402944225e−10 A`; `Id(B)=6.084047702e−10 A`, ≈**5% mesh sensitivity**. Three-depth 14.07% relative increase is **not yet a general mesh-converged magnitude**.
2. Outer Drain x≈60 nm high-|E| and potential contact/boundary sensitivity remain unresolved; this particularly limits interpreting all OFF-terminal drain current as gate GIDL.
3. `ElectrostaticPotential` ≠ directly calculated `ConductionBandEnergy`; `eDensity` sampled concentration ≠ current-density streamline/collection.
4. `Hurkx ON−OFF` is a model-controlled excess terminal current, not automatically a pure physically collected GIDL current.
5. No 3D Cgd, temperature-dependent 3D 1T1C retention or final MEB optimum was established today. Retention changes require future cell-level execution; old 2D/Legacy 1T1C results do not transfer.

## Next FIRST ACTION — fast 3D mechanism follow-through

**Use this working 3D model directly**, with unchanged physical/WF/mesh/solver lineage. At representative **24/36/48 nm, T300 K, Vd=1.2 V, Vg≈−0.7 V**, run/reuse matched 3D **Hurkx ON/OFF signed 4-terminal current** and spatial **Gate–Drain vs Outer Drain E/BTBT** analyses; record KCL and 3D ROI attribution. **Within this work, perform a bounded check of x≈60 nm Drain contact/outer-boundary membership** to qualify low-Vg leakage claims. A large 3D geometry/DC paper-fit reoptimization or 2D-model revalidation is **not** the next task. Then proceed to 3D MEB–Cgd and temperature/1T1C.

## External evidence and repo-local artifacts

See [data index](../../data/3d_vg06_channel_validation_20261025/README.md), executed 24/36/48 native TDR ZIP hashes, source deck manifests, crosssection CSV, and two SVG trends. The external raw archives and earlier unrelated historical evidence are not rewritten. This session closed as **3D WORKING BASELINE SELECTED / PHYSICAL VALIDATION CONTINUES**.
