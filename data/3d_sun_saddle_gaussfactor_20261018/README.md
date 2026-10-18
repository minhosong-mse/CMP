# 3D-Sun-SADDLE-V1 M1 GaussFactor: SDE + three-bias DC evidence (2026-10-18)

**PROVISIONAL; no baseline freeze.** Five-factor 3D Gaussian *lateral* S/D dopant-spread implementation test at unchanged ARgate6 / DBCAT36 nm / JunctionRatio0.4 / Wfin17 nm / RfilletFactor1 / T300K. `GaussFactor` is a CMP reconstruction assumption; its published literal value has not been established.

- Full research record: [GaussFactor checkpoint](../../docs/progress/3d_sun_saddle_v1_gaussfactor_20261018.md).
- `DC_METRICS_5FACTOR.csv`: threshold, SS, DIBL, ON/OFF terminal current, inclusion/exclusion, both linear-vs-log interpolation methods, with missing endpoints blank.
- `RUN_STATUS_15_NODES.csv`: 15 bias-node provenance/status, solver threads, walltime, collected gate-point counts and last reached Vg. 12/15 reached target.
- `MESH_COMPARISON_5FACTOR.csv`: SDE point/tetra count, unresolved minimum mesh edge.
- `SOURCE_MANIFEST.csv`: hashes of the **separately preserved conversation-source ZIPs**; uploaded unredacted server logs and full raw PLT not republished here due host/license/user-machine paths and archive size.
- Three SWB SDevice source templates in `code/sdevice/3d_sun_saddle_v1/GF_IDVG_*.cmd` and SDE Gaussian split source in `code/sde/3d_sun_saddle_v1/SDE_M1_GAUSSFACTOR_SPLIT.cmd` (derived from same executed M1 parents).

**Reproduction conventions:** LOG-current Vth first threshold crossing at `8.5e−8 A`; SS monotonic `1e−12..1e−9 A`; DIBL (0.05 vs 1.2 V); indicative Ion/Ioff `Vg=2/-1`, `Vd=1.2`. All currents are 3D terminal A, not A/µm; paper normalization definition not yet matched.

**Source traceability:** The original uploaded 424-entry CORE ZIP contains `GF_IDVG_*_n*_des.plt`, node logs, preprocessed SDevice commands and SWB status; its SHA256 is recorded in `SOURCE_MANIFEST.csv`. An offline analysis package also contains the complete 1550-point extracted CSV and seven figures, but it is NOT stored in this Git commit. Don't substitute these summary tables for actual executed PLT if revalidation needs full points.

**Scientific gate:** mesh/topology repair and matched-bias 3D E-field + BTBT spatial/volume-integrated validation before claiming GIDL or paper Vth/Ion/Ioff reproduction; GF0 nominal remains reference, not final adopted physical calibration.
