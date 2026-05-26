# Template Acceptance Checklist

Use before marking a template **accepted**.

## Structure

- [ ] All sections from [agent-template-spec.md](../template-specs/agent-template-spec.md) present
- [ ] Purpose and forbidden behavior explicit
- [ ] Workflow documented
- [ ] Tools allowlisted (or none declared)

## Safety

- [ ] Fail-closed gate referenced
- [ ] Verification gate referenced
- [ ] Human approval gate for risky outputs
- [ ] Escalation path defined
- [ ] Anti-patterns section complete

## Memory & Tools

- [ ] Memory boundaries documented
- [ ] No unbounded memory
- [ ] No unrestricted shell/filesystem
- [ ] Production write requires human gate

## Evaluation & Trace

- [ ] Evaluation scenarios with pass/fail criteria
- [ ] Expected traces documented
- [ ] Failure modes listed
- [ ] Trace review checklist passable

## Governance

- [ ] Related prototypes linked (reference only)
- [ ] Governance docs referenced
- [ ] Change proposal template included
- [ ] Phase 3 scope compliant (no CV/twin/RAG/MCP)

## Sign-off

| Role | Name | Date | OK |
|------|------|------|-----|
| Author | | | |
| Reviewer | | | |
