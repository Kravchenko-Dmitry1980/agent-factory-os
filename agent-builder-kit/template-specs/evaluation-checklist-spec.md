# Evaluation Checklist Spec

Every future agent template must ship evaluation coverage before acceptance.

---

## Required Check Categories

| Category | What to verify |
|----------|----------------|
| **Happy path** | Draft → gates → approval → completed |
| **Fail path** | Rejection terminates cleanly |
| **Missing approval** | Publish blocked without human decision |
| **Malformed LLM output** | Unparseable output fails closed |
| **Verification failure** | Bad draft blocked at verification |
| **Escalation** | Ambiguity routes to human |
| **Unsafe action block** | Bypass attempt blocked |
| **Audit present** | Trace complete for every scenario |
| **Rollback decision** | Template change has rollback plan |

---

## Repository References

| Resource | Path |
|----------|------|
| Quality gates | `evaluation/quality-gates/` |
| Scenarios | `evaluation/scenarios/` |
| Review loop scenarios | `evaluation/scenarios/review-loop-scenarios.md` |
| Smoke checks | `evaluation/scripts/run_demo_smoke_checks.py` (Phase 2 runtime; not part of kit) |
| Trace checks | `evaluation/scripts/check_expected_text_traces.py` (Phase 2 runtime) |

**Note:** Scripts are Phase 2 evaluation harness. Templates **reference** them; kit does not embed runners.

---

## Per-Template Evaluation Doc

Each template must include `evaluation.md` with:

1. Scenario name
2. Input description
3. Expected behavior
4. Expected event trace (text)
5. Pass criteria
6. Fail criteria
7. Why it matters

---

## Evaluation Gate

Template cannot move to **accepted** until:

- [ ] All required categories have at least one scenario
- [ ] Expected traces documented
- [ ] Pass/fail criteria explicit
- [ ] Phase 3 template review checklist completed

See [safety-gates/evaluation-gate.md](../safety-gates/evaluation-gate.md)

---

## Explicitly Out of Scope (v0.1)

- Benchmark metrics
- Model scoring / leaderboard
- Automated LLM-as-judge production pipeline

---

## Related

- [evaluation-checklists/](../evaluation-checklists/README.md)
- [templates/review-assistant-agent/evaluation.md](../templates/review-assistant-agent/evaluation.md)
