# Mesh A 3D Hurkx controlled-run protocol (2026-10-21)

User-executed source bundle: `CMP_3D_HURKX_AB_CONTROL_20261021.zip` (SHA256 in [evidence manifest](../../../../data/3d_sun_flat_sd_hurkx_20261021/native_archive_sha256.csv)). Original executable source remains in that user archive, including `prepare_hurkx_ab.py`, `run_one_case.sh`, `export_one_plt.sh`, `export_terminal_plt.tcl`, and `collect_hurkx_results.py`.

1. Before using the archived scripts, confirm real `B0_3D_highneg/pp47_des.cmd` and exact `n41_msh.tdr` file. Verifier demands T300K, WF4.8eV, Vd1.2V, Vg-1.0V, Source/Drain/Gate/Substrate, and exactly one `Recombination(Band2Band(Hurkx))` in the PP deck.
2. Prepare isolated `CMP_3D_HURKX_AB_20261021_RUN/ON` and `OFF` with `prepare_hurkx_ab.py`. Each `cmp_highneg.cmd` retains the same solver, geometry/mesh, bias ramp; `Grid` path is absolutized for separate directories; OFF deletes exactly one Hurkx clause.
3. Run `bash run_one_case.sh ... ON` then `... OFF` one by one; executable refuses overwriting previous outputs.
4. Require `sdevice_exit_status=0`, Vg-1.0 endpoint, 205 matched gate samples, signed four-terminal KCL and correct carrier components before comparing.
5. Extract both final native `n47_QC_D2_NEG_VG_0002_des.tdr` using user-executed `CMP_3D_EFIELD_BTBT_BOUNDARY_AUDIT_V2_PATCH.zip` (with Python3.8 `.removesuffix('.csv')` -> `[:-4]` compatibility fix). SVisual field name is **`Abs(ElectricField-V)`**.
6. Source evidence stays external due to size; compact derived numerical tables under [data](../../../../data/3d_sun_flat_sd_hurkx_20261021/). Do not equate `ΔId` to terminal-collected pure GIDL and do not characterize Face 91 peak membership as proven.

The code in this directory is intended for documentation/replay; no additional Sentaurus jobs were launched by the GitHub close-out.

**Implementation note:** checked-in `prepare_hurkx_ab.py` is a post-run replay-safe variant of the user-executed archive script: it additionally recognizes `pp41_dvs.cmd`/`n41_dvs.cmd` and corrects the contact-probe key name. This variant was **not** the file used for the original ON/OFF numerical execution; exact user-executed script is identified by the external control ZIP SHA256.
