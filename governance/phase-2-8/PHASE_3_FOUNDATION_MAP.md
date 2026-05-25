# Phase 3 — Foundation Map

**Rule:** migrate **patterns, specs, checklists** — not prototype Python code wholesale.

| Phase 3 need | Existing foundation | Gap | Use in Phase 3 |
|--------------|---------------------|-----|----------------|
| Template safety | fail-closed-external-action, doctrine fail-closed | Unified spec format | Safety gate template |
| Agent workflow | review-loop-agent, query-loop.md | Kit folder structure | Review Assistant template |
| Review loop | review-loop + review-queue-workflow | Multi-workflow doc | Primary v0.1 pattern |
| Memory boundary | bounded-memory-agent, doctrine | Per-template limits | Memory boundary template |
| Evaluation | evaluation/scripts, quality-gates | Template-specific expected strings | Acceptance checklist |
| Observability | observability/examples, canonical-events | Auto trace generation | Trace template |
| Rollback | evolution/rollback-thinking, operator rollback runbook | Automated rollback | Change + rollback section in kit |
| Human approval | fail-closed, telegram-review-gate docs | Production Telegram | Approval policy template |
| Safe change | evolution/change-proposals/change-template.md | CI gate | Link in kit |
| Operator onboarding | operator-playbooks/start-here | RU playbooks | Builder user guide (EN first) |
| Russian training | curriculum/ru/ full mirror | EN playbook body | Primary path for RU interns |
| Anti-pattern detection | agent-os/09_antipatterns, curriculum lessons | Automated lint | Anti-pattern checklist in kit |
| Escalation | escalation-workflow, observability escalation-trace | Template for triage agent (v0.2) | Reference only in v0.1 |
| GUI safety | gui-verification-loop | Real GUI automation | Defer from first template |
| Real LLM boundary | llm-verification-adapter | Production API keys policy | Mention in verify section |
| Promotion discipline | promotion-pipeline-simulator | Real git promotion | Advanced template later |
| Audit lineage | filesystem-audit-log, audit.py | Central audit service | Trace + audit template |
| Drift prevention | evolution/drift-detection | Metrics dashboard | Early warning checklist |

---

## Critical path for v0.1

```
review-loop-agent (pattern)
  → Review Assistant Agent Template (spec)
    → evaluation checklist (acceptance)
      → observability trace template (proof)
        → change proposal (evolution)
```

No code copy — document the **gates and events** each step must emit.
