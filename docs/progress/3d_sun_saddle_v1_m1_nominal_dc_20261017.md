# Independent 3D-Sun-SADDLE-V1 M1 nominal BCAT DC validation checkpoint — 2026-10-17

**Lineage and provenance:** A *new* 3D explicit-saddle reconstruction (not historical `3D-Sun-B0`, not frozen `B0-2D-PAPER-CAL`), with all five SDE geometry variables at Sun 2022 nominal. **Six SDevice simulations passed numerically. Model and mesh QC remain PROVISIONAL; no literature reproduction freeze or 3D adoption decision.**

**Main evidence and figures:** [3D baseline validation, plots and numerical comparisons](../validation/3d_sun_saddle_v1_20261017/README.md).

## Observed history and results

1. Geometry review: original FAST `M0` reconstructs an explicit rounded buried Si saddle, 5-nm oxide envelope, W gate material for photo-only `n1_W_VIS_bnd.tdr`, and W boundary contact used for electrical SDevice (body removed in production). Source/drain As-doped silicon fins verified in mesh/TDR cut.
2. `M0` quick Vd=0.05 V Id–Vg succeeds (259,919 SVisual elements); earlier negative-to-positive high-Vd sweep fails Newton/MinStep. Continue direction is a confounder.
3. `M1` saddle-crest local refinement: 538,096 SVisual elements, 84,537 input mesh points. All 6 completed n1 meshes are byte-identical SHA256 `f045dd9e52e8105620ea5dbc79ccb048f58c7f85b5d067662ef07164222f1283`.
4. `B0_3D` D0 Vd0.05 Vg0→1.5, `B0_3D_Copy` D1 Vd1.2 Vg0→2, `B0_3D_Copy_Copy` D2 Vd1.2 Vg0→−1: all complete. Representative bias TDR snapshots generated.
5. `B0_3D_D3_1`, `B0_3D_D3_2`, `B0_3D_D3_3`: Id–Vd Vd0→2 at fixed Vg0.1/0.6/1.2 V. All 107/108/109 original PLT points parsed, exact terminal endpoint reached; no fatal MinStep. Peak RAM 4.65/3.95/4.30 GB. At Vd2 terminal drain currents 8.3194e−14, 7.1302e−10, 3.9264e−6 A respectively.
6. D1/D3 consistency at Vd1.2: Vg0.1 interpolated mismatch 0.879%; 0.6/1.2 essentially equal. D3 Vg0.1 drain current largely balances substrate, not source (source collection ≈0.278% at Vd2).
7. Extracted *provisional* Vth high Vd 0.786046 V vs Sun 0.656 V (+0.130 V); SS 77.079 vs 76 mV/dec; DIBL 22.814 vs 23.6 mV/V; indicative Ion/Ioff 1.6725e8 vs Sun 3.4e10 but **different/unverified endpoint definitions**. Id–Vd low-gate traces substantially differ from paper visually. Not paper calibrated.
8. Serious mesh quality issue persists despite numerical completion: minimum edge 0.000835 nm, worst R/H 3.23e8; 189 non-Delaunay. NO all-region field/BTBT mesh convergence or definitive retention/GIDL claim.

## Explicit research gates remaining

- Establish electrical effective width and matched paper extraction conventions before claiming nominal Vth/SS/DIBL/Id–Vd reproduction.
- Check geometry Boolean sliver at saddle/oxide and independent *repaired* mesh sensitivity (minimum edge, R/H, DC, potential, field, BTBT and localized leakage).
- For Vg<0 drain-to-body current, separate Hurkx BTBT contribution from other carrier paths (ON/OFF, signed electrode currents, region-integrated generation).
- Do **not** initiate full five-parameter sweeps, copy these values into other lineage frozen files, update main README or infer retention improvements until the verification gates have passed.

**Archival policy:** complete user-executed PP-CMD, .log, native .plt, and .tdr in four collected CORE/TDR chat-source archives; the GitHub validation directory stores a public, deliberately compact numerical evidence index and resampled figure CSV. Full reproducibility bundle is supplied separately in the same ChatGPT delivery.
