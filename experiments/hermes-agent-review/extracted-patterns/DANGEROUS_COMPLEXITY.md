# Dangerous Complexity Areas

Areas in Hermes architecture that pose maintenance, understanding, or integration risks.

---

## Code Complexity

| File | Lines | Risk |
|------|-------|------|
| `hermes_cli/main.py` | ~14,000 | God entry point — all CLI commands |
| `gateway/run.py` | ~18,500 | Platform matrix — 20 adapters |
| `cli.py` | ~15,000 | TUI + REPL + slash commands |
| `tools/mcp_tool.py` | ~3,600 | OAuth, reconnect, sampling |
| `tools/delegate_tool.py` | ~2,800 | Subagent lifecycle |
| `hermes_cli/config.py` | ~5,650 | Config migration complexity |
| `agent/conversation_loop.py` | ~4,300 | Core loop state machine |

**Risk:** Changes require understanding large monolithic files.

**Mitigation in Hermes:** Extensive test suite (~3000+ tests).

---

## Conceptual Complexity

### Dual Multi-Agent Models

`delegate_task` and Kanban look similar but are fundamentally different.

**Risk:** Users choose wrong primitive → failed workflows.

**Mitigation:** Decision matrix in docs. Still easy to misuse.

### Memory Provider Matrix

8 external providers × built-in × Honcho config knobs (15+).

**Risk:** Misconfiguration → cost explosion or corrupted user model.

**Mitigation:** One-provider rule. Agent context tagging. Setup wizard.

### Profile × Gateway × Kanban

Three isolation dimensions interact:
- Profile = agent identity
- Gateway = platform session
- Kanban board = task queue

**Risk:** State confusion across dimensions.

**Mitigation:** Explicit env vars (HERMES_KANBAN_BOARD). Documentation.

---

## Operational Complexity

### Gateway Platform Matrix

20 messaging platform adapters, each with:
- Auth flow
- Message format
- Media handling
- Rate limits
- Platform-specific quirks

**Risk:** Any platform API change breaks adapter.

### OAuth MCP Flow

Interactive OAuth in headless environments requires:
- Paste-back flow
- SSH port forwarding
- 30s auto-reload race condition

**Risk:** Auth failures in production deployments.

### Sandbox Backend Selection

7 backends with different:
- Config schemas
- Persistence models
- Cost structures
- Security boundaries

**Risk:** Wrong backend for use case.

---

## Integration Complexity (If Connecting to Agent-OS)

| Area | Complexity | Recommendation |
|------|------------|----------------|
| Full runtime | Very high | Do not integrate |
| Memory patterns | Low | Extract knowledge only |
| Multi-agent patterns | Medium | Extract decision matrix |
| MCP client | Medium | Reference, don't port |
| Gateway | Very high | Do not integrate |
| Skills system | Medium | Extract progressive disclosure |

---

## Anti-Pattern Indicators in Hermes

These are **not bugs** but complexity signals:

1. **Monolithic entry points** — main.py, run.py, cli.py
2. **Config migration chain** — config.py grows with each version
3. **Platform adapter proliferation** — 20 and counting
4. **Provider plugin matrix** — 8 memory providers
5. **Skill catalog size** — 160+ skills
6. **Honcho config surface** — 15+ orthogonal knobs

---

## Lessons for Agent-OS Design

If building agent runtime (not recommended from this research):

1. **Avoid monolithic entry points** — split CLI commands early
2. **Limit plugin matrix** — one-provider rule is good pattern
3. **Explicit primitive distinction** — document delegate vs Kanban clearly
4. **Bound memory by design** — char limits are feature
5. **Test suite investment** — Hermes survives complexity via 3000+ tests

---

## Safe Extraction Zones

These areas are safe to extract patterns without inheriting complexity:

- Memory char limits + frozen snapshot
- Progressive skill disclosure levels
- Subagent tool restrictions list
- Kanban vs delegate decision matrix
- Profile isolation model
- Agent context tagging
- Curator invariants (never auto-delete)

See `anti-patterns/ANTI_PATTERNS.md` for explicit anti-patterns.
