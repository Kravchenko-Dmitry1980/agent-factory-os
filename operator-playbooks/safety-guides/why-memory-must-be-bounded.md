# Why Memory Must Be Bounded

Unbounded memory = silent context drift, cost explosion, and unreviewed "facts" accumulating forever.

---

## Problems without bounds

- Old wrong answers persist
- Prompt grows until failures are mysterious
- No clear snapshot to rollback to

---

## Our approach

- **Frozen snapshot** at session start
- **Character limits** on durable memory
- **Verification before writeback**
- Reject overflow — no silent truncate

---

## Demo

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
```

Doctrine: `agent-os/doctrine/bounded-memory.md`

Anti-pattern: `agent-os/09_antipatterns/unbounded-memory-growth.md`
