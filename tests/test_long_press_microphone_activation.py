"""
Изолированные тесты для проверки активации микрофона при LONG_PRESS
"""
import asyncio
import logging
from unittest.mock import AsyncMock, MagicMock, Mock, patch
from typing import Dict, Any

import pytest
import pytest_asyncio

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler
from integration.integrations.input_processing_integration import InputProcessingIntegration, InputState
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType

logger = logging.getLogger(__name__)


class TestLongPressMicrophoneActivation:
    """Тесты для проверки активации микрофона при LONG_PRESS"""

    @pytest.fixture
    def event_bus(self):
        """Создает EventBus для тестов"""
        return EventBus()

    @pytest.fixture
    def state_manager(self, event_bus):
        """Создает ApplicationStateManager для тестов"""
        manager = ApplicationStateManager()
        manager.attach_event_bus(event_bus)
        return manager

    @pytest.fixture
    def error_handler(self):
        """Создает ErrorHandler для тестов"""
        return ErrorHandler()

    @pytest.fixture
    def keyboard_monitor(self):
        """Создает мок keyboard_monitor"""
        monitor = Mock()
        monitor.key_pressed = True  # Клавиша нажата
        return monitor

    @pytest_asyncio.fixture
    async def input_integration(self, event_bus, state_manager, error_handler, keyboard_monitor):
        """Создает InputProcessingIntegration для тестов"""
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
            auto_start=False,  # Не запускаем автоматически в тестах
            keyboard_backend="auto",
            min_recording_duration_sec=0.1,
            playback_idle_grace_sec=0.3,
            playback_wait_timeout_sec=5.0,
            recording_prestart_delay_sec=0.0,  # Убираем задержку для тестов
            mic_reset_timeout_sec=5.0,
        )
        
        integration = InputProcessingIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config,
        )
        
        await integration.initialize()
        
        # ✅ КРИТИЧНО: Устанавливаем keyboard_monitor ПОСЛЕ инициализации
        # (инициализация может создать реальный keyboard_monitor)
        integration.keyboard_monitor = keyboard_monitor
        
        yield integration
        try:
            await integration.stop()
        except Exception:
            pass

    @pytest.mark.asyncio
    async def test_long_press_activates_microphone_when_key_still_pressed(
        self, input_integration, event_bus, state_manager, keyboard_monitor
    ):
        """Тест: LONG_PRESS активирует микрофон, если клавиша все еще нажата"""
        # Устанавливаем начальное состояние
        state_manager.set_mode(AppMode.SLEEPING)
        
        # Отслеживаем публикацию voice.recording_start
        recording_start_events = []
        
        async def capture_recording_start(event):
            event_type = event.get("type") if isinstance(event, dict) else None
            payload = event.get("data") if isinstance(event, dict) else event
            if event_type == "voice.recording_start":
                recording_start_events.append((event_type, payload))
        
        await event_bus.subscribe("voice.recording_start", capture_recording_start)
        
        # Создаем LONG_PRESS событие
        long_press_event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.LONG_PRESS,
            timestamp=1234567890.0,
            duration=0.7,
        )
        
        # ✅ КРИТИЧНО: Клавиша все еще нажата
        keyboard_monitor.key_pressed = True
        
        # Устанавливаем pending_session_id для имитации состояния
        input_integration._pending_session_id = long_press_event.timestamp
        input_integration._input_state = InputState.PENDING  # ✅ Устанавливаем состояние PENDING
        
        # ✅ Мокируем методы ожидания для успешного выполнения
        input_integration._ensure_playback_idle = AsyncMock(return_value=None)
        input_integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=None)
        input_integration._wait_for_mic_opened = AsyncMock(return_value=True)  # ✅ Возвращаем True для успешного открытия
        input_integration._can_start_recording = AsyncMock(return_value=(True, "ok"))
        
        # Вызываем обработчик LONG_PRESS
        await input_integration._handle_long_press(long_press_event)
        
        # Даем время на обработку
        await asyncio.sleep(0.5)
        
        # Проверяем, что voice.recording_start был опубликован
        assert len(recording_start_events) > 0, "voice.recording_start должен быть опубликован при LONG_PRESS"
        
        logger.info("✅ Тест пройден: LONG_PRESS активирует микрофон, если клавиша все еще нажата")

    @pytest.mark.asyncio
    async def test_release_does_not_cancel_when_key_still_pressed(
        self, input_integration, event_bus, state_manager, keyboard_monitor
    ):
        """Тест: RELEASE не отменяет pending recording, если клавиша все еще нажата"""
        # Устанавливаем начальное состояние
        state_manager.set_mode(AppMode.SLEEPING)
        
        # Устанавливаем pending_session_id
        test_session_id = 1234567890.0
        input_integration._pending_session_id = test_session_id
        input_integration._recording_started = False
        
        # ✅ КРИТИЧНО: Клавиша все еще нажата
        keyboard_monitor.key_pressed = True
        
        # ✅ КРИТИЧНО: Устанавливаем keyboard_monitor в интеграцию (на случай, если он был перезаписан)
        input_integration.keyboard_monitor = keyboard_monitor
        
        # ✅ КРИТИЧНО: Проверяем, что keyboard_monitor правильно настроен
        assert hasattr(input_integration.keyboard_monitor, 'key_pressed'), \
            "keyboard_monitor должен иметь атрибут key_pressed"
        assert input_integration.keyboard_monitor.key_pressed == True, \
            f"key_pressed должен быть True перед вызовом RELEASE, но был {input_integration.keyboard_monitor.key_pressed}"
        
        # Создаем RELEASE событие
        release_event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.RELEASE,
            timestamp=1234567890.1,
            duration=0.7,
        )
        
        # Вызываем обработчик RELEASE
        await input_integration._handle_key_release(release_event)
        
        # Даем время на обработку
        await asyncio.sleep(0.1)
        
        # ✅ КРИТИЧНО: Проверяем, что keyboard_monitor.key_pressed все еще True
        # (в реальном коде он может быть обновлен, но в тесте мы контролируем его)
        if hasattr(input_integration.keyboard_monitor, 'key_pressed'):
            logger.info(f"🔍 После RELEASE: key_pressed={input_integration.keyboard_monitor.key_pressed}")
        
        # Проверяем, что _pending_recording_cancelled_event НЕ установлен
        assert not input_integration._pending_recording_cancelled_event.is_set(), \
            f"_pending_recording_cancelled_event не должен быть установлен, если клавиша все еще нажата. " \
            f"keyboard_monitor={input_integration.keyboard_monitor}, " \
            f"has_key_pressed={hasattr(input_integration.keyboard_monitor, 'key_pressed') if input_integration.keyboard_monitor else False}, " \
            f"key_pressed={getattr(input_integration.keyboard_monitor, 'key_pressed', None) if input_integration.keyboard_monitor else None}"
        
        # Проверяем, что _pending_session_id не был сброшен
        assert input_integration._pending_session_id == test_session_id, \
            "_pending_session_id не должен быть сброшен, если клавиша все еще нажата"
        
        logger.info("✅ Тест пройден: RELEASE не отменяет pending recording, если клавиша все еще нажата")

    @pytest.mark.asyncio
    async def test_release_cancels_when_key_released(
        self, input_integration, event_bus, state_manager, keyboard_monitor
    ):
        """Тест: RELEASE отменяет pending recording, если клавиша отпущена"""
        # Устанавливаем начальное состояние
        state_manager.set_mode(AppMode.SLEEPING)
        
        # Устанавливаем pending_session_id
        test_session_id = 1234567890.0
        input_integration._pending_session_id = test_session_id
        input_integration._recording_started = False
        
        # ✅ КРИТИЧНО: Клавиша отпущена
        keyboard_monitor.key_pressed = False
        
        # Создаем RELEASE событие
        release_event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.RELEASE,
            timestamp=1234567890.1,
            duration=0.7,
        )
        
        # Вызываем обработчик RELEASE
        await input_integration._handle_key_release(release_event)
        
        # Даем время на обработку
        await asyncio.sleep(0.1)
        
        # Проверяем, что _pending_recording_cancelled_event установлен
        assert input_integration._pending_recording_cancelled_event.is_set(), \
            "_pending_recording_cancelled_event должен быть установлен, если клавиша отпущена"
        
        # Проверяем, что _pending_session_id был сброшен
        assert input_integration._pending_session_id is None, \
            "_pending_session_id должен быть сброшен, если клавиша отпущена"
        
        logger.info("✅ Тест пройден: RELEASE отменяет pending recording, если клавиша отпущена")

    @pytest.mark.asyncio
    async def test_long_press_checks_cancellation_before_waiting(
        self, input_integration, event_bus, state_manager, keyboard_monitor
    ):
        """Тест: LONG_PRESS проверяет отмену перед ожиданием остановки воспроизведения"""
        # Устанавливаем начальное состояние
        state_manager.set_mode(AppMode.SLEEPING)
        
        # Устанавливаем pending_session_id
        test_session_id = 1234567890.0
        input_integration._pending_session_id = test_session_id
        input_integration._input_state = InputState.PENDING  # ✅ Устанавливаем состояние PENDING
        
        # ✅ КРИТИЧНО: Устанавливаем _pending_recording_cancelled_event ДО вызова LONG_PRESS
        input_integration._pending_recording_cancelled_event.set()
        
        # ✅ Мокируем методы ожидания (они не должны вызываться, так как отмена произойдет раньше)
        input_integration._ensure_playback_idle = AsyncMock(return_value=None)
        input_integration._wait_for_mic_closed_with_timeout = AsyncMock(return_value=None)
        input_integration._can_start_recording = AsyncMock(return_value=(True, "ok"))
        
        # Создаем LONG_PRESS событие
        long_press_event = KeyEvent(
            key="ctrl_n",
            event_type=KeyEventType.LONG_PRESS,
            timestamp=1234567890.0,
            duration=0.7,
        )
        
        # Клавиша все еще нажата
        keyboard_monitor.key_pressed = True
        
        # Отслеживаем публикацию voice.recording_start
        recording_start_events = []
        
        async def capture_recording_start(event):
            event_type = event.get("type") if isinstance(event, dict) else None
            if event_type == "voice.recording_start":
                recording_start_events.append(event)
        
        await event_bus.subscribe("voice.recording_start", capture_recording_start)
        
        # Вызываем обработчик LONG_PRESS
        await input_integration._handle_long_press(long_press_event)
        
        # Даем время на обработку
        await asyncio.sleep(0.2)
        
        # Проверяем, что voice.recording_start НЕ был опубликован (запись была отменена)
        assert len(recording_start_events) == 0, \
            "voice.recording_start не должен быть опубликован, если запись была отменена"
        
        # Проверяем, что _pending_session_id был сброшен
        assert input_integration._pending_session_id is None, \
            "_pending_session_id должен быть сброшен при отмене записи"
        
        logger.info("✅ Тест пройден: LONG_PRESS проверяет отмену перед ожиданием остановки воспроизведения")

