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
                    "recent_context": "User repeatedly asks about Montreal weather",
                    "long_term_context": "",
                },
            }
        if action == "get_context":
            self.get_context_calls += 1
            return {"memory": {"recent_context": "from-db", "long_term_context": ""}}
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
    assert cached.get("recent_context") == "User repeatedly asks about Montreal weather"
    assert module.get_context_calls == 0
