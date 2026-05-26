# Real Provider Boundary — Review Assistant Thin

**Phase 3.3** — local OpenAI-compatible endpoint only. **Mock remains default.**

---

## Purpose

Minimal real-provider boundary proving:

```text
synthetic task → HTTP chat-completions → parse → safety → verification → approval → delivery/block
```

Provider output is **untrusted** — same as mock v0.2.

---

## Not included

- OpenAI cloud by default
- Anthropic, GigaChat, YandexGPT, Bitrix, NeuralDeep
- Provider framework / registry / router
- RAG, MCP, runtime, factory
- Sensitive data in prompts

---

## Modes

| Mode | How | Network |
|------|-----|---------|
| **Default** | No `--real-provider` | None for real scenarios |
| **Real** | `--real-provider` + env | Only when explicitly enabled |

---

## Environment variables

| Variable | Required | Notes |
|----------|----------|-------|
| `RA_LLM_BASE_URL` | yes for real mode | e.g. `http://127.0.0.1:1234` |
| `RA_LLM_API_KEY` | optional | Local endpoints often need none |
| `RA_LLM_MODEL` | optional | Default `local-model` |

**Never** commit keys. **Never** log/trace env values.

---

## Endpoint shape

```text
{RA_LLM_BASE_URL}/v1/chat/completions
```

OpenAI-compatible JSON. Stdlib `urllib.request` only.

---

## Scenarios

```powershell
python minimal_demo.py --scenario real_provider_forbidden_without_flag
python minimal_demo.py --scenario real_provider_missing_config --real-provider
python minimal_demo.py --scenario real_provider_synthetic --real-provider
```

---

## Synthetic prompt only

Fixed non-sensitive task text in code — not user input.

---

## Trace events

`provider_request_prepared`, `provider_disabled`, `provider_config_missing`, `provider_request_started`, `provider_response_received`, `provider_parse_*`, `provider_timeout`, `provider_error`, etc.

No secrets in trace.

---

## Planning reference

`governance/phase-3-3-plan/PROVIDER_BOUNDARY_CONTRACT.md`

---

## Rollback

Disable `--real-provider`; revert Phase 3.3 commits; mock v0.2 baseline must PASS all checks.
