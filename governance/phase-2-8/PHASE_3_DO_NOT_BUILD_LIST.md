# Phase 3.0 — Do Not Build List

Strict list. Violation = **NO-GO** per [PHASE_3_GO_NO_GO.md](PHASE_3_GO_NO_GO.md).

| Do not build | Why tempting | Why dangerous | When maybe allowed |
|--------------|--------------|---------------|-------------------|
| Agent swarm | «Multi-agent is modern» | Scales errors; hides gates | After single template + factory discipline |
| Autonomous multi-agent platform | Product vision | Removes human loop | Post–Builder Kit v1+ with ops model |
| Digital twin builder | Cool narrative | Needs identity, replay, long eval | Phase 5+ per DIGITAL_TWIN_DEFER |
| CV agent builder | CV market | Evidence/verify/human review hard | Phase 4+ with evidence contracts |
| RAG platform | «Agents need memory» | Replaces verify; drift | User-approved RAG phase only |
| MCP runtime | Cursor ecosystem | Tool sprawl, auth complexity | Dedicated MCP phase |
| LangGraph / workflow engine | Faster coding | Framework drift | Never as default; optional experiment outside kit |
| Workflow engine (generic) | Orchestration hype | Hides gate visibility | Queue demo patterns as docs only |
| Prompt marketplace | Monetization | No governance on prompts | Not planned in repo mission |
| Web dashboard | Visibility | Productization | Observability stays text traces |
| Production API backend | «Ship it» | Security, compliance | External product decision |
| SaaS product | Business | Conflicts with learning lab | Out of repo |
| Model evaluation platform | ML team ask | Benchmark drift | evaluation/ stays local behavioral |
| Auto-curator | Scale knowledge | Promotion without review | agent-os promotion pipeline only |
| Self-improving agent | AGI narrative | Uncontrolled drift | Forbidden until research phase |
| Memory synthesis engine | «Smarter agents» | Unbounded memory | bounded-memory doctrine |
| YOLO / medical CV agent | Domain demand | Harm risk | CV_AGENT_FUTURE requirements first |
| Production Telegram bot | Real users | Operational risk | integrations-real mock only in 3.0 |
| Production FastAPI service | API product | Same | Adapter demo only |
| Video tracking factory | CV extension | Data + eval complexity | Far future |
| Code generator (default) | Speed | Bypasses proposal/smoke | Per-artifact user approval |
| `shared/` runtime package | DRY | Platform drift | Never as mandatory import |

---

## Allowed mentions in Phase 3 docs

- Future direction paragraphs
- Requirement lists (CV, twin) **without implementation**
- Links to existing demos as **references**

---

## Enforcement

Phase 3 PRs / doc reviews check this list + [PHASE_3_MINIMAL_SCOPE.md](PHASE_3_MINIMAL_SCOPE.md).
