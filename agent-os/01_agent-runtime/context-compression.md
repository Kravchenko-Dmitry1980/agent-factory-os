# Context Compression

## Definition

**Context compression** is the layered reduction of message history before each API call — from light trimming to full conversation summarization — preserving cache efficiency and avoiding hard limits.

## Key Ideas

| Layer | Operation |
|-------|-----------|
| 0 Tool result budget | Per-message size limits |
| 1 Snip compact | Physically remove old messages |
| 2 Microcompact | Remove tool results by tool_use_id |
| 3 Context collapse | Replace spans with summaries |
| 4 Auto-compact | Fork conversation to summarize history |

- Order matters: collapse before auto-compact may make auto-compact a no-op.
- Auto-compact threshold: effectiveWindow − 13,000 tokens; blocking limit − 3,000.
- Circuit breaker: 3 consecutive auto-compact failures → stop trying.

## Architecture Implications

- Cached microcompact defers boundary message until API reports `cache_deleted_input_tokens`.
- Reactive compact catches 413 after proactive compact fails.
- Compact agent uses `querySource: 'compact'` to avoid blocking limit deadlock.

## Production Implications

- Infinite compact-fail-retry observed at 250K API calls/day without circuit breaker.
- Token counting mixes authoritative API counts + conservative estimates for new messages.
- Thinking blocks have inviolable preservation rules across compaction.

## Related Concepts

- [[query-loop]]
- [[memory-compaction]]
- [[error-recovery-ladder]]

## Sources

- `Books/claude/ch05-agent-loop.md`

## My Notes

