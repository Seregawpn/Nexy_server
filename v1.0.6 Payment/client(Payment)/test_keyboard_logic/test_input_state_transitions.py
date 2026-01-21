"""
Изолированные тесты для проверки логики обработки Control+N

Тестирует:
- Переходы состояния через InputState enum
- Атомарность операций с asyncio.Lock
- Синхронизацию через asyncio.Event
- Защиту от race conditions
"""

import asyncio
import pytest
from unittest.mock import Mock, AsyncMock, MagicMock
from typing import Optional
import time

# Импортируем классы для тестирования
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from integration.integrations.input_processing_integration import (
    InputProcessingIntegration,
    InputState
)
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.event_bus import EventBus
from integration.core.error_handler import ErrorHandler
from config.unified_config_loader import InputProcessingConfig


class TestInputStateTransitions:
    """Тесты переходов состояния через InputState enum"""
    
    @pytest.fixture
    def integration(self):
        """Создает экземпляр InputProcessingIntegration с моками"""
        event_bus = Mock(spec=EventBus)
        event_bus.publish = AsyncMock()
        event_bus.subscribe = AsyncMock()
        
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_current_session_id = Mock(return_value=None)
        state_manager.get_current_mode = Mock(return_value=AppMode.SLEEPING)
        state_manager.update_session_id = Mock()
        
        error_handler = Mock(spec=ErrorHandler)
        error_handler.handle_error = AsyncMock()
        
        config = Mock(spec=InputProcessingConfig)
        config.min_recording_duration_sec = 0.1
        config.playback_wait_timeout_sec = 0.5
        config.playback_idle_grace_sec = 0.0
        config.recording_prestart_delay_sec = 0.0
        config.mic_reset_timeout_sec = 0.0
        
        integration = InputProcessingIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config
        )
        
        # Мокируем keyboard_monitor
        integration.keyboard_monitor = Mock()
        integration.keyboard_monitor.key_pressed = True
        integration.keyboard_monitor.register_callback = Mock()
        
        return integration
    
    @pytest.mark.asyncio
    async def test_initial_state_is_idle(self, integration):
        """Проверяем, что начальное состояние - IDLE"""
        assert integration._input_state == InputState.IDLE
    
    @pytest.mark.asyncio
    async def test_press_transitions_to_pending(self, integration):
        """Проверяем переход PRESS → PENDING"""
        event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.PRESS,
            timestamp=time.time()
        )
        
        await integration._handle_press(event)
        
        assert integration._input_state == InputState.PENDING
        assert integration._pending_session_id is not None
    
    @pytest.mark.asyncio
    async def test_long_press_transitions_to_listening(self, integration):
        """Проверяем переход LONG_PRESS → LISTENING"""
        # Сначала устанавливаем PENDING
        integration._input_state = InputState.PENDING
        integration._pending_session_id = time.time()
        integration._mic_active = False
        integration._recording_started = False
        
        event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.LONG_PRESS,
            timestamp=time.time(),
            duration=0.7
        )
        
        # Мокируем методы, которые вызываются внутри
        integration._ensure_playback_idle = AsyncMock()
        integration._wait_for_mic_closed = AsyncMock()
        integration._reset_session = Mock()
        integration._set_session_id = Mock()
        
        await integration._handle_long_press(event)
        
        # Проверяем, что состояние изменилось на LISTENING
        assert integration._input_state == InputState.LISTENING
        assert integration._recording_started is True
    
    @pytest.mark.asyncio
    async def test_release_after_recording_transitions_to_processing(self, integration):
        """Проверяем переход RELEASE (с записью) → PROCESSING"""
        # Устанавливаем LISTENING
        integration._input_state = InputState.LISTENING
        integration._recording_started = True
        integration._mic_active = True
        
        event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.RELEASE,
            timestamp=time.time(),
            duration=1.0
        )
        
        # Мокируем методы
        integration._should_stop_recording = Mock(return_value=True)
        integration._wait_for_mic_closed = AsyncMock()
        integration._get_active_session_id = Mock(return_value=123.456)
        
        await integration._handle_key_release(event)
        
        # Проверяем, что состояние изменилось на PROCESSING
        assert integration._input_state == InputState.PROCESSING
    
    @pytest.mark.asyncio
    async def test_release_without_recording_transitions_to_idle(self, integration):
        """Проверяем переход RELEASE (без записи) → IDLE"""
        # Устанавливаем PENDING
        integration._input_state = InputState.PENDING
        integration._recording_started = False
        integration._mic_active = False
        
        event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.RELEASE,
            timestamp=time.time(),
            duration=0.3
        )
        
        # Мокируем методы
        integration._should_stop_recording = Mock(return_value=False)
        
        await integration._handle_key_release(event)
        
        # Проверяем, что состояние вернулось в IDLE
        assert integration._input_state == InputState.IDLE


