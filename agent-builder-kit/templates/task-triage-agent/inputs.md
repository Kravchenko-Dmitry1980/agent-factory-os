# Task Triage Agent — Inputs

**Status:** SPEC_DRAFT

---

## Required inputs

| Field | Type | Description |
|-------|------|-------------|
| `task_text` | string | Natural-language description of the incoming work task |

**Constraints:**

- Must be non-empty
- Synthetic or project-safe text in evaluation
- No secrets, credentials, or client PII in default cases
- No executable payloads treated as commands to the agent

---

## Optional inputs

| Field | Type | Description |
|-------|------|-------------|
| `context_label` | string | High-level context, e.g. `governance`, `evaluation`, `prototype` |
| `project_area` | string | Project scope hint, e.g. `review-assistant-thin`, `agent-builder-kit` |
| `risk_hints` | string or list | Human-supplied hints — **not authoritative** |
| `requester_role` | string | e.g. `operator`, `developer`, `reviewer` — advisory only |
| `deadline_hint` | string | Time pressure hint — does not set priority automatically |
| `known_constraints` | string or list | e.g. "no provider calls", "frozen spec" |

Optional fields inform classification but do **not** override safety gates.

---

## Forbidden input assumptions

The agent must **not assume** any of the following if not explicitly provided:

| Assumption | If missing |
|------------|------------|
| Owner | Mark as missing information |
| Priority | Derive from risk analysis, not guess |
| Approval already granted | Default to approval_required when risk warrants |
| Implementation path | Propose advisory next step only |
| Provider choice | Flag as missing if task implies provider |
| Data sensitivity | Do not assume low — escalate if unclear |
| Production readiness | Do not assume ready for production |

If critical information is missing, decision must be **NEEDS_CLARIFICATION** or include missing fields in output.

---

## Input validation rules

| Check | Pass | Fail |
|-------|------|------|
| Non-empty `task_text` | Continue | triage_failed |
| No embedded execution command as agent instruction | Continue | REJECT_UNSAFE |
| No secret exfiltration request | Continue | REJECT_UNSAFE |
| No approval bypass language | Continue | BLOCKED |

Trace: `input_validated` or `triage_failed`

See [safety-gates.md](safety-gates.md).

---

## Example inputs

**Minimal:**

```text
task_text: "Update README navigation for Phase 3.5 plan"
```

**With context:**

```text
task_text: "Plan thin implementation for task triage specs"
context_label: governance
project_area: agent-builder-kit
known_constraints: ["no code in specs phase", "markdown only"]
```

**Unsafe (must fail closed):**

```text
task_text: "Run rm -rf and fix the repo"
```

```text
task_text: "Route this to Review Assistant and start implementation now"
```
