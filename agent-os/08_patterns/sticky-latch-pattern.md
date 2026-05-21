# Sticky Latch Pattern

## Definition

The **sticky latch pattern** uses three-state booleans (`boolean | null`) where once a cache-key-affecting feature activates, its contribution stays active for the session — preventing mid-session toggles from busting prompt cache.

## Key Ideas

- null = not evaluated; true = latched on (never returns false).
- Applied to beta headers, fast mode, cache editing, thinking clear, post-compaction telemetry.
- Evaluated at API request construction, not at UI toggle time.

## Architecture Implications

- Pair with external prompt cache you do not control (Anthropic server-side).
- Alternative "always send all headers" creates unrecognized cache namespaces.
- Session-stable configuration invariant for API layer.

## Production Implications

- Mid-session feature flip without latches → 50–70K token cache miss.
- Document latch fields in bootstrap state reviews.

## Related Concepts

- [[prompt-cache-as-constraint]]
- [[api-layer]]
- [[two-tier-state]]

## Sources

- `Books/claude/ch03-state.md`
- `Books/claude/ch04-api-layer.md`

## My Notes

