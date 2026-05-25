# Cursor Operator Path

---

## Goal

Use Cursor effectively **inside** this repo: run demos, read traces, evaluate changes, avoid unsafe AI-assisted refactors.

## Estimated Time

1 day

---

## What to Read

1. [../start-here/first-2-hours.md](../start-here/first-2-hours.md)
2. [../governance/no-blind-patching.md](../governance/no-blind-patching.md)
3. [../change-guides/how-to-change-safely.md](../change-guides/how-to-change-safely.md)
4. `agent-os/04_multi-agent/subagent-tool-restrictions.md` (if using subagents)

---

## What to Run

Daily operator bundle:

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/summarize_evaluation_status.py
```

Before any AI-suggested code change to prototypes:

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
# make change
python evaluation/scripts/run_demo_smoke_checks.py
```

---

## What to Avoid

- Asking AI to "refactor prototypes into a framework"
- Accepting large diffs without running smoke checks
- Letting AI remove approval gates for "simplicity"
- Auto-committing without human review of gate logic

---

## Expected Outcome

- Comfortable running demos from PowerShell in repo root
- Uses evaluation scripts after AI-assisted edits
- Knows when to reject AI suggestions (gate removal, shared runtime)

---

## Checkpoint Questions

1. What should you run after Cursor changes prototype code?
2. Why should AI not merge shared orchestration?
3. Where is the red-flag checklist?

Answer: [../../evaluation/manual-review/red-flag-checklist.md](../../evaluation/manual-review/red-flag-checklist.md)
