# Stateful Systems

## Definition

A **stateful agent system** maintains process-scoped and session-scoped data across turns: message history, configuration, cost metrics, permission mode, and UI-reactive state — with explicit tiers for access patterns.

## Key Ideas

- Long-running agents cannot use a single global reactive store — infrastructure state changes rarely; UI state changes constantly.
- **Two-tier state**: mutable process singleton (bootstrap) + minimal reactive store (AppState).
- State bridges via centralized **onChange side effects**, not scattered notifications.
- Some fields intentionally **duplicate across tiers** (e.g., model name) to preserve dependency direction.

## Architecture Implications

- Bootstrap state must be a **DAG leaf** — importable before React, plugins, or services.
- Reactive store uses updater functions `(prev) => next` and `Object.is` equality to prevent spurious renders.
- Context builders (git status, CLAUDE.md) memoize once per session to avoid prompt cache busting.

## Production Implications

- Ungoverned global state busts 50K+ token prompt caches and creates import cycles.
- Sticky latches on beta headers prevent mid-session cache invalidation from feature toggles.
- Process-exit persistence is acceptable for diagnostic counters; not for transactional data.

## Related Concepts

- [[two-tier-state]]
- [[sticky-latch-pattern]]
- [[shared-state]]
- [[bootstrap-pipeline]]

## Sources

- `Books/claude/ch03-state.md` — two-tier architecture

## My Notes

