# Golden Path Sequence

End-to-end sequence from user message to rendered output.

```mermaid
sequenceDiagram
    participant U as User
    participant Q as Query Loop
    participant M as Model API
    participant SE as Streaming Executor
    participant T as Tool System

    U->>Q: UserMessage
    Q->>Q: Token check / compact
    Q->>M: Stream request
    M-->>Q: Tokens + tool_use blocks
    M-->>SE: Start safe tools early
    SE->>T: Execute concurrent reads
    T-->>SE: Results
    Q->>T: Execute remaining tools
    T-->>Q: ToolResultMessages
    Q->>U: Yield messages
    Q->>Q: Continue or terminate
```

## Related Concepts

- [[golden-path]]
- [[streaming-tool-executor]]
- [[tool-runtime]]

## Sources

- `Books/claude/ch01-architecture.md`

## My Notes

