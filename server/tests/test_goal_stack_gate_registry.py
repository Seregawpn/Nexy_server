from collections import Counter
from pathlib import Path
import sys


tests_root = Path(__file__).parent
sys.path.insert(0, str(tests_root))

from goal_stack_gate_registry import (
    CANONICAL_20_CASE_GATE,
    EXTENDED_40_CASE_GATE,
    SUPPLEMENTAL_20_CASE_GATE,
    build_goal_stack_gate_matrix_rows,
)


def test_goal_stack_gate_registry_has_canonical_shape():
    assert len(CANONICAL_20_CASE_GATE) == 20

    case_ids = [case.case_id for case in CANONICAL_20_CASE_GATE]
    assert len(set(case_ids)) == 20

    tier_counts = Counter(case.tier for case in CANONICAL_20_CASE_GATE)
    assert tier_counts["core"] == 16
    assert tier_counts["rotatable"] == 4


def test_goal_stack_gate_registry_has_supplemental_shape():
    assert len(SUPPLEMENTAL_20_CASE_GATE) == 20

    case_ids = [case.case_id for case in SUPPLEMENTAL_20_CASE_GATE]
    assert len(set(case_ids)) == 20
    assert all(case.tier == "supplemental" for case in SUPPLEMENTAL_20_CASE_GATE)


def test_goal_stack_gate_registry_keeps_extended_ids_unique():
    case_ids = [case.case_id for case in EXTENDED_40_CASE_GATE]
    assert len(case_ids) == 40
    assert len(set(case_ids)) == 40


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


def test_goal_stack_gate_registry_has_diverse_matrix_columns():
    rows = build_goal_stack_gate_matrix_rows()

    assert len(rows) == 20
    assert all(row["interaction_shape"] for row in rows)
    assert all(row["noise_profile"] for row in rows)
    assert all(row["slot_pattern"] for row in rows)
    assert all(row["outcome_shape"] for row in rows)

    interaction_shapes = {row["interaction_shape"] for row in rows}
    noise_profiles = {row["noise_profile"] for row in rows}
    slot_patterns = {row["slot_pattern"] for row in rows}
    outcome_shapes = {row["outcome_shape"] for row in rows}

    assert {"direct", "follow_up", "pivot", "cancel", "non_task"} <= interaction_shapes
    assert {"clean", "pronoun", "fragment", "stt_like"} <= noise_profiles
    assert {"full_payload", "missing_message", "missing_app", "known_slot_reuse", "noisy_recovery", "none"} <= slot_patterns
    assert {"clarify", "execute", "answer", "cancel"} <= outcome_shapes


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


def test_goal_stack_gate_registry_keeps_memory_contract_complete():
    for case in CANONICAL_20_CASE_GATE:
        assert case.memory_prompt is not None
        assert case.memory_response is not None
        assert case.memory_expected_goal is not None


def test_goal_stack_gate_registry_keeps_deterministic_contract_complete():
    for case in CANONICAL_20_CASE_GATE:
        assert case.deterministic_request is not None
        assert case.deterministic_expected_category is not None
        assert case.deterministic_expected_route is not None
        assert case.deterministic_expected_text is not None


def test_goal_stack_gate_registry_keeps_supplemental_contract_complete():
    rows = build_goal_stack_gate_matrix_rows(SUPPLEMENTAL_20_CASE_GATE)
    assert len(rows) == 20
    for case in SUPPLEMENTAL_20_CASE_GATE:
        assert case.live_request is not None
        assert case.classifier_request is not None
        assert case.memory_prompt is not None
        assert case.deterministic_request is not None
