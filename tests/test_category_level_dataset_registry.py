from collections import Counter
from pathlib import Path
import sys


tests_root = Path(__file__).parent
sys.path.insert(0, str(tests_root))

from category_level_dataset_registry import (
    CATEGORY_CAMPAIGNS,
    CATEGORY_LEVEL_180_CASE_GATE,
    CATEGORY_ORDER,
    FULL_CATEGORY_LEVEL_CAMPAIGN,
    LEVEL_1_30_CASE_CAMPAIGN,
    LEVEL_1_CASE_INPUTS,
    LEVEL_2_36_CASE_CAMPAIGN,
    LEVEL_2_CASE_INPUTS,
    LEVEL_CAMPAIGNS,
    LEVEL_ORDER,
    PROMPT_OWNER_BY_CATEGORY,
    build_category_level_heatmap_rows,
    build_category_level_matrix_rows,
)


def test_category_level_dataset_registry_has_canonical_shape():
    assert len(CATEGORY_LEVEL_180_CASE_GATE) == 180

    case_ids = [case.case_id for case in CATEGORY_LEVEL_180_CASE_GATE]
    assert len(set(case_ids)) == 180


def test_category_level_dataset_registry_keeps_category_coverage_balanced():
    counts = Counter(case.category for case in CATEGORY_LEVEL_180_CASE_GATE)

    assert tuple(counts) == CATEGORY_ORDER
    assert all(counts[category] == 20 for category in CATEGORY_ORDER)
    assert set(CATEGORY_CAMPAIGNS) == set(CATEGORY_ORDER)


def test_category_level_dataset_registry_keeps_level_coverage_balanced():
    counts = Counter(case.level for case in CATEGORY_LEVEL_180_CASE_GATE)

    assert tuple(counts) == LEVEL_ORDER
    assert all(counts[level] == 36 for level in LEVEL_ORDER)
    assert set(LEVEL_CAMPAIGNS) == set(LEVEL_ORDER)


def test_category_level_dataset_registry_keeps_four_cases_per_category_level_cell():
    cell_counts = Counter((case.category, case.level) for case in CATEGORY_LEVEL_180_CASE_GATE)
    assert all(cell_counts[(category, level)] == 4 for category in CATEGORY_ORDER for level in LEVEL_ORDER)


def test_category_level_dataset_registry_keeps_contract_complete():
    for case in CATEGORY_LEVEL_180_CASE_GATE:
        assert case.summary
        assert case.user_input
        assert case.expected_route == case.category
        assert case.expected_goal_state in {"set", "keep", "replace", "clear", "empty"}
        assert case.expected_behavior in {
            "answer",
            "continue_answer",
            "clarify",
            "disambiguate",
            "execute",
            "continue_execute",
            "replace",
            "cancel",
        }
        assert case.prompt_owner == PROMPT_OWNER_BY_CATEGORY[case.category]
        assert case.owner_focus == ("classifier", "generator", "memory", "live")


def test_category_level_dataset_registry_keeps_behavior_to_command_contract_consistent():
    for case in CATEGORY_LEVEL_180_CASE_GATE:
        if case.expected_behavior in {"execute", "continue_execute", "replace"}:
            assert case.expected_command is not None
        if case.expected_behavior in {"answer", "continue_answer", "clarify", "disambiguate", "cancel"}:
            assert case.expected_command is None


def test_category_level_dataset_registry_keeps_non_action_routes_command_free():
    non_action = {"none", "capability", "describe", "google_search"}
    for case in CATEGORY_LEVEL_180_CASE_GATE:
        if case.category in non_action:
            assert case.expected_command is None


def test_category_level_dataset_registry_keeps_level_intent_shapes_stable():
    level_1 = {case.expected_behavior for case in LEVEL_CAMPAIGNS[1]}
    level_2 = {case.expected_behavior for case in LEVEL_CAMPAIGNS[2]}
    level_3 = {case.expected_behavior for case in LEVEL_CAMPAIGNS[3]}
    level_4 = {case.expected_behavior for case in LEVEL_CAMPAIGNS[4]}
    level_5 = {case.expected_behavior for case in LEVEL_CAMPAIGNS[5]}

    assert level_1 <= {"answer", "execute"}
    assert level_2 == {"clarify"}
    assert level_3 <= {"continue_answer", "continue_execute"}
    assert level_4 <= {"answer", "execute", "clarify"}
    assert level_5 <= {"answer", "disambiguate", "replace", "cancel"}


def test_category_level_dataset_registry_exposes_full_campaign_owner():
    assert FULL_CATEGORY_LEVEL_CAMPAIGN is CATEGORY_LEVEL_180_CASE_GATE
    assert len(FULL_CATEGORY_LEVEL_CAMPAIGN) == 180


def test_category_level_dataset_registry_exposes_curated_level_1_30_campaign():
    assert len(LEVEL_1_30_CASE_CAMPAIGN) == 30
    assert all(case.level == 1 for case in LEVEL_1_30_CASE_CAMPAIGN)
    assert {case.category for case in LEVEL_1_30_CASE_CAMPAIGN} == set(CATEGORY_ORDER)


def test_category_level_dataset_registry_uses_real_level_1_user_inputs():
    for category, prompts in LEVEL_1_CASE_INPUTS.items():
        category_cases = [case for case in CATEGORY_LEVEL_180_CASE_GATE if case.category == category and case.level == 1]
        assert len(category_cases) == 4
        assert tuple(case.user_input for case in category_cases) == tuple(prompt for _, prompt in prompts)


def test_category_level_dataset_registry_uses_real_level_2_user_inputs():
    for category, prompts in LEVEL_2_CASE_INPUTS.items():
        category_cases = [case for case in CATEGORY_LEVEL_180_CASE_GATE if case.category == category and case.level == 2]
        assert len(category_cases) == 4
        assert tuple(case.user_input for case in category_cases) == tuple(prompt for _, prompt in prompts)


def test_category_level_dataset_registry_keeps_heatmap_rows_complete():
    rows = build_category_level_heatmap_rows()

    assert len(rows) == len(CATEGORY_ORDER) * len(LEVEL_ORDER)
    assert all(row["cases"] == 4 for row in rows)


def test_category_level_dataset_registry_exposes_curated_level_2_36_campaign():
    assert len(LEVEL_2_36_CASE_CAMPAIGN) == 36
    assert all(case.level == 2 for case in LEVEL_2_36_CASE_CAMPAIGN)
    assert {case.category for case in LEVEL_2_36_CASE_CAMPAIGN} == set(CATEGORY_ORDER)


def test_category_level_dataset_registry_keeps_matrix_rows_complete():
    rows = build_category_level_matrix_rows()

    assert len(rows) == 180
    assert all(row["interaction_shape"] for row in rows)
    assert all(row["outcome_shape"] for row in rows)
    assert all(row["prompt_owner"] for row in rows)

    interaction_shapes = {row["interaction_shape"] for row in rows}
    outcome_shapes = {row["outcome_shape"] for row in rows}

    assert {"direct", "follow_up", "recovery", "ambiguous", "replace", "cancel"} <= interaction_shapes
    assert {"answer", "clarify", "execute", "replace", "cancel"} <= outcome_shapes
