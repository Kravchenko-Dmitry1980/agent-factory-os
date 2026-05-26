# Desktop Security Risks

Hermes Desktop threat model notes for Agent-OS research.

---

## Electron / desktop shell

- Large attack surface vs stdlib Python demo
- Unsigned installers (Windows SmartScreen, Fedora nogpgcheck)
- Auto-updater (`electron-updater`) — supply chain trust

---

## IPC validation

- Main/renderer/preload boundary (Hermes has hardening tests)
- Risk: over-exposed IPC handlers → RCE from renderer
- Our future console: minimize IPC; read-only first

---

## Secret storage

- Keys in `~/.hermes/.env`, credential pools
- OAuth tokens (scaffolding in RU fork)
- Backup/export may include secrets

---

## Filesystem access

- Hermes agent toolsets: file, terminal, browser
- Installer writes to home directory
- Session DB local SQLite

---

## Tool execution

- 14 toolsets including shell and code execution
- Tool output feeds back to model — injection chain

---

## Update process

- Remote update channel compromise
- User trained to bypass SmartScreen ("Run anyway")

---

## Gateway exposure

- 16 platforms; tokens in config
- Always-on bots — message injection from channels

---

## Schedule / cron risk

- Unattended runs without human in loop
- 15 delivery targets — accidental external sends

---

## Provider key leakage

- Logs, debug dump, backup ZIP, screenshots
- PostHog analytics dependency — telemetry scope review needed

---

## Remote mode risk

- Desktop stores remote API URL + key
- Extends trust to network endpoint
- Shared machines — key persistence

---

## Agent-OS takeaway

Desktop operator layer needs **separate security architecture** before any UI build. Hermes is useful as **checklist input**, not security model to copy wholesale.
