# Execution Feedback

## Definition

**Execution feedback** is harness-mediated information returned to the model after tool runs or verification — results, blocking errors, stop hook messages, memory writes, and budget nudges that shape the next loop iteration.

## Key Ideas

- Tool results as structured tool_result messages referencing tool_use IDs.
- Stop hook blocking errors force continuation when "done" was premature.
- Token budget nudge injects remaining budget on continuation.
- Episodic memory writes capture validated feedback across sessions.

## Architecture Implications

- Feedback enters message history — model reasoned over on next turn.
- Withheld errors excluded from stream until recovery fails ([[withholding-errors]]).
- newMessages and contextModifier extend feedback beyond raw tool output.

## Production Implications

- Noisy feedback (duplicate notifications) confuses model — use `notified` guards.
- Feedback loops without limits → [[infinite-retry-loops]].

## Related Concepts

- [[feedback-loops]]
- [[execution-verification]]
- [[stop-hooks]]
- [[episodic-memory]]

## Sources

- `Books/claude/ch05-agent-loop.md`
- `Books/claude/ch06-tools.md`
- `Books/claude/ch11-memory.md`

## My Notes

