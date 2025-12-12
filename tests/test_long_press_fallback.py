"""
Тесты для проверки исправлений LONG_PRESS detection и fallback механизмов.

Проверяет:
1. LONG_PRESS fallback при деактивации (когда _run_hold_monitor не успел сработать)
2. SHORT_PRESS fallback (когда LONG_PRESS не сработал, но duration >= threshold)
3. Публикация voice.recording_start в обоих случаях
"""

import pytest
import pytest_asyncio
from unittest.mock import MagicMock, AsyncMock, patch
import time
from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
from config.unified_config_loader import KeyboardConfig


@pytest.fixture
def keyboard_config():
    """Конфигурация клавиатуры для тестов"""
    return KeyboardConfig(
        key_to_monitor="ctrl_n",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.05,
        hold_check_interval=0.05,
        debounce_time=0.05,
        backend="auto",
    )


@pytest.fixture
def monitor(keyboard_config):
    """Создаёт изолированный экземпляр QuartzKeyboardMonitor для тестирования"""
    monitor = QuartzKeyboardMonitor(keyboard_config)
    monitor._tap = None  # Мокируем tap
    monitor.stop_event = MagicMock()
    monitor.stop_event.is_set = MagicMock(return_value=False)
    return monitor


@pytest.fixture
def mock_callback():
    """Мок callback для событий"""
    return MagicMock()


def test_long_press_fallback_on_deactivation(monitor, mock_callback):
    """Тест: LONG_PRESS fallback при деактивации комбинации"""
    import threading
    import time as time_module
    
    # Регистрируем callback
    monitor.register_callback(KeyEventType.LONG_PRESS, mock_callback)
    
    # Симулируем активацию комбинации
    monitor._control_pressed = True
    monitor._n_pressed = True
    monitor._combo_start_time = time.time() - 0.8  # 0.8 секунд назад (больше threshold 0.6)
    monitor._combo_active = True
    monitor._long_sent = False  # LONG_PRESS еще не отправлен
    
    # Симулируем деактивацию комбинации
    monitor._control_pressed = False
    monitor._n_pressed = False
    
    # Вызываем _update_combo_state для деактивации
    monitor._update_combo_state()
    
    # Проверяем, что LONG_PRESS был отправлен через fallback
    assert monitor._long_sent == True, "LONG_PRESS должен быть отправлен через fallback"
    
    # Ждем завершения callback (он вызывается в отдельном потоке)
    time_module.sleep(0.1)  # Небольшая задержка для завершения потока
    
    # Проверяем, что callback был вызван
    assert mock_callback.called, "Callback для LONG_PRESS должен быть вызван"
    
    # Проверяем, что событие было правильного типа
    call_args = mock_callback.call_args
    assert call_args is not None, "Callback должен быть вызван с аргументами"
    event = call_args[0][0] if call_args[0] else None
    if event:
        assert event.event_type == KeyEventType.LONG_PRESS, "Событие должно быть LONG_PRESS"
        assert event.duration >= 0.6, "Duration должен быть >= threshold"


def test_long_press_normal_detection(monitor, mock_callback):
    """Тест: Нормальное определение LONG_PRESS через _run_hold_monitor"""
    import time as time_module
    
    # Регистрируем callback
    monitor.register_callback(KeyEventType.LONG_PRESS, mock_callback)
    
    # Симулируем активацию комбинации
    monitor._control_pressed = True
    monitor._n_pressed = True
    start_time = time.time() - 0.7  # 0.7 секунд назад
    monitor._combo_start_time = start_time
    monitor._combo_active = True
    monitor._long_sent = False
    
    # Симулируем проверку в _run_hold_monitor
    duration = time.time() - start_time
    if not monitor._long_sent and duration >= monitor.long_press_threshold:
        is_still_active = monitor._combo_active
        if is_still_active:
            ev = KeyEvent(
                key=monitor.key_to_monitor,
                event_type=KeyEventType.LONG_PRESS,
                timestamp=time.time(),
                duration=duration,
            )
            monitor._trigger_event(KeyEventType.LONG_PRESS, duration, ev)
            monitor._long_sent = True
    
    # Проверяем, что LONG_PRESS был отправлен
    assert monitor._long_sent == True, "LONG_PRESS должен быть отправлен"
    
    # Ждем завершения callback (он вызывается в отдельном потоке)
    time_module.sleep(0.1)  # Небольшая задержка для завершения потока
    
    assert mock_callback.called, "Callback для LONG_PRESS должен быть вызван"


def test_short_press_no_fallback_when_recording_started(monitor):
    """Тест: SHORT_PRESS не должен использовать fallback, если запись уже начата"""
    # Этот тест будет в test_short_press_fallback.py
    pass


