# Transcript Save Plan

**Date:** 2026-05-26  
**Status:** PLAN_ONLY

Optional future transcript saving for Demo Runner. **Not enabled by default.**

---

## Default behavior

| Setting | Value |
|---------|-------|
| Transcript save | **disabled** |
| Enable | explicit flag only, e.g. `--save-transcript` or menu prompt «Сохранить? (y/N)» |
| Default answer | **N** |

Transcript saving must not appear in impl until Phase 3.5.2-Impl explicitly approves this section.

---

## Potential future path

```text
demos/review-assistant-runner/transcripts/
├── 2026-05-26_143022_missing_approval.md
├── 2026-05-26_143105_happy.md
└── ...
```

**Gitignore recommendation (impl phase):** add `demos/review-assistant-runner/transcripts/*.md` if transcripts may contain env snippets — plan only.

---

## Transcript contents

| Section | Include |
|---------|---------|
| Timestamp | ISO local time |
| Selected scenario | Menu ID + scenario name |
| Russian title | From menu plan |
| Command | Exact subprocess command |
| Raw output | Full stdout/stderr from demo |
| Parsed decision | DELIVERED / BLOCKED / etc. |
| Parsed delivered | yes/no |
| Operator summary | Russian block from [OPERATOR_OUTPUT_FORMAT_RU.md](OPERATOR_OUTPUT_FORMAT_RU.md) |
| Safety interpretation | One-line status |
| Runner version | e.g. demo-runner-v0.1 |

---

## Forbidden in transcripts

| Forbidden | Reason |
|-----------|--------|
| Secrets / API keys | Security |
| Raw auth headers | Security |
| Private client data | Policy |
| Real project data | Unless explicitly approved synthetic |
| Full provider config dumps | May leak URLs with tokens |
| Passwords from env | Redact `RA_*` if sensitive |

**Redaction rule (future):** if env vars printed, show only `RA_LLM_BASE_URL=***` unless operator opts in to debug mode (not in v0.1 runner plan).

---

## Transcript format (Markdown)

```markdown
# Demo Transcript — {scenario}

**Date:** {timestamp}
**Scenario:** {name}
**Command:** `{cmd}`

## Operator Summary

{russian_summary_block}

## Raw Output

```
{stdout}
```

## Safety Note

{safety_status}
```

---

## When to save

| Trigger | Allowed |
|---------|---------|
| `--save-transcript` flag | yes |
| Post-run prompt default N | yes |
| Auto-save every run | **no** |
| Save to cloud | **no** |

---

## Rollback

If transcripts leak secrets or grow unbounded → disable feature, delete folder, document in governance.

See [ROLLBACK_PLAN.md](ROLLBACK_PLAN.md).
