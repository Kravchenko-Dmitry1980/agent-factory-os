# LLM Verification Adapter

Real LLM call (optional) with verification boundaries.

**LLM output ≠ truth**

## Run

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario uncertain

# Real (requires OPENAI_API_KEY)
python integrations-real/llm-verification-adapter/minimal-demo.py --real
```

One model only. No swarm.
