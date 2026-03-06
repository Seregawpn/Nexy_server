import pytest

from modules.memory_management.core.memory_manager import MemoryManager


@pytest.mark.asyncio
async def test_short_term_memory_returns_full_current_and_previous_turns():
    manager = MemoryManager(db_manager=None)
    manager.memory_analyzer = None

    await manager.update_memory_background(
        hardware_id="hw-short-replace",
        prompt="First prompt about weather in Toronto",
        response="First response",
    )
    ctx_first = await manager.get_memory_context("hw-short-replace")
    first_short = ctx_first.get("short_term_context", "")
    assert "First prompt about weather in Toronto" in first_short

    await manager.update_memory_background(
        hardware_id="hw-short-replace",
        prompt="Second prompt about restaurants in Montreal",
        response="Second response",
    )
    ctx_second = await manager.get_memory_context("hw-short-replace")
    second_short = ctx_second.get("short_term_context", "")

    assert "Second prompt about restaurants in Montreal" in second_short
    assert "CURRENT_TURN:" in second_short
    assert "PREVIOUS_TURN_1:" in second_short
    assert "Second prompt about restaurants in Montreal" in second_short
    assert "First prompt about weather in Toronto" in second_short
