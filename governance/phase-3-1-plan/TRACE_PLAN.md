# Trace Plan — Phase 3.1 Thin Review Assistant

**Format:** Human-readable text. No telemetry backend. No JSON schema unless explicitly approved later.

---

## Required events

Future implementation must emit lines mappable to canonical events:

| Event | When required |
|-------|---------------|
| `task_started` | Task accepted |
| `draft_created` | After draft (may use `task_started actor=worker action=draft_created`) |
| `critique_completed` | After critique (or `verification_passed/failed actor=critic advisory=true`) |
| `verification_passed` OR `verification_failed` | After verification gate |
| `approval_requested` | Before delivery |
| `approval_denied` OR `approval_timeout` OR human approve (`verification_passed actor=human`) | Approval terminal |
| `unsafe_action_blocked` | Bypass attempt |
| `escalation_triggered` | Critic uncertain / policy |
| `task_completed` OR `task_failed` | Terminal |

Source: `observability/event-taxonomy/canonical-events.md`

---

## Line format (recommended)

```text
[timestamp] EVENT_NAME actor=... detail=...
```

Optional footer:

```text
OUTCOME status=completed|rejected|failed
GOVERNANCE gates_passed=N gates_failed=M escalated=yes|no
```

Align with [trace-templates/expected-trace-template.md](../../agent-builder-kit/trace-templates/expected-trace-template.md)

---

## Per-scenario minimum events

| Scenario | Minimum sequence |
|----------|------------------|
| happy | task_started → verification_passed (critic) → approval_requested → verification_passed (human) → task_completed |
| reject | task_started → approval_requested → approval_denied → task_failed |
| uncertain | task_started → verification_failed → escalation_triggered → approval_requested |
| bypass | task_started → unsafe_action_blocked → task_failed |

Reference: [expected-traces.md](../../agent-builder-kit/templates/review-assistant-agent/expected-traces.md)

---

## Repository examples (compare, do not modify)

| File | Use |
|------|-----|
| `observability/examples/successful-review-trace.txt` | Happy path shape |
| `observability/examples/failed-review-trace.txt` | Human deny shape |

Automated check (unchanged scripts):

```powershell
python evaluation/scripts/check_expected_text_traces.py
```

Impl traces are **separate** from examples/ — compare **semantically**, not by editing examples.

---

## Good vs bad trace

**Good:** every gate visible; critic `advisory=true`; human before complete.

**Bad:** `Done. Published.` only — **fail** acceptance.

---

## Trace review checklist

Use [trace-review-checklist.md](../../agent-builder-kit/evaluation-checklists/trace-review-checklist.md) after implementation.

---

## Diagram

Flow events: [diagrams/review-assistant-flow.md](diagrams/review-assistant-flow.md)
