# Verification Impact

## Changes That Weaken Verification

- Merge critic into verifier role
- Single "quality score" replaces pass/fail/uncertain
- Skip GUI A/B/C check on "trusted" screens
- LLM self-verify its own output
- Remove malformed output handling

## Observable Regression

Before: `verification_failed` → deny  
After: `task_completed` without verify event

## critic != truth Reminder

Any change merging critique and verification → [verification-impact](../drift-detection/drift-patterns.md) **verification drift**.

## Test

Run Phase 2.0–2.2 failure scenarios — all must still fail closed.
