# Reusable Patterns

Extracted from Hermes Agent for potential Agent-OS integration.

---

## Memory Patterns

### 1. Frozen Memory Snapshot
Inject memory into system prompt once at session start. Mid-session writes persist to disk but don't update prompt. Preserves LLM prefix cache.

**Apply to:** Any agent with prompt caching.

### 2. Bounded Curated Memory
Hard char limits (2200/1375) force curation. § delimiter for structured entries. Substring matching for replace/remove.

**Apply to:** Prevent unbounded memory growth.

### 3. One-External-Provider Rule
Only one external memory provider active. Built-in always runs. Prevents tool schema bloat and conflicting backends.

**Apply to:** Plugin architectures with memory providers.

### 4. Agent Context Tagging
Tag agent context as primary/subagent/cron/flush. Providers skip writes for non-primary contexts.

**Apply to:** Prevent cron/subagent memory corruption.

### 5. Context Fencing
Wrap provider output in `<memory-context>` tags. Scrub before UI display. Streaming scrubber for chunk boundaries.

**Apply to:** Prevent memory injection appearing as user content.

---

## Skill Patterns

### 6. Progressive Disclosure
Three-level loading: list (~3k tokens) → full content → reference file. Load only when needed.

**Apply to:** Large skill libraries.

### 7. Curator Lifecycle
Inactivity-triggered auxiliary agent reviews agent-created skills. Pin/archive/consolidate. Never auto-delete.

**Apply to:** Self-improving procedural memory.

### 8. Platform-Restricted Skills
`platforms: [macos, linux]` in skill metadata. Hidden on incompatible platforms.

**Apply to:** Environment-aware skill loading.

---

## Multi-Agent Patterns

### 9. Kanban vs Delegate Matrix
Two distinct primitives: RPC fork-join (delegate) vs durable queue (Kanban). Decision matrix for when to use each.

**Apply to:** Multi-agent architecture design.

### 10. Subagent Tool Restrictions
Block recursive delegate, memory writes, clarify, send_message in subagents. Summary-only return.

**Apply to:** Subagent safety boundaries.

### 11. Profile Isolation
Each profile = separate HERMES_HOME with own config, memory, sessions, skills. Command alias auto-created.

**Apply to:** Digital twin instances.

---

## Runtime Patterns

### 12. Prefetch-Before-Turn
Background memory recall before each turn. Non-blocking. Injected as fenced context.

**Apply to:** Proactive memory systems.

### 13. on_pre_compress Hook
Extract memories before context compression. Preserve knowledge that would be lost in summarization.

**Apply to:** Memory-aware compression.

### 14. execute_code RPC
Python scripts call agent tools via RPC. Collapse multi-step pipelines into single turn.

**Apply to:** Reasoning compression.

### 15. Serverless Hibernate
Modal/Daytona backends hibernate when idle. Wake on demand. Minimal cost between sessions.

**Apply to:** Cloud agent deployment.

---

## Prompt Patterns

### 16. SOUL.md Personality
Separate personality file injected into system prompt. User-editable agent character.

**Apply to:** Agent personalization.

### 17. Context Files (AGENTS.md)
Project-specific context files auto-loaded. `.hermes.md` for Hermes-specific project config.

**Apply to:** Project-aware agents.

---

## Priority for Agent-OS

| Priority | Pattern |
|----------|---------|
| High | Frozen memory snapshot, Kanban vs delegate, Progressive disclosure |
| Medium | Curator lifecycle, One-provider rule, Profile isolation |
| Low | Serverless hibernate, Platform-restricted skills |
