# Telegram Adapter Fails

## Symptom

Errors from `integrations-real/telegram-review-gate/minimal-demo.py`.

## Default: mock mode

Runs **without** `TELEGRAM_BOT_TOKEN`. Onboarding should use mock only.

```powershell
python integrations-real/telegram-review-gate/minimal-demo.py
```

## Real mode (optional)

```powershell
$env:TELEGRAM_BOT_TOKEN = "..."
$env:TELEGRAM_CHAT_ID = "..."
python integrations-real/telegram-review-gate/minimal-demo.py --real
```

## Common issues

| Issue | Action |
|-------|--------|
| Invalid token | Use mock for learning |
| Timeout deny | Expected fail-closed — verify audit |
| httpx missing | `pip install httpx` |

## Governance

Timeout must **deny**, not auto-approve. See fail-closed doctrine.

Do not commit tokens or `integrations-real/.data/` contents.

Reference: `integrations-real/telegram-review-gate/README.md`
