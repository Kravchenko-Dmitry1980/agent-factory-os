# Telegram Review Gate — Architecture

## Components

| Piece | Role |
|-------|------|
| **Workflow** | Proposes action, blocks until approval |
| **Review request** | Fingerprint-bound pending record |
| **Telegram channel** | Human approve/reject (or mock file) |
| **Gate** | Deny-by-default on timeout |
| **Audit** | JSONL append in `.data/telegram-review-gate/` |

## Modes

- **Mock:** writes pending request; CLI flag or timeout simulates human
- **Real:** `sendMessage` + short `getUpdates` poll (single process)

## Non-Goals

- Webhook server
- Multi-chat routing
- Bot command framework
