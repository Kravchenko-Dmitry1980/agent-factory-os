# Task Triage Agent — Safety Gates

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Required gates

### 1. Input safety gate

**Purpose:** Reject or escalate unsafe/unclear task input.

| Check | Pass | Fail |
|-------|------|------|
| Non-empty task text | Continue | triage_failed |
| No embedded execution commands | Continue | REJECT_UNSAFE |
| No secret exfiltration ask | Continue | REJECT_UNSAFE |
| No approval bypass language | Continue | BLOCKED |

Trace: `input_validated` or `triage_failed`

---

### 2. Execution boundary gate

**Purpose:** Prevent task execution from triage path.

| Check | Pass | Fail |
|-------|------|------|
| Task does not request run/modify/send | Continue | REJECT_UNSAFE |
| Output does not imply execution | Continue | triage_failed |
| Trace includes execution_blocked when needed | Continue | eval FAIL |

Trace: `execution_blocked`

See [TASK_TRIAGE_AGENT_NO_EXECUTION_POLICY.md](TASK_TRIAGE_AGENT_NO_EXECUTION_POLICY.md)

---

### 3. Orchestrator boundary gate

**Purpose:** Prevent routing/delegation/multi-agent control.

| Check | Pass | Fail |
|-------|------|------|
| No delegate-to-agent language in task | Continue or BLOCKED | BLOCKED |
| No auto-route recommendation | Continue | BLOCKED |
| No queue/ticket creation | Continue | BLOCKED |

Trace: `orchestrator_boundary_enforced`

See [TASK_TRIAGE_AGENT_NO_ORCHESTRATOR_POLICY.md](TASK_TRIAGE_AGENT_NO_ORCHESTRATOR_POLICY.md)

---

### 4. Tool boundary gate

**Purpose:** No tool use by default.

| Check | Pass | Fail |
|-------|------|------|
| No tool invocation in workflow | Continue | triage_failed |
| No MCP/shell/API in spec | Continue | scope violation |

Future tool use requires separate governance phase.

---

### 5. Approval gate

**Purpose:** Recommend human approval when risk warrants.

| Condition | approval_required |
|-----------|-------------------|
| risk low, bounded doc task | false (advisory still human-reviewed) |
| risk medium | **true** |
| risk high / critical | **true** |
| frozen spec touch | **true** |
| provider addition | **true** |

Trace: `approval_required`

Triage approval ≠ implementation approval — both may be needed sequentially.

---

### 6. Escalation gate

**Purpose:** Escalate unclear ownership, security, provider, data, or architecture drift.

| Trigger | Action |
|---------|--------|
| Security / secret / bypass | ESCALATE or REJECT_UNSAFE |
| Frozen spec change | ESCALATE |
| Provider/cloud without policy | ESCALATE |
| Architecture drift (runtime/factory) | ESCALATE |
| Unclear ownership | NEEDS_CLARIFICATION or ESCALATE |

Trace: `escalation_required`

---

### 7. Trace gate

**Purpose:** Every decision must be traceable.

| Requirement | Detail |
|-------------|--------|
| All workflow steps logged | Human-readable |
| Final decision in trace | Required |
| No silent routing | Forbidden |
| No secrets in trace | Required |

Trace: full event chain through `triage_completed`

See [TASK_TRIAGE_AGENT_TRACE_PLAN.md](TASK_TRIAGE_AGENT_TRACE_PLAN.md)

---

## Gate order (fail-closed)

```text
input_validation
  → execution_boundary (early exit if REJECT_UNSAFE)
  → orchestrator_boundary (early exit if BLOCKED)
  → classification + risk
  → approval + escalation assessment
  → trace + final decision
```

---

## Diagram

See [diagrams/triage-safety-gates.md](diagrams/triage-safety-gates.md).
