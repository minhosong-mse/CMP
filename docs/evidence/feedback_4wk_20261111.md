# Week-4 CMP mentor feedback — reviewed during 2026-11-11 follow-up

> **Status: Recorded / open verification actions.** Do not infer the feedback was delivered on exactly this date; it was discussed in the surrounding fourth-week presentation workflow.

## F4-1. Saddle-fin height 48nm and constant-current Vth backward inference

- Sun, Baac & Shin, *Micromachines* (2022), DOI `10.3390/mi13091476`: explicit nominal `Wfin=17nm` and `Hfin=48nm`; nominal Vth≈0.656V and constant-current `Id,crit=1e-7 A × (W/L)`.
- The independent CMP 3D SDE preserves `Hfin=48nm` and separately defines `Hsaddle=48nm`. **The latter is a reconstruction assumption** rather than a fully paper-derived coordinate definition.
- Preliminary inverse check with the CMP 36nm high-Vd Id–Vg transfer curve at paper Vth≈0.656V (current of order `3.3e-9A`, assuming `L=20nm`) implies `W_inferred~0.66nm`. For a heuristic `Weff=Wfin+2H`, `H~(0.66-17)/2=-8.17nm`, physically impossible. The apparent negative height is **evidence that width-only inversion cannot reconcile different electrostatic/current/bias models**, **not a measured negative fin height** or proof that 48nm is wrong.
- Ambiguity remains in paper's exact `W` normalization, whether `Hfin` corresponds to the simulated upper fin vs lower saddle, and Vth bias equivalence. **No replacement Hsaddle derived or accepted.**
- Fourth-week presentation: show attempted inverse expression, observed contradiction, and plan controlled height-sensitivity simulations only after consistent geometry/current definitions, not arbitrary forced fitting.

## F4-2. Temperature must enter retention validation

- The user reported feedback that a single-temperature Retention readout alone is inadequate for the project's temperature-dependent objective.
- Current independently executed transistor temperature matrix is `233/300/340/380K`; Nov-11 SN I–V integral estimates now exist for 5 MEB × 4 T under a **10fF assumption**, with 16 completed 100ns Holds.
- Important wording: the computed trend answers a preliminary **model-internal** temperature-to-storage-node question; it is **not** a direct full VSN 1.0→0.8V crossing, calibrated read-failure criterion, or demonstrated refresh margin.
- Next gate: selectively recover 4 Hold failures, validate C_eff/3D current scaling, compare direct transient vs integral and move toward Write–Hold–Read.

References: [3D report](3d_1t1c_ivsn_hold_analysis_20261111.md), [search range proposal](3d_meb_exploratory_range_20261111.md), [Sun original paper](https://doi.org/10.3390/mi13091476).
