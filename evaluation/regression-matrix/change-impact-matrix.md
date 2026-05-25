# Change Impact Matrix

Map change type → areas to re-check.

| Change type | Touch areas | Required scenarios | Trace examples |
|-------------|-------------|-------------------|----------------|
| Retry constant | Queue, escalation | exhausted, escalate | escalation-trace.txt |
| Approval logic | Review, fail-closed, telegram | no-approval, denied, timeout | failed-review-trace.txt |
| Critic rules | Review, promotion | uncertain-critic, unsupported-claim | successful-review-trace.txt |
| Memory limit | Memory, bounded workflow | over-limit, unverified | (demo audit) |
| LLM parser | LLM adapter | malformed, uncertain, timeout | malformed-llm-trace.txt |
| GUI matcher | GUI workflows | match, mismatch, uncertain | unsafe-gui-action-trace.txt |
| Promotion rules | Promotion sim | valid, no-provenance, topology | (demo audit) |
| Shared module | All demos using it | smoke checks all | all examples |
| Audit format | Observability | trace-diff-checklist | all examples |
| New demo scenario | That demo only | new scenario doc | new local trace |

---

## Impact Severity Guide

| Scope | Re-check depth |
|-------|----------------|
| Single demo, one scenario | That scenario + smoke |
| Shared gates.py / audit.py | All prototype smoke + CB matrix |
| integrations-real adapter | Adapter scenarios + prototype equivalent |
| Documentation only | No demo re-run required |
| evolution/ policy change | Manual review only |

---

## Coupling Hotspots

From `evolution/impact-analysis/hidden-coupling-analysis.md`:

| Hotspot | Hidden dependents |
|---------|-------------------|
| `prototypes/shared/gates.py` | All prototypes |
| `prototypes/shared/audit.py` | All audit dumps |
| Retry constants | queue + escalation + local-queue-worker |
| Approval enum | review + fail-closed + telegram |

Change in hotspot → run full smoke + trace check script.

---

## Template: Change Entry

```text
Change:
Areas touched:
Scenarios to re-run:
Baseline trace:
Post-change trace:
Verdict: PASS / FAIL
Rollback needed: yes / no
```

Store locally in `evaluation/reports/` if desired — not required in git.
