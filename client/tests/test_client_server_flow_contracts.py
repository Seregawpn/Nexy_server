import asyncio
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.action_execution_integration import ActionExecutionIntegration
from integration.integrations.grpc_client_integration import GrpcClientIntegration


class _FakeStreamResponse:
    def __init__(self, content: str, value: str = ""):
        self._content = content
        self.text_chunk = value
        self.end_message = value

    def WhichOneof(self, _: str):
        return self._content


class _FakeGrpcClient:
    async def stream_audio(self, **kwargs):
        yield _FakeStreamResponse(
            "text_chunk",
            '{"command":"open_app","args":{"app_name":"Calculator"}}',
        )
        yield _FakeStreamResponse("end_message", "done")

    def is_connected(self) -> bool:
        return True


@pytest.mark.asyncio
async def test_grpc_ignores_action_like_text_chunk_contract():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = GrpcClientIntegration(event_bus, state_manager, ErrorHandler())

    integration._client = _FakeGrpcClient()  # type: ignore[assignment]
    integration._await_hardware_id = AsyncMock(return_value="hw-test")  # type: ignore[method-assign]
    integration._ensure_connected = AsyncMock(return_value=True)  # type: ignore[method-assign]
    integration._sessions["sid-1"] = {"text": "open calculator"}

    published: list[tuple[str, dict]] = []

    async def _capture_publish(event_type: str, data=None):
        published.append((event_type, data or {}))

    integration.event_bus.publish = _capture_publish  # type: ignore[assignment]

    await integration._send_in_grpc_loop("sid-1")

    event_types = [event_type for event_type, _ in published]
    assert "grpc.response.action" not in event_types
    assert "grpc.response.text" in event_types
    assert "grpc.request_completed" in event_types


@pytest.mark.asyncio
async def test_grpc_request_cancel_requires_session_id():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = GrpcClientIntegration(event_bus, state_manager, ErrorHandler())

    task = asyncio.create_task(asyncio.sleep(1.0))
    integration._inflight["sid-keep"] = task

    try:
        await integration._on_request_cancel({"data": {}})
        assert "sid-keep" in integration._inflight
        assert not task.cancelled()
    finally:
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task


@pytest.mark.asyncio
async def test_action_execution_cancel_trigger_is_interrupt_only():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = ActionExecutionIntegration(event_bus, state_manager, ErrorHandler())
    integration._cancel_all_actions = AsyncMock()  # type: ignore[method-assign]

    await integration._do_start()
    try:
        await event_bus.publish("interrupt.request", {"type": "speech_stop"})
        await event_bus.publish("keyboard.short_press", {"source": "keyboard"})
    finally:
        await integration._do_stop()

    reasons = [call.kwargs.get("reason") for call in integration._cancel_all_actions.await_args_list]
    assert "interrupt" in reasons
    assert "keyboard_short_press" not in reasons
