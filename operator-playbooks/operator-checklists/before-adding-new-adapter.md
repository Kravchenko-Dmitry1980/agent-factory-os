# Before Adding New Adapter

High drift risk — extra scrutiny required.

- [ ] Read `integrations-real/governance/integration-boundaries.md`
- [ ] One adapter = one lesson (no UniversalAdapter)
- [ ] Mock mode works without credentials
- [ ] Fail-closed preserved (timeout, malformed, deny)
- [ ] Append-only audit pattern
- [ ] Change proposal + impact analysis written first
- [ ] Evaluation scenarios updated (if behavior documented)
- [ ] No new orchestration engine

Checklist: `integrations-real/governance/adapter-complexity-limits.md`

If unsure — discuss before coding.
