# LLM Adapter Fails

## Symptom

Errors from `integrations-real/llm-verification-adapter/minimal-demo.py`.

## Mock mode (default — no key)

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
```

Malformed must **reject** — that is success for fail-closed.

## Real mode

Requires `OPENAI_API_KEY`. Network errors are expected failure modes — should reject, not crash unhandled.

```powershell
$env:OPENAI_API_KEY = "sk-..."
python integrations-real/llm-verification-adapter/minimal-demo.py --real --scenario happy
```

## Common issues

| Issue | Fix |
|-------|-----|
| Timeout | Use mock for onboarding; check `--timeout` |
| Import httpx | `pip install httpx` |
| Rate limit | Not an onboarding problem — use mock |

## Trace reference

`observability/examples/malformed-llm-trace.txt`

Remember: **LLM output != truth** even when parse succeeds.

See [../safety-guides/why-llm-output-is-not-truth.md](../safety-guides/why-llm-output-is-not-truth.md)
