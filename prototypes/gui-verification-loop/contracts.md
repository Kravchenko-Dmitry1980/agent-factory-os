# GUI Verification Loop — Contracts

## Inputs

| Field | Type | Required |
|-------|------|----------|
| `screen_before` | mock state id | yes |
| `planned_action` | click descriptor | yes |
| `expected_screen_after` | mock state id | yes |
| `screen_after` | mock state id | after action |

## Outputs

| Field | Type | When |
|-------|------|------|
| `outcome` | A / B / C | after visual verify |
| `click_executed` | bool | terminal |
| `rejection_reason` | string | if rejected |

## Verification Points

- Compare `screen_after` to `expected_screen_after`
- A → allow progress; B/C → reject click advancement

## Failure States

| State | Outcome | Action |
|-------|---------|--------|
| Wrong screen | B | Replan, no goal advance |
| No change | C | Retry limit, fail-closed |
| Unverified click | — | Never execute without verify pass |

## Escalation Points

- Repeated C on same subgoal → circuit breaker (demo: 2 strikes)
