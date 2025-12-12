"""
Изолированный тест для проверки активации callback в Google Speech Recognition.

Проверяет, что callback вызывается при использовании listen_in_background
и что настройки energy_threshold и pause_threshold корректны.
"""

import pytest
import pytest_asyncio
from unittest.mock import MagicMock, AsyncMock, patch, call
import asyncio
import threading
import speech_recognition as sr


@pytest_asyncio.fixture
async def voice_integration():
    """Создаёт изолированный экземпляр VoiceRecognitionIntegration для тестирования"""
    mock_event_bus = MagicMock(spec=type('EventBus', (), {}))
    mock_event_bus.publish = AsyncMock()
    mock_event_bus.subscribe = AsyncMock()
    mock_event_bus.unsubscribe = AsyncMock()
    
    mock_state_manager = MagicMock(spec=type('StateManager', (), {}))
    mock_state_manager.is_microphone_active = MagicMock(return_value=False)
    mock_state_manager.set_microphone_state = MagicMock(return_value=True)
    mock_state_manager.force_close_microphone = MagicMock(return_value=True)
    mock_state_manager.get_current_session_id = MagicMock(return_value="test_session")
    mock_state_manager.update_session_id = MagicMock(return_value=None)  # ✅ Добавляем недостающий метод
    
    mock_error_handler = MagicMock(spec=type('ErrorHandler', (), {}))
    mock_error_handler.handle_error = AsyncMock()
    
    from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
    
    integration = VoiceRecognitionIntegration(
        event_bus=mock_event_bus,
        state_manager=mock_state_manager,
        error_handler=mock_error_handler
    )
    
    # Инициализируем Google recognizer
    integration._google_recognizer = sr.Recognizer()
    integration._avf_device_info = {"device_info": {"name": "Test Mic"}}
    integration._google_audio_chunks_lock = threading.Lock()
    integration._google_audio_chunks = []
    integration._google_chunk_event = threading.Event()
    integration._google_recording_active = False
    integration._use_avf = True
    
    return integration, mock_event_bus, mock_state_manager


def create_mock_audio_data(sample_rate=16000, duration_sec=0.5):
    """Создаёт мок AudioData для тестирования"""
    import struct
    import math
    sample_width = 2  # 16-bit
    num_samples = int(sample_rate * duration_sec)
    audio_bytes = b''
    for i in range(num_samples):
        # Простая синусоида на 440Hz
        value = int(32767 * 0.3 * math.sin(2 * math.pi * 440 * i / sample_rate))
        audio_bytes += struct.pack('<h', value)
    
    audio_data = sr.AudioData(audio_bytes, sample_rate, sample_width)
    return audio_data


