from pathlib import Path
import sys

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from experimental.assistant_runtime_v2.active_context import ActiveContextState
from experimental.assistant_runtime_v2.task_lifecycle import TaskLifecycleManager


def test_task_lifecycle_begin_turn_uses_prepared_route_without_local_nlu():
    manager = TaskLifecycleManager()
    state = ActiveContextState(session_id="s1")

    manager.begin_turn(
        {
            "session_id": "s1",
            "text": "anything",
            "prepared_request": {"route": "messages"},
        },
        state,
    )

    assert state.status == "turn_started"
    assert state.last_user_text == "anything"
    assert state.domain is None
    assert state.goal is None


def test_task_lifecycle_observes_canonical_command_payload():
    manager = TaskLifecycleManager()
    state = ActiveContextState(session_id="s2")

    manager.observe_stream_item(
        {
            "command_payload": {
                "payload": {
                    "command": "send_message",
                    "args": {"contact": "Sophia", "message": "How are you?"},
                }
            }
        },
        state,
    )

    assert state.status == "observed_command"
    assert state.domain == "messages"
    assert state.goal == "send_message"
    assert state.intent == "send_message"
    assert state.filled_slots == {"contact": "Sophia", "message": "How are you?"}


def test_task_lifecycle_finish_turn_clears_passive_state():
    manager = TaskLifecycleManager()
    state = ActiveContextState(
        session_id="s3",
        domain="messages",
        goal="send_message",
        intent="send_message",
        filled_slots={"contact": "Sophia"},
        status="observed_command",
    )

    manager.finish_turn(
        state,
        {
            "_assistant_runtime_v2_signals": {
                "goal_state": "keep",
                "current_goal": "User wants to send a message to Sophia. Missing detail: message text.",
                "route": "messages",
            }
        },
    )

    assert state.status == "idle"
    assert state.domain is None
    assert state.goal is None
    assert state.intent is None
    assert state.filled_slots == {}
