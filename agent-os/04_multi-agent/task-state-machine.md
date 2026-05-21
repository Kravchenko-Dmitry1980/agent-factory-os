# Task State Machine

## Definition

The **task state machine** is the unified lifecycle model for all background work — `pending → running → completed | failed | killed` — shared by bash, agents, teammates, workflows, and monitors.

## Key Ideas

- Seven task types; single-char ID prefix (`a`, `b`, `t`, `r`, `w`, `m`, `d`).
- Base state: outputFile, outputOffset, notified, toolUseId, timestamps.
- Flat map in AppState.tasks — no explicit parent-child tree.
- Task interface evolved to `kill()` only — spawn/render not polymorphic.

## Architecture Implications

- `pendingMessages` queue for SendMessage; drained at tool-round boundaries.
- `isBackgrounded` vs born-async distinction affects UI and lifecycle.
- `evictAfter` GC for completed non-retained tasks.

## Production Implications

- `notified` prevents duplicate completion messages to parent.
- ~2.8T ID combinations resist symlink brute-force on output files.
- Kill dispatches by type through minimal registry.

## Related Concepts

- [[orchestration]]
- [[coordination]]
- [[subagents]]

## Sources

- `Books/claude/ch10-coordination.md`

## My Notes

