# 2026-11-23 — 3D BCAT MEB × T × RunMode numerical extraction complete

**Status: DATA ACQUISITION COMPLETE / CMP-EXECUTED / SCIENTIFIC-PROVISIONAL.** This is a source-provenance-preserving numerical completion of the `3D-Sun-SADDLE-V1 / Flat upper S/D` 24–60 nm MEB × four temperature × five RunMode sweep. **No final design conclusion, physical-retention validation, optimization or global freeze is claimed.**

## Final source and counts

- Last native external input: `CMP_MAIN_MEB53_R1_FINAL_NOV23_20261123_220510.zip`, SHA256 `3be0f42ee8f4025cabcd8ee2af766bd682938fe9a63f839235755e47ffe14e32`.
- 214 ZIP entries; integrity clean, 31 selected mappings (includes ten older R1 and 17 non-executed placeholders). Only **three** newly recovered `CMP_eeeeeeee_53` 53 nm cases were imported. Existing 17 valid MEB53 cases were left unchanged.
- R1 mode-1 MEB53 / 358.15 K / n39: VD 1.2 V and VG 2.0 V; 446 native PLT data points.
- R1 mode-5 MEB53 / 358.15 K / n40: VD 1.2 V and VG −0.7 V; 446 native PLT data points.
- R1 mode-7 MEB53 / 368.15 K / n47: VSN 0.8 → 1.0 V, 101 points; native circuit current directions and terminal conditions checked.
- All three PP SDE/source trees and SDevice mode-specific executed scripts match previous SDE lineage and accepted numerical-only R1 executed references (after parameter/node normalization). The original 53 nm incomplete traces remain in the immutable [36-depth checkpoint](../../data/3d_meb_jedec_36depth_20261123/README.md). Exactly **three** formerly RERUN unique keys become PASS; all other accepted cases are preserved.

## Summary of complete verified numerical data

| Item | Completed |
|---|---:|
| Distinct MEB depths (24 to 60 nm inclusive) | **37/37** |
| Four temperatures × five modes per MEB | **20/20** |
| Unique source-mapped SDevice endpoints | **740/740** |
| Numerically terminal-complete endpoints | **740/740** |
| Complete MEB×temperature metric rows | **148/148** |
| Total separate numerical-only R1 recovered original failures | **19** (11 earlier + 5 MEB35 export + last 3) |
| Unresolved original failed keys in canonical latest master | **0** |
| Cold 233.15 K low-current IVSN relative KCL warnings | **25** |

The latest canonical master lives at [37-depth complete data](../../data/3d_meb_jedec_37depth_complete_20261123/README.md) with [source manifest](../../data/3d_meb_jedec_37depth_complete_20261123/SOURCE_MANIFEST.md). The final new MEB53-specific metric patch sets at 358.15 K `Ion=3.55437142929763e-06 A`, `Ioff=3.0872777115181e-13 A`, `SS=96.9063776395741 mV/dec`; DIBL and Hurkx excess were recomputed from the previously accepted Mode0/Mode6 and new Mode1/Mode5, respectively. At 368.15 K `t_est=0.00364930797877905 s` is the assumed 10 fF integral and must not be reported as measured retention.

Incremental curves now actually copied to GitHub: **2,607+1,618+1,503+446 = 6,174 DC** and **505+404+303+101 = 1,313 IVSN** numeric rows. Older raw and processed curve archives remain in earlier checkpoint folders (not duplicated). Native original SWB ZIP/TDR/log artifacts are **external** per D-005; the GitHub file listing does not claim to host the complete native binary files. The CSV audit `validate_37depth_complete.py` checks internal integrity, not physical truth.

## Explicit boundary between next stages

**Completed now:** execution coverage, successful native endpoint checks, six-metric table and source traceability for the fixed 740-case campaign. No new TCAD simulations are required merely to fill missing scheduled sweep nodes.

**Not completed, reserved for later approved analysis:** physical interpretation, temperature-graded/design-range screening, calibrated 1T1C Write/Hold/Read, actual DRAM retention, mesh/grid equivalence convergence study, SRH/BTBT decomposition and literature-aligned final claims. Current archive is not a scientific optimum/production freeze. Maintain relative interpretation and the documented 25 cold IVSN warnings.

**Next first action:** when authorized, analyze the full 148-row six-metric master for consistent temperature-dependent relative design screening and determine whether additional physical validation is necessary. Do not silently change physics/mesh/source to force a conclusion.

Historical 18/21/33/34/35/36/37-depth checkpoints, root README and original failures are intentionally preserved.
