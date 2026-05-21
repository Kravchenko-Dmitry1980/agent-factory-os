# Orchestration

## Definition

**Orchestration** is the coordination of multiple execution units — tool batches, background tasks, subagents, swarms — into coherent work with shared state machines, messaging, and termination semantics.

## Key Ideas

- Layers: serial/concurrent tool batches → background tasks → coordinator-worker → swarm peers.
- Unified **Task** abstraction: `pending → running → completed | failed | killed`.
- Parent-child relationships are implicit in conversation flow, not a tree in the task store.
- `SendMessage` queues to running agents; drained at tool-round boundaries.

## Architecture Implications

- Task output streams to disk files; parents read incrementally via `outputOffset`.
- Seven task types share base state; polymorphic interface minimized to `kill()` only.
- Coordinator mode spawns workers with bubble permissions and aggregated result retrieval.

## Production Implications

- Flat task map with prefixed IDs (`a`, `b`, `t`) aids human debugging at scale.
- `notified` flag prevents duplicate completion messages to parent loop.
- Eviction/GC for completed tasks prevents unbounded AppState growth.

## Related Concepts

- [[coordination]]
- [[task-state-machine]]
- [[subagents]]
- [[swarms]]
- [[concurrency]]

## Sources

- `Books/claude/ch07-concurrency.md`
- `Books/claude/ch10-coordination.md`

## My Notes

