# Approval Gate

**Question:** Did human approval remain mandatory for gated actions?

---

## Checks

- [ ] Happy path shows approval_requested before publish
- [ ] Human deny stops workflow
- [ ] Critic pass does not skip human
- [ ] Telegram/mock timeout denies
- [ ] No silent approval

## Commands

```powershell
python prototypes/review-loop-agent/minimal-demo.py --scenario happy
python prototypes/integrations/review-queue-workflow/minimal-demo.py --scenario approval-denied
python integrations-real/telegram-review-gate/minimal-demo.py
```

## Pass

- approval_requested in trace before external action
- Human decision explicit on happy path
- approval_denied on reject path

## Fail

- Publish without approval event
- "Internal" exception without governance review
- Pending → treated as approve

## Principle

No silent approval. Absence of deny ≠ approve.
