# Run Real Adapters

## Purpose

Run Phase 2.2 local adapters with **mock mode default** (no API keys required).

## When to Use

- Learning real I/O failure modes (timeout, malformed JSON)
- After changing `integrations-real/` code
- Validating fail-closed survives real boundaries

## Commands

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/local-queue-worker/minimal-demo.py --scenario recovery
python integrations-real/telegram-review-gate/minimal-demo.py
python integrations-real/filesystem-audit-log/minimal-demo.py --scenario happy
python integrations-real/fastapi-review-api/minimal-demo.py --scenario happy
```

Optional (requires credentials):

```powershell
$env:OPENAI_API_KEY = "your-key"
python integrations-real/llm-verification-adapter/minimal-demo.py --real --scenario happy
```

## Expected Result

- Mock mode works without tokens
- Malformed scenario shows reject
- Audit or log output visible
- Data under `integrations-real/.data/` (gitignored)

## Common Failures

| Symptom | See |
|---------|-----|
| LLM errors | [../troubleshooting/llm-adapter-fails.md](../troubleshooting/llm-adapter-fails.md) |
| Telegram errors | [../troubleshooting/telegram-adapter-fails.md](../troubleshooting/telegram-adapter-fails.md) |
| FastAPI errors | [../troubleshooting/fastapi-adapter-fails.md](../troubleshooting/fastapi-adapter-fails.md) |

## What to Do If It Fails

1. Confirm mock mode (no `--real` unless intentional)
2. Check optional deps: `pip install fastapi uvicorn httpx` if FastAPI demo fails
3. Do not commit `.data/` or secrets

## What NOT to Do

- Do not build UniversalAdapter layer
- Do not require cloud services for onboarding
- Do not store API keys in repo

Reference: [../../integrations-real/README.md](../../integrations-real/README.md)
