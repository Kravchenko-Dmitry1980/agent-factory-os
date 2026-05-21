# Hooks Lifecycle

## Definition

**Hooks lifecycle** encompasses 27 distinct events across four execution types — shell, single-shot LLM, multi-turn agent, HTTP webhook — where user-defined interceptors can observe, modify, or block behavior.

## Key Ideas

- Four execution types: shell commands, LLM prompts, agent conversations, HTTP webhooks.
- PreToolUse: block tools before permission prompt.
- PostToolUse: modify results after execution.
- Stop hooks: evaluate completion; can force loop continuation.
- Snapshot frozen at setup — post-start config changes ignored.

## Architecture Implications

- Permission system partially implemented through PreToolUse hooks.
- Stop hooks can end entire query loop or inject blocking errors.
- Hook rules match tool name + optional content patterns.

## Production Implications

- Malicious hook config blocked by frozen snapshot + trust boundary.
- Hook-induced token injection caused infinite error loops — guarded in query loop.
- Extension point for enterprise policy without forking core runtime.

## Related Concepts

- [[harness-mechanisms]]
- [[stop-hooks]]
- [[permission-modes]]

## Sources

- `Books/claude/ch01-architecture.md`
- `Books/claude/ch06-tools.md`

## My Notes

