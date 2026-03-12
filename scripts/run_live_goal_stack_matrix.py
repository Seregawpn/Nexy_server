#!/usr/bin/env python3
"""
Live matrix runner for goal lifecycle stack:
1. Memory only (real MemoryAnalyzer + DB persistence)
2. Memory + classification (real TextProcessor classifier)
3. Memory + classification + generation (real workflow/service path)

Uses production-like module owners:
- DatabaseManager
- MemoryManager / MemoryManagementAdapter / MemoryWorkflowIntegration
- TextProcessingModule / TextProcessor / LangChainGeminiProvider
- StreamingWorkflowIntegration / GrpcServiceIntegration

This script intentionally does not use keyword heuristics or fake providers.

Canonical gate policy:
- registry: server/server/tests/goal_stack_gate_registry.py
- process: server/server/Docs/GOAL_STACK_TEST_GATE.md
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[2]
SERVER_ROOT = Path(__file__).resolve().parents[1]
TESTS_ROOT = SERVER_ROOT / "tests"

import sys

sys.path.insert(0, str(SERVER_ROOT))
sys.path.insert(0, str(TESTS_ROOT))

from config.unified_config import get_config
from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration
from integrations.workflow_integrations.memory_workflow_integration import MemoryWorkflowIntegration
from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from modules.database.core.database_manager import DatabaseManager
from modules.memory_management.adapter import MemoryManagementAdapter
from modules.memory_management.core.memory_manager import MemoryManager
from modules.text_processing.module import TextProcessingModule
from goal_stack_gate_registry import CANONICAL_20_CASE_GATE, L1_BASIC_DIRECT_20_CASE_GATE, L2_CLARIFICATION_SLOT_FILL_20_CASE_GATE


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("live_goal_stack_matrix")


def _selected_gate_cases():
    gate_set = os.environ.get("GOAL_STACK_GATE_SET", "canonical").strip().lower()
    if gate_set == "canonical":
        return "canonical", CANONICAL_20_CASE_GATE
    if gate_set == "l1":
        return "l1", L1_BASIC_DIRECT_20_CASE_GATE
    if gate_set == "l2":
        return "l2", L2_CLARIFICATION_SLOT_FILL_20_CASE_GATE
    raise RuntimeError(f"Unsupported GOAL_STACK_GATE_SET={gate_set!r}; expected 'canonical', 'l1', or 'l2'")


class LightweightAudioModule:
    """Minimal audio module to keep workflow contract real without invoking TTS."""

    def __init__(self) -> None:
        self.is_initialized = True
        self.name = "audio_generation"

    async def process(self, payload: Dict[str, Any]):
        async def _gen():
            text = str(payload.get("text") or "")
            if text:
                yield b"a" * 256

        return _gen()


@dataclass
class MemoryCase:
    case_id: str
    prompt: str
    response: str
    expected_state: str
    goal_contains: Optional[List[str]] = None
    seed_turns: Optional[List[tuple[str, str]]] = None


def _memory_case_passes(
    case: MemoryCase,
    *,
    actual_state: str,
    actual_goal: str,
) -> bool:
    normalized_goal = str(actual_goal or "").strip()
    if case.expected_state in {"clear", "empty"}:
        return actual_state in {"clear", "empty"} and not normalized_goal
    return actual_state == case.expected_state and _contains_all(normalized_goal, case.goal_contains)


@dataclass
class ClassifierCase:
    case_id: str
    seed_turns: List[tuple[str, str]]
    request: str
    expected_route: str


@dataclass
class FullCycleCase:
    case_id: str
    hardware_id: str
    request: str
    expected_route: str
    expected_command: Optional[str] = None
    expected_text_contains: Optional[List[str]] = None
    expect_goal_state: Optional[str] = None
    seed_turns: Optional[List[tuple[str, str]]] = None


# Registry is the single source of truth for all live gate case definitions.


def _build_registry_live_cases(selected_cases) -> List[FullCycleCase]:
    live_cases: List[FullCycleCase] = []
    for gate_case in selected_cases:
        if "live" not in gate_case.owner_focus:
            continue
        if not gate_case.live_request or not gate_case.live_expected_route or not gate_case.live_hardware_id:
            raise RuntimeError(f"Live gate case is incomplete: {gate_case.case_id}")
        live_cases.append(
            FullCycleCase(
                case_id=gate_case.case_id,
                hardware_id=gate_case.live_hardware_id,
                request=gate_case.live_request,
                expected_route=gate_case.live_expected_route,
                expected_command=gate_case.live_expected_command,
                expected_text_contains=list(gate_case.live_expected_text_contains) or None,
                expect_goal_state=gate_case.live_expected_goal_state,
                seed_turns=list(gate_case.live_seed_turns) or None,
            )
        )
    expected = sum(1 for gate_case in selected_cases if "live" in gate_case.owner_focus)
    if len(live_cases) != expected:
        raise RuntimeError(f"Expected {expected} live gate cases, got {len(live_cases)}")
    return live_cases


def _build_registry_memory_cases(selected_cases) -> List[MemoryCase]:
    memory_cases: List[MemoryCase] = []
    for gate_case in selected_cases:
        if "memory" not in gate_case.owner_focus:
            continue
        if (
            gate_case.memory_prompt is None
            or gate_case.memory_response is None
            or gate_case.live_expected_goal_state is None
            or gate_case.memory_expected_goal is None
        ):
            raise RuntimeError(f"Memory gate case is incomplete: {gate_case.case_id}")
        goal_contains: Optional[List[str]] = None
        if gate_case.memory_expected_goal:
            goal_contains = [gate_case.memory_expected_goal]
        memory_cases.append(
            MemoryCase(
                case_id=gate_case.case_id.replace("g", "m", 1),
                prompt=gate_case.memory_prompt,
                response=gate_case.memory_response,
                expected_state=gate_case.live_expected_goal_state,
                goal_contains=goal_contains,
                seed_turns=list(gate_case.live_seed_turns) or None,
            )
        )
    expected = sum(1 for gate_case in selected_cases if "memory" in gate_case.owner_focus)
    if len(memory_cases) != expected:
        raise RuntimeError(f"Expected {expected} memory gate cases, got {len(memory_cases)}")
    return memory_cases


def _build_registry_classifier_cases(selected_cases) -> List[ClassifierCase]:
    classifier_cases: List[ClassifierCase] = []
    for gate_case in selected_cases:
        if "classifier" not in gate_case.owner_focus:
            continue
        if gate_case.classifier_request is None or gate_case.classifier_expected_route is None:
            raise RuntimeError(f"Classifier gate case is incomplete: {gate_case.case_id}")
        classifier_cases.append(
            ClassifierCase(
                case_id=gate_case.case_id.replace("g", "c", 1),
                seed_turns=list(gate_case.live_seed_turns),
                request=gate_case.classifier_request,
                expected_route=gate_case.classifier_expected_route,
            )
        )
    expected = sum(1 for gate_case in selected_cases if "classifier" in gate_case.owner_focus)
    if len(classifier_cases) != expected:
        raise RuntimeError(f"Expected {expected} classifier gate cases, got {len(classifier_cases)}")
    return classifier_cases


SELECTED_GATE_NAME, SELECTED_GATE_CASES = _selected_gate_cases()

MEMORY_CASES: List[MemoryCase] = _build_registry_memory_cases(SELECTED_GATE_CASES)
CLASSIFIER_CASES: List[ClassifierCase] = _build_registry_classifier_cases(SELECTED_GATE_CASES)
FULL_CYCLE_CASES: List[FullCycleCase] = _build_registry_live_cases(SELECTED_GATE_CASES)


def _norm(value: Any) -> str:
    return " ".join(str(value or "").split()).strip().lower()


def _contains_all(text: str, parts: Optional[List[str]]) -> bool:
    if not parts:
        return True
    hay = _norm(text)
    return all(_norm(part) in hay for part in parts)


def _execution_passes(
    case: FullCycleCase,
    *,
    command: Optional[str],
    text: str,
) -> bool:
    """
    Product acceptance must prioritize execution truth over post-memory cleanup.

    Primary acceptance sources:
    - actual command payload (when expected)
    - final user-visible text
    """
    return (
        (case.expected_command is None or command == case.expected_command)
        and _contains_all(text, case.expected_text_contains)
    )


def _memory_passes(
    case: FullCycleCase,
    *,
    actual_state: str,
    actual_goal: str,
) -> bool:
    """
    Memory acceptance is a secondary post-condition.

    Product truth for completed tasks: no active goal should remain after memory update.
    Internal clear/empty label differences are acceptable when current_goal is empty.
    """
    if case.expect_goal_state is None:
        return True

    goal_state_matches = actual_state == case.expect_goal_state
    if (
        not goal_state_matches
        and case.expect_goal_state in {"clear", "empty"}
        and actual_state in {"clear", "empty"}
        and not actual_goal.strip()
    ):
        goal_state_matches = True
    return goal_state_matches


def _extract_text(items: List[Dict[str, Any]]) -> str:
    chunks = [str(item.get("text_response") or "").strip() for item in items if item.get("text_response")]
    return " ".join(chunk for chunk in chunks if chunk).strip()


def _extract_command(items: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    for item in items:
        payload = item.get("command_payload")
        if isinstance(payload, dict):
            return payload
    return None


def _extract_route(items: List[Dict[str, Any]]) -> str:
    for item in items:
        if not item.get("is_final"):
            continue
        route = str(item.get("resolved_route") or item.get("route") or "").strip().lower()
        if route:
            return route
    for item in items:
        route = str(item.get("resolved_route") or item.get("route") or "").strip().lower()
        if route:
            return route
    return "none"


def _json_safe(value: Any) -> Any:
    if isinstance(value, bytes):
        return {
            "__type__": "bytes",
            "len": len(value),
        }
    if isinstance(value, dict):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, tuple):
        return [_json_safe(item) for item in value]
    return value


async def _run_request(service: GrpcServiceIntegration, request_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    async for item in service.process_request_complete(request_data):
        items.append(item)
    return items


async def _fetch_snapshot(db: DatabaseManager, hardware_id: str) -> Dict[str, Any]:
    memory = await db.get_user_memory(hardware_id)
    short_raw = str(memory.get("short") or "")
    long_raw = str(memory.get("long") or "")
    snapshot: Dict[str, Any] = {}
    if short_raw:
        try:
            snapshot = json.loads(short_raw)
        except Exception:
            snapshot = {"raw_short": short_raw}
    snapshot["_long"] = long_raw
    return snapshot


def _snapshot_signature(snapshot: Dict[str, Any]) -> tuple[str, str, str]:
    return (
        str(snapshot.get("goal_state") or ""),
        str(snapshot.get("current_goal") or ""),
        str(snapshot.get("_long") or ""),
    )


async def _wait_for_snapshot_update(
    db: DatabaseManager,
    hardware_id: str,
    previous_snapshot: Optional[Dict[str, Any]],
    *,
    timeout_sec: float = 2.0,
    poll_sec: float = 0.1,
) -> tuple[Dict[str, Any], bool]:
    deadline = asyncio.get_running_loop().time() + timeout_sec
    previous_signature = _snapshot_signature(previous_snapshot or {})
    latest = previous_snapshot or {}
    while True:
        latest = await _fetch_snapshot(db, hardware_id)
        current_signature = _snapshot_signature(latest)
        if previous_snapshot is None:
            # Give the background save path one chance to materialize something non-default.
            if current_signature != ("", "", ""):
                return latest, False
        elif current_signature != previous_signature:
            return latest, False
        if asyncio.get_running_loop().time() >= deadline:
            return latest, True
        await asyncio.sleep(poll_sec)


async def _ensure_user(db: DatabaseManager, hardware_id: str) -> None:
    existing = await db.get_user_by_hardware_id(hardware_id)
    if existing:
        return
    created = await db.create_user(
        hardware_id,
        metadata={
            "source": "live_goal_stack_matrix",
        },
    )
    if not created:
        raise RuntimeError(f"Failed to create test user for hardware_id={hardware_id}")


async def _build_live_stack() -> Dict[str, Any]:
    config = get_config()

    db = DatabaseManager(config.get_module_config("database"))
    ok = await db.initialize()
    if not ok:
        raise RuntimeError("DatabaseManager initialize failed")

    memory_adapter = MemoryManagementAdapter()
    await memory_adapter.initialize(config.get_module_config("memory"))
    memory_adapter.set_database_manager(db)

    memory_workflow = MemoryWorkflowIntegration(memory_manager=memory_adapter)
    ok = await memory_workflow.initialize()
    if not ok:
        raise RuntimeError("MemoryWorkflowIntegration initialize failed")

    text_module = TextProcessingModule()
    await text_module.initialize(config.get_module_config("text_processing"))

    audio_module = LightweightAudioModule()

    streaming = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
        memory_workflow=memory_workflow,
    )
    ok = await streaming.initialize()
    if not ok:
        raise RuntimeError("StreamingWorkflowIntegration initialize failed")

    service = GrpcServiceIntegration(
        streaming_workflow=streaming,
        memory_workflow=memory_workflow,
        interrupt_workflow=None,
    )
    ok = await service.initialize()
    if not ok:
        raise RuntimeError("GrpcServiceIntegration initialize failed")

    return {
        "config": config,
        "db": db,
        "memory_adapter": memory_adapter,
        "memory_workflow": memory_workflow,
        "text_module": text_module,
        "streaming": streaming,
        "service": service,
    }


async def _cleanup_live_stack(stack: Dict[str, Any]) -> None:
    for key in ("service", "streaming", "text_module", "memory_adapter"):
        obj = stack.get(key)
        cleanup = getattr(obj, "cleanup", None)
        if callable(cleanup):
            try:
                await cleanup()
            except Exception as exc:
                logger.warning("cleanup failed for %s: %s", key, exc)
    db = stack.get("db")
    if db:
        try:
            await db.cleanup()
        except Exception as exc:
            logger.warning("db cleanup failed: %s", exc)


async def run_memory_only(stack: Dict[str, Any]) -> Dict[str, Any]:
    adapter: MemoryManagementAdapter = stack["memory_adapter"]
    db: DatabaseManager = stack["db"]
    results: List[Dict[str, Any]] = []

    for case in MEMORY_CASES:
        hardware_id = f"live-mem-{case.case_id}-{uuid.uuid4().hex[:8]}"
        await _ensure_user(db, hardware_id)
        if case.seed_turns:
            await _seed_memory(adapter, hardware_id, case.seed_turns)
        response = await adapter.process(
            {
                "action": "update_background",
                "hardware_id": hardware_id,
                "prompt": case.prompt,
                "response": case.response,
            }
        )
        snapshot = await _fetch_snapshot(db, hardware_id)
        actual_goal = str(snapshot.get("current_goal") or "")
        actual_state = str(snapshot.get("goal_state") or "")
        passed = _memory_case_passes(
            case,
            actual_state=actual_state,
            actual_goal=actual_goal,
        )
        results.append(
            {
                "id": case.case_id,
                "hardware_id": hardware_id,
                "passed": passed,
                "expected_state": case.expected_state,
                "actual_state": actual_state,
                "actual_goal": actual_goal,
                "adapter_response": response,
            }
        )
        logger.info("memory_only %s -> %s", case.case_id, "PASS" if passed else "FAIL")

    return {
        "name": "memory_only",
        "passed": sum(1 for item in results if item["passed"]),
        "total": len(results),
        "results": results,
    }


async def _seed_memory(adapter: MemoryManagementAdapter, hardware_id: str, turns: List[tuple[str, str]]) -> None:
    for prompt, response in turns:
        await adapter.process(
            {
                "action": "update_background",
                "hardware_id": hardware_id,
                "prompt": prompt,
                "response": response,
            }
        )


async def _prepare_route_observation(
    *,
    adapter: MemoryManagementAdapter,
    text_module: TextProcessingModule,
    hardware_id: str,
    request: str,
    session_id: str,
) -> Dict[str, Any]:
    memory_context = await adapter.process(
        {
            "action": "get_context",
            "hardware_id": hardware_id,
            "user_input": request,
            "apply_medium_gate": True,
        }
    )
    runtime_memory_context = ""
    if isinstance(memory_context, dict):
        memory_payload = memory_context.get("memory") or {}
        runtime_memory_context = (
            "Current goal:\n"
            f"{memory_payload.get('current_goal_context', '')}\n\n"
            "Short-term memory:\n"
            f"{memory_payload.get('short_term_context', '')}\n\n"
            "Long-term memory:\n"
            f"{memory_payload.get('factual_long_term_context', '')}"
        )

    processor = text_module.get_processor()
    prepared = await processor.prepare_generation_request(
        request,
        session_id=session_id,
        runtime_memory_context=runtime_memory_context,
        has_image=False,
        use_google_search=None,
    )
    return {
        "memory_context": memory_context,
        "runtime_memory_context": runtime_memory_context,
        "prepared_request": prepared,
        "route": str((prepared or {}).get("route") or "none"),
    }


async def run_memory_and_classifier(stack: Dict[str, Any]) -> Dict[str, Any]:
    adapter: MemoryManagementAdapter = stack["memory_adapter"]
    text_module: TextProcessingModule = stack["text_module"]
    results: List[Dict[str, Any]] = []

    for case in CLASSIFIER_CASES:
        hardware_id = f"live-cls-{case.case_id}-{uuid.uuid4().hex[:8]}"
        await _ensure_user(stack["db"], hardware_id)
        if case.seed_turns:
            await _seed_memory(adapter, hardware_id, case.seed_turns)
        prepared_result = await _prepare_route_observation(
            adapter=adapter,
            text_module=text_module,
            hardware_id=hardware_id,
            request=case.request,
            session_id=f"live-cls-{case.case_id}",
        )
        prepared = prepared_result["prepared_request"]
        actual_route = prepared_result["route"]
        passed = actual_route == case.expected_route
        results.append(
            {
                "id": case.case_id,
                "hardware_id": hardware_id,
                "passed": passed,
                "expected_route": case.expected_route,
                "actual_route": actual_route,
                "prepared": prepared,
                "runtime_memory_context": prepared_result["runtime_memory_context"],
            }
        )
        logger.info("memory_classifier %s -> %s", case.case_id, "PASS" if passed else "FAIL")

    return {
        "name": "memory_classifier",
        "passed": sum(1 for item in results if item["passed"]),
        "total": len(results),
        "results": results,
    }


async def run_full_cycle(stack: Dict[str, Any]) -> Dict[str, Any]:
    service: GrpcServiceIntegration = stack["service"]
    adapter: MemoryManagementAdapter = stack["memory_adapter"]
    text_module: TextProcessingModule = stack["text_module"]
    db: DatabaseManager = stack["db"]
    results: List[Dict[str, Any]] = []
    run_suffix = uuid.uuid4().hex[:8]
    snapshots_by_hardware: Dict[str, Dict[str, Any]] = {}

    for idx, case in enumerate(FULL_CYCLE_CASES, start=1):
        run_hardware_id = f"{case.hardware_id}-{run_suffix}"
        await _ensure_user(db, run_hardware_id)
        if case.seed_turns and run_hardware_id not in snapshots_by_hardware:
            await _seed_memory(stack["memory_adapter"], run_hardware_id, case.seed_turns)
            snapshots_by_hardware[run_hardware_id] = await _fetch_snapshot(db, run_hardware_id)
        session_id = str(uuid.uuid4())
        prepared_result = await _prepare_route_observation(
            adapter=adapter,
            text_module=text_module,
            hardware_id=run_hardware_id,
            request=case.request,
            session_id=session_id,
        )
        items = await _run_request(
            service,
            {
                "text": case.request,
                "session_id": session_id,
                "hardware_id": run_hardware_id,
            },
        )
        text = _extract_text(items)
        command_payload = _extract_command(items)
        command = None
        if isinstance(command_payload, dict):
            command = str((command_payload.get("payload") or {}).get("command") or "")
        snapshot, snapshot_timeout = await _wait_for_snapshot_update(
            db,
            run_hardware_id,
            snapshots_by_hardware.get(run_hardware_id),
        )
        snapshots_by_hardware[run_hardware_id] = snapshot
        actual_goal = str(snapshot.get("current_goal") or "")
        actual_state = str(snapshot.get("goal_state") or "")
        if not actual_state and not actual_goal:
            actual_state = "empty"
        route = prepared_result["route"]
        execution_pass = _execution_passes(
            case,
            command=command,
            text=text,
        )
        memory_pass = _memory_passes(
            case,
            actual_state=actual_state,
            actual_goal=actual_goal,
        )
        passed = execution_pass
        results.append(
            {
                "id": case.case_id,
                "hardware_id": run_hardware_id,
                "request": case.request,
                "passed": passed,
                "execution_pass": execution_pass,
                "memory_pass": memory_pass,
                "session_id": session_id,
                "expected_route": case.expected_route,
                "route_observed": route,
                "expected_command": case.expected_command,
                "actual_command": command,
                "text": text,
                "goal_state": actual_state,
                "current_goal": actual_goal,
                "snapshot_timeout": snapshot_timeout,
                "items": _json_safe(items),
            }
        )
        logger.info(
            "full_cycle %s -> exec=%s memory=%s",
            case.case_id,
            "PASS" if execution_pass else "FAIL",
            "PASS" if memory_pass else "FAIL",
        )

    return {
        "name": "full_cycle",
        "passed": sum(1 for item in results if item["execution_pass"]),
        "memory_passed": sum(1 for item in results if item["memory_pass"]),
        "total": len(results),
        "results": results,
    }


async def main() -> int:
    stack = await _build_live_stack()
    try:
        suites = []
        suites.append(await run_memory_only(stack))
        suites.append(await run_memory_and_classifier(stack))
        suites.append(await run_full_cycle(stack))

        summary = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "root": str(ROOT),
            "gate_set": SELECTED_GATE_NAME,
            "suites": suites,
        }
        out_path = ROOT / "Docs" / "assistant_exchange" / "codex" / f"live_goal_stack_matrix_result__{SELECTED_GATE_NAME}.json"
        out_path.write_text(json.dumps(_json_safe(summary), ensure_ascii=False, indent=2), encoding="utf-8")

        print(json.dumps(_json_safe(summary), ensure_ascii=False, indent=2))

        failed = False
        for suite in suites:
            if suite["name"] == "full_cycle":
                if suite["passed"] != suite["total"] or suite["memory_passed"] != suite["total"]:
                    failed = True
                    break
            elif suite["passed"] != suite["total"]:
                failed = True
                break
        return 1 if failed else 0
    finally:
        await _cleanup_live_stack(stack)


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
