import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, Mock

from integrations.workflow_integrations.streaming_workflow_integration import (
    StreamingWorkflowIntegration,
)


class _CaptureTextModule:
    def __init__(self):
        self.is_initialized = True
        self.name = "text_processing"
        self.captured_input = None
        self._processor = Mock()
        self._processor.live_provider = Mock()
        self._processor.prepare_generation_request = AsyncMock(side_effect=self._prepare_generation_request)

    async def _prepare_generation_request(self, text, session_id=None, runtime_memory_context=None, has_image=False, use_google_search=None):
        route = "whatsapp" if "whatsapp" in str(text).lower() else "none"
        return {
            "system_prompt_override": "prompt",
            "sections": {"primary_route": route},
            "normalized_text": text,
            "routing_system_context": "",
            "primary_route": route,
            "use_google_search": False,
        }

    async def process(self, payload):
    # Payload now carries plain user text + separate runtime_memory_context.
        self.captured_input = payload
        async def _gen():
            yield {"text_response": '{"text":"ok"}'}

        return _gen()

    def get_processor(self):
        return self._processor


@pytest_asyncio.fixture
async def workflow_with_memory():
    text_module = _CaptureTextModule()

    audio_module = Mock()
    audio_module.is_initialized = True
    audio_module.name = "audio_generation"
    audio_module.process = AsyncMock(return_value=None)

    memory_workflow = Mock()
    memory_workflow.is_initialized = True
    memory_workflow.prefetch_memory = AsyncMock()
    memory_workflow.get_memory_context_parallel = AsyncMock(
        return_value={
            "short_term_context": "User asked to remember preference",
            "factual_long_term_context": "User likes sports",
        }
    )

    workflow = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
        memory_workflow=memory_workflow,
    )
    await workflow.initialize()
    return workflow, text_module


@pytest.mark.asyncio
async def test_memory_is_injected_into_llm_input_payload(workflow_with_memory):
    workflow, text_module = workflow_with_memory

    request_data = {
        "text": "Что ты помнишь про меня?",
        "session_id": "s-1",
        "hardware_id": "h-1",
    }

    async for _ in workflow.process_request_streaming(request_data):
        pass

    assert text_module.captured_input is not None
    llm_input_text = str(text_module.captured_input.get("text", ""))
    llm_runtime_memory = str(text_module.captured_input.get("runtime_memory_context", ""))
    assert llm_input_text == "Что ты помнишь про меня?"
    assert "MEMORY_CONTEXT:" not in llm_input_text
    assert "Short-term memory:" in llm_runtime_memory
    assert "User asked to remember preference" in llm_runtime_memory
    assert "Long-term memory:" in llm_runtime_memory
    assert "User likes sports" in llm_runtime_memory


@pytest.mark.asyncio
async def test_follow_up_does_not_inject_previous_route_context(workflow_with_memory):
    workflow, text_module = workflow_with_memory

    first = {
        "text": "send to Sophia in WhatsApp how are you doing",
        "session_id": "s-route",
        "hardware_id": "h-route",
    }
    async for _ in workflow.process_request_streaming(first):
        pass

    ctx = workflow._session_registry.get_session_context("s-route")
    assert "last_primary_route" not in ctx

    second = {
        "text": "tell me more",
        "session_id": "s-route",
        "hardware_id": "h-route",
    }
    async for _ in workflow.process_request_streaming(second):
        pass

    llm_input_text = str(text_module.captured_input.get("text", ""))
    assert "Routing Context (previous-primary-route):" not in llm_input_text
