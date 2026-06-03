# Codex for OSS — Application Note

## Repository qualification (under 500 characters)

Agent Factory OS is an early-stage open-source project for governance-first AI agent engineering. It provides agent templates, safety gates, freeze/sign-off workflows, local provider boundaries, evaluation harnesses, and operator-friendly CLI demos for building auditable, maintainable AI agents.

## API credits usage (under 500 characters)

I will use ChatGPT Pro/Codex to improve the open-source agent engineering workflow: review architecture changes, generate safer templates, refine evaluation harnesses, document agent patterns, and accelerate implementation while preserving governance, traceability, and human approval gates.

---

## Longer project summary

### Why it matters

Most agent repos optimize for demos and autonomy. Agent Factory OS optimizes for **auditability**: explicit approval, fail-closed delivery, frozen baselines, and no-network evaluation so teams can evolve agents without treating LLM output as truth.

### Who benefits

- Open-source contributors learning safe agent patterns
- Operators running local CLI demos with readable traces
- Maintainers using phase reviews and freeze records for controlled change

### Implemented today

- Review Assistant template + thin implementation
- Provider safety harness (16 cases, PASS=16 no network)
- Demo Runner v0.1 with happy / missing_approval scenarios
- Evaluation baselines (thin, mock LLM, smoke, text traces)
- Governance artifacts and Task Triage agent specs (v0.1)

### Planned

Free-form CLI freeze, memory triage, task triage thin implementation, optional live provider harness — see [ROADMAP.md](../../ROADMAP.md).

### Non-production

Not a hosted product, not security-certified, not affiliated with model vendors. Real providers are opt-in only.

### Maintenance evidence

- Phase-based development under `governance/`
- Freeze records under `*/freeze/`
- Runnable validation scripts under `evaluation/scripts/`
- Russian operator curriculum (`START_HERE_RU.md`, `QUICKSTART_RU.md`)
- Documented roadmap and contribution/security policies

**Disclaimer:** This note does not guarantee program approval or any official OpenAI partnership.
