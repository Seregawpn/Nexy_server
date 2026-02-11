import os
import sys
import time

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.integrations.screenshot_capture_integration import ScreenshotCaptureIntegration
from modules.screenshot_capture.core.screenshot_capture import ScreenshotCapture
from modules.screenshot_capture.core.types import (
    ScreenshotConfig,
    ScreenshotFormat,
    ScreenshotQuality,
    ScreenshotRegion,
)


class _DummyStateManager:
    pass


@pytest.mark.asyncio
async def test_screenshot_integration_prefers_mode_event_session_id(monkeypatch) -> None:
    event_bus = EventBus()
    integration = ScreenshotCaptureIntegration(
        event_bus=event_bus,
        state_manager=_DummyStateManager(),
        error_handler=ErrorHandler(event_bus),
    )
    integration._last_session_id = "stale-session"

    calls: list[tuple[object, bool]] = []

    async def _fake_capture_once(session_id, is_early=False):
        calls.append((session_id, is_early))

    monkeypatch.setattr(integration, "_capture_once", _fake_capture_once)

    await integration._on_mode_changed(
        {
            "data": {
                "mode": "processing",
                "session_id": "current-session",
            }
        }
    )

    assert calls == [("current-session", False)]


@pytest.mark.asyncio
async def test_screenshot_integration_out_of_order_replay_keeps_mode_session(monkeypatch) -> None:
    event_bus = EventBus()
    integration = ScreenshotCaptureIntegration(
        event_bus=event_bus,
        state_manager=_DummyStateManager(),
        error_handler=ErrorHandler(event_bus),
    )

    calls: list[tuple[object, bool]] = []

    async def _fake_capture_once(session_id, is_early=False):
        calls.append((session_id, is_early))

    async def _fake_capture_once_early(_session_id):
        return None

    monkeypatch.setattr(integration, "_capture_once", _fake_capture_once)
    monkeypatch.setattr(integration, "_capture_once_early", _fake_capture_once_early)

    await integration._on_recording_start({"data": {"session_id": "A"}})
    await integration._on_recording_start({"data": {"session_id": "B"}})

    # Out-of-order: PROCESSING arrives for old request A after B was already seen.
    await integration._on_mode_changed(
        {
            "data": {
                "mode": "processing",
                "session_id": "A",
            }
        }
    )

    assert integration._last_session_id == "A"
    assert calls[-1] == ("A", False)


@pytest.mark.asyncio
async def test_capture_screenshot_timeout_returns_error_result(monkeypatch) -> None:
    def _fake_initialize_bridge(self) -> None:
        self._bridge = object()
        self._initialized = True

    monkeypatch.setattr(ScreenshotCapture, "_initialize_bridge", _fake_initialize_bridge)

    capture = ScreenshotCapture(
        ScreenshotConfig(
            format=ScreenshotFormat.JPEG,
            quality=ScreenshotQuality.MEDIUM,
            region=ScreenshotRegion.FULL_SCREEN,
            timeout=0.01,
        )
    )

    def _slow_capture_sync(_config):
        time.sleep(0.2)
        raise AssertionError("timeout must happen before slow capture completes")

    monkeypatch.setattr(capture, "_capture_sync", _slow_capture_sync)

    result = await capture.capture_screenshot()

    assert result.success is False
    assert result.error == "Таймаут захвата скриншота"


@pytest.mark.asyncio
async def test_screenshot_publish_idempotent_without_force_replay() -> None:
    event_bus = EventBus()
    integration = ScreenshotCaptureIntegration(
        event_bus=event_bus,
        state_manager=_DummyStateManager(),
        error_handler=ErrorHandler(event_bus),
    )

    published: list[dict[str, object]] = []

    async def _capture(event):
        payload = event.get("data", {}) if isinstance(event, dict) else {}
        published.append(dict(payload))

    await event_bus.subscribe("screenshot.captured", _capture)

    payload = {
        "session_id": "sid-1",
        "image_path": "/tmp/test.jpg",
        "format": "jpeg",
        "width": 100,
        "height": 100,
        "size_bytes": 1024,
        "mime_type": "image/jpeg",
        "capture_time": 0.01,
    }

    assert await integration._publish_captured(payload) is True
    assert await integration._publish_captured(payload) is False
    assert len(published) == 1
    assert "replay_reason" not in published[0]


@pytest.mark.asyncio
async def test_screenshot_publish_force_replay_sets_reason() -> None:
    event_bus = EventBus()
    integration = ScreenshotCaptureIntegration(
        event_bus=event_bus,
        state_manager=_DummyStateManager(),
        error_handler=ErrorHandler(event_bus),
    )

    published: list[dict[str, object]] = []

    async def _capture(event):
        payload = event.get("data", {}) if isinstance(event, dict) else {}
        published.append(dict(payload))

    await event_bus.subscribe("screenshot.captured", _capture)

    payload = {
        "session_id": "sid-2",
        "image_path": "/tmp/test2.jpg",
        "format": "jpeg",
        "width": 100,
        "height": 100,
        "size_bytes": 2048,
        "mime_type": "image/jpeg",
        "capture_time": 0.02,
    }

    assert await integration._publish_captured(payload) is True
    assert await integration._publish_captured(
        payload,
        force_replay=True,
        replay_reason="processing_entry_after_early_capture",
    ) is True

    assert len(published) == 2
    assert "replay_reason" not in published[0]
    assert published[1].get("replay_reason") == "processing_entry_after_early_capture"


@pytest.mark.asyncio
async def test_screenshot_publish_cache_eviction_allows_republish() -> None:
    event_bus = EventBus()
    integration = ScreenshotCaptureIntegration(
        event_bus=event_bus,
        state_manager=_DummyStateManager(),
        error_handler=ErrorHandler(event_bus),
    )
    integration._published_sessions_max = 2

    published: list[dict[str, object]] = []

    async def _capture(event):
        payload = event.get("data", {}) if isinstance(event, dict) else {}
        published.append(dict(payload))

    await event_bus.subscribe("screenshot.captured", _capture)

    def _payload(session_id: str) -> dict[str, object]:
        return {
            "session_id": session_id,
            "image_path": f"/tmp/{session_id}.jpg",
            "format": "jpeg",
            "width": 100,
            "height": 100,
            "size_bytes": 1024,
            "mime_type": "image/jpeg",
            "capture_time": 0.01,
        }

    assert await integration._publish_captured(_payload("sid-1")) is True
    assert await integration._publish_captured(_payload("sid-2")) is True
    assert await integration._publish_captured(_payload("sid-3")) is True

    assert "sid-1" not in integration._published_sessions
    assert "sid-1" not in integration._captured_by_session

    # sid-1 was evicted, so publish is allowed again.
    assert await integration._publish_captured(_payload("sid-1")) is True
    assert len(published) == 4
