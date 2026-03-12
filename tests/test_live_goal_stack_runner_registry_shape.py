from pathlib import Path
import sys
from types import SimpleNamespace
import pytest


project_root = Path(__file__).parent.parent
tests_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(tests_root))

from goal_stack_gate_registry import CANONICAL_20_CASE_GATE
from scripts.run_live_goal_stack_matrix import (
    _prepare_route_observation,
    _memory_case_passes,
    _build_registry_classifier_cases,
    _build_registry_live_cases,
    _build_registry_memory_cases,
)


def test_live_goal_stack_runner_uses_registry_owner_counts_for_memory_cases():
    cases = _build_registry_memory_cases(CANONICAL_20_CASE_GATE)

    assert len(cases) == 16


def test_live_goal_stack_runner_uses_registry_owner_counts_for_classifier_cases():
    cases = _build_registry_classifier_cases(CANONICAL_20_CASE_GATE)

    assert len(cases) == 20


def test_live_goal_stack_runner_uses_registry_owner_counts_for_live_cases():
    cases = _build_registry_live_cases(CANONICAL_20_CASE_GATE)

    assert len(cases) == 20


def test_live_goal_stack_runner_memory_accepts_terminal_clear_empty_equivalence():
    case = next(case for case in _build_registry_memory_cases(CANONICAL_20_CASE_GATE) if case.case_id == "m05_browser_direct")

    assert case.expected_state == "clear"
    assert _memory_case_passes(case, actual_state="empty", actual_goal="") is True


def test_live_goal_stack_runner_registry_memory_pairs_match_continuation_turns():
    memory_cases = {case.case_id: case for case in _build_registry_memory_cases(CANONICAL_20_CASE_GATE)}

    assert memory_cases["m06_browser_followup_short"].prompt == "swap it over to sleep sounds"
    assert memory_cases["m06_browser_followup_short"].response == "Opening YouTube to play sleep sounds."
    assert memory_cases["m08_search_followup_topic"].prompt == "global affairs"
    assert memory_cases["m08_search_followup_topic"].response == "Here are the latest global affairs headlines."
    assert memory_cases["m14_replace_browser_to_message"].prompt == "Skip that, text Sophia"
    assert memory_cases["m14_replace_browser_to_message"].response == "What message would you like to send to Sophia?"


@pytest.mark.asyncio
async def test_live_goal_stack_runner_prepares_route_from_current_memory_owner_path():
    class _Adapter:
        async def process(self, payload):
            assert payload["action"] == "get_context"
            return {
                "memory": {
                    "current_goal_context": "User wants to send a message to Sophia. Missing detail: message text.",
                    "short_term_context": "CURRENT_TURN:\nUSER: send a message to Sophia\nASSISTANT: What message would you like to send to Sophia?",
                    "factual_long_term_context": "",
                }
            }

    class _Processor:
        async def prepare_generation_request(self, text, **kwargs):
            assert "User wants to send a message to Sophia" in kwargs["runtime_memory_context"]
            return {"route": "messages", "user_input": text}

    text_module = SimpleNamespace(get_processor=lambda: _Processor())
    prepared = await _prepare_route_observation(
        adapter=_Adapter(),
        text_module=text_module,
        hardware_id="hw-route",
        request="tell her i am outside",
        session_id="sess-route",
    )

    assert prepared["route"] == "messages"
    assert prepared["prepared_request"]["route"] == "messages"
