"""
Изолированный тест для проверки задержки активации микрофона.

Проверяет:
1. Время между LONG_PRESS и voice.recording_start
2. Время между voice.recording_start и microphone.opened
3. Блокирующие операции в _handle_long_press
4. Влияние playback_idle_grace_sec и playback_wait_timeout_sec
"""

import pytest
import asyncio
import time
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
from integration.integrations.input_processing_integration import InputProcessingIntegration, InputState
from integration.core.state_manager import AppMode


@pytest.fixture
def mock_event_bus():
    """Мок EventBus"""
    bus = Mock(spec=EventBus)
    bus.publish = AsyncMock()
    return bus


@pytest.fixture
def mock_state_manager():
    """Мок StateManager"""
    manager = Mock(spec=ApplicationStateManager)
    manager.is_microphone_active = Mock(return_value=False)
    manager.get_current_mode = Mock(return_value=AppMode.SLEEPING)
    manager.set_session_id = Mock()
    manager.get_session_id = Mock(return_value=None)
    manager.get_microphone_state = Mock(return_value=("idle", None))
    return manager


@pytest.fixture
def mock_error_handler():
    """Мок ErrorHandler"""
    return Mock(spec=ErrorHandler)


@pytest.fixture
def mock_keyboard_monitor():
    """Мок KeyboardMonitor"""
    monitor = Mock()
    monitor.key_pressed = True
    return monitor


@pytest.fixture
def input_integration(mock_event_bus, mock_state_manager, mock_error_handler, mock_keyboard_monitor):
    """Создает InputProcessingIntegration с моками"""
    config = InputProcessingConfig(
        keyboard=KeyboardConfig(
            key_to_monitor="ctrl_n",
            short_press_threshold=0.1,
            long_press_threshold=0.6,
            event_cooldown=0.1,
            hold_check_interval=0.05,
            debounce_time=0.1,
            backend="auto",
            combo_timeout_sec=10.0,
            key_state_timeout_sec=5.0
        ),
        enable_keyboard_monitoring=True,
        auto_start=True,
        min_recording_duration_sec=0.6,
        playback_idle_grace_sec=0.3,
        playback_wait_timeout_sec=5.0,
        recording_prestart_delay_sec=0.0,
        mic_reset_timeout_sec=60.0
    )
    
    integration = InputProcessingIntegration(
        event_bus=mock_event_bus,
        state_manager=mock_state_manager,
        error_handler=mock_error_handler,
        config=config
    )
    
    integration.keyboard_monitor = mock_keyboard_monitor
    integration._playback_active = False  # Воспроизведение не активно
    integration._last_playback_stop_ts = time.monotonic()  # Недавно остановлено
    
    return integration


@pytest.mark.asyncio
async def test_long_press_to_recording_start_delay(input_integration, mock_event_bus):
    """
    Тест 1: Проверка задержки между LONG_PRESS и voice.recording_start
    
    Ожидаемое время: < 0.1 секунды (неблокирующее ожидание)
    """
    # Устанавливаем состояние PENDING (как после PRESS)
    input_integration._input_state = InputState.PENDING
    input_integration._pending_session_id = time.monotonic()
    input_integration._playback_active = False  # Воспроизведение не активно
    input_integration._last_playback_stop_ts = time.monotonic()
    
    # Мокируем методы проверки
    input_integration._can_start_recording = AsyncMock(return_value=(True, "ok"))
    
    # Создаем LONG_PRESS событие
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=time.monotonic(),
        duration=0.6
    )
    
    # Замеряем время
    start_time = time.monotonic()
    await input_integration._handle_long_press(long_press_event)
    elapsed_time = time.monotonic() - start_time
    
    # Проверяем, что voice.recording_start был опубликован
    assert mock_event_bus.publish.called
    published_events = [call[0][0] for call in mock_event_bus.publish.call_args_list]
    assert "voice.recording_start" in published_events
    
    # Проверяем, что задержка минимальна (< 0.1 секунды - неблокирующее)
    print(f"⏱️ Время между LONG_PRESS и voice.recording_start: {elapsed_time:.3f}s")
    assert elapsed_time < 0.1, f"Задержка слишком большая: {elapsed_time:.3f}s (ожидалось < 0.1s для неблокирующего режима)"


@pytest.mark.asyncio
async def test_playback_idle_grace_delay(input_integration):
    """
    Тест 2: Проверка влияния playback_idle_grace_sec на задержку
    
    Ожидаемое время: ~0.3 секунды (playback_idle_grace_sec)
    """
    input_integration._playback_active = False
    input_integration._last_playback_stop_ts = time.monotonic() - 0.1  # Остановлено 0.1 секунды назад
    
    start_time = time.monotonic()
    await input_integration._ensure_playback_idle(for_recording=True)
    elapsed_time = time.monotonic() - start_time
    
    # Проверяем, что задержка соответствует playback_idle_grace_sec
    expected_delay = 0.3 - 0.1  # 0.3 секунды минус уже прошедшее время
    print(f"⏱️ Время _ensure_playback_idle с grace: {elapsed_time:.3f}s (ожидалось ~{expected_delay:.3f}s)")
    assert abs(elapsed_time - expected_delay) < 0.1, f"Задержка не соответствует ожидаемой: {elapsed_time:.3f}s"


