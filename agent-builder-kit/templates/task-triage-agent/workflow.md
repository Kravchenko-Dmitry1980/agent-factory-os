# Task Triage Agent — Workflow

**Status:** SPEC_DRAFT

---

## Standard workflow

```text
task_received
  → input_validation
  → task_type_classification
  → risk_detection
  → missing_info_detection
  → no_execution_check
  → no_orchestrator_check
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
| `no_execution_check` | Enforce execution boundary | REJECT_UNSAFE if execution requested |
| `no_orchestrator_check` | Enforce orchestrator boundary | BLOCKED if routing/delegation requested |
| `next_step_proposal` | Advisory next action | Must not be "execute now" |
| `approval_need_assessment` | Recommend HITL | true for medium+ or policy |
| `escalation_need_assessment` | Recommend escalation | true for critical/security/architecture |
| `final_triage_decision` | One of allowed decisions | Never EXECUTED/ROUTED |
| `trace` | Emit all step events | Required |

---

## Decision shortcuts

| Condition | Typical decision |
|-----------|------------------|
| Task asks to run command / modify files | REJECT_UNSAFE |
| Task asks to delegate to agents / create queue | BLOCKED |
| Task asks to remove approval / bypass gates | BLOCKED or ESCALATE |
| Task asks to change frozen spec | ESCALATE + approval_required |
| Task lacks target/acceptance criteria | NEEDS_CLARIFICATION |
| Task is clear doc/governance update | TRIAGED, risk low |
| Task adds provider/cloud without plan | ESCALATE, risk high |

---

## Explicitly absent steps

The workflow has **no**:

| Missing step | Policy |
|--------------|--------|
| Execution step | [no-execution-boundary.md](no-execution-boundary.md) |
| Delegation step | [no-orchestrator-boundary.md](no-orchestrator-boundary.md) |
| Automatic routing step | No agent dispatch |
| Tool call step | No MCP/shell/API |
| Ticket creation step | No PM platform |
| File modification step | No repo writes |
| Provider call step (default) | [provider-policy.md](provider-policy.md) |
| Task queue step | No backlog/scheduling |
| Message sending step | No external delivery |

---

## Human handoff

After `triage_completed`:

1. Human reads trace and advisory fields
2. Human decides: plan / implement / review / defer / reject
3. **No automatic handoff** to Review Assistant or any agent

Optional human note: "Proceed with Phase X impl" — outside triage agent scope.

---

## Gate order (fail-closed)

```text
input_validation
  → no_execution_check (early exit if REJECT_UNSAFE)
  → no_orchestrator_check (early exit if BLOCKED)
  → classification + risk + missing_info
  → next_step + approval + escalation
  → trace + final decision
```

See [safety-gates.md](safety-gates.md).
