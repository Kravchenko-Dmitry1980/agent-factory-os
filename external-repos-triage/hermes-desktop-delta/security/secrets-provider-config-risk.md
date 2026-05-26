# Secrets and Provider Config Risk

---

## API key storage (Hermes pattern)

- Written to `~/.hermes/.env`
- Credential pools for rotation
- RU fork: `NEURALDEEP_API_KEY`, `BITRIX_VIBECODE_API_KEY`

**Risks:** plaintext on disk, backup inclusion, shared PC, malware scan exfiltration.

---

## Provider config files

- `config.yaml` model blocks, base URLs
- Custom provider entries without registry validation

**Risks:** config drift from approved boundary; wrong endpoint sends data to untrusted host.

---

## Logging secrets

- Gateway logs, agent logs, debug dump from Settings
- Token usage in chat footer

**Risks:** keys or PII in log files; accidental share in support tickets.

---

## Exporting configs

- Backup/import full Hermes data

**Risks:** ZIP contains `.env`; user emails backup.

---

## Local backups

- User-driven backup without encryption warning

**Risks:** cloud sync folders pick up secrets.

---

## Screenshots / screen share

- Provider screens show key entry fields

**Risks:** training sessions leak keys.

---

## Shared machines

- Multi-user desktop; Hermes home in user profile

**Risks:** cross-user read if permissions wrong.

---

## Agent-OS policy (current + future)

| Rule | Status |
|------|--------|
| No keys in repo | now |
| Env vars only for real provider | Phase 3.3+ |
| Masked display in any future UI | later |
| No export of secrets in eval artifacts | now |
| Provider config change = change proposal | now |

---

## Lesson from Hermes

Provider wizard UX **accelerates** key placement on disk — governance must slow and audit, not streamline blindly.
