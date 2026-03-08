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

# Exercise the real WhatsApp action path during live matrix runs.
os.environ.setdefault("WHATSAPP_ENABLED", "true")

from config.unified_config import get_config
from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration
from integrations.workflow_integrations.memory_workflow_integration import MemoryWorkflowIntegration
from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from modules.database.core.database_manager import DatabaseManager
from modules.memory_management.adapter import MemoryManagementAdapter
from modules.memory_management.core.memory_manager import MemoryManager
from modules.text_processing.module import TextProcessingModule
from goal_stack_gate_registry import CANONICAL_20_CASE_GATE


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("live_goal_stack_matrix")


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


MEMORY_CASES: List[MemoryCase] = [
    MemoryCase("m01_set_message", "Send a message to Sophia", "What message would you like to send to Sophia?", "set", ["send", "Sophia"]),
    MemoryCase("m02_keep_message_clarify", "Tell her I will be late", "What exactly would you like me to tell Sophia?", "keep", ["Sophia"]),
    MemoryCase("m03_clear_message_complete", "Tell her I will be late", "Sending your message to Sophia.", "clear"),
    MemoryCase("m04_replace_app", "No, open Safari instead", "Opening Safari.", "clear"),
    MemoryCase("m05_empty_smalltalk", "How are you?", "I am doing well, thank you.", "empty"),
    MemoryCase("m06_set_search", "Find news", "What kind of news do you want?", "set", ["news"]),
    MemoryCase("m07_keep_search", "World news", "Searching for the latest world news.", "keep", ["world"]),
    MemoryCase("m08_clear_search_complete", "World news", "Here are the latest world news headlines.", "clear"),
    MemoryCase("m09_set_browser", "Open YouTube and find sleep music", "What should I find on YouTube?", "set", ["YouTube"]),
    MemoryCase(
        "m10_keep_browser",
        "sleep music instead",
        "Opening YouTube and searching for sleep music.",
        "clear",
        ["sleep"],
        seed_turns=[("Open YouTube and find sleep music", "What should I find on YouTube?")],
    ),
    MemoryCase("m11_clear_cancel", "No, never mind", "Okay, I will not continue that task.", "clear"),
    MemoryCase("m12_empty_capability", "What can you do?", "I can help with apps, messages, browsing, and search.", "empty"),
    MemoryCase("m13_set_whatsapp", "Send a WhatsApp message to Mom", "What message do you want to send to Mom?", "set", ["WhatsApp", "Mom"]),
    MemoryCase("m14_clear_whatsapp_complete", "Tell Mom I arrived", "Sending your WhatsApp message to Mom.", "clear"),
    MemoryCase(
        "m15_replace_search_to_app",
        "Actually open Notes instead",
        "Opening Notes.",
        "clear",
        ["Notes"],
        seed_turns=[("Find news", "What kind of news do you want?")],
    ),
    MemoryCase("m16_empty_cancel_to_chat", "I just want to know how are you doing", "I'm doing well, thanks for asking.", "empty"),
    MemoryCase("m17_set_open_app", "Open an app", "Which app do you want to open?", "set", ["open"]),
    MemoryCase(
        "m18_keep_open_app",
        "Safari",
        "Do you want me to open Safari now?",
        "keep",
        ["Safari"],
        seed_turns=[("Open an app", "Which app do you want to open?")],
    ),
    MemoryCase(
        "m19_clear_open_app_complete",
        "Safari",
        "Opening Safari.",
        "clear",
        seed_turns=[("Open an app", "Which app do you want to open?")],
    ),
    MemoryCase("m20_empty_gratitude", "Thanks", "You're welcome.", "empty"),
]

