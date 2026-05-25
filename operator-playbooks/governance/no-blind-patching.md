# No Blind Patching

When something fails, **understand first** — do not patch until you know which invariant broke.

---

## Bad loop

```text
demo fails → random fix → demo passes → gate silently removed → future incident
```

---

## Good loop

```text
demo fails → read error + trace → identify gate → rollback or targeted fix → smoke + trace compare
```

---

## Especially dangerous patches

- Increase MAX_RETRIES
- Comment out approval check
- Catch-all except on LLM parse
- Remove escalation event
- Truncate memory instead of reject

---

## If AI suggests a patch

1. Which gate does it touch?
2. Run fail-path demo after patch
3. Reject if audit gets thinner

Troubleshooting: [../troubleshooting/common-errors.md](../troubleshooting/common-errors.md)
