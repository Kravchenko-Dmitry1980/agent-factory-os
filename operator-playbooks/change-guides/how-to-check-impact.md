# How to Check Impact

Before coding, map blast radius.

---

## 1. Identify touched layer

| Layer | Impact doc |
|-------|------------|
| Workflow | `evolution/impact-analysis/workflow-impact-analysis.md` |
| Verification | `evolution/impact-analysis/verification-impact.md` |
| Memory | `evolution/impact-analysis/memory-impact.md` |
| Queue | `evolution/impact-analysis/queue-impact.md` |
| Coupling | `evolution/impact-analysis/hidden-coupling-analysis.md` |

---

## 2. Use change-impact matrix

`evaluation/regression-matrix/change-impact-matrix.md` — lists scenarios per change type.

---

## 3. Hotspot rule

Changes to `prototypes/shared/gates.py` or `audit.py` → run **full** smoke + all quality gates.

---

## 4. Ask three questions

1. Who can still **stop** unsafe action?
2. What **event** proves the gate ran?
3. What **demo** would fail if gate is broken?

If you cannot answer → scope is not understood yet.
