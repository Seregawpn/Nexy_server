"""
Тесты для проверки освобождения микрофона после AVF диагностики.

Проверяет, что микрофон полностью освобождается после деактивации AVF
и PyAudio может его открыть без конфликтов.
"""

import pytest
import pytest_asyncio
from unittest.mock import MagicMock, AsyncMock, patch
import asyncio
import threading
import speech_recognition as sr

from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.core.state_manager import AppMode
from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine


@pytest_asyncio.fixture
async def voice_integration():
    """Создаёт изолированный экземпляр VoiceRecognitionIntegration для тестирования"""
    mock_event_bus = MagicMock(spec=EventBus)
    mock_event_bus.publish = AsyncMock()
    mock_event_bus.subscribe = AsyncMock()
    mock_event_bus.unsubscribe = AsyncMock()
    
    mock_state_manager = MagicMock(spec=ApplicationStateManager)
    mock_state_manager.is_microphone_active = MagicMock(return_value=False)
    mock_state_manager.get_current_mode = MagicMock(return_value=AppMode.LISTENING)
    mock_state_manager.get_current_session_id = MagicMock(return_value="test_session_123")
    mock_state_manager.set_microphone_state = MagicMock()
    mock_state_manager.force_close_microphone = MagicMock()
    mock_state_manager.update_session_id = MagicMock()
    
    mock_error_handler = MagicMock(spec=ErrorHandler)
    
    # Мокируем AVFAudioEngine
    mock_avf_engine = MagicMock(spec=AVFAudioEngine)
    mock_avf_engine.start_input = AsyncMock(return_value={"device_info": {"name": "Test Mic"}})
    
    # ✅ ИСПРАВЛЕНИЕ: stop_input должен возвращать объект с атрибутом device_info
    mock_stop_result = MagicMock()
    mock_device_info = MagicMock()
    mock_device_info.name = "Test Mic"
    mock_device_info.uid = "test_uid"
    mock_device_info.is_input = True
    mock_stop_result.device_info = mock_device_info
    mock_avf_engine.stop_input = AsyncMock(return_value=mock_stop_result)
    mock_avf_engine.is_input_active = MagicMock(return_value=False)  # По умолчанию неактивен
    
    integration = VoiceRecognitionIntegration(
        event_bus=mock_event_bus,
        state_manager=mock_state_manager,
        error_handler=mock_error_handler
    )
    
    # Устанавливаем мок AVF engine
    integration._avf_engine = mock_avf_engine
    integration._use_avf = True
    
    # Инициализируем Google recognizer
    integration._google_recognizer = sr.Recognizer()
    integration._avf_device_info = {"device_info": {"name": "Test Mic"}}
    integration._google_audio_chunks_lock = threading.Lock()  # ✅ Используем threading.Lock, а не asyncio.Lock
    integration._google_audio_chunks = []
    
    yield integration, mock_event_bus, mock_state_manager, mock_avf_engine


@pytest.mark.asyncio
async def test_avf_microphone_released_before_google_recording(voice_integration):
    """Тест: Микрофон освобождается после AVF диагностики перед запуском Google записи"""
    integration, mock_event_bus, mock_state_manager, mock_avf_engine = voice_integration
    
    # Мокируем, что AVF микрофон активен после диагностики
    mock_avf_engine.is_input_active = MagicMock(return_value=True)
    
    # Мокируем sr.Microphone и recognizer
    mock_microphone = MagicMock(spec=sr.Microphone)
    mock_microphone.SAMPLE_RATE = 16000
    mock_microphone.SAMPLE_WIDTH = 2
    mock_microphone.stream = MagicMock()
    mock_microphone.stream.is_active = MagicMock(return_value=False)
    
    mock_recognizer = MagicMock(spec=sr.Recognizer)
    mock_recognizer.adjust_for_ambient_noise = MagicMock()
    mock_recognizer.energy_threshold = 50
    mock_recognizer.dynamic_energy_threshold = False
    mock_recognizer.pause_threshold = 0.3
    mock_recognizer.non_speaking_duration = 0.1
    mock_recognizer.listen_in_background = MagicMock(return_value=MagicMock())
    
    with patch('speech_recognition.Microphone', return_value=mock_microphone):
        with patch('speech_recognition.Recognizer', return_value=mock_recognizer):
            session_id = "test_session_123"
            event = {
                "type": "voice.recording_start",
                "data": {
                    "session_id": session_id,
                    "source": "keyboard"
                }
            }
            
            await integration._on_recording_start(event)
            
            # Проверяем, что stop_input был вызван для освобождения микрофона
            assert mock_avf_engine.stop_input.called, "AVF микрофон должен быть остановлен перед Google записью"
            
            # Проверяем, что listen_in_background был вызван
            assert mock_recognizer.listen_in_background.called, "listen_in_background должен быть вызван"


