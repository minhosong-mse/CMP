# B0-2D-PAPER-CAL — Post-Freeze Mesh Revalidation Debugging Checkpoint

> **Status:** PAUSED / PROVISIONAL  
> **Date:** 2026-10-07  
> **Target lineage:** `B0-2D-PAPER-CAL`  
> **Frozen baseline remains:** `C7_4 / B_QF_HALF`  
> **Purpose:** preserve the post-freeze mesh/debugging work without reopening or rewriting the validated C7_4/FZ-C baseline.

## 1. Canonical reference remains unchanged

The authoritative frozen result is still the 2026-10-05 C7_4 final freeze.

Frozen numerical reference:

- `Vth @0.05 V ≈ 0.682485 V`
- `Vth @1.20 V ≈ 0.65570 V`
- `SSquick @1.20 V ≈ 75.827 mV/dec`
- `DIBL 0.05→1.20 V ≈ 23.29 mV/V`

Frozen FZ-C nominal GIDL convergence:

| Metric | Mesh1 | Mesh2 | Mesh1→2 |
|---|---:|---:|---:|
| GIDL | 5.8010e-13 | 5.8256e-13 | +0.424% |
| BTBTmax | 7.2656e23 | 7.2635e23 | -0.029% |
| E@BTBT | 1.1232e6 | 1.1423e6 | +1.69% |
| Xhot | 0.034570 um | 0.034863 um | +0.293 nm |
| Yhot | 0.252174 um | 0.252174 um | 0 nm |

Therefore the existing policy remains in force:

- broad DC: MeshLevel 0
- broad GIDL: MeshLevel 1
- selected mechanism/final evidence: MeshLevel 2
- Rescue V2: numerical reference/fallback

This checkpoint does **not** supersede FZ-C and does **not** freeze a replacement mesh.

## 2. Why a post-freeze mesh debug branch was opened

During production-revalidation preparation, a local SDE lineage was used to rerun MEB 31/36/41 GIDL cases. Its absolute GIDL values differed strongly from the frozen nominal reference, so mesh sensitivity was initially suspected.

A later DC cross-check showed that the local deck was not a controlled mesh-only copy of the frozen C7_4 parent.

For the local lineage:

| MEB | Vth @0.05 V | Vth @1.20 V |
|---:|---:|---:|
| 31 nm | 0.663089 | 0.638179 |
| 36 nm | 0.663083 | 0.638303 |
| 41 nm | 0.663070 | 0.637991 |

At nominal 36 nm this is about **-19.4 mV** at 0.05 V and **-17.4 mV** at 1.20 V versus the frozen C7_4 reference.

**Consequence:** subsequent absolute GIDL differences from the frozen reference cannot be attributed to mesh alone. The exact geometry/calibration/deck lineage must be recovered before a production mesh A/B comparison is accepted.

## 3. Debugging sequence and status

### 3.1 Initial H1 smoke — invalid for MEB comparison

The first local H1 smoke deck contained lineage errors:

- `GateTop=0.036` was hardcoded instead of following the MEB parameter;
- `Ywidth=0.320 um` instead of the frozen 0.480-um domain;
- the corresponding hotspot Y coordinate was shifted from the frozen nominal region.

This run was useful for detecting the setup problem but is **INVALID for controlled 31/36/41 MEB comparison**.

### 3.2 Corrected local H1 lineage — executed but not a controlled bridge

After correcting the obvious MEB/domain setup, the following GIDL/spatial values were obtained:

| MEB | GIDL_End | BTBTmax | Xhot [um] | Yhot [um] | E@BTBT |
|---:|---:|---:|---:|---:|---:|
| 31 | 3.42761996e-11 | 7.02277192e22 | 0.03222656 | 0.25406250 | 9.74961288e5 |
| 36 | 7.50196348e-13 | 6.49925873e23 | 0.03632813 | 0.25217399 | 1.16177705e6 |
| 41 | 2.91753239e-13 | 1.22924905e24 | 0.04101562 | 0.25217399 | 1.12757805e6 |

All three runs reached the requested endpoint and loaded spatial output. However, the later DC check above showed that this local lineage was not numerically identical to frozen C7_4, so these absolute values remain local-debug evidence only.