@pytest.mark.asyncio
async def test_playback_active_blocking_delay(input_integration):
    """
    Тест 3: Проверка блокировки при активном воспроизведении
    
    Ожидаемое время: < 0.4 секунды (таймаут 0.3s + retry логика)
    """
    input_integration._playback_active = True  # Воспроизведение активно
    input_integration._playback_waiters = []
    
    # Мокируем waiter, который никогда не завершится (симуляция активного воспроизведения)
    async def mock_ensure_playback_idle():
        loop = asyncio.get_running_loop()
        waiter = loop.create_future()
        input_integration._playback_waiters.append(waiter)
        try:
            await asyncio.wait_for(waiter, input_integration._playback_wait_timeout)
        except asyncio.TimeoutError:
            if not waiter.done():
                waiter.set_result(False)
            await asyncio.sleep(0.1)
            for retry in range(3):
                if not input_integration._playback_active:
                    break
                await asyncio.sleep(0.1)
        finally:
            if waiter in input_integration._playback_waiters:
                input_integration._playback_waiters.remove(waiter)
    
    start_time = time.monotonic()
    await asyncio.wait_for(mock_ensure_playback_idle(), timeout=0.3)
    elapsed_time = time.monotonic() - start_time
    
    print(f"⏱️ Время _ensure_playback_idle с активным воспроизведением: {elapsed_time:.3f}s")
    assert elapsed_time < 0.4, f"Задержка слишком большая: {elapsed_time:.3f}s (ожидалось < 0.4s)"


@pytest.mark.asyncio
async def test_full_activation_chain_delay(input_integration, mock_event_bus, mock_state_manager):
    """
    Тест 4: Полная цепочка активации микрофона (LONG_PRESS → microphone.opened)
    
    Ожидаемое время: < 1.0 секунды
    """
    # Устанавливаем состояние
    input_integration._input_state = input_integration.InputState.PENDING
    input_integration._pending_session_id = time.monotonic()
    input_integration._playback_active = False
    input_integration._last_playback_stop_ts = time.monotonic()
    
    # Мокируем методы ожидания
    input_integration._ensure_playback_idle = AsyncMock()
    input_integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
    input_integration._can_start_recording = AsyncMock(return_value=(True, "ok"))
    
    # Мокируем событие microphone.opened (симуляция быстрого открытия микрофона)
    microphone_opened_event = None
    async def mock_publish(event_type, payload):
        nonlocal microphone_opened_event
        if event_type == "voice.recording_start":
            # Симулируем быстрое открытие микрофона
            await asyncio.sleep(0.1)
            microphone_opened_event = ("microphone.opened", payload)
            mock_state_manager.is_microphone_active.return_value = True
    
    mock_event_bus.publish = AsyncMock(side_effect=mock_publish)
    
    # Создаем LONG_PRESS событие
    long_press_event = KeyEvent(
        event_type=KeyEventType.LONG_PRESS,
        key="ctrl_n",
        timestamp=time.monotonic(),
        duration=0.6
    )
    
    # Замеряем время
    start_time = time.monotonic()
    await input_integration._handle_long_press(long_press_event)
    elapsed_time = time.monotonic() - start_time
    
    print(f"⏱️ Полное время активации микрофона: {elapsed_time:.3f}s")
    assert elapsed_time < 1.0, f"Задержка слишком большая: {elapsed_time:.3f}s (ожидалось < 1.0s)"


@pytest.mark.asyncio
async def test_playback_wait_timeout_configuration(input_integration):
    """
    Тест 5: Проверка конфигурации playback_wait_timeout_sec
    
    Проверяет, что таймаут не блокирует дольше необходимого
    """
    # Проверяем, что таймаут установлен правильно
    assert input_integration._playback_wait_timeout == 5.0
    assert input_integration._playback_idle_grace == 0.3
    
    # Проверяем, что в _handle_long_press используется правильный таймаут
    input_integration._playback_active = True
    
    start_time = time.monotonic()
    try:
        await asyncio.wait_for(input_integration._ensure_playback_idle(), timeout=0.3)
    except asyncio.TimeoutError:
        elapsed_time = time.monotonic() - start_time
        print(f"⏱️ Таймаут _ensure_playback_idle: {elapsed_time:.3f}s")
        assert elapsed_time < 0.4, f"Таймаут слишком большой: {elapsed_time:.3f}s"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])

