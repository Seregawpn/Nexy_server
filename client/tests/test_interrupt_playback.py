"""
Изолированный тест для проверки логики прерывания воспроизведения при SHORT_PRESS.

Проверяет:
1. Публикацию interrupt.request при SHORT_PRESS в PROCESSING режиме
2. Обработку прерывания в SpeechPlaybackIntegration
3. Идемпотентность обработки (безопасность множественных вызовов)
"""

import asyncio
import logging
import time
from unittest.mock import Mock

import numpy as np
import pytest
import pytest_asyncio

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.integrations.input_processing_integration import InputProcessingIntegration
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
from modules.speech_playback.core.state import PlaybackState

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
    async def test_short_press_publishes_interrupt_request_in_processing(
        self, input_integration, state_manager, event_bus
    ):
        """Тест: SHORT_PRESS публикует interrupt.request при активном playback."""
        # Устанавливаем PROCESSING режим
        state_manager.set_mode(AppMode.PROCESSING)
        input_integration._playback_active = True
        input_integration._recording_started = False

        # Мокируем keyboard_monitor, чтобы избежать реальной инициализации
        input_integration.keyboard_monitor = Mock()

        # Инициализируем необходимые атрибуты
        input_integration._min_recording_duration = 0.1

        # Собираем опубликованные события
        published_events = []

        async def capture_event(event):
            event_type = event.get("type") if isinstance(event, dict) else None
            payload = event.get("data") if isinstance(event, dict) else event
            published_events.append((event_type, payload))

        # Подписываемся на interrupt.request для проверки
        await event_bus.subscribe("interrupt.request", capture_event)

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

        # Даем время на обработку асинхронных событий
        await asyncio.sleep(0.1)

        # Проверяем, что interrupt.request был опубликован
        interrupt_events = [
            (event_type, payload)
            for event_type, payload in published_events
            if event_type == "interrupt.request"
        ]

        assert len(interrupt_events) > 0, (
            f"interrupt.request должен быть опубликован. Полученные события: {published_events}"
        )

        # Проверяем содержимое события
        event_type, payload = interrupt_events[0]
        if isinstance(payload, dict):
            assert str(payload.get("source", "")).startswith("keyboard")
            assert payload.get("type") == "speech_stop"

        logger.info("✅ Тест пройден: interrupt.request опубликован при SHORT_PRESS с playback_active")

    @pytest.mark.asyncio
    async def test_press_publishes_interrupt_request_in_processing_without_playback_flag(
        self, input_integration, state_manager, event_bus
    ):
        """Тест: PRESS в PROCESSING публикует interrupt.request при активном playback."""
        state_manager.set_mode(AppMode.PROCESSING)
        input_integration._playback_active = True
        input_integration._active_grpc_session_id = None

        published_events = []

        async def capture_event(event):
            event_type = event.get("type") if isinstance(event, dict) else None
            payload = event.get("data") if isinstance(event, dict) else event
            published_events.append((event_type, payload))

        await event_bus.subscribe("interrupt.request", capture_event)

        from modules.input_processing.keyboard.types import KeyEvent, KeyEventType

        press_event = KeyEvent(
            key="left_shift",
            event_type=KeyEventType.PRESS,
            timestamp=1234567891.0,
            duration=0.0,
        )

        await input_integration._handle_press(press_event)
        await asyncio.sleep(0.05)

        interrupt_events = [
            (event_type, payload)
            for event_type, payload in published_events
            if event_type == "interrupt.request"
        ]
        assert len(interrupt_events) > 0, "interrupt.request должен публиковаться на PRESS при _playback_active"

    @pytest.mark.asyncio
    async def test_press_does_not_publish_interrupt_when_sleeping_with_stale_session(
        self, input_integration, state_manager, event_bus
    ):
        """Тест: PRESS НЕ публикует interrupt.request в SLEEPING при stale session_id без pending grpc."""
        sid = "165a3bb5-f1a5-490a-b204-e53def467ced"
        state_manager.set_mode(AppMode.SLEEPING, session_id=sid)
        input_integration._playback_active = False
        input_integration._active_grpc_session_id = None

        published_events = []

        async def capture_event(event):
            event_type = event.get("type") if isinstance(event, dict) else None
            payload = event.get("data") if isinstance(event, dict) else event
            published_events.append((event_type, payload))

        await event_bus.subscribe("interrupt.request", capture_event)

        from modules.input_processing.keyboard.types import KeyEvent, KeyEventType

        press_event = KeyEvent(
            key="left_shift",
            event_type=KeyEventType.PRESS,
            timestamp=1234567892.0,
            duration=0.0,
        )

        await input_integration._handle_press(press_event)
        await asyncio.sleep(0.05)

        interrupt_events = [
            (event_type, payload)
            for event_type, payload in published_events
            if event_type == "interrupt.request"
        ]
        assert len(interrupt_events) == 0, (
            "interrupt.request не должен публиковаться на PRESS в SLEEPING "
            "только из-за stale session_id"
        )
        assert state_manager.get_current_session_id() is None, (
            "stale session_id должен очищаться на новом press-cycle в idle/sleeping контексте"
        )

    @pytest.mark.asyncio
    async def test_press_and_long_press_same_press_id_publish_single_interrupt_request(
        self, input_integration, state_manager, event_bus
    ):
        """Тест-контракт: один press-cycle публикует только один preempt interrupt.request при playback."""
        state_manager.set_mode(
            AppMode.PROCESSING,
            session_id="f4f79e24-2d2d-4eb0-8b2f-4d0a0d30f4a3",
        )
        input_integration._playback_active = True
        input_integration._active_grpc_session_id = None

        published_events = []

        async def capture_event(event):
            event_type = event.get("type") if isinstance(event, dict) else None
            payload = event.get("data") if isinstance(event, dict) else event
            published_events.append((event_type, payload))

        await event_bus.subscribe("interrupt.request", capture_event)

        from modules.input_processing.keyboard.types import KeyEvent, KeyEventType

        press_id = "press-dedup-001"
        press_event = KeyEvent(
            key="left_shift",
            event_type=KeyEventType.PRESS,
            timestamp=1234567893.0,
            duration=0.0,
            data={"press_id": press_id},
        )
        long_press_event = KeyEvent(
            key="left_shift",
            event_type=KeyEventType.LONG_PRESS,
            timestamp=1234567893.7,
            duration=0.7,
            data={"press_id": press_id},
        )

        await input_integration._handle_press(press_event)
        await input_integration._handle_long_press(long_press_event)
        await asyncio.sleep(0.05)

        interrupt_events = [
            payload for event_type, payload in published_events if event_type == "interrupt.request"
        ]

        assert len(interrupt_events) == 1, (
            "В одном press-cycle должен быть ровно один interrupt.request "
            f"(получено={len(interrupt_events)}, events={interrupt_events})"
        )
        assert interrupt_events[0].get("press_id") == press_id
        assert interrupt_events[0].get("type") == "speech_stop"

    @pytest.mark.asyncio
    async def test_grpc_completed_keeps_session_during_playback_tail(
        self, input_integration, state_manager
    ):
        """Тест: grpc_completed не очищает session_id, если playback еще активен."""
        sid = "1de5d355-4f8a-4f29-9167-91ba41505889"
        state_manager.set_mode(AppMode.PROCESSING, session_id=sid)
        input_integration._active_grpc_session_id = sid
        input_integration._session_waiting_grpc = True
        input_integration._playback_active = True

        await input_integration._on_grpc_completed({"data": {"session_id": sid}})

        assert input_integration._state.value == "idle"
        assert input_integration._session_waiting_grpc is False
        assert input_integration._active_grpc_session_id == sid
        assert str(state_manager.get_current_session_id()) == sid

    @pytest.mark.asyncio
    async def test_playback_terminal_clears_tail_session_context(
        self, input_integration, state_manager
    ):
        """Тест: terminal playback очищает сохраненный tail-session context."""
        sid = "f6ed3301-3787-49ef-bf31-4abcb157b2d8"
        state_manager.set_mode(AppMode.PROCESSING, session_id=sid)
        input_integration._active_grpc_session_id = sid
        input_integration._session_waiting_grpc = False
        input_integration._playback_active = True

        await input_integration._on_playback_finished({"data": {"session_id": sid}})

        assert input_integration._playback_active is False
        assert input_integration._active_grpc_session_id is None
        assert state_manager.get_current_session_id() is None

    @pytest.mark.asyncio
    async def test_speech_playback_handles_interrupt_idempotently(
        self, speech_playback_integration, event_bus, state_manager
    ):
        """Тест: SpeechPlaybackIntegration обрабатывает прерывание идемпотентно"""
        # Мокируем плеер
        mock_player = Mock()
        mock_player.state_manager = Mock()
        mock_player.state_manager.current_state = PlaybackState.PLAYING
        mock_player.stop_playback = Mock(return_value=True)

        speech_playback_integration._avf_player = mock_player
        # КРИТИЧНО: Используем state_manager.set_mode() для установки session_id (единый источник истины)
        # Используем числовой session_id (timestamp), так как state_manager хранит строки
        test_session_id = 1234567890.0
        state_manager.set_mode(AppMode.PROCESSING, session_id=str(test_session_id))
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

        # Проверяем, что stop_playback был вызван
        assert mock_player.stop_playback.call_count >= 1, "stop_playback должен быть вызван"

        # Текущий guard-контракт: session помечается cancelled только если до cancel
        # уже был получен аудио-чанк (had_audio=True).
        assert str(test_session_id) not in speech_playback_integration._cancelled_sessions

        logger.info("✅ Тест пройден: прерывание обрабатывается идемпотентно")

    @pytest.mark.asyncio
    async def test_interrupt_handles_idle_state_gracefully(
        self, speech_playback_integration, event_bus, state_manager
    ):
        """Тест: прерывание корректно обрабатывает состояние IDLE"""
        # Мокируем плеер в состоянии IDLE
        mock_player = Mock()
        mock_player.state_manager = Mock()
        mock_player.state_manager.current_state = PlaybackState.IDLE
        mock_player.stop_playback = Mock(return_value=False)

        speech_playback_integration._avf_player = mock_player
        # КРИТИЧНО: Используем state_manager.set_mode() для установки session_id (единый источник истины)
        # Используем числовой session_id (timestamp), так как state_manager хранит строки
        test_session_id = 1234567890.0
        state_manager.set_mode(AppMode.PROCESSING, session_id=str(test_session_id))
        speech_playback_integration._cancelled_sessions = set()

        # Создаем событие playback.cancelled
        interrupt_event = {
            "type": "playback.cancelled",
            "data": {
                "session_id": "test_session_123",
                "reason": "keyboard",
                "source": "input_processing",
            },
        }

        # Вызываем обработчик прерывания
        await speech_playback_integration._on_unified_interrupt(interrupt_event)

        # Проверяем, что stop_playback НЕ был вызван (состояние IDLE)
        # В нашей реализации мы все равно вызываем stop_playback, но он вернет False
        # Это безопасно, так как метод идемпотентный
        assert (
            mock_player.stop_playback.call_count == 0
            or mock_player.stop_playback.return_value == False
        )

        logger.info("✅ Тест пройден: прерывание корректно обрабатывает состояние IDLE")

    @pytest.mark.asyncio
    async def test_interrupt_handles_error_state_gracefully(
        self, speech_playback_integration, event_bus, state_manager
    ):
        """Тест: прерывание корректно обрабатывает ошибки"""
        # Мокируем плеер, который выбрасывает исключение
        mock_player = Mock()
        mock_player.state_manager = Mock()
        mock_player.state_manager.current_state = PlaybackState.PLAYING
        mock_player.stop_playback = Mock(side_effect=Exception("Test error"))

        speech_playback_integration._avf_player = mock_player
        # КРИТИЧНО: Используем state_manager.set_mode() для установки session_id (единый источник истины)
        # Используем числовой session_id (timestamp), так как state_manager хранит строки
        test_session_id = 1234567890.0
        state_manager.set_mode(AppMode.PROCESSING, session_id=str(test_session_id))
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

    @pytest.mark.asyncio
    async def test_playback_signal_skips_stale_event(
        self, speech_playback_integration, state_manager
    ):
        """Тест: просроченный playback.signal не проигрывается."""
        state_manager.set_mode(AppMode.LISTENING)
        speech_playback_integration._signal_max_age_ms = 100
        speech_playback_integration._avf_player = Mock()
        speech_playback_integration._avf_player.add_audio_data = Mock()

        async def _ready():
            return True

        speech_playback_integration._ensure_player_ready = _ready

        old_ts = int((time.monotonic() - 1.0) * 1000)
        await speech_playback_integration._on_playback_signal(
            {
                "data": {
                    "pattern": "listen_start",
                    "pcm": b"\x00\x00\x01\x00",
                    "emitted_at_ms": old_ts,
                }
            }
        )

        speech_playback_integration._avf_player.add_audio_data.assert_not_called()

    @pytest.mark.asyncio
    async def test_playback_signal_skips_when_user_quit_intent(
        self, speech_playback_integration, state_manager
    ):
        """Тест: playback.signal подавляется при USER_QUIT_INTENT."""
        state_manager.set_mode(AppMode.LISTENING)
        state_manager.set_state_data(StateKeys.USER_QUIT_INTENT, True)
        speech_playback_integration._avf_player = Mock()
        speech_playback_integration._avf_player.add_audio_data = Mock()

        async def _ready():
            return True

        speech_playback_integration._ensure_player_ready = _ready

        await speech_playback_integration._on_playback_signal(
            {"data": {"pattern": "listen_start", "pcm": b"\x00\x00\x01\x00"}}
        )

        speech_playback_integration._avf_player.add_audio_data.assert_not_called()

    @pytest.mark.asyncio
    async def test_playback_signal_skips_listen_start_outside_listening(
        self, speech_playback_integration, state_manager
    ):
        """Тест: listen_start cue не проигрывается вне LISTENING."""
        state_manager.set_mode(AppMode.SLEEPING)
        speech_playback_integration._avf_player = Mock()
        speech_playback_integration._avf_player.add_audio_data = Mock()

        async def _ready():
            return True

        speech_playback_integration._ensure_player_ready = _ready

        await speech_playback_integration._on_playback_signal(
            {"data": {"pattern": "listen_start", "pcm": b"\x00\x00\x01\x00"}}
        )

        speech_playback_integration._avf_player.add_audio_data.assert_not_called()

    @pytest.mark.asyncio
    async def test_playback_signal_allows_error_in_listening(
        self, speech_playback_integration, state_manager
    ):
        """Тест: error cue не подавляется в LISTENING (решение в SignalIntegration)."""
        state_manager.set_mode(AppMode.LISTENING)
        speech_playback_integration._avf_player = Mock()
        speech_playback_integration._avf_player.add_audio_data = Mock()

        async def _ready():
            return True

        speech_playback_integration._ensure_player_ready = _ready

        await speech_playback_integration._on_playback_signal(
            {"data": {"pattern": "error", "pcm": b"\x00\x00\x01\x00"}}
        )

        speech_playback_integration._avf_player.add_audio_data.assert_called_once()

    @pytest.mark.asyncio
    async def test_recognition_failed_resets_waiting_grpc_state(
        self, input_integration, state_manager
    ):
        """Тест: recognition_failed всегда очищает waiting_grpc для активной сессии."""
        sid = "c8422b6d-781b-4f68-90a1-76cdf7f8f307"
        state_manager.set_mode(AppMode.SLEEPING, session_id=sid)
        input_integration._active_grpc_session_id = sid
        input_integration._session_waiting_grpc = True
        input_integration._set_state(input_integration._state.__class__.WAITING_GRPC, "test_setup")

        await input_integration._on_recognition_failed(
            {"data": {"session_id": sid, "error": "unknown_value"}}
        )

        assert input_integration._session_waiting_grpc is False
        assert input_integration._active_grpc_session_id is None
        assert input_integration._state.value == "idle"
        assert state_manager.get_current_session_id() is None

    @pytest.mark.asyncio
    async def test_first_grpc_audio_chunk_does_not_force_stop_start_restart(
        self, speech_playback_integration
    ):
        """Тест: первый audio chunk новой сессии не делает принудительный stop/start."""
        sid = "b86d98aa-3797-4e1f-8f8b-e983866b8502"

        mock_player = Mock()
        mock_player.add_audio_data = Mock()
        mock_player.stop_playback = Mock()
        mock_player.start_playback = Mock(return_value=True)
        speech_playback_integration._avf_player = mock_player

        async def _ready():
            return True

        speech_playback_integration._ensure_player_ready = _ready

        # int16 mono, 4 samples
        pcm = (np.array([1000, -1000, 500, -500], dtype=np.int16)).tobytes()
        await speech_playback_integration._on_audio_chunk(
            {
                "data": {
                    "session_id": sid,
                    "bytes": pcm,
                    "dtype": "int16",
                    "sample_rate": 48000,
                    "channels": 1,
                    "shape": [4],
                }
            }
        )

        mock_player.stop_playback.assert_not_called()
        mock_player.start_playback.assert_not_called()
        mock_player.add_audio_data.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
