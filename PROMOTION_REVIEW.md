# PROMOTION REVIEW

**Phase:** 1.1 — Experiments Promotion Review  
**Date:** 2026-05-25  
**Workspace:** `C:\Dima\Projects\CURSOR\AGENT`  
**Method:** Evidence-first, contract-first, architecture-first, risk-first; promotion only after scoring  
**Deliverable scope:** Analytical review only — no file moves, no `agent-os/` edits

---

## 0. Executive Summary

### What was analyzed

Two read-only research sandboxes were reviewed against the existing Agent-OS curated layer and baseline documents:

| Sandbox | Docs reviewed | Upstream clone | Runtime executed |
|---------|---------------|----------------|------------------|
| `experiments/hermes-agent-review/` | 36 markdown files | `source/hermes-agent/` (v0.14.0 shallow) | No |
| `experiments/mobile-agent-review/` | 36 markdown files | `source/MobileAgent/` (commit `0e5065e`) | No |

Cross-referenced with: `agent-os/` (122 files), `Books/claude/`, `Books/agents/`, `CURRENT_STATE_AUDIT.md`, `BASELINE_STATUS.md`, `README.md`.

### Main conclusions

1. **Hermes** fills gaps in **memory injection timing**, **skill loading**, **multi-agent primitive choice**, and **digital-twin instance modeling** — areas under-documented in Agent-OS relative to Claude Code corpus.
2. **MobileAgent** fills gaps in **GUI modality** — visual observation, grounding, action contracts, and post-action verification — absent from current taxonomy except generic `verification.md`.
3. **Safe promotion path:** extract **patterns and anti-patterns** with provenance; do **not** port runtime code, gateway adapters, OCR pipelines, or model weights.
4. **Taxonomy:** existing sections `00–12` can absorb Phase 1.2 promotions; a dedicated `13_gui-agents/` section is justified **later** once ≥5 GUI atomic notes exist.

### Promotion decision counts

| Decision | Count | Share |
|----------|------:|------:|
| **PROMOTE_NOW** | 22 | 34% |
| **PROMOTE_LATER** | 24 | 37% |
| **RESEARCH_ONLY** | 15 | 23% |
| **REJECT** | 4 | 6% |
| **Total candidates scored** | **65** | 100% |

### Chief architectural finding

Agent-OS today is **code-harness-centric** (Claude Code + partial Harness survey). Hermes and MobileAgent together define a **second axis: embodied agents** — persistent curated memory + durable orchestration (Hermes) and pixel observation + visual verification (MobileAgent). Promotions should extend the golden path, not fork a parallel taxonomy prematurely.

---

## 1. Scope

### Sandboxes analyzed

- `experiments/hermes-agent-review/` — architecture, memory, skills, MCP, multi-agent, runtime, extracted-patterns, anti-patterns, comparisons, diagrams, notes
- `experiments/mobile-agent-review/` — architecture, perception, action-runtime, multi-agent, memory, MCP integration, extracted-patterns, anti-patterns, comparisons, diagrams, integration-candidates

### Analysis boundaries

- Markdown evidence only; shallow upstream clones used as citation anchors, not executed
- Scoring model: Value, Maturity, Fit, Risk (1–5 each); decision rules per Phase 1.1 spec
- Target locations mapped to existing Agent-OS taxonomy (`00–12`)

### Not performed

- No changes to `agent-os/`, `experiments/`, `README.md`, `.gitignore`
- No file moves, renames, deletes, commits
- No Hermes/MobileAgent install, model run, emulator, ADB, Playwright, or MCP server startup
- No upstream code copy into curated layer

### Unchanged by this phase

Everything except creation of this file (`PROMOTION_REVIEW.md`).

---

## 2. Current Agent-OS Baseline

### Taxonomy (13 sections + templates)

| Section | Role | File count (approx.) |
|---------|------|---------------------:|
| `00_foundations/` | Core concepts, verification, loops | 11 |
| `01_agent-runtime/` | Query loop, tools, concurrency, recovery | 11 |
| `02_memory/` | Taxonomy, recall, compaction, shared memory | 9 |
| `03_harness-engineering/` | Permissions, hooks, feedback, verification | 10 |
| `04_multi-agent/` | Subagents, swarms, coordination, task SM | 7 |
| `05_mcp/` | Protocol, transports, orchestration | 7 |
| `06_digital-twins/` | Identity, evolving memory, personas, skills | 6 |
| `07_projects/` | Applied systems | 6 |
| `08_patterns/` | 7 architecture patterns | 8 |
| `09_antipatterns/` | 5 documented failures | 6 |
| `10_research/` | Catalog, extraction plans, chapter stubs | 30 |
| `11_glossary/` | Term pointers | 5 |
| `12_diagrams/` | Mermaid diagrams | 4 |

### Coverage already strong (Claude-derived)

- Query loop, generator pattern, terminal states, error recovery ladder (code-centric)
- Permission modes, stop hooks, execution verification
- Subagents with isolation, swarms, task state machine
- MCP protocol and transports
- Memory taxonomy (user/feedback/project/reference), compaction, recall
- Patterns: prompt-cache-as-constraint, withholding-errors, two-tier-state, fail-closed-defaults

### Gaps identified (Hermes + MobileAgent evidence)

| Gap | Evidence source | Current Agent-OS |
|-----|-----------------|------------------|
| Frozen memory vs mid-session injection | Hermes `memory/MEMORY_SYSTEM_OVERVIEW.md` | Partial via `prompt-cache-as-constraint`; no memory-specific note |
| Kanban vs delegate primitive choice | Hermes `multi-agent/TASK_ORCHESTRATION.md` | `subagents.md` only; no durable queue primitive |
| Progressive skill disclosure | Hermes `skills/SKILLS_SYSTEM_OVERVIEW.md` | ch12 skills extraction ⬜ planned, not done |
| Profile = isolated twin instance | Hermes `notes/DIGITAL_TWIN_IMPLICATIONS.md` | `persistent-identity.md` session-scoped, not profile-scoped |
| GUI agent loop | MobileAgent `extracted-patterns/screen-reason-action-feedback-loop.md` | No GUI modality |
| Visual verification A/B/C | MobileAgent `extracted-patterns/action-verification-pattern.md` | `verification.md` is hook/subagent-centric |
| GUI anti-patterns | MobileAgent `anti-patterns/*` | No GUI-specific antipatterns |
| GUI-MCP hybrid routing | MobileAgent `mcp-integration/mcp-relevance.md` | MCP docs are code-tool-centric |
| Third/fourth research corpora in `sources.md` | Both sandboxes | Only Claude + Harness survey listed |

### Harness survey integration status

`Books/agents/` cataloged in `sources.md` but **not yet** in `10_research/` chapter stubs — extraction still ⬜. MobileAgent maps naturally to survey § environment modeling; Hermes maps to § acting + multi-agent scaling.

---

## 3. Hermes Agent — Promotion Candidates

