# Change Lock — Review Assistant Thin v0.3

After v0.3 freeze, any change to **frozen implementation files** (see [V0_3_IMPLEMENTATION_MANIFEST.md](V0_3_IMPLEMENTATION_MANIFEST.md)) requires:

1. **Change proposal** — what/why/impact
2. **Impact analysis** — scenarios affected (all 13), spec alignment
3. **Security review** — especially provider boundary and data policy
4. **Provider / data policy review** — synthetic-only, no secrets, no cloud default
5. **Evaluation run** — all 5 check scripts (thin, llm mock, provider contract, smoke, trace)
6. **Trace comparison** — before/after vs [V0_3_SCENARIO_BASELINE.md](V0_3_SCENARIO_BASELINE.md)
7. **Rollback plan** — [V0_3_ROLLBACK_RECORD.md](V0_3_ROLLBACK_RECORD.md)
8. **Explicit approval** — user/lead message

---

## Forbidden without new phase

| Change | Why blocked |
|--------|-------------|
| OpenAI cloud | Scope expansion; separate approval |
| Anthropic cloud | Scope expansion |
| GigaChat / YandexGPT / RU providers | Out of scope |
| Bitrix / NeuralDeep integrations | Out of scope |
| Provider abstraction framework | Platform drift |
| Model router / provider registry | Platform drift |
| Fallback provider chain | Platform drift |
| RAG / MCP | Out of scope |
| Persistent memory | Template v0.1 forbids |
| Second agent / second template | Phase scope |
| Runtime / factory / generator | Explicitly excluded |
| Auto-publish | Safety violation |
| Hidden tool execution from provider output | Safety violation |
| Real user / project / client data in prompts | Safety violation |
| Interactive CLI approval | Separate approval |
| Telegram / FastAPI service | Production adapter |
| Operator Console / desktop UI | Separate phase |
| Shared framework extraction | Platform drift |

---

## v0.3-specific lock

| Item | Rule |
|------|------|
| Mock LLM boundary | Frozen — change only via proposal |
| Real provider boundary | Frozen — local OpenAI-compatible only |
| `--real-provider` flag gate | Frozen — no implicit real mode |
| 3 real provider scenarios | Frozen expected decisions and events |
| `real_provider_boundary.md` | Frozen with impl |
| Disabled-by-default network | Frozen — mock default |
| Synthetic-only live prompt | Frozen policy |

---

## Allowed without unfreeze (non-semantic)

- Typo fixes in docs (no behavior change)
- Navigation links and freeze metadata append
- Governance reviews and validation record updates
- Evaluation script baseline string updates if trace format typo-only

---

## Frozen spec

`agent-builder-kit/templates/review-assistant-agent/` — **separate** CHANGE_LOCK. Do not edit spec to match impl drift.

---

## Version history

| Version | Active change lock |
|---------|-------------------|
| v0.1 | [CHANGE_LOCK.md](CHANGE_LOCK.md) (historical) |
| v0.2 | [V0_2_CHANGE_LOCK.md](V0_2_CHANGE_LOCK.md) (superseded for new changes) |
| **v0.3** | **This file (active)** |

Any behavior change → follow this lock or open new phase with explicit scope.
