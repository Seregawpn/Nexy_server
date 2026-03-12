from pathlib import Path
import sys
from unittest.mock import AsyncMock

import pytest

project_root = Path(__file__).parent.parent
tests_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(tests_root))

from modules.text_processing.core.text_processor import TextProcessor
from goal_stack_gate_registry import (
    CANONICAL_20_CASE_GATE,
    L1_BASIC_DIRECT_20_CASE_GATE,
    L1_DIRECT_CONFIDENCE_PROBES,
    L2_CLARIFICATION_SLOT_FILL_20_CASE_GATE,
    SUPPLEMENTAL_20_CASE_GATE,
)


def _runtime_memory(current_goal: str = "", short_term: str = "") -> str:
    parts = []
    if current_goal:
        parts.append(f"Current goal:\n{current_goal}")
    if short_term:
        parts.append(
            "Short-term memory:\n"
            "Current/recent dialogue turns (USER/ASSISTANT order).\n"
            f"{short_term}"
        )
    parts.append("Medium-term memory:\nNo data")
    return "\n\n".join(parts)


CLASSIFIER_BASIC_CASES = [
    case for case in CANONICAL_20_CASE_GATE if case.classifier_request is not None
]

SUPPLEMENTAL_CLASSIFIER_CASES = [
    case for case in SUPPLEMENTAL_20_CASE_GATE if case.classifier_request is not None
]

L1_CLASSIFIER_CASES = [
    case for case in L1_BASIC_DIRECT_20_CASE_GATE if case.classifier_request is not None
]
L1_CONFIDENCE_CLASSIFIER_CASES = [
    case for case in L1_DIRECT_CONFIDENCE_PROBES if case.classifier_request is not None
]
L2_CLASSIFIER_CASES = [
    case for case in L2_CLARIFICATION_SLOT_FILL_20_CASE_GATE if case.classifier_request is not None
]


@pytest.mark.asyncio
@pytest.mark.parametrize("case", CLASSIFIER_BASIC_CASES, ids=[case.case_id for case in CLASSIFIER_BASIC_CASES])
async def test_classifier_basic_matrix(case):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(
        return_value={"category": case.classifier_expected_route}
    )

    runtime_memory_context = None
    if case.classifier_runtime_current_goal or case.classifier_runtime_short_term:
        runtime_memory_context = _runtime_memory(
            current_goal=case.classifier_runtime_current_goal or "",
            short_term=case.classifier_runtime_short_term or "",
        )

    route_flags, _ = await tp._build_prompt_for_text(
        case.classifier_request or "",
        session_id=f"classifier-matrix-{case.case_id}",
        runtime_memory_context=runtime_memory_context,
        has_image=case.classifier_has_image,
    )

    assert route_flags["route"] == case.classifier_expected_route

    if case.classifier_has_image:
        tp.live_provider.classify_intent_decision.assert_not_awaited()
        return

    tp.live_provider.classify_intent_decision.assert_awaited_once()
    call = tp.live_provider.classify_intent_decision.await_args_list[0]
    classifier_context = call.kwargs["classifier_context"]

    if case.classifier_runtime_current_goal:
        assert "current_goal" in classifier_context
        assert classifier_context["current_goal"]
    else:
        assert "current_goal" not in classifier_context

    if case.classifier_runtime_short_term:
        assert "short_term_memory" in classifier_context
        assert classifier_context["short_term_memory"]
    else:
        assert "short_term_memory" not in classifier_context


@pytest.mark.asyncio
@pytest.mark.parametrize("case", SUPPLEMENTAL_CLASSIFIER_CASES, ids=[case.case_id for case in SUPPLEMENTAL_CLASSIFIER_CASES])
async def test_classifier_additional_matrix(case):
    await test_classifier_basic_matrix(case)


@pytest.mark.asyncio
@pytest.mark.parametrize("case", L1_CLASSIFIER_CASES, ids=[case.case_id for case in L1_CLASSIFIER_CASES])
async def test_classifier_l1_basic_direct_campaign(case):
    await test_classifier_basic_matrix(case)


@pytest.mark.asyncio
@pytest.mark.parametrize("case", L1_CONFIDENCE_CLASSIFIER_CASES, ids=[case.case_id for case in L1_CONFIDENCE_CLASSIFIER_CASES])
async def test_classifier_l1_direct_confidence_probes(case):
    await test_classifier_basic_matrix(case)


@pytest.mark.asyncio
@pytest.mark.parametrize("case", L2_CLASSIFIER_CASES, ids=[case.case_id for case in L2_CLASSIFIER_CASES])
async def test_classifier_l2_clarification_slot_fill_campaign(case):
    await test_classifier_basic_matrix(case)