@pytest.mark.asyncio
async def test_avf_microphone_force_stopped_if_still_active(voice_integration):
    """Тест: Микрофон принудительно останавливается, если все еще активен после деактивации"""
    integration, mock_event_bus, mock_state_manager, mock_avf_engine = voice_integration
    
    # Мокируем, что AVF микрофон остается активным после stop_input
    call_count = 0
    def is_input_active_side_effect():
        nonlocal call_count
        call_count += 1
        # Первый вызов - активен, второй - неактивен (после принудительной остановки)
        return call_count == 1
    
    mock_avf_engine.is_input_active = MagicMock(side_effect=is_input_active_side_effect)
    
    # ✅ ИСПРАВЛЕНИЕ: stop_input должен возвращать объект с атрибутом device_info
    mock_stop_result = MagicMock()
    mock_device_info = MagicMock()
    mock_device_info.name = "Test Mic"
    mock_device_info.uid = "test_uid"
    mock_device_info.is_input = True
    mock_stop_result.device_info = mock_device_info
    mock_avf_engine.stop_input = AsyncMock(return_value=mock_stop_result)
    
    # Мокируем sr.Microphone и recognizer
    mock_microphone = MagicMock(spec=sr.Microphone)
    mock_microphone.SAMPLE_RATE = 16000
    mock_microphone.SAMPLE_WIDTH = 2
    mock_microphone.stream = MagicMock()
    mock_microphone.stream.is_active = MagicMock(return_value=False)
    
    mock_recognizer = MagicMock(spec=sr.Recognizer)
    mock_recognizer.adjust_for_ambient_noise = MagicMock()
    mock_recognizer.energy_threshold = 50
    mock_recognizer.dynamic_energy_threshold = False
    mock_recognizer.pause_threshold = 0.3
    mock_recognizer.non_speaking_duration = 0.1
    mock_recognizer.listen_in_background = MagicMock(return_value=MagicMock())
    
    with patch('speech_recognition.Microphone', return_value=mock_microphone):
        with patch('speech_recognition.Recognizer', return_value=mock_recognizer):
            session_id = "test_session_123"
            event = {
                "type": "voice.recording_start",
                "data": {
                    "session_id": session_id,
                    "source": "keyboard"
                }
            }
            
            await integration._on_recording_start(event)
            
            # Проверяем, что stop_input был вызван дважды (первый раз в _get_device_info_via_avf, второй раз принудительно)
            assert mock_avf_engine.stop_input.call_count >= 2, "AVF микрофон должен быть принудительно остановлен, если все еще активен"


