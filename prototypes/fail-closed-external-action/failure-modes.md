# Fail-Closed External Action — Failure Modes

## Hallucination

Agent proposes action on wrong target (wrong email, wrong API). **Mitigation:** verification step; uncertain → deny.

## Retry Loops

Auto-retry denied external calls. **Mitigation:** no auto-retry without new approval.

## Missing Verification

Execute on intent alone. **Mitigation:** verify before approval gate.

## Memory Drift

Stale approval token reused for different action. **Mitigation:** action hash bound to approval in demo.

## Unsafe Autonomy

Auto-execute "low risk" actions. **Mitigation:** deny-by-default for all; low risk still logs.

## Missing Escalation

Deny without human queue. **Mitigation:** audit + escalate flag for high-risk.

## Governance Bypass

Direct `execute()` call. **Demo:** execute checks approval registry.
