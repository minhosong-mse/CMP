# 2026-11-21 — Six-metric MEB × temperature extraction checkpoint

**State: PARTIAL / SCIENTIFIC-PROVISIONAL.** User-provided external exports from Nov-19 and Nov-21 are archived as numerical CSVs; no new solver runs during extraction.

- Nov-19: 24/30/31/36/37/44/49/50/55 nm, 172/180 valid.
- Nov-21 main account: 25/32/33/38/45/51/56 nm, 139/140 valid.
- Nov-21 other account: 28/29 nm, 40/40 valid.
- Cumulative: 18/37 depths exported, 351/740 full-grid jobs and 351/360 exported jobs endpoint-complete. 65/72 MEB×T rows complete across five modes, all 18 sampled 300 K rows complete. Ten cold IVSN warnings retained.
- Actual T=233.15/300/358.15/368.15 K, no 340 K. Keep older 233/300/340/380 K IVSN campaign separate; do not fill gaps from historical files.

**Next:** inspect external SWB queue and export missing depths first, then selectively recover incomplete/missing nodes; 380+9 target jobs remain unverified. Use [exact node list and evidence](../evidence/3d_meb_jedec_18depth_qc_20261121.md). Then merge comparable data, perform six-metric design-range screening and evaluate spatial transport evidence if needed. Maintain frozen geometry and physical-model lineage, defer additional validation as agreed; no final optimum or physical retention claim.

[Data archive](../../data/3d_meb_jedec_18depth_20261121/README.md) · [Extraction source](../../code/scripts/analysis/3d_meb_jedec_20261121/qc_nov21.py).
