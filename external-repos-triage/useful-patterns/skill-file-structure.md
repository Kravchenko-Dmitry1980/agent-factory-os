# Pattern: Skill File Structure

| Field | Value |
|-------|-------|
| **Source repo** | scientific-agent-skills |
| **Pattern** | YAML frontmatter (`name`, `description`, `license`) + long body with when-to-trigger / when-NOT + requirements |

## Why Useful

Clear trigger boundaries reduce accidental skill activation. Matches agentskills.io — portable to Cursor.

## How It Could Help Later

Agent Builder Kit `skill-template-spec.md`: required frontmatter fields + forbidden triggers list.

## Why Not Adopt Now

Installing 138 skills violates supply-chain policy.

## Safe Future Use

Copy **schema only** into our spec; author 1–2 lab skills with mentor review.
