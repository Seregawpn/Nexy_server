from pathlib import Path
import sys
from unittest.mock import AsyncMock

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "tests"))

from goal_stack_gate_registry import CANONICAL_20_CASE_GATE
from integrations.workflow_integrations.streaming_workflow_integration import (
    StreamingWorkflowIntegration,
)
from modules.text_processing.core.text_processor import TextProcessor


def _case(case_id: str):
    for case in CANONICAL_20_CASE_GATE:
        if case.case_id == case_id:
            return case
    raise AssertionError(f"case not found: {case_id}")


MULTI_TURN_BASELINE_CASES = (
    _case("g01_messages_start"),           # clarification start -> set
    _case("g02_messages_followup_pronoun"),# follow-up slot fill -> clear
    _case("g08_search_followup_topic"),    # slot reuse -> clear
    _case("g12_cancel_old_task"),          # cancel -> clear with none route
    _case("g13_replace_message_to_app"),   # replace -> clear with new command
    _case("g14_replace_browser_to_message"), # replace -> set with new clarification
)


@pytest.mark.asyncio
@pytest.mark.parametrize("case", MULTI_TURN_BASELINE_CASES, ids=lambda c: c.case_id)
async def test_multi_turn_lifecycle_baseline_keeps_classifier_route_and_lifecycle_contract(case):
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
        session_id=f"baseline-{case.case_id}",
        runtime_memory_context=runtime_memory_context,
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


def test_multi_turn_lifecycle_baseline_keeps_transition_coverage_explicit():
    transitions = {case.transition_type for case in MULTI_TURN_BASELINE_CASES}
    assert {"new_task", "pronoun_continuation", "continuation_completion", "cancel", "replace"} <= transitions


def test_multi_turn_lifecycle_baseline_keeps_goal_state_coverage_explicit():
    goal_states = {case.live_expected_goal_state for case in MULTI_TURN_BASELINE_CASES}
    assert {"set", "clear"} <= goal_states
