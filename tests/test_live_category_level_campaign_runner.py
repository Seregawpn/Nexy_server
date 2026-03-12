from __future__ import annotations

from scripts.run_live_category_level_campaign import (
    CAMPAIGN_PRESETS,
    _infer_behavior,
    _normalize_goal_state,
)
from scripts.run_live_goal_stack_matrix import _extract_route


def test_live_category_level_campaign_runner_exposes_level1_30_preset() -> None:
    assert "level1_30" in CAMPAIGN_PRESETS
    assert len(CAMPAIGN_PRESETS["level1_30"]) == 30


def test_live_category_level_campaign_runner_exposes_level2_36_preset() -> None:
    assert "level2_36" in CAMPAIGN_PRESETS
    assert len(CAMPAIGN_PRESETS["level2_36"]) == 36


def test_live_category_level_campaign_runner_infers_execute_behavior_from_command() -> None:
    assert _infer_behavior(command="send_message", goal_state="clear", text="Sending now.") == "execute"


def test_live_category_level_campaign_runner_infers_clarify_behavior_from_active_goal_state() -> None:
    assert _infer_behavior(command=None, goal_state="set", text="What would you like to send?") == "clarify"


def test_live_category_level_campaign_runner_normalizes_terminal_goal_state() -> None:
    assert _normalize_goal_state(expected_state="clear", actual_state="empty", actual_goal="") == "clear"


def test_live_category_level_campaign_runner_uses_final_runtime_route_when_present() -> None:
    items = [
        {"success": True, "route": "capability"},
        {"success": True, "is_final": True, "resolved_route": "messages"},
    ]

    assert _extract_route(items) == "messages"


def test_live_category_level_campaign_runner_prefers_resolved_route_from_final_result() -> None:
    items = [
        {"success": True, "text_response": "Yes, I can."},
        {"success": True, "is_final": True, "resolved_route": "capability"},
    ]

    assert _extract_route(items) == "capability"
