#!/usr/bin/env python3
"""
Summarize canonical category-level quality campaign coverage.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import json
from pathlib import Path
import sys
from typing import Iterable, Optional


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TESTS_ROOT = PROJECT_ROOT / "tests"
sys.path.insert(0, str(TESTS_ROOT))

from category_level_dataset_registry import (  # type: ignore[import-not-found]
    CATEGORY_LEVEL_180_CASE_GATE,
    LEVEL_1_30_CASE_CAMPAIGN,
    LEVEL_2_36_CASE_CAMPAIGN,
    CATEGORY_ORDER,
    LEVEL_ORDER,
    CategoryLevelCase,
    build_category_level_heatmap_rows,
)


CAMPAIGN_PRESETS: dict[str, tuple[CategoryLevelCase, ...]] = {
    "full": CATEGORY_LEVEL_180_CASE_GATE,
    "level1_30": LEVEL_1_30_CASE_CAMPAIGN,
    "level2_36": LEVEL_2_36_CASE_CAMPAIGN,
}


@dataclass(frozen=True)
class CampaignObservedResult:
    case_id: str
    observed_route: str
    observed_goal_state: str
    observed_behavior: str
    observed_command: Optional[str]


@dataclass(frozen=True)
class CampaignEvaluationResult:
    case_id: str
    category: str
    level: int
    ok: bool
    failure_type: str
    owner: str


def select_cases(
    campaign: str | None = None,
    category: str | None = None,
    level: int | None = None,
) -> tuple[CategoryLevelCase, ...]:
    selected = CAMPAIGN_PRESETS.get(campaign or "full", CATEGORY_LEVEL_180_CASE_GATE)
    if category is not None:
        selected = tuple(case for case in selected if case.category == category)
    if level is not None:
        selected = tuple(case for case in selected if case.level == level)
    return selected


def build_campaign_summary(cases: Iterable[CategoryLevelCase]) -> dict[str, object]:
    selected = tuple(cases)
    category_counts = Counter(case.category for case in selected)
    level_counts = Counter(case.level for case in selected)
    behavior_counts = Counter(case.expected_behavior for case in selected)
    command_counts = Counter(case.expected_command or "none" for case in selected)
    owner_counts = Counter(owner for case in selected for owner in case.owner_focus)
    memory_case_count = sum(1 for case in selected if case.memory_expected)

    return {
        "cases": len(selected),
        "category_counts": dict(category_counts),
        "level_counts": dict(level_counts),
        "behavior_counts": dict(behavior_counts),
        "command_counts": dict(command_counts),
        "owner_counts": dict(owner_counts),
        "memory_case_count": memory_case_count,
    }


def evaluate_case_result(
    case: CategoryLevelCase,
    observed: CampaignObservedResult,
) -> CampaignEvaluationResult:
    if observed.observed_route != case.expected_route:
        return CampaignEvaluationResult(case.case_id, case.category, case.level, False, "route_mismatch", "classifier")
    if observed.observed_goal_state != case.expected_goal_state:
        return CampaignEvaluationResult(case.case_id, case.category, case.level, False, "goal_state_mismatch", "memory")
    if observed.observed_behavior != case.expected_behavior:
        return CampaignEvaluationResult(case.case_id, case.category, case.level, False, "behavior_mismatch", "generator")
    if (observed.observed_command or None) != case.expected_command:
        return CampaignEvaluationResult(case.case_id, case.category, case.level, False, "command_mismatch", "parser")
    return CampaignEvaluationResult(case.case_id, case.category, case.level, True, "ok", "none")


def build_evaluation_summary(results: Iterable[CampaignEvaluationResult]) -> dict[str, object]:
    selected = tuple(results)
    return {
        "cases": len(selected),
        "ok_cases": sum(1 for result in selected if result.ok),
        "failed_cases": sum(1 for result in selected if not result.ok),
        "failure_type_counts": dict(Counter(result.failure_type for result in selected if not result.ok)),
        "owner_counts": dict(Counter(result.owner for result in selected if not result.ok)),
        "category_counts": dict(Counter(result.category for result in selected if not result.ok)),
        "level_counts": dict(Counter(result.level for result in selected if not result.ok)),
    }


def load_observed_results(results_path: Path) -> tuple[CampaignObservedResult, ...]:
    rows = json.loads(results_path.read_text())
    return tuple(
        CampaignObservedResult(
            case_id=row["case_id"],
            observed_route=row["observed_route"],
            observed_goal_state=row["observed_goal_state"],
            observed_behavior=row["observed_behavior"],
            observed_command=row.get("observed_command"),
        )
        for row in rows
    )


def evaluate_observed_results(
    observed_results: Iterable[CampaignObservedResult],
    campaign: str | None = None,
    category: str | None = None,
    level: int | None = None,
) -> tuple[CampaignEvaluationResult, ...]:
    case_index = {case.case_id: case for case in select_cases(campaign=campaign, category=category, level=level)}
    evaluations: list[CampaignEvaluationResult] = []
    for observed in observed_results:
        case = case_index.get(observed.case_id)
        if case is None:
            continue
        evaluations.append(evaluate_case_result(case, observed))
    return tuple(evaluations)


def _print_counter_block(title: str, values: dict[object, int], order: tuple[object, ...] | None = None) -> None:
    print(title)
    keys = order or tuple(values)
    for key in keys:
        if key in values:
            print(f"  {key}: {values[key]}")


def summarize(
    campaign: str | None = None,
    category: str | None = None,
    level: int | None = None,
    results_path: Path | None = None,
) -> int:
    cases = select_cases(campaign=campaign, category=category, level=level)
    if not cases:
        print("no cases selected")
        return 1

    summary = build_campaign_summary(cases)
    print(f"selected_cases={summary['cases']}")
    _print_counter_block("categories", summary["category_counts"], CATEGORY_ORDER)
    _print_counter_block("levels", summary["level_counts"], LEVEL_ORDER)
    _print_counter_block("behaviors", summary["behavior_counts"])
    _print_counter_block("commands", summary["command_counts"])
    _print_counter_block("owners", summary["owner_counts"], ("classifier", "generator", "memory", "live"))
    print(f"memory_cases={summary['memory_case_count']}")

    print("heatmap")
    for row in build_category_level_heatmap_rows(cases):
        if row["cases"] == 0:
            continue
        print(
            f"  {row['category']}:L{row['level']} "
            f"cases={row['cases']} "
            f"memory={row['memory_cases']} "
            f"answer={row['answer_cases']} "
            f"clarify={row['clarify_cases']} "
            f"execute={row['execute_cases']} "
            f"replace={row['replace_cases']} "
            f"cancel={row['cancel_cases']}"
        )

    if results_path is not None:
        observed_results = load_observed_results(results_path)
        evaluation_summary = build_evaluation_summary(
            evaluate_observed_results(observed_results, category=category, level=level)
            if campaign is None
            else evaluate_observed_results(observed_results, campaign=campaign, category=category, level=level)
        )
        print("evaluation")
        print(f"  cases={evaluation_summary['cases']}")
        print(f"  ok_cases={evaluation_summary['ok_cases']}")
        print(f"  failed_cases={evaluation_summary['failed_cases']}")
        _print_counter_block("  failure_types", evaluation_summary["failure_type_counts"])
        _print_counter_block("  failed_owners", evaluation_summary["owner_counts"])
        _print_counter_block("  failed_categories", evaluation_summary["category_counts"], CATEGORY_ORDER)
        _print_counter_block("  failed_levels", evaluation_summary["level_counts"], LEVEL_ORDER)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaign", choices=tuple(CAMPAIGN_PRESETS))
    parser.add_argument("--category", choices=CATEGORY_ORDER)
    parser.add_argument("--level", type=int, choices=LEVEL_ORDER)
    parser.add_argument("--results-json")
    args = parser.parse_args()
    return summarize(
        campaign=args.campaign,
        category=args.category,
        level=args.level,
        results_path=Path(args.results_json) if args.results_json else None,
    )


if __name__ == "__main__":
    raise SystemExit(main())
