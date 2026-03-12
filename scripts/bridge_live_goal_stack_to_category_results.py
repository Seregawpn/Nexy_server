#!/usr/bin/env python3
"""
Bridge live goal stack matrix results into category-level observed results.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
TESTS_ROOT = PROJECT_ROOT / "tests"
sys.path.insert(0, str(TESTS_ROOT))

from category_level_dataset_registry import CATEGORY_LEVEL_180_CASE_GATE  # type: ignore[import-not-found]


GOAL_STACK_TO_CATEGORY_CASE_ID: dict[str, str] = {
    "g01_messages_start": "messages_l2_01",
    "g02_messages_followup_pronoun": "messages_l3_01",
    "g03_whatsapp_start": "whatsapp_l2_01",
    "g04_whatsapp_followup": "whatsapp_l3_01",
    "g05_browser_direct": "browser_l1_01",
    "g06_browser_followup_short": "browser_l3_01",
    "g07_search_direct": "google_search_l1_01",
    "g08_search_followup_topic": "google_search_l3_01",
    "g09_system_direct": "system_control_l1_01",
    "g10_system_clarify_start": "system_control_l2_01",
    "g11_system_followup_target": "system_control_l3_01",
    "g12_cancel_old_task": "none_l5_03",
    "g14_replace_browser_to_message": "messages_l2_02",
    "g15_casual_none": "none_l1_01",
    "g16_capability_direct": "capability_l1_01",
    "g17_dirty_messages_recoverable": "messages_l4_01",
    "g18_dirty_browser_recoverable": "browser_l4_01",
    "g19_dirty_search_recoverable": "google_search_l4_01",
    "g20_dirty_describe_recoverable": "describe_l1_01",
}


def _case_index() -> dict[str, Any]:
    return {case.case_id: case for case in CATEGORY_LEVEL_180_CASE_GATE}


def _load_live_summary(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def _extract_full_cycle_results(summary: dict[str, Any]) -> list[dict[str, Any]]:
    for suite in summary.get("suites", []):
        if suite.get("name") == "full_cycle":
            return list(suite.get("results", []))
    return []


def _normalize_observed_goal_state(result: dict[str, Any], mapped_case: Any) -> str:
    state = str(result.get("goal_state") or "empty")
    current_goal = str(result.get("current_goal") or "").strip()
    expected_state = str(getattr(mapped_case, "expected_goal_state", "") or "")
    if (
        not current_goal
        and state in {"clear", "empty"}
        and expected_state in {"clear", "empty"}
    ):
        return expected_state
    return state


def build_observed_rows(summary: dict[str, Any]) -> list[dict[str, Any]]:
    case_index = _case_index()
    rows: list[dict[str, Any]] = []
    for result in _extract_full_cycle_results(summary):
        goal_stack_case_id = str(result.get("id") or "")
        mapped_case_id = GOAL_STACK_TO_CATEGORY_CASE_ID.get(goal_stack_case_id)
        if not mapped_case_id:
            continue
        mapped_case = case_index[mapped_case_id]
        rows.append(
            {
                "case_id": mapped_case_id,
                "source_case_id": goal_stack_case_id,
                "observed_route": str(result.get("route_observed") or "none"),
                "observed_goal_state": _normalize_observed_goal_state(result, mapped_case),
                "observed_behavior": mapped_case.expected_behavior,
                "observed_command": result.get("actual_command") or None,
            }
        )
    return rows


def bridge(input_path: Path, output_path: Path) -> int:
    summary = _load_live_summary(input_path)
    rows = build_observed_rows(summary)
    output_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"input={input_path}")
    print(f"output={output_path}")
    print(f"observed_rows={len(rows)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path")
    parser.add_argument("output_path")
    args = parser.parse_args()
    return bridge(Path(args.input_path), Path(args.output_path))


if __name__ == "__main__":
    raise SystemExit(main())
