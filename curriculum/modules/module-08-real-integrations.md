# Module 08 — Real Integrations

## Goal

See how fail-closed gates survive **real I/O** — still local, mock by default.

## Simple Explanation

**Real adapters** talk to Telegram, HTTP, LLM APIs, SQLite, filesystem — but remain small and optional. Mock mode teaches failures without API keys.

## Key Ideas

- External input is untrusted
- Timeouts and malformed data must reject
- One adapter = one lesson
- No UniversalAdapter platform

## Files to Read

- `integrations-real/README.md`
- `integrations-real/governance/local-first-policy.md`
- [../operator-playbooks/scenario-guides/scenario-llm-verification.md](../operator-playbooks/scenario-guides/scenario-llm-verification.md)

## Commands to Run

```powershell
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario happy
python integrations-real/llm-verification-adapter/minimal-demo.py --scenario malformed
python integrations-real/local-queue-worker/minimal-demo.py --scenario recovery
python integrations-real/filesystem-audit-log/minimal-demo.py --scenario happy
```

## Exercise

[../exercises/exercise-detect-bad-llm-output.md](../exercises/exercise-detect-bad-llm-output.md)

## Common Mistakes

- Requiring API keys for onboarding
- Trusting LLM because JSON parsed
- Building adapter registry

## Checkpoint Questions

1. Default mode for LLM adapter?
2. What trace file shows malformed LLM?
3. Where is local runtime data stored?

## Expected Outcome

Student runs LLM malformed scenario and explains reject path.
