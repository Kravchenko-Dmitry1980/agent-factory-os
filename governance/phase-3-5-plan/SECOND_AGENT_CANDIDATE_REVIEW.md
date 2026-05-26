# Second Agent Candidate Review — Phase 3.5

**Date:** 2026-05-26  
**Purpose:** Compare candidates for the second text agent template.

---

## Comparison summary

| Candidate | Value | Risk | Complexity | Reuse of Review Assistant pattern | Recommendation |
|-----------|-------|------|------------|-----------------------------------|----------------|
| **A — Task Triage Agent** | High — classifies work before execution | **High** — orchestrator/PM drift | Medium | High — gates, trace, HITL | **Recommended** (with strict boundaries) |
| B — Safe Content Draft Agent | Medium — simple drafts | Low–Medium — duplicates Review Assistant | Low | Very high — near duplicate | **Reject** as second template |
| C — Meeting Summary Review Agent | Medium — neuro-secretary relevance | Medium — domain pipeline early | Medium–High | Medium | **Defer** — product-specific |
| D — Research Note Agent | Medium — repo/Books triage | Medium — RAG/graph pull | Medium | Medium | **Defer** — knowledge layer early |

---

## Candidate A — Task Triage Agent

### Purpose

Classify an incoming task and suggest a safe next step. Advisory only.

### Pros

- High utility in real AI/Cursor project workflows
- Text-only — no external actions required by default
- Complements Review Assistant (before vs during review)
- Helps project leadership prioritize without executing
- Evaluable with synthetic task descriptions
- Fits governance-heavy repo culture

### Risks

| Risk | Drift form |
|------|------------|
| Orchestrator illusion | "Triage then auto-start Review Assistant" |
| Task manager | Tickets, backlog, assignments |
| Multi-agent router | Route to agent X/Y/Z |
| Early execution | "I'll implement this now" |
| PM platform | Sprint boards, scheduling, delegation |

**Mitigation:** [TASK_TRIAGE_AGENT_NO_ORCHESTRATOR_POLICY.md](TASK_TRIAGE_AGENT_NO_ORCHESTRATOR_POLICY.md), [TASK_TRIAGE_AGENT_NO_EXECUTION_POLICY.md](TASK_TRIAGE_AGENT_NO_EXECUTION_POLICY.md)

---

## Candidate B — Safe Content Draft Agent

### Purpose

Create safe text drafts (similar to Review Assistant).

### Pros

- Simple mental model
- Close to existing template
- Easy evaluation overlap

### Cons

- **Duplicates Review Assistant** domain
- Blurs "second template" learning value
- Lower differentiation for Agent Builder Kit
- Encourages template sprawl without new capability

**Verdict:** Reject as second template. Extend Review Assistant if draft variants needed.

---

## Candidate C — Meeting Summary Review Agent

### Purpose

Review meeting summaries for quality and safety before use.

### Pros

- Relevant to neuro-secretary / meeting products
- Practical in meeting-heavy workflows

### Cons

- Pulls **domain pipeline** too early (transcripts, summarization contracts)
- Product-specific before second generic template exists
- May expand toward Hermes/neuro-secretary integration prematurely

**Verdict:** Defer to Phase 4+ or product-specific track.

---

## Candidate D — Research Note Agent

### Purpose

Turn research notes into structured summaries.

### Pros

- Useful for repo triage and Books folder
- Text-only

### Cons

- May pull **RAG / knowledge graph** too early
- Duplicates existing research/triage processes in governance
- Overlaps with manual review and curriculum work

**Verdict:** Defer until knowledge layer is explicitly planned.

---

## Decision matrix (weighted)

| Criterion | Weight | A Triage | B Draft | C Meeting | D Research |
|-----------|--------|----------|---------|-----------|------------|
| Utility | 25% | 9 | 5 | 7 | 6 |
| Safety / low drift | 30% | 6* | 8 | 6 | 5 |
| Text-only default | 15% | 10 | 10 | 9 | 10 |
| Complements Review Assistant | 15% | 10 | 3 | 7 | 6 |
| Evaluability (synthetic) | 15% | 9 | 7 | 6 | 7 |
| **Weighted score** | | **8.0** | 6.1 | 6.7 | 6.4 |

\* Score assumes no-orchestrator and no-execution policies enforced. Without policies, A drops to ~3.

---

## Recommendation

**Task Triage Agent wins** as second template candidate — **plan only**, with strict no-orchestrator and no-execution boundaries.

See [RECOMMENDED_AGENT_DECISION.md](RECOMMENDED_AGENT_DECISION.md).
