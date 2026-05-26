# Review Assistant Agent — Safety Gates

Required gates for this template.

## 1. Fail-Closed Gate

Default stop on uncertainty, missing approval, verification failure.

→ [safety-gates/fail-closed-gate.md](../../safety-gates/fail-closed-gate.md)

## 2. Verification Gate

Check draft before human handoff. Emit `verification_passed` or `verification_failed`.

→ [safety-gates/verification-gate.md](../../safety-gates/verification-gate.md)

## 3. Human Approval Gate

`approval_requested` before delivery. No auto-publish.

→ [safety-gates/human-approval-gate.md](../../safety-gates/human-approval-gate.md)

## 4. Escalation Gate

Critic uncertain or repeated failure → `escalation_triggered` → supervisor/human.

→ [safety-gates/escalation-gate.md](../../safety-gates/escalation-gate.md)

## 5. Evaluation Gate

Five scenarios in [evaluation.md](evaluation.md) before acceptance.

→ [safety-gates/evaluation-gate.md](../../safety-gates/evaluation-gate.md)

## Gate Order (Conceptual)

```
draft → verification → (critique advisory) → approval → output
         ↓ fail              ↓ uncertain
      stop/escalate      fail-closed/escalate
```

## Not Required in v0.1

- Tool-use gate (no external tools beyond draft/critic conceptually)
- Memory-boundary gate active (minimal memory — see memory-boundaries.md)

## Trace Expectation

Every scenario must show gate pass/fail in [expected-traces.md](expected-traces.md)
