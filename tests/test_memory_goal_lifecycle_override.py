from modules.memory_management.core.memory_manager import MemoryManager


def test_informational_routes_force_empty_goal_state():
    manager = MemoryManager(db_manager=None)

    state, goal = manager._override_goal_state_from_runtime_outcome(
        route="capability",
        behavior="answer",
        command_name="",
        command_present=False,
        analyzed_goal_state="set",
        analyzed_current_goal="User wants to know assistant capabilities.",
    )

    assert state == "empty"
    assert goal == ""


def test_execute_with_command_forces_empty_goal_state():
    manager = MemoryManager(db_manager=None)

    state, goal = manager._override_goal_state_from_runtime_outcome(
        route="browser",
        behavior="execute",
        command_name="browser_use",
        command_present=True,
        analyzed_goal_state="set",
        analyzed_current_goal="User wants to search Wikipedia for Helen Keller.",
    )

    assert state == "empty"
    assert goal == ""


def test_clarify_preserves_pending_goal_when_present():
    manager = MemoryManager(db_manager=None)

    state, goal = manager._override_goal_state_from_runtime_outcome(
        route="messages",
        behavior="clarify",
        command_name="",
        command_present=False,
        analyzed_goal_state="keep",
        analyzed_current_goal="User wants to text Sophia. Missing detail: message text.",
    )

    assert state == "set"
    assert "Sophia" in goal
