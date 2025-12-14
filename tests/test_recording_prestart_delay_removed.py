"""
Изолированный тест для проверки, что recording_prestart_delay убран и не влияет на скорость активации.

Проверяет, что при LONG_PRESS нет дополнительной задержки после ожидания закрытия микрофона.
"""

import pytest
import pytest_asyncio
import asyncio
from unittest.mock import Mock, AsyncMock, patch
from typing import List, Dict, Any

from integration.integrations.input_processing_integration import InputProcessingIntegration, InputState
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.event_bus import EventBus
from integration.core.error_handler import ErrorHandler
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
from config.unified_config_loader import InputProcessingConfig, KeyboardConfig


class TestRecordingPrestartDelayRemoved:
    """Тесты для проверки, что recording_prestart_delay убран"""
    
    @pytest.fixture
    def mock_event_bus(self):
        """Мок EventBus с отслеживанием времени событий"""
        bus = Mock(spec=EventBus)
        bus.subscribe = AsyncMock()
        bus._event_order: List[tuple] = []
        bus._event_times: List[float] = []
        
        async def track_publish(event_name: str, data: Dict[str, Any] = None):
            """Отслеживаем порядок и время публикации событий"""
            import time
            bus._event_order.append((event_name, data))
            bus._event_times.append(time.time())
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
        return manager
    
    @pytest.fixture
    def mock_error_handler(self):
        """Мок ErrorHandler"""
        handler = Mock(spec=ErrorHandler)
        handler.handle_error = AsyncMock()
        return handler
    
    @pytest.fixture
    def mock_config(self):
        """Мок конфигурации с recording_prestart_delay = 0.0"""
        config = Mock(spec=InputProcessingConfig)
        config.enable_keyboard_monitoring = True
        config.keyboard_backend = "auto"
        config.keyboard = Mock(spec=KeyboardConfig)
        config.keyboard.long_press_threshold = 0.6
        config.min_recording_duration_sec = 0.6
        config.recording_prestart_delay_sec = 0.0  # ✅ УБРАНО
        config.playback_wait_timeout_sec = 0.5
        config.playback_idle_grace_sec = 0.0
        config.mic_reset_timeout_sec = 5.0
        return config
    
    @pytest_asyncio.fixture
    async def integration(self, mock_event_bus, mock_state_manager, mock_error_handler, mock_config):
        """Создаем интеграцию с моками"""
        integration = InputProcessingIntegration(
            event_bus=mock_event_bus,
            state_manager=mock_state_manager,
            error_handler=mock_error_handler,
            config=mock_config
        )
        # Устанавливаем мок keyboard_monitor
        integration.keyboard_monitor = Mock()
        integration.keyboard_monitor.key_pressed = True
        
        # Инициализируем интеграцию
        await integration.initialize()
        await integration.start()
        
        return integration
    
    @pytest.mark.asyncio
    async def test_no_prestart_delay_after_mic_closed(
        self, integration, mock_event_bus, mock_state_manager
    ):
        """
        Тест: recording_prestart_delay = 0.0, нет дополнительной задержки после ожидания закрытия микрофона.
        """
        # Настраиваем моки
        mock_state_manager.get_current_mode.return_value = AppMode.SLEEPING
        mock_state_manager.get_current_session_id.return_value = None
        mock_state_manager.is_microphone_active.return_value = False
        
        # Отслеживаем время вызова _ensure_playback_idle
        ensure_playback_idle_called = {"time": None}
        original_ensure_playback_idle = integration._ensure_playback_idle
        
        async def track_ensure_playback_idle(*args, **kwargs):
            """Отслеживаем время вызова _ensure_playback_idle"""
            import time
            ensure_playback_idle_called["time"] = time.time()
            return await original_ensure_playback_idle(*args, **kwargs)
        
        integration._ensure_playback_idle = track_ensure_playback_idle
        
        # Мокируем _wait_for_mic_opened
        wait_for_mic_opened_called = {"time": None}
        async def mock_wait_for_mic_opened(timeout: float = 5.0) -> bool:
            """Мок ожидания открытия микрофона"""
            import time
            wait_for_mic_opened_called["time"] = time.time()
            await asyncio.sleep(0.05)  # Минимальная задержка для имитации
            mock_state_manager.is_microphone_active.return_value = True
            return True
        
        integration._wait_for_mic_opened = mock_wait_for_mic_opened
        
        # Мокируем _wait_for_mic_closed_with_timeout
        integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
        
        # Устанавливаем состояние PENDING
        integration._input_state = InputState.PENDING
        integration._pending_session_id = 1234567890.0
        
        # Проверяем, что recording_prestart_delay = 0.0
        assert integration._recording_prestart_delay == 0.0, (
            f"recording_prestart_delay должен быть 0.0, но равен {integration._recording_prestart_delay}"
        )
        
        # Создаем событие LONG_PRESS
        long_press_event = KeyEvent(
            event_type=KeyEventType.LONG_PRESS,
            key="ctrl_n",
            timestamp=1234567890.0,
            duration=0.7
        )
        
        # Запускаем обработку LONG_PRESS
        import time
        start_time = time.time()
        await integration._handle_long_press(long_press_event)
        end_time = time.time()
        
        # Проверяем, что voice.recording_start был опубликован
        recording_start_published = False
        for event_name, data in mock_event_bus._event_order:
            if event_name == "voice.recording_start":
                recording_start_published = True
                break
        
        assert recording_start_published, "voice.recording_start должен быть опубликован"
        
        # Проверяем, что _ensure_playback_idle был вызван
        assert ensure_playback_idle_called["time"] is not None, "_ensure_playback_idle должен быть вызван"
        
        # Проверяем, что _wait_for_mic_opened был вызван
        assert wait_for_mic_opened_called["time"] is not None, "_wait_for_mic_opened должен быть вызван"
        
        # КРИТИЧНО: Проверяем, что между _ensure_playback_idle и voice.recording_start нет большой задержки
        # (recording_prestart_delay = 0.0, поэтому задержка должна быть минимальной)
        if ensure_playback_idle_called["time"] and len(mock_event_bus._event_times) > 0:
            # Находим время публикации voice.recording_start
            recording_start_time = None
            for idx, (event_name, _) in enumerate(mock_event_bus._event_order):
                if event_name == "voice.recording_start":
                    recording_start_time = mock_event_bus._event_times[idx]
                    break
            
            if recording_start_time:
                delay_after_playback_idle = recording_start_time - ensure_playback_idle_called["time"]
                # Задержка должна быть минимальной (только время на выполнение кода, без sleep)
                assert delay_after_playback_idle < 0.1, (
                    f"Задержка после _ensure_playback_idle должна быть < 0.1s (recording_prestart_delay=0.0), "
                    f"но равна {delay_after_playback_idle:.3f}s"
                )
    
    @pytest.mark.asyncio
    async def test_prestart_delay_config_is_zero(
        self, integration
    ):
        """
        Тест: проверяем, что recording_prestart_delay действительно = 0.0 в конфигурации.
        """
        assert integration._recording_prestart_delay == 0.0, (
            f"recording_prestart_delay должен быть 0.0, но равен {integration._recording_prestart_delay}"
        )
        
        # Проверяем, что в _ensure_playback_idle задержка не применяется
        # (так как for_recording=True, но _recording_prestart_delay=0.0)
        import time
        start_time = time.time()
        await integration._ensure_playback_idle(for_recording=True)
        end_time = time.time()
        
        # Задержка должна быть минимальной (только время выполнения, без sleep)
        delay = end_time - start_time
        assert delay < 0.05, (
            f"Задержка в _ensure_playback_idle должна быть < 0.05s (recording_prestart_delay=0.0), "
            f"но равна {delay:.3f}s"
        )