@pytest.mark.asyncio
async def test_energy_threshold_lowered_for_callback(voice_integration):
    """Тест: energy_threshold снижается для гарантированного вызова callback"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок микрофона и recognizer
    mock_microphone = MagicMock(spec=sr.Microphone)
    mock_microphone.SAMPLE_RATE = 16000
    mock_microphone.SAMPLE_WIDTH = 2
    
    # Мокируем adjust_for_ambient_noise
    original_adjust = integration._google_recognizer.adjust_for_ambient_noise
    integration._google_recognizer.adjust_for_ambient_noise = MagicMock()
    
    # Устанавливаем начальный порог
    integration._google_recognizer.energy_threshold = 300
    
    # Мокируем listen_in_background
    mock_stop_listening = MagicMock()
    integration._google_recognizer.listen_in_background = MagicMock(return_value=mock_stop_listening)
    
    # Симулируем активацию микрофона
    session_id = "test_session_123"
    event = {
        "type": "voice.recording_start",
        "data": {
            "session_id": session_id,
            "source": "keyboard"
        }
    }
    
    # ✅ КРИТИЧНО: Мокируем AVF engine для использования новой логики
    mock_avf_engine = MagicMock()
    mock_avf_engine.start_input = AsyncMock(return_value={"device_info": {"name": "Test Mic"}})
    integration._avf_engine = mock_avf_engine
    integration._use_avf = True
    
    # Вызываем обработчик активации
    await integration._on_recording_start(event)
    
    # Проверяем, что energy_threshold был снижен
    assert integration._google_recognizer.energy_threshold <= 150, f"energy_threshold должен быть снижен (текущий: {integration._google_recognizer.energy_threshold})"
    
    # Проверяем, что dynamic_energy_threshold установлен в False
    assert integration._google_recognizer.dynamic_energy_threshold == False, "dynamic_energy_threshold должен быть False"
    
    # Проверяем, что pause_threshold установлен в правильное значение (0.3 для частых callback'ов)
    assert integration._google_recognizer.pause_threshold == 0.3, f"pause_threshold должен быть 0.3 (текущий: {integration._google_recognizer.pause_threshold})"
    
    # Проверяем, что non_speaking_duration установлен в минимальное значение
    assert integration._google_recognizer.non_speaking_duration == 0.1, f"non_speaking_duration должен быть 0.1 (текущий: {integration._google_recognizer.non_speaking_duration})"
    
    # Восстанавливаем оригинальный метод
    integration._google_recognizer.adjust_for_ambient_noise = original_adjust


@pytest.mark.asyncio
async def test_callback_receives_audio_data(voice_integration):
    """Тест: callback получает и обрабатывает аудио данные"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок микрофона
    mock_microphone = MagicMock(spec=sr.Microphone)
    mock_microphone.SAMPLE_RATE = 16000
    mock_microphone.SAMPLE_WIDTH = 2
    
    # Создаём реальный AudioData для тестирования
    audio_data = create_mock_audio_data(sample_rate=16000, duration_sec=0.5)
    
    # Мокируем listen_in_background чтобы захватить callback
    captured_callback = None
    
    def capture_listen_in_background(mic, cb):
        nonlocal captured_callback
        captured_callback = cb
        return MagicMock()  # mock stop_listening
    
    # ✅ КРИТИЧНО: Мокируем создание sr.Microphone() и sr.Recognizer()
    with patch('speech_recognition.Microphone', return_value=mock_microphone):
        with patch('speech_recognition.Recognizer') as mock_recognizer_class:
            # Создаём мок recognizer (без spec, чтобы избежать InvalidSpecError)
            mock_recognizer = MagicMock()
            mock_recognizer.listen_in_background = capture_listen_in_background
            mock_recognizer.adjust_for_ambient_noise = MagicMock()
            mock_recognizer.energy_threshold = 50
            mock_recognizer.dynamic_energy_threshold = False
            mock_recognizer.pause_threshold = 0.3
            mock_recognizer.non_speaking_duration = 0.1
            mock_recognizer_class.return_value = mock_recognizer
            
            # Симулируем активацию микрофона
            session_id = "test_session_123"
            event = {
                "type": "voice.recording_start",
                "data": {
                    "session_id": session_id,
                    "source": "keyboard"
                }
            }
            
            # ✅ КРИТИЧНО: Мокируем AVF engine для использования новой логики
            mock_avf_engine = MagicMock()
            mock_avf_engine.start_input = AsyncMock(return_value={"device_info": {"name": "Test Mic"}})
            integration._avf_engine = mock_avf_engine
            integration._use_avf = True
            
            # Вызываем обработчик активации
            await integration._on_recording_start(event)
    
            # Проверяем, что callback был захвачен
            assert captured_callback is not None, "Callback должен быть захвачен из listen_in_background"
            
            # Вызываем callback с тестовыми данными
            integration._google_recording_active = True
            integration._google_stop_listening = MagicMock()  # Устанавливаем stop_listening для проверки в callback
            
            # Вызываем callback
            captured_callback(mock_recognizer, audio_data)
            
            # Проверяем, что аудио данные были добавлены в список
            assert len(integration._google_audio_chunks) > 0, "Аудио данные должны быть добавлены в список"
            assert integration._google_chunk_event.is_set(), "Событие _google_chunk_event должно быть установлено"


