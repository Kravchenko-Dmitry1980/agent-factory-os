# GUI Safe Action Workflow

**Composes:** GUI verification + fail-closed execution + approval boundaries.

Mock environment only — no ADB, browser, or emulator.

## Flow

```
observe → proposed action → visual verification → approval gate → execute/reject
```

## Run

```powershell
python prototypes/integrations/gui-safe-action-workflow/minimal-demo.py
python prototypes/integrations/gui-safe-action-workflow/minimal-demo.py --scenario mismatch
python prototypes/integrations/gui-safe-action-workflow/minimal-demo.py --scenario no-approval
python prototypes/integrations/gui-safe-action-workflow/minimal-demo.py --scenario uncertain
```
