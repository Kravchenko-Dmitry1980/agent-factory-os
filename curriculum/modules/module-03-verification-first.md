# Module 03 — Verification First

## Goal

Place **verification before** trust, publish, memory write, or external action.

## Simple Explanation

**Verification** means checking defined criteria (structure, policy, visual match, tests) — not asking "does this sound good?"

## Key Ideas

- Verification-before-writeback
- Structure check ≠ factual truth (especially for LLM)
- GUI visual verification before click
- Promotion gates before corpus entry

## Files to Read

- `agent-os/doctrine/verification-first.md`
- `agent-os/08_patterns/verification-before-writeback.md`
- [../lessons/lesson-llm-output-is-not-truth.md](../lessons/lesson-llm-output-is-not-truth.md)

## Commands to Run

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python prototypes/gui-verification-loop/minimal-demo.py --scenario outcome-b
```

## Exercise

[../exercises/exercise-detect-bad-llm-output.md](../exercises/exercise-detect-bad-llm-output.md)

## Common Mistakes

- Skipping verifier on "fast path"
- Treating JSON parse success as correctness
- Visual guess instead of verify step

## Checkpoint Questions

1. What is verified before memory write in bounded-memory demo?
2. What happens on malformed LLM output?
3. Verification-first vs "ask critic" — difference?

## Expected Outcome

Student can point to verification step in audit for two different demos.
