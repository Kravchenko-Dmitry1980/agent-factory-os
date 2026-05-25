# Scenario: LLM Verification

## What It Teaches

LLM output is **untrusted input**. Parse/schema check ≠ factual truth. Malformed → reject.

## What Can Go Wrong

- Trust JSON because it parsed
- Skip verifier on cache
- Timeout → use guess

## Correct Safe Behavior

- `happy` → structural pass + reminder LLM != truth
- `malformed` → reject
- `uncertain` → reject or escalate

## Files to Run

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario uncertain
```

## Traces to Inspect

- `observability/examples/malformed-llm-trace.txt`

## Evaluation Checks

- `evaluation/scenarios/real-adapter-scenarios.md`
- Smoke: `llm malformed`
- Trace script includes malformed-llm-trace.txt

## Deep Docs

- [../safety-guides/why-llm-output-is-not-truth.md](../safety-guides/why-llm-output-is-not-truth.md)
- [../troubleshooting/llm-adapter-fails.md](../troubleshooting/llm-adapter-fails.md)