### 3.3 H1.1 local refinement — nominal peak metrics stabilized faster than terminal GIDL

H1.1 changed only the local mesh within the same local-debug lineage.

| MEB | GIDL_End | BTBTmax | Xhot [um] | Yhot [um] | E@BTBT |
|---:|---:|---:|---:|---:|---:|
| 31 | 7.72003923e-12 | 2.40962030e23 | 0.03222656 | 0.25359374 | 1.02428048e6 |
| 36 | 6.07429814e-13 | 6.69025570e23 | 0.03515625 | 0.25217399 | 1.16064597e6 |
| 41 | 3.37238658e-13 | 9.77230652e23 | 0.04042969 | 0.25217399 | 1.13076432e6 |

At 36 nm, H1→H1.1 changed:

- GIDL by about **-19.0%**
- BTBTmax by about **+2.94%**
- E@BTBT by about **-0.10%**
- Xhot by about **-1.17 nm**

So the local peak-related quantities were becoming more stable while the terminal leakage was still strongly mesh-sensitive. H1.1 therefore did **not** establish mesh independence.

### 3.4 Later local refinement sequence — nominal 36 nm became stable, 31 nm did not

Several additional refinements were run before the workflow was stopped. The exact local deck filenames were not canonically mapped into GitHub, so they are preserved here only as execution sequence L1/L2/L3 rather than promoted as named project decks.

| Seq. | MEB | GIDL_End | BTBTmax | BTBTint_Si_2D proxy | Xhot [um] | Yhot [um] | E@BTBT |
|---|---:|---:|---:|---:|---:|---:|---:|
| L1 | 31 | 6.49381094e-12 | 2.67370636e23 | — | 0.03222656 | 0.25359374 | 1.02617275e6 |
| L1 | 36 | 6.05048828e-13 | 7.05805891e23 | — | 0.03515625 | 0.25217399 | 1.16207359e6 |
| L1 | 41 | 3.40303562e-13 | 9.82039169e23 | — | 0.04042969 | 0.25217399 | 1.13195380e6 |
| L2 | 31 | 5.61258459e-12 | 2.66685959e23 | 2.15015236e6 | 0.03222656 | 0.25359374 | 1.02247796e6 |
| L2 | 36 | 5.84046335e-13 | 7.29549560e23 | 3.15296392e6 | 0.03515625 | 0.25217399 | 1.15919515e6 |
| L2 | 41 | 3.30168470e-13 | 9.88911357e23 | 2.04509676e6 | 0.04042969 | 0.25217399 | 1.12947331e6 |
| L3 | 31 | 4.30171250e-12 | 3.00266584e23 | 2.40395575e6 | 0.03164063 | 0.25359374 | 1.03511102e6 |
| L3 | 36 | 5.81317032e-13 | 7.63681396e23 | 3.25124862e6 | 0.03515625 | 0.25217399 | 1.16045171e6 |
| L3 | 41 | 3.32345069e-13 | 9.88479223e23 | 2.06194710e6 | 0.04042969 | 0.25217399 | 1.13021280e6 |

Important observations:

- L2→L3 GIDL changed only about **-0.47% at 36 nm** and **+0.66% at 41 nm**.
- The same step changed 31-nm GIDL by about **-23.36%**.
- Therefore convergence at nominal 36 nm alone was not sufficient to freeze one common mesh for the full 31/36/41 comparison.
- `BTBTint_Si_2D` is kept as the session's spatial-integration proxy. No physical unit or exact current equivalence is inferred here.

The direction `31 > 36 > 41` in terminal GIDL is not itself evidence of a mesh failure. The problem is the **uncontrolled absolute shift under mesh refinement and incomplete lineage identity**, especially at the 31-nm endpoint.

### 3.5 Over-refinement / runtime failure

Two over-refinement warning points were encountered:

- an earlier global-overfine attempt grew to roughly **154k elements** and was discarded;
- a later targeted branch reached roughly **30k elements** and then failed in SDevice.

In the failed high-density branch, the inspected BTBT-related spatial fields no longer appeared in the expected drain-side location and instead appeared displaced toward the top of the structure. Because the device run failed, this was treated as a numerical/deck warning, **not** as a new physical mechanism.

