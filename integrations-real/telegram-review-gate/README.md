# Telegram Review Gate

HITL approval through Telegram Bot API (optional) or local mock.

## Flow

```
workflow → review request → Telegram approve/reject → continue OR stop
```

## Run

```powershell
# Mock (default) — deny on timeout
python integrations-real/telegram-review-gate/minimal-demo.py
python integrations-real/telegram-review-gate/minimal-demo.py --mock-approve
python integrations-real/telegram-review-gate/minimal-demo.py --mock-reject

# Real (requires env)
$env:TELEGRAM_BOT_TOKEN="..."
$env:TELEGRAM_CHAT_ID="..."
python integrations-real/telegram-review-gate/minimal-demo.py --real
```

Single local process. No scaling. No production bot infra.
