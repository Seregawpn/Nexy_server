import asyncio

import pytest

from modules.memory_management.core.memory_manager import MemoryManager


class _StatefulFakeDB:
    def __init__(self):
        self.short = ""
        self.long = ""

    async def get_user_memory(self, hardware_id: str):
        return {"short": self.short, "long": self.long}

    async def update_user_memory(self, hardware_id: str, short_memory: str, long_memory: str):
        self.short = short_memory
        self.long = long_memory
        return True


@pytest.mark.asyncio
async def test_medium_term_retention_seconds_prunes_fast_cycle_without_touching_long_term():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = None
    manager.set_medium_term_retention(days=30, seconds=1)

    await manager.update_memory_background(
        hardware_id="hw-medium-seconds",
        prompt="Запомни это: меня зовут Сергей и я люблю Nike",
        response="Принял, запомнил.",
    )

    context_now = await manager.get_memory_context(
        hardware_id="hw-medium-seconds",
        user_input="Что мы обсуждали раньше?",
    )
    assert context_now.get("medium_term_context", "") != ""
    assert context_now.get("medium_term_context", "").startswith("[")
    assert context_now.get("factual_long_term_context", "") != ""

    await asyncio.sleep(1.2)

    context_after = await manager.get_memory_context(
        hardware_id="hw-medium-seconds",
        user_input="Что мы обсуждали раньше?",
    )
    assert context_after.get("medium_term_context", "") == ""
    # Fast medium-term cleanup must not wipe factual long-term profile.
    assert context_after.get("factual_long_term_context", "") != ""
