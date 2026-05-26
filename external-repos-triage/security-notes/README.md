# Security Notes (External Repos)

Research-only. See [../../governance/phase-2-10/SKILL_ECOSYSTEM_SECURITY_REVIEW.md](../../governance/phase-2-10/SKILL_ECOSYSTEM_SECURITY_REVIEW.md).

**Rule:** treat every external skill/template/hook/MCP as **untrusted until reviewed**.

| Risk class | Examples in triage set |
|------------|------------------------|
| Prompt injection | SKILL.md body instructions |
| Tool overreach | MCP, hooks, ruflo plugins |
| Data exfiltration | network calls in skills |
| CI token abuse | claude-code-action |
| Supply chain | bulk npx installs |

No scanners were run in Phase 2.10 (no install). scientific-agent-skills documents Cisco skill-scanner for **future** manual use.
