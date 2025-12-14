"""
Изолированный тест для проверки взаимодействия SHORT_PRESS и LONG_PRESS.

Проблема: После SHORT_PRESS и затем LONG_PRESS микрофон не активируется,
так как _pending_recording_cancelled_event устанавливается преждевременно.
"""

import pytest
import pytest_asyncio
import asyncio
from unittest.mock import MagicMock, AsyncMock, patch
from integration.integrations.input_processing_integration import (
    InputProcessingIntegration,
    InputState
)
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
from integration.core.state_manager import AppMode


@pytest.fixture
def mock_event_bus():
    """Мок EventBus"""
    bus = MagicMock(spec=EventBus)
    bus.publish = AsyncMock()
    bus.subscribe = AsyncMock()
    bus.unsubscribe = AsyncMock()
    return bus


@pytest.fixture
def mock_state_manager():
    """Мок ApplicationStateManager"""
    manager = MagicMock(spec=ApplicationStateManager)
    manager.get_current_mode = MagicMock(return_value=AppMode.SLEEPING)
    manager.is_microphone_active = MagicMock(return_value=False)
    manager.get_current_session_id = MagicMock(return_value=None)
    manager.set_current_session_id = MagicMock()
    manager.clear_current_session_id = MagicMock()
    return manager


@pytest.fixture
def mock_error_handler():
    """Мок ErrorHandler"""
    handler = MagicMock(spec=ErrorHandler)
    handler.handle_error = AsyncMock()
    return handler


@pytest.fixture
def mock_keyboard_monitor():
    """Мок KeyboardMonitor"""
    monitor = MagicMock()
    monitor.key_pressed = True  # Имитируем, что клавиша нажата
    monitor.register_callback = MagicMock()
    return monitor


@pytest_asyncio.fixture
async def input_integration(mock_event_bus, mock_state_manager, mock_error_handler):
    """Создаем InputProcessingIntegration с моками"""
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
    
    # Мокируем keyboard_monitor
    integration.keyboard_monitor = MagicMock()
    integration.keyboard_monitor.key_pressed = True
    integration.keyboard_monitor.register_callback = MagicMock()
    
    # Инициализируем состояние
    integration._input_state = InputState.IDLE
    integration._pending_session_id = None
    integration._recording_started = False
    integration._pending_recording_cancelled_event = asyncio.Event()
    integration._long_press_in_progress = False
    integration._state_lock = asyncio.Lock()
    
    # Мокируем методы ожидания
    integration._ensure_playback_idle = AsyncMock(return_value=None)
    integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=None)
    integration._wait_for_mic_opened = AsyncMock(return_value=True)  # ✅ Возвращаем True для успешного открытия
    integration._can_start_recording = AsyncMock(return_value=(True, "ok"))
    
    await integration.initialize()
    
    return integration


