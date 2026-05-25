# Real Integration Adapters (Phase 2.2)

**Status:** Local-first real adapters — not a platform.

---

## Why Real Integrations Are Now Allowed

Phases 2.0–2.1 validated governance with mocks. Phase 2.2 asks:

> Do fail-closed gates survive **real** I/O boundaries?

Real timeouts, malformed JSON, network failures, and filesystem edge cases expose gaps that mocks hide.

---

## Why Integrations Remain Intentionally Small

| Property | Rationale |
|----------|-----------|
| **Local-first** | No cloud, no cluster |
| **Single process** | No worker fleet |
| **Optional credentials** | Mock mode without API keys |
| **One adapter = one lesson** | No universal adapter layer |
| **< 60 min read** | Educational, not operable at scale |

---

## Platform Drift Is Dangerous

Phase 2.2 is the **second-highest drift risk** (after 2.1 framework extraction).

Stop if you see:

- `UniversalAdapter`, `IntegrationRegistry`, plugin loading
- Shared orchestration engine across adapters
- Production auth, K8s manifests, Redis/Celery

---

## Governance Still Dominates Architecture

Real I/O does **not** relax:

- Fail-closed on uncertainty
- Deny-by-default approval
- Verification before writeback
- Append-only audit lineage
- Bounded retries + escalation

External systems are **untrusted inputs**, not sources of truth.

---

## Adapters

| Adapter | Real boundary |
|---------|---------------|
| [telegram-review-gate](telegram-review-gate/) | Telegram Bot API (optional) |
| [fastapi-review-api](fastapi-review-api/) | HTTP + SQLite |
| [llm-verification-adapter](llm-verification-adapter/) | OpenAI-compatible API (optional) |
| [local-queue-worker](local-queue-worker/) | SQLite durable queue |
| [filesystem-audit-log](filesystem-audit-log/) | Append-only JSONL |

Governance: [governance/](governance/)  
Diagrams: [diagrams/](diagrams/)

---

## Optional Dependencies

```powershell
pip install fastapi uvicorn httpx
```

All adapters run in **mock mode** without credentials.

## Local Data

Runtime artifacts: `integrations-real/.data/` (gitignored).

## Run

```powershell
python integrations-real/telegram-review-gate/minimal-demo.py
python integrations-real/fastapi-review-api/minimal-demo.py
python integrations-real/llm-verification-adapter/minimal-demo.py
python integrations-real/local-queue-worker/minimal-demo.py
python integrations-real/filesystem-audit-log/minimal-demo.py
```

Environment (optional):

- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
- `OPENAI_API_KEY`, `OPENAI_BASE_URL` (default OpenAI)

---

## Relation to Previous Phases

```
prototypes/              → mocked governance lessons
prototypes/integrations/ → composed mock workflows
integrations-real/       → minimal real I/O boundaries
```

Do not promote adapter code into a production repo.
