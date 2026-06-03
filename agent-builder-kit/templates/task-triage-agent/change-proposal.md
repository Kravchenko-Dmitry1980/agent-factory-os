# Task Triage Agent — Change Proposal

**Status:** SPEC_DRAFT

---

## Purpose

Define how future changes to Task Triage Agent template must be proposed, reviewed, and approved.

---

## Any future change requires

| Field | Description |
|-------|-------------|
| **Reason** | Why the change is needed |
| **Scope** | What is in / out of the change |
| **Affected docs** | List of template files to update |
| **Safety impact** | Effect on safety gates |
| **No-execution impact** | Effect on execution boundary |
| **No-orchestrator impact** | Effect on orchestrator boundary |
| **Evaluation impact** | New/changed eval cases |
| **Rollback plan** | How to revert if change fails |
| **Human approval** | Explicit approver before merge |

---

## Change proposal template

```markdown
# Change Proposal: [title]

**Date:**
**Proposer:**
**Template version:** v0.1-draft → v0.1.x

## Reason

## Scope

## Affected docs

## Safety impact

## No-execution impact

## No-orchestrator impact

## Evaluation impact

## Rollback plan

## Approval

| Reviewer | Date | Verdict |
|----------|------|---------|
```

---

## Forbidden changes without new phase

| Change | Required phase |
|--------|----------------|
| Adding code | Phase 3.6-Impl or later — explicit approval |
| Adding provider calls | Separate provider phase |
| Adding tools (MCP, shell, API) | Separate tools phase |
| Adding memory / persistence | Separate memory phase |
| Adding routing / delegation | **Forbidden** — violates no-orchestrator |
| Adding task queue | **Forbidden** — PM platform drift |
| Adding runtime/factory behavior | **Forbidden** — scope violation |
| Modifying frozen Review Assistant specs | Separate change proposal + governance |
| Modifying provider safety harness | Separate eval phase |

---

## Allowed changes in specs phase (before freeze)

- Clarify wording in template docs
- Add evaluation cases (synthetic)
- Fix inconsistencies between template files
- Update acceptance criteria evidence
- Navigation links in README files

All require governance review note — no silent edits to frozen artifacts.

---

## Freeze and version bumps

| Event | Action |
|-------|--------|
| Phase 3.5-Freeze | Lock v0.1 specs; sign-off bundle |
| Post-freeze doc fix | Patch version + change proposal |
| Contract enum change | Minor/major version + full review |
| Impl addition | New phase — do not fold into specs freeze |

See [sign-off/README.md](sign-off/README.md), [implementation-notes.md](implementation-notes.md).

---

## Governance review trigger

Stop immediately if a change proposal introduces:

- execute, run, deploy in core workflow
- route, delegate, dispatch, queue in core workflow
- provider-by-default
- memory writeback
- benchmark scoring platform

See [anti-patterns.md](anti-patterns.md).
