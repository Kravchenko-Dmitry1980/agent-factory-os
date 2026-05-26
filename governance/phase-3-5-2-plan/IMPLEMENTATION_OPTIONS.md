# Implementation Options

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## Option A — Documentation only

**Description:** Keep hands-on markdown; operator runs commands manually.

| Pros | Cons |
|------|------|
| Safest — zero code risk | Still not touchable at runtime |
| No maintenance | No menu, no live Russian summary |
| Already done (Phase 3.5.1) | Stakeholder demos need hand-holding |

**Verdict:** Current state. Insufficient for operator UX goal.

---

## Option B — One small stdlib CLI wrapper (recommended)

**Description:** Single `demo_runner.py` — menu, subprocess, parse, Russian summary.

| Pros | Cons |
|------|------|
| Tangible improvement | Could grow if discipline slips |
| Low complexity | Parse fragility if demo output format changes |
| No agent logic change | Manual testing burden |
| No dependencies | No fancy TUI |
| Aligns with Phase 3.5.1 recommendation | |

**Verdict:** **Recommended for Phase 3.5.2-Impl.**

---

## Option C — Rich terminal UI

**Description:** Use `rich`, `prompt_toolkit`, or curses for colors, tables, progress.

| Pros | Cons |
|------|------|
| Nicer UX | Requires dependency |
| Better menus | Violates stdlib-only plan |
| | Platform compatibility issues on Windows |
| | Scope creep toward product UI |

**Verdict:** **Defer.** Not for v0.1 runner.

---

## Option D — Web UI / Operator Console

**Description:** Browser dashboard, chat, history, agent cards.

| Pros | Cons |
|------|------|
| Product-like feel | Too early |
| Good for demos | Platform drift |
| | High effort |
| | Conflicts with lab scope |

**Verdict:** **Out of scope.** Backlog only.

---

## Comparison matrix

| Criterion | A Docs | B Stdlib | C Rich | D Web |
|-----------|--------|----------|--------|-------|
| Operator UX | Low | Medium | High | Highest |
| Risk | None | Low | Medium | High |
| Dependencies | 0 | 0 | 1+ | Many |
| Time to impl | 0 | Small | Medium | Large |
| Agent logic change | No | No | No | Tempting |
| Fits Phase 3 | Yes | **Yes** | Marginal | No |

---

## Recommendation

**Option B** for Phase 3.5.2-Impl.

Path: [RECOMMENDED_IMPLEMENTATION_PATH.md](RECOMMENDED_IMPLEMENTATION_PATH.md).
