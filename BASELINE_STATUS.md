# BASELINE STATUS

## Date

2026-05-21 — Phase 0.1 (Git Baseline + Source Policy)

## Current State

| Parameter | Value |
|-----------|-------|
| Root | `C:\Dima\Projects\CURSOR\AGENT` |
| Purpose | Engineering knowledge operating system for AI agents |
| Files (excl. `.git`, `.venv`) | 156 |
| Markdown files | 153 |
| Agent-OS sections | 13 (`00_foundations` … `12_diagrams`) + `templates/` |
| Atomic notes (partial) | ~85 in `agent-os/00–09/` |
| Empty files | 0 |

Repository layout unchanged from [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md): no files moved, deleted, or renamed.

## Git

| Check | Status |
|-------|--------|
| `git init` | ✅ Done |
| Branch | `master` |
| Commits | ❌ None yet |
| `.gitignore` | ✅ Created (Phase 0.1) |
| Remote | Not configured |

**Phase 0.1 deliverables:** `.gitignore`, updated `sources.md`, updated root `README.md`, this file.

Initial commit is **not** performed automatically — ready when you run `git add` + `git commit`.

## Source Corpora

### A. Claude Code architecture

| Field | Value |
|-------|-------|
| Path | `Books/claude/` |
| Status | Canonical source |
| Format | 18 markdown chapters |
| Policy | Read-only during extraction |
| Agent-OS integration | Catalog stubs in `agent-os/10_research/chapters/` |

### B. Code as Agent Harness survey

| Field | Value |
|-------|-------|
| Source PDF | `Books/agents/all.pdf` (102 pages, ~9.9 MB) |
| Converted chapters | `Books/agents/chapters/` (6 files) |
| Raw / cleaned | `Books/agents/raw/all.raw.md`, `Books/agents/cleaned/all.cleaned.md` |
| Status | Converted source corpus, not yet fully cataloged in Agent-OS |
| Policy | PDF immutable; generated markdown — no manual edits until QA complete |

Policy documented in [agent-os/10_research/sources.md](agent-os/10_research/sources.md).

## Generated Artifacts

| Artifact | Location | Regenerable |
|----------|----------|-------------|
| Raw PDF extraction | `Books/agents/raw/all.raw.md` | Yes (`convert_pdf_to_md.py`) |
| Cleaned markdown | `Books/agents/cleaned/all.cleaned.md` | Yes |
| Survey chapters | `Books/agents/chapters/*.md` | Yes (re-run pipeline) |
| Pipeline index / report | `Books/agents/index.md`, `conversion_report.md` | Yes |
| Research chapter stubs | `agent-os/10_research/chapters/ch01–ch18` | N/A (catalog layer) |
| Extraction plans | `agent-os/10_research/**/extraction-plan.md` | Manual |

PDF conversion completed 2026-05-21 with **zero errors** (see `Books/agents/conversion_report.md`). Manual QA of tables/citations still pending.

## Immediate Risks

| Risk | Mitigation (Phase 0.1) |
|------|------------------------|
| `.venv/` accidentally committed | `.gitignore` excludes `.venv/` |
| Two corpora, one documented | `sources.md` + root README updated for both |
| Source/generated mixed in `Books/agents/` | Policy: PDF frozen; chapters no manual edit until QA |
| Orphan `Books/agents/READA.md` | Documented in audit; not removed (out of scope) |
| No git baseline | Ready for initial commit after review |
| Harness survey not in research catalog | Flagged — address in Phase 1 |

## Next Safe Step

**Phase 1 — Knowledge OS Bootstrap:**

1. Review untracked files (`git status`)
2. Create initial commit (baseline snapshot)
3. Add harness survey catalog stubs in `agent-os/10_research/` (6 chapters)
4. Manual QA of PDF conversion (tables, figures, citations)
5. Continue extraction per `extraction-plan.md` (ch09, ch12–14, ch16–18)

See [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md) §9 for full roadmap.