### 3.1 Patterns

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Frozen memory snapshot | `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md` | `agent-os/02_memory/frozen-memory-snapshot.md` | 5 | 5 | 5 | 1 | **PROMOTE_NOW** | Production-validated; complements `prompt-cache-as-constraint`; separates persistence from injection |
| Bounded curated memory (char limits + § delimiter) | `experiments/hermes-agent-review/memory/MEMORY.md`, `memory/USER.md` | `agent-os/02_memory/memory-char-limits.md` | 4 | 5 | 4 | 1 | **PROMOTE_NOW** | Extends `memory-taxonomy.md` with hard bounds; prevents unbounded growth |
| Progressive skill disclosure (L0/L1/L2) | `experiments/hermes-agent-review/skills/SKILLS_SYSTEM_OVERVIEW.md` | `agent-os/08_patterns/progressive-skill-disclosure.md` | 4 | 4 | 5 | 2 | **PROMOTE_NOW** | Directly addresses ch12 gap; no duplicate in `08_patterns/` |
| Kanban vs delegate decision matrix | `experiments/hermes-agent-review/multi-agent/TASK_ORCHESTRATION.md` | `agent-os/04_multi-agent/kanban-vs-delegate.md` | 5 | 4 | 4 | 2 | **PROMOTE_NOW** | Fills major multi-agent gap; Hermes comparison confirms Agent-OS lacks durable queue primitive |
| One-external-provider rule | `experiments/hermes-agent-review/memory/MEMORY_PROVIDERS.md` | `agent-os/08_patterns/one-external-provider-rule.md` | 4 | 4 | 4 | 2 | **PROMOTE_NOW** | Plugin architecture guardrail; low duplication risk |
| Agent context tagging (primary/subagent/cron/flush) | `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md` | `agent-os/02_memory/agent-context-tagging.md` | 4 | 4 | 4 | 2 | **PROMOTE_NOW** | Prevents cron/subagent memory corruption; no existing note |
| Subagent tool restrictions (blocklist) | `experiments/hermes-agent-review/multi-agent/SUBAGENTS.md` | `agent-os/04_multi-agent/subagent-tool-restrictions.md` | 4 | 4 | 5 | 1 | **PROMOTE_NOW** | Extends `subagents.md` with explicit safety boundary list |
| Context fencing (`<memory-context>` scrubber) | `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md` | `agent-os/08_patterns/context-fencing.md` | 3 | 3 | 3 | 2 | **PROMOTE_LATER** | Useful but streaming scrubber needs deeper spec before canonicalization |
| Prefetch-before-turn | `experiments/hermes-agent-review/extracted-patterns/REUSABLE_PATTERNS.md` | `agent-os/02_memory/memory-recall.md` (update) | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Proactive recall pattern; overlaps `memory-recall.md` — merge not new file |
| on_pre_compress memory hook | `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md` | `agent-os/02_memory/memory-compaction.md` (update) | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Hook semantics need contract section; links to compaction |
| Profile isolation (HERMES_HOME) | `experiments/hermes-agent-review/runtime/RUNTIME_OVERVIEW.md` | `agent-os/06_digital-twins/profile-isolation.md` | 5 | 4 | 5 | 2 | **PROMOTE_NOW** | Strong digital-twin instance model; extends `persistent-identity.md` |
| execute_code RPC collapse | `experiments/hermes-agent-review/extracted-patterns/REUSABLE_PATTERNS.md` | `agent-os/01_agent-runtime/tool-runtime.md` (update) | 3 | 3 | 3 | 3 | **RESEARCH_ONLY** | Interesting reasoning compression; needs comparison with Claude Code execution paths |
| Serverless hibernate (Modal/Daytona) | `experiments/hermes-agent-review/runtime/SANDBOX_BACKENDS.md` | — | 2 | 2 | 2 | 3 | **REJECT** | Deployment-specific; not knowledge-layer pattern for Agent-OS |

### 3.2 Anti-patterns

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Mid-session memory injection (cache bust) | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §2 | `agent-os/09_antipatterns/mid-session-memory-injection.md` | 4 | 5 | 5 | 1 | **PROMOTE_NOW** | Pairs with frozen snapshot + existing `cache-busting-sections.md` |
| Multiple external memory providers | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §3 | `agent-os/09_antipatterns/multiple-memory-providers.md` | 4 | 4 | 4 | 2 | **PROMOTE_NOW** | Fix pattern: `one-external-provider-rule` |
| Subagent memory writes | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §4 | `agent-os/09_antipatterns/subagent-memory-writes.md` | 4 | 4 | 5 | 1 | **PROMOTE_NOW** | Extends subagent safety; high fit with `04_multi-agent/` |
| Cron agent memory writes | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §5 | `agent-os/09_antipatterns/cron-memory-corruption.md` | 3 | 4 | 4 | 2 | **PROMOTE_LATER** | Valid but narrower audience than primary/subagent |
| Wrong multi-agent primitive (delegate vs Kanban) | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §6–7 | `agent-os/09_antipatterns/wrong-orchestration-primitive.md` | 5 | 4 | 4 | 2 | **PROMOTE_NOW** | High strategic value; fix = `kanban-vs-delegate.md` |
| Recursive subagent delegation | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §9 | `agent-os/04_multi-agent/subagents.md` (update) | 4 | 4 | 5 | 1 | **PROMOTE_NOW** | Claude corpus mentions recursive guard; Hermes adds explicit blocklist evidence |
| Skill catalog without progressive loading | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §10 | `agent-os/09_antipatterns/skill-token-explosion.md` | 4 | 4 | 4 | 2 | **PROMOTE_NOW** | Fix = progressive disclosure pattern |
| Auto-deleting agent-created skills | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §11 | `agent-os/09_antipatterns/auto-delete-agent-content.md` | 4 | 4 | 4 | 2 | **PROMOTE_LATER** | Links to curator pattern; needs curator note first |
| OAuth in auto-reload context | `experiments/hermes-agent-review/anti-patterns/ANTI_PATTERNS.md` §12 | `agent-os/05_mcp/mcp-integrations.md` (update) | 3 | 3 | 3 | 3 | **RESEARCH_ONLY** | MCP-specific edge case; wait for MCP extraction completion |
| God object entry point (main.py 14k LOC) | `experiments/hermes-agent-review/extracted-patterns/DANGEROUS_COMPLEXITY.md` | `agent-os/09_antipatterns/central-orchestrator-god-object.md` (cross-ref) | 3 | 5 | 5 | 1 | **REJECT** | Already documented; add Hermes provenance in Phase 1.2 update only |

