# CMP Model Scope and Claim Boundaries

> Last synchronized: 2026-09-22  
> Purpose: define what the CMP models can and cannot support after the first/second presentation feedback cycles.

## 1. Model hierarchy

CMP no longer treats “the baseline” as a single model with one fidelity claim.

### 1.1 Main DOE model — B0 simplified 2D BCAT

```text
Model ID                 B0
Geometry                 simplified 2D BCAT cross-section
Nominal MEB / GateTop    36 nm
Gate length              20 nm
Recess depth             120 nm
SiO2 liner               5 nm
Junction depth           48 nm
Body doping              B, 1e17 cm^-3
S/D doping               As, 1e20 cm^-3
Gate                     single-WF W, 4.8 eV
```

Role:

- dense MEB design-space exploration;
- reproducible relative comparison;
- Cgd / DC / GIDL / temperature / 1T1C protocol development;
- candidate-range screening.

The physical MEB etch process is not simulated. `MEB_Depth` represents the resulting gate-top depth.

### 1.2 Validation anchor — 3D-Sun-B0

A literature-consistent 3D reconstruction was built from the explicit structural information reported by Sun et al.

Nominal structural anchors include:

```text
Lgate      = 20 nm
Drecess    = 120 nm
DBCAT      = 36 nm
Tox        = 5 nm
Wfin       = 17 nm
Djunction  = 48 nm
Gate WF    = 4.8 eV
```

Completed baseline-feedback checkpoints include geometry/contact/doping freeze, source/drain junction checks, G0/G1/G2 electrical runs, sensitivity checks, and DC electrical-mesh convergence.

Important boundary:

> `3D-Sun-B0` is a **literature-consistent 3D reconstruction**, not an exact calibrated reproduction of the absolute Sun-et-al. electrical characteristics.

Representative reconstruction-defined metrics remain different from the paper nominal values. The discrepancy was not force-fitted away because the full process/CAD/calibration deck is not published.

Role:

- higher-fidelity model-fidelity anchor;
- controlled 2D↔3D comparison;
- selected-point validation after the final/near-final MEB decision matures.

The 3D model is **not** used for a full MEB × temperature × gate-scheme factorial sweep in the current mainline.

## 2. Established transistor-level methods

### DC

- internal Vth / SS / Ion / DIBL rules are frozen in Run 1;
- `Mesh-DC = Medium / Mesh_Code 1` was selected by the current DC convergence study;
- these are project-internal comparison metrics, not production calibration.

### GIDL / BTBT

- formal relative GIDL branch uses `Band2Band(Model=NonlocalPath)`;
- formal endpoint condition is `VD=1.2 V`, `VG=-0.7 V`;
- `Mesh-GIDL = Mesh_Code 3` uses the common drain-side refinement ROI;
- terminal current is a project-internal relative leakage metric;
- absolute BTBT calibration is not claimed.

### Mesh / hotspot feedback

For the complete R6.5 set `36/41/43/45/47/48/49/51 nm`:

- all independently extracted BTBT hotspots remain inside the same Mesh-Code 3 ROI;
- minimum nearest-edge margin = `9.875 nm`;
- observed X-hotspot motion over 36→51 nm is small relative to the ROI.

This supports **coverage and comparison consistency**, not universal absolute mesh independence.

### E-field interpretation after feedback

The historical Run-5 field metric:

```text
E_wall,max
Y = 0.116 um
X = 0.032–0.070 um
```

is retained for chronology and reproducibility but is no longer the sole/primary mechanism interpretation.

The current feedback-resolved mechanism evidence uses:

1. full-Si BTBT hotspot localization;
2. hotspot-following cut;
3. BTBT amplitude/profile;
4. 10/20/50% BTBT-active-region sensitivity;
5. active-region `int(|E| dx)`;
6. 1-D `int(G_BTBT dx)` only as a spatial-generation trend cross-check.

The representative 20% criterion is a CMP analysis choice, not a universal literature standard.

No direct quantitative `Cgd → E-field → GIDL` causal law is claimed from the correlation alone.

## 3. Extended-MEB interpretation

R6.5 established the following project roles:

- `P1 = 41 nm`: historical initial screened-window candidate;
- `P2 = 48 nm`: transistor-level electrostatic/GIDL candidate carried into cell validation;
- `49 nm`: primary challenger / sensitivity point;
- `51 nm`: low-current / background-sensitive boundary reference.

