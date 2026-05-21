# Planning

## Definition

**Planning mode** is a harness state where the agent is read-only: all mutations are blocked while the model explores, analyzes, and proposes a plan before execution.

## Key Ideas

- Permission mode `plan` denies write operations while allowing reads and analysis.
- Plan mode is entered via tools like `EnterPlanMode` that return **context modifiers** changing permission mode.
- Planning separates **exploration** from **execution** — reducing accidental mutations during design phases.
- Explore and Plan built-in agent types optimize for search and planning workloads respectively.

## Architecture Implications

- Context modifiers from non-concurrent-safe tools apply immediately; concurrent batches queue modifiers.
- Plan mode state tracked in bootstrap session flags (e.g., `hasExitedPlanMode`).
- Coordinator and swarm modes may use planning agents as first phase before parallel workers.

## Production Implications

- Users expect explicit transition from plan → act with permission prompts restored.
- Plan-only sessions still consume context window — compaction applies equally.
- Misconfigured plan mode that blocks necessary reads frustrates users — tool `isReadOnly` must be accurate.

## Related Concepts

- [[permission-modes]]
- [[harness]]
- [[subagents]]
- [[tool-runtime]]

## Sources

- `Books/claude/ch01-architecture.md` — plan permission mode
- `Books/claude/ch06-tools.md` — EnterPlanMode context modifier
- `Books/claude/ch08-sub-agents.md` — Explore/Plan agents

## My Notes

