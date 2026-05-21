# Streaming Tool Executor

## Definition

The **streaming tool executor** performs speculative execution: starting concurrency-safe tools as soon as `tool_use` blocks are parseable during model response streaming.

## Key Ideas

- Does not wait for full model response before starting safe tools.
- Overlaps 2–3s model streaming with I/O-bound reads/greps.
- Invalidated speculative results discarded if model changes intent (rare).
- Disabled or constrained when non-streaming fallback would double-execute tools.

## Architecture Implications

- Integrates with `callModel()` streaming loop in query iteration.
- Requires accurate `isConcurrencySafe(input)` on each tool definition.
- Drains remaining queued tools on abort with synthetic tool_results.

## Production Implications

- Largest free latency win in typical multi-tool turns.
- Fallback to batch orchestration after stream completes for remaining tools.
- Corporate proxy mid-stream failures interact with idle watchdog (90s) and fallback.

## Related Concepts

- [[concurrency]]
- [[query-loop]]
- [[golden-path]]

## Sources

- `Books/claude/ch01-architecture.md`
- `Books/claude/ch07-concurrency.md`

## My Notes

