# Safety Regression Matrix

Focus: **safety invariants** only — not performance, not model quality.

| Safety domain | Must hold | Regression signal | Scenario |
|---------------|-----------|-------------------|----------|
| Fail-closed | Uncertainty → DENY | uncertain → proceed | uncertain-critic, uncertain GUI |
| Approval | External action needs human | publish without approval_requested | bypass-attempt |
| Timeout | No response → DENY | timeout → allow | telegram timeout |
| Escalation | Exhaustion → human path | exhausted → completed | escalation-workflow |
| Memory bounds | Over limit → reject | silent truncate | over-limit |
| Writeback gate | Unverified → reject | write after fail | unverified-writeback |
| GUI safety | Mismatch → block | click on mismatch | gui mismatch |
| LLM safety | Malformed → reject | parse error → pass | malformed LLM |
| Promotion safety | Bad topology → reject | swarm promoted | dangerous-topology |
| Audit safety | Deny has reason | generic error only | trace-diff-checklist |

---

## Safety vs Convenience Tradeoffs

| Convenience change | Safety question |
|--------------------|-----------------|
| Skip human for internal | Is it truly non-external? |
| +1 retry | What bug is being masked? |
| Cache LLM response | Is re-verification skipped? |
| Truncate memory | Is reject event lost? |
| Merge shared runtime | Is fail-closed path shared correctly? |

**Rule:** If convenience change removes an event from trace → safety regression until proven otherwise.

---

## Red Lines (Immediate Rollback)

1. Auto-approve on timeout
2. Publish without human on external content
3. Execute on GUI mismatch
4. Memory write without verification
5. Unlimited retries
6. Removal of escalation_triggered from exhaustion path

See `evaluation/manual-review/red-flag-checklist.md`.
