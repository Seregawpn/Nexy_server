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
    "user_text,classifier_category,expected_route,command_name,args,text_response",
    [
        (
            "send hello to Sophia",
            "messages",
            "messages",
            "send_message",
            {"contact": "Sophia", "message": "hello"},
            "Sending your message to Sophia.",
        ),
        (
            "send hi to Mom on WhatsApp",
            "whatsapp",
            "whatsapp",
            "send_whatsapp_message",
            {"contact": "Mom", "message": "hi"},
            "Sending your WhatsApp message to Mom.",
        ),
        (
            "open Telegram",
            "system_control",
            "system_control",
            "open_app",
            {"app_name": "Telegram"},
            "Opening Telegram.",
        ),
        (
            "close Spotify",
            "system_control",
            "system_control",
            "close_app",
            {"app_name": "Spotify"},
            "Closing Spotify.",
        ),
        (
            "open YouTube and play jazz",
            "browser",
            "browser",
            "browser_use",
            {"task": "open youtube and play jazz"},
            "Opening YouTube and playing jazz.",
        ),
        (
            "buy subscription",
            "payment",
            "payment",
            "buy_subscription",
            {},
            "Opening the subscription purchase page.",
        ),
        (
            "manage my subscription",
            "payment",
            "payment",
            "manage_subscription",
            {},
            "Opening subscription management.",
        ),
    ],
)
async def test_single_turn_action_baseline_is_route_and_command_consistent(
    user_text: str,
    classifier_category: str,
    expected_route: str,
    command_name: str,
    args: dict,
    text_response: str,
):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": classifier_category})

    prepared, user_input = await tp._build_prompt_for_text(user_text)

    assert user_input == user_text
    assert prepared["route"] == expected_route

    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": "clear",
            "current_goal": "",
            "route": expected_route,
        }
    }
    result = StreamingWorkflowIntegration._compute_runtime_v2_consistency(
        request_data,
        command_payload={"payload": {"command": command_name, "args": args}},
        text_response=text_response,
    )

    assert result["ok"] is True
    assert result["reason"] == "consistent"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_text,classifier_category,expected_route",
    [
        ("send a message to Sophia", "messages", "messages"),
        ("message Mom on WhatsApp", "whatsapp", "whatsapp"),
        ("open Safari", "system_control", "system_control"),
        ("open YouTube and find lofi", "browser", "browser"),
        ("cancel my subscription", "payment", "payment"),
    ],
)
async def test_single_turn_action_baseline_keeps_executable_route_not_none(
    user_text: str,
    classifier_category: str,
    expected_route: str,
):
    tp = TextProcessor(config={})
    tp.live_provider.classify_intent_decision = AsyncMock(return_value={"category": classifier_category})

    prepared, _ = await tp._build_prompt_for_text(user_text)

    assert prepared["route"] == expected_route
    assert prepared["route"] != "none"