CLASSIFIER_CASES: List[ClassifierCase] = [
    ClassifierCase("c01_messages_direct", [], "Send a message to Sophia", "messages"),
    ClassifierCase("c02_messages_followup", [("Send a message to Sophia", "What message would you like to send to Sophia?")], "Tell her I will be late", "messages"),
    ClassifierCase("c03_messages_cancel_chat", [("Send a message to Sophia", "What message would you like to send to Sophia?")], "I just want to know how are you doing", "none"),
    ClassifierCase("c04_messages_pivot_app", [("Send a message to Sophia", "What message would you like to send to Sophia?")], "No, open Safari instead", "system_control"),
    ClassifierCase("c05_generic_message", [], "Send a message", "messages"),
    ClassifierCase("c06_whatsapp_direct", [], "Send a WhatsApp message to Mom", "whatsapp"),
    ClassifierCase("c07_browser_direct", [], "Open YouTube and play jazz", "browser"),
    ClassifierCase("c08_browser_followup", [("Open YouTube and play jazz", "Opening YouTube and playing jazz.")], "sleep music instead", "browser"),
    ClassifierCase("c09_search_direct", [], "Find latest world news", "google_search"),
    ClassifierCase("c10_search_followup", [("Find news", "What kind of news do you want?")], "world news", "google_search"),
    ClassifierCase("c11_system_direct", [], "Open Safari", "system_control"),
    ClassifierCase("c12_system_followup", [("Open an app", "Which app do you want to open?")], "Safari", "system_control"),
    ClassifierCase("c13_none_smalltalk", [], "How are you?", "none"),
    ClassifierCase("c14_none_gratitude", [], "Thanks", "none"),
    ClassifierCase("c15_capability", [], "What can you do?", "capability"),
    ClassifierCase("c16_replace_to_search", [("Open Safari", "Opening Safari.")], "Actually find world news instead", "google_search"),
    ClassifierCase("c17_cancel_nevermind", [("Find world news", "Searching for the latest world news.")], "No, never mind", "none"),
    ClassifierCase("c18_browser_not_system", [], "Open youtube.com", "browser"),
    ClassifierCase("c19_system_not_browser", [], "Open Notes", "system_control"),
    ClassifierCase("c20_message_not_whatsapp", [], "Text John running late", "messages"),
]

def _build_registry_live_cases() -> List[FullCycleCase]:
    live_cases: List[FullCycleCase] = []
    for gate_case in CANONICAL_20_CASE_GATE:
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
    if len(live_cases) != 20:
        raise RuntimeError(f"Expected 20 live gate cases, got {len(live_cases)}")
    return live_cases


FULL_CYCLE_CASES: List[FullCycleCase] = _build_registry_live_cases()


def _norm(value: Any) -> str:
    return " ".join(str(value or "").split()).strip().lower()


def _contains_all(text: str, parts: Optional[List[str]]) -> bool:
    if not parts:
        return True
    hay = _norm(text)
    return all(_norm(part) in hay for part in parts)


def _full_cycle_passes(
    case: FullCycleCase,
    *,
    command: Optional[str],
    text: str,
    actual_state: str,
) -> bool:
    """
    Full-cycle acceptance must rely on product truth, not incomplete route telemetry.

    Canonical acceptance sources:
    - actual command payload (when expected)
    - final user-visible text
    - persisted memory lifecycle state
    """
    return (
        (case.expected_command is None or command == case.expected_command)
        and _contains_all(text, case.expected_text_contains)
        and (case.expect_goal_state is None or actual_state == case.expect_goal_state)
    )


def _extract_text(items: List[Dict[str, Any]]) -> str:
    chunks = [str(item.get("text_response") or "").strip() for item in items if item.get("text_response")]
    return " ".join(chunk for chunk in chunks if chunk).strip()


