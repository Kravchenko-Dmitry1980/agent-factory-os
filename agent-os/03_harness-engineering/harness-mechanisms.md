# Harness Mechanisms

## Definition

**Harness mechanisms** are the concrete runtime components that enforce harness policy: 14-step tool pipeline, permission resolution chain, hook system, result budgeting, and stop hook orchestration.

## Key Ideas

- PreToolUse hooks can deny, modify input, inject context, or stop execution.
- PostToolUse hooks can modify output or block continuation.
- Permission chain: hook → rules → tool.checkPermissions → mode → prompt/classifier.
- Speculative classifier starts in parallel for Bash to hide latency.

## Architecture Implications

- Hook snapshot frozen at setup — disk changes after start ignored.
- Input backfill clones input — original preserved for transcript stability.
- PermissionDenied hooks run after denial for telemetry/extension.

## Production Implications

- AST parse failure on Bash → fail-safe hook always runs.
- `.claude/` edits classifierApprovable; path bypass attempts not approvable.
- 27 hook event types across 4 execution types (shell, LLM, agent, HTTP).

## Related Concepts

- [[harness-interface]]
- [[hooks-lifecycle]]
- [[execution-verification]]
- [[tool-runtime]]

## Sources

- `Books/claude/ch06-tools.md`
- `Books/claude/ch01-architecture.md`

## My Notes

