# USER.md — Concept Documentation

**Runtime path:** `~/.hermes/memories/USER.md`  
**Code:** `tools/memory_tool.py`  
**Char limit:** 1,375 (~500 tokens)

---

## Definition

USER.md is the **user profile store** — bounded facts about the user's identity, preferences, communication style, and expectations. Enables personalization across sessions without re-asking.

---

## What Goes in USER.md

| Category | Examples |
|----------|----------|
| Identity | Name, role, timezone |
| Communication style | "Prefers concise responses", "Wants code examples" |
| Pet peeves | "Dislikes verbose explanations", "No emoji in code" |
| Workflow habits | "Reviews PRs in mornings", "Uses vim keybindings" |
| Technical level | "Senior Rust developer", "Learning Python" |

---

## USER.md vs MEMORY.md

| Aspect | USER.md | MEMORY.md |
|--------|---------|-----------|
| About | The user | The environment/work |
| Target param | `user` | `memory` |
| Limit | 1,375 chars | 2,200 chars |
| Typical entries | 5-10 | 8-15 |
| Updates when | User preferences change | Environment/work changes |

---

## Format in System Prompt

```
══════════════════════════════════════════════
USER PROFILE [45% — 619/1,375 chars]
══════════════════════════════════════════════
Name: Alex, Senior backend engineer, UTC+3
§
Prefers TypeScript over JavaScript, concise responses
§
Reviews PRs in morning, avoids Friday deploys
```

---

## Honcho Integration

When Honcho is active as external memory provider:
- USER.md provides immediate, bounded user facts
- Honcho peer card provides deeper dialectic user modeling
- Both coexist — USER.md is fast/static, Honcho is dynamic/deep

Honcho config for profiles:
- Each profile gets dedicated AI peer
- Shared user workspace
- `--clone` creates new AI peer automatically

---

## Digital Twin Implications

USER.md is the **minimal viable user model**:
- Bounded (forces curation)
- Agent-managed (not user-edited directly)
- Session-persistent (frozen snapshot)
- Complements external providers (Honcho dialectic)

For digital twin architecture:
- USER.md = static profile layer
- Honcho = dynamic modeling layer
- Session search = episodic recall layer
- Skills = procedural knowledge layer

---

## Agent-OS Relevance

Maps to:
- `06_digital-twins/persistent-identity.md` — user model persistence
- `02_memory/memory-taxonomy.md` — user model as memory type
- Separation of user facts vs environment facts
