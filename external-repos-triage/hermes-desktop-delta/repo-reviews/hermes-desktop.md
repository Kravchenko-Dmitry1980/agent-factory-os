# Repository Review: hermes-desktop

## Basic Info

| Field | Value |
|-------|-------|
| **URL** | https://github.com/fathah/hermes-desktop |
| **Local path** | `external-repos-triage/source/hermes-desktop/` |
| **Commit inspected** | `075e516` (2026-05-26) |
| **Package version** | 0.5.1 |
| **Main purpose** | Native desktop GUI for installing, configuring, and operating Hermes Agent |
| **Main stack** | Electron 39, React 19, TypeScript 5.9, Tailwind 4, Vite 7, better-sqlite3, i18next, Vitest |
| **License** | MIT |
| **Maturity signal** | Active development; README warns features may break; releases + downloads badges; large test suite |
| **Activity signal** | Very recent commits (same day as triage); merge PR #382 (Nous Portal providers) |

---

## What It Is

Desktop **operator shell** around [Hermes Agent](https://github.com/NousResearch/hermes-agent): guided install into `~/.hermes`, provider setup, streaming chat, session history, profiles, memory, skills, tools, cron schedules, 16 messaging gateways, persona (SOUL.md), auto-updater.

Talks to local Hermes API (`127.0.0.1:8642`) or **remote mode** (URL + API key).

---

## What It Is Not

- Not Agent-OS or Agent Builder Kit
- Not a governance-first template system
- Not approval-gate / freeze-record oriented
- Not production-safe by default (unsigned installers, broad tool surface)
- Not something we run or adopt in Phase 3

---

## Main Surfaces

| Surface | Role | Agent-OS relevance |
|---------|------|-------------------|
| **Chat** | SSE streaming, slash commands, tool progress | Future trace + approval UX reference |
| **Sessions** | SQLite FTS5 history, resume | Future session/trace viewer |
| **Profiles / Agents** | Isolated Hermes environments | Profile ≠ our template model |
| **Memory** | Edit entries + external memory providers | **Dangerous** — conflicts memory-boundary doctrine |
| **Skills** | Browse/install skills | Supply-chain risk if copied blindly |
| **Tools** | 14 toolsets toggle | Shows autonomy surface area |
| **Schedules** | Cron + 15 delivery targets | **Dangerous** — unattended autonomy |
| **Gateways** | Telegram, Discord, Slack, … (16) | **Dangerous** — outbound messaging |
| **Providers / Models** | Multi-provider + credential pools | UX lessons only; not our framework |
| **Settings** | Backup, logs, network, theme | Ops patterns |
| **Updates / Installers** | electron-updater, unsigned builds | Security concern |

Additional: Persona (SOUL.md), Kanban, Office (Claw3d 3D UI).

---

## Useful Ideas for Agent-OS

- **Visible operator surfaces** for non-builder users (approvals, traces, eval status)
- **Session/search UX** for long-running agent work
- **Provider setup wizard** patterns (without copying credential storage)
- **Tool/skill enable-disable** as governance UI concept
- **Security hardening tests** (electron-security.test.ts — contextIsolation, sandbox)
- **i18n framework** ready for community locales

---

## Dangerous Ideas for Agent-OS

- **Self-improving / closed learning loop** marketing (Hermes Agent core)
- **16 gateways + schedules** — autonomy without our approval gates
- **Remote mode** — expands attack surface
- **Skill installer** — supply chain
- **Memory providers** (Mem0, Supermemory, …) — persistent memory hype
- **Persona/SOUL editor** — persona-over-architecture drift
- **Provider registry in desktop** — tempts premature multi-provider framework

---

## Security Concerns

- Electron IPC + preload trust boundary (mitigated in code, still complex)
- API keys in `~/.hermes/.env` and credential pools
- Installer runs shell scripts (Hermes official installer)
- Unsigned Windows/macOS builds
- Remote API mode with shared API key
- Gateway tokens in local config
- Auto-updater trust chain
- PostHog analytics in dependencies

---

## What We Can Learn

- Operator Console is a **separate product layer** from specs/templates
- GUI makes **hidden autonomy** easy (tools, schedules, gateways)
- Provider UX ≠ provider governance — need explicit gates
- Desktop security is its own architecture domain

---

## What We Must Not Copy

- Electron app structure, npm stack, Hermes installer flow
- Gateway/schedule implementations
- Skill install UX without supply-chain review
- Memory provider integrations
- Provider registry as our abstraction
- Remote mode defaults

---

## Decision

**STUDY_LATER / RESEARCH_ONLY**

Use for Operator Console backlog and security checklist. **Do not adopt** into Agent-OS Phase 3.
