# Generator Loop Pattern

## Definition

The **generator loop pattern** implements the agent heartbeat as an async generator — yielding messages/events and returning a typed terminal reason — instead of callbacks or event emitters.

## Key Ideas

- Natural backpressure: consumer pulls via `for await`.
- Clean cancellation via `.return()` on generator.
- Composability: `yield*` delegates to sub-generators (stop hooks, tool runners).
- Lazy start: body runs on first `.next()`, not at construction.

## Architecture Implications

- Replace callback chains and promise nesting in agent loops.
- Retry wrappers as generators yielding status events (`SystemAPIErrorMessage`).
- Terminal union type documents all exit reasons for callers.

## Production Implications

- SDK and REPL share one loop implementation — no behavioral drift.
- Cannot rewind generator — acceptable for forward-only agents.

## Related Concepts

- [[query-loop]]
- [[execution-loops]]
- [[withholding-errors]]

## Sources

- `Books/claude/ch01-architecture.md` — Apply This
- `Books/claude/ch05-agent-loop.md`

## My Notes

