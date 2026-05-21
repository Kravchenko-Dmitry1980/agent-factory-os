# Coordination

## Definition

**Multi-agent coordination** is the layered stack of patterns — background tasks, coordinator-worker hierarchies, swarm peers — unified by the task state machine and SendMessage protocol.

## Key Ideas

- Background bash/agents: fire-and-forget with disk-streamed output.
- Coordinator mode: manager spawns workers, aggregates results, bubble permissions.
- Swarm: named in-process teammates via SendMessage({to: name}).
- Remote agents bridge to Claude Code Runtime environments.

## Architecture Implications

- Messages queued to running agents; not injected mid-tool-execution.
- Coordinator system prompt slimmed — usage covered at coordinator level.
- Dream tasks: speculative background thinking while awaiting user input.

## Production Implications

- Wide tasks (40-file refactor) need parallelism — single thread hits ceiling.
- Flat task store scales to dozens concurrent; eviction prevents memory leak.
- Worker isolation (worktree) prevents conflicting edits on same files.

## Related Concepts

- [[orchestration]]
- [[swarms]]
- [[synchronization]]
- [[role-systems]]

## Sources

- `Books/claude/ch10-coordination.md`

## My Notes

