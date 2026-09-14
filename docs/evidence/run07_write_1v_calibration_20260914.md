# Run 07A — 1 V Write Calibration Freeze

Status: **PASS — 300 K representative write condition frozen for the next retention stages**.

## Condition

```text
MEB_Depth = 0.036 um
Mesh_Code = 1
Temperature = 300 K
AreaFactor = 0.017
Ccell = 10 fF
VBL_WRITE = 1.2 V
VWL_ON = 3.0 V
VWL_HOLD = -0.7 V
Twrite = 667 ns
Thold = 100 ns
```

The storage node is initialized with `Set(sn=0)` and released by `Unset(sn)` before the transient.

## Result

The accepted Hold-start point is the first sample after both BL and WL complete the write-to-hold switching and are settled at BL=0 V and WL=-0.7 V.

```text
VSN_hold_start = 1.00001464973547 V
VSN_hold_end   = 1.00001464946294 V
DeltaVSN_100ns = 2.72529998568416e-10 V
Error vs 1 V   = +14.65 uV
Relative error = +0.001465 %
```

Therefore the practical 300 K reference write condition is frozen as:

```text
AreaFactor = 0.017
Twrite = 667 ns
VSN_start ~= 1.000015 V
```

This value is an executed TCAD point, not only the prior 650/675 ns linear interpolation.

## Interpretation / claim boundary

- The result closes the Run-7A write-time calibration objective for the 300 K B0 feasibility model.
- The ~100 ns floating-Hold change remains at numerical-floor scale and is not a measured retention-time number.
- The 667 ns condition is the 300 K normalization anchor for later temperature-normalized Hold and integrated Write-Hold-Read studies.
- `AreaFactor=0.017` remains an effective-width proxy, not production calibration.

## Evidence figures

- `assets/images/run07/06_r7_A_n409_write_hold_overall_667ns.svg`
- `assets/images/run07/07_r7_A_n409_vsn_write_to_1V_667ns.svg`
- `assets/images/run07/08_r7_A_n409_1V_settling_zoom_667ns.svg`

Processed result:

- `data/run07/processed/write_1v_calibration_af0017.csv`

Raw `.plt` and solver log remain in the TCAD/local archive under the repository evidence policy.
