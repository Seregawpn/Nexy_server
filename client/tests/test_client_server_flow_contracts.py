import asyncio
from pathlib import Path
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


class _FakeGrpcClientCaptureArgs:
    def __init__(self):
        self.calls: list[dict] = []

    async def stream_audio(self, **kwargs):
        self.calls.append(kwargs)
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
async def test_grpc_prefers_screenshot_base64_over_file_read(monkeypatch):
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    integration = GrpcClientIntegration(event_bus, state_manager, ErrorHandler())

    fake_client = _FakeGrpcClientCaptureArgs()
    integration._client = fake_client  # type: ignore[assignment]
    integration._await_hardware_id = AsyncMock(return_value="hw-test")  # type: ignore[method-assign]
    integration._ensure_connected = AsyncMock(return_value=True)  # type: ignore[method-assign]

    sid = "sid-base64-priority"
    integration._sessions[sid] = {
        "text": "check screenshot priority",
        "screenshot_base64": "YmFzZTY0LWZyb20tZXZlbnQ=",
        "screenshot_path": "/tmp/should-not-be-read.png",
        "width": 800,
        "height": 600,
    }

    def _read_bytes_must_not_be_called(_self):
        raise AssertionError("Path.read_bytes must not be used when screenshot_base64 exists")

    monkeypatch.setattr(Path, "read_bytes", _read_bytes_must_not_be_called)

    await integration._send_in_grpc_loop(sid)

    assert len(fake_client.calls) == 1
    request_kwargs = fake_client.calls[0]
    assert request_kwargs["session_id"] == sid
    assert request_kwargs["screenshot_base64"] == "YmFzZTY0LWZyb20tZXZlbnQ="
    assert request_kwargs["screen_info"] == {"width": 800, "height": 600}


@pytest.mark.asyncio
async def test_grpc_request_cancel_rejects_missing_session_id():
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = GrpcClientIntegration(event_bus, state_manager, ErrorHandler())

    task_old = asyncio.create_task(asyncio.sleep(1.0))
    task_latest = asyncio.create_task(asyncio.sleep(1.0))
    integration._inflight["sid-old"] = task_old
    integration._inflight["sid-latest"] = task_latest

    try:
        await integration._on_request_cancel({"data": {}})
        assert "sid-old" in integration._inflight
        assert "sid-latest" in integration._inflight
        assert not task_old.cancelled()
        assert not task_latest.cancelled()
    finally:
        task_old.cancel()
        task_latest.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task_old
        with pytest.raises(asyncio.CancelledError):
            await task_latest


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
