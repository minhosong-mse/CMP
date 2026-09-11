# R7 Evidence — Write Screen (AF=0.017)

## Purpose
Verify 1T1C D1 write feasibility and identify a preliminary write condition for downstream Hold/Read feasibility.

## Fixed conditions
- B0 MEB depth: 36 nm
- Temperature: 300 K
- AreaFactor: 0.017
- Ccell: 10 fF
- VBL_WRITE: 1.2 V
- VWL_HOLD: -0.7 V

## Results

| node | VWL_ON [V] | Twrite [ns] | VSN_final [V] |
|---:|---:|---:|---:|
| 182 | 1.5 | 100 | 0.157485 |
| 183 | 2.0 | 100 | 0.428389 |
| 184 | 2.5 | 100 | 0.675346 |
| 185 | 3.0 | 100 | 0.866426 |
| 194 | 1.5 | 200 | 0.190966 |
| 195 | 2.0 | 200 | 0.469623 |
| 196 | 2.5 | 200 | 0.723916 |
| 197 | 3.0 | 200 | 0.919497 |
| 206 | 1.5 | 300 | 0.209947 |
| 207 | 2.0 | 300 | 0.492115 |
| 208 | 2.5 | 300 | 0.750794 |
| 209 | 3.0 | 300 | 0.948118 |

## Result
VSN increases monotonically with both VWL_ON and Twrite. The maximum screened value is **0.948118 V** at 3.0 V / 300 ns.

This establishes **write feasibility**, but not a final write-condition freeze because the working literature-compatible 1.0 V initial state was not reached within this screen.

Processed source:

- `data/run07/processed/write_screen_af0017.csv`