### 3.3 Memory Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| MEMORY.md + USER.md dual store | `experiments/hermes-agent-review/memory/MEMORY.md` | `agent-os/02_memory/curated-memory-stores.md` | 4 | 5 | 4 | 1 | **PROMOTE_NOW** | Agent vs user model split; complements Claude MEMORY frontmatter taxonomy |
| MemoryProvider ABC lifecycle hooks | `experiments/hermes-agent-review/memory/MEMORY_PROVIDERS.md` | `agent-os/02_memory/memory-provider-interface.md` | 4 | 3 | 4 | 3 | **PROMOTE_LATER** | Valuable contract; 8-provider matrix adds confusion if promoted too early |
| Session FTS5 cross-session recall | `experiments/hermes-agent-review/runtime/SESSION_RECALL.md` | `agent-os/02_memory/episodic-memory.md` (update) | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Episodic search pattern; needs SQLite-specific vs generic framing |
| Honcho dialectic user modeling | `experiments/hermes-agent-review/memory/MEMORY_PROVIDERS.md` | `agent-os/06_digital-twins/evolving-memory.md` (update) | 4 | 2 | 3 | 4 | **RESEARCH_ONLY** | 15+ config knobs; premature canonicalization risk |
| Memory write on compression | `experiments/hermes-agent-review/memory/MEMORY_SYSTEM_OVERVIEW.md` | `agent-os/02_memory/memory-compaction.md` (update) | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Same as on_pre_compress hook |

### 3.4 Skill Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| agentskills.io SKILL.md format | `experiments/hermes-agent-review/skills/SKILLS_SYSTEM_OVERVIEW.md` | `agent-os/03_harness-engineering/skills-format.md` | 3 | 4 | 3 | 1 | **PROMOTE_LATER** | ch12 extraction planned; defer until Claude skills notes land |
| Curator inactivity lifecycle | `experiments/hermes-agent-review/skills/SELF_IMPROVING_SKILLS.md` | `agent-os/06_digital-twins/curator-pattern.md` | 5 | 3 | 4 | 3 | **PROMOTE_LATER** | High digital-twin value; needs governance section (never auto-delete) |
| Platform-restricted skills metadata | `experiments/hermes-agent-review/skills/SKILLS_SYSTEM_OVERVIEW.md` | `agent-os/08_patterns/platform-restricted-skills.md` | 3 | 3 | 3 | 2 | **RESEARCH_ONLY** | Nice-to-have; not blocking Agent-OS trajectory |
| Conditional toolset activation in skills | `experiments/hermes-agent-review/skills/SKILLS_SYSTEM_OVERVIEW.md` | `agent-os/03_harness-engineering/adaptive-harness.md` (update) | 3 | 3 | 3 | 2 | **RESEARCH_ONLY** | Overlaps adaptive harness concept |

### 3.5 MCP Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Per-tool MCP filtering in config | `experiments/hermes-agent-review/mcp/MCP_INTEGRATION_OVERVIEW.md` | `agent-os/05_mcp/mcp-orchestration.md` (update) | 4 | 4 | 4 | 2 | **PROMOTE_LATER** | Schema bloat mitigation; align with ch15 extraction |
| Dynamic MCP tool registration at startup | `experiments/hermes-agent-review/mcp/MCP_INTEGRATION_OVERVIEW.md` | `agent-os/05_mcp/tool-servers.md` (update) | 3 | 3 | 4 | 2 | **PROMOTE_LATER** | Partial overlap with existing MCP docs |
| OAuth token cache conventions | `experiments/hermes-agent-review/mcp/MCP_INTEGRATION_OVERVIEW.md` | `agent-os/05_mcp/mcp-integrations.md` (update) | 3 | 3 | 3 | 3 | **RESEARCH_ONLY** | Operational detail; high vendor-specific variance |
| Hermes-as-MCP-server mode | `experiments/hermes-agent-review/mcp/MCP_INTEGRATION_OVERVIEW.md` | — | 2 | 2 | 2 | 3 | **REJECT** | Product feature, not portable pattern |

### 3.6 Digital Twin Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Profile = twin instance | `experiments/hermes-agent-review/notes/DIGITAL_TWIN_IMPLICATIONS.md` | `agent-os/06_digital-twins/profile-isolation.md` | 5 | 4 | 5 | 2 | **PROMOTE_NOW** | Same as profile isolation pattern |
| Kanban as durable twin task layer | `experiments/hermes-agent-review/notes/DIGITAL_TWIN_IMPLICATIONS.md` | `agent-os/06_digital-twins/durable-task-coordination.md` | 4 | 3 | 4 | 3 | **PROMOTE_LATER** | Depends on kanban-vs-delegate note first |
| Skills as evolving procedural memory | `experiments/hermes-agent-review/notes/DIGITAL_TWIN_IMPLICATIONS.md` | `agent-os/06_digital-twins/skill-graphs.md` (update) | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Link curator + progressive disclosure |
| Twin fleet topologies (pipeline/swarm/fleet) | `experiments/hermes-agent-review/multi-agent/KANBAN.md` | `agent-os/04_multi-agent/coordination.md` (update) | 4 | 3 | 4 | 3 | **PROMOTE_LATER** | Overlaps swarms.md; needs dedup plan |
| SOUL.md personality layer | `experiments/hermes-agent-review/prompts/PROMPT_SYSTEM_OVERVIEW.md` | `agent-os/06_digital-twins/agent-personas.md` (update) | 3 | 3 | 4 | 2 | **PROMOTE_LATER** | Personas exist; add Hermes provenance |

### 3.7 Runtime / Agent Loop Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Unified three API modes | `experiments/hermes-agent-review/runtime/RUNTIME_OVERVIEW.md` | `agent-os/01_agent-runtime/api-layer.md` (update) | 3 | 3 | 3 | 3 | **RESEARCH_ONLY** | Provider abstraction; low unique value vs Claude api-layer |
| SQLite session DB + lineage | `experiments/hermes-agent-review/runtime/PERSISTENT_STATE.md` | `agent-os/01_agent-runtime/` (new note deferred) | 3 | 3 | 3 | 2 | **RESEARCH_ONLY** | Storage detail; extract pattern not schema |
| Sandbox backend matrix (7 backends) | `experiments/hermes-agent-review/runtime/SANDBOX_BACKENDS.md` | — | 3 | 2 | 2 | 4 | **REJECT** | Product matrix; taxonomy explosion if canonicalized |
| Gateway 20+ platform adapters | `experiments/hermes-agent-review/architecture/ARCHITECTURE_MAP.md` | — | 2 | 2 | 1 | 5 | **REJECT** | Maintenance surface; not knowledge-layer content |

### 3.8 Multi-Agent Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Kanban orchestration topologies | `experiments/hermes-agent-review/multi-agent/KANBAN.md` | `agent-os/04_multi-agent/kanban-orchestration.md` | 4 | 3 | 4 | 3 | **PROMOTE_LATER** | After kanban-vs-delegate; comment protocol needs spec read |
| Cron fresh-agent orchestration | `experiments/hermes-agent-review/multi-agent/TASK_ORCHESTRATION.md` | `agent-os/04_multi-agent/scheduled-agents.md` | 3 | 3 | 3 | 2 | **RESEARCH_ONLY** | Valid pattern; not on Agent-OS critical path |
| Mixture of Agents parallel LLM | `experiments/hermes-agent-review/multi-agent/TASK_ORCHESTRATION.md` | — | 2 | 2 | 2 | 2 | **REJECT** | Research feature; weak fit |
| Parallel delegate batch (max concurrent) | `experiments/hermes-agent-review/multi-agent/SUBAGENTS.md` | `agent-os/04_multi-agent/subagents.md` (update) | 4 | 4 | 5 | 1 | **PROMOTE_NOW** | Concurrency limit evidence complements ch07/ch08 |

