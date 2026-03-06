import pytest

from integrations.workflow_integrations.memory_workflow_integration import (
    MemoryWorkflowIntegration,
)
from modules.memory_management.core.memory_manager import MemoryManager


class _FakeDBManager:
    def __init__(self, short_memory: str, long_memory: str):
        self._short_memory = short_memory
        self._long_memory = long_memory

    async def get_user_memory(self, hardware_id: str):
        return {"short": self._short_memory, "long": self._long_memory}


@pytest.mark.asyncio
async def test_regular_question_does_not_activate_medium_term_memory():
    manager = MemoryManager(
        db_manager=_FakeDBManager(
            short_memory="Current communication: User compared white sneakers and black sneakers.\nProgress: shortlist prepared.\nPrevious communications:\n- Discussed weather in Montreal; forecast delivered.",
            long_memory="User name is Alex; User likes running.",
        )
    )

    context = await manager.get_memory_context(
        "hw-regular",
        user_input="What is the weather today?",
    )

    assert isinstance(context, dict)
    assert context.get("memory_gate") == "none"
    assert context.get("medium_term_context", "") == ""
    assert "Alex" in context.get("factual_long_term_context", "")


@pytest.mark.asyncio
async def test_memory_intent_question_activates_medium_term_memory():
    manager = MemoryManager(
        db_manager=_FakeDBManager(
            short_memory="Current communication: User compared white sneakers and black sneakers.\nProgress: shortlist prepared.\nPrevious communications:\n- Discussed weather in Montreal; forecast delivered.",
            long_memory="User likes running.",
        )
    )

    context = await manager.get_memory_context(
        "hw-memory-intent",
        user_input="Do you remember which sneakers I chose last time?",
    )

    assert isinstance(context, dict)
    assert context.get("memory_gate") == "keyword"
    assert "white sneakers" in context.get("medium_term_context", "")


@pytest.mark.asyncio
async def test_manager_returns_medium_term_when_gate_disabled():
    manager = MemoryManager(
        db_manager=_FakeDBManager(
            short_memory="Current communication: User compared white sneakers and black sneakers.\nProgress: shortlist prepared.\nPrevious communications:\n- Discussed weather in Montreal; forecast delivered.",
            long_memory="User likes running.",
        )
    )

    context = await manager.get_memory_context(
        "hw-memory-no-gate",
        user_input="What is the weather today?",
        apply_medium_gate=False,
    )

    assert isinstance(context, dict)
    assert context.get("memory_gate") == "disabled"
    assert "white sneakers" in context.get("medium_term_context", "")


@pytest.mark.asyncio
async def test_manager_empty_context_keeps_canonical_shape():
    manager = MemoryManager(
        db_manager=_FakeDBManager(
            short_memory="",
            long_memory="",
        )
    )

    context = await manager.get_memory_context(
        "",
        user_input="Do you remember this?",
    )

    assert isinstance(context, dict)
    assert context.get("short_term_context", "") == ""
    assert context.get("medium_term_context", "") == ""
    assert context.get("factual_long_term_context", "") == ""
    assert context.get("memory_gate") == "keyword"
    assert "formatted_prompt" in context


class _CountingMemoryModule:
    def __init__(self):
        self.get_context_calls = 0
        self._manager = MemoryManager(db_manager=_FakeDBManager(short_memory="", long_memory=""))

    async def process(self, payload):
        if payload.get("action") == "get_context":
            self.get_context_calls += 1
            user_input = (payload.get("user_input") or "").lower()
            apply_medium_gate = bool(payload.get("apply_medium_gate", True))
            include_medium = (
                (not apply_medium_gate)
                or ("remember" in user_input)
                or ("previous" in user_input)
            )
            return {
                "memory": {
                    "short_term_context": "Current session context",
                    "medium_term_context": "Previous session summary" if include_medium else "",
                    "factual_long_term_context": "User likes running",
                }
            }
        return {}

    def get_manager(self):
        return self._manager


@pytest.mark.asyncio
async def test_short_term_memory_path_uses_cache_for_fast_second_request():
    module = _CountingMemoryModule()
    workflow = MemoryWorkflowIntegration(memory_manager=module)
    workflow.is_initialized = True

    first = await workflow.get_memory_context_parallel(
        "hw-fast-short-term",
        user_input="What is next?",
    )
    second = await workflow.get_memory_context_parallel(
        "hw-fast-short-term",
        user_input="What is next?",
    )

    assert first is not None
    assert second is not None
    assert module.get_context_calls == 1
    assert second.get("short_term_context") == "Current session context"


@pytest.mark.asyncio
async def test_cached_medium_term_is_hidden_when_current_request_has_no_memory_keywords():
    module = _CountingMemoryModule()
    workflow = MemoryWorkflowIntegration(memory_manager=module)
    workflow.is_initialized = True

    # 1) Populate cache with a keyword-based request (medium-term allowed).
    keyword_ctx = await workflow.get_memory_context_parallel(
        "hw-medium-cache-gate",
        user_input="Do you remember our previous discussion?",
    )
    assert keyword_ctx is not None
    assert keyword_ctx.get("medium_term_context") == "Previous session summary"

    # 2) Regular request must not reuse "memory-intent" cache variant.
    # It should fetch/resolve a no-medium variant and return medium hidden.
    regular_ctx = await workflow.get_memory_context_parallel(
        "hw-medium-cache-gate",
        user_input="What is the weather today?",
    )
    assert regular_ctx is not None
    assert module.get_context_calls == 2
    assert regular_ctx.get("medium_term_context", "") == ""


@pytest.mark.asyncio
async def test_cached_medium_term_is_preserved_when_gate_disabled():
    module = _CountingMemoryModule()
    workflow = MemoryWorkflowIntegration(memory_manager=module)
    workflow.is_initialized = True

    ctx = await workflow.get_memory_context_parallel(
        "hw-medium-gate-disabled",
        user_input="What is the weather today?",
        apply_medium_gate=False,
    )

    assert ctx is not None
    assert ctx.get("medium_term_context") == "Previous session summary"
