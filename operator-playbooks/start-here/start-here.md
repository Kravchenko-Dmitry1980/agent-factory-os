# Start Here

Welcome. You do not need to read the entire repository on day one.

---

## Who This Is For

- New teammate or intern
- Developer exploring governed AI workflows
- Project lead who needs orientation
- Cursor operator running local demos

---

## Three Rules Before Anything Else

1. **This is a learning lab**, not production software you deploy.
2. **AI output can look correct and still be wrong** — gates exist for that reason.
3. **When unsure, do not patch** — read troubleshooting, then ask or rollback.

---

## Your First Path

| Step | Document | Time |
|------|----------|------|
| 1 | [README.md](../README.md) (this folder) | 5 min |
| 2 | [first-30-minutes.md](first-30-minutes.md) | 30 min |
| 3 | [first-2-hours.md](first-2-hours.md) | 2 hr |
| 4 | [first-day.md](first-day.md) | rest of day |
| 5 | Pick a [learning path](../learning-paths/) | ongoing |

---

## One Command to Try Now

```powershell
cd C:\Dima\Projects\CURSOR\AGENT
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
```

You should see: draft → critic → human approve → published, plus an audit log.

---

## If You Feel Lost

- **Too much reading?** → [first-30-minutes.md](first-30-minutes.md) only
- **Need commands?** → [../runbooks/run-prototypes.md](../runbooks/run-prototypes.md)
- **Something broke?** → [../troubleshooting/common-errors.md](../troubleshooting/common-errors.md)
- **About to change code?** → [../change-guides/how-to-change-safely.md](../change-guides/how-to-change-safely.md)

---

## Checkpoint (Can You Answer These?)

- What is this repo **not**? (Hint: not a production AI platform)
- What does "fail-closed" mean in one sentence?
- Where do trace examples live?

Answers: [../onboarding/onboarding-assessment.md](../onboarding/onboarding-assessment.md)