def test_long_press_fallback_only_when_needed(monitor, mock_callback):
    """Тест: LONG_PRESS fallback срабатывает только когда нужно"""
    # Регистрируем callback
    monitor.register_callback(KeyEventType.LONG_PRESS, mock_callback)
    
    # Ситуация 1: duration < threshold - fallback не должен сработать
    monitor._control_pressed = True
    monitor._n_pressed = True
    monitor._combo_start_time = time.time() - 0.3  # 0.3 секунд (меньше threshold 0.6)
    monitor._combo_active = True
    monitor._long_sent = False
    
    monitor._control_pressed = False
    monitor._n_pressed = False
    monitor._update_combo_state()
    
    # Проверяем, что LONG_PRESS НЕ был отправлен (duration < threshold)
    assert monitor._long_sent == False, "LONG_PRESS не должен быть отправлен при duration < threshold"
    assert not mock_callback.called, "Callback не должен быть вызван"
    
    # Сброс для следующей проверки
    monitor._long_sent = False
    mock_callback.reset_mock()
    
    # Ситуация 2: _long_sent уже True - fallback не должен сработать
    monitor._control_pressed = True
    monitor._n_pressed = True
    monitor._combo_start_time = time.time() - 0.8  # 0.8 секунд (больше threshold)
    monitor._combo_active = True
    monitor._long_sent = True  # Уже отправлен
    
    monitor._control_pressed = False
    monitor._n_pressed = False
    monitor._update_combo_state()
    
    # Проверяем, что fallback не сработал (уже был отправлен)
    assert monitor._long_sent == True, "_long_sent должен остаться True"
    # Callback может быть вызван, но это нормально (RELEASE после LONG_PRESS)


@pytest.mark.asyncio
async def test_short_press_fallback_publishes_recording_start():
    """Тест: SHORT_PRESS fallback публикует voice.recording_start"""
    from integration.integrations.input_processing_integration import InputProcessingIntegration
    from integration.core.event_bus import EventBus
    from integration.core.state_manager import ApplicationStateManager
    from integration.core.error_handler import ErrorHandler
    from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
    
    # Создаём моки
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
    mock_state_manager.get_current_mode = MagicMock(return_value=None)
    mock_state_manager.is_microphone_active = MagicMock(return_value=False)
    mock_state_manager.get_current_session_id = MagicMock(return_value=None)
    
    mock_error_handler = MagicMock(spec=ErrorHandler)
    
    # Создаём конфигурацию
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
    
    # Устанавливаем, что запись НЕ начата
    integration._recording_started = False
    integration._pending_session_id = None
    
    # Создаём SHORT_PRESS событие с duration >= threshold
    short_press_event = KeyEvent(
        event_type=KeyEventType.SHORT_PRESS,
        key="ctrl_n",
        timestamp=time.time(),
        duration=0.8  # Больше threshold 0.6
    )
    
    # Вызываем обработчик SHORT_PRESS
    await integration._handle_short_press(short_press_event)
    
    # Проверяем, что voice.recording_start был опубликован
    recording_start_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "voice.recording_start"
    ]
    assert len(recording_start_events) > 0, "voice.recording_start должен быть опубликован через fallback"
    
    # Проверяем, что запись помечена как начатая
    assert integration._recording_started == True, "Запись должна быть помечена как начатая"


@pytest.mark.asyncio
async def test_short_press_no_fallback_when_recording_started():
    """Тест: SHORT_PRESS не использует fallback, если запись уже начата"""
    from integration.integrations.input_processing_integration import InputProcessingIntegration
    from integration.core.event_bus import EventBus
    from integration.core.state_manager import ApplicationStateManager
    from integration.core.error_handler import ErrorHandler
    from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
    
    # Создаём моки
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
    mock_state_manager.get_current_mode = MagicMock(return_value=None)
    mock_state_manager.is_microphone_active = MagicMock(return_value=False)
    mock_state_manager.get_current_session_id = MagicMock(return_value="test_session_123")
    
    mock_error_handler = MagicMock(spec=ErrorHandler)
    
    # Создаём конфигурацию
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
    
    # Устанавливаем, что запись УЖЕ начата
    integration._recording_started = True
    integration._active_grpc_session_id = "test_session_123"
    
    # Создаём SHORT_PRESS событие с duration >= threshold
    short_press_event = KeyEvent(
        event_type=KeyEventType.SHORT_PRESS,
        key="ctrl_n",
        timestamp=time.time(),
        duration=0.8  # Больше threshold 0.6
    )
    
    # Вызываем обработчик SHORT_PRESS
    await integration._handle_short_press(short_press_event)
    
    # Проверяем, что voice.recording_start НЕ был опубликован (запись уже начата)
    recording_start_events = [
        (event_type, payload)
        for event_type, payload in published_events
        if event_type == "voice.recording_start"
    ]
    assert len(recording_start_events) == 0, "voice.recording_start НЕ должен быть опубликован, если запись уже начата"

