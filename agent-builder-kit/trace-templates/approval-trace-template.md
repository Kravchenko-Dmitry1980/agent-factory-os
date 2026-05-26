# Approval Trace Template

Focus on human approval sub-flow.

```
TRACE id=<trace-id> workflow=<agent-name> scenario=approval-flow
────────────────────────────────────────────────────────
[<time>] task_started
[<time>] ... draft and verification events ...
[<time>] approval_requested   actor=human  required=true artifact_id=<id>
[<time>] ... waiting ...
[<time>] verification_passed  actor=human  decision=approve  fingerprint=<hash>
[<time>] task_completed       actor=publisher  delivered=true
────────────────────────────────────────────────────────
APPROVAL approver_role=<role> timeout_policy=deny-by-default
```

## Denial variant

```
[<time>] approval_requested   actor=human  required=true
[<time>] approval_denied       actor=human  reason=<reason>
[<time>] task_failed           actor=system reason=approval_denied
```

## Timeout variant

```
[<time>] approval_requested   actor=human  required=true
[<time>] approval_timeout      actor=system policy=deny-by-default
[<time>] task_failed           actor=system reason=no_approval
```

**Rule:** No approval = no risky action.
