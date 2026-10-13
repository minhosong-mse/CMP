# NonlocalPath pilot data checkpoint — 2026-10-13/14

**Status:** OFF six selected depths source-QC PASSED; ON 36/39 nm are screenshot-derived hotspot observations **only**. No mesh convergence, whole-Si generation integral or final model selection.

- `off_6_qc.csv`: independently reviewed OFF final terminal currents from user-provided ZIP `CMP_NONLOCAL_OFF_6_EVIDENCE.zip`; archive SHA256 `086d50fadc4a271728030b42000aac62015ea77562c3bc1fbcecc3b1f6fe1e92`; 104/104 source-file hash/length PASS. ZIP is **not** stored here; archive remains in the conversation and user's source environment.
- `on_2_hotspot_svisual.csv`: selected Silicon full-domain `Band2BandGeneration` maxima transcribed from user screenshots at 36 and 39 nm; screenshots themselves are **not** stored here and exact ON pp-CMD/log/TDR are pending. SHA256 values of original uploaded PNGs recorded row-wise.
- **Selected OFF MEBs:** 31/36/39/41/**46**/51 nm (48 nm was not one of the six).
- **Never attribute old Atlas OFF-vs-pilot OFF differences to BTBT model choice:** both have BTBT off and differ by ~2.39–3.80x. Historical Atlas results remain in `../paper_cal/atlas_300k_20261008/`.
- Detailed research context and next-step gates: [2026-10-14 checkpoint](../../docs/progress/nonlocalpath_hotspot_pilot_checkpoint_20261014.md).

No original evidence, 2026-10-08 validated master, or frozen calibration files were modified.
