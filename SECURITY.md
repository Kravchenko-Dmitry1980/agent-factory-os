# Security Policy

## Reporting

- **Do not** post API keys, tokens, passwords, or private data in public GitHub issues
- Report security concerns via GitHub Issues with minimal reproduction, or contact the repository maintainer privately if contact details are published on the profile

## Contributor expectations

- Never commit `.env`, `.venv`, credentials, or live endpoint URLs with secrets
- Use environment variables only on your machine for optional local provider runs
- Real local provider (e.g. LM Studio) is **opt-in only** via explicit flags and operator confirmation
- Do not use real client, financial, medical, or personal data in demos, transcripts, or evaluation fixtures

## Scope of assurance

Agent Factory OS is an **early-stage, local-first** engineering repository. It does **not** claim production security certification, formal threat modeling completion, or enterprise compliance readiness.

## Safe defaults

- Mock LLM and synthetic provider safety harnesses are the default validation path
- Demos and scripts are designed to **fail closed** when approval or configuration is missing
- Transcript policies discourage logging secrets and raw provider configuration

## Dependencies

This project intentionally avoids adding runtime dependencies for core demos where possible. Review any new dependency for supply-chain risk before proposing it in governance.

## If you accidentally committed a secret

1. Revoke the credential at the provider immediately
2. Do not rely on git history deletion alone — rotate keys
3. Open a private report to the maintainer if the secret reached a public remote