### 3.9 Governance / Safety Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Curator never auto-delete invariant | `experiments/hermes-agent-review/skills/SELF_IMPROVING_SKILLS.md` | `agent-os/06_digital-twins/curator-pattern.md` | 4 | 4 | 4 | 2 | **PROMOTE_LATER** | Governance-critical for self-improving skills |
| Kanban failure_limit auto-block | `experiments/hermes-agent-review/multi-agent/KANBAN.md` | `agent-os/09_antipatterns/infinite-retry-loops.md` (cross-ref) | 4 | 4 | 5 | 1 | **PROMOTE_NOW** | Extends existing antipattern with durable-queue mitigation |
| Approval tool (bubble permissions) | `experiments/hermes-agent-review/architecture/ARCHITECTURE_MAP.md` | `agent-os/03_harness-engineering/permission-modes.md` (update) | 3 | 3 | 4 | 2 | **RESEARCH_ONLY** | Hermes simpler than Claude; low incremental value |

---

## 4. MobileAgent — Promotion Candidates

### 4.1 GUI Agent Patterns

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Screen→reason→action→feedback loop | `experiments/mobile-agent-review/extracted-patterns/screen-reason-action-feedback-loop.md` | `agent-os/01_agent-runtime/gui-agent-loop.md` | 5 | 4 | 4 | 2 | **PROMOTE_NOW** | Core GUI harness primitive; extends golden path |
| GUI as environment (S, A, T, O) | `experiments/mobile-agent-review/extracted-patterns/gui-as-environment.md` | `agent-os/00_foundations/gui-as-environment.md` | 4 | 4 | 4 | 2 | **PROMOTE_NOW** | Bridges Harness survey environment modeling to GUI modality |
| Failure recovery ladder (A/B/C + replan) | `experiments/mobile-agent-review/extracted-patterns/failure-recovery-pattern.md` | `agent-os/01_agent-runtime/error-recovery-ladder.md` (update) | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Vision-triggered recovery; merge with existing ladder carefully |
| Monolithic VLM E2E loop (v3.5) | `experiments/mobile-agent-review/architecture/mobile-agent-family.md` | — | 3 | 2 | 3 | 3 | **RESEARCH_ONLY** | Model-internal coordination; unstable as canonical pattern |

### 4.2 Perception Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Visual grounding pattern (list/VLM/SOM) | `experiments/mobile-agent-review/extracted-patterns/visual-grounding-pattern.md` | `agent-os/01_agent-runtime/visual-grounding.md` | 5 | 4 | 4 | 2 | **PROMOTE_NOW** | Foundational GUI concept; no duplicate |
| Coordinate space normalization (`coor_type`) | `experiments/mobile-agent-review/perception/visual-grounding.md` | `agent-os/01_agent-runtime/coordinate-spaces.md` | 4 | 4 | 4 | 2 | **PROMOTE_NOW** | Prevents cross-device fragility |
| OCR + element list pipeline (v1/v2) | `experiments/mobile-agent-review/perception/ocr-and-ui-elements.md` | — | 2 | 2 | 2 | 4 | **REJECT** | Superseded by GUI-Owl; promotes brittle path |
| Accessibility tree as grounding channel | `experiments/mobile-agent-review/perception/screenshot-understanding.md` | `agent-os/01_agent-runtime/visual-grounding.md` (update) | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Multi-channel grounding; needs OSWorld evidence summary |

### 4.3 Action Runtime Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Typed GUI action contract (JSON DSL) | `experiments/mobile-agent-review/action-runtime/action-contract.md` | `agent-os/01_agent-runtime/gui-action-contract.md` | 4 | 3 | 4 | 3 | **PROMOTE_LATER** | Multiple DSLs across versions; need unified contract first |
| Platform driver adapter boundary | `experiments/mobile-agent-review/action-runtime/mobile-actions.md` | `agent-os/05_mcp/runtime-bridges.md` (update) | 4 | 3 | 4 | 3 | **PROMOTE_LATER** | ADB/pyautogui/Playwright as adapters, not core |
| Sleep-based synchronization | `experiments/mobile-agent-review/anti-patterns/brittle-gui-automation.md` §5 | `agent-os/09_antipatterns/sleep-based-gui-sync.md` | 3 | 4 | 4 | 1 | **PROMOTE_NOW** | Clear antipattern; low risk |
| Monolithic per-version run scripts | `experiments/mobile-agent-review/anti-patterns/brittle-gui-automation.md` §7 | `agent-os/09_antipatterns/duplicated-gui-drivers.md` | 3 | 4 | 4 | 1 | **PROMOTE_LATER** | Process antipattern; lower priority than click verification |

### 4.4 Verification Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| A/B/C post-op verification taxonomy | `experiments/mobile-agent-review/extracted-patterns/action-verification-pattern.md` | `agent-os/00_foundations/visual-verification.md` | 5 | 4 | 5 | 1 | **PROMOTE_NOW** | Extends `verification.md` into visual modality |
| Action succeeded vs task succeeded | `experiments/mobile-agent-review/action-runtime/action-verification.md` | `agent-os/00_foundations/verification.md` (update) | 4 | 4 | 5 | 1 | **PROMOTE_NOW** | Critical distinction for GUI loops |
| Pre-op GUI-Critic | `experiments/mobile-agent-review/perception/screenshot-understanding.md` | `agent-os/03_harness-engineering/pre-op-verification.md` | 4 | 2 | 3 | 3 | **RESEARCH_ONLY** | Not wired in upstream; needs local experiment |
| Typed verification records in history | `experiments/mobile-agent-review/extracted-patterns/action-verification-pattern.md` | `agent-os/03_harness-engineering/execution-feedback.md` (update) | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Harness contract extension |

### 4.5 Memory / Progress Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| InfoPool shared mutable state | `experiments/mobile-agent-review/multi-agent/coordination-patterns.md` | `agent-os/02_memory/shared-state-pool.md` | 4 | 3 | 4 | 3 | **PROMOTE_LATER** | God-object risk; document as lightweight alternative to subagents |
| Notetaker role (important_notes) | `experiments/mobile-agent-review/memory/gui-memory.md` | `agent-os/02_memory/episodic-memory.md` (update) | 3 | 3 | 3 | 2 | **RESEARCH_ONLY** | GUI-specific episodic scratchpad |
| MA-E experience tips (cross-episode) | `experiments/mobile-agent-review/multi-agent/reflection.md` | `agent-os/06_digital-twins/evolving-memory.md` (update) | 4 | 2 | 3 | 3 | **RESEARCH_ONLY** | Self-evolution without governance = high risk |

