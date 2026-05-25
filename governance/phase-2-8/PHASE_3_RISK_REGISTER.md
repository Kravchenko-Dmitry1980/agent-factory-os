# Phase 3 — Risk Register

| Risk | Severity | Why dangerous | Early signal | Mitigation |
|------|----------|---------------|--------------|------------|
| Agent factory scope explosion | **Critical** | Weakens all gates; hype to stakeholders | «Builder» → «Factory» in slides | MINIMAL_SCOPE + DO_NOT_BUILD |
| Template becomes framework | **Critical** | Hides gates; shared runtime | `kit/shared/`, LangGraph mention | FREEZE shared extraction |
| Demo becomes product | **High** | Skips evaluation; production claims | «MVP ready» language | AGENT_FACTORY_VS_LEARNING_LAB |
| `prototypes/shared/` → runtime | **High** | One import path for all agents | Central gates.py package | Keep shared labeled not-a-framework |
| Digital twin hype | **High** | Identity/replay complexity early | Twin template in 3.0 backlog | DIGITAL_TWIN_DEFER |
| CV-agent complexity jump | **High** | False confidence from vision models | YOLO template first | CV_AGENT_FUTURE |
| RAG premature | **High** | Memory substitute for verify | Vector DB tickets | FREEZE RAG |
| MCP runtime premature | **High** | Tool sprawl without governance | MCP server in Phase 3 | FREEZE MCP |
| Evaluation skipped | **High** | Regressions invisible | No smoke before «done» | Template acceptance checklist |
| Human approval removed | **Critical** | Unsafe autonomy | Auto-approve timeout | Template mandatory HITL section |
| Critic treated as truth | **High** | Silent wrong publish | PASS → ship | Lesson + trace in template |
| LLM output treated as truth | **High** | Hallucination in production narrative | JSON → API | Verification template section |
| Russian curriculum unused | **Medium** | Team skips safety pedagogy | Interns read only code | RU track + mentor |
| Operator playbooks ignored | **Medium** | Improvised unsafe ops | No runbook citations | Onboarding workshop |
| Platform drift | **High** | Unified demo runtime | shared/gates for all | evolution unsafe-shared-runtime |
| Productization too early | **High** | SaaS before discipline | Dashboard requests | DO_NOT_BUILD |
| Governance index stale | **Low** | Wrong entry points | Old Phase 1.4 only in README | Link phase-2-8 |
| Assessment sign-off missing | **Medium** | False GO | Phase 3 code without H1–H5 | CONDITIONAL GO human gates |

---

## Top 5 watch metrics

1. Smoke PASS count before any template marked «accepted»
2. Count of new `.py` files outside approved paths
3. Occurrences of «factory» / «platform» / «production» in Phase 3 docs
4. Mentor sign-off file present (yes/no)
5. New dependencies in repo (should stay zero for v0.1 specs)
