# RU-First UX Lessons

From Hermes Desktop RU fork + Agent-OS context.

---

## Why RU-first UX matters

- Primary users and operators may prefer Russian for setup, errors, and governance terms
- Provider names (NeuralDeep, Bitrix VibeCode) need clear RU descriptions
- Reduces friction for learners entering via `curriculum/ru/`

---

## Why Russian learners/operators need Russian entry

- Technical English barrier blocks approval/trace understanding
- Error messages in English hide safety implications
- Hermes RU fork shows **full locale coverage** per screen module — not just README translation

---

## Why curriculum/ru/ was correct

- Learning path precedes operator tooling
- Markdown curriculum scales without Electron complexity
- RU docs align with governance-first teaching before GUI

---

## Future Operator Console: RU-first mode

When console exists (Phase 4+):

- Russian UI for navigation, approvals, freeze status
- Bilingual governance terms (RU + link to spec)
- Provider warnings in Russian
- **Default language** configurable; RU not afterthought

---

## What to avoid in localization

| Pitfall | Why |
|---------|-----|
| Partial translation | Mixed RU/EN hides critical safety strings |
| Translating without governance review | "Approve" vs "Publish" confusion |
| Locale-only fork without upstream merge | Stale security fixes (fork risk) |
| Marketing RU without architecture quality | Hype over gates |
| Assuming RU providers "just work" | Planned ≠ implemented |

---

## Hermes RU fork lesson

Minimal delta works: **i18n + provider presets + URL detect**. Our delta should be **docs + future console spec**, not a fork.
