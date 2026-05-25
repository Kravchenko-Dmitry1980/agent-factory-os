# What Not to Touch

Unless you have explicit charter and governance review — **do not** do these things.

---

## Code & Architecture

| Do not | Why |
|--------|-----|
| Extract shared orchestration engine from prototypes | Platform drift |
| Merge all demos into one framework | Hides governance lessons |
| Add `UniversalAdapter` / plugin registry | Phase 2.2 anti-pattern |
| Increase retry limits "temporarily" | Masks verification bugs |
| Add auto-approve for "internal" actions | Hidden autonomy |
| Skip verification on LLM cache/fast path | Untrusted input leak |
| Remove escalation on retry exhaustion | Invisible failures |
| Instrument demos with heavy telemetry | Observability platform drift |

---

## Repository Areas

| Path | Operator rule |
|------|---------------|
| `Books/` | Read-only for operators — source corpus |
| `experiments/` | Read-only — research perimeter |
| `agent-os/` | Do not add notes without promotion process |
| `prototypes/shared/` | Change only with full smoke + evaluation |
| `integrations-real/.data/` | Local runtime data — do not commit secrets |

---

## Process

| Do not | Do instead |
|--------|------------|
| Patch blindly when demo fails | Read troubleshooting → rollback if needed |
| Add CI/CD for "convenience" | Use existing evaluation scripts manually |
| Add pytest harness | Use evaluation scenarios + human trace compare |
| Promote tutorial patterns to doctrine | Follow `governance/PROMOTION_STRATEGY.md` |
| Trust AI-generated architecture | Verify against doctrine + run demos |

---

## Safe to Touch (With Care)

- `operator-playbooks/` — documentation improvements
- `evaluation/reports/` — local notes (optional)
- `evolution/change-proposals/` — write proposals before code changes
- Single prototype **after** change proposal + regression check

---

## When You Must Change Shared Code

Required sequence:

1. [../change-guides/how-to-write-change-proposal.md](../change-guides/how-to-write-change-proposal.md)
2. [../operator-checklists/before-changing-workflow.md](../operator-checklists/before-changing-workflow.md)
3. Run [../runbooks/run-evaluation-checks.md](../runbooks/run-evaluation-checks.md)
4. [../operator-checklists/after-changing-workflow.md](../operator-checklists/after-changing-workflow.md)

---

## Red Line

If your change makes the system **easier to run** but **harder to audit why a decision happened** — stop. That is governance regression.

See [../governance/no-blind-patching.md](../governance/no-blind-patching.md)
