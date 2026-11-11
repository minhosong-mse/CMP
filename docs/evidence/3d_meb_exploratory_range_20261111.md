# 2026-11-11 — Provisional 3D MEB search-range design (NOT an optimal range)

> **Status: PLANNED / CONDITIONAL, not a freeze.** This is an exploratory design-of-experiments proposal derived from five 300K data points and the user-requested broad range selection. Distinct from historical 2D Legacy 48nm selection and Sun-paper 36nm structural anchor.

## 1. Observed five-point 300K behavior

Source [six-metric join](../../data/3d_1t1c_retention_20261111/CMP_300K_MEB_six_metrics.csv) shows from MEB 36→60nm: Ion −12.8%, Ioff −38.6%, SS +4.23mV/dec, DIBL +9.17mV/V, Hurkx ON−OFF excess −78.6%, IVSN 10fF t_est ×3.48. The 48→60nm incremental Hurkx reduction is small relative to earlier gains, while Ion/DIBL penalties continue. These directions are model-internal and neither establish physical collected GIDL nor measured Retention crossing.

## 2. **Hypothetical relative pass filters** (not CMP-frozen, not production specifications)

Use 36nm 300K as an internal reference. Candidate constraints **for exploration only**, chosen to reveal tradeoffs:

| Metric | Proposed comparator | Approx. first crossing from 5 observed points |
|---|---|---|
| Ion | >=90% of nominal 36nm Ion | upper ~57nm |
| high-Vd SS | <=36nm SS + 3 mV/dec | upper ~56nm |
| DIBL proxy | <=36nm DIBL + 5 mV/V | upper ~55nm |
| Hurkx ON−OFF | <=50% of 36nm excess | lower ~44nm |
| 10fF SN I–V t_est | >=2× of 36nm estimate | lower ~42nm |

Crossings estimated **only by piecewise linear interpolation** between executed depths, with no new Sentaurus executions. The simultaneous intersection is approximately **44–55nm**, but it is a *hypothetical relative-guardrail overlap*, not experimentally validated, not a hard acceptance criterion, and not an optimized device. A wider **42–56nm** concentration band is selected to reduce boundary exclusion bias; possible **44–54nm** contender band remains **UNCONFIRMED**.

## 3. Staged MEB coverage, not execution claim

1. **Broad bracket**: MEB 36–60nm (5 already executed IVSN depths, not a dense sweep).
2. **300K coarse interpolation test**: `36 38 40 42 44 46 48 50 52 54 56 58 60` nm, 2nm steps. Five historical IVSN depths are 36/41/48/54/60 (41 also retained off-grid). **9 incremental 300K IVSN conditions if reusing 36/48/54/60**: `38 40 42 44 46 50 52 56 58` nm.
3. **Bounded local resolution**: 42–56nm at 1nm steps only after coarse results and solver numerical equivalence warrant it.
4. **Follow-on**: compare only selected MEB at 233/300/340/380K with matched cell, C_eff and direct Hold/Write/Read checks; cold validation not assumed.
5. All 24–48nm historical 300K 3D transistor evidence may help select extra depths but must retain exact branch/mesh/bias/physics provenance; do not blindly attach new absolute 1T1C results.

## 4. Interpretive caveats and handoff

- `Hurkx ON−OFF` is a terminal model excess at VG −0.7/Vd1.2, *not* storage-node discharge current.
- `t_est` derives from direct IVSN under assumed C=10fF; mesh scaling, Ceff, temperature physics and actual 0.8V crossing unverified.
- Historical 2D `P1=41`, `P2=48`, `49 challenger` remain valid in their own legacy scope; do not reclassify as 3D optimum.
- Even if relative filters intersect numerically, absolute chip-level specs, write/read pass, process variation, RC and production retention must be established before claiming a useful robust design range.
- This plan authorizes **no new runs automatically**. Prioritize four Hold recovery points + grid/physics/C_eff QC before additional 300K IVSN depth matrix.

Evidence: [Nov-11 IVSN/Hold analysis](3d_1t1c_ivsn_hold_analysis_20261111.md). 
