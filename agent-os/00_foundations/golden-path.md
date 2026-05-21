# Golden Path

## Definition

The **golden path** is the end-to-end data flow from user input through query loop, model API, tool execution, and rendered output — the thread that connects all agent subsystems.

## Key Ideas

1. User message enters query loop
2. Token check → auto-compact if needed
3. Model streams response; streaming executor starts safe tools early
4. Remaining tools execute through validation → hooks → permissions → execute
5. Tool results append to history; loop continues or terminates

## Architecture Implications

- Generator pattern gives natural backpressure between loop and UI.
- Speculative tool execution overlaps model streaming with I/O-bound reads.
- Entire flow is re-entrant: no separate "tool result phase" — one continuous loop.

## Production Implications

- Permission chain: hook rule → tool.checkPermissions → mode → prompt/classifier.
- Discarded speculative results if model invalidates tool call (rare).
- Tracing one request end-to-end is the primary debugging methodology.

## Related Concepts

- [[query-loop]]
- [[streaming-tool-executor]]
- [[permission-modes]]
- [[six-abstractions]]

## Sources

- `Books/claude/ch01-architecture.md` — sequence diagram

## My Notes

