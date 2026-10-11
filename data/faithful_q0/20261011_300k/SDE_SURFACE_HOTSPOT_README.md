# Faithful-Q0 / Phase 1 near-surface hotspot targeted mesh (SDE only)

**Parent:** user-executed `CMP_FAITHFUL_Q0_ALL15_4PROJECTS_EVIDENCE.zip` → `raw/on_spatial/sde_dvs.cmd`. On-terminal and OFF-terminal copies are byte-identical.

**Modification:** two additional SDE local `Ref/Eval` windows `Q0SurfaceOuter/Core`, around *observed* Faithful-Q0 near-surface hotspot X=0.002343750 um, Y=0.266250014 um (MEB 33..51 nm). All previous GIDL windows follow MEB and remain untouched; **no geometry, doping, contact, physical model, Qf, bias, temperature or SVisual edits**.

At Q0 geometry YoxR=0.255 um, YdL=0.270 um, and default `SurfaceRefineLevel=1`:
- OUTER X=0..0.015 um; Y=0.258..0.276 um; max 1.5×1.0 nm; min 0.35×0.25 nm.
- CORE X=0..0.008 um; Y=0.263..0.270 um; max 0.65×0.40 nm; min 0.18×0.12 nm.

`SurfaceRefineLevel=2` optional refinement: OUTER max 1.2×0.8 nm/min 0.30×0.20 nm; CORE max 0.55×0.35 nm/min 0.18×0.12 nm. This is a **targeted mesh-policy change**; results must be labeled independently from original Atlas-L2 and not silently pooled.

## SWB procedure

1. Duplicate the existing Q0 ON-terminal, ON-spatial, and OFF-terminal projects, keeping the MEB, SDevice and SVisual settings unchanged. **Do not overwrite the validated original projects.**
2. Replace ONLY SDE with `CMP_FAITHFUL_Q0_GIDL_SDE_SURFACE_HOTSPOT_PHASE1.cmd` in **all three** project graphs. ON and OFF must use exactly the same updated mesh definition.
3. Run **MEBDepth=0.036 um first** in all three graphs. Inspect generated `n*_msh.cmd`, `n*_msh.log`, mesh/TDR to confirm the new windows appear and actually cover the hotspot. SDE 'done' alone does not verify generated mesh density.
4. Run existing 300 K Hurkx ON, BTBT-OFF and spatial SVisual unchanged. Recover signed drain currents, KCL, BTBTmax, Xhot/Yhot, E@BTBT, whole-Si BTBT integral, 20%-active area, and cutline diagnostics.
5. Compare existing original Q0 Atlas-L2 vs new Level-1 and, if stable enough, Level-2 optional. If using Level 2, edit only `(define SurfaceRefineLevel 1)` → `(define SurfaceRefineLevel 2)` in **all three SDE copies**, then execute a separately labeled copy. Keep geometry and physics fixed.
6. If 36 nm validates, extend to 41 and 48 nm. **31 nm is a distinct hotspot (X≈0.02930 um)** and this near-surface box intentionally does not cover it; do not claim 31-nm convergence without its own ROI audit.

## Intended diagnostics / limitations

- Static Scheme parentheses and command pattern validated against the *executed* Q0 SDE and SDE T-2022.03 manual local refinement syntax; **Sentaurus run/convergence NOT tested here**.
- Existing `Ycut` does not necessarily pass the near-surface hotspot; global-Si integral and moving hotspot are primary. Fixed-cut comparisons must be physically qualified.
- Even perfect mesh convergence does not prove PAPER-CAL and Q0 have the same BTBT mechanism. The ON/OFF cancellation and q×∫BTBT-to-terminal discrepancy are separate Phase 2 investigations.

Original SDE SHA256: `4e3f83d0df4fa60d25bd53e098576dad83607e1d2a2f8a24b33c5f58c3dd65eb`
Modified SDE SHA256: `27ddaaabe1c7ab399e6c3efb9215d87e8e485bcc97c69e697fb5b7e1f232c169`