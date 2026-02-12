from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from integration.integrations.permission_restart_integration import (
    PermissionRestartIntegration,
)


@pytest.mark.asyncio
async def test_v2_enabled_does_not_subscribe_legacy_restart_events() -> None:
    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=Mock(),
        error_handler=Mock(),
        config={"enabled": True},
    )
    integration._config = SimpleNamespace(enabled=True)
    integration._restart_handler = object()
    integration._v2_enabled = True
    integration._resume_pending_first_run_restart = AsyncMock()

    subscribed: list[str] = []
    integration._subscribe = AsyncMock(
        side_effect=lambda event_type, _handler, _priority: subscribed.append(event_type)
    )

    started = await integration._do_start()

    assert started is True
    assert "permissions.changed" not in subscribed
    assert "permissions.first_run_restart_pending" not in subscribed
    assert "permissions.first_run_completed" not in subscribed
    assert "updater.update_started" in subscribed
    assert "updater.update_completed" in subscribed
    assert "updater.update_skipped" in subscribed
    assert "updater.update_failed" in subscribed
    assert "app.startup" in subscribed
    integration._resume_pending_first_run_restart.assert_not_awaited()


@pytest.mark.asyncio
async def test_v2_enabled_ignores_first_run_restart_pending() -> None:
    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=Mock(),
        error_handler=Mock(),
        config={"enabled": True},
    )
    integration._config = SimpleNamespace(enabled=True)
    integration._v2_enabled = True
    integration._detector = Mock()
    integration._detector.process_event = Mock()

    await integration._on_first_run_restart_pending(
        {
            "data": {
                "session_id": "v2-session",
                "permissions": ["accessibility"],
                "is_last_batch": True,
                "batch_index": 0,
                "total_batches": 1,
                "source": "v2_integration",
            }
        }
    )

    integration._detector.process_event.assert_not_called()
    assert integration._restart_task is None


@pytest.mark.asyncio
async def test_initialize_logs_legacy_freeze_warning_when_v2_enabled(
    monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
) -> None:
    class _DummyRestartHandler:
        def __init__(self, config) -> None:
            self.config = config

    monkeypatch.setattr(
        "integration.integrations.permission_restart_integration.PermissionsRestartHandler",
        _DummyRestartHandler,
    )

    integration = PermissionRestartIntegration(
        event_bus=Mock(),
        state_manager=Mock(),
        error_handler=Mock(),
        config={"enabled": True},
    )
    monkeypatch.setattr(integration, "_is_v2_enabled", lambda: True)

    with caplog.at_level("WARNING"):
        initialized = await integration._do_initialize()

    assert initialized is True
    assert any(
        "legacy permission restart paths are frozen" in record.message for record in caplog.records
    )
