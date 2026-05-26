#!/usr/bin/env python3
"""Review Assistant thin demo — v0.2 mock LLM + Phase 3.3 real provider boundary.

Flow: task → [mock LLM | real provider] → draft → verification → approval → deliver.

Mock LLM is default. Real local OpenAI-compatible endpoint only with --real-provider.
Stdlib only. Synthetic prompts only for real provider. No secrets in trace.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

PROVIDER_TIMEOUT_SECONDS = 30
PROVIDER_MAX_OUTPUT_CHARS = 8000

SYNTHETIC_REAL_PROVIDER_TASK = (
    "Write a short neutral draft explaining that a document has been "
    "reviewed and requires human approval before sending."
)

UNSAFE_PROVIDER_PATTERNS = (
    "rm -rf",
    "delete all production",
    "execute:",
    "run shell",
    "bypass approval",
    "already approved",
    "ignore previous instructions",
)

UNCERTAIN_PROVIDER_PATTERNS = (
    "cannot verify",
    "unverified claim",
    "uncertain",
    "cannot confirm",
)


class CritiqueResult(str, Enum):
    OK = "OK"
    UNCERTAIN = "UNCERTAIN"
    BAD_DRAFT = "BAD_DRAFT"


class ApprovalMode(str, Enum):
    GRANTED = "granted"
    DENIED = "denied"
    MISSING = "missing"
    TIMEOUT = "timeout"


class FinalDecision(str, Enum):
    DELIVERED = "DELIVERED"
    BLOCKED = "BLOCKED"
    ESCALATED = "ESCALATED"
    FAILED = "FAILED"


DELIVER_SCENARIOS = frozenset({"happy", "llm_valid_draft", "real_provider_synthetic"})


@dataclass
class TraceEvent:
    name: str
    detail: dict[str, Any] = field(default_factory=dict)

    def format_line(self) -> str:
        if not self.detail:
            return f"- {self.name}"
        parts = ", ".join(f"{k}={v}" for k, v in self.detail.items())
        return f"- {self.name}: {parts}"


@dataclass
class ReviewScenario:
    name: str
    task: str
    critique: CritiqueResult
    approval: ApprovalMode
    bypass_attempt: bool = False
    uses_llm: bool = False
    uses_real_provider: bool = False


@dataclass
class MockLLMResponse:
    status: str
    draft: str
    critique: str
    uncertain: bool = False
    unsafe: bool = False


@dataclass
class ProviderRequest:
    model: str
    messages: list[dict[str, str]]
    temperature: float = 0.2
    max_tokens: int = 300


@dataclass
class ProviderResult:
    draft: str
    raw_length: int


@dataclass
class ProviderError:
    code: str
    message: str = ""


@dataclass
class ReviewResult:
    scenario: str
    draft_id: str
    draft_text: str
    critique: CritiqueResult
    verification_passed: bool
    verification_reason: str
    approval_status: str
    final_decision: FinalDecision
    delivered: bool
    trace: list[TraceEvent] = field(default_factory=list)

    def add(self, name: str, **detail: Any) -> None:
        self.trace.append(TraceEvent(name, detail))


SCENARIOS: dict[str, ReviewScenario] = {
    "happy": ReviewScenario(
        name="happy",
        task="Summarize Q1 metrics for external blog post",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
    ),
    "missing_approval": ReviewScenario(
        name="missing_approval",
        task="Draft report for operator review",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.TIMEOUT,
    ),
    "critic_uncertain": ReviewScenario(
        name="critic_uncertain",
        task="Report includes unverified revenue figures",
        critique=CritiqueResult.UNCERTAIN,
        approval=ApprovalMode.MISSING,
    ),
    "bad_draft": ReviewScenario(
        name="bad_draft",
        task="Produce empty invalid draft",
        critique=CritiqueResult.BAD_DRAFT,
        approval=ApprovalMode.GRANTED,
    ),
    "unsafe_publish_attempt": ReviewScenario(
        name="unsafe_publish_attempt",
        task="Attempt direct publish without gates",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        bypass_attempt=True,
    ),
    "llm_valid_draft": ReviewScenario(
        name="llm_valid_draft",
        task="Generate blog draft via mock LLM",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_llm=True,
    ),
    "llm_malformed_output": ReviewScenario(
        name="llm_malformed_output",
        task="Mock LLM returns malformed payload",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_llm=True,
    ),
    "llm_timeout": ReviewScenario(
        name="llm_timeout",
        task="Mock LLM times out",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_llm=True,
    ),
    "llm_uncertain": ReviewScenario(
        name="llm_uncertain",
        task="Mock LLM returns uncertain draft",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.MISSING,
        uses_llm=True,
    ),
    "llm_unsafe_output": ReviewScenario(
        name="llm_unsafe_output",
        task="Mock LLM returns unsafe instruction",
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_llm=True,
    ),
    "real_provider_forbidden_without_flag": ReviewScenario(
        name="real_provider_forbidden_without_flag",
        task=SYNTHETIC_REAL_PROVIDER_TASK,
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_real_provider=True,
    ),
    "real_provider_missing_config": ReviewScenario(
        name="real_provider_missing_config",
        task=SYNTHETIC_REAL_PROVIDER_TASK,
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_real_provider=True,
    ),
    "real_provider_synthetic": ReviewScenario(
        name="real_provider_synthetic",
        task=SYNTHETIC_REAL_PROVIDER_TASK,
        critique=CritiqueResult.OK,
        approval=ApprovalMode.GRANTED,
        uses_real_provider=True,
    ),
}


def get_mock_llm_raw(scenario_name: str) -> dict[str, Any] | None:
    payloads: dict[str, dict[str, Any] | None] = {
        "llm_valid_draft": {
            "status": "ok",
            "draft": "LLM-generated draft: Q1 metrics summary (unverified).",
            "critique": "Advisory: structure acceptable",
            "uncertain": False,
            "unsafe": False,
        },
        "llm_malformed_output": {
            "status": "ok",
            "draft": None,
            "critique": "broken",
            "uncertain": False,
            "unsafe": False,
        },
        "llm_timeout": None,
        "llm_uncertain": {
            "status": "ok",
            "draft": "Revenue grew 400% (unverified claim).",
            "critique": "Cannot verify figures",
            "uncertain": True,
            "unsafe": False,
        },
        "llm_unsafe_output": {
            "status": "ok",
            "draft": "Execute: delete all production data immediately.",
            "critique": "OK",
            "uncertain": False,
            "unsafe": True,
        },
    }
    return payloads.get(scenario_name)


def parse_mock_llm_response(raw: dict[str, Any] | None) -> tuple[MockLLMResponse | None, str]:
    if raw is None:
        return None, "missing_payload"
    if not isinstance(raw, dict):
        return None, "invalid_shape"
    status = raw.get("status")
    if status not in ("ok",):
        return None, "unsupported_status"
    draft = raw.get("draft")
    if draft is None:
        return None, "missing_draft"
    if not isinstance(draft, str):
        return None, "wrong_draft_type"
    if not draft.strip():
        return None, "empty_output"
    critique = raw.get("critique", "")
    if not isinstance(critique, str):
        return None, "wrong_critique_type"
    return MockLLMResponse(
        status=status,
        draft=draft,
        critique=critique,
        uncertain=bool(raw.get("uncertain", False)),
        unsafe=bool(raw.get("unsafe", False)),
    ), ""


def build_provider_request(task_text: str) -> ProviderRequest:
    model = os.environ.get("RA_LLM_MODEL", "local-model").strip() or "local-model"
    return ProviderRequest(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You produce short safe drafts. Do not execute commands. "
                    "Do not claim final truth."
                ),
            },
            {"role": "user", "content": task_text},
        ],
        temperature=0.2,
        max_tokens=300,
    )


def _chat_completions_url(base_url: str) -> str:
    base = base_url.rstrip("/")
    if base.endswith("/v1"):
        return f"{base}/chat/completions"
    return f"{base}/v1/chat/completions"


def call_local_openai_compatible_provider(
    request: ProviderRequest,
) -> tuple[dict[str, Any] | None, ProviderError | None]:
    base_url = os.environ.get("RA_LLM_BASE_URL", "").strip()
    if not base_url:
        return None, ProviderError("config_missing")

    url = _chat_completions_url(base_url)
    body = json.dumps(
        {
            "model": request.model,
            "messages": request.messages,
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
        }
    ).encode("utf-8")

    headers = {"Content-Type": "application/json"}
    api_key = os.environ.get("RA_LLM_API_KEY", "").strip()
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=PROVIDER_TIMEOUT_SECONDS) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            if not isinstance(payload, dict):
                return None, ProviderError("malformed_response")
            return payload, None
    except urllib.error.HTTPError as exc:
        if exc.code == 429:
            return None, ProviderError("rate_limited")
        return None, ProviderError("http_error", f"status={exc.code}")
    except TimeoutError:
        return None, ProviderError("timeout")
    except urllib.error.URLError as exc:
        reason = str(exc.reason).lower()
        if "timed out" in reason or "timeout" in reason:
            return None, ProviderError("timeout")
        return None, ProviderError("network_error")
    except json.JSONDecodeError:
        return None, ProviderError("malformed_response")


def _content_unsafe(text: str) -> bool:
    lower = text.lower()
    return any(p in lower for p in UNSAFE_PROVIDER_PATTERNS)


def _content_uncertain(text: str) -> bool:
    lower = text.lower()
    return any(p in lower for p in UNCERTAIN_PROVIDER_PATTERNS)


def parse_provider_response(payload: dict[str, Any]) -> tuple[ProviderResult | None, ProviderError | None]:
    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices:
        return None, ProviderError("missing_choices")

    first = choices[0]
    if not isinstance(first, dict):
        return None, ProviderError("invalid_choice")

    message = first.get("message")
    if not isinstance(message, dict):
        return None, ProviderError("missing_message")

    content = message.get("content")
    if content is None:
        return None, ProviderError("missing_content")
    if not isinstance(content, str):
        return None, ProviderError("wrong_content_type")
    if not content.strip():
        return None, ProviderError("empty_output")
    if len(content) > PROVIDER_MAX_OUTPUT_CHARS:
        return None, ProviderError("output_too_large")

    return ProviderResult(draft=content.strip(), raw_length=len(content)), None


def run_mock_llm_boundary(scenario: ReviewScenario, result: ReviewResult) -> bool:
    result.add("llm_request_started", mode="mock", scenario=scenario.name)

    if scenario.name == "llm_timeout":
        result.add("llm_timeout", policy="fail_closed")
        result.add("escalation_triggered", reason="llm_timeout")
        result.final_decision = FinalDecision.ESCALATED
        result.add(
            "task_failed",
            decision=FinalDecision.ESCALATED.value,
            reason="llm_timeout",
        )
        return False

    raw = get_mock_llm_raw(scenario.name)
    result.add("llm_response_received", mode="mock")

    parsed, fail_reason = parse_mock_llm_response(raw)
    if parsed is None:
        result.add("llm_parse_failed", reason=fail_reason)
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="llm_parse_failed",
        )
        return False

    if parsed.unsafe:
        result.add("llm_unsafe_output", reason="policy_block")
        result.add("unsafe_action_blocked", reason="llm_unsafe_content")
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="llm_unsafe_output",
        )
        return False

    if parsed.uncertain:
        result.add("llm_uncertain", reason="unverified_claims")
        result.add("escalation_triggered", reason="llm_uncertain")
        result.final_decision = FinalDecision.ESCALATED
        result.add(
            "task_failed",
            decision=FinalDecision.ESCALATED.value,
            reason="llm_uncertain",
        )
        return False

    result.add("llm_parse_passed", format="plain")
    result.draft_text = parsed.draft
    result.draft_id = f"llm-draft-{scenario.name[:8]}"
    result.add("draft_created", draft_id=result.draft_id, source="llm_unverified")
    result.add(
        "critique_completed",
        result=CritiqueResult.OK.value,
        advisory=True,
        note=parsed.critique[:40],
    )
    return True


def run_real_provider_boundary(
    scenario: ReviewScenario,
    result: ReviewResult,
    real_provider_enabled: bool,
) -> bool:
    result.add("provider_request_prepared", mode="real", synthetic=True)

    if not real_provider_enabled:
        result.add("provider_disabled", reason="real_provider_flag_required")
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="provider_disabled",
        )
        return False

    base_url = os.environ.get("RA_LLM_BASE_URL", "").strip()
    if not base_url or scenario.name == "real_provider_missing_config":
        result.add("provider_config_missing", var="RA_LLM_BASE_URL")
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="provider_config_missing",
        )
        return False

    task_text = SYNTHETIC_REAL_PROVIDER_TASK
    request = build_provider_request(task_text)
    result.add("provider_request_started", mode="real")

    raw_payload, provider_err = call_local_openai_compatible_provider(request)
    if provider_err is not None:
        code = provider_err.code
        if code == "timeout":
            result.add("provider_timeout", policy="fail_closed")
            result.add("escalation_triggered", reason="provider_timeout")
            result.final_decision = FinalDecision.ESCALATED
            result.add(
                "task_failed",
                decision=FinalDecision.ESCALATED.value,
                reason="provider_timeout",
            )
        elif code == "rate_limited":
            result.add("provider_rate_limited")
            result.add("provider_error", reason=code)
            result.final_decision = FinalDecision.FAILED
            result.add(
                "task_failed",
                decision=FinalDecision.FAILED.value,
                reason="provider_rate_limited",
            )
        else:
            result.add("provider_error", reason=code)
            result.final_decision = FinalDecision.FAILED
            result.add(
                "task_failed",
                decision=FinalDecision.FAILED.value,
                reason="provider_error",
            )
        return False

    result.add("provider_response_received", mode="real")

    parsed, parse_err = parse_provider_response(raw_payload or {})
    if parse_err is not None:
        result.add("provider_parse_failed", reason=parse_err.code)
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="provider_parse_failed",
        )
        return False

    if _content_unsafe(parsed.draft):
        result.add("provider_unsafe_output", reason="policy_block")
        result.add("unsafe_action_blocked", reason="provider_unsafe_content")
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="provider_unsafe_output",
        )
        return False

    if _content_uncertain(parsed.draft):
        result.add("provider_uncertain_output", reason="unverified_claims")
        result.add("escalation_triggered", reason="provider_uncertain")
        result.final_decision = FinalDecision.ESCALATED
        result.add(
            "task_failed",
            decision=FinalDecision.ESCALATED.value,
            reason="provider_uncertain",
        )
        return False

    result.add("provider_parse_passed", format="openai_chat")
    result.draft_text = parsed.draft
    result.draft_id = f"provider-draft-{scenario.name[:8]}"
    result.add("draft_created", draft_id=result.draft_id, source="provider_unverified")
    result.add(
        "critique_completed",
        result=CritiqueResult.OK.value,
        advisory=True,
        note="provider_output_unverified",
    )
    return True


def run_verification(
    draft_text: str, critique: CritiqueResult
) -> tuple[bool, str]:
    if not draft_text.strip():
        return False, "draft_empty"
    if critique == CritiqueResult.BAD_DRAFT:
        return False, "critique_flagged_bad_draft"
    if len(draft_text) < 10:
        return False, "draft_too_short"
    if critique == CritiqueResult.UNCERTAIN:
        return True, "basic_safety_with_caution"
    return True, "basic_safety"


def apply_approval(
    scenario: ReviewScenario, verification_passed: bool
) -> tuple[str, bool]:
    if not verification_passed:
        return "skipped_verification_failed", False

    mode = scenario.approval
    if mode == ApprovalMode.GRANTED:
        return "granted", True
    if mode == ApprovalMode.DENIED:
        return "denied", False
    if mode == ApprovalMode.TIMEOUT:
        return "timeout", False
    return "missing", False


def finish_approval_gate(scenario: ReviewScenario, result: ReviewResult) -> ReviewResult:
    result.add("approval_requested", mode="mock")
    approval_status, approved = apply_approval(scenario, result.verification_passed)
    result.approval_status = approval_status

    if approved:
        result.add("approval_granted", source="scenario")
    elif approval_status == "denied":
        result.add("approval_denied", source="scenario")
    elif approval_status == "timeout":
        result.add("approval_timeout", policy="deny_by_default")
    else:
        result.add("approval_denied", reason="approval_missing")

    if result.critique == CritiqueResult.UNCERTAIN and not approved:
        result.final_decision = FinalDecision.ESCALATED
        result.add(
            "task_failed",
            decision=FinalDecision.ESCALATED.value,
            reason="no_delivery_without_approval_after_uncertainty",
        )
        return result

    if not approved:
        result.final_decision = FinalDecision.BLOCKED
        result.add(
            "task_failed",
            decision=FinalDecision.BLOCKED.value,
            reason=f"approval_{approval_status}",
        )
        return result

    result.delivered = True
    result.final_decision = FinalDecision.DELIVERED
    result.add("task_completed", decision=FinalDecision.DELIVERED.value)
    return result


def run_pipeline(scenario: ReviewScenario, real_provider_enabled: bool = False) -> ReviewResult:
    result = ReviewResult(
        scenario=scenario.name,
        draft_id="",
        draft_text="",
        critique=scenario.critique,
        verification_passed=False,
        verification_reason="",
        approval_status="pending",
        final_decision=FinalDecision.FAILED,
        delivered=False,
    )

    result.add("task_started", scenario=scenario.name, task=scenario.task)

    if scenario.bypass_attempt:
        result.add("unsafe_action_blocked", reason="bypass_not_allowed")
        result.final_decision = FinalDecision.FAILED
        result.add("task_failed", decision=FinalDecision.FAILED.value, reason="unsafe_publish_attempt")
        return result

    if scenario.uses_real_provider:
        if not run_real_provider_boundary(scenario, result, real_provider_enabled):
            return result
        critique = CritiqueResult.OK
        result.critique = critique
    elif scenario.uses_llm:
        if not run_mock_llm_boundary(scenario, result):
            return result
        critique = CritiqueResult.OK
        result.critique = critique
    else:
        draft_id = f"local-draft-{scenario.name[:3]}"
        draft_text = "" if scenario.name == "bad_draft" else f"Draft for task: {scenario.task}"
        result.draft_id = draft_id
        result.draft_text = draft_text
        result.add("draft_created", draft_id=draft_id)
        critique = scenario.critique
        result.critique = critique
        result.add("critique_completed", result=critique.value, advisory=True)
        if critique == CritiqueResult.UNCERTAIN:
            result.add("escalation_triggered", reason="critic_uncertain")

    verification_passed, verification_reason = run_verification(result.draft_text, result.critique)
    result.verification_passed = verification_passed
    result.verification_reason = verification_reason

    if verification_passed:
        result.add("verification_passed", checks=verification_reason)
    else:
        result.add("verification_failed", reason=verification_reason)
        result.final_decision = FinalDecision.FAILED
        result.add(
            "task_failed",
            decision=FinalDecision.FAILED.value,
            reason="verification_failed",
        )
        return result

    return finish_approval_gate(scenario, result)


def print_trace(result: ReviewResult) -> None:
    print("TRACE")
    for event in result.trace:
        print(event.format_line())
    print(f"\nFINAL decision={result.final_decision.value} delivered={result.delivered}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Review Assistant thin demo (mock default + optional real provider)"
    )
    parser.add_argument(
        "--scenario",
        default="happy",
        choices=sorted(SCENARIOS.keys()),
        help="Scenario to run",
    )
    parser.add_argument(
        "--real-provider",
        action="store_true",
        help="Enable real local OpenAI-compatible provider (opt-in; requires RA_LLM_BASE_URL)",
    )
    args = parser.parse_args()

    scenario = SCENARIOS[args.scenario]
    print("=== Review Assistant Thin (prototypes-derived) ===")
    if args.real_provider:
        print("Mode: real provider enabled (local OpenAI-compatible endpoint)")
    else:
        print("Mode: mock/default (no real provider network)")
    print("Principle: provider/LLM output != truth; human approval mandatory\n")

    result = run_pipeline(scenario, real_provider_enabled=args.real_provider)
    print_trace(result)

    if args.scenario in DELIVER_SCENARIOS:
        return 0 if result.delivered else 1
    return 0 if not result.delivered else 1


if __name__ == "__main__":
    sys.exit(main())
