# Six Abstractions

Architecture diagram: the six core abstractions of a production agent runtime and their relationships.

```mermaid
graph TD
    User([User]) --> REPL["REPL / UI<br/>Input, display"]
    REPL --> QL["Query Loop<br/>Async generator"]
    QL --> TS["Tool System<br/>40+ self-describing tools"]
    QL --> SL["State Layer<br/>Bootstrap + AppState"]
    TS -->|tool results| QL
    QL -->|spawns| Tasks["Tasks<br/>Sub-agents, state machines"]
    Tasks -->|own query loop| QL
    QL -->|fires| Hooks["Hooks<br/>27 lifecycle events"]
    Hooks -->|PreToolUse: block| TS
    Memory["Memory<br/>CLAUDE.md, MEMORY.md"] -->|system prompt| QL
```

## Related Concepts

- [[six-abstractions]]
- [[golden-path]]
- [[what-is-an-agent]]

## Sources

- `Books/claude/ch01-architecture.md`

## My Notes

