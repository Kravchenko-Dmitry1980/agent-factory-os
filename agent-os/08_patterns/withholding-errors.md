# Withholding Errors

## Definition

The **withholding errors pattern** suppresses recoverable error messages from the agent yield stream until all recovery paths fail — preventing downstream consumers from disconnecting mid-recovery.

## Key Ideas

- SDK/desktop consumers terminate on any message with `error` field.
- Withheld errors pushed to internal assistantMessages buffer for recovery checks.
- Surface only when reactive compact, collapse, escalation exhausted.

## Architecture Implications

- Integrates with error recovery ladder and context compression.
- Separate handling for unrecoverable errors (yield immediately after exhaustion).
- Model fallback tombstones failed attempt messages before retry.

## Production Implications

- Without withholding, recovery loop runs but nobody listens.
- Critical for multi-consumer agent architectures (REPL + SDK + hooks).

## Related Concepts

- [[error-recovery-ladder]]
- [[query-loop]]
- [[infinite-retry-loops]]

## Sources

- `Books/claude/ch05-agent-loop.md`

## My Notes

