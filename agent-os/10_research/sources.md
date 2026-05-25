# Original Sources — Preservation Policy

Two independent source corpora feed the Knowledge OS. **Books/** is the source layer; **agent-os/** is the curated knowledge layer.

---

## A. Claude Code Architecture Corpus

| Field | Value |
|-------|-------|
| **Path** | `Books/claude/` |
| **Status** | Canonical source |
| **Format** | Markdown chapters (18 files) |
| **Policy** | Read-only during extraction |

```
Books/claude/
├── ch01-architecture.md
├── ch02-bootstrap.md
├── …
└── ch18-epilogue.md
```

| Rule | Policy |
|------|--------|
| Modify chapter text | ❌ Forbidden during research phase |
| Move chapter files | ❌ Keep in `Books/claude/` |
| Copy chapter bodies into research | ❌ Use index stubs + links only |
| Extract to atomic notes | ✅ Into `agent-os/00–09/` per [extraction-plan.md](extraction-plan.md) |
| Cite source in extractions | ✅ `Books/claude/chXX-*.md` in `## Sources` |

**Provenance:** Markdown chapters decomposed from PDF book on Claude Code architecture. Language: English (source).

**Research catalog:** [chapters/index.md](chapters/index.md) — index stubs only, no chapter body copies.

---

## B. Code as Agent Harness Survey Corpus

| Field | Value |
|-------|-------|
| **Source PDF** | `Books/agents/all.pdf` |
| **Converted chapters** | `Books/agents/chapters/` (6 files) |
| **Raw extraction** | `Books/agents/raw/all.raw.md` |
| **Cleaned extraction** | `Books/agents/cleaned/all.cleaned.md` |
| **Status** | Converted source corpus, not yet fully cataloged in Agent-OS |
| **Policy** | PDF is immutable source; generated markdown should not be manually edited until QA is complete |

```
Books/agents/
├── all.pdf                      ← immutable source (102 pages)
├── convert_pdf_to_md.py         ← reproducible pipeline
├── raw/all.raw.md               ← regenerable intermediate
├── cleaned/all.cleaned.md       ← regenerable intermediate
├── chapters/ch01–ch06*.md       ← converted chapters (post-pipeline)
├── index.md                     ← chapter navigation
└── conversion_report.md         ← pipeline report
```

| Rule | Policy |
|------|--------|
| Modify `all.pdf` | ❌ Immutable source |
| Manually edit `chapters/*.md` | ❌ Until conversion QA is complete |
| Re-run pipeline | ✅ Via `convert_pdf_to_md.py` (overwrites generated outputs) |
| Extract to atomic notes | ⬜ Planned — catalog not yet in `10_research/` |
| Cite source in extractions | ✅ `Books/agents/chapters/chXX-*.md` or `all.pdf` in `## Sources` |

**Provenance:** Survey *Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems* (arXiv 2605.18747). Converted 2026-05-21; see `Books/agents/conversion_report.md`.

---

## C. Brain OS Research Corpus

| Field | Value |
|-------|-------|
| **Path** | `Books/brain-os/` |
| **Status** | **Research tier — non-canonical — promotion-gated** |
| **Format** | Extracted markdown KB from author draft |
| **Policy** | Read-only; ideas only; strip plane branding before any curated promotion |

| Rule | Policy |
|------|--------|
| Treat as canonical source | ❌ Forbidden |
| Auto-promote to `agent-os/00–09/` | ❌ Requires PROMOTION_REVIEW + governance gate |
| Cite in curated extractions | ✅ With `source_tier: research` metadata |
| Promote adaptation-service, replay, curator automation | ❌ Frozen per governance |

**Provenance:** Author draft Brain OS documentation. Maturity labels in corpus; not production-validated as whole.

---

## D. Hermes Agent Research Sandbox

| Field | Value |
|-------|-------|
| **Path** | `experiments/hermes-agent-review/` |
| **Status** | **Research tier — non-canonical — promotion-gated** |
| **Upstream clone** | `experiments/hermes-agent-review/source/hermes-agent/` (reference only) |
| **Policy** | Pattern extraction source; no runtime code in curated layer |

| Rule | Policy |
|------|--------|
| Treat as canonical source | ❌ Forbidden |
| Copy upstream Python into agent-os | ❌ Forbidden |
| Promote scored PROMOTE_NOW patterns | ✅ Into existing taxonomy with provenance |
| Promote gateway matrix, provider catalog, sandbox backends | ❌ REJECT per PROMOTION_REVIEW |

**Provenance:** Phase 1.1 sandbox review; see `PROMOTION_REVIEW.md` §3.

---

## E. MobileAgent Research Sandbox

| Field | Value |
|-------|-------|
| **Path** | `experiments/mobile-agent-review/` |
| **Status** | **Research tier — non-canonical — promotion-gated** |
| **Upstream clone** | `experiments/mobile-agent-review/source/MobileAgent/` (reference only) |
| **Policy** | GUI modality research; no ADB/runtime in curated layer |

| Rule | Policy |
|------|--------|
| Treat as canonical source | ❌ Forbidden |
| Promote OCR pipelines, run scripts, model weights | ❌ REJECT per PROMOTION_REVIEW |
| Promote loop/verification/grounding concepts | ✅ With GUI anti-pattern pairs |

**Provenance:** Phase 1.1 sandbox review; see `PROMOTION_REVIEW.md` §4.

---

## Layer Model

```
Books/claude/                    ← canonical source (primary)
Books/agents/                    ← canonical source (secondary, QA pending)
Books/brain-os/                  ← research corpus (promotion-gated)
experiments/hermes-agent-review/ ← research sandbox (promotion-gated)
experiments/mobile-agent-review/ ← research sandbox (promotion-gated)
agent-os/10_research/            ← catalog, plans, navigation
agent-os/00–09/                  ← curated atomic knowledge
governance/                      ← promotion policy and logs
```

## Up

- [Research README](README.md)
- [Claude chapters index](chapters/index.md)
- [Master extraction plan](extraction-plan.md)