class TestAtomicOperations:
    """Тесты атомарности операций с asyncio.Lock"""
    
    @pytest.fixture
    def integration(self):
        """Создает экземпляр InputProcessingIntegration с моками"""
        event_bus = Mock(spec=EventBus)
        event_bus.publish = AsyncMock()
        event_bus.subscribe = AsyncMock()
        
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_current_session_id = Mock(return_value=None)
        state_manager.get_current_mode = Mock(return_value=AppMode.SLEEPING)
        state_manager.update_session_id = Mock()
        
        error_handler = Mock(spec=ErrorHandler)
        error_handler.handle_error = AsyncMock()
        
        config = Mock(spec=InputProcessingConfig)
        config.min_recording_duration_sec = 0.1
        config.playback_wait_timeout_sec = 0.5
        config.playback_idle_grace_sec = 0.0
        config.recording_prestart_delay_sec = 0.0
        config.mic_reset_timeout_sec = 0.0
        
        integration = InputProcessingIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config
        )
        
        return integration
    
    @pytest.mark.asyncio
    async def test_long_press_in_progress_flag_atomic(self, integration):
        """Проверяем, что флаг _long_press_in_progress устанавливается атомарно"""
        integration._input_state = InputState.PENDING
        integration._pending_session_id = time.time()
        integration._mic_active = False
        integration._recording_started = False
        integration.keyboard_monitor = Mock()
        integration.keyboard_monitor.key_pressed = True
        
        event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.LONG_PRESS,
            timestamp=time.time(),
            duration=0.7
        )
        
        # Мокируем методы
        integration._ensure_playback_idle = AsyncMock()
        integration._wait_for_mic_closed = AsyncMock()
        integration._reset_session = Mock()
        integration._set_session_id = Mock()
        
        # Запускаем два LONG_PRESS одновременно (симуляция race condition)
        task1 = asyncio.create_task(integration._handle_long_press(event))
        task2 = asyncio.create_task(integration._handle_long_press(event))
        
        await asyncio.gather(task1, task2, return_exceptions=True)
        
        # Проверяем, что флаг сброшен после завершения
        assert integration._long_press_in_progress is False


