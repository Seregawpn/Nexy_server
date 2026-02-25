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

    async def process(self, payload):
        # Payload is expected to contain enriched text under "text"
        self.captured_input = payload

        async def _gen():
            yield {"text_response": '{"text":"ok"}'}

        return _gen()


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
            "recent_context": "User asked to remember preference",
            "long_term_context": "User likes sports",
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
    assert "SYSTEM_CONTEXT:" in llm_input_text
    assert "Memory Context (recent): User asked to remember preference" in llm_input_text
    assert "Memory Context (long-term): User likes sports" in llm_input_text
