from pathlib import Path
import sys
from unittest.mock import Mock, patch

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration


class _StubRuntimeV2:
    def __init__(self) -> None:
        self.calls: list[dict] = []

    async def process_request_streaming(self, request_data, *, legacy_handler):
        self.calls.append({"request_data": request_data, "legacy_handler": legacy_handler})
        yield {"success": True, "runtime": "v2"}


async def _collect(workflow: StreamingWorkflowIntegration, request_data: dict) -> list[dict]:
    items: list[dict] = []
    async for item in workflow.process_request_streaming(request_data):
        items.append(item)
    return items


@pytest.fixture
def workflow() -> StreamingWorkflowIntegration:
    text_module = Mock()
    text_module.is_initialized = True
    text_module.name = "text_processing"
    audio_module = Mock()
    audio_module.is_initialized = True
    audio_module.name = "audio_generation"
    workflow = StreamingWorkflowIntegration(text_processor=text_module, audio_processor=audio_module)
    workflow.is_initialized = True
    return workflow


@pytest.mark.asyncio
async def test_runtime_switch_uses_current_path_by_default(workflow: StreamingWorkflowIntegration):
    called: list[dict] = []

    async def current_path(request_data):
        called.append(request_data)
        yield {"success": True, "runtime": "current"}

    workflow._process_request_streaming_current = current_path
    runtime_v2 = _StubRuntimeV2()
    workflow._runtime_v2 = runtime_v2

    with patch("integrations.workflow_integrations.streaming_workflow_integration.get_config") as mock_get_config:
        cfg = Mock()
        cfg.is_feature_enabled.return_value = False
        cfg.is_kill_switch_active.return_value = False
        mock_get_config.return_value = cfg

        result = await _collect(workflow, {"session_id": "sid-1", "hardware_id": "hw-1", "text": "hello"})

    assert result == [{"success": True, "runtime": "current"}]
    assert called and called[0]["session_id"] == "sid-1"
    assert runtime_v2.calls == []


@pytest.mark.asyncio
async def test_runtime_switch_routes_to_v2_when_feature_enabled(workflow: StreamingWorkflowIntegration):
    async def current_path(_request_data):
        raise AssertionError("current runtime should not be called when v2 is enabled")
        yield {}

    workflow._process_request_streaming_current = current_path
    runtime_v2 = _StubRuntimeV2()
    workflow._runtime_v2 = runtime_v2

    with patch("integrations.workflow_integrations.streaming_workflow_integration.get_config") as mock_get_config:
        cfg = Mock()
        cfg.is_feature_enabled.side_effect = lambda name: name == "assistant_runtime_v2"
        cfg.is_kill_switch_active.return_value = False
        mock_get_config.return_value = cfg

        result = await _collect(workflow, {"session_id": "sid-2", "hardware_id": "hw-2", "text": "hello"})

    assert result == [{"success": True, "runtime": "v2"}]
    assert len(runtime_v2.calls) == 1
    assert runtime_v2.calls[0]["request_data"]["session_id"] == "sid-2"
