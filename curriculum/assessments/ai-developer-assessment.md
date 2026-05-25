# AI Developer Assessment

## Written Questions

All ten core questions (see beginner assessment) plus:

11. What is verification-before-writeback?
12. What events appear in escalation-trace.txt?
13. What is the impact of editing prototypes/shared/gates.py?

## Practical Tasks

1. Run fail-closed + LLM malformed + escalation demos in sequence
2. Map demo audit actions to canonical events (one example)
3. Draft skeleton change proposal for hypothetical gate change
4. Run smoke before/after — explain what smoke does NOT prove

## Red Flag Recognition

Review snippet: *"Let's cache LLM responses and skip verifier on cache hit."*

**Expected:** verification bypass; reject; fail-closed violation.

## Explain In Your Own Words

Explain retry vs escalation vs rejection — three different terminals.

## Pass Criteria

- Practical tasks without command lookup for core demos
- Impact question mentions full smoke + all dependents
- Red flag identified with verification argument
- Change proposal mentions gates and rollback

## Fail Criteria

Approves cache skip; cannot read escalation trace; no shared module caution.

Track: [../role-based-tracks/track-ai-developer.md](../role-based-tracks/track-ai-developer.md)
