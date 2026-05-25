# Memory Drift Analysis

## What Operators Report

> "Agent saved it but doesn't remember."

## Often Actually

| Cause | Observable |
|-------|------------|
| Frozen snapshot | Write succeeded, snapshot unchanged mid-session |
| Stale context load | `context_load` without fresh durable slice |
| Unverified write rejected | `memory_write_rejected` — operator didn't see reject |
| Overflow | `memory_write_rejected reason=overflow` |

## Trace Pattern (Drift)

```
memory write accepted (durable)
... agent acts on snapshot only ...
verification_failed (agent used stale fact)
```

## Mitigation Visibility

Log explicitly:

```
snapshot_frozen chars=2000
memory_write_accepted durable_size=450 snapshot_unchanged=true
context_load explicit=true
```

## Not Drift

Verified durable write + documented snapshot semantics = **by design**, not bug.