class TestEventSynchronization:
    """Тесты синхронизации через asyncio.Event"""
    
    @pytest.fixture
    def integration(self):
        """Создает экземпляр InputProcessingIntegration с моками"""
        event_bus = Mock(spec=EventBus)
        event_bus.publish = AsyncMock()
        event_bus.subscribe = AsyncMock()
        
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_current_session_id = Mock(return_value=None)
        state_manager.get_current_mode = Mock(return_value=AppMode.SLEEPING)
        state_manager.update_session_id = Mock()
        
        error_handler = Mock(spec=ErrorHandler)
        error_handler.handle_error = AsyncMock()
        
        config = Mock(spec=InputProcessingConfig)
        config.min_recording_duration_sec = 0.1
        config.playback_wait_timeout_sec = 0.5
        config.playback_idle_grace_sec = 0.0
        config.recording_prestart_delay_sec = 0.0
        config.mic_reset_timeout_sec = 0.0
        
        integration = InputProcessingIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config
        )
        
        return integration
    
    @pytest.mark.asyncio
    async def test_pending_recording_cancelled_event(self, integration):
        """Проверяем, что asyncio.Event правильно синхронизирует отмену"""
        # Устанавливаем PENDING
        integration._input_state = InputState.PENDING
        integration._pending_session_id = time.time()
        integration._recording_started = False
        
        # Симулируем RELEASE, который устанавливает event
        release_event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.RELEASE,
            timestamp=time.time(),
            duration=0.3
        )
        
        integration._should_stop_recording = Mock(return_value=False)
        
        await integration._handle_key_release(release_event)
        
        # Проверяем, что event установлен
        assert integration._pending_recording_cancelled_event.is_set() is True
    
    @pytest.mark.asyncio
    async def test_long_press_checks_cancelled_event(self, integration):
        """Проверяем, что LONG_PRESS проверяет event и выходит, если он установлен"""
        integration._input_state = InputState.PENDING
        integration._pending_session_id = time.time()
        integration._mic_active = False
        integration._recording_started = False
        integration.keyboard_monitor = Mock()
        integration.keyboard_monitor.key_pressed = True
        
        # Устанавливаем event (симулируем, что RELEASE уже пришел)
        integration._pending_recording_cancelled_event.set()
        
        event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.LONG_PRESS,
            timestamp=time.time(),
            duration=0.7
        )
        
        # Мокируем методы
        integration._ensure_playback_idle = AsyncMock()
        integration._wait_for_mic_closed = AsyncMock()
        
        await integration._handle_long_press(event)
        
        # Проверяем, что запись НЕ началась (event был установлен)
        assert integration._recording_started is False
        assert integration._pending_session_id is None


class TestRaceConditions:
    """Тесты защиты от race conditions"""
    
    @pytest.fixture
    def integration(self):
        """Создает экземпляр InputProcessingIntegration с моками"""
        event_bus = Mock(spec=EventBus)
        event_bus.publish = AsyncMock()
        event_bus.subscribe = AsyncMock()
        
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_current_session_id = Mock(return_value=None)
        state_manager.get_current_mode = Mock(return_value=AppMode.SLEEPING)
        state_manager.update_session_id = Mock()
        
        error_handler = Mock(spec=ErrorHandler)
        error_handler.handle_error = AsyncMock()
        
        config = Mock(spec=InputProcessingConfig)
        config.min_recording_duration_sec = 0.1
        config.playback_wait_timeout_sec = 0.5
        config.playback_idle_grace_sec = 0.0
        config.recording_prestart_delay_sec = 0.0
        config.mic_reset_timeout_sec = 0.0
        
        integration = InputProcessingIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config
        )
        
        return integration
    
    @pytest.mark.asyncio
    async def test_concurrent_long_press_and_release(self, integration):
        """Проверяем защиту от race condition между LONG_PRESS и RELEASE"""
        integration._input_state = InputState.PENDING
        integration._pending_session_id = time.time()
        integration._mic_active = False
        integration._recording_started = False
        integration.keyboard_monitor = Mock()
        integration.keyboard_monitor.key_pressed = True
        
        long_press_event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.LONG_PRESS,
            timestamp=time.time(),
            duration=0.7
        )
        
        release_event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.RELEASE,
            timestamp=time.time(),
            duration=0.3
        )
        
        # Мокируем методы
        integration._ensure_playback_idle = AsyncMock()
        integration._wait_for_mic_closed = AsyncMock()
        integration._reset_session = Mock()
        integration._set_session_id = Mock()
        integration._should_stop_recording = Mock(return_value=False)
        
        # Запускаем LONG_PRESS и RELEASE одновременно
        long_press_task = asyncio.create_task(integration._handle_long_press(long_press_event))
        await asyncio.sleep(0.01)  # Небольшая задержка
        release_task = asyncio.create_task(integration._handle_key_release(release_event))
        
        await asyncio.gather(long_press_task, release_task, return_exceptions=True)
        
        # Проверяем, что система в корректном состоянии
        # Если RELEASE пришел раньше, запись не должна была начаться
        # Если LONG_PRESS успел, то состояние должно быть LISTENING или PROCESSING
        assert integration._input_state in [InputState.IDLE, InputState.LISTENING, InputState.PROCESSING]


