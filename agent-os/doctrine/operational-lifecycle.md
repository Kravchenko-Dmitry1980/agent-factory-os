# Operational Lifecycle

Canonical lifecycle **worldview** for Agent-OS — not a workflow engine, BPMN runtime, or orchestration implementation.

Synthesizes: Claude harness loop, verification cluster, multi-agent coordination, and operational references (swarm-playbooks cited by path only).

---

## Unified Lifecycle

```
goal → routing → planning → decomposition → execution → verification → critique → review → escalation → approval → writeback
```

Not every stage applies to every task modality. Single-agent code tasks may collapse critique/review; durable orchestration expands them.

---

## Stage Reference

| Stage | Purpose | Canonical anchors | Human | Governance | Verification mandatory? |
|-------|---------|-------------------|-------|------------|-------------------------|
| **Goal** | Define intent, success criteria, risk class | task framing; [[memory-aware-execution]] intake | Defines goal | Risk tier assignment | No |
| **Routing** | Choose path: single loop, delegate, durable queue | [[kanban-vs-delegate]]; [[durable-task-coordination]] | Optional override | Tool/policy routing | No |
| **Planning** | Decompose work; expose skills/tools tiers | [[planning]]; [[progressive-skill-disclosure]] | Large/complex plans | Permission scope set | No |
| **Decomposition** | Persist units of work with deps | [[task-state-machine]]; [[durable-task-coordination]] | Edit plan (ops ref) | Queue persistence rules | No |
| **Execution** | Run loop: model ↔ tools | [[query-loop]] ∥ [[gui-agent-loop]] | Answer blocking questions | [[permission-modes]]; [[subagent-tool-restrictions]] | Per action (modal) |
| **Verification** | Prove outcome before terminal | [[verification]]; [[visual-verification]]; [[execution-verification]]; [[fail-closed-agent-loop]] | High-risk domains | Verify gate enforced | **Yes** |
| **Critique** | Heuristic quality pass (optional) | — (LLM critic = operational only) | None | Bounded rounds; not truth | **No** — not verification |
| **Review** | Human accountability checkpoint | [[execution-verification]] UX adjacency | **Required** for release class | Review queue discipline | Human judgment |
| **Escalation** | Pause for missing input / risk | human-escalation-gate (research) | **Required** when triggered | Escalation policy | Depends on tier |
| **Approval** | Consent for external effect | [[permission-modes]]; fail-closed external tools | **Required** | External action policy | Implicit in gate |
| **Writeback** | Durable memory/skills update | [[verification-before-writeback]] | High-risk stores | Promotion to durable tier | **Yes** — pass gate |

---

## Where Humans Intervene

1. **Goal** — define success, fixtures, escalation thresholds
2. **Planning** — approve large/destructive plans (operational pattern; heuristic in swarm reference)
3. **Execution** — unblock `waiting_question` / permission prompts
4. **Review** — mandatory for external-facing artifacts
5. **Escalation** — medical, legal, HR-class domains (research: human-escalation-gate)
6. **Approval** — publish, send, pay, irreversible API mutations
7. **Writeback** — optional human gate for curated memory promotion

Humans are **decision authority** at approval/review/escalation — not optional spectators.

---

## Where Governance Intervenes

- **Routing** — which primitive (delegate vs durable queue)
- **Planning** — tool allowlists, subagent restrictions
- **Execution** — permission modes, fail-closed defaults
- **Verification** — required gates before terminal/writeback
- **Writeback** — char limits, taxonomy, profile isolation
- **Promotion** — research → curated (outside runtime lifecycle but shapes knowledge)

Prompt text is **not** governance. Policy lives in harness, permissions, and promotion pipeline.

---

## Where Verification Is Mandatory

| Transition | Gate |
|------------|------|
| Tool side effect (write assumed) | Permission + outcome check |
| Loop termination | Stop hooks / verification subagent / visual delta |
| GUI action | [[visual-verification]] A/B/C taxonomy |
| Durable writeback | [[verification-before-writeback]] |
| External approval | Human + prior verify stack |

**Critique stage never satisfies verification.**

---

## Where Anti-patterns Emerge

| Stage | Common failures |
|-------|-----------------|
| Goal | Vague scope → tutorial-driven architecture |
| Routing | Wrong primitive → blocking parent or lost work |
| Planning | Prompt chain fragility; god orchestrator |
| Execution | Unverified GUI clicks; infinite retry |
| Verification | Skipped for speed; critic as fake verify |
| Critique | Uncapped rework cost |
| Review | Automation without review |
| Writeback | Mid-session injection; unbounded growth |
| Autonomy | Recursive self-improvement |

See [anti-pattern-families.md](anti-pattern-families.md).

---

## Where Fail-closed Applies

- Parse/tool batch failure → serial safe path ([[fail-closed-defaults]])
- Verify fail / ambiguous terminal → loop continues or halts ([[fail-closed-agent-loop]])
- Writeback without verify → **reject**
- External tool without approval → **deny**
- Permission denial → non-success path

---

## Modality Notes

**Code path:** prepare → model → tools → append → verify → terminate check ([[query-loop]])

**GUI path:** observe → act → verify → reflect ([[gui-agent-loop]])

Same lifecycle worldview; different verify instrumentation.

---

## Operational Reference (non-canonical)

`Books/swarm-playbooks/lifecycle/orchestration-lifecycle.md` — useful UX ordering (plan approval, review page, critic rounds). Aligns with stages above; does **not** override harness verification doctrine.

---

## Sources

- `agent-os/00_foundations/golden-path.md`
- `agent-os/04_multi-agent/kanban-vs-delegate.md`
- `agent-os/08_patterns/verification-before-writeback.md`
- `governance/CONSOLIDATION_CANDIDATES.md` § Operational Lifecycle
- `Books/swarm-playbooks/lifecycle/orchestration-lifecycle.md` (reference)
