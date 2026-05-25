# Evaluation Reports (Local)

Optional folder for **local-only** evaluation notes — not required in git.

---

## Suggested Use

Save after a change review:

```text
evaluation/reports/YYYY-MM-DD-change-slug.md
```

Include:

- Scenarios run
- Smoke script output summary
- Trace diff notes
- Quality gate verdict
- Reviewer name

---

## Do Not Commit

- Live API responses with secrets
- Customer data
- Large trace dumps (use excerpts)

---

## Gitignore

Add `evaluation/reports/*.md` locally if you want to keep notes private — optional, not enforced by Phase 2.5.
