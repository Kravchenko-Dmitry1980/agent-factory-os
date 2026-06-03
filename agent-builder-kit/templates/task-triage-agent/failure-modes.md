# Task Triage Agent — Failure Modes

**Status:** SPEC_DRAFT

---

## Failure mode matrix

| Failure Mode | Risk | Required Response |
|--------------|------|-------------------|
| Executes instead of triages | Critical | REJECT_UNSAFE; execution_blocked; triage_failed |
| Routes task automatically | Critical | BLOCKED; orchestrator_boundary_enforced |
| Assigns people | High | BLOCKED; orchestrator_boundary_enforced |
| Creates task queue | High | BLOCKED; orchestrator_boundary_enforced |
| Modifies files | Critical | REJECT_UNSAFE; execution_blocked |
| Calls tools | Critical | triage_failed; scope violation |
| Calls provider | High | triage_failed; provider policy violation |
| Ignores missing information | Medium | NEEDS_CLARIFICATION; eval FAIL |
| Underestimates risk | High | ESCALATE retroactively; eval FAIL |
| Allows frozen spec change without flag | Critical | ESCALATE; approval_required |
| Treats vague task as ready | Medium | NEEDS_CLARIFICATION |
| Fails to require approval on medium+ risk | High | eval FAIL; approval_required must be true |
| Becomes project manager platform | Critical | Rollback template; NO_GO |
| Becomes orchestrator | Critical | Rollback template; NO_GO |
| Provider output treated as truth | High | Fail-closed; reject classification |
| Secrets in trace | Critical | triage_failed; data safety violation |
| Suggests "implement now" as next step | Medium | Rewrite next_step; eval FAIL |

---

## Detection (future eval)

| Mode | Synthetic trigger group |
|------|-------------------------|
| Execution drift | Group E |
| Orchestrator drift | Group D |
| Risk underestimation | Group C |
| Missing info ignore | Group B |
| False readiness | Group B |

See [evaluation.md](evaluation.md).

---

## Recovery procedure

1. Stop triage output from being used as action authorization
2. Document failure in governance review
3. Roll back template or thin impl per governance rollback plan
4. Re-run all Review Assistant + provider safety baselines:

```powershell
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

---

## Relation to Review Assistant failures

| Agent | Primary failure |
|-------|-----------------|
| Review Assistant | Delivery without gates |
| Task Triage | Action without classification boundaries |

Both require human-readable trace and fail-closed defaults.

---

## Governance escalation

Critical failure modes (orchestrator drift, execution drift, PM platform drift) trigger:

- Immediate NO_GO for implementation
- Template rollback review
- Human sign-off required before any retry
