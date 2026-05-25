# Memory Providers — Detailed Reference

**Config:** `~/.hermes/config.yaml` → `memory.provider`  
**Setup:** `hermes memory setup`  
**Code:** `plugins/memory/`, `agent/memory_provider.py`

---

## One-Provider Rule

```yaml
memory:
  provider: honcho   # Only ONE external provider
```

Built-in MEMORY.md + USER.md always active regardless of external provider.

Attempting to register second external provider → rejected with warning.

---

## Provider Comparison

| Provider | Storage | Cost | Depth | Best For |
|----------|---------|------|-------|----------|
| **Honcho** | Cloud/self-hosted | Paid/free | Deep (dialectic) | User modeling, multi-agent |
| **Hindsight** | Provider-specific | Varies | Medium | Long-term recall |
| **Mem0** | Cloud/local | Varies | Medium | Semantic search |
| **OpenViking** | Vector DB | Varies | Medium | Vector memory |
| **Supermemory** | Cloud | Varies | Medium | Cloud persistence |
| **RetainDB** | Structured | Varies | Medium | Retention policies |
| **Holographic** | Holographic | Varies | Medium | Compressed encoding |
| **ByteRover** | Byte-level | Varies | Medium | Fine-grained storage |

---

## Honcho Architecture (Most Documented)

### Two-Layer Injection

```
┌─────────────────────────────────────────┐
│ Base Layer (contextCadence)             │
│ - Session summary                       │
│ - User representation                   │
│ - Peer card                             │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│ Dialectic Layer (dialecticCadence)      │
│ - LLM-synthesized reasoning             │
│ - Cold-start vs warm prompts            │
│ - Depth 1-3 passes                      │
└─────────────────────────────────────────┘
```

### Key Config Knobs

| Key | Default | Controls |
|-----|---------|----------|
| `contextCadence` | 1 | Base layer refresh (API calls) |
| `dialecticCadence` | 2 | Dialectic LLM frequency |
| `dialecticDepth` | 1 | Reasoning passes (1-3) |
| `dialecticMaxChars` | 600 | Max injected chars |
| `recallMode` | hybrid | hybrid/context/tools |
| `writeFrequency` | async | async/turn/session/N |
| `sessionStrategy` | per-directory | Session scoping |

### Honcho Tools (5)

1. `honcho_profile` — read/update peer card
2. `honcho_search` — semantic search
3. `honcho_context` — session context
4. `honcho_reasoning` — LLM-synthesized
5. `honcho_conclude` — create/delete conclusions

---

## Lifecycle Integration

```
Session Start
  → initialize(session_id)
  → system_prompt_block() injected

Each Turn
  → prefetch(query) [background, non-blocking]
  → ... agent loop ...
  → sync_turn(user, assistant) [async write]

Context Compression
  → on_pre_compress(messages) → extract memories

Subagent Delegation
  → on_delegation(task, result) → parent observes

Built-in Memory Write
  → on_memory_write(action, target, content) → mirror

Session End
  → on_session_end(messages) → batch extraction
  → shutdown()
```

---

## Context Fencing

All provider output sanitized before UI display:

```python
# Stripped patterns:
# - <memory-context>...</memory-context>
# - [System note: The following is recalled memory context...]
# - StreamingContextScrubber for chunk boundaries
```

Prevents memory injection from appearing as user-visible content.

---

## Dangerous Complexity

Honcho alone has 15+ config knobs. Risk of misconfiguration:
- Too frequent dialectic → cost explosion
- Wrong sessionStrategy → context bleed between projects
- cron agent_context → corrupted user representation (mitigated by tagging)

**Mitigation:** One-provider rule, agent_context tagging, context fencing.

---

## Agent-OS Integration Candidate

Extract MemoryProvider ABC as reference for `02_memory/` provider abstraction:
- Lifecycle hooks pattern
- One-provider enforcement
- Context fencing
- Agent context tagging (primary/subagent/cron)