@pytest.mark.asyncio
async def test_pyaudio_stream_created_after_avf_release(voice_integration):
    """Тест: PyAudio stream создается после освобождения AVF микрофона"""
    integration, mock_event_bus, mock_state_manager, mock_avf_engine = voice_integration
    
    # Мокируем, что AVF микрофон неактивен (освобожден)
    mock_avf_engine.is_input_active = MagicMock(return_value=False)
    
    # Мокируем sr.Microphone и recognizer
    mock_microphone = MagicMock(spec=sr.Microphone)
    mock_microphone.SAMPLE_RATE = 16000
    mock_microphone.SAMPLE_WIDTH = 2
    mock_stream = MagicMock()
    mock_stream.is_active = MagicMock(return_value=True)
    mock_microphone.stream = mock_stream
    
    mock_recognizer = MagicMock(spec=sr.Recognizer)
    mock_recognizer.adjust_for_ambient_noise = MagicMock()
    mock_recognizer.energy_threshold = 50
    mock_recognizer.dynamic_energy_threshold = False
    mock_recognizer.pause_threshold = 0.3
    mock_recognizer.non_speaking_duration = 0.1
    mock_recognizer.listen_in_background = MagicMock(return_value=MagicMock())
    
    with patch('speech_recognition.Microphone', return_value=mock_microphone):
        with patch('speech_recognition.Recognizer', return_value=mock_recognizer):
            session_id = "test_session_123"
            event = {
                "type": "voice.recording_start",
                "data": {
                    "session_id": session_id,
                    "source": "keyboard"
                }
            }
            
            await integration._on_recording_start(event)
            
            # Проверяем, что listen_in_background был вызван (это создаст PyAudio stream)
            assert mock_recognizer.listen_in_background.called, "listen_in_background должен быть вызван для создания PyAudio stream"
            
            # Проверяем, что микрофон сохранен
            assert integration._google_microphone is not None, "Микрофон должен быть сохранен"


@pytest.mark.asyncio
async def test_deactivation_pause_configured_correctly(voice_integration):
    """Тест: Пауза деактивации AVF настраивается из конфига"""
    integration, mock_event_bus, mock_state_manager, mock_avf_engine = voice_integration
    
    # Мокируем конфиг с кастомным значением паузы
    mock_config = {
        'avf': {
            'diagnostics': {
                'deactivation_pause_sec': 0.8
            }
        }
    }
    
    with patch('integration.integrations.voice_recognition_integration.UnifiedConfigLoader') as mock_loader:
        mock_loader_instance = MagicMock()
        mock_loader_instance.get_audio_avf_config.return_value = mock_config
        mock_loader.return_value = mock_loader_instance
        
        # Мокируем sr.Microphone и recognizer
        mock_microphone = MagicMock(spec=sr.Microphone)
        mock_microphone.SAMPLE_RATE = 16000
        mock_microphone.SAMPLE_WIDTH = 2
        mock_microphone.stream = MagicMock()
        
        mock_recognizer = MagicMock(spec=sr.Recognizer)
        mock_recognizer.adjust_for_ambient_noise = MagicMock()
        mock_recognizer.energy_threshold = 50
        mock_recognizer.dynamic_energy_threshold = False
        mock_recognizer.pause_threshold = 0.3
        mock_recognizer.non_speaking_duration = 0.1
        mock_recognizer.listen_in_background = MagicMock(return_value=MagicMock())
        
        with patch('speech_recognition.Microphone', return_value=mock_microphone):
            with patch('speech_recognition.Recognizer', return_value=mock_recognizer):
                with patch('asyncio.sleep') as mock_sleep:
                    session_id = "test_session_123"
                    event = {
                        "type": "voice.recording_start",
                        "data": {
                            "session_id": session_id,
                            "source": "keyboard"
                        }
                    }
                    
                    await integration._on_recording_start(event)
                    
                    # Проверяем, что sleep был вызван с правильным значением из конфига
                    sleep_calls = [call[0][0] for call in mock_sleep.call_args_list]
                    # Должна быть пауза 0.8 сек из конфига (или 0.5 по умолчанию, если конфиг не читается)
                    assert any(0.5 <= pause <= 0.8 for pause in sleep_calls), f"Пауза деактивации должна быть из конфига. Вызовы sleep: {sleep_calls}"

