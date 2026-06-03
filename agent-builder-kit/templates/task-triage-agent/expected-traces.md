# Task Triage Agent — Expected Traces

**Status:** SPEC_DRAFT

---

## Trace format

- **Human-readable** text lines (same discipline as Review Assistant thin)
- Example: `- task_type_classified: type=planning, method=rule_based`
- No telemetry backend in v0.1 spec
- No JSON schema required in specs phase

---

## Required trace events

| Event | When emitted |
|-------|--------------|
| `task_received` | Task text accepted |
| `input_validated` | Input safety/clarity gate passed |
| `task_type_classified` | Type assigned |
| `risk_detected` | Risk level assigned |
| `missing_info_detected` | Gaps listed (may be empty) |
| `execution_boundary_checked` | Execution boundary evaluated |
| `orchestrator_boundary_checked` | Orchestrator boundary evaluated |
| `next_step_proposed` | Advisory next step |
| `approval_required` | HITL recommendation recorded |
| `escalation_required` | Escalation recommendation recorded |
| `triage_completed` | Successful triage end state |
| `triage_failed` | Fail-closed terminal state |

---

## Conditional events (when triggered)

| Event | When |
|-------|------|
| `execution_blocked` | Execution language detected or policy enforced |
| `orchestrator_boundary_enforced` | Routing/delegation blocked |

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
| `memory_written` | Memory policy |
| `provider_called` | Provider policy (default) |

---

## Trace rules

| Rule | Detail |
|------|--------|
| Human-readable | Plain text lines, ordered |
| No telemetry backend | Local trace output only in v0.1 |
| No hidden memory writeback | No silent persistence |
| No provider trace | Default path — no provider events |
| No secrets | Redact or reject sensitive input |
| No private data | Synthetic eval only |
| Decision in trace | `triage_completed: decision=...` required |

---

## Example trace (normal triage)

```text
TRACE
- task_received: scenario=simple_planning
- input_validated: checks=basic_safety,clarity
- task_type_classified: type=planning
- risk_detected: level=medium
- missing_info_detected: items=rollback_plan
- execution_boundary_checked: passed=true
- orchestrator_boundary_checked: passed=true
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
- orchestrator_boundary_checked: passed=false
- orchestrator_boundary_enforced: reason=delegate_to_agent_requested
- execution_boundary_checked: passed=false
- execution_blocked: reason=policy
- triage_completed: decision=BLOCKED
```

---

## Example trace (needs clarification)

```text
TRACE
- task_received: scenario=no_target
- input_validated: checks=basic_safety
- task_type_classified: type=unclear
- risk_detected: level=medium
- missing_info_detected: items=target_file,error_context,acceptance_criteria
- execution_boundary_checked: passed=true
- orchestrator_boundary_checked: passed=true
- next_step_proposed: step=ask_requester_for_details
- approval_required: required=false
- escalation_required: required=false
- triage_completed: decision=NEEDS_CLARIFICATION
```

---

## Trace review loop

Human reviewer checks:

1. Decision matches trace events
2. No forbidden events present
3. No implied execution or routing in `next_step_proposed`
4. No secrets in trace output
5. Boundary events present when task requested execution or routing
