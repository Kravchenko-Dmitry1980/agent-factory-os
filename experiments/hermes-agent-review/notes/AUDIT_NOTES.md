# Architecture Audit Notes

Ad-hoc notes from initial architecture audit (2026-05-25).

---

## First Impressions

Hermes is a **production monolith**, not a research prototype. Evidence:
- 3000+ tests
- 20+ gateway platforms
- 8 memory providers
- Docusaurus docs site with i18n
- MIT license, active development (v0.14.0)

Compare to Agent-OS: knowledge corpus vs runnable product.

---

## Surprising Findings

1. **Two multi-agent primitives** — not one. Kanban is first-class, not afterthought.

2. **Frozen memory snapshot** — explicit design for prompt cache, not oversight.

3. **Curator** — self-improving skills with inactivity trigger, not cron.

4. **One-provider rule** — enforced in code, not just docs.

5. **Profiles as digital twins** — Kanban workers are profiles, not subagents.

6. **7 sandbox backends** — including serverless hibernate (Modal, Daytona).

---

## Code Smells (Non-blocking for Research)

- main.py, run.py, cli.py are very large
- config.py migration chain grows each version
- mcp_tool.py handles too many concerns

These are production trade-offs, not research blockers.

---

## Docs Quality

Excellent. Docusaurus site with:
- User guide
- Developer guide (26 files)
- Reference
- Generated skill catalog
- i18n (zh-Hans)

Better documented than most open-source agents.

---

## Comparison Insight

| Source | Strength |
|--------|----------|
| Claude Code | Fleet-scale patterns, error recovery |
| Code-as-Harness | Theoretical framework |
| Hermes | Self-improving loop, multi-platform, production features |

Agent-OS benefits from all three, none replaces others.

---

## Next Deep Dives

Priority order:
1. conversation_loop.py state machine
2. hermes_state.py SQLite schema
3. delegate_tool.py restrictions exhaustive
4. kanban_db.py schema + dispatcher logic
5. Honcho plugin dialectic implementation

---

## Questions for Phase 2

- How does skill creation trigger vs memory write?
- What's the exact FTS5 schema?
- How does gateway session key resolve?
- What's the curator skill quality heuristic?
- How does execute_code RPC work internally?
