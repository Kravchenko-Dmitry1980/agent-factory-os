# Agent Loop

## Definition

The **agent loop** is the repeated model→tool→result cycle at the heart of every agent runtime. In this knowledge base, the canonical deep dive is [[query-loop]].

## Key Ideas

- Single code path (`query()`) for REPL, SDK, subagents, headless.
- Async generator with typed terminal return.
- Four compression layers before each API call.
- Error recovery ladder with explicit circuit breakers.

## Architecture Implications

- See [[query-loop]] for loop state, transitions, and deps injection.
- Alias note for discoverability (`agent-loop` ↔ `query-loop`).

## Production Implications

- See [[infinite-retry-loops]] for failure modes without limits.

## Related Concepts

- [[query-loop]]
- [[execution-loops]]
- [[generator-loop-pattern]]
- [[agent-loop-state-diagram]]

## Sources

- `Books/claude/ch05-agent-loop.md`

## My Notes

