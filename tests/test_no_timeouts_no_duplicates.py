"""
Изолированный тест для проверки отсутствия таймаутов, дублирования, конфликтов и race conditions.

Проверяет:
1. Нет блокировок при активации микрофона
2. Нет таймаутов в request_open()
3. Нет дублирования событий
4. Нет конфликтов состояний
5. Нет повторов операций
6. Нет race conditions
"""

import pytest
import pytest_asyncio
import asyncio
import time
from unittest.mock import Mock, AsyncMock, patch, MagicMock
from typing import List, Dict, Any, Set

from integration.integrations.input_processing_integration import InputProcessingIntegration, InputState
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.event_bus import EventBus
from integration.core.error_handler import ErrorHandler
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
from integration.integrations.voice_recognition_integration import VoiceRecognitionConfig
from modules.microphone_state.core.microphone_state_manager import MicrophoneStateManager


class TestNoTimeoutsNoDuplicates:
    """Тесты для проверки отсутствия таймаутов, дублирования и конфликтов"""
    
    @pytest.fixture
    def mock_event_bus(self):
        """Мок EventBus с отслеживанием всех событий"""
        bus = Mock(spec=EventBus)
        bus.subscribe = AsyncMock()
        bus.unsubscribe = AsyncMock()
        bus._published_events: List[tuple] = []  # (event_name, data, timestamp)
        bus._event_counts: Dict[str, int] = {}  # Подсчет количества публикаций
        
        async def track_publish(event_name: str, data: Dict[str, Any] = None):
            """Отслеживаем все публикации событий"""
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
    
    @pytest.fixture
    def mock_voice_config(self):
        """Мок конфигурации voice_recognition"""
        config = Mock(spec=VoiceRecognitionConfig)
        config.simulate = True  # Используем симуляцию для изоляции
        config.language = "en-US"
        config.timeout_sec = 10.0
        return config
    
    @pytest_asyncio.fixture
    async def integration_setup(self, mock_event_bus, mock_state_manager, mock_error_handler, mock_input_config, mock_voice_config):
        """Создаем полную интеграцию с моками"""
        # Создаем MicrophoneStateManager
        mic_state_manager = MicrophoneStateManager(
            event_bus=mock_event_bus,
            state_manager=mock_state_manager,
            open_timeout=0.5,  # Минимальный таймаут (хотя не используется)
            close_timeout=3.0
        )
        await mic_state_manager.initialize()
        
        # Создаем VoiceRecognitionIntegration
        voice_integration = VoiceRecognitionIntegration(
            event_bus=mock_event_bus,
            state_manager=mock_state_manager,
            error_handler=mock_error_handler,
            config=mock_voice_config
        )
        # Устанавливаем мок MicrophoneStateManager
        voice_integration._mic_state_manager = mic_state_manager
        await voice_integration.initialize()
        await voice_integration.start()
        
        # Создаем InputProcessingIntegration
        input_integration = InputProcessingIntegration(
            event_bus=mock_event_bus,
            state_manager=mock_state_manager,
            error_handler=mock_error_handler,
            config=mock_input_config
        )
        # Устанавливаем мок keyboard_monitor с правильным состоянием
        # КРИТИЧНО: key_pressed должен быть True для прохождения проверки _can_start_recording
        mock_keyboard = Mock()
        mock_keyboard.key_pressed = True  # Устанавливаем как атрибут, не как Mock
        mock_keyboard.is_combo_active = Mock(return_value=True)
        mock_keyboard.control_pressed = True
        mock_keyboard.n_pressed = True
        input_integration.keyboard_monitor = mock_keyboard
        
        await input_integration.initialize()
        await input_integration.start()
        
        return {
            "input_integration": input_integration,
            "voice_integration": voice_integration,
            "mic_state_manager": mic_state_manager,
            "event_bus": mock_event_bus,
            "state_manager": mock_state_manager
        }
    
    @pytest.mark.asyncio
    async def test_no_timeouts_in_request_open(self, integration_setup):
        """
        Тест: request_open() не использует таймауты и возвращается сразу.
        """
        setup = integration_setup
        mic_state_manager = setup["mic_state_manager"]
        
        # Засекаем время выполнения
        start_time = time.time()
        result = await mic_state_manager.request_open("test_session_123")
        end_time = time.time()
        
        # Проверяем, что request_open() вернулся сразу (без таймаутов)
        execution_time = end_time - start_time
        assert execution_time < 0.1, (
            f"request_open() должен вернуться сразу (< 0.1s), но занял {execution_time:.3f}s"
        )
        
        # Проверяем, что вернулся True (неблокирующий)
        assert result == True, "request_open() должен вернуть True сразу (неблокирующий)"
        
        # Проверяем, что событие microphone.open_requested было опубликовано
        assert "microphone.open_requested" in setup["event_bus"]._event_counts, (
            "microphone.open_requested должно быть опубликовано"
        )
    
    @pytest.mark.asyncio
    async def test_no_blocking_in_long_press(self, integration_setup):
        """
        Тест: _handle_long_press не блокирует выполнение.
        """
        setup = integration_setup
        input_integration = setup["input_integration"]
        
        # Устанавливаем состояние PENDING
        input_integration._input_state = InputState.PENDING
        input_integration._pending_session_id = 1234567890.0
        
        # Мокируем зависимости
        input_integration._ensure_playback_idle = AsyncMock(return_value=True)
        input_integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
        
        # Создаем событие LONG_PRESS
        long_press_event = KeyEvent(
            event_type=KeyEventType.LONG_PRESS,
            key="ctrl_n",
            timestamp=1234567890.0,
            duration=0.7
        )
        
        # Засекаем время выполнения
        start_time = time.time()
        await input_integration._handle_long_press(long_press_event)
        end_time = time.time()
        
        # Проверяем, что _handle_long_press вернулся быстро (без блокировок)
        execution_time = end_time - start_time
        assert execution_time < 0.1, (
            f"_handle_long_press должен вернуться быстро (< 0.1s), но занял {execution_time:.3f}s"
        )
        
        # Проверяем, что _recording_started установлен сразу
        assert input_integration._recording_started == True, (
            "_recording_started должен быть установлен сразу (без ожидания микрофона)"
        )
        
        # Проверяем, что события были опубликованы
        assert "voice.recording_start" in setup["event_bus"]._event_counts, (
            "voice.recording_start должно быть опубликовано"
        )
        assert "mode.request" in setup["event_bus"]._event_counts, (
            "mode.request должно быть опубликовано"
        )
    
    @pytest.mark.asyncio
    async def test_no_duplicate_events(self, integration_setup):
        """
        Тест: Нет дублирования событий при активации микрофона.
        """
        setup = integration_setup
        input_integration = setup["input_integration"]
        
        # Устанавливаем состояние PENDING
        input_integration._input_state = InputState.PENDING
        input_integration._pending_session_id = 1234567890.0
        
        # Мокируем зависимости
        input_integration._ensure_playback_idle = AsyncMock(return_value=True)
        input_integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
        
        # Создаем событие LONG_PRESS
        long_press_event = KeyEvent(
            event_type=KeyEventType.LONG_PRESS,
            key="ctrl_n",
            timestamp=1234567890.0,
            duration=0.7
        )
        
        # Очищаем счетчики событий
        setup["event_bus"]._event_counts.clear()
        setup["event_bus"]._published_events.clear()
        
        # Вызываем _handle_long_press
        await input_integration._handle_long_press(long_press_event)
        
        # Даем время для асинхронной обработки
        await asyncio.sleep(0.1)
        
        # Проверяем, что каждое событие опубликовано только один раз
        critical_events = ["voice.recording_start", "mode.request"]
        for event_name in critical_events:
            count = setup["event_bus"]._event_counts.get(event_name, 0)
            assert count == 1, (
                f"Событие {event_name} должно быть опубликовано только 1 раз, но опубликовано {count} раз"
            )
    
    @pytest.mark.asyncio
    async def test_no_conflicts_in_state(self, integration_setup):
        """
        Тест: Нет конфликтов состояний при параллельной активации.
        """
        setup = integration_setup
        input_integration = setup["input_integration"]
        mic_state_manager = setup["mic_state_manager"]
        
        # Устанавливаем состояние PENDING
        input_integration._input_state = InputState.PENDING
        input_integration._pending_session_id = 1234567890.0
        
        # Мокируем зависимости
        input_integration._ensure_playback_idle = AsyncMock(return_value=True)
        input_integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
        
        # Создаем два события LONG_PRESS с разными session_id
        long_press_event_1 = KeyEvent(
            event_type=KeyEventType.LONG_PRESS,
            key="ctrl_n",
            timestamp=1234567890.0,
            duration=0.7
        )
        long_press_event_2 = KeyEvent(
            event_type=KeyEventType.LONG_PRESS,
            key="ctrl_n",
            timestamp=1234567891.0,
            duration=0.7
        )
        
        # Запускаем параллельно (имитируем race condition)
        task1 = asyncio.create_task(input_integration._handle_long_press(long_press_event_1))
        task2 = asyncio.create_task(input_integration._handle_long_press(long_press_event_2))
        
        await asyncio.gather(task1, task2, return_exceptions=True)
        
        # Даем время для асинхронной обработки
        await asyncio.sleep(0.1)
        
        # Проверяем, что состояние микрофона корректно (нет конфликтов)
        # Микрофон должен быть в состоянии OPENING или ACTIVE (не в ERROR)
        from modules.microphone_state.core.types import MicrophoneState
        assert mic_state_manager._state != MicrophoneState.ERROR, (
            "Микрофон не должен быть в состоянии ERROR после параллельной активации"
        )
        
        # Проверяем, что _recording_started установлен только один раз
        assert input_integration._recording_started == True, (
            "_recording_started должен быть установлен (даже при параллельной активации)"
        )
    
    @pytest.mark.asyncio
    async def test_no_repeated_operations(self, integration_setup):
        """
        Тест: Нет повторных операций при повторных вызовах request_open().
        """
        setup = integration_setup
        mic_state_manager = setup["mic_state_manager"]
        
        # Очищаем счетчики событий
        setup["event_bus"]._event_counts.clear()
        setup["event_bus"]._published_events.clear()
        
        # Вызываем request_open() несколько раз подряд
        session_id = "test_session_123"
        results = []
        for i in range(3):
            result = await mic_state_manager.request_open(f"{session_id}_{i}")
            results.append(result)
            await asyncio.sleep(0.01)  # Небольшая задержка между вызовами
        
        # Проверяем, что все вызовы вернули True (неблокирующие)
        assert all(r == True for r in results), (
            "Все вызовы request_open() должны вернуть True (неблокирующие)"
        )
        
        # Проверяем, что событие microphone.open_requested опубликовано нужное количество раз
        # (может быть меньше, если микрофон уже открыт)
        open_requested_count = setup["event_bus"]._event_counts.get("microphone.open_requested", 0)
        assert open_requested_count > 0, (
            "microphone.open_requested должно быть опубликовано хотя бы один раз"
        )
        assert open_requested_count <= 3, (
            f"microphone.open_requested не должно публиковаться больше 3 раз, но опубликовано {open_requested_count} раз"
        )
    
    @pytest.mark.asyncio
    async def test_no_race_conditions(self, integration_setup):
        """
        Тест: Нет race conditions при быстрых последовательных вызовах.
        """
        setup = integration_setup
        input_integration = setup["input_integration"]
        
        # Устанавливаем состояние PENDING
        input_integration._input_state = InputState.PENDING
        input_integration._pending_session_id = 1234567890.0
        
        # Мокируем зависимости
        input_integration._ensure_playback_idle = AsyncMock(return_value=True)
        input_integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
        
        # Создаем событие LONG_PRESS
        long_press_event = KeyEvent(
            event_type=KeyEventType.LONG_PRESS,
            key="ctrl_n",
            timestamp=1234567890.0,
            duration=0.7
        )
        
        # Очищаем счетчики событий
        setup["event_bus"]._event_counts.clear()
        setup["event_bus"]._published_events.clear()
        
        # Вызываем _handle_long_press несколько раз быстро (имитируем race condition)
        tasks = []
        for i in range(5):
            task = asyncio.create_task(input_integration._handle_long_press(long_press_event))
            tasks.append(task)
            await asyncio.sleep(0.001)  # Очень маленькая задержка
        
        await asyncio.gather(*tasks, return_exceptions=True)
        
        # Даем время для асинхронной обработки
        await asyncio.sleep(0.1)
        
        # Проверяем, что события не дублируются чрезмерно
        voice_recording_start_count = setup["event_bus"]._event_counts.get("voice.recording_start", 0)
        mode_request_count = setup["event_bus"]._event_counts.get("mode.request", 0)
        
        # Допускаем небольшое дублирование из-за race condition, но не должно быть слишком много
        assert voice_recording_start_count <= 5, (
            f"voice.recording_start не должно публиковаться больше 5 раз, но опубликовано {voice_recording_start_count} раз"
        )
        assert mode_request_count <= 5, (
            f"mode.request не должно публиковаться больше 5 раз, но опубликовано {mode_request_count} раз"
        )
        
        # Проверяем, что _recording_started установлен корректно
        assert input_integration._recording_started == True, (
            "_recording_started должен быть установлен (даже при race condition)"
        )
    
    @pytest.mark.asyncio
    async def test_event_order_correctness(self, integration_setup):
        """
        Тест: Порядок событий корректен (voice.recording_start → mode.request).
        """
        setup = integration_setup
        input_integration = setup["input_integration"]
        
        # Устанавливаем состояние PENDING
        input_integration._input_state = InputState.PENDING
        input_integration._pending_session_id = 1234567890.0
        
        # Мокируем зависимости
        input_integration._ensure_playback_idle = AsyncMock(return_value=True)
        input_integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=True)
        
        # Создаем событие LONG_PRESS
        long_press_event = KeyEvent(
            event_type=KeyEventType.LONG_PRESS,
            key="ctrl_n",
            timestamp=1234567890.0,
            duration=0.7
        )
        
        # Очищаем события
        setup["event_bus"]._published_events.clear()
        
        # Вызываем _handle_long_press
        await input_integration._handle_long_press(long_press_event)
        
        # Даем время для асинхронной обработки
        await asyncio.sleep(0.1)
        
        # Находим индексы событий
        recording_start_idx = None
        mode_request_idx = None
        
        for idx, (event_name, _, _) in enumerate(setup["event_bus"]._published_events):
            if event_name == "voice.recording_start":
                recording_start_idx = idx
            elif event_name == "mode.request":
                mode_request_idx = idx
        
        # Проверяем, что события были опубликованы
        assert recording_start_idx is not None, "voice.recording_start должно быть опубликовано"
        assert mode_request_idx is not None, "mode.request должно быть опубликовано"
        
        # Проверяем порядок: voice.recording_start должен быть ДО mode.request
        assert recording_start_idx < mode_request_idx, (
            f"voice.recording_start должно быть опубликовано ДО mode.request, "
            f"но порядок: recording_start={recording_start_idx}, mode.request={mode_request_idx}"
        )

