# Adaptive Harness

## Definition

An **adaptive harness** adjusts enforcement strictness based on context — permission modes, auto classifier, acceptEdits, plan mode — while preserving session-stable cache and security invariants.

## Key Ideas

- Seven permission modes from `bypassPermissions` to `plan` (most to least permissive).
- `auto` mode: lightweight LLM classifies tool vs transcript consistency.
- Mode changes synced via centralized state diff handler.
- Sticky latches prevent mode toggles from busting prompt cache mid-session.

## Architecture Implications

- Subagents default `bubble` — escalate permissions to parent/user.
- Feature flags gate auto mode, fast mode, cache editing headers.
- GrowthBook experiments for runtime A/B without new binary.

## Production Implications

- `bypassPermissions` internal/testing only — catastrophic in production.
- Mode misconfiguration is security posture — know active mode, not individual checks.
- Classifier two-stage: fast model then extended thinking for ambiguous Bash.

## Related Concepts

- [[permission-modes]]
- [[harness-mechanisms]]
- [[sticky-latch-pattern]]

## Sources

- `Books/claude/ch01-architecture.md`
- `Books/claude/ch03-state.md`
- `Books/claude/ch06-tools.md`

## My Notes

