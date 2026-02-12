from unittest.mock import AsyncMock, Mock

import pytest

from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.input_processing_integration import InputProcessingIntegration


@pytest.mark.asyncio
async def test_secure_input_healthcheck_cooldown_and_restore(monkeypatch):
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler()

    keyboard_config = KeyboardConfig(
        key_to_monitor="ctrl_n",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.1,
        hold_check_interval=0.05,
        debounce_time=0.1,
        backend="auto",
    )
    config = InputProcessingConfig(
        keyboard=keyboard_config,
        enable_keyboard_monitoring=True,
        auto_start=False,
        keyboard_backend="auto",
        playback_wait_timeout_sec=1.0,
    )

    integration = InputProcessingIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config,
    )

    integration.is_running = True
    integration._using_quartz = True
    integration.keyboard_monitor = Mock()
    integration.keyboard_monitor.get_status = Mock(
        side_effect=[
            {"tap_enabled": False},
            {"tap_enabled": False},
            {"tap_enabled": True},
        ]
    )
    integration._force_stop = AsyncMock()  # type: ignore[method-assign]

    sleep_ticks = {"count": 0}

    async def fake_sleep(_: float):
        sleep_ticks["count"] += 1
        if sleep_ticks["count"] >= 3:
            integration.is_running = False

    monotonic_values = [100.0, 100.2]

    def fake_monotonic() -> float:
        if monotonic_values:
            return monotonic_values.pop(0)
        return 100.2

    monkeypatch.setattr(
        "integration.integrations.input_processing_integration.asyncio.sleep", fake_sleep
    )
    monkeypatch.setattr(
        "integration.integrations.input_processing_integration.time.monotonic",
        fake_monotonic,
    )

    await integration._run_health_check()

    assert integration._force_stop.await_count == 1
    assert integration._secure_input_active is False
    assert integration.ptt_available is True
