# Task Triage Agent — Contract (Future Template)

**Date:** 2026-05-26  
**Status:** PLAN_ONLY — contract spec for future `agent-builder-kit/templates/task-triage-agent/`

---

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `task_text` | **Yes** | Natural-language task description |
| `context_label` | No | e.g. "governance", "evaluation", "prototype" |
| `project_area` | No | e.g. "review-assistant-thin", "agent-builder-kit" |
| `risk_hints` | No | Human-supplied hints (not authoritative) |

**Constraints:**

- Synthetic or project-safe text only in evaluation
- No secrets, credentials, or client PII in default cases
- No executable payloads in task text as commands to agent

---

## Outputs

| Field | Description |
|-------|-------------|
| `task_type` | From allowed enum |
| `priority_class` | low / medium / high / blocked |
| `risk_level` | low / medium / high / critical |
| `missing_information` | List of gaps |
| `suggested_next_step` | Advisory string |
| `approval_required` | boolean + reason |
| `escalation_required` | boolean + reason |
| `final_triage_decision` | From allowed decisions |
| `trace` | Ordered human-readable events |

Provider/LLM output (if ever used) is **not truth** — classification must pass safety gates.

---

## Task types (allowed)

| Type | Example trigger |
|------|-----------------|
| `planning` | "Plan Phase 3.5", "design approach" |
| `implementation` | "Add adapter", "implement script" |
| `review` | "Review PR", "check governance doc" |
| `debugging` | "Fix failing check", "diagnose error" |
| `research` | "Compare options", "triage external repo" |
| `documentation` | "Write README", "update freeze record" |
| `governance` | "Freeze artifact", "GO/NO-GO review" |
| `evaluation` | "Add harness case", "run smoke checks" |
| `security` | "Prompt injection", "secret handling" |
| `product` | Product-specific feature (often → escalate) |
| `unclear` | Insufficient information |

---

## Priority classes (allowed)

| Class | Meaning |
|-------|---------|
| `low` | Safe, bounded, clear |
| `medium` | Needs plan or approval |
| `high` | Significant risk or cross-cutting change |
| `blocked` | Cannot proceed — missing info or policy block |

---

## Risk levels (allowed)

| Level | Typical triggers |
|-------|------------------|
| `low` | Doc typo, navigation link |
| `medium` | New eval script, template spec change |
| `high` | Provider boundary, frozen spec touch, agent behavior |
| `critical` | Secret exposure, approval removal, orchestrator, execution |

---

## Final decisions (allowed)

| Decision | Meaning |
|----------|---------|
| `TRIAGED` | Classification complete; human may act on advice |
| `NEEDS_CLARIFICATION` | Missing info blocks confident triage |
| `ESCALATE` | Human lead / security / architecture review required |
| `BLOCKED` | Policy violation or forbidden action requested |
| `REJECT_UNSAFE` | Unsafe task (execution, secrets, bypass) |

**Forbidden decisions:** `EXECUTED`, `ROUTED`, `ASSIGNED`, `DELIVERED`, `AUTO_APPROVED`

---

## Invariants

1. No output field may imply task was executed
2. No output field may name a target agent to auto-start
3. `approval_required=true` when risk ≥ medium or frozen touch
4. `REJECT_UNSAFE` for execution/orchestrator/secret bypass requests
5. Trace must include `execution_blocked` and/or `orchestrator_boundary_enforced` when relevant

---

## Template file structure (future impl)

Mirror Review Assistant template:

- `agent-card.md`
- `workflow.md`
- `safety-gates.md`
- `memory-boundaries.md`
- `human-approval.md`
- `evaluation.md`
- `expected-traces.md`
- `failure-modes.md`
- `anti-patterns.md`
- `change-proposal.md`
- `acceptance-criteria.md`
- `sign-off/` (after eval)

**Not created in Phase 3.5-Plan.**
