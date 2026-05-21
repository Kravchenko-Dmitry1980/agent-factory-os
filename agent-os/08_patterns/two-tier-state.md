# Two-Tier State

## Definition

The **two-tier state pattern** splits process infrastructure state (mutable singleton, pre-React) from UI-reactive state (immutable snapshots, subscribers) bridged by centralized onChange side effects.

## Key Ideas

- Tier 1 bootstrap: ~80 fields, getter/setter access, DAG leaf module.
- Tier 2 AppState: ~34-line store, updater functions, Object.is guard.
- Controlled duplication (e.g., model name) bridged by onChangeAppState diff handler.

## Architecture Implications

- API client reads bootstrap; React reads AppState — never cross-import.
- Memoized context builders cache in bootstrap to break circular deps.
- Signals for rare bootstrap events (sessionSwitched) without full pub/sub framework.

## Production Implications

- Single reactive store for cost telemetry → full tree reconcile every API call.
- ESLint enforces bootstrap import restrictions.

## Related Concepts

- [[stateful-systems]]
- [[sticky-latch-pattern]]
- [[feedback-loops]]

## Sources

- `Books/claude/ch03-state.md`

## My Notes

