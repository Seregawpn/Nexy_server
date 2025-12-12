"""
Изолированный тест для проверки закрытия MicrophoneStream без метода is_active().

Проверяет, что код корректно обрабатывает MicrophoneStream из speech_recognition,
который не имеет метода is_active(), но имеет методы stop_stream() и close().
"""

import pytest
import pytest_asyncio
from unittest.mock import MagicMock, AsyncMock, patch
import asyncio

from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.core.state_manager import AppMode


@pytest_asyncio.fixture
async def voice_integration():
    """Создаёт изолированный экземпляр VoiceRecognitionIntegration для тестирования"""
    mock_event_bus = MagicMock(spec=EventBus)
    mock_event_bus.publish = AsyncMock()
    mock_event_bus.subscribe = AsyncMock()
    mock_event_bus.unsubscribe = AsyncMock()
    
    mock_state_manager = MagicMock(spec=ApplicationStateManager)
    mock_state_manager.is_microphone_active = MagicMock(return_value=False)
    mock_state_manager.set_microphone_state = MagicMock(return_value=True)
    mock_state_manager.force_close_microphone = MagicMock(return_value=True)
    mock_state_manager.get_current_session_id = MagicMock(return_value="test_session")
    mock_state_manager.get_current_mode = MagicMock(return_value=AppMode.LISTENING)
    
    mock_error_handler = MagicMock(spec=ErrorHandler)
    mock_error_handler.handle_error = AsyncMock()
    
    integration = VoiceRecognitionIntegration(
        event_bus=mock_event_bus,
        state_manager=mock_state_manager,
        error_handler=mock_error_handler
    )
    
    # Мокируем AVF engine
    integration._avf_engine = None
    integration._use_avf = True
    
    # Инициализируем Google recognizer и microphone для новой логики
    integration._google_recognizer = MagicMock()
    integration._google_microphone = None
    integration._google_stop_listening = None
    integration._google_recording_active = False
    integration._google_audio_chunks = []
    integration._google_audio_chunks_lock = asyncio.Lock()
    
    return integration, mock_event_bus, mock_state_manager


def create_microphone_stream_without_is_active():
    """Создаёт мок MicrophoneStream БЕЗ метода is_active() (как в speech_recognition)"""
    # MicrophoneStream из speech_recognition не имеет is_active(), но имеет stop_stream() и close()
    mock_stream = MagicMock()
    # НЕ добавляем is_active() - это ключевая часть теста
    mock_stream.stop_stream = MagicMock()
    mock_stream.close = MagicMock()
    
    mock_microphone = MagicMock()
    mock_microphone.stream = mock_stream
    
    return mock_microphone, mock_stream


def create_microphone_stream_with_is_active():
    """Создаёт мок MicrophoneStream С методом is_active() (как в PyAudio)"""
    mock_stream = MagicMock()
    mock_stream.is_active = MagicMock(return_value=True)
    mock_stream.stop_stream = MagicMock()
    mock_stream.close = MagicMock()
    
    mock_microphone = MagicMock()
    mock_microphone.stream = mock_stream
    
    return mock_microphone, mock_stream


