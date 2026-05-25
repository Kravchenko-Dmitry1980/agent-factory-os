# Exercise: Write Change Proposal

## Purpose

Practice safe change discipline **on paper** — no required code edit.

## Time

30 minutes

## Steps

1. Read `evolution/change-proposals/change-template.md`
2. Hypothetical change: "Increase MAX_RETRIES from 3 to 5 in queue demo"
3. Fill template sections:
   - Which gate moves?
   - Risk level
   - Scenarios to re-run
   - Rollback plan
4. Mentor reviews

## Expected Result

One-page proposal identifying escalation impact.

## What To Observe

- Proposal forces gate thinking before coding
- Links to evaluation scenarios

## Questions

1. Why is this high/medium/low risk?
2. Which traces might change?

## Pass Criteria

Names retry/escalation impact; lists evaluation scenarios; rollback defined.

## Fail Criteria

"No risk — just one number"; no rollback; no scenarios.

Guide: [../operator-playbooks/change-guides/how-to-write-change-proposal.md](../operator-playbooks/change-guides/how-to-write-change-proposal.md)
