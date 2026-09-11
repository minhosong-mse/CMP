# First-presentation E-field / BTBT feedback dataset — 2026-09-11

This folder contains standardized post-processing data for the 31/36/41 nm feedback-validation set.

- `btbt_profiles_31_36_41.csv`: all exported hotspot-following Band2BandGeneration profile points.
- `abse_profiles_31_36_41.csv`: all exported hotspot-following `Abs(ElectricField-V)` profile points.
- `ex_profiles_31_36_41.csv`: all exported hotspot-following `ElectricField-X` profile points.
- `efield_btbt_validation_summary.csv`: consolidated scalar results, hotspot coordinates, active widths, integrals, and ROI margins.
- `btbt_threshold_sensitivity.csv`: 10/20/50% active-region sensitivity results.

Source condition: Mesh_Code 3, 300 K, VD=1.2 V, final VG=-0.7 V, NonlocalPath ON.

The original SVisual exports used dataset labels `n36_des`, `n35_des`, and `n37_des`; these labels are SWB node/dataset names and should not be interpreted as MEB depth. The standardized files map them to the formal MEB values 31, 36, and 41 nm according to the executed Run 4/5 matrix.
