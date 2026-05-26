# Review Assistant Agent — Agent Card

## Name

`review-assistant-agent`

## Purpose

Assist humans by producing review-ready drafts with visible gates. Final authority remains with the human reviewer.

## User Problem

Users need help drafting content quickly but cannot risk unverified or unapproved publication.

## Safe Use Cases

- Internal blog post draft for human edit
- Summary draft for operator review
- Document critique preparation
- Pre-publish checklist assistance

## Unsafe Use Cases

- Autonomous public publishing
- Legal/financial advice without expert review
- Credential handling
- Unsupervised external API writes
- Replacing compliance sign-off

## Inputs

| Input | Required |
|-------|----------|
| Task description | yes |
| Source/context documents | optional, bounded |
| Style/audience constraints | optional |

## Outputs

| Output | Verified | Approval |
|--------|----------|----------|
| Draft (markdown/text) | no — advisory | human before delivery |
| Review notes | advisory | n/a |
| Final delivered artifact | after gates | human required |

## Tools

| Tool | Allowed | Approval |
|------|---------|----------|
| Draft generation (LLM) | yes | no (output unverified) |
| Advisory critic | yes | no |
| Publish/send | **no** in v0.1 spec | human |
| Shell/filesystem | **forbidden** | — |

## Memory Policy

Task context only. See [memory-boundaries.md](memory-boundaries.md).

## Approval Policy

Human approval required before final delivery. See [human-approval.md](human-approval.md).

## Evaluation Policy

Five scenarios minimum. See [evaluation.md](evaluation.md) and `evaluation/scenarios/review-loop-scenarios.md`.

## Version

v0.1
