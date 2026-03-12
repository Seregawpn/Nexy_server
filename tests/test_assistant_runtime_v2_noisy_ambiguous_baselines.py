from pathlib import Path
import sys
from unittest.mock import AsyncMock

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "tests"))

from goal_stack_gate_registry import CANONICAL_20_CASE_GATE, L2_CLARIFICATION_SLOT_FILL_20_CASE_GATE
from integrations.workflow_integrations.streaming_workflow_integration import (
    StreamingWorkflowIntegration,
)
from modules.text_processing.core.text_processor import TextProcessor


def _case(cases, case_id: str):
    for case in cases:
        if case.case_id == case_id:
            return case
    raise AssertionError(f"case not found: {case_id}")


NOISY_BASELINE_CASES = (
    _case(CANONICAL_20_CASE_GATE, "g17_dirty_messages_recoverable"),
    _case(CANONICAL_20_CASE_GATE, "g18_dirty_browser_recoverable"),
    _case(CANONICAL_20_CASE_GATE, "g19_dirty_search_recoverable"),
    _case(CANONICAL_20_CASE_GATE, "g20_dirty_describe_recoverable"),
    _case(L2_CLARIFICATION_SLOT_FILL_20_CASE_GATE, "l2_15_browser_followup_rain_sounds"),
    _case(L2_CLARIFICATION_SLOT_FILL_20_CASE_GATE, "l2_19_system_followup_safari_please"),
)


@pytest.mark.asyncio
@pytest.mark.parametrize("case", NOISY_BASELINE_CASES, ids=lambda c: c.case_id)
async def test_noisy_ambiguous_baseline_keeps_route_and_consistency(case):
    tp = TextProcessor(config={})
    classifier_category = case.classifier_expected_route or case.deterministic_expected_route or "none"
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": classifier_category})

    runtime_memory_context = None
    if case.classifier_runtime_current_goal or case.classifier_runtime_short_term:
        sections = []
        if case.classifier_runtime_current_goal:
            sections.append(f"Current goal:\n{case.classifier_runtime_current_goal}")
        if case.classifier_runtime_short_term:
            sections.append(f"Short-term memory:\n{case.classifier_runtime_short_term}")
        runtime_memory_context = "\n\n".join(sections)

    request_text = case.classifier_request or case.deterministic_request or case.live_request or ""
    prepared, _ = await tp._build_prompt_for_text(
        request_text,
        session_id=f"noisy-{case.case_id}",
        runtime_memory_context=runtime_memory_context,
        has_image=bool(getattr(case, "classifier_has_image", False)),
    )

    expected_route = case.classifier_expected_route or case.deterministic_expected_route
    assert prepared["route"] == expected_route

    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": case.live_expected_goal_state or "-",
            "current_goal": case.classifier_runtime_current_goal or case.deterministic_seed_goal or "",
            "route": expected_route or "none",
        }
    }
    command_payload = None
    if case.deterministic_expected_command:
        command_payload = {
            "payload": {
                "command": case.deterministic_expected_command,
                "args": case.deterministic_expected_args or {},
            }
        }

    result = StreamingWorkflowIntegration._compute_runtime_v2_consistency(
        request_data,
        command_payload=command_payload,
        text_response=case.deterministic_expected_text or "",
    )

    assert result["ok"] is True
    assert result["reason"] == "consistent"


def test_noisy_ambiguous_baseline_keeps_noise_profiles_explicit():
    noise_profiles = {case.noise_profile for case in NOISY_BASELINE_CASES}
    assert {"stt_like", "fragment"} <= noise_profiles


def test_noisy_ambiguous_baseline_keeps_recovery_shapes_explicit():
    slot_patterns = {case.slot_pattern for case in NOISY_BASELINE_CASES}
    assert "noisy_recovery" in slot_patterns
    assert "full_payload" in slot_patterns
