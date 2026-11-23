# MEB 53 nm — selective numerical recovery R1 (2026-11-23)

**Status: PREPARED / PLANNED, NOT YET EXECUTED OR CONVERGENCE-VALIDATED.**

This is a **three-node-only** recovery plan for the existing `3D-Sun-SADDLE-V1 / Flat upper S/D` 36-depth campaign. It does not modify, replace or supersede the source-mapped original failures, nor does it upgrade the scientific state of the sweep.

## Fixed provenance and scope

- Account: **MAIN**.
- Original SWB project: `CMP_3D_Temp_49-60_Copy_Copy`.
- Original MEB 53 nm SDE/mesh grid node: **3166**; newly copied SWB project may assign different node IDs.
- Physics, geometry, mesh, Hurkx mode policy, 4.8 eV gate workfunction, original temperatures, bias endpoints, and output definitions **remain unchanged**.
- Use the numerical-only parent [Recovery R1](../../code/sdevice/3d_sun_saddle_v1/CMP_3D_JEDEC_RECOVERY_R1_des.cmd); the [53 nm source](../../code/sdevice/3d_sun_saddle_v1/CMP_MEB53_R1_ONLY_des.cmd) has **the identical executable body**, only a 53 nm-specific comment header.
- Original R1 SHA-256: `c0ee12be0d25c6c399dab6ea5d20248e1cb34de3c4b8faa128bb4f2d314d6e44`; dedicated CMD SHA-256: `a58eac8aa1f33af310bc77b51c7a452372bc3f5f61df1284246a0aaceaa5dc37`. Reassembled parent header + dedicated executable body reproduces the original R1 SHA.

## Only the following three targets

| MEB nm | Temp K | RunMode | Original SDevice node | Observed stopped bias | Required terminal condition |
|---:|---:|---:|---:|---|---|
| 53 | 358.15 | 1 | 3182 | VD = 0.888653 V; VG = 0.001423 V | VD = 1.2 V; VG = 2.0 V |
| 53 | 358.15 | 5 | 3183 | VD = 0.879653 V; VG = 0 V | VD = 1.2 V; VG = −0.7 V |
| 53 | 368.15 | 7 | 3191 | VSN = 0.806 V; only 4 samples | VSN = 0.8–1.0 V; exactly 101 samples |

The associated machine-readable [run sheet](3d_meb53_r1_run_sheet_20261123.csv) preserves the original project/IDs. These failures are **Newton nonconvergence / step below MinStep** in the original solver logs. The `Done` state does not guarantee complete bias sweep. No valid alternate completion was present in the native 53 nm export.

## SWB run instructions

1. On the main Linux account, **copy** `CMP_3D_Temp_49-60_Copy_Copy` to an isolated project (suggested: `CMP_MEB53_R1_ONLY`). Never overwrite the executed source or its PP results.
2. In the **copied project**, replace the SDevice **source** .cmd with [CMP_MEB53_R1_ONLY_des.cmd](../../code/sdevice/3d_sun_saddle_v1/CMP_MEB53_R1_ONLY_des.cmd). Do **not** edit generated `pp3182_des.cmd`, `pp3183_des.cmd` or `pp3191_des.cmd`.
3. Select exactly three MEB=53 node conditions above. Preprocess these SDevice nodes. Check their new grid links to the 53 nm SDE; node IDs need not remain 3182/3183/3191.
4. Optionally check static source configuration after preprocessing:

   ```bash
   python3 cmp_meb53_r1_preflight.py /path/to/CMP_MEB53_R1_ONLY
   ```

   The [preflight script](../../code/scripts/analysis/3d_meb_jedec_20261123/cmp_meb53_r1_preflight.py) checks SWB tree, grid/SDE depth, temperature, physics, numerical controls and exact three selected conditions. **Preflight PASS is not proof of solver convergence.**
5. Run only the three SDevice nodes. Prefer Mode 1 and 5 first, then Mode 7. Require native `pp*_des.cmd`, `n*_des.log`, `n*_des.sta`, result PLTs and `gtree.dat` for post-run verification.
6. Inspect real PLT terminal endpoints and solver logs, not `Done` alone. Mode 7 also requires 101-point `VSN=0.8..1.0`, expected current signs and KCL QA.
7. Export using:

   ```bash
   cd ~
   python3 cmp_swb_export_v3.py --account MAIN --depths 53 --tag CMP_MAIN_MEB53_R1
   ```

   The exporter can prefer an older project copy. Inspect `NODE_MAPPING.csv` / `CANDIDATES.csv` for the **new R1 nodes**. If the new nodes were omitted, preserve their PP/log/sta/PLT, mesh-SDE PP and `gtree.dat` as a **separate native ZIP** instead of falsely accepting an old partial curve.

## R1 continuation preserved

- Modes 1, 5: `InitialStep=1.0e-4`, `Increment=1.15`, `MinStep=1.0e-9`, `MaxStep=5.0e-3`, `Extrapolate(MinStep=1.0e-5)`, `Coupled(Iterations=80)`.
- Mode 7: first ramp to 0.8 V `InitialStep=1e-4`, second ramp 0.8–1.0 V `InitialStep=2.5e-4`; `MinStep=1e-12`, `MaxStep=0.005`, `Extrapolate(MinStep=1e-6)`, retained `CurrentPlot(...Intervals=100)`.
- Mode 7 circuit keeps assumed `Ccell=1e-14 F` and `WL=-0.7 V`; this is not a physical retention experiment.

## What remains unchanged

**36/37 MEB depths exported; 712/720 endpoint-complete; 8 incomplete existing endpoints; MEB 35 nm remains unexported (20 conditions).** These three 53 nm outcomes remain **RERUN / UNVERIFIED** until external SWB results have been received and independently checked. All earlier QC/metric CSVs and the root README remain immutable. No production optimum, true GIDL separation, or physical 1T1C retention claim is made.

Source: [36-depth checkpoint](3d_meb_jedec_36depth_checkpoint_20261123.md); [canonical eight failed targets](../../data/3d_meb_jedec_36depth_20261123/remaining_reruns.csv).
