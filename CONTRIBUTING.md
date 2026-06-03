# Contributing to Agent Factory OS

Thank you for helping improve this governance-first agent engineering project.

## What we welcome

- Documentation improvements (EN/RU)
- Agent **templates** and specs under `agent-builder-kit/`
- **Prototypes** and thin implementations with clear boundaries
- **Evaluation** checks that run without network by default
- **Governance** artifacts (reviews, freeze notes) when tied to an approved change
- Operator playbooks and curriculum updates

## What requires extra care

- Do **not** add production runtime, orchestrators, or “factory” automation without an explicit governance path
- Major behavioral or architectural changes need a **change proposal** (see `agent-builder-kit/` templates and `governance/`)
- Do **not** expand real-provider surfaces without updating provider policy and safety harness baselines

## Safety rules (mandatory)

- **No secrets** in commits (API keys, tokens, `.env`, private keys)
- **No provider calls by default** in CI or PR checks — use mock/no-network modes
- **No unsafe automation** (auto-publish, auto-approve, unbounded memory writeback)
- **No real client, private, or medical data** in demos or transcripts

## Before opening a PR

Run local baselines (no network):

```powershell
python evaluation/scripts/check_review_assistant_provider_safety.py
python evaluation/scripts/check_review_assistant_thin.py
python evaluation/scripts/check_review_assistant_llm_mock.py
python evaluation/scripts/check_review_assistant_real_provider_contract.py
python evaluation/scripts/run_demo_smoke_checks.py
python evaluation/scripts/check_expected_text_traces.py
python demos/review-assistant-runner/demo_runner.py --scenario happy
```

Report PASS/FAIL summaries in the PR description.

## Style

- Match existing folder conventions and kebab-case filenames
- Prefer small, reviewable diffs
- Keep traces human-readable; document new scenarios in demo READMEs

## Questions

Open a GitHub issue for design questions or use discussions if enabled by the maintainer.
