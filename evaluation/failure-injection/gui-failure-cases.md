# GUI Failure Cases

Demos: `prototypes/gui-verification-loop/`, `prototypes/integrations/gui-safe-action-workflow/`

---

## Case 1: Screen Mismatch

**Inject:**

```powershell
python prototypes/gui-verification-loop/minimal-demo.py --scenario mismatch
```

**Expected:** verification_failed, unsafe_action_blocked, no click

**Trace:** `observability/examples/unsafe-gui-action-trace.txt`

---

## Case 2: Uncertain Visual State

**Inject:**

```powershell
python prototypes/gui-verification-loop/minimal-demo.py --scenario uncertain
```

**Expected:** block; uncertainty logged

---

## Case 3: Happy Match (Control)

**Inject:**

```powershell
python prototypes/gui-verification-loop/minimal-demo.py --scenario match
```

**Expected:** verification_passed before action

---

## Case 4: Unverified Click Attempt (Conceptual)

**Anti-pattern:** Click coordinates without snapshot

**Expected:** blocked in governed workflow

**Check:** gui-safe-action-workflow demo requires verification step

---

## Regression Watch

- Remove visual check, keep click
- Uncertain → proceed anyway
- Screenshot-only without semantic check (brittle automation)
