from pathlib import Path
import sys


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.bridge_live_goal_stack_to_category_results import build_observed_rows


def test_goal_stack_bridge_maps_supported_cases_into_category_observed_rows():
    summary = {
        "suites": [
            {
                "name": "full_cycle",
                "results": [
                    {
                        "id": "g01_messages_start",
                        "route_observed": "messages",
                        "goal_state": "set",
                        "actual_command": None,
                    },
                    {
                        "id": "g02_messages_followup_pronoun",
                        "route_observed": "messages",
                        "goal_state": "clear",
                        "actual_command": "send_message",
                    },
                    {
                        "id": "g05_browser_direct",
                        "route_observed": "browser",
                        "goal_state": "clear",
                        "current_goal": "",
                        "actual_command": "browser_use",
                    },
                    {
                        "id": "g20_dirty_describe_recoverable",
                        "route_observed": "describe",
                        "goal_state": "empty",
                        "current_goal": "",
                        "actual_command": None,
                    },
                ],
            }
        ]
    }

    rows = build_observed_rows(summary)

    assert rows == [
        {
            "case_id": "messages_l2_01",
            "source_case_id": "g01_messages_start",
            "observed_route": "messages",
            "observed_goal_state": "set",
            "observed_behavior": "clarify",
            "observed_command": None,
        },
        {
            "case_id": "messages_l3_01",
            "source_case_id": "g02_messages_followup_pronoun",
            "observed_route": "messages",
            "observed_goal_state": "clear",
            "observed_behavior": "continue_execute",
            "observed_command": "send_message",
        },
        {
            "case_id": "browser_l1_01",
            "source_case_id": "g05_browser_direct",
            "observed_route": "browser",
            "observed_goal_state": "empty",
            "observed_behavior": "execute",
            "observed_command": "browser_use",
        },
        {
            "case_id": "describe_l1_01",
            "source_case_id": "g20_dirty_describe_recoverable",
            "observed_route": "describe",
            "observed_goal_state": "empty",
            "observed_behavior": "answer",
            "observed_command": None,
        },
    ]


def test_goal_stack_bridge_maps_newly_supported_direct_browser_case():
    summary = {
        "suites": [
            {
                "name": "full_cycle",
                "results": [
                    {
                        "id": "g05_browser_direct",
                        "route_observed": "browser",
                        "goal_state": "clear",
                        "actual_command": "browser_use",
                    }
                ],
            }
        ]
    }

    assert build_observed_rows(summary) == [
        {
            "case_id": "browser_l1_01",
            "source_case_id": "g05_browser_direct",
            "observed_route": "browser",
            "observed_goal_state": "empty",
            "observed_behavior": "execute",
            "observed_command": "browser_use",
        }
    ]


def test_goal_stack_bridge_still_skips_cases_without_mapping():
    summary = {
        "suites": [
            {
                "name": "full_cycle",
                "results": [
                    {
                        "id": "g13_replace_message_to_app",
                        "route_observed": "system_control",
                        "goal_state": "clear",
                        "current_goal": "",
                        "actual_command": "open_app",
                    }
                ],
            }
        ]
    }

    assert build_observed_rows(summary) == []


def test_goal_stack_bridge_maps_safe_replace_to_message_clarification_case():
    summary = {
        "suites": [
            {
                "name": "full_cycle",
                "results": [
                    {
                        "id": "g14_replace_browser_to_message",
                        "route_observed": "messages",
                        "goal_state": "set",
                        "current_goal": "User wants to send a message to Sophia. Missing detail: message text.",
                        "actual_command": None,
                    }
                ],
            }
        ]
    }

    assert build_observed_rows(summary) == [
        {
            "case_id": "messages_l2_02",
            "source_case_id": "g14_replace_browser_to_message",
            "observed_route": "messages",
            "observed_goal_state": "set",
            "observed_behavior": "clarify",
            "observed_command": None,
        }
    ]


def test_goal_stack_bridge_normalizes_terminal_clear_empty_for_direct_completion_cases():
    summary = {
        "suites": [
            {
                "name": "full_cycle",
                "results": [
                    {
                        "id": "g09_system_direct",
                        "route_observed": "system_control",
                        "goal_state": "clear",
                        "current_goal": "",
                        "actual_command": "open_app",
                    },
                    {
                        "id": "g19_dirty_search_recoverable",
                        "route_observed": "google_search",
                        "goal_state": "clear",
                        "current_goal": "",
                        "actual_command": None,
                    },
                ],
            }
        ]
    }

    rows = build_observed_rows(summary)

    assert rows == [
        {
            "case_id": "system_control_l1_01",
            "source_case_id": "g09_system_direct",
            "observed_route": "system_control",
            "observed_goal_state": "empty",
            "observed_behavior": "execute",
            "observed_command": "open_app",
        },
        {
            "case_id": "google_search_l4_01",
            "source_case_id": "g19_dirty_search_recoverable",
            "observed_route": "google_search",
            "observed_goal_state": "empty",
            "observed_behavior": "answer",
            "observed_command": None,
        },
    ]
