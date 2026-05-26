# Option B — Second Template Review

**Status:** Review only — **no second template created**

---

## Why Option B was considered

After one frozen template + thin impl, a second text-only template could broaden the Builder Kit without LLM complexity.

---

## Candidate 1 — Task Triage Agent

**Purpose:** Classify/route incoming tasks (read-only routing proposal).

| Pros | Cons |
|------|------|
| Simple text I/O | Becomes **orchestrator** if routing executes actions |
| Useful for project work | Encourages multi-agent runtime early |
| No external publish by default | Hard to keep fail-closed without becoming "factory router" |

**Risk level:** Medium-high (runtime/orchestrator drift)

---

## Candidate 2 — Safe Content Draft Agent

**Purpose:** Another draft + review agent variant.

| Pros | Cons |
|------|------|
| Close to Review Assistant patterns | **Duplicates** Review Assistant |
| Easy evaluation reuse | May encourage auto-publish if differentiated wrong |
| Familiar gates | Dilutes focus on hardening first agent |

**Risk level:** Medium (duplication, not new learning)

---

## Candidate 3 — Meeting Summary Review Agent

**Purpose:** Summarize meetings for human review.

| Pros | Cons |
|------|------|
| Practical (neuro-secretary patterns) | Pulls **summarization pipeline** early |
| Human review fits template model | Domain scope creep (transcripts, PII) |
| Good curriculum story | Needs LLM anyway for real value |

**Risk level:** Medium-high (scope + LLM dependency without boundary first)

---

## Conclusion

Second template is **useful later** but **not the next safest step**.

| Reason | Explanation |
|--------|-------------|
| Surface area | New acceptance criteria, traces, anti-patterns, freeze cycle |
| Factory illusion | Two templates → pressure for shared runtime |
| Review Assistant incomplete | Simulated draft/critic; LLM boundary not proven |
| Governance load | Template review process still maturing on first agent |

**Postpone Option B** until:

- LLM boundary mock-first is safe (if Review Assistant needs LLM)
- User explicitly approves second template phase
- No runtime/factory drift observed

See [SECOND_TEMPLATE_RISK_REVIEW.md](SECOND_TEMPLATE_RISK_REVIEW.md)

---

## When Option B becomes viable

After Phase 3.2+ LLM boundary (or explicit decision to stay mock-only) + stable template lifecycle + user approval for "Phase 3.x — Second Template Spec".

Recommended first second template (future): **Task Triage Agent** as **spec-only** — not impl — if routing stays advisory-only.
