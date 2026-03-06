import pytest

from modules.memory_management.core.memory_manager import MemoryManager


@pytest.mark.asyncio
async def test_heuristic_fallback_extracts_preference_on_remember_intent():
    manager = MemoryManager(db_manager=None)
    manager.memory_analyzer = None

    short_memory, medium_memory, long_memory = await manager.analyze_conversation(
        prompt="Я люблю заниматься спортом, запомни это.",
        response="Хорошо, запомню.",
        hardware_id="test-hardware",
    )

    assert short_memory
    assert medium_memory
    assert "спорт" in long_memory.lower()


@pytest.mark.asyncio
async def test_heuristic_fallback_does_not_store_command_style_remember_payload():
    manager = MemoryManager(db_manager=None)
    manager.memory_analyzer = None

    _, _, long_memory = await manager.analyze_conversation(
        prompt="Запомни это: мой пароль qwerty123",
        response="Ок",
        hardware_id="test-hardware",
    )

    assert "пароль qwerty123" not in long_memory.lower()
    assert long_memory == ""


@pytest.mark.asyncio
async def test_short_term_memory_is_saved_as_chat_summary_without_db():
    manager = MemoryManager(db_manager=None)
    manager.memory_analyzer = None

    updated = await manager.update_memory_background(
        hardware_id="hw-chat",
        prompt="What is the weather in Montreal right now?",
        response="In Montreal now it is -2C and light snow.",
    )

    assert updated is not None
    assert "medium" in updated
    assert "factual_long" in updated
    short_memory = updated.get("short", "")
    assert "CURRENT_REQUEST:" not in short_memory
    assert "weather in montreal" in short_memory.lower()
    assert "assistant:" in short_memory.lower()

    context = await manager.get_memory_context("hw-chat")
    assert isinstance(context, dict)
    assert "weather in montreal" in context.get("short_term_context", "").lower()
