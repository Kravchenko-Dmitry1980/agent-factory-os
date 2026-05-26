# Security and Provider Risk Register

Phase 3.2.2 — Hermes Desktop delta.

| Risk | Severity | Early Signal | Mitigation |
|------|----------|--------------|------------|
| API key leakage | **High** | Keys in `.env`, backup ZIP, logs | Env-only; no keys in repo; masked UI future; no backup export without strip |
| Provider config drift | **High** | Custom URL to untrusted host | Single approved provider; change proposal; freeze |
| Unsafe gateway sends | **High** | Test msg to production channel | Do not build gateways |
| Schedule autonomy | **High** | Cron job runs without human | Do not build schedules |
| Desktop IPC risk | **High** | Broad IPC handlers | Defer Electron; hardening checklist if built |
| Local file exposure | **High** | Agent reads `.env`, SSH keys | Tool boundary; deny-list; workspace root policy |
| Update mechanism risk | **Medium** | Unsigned installer bypass normalized | No auto-updater in Lab; signed releases if ever |
| RU provider assumptions | **Medium** | "Planned" treated as ready | Implemented vs planned labels in docs |
| Fork staleness | **Medium** | RU fork lags upstream security | Never depend on fork; shallow clone snapshot only |
| UI hiding governance state | **Medium** | Pretty chat UI; no freeze visible | Governance-first console spec |
| Remote mode trust | **Medium** | Shared API key on desktop | Exclude from Phase 3.3 plan |
| Skill supply chain | **High** | One-click skill install | No skill installer; review-only future |
| Memory writeback | **High** | Mem0/Supermemory toggles | Memory boundary doctrine; no providers |
| Persona/SOUL drift | **Medium** | Personality editor | Reject persona-over-architecture |
| Multi-provider framework | **High** | Registry + switcher UI | Mock v0.2 + single provider plan |
| OAuth scaffolding incomplete | **Medium** | Bitrix login throws in RU fork | Do not implement OAuth until endpoint exists |
| Telemetry (PostHog) | **Low** | Analytics in dependencies | No analytics in our impl; note for console |
| Prompt injection via gateway | **High** | Inbound Telegram message → tools | No gateways |

---

## Review cadence

Update this register when:

- Phase 3.3 provider plan published
- Operator Console plan starts
- New external desktop/agent UI repos triaged

---

## Owner

Governance / research — no runtime owner until console phase approved.