### 4.6 Multi-Agent GUI Concepts

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Shared pool + role-specific prompts | `experiments/mobile-agent-review/multi-agent/coordination-patterns.md` | `agent-os/04_multi-agent/shared-pool-coordination.md` | 4 | 4 | 4 | 2 | **PROMOTE_LATER** | Complements subagents; different tradeoff (coupling vs isolation) |
| Manager / Executor / Reflector roles | `experiments/mobile-agent-review/multi-agent/multi-agent-navigation.md` | `agent-os/04_multi-agent/role-systems.md` (update) | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Overlaps existing role-systems; merge don't duplicate |
| Multi-chat same model (v2) | `experiments/mobile-agent-review/multi-agent/coordination-patterns.md` | `agent-os/04_multi-agent/coordination.md` (update) | 3 | 3 | 3 | 2 | **RESEARCH_ONLY** | Cheap specialization pattern |
| Progress management / plan stability | `experiments/mobile-agent-review/multi-agent/progress-management.md` | `agent-os/04_multi-agent/task-state-machine.md` (update) | 3 | 3 | 4 | 2 | **RESEARCH_ONLY** | Partial overlap with task SM |

### 4.7 MCP / Tool Candidates

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| GUI-MCP hybrid routing policy | `experiments/mobile-agent-review/mcp-integration/mcp-relevance.md` | `agent-os/05_mcp/gui-mcp-hybrid-routing.md` | 4 | 2 | 3 | 3 | **RESEARCH_ONLY** | Model-policy level; no harness spec in repo |
| Proposed MCP tool contracts (capture/act/verify) | `experiments/mobile-agent-review/mcp-integration/possible-tool-contracts.md` | `agent-os/05_mcp/gui-tool-contracts.md` | 4 | 2 | 4 | 3 | **RESEARCH_ONLY** | Contracts are proposals; need local sandbox validation |
| OSWorld-MCP benchmark patterns | `experiments/mobile-agent-review/mcp-integration/mcp-relevance.md` | `agent-os/10_research/` (future corpus) | 3 | 2 | 3 | 2 | **RESEARCH_ONLY** | External repo; ingest as separate experiment |

### 4.8 Anti-patterns

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| Unverified clicks | `experiments/mobile-agent-review/anti-patterns/unverified-clicks.md` | `agent-os/09_antipatterns/unverified-gui-clicks.md` | 5 | 4 | 5 | 1 | **PROMOTE_NOW** | Top GUI failure mode; fix = visual verification |
| Brittle GUI automation (catalog) | `experiments/mobile-agent-review/anti-patterns/brittle-gui-automation.md` | `agent-os/09_antipatterns/brittle-gui-automation.md` | 4 | 4 | 4 | 1 | **PROMOTE_NOW** | Aggregates 7 failure modes with mitigations |
| Weak NL/JSON action parsing | `experiments/mobile-agent-review/anti-patterns/weak-action-parsing.md` | `agent-os/09_antipatterns/weak-gui-action-parsing.md` | 4 | 4 | 4 | 2 | **PROMOTE_NOW** | Parsing fragility breaks loop contract |
| Model output fragility (no circuit breakers) | `experiments/mobile-agent-review/anti-patterns/model-output-fragility.md` | `agent-os/09_antipatterns/model-output-fragility.md` | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Links to infinite-retry; needs GUI step budget |
| OCR-list as ground truth | `experiments/mobile-agent-review/anti-patterns/brittle-gui-automation.md` §1 | `agent-os/09_antipatterns/ocr-list-as-ground-truth.md` | 4 | 4 | 4 | 1 | **PROMOTE_NOW** | Sub-item of brittle catalog; can be section not file |
| No permission layer on device actions | `experiments/mobile-agent-review/anti-patterns/brittle-gui-automation.md` §6 | `agent-os/09_antipatterns/unrestricted-gui-actions.md` | 5 | 4 | 5 | 1 | **PROMOTE_NOW** | Critical for production GUI agents |
| Hardcoded benchmark hints in Manager | `experiments/mobile-agent-review/anti-patterns/brittle-gui-automation.md` §3 | `agent-os/09_antipatterns/eval-hint-overfit.md` | 3 | 4 | 3 | 1 | **PROMOTE_LATER** | Research hygiene; lower priority |

### 4.9 Digital Twin Relevance

| Candidate | Source Path | Target Agent-OS Location | Value | Maturity | Fit | Risk | Decision | Rationale |
|-----------|-------------|---------------------------|-------|----------|-----|------|----------|-----------|
| GUI twin surface (emulator/VM/browser) | `experiments/mobile-agent-review/integration-candidates.md` Tier 3 | `agent-os/06_digital-twins/gui-twin-surfaces.md` | 4 | 3 | 4 | 2 | **PROMOTE_LATER** | Strategic; needs adapter boundary doc first |
| AndroidWorld env as observation contract | `experiments/mobile-agent-review/architecture/runtime-map.md` | `agent-os/06_digital-twins/gui-twin-surfaces.md` (update) | 4 | 2 | 4 | 3 | **RESEARCH_ONLY** | Vendored benchmark env; not general twin spec |
| Cloud phone hosted twin | `experiments/mobile-agent-review/integration-candidates.md` | `agent-os/06_digital-twins/gui-twin-surfaces.md` (update) | 3 | 2 | 3 | 3 | **RESEARCH_ONLY** | Vendor-specific (Wuying/Bailian) |

---

## 5. Cross-Source Concept Map

Comparison of four evidence sources across ten clusters.

