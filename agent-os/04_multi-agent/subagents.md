# Subagents

## Definition

**Subagents** are child agent instances spawned via the Agent tool — each runs an independent `query()` loop with isolated message history, tool pool, permission boundary, and abort controller.

## Key Ideas

- Parent sees final output only — not child internal reasoning (unless transcript injected).
- Sync vs async: `run_in_background`, agent definition, coordinator, proactive force async.
- Isolation: git worktree or remote session for parallel filesystem safety.
- Recursive guard prevents fork-of-fork pathologies.

## Architecture Implications

- `runAgent()` 15-step lifecycle: pure execution; routing in AgentTool.call().
- Dynamic schema via feature flags — model never sees unusable parameters.
- Worker tool pool assembled per agent definition; MCP servers waited up to 30s.

## Production Implications

- Bubble permission mode mandatory for headless children.
- outputFile path for async results — filesystem IPC survives restarts.
- Named agents (`name` field) enable SendMessage routing in swarms.

## Related Concepts

- [[task-state-machine]]
- [[coordination]]
- [[swarms]]
- [[permission-modes]]

## Sources

- `Books/claude/ch08-sub-agents.md`

## My Notes

