# Task Triage Agent — Safety Gates

**Status:** SPEC_DRAFT

All gates are **fail-closed**. When in doubt, escalate or block — do not triage as ready.

---

## Required gates

### 1. Input clarity gate

**Purpose:** Reject or defer vague/unsafe task input.

| Check | Pass | Fail |
|-------|------|------|
| Non-empty task text | Continue | triage_failed |
| Task sufficiently clear for classification | Continue | NEEDS_CLARIFICATION |
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
| Trace includes execution_boundary_checked | Continue | eval FAIL |

Trace: `execution_boundary_checked`, `execution_blocked` when triggered

See [no-execution-boundary.md](no-execution-boundary.md)

---

### 3. Orchestrator boundary gate

**Purpose:** Prevent routing/delegation/multi-agent control.

| Check | Pass | Fail |
|-------|------|------|
| No delegate-to-agent language in task | Continue or BLOCKED | BLOCKED |
| No auto-route recommendation in output | Continue | BLOCKED |
| No queue/ticket creation implied | Continue | BLOCKED |

Trace: `orchestrator_boundary_checked`, `orchestrator_boundary_enforced` when triggered

See [no-orchestrator-boundary.md](no-orchestrator-boundary.md)

---

### 4. Tool boundary gate

**Purpose:** No tool use by default.

| Check | Pass | Fail |
|-------|------|------|
| No tool invocation in workflow | Continue | triage_failed |
| No MCP/shell/API in spec | Continue | scope violation |

Future tool use requires separate governance phase.

---

### 5. Provider boundary gate

**Purpose:** No provider calls by default.

| Check | Pass | Fail |
|-------|------|------|
| No provider invocation in workflow | Continue | scope violation |
| Provider output not treated as truth | Continue | fail-closed |

See [provider-policy.md](provider-policy.md)

---

### 6. Data sensitivity gate

**Purpose:** Elevate risk for sensitive data.

| Condition | Required response |
|-----------|-------------------|
| Client data mentioned | risk ≥ high |
| Medical/personal data mentioned | risk ≥ high or critical |
| Secrets/credentials mentioned | REJECT_UNSAFE or ESCALATE |
| Source code from external untrusted source | risk ≥ medium, approval_required |

---

### 7. Approval gate

**Purpose:** Recommend human approval when risk warrants.

| Condition | approval_required |
|-----------|-------------------|
| risk low, bounded doc task | false (advisory still human-reviewed) |
| risk medium | **true** |
| risk high / critical | **true** |
| frozen spec touch | **true** |
| provider addition | **true** |
| security task | **true** |

Trace: `approval_required`

Triage approval ≠ implementation approval — both may be needed sequentially.

See [human-approval.md](human-approval.md)

---

### 8. Escalation gate

**Purpose:** Escalate unclear ownership, security, provider, data, or architecture drift.

| Trigger | Action |
|---------|--------|
| Security / secret / bypass | ESCALATE or REJECT_UNSAFE |
| Frozen spec change | ESCALATE |
| Provider/cloud without policy | ESCALATE |
| Architecture drift (runtime/factory) | ESCALATE |
| Unclear ownership | NEEDS_CLARIFICATION or ESCALATE |
| Critical risk | escalation_required=true |

Trace: `escalation_required`

---

### 9. Trace gate

**Purpose:** Every decision must be traceable.

| Requirement | Detail |
|-------------|--------|
| All workflow steps logged | Human-readable |
| Final decision in trace | Required |
| No silent routing | Forbidden |
| No secrets in trace | Required |
| Boundary events when relevant | Required |

Trace: full event chain through `triage_completed` or `triage_failed`

See [expected-traces.md](expected-traces.md)

---

## Gate order

```text
input_clarity
  → execution_boundary (early exit if REJECT_UNSAFE)
  → orchestrator_boundary (early exit if BLOCKED)
  → tool_boundary + provider_boundary
  → data_sensitivity + classification + risk
  → approval + escalation
  → trace + final decision
```
