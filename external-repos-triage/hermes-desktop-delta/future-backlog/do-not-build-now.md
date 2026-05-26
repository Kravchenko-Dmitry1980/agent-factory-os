# Do Not Build Now

Strict prohibitions after Hermes Desktop triage.

---

## Forbidden now

| Item | Why |
|------|-----|
| Operator Console implementation | No provider/template maturity |
| Electron app | Security/complexity; wrong phase |
| Tauri app | Same |
| Provider settings UI | Tempts framework + secrets on disk |
| Gateways (Telegram, …) | Unattended outbound risk |
| Schedules / cron UI | Autonomy without approval |
| Remote desktop mode | API key + network trust |
| Skill installer | Supply chain |
| Real provider switching | No framework; v0.2 mock only |
| Desktop updater | Supply chain |
| Remote agent server | Runtime drift |
| Multi-provider registry | Hermes pattern — reject for Phase 3 |
| GigaChat/YandexGPT integration | Not approved; some planned only in fork |
| Memory provider integrations | Doctrine conflict |
| Persona/SOUL editor | Persona-over-architecture |

---

## When some items may become allowed

| Item | Preconditions |
|------|---------------|
| Single real provider | Phase 3.3 plan + approval + freeze |
| Provider config spec (md) | After first real provider frozen |
| Operator Console plan | Phase 4; 2–3 templates |
| Operator Console MVP | Phase 4+ impl approval |
| RU provider research | After global provider boundary proven |
| Skill review (read-only) | Supply-chain governance phase |

---

## Never (Agent-OS Lab core)

- 16-gateway messaging platform
- Self-improving closed loop as product goal
- Digital twin / CV features
- Agent factory / runtime generator

---

## Current focus

**review-assistant-thin-v0.2** + Phase 3.3 Real LLM Provider Boundary **Plan**.