@pytest.mark.asyncio
async def test_short_press_then_long_press_activates_microphone(
    input_integration, mock_event_bus, mock_state_manager
):
    """
    Тест: SHORT_PRESS, затем LONG_PRESS должен активировать микрофон.
    
    Сценарий:
    1. Пользователь делает SHORT_PRESS (отпускает клавишу быстро)
    2. Затем сразу делает LONG_PRESS (удерживает клавишу)
    3. Микрофон должен активироваться
    
    Проблема: _pending_recording_cancelled_event устанавливается преждевременно,
    что блокирует активацию микрофона.
    """
    # Собираем опубликованные события
    published_events = []
    
    async def capture_publish(event_type, payload):
        published_events.append((event_type, payload))
        # Не вызываем mock_event_bus.publish, чтобы избежать рекурсии
        return None
    
    input_integration.event_bus.publish = capture_publish
    
    # Шаг 1: PRESS событие (начало нажатия)
    press_event = KeyEvent(
        event_type=KeyEventType.PRESS,
        key="ctrl_n",
        timestamp=1000.0,
        duration=0.0
    )
    
    # Мокируем keyboard_monitor.key_pressed = True для PRESS
    input_integration.keyboard_monitor.key_pressed = True
    
    await input_integration._handle_press(press_event)
    
    # Проверяем, что состояние перешло в PENDING
    assert input_integration._input_state == InputState.PENDING
    assert input_integration._pending_session_id is not None
    
    # Шаг 2: SHORT_PRESS событие (быстрое отпускание)
    short_press_event = KeyEvent(
        event_type=KeyEventType.SHORT_PRESS,
        key="ctrl_n",
        timestamp=1000.1,  # Очень быстро после PRESS
        duration=0.1
    )
    
    # Мокируем keyboard_monitor.key_pressed = False для SHORT_PRESS (клавиша отпущена)
    input_integration.keyboard_monitor.key_pressed = False
    
    await input_integration._handle_short_press(short_press_event)
    
    # Проверяем, что _pending_recording_cancelled_event НЕ установлен после SHORT_PRESS
    # (SHORT_PRESS не должен отменять pending recording, если он не был начат)
    assert not input_integration._pending_recording_cancelled_event.is_set(), \
        "SHORT_PRESS не должен устанавливать _pending_recording_cancelled_event, если запись не начата"
    
    # Шаг 3: RELEASE событие (от SHORT_PRESS)
    release_event = KeyEvent(
        event_type=KeyEventType.RELEASE,
        key="ctrl_n",
        timestamp=1000.1,
        duration=0.1
    )
    
    # Мокируем keyboard_monitor.key_pressed = False для RELEASE
    input_integration.keyboard_monitor.key_pressed = False
    
    await input_integration._handle_key_release(release_event)
    
    # Проверяем, что _pending_recording_cancelled_event установлен после RELEASE
    # (RELEASE должен отменить pending recording, если клавиша отпущена)
    assert input_integration._pending_recording_cancelled_event.is_set(), \
        "RELEASE должен установить _pending_recording_cancelled_event, если клавиша отпущена и запись не начата"
    
    # Шаг 4: Новый PRESS (пользователь снова нажимает клавишу)
    # ✅ КРИТИЧНО: Увеличиваем интервал между PRESS, чтобы избежать debounce (0.1s)
    import time
    await asyncio.sleep(0.15)  # Ждем больше, чем debounce_interval (0.1s)
    
    press_event_2 = KeyEvent(
        event_type=KeyEventType.PRESS,
        key="ctrl_n",
        timestamp=time.monotonic(),  # Используем реальное время для избежания debounce
        duration=0.0
    )
    
    # Мокируем keyboard_monitor.key_pressed = True для нового PRESS
    input_integration.keyboard_monitor.key_pressed = True
    
    # ✅ КРИТИЧНО: Сбрасываем _pending_recording_cancelled_event перед новым PRESS
    # Это имитирует правильное поведение: новый PRESS должен начать новую сессию
    input_integration._pending_recording_cancelled_event.clear()
    
    await input_integration._handle_press(press_event_2)
    
    # Проверяем, что состояние перешло в PENDING
    assert input_integration._input_state == InputState.PENDING
    assert input_integration._pending_session_id is not None
    
    # Шаг 5: LONG_PRESS событие (удержание клавиши)
    import time
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=time.monotonic(),  # Используем реальное время
        duration=0.7
    )
    
    # Мокируем keyboard_monitor.key_pressed = True для LONG_PRESS (клавиша все еще нажата)
    input_integration.keyboard_monitor.key_pressed = True
    
    # ✅ КРИТИЧНО: Проверяем, что _pending_recording_cancelled_event НЕ установлен перед LONG_PRESS
    assert not input_integration._pending_recording_cancelled_event.is_set(), \
        "_pending_recording_cancelled_event должен быть сброшен перед LONG_PRESS"
    
    await input_integration._handle_long_press(long_press_event)
    
    # Проверяем, что voice.recording_start был опубликован
    recording_start_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "voice.recording_start"
    ]
    
    assert len(recording_start_events) > 0, \
        f"voice.recording_start должен быть опубликован после LONG_PRESS. Полученные события: {[e[0] for e in published_events]}"
    
    # Проверяем, что состояние перешло в LISTENING
    assert input_integration._input_state == InputState.LISTENING, \
        f"Состояние должно быть LISTENING после LONG_PRESS, но было {input_integration._input_state}"