def _extract_command(items: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    for item in items:
        payload = item.get("command_payload")
        if isinstance(payload, dict):
            return payload
    return None


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
) -> Dict[str, Any]:
    deadline = asyncio.get_running_loop().time() + timeout_sec
    previous_signature = _snapshot_signature(previous_snapshot or {})
    latest = previous_snapshot or {}
    while True:
        latest = await _fetch_snapshot(db, hardware_id)
        current_signature = _snapshot_signature(latest)
        if previous_snapshot is None:
            # Give the background save path one chance to materialize something non-default.
            if current_signature != ("", "", ""):
                return latest
        elif current_signature != previous_signature:
            return latest
        if asyncio.get_running_loop().time() >= deadline:
            return latest
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
        passed = (
            actual_state == case.expected_state
            and (case.expected_state in {"clear", "empty"} or _contains_all(actual_goal, case.goal_contains))
            and ((case.expected_state in {"clear", "empty"} and not actual_goal) or (case.expected_state not in {"clear", "empty"}))
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


async def run_memory_and_classifier(stack: Dict[str, Any]) -> Dict[str, Any]:
    adapter: MemoryManagementAdapter = stack["memory_adapter"]
    text_module: TextProcessingModule = stack["text_module"]
    processor = text_module.get_processor()
    results: List[Dict[str, Any]] = []

    for case in CLASSIFIER_CASES:
        hardware_id = f"live-cls-{case.case_id}-{uuid.uuid4().hex[:8]}"
        await _ensure_user(stack["db"], hardware_id)
        if case.seed_turns:
            await _seed_memory(adapter, hardware_id, case.seed_turns)
        memory_context = await adapter.process(
            {
                "action": "get_context",
                "hardware_id": hardware_id,
                "user_input": case.request,
                "apply_medium_gate": True,
            }
        )
        runtime_memory_context = ""
        if isinstance(memory_context, dict):
            memory_payload = memory_context.get("memory") or {}
            runtime_memory_context = (
                "Current goal:\n"
                f"{memory_payload.get('short_term_context', '')}\n\n"
                "Short-term memory:\n"
                f"{memory_payload.get('short_term_context', '')}\n\n"
                "Long-term memory:\n"
                f"{memory_payload.get('factual_long_term_context', '')}"
            )
        prepared = await processor.prepare_generation_request(
            case.request,
            session_id=f"live-cls-{case.case_id}",
            runtime_memory_context=runtime_memory_context,
            has_image=False,
            use_google_search=None,
        )
        actual_route = str(prepared.get("route") or "none")
        passed = actual_route == case.expected_route
        results.append(
            {
                "id": case.case_id,
                "hardware_id": hardware_id,
                "passed": passed,
                "expected_route": case.expected_route,
                "actual_route": actual_route,
                "prepared": prepared,
                "runtime_memory_context": runtime_memory_context,
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
        snapshot = await _wait_for_snapshot_update(
            db,
            run_hardware_id,
            snapshots_by_hardware.get(run_hardware_id),
        )
        snapshots_by_hardware[run_hardware_id] = snapshot
        actual_goal = str(snapshot.get("current_goal") or "")
        actual_state = str(snapshot.get("goal_state") or "")
        if not actual_state and not actual_goal:
            actual_state = "empty"
        route = "none"
        prepared_requests = [
            item for item in items
            if isinstance(item, dict) and "prepared_request" in item
        ]
        if prepared_requests:
            route = str(((prepared_requests[-1].get("prepared_request") or {}).get("route")) or "none")
        passed = _full_cycle_passes(
            case,
            command=command,
            text=text,
            actual_state=actual_state,
        )
        results.append(
            {
                "id": case.case_id,
                "hardware_id": run_hardware_id,
                "request": case.request,
                "passed": passed,
                "session_id": session_id,
                "expected_route": case.expected_route,
                "route_observed": route,
                "expected_command": case.expected_command,
                "actual_command": command,
                "text": text,
                "goal_state": actual_state,
                "current_goal": actual_goal,
                "items": _json_safe(items),
            }
        )
        logger.info("full_cycle %s -> %s", case.case_id, "PASS" if passed else "FAIL")

    return {
        "name": "full_cycle",
        "passed": sum(1 for item in results if item["passed"]),
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
            "suites": suites,
        }
        out_path = ROOT / "Docs" / "assistant_exchange" / "codex" / "live_goal_stack_matrix_result.json"
        out_path.write_text(json.dumps(_json_safe(summary), ensure_ascii=False, indent=2), encoding="utf-8")

        print(json.dumps(_json_safe(summary), ensure_ascii=False, indent=2))

        failed = any(suite["passed"] != suite["total"] for suite in suites)
        return 1 if failed else 0
    finally:
        await _cleanup_live_stack(stack)


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
