# 2026-11-11 — External 3D SN I–V / short-Hold evidence checkpoint (PROVISIONAL)

**Lineage:** `3D-Sun-SADDLE-V1 / Flat upper S/D` independently executed on Sentaurus T-2022.03 outside Git. No new TCAD simulation was run during this Git archiving. **Status:** IVSN extraction/evidence 20/20 and 100ns Hold 16/20 complete; scientific retention time and MEB design range unvalidated.

## Completed this session

- User delivered an original 3D MixedMode archive, SHA256 `861104a9aa070b8ba1078d64c056b8f11cc76c8c6415b50e21cce885041dc371`.
- Corrected output-file selection analytically: `IVSN_0P8_TO_1P0_n*_ivsn_sys.plt` and `DIRECT_HOLD_n*_hold_sys.plt` carry actual data; unprefixed names can be initialization-only. Prior SVisual `found 60` glob failure is a routing issue, not a numerical IVSN failure.
- From 20×101 VSN currents, computed 10fF constant-C `t_est(1→0.8)`; recomputed numbers against the archived curves with **max relative error below 1e-12** (numerical exactness of the reduction only).
- 16/20 direct Hold completed 100ns, with 4 known failures. 16/16 direct voltage-loss early-time slopes agree with IVSN initial slope within 0.0766% by existing QC. **No actual 0.8V crossing.**
- Joined the existing independent 300K 3D 140-case DC metrics with the new 1T1C estimates at 5 depths and created six separate plots; interpreting Hurkx model excess and t_est separately.
- Drafted **36–60nm exploratory search / 42–56nm focused comparison; approximate relative-filter overlap 44–55nm is NOT an optimum or a freeze**.
- Recorded week-4 feedback on Hfin/Hsaddle inverse Vth impossibility and mandatory temperature-aware retention.
- No changes to frozen historical 2D, original SDE geometry, current physics, 300K evidence, root README or past scientific claims.

## Blocked and not executed

1. Four 3D direct Hold conditions: `36/380 n1968`, `54/380 n2238`, `60/380 n2328` (initial Coupled), `48/233 n123` (transient ~4.9ns). Four numerical recovery branches **not yet verified/executed**; avoid modifying the valid 16 results.
2. Original Nov-09 temperature campaign partial targets: `36/380 Mode5 n1979`, `54/340 Mode1 n1686`. Separate lineage/execution and separate diagnostics.
3. Cross-project mesh/PP/physics normalization and 54/60 structure-node mapping, x≈60nm Outer Drain/Face91 attribution, mesh sensitivity, low-T model, physical Ceff and original 3D current scaling. No completed 3D Cgd, no direct 0.8V crossing, no Write–Hold–Read or selected final design range.
4. SVisual tool routing `glob` bug and exact prefix selection; scientifically recover data directly from SDevice CSV in meantime.

## Next FIRST action

- **Selective external Hold rescue** only for the four failures in a separate SWB branch with T-2022.03-verified numerical continuation, while preserving other original results.
- Verify original 3D mesh/PP/Node mappings and 10fF plus current scaling; perform representative IVSN and short-Hold numerical sensitivity + Outer Drain contact QC before claiming a physical retention metric.
- Separately recover prior Nov-09 2 incomplete temperature DC cases as needed; then consider additional **9 proposed 300K IVSN MEB depths** `38/40/42/44/46/50/52/56/58`; not yet run.
- After guardrails, select MEB and temperature representative points for longer direct-Hold (or separately, Write–Hold–Read) validation, never extrapolating short Hold as a direct physical retention time.

Evidence: [20-case data](../../data/3d_1t1c_retention_20261111/README.md), [technical review](../evidence/3d_1t1c_ivsn_hold_analysis_20261111.md), [candidate range proposal](../evidence/3d_meb_exploratory_range_20261111.md).
