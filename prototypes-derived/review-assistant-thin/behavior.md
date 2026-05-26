# Behavior — Review Assistant Thin

## Flow

```text
task_started
  → draft_created
  → critique_completed (advisory)
  → verification_passed | verification_failed
  → approval_requested (if verification passed)
  → approval_granted | approval_denied | approval_timeout
  → task_completed | task_failed
```

Special paths:

- **critic_uncertain:** `escalation_triggered` after critique; delivery only if approval granted (scenario uses missing approval → no delivery)
- **bad_draft:** verification fails before approval matters
- **unsafe_publish_attempt:** `unsafe_action_blocked` immediately — no draft path

## Rules

1. **Critique is advisory** — OK does not mean deliver without approval
2. **Verification is mandatory** — failure stops pipeline
3. **Human approval simulated by scenario** — no auto-approve on timeout
4. **Fail-closed** — missing approval, uncertainty without approval, verification fail → no delivery
5. **Trace always printed** — every step emits an event line

## Mock LLM flow (Phase 3.2)

```text
task_started
  → llm_request_started
  → llm_response_received | llm_timeout
  → llm_parse_passed | llm_parse_failed | llm_uncertain | llm_unsafe_output
  → draft_created (if parse ok)
  → verification → approval → task_completed | task_failed
```

**No LLM bypass:** parse/safety failures never reach approval.

## Rules (LLM)

6. **LLM output is untrusted** — same as critic advisory
7. **No fallback draft on timeout**
8. **Unsafe LLM output blocked before verification**

## Mock only

Draft from local dict payloads. See [llm_boundary.md](llm_boundary.md). No network.
