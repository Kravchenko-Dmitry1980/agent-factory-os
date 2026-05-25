# Approval Failure Cases

Demos: `prototypes/fail-closed-external-action/`, `prototypes/review-loop-agent/`, `integrations-real/telegram-review-gate/`

---

## Case 1: Missing Approval

**Inject:**

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
```

**Expected:** execute denied; approval_timeout or equivalent

---

## Case 2: Explicit Rejection

**Inject:**

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario rejected
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

**Expected:** approval_denied, task_failed, no publish

**Trace:** `observability/examples/failed-review-trace.txt`

---

## Case 3: Bypass Attempt

**Inject:**

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario bypass-attempt
```

**Expected:** blocked; Published: False

---

## Case 4: Telegram Timeout (Mock)

**Inject:**

```powershell
python integrations-real/telegram-review-gate/minimal-demo.py
```

**Expected:** mock mode works; timeout path documented

---

## Case 5: Uncertain Verification + Approval Gap

**Inject:**

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario uncertain
```

**Expected:** deny even if approval somehow set — verification first

---

## Regression Watch

- Auto-approve on timeout
- Internal email exception
- Approve flag default True
