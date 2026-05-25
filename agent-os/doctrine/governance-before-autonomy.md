# Governance-before-autonomy Doctrine

Autonomy is **earned under governance**, not granted by prompt charisma.

---

## Core Thesis

Agents that gain tools, memory write access, multi-agent spawn capability, or external integrations without governance layers scale **risk faster than throughput**. Agent-OS treats governance as prerequisite infrastructure — promotion gates, permission modes, tool restrictions, approval boundaries — not as bureaucracy to skip in v1.

---

## Consolidated Governance Layers

### 1. Harness permissions

[[permission-modes]] — side-effect classes enforced before tool execution. **Not** prompt honor system.

### 2. Tool restrictions

[[subagent-tool-restrictions]] — blocklists and scoped toolsets prevent recursion, shared-store corruption, uncontrolled spawn.

### 3. Promotion gates

[governance/PROMOTION_STRATEGY.md](../../governance/PROMOTION_STRATEGY.md) — research → curated pipeline; no stage skip; scored decisions logged.

### 4. Human escalation

High-risk outcomes route to human decision (research: human-escalation-gate; operational: review/approval queues in swarm reference).

### 5. Review queues

Human batch checkpoint before release-class outcomes — distinct from automated critique (operational alignment: `Books/swarm-playbooks/patterns/review-gate.md`).

### 6. Safe autonomy levels

Progressive expansion (operational reference: safe-autonomy):

| Level | Posture |
|-------|---------|
| L0 | Human all external actions |
| L1 | Agent drafts; human approves visible output |
| L2 | Multi-agent internal; human review queue |
| L3+ | Closed loops only with approval gates wired |

Canonical anchor: [[progressive-skill-disclosure]] — tiered capability exposure, not day-one full autonomy.

### 7. Fail-closed defaults

[[fail-closed-defaults]] — unsafe paths opt-in; governance at tool registration time.

---

## Explicitly Rejected

### Unrestricted autonomy

- All tools to all agents by default
- Publish/send without approval event
- Solo task modes bypassing review policy

Maps to operational anti-patterns: unbounded-agent-autonomy, automation-without-review.

### Recursive self-improvement

[[recursive-self-improvement]] — ungoverned spawn/rewrite of skills, memory, policy without depth limits, rollback, or verification.

**Never promote** as architecture goal.

### Prompt-only governance

Policies embedded only in system prompts:

- no audit trail
- no fail-closed enforcement
- bypass via tool calls or subagent paths

Governance lives in **harness + promotion pipeline + permission layer**.

---

## Approval Gates

External-effect class actions require explicit human approval **after** verification stack:

- publish / send / pay / irreversible API mutation
- align with [[fail-closed-agent-loop]] and [[verification-before-writeback]]

Operational pattern reference: approval-before-external-action (swarm-playbooks — not curated).

---

## Governance vs Operations

| Layer | Location | Role |
|-------|----------|------|
| Canonical governance | agent-os curated + governance/ | Principles, patterns, promotion |
| Operational playbooks | Books/swarm-playbooks/ | UX patterns, HITL flows — **non-canonical** |
| Research | brain-os, experiments | Ideas — score before promote |

Phase 1.4 doctrine cites operations; does **not** promote them.

---

## Sources

- `agent-os/09_antipatterns/recursive-self-improvement.md`
- `agent-os/03_harness-engineering/permission-modes.md`
- `agent-os/04_multi-agent/subagent-tool-restrictions.md`
- `governance/PROMOTION_STRATEGY.md`
- `Books/swarm-playbooks/hitl/`
- `governance/CONSOLIDATION_CANDIDATES.md`

See also: [diagrams/governance-before-autonomy.md](diagrams/governance-before-autonomy.md)
