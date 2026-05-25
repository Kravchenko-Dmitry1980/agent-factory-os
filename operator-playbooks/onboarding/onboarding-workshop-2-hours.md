# Onboarding Workshop (2 hours)

Extended facilitated session.

---

## Agenda

| Block | Content |
|-------|---------|
| 0:00–0:30 | [onboarding-workshop-30-min.md](onboarding-workshop-30-min.md) |
| 0:30–1:00 | Run fail-closed + bounded memory demos |
| 1:00–1:20 | Read failed-review + escalation traces |
| 1:20–1:40 | [../safety-guides/why-fail-closed-matters.md](../safety-guides/why-fail-closed-matters.md) discussion |
| 1:40–2:00 | [onboarding-assessment.md](onboarding-assessment.md) group Q&A |

---

## Extra commands

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/bounded-memory-agent/minimal-demo.py --scenario overflow
python prototypes/queue-orchestration/minimal-demo.py --scenario max-retries
```

---

## Exercise

Pair up: one person explains audit log from bypass demo to partner.

---

## Close

Assign learning path by role from [../learning-paths/](../learning-paths/)
