# Evaluation Boundaries

Phase 2.5 scope limits — what evaluation **is** and **is not**.

---

## In Scope

- Markdown scenarios and expected outcomes
- Human trace comparison
- Local Python helpers (read-only checks)
- Quality gate checklists before change
- Regression matrices for reviewer
- Failure injection via existing demo flags

---

## Out of Scope

| Forbidden | Why |
|-----------|-----|
| CI/CD pipelines | Becomes deployment engineering |
| GitHub Actions | Automated merge gate drift |
| pytest/unittest harness | Test framework emergence |
| Benchmark suites | Model platform drift |
| Leaderboards / scoring | Wrong success metric |
| Cloud evaluation | Not local-first |
| RAG/vector eval | Wrong problem domain |
| Production load testing | Not Phase 2.5 |
| Modifying prototype runtime | Evaluation observes, does not refactor |

---

## Repository Touch Rules

Evaluation may:

- Add files under `evaluation/`
- Add governance review under `governance/PHASE_2_5_*`

Evaluation must not:

- Modify `agent-os/`, `Books/`, `experiments/` via scripts
- Add instrumentation middleware to demos without separate phase
- Require API keys for default checks

---

## Success Criterion

Reviewer can answer in 30 minutes: **Did small behavior stay safe?**

Not: **What is our test coverage percentage?**
