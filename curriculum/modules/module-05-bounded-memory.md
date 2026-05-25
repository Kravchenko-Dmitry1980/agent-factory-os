# Module 05 — Bounded Memory

## Goal

Keep memory **limited**, **verified**, and **recoverable** via frozen snapshot.

## Simple Explanation

Memory is not "everything the model ever said." We keep a **curated snapshot** plus small verified durable notes — with a character limit.

## Key Ideas

- Frozen memory snapshot at session start
- Verification before writeback
- Reject overflow — no silent truncate
- Mid-session injection is dangerous

## Files to Read

- `agent-os/doctrine/bounded-memory.md`
- `agent-os/02_memory/frozen-memory-snapshot.md`
- [../lessons/lesson-memory-boundaries.md](../lessons/lesson-memory-boundaries.md)

## Commands to Run

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario happy
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback
```

## Exercise

Observe three scenarios; note audit differences (no code changes).

## Common Mistakes

- Unbounded context "because model is smart"
- Writing agent output to memory without verification
- Truncating instead of rejecting

## Checkpoint Questions

1. What is frozen snapshot?
2. What happens on overflow scenario?
3. Why reject unverified writeback?

## Expected Outcome

Student states max-size rule and verification rule in own words.
