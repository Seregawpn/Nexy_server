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
                    "recent_context": "User asked to remember current task",
                    "long_term_context": "User likes sports",
                }
            }
        return {}


@pytest.mark.asyncio
async def test_memory_workflow_returns_context_without_one_request_lag():
    integration = MemoryWorkflowIntegration(memory_manager=_FakeMemoryModule())
    integration.is_initialized = True

    context = await integration.get_memory_context_parallel("hw-1")

    assert context is not None
    assert context.get("recent_context")
    assert context.get("long_term_context")


def test_streaming_enrich_context_includes_long_term_memory():
    workflow = StreamingWorkflowIntegration()

    enriched = workflow._enrich_context(
        "Что ты помнишь про меня?",
        {
            "recent_context": "Asked to remember preference",
            "long_term_context": "User likes sports",
        },
        None,
    )

    assert "Memory Context (recent): Asked to remember preference" in enriched
    assert "Memory Context (long-term): User likes sports" in enriched
