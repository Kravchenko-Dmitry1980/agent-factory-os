# Scattered Permission Sync

## Definition

**Scattered permission sync** is the anti-pattern of notifying external systems from individual mutation sites instead of centralized state diff handlers — guaranteeing drift when new paths are added.

## Key Ideas

- Symptom: 6 of 8 permission mode mutation paths missed remote sync.
- Fix: onChangeAppState detects permission mode diff once.
- "Scattered callsites need zero changes" after centralization.

## Architecture Implications

- Hook store onChange/onTransition for all side effects keyed by field diff.
- Applies to any multi-consumer state (CCR, telemetry, disk persistence).

## Production Implications

- External session metadata diverges silently from UI state.
- New slash command or shortcut introduces regression without structural fix.

## Related Concepts

- [[two-tier-state]]
- [[feedback-loops]]
- [[permission-modes]]

## Sources

- `Books/claude/ch03-state.md`

## My Notes

