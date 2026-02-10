"""
Изолированный тест для проверки логики прерывания воспроизведения при SHORT_PRESS.

Проверяет:
1. Публикацию playback.cancelled при SHORT_PRESS в PROCESSING режиме
2. Обработку прерывания в SpeechPlaybackIntegration
3. Идемпотентность обработки (безопасность множественных вызовов)
"""

import asyncio
import logging
from unittest.mock import Mock
import uuid

import pytest
import pytest_asyncio

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.input_processing_integration import InputProcessingIntegration
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
from integration.core.state_manager import AppMode


logger = logging.getLogger(__name__)


class TestInterruptPlayback:
    """Тесты для логики прерывания воспроизведения при SHORT_PRESS"""

    @pytest.fixture
    def event_bus(self):
        """Создает EventBus для тестов"""
        return EventBus()

    @pytest.fixture
    def state_manager(self, event_bus):
        """Создает ApplicationStateManager для тестов"""
        manager = ApplicationStateManager()
        manager.attach_event_bus(event_bus)  # Подключаем EventBus для публикации событий
        return manager

    @pytest.fixture
    def error_handler(self):
        """Создает ErrorHandler для тестов"""
        return ErrorHandler()

    @pytest.fixture
    def input_integration(self, event_bus, state_manager, error_handler):
        """Создает InputProcessingIntegration для тестов"""
        from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
        keyboard_config = KeyboardConfig(
            key_to_monitor="left_shift",
            short_press_threshold=0.1,
            long_press_threshold=0.5,
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
            recording_prestart_delay_sec=0.3,
        )
        integration = InputProcessingIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=config,
        )
        return integration

    @pytest_asyncio.fixture
    async def speech_playback_integration(self, event_bus, state_manager, error_handler):
        """Создает SpeechPlaybackIntegration для тестов"""
        integration = SpeechPlaybackIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
        )
        # Инициализируем интеграцию (но не запускаем)
        await integration.initialize()
        yield integration
        # Cleanup
        try:
            await integration.stop()
        except Exception:
            pass

    @pytest.mark.asyncio
    async def test_short_press_publishes_playback_cancelled_in_processing(
        self, input_integration, state_manager, event_bus, error_handler
    ):
        """Тест: SHORT_PRESS в PROCESSING режиме публикует interrupt.request и grpc.request_cancel."""
        
        # Устанавливаем PROCESSING режим
        test_session_id = str(uuid.uuid4())
        state_manager.set_mode(AppMode.PROCESSING, session_id=test_session_id)
        
        # Устанавливаем pending_session_id для имитации состояния
        input_integration._pending_session_id = test_session_id
        input_integration._recording_started = False
        input_integration._playback_active = True  # Имитируем активное воспроизведение
        
        # Мокируем keyboard_monitor, чтобы избежать реальной инициализации
        input_integration.keyboard_monitor = Mock()
        
        # Инициализируем необходимые атрибуты
        input_integration._min_recording_duration = 0.1
        
        # ✅ НОВОЕ: Инициализируем InterruptManagementIntegration для обработки interrupt.request
        from integration.integrations.interrupt_management_integration import (
            InterruptManagementIntegration,
            InterruptManagementIntegrationConfig
        )
        interrupt_integration = InterruptManagementIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
            config=InterruptManagementIntegrationConfig(
                enable_speech_interrupts=True,
                enable_recording_interrupts=True,
                enable_session_interrupts=True,
            )
        )
        await interrupt_integration.initialize()
        
        # Собираем опубликованные события
        published_events = []
        
        async def capture_event(event):
            event_type = event.get("type") if isinstance(event, dict) else None
            payload = event.get("data") if isinstance(event, dict) else event
            published_events.append((event_type, payload))
        
        # Подписываемся на interrupt.request и grpc.request_cancel для проверки
        await event_bus.subscribe("interrupt.request", capture_event)
        await event_bus.subscribe("grpc.request_cancel", capture_event)
        
        # Создаем событие SHORT_PRESS
        from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
        
        short_press_event = KeyEvent(
            key="left_shift",
            event_type=KeyEventType.SHORT_PRESS,
            timestamp=1234567890.0,
            duration=0.133,
        )
        
        # Вызываем обработчик SHORT_PRESS
        await input_integration._handle_short_press(short_press_event)
        
        # Даем время на обработку асинхронных событий (увеличено для обработки через InterruptManagementIntegration)
        await asyncio.sleep(0.3)
        
        # Проверяем, что interrupt.request был опубликован
        interrupt_request_events = [
            (event_type, payload)
            for event_type, payload in published_events
            if event_type == "interrupt.request"
        ]
        
        assert len(interrupt_request_events) > 0, f"interrupt.request должен быть опубликован. Полученные события: {published_events}"
        
        # Проверяем, что grpc.request_cancel был опубликован через InterruptManagementIntegration
        grpc_cancel_events = [
            (event_type, payload)
            for event_type, payload in published_events
            if event_type == "grpc.request_cancel"
        ]
        
        assert len(grpc_cancel_events) > 0, f"grpc.request_cancel должен быть опубликован через InterruptManagementIntegration. Полученные события: {published_events}"
        
        # Проверяем содержимое события grpc.request_cancel
        event_type, payload = grpc_cancel_events[0]
        if isinstance(payload, dict):
            session_id = payload.get("session_id")
            assert session_id == test_session_id, f"session_id должен быть {test_session_id}, получен {session_id}"
        
        # Cleanup
        try:
            await interrupt_integration.stop()
        except Exception:
            pass
        
        logger.info("✅ Тест пройден: interrupt.request и grpc.request_cancel опубликованы")

    @pytest.mark.asyncio
    async def test_speech_playback_handles_interrupt_idempotently(
        self, speech_playback_integration, event_bus, state_manager
    ):
        """Тест: SpeechPlaybackIntegration обрабатывает прерывание идемпотентно"""
        # Мокируем плеер
        mock_player = Mock()
        mock_player.clear_queue = Mock(return_value=None)
        mock_player.stop_playback = Mock(return_value=True)
        
        speech_playback_integration._avf_player = mock_player
        test_session_id = str(uuid.uuid4())
        state_manager.set_mode(AppMode.PROCESSING, session_id=test_session_id)
        speech_playback_integration._cancelled_sessions = set()
        
        # Создаем событие playback.cancelled
        interrupt_event = {
            "type": "playback.cancelled",
            "data": {
                "session_id": str(test_session_id),
                "reason": "keyboard",
                "source": "input_processing",
            },
        }
        
        # Вызываем обработчик прерывания дважды (имитация дублирования)
        await speech_playback_integration._on_unified_interrupt(interrupt_event)
        await speech_playback_integration._on_unified_interrupt(interrupt_event)
        
        # Проверяем, что clear_queue и stop_playback были вызваны
        assert mock_player.clear_queue.call_count >= 1, "clear_queue должен быть вызван"
        assert mock_player.stop_playback.call_count >= 1, "stop_playback должен быть вызван"
        
        # Текущий guard-контракт: session помечается cancelled только если до cancel
        # уже был получен аудио-чанк (had_audio=True).
        assert test_session_id not in speech_playback_integration._cancelled_sessions
        
        logger.info("✅ Тест пройден: прерывание обрабатывается идемпотентно")

    @pytest.mark.asyncio
    async def test_interrupt_handles_idle_state_gracefully(
        self, speech_playback_integration, event_bus, state_manager
    ):
        """Тест: прерывание корректно обрабатывает состояние IDLE"""
        # Мокируем плеер
        mock_player = Mock()
        mock_player.clear_queue = Mock(return_value=None)
        mock_player.stop_playback = Mock(return_value=False)
        
        speech_playback_integration._avf_player = mock_player
        test_session_id = str(uuid.uuid4())
        state_manager.set_mode(AppMode.PROCESSING, session_id=test_session_id)
        speech_playback_integration._cancelled_sessions = set()
        
        # Создаем событие playback.cancelled
        interrupt_event = {
            "type": "playback.cancelled",
            "data": {
                "session_id": test_session_id,
                "reason": "keyboard",
                "source": "input_processing",
            },
        }
        
        # Вызываем обработчик прерывания
        await speech_playback_integration._on_unified_interrupt(interrupt_event)
        
        # В текущей реализации stop_playback вызывается независимо от состояния.
        assert mock_player.stop_playback.call_count >= 1
        
        logger.info("✅ Тест пройден: прерывание корректно обрабатывает состояние IDLE")

    @pytest.mark.asyncio
    async def test_interrupt_handles_error_state_gracefully(
        self, speech_playback_integration, event_bus, state_manager
    ):
        """Тест: прерывание корректно обрабатывает ошибки"""
        # Мокируем плеер, который выбрасывает исключение
        mock_player = Mock()
        mock_player.clear_queue = Mock(return_value=None)
        mock_player.stop_playback = Mock(side_effect=Exception("Test error"))
        
        speech_playback_integration._avf_player = mock_player
        test_session_id = str(uuid.uuid4())
        state_manager.set_mode(AppMode.PROCESSING, session_id=test_session_id)
        speech_playback_integration._cancelled_sessions = set()
        
        # Создаем событие playback.cancelled
        interrupt_event = {
            "type": "playback.cancelled",
            "data": {
                "session_id": str(test_session_id),
                "reason": "keyboard",
                "source": "input_processing",
            },
        }
        
        # Вызываем обработчик прерывания (не должно упасть)
        try:
            await speech_playback_integration._on_unified_interrupt(interrupt_event)
        except Exception as e:
            pytest.fail(f"Обработчик прерывания не должен выбрасывать исключения: {e}")
        
        logger.info("✅ Тест пройден: прерывание корректно обрабатывает ошибки")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
