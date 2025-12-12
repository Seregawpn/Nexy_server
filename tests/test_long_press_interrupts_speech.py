"""
Тесты для проверки прерывания речи при LONG_PRESS во время воспроизведения.

Проверяет, что LONG_PRESS во время воспроизведения речи ассистента
корректно прерывает воспроизведение и активирует микрофон.
"""

import pytest
import pytest_asyncio
from unittest.mock import MagicMock, AsyncMock, patch
import asyncio
from integration.core.state_manager import AppMode

from integration.integrations.input_processing_integration import InputProcessingIntegration, InputState
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType


@pytest_asyncio.fixture
async def input_integration():
    """Создаёт изолированный экземпляр InputProcessingIntegration для тестирования"""
    mock_event_bus = MagicMock(spec=EventBus)
    published_events = []
    
    async def mock_publish(event_type, payload=None):
        if payload is None:
            payload = {}
        published_events.append((event_type, payload))
    
    mock_event_bus.publish = AsyncMock(side_effect=mock_publish)
    mock_event_bus.subscribe = AsyncMock()
    mock_event_bus.unsubscribe = AsyncMock()
    
    mock_state_manager = MagicMock(spec=ApplicationStateManager)
    mock_state_manager.get_current_mode = MagicMock(return_value=AppMode.PROCESSING)
    mock_state_manager.get_current_session_id = MagicMock(return_value="test_session_123")
    mock_state_manager.is_microphone_active = MagicMock(return_value=False)
    mock_state_manager.set_microphone_state = MagicMock()
    mock_state_manager.force_close_microphone = MagicMock()
    mock_state_manager.update_session_id = MagicMock()
    
    mock_error_handler = MagicMock(spec=ErrorHandler)
    
    from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
    
    keyboard_config = KeyboardConfig(
        key_to_monitor="ctrl_n",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.05,
        hold_check_interval=0.05,
        debounce_time=0.05,
        backend="auto",
    )
    
    config = InputProcessingConfig(
        keyboard=keyboard_config,
        enable_keyboard_monitoring=True,
        auto_start=False,
        keyboard_backend="auto",
        min_recording_duration_sec=0.1,
        playback_idle_grace_sec=0.3,
        playback_wait_timeout_sec=5.0,
        recording_prestart_delay_sec=0.0,
        mic_reset_timeout_sec=5.0,
    )
    
    integration = InputProcessingIntegration(
        event_bus=mock_event_bus,
        state_manager=mock_state_manager,
        error_handler=mock_error_handler,
        config=config
    )
    
    # Мокируем методы ожидания
    integration._ensure_playback_idle = AsyncMock(return_value=None)
    integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=None)
    integration._wait_for_mic_opened = AsyncMock(return_value=True)
    integration._can_start_recording = AsyncMock(return_value=(True, "ok"))
    
    # Мокируем keyboard_monitor
    mock_keyboard_monitor = MagicMock()
    mock_keyboard_monitor.key_pressed = True
    integration.keyboard_monitor = mock_keyboard_monitor
    
    yield integration, mock_event_bus, mock_state_manager, published_events


@pytest.mark.asyncio
async def test_long_press_interrupts_speech_during_playback(input_integration):
    """Тест: LONG_PRESS во время воспроизведения речи прерывает воспроизведение"""
    integration, mock_event_bus, mock_state_manager, published_events = input_integration
    
    # Устанавливаем, что воспроизведение активно
    integration._playback_active = True
    integration._active_grpc_session_id = "test_session_123"
    
    # Создаём LONG_PRESS событие
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=1000.0,
        duration=0.7
    )
    
    # Вызываем обработчик LONG_PRESS
    await integration._handle_long_press(long_press_event)
    
    # Проверяем, что interrupt.request был опубликован
    interrupt_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "interrupt.request"
    ]
    assert len(interrupt_events) > 0, "interrupt.request должен быть опубликован при LONG_PRESS во время PROCESSING"
    
    # Проверяем, что interrupt.request содержит правильные данные
    interrupt_payload = interrupt_events[0][1]
    assert interrupt_payload.get("source") == "keyboard", "source должен быть 'keyboard'"
    assert interrupt_payload.get("reason") == "user_interrupt", "reason должен быть 'user_interrupt'"
    assert interrupt_payload.get("session_id") == "test_session_123", "session_id должен совпадать с активной сессией"
    
    # Проверяем, что _ensure_playback_idle был вызван для ожидания остановки воспроизведения
    assert integration._ensure_playback_idle.called, "_ensure_playback_idle должен быть вызван для ожидания остановки воспроизведения"


