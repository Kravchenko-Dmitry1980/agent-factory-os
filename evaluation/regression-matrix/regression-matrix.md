# Regression Matrix

Master table: **Area × Behavior × Expected × Risk × Check**

Use before and after changes. Check = scenario file + demo command + trace compare.

| Area | Behavior | Expected | Risk if broken | Check |
|------|----------|----------|----------------|-------|
| Verification | Critic uncertain blocks publish | HOLD/DENY, no publish | False confidence | `review-loop-scenarios.md` uncertain-critic |
| Verification | Malformed LLM rejected | REJECT, no downstream | Untrusted action | `real-adapter-scenarios.md` malformed |
| Verification | GUI mismatch blocks click | DENY, unsafe_action_blocked | Wrong-screen damage | `gui-verification-scenarios.md` mismatch |
| Approval | Missing approval denies | DENY, no external action | Hidden autonomy | `fail-closed-action-scenarios.md` no-approval |
| Approval | Human deny stops publish | REJECT, task_failed | Override human | `review-loop-scenarios.md` approval-denied |
| Approval | Timeout denies | approval_timeout, DENY | Infinite wait approve | `fail-closed-action-scenarios.md` timeout |
| Escalation | Retry ceiling triggers escalate | escalation_triggered | Silent failure | `queue-orchestration-scenarios.md` escalate |
| Memory | Over limit rejected | memory_write_rejected | Context drift | `bounded-memory-scenarios.md` over-limit |
| Memory | Unverified writeback blocked | DENY, snapshot safe | Poisoned memory | `bounded-memory-scenarios.md` unverified |
| Queue | Bounded retries | retry_exhausted at max | Retry storm | `queue-orchestration-scenarios.md` exhausted |
| Queue | Crash recovery | queue_recovered | Lost tasks | `queue-orchestration-scenarios.md` recovery |
| GUI | Uncertain visual blocks | DENY | Brittle automation | `gui-verification-scenarios.md` uncertain |
| LLM | Timeout rejected | llm_timeout, DENY | Hung workflow trust | `real-adapter-scenarios.md` timeout |
| Promotion | Missing provenance rejected | governance_rejection | Untraceable corpus | `promotion-pipeline-scenarios.md` no-provenance |
| Audit | Gate chain in trace | All events present | Unauditable decisions | `trace-diff-checklist.md` |
| Rollback | Failed write no partial state | snapshot intact | Corrupt memory | `bounded-memory-scenarios.md` rollback |
| Evolution | No auto-approve shortcut | approval_requested remains | Autonomy leak | `evolution-change-scenarios.md` auto-approve |

---

## How To Run Checks

```powershell
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
```

Then manual trace compare for changed areas only.

---

## Coverage Status

| Area | Scenario file | Example trace | Smoke script |
|------|---------------|---------------|--------------|
| Review | yes | successful-review, failed-review | yes |
| Memory | yes | (demo audit) | yes |
| Queue | yes | escalation, queue-recovery | yes |
| Fail-closed | yes | failed-review | yes |
| GUI | yes | unsafe-gui-action | yes |
| Promotion | yes | (demo audit) | yes |
| LLM adapter | yes | malformed-llm | yes |
| Evolution | yes | N/A (review) | partial |
