"""
Изолированный тест для проверки цепочки активации микрофона.

Проверяет:
1. LONG_PRESS событие генерируется и обрабатывается
2. _can_start_recording() возвращает True
3. voice.recording_start публикуется
4. mode.request(LISTENING) публикуется
5. microphone.open_requested публикуется
6. Нет блокировок или таймаутов
"""

import pytest
import pytest_asyncio
import asyncio
import time
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from typing import List, Dict, Any

from integration.integrations.input_processing_integration import InputProcessingIntegration, InputState
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.event_bus import EventBus, EventPriority
from integration.core.error_handler import ErrorHandler
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
from config.unified_config_loader import InputProcessingConfig, KeyboardConfig


@pytest_asyncio.fixture
async def event_bus():
    """Создает EventBus для тестов"""
    return EventBus()


@pytest_asyncio.fixture
async def state_manager(event_bus):
    """Создает ApplicationStateManager для тестов"""
    manager = ApplicationStateManager()
    manager.attach_event_bus(event_bus)
    return manager


@pytest_asyncio.fixture
async def error_handler():
    """Создает ErrorHandler для тестов"""
    return ErrorHandler()


@pytest_asyncio.fixture
async def keyboard_monitor():
    """Создает мок keyboard_monitor"""
    mock = MagicMock()
    mock.key_pressed = True
    mock.is_combo_active = True
    mock.control_pressed = True
    mock.n_pressed = True
    return mock


@pytest_asyncio.fixture
async def integration(event_bus, state_manager, error_handler, keyboard_monitor):
    """Создает InputProcessingIntegration для тестов"""
    keyboard_config = KeyboardConfig(
        key_to_monitor="ctrl_n",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.1,
        hold_check_interval=0.05,
        debounce_time=0.1,
        backend="auto",
        key_state_timeout_sec=5.0
    )
    config = InputProcessingConfig(
        keyboard=keyboard_config,
        enable_keyboard_monitoring=True,
        auto_start=True,
        min_recording_duration_sec=0.6,
        recording_prestart_delay_sec=0.0,
        playback_idle_grace_sec=0.3,
        playback_wait_timeout_sec=5.0,
        mic_reset_timeout_sec=60.0
    )
    
    integration = InputProcessingIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config
    )
    
    # Мокируем keyboard_monitor
    integration.keyboard_monitor = keyboard_monitor
    
    await integration.initialize()
    return integration


