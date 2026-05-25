# Manual Review Guide

Phase 2.5 evaluation is **human judgment assisted by scenarios** — not automated pass/fail from a platform.

---

## When To Review

- Before merging governance-touching changes
- After modifying shared gates, audit, or retry constants
- When demo behavior "feels" different but exits 0
- When adding new adapter or workflow integration

---

## Review Process

1. **Read the change** — what gate moved?
2. **Pick scenarios** — from `change-impact-matrix.md`
3. **Run demos** — record output locally
4. **Compare traces** — `trace-diff-checklist.md`
5. **Run quality gates** — applicable gate files
6. **Check red flags** — `red-flag-checklist.md`
7. **Verdict** — PASS / FAIL / rollback

---

## What To Look For

| Signal | Action |
|--------|--------|
| Fewer audit lines | Investigate — likely regression |
| New "shortcut" branch | Map to fail-closed scenarios |
| Retry constant change | Run escalation scenarios |
| Shared module extraction | Run full smoke checks |
| "Mock only" exception | Verify real adapter still gated |

---

## What NOT To Trust

- Exit code 0 alone
- Plausible LLM prose
- Critic PASS verdict
- "It worked on my machine" without trace
- Metric count without event names

---

## Output

Document locally (optional):

```text
Change ID / description:
Scenarios executed:
Trace diff notes:
Gate results:
Human verdict:
```

No required template file in git — keep review lightweight.

---

## Time Budget

Target: **15–30 minutes** for a focused local review. If review requires hours of automation setup — scope has drifted toward platform thinking.
