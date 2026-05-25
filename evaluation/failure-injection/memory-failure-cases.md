# Memory Failure Cases

Demo: `prototypes/bounded-memory-agent/`

---

## Case 1: Over Character Limit

**Inject:**

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario over-limit
```

**Expected:** memory_write_rejected; snapshot unchanged

---

## Case 2: Unverified Writeback

**Inject:**

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario unverified-writeback
```

**Expected:** no write; verification_failed path

---

## Case 3: Snapshot Rollback

**Inject:**

```powershell
python prototypes/bounded-memory-agent/minimal-demo.py --scenario snapshot-rollback
```

**Expected:** prior snapshot intact; failure auditable

---

## Case 4: Mid-Session Injection (Conceptual)

**Anti-pattern:** Inject memory mid-loop without verification

**Expected in governed system:** reject — see `agent-os/09_antipatterns/mid-session-memory-injection.md`

**Check:** bounded-memory demo has no unguarded inject path

---

## Regression Watch

- Silent truncation instead of reject
- Raise limit without governance doc
- Write on verification_failed
