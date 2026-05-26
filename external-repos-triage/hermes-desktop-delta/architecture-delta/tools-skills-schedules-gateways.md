# Tools, Skills, Schedules, Gateways

Hermes Desktop surfaces with autonomy implications.

---

## Tools (14 toolsets)

| Aspect | Assessment |
|--------|------------|
| Hermes | web, browser, terminal, file, code exec, vision, image, TTS, … |
| Useful later | Read-only **tool boundary** viewer per template |
| Dangerous now | Toggle enables shell/file/browser without our gates |
| Required governance | tool-boundary-spec, tool-use-gate |
| Required approval | Human approval before destructive tool classes |

---

## Skills

| Aspect | Assessment |
|--------|------------|
| Hermes | Browse, install bundled + external skills |
| Useful later | Skill **review queue** (metadata, source trust) |
| Dangerous now | Skill installer = supply chain (Phase 2.10 pattern) |
| Required governance | source-trust-policy, external-template-policy |
| Required approval | Explicit install approval + eval |

---

## Schedules (cron)

| Aspect | Assessment |
|--------|------------|
| Hermes | Cron builder, 15 delivery targets |
| Useful later | Maybe **read-only** schedule audit (if ever allowed) |
| Dangerous now | Unattended autonomy, approval bypass |
| Required governance | human-approval-gate, fail-closed-gate |
| Required approval | Separate phase; never default-on |

---

## Gateways (16 messaging platforms)

| Aspect | Assessment |
|--------|------------|
| Hermes | Telegram, Discord, Slack, WhatsApp, Signal, … |
| Useful later | None for Agent-OS Lab core |
| Dangerous now | Accidental sends, token storage, always-on bot |
| Required governance | escalation-gate, memory-boundary-gate |
| Required approval | Per-channel security review + operator sign-off |

---

## Summary

| Surface | Agent-OS timing |
|---------|-----------------|
| Tools | MUCH_LATER (viewer only first) |
| Skills | MUCH_LATER (review, not installer) |
| Schedules | Do not build |
| Gateways | Do not build |

Hermes bundles all four as **product features**. We treat them as **governance hazards** until explicit future phase.