The correct response was to stop rather than continue interpreting the field plot.

### 3.6 SDE-only hotspot refinement check

A later SDE-only trial intentionally kept the baseline-style mesh and tightened the BTBT region. The produced structure showed about:

- **29,011 elements**
- **14,131 points**

The structure was useful for visual mesh inspection, but it was not promoted because SDevice validation had not established controlled same-parent convergence.

### 3.7 Manual-grounded v3 draft — not executed / not canonical

A local draft named `CMP_MANUAL_OPT_MESH_SDE_v3.cmd` was prepared after consulting the T-2022.03 mesh/SDE guidance. Its design intent was:

- retain calibrated global/gate/interface refinement;
- remove the expensive full-width junction-depth band;
- keep local source/drain doping-gradient refinement;
- use one compact anisotropic drain-side BTBT window;
- apply local interface refinement only where GIDL is expected.

This draft was **not executed** and is deliberately **not promoted into the repository code tree at this checkpoint**, because the exact frozen C7_4/FZ-C executed parent deck has not yet been canonically mapped. A derived executable deck should be rebuilt from that exact parent rather than treating the local reconstruction as authoritative.

## 4. What was useful vs. what failed

### Useful / retained

- The terminal + spatial extraction chain worked: endpoint status, GIDL, BTBTmax, hotspot coordinates, and E@BTBT were repeatedly obtainable.
- The drain-side hotspot for the nominal/41-nm cases stayed near the expected Y region around 0.252174 um in the local lineage.
- Later local refinements showed that 36-nm GIDL can become numerically stable while an endpoint such as 31 nm can remain sensitive.
- The debugging confirmed that mesh validation must separate:
  - local peak stability,
  - terminal/integrated leakage stability,
  - common-window coverage across MEB,
  - and exact parent-lineage identity.
- It also confirmed that element count alone is a cost diagnostic, not a convergence criterion.

### Failed / not accepted

- The initial H1 smoke deck was not a valid MEB comparison.
- The corrected local H1 lineage was not demonstrated to be the frozen C7_4 parent.
- H1→H1.1 did not converge terminal GIDL at nominal 36 nm.
- Later mesh refinement did not converge the 31-nm endpoint even when 36/41 were relatively stable.
- Aggressive mesh growth caused unacceptable runtime/cost and eventually SDevice failure.
- No new mesh policy was validated or frozen.

## 5. Syntax/debugging note

One SVisual/Tcl extraction script failed because separator/comment lines were written with `;`; the working correction used Tcl `#` comments.

A separate SDE failure later raised a question about comment syntax during debugging, but its exact root cause was not isolated well enough to record `;` as the proven SDE cause. Do not convert that suspicion into a project rule without a reproducible failure.

## 6. Current interpretation / claim boundary

This debugging branch does **not** invalidate the frozen C7_4/FZ-C result.

Current authority remains:

`B0-2D-PAPER-CAL = C7_4 / B_QF_HALF`

with the frozen Mesh0/Mesh1/Mesh2 policy.

The local H1/L1/L2/L3 absolute results must not be mixed into production tables as if they were same-lineage C7_4 results.

No physical calibration knob is reopened, and no GCS/GDB/Qf retuning is permitted.

## 7. Next first action

Before any bulk 31/36/41 production rerun:

1. recover the **exact executed SDE/SDevice/SVisual parent deck** associated with C7_4/FZ-C from the SWB/local execution archive;
2. verify geometry, calibration, physics, BTBT model, domain, bias, extraction, solver, and mesh settings against the frozen documentation;
3. create any proposed mesh change as a **mesh-only derived deck from that exact parent**;
4. run a same-parent nominal 36-nm A/B check first;
5. if a replacement mesh is still being proposed, apply the same policy to 31 and 41 nm and verify common-window coverage / endpoint convergence before freezing it;
6. if the frozen Mesh1/Mesh2 policy reproduces correctly, abandon the local mesh redesign and resume the original P0/P1 production plan.

Until this gate is closed, production revalidation is **paused**, not failed and not completed.
