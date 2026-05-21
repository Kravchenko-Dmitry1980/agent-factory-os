# Shared State

## Definition

**Shared state** is data accessible across agent turns, subagents, or team members — spanning bootstrap singleton fields, AppState task maps, memory directories, and output files for async IPC.

## Key Ideas

- Not all shared state should be reactive — tier by access pattern ([[two-tier-state]]).
- Multi-agent: flat task map; parent-child implicit via toolUseId, not tree store.
- Memory shared at git root across worktrees ([[shared-memory]]).
- Concurrent tools share ToolUseContext read-only; modifiers queued until batch ends.

## Architecture Implications

- Explicit bridges (onChange, outputFile, SendMessage queue) over implicit globals.
- Fork subagents: frozen parent system prompt; isolated message history.
- CLAUDE.md cached in bootstrap breaks classifier circular dependency.

## Production Implications

- Race on concurrent context modifiers → apply in tool order after batch.
- Shared mutable state without isolation → conflicting edits (use worktree isolation).

## Related Concepts

- [[shared-memory]]
- [[stateful-systems]]
- [[synchronization]]
- [[two-tier-state]]

## Sources

- `Books/claude/ch03-state.md`
- `Books/claude/ch07-concurrency.md`
- `Books/claude/ch10-coordination.md`
- `Books/claude/ch11-memory.md`

## My Notes

