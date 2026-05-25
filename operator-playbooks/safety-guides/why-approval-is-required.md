# Why Approval Is Required

Some actions have **real consequences** — email, publish, payment, production deploy. Automation must not guess permission.

---

## Principle

- **Explicit approve** → may proceed
- **Missing / timeout / reject** → deny (fail-closed)
- No "implicit yes"

---

## Not just bureaucracy

Approval creates an **audit point**: who allowed this, when.

---

## Demos

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
```

Human gate: `agent-os/doctrine/governance-before-autonomy.md`
