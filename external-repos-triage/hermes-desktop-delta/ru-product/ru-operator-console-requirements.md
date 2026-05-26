# RU Operator Console Requirements (Future)

Draft requirements — **not implementation**. Phase 4+ reference.

---

## Interface

- [ ] Russian UI for all operator-critical screens
- [ ] Bilingual links to frozen specs (RU summary + EN canonical)
- [ ] Clear RU labels for DELIVERED / BLOCKED / ESCALATED / FAILED

---

## Provider-safe configuration

- [ ] No API keys in repo or screenshots
- [ ] Env-based secrets only; masked in UI
- [ ] Explicit "provider not approved" for unvetted RU endpoints
- [ ] Implemented vs planned provider badges

---

## Visible governance

- [ ] Freeze version (e.g. review-assistant-thin-v0.2)
- [ ] Change lock status
- [ ] Evaluation PASS/FAIL last run
- [ ] Governance phase / verdict links

---

## Approvals and traces

- [ ] Approval queue with pending items
- [ ] Trace viewer with required events highlighted
- [ ] No delivery without visible approval_granted

---

## Safety warnings

- [ ] "LLM output ≠ truth" on every provider screen
- [ ] No hidden autonomy (tools/schedules/gateways disabled by default)
- [ ] Escalation reasons visible in RU

---

## Non-goals (v1 console)

- No skill installer
- No gateway configuration
- No schedule/cron UI
- No persona/SOUL editor
- No digital twin features
