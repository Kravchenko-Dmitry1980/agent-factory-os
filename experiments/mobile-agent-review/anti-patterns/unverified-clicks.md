# Unverified Clicks

---

## Anti-Pattern

Execute tap/swipe and assume success without observing UI delta.

---

## Where MobileAgent Addresses It

- v2+ mandatory reflection path (optional but default on)
- v3 ActionReflector + error_flag_plan
- GUI-Critic pre-op (research, not integrated)

---

## Where Gap Remains

### v3.5 E2E mobile loop

Single VLM cycle — less explicit A/B/C in Python; relies on model observing next screenshot without structured verification record.

### Disabled reflection

v2 README explicitly allows turning off reflection for speed → **unverified clicks**.

### False A outcomes

Reflector may classify success prematurely — no second-check harness.

### No haptic/system event confirmation

ADB `input tap` return code ignored; no wait for activity change.

---

## Contrast with Agent-OS Ideal

Claude Code: tool result carries stdout/stderr — structured feedback.

GUI: feedback is visual — must be **explicit verification step** in loop contract.

---

## Recommendation

Never disable verification in production GUI agents without:
- Alternative env reward signal
- Or strong benchmark-proven E2E model with thinking variant

Extract **A/B/C taxonomy** as reusable verification enum for Agent-OS GUI modality.
