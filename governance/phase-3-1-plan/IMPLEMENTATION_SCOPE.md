# Implementation Scope — Phase 3.1 Thin Review Assistant

**Applies to:** future implementation only (not Phase 3.1-Plan)

---

## Allowed future behavior

| # | Behavior | Notes |
|---|----------|-------|
| A1 | Accept a text task | CLI arg or stdin |
| A2 | Produce a draft | Marked unverified |
| A3 | Run simple critique | Simulated or rule-based critic; **advisory** |
| A4 | Run verification checks | Format, non-empty, policy stubs |
| A5 | Require human approval | CLI prompt, explicit flag, or mock approval |
| A6 | Block delivery without approval | Fail-closed |
| A7 | Block on critic `uncertain` | Escalate or hold |
| A8 | Block bypass publish attempt | `unsafe_action_blocked` in trace |
| A9 | Emit human-readable trace | Text lines, canonical event names |
| A10 | Output approved result or fail reason | Terminal state clear |
| A11 | Scenario modes | e.g. `--scenario happy`, `uncertain-critic`, `bypass-attempt` aligned with prototype |

---

## Forbidden future behavior

| # | Behavior |
|---|----------|
| F1 | Auto-publish / auto-deliver without human approval |
| F2 | External API calls by default |
| F3 | Telegram send |
| F4 | FastAPI or HTTP service |
| F5 | Database read/write |
| F6 | Persistent memory / long-term profile |
| F7 | Second agent or multi-agent flow |
| F8 | External template import |
| F9 | Code generator (template → files) |
| F10 | Reusable runtime / agent engine / plugin system |
| F11 | Critic pass treated as final approval |
| F12 | Hidden memory writeback |
| F13 | Modification of `prototypes/`, `integrations-real/`, eval scripts, observability examples |

---

## Out of scope (Phase 3.1 entirely)

- Agent Factory / Builder Kit runtime
- Production deployment
- CV / digital twin / RAG / MCP / LangGraph
- Real LLM API (optional future phase with explicit approval)
- Dashboard / SaaS
- Shared `agent-runtime/` library extraction
- Changes to frozen Review Assistant v0.1 spec semantics

---

## Requires future approval (not Phase 3.1 default)

| Item | Approver |
|------|----------|
| New pip dependency | User + lead |
| Real LLM adapter | Separate phase proposal |
| Network call | Separate phase proposal |
| Move impl into `agent-builder-kit/implementations/` | Governance review |
| Persist audit to filesystem beyond stdout | User approval |
| Second scenario pack beyond frozen five | Template change proposal |

---

## Smallest safe scope (MVP for Phase 3.1 impl)

One folder, one entry script, ~same surface as `prototypes/review-loop-agent/minimal-demo.py`:

- 3–5 scenario flags
- Audit list printed to stdout
- Human approve via `--human approve|reject` or interactive prompt
- No shared imports from a new “framework” package

Align outputs to [BEHAVIOR_CONTRACT.md](BEHAVIOR_CONTRACT.md) and frozen [evaluation.md](../../agent-builder-kit/templates/review-assistant-agent/evaluation.md).

---

## Scope boundary diagram

See [diagrams/thin-implementation-boundary.md](diagrams/thin-implementation-boundary.md)
