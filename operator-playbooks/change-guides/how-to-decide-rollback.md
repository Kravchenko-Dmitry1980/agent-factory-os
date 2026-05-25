# How to Decide Rollback

Rollback when governance is worse, not when convenience is worse.

---

## Rollback triggers

- Smoke FAIL on fail-closed / escalation / approval paths
- Missing `approval_requested` on publish path
- `retry_exhausted` removed from flow
- Audit events disappeared
- Mentor/lead says stop

See `evolution/rollback-thinking/rollback-triggers.md`

---

## Do not rollback for

- Docs typo in operator-playbooks
- Expected mock output wording change **if** gates still correct and scenarios updated

---

## Rollback first, debug second

Under pressure, forward fixes add complexity. Revert → confirm green smoke → root cause calmly.

Strategies: `evolution/rollback-thinking/rollback-strategies.md`

Runbook: [../runbooks/rollback-after-failure.md](../runbooks/rollback-after-failure.md)

Examples: `evolution/examples/rollback-success.md`, `rollback-failure.md`

---

## After rollback

Update change proposal with failure notes. Do not retry same patch blindly.
