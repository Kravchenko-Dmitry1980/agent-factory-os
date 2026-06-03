# Task Triage Agent — Human Approval Policy

**Status:** SPEC_DRAFT

---

## Core principle

**Triage output is advisory. Human decides next action.**

Task Triage Agent may recommend that human approval is required. It does **not** grant approval and does **not** replace human judgment.

---

## Human approval is required before

| Action | Why |
|--------|-----|
| Implementation starts | Execution boundary — triage is not authorization |
| Task affects frozen specs | Change lock — governance review required |
| Task touches provider boundary | Provider policy — mock-first, synthetic data |
| Task touches data/secrets | Data sensitivity gate |
| Task involves security | Security escalation |
| Task creates or modifies agent templates | Template governance |
| Task changes evaluation logic | Baseline regression risk |
| Task escalates from triage to execution | Triage ≠ execution approval |

---

## approval_required field

| Condition | approval_required |
|-----------|-------------------|
| risk_level = low, bounded doc task | false (human still reviews advisory output) |
| risk_level = medium | **true** |
| risk_level = high | **true** |
| risk_level = critical | **true** + escalation_required |
| frozen spec touch | **true** |
| provider addition | **true** |
| security task | **true** |
| governance task | **true** (medium+ typical) |

Trace: `approval_required: required=true, reason=...`

---

## Two-stage approval model

```text
Stage 1: Triage approval (advisory)
  Human reviews triage output — is classification acceptable?

Stage 2: Implementation approval (separate)
  Human approves actual work — plan, code, deploy, etc.
```

Triage may recommend Stage 1 attention. It never satisfies Stage 2.

---

## Deny-by-default

| Situation | Default |
|-----------|---------|
| Unclear if approval needed | approval_required=true |
| Risk ambiguous | Escalate, do not auto-clear |
| Task requests approval removal | BLOCKED or REJECT_UNSAFE |
| Task says "no human needed" | BLOCKED |

---

## Forbidden behaviors

| Forbidden | Response |
|-----------|----------|
| Auto-approve implementation | BLOCKED |
| Claim "approval granted" in output | triage_failed |
| Skip approval on medium+ risk | eval FAIL |
| Replace human reviewer | Policy violation |

---

## Relation to Review Assistant HITL

Review Assistant requires human approval **before delivery**.

Task Triage requires human judgment **before treating triage as action guidance**.

Both agents: human authority is final. See [templates/review-assistant-agent/human-approval.md](../review-assistant-agent/human-approval.md) for comparison.
