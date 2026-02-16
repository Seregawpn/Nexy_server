import asyncio
import os
import sys
from unittest.mock import AsyncMock, Mock

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integration.core.event_bus import EventBus
from integration.integrations.browser_use_integration import BrowserUseIntegration
from integration.integrations.grpc_client_integration import (
    GrpcClientIntegration,
    GrpcClientIntegrationConfig,
)


@pytest.mark.asyncio
async def test_browser_install_started_tts_waits_for_welcome_completion() -> None:
    bus = EventBus()
    integration = BrowserUseIntegration(bus)

    tts_events: list[dict] = []
    notifications: list[dict] = []

    async def on_tts(event):
        tts_events.append(event.get("data", {}))

    async def on_notification(event):
        notifications.append(event.get("data", {}))

    await bus.subscribe("grpc.tts_request", on_tts)
    await bus.subscribe("system.notification", on_notification)

    await integration._handle_install_status({"status": "started"})
    await asyncio.sleep(0)

    assert len(notifications) == 1
    assert notifications[0].get("message") == (
        "Browser is installing. It may take a few minutes. After that, you can use browser use."
    )
    assert tts_events == []

    await integration._on_welcome_completed({"data": {"success": True}})
    await asyncio.sleep(0)

    assert len(tts_events) == 1
    assert tts_events[0].get("text") == (
        "Browser is installing. It may take a few minutes. After that, you can use browser use."
    )


@pytest.mark.asyncio
async def test_browser_already_installed_tts_emits_when_welcome_done() -> None:
    bus = EventBus()
    integration = BrowserUseIntegration(bus)
    integration._welcome_completed = True
    integration._welcome_completed_event.set()

    tts_events: list[dict] = []

    async def on_tts(event):
        tts_events.append(event.get("data", {}))

    await bus.subscribe("grpc.tts_request", on_tts)

    await integration._handle_install_status({"status": "already_installed"})
    await asyncio.sleep(0)

    assert tts_events == []


@pytest.mark.asyncio
async def test_install_completion_announcement_is_silent_by_contract() -> None:
    bus = EventBus()
    integration = BrowserUseIntegration(bus)
    integration._welcome_completed = True
    integration._welcome_completed_event.set()

    tts_events: list[dict] = []

    async def on_tts(event):
        tts_events.append(event.get("data", {}))

    await bus.subscribe("grpc.tts_request", on_tts)

    await integration._handle_install_status({"status": "completed"})
    await asyncio.sleep(0)

    assert tts_events == []


class _FakeGrpcClient:
    def __init__(self) -> None:
        self.stream_calls = 0

    async def stream_tts_audio(self, text: str, session_id: str):
        self.stream_calls += 1
        yield {"type": "end", "message": "ok"}


@pytest.mark.asyncio
async def test_server_tts_skips_when_grpc_connection_unavailable() -> None:
    bus = EventBus()
    integration = GrpcClientIntegration(
        event_bus=bus,
        state_manager=Mock(),
        error_handler=Mock(),
        config=GrpcClientIntegrationConfig(),
    )

    fake_client = _FakeGrpcClient()
    integration._client = fake_client
    integration._ensure_connected = AsyncMock(side_effect=[False] * 16)  # type: ignore[method-assign]

    await integration._play_server_tts("hello", "system")

    assert fake_client.stream_calls == 0
    assert integration._ensure_connected.await_count == 9


@pytest.mark.asyncio
async def test_server_tts_retries_connect_and_streams_on_second_attempt() -> None:
    bus = EventBus()
    integration = GrpcClientIntegration(
        event_bus=bus,
        state_manager=Mock(),
        error_handler=Mock(),
        config=GrpcClientIntegrationConfig(),
    )

    fake_client = _FakeGrpcClient()
    integration._client = fake_client
    integration._ensure_connected = AsyncMock(side_effect=[False, True])  # type: ignore[method-assign]

    await integration._play_server_tts("hello", "system")

    assert fake_client.stream_calls == 1
    assert integration._ensure_connected.await_count == 2


@pytest.mark.asyncio
async def test_browser_task_started_emits_immediate_start_tts() -> None:
    bus = EventBus()
    integration = BrowserUseIntegration(bus)

    tts_events: list[dict] = []

    async def on_tts(event):
        tts_events.append(event.get("data", {}))

    await bus.subscribe("grpc.tts_request", on_tts)

    async def fake_process(_request):
        yield {
            "type": "BROWSER_TASK_STARTED",
            "task_id": "t1",
            "session_id": "s1",
            "description": "Starting browser automation: search",
        }
        yield {
            "type": "BROWSER_TASK_COMPLETED",
            "task_id": "t1",
            "session_id": "s1",
            "description": "done",
        }

    integration.module.process = fake_process  # type: ignore[method-assign]
    await integration._run_process({"session_id": "s1", "args": {"task": "search"}})
    await asyncio.sleep(0)

    assert any(
        evt.get("source") == "browser_start"
        and evt.get("text") == "Browser opened. Starting search now."
        for evt in tts_events
    )
