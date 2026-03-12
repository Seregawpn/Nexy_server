#!/usr/bin/env python3
"""
Live full-cycle runner for category-level campaigns.

Uses the existing production-like stack and emits observed rows compatible with
run_category_level_campaign.py --results-json.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import uuid
from pathlib import Path
from typing import Any

import sys

ROOT = Path(__file__).resolve().parents[2]
SERVER_ROOT = Path(__file__).resolve().parents[1]
TESTS_ROOT = SERVER_ROOT / "tests"

sys.path.insert(0, str(SERVER_ROOT))
sys.path.insert(0, str(TESTS_ROOT))

from category_level_dataset_registry import (  # type: ignore[import-not-found]
    CATEGORY_LEVEL_180_CASE_GATE,
    LEVEL_1_30_CASE_CAMPAIGN,
    LEVEL_2_36_CASE_CAMPAIGN,
    CategoryLevelCase,
)
from scripts.run_live_goal_stack_matrix import (  # type: ignore[import-not-found]
    _build_live_stack,
    _cleanup_live_stack,
    _extract_route,
    _ensure_user,
    _extract_command,
    _extract_text,
    _fetch_snapshot,
    _prepare_route_observation,
    _run_request,
    _wait_for_snapshot_update,
)


logger = logging.getLogger("live_category_level_campaign")


CAMPAIGN_PRESETS: dict[str, tuple[CategoryLevelCase, ...]] = {
    "full": CATEGORY_LEVEL_180_CASE_GATE,
    "level1_30": LEVEL_1_30_CASE_CAMPAIGN,
    "level2_36": LEVEL_2_36_CASE_CAMPAIGN,
}


def _infer_behavior(*, command: str | None, goal_state: str, text: str) -> str:
    if command:
        return "execute"
    if goal_state in {"set", "keep", "replace"}:
        return "clarify"
    if text.strip():
        return "answer"
    return "answer"


def _normalize_goal_state(*, expected_state: str, actual_state: str, actual_goal: str) -> str:
    if (
        not actual_goal.strip()
        and actual_state in {"clear", "empty"}
        and expected_state in {"clear", "empty"}
    ):
        return expected_state
    return actual_state


async def run_campaign(cases: tuple[CategoryLevelCase, ...]) -> list[dict[str, Any]]:
    stack = await _build_live_stack()
    try:
        service = stack["service"]
        adapter = stack["memory_adapter"]
        text_module = stack["text_module"]
        db = stack["db"]
        run_suffix = uuid.uuid4().hex[:8]
        snapshots_by_hardware: dict[str, dict[str, Any]] = {}
        rows: list[dict[str, Any]] = []

        for case in cases:
            hardware_id = f"live-cat-{case.case_id}-{run_suffix}"
            await _ensure_user(db, hardware_id)
            previous_snapshot = snapshots_by_hardware.get(hardware_id)
            session_id = str(uuid.uuid4())
            prepared_result = await _prepare_route_observation(
                adapter=adapter,
                text_module=text_module,
                hardware_id=hardware_id,
                request=case.user_input,
                session_id=session_id,
            )
            items = await _run_request(
                service,
                {
                    "text": case.user_input,
                    "session_id": session_id,
                    "hardware_id": hardware_id,
                },
            )
            text = _extract_text(items)
            command_payload = _extract_command(items)
            observed_route = _extract_route(items)
            command = None
            if isinstance(command_payload, dict):
                command = str((command_payload.get("payload") or {}).get("command") or "")
            snapshot, snapshot_timeout = await _wait_for_snapshot_update(
                db,
                hardware_id,
                previous_snapshot,
            )
            snapshots_by_hardware[hardware_id] = snapshot
            actual_goal = str(snapshot.get("current_goal") or "")
            raw_state = str(snapshot.get("goal_state") or "")
            if not raw_state and not actual_goal:
                raw_state = "empty"
            normalized_state = _normalize_goal_state(
                expected_state=case.expected_goal_state,
                actual_state=raw_state,
                actual_goal=actual_goal,
            )
            behavior = _infer_behavior(command=command, goal_state=normalized_state, text=text)
            rows.append(
                {
                    "case_id": case.case_id,
                    "observed_route": observed_route or prepared_result["route"],
                    "observed_goal_state": normalized_state,
                    "observed_behavior": behavior,
                    "observed_command": command or None,
                    "snapshot_timeout": snapshot_timeout,
                }
            )
            logger.info(
                "category_level %s -> route=%s behavior=%s command=%s goal_state=%s",
                case.case_id,
                observed_route or prepared_result["route"],
                behavior,
                command or "-",
                normalized_state,
            )

        return rows
    finally:
        await _cleanup_live_stack(stack)


async def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--campaign", default="level1_30", choices=tuple(CAMPAIGN_PRESETS))
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = await run_campaign(CAMPAIGN_PRESETS[args.campaign])
    output_path = Path(args.output)
    output_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"campaign={args.campaign}")
    print(f"output={output_path}")
    print(f"observed_rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
