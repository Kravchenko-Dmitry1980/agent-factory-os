# API Layer

## Definition

The **API layer** transforms session state into provider-agnostic streaming HTTP requests — system prompt construction, cache scopes, beta headers, message normalization, retries, and watchdog streaming.

## Key Ideas

- `getAnthropicClient()` factory: Direct, Bedrock, Vertex, Azure — single interface.
- System prompt split at **dynamic boundary**: static (global cache) vs dynamic (per-session).
- `DANGEROUS_uncachedSystemPromptSection` naming forces documentation of cache-breaking sections.
- Idle watchdog: 90s no chunks → abort stream → non-streaming fallback.

## Architecture Implications

- Conditional sections before boundary multiply cache variants as 2^N — runtime bits forbidden in static prefix.
- Sticky latches evaluated at request construction for session-stable beta headers.
- Output cap default 8K; one retry at 64K on hit (<1% requests).

## Production Implications

- Prompt cache is largest cost lever — architectural constraint, not feature toggle.
- Corporate proxies cause HTTP 200 non-SSE bodies — fallback required.
- Client request ID header enables timeout correlation with server logs.

## Related Concepts

- [[prompt-cache-as-constraint]]
- [[sticky-latch-pattern]]
- [[query-loop]]
- [[cache-busting-sections]]

## Sources

- `Books/claude/ch04-api-layer.md`

## My Notes

