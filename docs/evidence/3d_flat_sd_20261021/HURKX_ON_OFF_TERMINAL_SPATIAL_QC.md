# 2026-10-21 Flat-S/D Mesh A Hurkx ON/OFF: execution and spatial QC

**Status:** native SDevice ON/OFF endpoint and carrier-current separation numerically verified; physical leakage-source attribution remains conditional.

- Native source: `B0_3D_highneg/pp47_des.cmd` + `n41_msh.tdr`, T-2022.03. Same mesh SHA, same 205 gate voltage coordinates, both run status 0. Only Hurkx model term removed for OFF, with absolute Grid reference in isolated output directory. No frozen parameters modified.
- Final Vd=1.2V, Vg=-1V; signed drain current ON +9.13930068118819e-14 A, OFF +5.37371375833755e-15 A. ΔId=+8.601929305354435e-14 A, 94.1202134104% decrease from ON. Drain electron current ON +8.60241285526872e-14 A, OFF +9.34658584575121e-21 A; hole currents ~+5.37e-15 A nearly unchanged. Final |4-terminal KCL| ON 8.83524e-29 A, OFF 3.15544e-30 A.
- Original SDevice Mesh A n47 final Id +9.13930067836956e-14 A; new ON final Id +9.13930068118819e-14 A, difference ~2.82e-23 A.
- 3D SVisual TDR ON/OFF fixed-cut: 12 lines each, 843 coordinate/doping-matched samples; max ON/OFF |E| sample difference 0.1 V/cm; OFF signed BTBT sample/ROI maxima 0, ON localized >0. `Abs(ElectricField-V)` (not nonexistent `Abs(ElectricField)`) is the runtime field.
- SDE PP-CMD `pp41_dvs.cmd` and `n41_dvs.out` show `P.Drain=(+60,0,-25) nm`, `sdegeo:set-contact(find-face-id(P.Drain),"drain")`, and face ID **91**. SVisual `n41_bnd.tdr` opened. Peak at (+60,+7.5,-48) nm is on outer drain boundary; no verified Face 91 element membership yet.
- **NOT demonstrated:** entire Id being GIDL, contact-independent finite-domain field, signed full-volume ON/OFF BTBT q-integrals, absolute convergence, MEB optimum or retention. Negative-generation and current collection partition must be preserved. Follow D-052 selected-point mesh policy.
