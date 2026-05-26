# Repo Comparison Matrix

**Inspected:** 2026-05-25 (shallow clone, read-only)

| Dimension | scientific-agent-skills | claude-code-templates | SuperClaude | agentic-project-management | claude-code-action | ruflo |
|-----------|----------------------|----------------------|-------------|---------------------------|-------------------|-------|
| **Skill structure** | Strong (agentskills.io SKILL.md) | Skills as catalog item | Via ecosystem | Customization skill | N/A | 30+ skills plugins |
| **Agent template structure** | Per-domain skills | Rich agent paths | 20 agents | Planner/Manager/Worker | N/A | 98 agents |
| **Workflow structure** | Scientific pipelines | Commands + hooks | 30 /sc commands | Spec/Plan/Rules + handoff | GH workflow modes | Swarm/workflows |
| **Project management** | Low | Low | Medium (TASK.md) | **High** | Issue/PR triage | Goals plugin |
| **Automation** | npx skills add | npx component install | pip/npm install | apm init CLI | **GitHub Actions** | hooks + daemon |
| **Runtime risk** | Medium (skill instructions) | **High** (MCP/hooks) | High (MCP) | Medium (CLI) | **High** (CI bot) | **Critical** |
| **Security risk** | Supply-chain skills | Marketplace dump | MCP + personas | apm-auto autonomy | Token/PR write | MCP+swarm+RAG |
| **Phase 3 usefulness** | **INDIRECT** (skill spec) | **INDIRECT** (taxonomy) | LOW | LOW | **NONE** | **NONE** |
| **Long-term usefulness** | High (domain skills) | Medium | Medium | Medium | Medium (CI) | Low/negative |

## Recommended review order (future)

1. scientific-agent-skills — SKILL.md + SECURITY.md  
2. claude-code-templates — category taxonomy only (sample 10 files)  
3. agentic-project-management — planning doc templates  
4. SuperClaude — commands.md decision tree  
5. claude-code-action — security.md + solutions (no enable)  
6. ruflo — **do not deep-dive** except anti-pattern teaching
