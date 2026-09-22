# Turn 01 Presentation Note

## Presentation

**MEB 기반 GIDL 저감의 온도 의존적 1T1C Retention 전달 특성 분석**

## Role in the CMP chronology

Turn 01 formalized the transition from a broad HBM / DRAM reliability context to a narrower device-level BCAT study with a traceable mechanism chain:

```text
MEB depth
→ gate-drain coupling / Cgd
→ drain-side electric field
→ BTBT / GIDL
→ 1T1C retention
→ effective MEB design range
```

At this milestone:

- Run 0–6.5 transistor-level work had been completed.
- `P1=41 nm` was retained as the historical initial screened-window candidate.
- extended MEB screening moved the cell-validation handoff to `P2=48 nm`.
- `48 nm` was explicitly a retention-validation candidate, not a final/global/production optimum.
- the simplified 2D BCAT model was still the main DOE framework.
- Run 7 was introduced to determine whether the transistor-level GIDL advantage actually transfers to a 1T1C storage-node retention benefit.

## Feedback that followed

The presentation triggered four major validation tasks:

1. verify that the common Mesh-GIDL refinement continues to cover the actual per-MEB BTBT hotspot;
2. re-evaluate electric field in the actual BTBT/GIDL critical region rather than relying on one historical fixed cut;
3. check the electrical fidelity of the simplified 2D baseline against a literature-consistent 3D BCAT reconstruction and assess practical BCAT trade-offs;
4. make the 1T1C write / hold / read and retention protocol explicit and reproducible.

Those tasks are tracked in [FEEDBACK_LOG.md](../../FEEDBACK_LOG.md).