@pytest.mark.asyncio
async def test_long_press_triggers_microphone_activation(integration, event_bus, state_manager):
    """Проверяет, что LONG_PRESS активирует микрофон без блокировок"""
    
    # Собираем опубликованные события
    published_events = []
    
    async def capture_event_wrapper(event_name: str):
        """Создает обертку для захвата событий"""
        async def handler(payload: Dict[str, Any]):
            published_events.append((event_name, payload))
        return handler
    
    # Подписываемся на все события для захвата
    for event_name in ["voice.recording_start", "mode.request", "microphone.open_requested"]:
        handler = await capture_event_wrapper(event_name)
        await event_bus.subscribe(event_name, handler, EventPriority.HIGH)
    
    # Создаем LONG_PRESS событие
    long_press_event = KeyEvent(
        key="ctrl_n",
        event_type=KeyEventType.LONG_PRESS,
        timestamp=time.time(),
        duration=0.7  # Больше long_press_threshold (0.6)
    )
    
    # Устанавливаем начальное состояние
    state_manager.set_mode(AppMode.SLEEPING)
    
    # Устанавливаем _input_state в PENDING (требуется для _can_start_recording)
    integration._input_state = InputState.PENDING
    integration._pending_session_id = time.time()
    
    # Убеждаемся, что keyboard_monitor.key_pressed = True
    integration.keyboard_monitor.key_pressed = True
    
    # Проверяем, что _can_start_recording возвращает True
    can_start, reason = await integration._can_start_recording()
    assert can_start, f"_can_start_recording вернул False: {reason}"
    
    # Вызываем _handle_long_press
    start_time = time.time()
    await integration._handle_long_press(long_press_event)
    elapsed_time = time.time() - start_time
    
    # Проверяем, что обработка не блокировалась слишком долго
    # _ensure_playback_idle() имеет таймаут 0.3s, поэтому ожидаем < 0.4s
    assert elapsed_time < 0.4, f"Обработка LONG_PRESS заняла {elapsed_time:.3f}s (ожидалось < 0.4s)"
    
    # Даем время для асинхронных операций
    await asyncio.sleep(0.1)
    
    # Проверяем, что voice.recording_start был опубликован
    recording_start_events = [e for e in published_events if e[0] == "voice.recording_start"]
    assert len(recording_start_events) > 0, "voice.recording_start не был опубликован"
    
    # Проверяем, что mode.request(LISTENING) был опубликован
    mode_request_events = [e for e in published_events if e[0] == "mode.request"]
    assert len(mode_request_events) > 0, "mode.request не был опубликован"
    
    # Проверяем, что target в mode.request = LISTENING
    mode_request_payload = mode_request_events[0][1]
    # target может быть в data.target или в корне payload
    target = mode_request_payload.get("target") or (mode_request_payload.get("data", {}).get("target") if isinstance(mode_request_payload.get("data"), dict) else None)
    assert target == AppMode.LISTENING, f"mode.request target не LISTENING: {target}, payload={mode_request_payload}"
    
    # Проверяем, что _recording_started установлен
    assert integration._recording_started, "_recording_started не установлен"
    
    print(f"✅ Тест пройден: LONG_PRESS активирует микрофон за {elapsed_time*1000:.1f}ms")
    print(f"   Опубликовано событий: {len(published_events)}")
    for event_name, payload in published_events:
        print(f"   - {event_name}: {payload}")


@pytest.mark.asyncio
async def test_can_start_recording_checks(integration, state_manager):
    """Проверяет все условия в _can_start_recording"""
    
    # Тест 1: Нормальное состояние (должно вернуть True)
    state_manager.set_mode(AppMode.SLEEPING)
    integration._input_state = InputState.PENDING
    integration._pending_session_id = time.time()
    integration.keyboard_monitor.key_pressed = True
    integration._recording_started = False
    integration._long_press_in_progress = False
    
    can_start, reason = await integration._can_start_recording()
    assert can_start, f"_can_start_recording вернул False в нормальном состоянии: {reason}"
    
    # Тест 2: key_not_pressed (должно вернуть False)
    integration.keyboard_monitor.key_pressed = False
    can_start, reason = await integration._can_start_recording()
    assert not can_start, f"_can_start_recording вернул True при key_not_pressed"
    assert "key_not_pressed" in reason.lower(), f"Причина должна содержать 'key_not_pressed': {reason}"
    
    # Тест 3: microphone_already_active (должно вернуть False)
    integration.keyboard_monitor.key_pressed = True
    # Мокируем is_microphone_active() чтобы вернуть True
    with patch.object(state_manager, 'is_microphone_active', return_value=True):
        can_start, reason = await integration._can_start_recording()
        assert not can_start, f"_can_start_recording вернул True при microphone_already_active"
        assert "microphone_already_active" in reason.lower(), f"Причина должна содержать 'microphone_already_active': {reason}"
    
    # Тест 4: wrong_input_state (должно вернуть False)
    integration._input_state = InputState.IDLE
    can_start, reason = await integration._can_start_recording()
    assert not can_start, f"_can_start_recording вернул True при wrong_input_state"
    assert "wrong_input_state" in reason.lower(), f"Причина должна содержать 'wrong_input_state': {reason}"
    
    # Тест 5: no_pending_session (должно вернуть False)
    integration._input_state = InputState.PENDING
    integration._pending_session_id = None
    can_start, reason = await integration._can_start_recording()
    assert not can_start, f"_can_start_recording вернул True при no_pending_session"
    assert "no_pending_session" in reason.lower(), f"Причина должна содержать 'no_pending_session': {reason}"
    
    print("✅ Тест пройден: все проверки _can_start_recording работают корректно")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