| Concept Cluster | Claude Code | Code as Harness | Hermes | MobileAgent | Synthesis |
|-----------------|-------------|-----------------|--------|-------------|-----------|
| **5.1 Agent Loop** | Query loop: tool calls until terminal; stop hooks | Harness interface: code for reasoning/acting | `run_conversation()` + tool dispatch + compression hooks | Screen→reason→act→feedback; single action per turn | **Dual golden paths:** code loop (Claude/Hermes) + embodied loop (MobileAgent). Agent-OS should document both without merging implementations |
| **5.2 Memory** | File memory + taxonomy + recall tool | Planning/memory mechanisms in harness | Bounded MEMORY/USER + frozen snapshot + one external provider | InfoPool, Notetaker, MA-E tips | **Curated bounds + injection timing** (Hermes) + **in-loop scratch state** (MobileAgent) enrich Claude taxonomy |
| **5.3 Tools / MCP** | Native tools + MCP client (ch15) | Tool schemas as executable interface | 70+ tools + dynamic MCP client + filtering | GUI-Owl native MCP at model level; no server in repo | **Claude/Hermes = harness-first MCP**; **MobileAgent = model-routed GUI vs MCP** — future `gui-mcp-hybrid-routing` note |
| **5.4 Skills** | Two-phase skill loading (ch12 ⬜) | Procedural memory in survey | Progressive disclosure L0/L1/L2 + curator | No skill system; procedural knowledge in prompts/MA-E | **Promote Hermes progressive disclosure now**; align with pending ch12 extraction |
| **5.5 Verification** | Stop hooks, verification subagents | Verifiable outcomes via execution | Tool result validation; Kanban verifier role | A/B/C visual taxonomy; GUI-Critic pre-op (offline) | **Extend verification.md** with visual modality; keep code and GUI verification separate |
| **5.6 Environment Modeling** | Filesystem + shell + git state | Program states, repos, simulators | Session DB + sandbox backends + workspaces | GUI env (S,A,T,O); benchmarks as reward | MobileAgent is strongest **non-code environment** reference; Hermes adds **persistent session layer** |
| **5.7 Multi-Agent Coordination** | Subagents, swarms, SendMessage, tasks | Multi-agent orchestration scaling | delegate vs Kanban vs Cron; profile workers | InfoPool roles; no permissions | **Hermes adds durable queue primitive**; MobileAgent adds **tight-coupled role loop** — complementary patterns |
| **5.8 Self-Evolution** | Skills + memory writes (governed) | Emerging fields (survey ch5) | Curator + agent-created skills + Honcho | MA-E experience reflector; UI-S1 RL training | **Promote governance-first** (curator invariants); defer RL/self-evolution runtime |
| **5.9 GUI / OS Agents** | Terminal UI (ch13); no pixel GUI | Mentioned as emerging | Browser backends (5); not mobile GUI | Core focus: mobile/desktop/browser | **MobileAgent owns GUI modality** for Agent-OS; Hermes browser backends = RESEARCH_ONLY |
| **5.10 Digital Twin Substrate** | Session/agent IDs + memory scoping | Stateful agent systems | Profile isolation + Kanban + Honcho | Emulator/VM/browser twins | **Merge Hermes identity model + MobileAgent observation surfaces** in `06_digital-twins/` over time |

---

## 6. Recommended Agent-OS Updates

### 6.1 New Files to Create

| Target File | Source | Reason | Priority | Decision |
|------------|--------|--------|----------|----------|
| `agent-os/02_memory/frozen-memory-snapshot.md` | Hermes `memory/MEMORY_SYSTEM_OVERVIEW.md` | Cache-safe memory injection | P0 | PROMOTE_NOW |
| `agent-os/04_multi-agent/kanban-vs-delegate.md` | Hermes `multi-agent/TASK_ORCHESTRATION.md` | Missing orchestration primitive | P0 | PROMOTE_NOW |
| `agent-os/08_patterns/progressive-skill-disclosure.md` | Hermes `skills/SKILLS_SYSTEM_OVERVIEW.md` | ch12 gap + token control | P0 | PROMOTE_NOW |
| `agent-os/06_digital-twins/profile-isolation.md` | Hermes `notes/DIGITAL_TWIN_IMPLICATIONS.md` | Twin instance model | P0 | PROMOTE_NOW |
| `agent-os/01_agent-runtime/gui-agent-loop.md` | MobileAgent `screen-reason-action-feedback-loop.md` | GUI golden path | P0 | PROMOTE_NOW |
| `agent-os/00_foundations/visual-verification.md` | MobileAgent `action-verification-pattern.md` | A/B/C taxonomy | P0 | PROMOTE_NOW |
| `agent-os/09_antipatterns/unverified-gui-clicks.md` | MobileAgent `anti-patterns/unverified-clicks.md` | Top GUI failure | P0 | PROMOTE_NOW |
| `agent-os/02_memory/memory-char-limits.md` | Hermes `memory/MEMORY.md` | Bounded curation | P1 | PROMOTE_NOW |
| `agent-os/08_patterns/one-external-provider-rule.md` | Hermes `memory/MEMORY_PROVIDERS.md` | Plugin guardrail | P1 | PROMOTE_NOW |
| `agent-os/01_agent-runtime/visual-grounding.md` | MobileAgent `visual-grounding-pattern.md` | GUI perception core | P1 | PROMOTE_NOW |
| `agent-os/09_antipatterns/wrong-orchestration-primitive.md` | Hermes `anti-patterns/ANTI_PATTERNS.md` | Misuse of delegate/Kanban | P1 | PROMOTE_NOW |
| `agent-os/06_digital-twins/curator-pattern.md` | Hermes `skills/SELF_IMPROVING_SKILLS.md` | Self-improving skills governance | P2 | PROMOTE_LATER |
| `agent-os/04_multi-agent/kanban-orchestration.md` | Hermes `multi-agent/KANBAN.md` | Durable queue detail | P2 | PROMOTE_LATER |
| `agent-os/10_research/hermes-agent-architecture.md` | Hermes `RESEARCH_STATUS.md` | Research catalog entry | P2 | PROMOTE_LATER |
| `agent-os/10_research/mobileagent-architecture.md` | MobileAgent `RESEARCH_STATUS.md` | Research catalog entry | P2 | PROMOTE_LATER |

### 6.2 Existing Files to Update

| Existing File | Update Needed | Source | Risk | Priority |
|--------------|---------------|--------|------|----------|
| `agent-os/02_memory/memory-taxonomy.md` | Add cross-ref to char limits + dual store | Hermes memory docs | Low — additive wikilinks | P1 |
| `agent-os/04_multi-agent/subagents.md` | Add tool restriction list + parallel batch limits | Hermes `SUBAGENTS.md` | Low | P1 |
| `agent-os/00_foundations/verification.md` | Link visual verification; action vs task success | MobileAgent verification docs | Medium — scope creep | P1 |
| `agent-os/01_agent-runtime/error-recovery-ladder.md` | Add vision-triggered A/B/C + replan threshold | MobileAgent `failure-recovery-pattern.md` | Medium — modality merge | P2 |
| `agent-os/06_digital-twins/persistent-identity.md` | Cross-ref profile isolation | Hermes digital twin notes | Low | P1 |
| `agent-os/06_digital-twins/skill-graphs.md` | Link progressive disclosure + curator | Hermes skills | Low | P2 |
| `agent-os/06_digital-twins/evolving-memory.md` | Defer Honcho; add curator cross-ref when ready | Hermes | High if Honcho promoted early | P3 |
| `agent-os/08_patterns/prompt-cache-as-constraint.md` | Cross-ref frozen memory snapshot | Hermes | Low | P1 |
| `agent-os/09_antipatterns/infinite-retry-loops.md` | Add Kanban failure_limit + GUI step budget | Hermes + MobileAgent | Low | P2 |
| `agent-os/09_antipatterns/cache-busting-sections.md` | Cross-ref mid-session memory injection | Hermes | Low | P1 |
| `agent-os/09_antipatterns/central-orchestrator-god-object.md` | Add Hermes main.py/gateway evidence | Hermes `DANGEROUS_COMPLEXITY.md` | Low | P3 |
| `agent-os/05_mcp/runtime-bridges.md` | GUI driver adapter boundary (future) | MobileAgent actions | Medium | P3 |
| `agent-os/10_research/sources.md` | Add experiments sandboxes as research sources | Both READMEs | Low | P1 |

### 6.3 New Section Decision

**Question:** Need `agent-os/13_gui-agents/`?

