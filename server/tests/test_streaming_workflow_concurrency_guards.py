import asyncio
from pathlib import Path
import sys
from unittest.mock import AsyncMock, Mock

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.unified_config import WorkflowConfig
from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from modules.session_management.core.session_registry import SessionRegistry


async def _collect_results(workflow: StreamingWorkflowIntegration, request_data: dict):
    results = []
    async for item in workflow.process_request_streaming(request_data):
        results.append(item)
    return results


@pytest.fixture(autouse=True)
def clear_session_registry():
    registry = SessionRegistry()
    registry.clear()
    yield
    registry.clear()


@pytest.fixture
def mock_audio_module():
    module = Mock()
    module.is_initialized = True
    module.name = "audio_generation"

    async def generate_audio(*args, **kwargs):
        yield b"audio"

    module.process = AsyncMock(side_effect=lambda *args, **kwargs: generate_audio())
    return module


@pytest.mark.asyncio
async def test_rejects_concurrent_request_with_same_session_id(mock_audio_module):
    started = asyncio.Event()
    unblock = asyncio.Event()

    async def blocking_text_stream():
        started.set()
        await unblock.wait()
        yield "Ответ после блокировки."

    text_module = Mock()
    text_module.is_initialized = True
    text_module.name = "text_processing"
    text_module.process = AsyncMock(side_effect=lambda *args, **kwargs: blocking_text_stream())

    workflow = StreamingWorkflowIntegration(text_processor=text_module, audio_processor=mock_audio_module)
    await workflow.initialize()

    request_1 = {"text": "first", "session_id": "sid-1", "hardware_id": "hw-1"}
    request_2 = {"text": "second", "session_id": "sid-1", "hardware_id": "hw-2"}

    first_task = asyncio.create_task(_collect_results(workflow, request_1))
    await started.wait()

    second_results = await _collect_results(workflow, request_2)

    assert second_results, "Второй запрос должен вернуть ошибку concurrent_request"
    assert second_results[0].get("success") is False
    assert second_results[0].get("error_code") == "RESOURCE_EXHAUSTED"
    assert second_results[0].get("error_type") == "concurrent_request"

    unblock.set()
    await first_task


@pytest.mark.asyncio
async def test_rejects_concurrent_request_with_same_hardware_id_when_guard_enabled(mock_audio_module):
    started = asyncio.Event()
    unblock = asyncio.Event()

    async def blocking_text_stream():
        started.set()
        await unblock.wait()
        yield "Ответ после блокировки."

    text_module = Mock()
    text_module.is_initialized = True
    text_module.name = "text_processing"
    text_module.process = AsyncMock(side_effect=lambda *args, **kwargs: blocking_text_stream())

    workflow = StreamingWorkflowIntegration(
        text_processor=text_module,
        audio_processor=mock_audio_module,
        workflow_config=WorkflowConfig(prevent_concurrent_hardware_id_sessions=True),
    )
    await workflow.initialize()

    request_1 = {"text": "first", "session_id": "sid-a", "hardware_id": "hw-shared"}
    request_2 = {"text": "second", "session_id": "sid-b", "hardware_id": "hw-shared"}

    first_task = asyncio.create_task(_collect_results(workflow, request_1))
    await started.wait()

    second_results = await _collect_results(workflow, request_2)

    assert second_results, "Второй запрос должен вернуть ошибку concurrent_hardware_id"
    assert second_results[0].get("success") is False
    assert second_results[0].get("error_code") == "RESOURCE_EXHAUSTED"
    assert second_results[0].get("error_type") == "concurrent_hardware_id"

    unblock.set()
    await first_task
