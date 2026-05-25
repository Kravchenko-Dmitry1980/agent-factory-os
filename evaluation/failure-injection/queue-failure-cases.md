# Queue Failure Cases

Demos: `prototypes/queue-orchestration/`, `integrations-real/local-queue-worker/`

---

## Case 1: Transient Failure (Retry)

**Inject:**

```powershell
python prototypes/queue-orchestration/minimal-demo.py --scenario retry
```

**Expected:** retry_triggered, bounded count, eventual resolve or continue

---

## Case 2: Retry Exhaustion

**Inject:**

```powershell
python prototypes/queue-orchestration/minimal-demo.py --scenario exhausted
```

**Expected:** retry_exhausted at max; no unbounded loop

---

## Case 3: Escalation After Storm

**Inject:**

```powershell
python prototypes/integrations/escalation-workflow/minimal-demo.py
```

**Expected:** escalation_triggered; unsafe_action_blocked on auto-complete

**Trace:** `observability/examples/escalation-trace.txt`

---

## Case 4: Queue Recovery After Crash

**Inject:**

```powershell
python integrations-real/local-queue-worker/minimal-demo.py
```

**Expected:** queue_recovered or equivalent; pending tasks preserved

**Trace:** `observability/examples/queue-recovery-trace.txt`

---

## Case 5: Corrupted State (Manual Concept)

**Conceptual:** Inspect `.data/local-queue-worker/` after crash simulation

**Expected:** Worker refuses silent skip; audit shows recovery decision

**Note:** Do not commit corrupted state files — local `.data/` only

---

## Regression Watch

- MAX_RETRIES constant increase
- Remove escalation on exhausted
- Mark failed task as completed
