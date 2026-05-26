# Task Triage Agent — Trace Plan

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Trace format

- **Human-readable** text lines (same discipline as Review Assistant thin)
- Example: `- task_type_classified: type=planning, confidence=rule_based`
- No telemetry backend in v0.1 plan
- No JSON schema yet — define in future template `expected-traces.md`

---

## Required trace events

| Event | When emitted |
|-------|--------------|
| `task_received` | Task text accepted |
| `input_validated` | Input safety gate passed |
| `task_type_classified` | Type assigned |
| `risk_detected` | Risk level assigned |
| `missing_info_detected` | Gaps listed (may be empty) |
| `next_step_proposed` | Advisory next step |
| `approval_required` | HITL recommendation |
| `escalation_required` | Escalation recommendation |
| `execution_blocked` | Execution language detected or policy enforced |
| `orchestrator_boundary_enforced` | Routing/delegation blocked |
| `triage_completed` | Successful triage end state |
| `triage_failed` | Fail-closed terminal state |

---

## Optional events (future)

| Event | When |
|-------|------|
| `provider_request_prepared` | Only if provider phase approved |
| `classification_uncertain` | Ambiguous task — may pair with ESCALATE |

Default path: **no provider events**.

---

## Forbidden trace events

| Event | Reason |
|-------|--------|
| `task_executed` | Execution boundary |
| `agent_started` | Orchestrator boundary |
| `task_routed` | Orchestrator boundary |
| `ticket_created` | PM platform |
| `file_modified` | Execution boundary |
| `command_run` | Execution boundary |
| `approval_granted` (auto) | Triage does not grant impl approval |

---

## Example trace (normal triage)

```text
TRACE
- task_received: scenario=simple_planning
- input_validated: checks=basic_safety
- task_type_classified: type=planning
- risk_detected: level=medium
- missing_info_detected: items=rollback_plan
- next_step_proposed: step=create_implementation_plan
- approval_required: required=true, reason=medium_risk
- escalation_required: required=false
- triage_completed: decision=TRIAGED
```

---

## Example trace (orchestrator block)

```text
TRACE
- task_received: scenario=delegate_agents
- input_validated: checks=basic_safety
- orchestrator_boundary_enforced: reason=delegate_to_agent_requested
- execution_blocked: reason=policy
- triage_completed: decision=BLOCKED
```

---

## Trace review loop

Human reviewer checks:

1. Decision matches trace events
2. No forbidden events present
3. No implied execution or routing in `next_step_proposed`
4. No secrets in trace output

Future diagram: compare to Review Assistant [trace-review-loop](../../phase-3-4-plan/diagrams/trace-review-loop.md) pattern.
