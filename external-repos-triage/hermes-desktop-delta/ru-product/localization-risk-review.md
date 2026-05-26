# Localization Risk Review

Risks specific to RU fork and future RU Operator Console.

---

## Partial translation risk

Hermes upstream: English primary; zh locales. RU fork adds `ru/` but README still English-first.

**Risk:** Operators hit English errors in edge paths.  
**Mitigation:** Require complete safety-string coverage before RU console ship.

---

## Stale fork risk

`hermes-desktop-ru` tracks upstream but may lag security fixes (Electron, installer, IPC).

**Risk:** RU users on fork miss upstream hardening.  
**Mitigation:** Never depend on fork; treat as research snapshot only.

---

## Provider-specific assumptions

RU fork assumes OpenAI-compatible endpoints for NeuralDeep/Bitrix.

**Risk:** Different auth, rate limits, or logging vs global providers.  
**Mitigation:** Per-provider eval; no generic "custom URL" trust.

---

## Russian UX vs architecture quality

Localized UI can ship before governance UI exists (Hermes pattern).

**Risk:** Pretty RU interface hides missing approval/freeze surfaces.  
**Mitigation:** Agent-OS console must show governance **before** polish.

---

## Marketing hype risk

"Self-improving AI", "16 gateways", "closed learning loop" translate poorly to safety culture.

**Risk:** RU market copy emphasizes autonomy over gates.  
**Mitigation:** RU curriculum emphasizes **fail-closed**, not feature counts.

---

## Fork branding risk

RU fork rebrands for local market while inheriting upstream MIT and behavior.

**Risk:** Users think fork is officially supported/security-audited.  
**Mitigation:** Clear "research only" in our docs; no endorsement.
