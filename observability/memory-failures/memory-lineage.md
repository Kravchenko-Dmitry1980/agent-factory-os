# Memory Lineage

```
session_start → snapshot_frozen
  → context_load (optional explicit)
  → execute → critique → verification
  → memory_write_accepted | memory_write_rejected
  → (next session) session_reset → new snapshot
```

## parent_id Usage

Link write attempt to verifying event:

```
e10 verification_passed
e11 memory_write_accepted parent=e10
```

## Question for Postmortem

> Was the write rejected? If yes, did anything still persist?

Answer must come from lineage, not model chat history.
