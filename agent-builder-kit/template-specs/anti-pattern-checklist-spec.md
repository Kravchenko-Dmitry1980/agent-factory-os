# Anti-Pattern Checklist Spec

Before accepting any agent template, complete this scan.

---

## Pre-Acceptance Checklist

| # | Anti-pattern | Check |
|---|--------------|-------|
| 1 | LLM output treated as truth | Output marked unverified until gate passes |
| 2 | Critic treated as truth | Critic marked advisory; human final |
| 3 | Missing approval | Risky actions require `approval_requested` |
| 4 | Missing escalation | Ambiguity has escalation path |
| 5 | Missing evaluation | Scenarios defined with pass/fail |
| 6 | Missing audit | Trace covers full workflow |
| 7 | Unbounded memory | Caps and reset policy defined |
| 8 | Hidden autonomy | No silent publish or side effects |
| 9 | Unsafe tool use | Tool allowlist + approval rules |
| 10 | Platform drift | Template stays spec; no framework extraction |
| 11 | Framework extraction | Kit not promoted to runtime library |
| 12 | Template copied without provenance | Sources documented; no blind copy |
| 13 | External repo template dumping | External repos research-only (Phase 2.10) |

---

## Severity

| Level | Action |
|-------|--------|
| Blocker | Template cannot be accepted |
| Warning | Must document mitigation before accept |
| Info | Track in template backlog |

Items 1–9 are **blockers** for v0.1.

---

## Review Process

1. Author completes checklist in template `anti-patterns.md`
2. Reviewer independently verifies
3. Record in [evaluation-checklists/phase-3-template-review-checklist.md](../evaluation-checklists/phase-3-template-review-checklist.md)

---

## Repository Anti-Pattern Sources

- `agent-os/09_antipatterns/`
- `Books/swarm-playbooks/anti-patterns/`
- `observability/event-taxonomy/anti-pattern-events.md`
- `governance/phase-2-10/` (external repo risks)

---

## Related

- [templates/review-assistant-agent/anti-patterns.md](../templates/review-assistant-agent/anti-patterns.md)
- [governance/no-external-template-import-policy.md](../governance/no-external-template-import-policy.md)
