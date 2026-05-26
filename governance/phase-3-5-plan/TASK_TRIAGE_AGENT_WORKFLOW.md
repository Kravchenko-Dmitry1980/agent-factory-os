# Task Triage Agent — Workflow

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Standard workflow

```text
task_received
  → input_validation
  → task_type_classification
  → risk_detection
  → missing_info_detection
  → next_step_proposal
  → approval_need_assessment
  → escalation_need_assessment
  → final_triage_decision
  → trace
  → triage_completed | triage_failed
```

---

## Step definitions

| Step | Purpose | Fail-closed |
|------|---------|-------------|
| `task_received` | Accept task text + optional context | Reject empty/malformed input |
| `input_validation` | Safety scan for execution/orchestrator language | BLOCKED / REJECT_UNSAFE |
| `task_type_classification` | Assign task type enum | `unclear` if insufficient |
| `risk_detection` | Assess risk level | Elevate on frozen/provider/secret touch |
| `missing_info_detection` | List required missing fields | NEEDS_CLARIFICATION if critical gaps |
| `next_step_proposal` | Advisory next action | Must not be "execute now" |
| `approval_need_assessment` | Recommend HITL | true for medium+ or policy |
| `escalation_need_assessment` | Recommend escalation | true for critical/security/architecture |
| `final_triage_decision` | One of allowed decisions | Never EXECUTED/ROUTED |
| `trace` | Emit all step events | Required |

---

## Explicit absences

The workflow has **no**:

| Missing step | Policy |
|--------------|--------|
| Execution step | [NO_EXECUTION_POLICY](TASK_TRIAGE_AGENT_NO_EXECUTION_POLICY.md) |
| Delegation step | [NO_ORCHESTRATOR_POLICY](TASK_TRIAGE_AGENT_NO_ORCHESTRATOR_POLICY.md) |
| Automatic routing step | No agent dispatch |
| Tool call step | No MCP/shell/API |
| Ticket creation step | No PM platform |
| File modification step | No repo writes |
| Provider call step (default) | [PROVIDER_POLICY](TASK_TRIAGE_AGENT_PROVIDER_POLICY.md) |

---

## Decision shortcuts

| Condition | Typical decision |
|-----------|------------------|
| Task asks to run command / modify files | REJECT_UNSAFE |
| Task asks to delegate to agents / create queue | BLOCKED + orchestrator_boundary_enforced |
| Task asks to remove approval / bypass gates | BLOCKED or ESCALATE |
| Task asks to change frozen spec | ESCALATE + approval_required |
| Task lacks target/acceptance criteria | NEEDS_CLARIFICATION |
| Task is clear doc/governance update | TRIAGED, risk low |
| Task adds provider/cloud without plan | ESCALATE, risk high |

---

## Human handoff

After `triage_completed`:

1. Human reads trace and advisory fields
2. Human decides: plan / implement / review / defer / reject
3. **No automatic handoff** to Review Assistant or any agent

Optional human note: "Proceed with Phase X impl" — outside triage agent scope.

---

## Diagram

See [diagrams/task-triage-flow.md](diagrams/task-triage-flow.md).
