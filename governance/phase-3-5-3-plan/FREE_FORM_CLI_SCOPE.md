# Free-Form CLI — Scope

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

---

## In scope (future implementation)

| Capability | Notes |
|------------|-------|
| Text input from operator | Single task per run |
| Input validation | Empty rejected; secret-like warned/blocked |
| No-network default mode | Mode 1: safe mock/default |
| Optional local provider | Mode 2: explicit only + confirmation |
| Draft/review flow | Review Assistant-like gates |
| Verification gate | Visible pass/fail |
| Approval gate | Simulated prompt; default no |
| Unsafe output gate | Block delivery even if approved |
| Russian summary | Operator-facing |
| TRACE explanation | Human-readable, no backend |
| Safety status | OK / BLOCKED / ESCALATED / FAILED / WARNING |
| Optional transcript | `--save-transcript` only |
| No external action | No publish, files, network side effects (except chosen provider mode) |

---

## Out of scope

| Item | Reason |
|------|--------|
| Web UI / desktop UI | Not terminal CLI plan |
| Operator Console | Separate backlog |
| Persistent sessions | No memory layer |
| Memory / database | Forbidden |
| Multi-turn chat loop | Single run only in v1 |
| Task queue | Not orchestrator |
| Real publishing | Demo only |
| File modification | No execution |
| Task routing to other agents | Not triage impl |
| Provider calls by default | Policy |
| Model comparison / A-B | Not eval platform |
| Production deployment | Lab artifact |
| Cloud providers | Local explicit only in Mode 2 |
| Modifying `minimal_demo.py` | Agent logic frozen |
| Modifying `demo_runner.py` | Runner v0.1 frozen |

---

## Boundary with Demo Runner v0.1

| Demo Runner v0.1 | Free-Form CLI (planned) |
|------------------|-------------------------|
| Fixed 15 scenarios | Custom task text |
| Wraps existing commands | Self-contained flow (impl detail TBD) |
| Frozen | New artifact |
| Baseline eval menu | Not required in v1 (optional link in docs) |

Both may coexist. Operator chooses entry point.

---

## v1 minimal slice

One script, one task, one run, mock/default default, Russian output, gates visible, exit.

No chat. No memory. No database.
