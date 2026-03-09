import pytest

from integrations.workflow_integrations.memory_workflow_integration import (
    MemoryWorkflowIntegration,
)
from integrations.workflow_integrations.streaming_workflow_integration import (
    StreamingWorkflowIntegration,
)


class _FakeMemoryModule:
    async def process(self, payload):
        if payload.get("action") == "get_context":
            return {
                "memory": {
                    "short_term_context": "User asked to remember current task",
                    "factual_long_term_context": "User likes sports",
                }
            }
        return {}


@pytest.mark.asyncio
async def test_memory_workflow_returns_context_without_one_request_lag():
    integration = MemoryWorkflowIntegration(memory_manager=_FakeMemoryModule())
    integration.is_initialized = True

    context = await integration.get_memory_context_parallel("hw-1")

    assert context is not None
    assert context.get("short_term_context")
    assert context.get("factual_long_term_context")


def test_streaming_runtime_memory_context_includes_long_term_memory():
    workflow = StreamingWorkflowIntegration()

    runtime_memory = workflow._build_runtime_memory_context(
        {
            "short_term_context": "Asked to remember preference",
            "factual_long_term_context": "User likes sports",
        },
        None,
    )

    assert "Short-term memory:" in runtime_memory
    assert "Asked to remember preference" in runtime_memory
    assert "Long-term memory:" in runtime_memory
    assert "User likes sports" in runtime_memory
