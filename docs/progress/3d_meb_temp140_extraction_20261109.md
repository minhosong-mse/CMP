# 2026-11-09 — Independent 3D MEB × Temperature extraction checkpoint (138/140)

> **Status: CMP-EXECUTED / EXTRACTION-PARTIAL-QC-PASSED / SCIENTIFIC-PROVISIONAL.** User-uploaded numerical review archive compared five 3D working-baseline MEB depths (36/41/48/54/60nm) at four temperatures (233/300/340/380K) and seven modes (0..6). Original SDevice simulations were executed on the external Linux server, not by this GitHub synchronization task.

## Numerical QC and source identity

- 140/140 preprocessed mapping, from 105 temperature SWB cases and 35 separately sourced 300K baseline cases. **138** target endpoint complete, **2** native incomplete sweeps, plus 552 valid spatial ROI summaries, 3864 raw scalar records, 552 cutlines and 138 per-case field inventories.
- Incomplete: `36nm/380K/Mode5/n1979` ended at Vg −0.66372928V instead of −0.7V (native solver `Newton didn't converge; Step-size less than MinStep`); `54nm/340K/Mode1/n1686` ended at Vg +0.108366V instead of +2.0V (solver cause not independently established). Retain both raw curves as **partial-only evidence**; never fill the missing endpoint or call them PASS.
- Source SDE preprocessed identities and normalized SDevice PP comparisons are described in the accompanying analysis report. This does not substitute for byte-identical grid TDR verification, 3D mesh convergence, or full contact/edge attribution.
- Data: [`data/3d_meb_temp140_partial_20261109/`](../../data/3d_meb_temp140_partial_20261109/). [`README.md`](../../data/3d_meb_temp140_partial_20261109/README.md) holds original review ZIP SHA-256, D-005 external native-storage policy, public source mapping, and a per-artifact SHA manifest. Code: [`code/scripts/analysis/3d_temp140_20261109/`](../../code/scripts/analysis/3d_temp140_20261109/). Analysis: [`docs/evidence/3d_meb_temp140_analysis_20261109.md`](../evidence/3d_meb_temp140_analysis_20261109.md).

## Preliminary observation, not mechanism/retention proof

- Within this working 3D model, increasing MEB depth generally decreases matched Hurkx ON−OFF terminal excess; Ion and DIBL worsen with increasing depth. High-temperature Vg=0 off-state current shows a smaller MEB dependence than model-internal Hurkx excess.
- Mode-5 Gate–Drain vs Outer–Drain positive BTBT-generation fraction crossover shifts with temperature (approx. 41nm at 300K, between 48–54nm at 233K, between 36–41nm at 340K). Outer boundary x≈60nm remains suspect; these are geometric ROI fractions, not proven collected GIDL components.
- 48nm is a comparative reference, **not a frozen optimum**. GIDL and spatial BTBT model outputs cannot be automatically converted to VSN current or t_ret.

## Next first actions

1. Re-run ONLY `n1979` and `n1686` using a minimum, version-verified solver/continuation change and preserve original provenance. Do not mix partial values into the endpoint-complete matrices.
2. Complete source-project native grid/physics verification, outer-drain x≈60nm Face91/contact attribution and selected mesh sensitivity, especially at high-temperature bias.
3. Move to a separate 3D 1T1C SN-current-versus-VSN hold protocol; start VSN=1V and integrate 1.0→0.8V with correct 3D capacitance/current scaling before calling anything a retention time.
