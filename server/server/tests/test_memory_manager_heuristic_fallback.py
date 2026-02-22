import pytest

from modules.memory_management.core.memory_manager import MemoryManager


@pytest.mark.asyncio
async def test_heuristic_fallback_extracts_preference_on_remember_intent():
    manager = MemoryManager(db_manager=None)
    manager.memory_analyzer = None

    short_memory, long_memory = await manager.analyze_conversation(
        prompt="Я люблю заниматься спортом, запомни это.",
        response="Хорошо, запомню.",
        hardware_id="test-hardware",
    )

    assert short_memory
    assert "спорт" in long_memory.lower()


@pytest.mark.asyncio
async def test_heuristic_fallback_sanitizes_secret_payload():
    manager = MemoryManager(db_manager=None)
    manager.memory_analyzer = None

    _, long_memory = await manager.analyze_conversation(
        prompt="Запомни это: мой пароль qwerty123",
        response="Ок",
        hardware_id="test-hardware",
    )

    assert "пароль qwerty123" not in long_memory.lower()
    assert "credentials" in long_memory.lower()
