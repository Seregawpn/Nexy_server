from pathlib import Path
import sys
from unittest.mock import AsyncMock

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.workflow_integrations.streaming_workflow_integration import (
    StreamingWorkflowIntegration,
)
from modules.text_processing.core.text_processor import TextProcessor


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_text,classifier_category,expected_route",
    [
        ("Привет", "none", "none"),
        ("Как дела?", "none", "none"),
        ("Спасибо", "none", "none"),
        ("Расскажи шутку", "none", "none"),
        ("Что ты умеешь?", "capability", "capability"),
        ("Чем ты можешь помочь?", "capability", "capability"),
    ],
)
async def test_simple_conversation_and_capability_baseline(
    user_text: str,
    classifier_category: str,
    expected_route: str,
):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": classifier_category})

    prepared, user_input = await tp._build_prompt_for_text(user_text)

    assert user_input == user_text
    assert prepared["route"] == expected_route

    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": "empty",
            "current_goal": "",
            "route": expected_route,
        }
    }
    result = StreamingWorkflowIntegration._compute_runtime_v2_consistency(
        request_data,
        command_payload=None,
        text_response="plain response",
    )
    assert result["ok"] is True
    assert result["reason"] == "consistent"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_text",
    [
        "Что на экране?",
        "Опиши экран",
        "Что ты видишь?",
        "Опиши, что открыто",
    ],
)
async def test_screen_description_baseline(user_text: str):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": "describe"})

    prepared, _ = await tp._build_prompt_for_text(user_text)

    assert prepared["route"] == "describe"
    assert prepared["describe"] is True

    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": "empty",
            "current_goal": "",
            "route": "describe",
        }
    }
    result = StreamingWorkflowIntegration._compute_runtime_v2_consistency(
        request_data,
        command_payload=None,
        text_response="I can see a browser window.",
    )
    assert result["ok"] is True
    assert result["reason"] == "consistent"
