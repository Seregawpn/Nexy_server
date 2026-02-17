from unittest.mock import AsyncMock, Mock

import pytest

from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.integrations.input_processing_integration import InputProcessingIntegration, PTTState


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


@pytest.mark.asyncio
async def test_secure_input_healthcheck_attempts_monitor_recovery(monkeypatch):
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
    integration._tap_recovery_retry_sec = 5.0
    integration.is_running = True
    integration._using_quartz = True
    integration._force_stop = AsyncMock()  # type: ignore[method-assign]

    tap_state = {"enabled": False}
    stop_calls = {"count": 0}
    start_calls = {"count": 0}

    monitor = Mock()

    def _status():
        return {"tap_enabled": tap_state["enabled"]}

    def _stop():
        stop_calls["count"] += 1

    def _start():
        start_calls["count"] += 1
        tap_state["enabled"] = True
        return True

    monitor.get_status = Mock(side_effect=_status)
    monitor.stop_monitoring = Mock(side_effect=_stop)
    monitor.start_monitoring = Mock(side_effect=_start)
    integration.keyboard_monitor = monitor

    sleep_ticks = {"count": 0}

    async def fake_sleep(_: float):
        sleep_ticks["count"] += 1
        if sleep_ticks["count"] >= 3:
            integration.is_running = False

    monotonic_values = [100.0, 106.0, 106.0]

    def fake_monotonic() -> float:
        if monotonic_values:
            return monotonic_values.pop(0)
        return 106.0

    monkeypatch.setattr(
        "integration.integrations.input_processing_integration.asyncio.sleep", fake_sleep
    )
    monkeypatch.setattr(
        "integration.integrations.input_processing_integration.time.monotonic",
        fake_monotonic,
    )

    await integration._run_health_check()

    assert integration._force_stop.await_count == 1
    assert stop_calls["count"] == 1
    assert start_calls["count"] == 1
    assert integration._secure_input_active is False
    assert integration.ptt_available is True


@pytest.mark.asyncio
async def test_quartz_release_watchdog_forces_terminal_stop(monkeypatch):
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
    integration._state = PTTState.RECORDING
    integration._recording_started = True
    integration._active_press_id = "press-1"
    state_manager.set_mode(AppMode.LISTENING, session_id="sid-1")

    monitor = Mock()
    monitor.get_status = Mock(
        side_effect=[
            {
                "tap_enabled": True,
                "combo_active": False,
                "control_pressed": False,
                "n_pressed": False,
            },
            {
                "tap_enabled": True,
                "combo_active": False,
                "control_pressed": False,
                "n_pressed": False,
            },
        ]
    )
    integration.keyboard_monitor = monitor

    stop_calls = {"count": 0}

    async def fake_request_terminal_stop(**kwargs):
        stop_calls["count"] += 1
        integration._recording_started = False
        return True

    integration._request_terminal_stop = fake_request_terminal_stop  # type: ignore[method-assign]

    mode_requests: list[dict] = []

    async def on_mode_request(event):
        mode_requests.append(event.get("data", {}))

    await event_bus.subscribe("mode.request", on_mode_request)

    sleep_ticks = {"count": 0}

    async def fake_sleep(_: float):
        sleep_ticks["count"] += 1
        if sleep_ticks["count"] >= 2:
            integration.is_running = False

    monkeypatch.setattr(
        "integration.integrations.input_processing_integration.asyncio.sleep", fake_sleep
    )

    await integration._run_health_check()

    assert stop_calls["count"] == 1
    assert len(mode_requests) == 1
    assert mode_requests[0].get("source") == "input_processing.quartz_release_watchdog"
