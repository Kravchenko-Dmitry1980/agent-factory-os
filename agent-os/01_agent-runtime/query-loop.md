# Query Loop

## Definition

The **query loop** (`query()`) is the single async generator that runs every agent interaction: streams model output, executes tools, manages context compression, recovers from errors, and returns a typed terminal reason.

## Key Ideas

- ~1,700 lines, one code path for REPL, SDK, subagents, headless.
- Outer wrapper tracks queued commands; inner `queryLoop()` does the work.
- State object reconstructed at every `continue` — immutable transitions in mutable loop.
- `querySource` discriminant (`repl`, `sdk`, `agent:xyz`, `compact`) gates behavior.

## Architecture Implications

- Deps injection: `callModel`, compactor, microcompactor, UUID — test seam.
- Config snapshotted once at entry; not re-read mid-loop.
- Four compression layers run before each API call in fixed order.

## Production Implications

- 10 terminal states, 7 continue reasons — full observability taxonomy.
- Withholding recoverable errors prevents SDK consumers from disconnecting mid-recovery.
- Death spiral guards: reactive compact once, max-output recovery ×3, auto-compact circuit breaker ×3.

## Related Concepts

- [[execution-loops]]
- [[generator-loop-pattern]]
- [[context-compression]]
- [[error-recovery-ladder]]
- [[terminal-states]]
- [[streaming-tool-executor]]
- [[gui-agent-loop]] (GUI modality parallel golden path)

## Sources

- `Books/claude/ch05-agent-loop.md`

## My Notes

