import asyncio
import time

import pytest

from integrations.workflow_integrations.memory_workflow_integration import (
    MemoryWorkflowIntegration,
)


class _DelayedMemoryModule:
    def __init__(self, delay_sec: float = 0.12):
        self.delay_sec = delay_sec
        self.get_context_calls = 0

    async def process(self, payload):
        if payload.get("action") != "get_context":
            return {}
        self.get_context_calls += 1
        await asyncio.sleep(self.delay_sec)
        return {
            "memory": {
                "short_term_context": f"fresh-{self.get_context_calls}",
                "medium_term_context": "",
                "factual_long_term_context": "fact",
            }
        }


@pytest.mark.asyncio
async def test_memory_cache_hit_returns_without_waiting_for_memory_module():
    module = _DelayedMemoryModule(delay_sec=0.12)
    workflow = MemoryWorkflowIntegration(memory_manager=module)
    workflow.is_initialized = True

    await workflow._cache_memory(
        "hw-hit",
        {
            "short_term_context": "cached-now",
            "medium_term_context": "",
            "factual_long_term_context": "fact",
        },
        user_input="hello",
        apply_medium_gate=True,
    )

    started = time.perf_counter()
    context = await workflow.get_memory_context_parallel(
        "hw-hit",
        user_input="hello",
        apply_medium_gate=True,
    )
    elapsed = time.perf_counter() - started

    assert context is not None
    assert context.get("short_term_context") == "cached-now"
    assert module.get_context_calls == 0
    assert elapsed < 0.06


@pytest.mark.asyncio
async def test_memory_stale_hit_returns_immediately_and_refreshes_in_background():
    module = _DelayedMemoryModule(delay_sec=0.12)
    workflow = MemoryWorkflowIntegration(memory_manager=module)
    workflow.is_initialized = True
    workflow.cache_ttl = 0
    workflow.cache_hard_ttl = 3600

    await workflow._cache_memory(
        "hw-stale",
        {
            "short_term_context": "stale-now",
            "medium_term_context": "",
            "factual_long_term_context": "fact",
        },
        user_input="hello",
        apply_medium_gate=True,
    )

    started = time.perf_counter()
    first = await workflow.get_memory_context_parallel(
        "hw-stale",
        user_input="hello",
        apply_medium_gate=True,
    )
    elapsed = time.perf_counter() - started

    assert first is not None
    assert first.get("short_term_context") == "stale-now"
    assert elapsed < 0.06

    await asyncio.sleep(0.16)

    second = await workflow.get_memory_context_parallel(
        "hw-stale",
        user_input="hello",
        apply_medium_gate=True,
    )

    assert second is not None
    assert second.get("short_term_context", "").startswith("fresh-")
    assert module.get_context_calls >= 1


@pytest.mark.asyncio
async def test_memory_cold_miss_is_bounded_and_populates_cache_async():
    module = _DelayedMemoryModule(delay_sec=0.12)
    workflow = MemoryWorkflowIntegration(memory_manager=module)
    workflow.is_initialized = True

    started = time.perf_counter()
    first = await workflow.get_memory_context_parallel(
        "hw-miss",
        user_input="hello",
        apply_medium_gate=True,
    )
    elapsed = time.perf_counter() - started

    assert first is None
    assert elapsed < 0.06

    await asyncio.sleep(0.16)

    second = await workflow.get_memory_context_parallel(
        "hw-miss",
        user_input="hello",
        apply_medium_gate=True,
    )

    assert second is not None
    assert second.get("short_term_context", "").startswith("fresh-")
    assert module.get_context_calls >= 1
