# Synchronization

## Definition

**Synchronization** in multi-agent systems covers message ordering, tool-round boundaries, context modifier application order, and permission escalation — ensuring coherent shared execution without race-induced corruption.

## Key Ideas

- SendMessage drained at tool-round boundaries — preserves turn structure.
- Concurrent tool batches: context modifiers applied in tool order after batch.
- Serial tools: modifiers applied immediately before next tool.
- Session permission mode synced via centralized onChange diff.

## Architecture Implications

- Parent-child not modeled in task store — sync via conversation + outputFile polling.
- Frozen parent system prompt for fork subagents — re-render could bust cache.
- Bubble mode serializes permission decisions up the hierarchy.

## Production Implications

- Mid-tool message injection would break agent turn assumptions — queued instead.
- Concurrent edits to same file require worktree isolation or serial AgentTool.
- 6 of 8 permission sync paths broken before centralization — sync must be structural.

## Related Concepts

- [[coordination]]
- [[concurrency]]
- [[shared-memory]]

## Sources

- `Books/claude/ch03-state.md`
- `Books/claude/ch07-concurrency.md`
- `Books/claude/ch10-coordination.md`

## My Notes

