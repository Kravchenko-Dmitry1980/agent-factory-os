# Memory Gate

**Question:** Did memory writeback remain controlled and bounded?

---

## Checks

- [ ] Under limit + verified → write allowed
- [ ] Over limit → memory_write_rejected
- [ ] Unverified → no writeback
- [ ] Rollback preserves snapshot
- [ ] No mid-session unbounded injection

## Commands

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario under-limit
python prototypes/bounded-memory-agent/minimal-demo.py --scenario over-limit
python prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback
python prototypes/bounded-memory-agent/minimal-demo.py --scenario snapshot-rollback
```

## Pass

- Verification before write on happy path
- Explicit reject on violation paths
- Size stays within MAX budget

## Fail

- Silent truncate without event
- Write after verification_failed
- Snapshot corruption without audit

## Doctrine link

`agent-os/doctrine/bounded-memory.md`, `verification-before-writeback`