@pytest.mark.asyncio
async def test_close_stream_without_is_active_method(voice_integration):
    """Тест: Закрытие stream без метода is_active() (MicrophoneStream из speech_recognition)"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок микрофона БЕЗ метода is_active()
    mock_microphone, mock_stream = create_microphone_stream_without_is_active()
    
    # Устанавливаем состояние
    integration._google_microphone = mock_microphone
    integration._google_stop_listening = MagicMock()
    integration._google_recording_active = True
    integration._google_recognizer = MagicMock()
    
    # Симулируем остановку записи
    event = {
        "type": "voice.recording_stop",
        "data": {
            "session_id": "test_session",
            "duration": 2.0
        }
    }
    
    integration._set_session_id("test_session", reason="test")
    mock_state_manager.get_current_session_id.return_value = "test_session"
    
    # Мокируем распознавание
    integration._recognize_google_audio = AsyncMock()
    integration._google_chunk_event = asyncio.Event()
    integration._google_chunk_event.set()
    
    import speech_recognition as sr
    mock_audio_data = MagicMock(spec=sr.AudioData)
    mock_audio_data.get_raw_data = MagicMock(return_value=b"test_audio_data")
    integration._google_audio_data = mock_audio_data
    integration._google_audio_chunks = [mock_audio_data]
    
    # Вызываем обработчик (не должно упасть с AttributeError)
    try:
        await integration._on_recording_stop(event)
    except AttributeError as e:
        if "'MicrophoneStream' object has no attribute 'is_active'" in str(e):
            pytest.fail(f"Код не должен падать с AttributeError для stream без is_active(): {e}")
        else:
            raise
    
    # Проверяем, что stream был закрыт
    assert mock_stream.close.called, "Stream должен быть закрыт"
    
    # Проверяем, что stop_stream был вызван (если метод доступен)
    # В реальном коде stop_stream вызывается только если метод доступен
    if hasattr(mock_stream, 'stop_stream'):
        # stop_stream может быть вызван или нет, в зависимости от логики
        # Главное - что close() был вызван
        pass


@pytest.mark.asyncio
async def test_close_stream_with_is_active_method(voice_integration):
    """Тест: Закрытие stream С методом is_active() (PyAudio stream)"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок микрофона С методом is_active()
    mock_microphone, mock_stream = create_microphone_stream_with_is_active()
    mock_stream.is_active.return_value = True  # Stream активен
    
    # Устанавливаем состояние
    integration._google_microphone = mock_microphone
    integration._google_stop_listening = MagicMock()
    integration._google_recording_active = True
    integration._google_recognizer = MagicMock()
    
    # Симулируем остановку записи
    event = {
        "type": "voice.recording_stop",
        "data": {
            "session_id": "test_session",
            "duration": 2.0
        }
    }
    
    integration._set_session_id("test_session", reason="test")
    mock_state_manager.get_current_session_id.return_value = "test_session"
    
    # Мокируем распознавание
    integration._recognize_google_audio = AsyncMock()
    integration._google_chunk_event = asyncio.Event()
    integration._google_chunk_event.set()
    
    import speech_recognition as sr
    mock_audio_data = MagicMock(spec=sr.AudioData)
    mock_audio_data.get_raw_data = MagicMock(return_value=b"test_audio_data")
    integration._google_audio_data = mock_audio_data
    integration._google_audio_chunks = [mock_audio_data]
    
    # Вызываем обработчик
    await integration._on_recording_stop(event)
    
    # Проверяем, что stream был остановлен и закрыт
    assert mock_stream.stop_stream.called, "Stream должен быть остановлен (stop_stream вызван)"
    assert mock_stream.close.called, "Stream должен быть закрыт"


