# Hermes Desktop Delta Triage

**Phase:** 3.2.2  
**Date:** 2026-05-26  
**Verdict:** Research-only

---

## Executive Summary

Hermes Desktop adds a **GUI operator layer** to Hermes Agent (install, chat, providers, tools, skills, schedules, gateways). The RU fork adds localization and RU-market provider presets (NeuralDeep, Bitrix VibeCode implemented; GigaChat/YandexGPT planned only).

**Decision:** Research-only. Add Operator Console to **future backlog**. **Do not change Phase 3.3 scope.**

---

## What Changed (Hermes ecosystem)

| Before | After (Hermes Desktop) |
|--------|------------------------|
| CLI-first Hermes Agent | Desktop GUI wrapper (v0.5.1, Electron) |
| Manual `~/.hermes` config | Wizard + provider screens + credential pools |
| Developer-operated | Operator-oriented (chat-first UX) |
| — | RU fork with `ru` locale + RU provider presets |

**Agent-OS delta:** We had no Hermes in Phase 2.10 triage. This is **new external reference**, not a regression.

---

## What Is Useful

- Proof that **operators want GUI** for sessions, providers, traces
- Provider wizard UX patterns (with security caveats)
- Electron hardening test ideas
- RU-first localization model (full locale modules)
- OpenAI-compatible custom endpoint pattern (RU fork)
- gui-surface-map for future console planning

---

## What Is Dangerous

- 16 gateways + schedules = unattended autonomy
- Skill installer = supply chain
- Memory providers + SOUL persona = digital twin drift
- Provider registry tempts multi-provider framework
- Remote mode + plaintext `.env` secrets
- Unsigned installers + auto-updater trust
- "Self-improving" marketing vs governance-first

---

## What This Means for Agent-OS

1. **Markdown-first remains correct** for Phase 3 builders
2. **Operator Console** belongs in Phase 4+ backlog (trace, approval, eval, freeze views)
3. **Never copy** Hermes feature bundle — cherry-pick governance-visible surfaces only
4. Hermes validates our **no-runtime/no-factory** discipline was right

---

## What This Means for RU Product Direction

- RU-first UX is validated (fork + our `curriculum/ru/`)
- RU providers belong in **research backlog** with implemented/planned honesty
- Future console needs RU mode per [ru-operator-console-requirements.md](../../external-repos-triage/hermes-desktop-delta/ru-product/ru-operator-console-requirements.md)
- Do not endorse RU fork as production path

---

## What This Means for Provider Strategy

- Phase 3.3 stays: **single real provider boundary plan**, not framework
- Hermes multi-provider UI is **counter-reference**
- RU providers: compare later after first global provider frozen
- Mock v0.2 baseline unchanged

---

## What Must Stay Frozen

- review-assistant-thin-v0.2
- Agent Builder Kit spec body
- No provider framework
- No desktop UI
- No gateways/schedules/skills install

---

## Decision

**Research-only.** Operator Console → future backlog. Phase 3.3 unchanged.
