# Concurrency

## Definition

**Tool concurrency** is input-dependent parallel execution of independent tool calls, combined with speculative execution during model streaming.

## Key Ideas

- Safety is **per-call**, not per-tool-type: `Bash("ls")` safe, `Bash("rm -rf")` not.
- `partitionToolCalls()` greedily merges consecutive concurrency-safe calls into batches.
- Default max concurrency: 10 (`CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY`).
- StreamingToolExecutor starts safe tools before model finishes response.

## Architecture Implications

- Concurrent batches queue context modifiers; applied in tool order after batch completes.
- Serial batches apply modifiers immediately — Edit then Read sees updated file.
- Parse failure or `isConcurrencySafe` throw → fail-closed to serial.

## Production Implications

- 3–5 tools/turn × 200ms serial = 1s; parallel reads cut to ~200ms wall time.
- Model emission order affects batch count — interleaved writes break parallelism.
- MCP `readOnlyHint` annotation drives concurrency classification (trust boundary).

## Related Concepts

- [[streaming-tool-executor]]
- [[tool-runtime]]
- [[orchestration]]
- [[self-describing-tools]]

## Sources

- `Books/claude/ch07-concurrency.md`

## My Notes

