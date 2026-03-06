import asyncio
import json

import pytest

from modules.memory_management.core.memory_manager import MemoryManager


class _InMemoryDb:
    def __init__(self):
        self.short = ""
        self.long = ""

    async def get_user_memory(self, hardware_id):
        await asyncio.sleep(0.005)
        return {"short": self.short, "long": self.long}

    async def update_user_memory(self, hardware_id, short_value, long_value):
        await asyncio.sleep(0.005)
        self.short = short_value
        self.long = long_value
        return True


class _AnalyzerByPrompt:
    async def analyze_conversation(self, prompt, response, **kwargs):
        await asyncio.sleep(0.01)
        if "alpha" in prompt:
            return "", "Previous communications:\n- Discussed alpha; done.", ""
        return "", "Previous communications:\n- Discussed beta; done.", ""


@pytest.mark.asyncio
async def test_parallel_updates_keep_consistent_merged_snapshot_with_user_lock():
    db = _InMemoryDb()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _AnalyzerByPrompt()

    await asyncio.gather(
        manager.update_memory_background("hw-race", "alpha", "ok"),
        manager.update_memory_background("hw-race", "beta", "ok"),
    )

    final_medium = db.short
    payload = json.loads(final_medium)
    medium_value = str(payload.get("medium", ""))
    # Medium-term keeps dated digest; lock guarantees deterministic no-corruption result.
    assert "[20" in medium_value
    assert "user_intent=alpha" in medium_value or "user_intent=beta" in medium_value
