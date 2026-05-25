# Memory Impact

## Sensitive Changes

- Increase `MAX_MEMORY_CHARS` without overflow tests
- Allow mid-session snapshot mutation
- Remove `verified=True` requirement
- Auto-writeback on critic pass
- Implicit context merge (no `context_load` event)

## Side Effects

| Change | Symptom |
|--------|---------|
| Larger limit | Slower sessions, cache pressure |
| Snapshot mutation | Non-deterministic replay |
| Unverified write | Durable hallucination |

## Observability

Must still emit `memory_write_rejected` on failure — see [observability/memory-failures/](../../observability/memory-failures/).

## Rollback Signal

Agents "remember" wrong facts after revert — check durable store + snapshot semantics.
