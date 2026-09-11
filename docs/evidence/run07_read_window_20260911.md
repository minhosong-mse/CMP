# R7 Evidence — Independent D0/D1 Charge-Sharing Read Window

## Purpose
Verify that the 1T1C circuit can distinguish stored D0 and D1 states through bitline charge sharing.

## Circuit / bias
- AreaFactor: 0.017
- Ccell: 10 fF
- CBL: 45 fF
- BL precharge: 0.5 V
- WL OFF: -0.7 V
- WL READ: 3.0 V
- Read pulse: 10 ns
- D0 VSN_INIT: 0 V
- D1 VSN_INIT: 0.9481 V

D1 VSN_INIT is mapped from the prior write-screen result near the strongest screened D1 condition.

## Results

| state | VSN init [V] | VBL init [V] | VSN final [V] | VBL final [V] | Delta VSN | Delta VBL | capacitor-charge error |
|---|---:|---:|---:|---:|---:|---:|---:|
| D0 (n136) | 0.000000 | 0.500000 | 0.324409 | 0.427884 | +324.41 mV | -72.12 mV | -0.0051% |
| D1 (n138) | 0.948100 | 0.500000 | 0.810658 | 0.530553 | -137.44 mV | +30.55 mV | +0.0014% |

D0/D1 final bitline separation:

`Delta VBL_window = VBL_D1 - VBL_D0 = 0.102669 V = 102.67 mV`

## Interpretation
- D0 drives BL downward by approximately 72.12 mV.
- D1 drives BL upward by approximately 30.55 mV.
- The final separation is approximately 102.67 mV.
- Capacitor-charge balance error is below 0.01%, supporting charge sharing as the dominant mechanism.

## Claim boundary
This is **independent read feasibility**, not yet `Read-after-Hold` and not a retention-time measurement.

Processed source:

- `data/run07/processed/read_window.csv`
