# Quality Gate Checklist

Run **before accepting** a change to prototypes, integrations-real, shared modules, or governance gates.

---

## 1. Scope

- [ ] Change scope documented (which demos/adapters)
- [ ] Risk class identified (low / medium / high) per `evolution/change-proposals/`
- [ ] Rollback path identified

## 2. Behavioral Checks

- [ ] Affected scenarios re-run locally
- [ ] Smoke script executed: `python evaluation/scripts/run_demo_smoke_checks.py`
- [ ] Trace check executed: `python evaluation/scripts/check_expected_text_traces.py`

## 3. Gate-Specific (check all that apply)

- [ ] [fail-closed-gate.md](fail-closed-gate.md)
- [ ] [verification-gate.md](verification-gate.md)
- [ ] [escalation-gate.md](escalation-gate.md)
- [ ] [memory-gate.md](memory-gate.md)
- [ ] [approval-gate.md](approval-gate.md)
- [ ] [audit-gate.md](audit-gate.md)

## 4. Trace Compare

- [ ] Baseline vs post-change trace compared
- [ ] No critical events removed
- [ ] OUTCOME block still correct

## 5. Governance

- [ ] No CI/CD files added
- [ ] No test framework dependency added
- [ ] No benchmark/leaderboard artifacts
- [ ] evaluation/ remains documentation + simple scripts

## 6. Verdict

| Verdict | Meaning |
|---------|---------|
| PASS | All applicable gates satisfied |
| CONDITIONAL | Docs-only or no demo touch |
| FAIL | Any safety gate failed — rollback first |

---

## Sign-Off (Human)

```text
Reviewer:
Date:
Change summary:
Scenarios run:
Verdict:
Notes:
```

Local only — no automated sign-off system.
