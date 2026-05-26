# Risk Review — Phase 3.1 Thin Review Assistant

**Review date:** 2026-05-26 (plan phase)

| Risk | Severity | Early signal | Mitigation |
|------|----------|--------------|------------|
| Thin implementation becomes runtime | **critical** | `shared/`, `engine/`, `runtime/` folders; multi-module abstractions | [NO_RUNTIME_DECISION.md](NO_RUNTIME_DECISION.md); Option B path; code review |
| Implementation modifies frozen specs | **critical** | git diff on `agent-builder-kit/templates/review-assistant-agent/` | CHANGE_LOCK; revert spec changes; fix impl only |
| Human approval skipped | **critical** | Happy path without `approval_requested` | [HUMAN_APPROVAL_PLAN.md](HUMAN_APPROVAL_PLAN.md); scenario tests |
| Critic treated as truth | **high** | Delivery on critic pass without human | Require `advisory=true`; human deny scenario |
| Trace missing or minimal | **high** | Output like "Done." only | [TRACE_PLAN.md](TRACE_PLAN.md); trace-review checklist |
| Evaluation skipped | **high** | No scenario runs documented | [EVALUATION_PLAN.md](EVALUATION_PLAN.md); POST_IMPLEMENTATION_CHECKLIST |
| Second agent added | **high** | New template folder or second entry script | Scope lock; FILE_BOUNDARY_PLAN |
| Shared abstractions grow | **high** | Imports from new `prototypes-derived/shared/` | Single-folder rule; reject PR |
| Prototype code modified | **critical** | git diff on `prototypes/` | Protected folder list; rollback |
| External templates imported | **high** | Upstream config files in impl | phase-2-10 policy; no import |
| Production adapter added | **high** | Telegram/FastAPI/network code | IMPLEMENTATION_SCOPE forbidden list |
| New dependencies silently | **medium** | `requirements.txt` diff | Pre/post checklist; user approval |
| kit becomes impl host | **medium** | Code under `agent-builder-kit/implementations/` without review | Recommend Option B |
| LLM API added "for realism" | **medium** | openai/httpx imports | Out of scope; separate phase |
| Platform drift from demo parity | **low** | Impl behaves unlike review-loop | Align to BEHAVIOR_CONTRACT + prototype contracts |

---

## Top 3 risks to watch during implementation

1. **Runtime extraction** — keep one script, no framework  
2. **Approval bypass** — every delivery path through human gate  
3. **Protected folder edits** — impl fixes only in new folder  

---

## Risk acceptance

Phase 3.1-Plan **accepts** residual risk that thin impl may need one retry if first attempt drifts — **mitigated by rollback plan**, not by expanding scope.

---

## Review cadence

| When | Action |
|------|--------|
| Before code | PRE_IMPLEMENTATION_CHECKLIST |
| After first runnable impl | POST_IMPLEMENTATION_CHECKLIST + trace compare |
| Before merge | Lead review + GO/NO-GO |
