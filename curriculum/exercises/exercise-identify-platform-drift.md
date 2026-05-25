# Exercise: Identify Platform Drift

## Purpose

Recognize platform drift proposals before they become code.

## Time

25 minutes

## Steps

1. Read [../lessons/lesson-platform-drift.md](../lessons/lesson-platform-drift.md)
2. Read `evolution/examples/unsafe-shared-runtime.md`
3. For each statement, mark **SAFE teaching** vs **DRIFT**:

   - a) Document linking three demos in a runbook
   - b) Extract `WorkflowEngine` used by all prototypes
   - c) Add pytest replacing smoke scripts
   - d) Student runs demos manually for assessment
   - e) UniversalAdapter for Telegram + LLM + queue

4. Discuss with peer or mentor

## Expected Result

b, c, e = DRIFT; a, d = SAFE

## What To Observe

- Drift often sounds efficient
- Documentation consolidation ≠ runtime consolidation

## Questions

1. Why is shared orchestrator tempting?
2. What is practice-before-platform?

## Pass Criteria

Correctly flags b/c/e; explains one consequence of drift.

## Fail Criteria

Labels runbook as drift; approves UniversalAdapter for "DRY".

Methodology: [../methodology/practice-before-platform.md](../methodology/practice-before-platform.md)
