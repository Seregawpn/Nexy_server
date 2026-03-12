from pathlib import Path
import sys
from unittest.mock import AsyncMock, Mock, patch

import pytest
import pytest_asyncio

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.workflow_integrations.streaming_workflow_integration import (
    StreamingWorkflowIntegration,
)


class _ScenarioTextModule:
    def __init__(self, route: str, response_chunk):
        self.is_initialized = True
        self.name = "text_processing"
        self._route = route
        self._response_chunk = response_chunk
        self._processor = Mock()
        self._processor.live_provider = Mock()
        self._processor.prepare_generation_request = AsyncMock(side_effect=self._prepare_generation_request)

    async def _prepare_generation_request(
        self,
        text,
        session_id=None,
        runtime_memory_context=None,
        has_image=False,
        use_google_search=None,
    ):
        return {
            "route_flags": {"route": self._route},
            "user_input": text,
            "route": self._route,
            "use_google_search": False,
        }

    async def process(self, payload):
        async def _gen():
            yield self._response_chunk

        return _gen()

    def get_processor(self):
        return self._processor


@pytest_asyncio.fixture
async def workflow_factory():
    async def _make(route: str, response_chunk, memory_context: dict):
        text_module = _ScenarioTextModule(route=route, response_chunk=response_chunk)

        audio_module = Mock()
        audio_module.is_initialized = True
        audio_module.name = "audio_generation"
        audio_module.process = AsyncMock(return_value=None)

        memory_workflow = Mock()
        memory_workflow.is_initialized = True
        memory_workflow.prefetch_memory = AsyncMock()
        memory_workflow.get_memory_context_parallel = AsyncMock(return_value=memory_context)

        workflow = StreamingWorkflowIntegration(
            text_processor=text_module,
            audio_processor=audio_module,
            memory_workflow=memory_workflow,
        )
        await workflow.initialize()
        return workflow

    return _make


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "route,response_chunk,memory_context,expected_final_lifecycle",
    [
        (
            "messages",
            '{"text":"What message would you like to send to Sophia?"}',
            {
                "goal_state_context": "set",
                "current_goal_context": "User wants to send a message to Sophia. Missing detail: message text.",
                "short_term_context": "",
                "medium_term_context": "",
                "factual_long_term_context": "",
            },
            "task_opened",
        ),
        (
            "messages",
            '{"command":"send_message","args":{"contact":"Sophia","message":"I am outside"},"text":"Sending your message to Sophia."}',
            {
                "goal_state_context": "clear",
                "current_goal_context": "",
                "short_term_context": "",
                "medium_term_context": "",
                "factual_long_term_context": "",
            },
            "task_closed",
        ),
        (
            "google_search",
            '{"text":"Here are the latest world headlines."}',
            {
                "goal_state_context": "empty",
                "current_goal_context": "",
                "short_term_context": "",
                "medium_term_context": "",
                "factual_long_term_context": "",
            },
            "task_inactive",
        ),
    ],
)
async def test_current_streaming_path_logs_runtime_v2_signal_scenarios(
    workflow_factory,
    route,
    response_chunk,
    memory_context,
    expected_final_lifecycle,
):
    workflow = await workflow_factory(route, response_chunk, memory_context)
    request_data = {
        "text": "test request",
        "session_id": f"sid-{route}",
        "hardware_id": f"hw-{route}",
    }

    with patch(
        "integrations.workflow_integrations.streaming_workflow_integration._log_request_path_workflow"
    ) as mock_log:
        async for _ in workflow._process_request_streaming_current(request_data):
            pass

    v2_signal_calls = [
        call for call in mock_log.call_args_list if call.args and call.args[0] == "workflow.v2_signals"
    ]
    assert len(v2_signal_calls) >= 2

    memory_call = next(call for call in v2_signal_calls if call.kwargs.get("phase") == "memory")
    final_call = next(call for call in v2_signal_calls if call.kwargs.get("phase") == "final")

    assert memory_call.kwargs["goal_state"] == memory_context["goal_state_context"]
    assert final_call.kwargs["route"] == route
    assert final_call.kwargs["goal_state"] == memory_context["goal_state_context"]
    assert final_call.kwargs["lifecycle"] == expected_final_lifecycle


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "route,response_chunk,memory_context",
    [
        (
            "none",
            '{"text":"Hello! How can I help?"}',
            {
                "goal_state_context": "empty",
                "current_goal_context": "",
                "short_term_context": "",
                "medium_term_context": "",
                "factual_long_term_context": "",
            },
        ),
        (
            "describe",
            '{"text":"I can see a browser window with a search page."}',
            {
                "goal_state_context": "empty",
                "current_goal_context": "",
                "short_term_context": "",
                "medium_term_context": "",
                "factual_long_term_context": "",
            },
        ),
        (
            "messages",
            '{"command":"send_message","args":{"contact":"Sophia","message":"Hi"},"text":"Sending your message to Sophia."}',
            {
                "goal_state_context": "clear",
                "current_goal_context": "",
                "short_term_context": "",
                "medium_term_context": "",
                "factual_long_term_context": "",
            },
        ),
    ],
)
async def test_current_streaming_path_logs_request_timing_snapshot(
    workflow_factory,
    route,
    response_chunk,
    memory_context,
):
    workflow = await workflow_factory(route, response_chunk, memory_context)
    request_data = {
        "text": "test request",
        "session_id": f"sid-timing-{route}",
        "hardware_id": f"hw-timing-{route}",
    }

    with patch(
        "integrations.workflow_integrations.streaming_workflow_integration._log_request_path_workflow"
    ) as mock_log:
        async for _ in workflow._process_request_streaming_current(request_data):
            pass

    timing_calls = [
        call for call in mock_log.call_args_list if call.args and call.args[0] == "workflow.timing"
    ]
    assert len(timing_calls) == 1

    timing_call = timing_calls[0]
    assert timing_call.kwargs["memory_done_elapsed_ms"] >= 0
    assert timing_call.kwargs["memory_done_absolute_ms"] >= 0
    assert timing_call.kwargs["route_done_elapsed_ms"] >= 0
    assert timing_call.kwargs["first_chunk_elapsed_ms"] >= 0
    assert timing_call.kwargs["first_chunk_absolute_ms"] >= 0
    assert timing_call.kwargs["final_flush_done_elapsed_ms"] >= 0
    assert timing_call.kwargs["parse_done_elapsed_ms"] >= 0
    assert timing_call.kwargs["command_done_elapsed_ms"] >= 0
    assert timing_call.kwargs["persist_done_elapsed_ms"] >= 0
    assert timing_call.kwargs["request_done_elapsed_ms"] >= 0
    assert timing_call.kwargs["request_done_absolute_ms"] >= 0
