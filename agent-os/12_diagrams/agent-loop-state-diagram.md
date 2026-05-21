# Agent Loop State Diagram

Single iteration of the query loop — context pipeline through tool execution and termination checks.

```mermaid
stateDiagram-v2
    [*] --> ContextPipeline: Destructure state

    ContextPipeline --> ModelStreaming: Messages ready
    note right of ContextPipeline
        Tool result budget
        Snip → Microcompact
        Collapse → Auto-compact
    end note

    ModelStreaming --> PostStream: Stream complete
    ModelStreaming --> ErrorHandling: Exception

    PostStream --> DoneCheck: No tool use
    PostStream --> ToolExecution: Has tool use

    DoneCheck --> Terminal_Complete: Pass checks
    DoneCheck --> ContextPipeline: Recovery needed

    ToolExecution --> ContextPipeline: Continue loop
    ToolExecution --> Terminal_Abort: Abort / hook stop

    ErrorHandling --> Terminal_Error: Unrecoverable
    ErrorHandling --> ContextPipeline: Retry path
```

## Related Concepts

- [[query-loop]]
- [[context-compression]]
- [[error-recovery-ladder]]
- [[terminal-states]]

## Sources

- `Books/claude/ch05-agent-loop.md`

## My Notes