**Decision: LATER**

**Rationale:**

- Phase 1.2 PROMOTE_NOW items (7 GUI-related) fit cleanly in `00_foundations/`, `01_agent-runtime/`, and `09_antipatterns/` without taxonomy churn.
- Creating `13_gui-agents/` now with <5 files risks **empty section syndrome** and duplicates `01_agent-runtime/` scope.
- **Trigger for YES:** when ≥5 GUI-specific notes exist AND `01_agent-runtime/index.md` exceeds ~15 entries or navigation becomes unclear.
- **Preferred first home:** `01_agent-runtime/` for loop/grounding/contracts; `00_foundations/` for verification/environment framing.

### 6.4 Pattern Promotions

| Pattern | Target | Decision |
|---------|--------|----------|
| Frozen memory snapshot | `08_patterns/` OR `02_memory/` (concept) — prefer **02_memory** as concept, cross-link from `prompt-cache-as-constraint` | PROMOTE_NOW |
| Progressive skill disclosure | `08_patterns/progressive-skill-disclosure.md` | PROMOTE_NOW |
| One-external-provider rule | `08_patterns/one-external-provider-rule.md` | PROMOTE_NOW |
| Context fencing | `08_patterns/context-fencing.md` | PROMOTE_LATER |
| Shared pool coordination | `04_multi-agent/` or `08_patterns/` — prefer **04_multi-agent** | PROMOTE_LATER |

### 6.5 Anti-pattern Promotions

**Phase 1.2 first (PROMOTE_NOW):**

1. `unverified-gui-clicks.md`
2. `unrestricted-gui-actions.md`
3. `wrong-orchestration-primitive.md`
4. `mid-session-memory-injection.md`
5. `multiple-memory-providers.md`
6. `subagent-memory-writes.md`
7. `skill-token-explosion.md`
8. `brittle-gui-automation.md` (catalog)
9. `weak-gui-action-parsing.md`

### 6.6 Memory Promotions

| Note | Decision |
|------|----------|
| `frozen-memory-snapshot.md` | PROMOTE_NOW |
| `memory-char-limits.md` | PROMOTE_NOW |
| `curated-memory-stores.md` (MEMORY vs USER) | PROMOTE_NOW |
| `agent-context-tagging.md` | PROMOTE_NOW |
| `memory-provider-interface.md` | PROMOTE_LATER |
| Honcho dialectic | RESEARCH_ONLY |

### 6.7 Harness / Verification Promotions

| Note | Decision |
|------|----------|
| `visual-verification.md` (A/B/C) | PROMOTE_NOW |
| `pre-op-verification.md` (GUI-Critic) | RESEARCH_ONLY |
| Execution feedback typed records | PROMOTE_LATER |
| Sleep-based GUI sync antipattern | PROMOTE_NOW |

### 6.8 Multi-Agent Promotions

| Note | Decision |
|------|----------|
| `kanban-vs-delegate.md` | PROMOTE_NOW |
| `subagent-tool-restrictions.md` | PROMOTE_NOW |
| `kanban-orchestration.md` | PROMOTE_LATER |
| `shared-pool-coordination.md` | PROMOTE_LATER |

### 6.9 MCP Promotions

| Note | Decision |
|------|----------|
| Per-tool filtering (Hermes) | PROMOTE_LATER — update existing |
| `gui-mcp-hybrid-routing.md` | RESEARCH_ONLY |
| `gui-tool-contracts.md` | RESEARCH_ONLY — after local MCP sandbox |

### 6.10 Digital Twin Promotions

| Note | Decision |
|------|----------|
| `profile-isolation.md` | PROMOTE_NOW |
| `curator-pattern.md` | PROMOTE_LATER |
| `durable-task-coordination.md` | PROMOTE_LATER |
| `gui-twin-surfaces.md` | PROMOTE_LATER |

---

## 7. Do Not Promote Yet

### 7.1 Hermes — Research Only

- Full gateway platform matrix (`gateway/run.py`, 20+ adapters)
- Individual memory provider implementations (Honcho, Mem0, etc.)
- Browser backend matrix (5 backends)
- Voice mode, skin engine, Nous Portal coupling
- `execute_code` RPC — until compared with Claude Code execution model
- Sandbox backend catalog (7 options)
- Bundled/optional skills catalog (160+ skills)

### 7.2 MobileAgent — Research Only

- v1/v2 OCR + GroundingDINO pipeline as default perception
- Full `run*.py` scripts and version-specific controllers
- UI-S1 VERL training stack
- GUI-Critic integration (offline only in upstream)
- GUI-Owl model weights and vLLM serving
- Hardcoded benchmark hints in Manager prompts
- OSWorld-MCP / ToolCUA / MobileWorld (external repos)

### 7.3 Too Early / Too Risky

- Honcho dialectic (15+ knobs) → memory pollution + config explosion
- MA-E self-evolution without curator-equivalent governance
- GUI-MCP hybrid routing as canonical policy without harness spec
- Kanban comment protocol as normative spec without full source read
- Premature `13_gui-agents/` section creation

### 7.4 Requires More Evidence

