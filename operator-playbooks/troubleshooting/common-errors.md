# Common Errors

Stay calm. Most issues are: wrong directory, wrong Python, wrong scenario flag, or a real regression after a change.

---

## Step 1: Inspect (Don't Patch)

1. What command did you run?
2. Full error text?
3. Did you change code recently?
4. Are you in repo root?

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python --version
```

---

## Step 2: Route to Guide

| Error type | Guide |
|------------|-------|
| Python won't start | [python-command-fails.md](python-command-fails.md) |
| Demo crashes | [demo-does-not-run.md](demo-does-not-run.md) |
| Trace looks wrong | [trace-does-not-match.md](trace-does-not-match.md) |
| Evaluation FAIL | [evaluation-fails.md](evaluation-fails.md) |
| Queue weird | [queue-behaves-wrong.md](queue-behaves-wrong.md) |
| LLM adapter | [llm-adapter-fails.md](llm-adapter-fails.md) |
| Telegram | [telegram-adapter-fails.md](telegram-adapter-fails.md) |
| FastAPI | [fastapi-adapter-fails.md](fastapi-adapter-fails.md) |

---

## Step 3: Rollback If Needed

If failure started **after your edit**:

→ [../runbooks/rollback-after-failure.md](../runbooks/rollback-after-failure.md)

---

## Step 4: Report

Tell project lead:

- Command
- Expected vs actual
- Whether smoke check fails
- Whether you changed code

No formal ticket system required.

---

## Never Do First

- Mass refactor to "fix" demo
- Increase retry limits
- Remove approval checks
- Add CI to hide flaky checks

See [../governance/no-blind-patching.md](../governance/no-blind-patching.md)
