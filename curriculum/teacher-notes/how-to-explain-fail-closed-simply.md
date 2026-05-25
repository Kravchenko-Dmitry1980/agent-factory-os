# How to Explain Fail-Closed Simply

> If we're **not sure it's safe**, we **don't do it**.

## Examples students understand

- ATM won't dispense if balance unclear — not "best guess withdraw"
- Door stays locked if ID scan fails — not "probably fine"

## Contrast

**Fail-open:** "Try anyway" — fast until disaster.  
**Fail-closed:** "Stop" — slower, auditable.

## Demo

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
```

Ask: "Did money leave?" → No. Good.

Lesson: [../lessons/lesson-fail-closed.md](../lessons/lesson-fail-closed.md)
