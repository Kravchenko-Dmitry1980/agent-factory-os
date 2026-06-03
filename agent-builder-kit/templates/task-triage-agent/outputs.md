# Task Triage Agent — Outputs

**Status:** SPEC_DRAFT

All outputs are **advisory**. No output field may imply the task was executed, routed, or assigned.

---

## Core output fields

| Field | Required | Description |
|-------|----------|-------------|
| `task_type` | yes | Classification from allowed enum |
| `priority_class` | yes | Urgency/blocking class |
| `risk_level` | yes | Risk assessment |
| `missing_information` | yes | List (may be empty) |
| `suggested_next_step` | yes | Advisory string for human |
| `approval_required` | yes | boolean + reason |
| `escalation_required` | yes | boolean + reason |
| `final_triage_decision` | yes | Terminal decision enum |
| `reason` | yes | Human-readable justification |
| `trace` | yes | Ordered event list |

Provider or LLM output (if ever used in a future phase) is **not truth** — classification must pass safety gates.

---

## task_type (allowed values)

| Value | Meaning |
|-------|---------|
| `planning` | Design approach, phase plan, architecture sketch |
| `implementation` | Code, scripts, adapters, features |
| `review` | PR review, governance doc review, quality check |
| `debugging` | Fix failing check, diagnose error |
| `research` | Compare options, external repo triage |
| `documentation` | README, guides, navigation updates |
| `governance` | Freeze, GO/NO-GO, change proposal |
| `evaluation` | Harness cases, smoke checks, eval scripts |
| `security` | Prompt injection, secret handling, policy |
| `product` | Product-specific feature — often → escalate |
| `unclear` | Insufficient information to classify confidently |

---

## priority_class (allowed values)

| Value | Meaning |
|-------|---------|
| `low` | Safe, bounded, clear |
| `medium` | Needs plan or approval |
| `high` | Significant risk or cross-cutting change |
| `blocked` | Cannot proceed — missing info or policy block |

---

## risk_level (allowed values)

| Value | Typical triggers |
|-------|------------------|
| `low` | Doc typo, navigation link |
| `medium` | New eval script, template spec change |
| `high` | Provider boundary, frozen spec touch, agent behavior |
| `critical` | Secret exposure, approval removal, orchestrator, execution |

---

## final_triage_decision (allowed values)

| Decision | Meaning |
|----------|---------|
| `TRIAGED` | Classification complete; human may act on advice |
| `NEEDS_CLARIFICATION` | Missing info blocks confident triage |
| `ESCALATE` | Human lead / security / architecture review required |
| `BLOCKED` | Policy violation or forbidden action requested |
| `REJECT_UNSAFE` | Unsafe task (execution, secrets, bypass) |

**Forbidden decisions:** `EXECUTED`, `ROUTED`, `ASSIGNED`, `DELIVERED`, `AUTO_APPROVED`

---

## Output invariants

1. No output field may imply task was executed
2. No output field may name a target agent to auto-start
3. `approval_required=true` when risk ≥ medium or frozen/provider touch
4. `REJECT_UNSAFE` for execution/orchestrator/secret bypass requests
5. Trace must include boundary events when relevant

See [contract.md](contract.md).
