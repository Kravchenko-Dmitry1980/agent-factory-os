# Lesson: LLM Output Is Not Truth

## What is this?

Text from a language model is **untrusted input** — even when formatted as JSON.

## Why does it matter?

Models invent facts, citations, and numbers confidently. Parsing JSON only proves **structure**, not **reality**.

## What can go wrong?

- Trusting structured output for financial/medical/legal actions
- Skipping verifier when response "looks valid"

## How do we check it?

Malformed scenario must reject. Happy scenario must remind LLM != truth.

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
```

Trace: `observability/examples/malformed-llm-trace.txt`

## Which demo shows it?

`integrations-real/llm-verification-adapter/`
