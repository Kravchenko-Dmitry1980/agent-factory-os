# AI Architect Path

---

## Goal

Connect doctrine → prototypes → observability → evaluation → safe evolution. Design governed workflows, not agent swarms.

## Estimated Time

2–3 days focused study

---

## What to Read

| Order | Document |
|-------|----------|
| 1 | `agent-os/doctrine/architecture-worldview.md` |
| 2 | `agent-os/doctrine/verification-first.md` |
| 3 | `agent-os/doctrine/governance-before-autonomy.md` |
| 4 | `prototypes/README.md` + each prototype's `contracts.md` |
| 5 | `observability/event-taxonomy/canonical-events.md` |
| 6 | `evaluation/regression-matrix/critical-behavior-matrix.md` |
| 7 | `evolution/impact-analysis/workflow-impact-analysis.md` |

---

## What to Run

All prototypes + one integration per domain:

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
python prototypes/integrations/escalation-workflow/minimal-demo.py --scenario retry-storm
python prototypes/integrations/governed-promotion-workflow/minimal-demo.py --scenario dangerous-topology
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
```

---

## What to Avoid

- Universal multi-agent templates without contracts
- Skipping failure-modes.md on any prototype
- Promoting experimental patterns without scoring
- Brain OS / control-plane product thinking in demos

---

## Expected Outcome

- Can draw review → verify → approve → publish flow
- Can name 5 critical behaviors (CB-01–CB-05 from evaluation matrix)
- Can write a minimal change proposal

---

## Checkpoint Questions

1. What is verification-before-writeback?
2. When must escalation_triggered appear?
3. What is platform drift?
4. How does promotion differ from "adding a markdown file"?