@pytest.mark.asyncio
async def test_callback_ignored_when_recording_inactive(voice_integration):
    """Тест: callback игнорируется, когда запись неактивна"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок микрофона
    mock_microphone = MagicMock(spec=sr.Microphone)
    mock_microphone.SAMPLE_RATE = 16000
    mock_microphone.SAMPLE_WIDTH = 2
    
    # Создаём реальный AudioData для тестирования
    audio_data = create_mock_audio_data(sample_rate=16000, duration_sec=0.5)
    
    # Мокируем listen_in_background чтобы захватить callback
    captured_callback = None
    
    def capture_listen_in_background(mic, cb):
        nonlocal captured_callback
        captured_callback = cb
        return MagicMock()  # mock stop_listening
    
    # ✅ КРИТИЧНО: Мокируем создание sr.Microphone() и sr.Recognizer()
    with patch('speech_recognition.Microphone', return_value=mock_microphone):
        with patch('speech_recognition.Recognizer') as mock_recognizer_class:
            # Создаём мок recognizer (без spec, чтобы избежать InvalidSpecError)
            mock_recognizer = MagicMock()
            mock_recognizer.listen_in_background = capture_listen_in_background
            mock_recognizer.adjust_for_ambient_noise = MagicMock()
            mock_recognizer.energy_threshold = 50
            mock_recognizer.dynamic_energy_threshold = False
            mock_recognizer.pause_threshold = 0.3
            mock_recognizer.non_speaking_duration = 0.1
            mock_recognizer_class.return_value = mock_recognizer
            
            # Симулируем активацию микрофона
            session_id = "test_session_123"
            event = {
                "type": "voice.recording_start",
                "data": {
                    "session_id": session_id,
                    "source": "keyboard"
                }
            }
            
            # ✅ КРИТИЧНО: Мокируем AVF engine для использования новой логики
            mock_avf_engine = MagicMock()
            mock_avf_engine.start_input = AsyncMock(return_value={"device_info": {"name": "Test Mic"}})
            integration._avf_engine = mock_avf_engine
            integration._use_avf = True
            
            # Вызываем обработчик активации
            await integration._on_recording_start(event)
            
            # Проверяем, что callback был захвачен
            assert captured_callback is not None, "Callback должен быть захвачен из listen_in_background"
            
            # Устанавливаем флаг неактивности
            integration._google_recording_active = False
            integration._google_stop_listening = None  # Устанавливаем stop_listening в None
            
            # Очищаем список чанков
            with integration._google_audio_chunks_lock:
                integration._google_audio_chunks = []
            
            # Вызываем callback (должен быть проигнорирован)
            captured_callback(mock_recognizer, audio_data)
            
            # Проверяем, что аудио данные НЕ были добавлены в список
            assert len(integration._google_audio_chunks) == 0, "Аудио данные НЕ должны быть добавлены, когда запись неактивна"


@pytest.mark.asyncio
async def test_energy_threshold_fallback_on_error(voice_integration):
    """Тест: energy_threshold устанавливается в fallback значение при ошибке настройки"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок микрофона
    mock_microphone = MagicMock(spec=sr.Microphone)
    mock_microphone.SAMPLE_RATE = 16000
    mock_microphone.SAMPLE_WIDTH = 2
    
    # Мокируем adjust_for_ambient_noise чтобы вызвать ошибку
    integration._google_recognizer.adjust_for_ambient_noise = MagicMock(side_effect=Exception("Test error"))
    
    # Устанавливаем начальный порог
    integration._google_recognizer.energy_threshold = 300
    
    # Мокируем listen_in_background
    mock_stop_listening = MagicMock()
    integration._google_recognizer.listen_in_background = MagicMock(return_value=mock_stop_listening)
    
    # Симулируем активацию микрофона
    session_id = "test_session_123"
    event = {
        "type": "voice.recording_start",
        "data": {
            "session_id": session_id,
            "source": "keyboard"
        }
    }
    
    # ✅ КРИТИЧНО: Мокируем AVF engine для использования новой логики
    mock_avf_engine = MagicMock()
    mock_avf_engine.start_input = AsyncMock(return_value={"device_info": {"name": "Test Mic"}})
    integration._avf_engine = mock_avf_engine
    integration._use_avf = True
    
    # Вызываем обработчик активации
    await integration._on_recording_start(event)
    
    # Проверяем, что energy_threshold был установлен в fallback значение
    assert integration._google_recognizer.energy_threshold == 50, f"energy_threshold должен быть установлен в 50 при ошибке (текущий: {integration._google_recognizer.energy_threshold})"

