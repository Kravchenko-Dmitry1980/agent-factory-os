# Local-First Policy

## Rules

1. **Run on developer machine** — no required cloud services
2. **Credentials optional** — mock mode must work without `.env`
3. **Single process** — no worker pools
4. **File/SQLite persistence** — no external database cluster
5. **Network calls** — only when adapter purpose requires it; timeout + fail-closed

## Network Adapters

| Adapter | Network | Fallback |
|---------|---------|----------|
| telegram-review-gate | Telegram API | Mock stdin/CLI approval |
| llm-verification-adapter | OpenAI API | Deterministic mock LLM |
| fastapi-review-api | localhost only | In-process TestClient |

## Offline Guarantee

`minimal-demo.py --mock` (or default without env) must complete without network.