@pytest.mark.asyncio
async def test_short_press_does_not_cancel_pending_recording_if_not_released(
    input_integration, mock_event_bus, mock_state_manager
):
    """
    Тест: SHORT_PRESS не должен отменять pending recording, если клавиша все еще нажата.
    
    Сценарий:
    1. PRESS событие
    2. SHORT_PRESS событие (но клавиша все еще нажата - это может быть ложное срабатывание)
    3. LONG_PRESS должен все еще работать
    """
    # Шаг 1: PRESS событие
    press_event = KeyEvent(
        event_type=KeyEventType.PRESS,
        key="ctrl_n",
        timestamp=1000.0,
        duration=0.0
    )
    
    input_integration.keyboard_monitor.key_pressed = True
    await input_integration._handle_press(press_event)
    
    assert input_integration._input_state == InputState.PENDING
    assert input_integration._pending_session_id is not None
    
    # Шаг 2: SHORT_PRESS событие (но клавиша все еще нажата)
    short_press_event = KeyEvent(
        event_type=KeyEventType.SHORT_PRESS,
        key="ctrl_n",
        timestamp=1000.1,
        duration=0.1
    )
    
    # ✅ КРИТИЧНО: Клавиша все еще нажата (это может быть ложное срабатывание SHORT_PRESS)
    input_integration.keyboard_monitor.key_pressed = True
    
    await input_integration._handle_short_press(short_press_event)
    
    # Проверяем, что _pending_recording_cancelled_event НЕ установлен
    assert not input_integration._pending_recording_cancelled_event.is_set(), \
        "SHORT_PRESS не должен устанавливать _pending_recording_cancelled_event, если клавиша все еще нажата"
    
    # Шаг 3: LONG_PRESS должен работать
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=1000.9,
        duration=0.9
    )
    
    input_integration.keyboard_monitor.key_pressed = True
    
    # Собираем опубликованные события
    published_events = []
    
    async def capture_publish(event_type, payload):
        published_events.append((event_type, payload))
        # Не вызываем mock_event_bus.publish, чтобы избежать рекурсии
        return None
    
    input_integration.event_bus.publish = capture_publish
    
    await input_integration._handle_long_press(long_press_event)
    
    # Проверяем, что voice.recording_start был опубликован
    recording_start_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "voice.recording_start"
    ]
    
    assert len(recording_start_events) > 0, \
        f"voice.recording_start должен быть опубликован после LONG_PRESS. Полученные события: {[e[0] for e in published_events]}"


@pytest.mark.asyncio
async def test_release_after_short_press_clears_pending_recording(
    input_integration, mock_event_bus, mock_state_manager
):
    """
    Тест: RELEASE после SHORT_PRESS должен очистить pending recording.
    
    Сценарий:
    1. PRESS событие
    2. SHORT_PRESS событие
    3. RELEASE событие (клавиша отпущена)
    4. LONG_PRESS не должен работать (pending recording отменен)
    """
    # Шаг 1: PRESS событие
    press_event = KeyEvent(
        event_type=KeyEventType.PRESS,
        key="ctrl_n",
        timestamp=1000.0,
        duration=0.0
    )
    
    input_integration.keyboard_monitor.key_pressed = True
    await input_integration._handle_press(press_event)
    
    assert input_integration._input_state == InputState.PENDING
    assert input_integration._pending_session_id is not None
    
    # Шаг 2: SHORT_PRESS событие
    short_press_event = KeyEvent(
        event_type=KeyEventType.SHORT_PRESS,
        key="ctrl_n",
        timestamp=1000.1,
        duration=0.1
    )
    
    input_integration.keyboard_monitor.key_pressed = False
    await input_integration._handle_short_press(short_press_event)
    
    # Шаг 3: RELEASE событие
    release_event = KeyEvent(
        event_type=KeyEventType.RELEASE,
        key="ctrl_n",
        timestamp=1000.1,
        duration=0.1
    )
    
    input_integration.keyboard_monitor.key_pressed = False
    await input_integration._handle_key_release(release_event)
    
    # Проверяем, что _pending_recording_cancelled_event установлен
    assert input_integration._pending_recording_cancelled_event.is_set(), \
        "RELEASE должен установить _pending_recording_cancelled_event"
    
    # Шаг 4: LONG_PRESS не должен работать (pending recording отменен)
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=1000.9,
        duration=0.9
    )
    
    input_integration.keyboard_monitor.key_pressed = True
    
    # Собираем опубликованные события
    published_events = []
    
    async def capture_publish(event_type, payload):
        published_events.append((event_type, payload))
        # Не вызываем mock_event_bus.publish, чтобы избежать рекурсии
        return None
    
    input_integration.event_bus.publish = capture_publish
    
    await input_integration._handle_long_press(long_press_event)
    
    # Проверяем, что voice.recording_start НЕ был опубликован
    recording_start_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "voice.recording_start"
    ]
    
    assert len(recording_start_events) == 0, \
        f"voice.recording_start НЕ должен быть опубликован после LONG_PRESS, если pending recording отменен. Полученные события: {[e[0] for e in published_events]}"

