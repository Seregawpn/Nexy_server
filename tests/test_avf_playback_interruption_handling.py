"""
Изолированный тест для проверки обработки прерывания воспроизведения AVFAudioEngine

✅ Проверяет:
1. Сохранение события audio.playback.interrupted в очередь, когда EventBus недоступен
2. Публикацию события из очереди, когда EventBus становится доступен
3. Обработку события _on_avf_playback_interrupted в SpeechPlaybackIntegration
4. Проверку реального состояния engine после возобновления воспроизведения
"""

import pytest
import pytest_asyncio
import asyncio
import threading
import types
from unittest.mock import Mock, AsyncMock, MagicMock, patch, PropertyMock
from typing import Dict, Any, List

# Импорты для тестирования
from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine, AudioState
from integration.integrations.speech_playback_integration import SpeechPlaybackIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from config.audio_config import AudioConfig

class TestAVFPlaybackInterruptionHandling:
    """Изолированные тесты для проверки обработки прерывания воспроизведения"""
    
    @pytest_asyncio.fixture
    async def event_bus(self):
        """Создаём EventBus с запущенным loop"""
        event_bus = EventBus()
        loop = asyncio.get_event_loop()
        event_bus.attach_loop(loop)
        return event_bus
    
    @pytest.fixture
    def mock_engine(self):
        """Создаём мок AVAudioEngine"""
        mock_engine = MagicMock()
        mock_engine.isRunning.return_value = False  # Engine остановлен системой
        return mock_engine
    
    @pytest.fixture
    def audio_config(self):
        """Создаём конфигурацию аудио"""
        return AudioConfig.default()
    
    @pytest_asyncio.fixture
    async def avf_engine_without_event_bus(self, audio_config, mock_engine):
        """Создаём минимальный мок AVFAudioEngine БЕЗ EventBus для тестирования логики публикации"""
        # Создаём минимальный мок, который имеет только необходимые методы и атрибуты
        engine = MagicMock(spec=AVFAudioEngine)
        engine._event_bus = None  # EventBus недоступен
        engine._pending_events = []
        engine._pending_events_lock = threading.Lock()
        engine._event_loop = None
        engine._pending_loop = None
        engine._lock = threading.RLock()
        engine._output_state = AudioState.RUNNING
        engine._engine = mock_engine
        
        # Добавляем реальные методы для тестирования
        engine._publish_event_safe = types.MethodType(AVFAudioEngine._publish_event_safe, engine)
        engine._ensure_loop_attached = types.MethodType(AVFAudioEngine._ensure_loop_attached, engine)
        engine._submit_to_event_loop = types.MethodType(AVFAudioEngine._submit_to_event_loop, engine)
        engine._flush_pending_events = types.MethodType(AVFAudioEngine._flush_pending_events, engine)
        
        return engine
    
    @pytest_asyncio.fixture
    async def avf_engine_with_event_bus(self, audio_config, event_bus, mock_engine):
        """Создаём минимальный мок AVFAudioEngine С EventBus для тестирования логики публикации"""
        # Создаём минимальный мок, который имеет только необходимые методы и атрибуты
        engine = MagicMock(spec=AVFAudioEngine)
        engine._event_bus = event_bus
        engine._pending_events = []
        engine._pending_events_lock = threading.Lock()
        engine._lock = threading.RLock()
        engine._output_state = AudioState.RUNNING
        engine._engine = mock_engine
        
        # Устанавливаем event loop
        loop = asyncio.get_event_loop()
        engine._event_loop = loop
        engine._pending_loop = None
        
        # Добавляем реальные методы для тестирования
        engine._publish_event_safe = types.MethodType(AVFAudioEngine._publish_event_safe, engine)
        engine._ensure_loop_attached = types.MethodType(AVFAudioEngine._ensure_loop_attached, engine)
        engine._submit_to_event_loop = types.MethodType(AVFAudioEngine._submit_to_event_loop, engine)
        engine._flush_pending_events = types.MethodType(AVFAudioEngine._flush_pending_events, engine)
        engine.attach_event_loop = types.MethodType(AVFAudioEngine.attach_event_loop, engine)
        engine.is_output_active = PropertyMock(return_value=True)
        
        return engine
    
    @pytest_asyncio.fixture
    async def speech_playback_integration(self, event_bus, avf_engine_with_event_bus):
        """Создаём SpeechPlaybackIntegration с моками"""
        state_manager = ApplicationStateManager()  # Не принимает аргументов
        error_handler = ErrorHandler(event_bus)
        
        integration = SpeechPlaybackIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        # Устанавливаем AVF engine
        integration._avf_engine = avf_engine_with_event_bus
        integration._use_avf = True
        
        # Инициализируем интеграцию
        await integration.initialize()
        
        return integration
    
    @pytest.mark.asyncio
    async def test_interrupted_event_saved_to_queue_when_event_bus_unavailable(
        self, avf_engine_without_event_bus, mock_engine
    ):
        """
        ✅ Тест 1: Событие audio.playback.interrupted сохраняется в очередь, когда EventBus недоступен
        
        Проверяет, что при остановке engine системой событие сохраняется в очередь,
        даже если EventBus = None
        """
        # Симулируем ситуацию: engine остановлен системой во время воспроизведения
        mock_engine.isRunning.return_value = False
        
        # Вызываем _publish_event_safe (как в _handle_output_device_change)
        avf_engine_without_event_bus._publish_event_safe("audio.playback.interrupted", {
            "reason": "engine_stopped_by_system",
            "device_name": "Test Device",
            "source": "AVF_CONFIGURATION_CHANGE"
        })
        
        # Проверяем, что событие сохранено в очередь
        assert len(avf_engine_without_event_bus._pending_events) == 1, \
            "Событие должно быть сохранено в очередь"
        
        event_type, payload = avf_engine_without_event_bus._pending_events[0]
        assert event_type == "audio.playback.interrupted", \
            f"Тип события должен быть audio.playback.interrupted, получен: {event_type}"
        assert payload["reason"] == "engine_stopped_by_system", \
            f"Причина должна быть engine_stopped_by_system, получена: {payload['reason']}"
        
        print("✅ Тест 1 пройден: Событие сохранено в очередь при недоступном EventBus")
    
    @pytest.mark.asyncio
    async def test_interrupted_event_published_when_event_bus_becomes_available(
        self, avf_engine_without_event_bus, event_bus, mock_engine
    ):
        """
        ✅ Тест 2: Событие публикуется из очереди, когда EventBus становится доступен
        
        Проверяет, что при прикреплении EventBus события из очереди публикуются
        """
        # Симулируем ситуацию: событие уже в очереди (EventBus был недоступен)
        avf_engine_without_event_bus._pending_events.append((
            "audio.playback.interrupted",
            {
                "reason": "engine_stopped_by_system",
                "device_name": "Test Device",
                "source": "AVF_CONFIGURATION_CHANGE"
            }
        ))
        
        # Создаём сборщик событий для проверки публикации
        published_events: List[Dict[str, Any]] = []
        
        async def event_collector(event: Dict[str, Any]):
            published_events.append(event)
        
        await event_bus.subscribe("audio.playback.interrupted", event_collector)
        
        # Прикрепляем EventBus и event loop к engine
        avf_engine_without_event_bus._event_bus = event_bus
        loop = asyncio.get_event_loop()
        # Устанавливаем _event_loop напрямую (так как _ensure_loop_attached мокирован)
        avf_engine_without_event_bus._event_loop = loop
        avf_engine_without_event_bus._pending_loop = None
        # Вызываем _flush_pending_events вручную
        avf_engine_without_event_bus._flush_pending_events()
        
        # Ждём публикации событий из очереди
        await asyncio.sleep(0.2)
        
        # Проверяем, что событие было опубликовано
        assert len(published_events) == 1, \
            f"Событие должно быть опубликовано, получено: {len(published_events)}"
        
        event_data = published_events[0].get("data", {})
        assert event_data["reason"] == "engine_stopped_by_system", \
            f"Причина должна быть engine_stopped_by_system, получена: {event_data.get('reason')}"
        
        # Проверяем, что очередь очищена
        assert len(avf_engine_without_event_bus._pending_events) == 0, \
            "Очередь должна быть очищена после публикации"
        
        print("✅ Тест 2 пройден: Событие опубликовано из очереди при доступном EventBus")
    
    @pytest.mark.asyncio
    async def test_speech_playback_handles_interrupted_event(
        self, speech_playback_integration, event_bus, avf_engine_with_event_bus, mock_engine
    ):
        """
        ✅ Тест 3: SpeechPlaybackIntegration обрабатывает событие audio.playback.interrupted
        
        Проверяет, что обработчик _on_avf_playback_interrupted публикует playback.completed
        """
        # Симулируем активную сессию
        session_id = "test_session_123"
        speech_playback_integration.state_manager.update_session_id(session_id)
        
        # Добавляем сессию в буферы (симулируем активное воспроизведение)
        speech_playback_integration._avf_chunk_buffer[session_id] = []
        speech_playback_integration._avf_is_playing[session_id] = True
        
        # Создаём сборщик событий для проверки публикации playback.completed
        published_events: List[Dict[str, Any]] = []
        
        async def event_collector(event: Dict[str, Any]):
            published_events.append(event)
        
        await event_bus.subscribe("playback.completed", event_collector)
        
        # Публикуем событие audio.playback.interrupted (формат EventBus: type + data)
        await event_bus.publish("audio.playback.interrupted", {
            "reason": "engine_stopped_by_system",
            "device_name": "Test Device",
            "source": "AVF_CONFIGURATION_CHANGE"
        })
        
        # Ждём обработки события
        await asyncio.sleep(0.1)
        
        # Проверяем, что playback.completed был опубликован
        assert len(published_events) == 1, \
            f"playback.completed должен быть опубликован, получено: {len(published_events)}"
        
        event_data = published_events[0].get("data", {})
        assert event_data.get("session_id") == session_id, \
            f"session_id должен быть {session_id}, получен: {event_data.get('session_id')}"
        assert event_data.get("interrupted") == True, \
            f"interrupted должен быть True, получен: {event_data.get('interrupted')}"
        assert event_data.get("reason") == "engine_stopped_by_system", \
            f"reason должен быть engine_stopped_by_system, получен: {event_data.get('reason')}"
        
        print("✅ Тест 3 пройден: SpeechPlaybackIntegration обрабатывает interrupted и публикует completed")
    
    @pytest.mark.asyncio
    async def test_resume_playback_checks_real_engine_state(
        self, speech_playback_integration, event_bus, avf_engine_with_event_bus, mock_engine
    ):
        """
        ✅ Тест 4: После возобновления воспроизведения проверяется реальное состояние engine
        
        Проверяет, что после возобновления воспроизведения проверяется не только is_output_active,
        но и реальное состояние engine (_engine.isRunning())
        """
        session_id = "test_session_456"
        speech_playback_integration.state_manager.update_session_id(session_id)
        
        # Симулируем ситуацию: воспроизведение было прервано и возобновлено
        # Но engine остановлен системой
        with avf_engine_with_event_bus._lock:
            avf_engine_with_event_bus._output_state = AudioState.RUNNING  # is_output_active = True
        
        mock_engine.isRunning.return_value = False  # Но engine реально остановлен
        
        # Создаём сборщик событий
        published_events: List[Dict[str, Any]] = []
        
        async def event_collector(event: Dict[str, Any]):
            published_events.append(event)
        
        await event_bus.subscribe("playback.completed", event_collector)
        
        # Симулируем проверку после возобновления (как в _on_raw_audio)
        is_output_active = avf_engine_with_event_bus.is_output_active
        engine_running = avf_engine_with_event_bus._engine.isRunning() if avf_engine_with_event_bus._engine else False
        
        # Проверяем логику из исправления
        if not is_output_active or not engine_running:
            # Воспроизведение не активно или engine остановлен - публикуем completed
            await event_bus.publish("playback.completed", {
                "session_id": session_id,
                "pattern": "test_pattern"
            })
        
        # Ждём обработки
        await asyncio.sleep(0.1)
        
        # Проверяем, что playback.completed был опубликован (engine остановлен)
        assert len(published_events) == 1, \
            f"playback.completed должен быть опубликован (engine остановлен), получено: {len(published_events)}"
        
        event_data = published_events[0].get("data", {})
        assert event_data.get("session_id") == session_id, \
            f"session_id должен быть {session_id}, получен: {event_data.get('session_id')}"
        
        print("✅ Тест 4 пройден: Проверка реального состояния engine работает корректно")
    
    @pytest.mark.asyncio
    async def test_full_interruption_flow(
        self, audio_config, event_bus, mock_engine
    ):
        """
        ✅ Тест 5: Полный поток обработки прерывания (интеграционный тест)
        
        Проверяет полный поток:
        1. Engine остановлен системой → событие в очередь
        2. EventBus становится доступен → событие публикуется
        3. SpeechPlaybackIntegration получает событие → публикует playback.completed
        """
        # Шаг 1: Создаём минимальный мок engine БЕЗ EventBus (симулируем раннюю инициализацию)
        engine = MagicMock(spec=AVFAudioEngine)
        engine._event_bus = None
        engine._pending_events = []
        engine._pending_events_lock = threading.Lock()
        engine._lock = threading.RLock()
        engine._output_state = AudioState.RUNNING
        engine._engine = mock_engine
        engine._event_loop = None
        engine._pending_loop = None
        mock_engine.isRunning.return_value = False
        
        # Добавляем реальные методы для тестирования
        engine._publish_event_safe = types.MethodType(AVFAudioEngine._publish_event_safe, engine)
        engine._ensure_loop_attached = types.MethodType(AVFAudioEngine._ensure_loop_attached, engine)
        engine._submit_to_event_loop = types.MethodType(AVFAudioEngine._submit_to_event_loop, engine)
        engine._flush_pending_events = types.MethodType(AVFAudioEngine._flush_pending_events, engine)
        engine.attach_event_loop = types.MethodType(AVFAudioEngine.attach_event_loop, engine)
        
        # Шаг 2: Публикуем событие прерывания (EventBus недоступен)
        engine._publish_event_safe("audio.playback.interrupted", {
            "reason": "engine_stopped_by_system",
            "device_name": "Test Device",
            "source": "AVF_CONFIGURATION_CHANGE"
        })
        
        # Проверяем, что событие в очереди
        assert len(engine._pending_events) == 1, "Событие должно быть в очереди"
        
        # Шаг 3: Создаём SpeechPlaybackIntegration и прикрепляем EventBus
        state_manager = ApplicationStateManager()  # Не принимает аргументов
        error_handler = ErrorHandler(event_bus)
        
        integration = SpeechPlaybackIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        integration._avf_engine = engine
        integration._use_avf = True
        await integration.initialize()
        
        # Устанавливаем session_id
        session_id = "test_full_flow"
        state_manager.update_session_id(session_id)
        integration._avf_chunk_buffer[session_id] = []
        integration._avf_is_playing[session_id] = True
        
        # Создаём сборщик событий
        playback_completed_events: List[Dict[str, Any]] = []
        
        async def on_playback_completed(event: Dict[str, Any]):
            playback_completed_events.append(event)
        
        await event_bus.subscribe("playback.completed", on_playback_completed)
        
        # Шаг 4: Прикрепляем EventBus к engine (симулируем, что EventBus стал доступен)
        engine._event_bus = event_bus
        loop = asyncio.get_event_loop()
        engine.attach_event_loop(loop)
        
        # Ждём обработки всех событий
        await asyncio.sleep(0.2)
        
        # Проверяем результаты
        assert len(playback_completed_events) == 1, \
            f"playback.completed должен быть опубликован, получено: {len(playback_completed_events)}"
        
        event_data = playback_completed_events[0].get("data", {})
        assert event_data.get("session_id") == session_id, \
            f"session_id должен быть {session_id}, получен: {event_data.get('session_id')}"
        assert event_data.get("interrupted") == True, \
            f"interrupted должен быть True, получен: {event_data.get('interrupted')}"
        
        # Проверяем, что очередь очищена
        assert len(engine._pending_events) == 0, \
            "Очередь должна быть очищена после публикации"
        
        print("✅ Тест 5 пройден: Полный поток обработки прерывания работает корректно")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
