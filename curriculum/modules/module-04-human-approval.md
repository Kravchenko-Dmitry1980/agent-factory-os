# Module 04 — Human Approval

## Goal

Use human approval for high-impact decisions — explicit, auditable, not implicit.

## Simple Explanation

Some actions need a **person** to say yes: publish externally, send email, confirm payment. Missing approval means **no**, not "maybe later auto-yes."

## Key Ideas

- Approval-before-external-action
- Timeout → deny (fail-closed)
- Human can disagree with critic
- No silent approval

## Files to Read

- `agent-os/doctrine/governance-before-autonomy.md`
- [../lessons/lesson-human-approval.md](../lessons/lesson-human-approval.md)
- [../operator-playbooks/safety-guides/why-approval-is-required.md](../operator-playbooks/safety-guides/why-approval-is-required.md)

## Commands to Run

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
python integrations-real/telegram-review-gate/minimal-demo.py
```

## Exercise

[../exercises/exercise-block-unsafe-action.md](../exercises/exercise-block-unsafe-action.md)

## Common Mistakes

- "Internal" bypass without governance review
- Treating pending as approved
- Removing human step for speed

## Checkpoint Questions

1. What happens in no-approval scenario?
2. Why is timeout deny important?
3. Who wins if critic passes and human denies?

## Expected Outcome

Student explains approval chain on happy path and deny path.
