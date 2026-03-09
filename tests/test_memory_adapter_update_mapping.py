import pytest

from modules.memory_management.adapter import MemoryManagementAdapter


class _FakeManager:
    async def update_memory_background(self, hardware_id: str, prompt: str, response: str):
        return {
            "short_live": "[2026-03-04] user_request=u; assistant_reply=a; outcome=ok",
            "short": "short-fallback",
            "medium": "medium-should-not-be-used-as-recent",
            "factual_long": "User name: Sergiy",
            "long": "",
        }

    async def get_memory_context(self, hardware_id: str, user_input=None):
        return {}


@pytest.mark.asyncio
async def test_update_background_returns_canonical_memory_keys():
    adapter = MemoryManagementAdapter()
    adapter._manager = _FakeManager()

    result = await adapter.process(
        {
            "action": "update_background",
            "hardware_id": "hw-1",
            "prompt": "hello",
            "response": "done",
        }
    )

    assert result.get("success") is True
    memory = result.get("memory", {})
    assert memory.get("short_term_context", "").startswith("[2026-03-04]")
    assert memory.get("medium_term_context") == "medium-should-not-be-used-as-recent"
    assert memory.get("factual_long_term_context") == "User name: Sergiy"
