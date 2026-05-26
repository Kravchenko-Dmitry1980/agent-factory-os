# Option Comparison Matrix — Phase 3.2

| Criterion | Option A: LLM Adapter | Option B: Second Template | Better |
|-----------|----------------------|---------------------------|--------|
| **Safety** | Extends one known agent; mock-first; gates unchanged | New template surface; orchestration risk (Triage) | **A** |
| **Learning value** | Real boundary failures (parse, timeout, injection) | New workflow patterns; less LLM depth | **A** |
| **Reuse of Review Assistant** | Direct extension of frozen impl + spec | Parallel duplicate or new domain | **A** |
| **Risk of factory drift** | Low if single adapter file, no registry | High — two templates → shared engine pressure | **A** |
| **Risk of runtime drift** | Medium — adapter could become framework | High — triage → router runtime | **A** |
| **Evaluation clarity** | Extend thin check + LLM events | Full new scenario set + acceptance | **A** (incremental) |
| **Implementation complexity** | Medium — one boundary, mock first | Medium-high — full template + impl | **A** (smaller scope) |
| **Governance complexity** | Medium — security + provider approval | High — second freeze, second acceptance | **A** |
| **Future value** | Enables realistic Review Assistant | Expands kit catalog | Tie (sequential) |
| **Fit for Phase 3.2** | **Strong** — natural next layer | **Weak** — premature proliferation | **A** |

---

## Score summary

| Option | Wins | Notes |
|--------|------|-------|
| A — LLM Adapter | 9 / 10 | Tie on future value; A still first sequentially |
| B — Second Template | 0 / 10 | Better as Phase 3.3+ after A |

---

## Condition for A winning

Option A wins **only if**:

- Mock-first mandatory
- No external API by default
- No runtime/registry/router
- Frozen thin v0.1 preserved; adapter additive
- Human approval unchanged

If A were implemented as "LLM platform" or multi-provider framework → **NO-GO**.

---

## Decision

**Recommend Option A** for Phase 3.2 planning and conditional future implementation.

See [RECOMMENDED_NEXT_STEP.md](RECOMMENDED_NEXT_STEP.md)

---

## Diagram

[diagrams/option-comparison.md](diagrams/option-comparison.md)
