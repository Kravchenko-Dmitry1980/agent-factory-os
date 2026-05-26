# Agent Template Spec

Every future agent template **must** include all sections below.

---

## Agent Name

Unique, descriptive identifier (e.g. `review-assistant-agent`).

---

## Purpose

One paragraph: what the agent helps with and what it explicitly does **not** do.

---

## User Problem

The human problem this agent addresses. Must be concrete, not aspirational.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Task description | yes | What the user wants |
| Context documents | optional | Bounded scope only |
| Constraints | optional | Style, length, audience |

---

## Outputs

| Output | Risk level | Approval required |
|--------|------------|-------------------|
| Draft / proposal | medium | yes before delivery |
| Final published artifact | high | yes, explicit human gate |

---

## Tools

List allowed tools with boundaries. Reference [tool-boundary-spec.md](tool-boundary-spec.md).

- No unrestricted shell
- No unrestricted filesystem
- No external API write without approval

---

## Memory

Reference [memory-boundary-spec.md](memory-boundary-spec.md).

- Task context only by default
- No automatic long-term profile mutation
- Writeback requires explicit approval

---

## Workflow

Reference [workflow-template-spec.md](workflow-template-spec.md).

Standard: input → validation → planning → draft → verification → (optional critique) → human review → approval/rejection → output → audit trace.

---

## Safety Gates

Minimum required gates (see [safety-gates/](../safety-gates/README.md)):

- fail-closed
- verification
- human approval
- tool-use (if tools present)
- memory-boundary (if memory present)
- escalation
- evaluation
- rollback (for changes)

---

## Human Approval

Reference [human-approval-spec.md](human-approval-spec.md).

- Deny-by-default for risky outputs
- No approval = no risky action

---

## Evaluation

Reference [evaluation-checklist-spec.md](evaluation-checklist-spec.md) and `evaluation/scenarios/`.

Must define: happy path, fail path, missing approval, verification failure, escalation, unsafe action block.

---

## Observability

Reference [observability-trace-spec.md](observability-trace-spec.md) and `observability/event-taxonomy/canonical-events.md`.

Text-first traces. No telemetry platform required in template spec.

---

## Failure Modes

Document known failures: hallucination, weak critique, missing approval, silent publish, unbounded loops, hidden memory writeback.

---

## Anti-patterns

Reference [anti-pattern-checklist-spec.md](anti-pattern-checklist-spec.md).

Template must list agent-specific anti-patterns to block.

---

## Change Policy

Reference [change-proposal-spec.md](change-proposal-spec.md) and `evolution/change-proposals/`.

Any template change goes through proposal → review → evaluation.

---

## Acceptance Criteria

Checklist for template acceptance. See [evaluation-checklists/template-acceptance-checklist.md](../evaluation-checklists/template-acceptance-checklist.md).

---

## Forbidden Behavior

Explicit list, e.g.:

- auto-publish without human approval
- treat LLM output as verified truth
- treat critic as final judge
- bypass safety gates
- unbounded memory growth
- hidden autonomy

---

## Related Prototypes

Link to repository prototypes that inspired the template (reference only, no code copy).

Example: `prototypes/review-loop-agent/`

---

## Governance References

- [governance/PHASE_3_START_CONDITIONS.md](../../governance/PHASE_3_START_CONDITIONS.md)
- [governance/phase-2-8/PHASE_3_MINIMAL_SCOPE.md](../../governance/phase-2-8/PHASE_3_MINIMAL_SCOPE.md)
- [agent-builder-kit/governance/phase-3-0-scope-lock.md](../governance/phase-3-0-scope-lock.md)

---

## Acceptance Rule

**No agent template is accepted without:**

- [ ] safety gates defined
- [ ] evaluation checklist defined
- [ ] failure modes documented
- [ ] human approval policy defined
- [ ] trace template defined
- [ ] anti-pattern checklist completed
