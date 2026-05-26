# Gateway and Schedule Risk

Hermes Desktop autonomy surfaces.

---

## Telegram / gateway actions

- 16 messaging integrations
- Tokens stored locally; bots can receive inbound messages
- Outbound sends from agent or scheduled jobs

**Risks:**

- Prompt injection via Telegram → tool execution
- Accidental publish to wrong channel
- Always-on listener expands attack window

---

## Scheduled tasks

- Cron: minutes, hourly, daily, weekly, custom
- 15 delivery targets (overlap with gateways)

**Risks:**

- Unattended autonomy without human approval
- Retry storms on failure
- Timezone/cron misconfiguration → off-hours sends

---

## Approval bypass

Hermes optimizes for **continuous assistant**, not **gated delivery**.

Schedules/gateways can act when operator is absent — conflicts with Review Assistant **approval_granted** model.

---

## Accidental sends

User enables gateway + schedule without understanding delivery target.

**Early signal:** test message to production channel.

---

## Agent-OS stance

| Feature | Decision |
|---------|----------|
| Gateways | Do not build |
| Schedules | Do not build |
| Unattended delivery | Forbidden without new governance phase |

---

## Future if ever allowed

Would require:

- human-approval-gate per delivery
- fail-closed on uncertainty
- separate security review per channel
- no default-on

Not on roadmap for Phase 3–4.
