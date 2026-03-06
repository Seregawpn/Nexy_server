import pytest
import asyncio
import json

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


class _FailingAnalyzer:
    async def analyze_conversation(self, *args, **kwargs):
        raise RuntimeError("forced analyzer failure")


class _ScriptedAnalyzer:
    def __init__(self):
        self.calls = 0

    async def analyze_conversation(self, prompt, response, **kwargs):
        self.calls += 1
        if self.calls == 1:
            return "", "Previous communications:\n- Discussed sneakers; shortlist ready.", "Name is Sergiy."
        return "", "Previous communications:\n- Discussed restaurants; shortlist ready.", ""


class _EmptyLongAnalyzer:
    async def analyze_conversation(self, *args, **kwargs):
        return "", "Previous communications:\n- Updated context.", ""


class _ClearLongAnalyzer:
    async def analyze_conversation(self, *args, **kwargs):
        return "", "Previous communications:\n- Updated context.", "__CLEAR_LONG_TERM__"


@pytest.mark.asyncio
async def test_regular_query_does_not_include_medium_memory_context():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = None  # deterministic heuristic/fallback path

    await manager.update_memory_background(
        hardware_id="hw-medium-1",
        prompt="I am looking for white sneakers, remember this",
        response="We shortlisted two white sneaker options.",
    )

    context = await manager.get_memory_context(
        hardware_id="hw-medium-1",
        user_input="What is the weather in Montreal today?",
    )

    assert isinstance(context, dict)
    assert context.get("memory_gate") == "none"
    assert context.get("medium_term_context", "") == ""


@pytest.mark.asyncio
async def test_memory_intent_query_includes_medium_memory_context():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = None

    await manager.update_memory_background(
        hardware_id="hw-medium-2",
        prompt="I am looking for white sneakers, remember this",
        response="We shortlisted two white sneaker options.",
    )

    context = await manager.get_memory_context(
        hardware_id="hw-medium-2",
        user_input="Do you remember what we discussed about sneakers?",
    )

    assert isinstance(context, dict)
    assert context.get("memory_gate") == "keyword"
    assert "[20" in context.get("medium_term_context", "")
    assert "sneakers" in context.get("medium_term_context", "").lower()


@pytest.mark.asyncio
async def test_medium_term_accumulates_dated_entries_and_keeps_long_snapshot():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _ScriptedAnalyzer()

    await manager.update_memory_background(
        hardware_id="hw-replace-1",
        prompt="first",
        response="first response",
    )
    first_payload = json.loads(db.short)
    assert "user_intent=first" in str(first_payload.get("medium", "")).lower()
    assert "sergiy" in db.long.lower()

    await manager.update_memory_background(
        hardware_id="hw-replace-1",
        prompt="second",
        response="second response",
    )
    second_payload = json.loads(db.short)
    second_medium = str(second_payload.get("medium", "")).lower()
    assert "user_intent=first" in second_medium
    assert "user_intent=second" not in second_medium
    assert "sergiy" in db.long.lower()


@pytest.mark.asyncio
async def test_medium_term_rollup_updates_after_interval_elapsed():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _ScriptedAnalyzer()
    manager.set_medium_term_rollup_interval(seconds=1)

    await manager.update_memory_background(
        hardware_id="hw-rollup-interval",
        prompt="first",
        response="first response",
    )
    first_payload = json.loads(db.short)
    assert "user_intent=first" in str(first_payload.get("medium", "")).lower()

    await asyncio.sleep(1.1)

    await manager.update_memory_background(
        hardware_id="hw-rollup-interval",
        prompt="second",
        response="second response",
    )
    second_payload = json.loads(db.short)
    second_medium = str(second_payload.get("medium", "")).lower()
    assert "user_intent=second" in second_medium
    assert "user_intent=first" in second_medium


@pytest.mark.asyncio
async def test_analyzer_failure_still_applies_full_replace_snapshot():
    db = _StatefulFakeDB()
    db.short = "Previous communications:\n- Discussed existing topic; ready."
    db.long = "Name is Sergiy."
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _FailingAnalyzer()

    updated = await manager.update_memory_background(
        hardware_id="hw-safe-replace",
        prompt="new request",
        response="new response",
    )

    assert updated is not None
    assert "new request" in updated.get("medium", "").lower()
    assert "sergiy" in updated.get("factual_long", "").lower()

    context = await manager.get_memory_context(
        "hw-safe-replace",
        user_input="Do you remember what we discussed?",
    )
    assert "new request" in context.get("short_term_context", "").lower()
    assert "new request" in context.get("medium_term_context", "").lower()


@pytest.mark.asyncio
async def test_llm_clear_marker_drops_existing_long_term():
    db = _StatefulFakeDB()
    db.short = "Previous communications:\n- Old context."
    db.long = "Name is Sergiy."
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _ClearLongAnalyzer()

    updated = await manager.update_memory_background(
        hardware_id="hw-clear-by-llm",
        prompt="any prompt",
        response="any response",
    )

    assert updated is not None
    assert updated.get("factual_long", "") == ""


@pytest.mark.asyncio
async def test_explicit_name_is_persisted_and_recalled_via_long_term_fallback():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    manager.memory_analyzer = _FailingAnalyzer()

    updated = await manager.update_memory_background(
        hardware_id="hw-name-1",
        prompt="Меня зовут Сергей",
        response="Приятно познакомиться, Сергей!",
    )

    assert updated is not None
    assert "серг" in updated.get("factual_long", "").lower()

    context = await manager.get_memory_context(
        hardware_id="hw-name-1",
        user_input="Как меня зовут?",
    )

    assert isinstance(context, dict)
    assert "серг" in context.get("factual_long_term_context", "").lower()
    assert context.get("memory_gate") == "keyword"
