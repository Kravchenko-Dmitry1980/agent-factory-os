# Verification Failure Types

| Type | Observable signal | Canonical event |
|------|-------------------|-----------------|
| **Malformed output** | Parse error, schema miss | `llm_malformed_output`, `verification_failed` |
| **Partial correctness** | Format OK, facts wrong | `verification_passed` (format only) — warn in trace |
| **Hallucinated structure** | Invented fields | `verification_failed` |
| **GUI mismatch** | Outcome B or C | `verification_failed`, `unsafe_action_blocked` |
| **Approval bypass** | Execute without approval event | anti-pattern `auto_approved` |
| **Silent failure** | No verify event, terminal success | anti-pattern `silent_complete` |

## LLM-Specific (Phase 2.2)

From `integrations-real/llm-verification-adapter/`:

- Timeout → `llm_timeout` → escalate
- JSON parse fail → `llm_malformed_output` → reject
- Low confidence → uncertain → escalate

**Reminder in trace:** `LLM output != truth`

## GUI-Specific

A/B/C taxonomy (`agent-os/00_foundations/visual-verification.md`):

- Only **A** may advance goal
- **B** = wrong screen → replan
- **C** = no change → bounded retry
