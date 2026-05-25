# Severity Levels

Human-readable priority — not metric labels.

| Level | Name | Meaning | Operator action |
|-------|------|---------|-----------------|
| S0 | **Critical autonomy** | Unsafe action almost executed or bypass attempted | Stop deployment, review gates |
| S1 | **Governance failure** | Fail-closed worked but policy chain broken | Fix workflow order |
| S2 | **Escalation expected** | Retry exhausted, human required | Triage queue |
| S3 | **Verification noise** | Recoverable verify fail, retry OK | Monitor retry count |
| S4 | **Informational** | Happy path milestones | No action |

## Event → Severity (default)

| Event | Default severity |
|-------|------------------|
| `unsafe_action_blocked` | S0 |
| `approval_bypass` (anti-pattern) | S0 |
| `governance_rejection` | S1 |
| `escalation_triggered` | S2 |
| `retry_triggered` | S3 |
| `verification_failed` | S3 (S2 if repeated) |
| `task_completed` | S4 |

## Rule

**Severity describes governance risk**, not log volume. One `escalation_triggered` beats 1000 `task_started`.
