import json
from typing import Any, Dict, List

import pytest
import pytest_asyncio

from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration
from integrations.workflow_integrations.memory_workflow_integration import MemoryWorkflowIntegration
from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from modules.memory_management.adapter import MemoryManagementAdapter
from modules.memory_management.core.memory_manager import MemoryManager


class _StatefulFakeDB:
    def __init__(self):
        self.short = ""
        self.long = ""
        self.updates = 0

    async def get_user_memory(self, hardware_id: str):
        return {"short": self.short, "long": self.long}

    async def update_user_memory(self, hardware_id: str, short_memory: str, long_memory: str):
        self.short = short_memory
        self.long = long_memory
        self.updates += 1
        return True


class _FactAwareTextModule:
    def __init__(self):
        self.is_initialized = True
        self.name = "text_processing"
        self.requests: List[Dict[str, str]] = []

    async def process(self, payload):
        user_text = str(payload.get("text", ""))
        runtime_memory = str(payload.get("runtime_memory_context", ""))
        lowered = user_text.lower()
        self.requests.append(
            {
                "text": user_text,
                "runtime_memory_context": runtime_memory,
            }
        )

        if "что ты помнишь" in lowered:
            response = "Я помню, что тебя зовут Сергей и ты любишь спорт."
        elif "софия" in lowered and "отправь сообщение" in runtime_memory.lower():
            response = "Понял, формирую сообщение для Софии: как у тебя дела?"
        else:
            response = "Принял. Продолжаем."

        async def _gen():
            # Возвращаем строку с пунктуацией, чтобы поток TTS гарантированно разбился на сегмент.
            yield response

        return _gen()


class _AudioChunkModule:
    def __init__(self):
        self.is_initialized = True
        self.name = "audio_generation"

    async def process(self, payload):
        async def _gen():
            yield b"a" * 1024
            yield b"b" * 768

        return _gen()


@pytest_asyncio.fixture
async def factual_stack():
    db = _StatefulFakeDB()
    manager = MemoryManager(db_manager=db)
    # Фактический режим: без LLM-анализатора, только deterministic memory path.
    manager.memory_analyzer = None

    memory_adapter = MemoryManagementAdapter()
    memory_adapter._manager = manager

    memory_workflow = MemoryWorkflowIntegration(memory_manager=memory_adapter)
    await memory_workflow.initialize()

    text_module = _FactAwareTextModule()
    audio_module = _AudioChunkModule()

    streaming = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=audio_module,
        memory_workflow=memory_workflow,
    )
    await streaming.initialize()

    service = GrpcServiceIntegration(
        streaming_workflow=streaming,
        memory_workflow=memory_workflow,
        interrupt_workflow=None,
    )
    await service.initialize()

    return {
        "db": db,
        "manager": manager,
        "memory_workflow": memory_workflow,
        "text_module": text_module,
        "service": service,
    }


async def _run_request(service: GrpcServiceIntegration, request_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    async for item in service.process_request_complete(request_data):
        items.append(item)
    return items


def _count_audio_chunks(items: List[Dict[str, Any]]) -> int:
    return sum(1 for item in items if isinstance(item.get("audio_chunk"), (bytes, bytearray)))


@pytest.mark.asyncio
async def test_full_cycle_memory_db_cache_and_audio_chunks(factual_stack):
    service = factual_stack["service"]
    db = factual_stack["db"]
    text_module = factual_stack["text_module"]
    memory_workflow = factual_stack["memory_workflow"]

    hardware_id = "hw-factual-cycle-1"

    req1_items = await _run_request(
        service,
        {
            "text": "Запомни: меня зовут Сергей, и я люблю спорт",
            "session_id": "sess-factual-1",
            "hardware_id": hardware_id,
        },
    )
    assert _count_audio_chunks(req1_items) > 0
    assert db.updates >= 1
    assert "серг" in db.long.lower()

    req2_items = await _run_request(
        service,
        {
            "text": "Что ты помнишь про меня?",
            "session_id": "sess-factual-2",
            "hardware_id": hardware_id,
        },
    )
    assert _count_audio_chunks(req2_items) > 0

    # Проверяем, что генератор реально получил memory context (не "магию").
    second_call = text_module.requests[-1]
    runtime_memory = second_call["runtime_memory_context"]
    assert "Short-term memory:" in runtime_memory
    assert "Long-term memory:" in runtime_memory
    assert "серг" in runtime_memory.lower()

    # Проверяем, что write-through кэш реально заполнен.
    cache_key = memory_workflow._variant_key(hardware_id, None, True)
    assert cache_key in memory_workflow.memory_cache


@pytest.mark.asyncio
async def test_ragged_requests_are_persisted_and_replayed_in_short_term_memory(factual_stack):
    service = factual_stack["service"]
    manager = factual_stack["manager"]
    text_module = factual_stack["text_module"]

    hardware_id = "hw-factual-ragged-1"

    ragged_inputs = [
        ("sess-ragged-1", "Отправь сообщение"),
        ("sess-ragged-2", "София как у тебя дела"),
        ("sess-ragged-3", "И скажи ей я буду через 10"),
    ]

    for session_id, text in ragged_inputs:
        items = await _run_request(
            service,
            {
                "text": text,
                "session_id": session_id,
                "hardware_id": hardware_id,
            },
        )
        assert _count_audio_chunks(items) > 0

    context = await manager.get_memory_context(
        hardware_id=hardware_id,
        user_input="Что у нас было в последних сообщениях?",
        apply_medium_gate=False,
    )
    short_ctx = str(context.get("short_term_context", ""))
    assert "CURRENT_TURN:" in short_ctx
    assert "PREVIOUS_TURN_1:" in short_ctx
    assert "софия как у тебя дела" in short_ctx.lower() or "софия" in short_ctx.lower()

    # На следующем запросе runtime memory должен прийти в text module и содержать рванный след.
    _ = await _run_request(
        service,
        {
            "text": "София и ещё про сообщение",
            "session_id": "sess-ragged-4",
            "hardware_id": hardware_id,
        },
    )

    last_runtime_memory = text_module.requests[-1]["runtime_memory_context"].lower()
    assert "short-term memory:" in last_runtime_memory
    assert "previous_turn_" in last_runtime_memory
    assert "отправь сообщение" in last_runtime_memory or "софия" in last_runtime_memory

    # Дополнительно проверяем, что DB short blob реально содержит short_current/short_previous.
    decoded = json.loads(factual_stack["db"].short)
    assert decoded.get("schema") == "memory_v2"
    assert decoded.get("short_current")
    assert isinstance(decoded.get("short_previous"), list)
