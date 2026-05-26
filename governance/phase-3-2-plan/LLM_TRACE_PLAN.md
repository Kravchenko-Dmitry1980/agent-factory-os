# LLM Trace Plan — Phase 3.2 (Future)

**Format:** Human-readable text. No telemetry backend.

---

## Future LLM boundary events

| Event | When |
|-------|------|
| `llm_request_started` | Adapter invoked |
| `llm_response_received` | Raw response available |
| `llm_parse_passed` | Parsed successfully |
| `llm_parse_failed` | Malformed / empty / schema fail |
| `llm_timeout` | Deadline exceeded |
| `llm_uncertain` | Uncertainty flagged |
| `llm_unsafe_output` | Policy block |

Align with repository: `observability/event-taxonomy/canonical-events.md` (`llm_timeout`, `llm_malformed_output`)

---

## Downstream gates (unchanged)

| Event | When |
|-------|------|
| `verification_passed` / `verification_failed` | After verification on parsed content |
| `approval_requested` | Before delivery |
| `approval_granted` / `approval_denied` / `approval_timeout` | Human decision |
| `escalation_triggered` | Uncertainty / policy |
| `unsafe_action_blocked` | Bypass or unsafe LLM action |
| `task_completed` / `task_failed` | Terminal |

---

## Example mock happy trace (conceptual)

```text
TRACE
- task_started: scenario=llm_happy
- llm_request_started: mode=mock prompt_type=draft
- llm_response_received: bytes=128
- llm_parse_passed: format=plain
- draft_created: source=llm_unverified
- critique_completed: result=OK advisory=True
- verification_passed: checks=basic_safety
- approval_requested: mode=mock
- approval_granted: source=scenario
- task_completed: decision=DELIVERED
```

---

## Example malformed trace

```text
- llm_request_started: mode=mock
- llm_response_received: bytes=0
- llm_parse_failed: reason=empty_output
- verification_failed: reason=no_draft
- task_failed: decision=FAILED
```

---

## Review checklist

- [ ] LLM events before verification
- [ ] No task_completed without approval on delivery path
- [ ] Malformed path has no approval_granted
- [ ] advisory flag on critique from LLM

Reference: [agent-builder-kit/trace-templates/](../../agent-builder-kit/trace-templates/)

---

## Diagram

[diagrams/llm-boundary.md](diagrams/llm-boundary.md)
