from pathlib import Path
import sys

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from experimental.assistant_runtime_v2.task_lifecycle import TaskLifecycleManager
from goal_stack_gate_registry import CANONICAL_20_CASE_GATE


def test_goal_state_registry_bridge_keeps_canonical_mapping():
    manager = TaskLifecycleManager()

    expected = {
        "set": "task_opened",
        "clear": "task_closed",
        "empty": "task_inactive",
    }

    observed_states = set()
    for case in CANONICAL_20_CASE_GATE:
        goal_state = case.live_expected_goal_state
        assert goal_state is not None, case.case_id
        observed_states.add(goal_state)
        assert manager._map_goal_state_to_event(goal_state) == expected[goal_state], case.case_id

    assert observed_states == set(expected)


def test_goal_state_registry_bridge_keeps_extended_mapping_contract():
    manager = TaskLifecycleManager()

    assert manager._map_goal_state_to_event("keep") == "task_continued"
    assert manager._map_goal_state_to_event("replace") == "task_replaced"


def test_goal_state_registry_bridge_keeps_transition_examples_stable():
    manager = TaskLifecycleManager()

    samples = {
        "g01_messages_start": "task_opened",
        "g02_messages_followup_pronoun": "task_closed",
        "g14_replace_browser_to_message": "task_opened",
        "g07_search_direct": "task_inactive",
    }

    case_by_id = {case.case_id: case for case in CANONICAL_20_CASE_GATE}

    for case_id, expected_event in samples.items():
        case = case_by_id[case_id]
        assert manager._map_goal_state_to_event(case.live_expected_goal_state) == expected_event
