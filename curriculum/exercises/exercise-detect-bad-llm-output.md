# Exercise: Detect Bad LLM Output

## Purpose

Recognize malformed LLM response handling — reject, not trust.

## Time

15 minutes

## Steps

1. Read [../lessons/lesson-llm-output-is-not-truth.md](../lessons/lesson-llm-output-is-not-truth.md)
2. Run:

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
```

3. Open `observability/examples/malformed-llm-trace.txt`
4. Compare demo output to trace events

## Expected Result

Malformed: reject decision. Happy: pass + reminder LLM != truth.

## What To Observe

- verification_failed / reject on malformed
- No "execute anyway" path

## Questions

1. Does JSON parse success mean content is true?
2. Which canonical events appear in example trace?

## Pass Criteria

Explains structural vs factual verification; identifies reject on malformed.

## Fail Criteria

Says malformed should proceed; cannot read trace file.