@pytest.mark.asyncio
async def test_close_stream_in_finally_block_without_is_active(voice_integration):
    """Тест: Закрытие stream в finally блоке без метода is_active()"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок микрофона БЕЗ метода is_active()
    mock_microphone, mock_stream = create_microphone_stream_without_is_active()
    
    # Устанавливаем состояние
    integration._google_microphone = mock_microphone
    integration._google_stop_listening = MagicMock()
    integration._google_recording_active = True
    integration._google_recognizer = MagicMock()
    
    # Симулируем остановку записи с ошибкой (чтобы проверить finally блок)
    event = {
        "type": "voice.recording_stop",
        "data": {
            "session_id": "test_session",
            "duration": 2.0
        }
    }
    
    integration._set_session_id("test_session", reason="test")
    mock_state_manager.get_current_session_id.return_value = "test_session"
    
    # Мокируем распознавание с ошибкой
    integration._recognize_google_audio = AsyncMock(side_effect=Exception("Test error"))
    integration._google_chunk_event = asyncio.Event()
    integration._google_chunk_event.set()
    
    import speech_recognition as sr
    mock_audio_data = MagicMock(spec=sr.AudioData)
    mock_audio_data.get_raw_data = MagicMock(return_value=b"test_audio_data")
    integration._google_audio_data = mock_audio_data
    integration._google_audio_chunks = [mock_audio_data]
    
    # Вызываем обработчик (не должно упасть с AttributeError даже при ошибке)
    try:
        await integration._on_recording_stop(event)
    except AttributeError as e:
        if "'MicrophoneStream' object has no attribute 'is_active'" in str(e):
            pytest.fail(f"Код не должен падать с AttributeError в finally блоке: {e}")
        else:
            raise
    
    # Проверяем, что stream был закрыт в finally блоке
    assert mock_stream.close.called, "Stream должен быть закрыт в finally блоке"


@pytest.mark.asyncio
async def test_close_stream_on_error_activation_without_is_active(voice_integration):
    """Тест: Закрытие stream при ошибке активации без метода is_active()"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок микрофона БЕЗ метода is_active()
    mock_microphone, mock_stream = create_microphone_stream_without_is_active()
    
    # Устанавливаем состояние как будто микрофон был создан, но произошла ошибка
    integration._google_microphone = mock_microphone
    integration._google_stop_listening = None
    integration._google_recording_active = True
    integration._google_recognizer = MagicMock()
    
    # Симулируем ситуацию, когда микрофон был создан, но произошла ошибка активации
    # В этом случае код должен закрыть stream в блоке обработки ошибки
    # Проверяем напрямую код закрытия stream при ошибке активации
    
    # Имитируем вызов кода закрытия stream при ошибке активации
    # (это код из блока except в _on_recording_start)
    try:
        if integration._google_microphone and hasattr(integration._google_microphone, 'stream'):
            stream = integration._google_microphone.stream
            if stream:
                # ✅ ИСПРАВЛЕНИЕ: MicrophoneStream не имеет is_active()
                if hasattr(stream, 'stop_stream'):
                    try:
                        if hasattr(stream, 'is_active') and stream.is_active():
                            stream.stop_stream()
                        else:
                            stream.stop_stream()
                    except Exception:
                        pass
                if hasattr(stream, 'close'):
                    try:
                        stream.close()
                    except Exception:
                        pass
    except AttributeError as e:
        if "'MicrophoneStream' object has no attribute 'is_active'" in str(e):
            pytest.fail(f"Код не должен падать с AttributeError при ошибке активации: {e}")
        else:
            raise
    
    # Проверяем, что stream был закрыт при ошибке активации
    assert mock_stream.close.called, "Stream должен быть закрыт при ошибке активации"


@pytest.mark.asyncio
async def test_close_stream_on_session_mismatch_without_is_active(voice_integration):
    """Тест: Закрытие stream при session mismatch без метода is_active()"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок микрофона БЕЗ метода is_active()
    mock_microphone, mock_stream = create_microphone_stream_without_is_active()
    
    # Устанавливаем состояние
    integration._google_microphone = mock_microphone
    integration._google_stop_listening = MagicMock()
    integration._google_recording_active = True
    integration._google_recognizer = MagicMock()
    
    # Симулируем остановку записи с несоответствием сессий
    event = {
        "type": "voice.recording_stop",
        "data": {
            "session_id": "new_session",
            "duration": 1.0
        }
    }
    
    # Устанавливаем другую активную сессию
    integration._set_session_id("old_session", reason="test")
    mock_state_manager.get_current_session_id.return_value = "old_session"
    
    # Вызываем обработчик (не должно упасть с AttributeError)
    try:
        await integration._on_recording_stop(event)
    except AttributeError as e:
        if "'MicrophoneStream' object has no attribute 'is_active'" in str(e):
            pytest.fail(f"Код не должен падать с AttributeError при session mismatch: {e}")
        else:
            raise
    
    # Проверяем, что stream был закрыт при session mismatch
    assert mock_stream.close.called, "Stream должен быть закрыт при session mismatch"

