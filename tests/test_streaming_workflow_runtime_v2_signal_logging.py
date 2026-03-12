from pathlib import Path
import sys
from unittest.mock import patch

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration


def test_runtime_v2_signal_annotation_keeps_request_scoped_contract():
    request_data = {}

    StreamingWorkflowIntegration._annotate_runtime_v2_signals(
        request_data,
        memory_context={
            "goal_state_context": "keep",
            "current_goal_context": "User wants to send a message to Sophia. Missing detail: message text.",
        },
        route="messages",
    )

    assert request_data["_assistant_runtime_v2_signals"] == {
        "goal_state": "keep",
        "current_goal": "User wants to send a message to Sophia. Missing detail: message text.",
        "route": "messages",
    }


def test_runtime_v2_signal_annotation_does_not_overwrite_existing_route_owner():
    request_data = {
        "_assistant_runtime_v2_signals": {
            "route": "capability",
        }
    }

    StreamingWorkflowIntegration._annotate_runtime_v2_signals(
        request_data,
        route="messages",
    )

    assert request_data["_assistant_runtime_v2_signals"]["route"] == "capability"


def test_runtime_v2_signal_logging_uses_canonical_lifecycle_mapping():
    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": "clear",
            "current_goal": "",
            "route": "messages",
        }
    }

    with patch(
        "integrations.workflow_integrations.streaming_workflow_integration._log_request_path_workflow"
    ) as mock_log:
        StreamingWorkflowIntegration._log_runtime_v2_signal_snapshot(
            "sid-1",
            request_data,
            phase="final",
        )

    mock_log.assert_called_once_with(
        "workflow.v2_signals",
        "sid-1",
        phase="final",
        route="messages",
        goal_state="clear",
        lifecycle="task_closed",
        has_goal=False,
    )


def test_runtime_v2_signal_logging_keeps_unknown_state_safe():
    assert StreamingWorkflowIntegration._derive_runtime_v2_lifecycle_event("weird") == "task_unknown"


def test_runtime_v2_consistency_reports_route_command_mismatch():
    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": "clear",
            "current_goal": "",
            "route": "messages",
        }
    }

    result = StreamingWorkflowIntegration._compute_runtime_v2_consistency(
        request_data,
        command_payload={"payload": {"command": "open_app", "args": {"app_name": "Safari"}}},
        text_response="Opening Safari.",
    )

    assert result["ok"] is False
    assert result["reason"] == "route_command_mismatch"


def test_runtime_v2_consistency_allows_preturn_set_goal_state_with_completed_command():
    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": "set",
            "current_goal": "User wants to send a message to Sophia. Missing detail: message text.",
            "route": "messages",
        }
    }

    result = StreamingWorkflowIntegration._compute_runtime_v2_consistency(
        request_data,
        command_payload={"payload": {"command": "send_message", "args": {"contact": "Sophia", "message": "Hi"}}},
        text_response="Sending your message to Sophia.",
    )

    assert result["ok"] is True
    assert result["reason"] == "consistent"


def test_runtime_v2_consistency_allows_empty_goal_state_with_preturn_current_goal():
    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": "empty",
            "current_goal": "User wants news. Missing detail: topic.",
            "route": "google_search",
        }
    }

    result = StreamingWorkflowIntegration._compute_runtime_v2_consistency(
        request_data,
        command_payload=None,
        text_response="Here are the latest world headlines.",
    )

    assert result["ok"] is True
    assert result["reason"] == "consistent"


def test_runtime_v2_consistency_reports_clear_goal_state_with_clarification_text():
    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": "clear",
            "current_goal": "",
            "route": "messages",
        }
    }

    result = StreamingWorkflowIntegration._compute_runtime_v2_consistency(
        request_data,
        command_payload=None,
        text_response="What message would you like to send to Sophia?",
    )

    assert result["ok"] is False
    assert result["reason"] == "clear_goal_state_with_clarification_text"


def test_runtime_v2_consistency_reports_consistent_case():
    request_data = {
        "_assistant_runtime_v2_signals": {
            "goal_state": "clear",
            "current_goal": "",
            "route": "messages",
        }
    }

    result = StreamingWorkflowIntegration._compute_runtime_v2_consistency(
        request_data,
        command_payload={"payload": {"command": "send_message", "args": {"contact": "Sophia", "message": "Hi"}}},
        text_response="Sending your message to Sophia.",
    )

    assert result["ok"] is True
    assert result["reason"] == "consistent"


def test_request_timing_annotation_and_logging_keep_request_scoped_contract():
    request_data = {}

    StreamingWorkflowIntegration._annotate_request_timing(
        request_data,
        stage="memory_done",
        started_at=10.0,
        now=10.025,
        absolute_ms=12.5,
    )
    StreamingWorkflowIntegration._annotate_request_timing(
        request_data,
        stage="final_flush_done",
        started_at=10.0,
        now=10.075,
    )
    StreamingWorkflowIntegration._annotate_request_timing(
        request_data,
        stage="parse_done",
        started_at=10.0,
        now=10.090,
    )
    StreamingWorkflowIntegration._annotate_request_timing(
        request_data,
        stage="command_done",
        started_at=10.0,
        now=10.110,
    )
    StreamingWorkflowIntegration._annotate_request_timing(
        request_data,
        stage="persist_done",
        started_at=10.0,
        now=10.130,
    )
    StreamingWorkflowIntegration._annotate_request_timing(
        request_data,
        stage="request_done",
        started_at=10.0,
        now=10.150,
        absolute_ms=150.0,
    )

    assert request_data["_request_timing_signals"] == {
        "memory_done": {
            "elapsed_ms": 25.0,
            "absolute_ms": 12.5,
        },
        "final_flush_done": {
            "elapsed_ms": 75.0,
        },
        "parse_done": {
            "elapsed_ms": 90.0,
        },
        "command_done": {
            "elapsed_ms": 110.0,
        },
        "persist_done": {
            "elapsed_ms": 130.0,
        },
        "request_done": {
            "elapsed_ms": 150.0,
            "absolute_ms": 150.0,
        },
    }

    with patch(
        "integrations.workflow_integrations.streaming_workflow_integration._log_request_path_workflow"
    ) as mock_log:
        StreamingWorkflowIntegration._log_request_timing_snapshot("sid-1", request_data)

    mock_log.assert_called_once_with(
        "workflow.timing",
        "sid-1",
        memory_done_elapsed_ms=25.0,
        memory_done_absolute_ms=12.5,
        final_flush_done_elapsed_ms=75.0,
        parse_done_elapsed_ms=90.0,
        command_done_elapsed_ms=110.0,
        persist_done_elapsed_ms=130.0,
        request_done_elapsed_ms=150.0,
        request_done_absolute_ms=150.0,
    )
