# Local Filesystem Risk

---

## Pinned context folders

Hermes agent can read workspace files via toolsets.

**Risk:** agent reads secrets (.env, SSH keys, credentials.json).

---

## Reading local files

File + terminal toolsets with broad paths.

**Risk:** exfiltration via model or gateway.

---

## Accidental secret exposure

- Debug dump includes config
- Chat references file contents in trace
- Backup ZIP includes entire `~/.hermes`

---

## Workspace isolation

Hermes profiles isolate config but not necessarily OS-level sandbox.

**Risk:** one profile compromise affects user home directory.

---

## Allowed folder boundaries (Agent-OS doctrine)

Our templates specify memory/tool boundaries — Hermes does not align:

- No pinned-folder UI in our scope now
- Future console: show **allowed paths** read-only
- Never default to "full home directory"

---

## Mitigations for future console

1. Explicit workspace root picker with warning
2. Deny-list patterns (.env, *.pem, credentials*)
3. Trace redaction for file paths containing secrets
4. No backup without secret strip option

---

## Hermes lesson

GUI makes file access **easy to enable** — our gates must make it **hard to enable by mistake**.
