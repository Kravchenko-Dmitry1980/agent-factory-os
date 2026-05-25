# Source Quality Review

## Documents Compared

| File | Size (extract) | Role |
|------|----------------|------|
| `Brain OS.docx` | ~14k chars | **Primary** — contracts, API, ER, events, risks, backlog |
| `Brain OS MD.docx` | ~5k chars | **Secondary** — formal spec v0.1 summary |

## Consistency

| Topic | Consistent? | Notes |
|-------|-------------|-------|
| Service list | ✅ | Same 12 services |
| Execution modes | ✅ | Same 6 modes |
| Lifecycle | ✅ | 10 steps align |
| Routing pseudocode | ⚠️ | MD version simplified vs full docx rules |
| Events | ⚠️ | MD shorter list; docx has writeback/fallback/escalation |
| ER / API | ❌ in MD | Only in full docx |

## Quality Issues

1. **Formatting loss** — ASCII diagrams collapsed in docx extract (single-line boxes)
2. **Empty sections** — ER diagram, sequence diagrams referenced but no content in extract
3. **Duplicate API** — same endpoints in both docs with different detail level
4. **Interpretation risk** — plane names (CAIM etc.) appear without formal IPC
5. **No version field** on TaskEnvelope / API (except event_version)

## Extraction Confidence

| Area | Confidence |
|------|------------|
| Control plane scope | high |
| Contracts JSON | high |
| Routing rules | high |
| Memory scoring | medium (weights unspecified) |
| Planes branding | low |
| Adaptation | low |

## Verdict

**Brain OS.docx** — primary extraction source. **Brain OS MD.docx** — index/summary cross-check. Neither is production-ready spec without OpenAPI + evaluator + replay + writeback rules.
