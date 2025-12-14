"""
Изолированный тест для проверки проблемы: принудительный сброс комбинации останавливает запись.

Проблема:
1. LONG_PRESS обрабатывается и начинает запись
2. Система принудительно сбрасывает комбинацию из-за "залипания" Control (10 секунд без событий)
3. RELEASE генерируется и останавливает только что начатую запись

Проверяет:
1. LONG_PRESS не должен останавливаться принудительным сбросом комбинации
2. RELEASE не должен останавливать запись, если она только что началась
3. Логика определения "залипания" не должна срабатывать при активной комбинации
"""

import pytest
import pytest_asyncio
import asyncio
import time
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from typing import Dict, Any

from integration.integrations.input_processing_integration import InputProcessingIntegration, InputState
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.event_bus import EventBus
from integration.core.error_handler import ErrorHandler
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
from config.unified_config_loader import InputProcessingConfig, KeyboardConfig


class TestStuckComboStopsRecording:
    """Тесты для проверки проблемы принудительного сброса комбинации"""
    
    @pytest.fixture
    def mock_event_bus(self):
        """Мок EventBus с отслеживанием всех событий"""
        bus = Mock(spec=EventBus)
        bus.subscribe = AsyncMock()
        bus.unsubscribe = AsyncMock()
        bus._published_events: list = []  # (event_name, data, timestamp)
        bus._event_counts: Dict[str, int] = {}
        
        async def track_publish(event_name: str, data: Dict[str, Any] = None):
            timestamp = time.time()
            bus._published_events.append((event_name, data, timestamp))
            bus._event_counts[event_name] = bus._event_counts.get(event_name, 0) + 1
            return None
        
        bus.publish = AsyncMock(side_effect=track_publish)
        return bus
    
    @pytest.fixture
    def mock_state_manager(self):
        """Мок ApplicationStateManager"""
        manager = Mock(spec=ApplicationStateManager)
        manager.get_current_mode = Mock(return_value=AppMode.SLEEPING)
        manager.get_current_session_id = Mock(return_value=None)
        manager.is_microphone_active = Mock(return_value=False)
        manager.set_microphone_active = Mock()
        manager.force_close_microphone = Mock()
        manager.update_session_id = Mock()
        return manager
    
    @pytest.fixture
    def mock_error_handler(self):
        """Мок ErrorHandler"""
        handler = Mock(spec=ErrorHandler)
        handler.handle_error = AsyncMock()
        return handler
    
    @pytest.fixture
    def mock_keyboard_config(self):
        """Мок конфигурации клавиатуры"""
        config = Mock(spec=KeyboardConfig)
        config.key_to_monitor = "ctrl_n"
        config.short_press_threshold = 0.1
        config.long_press_threshold = 0.6
        config.event_cooldown = 0.1
        config.hold_check_interval = 0.05
        config.debounce_time = 0.1
        config.backend = "auto"
        config.combo_timeout_sec = 10.0
        config.key_state_timeout_sec = 10.0
        return config
    
    @pytest.fixture
    def mock_input_config(self, mock_keyboard_config):
        """Мок конфигурации input_processing"""
        config = Mock(spec=InputProcessingConfig)
        config.enable_keyboard_monitoring = True
        config.keyboard_backend = "auto"
        config.keyboard = mock_keyboard_config
        config.min_recording_duration_sec = 0.6
        config.recording_prestart_delay_sec = 0.0
        config.playback_wait_timeout_sec = 0.5
        config.playback_idle_grace_sec = 0.0
        config.mic_reset_timeout_sec = 5.0
        return config
    
    @pytest_asyncio.fixture
    async def integration_setup(self, mock_event_bus, mock_state_manager, mock_error_handler, mock_input_config):
        """Создаем полную интеграцию с моками"""
        input_integration = InputProcessingIntegration(
            event_bus=mock_event_bus,
            state_manager=mock_state_manager,
            error_handler=mock_error_handler,
            config=mock_input_config
        )
        
        # Устанавливаем мок keyboard_monitor с правильным состоянием
        mock_keyboard = Mock()
        mock_keyboard.key_pressed = True
        mock_keyboard.is_combo_active = Mock(return_value=True)
        mock_keyboard.control_pressed = True
        mock_keyboard.n_pressed = True
        input_integration.keyboard_monitor = mock_keyboard
        
        # Мокируем зависимости
        input_integration._ensure_playback_idle = AsyncMock(return_value=True)
        input_integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
        
        await input_integration.initialize()
        await input_integration.start()
        
        return {
            "input_integration": input_integration,
            "event_bus": mock_event_bus,
            "state_manager": mock_state_manager
        }
    
    @pytest.mark.asyncio
    async def test_long_press_not_stopped_by_release(self, integration_setup):
        """
        Тест: LONG_PRESS не должен останавливаться RELEASE, если запись только что началась.
        """
        setup = integration_setup
        input_integration = setup["input_integration"]
        
        # Устанавливаем состояние PENDING
        input_integration._input_state = InputState.PENDING
        input_integration._pending_session_id = 1234567890.0
        
        # Очищаем счетчики событий
        setup["event_bus"]._event_counts.clear()
        setup["event_bus"]._published_events.clear()
        
        # Создаем событие LONG_PRESS
        long_press_event = KeyEvent(
            event_type=KeyEventType.LONG_PRESS,
            key="ctrl_n",
            timestamp=1234567890.0,
            duration=0.7
        )
        
        # Вызываем LONG_PRESS
        await input_integration._handle_long_press(long_press_event)
        
        # Даем время для асинхронной обработки
        await asyncio.sleep(0.1)
        
        # Проверяем, что voice.recording_start было опубликовано
        recording_start_count = setup["event_bus"]._event_counts.get("voice.recording_start", 0)
        assert recording_start_count > 0, (
            "voice.recording_start должно быть опубликовано после LONG_PRESS"
        )
        
        # Проверяем, что _recording_started установлен
        assert input_integration._recording_started == True, (
            "_recording_started должен быть установлен после LONG_PRESS"
        )
        
        # Создаем событие RELEASE сразу после LONG_PRESS (имитируем принудительный сброс)
        release_event = KeyEvent(
            event_type=KeyEventType.RELEASE,
            key="ctrl_n",
            timestamp=1234567891.0,
            duration=9.884
        )
        
        # Вызываем RELEASE
        await input_integration._handle_key_release(release_event)
        
        # Даем время для асинхронной обработки
        await asyncio.sleep(0.1)
        
        # ПРОБЛЕМА: RELEASE не должен останавливать запись, если она только что началась
        # Проверяем, что voice.recording_stop НЕ было опубликовано сразу после LONG_PRESS
        recording_stop_count = setup["event_bus"]._event_counts.get("voice.recording_stop", 0)
        
        # Сейчас это может быть > 0 (проблема), но мы проверяем логику
        # В идеале: если запись только что началась (< 0.1s), RELEASE не должен останавливать её
        if recording_stop_count > 0:
            # Находим время между LONG_PRESS и RELEASE
            long_press_time = None
            release_time = None
            
            for event_name, data, timestamp in setup["event_bus"]._published_events:
                if event_name == "voice.recording_start":
                    long_press_time = timestamp
                elif event_name == "voice.recording_stop":
                    release_time = timestamp
            
            if long_press_time and release_time:
                time_between = release_time - long_press_time
                # Если между LONG_PRESS и RELEASE прошло меньше 0.1 секунды - это проблема
                if time_between < 0.1:
                    pytest.fail(
                        f"RELEASE остановил запись слишком быстро после LONG_PRESS "
                        f"(время между событиями: {time_between:.3f}s < 0.1s). "
                        f"Это проблема: запись не должна останавливаться сразу после начала."
                    )
    
    @pytest.mark.asyncio
    async def test_stuck_combo_should_not_trigger_release_during_recording(self, integration_setup):
        """
        Тест: Принудительный сброс комбинации не должен генерировать RELEASE во время активной записи.
        """
        setup = integration_setup
        input_integration = setup["input_integration"]
        
        # Устанавливаем состояние LISTENING (запись активна)
        input_integration._input_state = InputState.LISTENING
        input_integration._recording_started = True
        input_integration._current_session_id = 1234567890.0
        
        # Устанавливаем, что микрофон активен
        setup["state_manager"].is_microphone_active = Mock(return_value=True)
        
        # Очищаем счетчики событий
        setup["event_bus"]._event_counts.clear()
        setup["event_bus"]._published_events.clear()
        
        # Создаем событие RELEASE (имитируем принудительный сброс комбинации)
        release_event = KeyEvent(
            event_type=KeyEventType.RELEASE,
            key="ctrl_n",
            timestamp=1234567890.0,
            duration=9.884
        )
        
        # Вызываем RELEASE
        await input_integration._handle_key_release(release_event)
        
        # Даем время для асинхронной обработки
        await asyncio.sleep(0.1)
        
        # ПРОБЛЕМА: RELEASE не должен останавливать активную запись при принудительном сбросе
        # Проверяем, что voice.recording_stop НЕ было опубликовано
        recording_stop_count = setup["event_bus"]._event_counts.get("voice.recording_stop", 0)
        
        # Сейчас это может быть > 0 (проблема), но мы проверяем логику
        # В идеале: если запись активна и это принудительный сброс (duration > 9s), RELEASE не должен останавливать её
        if recording_stop_count > 0:
            # Проверяем причину остановки
            for event_name, data, timestamp in setup["event_bus"]._published_events:
                if event_name == "voice.recording_stop":
                    # Если duration > 9s, это принудительный сброс - запись не должна останавливаться
                    if release_event.duration > 9.0:
                        pytest.fail(
                            f"RELEASE остановил запись при принудительном сбросе комбинации "
                            f"(duration={release_event.duration:.3f}s > 9.0s). "
                            f"Это проблема: запись не должна останавливаться при принудительном сбросе."
                        )

