# Do Not Adopt Now — Hermes Desktop

Phase 3.2.2 strict list.

---

## Hermes Desktop app (upstream)

| | |
|---|---|
| **Why tempting** | Full GUI for Hermes Agent; fast onboarding |
| **Why dangerous** | Autonomy bundle (tools/gateways/schedules); not governance-first; Electron secrets |
| **When allowed** | **Never adopt into Agent-OS** — reference only |

---

## Hermes Desktop RU fork

| | |
|---|---|
| **Why tempting** | RU UI + RU provider presets |
| **Why dangerous** | Fork staleness; unimplemented OAuth; planned providers marketed as roadmap |
| **When allowed** | Research comparison only; no dependency |

---

## Electron UI

| | |
|---|---|
| **Why tempting** | Hermes proves desktop demand |
| **Why dangerous** | IPC, updater, unsigned builds — separate security domain |
| **When allowed** | Phase 4+ console decision with security phase |

---

## Provider settings UI

| | |
|---|---|
| **Why tempting** | Easier than env vars |
| **Why dangerous** | Keys on disk; multi-provider drift |
| **When allowed** | After single provider frozen + masked UI spec |

---

## Skills installer

| | |
|---|---|
| **Why tempting** | One-click capability extension |
| **Why dangerous** | Supply chain (Phase 2.10 pattern) |
| **When allowed** | Separate supply-chain governance phase — likely read-only review only |

---

## Gateway layer

| | |
|---|---|
| **Why tempting** | Telegram/Slack integration |
| **Why dangerous** | Injection, accidental sends, always-on bots |
| **When allowed** | Not planned for Agent-OS Lab core |

---

## Schedules

| | |
|---|---|
| **Why tempting** | Automation |
| **Why dangerous** | Unattended autonomy; approval bypass |
| **When allowed** | Not planned without new human-gate phase |

---

## Remote mode

| | |
|---|---|
| **Why tempting** | Thin client to remote Hermes |
| **Why dangerous** | API key storage; network trust expansion |
| **When allowed** | Not default; defer indefinitely |

---

## Auto-updater

| | |
|---|---|
| **Why tempting** | User convenience |
| **Why dangerous** | Supply chain; unsigned package warnings normalized |
| **When allowed** | Only with signed release pipeline — not Phase 3 |

---

## Desktop secrets storage

| | |
|---|---|
| **Why tempting** | Credential pools, OAuth |
| **Why dangerous** | Plaintext `.env`, backup leakage |
| **When allowed** | Env-only policy first; OS keychain research much later |

---

## Tool execution UI

| | |
|---|---|
| **Why tempting** | Toggle 14 toolsets |
| **Why dangerous** | Shell/file/browser enablement |
| **When allowed** | Read-only tool boundary viewer — Phase 5+ |

---

## Multi-provider framework

| | |
|---|---|
| **Why tempting** | Hermes registry + wizard |
| **Why dangerous** | Violates Phase 3.2/v0.2 freeze; premature abstraction |
| **When allowed** | Only after 2+ individually approved providers — separate phase |

---

## Summary

**Nothing from Hermes Desktop is adopted in Phase 3.2.2.**

Use triage docs only.
