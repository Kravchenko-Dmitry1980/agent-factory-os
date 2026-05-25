# Experimental Ideas

Higher-risk or research-oriented ideas from Hermes worth tracking.

---

## 1. Trajectory Compression for Training

**Code:** `trajectory_compressor.py`, `batch_runner.py`

Generate agent trajectories, compress for training next-gen tool-calling models.

**Status:** Research feature, not production pattern.

**Potential:** Feedback loop — agent improves models that improve agent.

---

## 2. Mixture of Agents

**Code:** `tools/mixture_of_agents_tool.py`

Parallel calls to different LLMs on same question. Aggregator synthesizes.

**Status:** Experimental multi-LLM pattern.

**Potential:** Quality improvement via model diversity.

---

## 3. execute_code RPC Collapsing

**Code:** `tools/code_execution_tool.py`

Python script calls agent tools via RPC. Multi-step pipeline in single turn.

**Status:** Production feature, underdocumented pattern.

**Potential:** Reasoning compression — zero context cost for intermediates.

---

## 4. Honcho Dialectic Depth

**Config:** dialecticDepth 1-3, dialecticDepthLevels

Multi-pass LLM reasoning for user modeling:
- Pass 0: cold/warm prompt
- Pass 1: self-audit
- Pass 2: reconciliation

**Status:** Complex, cost-sensitive.

**Potential:** Deep user modeling for digital twins.

---

## 5. Cross-Session Mirroring

**Code:** `gateway/mirror.py`

Relay messages between sessions/platforms.

**Status:** Gateway feature.

**Potential:** Unified agent presence across platforms.

---

## 6. Skin Engine

**Code:** `hermes_cli/skin_engine.py`

CLI theming as personality extension.

**Status:** UI feature.

**Potential:** Visual identity for digital twins.

---

## 7. Gateway Hook System

**Code:** `gateway/hooks.py`, `gateway/builtin_hooks/`

Lifecycle events for gateway message processing.

**Status:** Extension point (no shipped hooks).

**Potential:** Custom gateway behavior without forking.

---

## 8. Context Engine Plugins

**Code:** `plugins/context_engine/`, `agent/context_engine.py`

Pluggable context management beyond default compressor.

**Status:** Plugin infrastructure exists.

**Potential:** Custom compression strategies.

---

## 9. ACP IDE Integration

**Code:** `acp_adapter/`

Agent Client Protocol for VS Code, Zed, JetBrains.

**Status:** Production feature.

**Potential:** IDE-as-entry-point pattern.

---

## 10. Voice Mode

**Docs:** `website/docs/user-guide/features/voice-mode.md`

Speech-to-text input, text-to-speech output.

**Status:** Feature with platform dependencies.

**Potential:** Multimodal agent interface.

---

## Evaluation Criteria

Before promoting to reusable pattern:

1. Is it architecture or feature?
2. Is it documented or inferred from code?
3. Does it generalize beyond Hermes?
4. What's the complexity cost?
5. Is there a simpler alternative?

---

## Recommended Experiments (in `experiments/` subfolder)

If user requests isolated experiments:

1. **MEMORY.md format prototype** — test char limits + § delimiter
2. **Progressive disclosure mock** — 3-level skill loading simulation
3. **Kanban decision tree** — interactive primitive selection
4. **Frozen snapshot benchmark** — measure cache impact

None of these require Hermes installation.
