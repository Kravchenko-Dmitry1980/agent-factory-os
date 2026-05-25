# Bounded Memory — Governance

| Rule | Enforcement |
|------|-------------|
| Bounded size | Char limit on durable store |
| Frozen snapshot | Immutable for session duration |
| Verification before writeback | `verified=True` required |
| Explicit context load | `load_context()` not implicit merge |
| Reset on new session | `reset_session()` clears snapshot |

## Alignment

- `agent-os/02_memory/memory-char-limits.md`
- `agent-os/02_memory/frozen-memory-snapshot.md`
- `prototypes/governance/prototype-boundaries.md`

## Forbidden

- Auto-growing vector memory
- Mid-session prompt injection of new memory blocks
- Writeback from unverified agent output
