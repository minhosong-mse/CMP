# 2026-11-22 — 21-depth BCAT DOE checkpoint

**PARTIAL / SCIENTIFIC-PROVISIONAL.** User supplied main-account 60 nm and other-account 48/59 nm exports and supplemental SDE PP files. No new local Sentaurus execution, calibration, or model change.

| MEB (nm) | 233.15 K | 300 K | 358.15 K | 368.15 K | Endpoint PASS |
|---:|---:|---:|---:|---:|---:|
| 48 | 5/5 | 5/5 | 5/5 | 4/5 | 19/20 |
| 59 | 5/5 | 5/5 | 5/5 | 5/5 | 20/20 |
| 60 | 5/5 | 5/5 | 4/5 | 5/5 | 19/20 |

58/60 new endpoints satisfy native PLT target, finite data, log/status, SWB tree, PP SDE and SDevice checks. 48 nm duplicates deduplicated. Cumulative 409/420 sampled (55.27% of all 740 planned jobs), 21/37 depths, 75/84 complete five-mode conditions, all 21 sampled 300 K conditions complete. Metric availability: Ion/Ioff/SS/DIBL 77 each, signed Hurkx excess 83, 10 fF IVSN estimates 81. Three added 233.15 K IVSN residual warnings (48: 8.70%, 59: 6.78%, 60: 2.37%); cumulative 13, maximum 14.84%. These warnings are not unqualified physical passes.

## New incomplete cases

- 60 nm / 358.15 K / mode 1: CMP_3D_Temp_49-60_Copy_Copy / n3364, Vg=0.0281151 V instead of 2 V. SWB reported done; log shows Newton nonconvergence and step below MinStep.
- 48 nm / 368.15 K / mode 7: CMP_final / n339, VSN=0.856 V instead of 1 V. Step below MinStep; failed status. CMP_final_Copy2 is the same source, not a second failed physical case.

At 300 K, 48/59/60 nm respectively have Ion 3.53268/3.20860/3.16964 µA, SS 80.2004/82.9551/83.3460 mV/dec, and assumed 10 fF IVSN estimates 177.004/228.008/233.837 ms. Numerical provisional outcomes only, not calibrated retention.

## Next action

Collect remaining 16 depths: 26/27/34/35/39/40/41/42/43/46/47/52/53/54/57/58 nm (320 targets). Recover only the 11 missing/incomplete sampled endpoints (check pending jobs before rerun). Await user-provided external solver outputs; do not overwrite existing valid cases. The full campaign has 331 not-yet-valid targets. Then finish six-metric and temperature-specific design screening.

Data and source hashes: [21-depth archive](../../data/3d_meb_jedec_21depth_20261122/README.md). Parent 18-depth archive remains immutable.
