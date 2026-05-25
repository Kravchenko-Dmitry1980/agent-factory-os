# Beginner Assessment

## Written Questions

Answer in your own words (2–4 sentences each).

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

Reference answers in [../onboarding/onboarding-assessment.md](../operator-playbooks/onboarding/onboarding-assessment.md) — use for self-check after mentor review.

## Practical Tasks

1. Run first demo exercise — pass criteria from [../exercises/exercise-run-first-demo.md](../exercises/exercise-run-first-demo.md)
2. Read one trace — pass criteria from [../exercises/exercise-read-trace.md](../exercises/exercise-read-trace.md)

## Red Flag Recognition

Which are dangerous? (Explain why)

- A) Remove human approval for internal docs
- B) Read observability examples
- C) Increase retries without proposal
- D) Run smoke checks after change

**Answers:** A and C dangerous.

## Explain In Your Own Words

Explain "this repository" to a friend in 60 seconds without saying "AI platform."

## Pass Criteria

- 7/10 written questions adequate (mentor judgment)
- Both practical tasks pass
- Red flags: 2/2 correct
- Can run review-loop happy + bypass demos unaided

## Fail Criteria

Cannot run demos; treats critic as truth; cannot define trace; approves A or C.