@pytest.mark.asyncio
async def test_long_press_publishes_grpc_cancel_during_playback(input_integration):
    """Тест: LONG_PRESS во время воспроизведения публикует grpc.request_cancel"""
    integration, mock_event_bus, mock_state_manager, published_events = input_integration
    
    # Устанавливаем активную gRPC сессию
    integration._active_grpc_session_id = "test_grpc_session_456"
    
    # Создаём LONG_PRESS событие
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=1000.0,
        duration=0.7
    )
    
    # Вызываем обработчик LONG_PRESS
    await integration._handle_long_press(long_press_event)
    
    # Проверяем, что grpc.request_cancel был опубликован
    grpc_cancel_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "grpc.request_cancel"
    ]
    assert len(grpc_cancel_events) > 0, "grpc.request_cancel должен быть опубликован при LONG_PRESS с активной gRPC сессией"
    
    # Проверяем, что session_id совпадает
    grpc_cancel_payload = grpc_cancel_events[0][1]
    assert grpc_cancel_payload.get("session_id") == "test_grpc_session_456", "session_id должен совпадать с активной gRPC сессией"


@pytest.mark.asyncio
async def test_long_press_waits_for_playback_stop(input_integration):
    """Тест: LONG_PRESS ждет остановки воспроизведения перед активацией микрофона"""
    integration, mock_event_bus, mock_state_manager, published_events = input_integration
    
    # Устанавливаем, что воспроизведение активно
    integration._playback_active = True
    
    # Создаём LONG_PRESS событие
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=1000.0,
        duration=0.7
    )
    
    # Вызываем обработчик LONG_PRESS
    await integration._handle_long_press(long_press_event)
    
    # Проверяем, что _ensure_playback_idle был вызван
    assert integration._ensure_playback_idle.called, "_ensure_playback_idle должен быть вызван для ожидания остановки воспроизведения"
    
    # Проверяем, что _wait_for_mic_closed_with_timeout был вызван после остановки воспроизведения
    assert integration._wait_for_mic_closed_with_timeout.called, "_wait_for_mic_closed_with_timeout должен быть вызван после остановки воспроизведения"


@pytest.mark.asyncio
async def test_long_press_activates_microphone_after_interrupt(input_integration):
    """Тест: LONG_PRESS активирует микрофон после прерывания воспроизведения"""
    integration, mock_event_bus, mock_state_manager, published_events = input_integration
    
    # Устанавливаем, что воспроизведение активно
    integration._playback_active = True
    integration._input_state = InputState.PENDING
    
    # Создаём LONG_PRESS событие
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=1000.0,
        duration=0.7
    )
    
    # Вызываем обработчик LONG_PRESS
    await integration._handle_long_press(long_press_event)
    
    # Проверяем, что voice.recording_start был опубликован после прерывания
    recording_start_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "voice.recording_start"
    ]
    assert len(recording_start_events) > 0, "voice.recording_start должен быть опубликован после прерывания воспроизведения"
    
    # Проверяем, что interrupt.request был опубликован ПЕРЕД voice.recording_start
    interrupt_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "interrupt.request"
    ]
    recording_start_events_list = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "voice.recording_start"
    ]
    
    # Находим индексы событий
    interrupt_index = None
    recording_index = None
    for i, (event_type, _) in enumerate(published_events):
        if event_type == "interrupt.request" and interrupt_index is None:
            interrupt_index = i
        if event_type == "voice.recording_start" and recording_index is None:
            recording_index = i
    
    assert interrupt_index is not None, "interrupt.request должен быть опубликован"
    assert recording_index is not None, "voice.recording_start должен быть опубликован"
    assert interrupt_index < recording_index, "interrupt.request должен быть опубликован ПЕРЕД voice.recording_start"


@pytest.mark.asyncio
async def test_long_press_timeout_force_interrupt(input_integration):
    """Тест: LONG_PRESS принудительно прерывает воспроизведение при таймауте ожидания"""
    integration, mock_event_bus, mock_state_manager, published_events = input_integration
    
    # Устанавливаем, что воспроизведение активно
    integration._playback_active = True
    integration._active_grpc_session_id = "test_session_123"
    
    # Мокируем _ensure_playback_idle, чтобы он вызывал TimeoutError
    async def mock_ensure_playback_idle_timeout():
        raise asyncio.TimeoutError("Timeout waiting for playback to stop")
    
    integration._ensure_playback_idle = AsyncMock(side_effect=mock_ensure_playback_idle_timeout)
    
    # Создаём LONG_PRESS событие
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=1000.0,
        duration=0.7
    )
    
    # Вызываем обработчик LONG_PRESS
    await integration._handle_long_press(long_press_event)
    
    # Проверяем, что interrupt.request был опубликован дважды (первый раз в начале, второй раз при таймауте)
    interrupt_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "interrupt.request"
    ]
    assert len(interrupt_events) >= 2, "interrupt.request должен быть опубликован дважды (в начале и при таймауте)"
    
    # Проверяем, что второй interrupt.request имеет reason="timeout"
    timeout_interrupts = [
        payload
        for event_type, payload in interrupt_events
        if payload.get("reason") == "timeout"
    ]
    assert len(timeout_interrupts) > 0, "interrupt.request с reason='timeout' должен быть опубликован при таймауте"