class TestDebounceProtection:
    """Тесты защиты от множественных нажатий (debounce)"""
    
    @pytest.fixture
    def integration(self):
        """Создает экземпляр InputProcessingIntegration с моками"""
        event_bus = Mock(spec=EventBus)
        event_bus.publish = AsyncMock()
        event_bus.subscribe = AsyncMock()
        
        state_manager = Mock(spec=ApplicationStateManager)
        state_manager.get_current_session_id = Mock(return_value=None)
        state_manager.get_current_mode = Mock(return_value=AppMode.SLEEPING)
        state_manager.update_session_id = Mock()
        
        error_handler = Mock(spec=ErrorHandler)
        error_handler.handle_error = AsyncMock()
        
        config = Mock(spec=InputProcessingConfig)
        config.min_recording_duration_sec = 0.1
        config.playback_wait_timeout_sec = 0.5
        config.playback_idle_grace_sec = 0.0
        config.recording_prestart_delay_sec = 0.0
        config.mic_reset_timeout_sec = 0.0
        
        integration = InputProcessingIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config
        )
        
        return integration
    
    @pytest.mark.asyncio
    async def test_press_debounce_ignores_rapid_presses(self, integration):
        """Проверяем, что debounce игнорирует быстрые повторные PRESS (< 0.1s)"""
        event1 = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.PRESS,
            timestamp=time.time()
        )
        
        # Первый PRESS должен пройти
        await integration._handle_press(event1)
        assert integration._input_state == InputState.PENDING
        first_pending_id = integration._pending_session_id
        
        # Второй PRESS сразу после первого (< 0.1s) должен быть проигнорирован
        await asyncio.sleep(0.05)  # 50ms - меньше debounce интервала
        event2 = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.PRESS,
            timestamp=time.time()
        )
        await integration._handle_press(event2)
        
        # Проверяем, что состояние не изменилось и pending_session_id остался прежним
        assert integration._input_state == InputState.PENDING
        assert integration._pending_session_id == first_pending_id
    
    @pytest.mark.asyncio
    async def test_press_debounce_allows_slow_presses(self, integration):
        """Проверяем, что debounce разрешает PRESS после достаточной паузы (> 0.1s)"""
        event1 = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.PRESS,
            timestamp=time.time()
        )
        
        # Первый PRESS
        await integration._handle_press(event1)
        assert integration._input_state == InputState.PENDING
        first_pending_id = integration._pending_session_id
        
        # Второй PRESS после достаточной паузы (> 0.1s) должен пройти
        await asyncio.sleep(0.15)  # 150ms - больше debounce интервала
        event2 = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.PRESS,
            timestamp=time.time()
        )
        await integration._handle_press(event2)
        
        # Проверяем, что состояние изменилось и pending_session_id обновился
        assert integration._input_state == InputState.PENDING
        assert integration._pending_session_id != first_pending_id
    
    @pytest.mark.asyncio
    async def test_press_cancels_previous_pending(self, integration):
        """Проверяем, что новый PRESS отменяет предыдущий pending_session_id"""
        event1 = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.PRESS,
            timestamp=time.time()
        )
        
        # Первый PRESS
        await integration._handle_press(event1)
        assert integration._input_state == InputState.PENDING
        first_pending_id = integration._pending_session_id
        
        # Второй PRESS после паузы должен отменить предыдущий
        await asyncio.sleep(0.15)
        event2 = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.PRESS,
            timestamp=time.time()
        )
        await integration._handle_press(event2)
        
        # Проверяем, что pending_session_id изменился
        assert integration._pending_session_id != first_pending_id
        assert integration._pending_session_id is not None


if __name__ == "__main__":
    # Запуск тестов
    pytest.main([__file__, "-v"])

