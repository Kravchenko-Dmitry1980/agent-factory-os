# Self-Improving Skills — Curator Pattern

**Code:** `agent/curator.py`, `tools/skill_manager_tool.py`, `tools/skill_usage.py`  
**State:** `~/.hermes/skills/.curator_state`

---

## Definition

Self-improving skills = agent-created skills that evolve through use, with automated lifecycle management by the Curator auxiliary agent.

---

## Closed Learning Loop

```
Agent completes complex task
  → Creates skill via skill_manage (if warranted)
  → Uses skill in future sessions
  → Curator reviews on inactivity (7-day default)
    → Pin valuable skills
    → Archive stale skills (30+ days unused)
    → Consolidate overlapping skills
    → Patch outdated procedures
  → Skills improve over time without user intervention
```

---

## Curator Architecture

```
Main Agent (idle for min_idle_hours)
  → maybe_run_curator() checks interval
    → Spawn forked AIAgent (auxiliary model)
      → toolset: skill_manage only
      → Reviews agent-created skills
      → Applies lifecycle transitions
    → Persist .curator_state
    → Optional: show summary to user
```

**Key design:** Curator uses auxiliary client, never touches main session's prompt cache.

---

## Lifecycle States

| State | Trigger | Action |
|-------|---------|--------|
| Active | Default | Available for use |
| Pinned | Manual or curator | Bypass all auto-transitions |
| Stale | 30+ days unused | Candidate for consolidation |
| Archived | 90+ days unused | Hidden but recoverable |

**Never:** Auto-delete. Archive only.

---

## Agent-Created vs Bundled

```python
# tools/skill_usage.py
is_agent_created(skill_path) → bool
```

Curator **only** touches agent-created skills. Bundled and hub-installed skills are immutable by curator.

---

## skill_manage Tool

Curator uses `skill_manage` with actions:
- `pin` — protect from auto-transitions
- `archive` — hide but preserve
- `consolidate` — merge overlapping skills
- `patch` — update procedure sections
- `create` — new skill from experience

---

## Configuration

```yaml
# Implicit defaults in curator.py
curator:
  interval_hours: 168      # 7 days between runs
  min_idle_hours: 2        # Agent must be idle
  stale_after_days: 30     # Mark stale
  archive_after_days: 90   # Auto-archive
```

Uses auxiliary model (configurable separately from main model).

---

## Comparison with Static Skills

| Aspect | Static (Cursor skills) | Self-Improving (Hermes) |
|--------|------------------------|-------------------------|
| Creation | User/manual | Agent after complex tasks |
| Updates | User edits | Curator + agent patches |
| Lifecycle | Manual | Automated stale/archive |
| Scope | Any skill | Agent-created only |
| Deletion | User deletes | Archive only (recoverable) |

---

## Digital Twin Implications

Skills as **procedural memory** that evolves:
- Agent learns workflows → encodes as skills
- Curator prunes outdated procedures
- Pinned skills = core competencies
- Archived skills = historical knowledge (recoverable)

This is closer to human skill acquisition than static prompt injection.

---

## Agent-OS Integration Candidate

Pattern for `06_digital-twins/evolving-memory.md`:
- Inactivity-triggered maintenance
- Lifecycle states (active/stale/archived)
- Auxiliary agent for review (not main loop)
- Never auto-delete invariant
- Agent-created scope restriction

---

## Open Questions

1. How does curator handle skill conflicts (two skills for same task)?
2. What triggers skill creation vs memory write?
3. How is skill quality evaluated before pinning?
4. Can user override curator decisions?
