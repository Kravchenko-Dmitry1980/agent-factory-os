# Red Flag Checklist

If any item is true after a change → **stop and rollback** until explained.

---

## Autonomy Leaks

- [ ] External action without `approval_requested` in trace
- [ ] Timeout results in proceed, not deny
- [ ] "Low risk" bypass added without governance doc
- [ ] Critic PASS skips human on publish path
- [ ] Pending approval treated as approved

## Verification Bypass

- [ ] Malformed LLM scenario exits success without reject
- [ ] GUI click on mismatch scenario
- [ ] Memory write after verification_failed
- [ ] Cached LLM response skips verifier

## Retry / Escalation

- [ ] Retry limit increased "temporarily"
- [ ] `retry_exhausted` no longer emitted
- [ ] Escalation removed from exhaustion path
- [ ] task_completed after retry storm

## Observability

- [ ] Audit events deleted or renamed without mapping
- [ ] Failures log as generic "error" only
- [ ] OUTCOME block removed from demo output
- [ ] Trace shorter with same logical flow

## Platform Drift

- [ ] New universal runner or test harness
- [ ] pytest/unittest required for basic check
- [ ] GitHub Actions or CI config added
- [ ] Shared orchestration engine across demos
- [ ] Benchmark scores or model leaderboard files

## Evaluation Drift

- [ ] Scripts call paid APIs by default
- [ ] Scripts modify agent-os/ or Books/
- [ ] Evaluation claims "production QA ready"
- [ ] Automated merge gate proposed

---

## Response

| Flags | Action |
|-------|--------|
| 0 | Continue quality gate review |
| 1 critical | Rollback immediately |
| 2+ | Rollback + evolution change proposal |

Critical = autonomy leak, verification bypass, escalation removal, platform drift.
