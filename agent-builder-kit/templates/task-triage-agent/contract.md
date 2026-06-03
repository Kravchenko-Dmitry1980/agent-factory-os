# Task Triage Agent — Contract

**Status:** SPEC_DRAFT  
**Version:** v0.1-draft

---

## Input contract

| Field | Required | Type | Notes |
|-------|----------|------|-------|
| `task_text` | **Yes** | string | Non-empty natural-language task |
| `context_label` | No | string | e.g. governance, evaluation, prototype |
| `project_area` | No | string | e.g. review-assistant-thin, agent-builder-kit |
| `risk_hints` | No | string or list | Human hints — not authoritative |
| `requester_role` | No | string | Advisory context only |
| `deadline_hint` | No | string | Does not auto-set priority |
| `known_constraints` | No | string or list | e.g. no provider, frozen spec |

---

## Output contract

| Field | Required | Type | Allowed Values / Notes |
|-------|----------|------|------------------------|
| `task_type` | Yes | enum | planning, implementation, review, debugging, research, documentation, governance, evaluation, security, product, unclear |
| `priority_class` | Yes | enum | low, medium, high, blocked |
| `risk_level` | Yes | enum | low, medium, high, critical |
| `missing_information` | Yes | list[string] | May be empty |
| `suggested_next_step` | Yes | string | Advisory only — no imperative execution |
| `approval_required` | Yes | boolean + reason | true when risk ≥ medium or policy touch |
| `escalation_required` | Yes | boolean + reason | true for critical/security/architecture |
| `final_triage_decision` | Yes | enum | TRIAGED, NEEDS_CLARIFICATION, ESCALATE, BLOCKED, REJECT_UNSAFE |
| `reason` | Yes | string | Human-readable justification |
| `trace` | Yes | list[string] | Ordered human-readable events |

---

## Decision contract

### Allowed decisions

| Decision | When to use |
|----------|-------------|
| `TRIAGED` | Classification complete; human may act on advice |
| `NEEDS_CLARIFICATION` | Critical gaps block confident triage |
| `ESCALATE` | Security, frozen spec, provider, architecture, unclear ownership |
| `BLOCKED` | Policy violation — orchestrator, queue, bypass |
| `REJECT_UNSAFE` | Execution, secrets, dangerous commands |

### Forbidden decisions

`EXECUTED`, `ROUTED`, `ASSIGNED`, `DELIVERED`, `AUTO_APPROVED`, `QUEUED`, `DISPATCHED`

---

## Contract rules

| Rule | Enforcement |
|------|-------------|
| Unclear task cannot be TRIAGED as ready | Use NEEDS_CLARIFICATION or task_type=unclear |
| High/critical risk requires `approval_required=true` | Approval gate |
| Unsafe task must be BLOCKED or REJECT_UNSAFE | Execution/orchestrator/secret gates |
| Task asking for execution must trigger no-execution boundary | REJECT_UNSAFE + execution_blocked trace |
| Task asking for routing/delegation must trigger no-orchestrator boundary | BLOCKED + orchestrator_boundary_enforced trace |
| Frozen spec touch requires ESCALATE + approval_required | Escalation gate |
| Provider addition without plan requires ESCALATE | Provider policy |
| No output may imply execution or routing occurred | Output invariants |

---

## Trace contract

Every triage must produce a trace containing at minimum:

- `task_received`
- `input_validated` or `triage_failed`
- `final_triage_decision` equivalent via `triage_completed` or `triage_failed`

When boundaries triggered, trace must include:

- `execution_boundary_checked` / `execution_blocked`
- `orchestrator_boundary_checked` / `orchestrator_boundary_enforced`

See [expected-traces.md](expected-traces.md).

---

## Versioning

Contract changes require [change-proposal.md](change-proposal.md) and governance review. Frozen contract changes require sign-off.
