# Brittle GUI Automation

Антипаттерны хрупкой автоматизации, наблюдаемые в MobileAgent и типичные для GUI agents.

---

## 1. OCR-List as Ground Truth

v2 prompts warn lists are inaccurate, yet actions often trust coordinates from OCR/DINO.

**Symptom:** Taps on wrong pixels, especially icons without text.

**Mitigation in repo:** Shift to GUI-Owl; disclaimer in prompt (weak).

---

## 2. Absolute Pixel Coordinates on Variable Layout

Same app, different devices/resolutions — v2 uses raw pixels without normalization.

**Mitigation:** v3+ normalized coords, smart_resize.

---

## 3. Hardcoded Task Notes in Manager

v3 `mobile_agent_e.py` embeds benchmark-specific hints (Audio Recorder icon shape).

**Symptom:** Overfit to eval suites, not generalizable.

---

## 4. Platform-Specific Driver Assumptions

ADB Keyboard required; iOS unsupported; Harmony version limits.

**Symptom:** Silent failures when prerequisites missing.

---

## 5. Sleep-Based Synchronization

Action loops use fixed sleeps after tap instead of wait-for-UI-stable.

**Symptom:** Flaky on slow networks / animations.

---

## 6. No Permission / Safety Layer

Unrestricted tap/type on real device — no confirm for payments, deletes, sends.

---

## 7. Monolithic Run Scripts

Each version duplicates controller logic — fixes don't propagate.

---

## Research Status

Document as **known limitations**, not blockers for pattern extraction.

When building production GUI harness, treat MobileAgent as **research reference**, not hardened runtime.
