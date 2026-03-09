import pytest

from integrations.workflow_integrations.memory_workflow_integration import (
    MemoryWorkflowIntegration,
)


class _FastPathMemoryModule:
    def __init__(self):
        self.get_context_calls = 0

    async def process(self, payload):
        action = payload.get("action")
        if action == "update_background":
            return {
                "success": True,
                "memory": {
                    "short_term_context": "User repeatedly asks about Montreal weather",
                    "factual_long_term_context": "",
                },
            }
        if action == "get_context":
            self.get_context_calls += 1
            return {"memory": {"short_term_context": "from-db", "factual_long_term_context": ""}}
        return {}


@pytest.mark.asyncio
async def test_save_background_uses_update_response_for_cache_without_fetch():
    module = _FastPathMemoryModule()
    integration = MemoryWorkflowIntegration(memory_manager=module)
    integration.is_initialized = True

    await integration._save_memory_background(
        {
            "hardware_id": "hw-fast",
            "prompt": "show weather in montreal",
            "response": "Here is the weather",
        }
    )

    cached = integration._get_cached_memory("hw-fast")
    assert cached is not None
    assert cached.get("short_term_context") == "User repeatedly asks about Montreal weather"
    assert module.get_context_calls == 0


@pytest.mark.asyncio
async def test_fastpath_cache_hides_medium_term_for_no_medium_bucket():
    module = _FastPathMemoryModule()
    integration = MemoryWorkflowIntegration(memory_manager=module)
    integration.is_initialized = True

    await integration._cache_memory(
        "hw-fast-gated",
        {
            "short_term_context": "Recent turn",
            "medium_term_context": "Should stay hidden for regular requests",
            "factual_long_term_context": "User likes Montreal",
        },
        apply_medium_gate=None,
    )

    regular_cached = integration._get_cached_memory(
        "hw-fast-gated",
        user_input="What is the weather today?",
        apply_medium_gate=True,
    )
    assert regular_cached is not None
    assert regular_cached.get("medium_term_context", "") == ""

    full_cached = integration._get_cached_memory(
        "hw-fast-gated",
        user_input="What is the weather today?",
        apply_medium_gate=False,
    )
    assert full_cached is not None
    assert full_cached.get("medium_term_context") == "Should stay hidden for regular requests"
