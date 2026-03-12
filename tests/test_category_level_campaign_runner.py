from pathlib import Path
import sys


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
tests_root = Path(__file__).parent
sys.path.insert(0, str(tests_root))

from scripts.run_category_level_campaign import (
    CAMPAIGN_PRESETS,
    CampaignObservedResult,
    build_campaign_summary,
    build_evaluation_summary,
    evaluate_observed_results,
    select_cases,
)


def test_category_level_campaign_runner_selects_full_campaign_by_default():
    cases = select_cases()

    assert len(cases) == 180


def test_category_level_campaign_runner_selects_curated_level1_30_campaign():
    cases = select_cases(campaign="level1_30")

    assert len(cases) == 30
    assert all(case.level == 1 for case in cases)
    assert set(CAMPAIGN_PRESETS) == {"full", "level1_30", "level2_36"}


def test_category_level_campaign_runner_selects_curated_level2_36_campaign():
    cases = select_cases(campaign="level2_36")

    assert len(cases) == 36
    assert all(case.level == 2 for case in cases)
    assert {case.category for case in cases} == {
        "none",
        "capability",
        "describe",
        "messages",
        "whatsapp",
        "system_control",
        "browser",
        "google_search",
        "payment",
    }


def test_category_level_campaign_runner_filters_by_category():
    cases = select_cases(category="messages")

    assert len(cases) == 20
    assert all(case.category == "messages" for case in cases)


def test_category_level_campaign_runner_filters_by_level():
    cases = select_cases(level=2)

    assert len(cases) == 36
    assert all(case.level == 2 for case in cases)


def test_category_level_campaign_runner_builds_consistent_full_summary():
    summary = build_campaign_summary(select_cases())

    assert summary["cases"] == 180
    assert summary["category_counts"]["messages"] == 20
    assert summary["category_counts"]["payment"] == 20
    assert summary["level_counts"][1] == 36
    assert summary["level_counts"][5] == 36
    assert summary["owner_counts"]["classifier"] == 180
    assert summary["owner_counts"]["generator"] == 180
    assert summary["owner_counts"]["memory"] == 180
    assert summary["owner_counts"]["live"] == 180


def test_category_level_campaign_runner_builds_curated_level1_summary():
    summary = build_campaign_summary(select_cases(campaign="level1_30"))

    assert summary["cases"] == 30
    assert summary["level_counts"][1] == 30
    assert summary["category_counts"]["messages"] == 4
    assert summary["category_counts"]["whatsapp"] == 4
    assert summary["category_counts"]["browser"] == 4


def test_category_level_campaign_runner_builds_curated_level2_summary():
    summary = build_campaign_summary(select_cases(campaign="level2_36"))

    assert summary["cases"] == 36
    assert summary["level_counts"][2] == 36
    assert summary["behavior_counts"]["clarify"] == 36
    assert summary["category_counts"]["messages"] == 4


def test_category_level_campaign_runner_builds_category_slice_summary():
    summary = build_campaign_summary(select_cases(category="none"))

    assert summary["cases"] == 20
    assert summary["behavior_counts"]["clarify"] == 4
    assert summary["behavior_counts"]["answer"] >= 8
    assert summary["command_counts"]["none"] == 20


def test_category_level_campaign_runner_evaluates_observed_results_and_maps_owner():
    observed = (
        CampaignObservedResult(
            case_id="messages_l3_01",
            observed_route="browser",
            observed_goal_state="clear",
            observed_behavior="continue_execute",
            observed_command="send_message",
        ),
        CampaignObservedResult(
            case_id="messages_l3_02",
            observed_route="messages",
            observed_goal_state="set",
            observed_behavior="continue_execute",
            observed_command="send_message",
        ),
        CampaignObservedResult(
            case_id="messages_l3_03",
            observed_route="messages",
            observed_goal_state="clear",
            observed_behavior="clarify",
            observed_command=None,
        ),
        CampaignObservedResult(
            case_id="messages_l3_04",
            observed_route="messages",
            observed_goal_state="clear",
            observed_behavior="continue_execute",
            observed_command="browser_use",
        ),
    )

    results = evaluate_observed_results(observed, category="messages", level=3)
    summary = build_evaluation_summary(results)

    assert summary["cases"] == 4
    assert summary["failed_cases"] == 4
    assert summary["failure_type_counts"]["route_mismatch"] == 1
    assert summary["failure_type_counts"]["goal_state_mismatch"] == 1
    assert summary["failure_type_counts"]["behavior_mismatch"] == 1
    assert summary["failure_type_counts"]["command_mismatch"] == 1
    assert summary["owner_counts"]["classifier"] == 1
    assert summary["owner_counts"]["memory"] == 1
    assert summary["owner_counts"]["generator"] == 1
    assert summary["owner_counts"]["parser"] == 1


def test_category_level_campaign_runner_counts_successful_observed_results():
    observed = tuple(
        CampaignObservedResult(
            case_id=case.case_id,
            observed_route=case.expected_route,
            observed_goal_state=case.expected_goal_state,
            observed_behavior=case.expected_behavior,
            observed_command=case.expected_command,
        )
        for case in select_cases(category="none", level=1)
    )

    summary = build_evaluation_summary(evaluate_observed_results(observed, category="none", level=1))

    assert summary["cases"] == 4
    assert summary["ok_cases"] == 4
    assert summary["failed_cases"] == 0