`48 nm` is not a global, production, process, 3D, or final optimum.

The geometry-derived W cross-section / normalized `1/A_W` RWL proxy shows that deeper MEB introduces a practical structural penalty. The 47–49 nm region is therefore treated as a diminishing-return candidate region rather than an automatically optimal region.

The proxy is **not** an actual distributed word-line resistance or RC-delay simulation.

## 4. Temperature scope

Completed existing temperature framework:

```text
300 / 340 / 380 K
```

These are fixed lattice-temperature / isothermal comparisons, not electrothermal self-heating simulations.

At the transistor level, the high-temperature leakage balance becomes increasingly background-sensitive.

At the B0 cell level, approximately normalized direct-Hold results have been committed at 300/340/380 K.

Planned extension:

```text
233 K = -40 °C
```

The 233 K point is **not yet a completed CMP result**.

## 5. 1T1C scope

Executed B0 anchors include:

```text
AreaFactor = 0.017
Ccell      = 10 fF
VBL_WRITE  = 1.2 V
VWL_ON     = 3.0 V
300 K Twrite ≈ 667 ns → VSN≈1 V
```

Completed:

- 300 K write-to-~1 V normalization;
- direct floating Hold to 100 us;
- independent D0/D1 Read transfer;
- integrated 300 K Write→Hold→Read for tested Hold windows;
- 340/380 K write normalization;
- approximately normalized 300/340/380 K direct Hold.

Still open:

- leakage-vs-V / final physical retention metric;
- retention-specific Mesh1/3 numerical check;
- formal MEB-to-cell retention comparison.

The short-window direct-Hold slope is **not** extrapolated into a physical retention time.

`VSN=0.8 V` remains a comparison criterion / literature-motivated window point, not a demonstrated CMP read-failure threshold.

## 6. High-WL write-transfer guardrail

The current write path reaches `VSN≈1 V`, but it requires `VWL_ON=3.0 V`.

This is now an unresolved performance guardrail.

Future selected-point analysis should consider:

- `VWL→VSN` transfer;
- write time;
- MEB dependence;
- Ion / Vth relation;
- read margin;
- leakage / retention interaction.

“1 V reached” alone is not treated as complete write-performance validation.

## 7. DWFG scope

The current baseline remains **20 nm single-WF**.

DWFG is a planned downstream transferability branch:

```text
derive SG MEB candidate/range
→ introduce literature-grounded DWFG extension
→ re-search BTBT hotspot / verify mesh ROI
→ compare field redistribution / GIDL / retention
→ determine common range or optimum-range shift
```

The project does not replace the 20 nm baseline with the 15 nm ICEIC device.

No DWFG result, SG/DWFG common window, or DWFG superiority is claimed before execution.

## 8. Final design-range claim boundary

The final target is a **usable/effective MEB design range**, not a single minimum-GIDL point.

Candidate synthesis may combine:

- GIDL suppression;
- 1T1C retention benefit;
- write/read feasibility;
- temperature robustness;
- geometry-derived word-line penalty;
- DWFG transferability when executed;
- selected-point 3D trend validation.

Not currently supported as completed project claims:

- production optimum;
- calibrated absolute retention time;
- refresh-burden reduction;
- actual distributed WL resistance / RC delay;
- variation-aware manufacturing process window;
- completed 233 K behavior;
- completed DWFG behavior;
- SG/DWFG common range;
- full 3D quantitative equivalence to the paper or a production DRAM cell.

## 9. Evidence links

- [Run Sheet](RUN_SHEET.md)
- [Decisions](DECISIONS.md)
- [Feedback Log](FEEDBACK_LOG.md)
- [3D baseline close-out](evidence/feedback_baseline_closeout_20260914.md)
- [E-field / BTBT hotspot validation](evidence/feedback_efield_hotspot_validation_20260911.md)
- [Full R6.5 mesh coverage](evidence/feedback_mesh_run65_full_validation_20260913.md)
- [RWL proxy trade-off](evidence/feedback_rwl_tradeoff_proxy_20260913.md)
- [Run-7 cell operation](evidence/run07_cell_operation_checkpoint_20260920.md)
- [Run-7 temperature-normalized Hold](evidence/run07_hold_temperature_normalized_20260921.md)
- [Post-Turn-02 roadmap](research/post_turn02_validation_roadmap.md)
