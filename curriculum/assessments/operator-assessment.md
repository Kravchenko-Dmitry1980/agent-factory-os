# Operator Assessment

For students completing Module 12 / operator playbooks.

## Written Questions

1. What is fail-closed?
2. Why is critic not truth?
3. Why is LLM output not truth?
4. Why do we need human approval?
5. What is a trace?
6. What is rollback?
7. What is platform drift?
8. Why should we not create a framework too early?
9. What makes a workflow safe?
10. When should we escalate to a human?

## Practical Tasks

1. Run full smoke: `python evaluation/scripts/run_demo_smoke_checks.py` — explain any FAIL
2. Navigate from symptom to troubleshooting doc without help
3. Complete before-running-demo + after-changing-workflow checklists verbally

## Red Flag Recognition

Identify regression in description:

*"Demo exits 0 but audit no longer shows approval_requested before publish."*

**Expected:** governance regression; rollback; not ship.

## Explain In Your Own Words

Explain difference between operator-playbooks and evaluation/ in 3 sentences.

## Pass Criteria

- All practical tasks pass
- 8/10 written adequate
- Names rollback + trace compare as response to regression
- Can locate runbooks for prototypes, evaluation, rollback

## Fail Criteria

Cannot run smoke; patches without runbook; confuses operator docs with CI.

Cross-check: [../operator-playbooks/onboarding/onboarding-assessment.md](../operator-playbooks/onboarding/onboarding-assessment.md)
