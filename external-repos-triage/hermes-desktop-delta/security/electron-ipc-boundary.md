# Electron IPC Boundary

Why desktop security is a separate architecture area.

---

## Trust model

```text
Renderer (React UI)  ←→  Preload (bridge)  ←→  Main (Node/Electron)
                              ↑
                         IPC channels
```

- **Renderer:** untrusted — user content, markdown, webviews
- **Main:** trusted — filesystem, spawn, secrets, Hermes API

---

## Hermes hardening (observed in source/tests)

- `nodeIntegration: false`
- `contextIsolation: true`
- `sandbox: true`
- Navigation/webview allowlists
- `shell.openExternal` routed through helper
- Installer uses `execFileSync` not shell string concat

Still complex — many IPC handlers for Hermes operations.

---

## IPC validation requirements

| Rule | Why |
|------|-----|
| Allowlist channel names | Prevent arbitrary invoke |
| Validate all payload shapes | No path injection |
| No raw shell from renderer | Command injection |
| Minimize preload surface | Smaller attack graph |

---

## Command execution risk

Main process can spawn Hermes CLI, installer scripts, doctor checks.

**Risk:** compromised renderer → arbitrary command if IPC too broad.

---

## File access risk

Read/write config, backup, logs, `~/.hermes/*`.

**Risk:** path traversal via IPC args.

---

## Agent-OS implication

If we ever build Operator Console:

- Prefer **web UI + local read-only API** over full Electron initially
- If Electron: copy **hardening checklist** from Hermes tests, not feature set
- Never expose terminal/skill install via IPC in v1

---

## Reference

Hermes: `tests/electron-security.test.ts`, `src/main/security.ts`, `src/main/index.ts`
