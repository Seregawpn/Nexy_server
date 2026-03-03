import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, Mock

from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration
from integrations.workflow_integrations.streaming_workflow_integration import (
    StreamingWorkflowIntegration,
)


class _InMemoryMemoryWorkflow:
    def __init__(self):
        self.is_initialized = True
        self._db = {}

    async def prefetch_memory(self, hardware_id: str):
        return True

    async def get_memory_context_parallel(self, hardware_id: str):
        return self._db.get(hardware_id)

    async def save_to_memory_background(self, data):
        hardware_id = data.get("hardware_id")
        prompt = str(data.get("prompt") or "").lower()

        if not hardware_id:
            return False

        # Simulate memory extraction/persistence from user "remember" intent.
        if "запомни" in prompt and ("люблю" in prompt and "спорт" in prompt):
            self._db[hardware_id] = {
                "recent_context": "User asked to remember a preference",
                "long_term_context": "User likes sports",
            }
        return True


class _CaptureTextModule:
    def __init__(self):
        self.is_initialized = True
        self.name = "text_processing"
        self.inputs = []

    async def process(self, payload):
        llm_input = str(payload.get("text", ""))
        self.inputs.append(llm_input)

        response_text = "Хорошо, я запомнил, что ты любишь спорт."
        if "что ты помнишь" in llm_input.lower() and "memory context" in llm_input.lower():
            response_text = "Я помню, что ты любишь спорт."

        async def _gen():
            yield {"text_response": response_text}

        return _gen()


@pytest_asyncio.fixture
async def service_stack():
    memory_workflow = _InMemoryMemoryWorkflow()
    text_module = _CaptureTextModule()

    audio_module = Mock()
    audio_module.is_initialized = True
    audio_module.name = "audio_generation"
    audio_module.process = AsyncMock(return_value=None)

    streaming = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
        memory_workflow=memory_workflow,
    )
    await streaming.initialize()

    service = GrpcServiceIntegration(
        streaming_workflow=streaming,
        memory_workflow=memory_workflow,
        interrupt_workflow=None,
    )
    await service.initialize()

    return service, text_module, memory_workflow


@pytest.mark.asyncio
async def test_user_flow_memory_reaches_llm_prompt(service_stack):
    service, text_module, memory_workflow = service_stack
    hardware_id = "hw-e2e-1"

    # 1) User teaches memory
    req1 = {
        "text": "Запомни: я люблю заниматься спортом",
        "session_id": "s1",
        "hardware_id": hardware_id,
    }
    async for _ in service.process_request_complete(req1):
        pass

    assert hardware_id in memory_workflow._db
    assert memory_workflow._db[hardware_id]["long_term_context"] == "User likes sports"

    # 2) User asks recall question
    req2 = {
        "text": "Что ты помнишь про меня?",
        "session_id": "s2",
        "hardware_id": hardware_id,
    }
    outputs = []
    async for item in service.process_request_complete(req2):
        outputs.append(item)

    # Ensure second request input sent to LLM contains injected memory context.
    assert len(text_module.inputs) >= 2
    second_llm_input = text_module.inputs[-1]
    assert "SYSTEM_CONTEXT:" in second_llm_input
    assert "Memory Context (long-term): User likes sports" in second_llm_input

    # Ensure user gets response from processing path.
    text_chunks = [str(i.get("text_response", "")) for i in outputs if i.get("text_response")]
    assert text_chunks
