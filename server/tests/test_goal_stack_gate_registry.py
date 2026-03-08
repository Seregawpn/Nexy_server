from collections import Counter
from pathlib import Path
import sys


tests_root = Path(__file__).parent
sys.path.insert(0, str(tests_root))

from goal_stack_gate_registry import CANONICAL_20_CASE_GATE


def test_goal_stack_gate_registry_has_canonical_shape():
    assert len(CANONICAL_20_CASE_GATE) == 20

    case_ids = [case.case_id for case in CANONICAL_20_CASE_GATE]
    assert len(set(case_ids)) == 20

    tier_counts = Counter(case.tier for case in CANONICAL_20_CASE_GATE)
    assert tier_counts["core"] == 16
    assert tier_counts["rotatable"] == 4


def test_goal_stack_gate_registry_has_required_transition_coverage():
    transitions = {case.transition_type for case in CANONICAL_20_CASE_GATE}

    assert "new_task" in transitions
    assert "pronoun_continuation" in transitions
    assert "short_continuation" in transitions
    assert "continuation_completion" in transitions
    assert "same_turn_completion" in transitions
    assert "cancel" in transitions
    assert "replace" in transitions
    assert "no_task" in transitions


def test_goal_stack_gate_registry_has_required_category_coverage():
    categories = Counter(case.category for case in CANONICAL_20_CASE_GATE)

    assert categories["messages"] >= 3
    assert categories["whatsapp"] >= 2
    assert categories["browser"] >= 3
    assert categories["google_search"] >= 3
    assert categories["system_control"] >= 3
    assert categories["none"] >= 2
    assert categories["capability"] >= 1
    assert categories["describe"] >= 1


def test_goal_stack_gate_registry_has_dirty_and_pair_coverage():
    dirty_cases = [case for case in CANONICAL_20_CASE_GATE if case.prompt_style == "dirty"]
    paired_cases = [case for case in CANONICAL_20_CASE_GATE if case.paired]

    assert len(dirty_cases) == 4
    assert len(paired_cases) >= 10


def test_goal_stack_gate_registry_keeps_owner_focus_explicit():
    for case in CANONICAL_20_CASE_GATE:
        assert case.owner_focus
        assert "live" in case.owner_focus
        for owner in case.owner_focus:
            assert owner in {"memory", "classifier", "generator", "live"}


def test_goal_stack_gate_registry_keeps_live_contract_complete():
    for case in CANONICAL_20_CASE_GATE:
        assert case.live_request
        assert case.live_expected_route
        assert case.live_hardware_id
        assert case.live_expected_goal_state is not None


def test_goal_stack_gate_registry_keeps_classifier_contract_complete():
    for case in CANONICAL_20_CASE_GATE:
        assert case.classifier_request is not None
        assert case.classifier_expected_route is not None
