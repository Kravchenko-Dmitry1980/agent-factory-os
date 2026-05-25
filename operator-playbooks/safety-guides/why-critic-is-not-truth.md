# Why Critic Is Not Truth

A **critic** (reviewer agent or checklist) gives **advisory** feedback. It is not a verifier.

---

## Difference

| Critic | Verifier |
|--------|----------|
| Opinion on quality | Checks defined criteria |
| Can miss facts | Should catch contract violations |
| May pass bad drafts | Should fail unmet specs |
| Advisory | Binding for gate |

---

## Real example in repo

Trace `failed-review-trace.txt`: **critic passed**, **human denied**.

---

## Danger

 Wiring critic PASS → auto publish = governance collapse.

---

## Demo

```powershell
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
```

Curated: `observability/verification-failures/critic-limitations.md`
