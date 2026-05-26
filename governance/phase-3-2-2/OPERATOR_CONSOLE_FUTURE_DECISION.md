# Operator Console Future Decision

**Phase:** 3.2.2  
**Date:** 2026-05-26

---

## Do we need Operator Console later?

# Yes, later.

Non-technical operators need visible approvals, traces, eval status, and freeze records. Markdown/repo navigation is insufficient at scale.

Hermes Desktop confirms demand — but implements wrong priority order (autonomy features before governance).

---

## When?

After ALL of:

1. Real provider boundary safely handled (post-Phase 3.3 impl + freeze)
2. At least **2–3 agent templates** with eval baselines
3. Evaluation dashboard need is real (manual script fatigue)
4. Approval queue need is real (not scenario flags only)
5. Provider governance documented (secrets, failure modes, rollback)

**Target:** Phase 4+ for plan/MVP; not before v0.2 + real provider path matures.

---

## What would it show?

| Surface | Purpose |
|---------|---------|
| Templates | Frozen spec status, version |
| Implementations | Derived impls (e.g. review-assistant-thin) |
| Approvals | Pending queue; grant/deny audit |
| Traces | Event timeline vs scenario baseline |
| Evaluation status | Last PASS/FAIL per check script |
| Freeze status | Active version, change lock |
| Provider boundary | Approved provider, mock vs real, warnings |
| Memory/tool/skill boundaries | Read-only limits |
| Governance | Phase verdicts, links |
| Research backlog | Triage summaries (incl. Hermes) |

---

## What is forbidden now?

| Forbidden | Reason |
|-----------|--------|
| Implementation | Phase 3 scope |
| UI framework choice (React/Electron) | Premature |
| Electron / Tauri | Security/complexity |
| Provider UI | Tempts framework |
| Gateway UI | Autonomy risk |
| Schedules UI | Unattended actions |
| Skill installer UI | Supply chain |
| Chat-first home | Wrong product shape |

---

## Hermes contrast

| Hermes Desktop | Agent-OS future console |
|----------------|-------------------------|
| Chat-first | Governance-first |
| 16 gateways | None |
| Skill install | Skill review (maybe) |
| SOUL persona | Template spec only |
| Multi-provider | Single approved provider initially |

---

## Decision record

**APPROVED:** Add Operator Console to future backlog.  
**REJECTED:** Start console in Phase 3.3 or adopt Hermes Desktop.
