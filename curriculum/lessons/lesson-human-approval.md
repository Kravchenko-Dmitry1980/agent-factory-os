# Lesson: Human Approval

## What is this?

A **human approval** step means a person explicitly allows a high-impact action after seeing context.

## Why does it matter?

Automation cannot carry legal, reputational, and ethical responsibility alone. Approval creates audit: who said yes.

## What can go wrong?

- Missing approval → proceed anyway
- Pending forever → later treated as yes
- Timeout → auto approve

## How do we check it?

Trace shows `approval_requested` before execute/publish. Deny paths show deny events.

```powershell
python prototypes/fail-closed-external-action/minimal-demo.py --scenario approved
python prototypes/fail-closed-external-action/minimal-demo.py --scenario no-approval
```

## Which demo shows it?

- fail-closed-external-action
- review-loop-agent (human decision on happy path)
- telegram-review-gate (mock)
