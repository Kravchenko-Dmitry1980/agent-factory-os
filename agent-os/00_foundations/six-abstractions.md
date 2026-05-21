# Six Abstractions

## Definition

The **six abstractions** are the core structural pillars of a production agent runtime: Query Loop, Tool System, Tasks, State, Memory, and Hooks — everything else supports these.

## Key Ideas

| Abstraction | Role |
|-------------|------|
| Query Loop | Async generator heartbeat; yields messages, returns terminal reason |
| Tool System | 40+ self-describing tools with permissions and rendering |
| Tasks | Background work units; subagents as state machines |
| State | Two-tier: bootstrap singleton + reactive AppState |
| Memory | CLAUDE.md, MEMORY.md, LLM relevance selection |
| Hooks | 27 lifecycle events; can block tools and stop loop |

## Architecture Implications

- Circular dependency: loop ↔ tools ↔ tasks ↔ hooks ↔ state ↔ memory is intentional.
- Memory injects into system prompt at session start; hooks intercept PreToolUse and Stop.
- Tasks spawn recursive `query()` with isolated message history.

## Production Implications

- Changing any abstraction affects all others — the loop touches every subsystem.
- Feature flags and compile-time elimination strip unused paths from shipped binaries.
- Multi-provider API layer stays transparent to loop and tools.

## Related Concepts

- [[what-is-an-agent]]
- [[golden-path]]
- [[query-loop]]
- [[tool-runtime]]
- [[hooks-lifecycle]]

## Sources

- `Books/claude/ch01-architecture.md`

## My Notes

