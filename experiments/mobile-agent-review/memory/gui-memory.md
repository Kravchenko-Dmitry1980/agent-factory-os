# GUI Memory

Что агент запоминает между шагами и сессиями в GUI-контексте.

---

## v2 Memory Agent

**Trigger:** After action (+ optional reflection)

**Prompt:** `get_memory_prompt()` — asks what on-screen content should be stored for later steps.

**Storage:** Single growing string `memory` injected in action prompt under `### Memory ###`

**Use cases:**
- Phone numbers, prices, names read from apps
- Multi-app tasks requiring recall

**Switch:** `memory_switch = False` if task doesn't need cross-step facts.

---

## v3 Notetaker

**Class:** `Notetaker` in `mobile_agent_e.py`

**Flag:** `--notetaker True` in `run_mobileagentv3.py`

**Storage:** `InfoPool.important_notes` — consolidated notes string

**Difference from v2 memory:** Explicit agent role tied to Manager replan prompts (`### Important Notes ###`).

---

## GUI-Owl 1.5 Built-in Memory

v3.5 README:
- Long-horizon memory without external workflow
- MemGUI-Bench performance claims
- Implemented in model weights + inference context, not separate Python module in `mobile_use/`

---

## Mobile-Agent-E Experience Memory

Persistent evolution beyond session:

| Component | Stores |
|-----------|--------|
| ExperienceRetrieverShortCut | Successful action sequences |
| ExperienceRetrieverTips | Textual tips |
| ExperienceReflector* | Updates after episodes |

Scripts: `scripts/run_tasks_evolution.sh`

Pattern: **self-evolving GUI memory** — closest to Agent-OS long-term memory concepts.

---

## What Is NOT Stored

- Full screenshot history indefinitely (context limits → summaries only)
- Structured semantic graph of UI
- User identity / cross-user memory
- Encrypted or PII-aware memory policies

---

## Agent-OS Taxonomy Mapping (Research Only)

| MobileAgent | Agent-OS concept |
|-------------|------------------|
| v2 `memory` string | Working / episodic scratchpad |
| v3 `important_notes` | Episodic memory (curated) |
| MA-E experience store | Semantic + procedural memory |
| GUI-Owl 1.5 internal | Model context compression (TBD) |

Do not merge into Agent-OS taxonomy yet — per experiment boundaries.
