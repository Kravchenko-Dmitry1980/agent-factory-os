# Skill Ecosystem Security Review

Applies to: scientific-agent-skills, claude-code-templates skills, any future Cursor/Claude skills.

## Risk categories

| Risk | Description | Mitigation |
|------|-------------|------------|
| Prompt injection | Skill text steers agent to harmful goals | Human review + provenance |
| Malicious tool instructions | Run rm, curl exfil, pip install malware | Allowed/forbidden action list |
| Data exfiltration | Upload secrets, env files | Deny paths in spec |
| Unsafe shell | Arbitrary bash | No auto-exec in lab skills |
| Hidden dependencies | pip install in skill body | Pin + review |
| Supply chain | Community skills | Scanner + author trust tier |
| Over-permissive tools | MCP all repos | MCP freeze Phase 3 |
| API leakage | Keys in prompts | .env policy |

## Rules (Agent-OS Lab)

1. **Never install skills blindly** — no `npx skills add` in AGENT repo workflow  
2. **Never run skill-suggested commands** without operator review  
3. **Never unrestricted shell/tool** in curriculum demos  
4. **Every lab skill** (if ever authored) requires: provenance, author, allowed actions, forbidden actions, review date  
5. **Every skill** requires safety boundary section (fail-closed, human approval)  
6. **Third-party skills** stay in `external-repos-triage/` — not agent-os  

## Reference: scientific-agent-skills

They document:

- Read SKILL.md before install  
- Do not install all at once  
- Cisco skill-scanner (optional) — we did **not** run in 2.10  

## Phase 3.0

No skills shipped. Only `skill-template-spec` **document** may reference agentskills.io fields.
