# Russian Provider Backlog

**Research only.** No implementation. No API keys. No calls.

Status verified against `hermes-desktop-ru` source at commit `2bbe940`.

| Provider | Potential Value | Risks | When to Consider |
|----------|-----------------|-------|------------------|
| **GigaChat** | Sber ecosystem; RU data residency expectations | API policy, cost, logging, auth complexity; **not in fork code** | Phase 3.3+ **plan** only after single global provider boundary proven; mark **planned/claimed** |
| **YandexGPT** | Yandex Cloud integration; RU market familiarity | Same as above; **README planned only** | Same — research doc + security review before any adapter |
| **Bitrix VibeCode** | Free BitrixGPT via OpenAI-compatible API; enterprise portals | Bitrix OAuth scaffolding incomplete; keys in `.env`; portal scope | If Bitrix enterprise users — **after** env secret policy + OAuth security review |
| **NeuralDeep Hub** | RU OSS aggregator; OpenAI-compatible `api.neuraldeep.ru` | Third-party hub trust; key in `.env`; Bitrix exchange endpoint **not built** | Research comparison only; not default provider |

---

## Honesty rule

| Provider | In RU fork code? | In README? |
|----------|------------------|------------|
| NeuralDeep | yes (default-models, detect-provider, env key) | yes |
| Bitrix VibeCode | yes (default-models, detect-provider; OAuth throws) | yes |
| GigaChat | **no** | planned |
| YandexGPT | **no** | planned |

---

## Before any RU provider integration

Must pass:

1. Security review
2. Data residency / policy review
3. Timeout and error handling eval
4. Trace + approval gate tests
5. Cost/logging review
6. Explicit user approval message
7. Freeze record

---

## Agent-OS stance

**No provider integration now.** Backlog for comparison research after mock → single real provider path is frozen.
