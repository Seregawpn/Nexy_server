import json
from pathlib import Path
import sys

import pytest

project_root = Path(__file__).parent.parent
tests_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(tests_root))

from modules.memory_management.core.memory_manager import MemoryManager
from goal_stack_gate_registry import CANONICAL_20_CASE_GATE, SUPPLEMENTAL_20_CASE_GATE


class _StatefulFakeDB:
    def __init__(self):
        self.short = ""
        self.long = ""

    async def get_user_memory(self, hardware_id: str):
        return {"short": self.short, "long": self.long}

    async def update_user_memory(self, hardware_id: str, short_memory: str, long_memory: str):
        self.short = short_memory
        self.long = long_memory
        return True


class _CaseAnalyzer:
    def __init__(self, short_memory: str, long_memory: str, current_goal: str):
        self.short_memory = short_memory
        self.long_memory = long_memory
        self.current_goal = current_goal

    async def analyze_conversation(self, prompt, response, **kwargs):
        return self.short_memory, "", self.long_memory, self.current_goal


class _GoalStateCaseAnalyzer:
    def __init__(self, short_memory: str, long_memory: str, current_goal: str, goal_state: str):
        self.short_memory = short_memory
        self.long_memory = long_memory
        self.current_goal = current_goal
        self.goal_state = goal_state

    async def analyze_conversation(self, prompt, response, **kwargs):
        return self.short_memory, "", self.long_memory, self.current_goal, self.goal_state


MEMORY_GATE_CASES = [case for case in CANONICAL_20_CASE_GATE if case.memory_prompt is not None]
SUPPLEMENTAL_MEMORY_GATE_CASES = [case for case in SUPPLEMENTAL_20_CASE_GATE if case.memory_prompt is not None]


@pytest.mark.asyncio
@pytest.mark.parametrize("case", MEMORY_GATE_CASES, ids=[case.case_id for case in MEMORY_GATE_CASES])
async def test_memory_basic_goal_matrix(case):
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _CaseAnalyzer(
        short_memory=f"[2026-03-07 00:00:00 UTC] USER: {case.memory_prompt} | ASSISTANT: {case.memory_response}",
        long_memory=case.memory_analyzer_long,
        current_goal=case.memory_current_goal or "",
    )

    updated = await manager.update_memory_background(
        hardware_id=f"hw-basic-goal-{case.case_id}",
        prompt=case.memory_prompt or "",
        response=case.memory_response or "",
    )

    assert updated is not None

    payload = json.loads(db.short)
    assert payload.get("current_goal", "") == (case.memory_expected_goal or "")
    assert payload.get("factual_long", "") == case.memory_expected_long

    context = await manager.get_memory_context(
        hardware_id=f"hw-basic-goal-{case.case_id}",
        user_input=case.memory_prompt,
    )

    assert context.get("current_goal_context", "") == (case.memory_expected_goal or "")
    assert context.get("factual_long_term_context", "") == case.memory_expected_long


@pytest.mark.asyncio
@pytest.mark.parametrize("case", SUPPLEMENTAL_MEMORY_GATE_CASES, ids=[case.case_id for case in SUPPLEMENTAL_MEMORY_GATE_CASES])
async def test_memory_additional_goal_matrix(case):
    await test_memory_basic_goal_matrix(case)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "case_name,prompt,response,analyzer_long,expected_long",
    [
        ("remember_name", "Remember this: my name is Sergiy", "I will remember that.", "User's first name is Sergiy.", "User's first name is Sergiy."),
        ("remember_preference", "Remember this: I like running", "I will remember that.", "User likes running.", "User likes running."),
        ("dont_store_transient_task", "Find me white sneakers", "I found several white sneaker options.", "", ""),
        ("remember_timezone", "Remember this: I live in Toronto timezone", "I will remember that.", "User timezone is Toronto.", "User timezone is Toronto."),
        ("remember_language", "Remember this: I prefer English", "I will remember that.", "User prefers English.", "User prefers English."),
    ],
)
async def test_memory_long_term_profile_matrix(
    case_name: str,
    prompt: str,
    response: str,
    analyzer_long: str,
    expected_long: str,
):
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _CaseAnalyzer(
        short_memory=f"[2026-03-07 00:00:00 UTC] USER: {prompt} | ASSISTANT: {response}",
        long_memory=analyzer_long,
        current_goal="",
    )

    updated = await manager.update_memory_background(
        hardware_id=f"hw-basic-goal-{case_name}",
        prompt=prompt,
        response=response,
    )

    assert updated is not None

    payload = json.loads(db.short)
    assert payload.get("factual_long", "") == expected_long

    context = await manager.get_memory_context(
        hardware_id=f"hw-basic-goal-{case_name}",
        user_input=prompt,
    )

    assert context.get("factual_long_term_context", "") == expected_long


@pytest.mark.asyncio
async def test_memory_goal_state_clear_forces_empty_current_goal():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _GoalStateCaseAnalyzer(
        short_memory="[2026-03-07 00:00:00 UTC] USER: Tell her I'll be late | ASSISTANT: Sending your message to Sophia.",
        long_memory="",
        current_goal="User wants to send a message to Sophia.",
        goal_state="clear",
    )

    updated = await manager.update_memory_background(
        hardware_id="hw-goal-state-clear",
        prompt="Tell her I'll be late",
        response="Sending your message to Sophia.",
    )

    assert updated is not None
    payload = json.loads(db.short)
    assert payload.get("goal_state") == "clear"
    assert payload.get("current_goal") == ""


@pytest.mark.asyncio
async def test_memory_goal_state_replace_without_goal_fails_closed_to_empty():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _GoalStateCaseAnalyzer(
        short_memory="[2026-03-07 00:00:00 UTC] USER: No, open Safari instead | ASSISTANT: Opening Safari.",
        long_memory="",
        current_goal="",
        goal_state="replace",
    )

    updated = await manager.update_memory_background(
        hardware_id="hw-goal-state-replace-empty",
        prompt="No, open Safari instead",
        response="Opening Safari.",
    )

    assert updated is not None
    payload = json.loads(db.short)
    assert payload.get("goal_state") == "empty"
    assert payload.get("current_goal") == ""