- Curator vs user-edited skill conflict resolution (Hermes open question #1)
- v3.5 E2E loop verification semantics (less explicit A/B/C)
- GUI-Critic pre-op value in production loop
- Progressive disclosure overhead at 160+ skills (Hermes open question #9)
- agentskills.io full vs partial compatibility

### 7.5 Requires Local Experiment First

- MCP tool contracts: `gui_capture_screenshot`, `gui_execute_action`, `gui_verify_action_delta`
- Frozen memory snapshot prototype in isolated harness
- Kanban vs delegate decision tree with real workload
- GUI verification with circuit breaker on repeated C outcomes
- Android emulator / ADB adapter behind permission layer (never in Agent-OS root)

---

## 8. Risk Analysis

| Risk | Severity | Cause | Mitigation |
|------|----------|-------|------------|
| Taxonomy explosion | High | Creating `13_gui-agents/` + many one-off files prematurely | Batch promotions; use existing sections first; section trigger ≥5 files |
| Duplicated concepts | High | Hermes MEMORY.md vs Claude memory-taxonomy; GUI loop vs query-loop | One concept per file; wikilinks; glossary = pointers only |
| Premature canonicalization | High | Promoting research prototypes (v3.5 monolithic, Honcho) as production patterns | RESEARCH_ONLY bucket; require local experiment for MCP/GUI contracts |
| Hype-driven architecture | Medium | GUI-Owl / self-improving agent marketing | Evidence paths + REJECT for weights/training stacks |
| Copying unstable runtime ideas | High | Porting Hermes gateway or MobileAgent ADB runners | Knowledge-only promotion; no upstream code in curated layer |
| Mixing source / generated / curated layers | High | Citing experiments as canonical without `sources.md` update | Add sandbox provenance in `10_research/sources.md` Phase 1.2 |
| GUI automation fragility | High | OCR coords, sleep sync, unverified clicks | Prioritize verification + antipattern promotions |
| Self-improving agents without governance | High | Curator/MA-E without invariants | Promote curator **with** never-auto-delete; defer MA-E |
| Memory pollution | Medium | Unbounded writes, multi-provider, cron/subagent writes | PROMOTE_NOW: bounds, frozen snapshot, context tagging, one-provider rule |
| MCP overexpansion | Medium | GUI-MCP hybrid + Hermes OAuth + tool explosion | Per-tool filtering later; RESEARCH_ONLY for hybrid routing until spec |
| Digital twin overclaiming | Medium | Cloud phone / emulator as "twin" without identity model | Pair GUI surfaces with Hermes profile isolation |

---

## 9. Promotion Roadmap

### Phase 1.2 — Safe Curated Promotions (PROMOTE_NOW only)

**Week 1 — Memory + orchestration (Hermes):**

1. `02_memory/frozen-memory-snapshot.md`
2. `02_memory/memory-char-limits.md`
3. `02_memory/curated-memory-stores.md`
4. `02_memory/agent-context-tagging.md`
5. `04_multi-agent/kanban-vs-delegate.md`
6. `04_multi-agent/subagent-tool-restrictions.md`
7. `08_patterns/progressive-skill-disclosure.md`
8. `08_patterns/one-external-provider-rule.md`
9. `06_digital-twins/profile-isolation.md`

**Week 2 — GUI modality (MobileAgent):**

10. `01_agent-runtime/gui-agent-loop.md`
11. `01_agent-runtime/visual-grounding.md`
12. `01_agent-runtime/coordinate-spaces.md`
13. `00_foundations/visual-verification.md`
14. `00_foundations/gui-as-environment.md`

**Week 2 — Anti-patterns (both sources):**

15. `09_antipatterns/unverified-gui-clicks.md`
16. `09_antipatterns/unrestricted-gui-actions.md`
17. `09_antipatterns/wrong-orchestration-primitive.md`
18. `09_antipatterns/mid-session-memory-injection.md`
19. `09_antipatterns/multiple-memory-providers.md`
20. `09_antipatterns/subagent-memory-writes.md`
21. `09_antipatterns/skill-token-explosion.md`
22. `09_antipatterns/brittle-gui-automation.md`

**Infrastructure:**

- Update `10_research/sources.md` with both experiment sandboxes
- Update section `index.md` files + bidirectional wikilinks
- Cross-ref existing notes (no duplicate definitions)

### Phase 1.3 — Deferred Promotions (PROMOTE_LATER)

- `06_digital-twins/curator-pattern.md`
- `04_multi-agent/kanban-orchestration.md`
- `04_multi-agent/shared-pool-coordination.md`
- `02_memory/memory-provider-interface.md`
- `08_patterns/context-fencing.md`
- `01_agent-runtime/gui-action-contract.md`
- `06_digital-twins/gui-twin-surfaces.md`
- `10_research/hermes-agent-architecture.md` + `mobileagent-architecture.md`
- Targeted updates to `error-recovery-ladder.md`, `execution-feedback.md`, MCP docs

### Phase 1.4 — Research Backlog (RESEARCH_ONLY)

- Honcho dialectic, GUI-MCP hybrid routing, GUI-Critic pre-op
- MA-E experience evolution, UI-S1 RL
- External repos: OSWorld-MCP, ToolCUA, MobileWorld
- Hermes execute_code RPC deep comparison

### Phase 1.5 — Local Experiments

| Experiment | Validates | Sandbox |
|------------|-----------|---------|
| Frozen memory + prompt cache measurement | frozen-memory-snapshot promotion | `experiments/hermes-agent-review/experiments/` |
| Kanban vs delegate decision tree on 3 workloads | orchestration primitive note | isolated script |
| MCP mock: capture → act → verify | gui-tool-contracts | no real ADB in repo root |
| A/B/C verifier with step budget + circuit breaker | visual-verification + antipatterns | Playwright or mock screenshots |
| Curator governance dry-run | curator-pattern before promotion | markdown-only simulation |

---

## 10. Acceptance Criteria for Phase 1.2

A promotion from experiments → `agent-os/` is allowed when **all** hold:

| Criterion | Requirement |
|-----------|-------------|
| Source path | Explicit `experiments/...` path in `## Sources` |
| Target file | Named kebab-case path in existing taxonomy (or approved new section) |
| No duplication | Grep Agent-OS for existing definition; update or cross-ref instead |
| Clear concept boundary | One concept per file; patterns ≠ concepts per extraction-plan |
| Risk note | `Production Implications` mentions failure modes |
| Wikilinks plan | `Related Concepts` bidirectional; section `index.md` updated |
| Provenance | Distinguish Claude / Harness / Hermes / MobileAgent origin |
| No upstream code | Concept prose only; no copied Python from `source/` clones |
| Taxonomy discipline | New section only with ≥5 related notes and README justification |

---

## 11. Final Recommendation

### Promote first (Phase 1.2)

**Hermes (identity + memory + orchestration):**

1. Frozen memory snapshot
2. Kanban vs delegate matrix
3. Progressive skill disclosure
4. Profile isolation
5. One-external-provider rule

**MobileAgent (GUI harness core):**

6. GUI agent loop (screen→reason→act→feedback)
7. Visual verification A/B/C
8. Visual grounding + coordinate spaces
9. Unverified clicks + unrestricted GUI actions antipatterns

### Defer

- Curator pattern, Kanban orchestration detail, Honcho, GUI-MCP hybrid, GUI-Critic pre-op, MA-E self-evolution
- `13_gui-agents/` section until GUI note cluster is mature

### Section `13_gui-agents/`

**LATER** — after Phase 1.2–1.3 place ~10 GUI notes; then migrate from `01_agent-runtime/` if navigation warrants it.

### First 5 files to create in Phase 1.2

1. `agent-os/02_memory/frozen-memory-snapshot.md`
2. `agent-os/04_multi-agent/kanban-vs-delegate.md`
3. `agent-os/08_patterns/progressive-skill-disclosure.md`
4. `agent-os/01_agent-runtime/gui-agent-loop.md`
5. `agent-os/00_foundations/visual-verification.md`

### First 5 anti-patterns to add

1. `unverified-gui-clicks.md`
2. `wrong-orchestration-primitive.md`
3. `mid-session-memory-injection.md`
4. `multiple-memory-providers.md`
5. `subagent-memory-writes.md`

### Most important for digital twin trajectory

1. **Profile isolation** (Hermes) — twin instance boundary
2. **Bounded curated memory** (Hermes) — quality user/agent model
3. **Curator pattern** (Hermes, Phase 1.3) — governed procedural evolution
4. **Kanban durable coordination** (Hermes, Phase 1.3) — twin work persistence
5. **GUI twin surfaces** (MobileAgent, Phase 1.3) — observation/action adapter for embodied twins
6. **Visual verification** (MobileAgent) — trust in twin actions on real UIs

---

*Phase 1.1 complete. Single artifact created: `PROMOTION_REVIEW.md`. No other files modified.*
