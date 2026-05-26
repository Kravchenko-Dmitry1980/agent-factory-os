# Template Freeze Policy

## Purpose

Prevent drift in accepted reference templates.

## When to Freeze

- After Phase 3.0 review PASS
- After explicit lead sign-off
- Before any implementation phase (Phase 3.1+)

## Frozen Means

- No direct edits to template files
- Changes only via [change-proposal-spec.md](../template-specs/change-proposal-spec.md)
- Rollback gate required for unfreeze

## Exceptions

- Typo fixes that do not change semantics → minor version + changelog note
- Governance-mandated scope corrections → documented in governance review

## Review Assistant v0.1

Target freeze after `governance/PHASE_3_0_BUILDER_KIT_REVIEW.md` verdict PASS.
