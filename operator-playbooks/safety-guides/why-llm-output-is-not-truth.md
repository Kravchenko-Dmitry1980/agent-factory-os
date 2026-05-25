# Why LLM Output Is Not Truth

Even valid JSON from an LLM is **untrusted input** until verified for your use case.

---

## Why

- Models hallucinate facts and citations
- Structured output only means **parseable**, not **true**
- Same prompt gives different answers

---

## Our rule

1. Parse/schema check (adapter layer)
2. Separate decision gate (allow/reject/escalate)
3. Reminder in demo output: LLM output != truth
4. No direct wire from LLM → external action

---

## Demo

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
```

Trace: `observability/examples/malformed-llm-trace.txt`
