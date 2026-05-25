# Fail-Closed Defaults

## Definition

**Fail-closed defaults** initialize new tools and classifications to the safest behavior until explicitly overridden — serial execution, write-assumed, hook on parse failure.

## Key Ideas

- buildTool(): isParallelSafe false, isReadOnly false by default.
- partitionToolCalls: parse failure → serial batch.
- Bash AST failure → matcher returns always-run hook (fail-safe).

## Architecture Implications

- Safe defaults + explicit opt-in to concurrency and read-only hints.
- checkPermissions default allow is OK — runs after general permission layer.
- MCP readOnlyHint is opt-in unsafe hint from server (trust boundary).

## Production Implications

- Forgotten concurrency flag → slower but safe, not corrupted state.
- Security reviews focus on opt-in unsafe paths, not every new tool.

## Related Concepts

- [[self-describing-tools]]
- [[tool-runtime]]
- [[permission-modes]]
- [[fail-closed-agent-loop]]

## Sources

- `Books/claude/ch06-tools.md`
- `Books/claude/ch07-concurrency.md`

## My Notes

