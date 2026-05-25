# Bounded Memory — Memory Model

## Stores

| Store | Scope | Write policy |
|-------|-------|--------------|
| **Durable store** | Cross-session | Verified writes only |
| **Session snapshot** | Current session | Frozen at bootstrap |
| **Working context** | Current turn | Explicit load, bounded |

## Snapshot Semantics

1. At session start: load curated memory → create **frozen snapshot**
2. Mid-session writes go to durable store but **do not mutate snapshot**
3. Agent sees snapshot unless explicit recall tool loads fresh slice

## Limits

- `MAX_MEMORY_CHARS = 2000` (demo default)
- Overflow → reject write, log failure
- Reset policy: new session = new snapshot

## Writeback Gate

```
proposed_memory → verify(source, consistency) → (pass) → durable write
                                              → (fail) → discard + audit
```

No silent append. No mid-session snapshot injection.
