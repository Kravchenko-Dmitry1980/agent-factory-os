# Change Proposal Template

Copy for any governed change. Markdown-only — no ticket platform required.

---

## Title

`<short name>`

## Change Type

- [ ] Adding new workflow
- [ ] Modifying retry logic
- [ ] Changing verification
- [ ] Adding memory writeback
- [ ] Introducing autonomy
- [ ] Integrating new adapter
- [ ] Changing escalation policy
- [ ] Changing approval boundaries
- [ ] Other: ___

## Why

What problem? Link to doctrine/governance/observability doc if applicable.

## Risk (1–5)

| Score | Meaning |
|-------|---------|
| 1 | Docs only |
| 2 | Demo behavior, mock only |
| 3 | Real adapter boundary |
| 4 | Gate order or HITL change |
| 5 | Autonomy or external action path |

## Governance Impact

Which gates move? Stronger or weaker?

- Promotion gate
- Approval gate
- Verification gate
- Escalation gate
- Rollback gate
- Observability gate

## Observability Impact

New/changed canonical events? Trace readability affected?

See [../impact-analysis/](../impact-analysis/).

## Rollback Plan

1. What to revert (file, flag, config)
2. How to verify rollback (trace signature)
3. Max time before rollback triggers

## Validation

- [ ] Fail-closed preserved
- [ ] Escalation still fires at ceiling
- [ ] Audit lineage intact
- [ ] No new shared framework module
- [ ] Example trace updated if behavior changed

## Decision

- [ ] Proceed
- [ ] Proceed with staged rollout (see safe-rollouts/)
- [ ] Reject — governance cost too high
