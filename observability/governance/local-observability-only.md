# Local Observability Only

## Storage

| Artifact | Location |
|----------|----------|
| Adapter audit JSONL | `integrations-real/.data/*/audit.jsonl` |
| SQLite audit/reviews | `integrations-real/.data/*/*.db` |
| Example traces | `observability/examples/*.txt` |

## Processing

- **Manual read** — text editor, `Get-Content`, `type`
- **Optional** — `python -m json.tool` per line
- **Forbidden** — ELK, Loki, CloudWatch agent

## Network

Observability layer emits **no network traffic**.

## Credentials

None required for Phase 2.3 content.

## Promotion

Insights may inform future `agent-os/03_harness-engineering/` notes — not monitoring infra repos.
