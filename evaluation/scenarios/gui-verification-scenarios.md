# GUI Verification Scenarios

System under test: `prototypes/gui-verification-loop/`, `prototypes/integrations/gui-safe-action-workflow/`

Run:

```powershell
python prototypes/gui-verification-loop/minimal-demo.py --scenario happy
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-b
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-c
python prototypes/integrations/gui-safe-action-workflow/minimal-demo.py
```

---

## Scenario: Screen Matches Expected State

### System Under Test

`prototypes/gui-verification-loop/minimal-demo.py --scenario happy`

### Input

Expected UI state A; actual screen matches A.

### Expected Behavior

Visual verification passes; click/action allowed (mock).

### Expected Event Trace

```
task_started → verification_passed (visual) → task_completed
```

### Expected Failure Mode

None.

### Pass Criteria

- Action executed (mock)
- Match reason in audit

### Fail Criteria

- Click without verification
- Verification skipped on "obvious" match

### Why This Matters

Even happy path must log visual verification step.

---

## Scenario: Screen Mismatch Blocks Click

### System Under Test

`prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-b`

### Input

Expected state A; actual screen shows B.

### Expected Behavior

Click blocked; fail-closed.

### Expected Event Trace

```
task_started → verification_failed (visual) → unsafe_action_blocked
```

Reference: `observability/examples/unsafe-gui-action-trace.txt`

### Expected Failure Mode

Block — GUI mismatch.

### Pass Criteria

- No click executed
- Mismatch reason visible

### Fail Criteria

- Click on wrong screen
- Mismatch logged but action proceeds

### Why This Matters

GUI automation without visual grounding causes real damage.

---

## Scenario: Uncertain Visual State Blocks Execution

### System Under Test

`prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-c`

### Input

Ambiguous overlay, loading spinner, or partial match.

### Expected Behavior

Treat uncertainty as failure; no action.

### Expected Event Trace

```
task_started → verification_failed (uncertain) → unsafe_action_blocked
```

### Expected Failure Mode

Block — uncertain visual state.

### Pass Criteria

- Action blocked
- Uncertainty explicitly logged

### Fail Criteria

- "Best guess" click
- Uncertainty → pass

### Why This Matters

Visual verification uses A/B/C taxonomy; C (uncertain) must fail closed.
