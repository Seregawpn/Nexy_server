"""
Поведенческие тесты: отсутствие дублей/блокировок в InputProcessingIntegration.
"""

import asyncio
import time
from unittest.mock import AsyncMock, Mock

import pytest
import pytest_asyncio

from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.input_processing_integration import InputProcessingIntegration, PTTState
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType


@pytest.fixture
def event_bus():
    bus = Mock(spec=EventBus)
    bus.subscribe = AsyncMock()
    bus.unsubscribe = AsyncMock()
    bus._published_events = []  # (event_name, data, ts)
    bus._event_counts = {}

    async def _publish(name, data=None):
        ts = time.time()
        bus._published_events.append((name, data, ts))
        bus._event_counts[name] = bus._event_counts.get(name, 0) + 1
        return None

    bus.publish = AsyncMock(side_effect=_publish)
    return bus


@pytest.fixture
def state_manager():
    manager = Mock(spec=ApplicationStateManager)
    manager.set_state_data = Mock()
    manager.update_session_id = Mock()
    manager.set_mode = Mock()
    return manager


@pytest.fixture
def input_config():
    keyboard = KeyboardConfig(
        key_to_monitor="left_shift",
        short_press_threshold=0.1,
        long_press_threshold=0.5,
        event_cooldown=0.05,
        hold_check_interval=0.05,
        debounce_time=0.05,
        backend="auto",
    )
    return InputProcessingConfig(
        keyboard=keyboard,
        enable_keyboard_monitoring=True,
        auto_start=False,
        keyboard_backend="auto",
        min_recording_duration_sec=0.1,
        playback_idle_grace_sec=0.3,
        playback_wait_timeout_sec=5.0,
        recording_prestart_delay_sec=0.0,
    )


@pytest_asyncio.fixture
async def input_integration(event_bus, state_manager, input_config):
    integration = InputProcessingIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(event_bus),
        config=input_config,
    )
    await integration.initialize()
    return integration


@pytest.mark.asyncio
async def test_long_press_non_blocking_and_publishes_required_events(input_integration, event_bus):
    input_integration._state = PTTState.ARMED
    input_integration._pending_session_id = "11111111-1111-4111-8111-111111111111"

    event = KeyEvent(
        key="left_shift",
        event_type=KeyEventType.LONG_PRESS,
        timestamp=1234567890.0,
        duration=0.7,
    )

    start = time.time()
    await input_integration._handle_long_press(event)
    elapsed = time.time() - start

    assert elapsed < 0.1
    assert event_bus._event_counts.get("voice.recording_start", 0) == 1
    assert event_bus._event_counts.get("mode.request", 0) == 1
    assert input_integration._recording_started is True


@pytest.mark.asyncio
async def test_repeated_long_press_does_not_duplicate_terminal_start(input_integration, event_bus):
    input_integration._state = PTTState.ARMED
    input_integration._pending_session_id = "22222222-2222-4222-8222-222222222222"

    event = KeyEvent(
        key="left_shift",
        event_type=KeyEventType.LONG_PRESS,
        timestamp=1234567890.0,
        duration=0.7,
    )

    await input_integration._handle_long_press(event)
    # Второй вызов должен быть проигнорирован (state уже RECORDING).
    await input_integration._handle_long_press(event)

    assert event_bus._event_counts.get("voice.recording_start", 0) == 1
    assert event_bus._event_counts.get("mode.request", 0) == 1


@pytest.mark.asyncio
async def test_event_order_recording_start_before_mode_request(input_integration, event_bus):
    input_integration._state = PTTState.ARMED
    input_integration._pending_session_id = "33333333-3333-4333-8333-333333333333"

    event = KeyEvent(
        key="left_shift",
        event_type=KeyEventType.LONG_PRESS,
        timestamp=1234567890.0,
        duration=0.7,
    )

    await input_integration._handle_long_press(event)
    await asyncio.sleep(0)

    names = [name for name, _, _ in event_bus._published_events]
    assert "voice.recording_start" in names
    assert "mode.request" in names
    assert names.index("voice.recording_start") < names.index("mode.request")
