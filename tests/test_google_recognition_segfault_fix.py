"""
Изолированный тест для проверки исправления segmentation fault в Google Speech Recognition.

Проверяет, что recognize_google запускается в отдельном потоке через run_in_executor,
что предотвращает конфликты с gRPC потоками и segmentation fault.
"""

import pytest
import pytest_asyncio
from unittest.mock import MagicMock, AsyncMock, patch
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
    integration._google_audio_chunks_lock = threading.Lock()  # ✅ Используем threading.Lock, как в реальном коде
    integration._google_audio_chunks = []
    
    return integration, mock_event_bus, mock_state_manager


def create_mock_audio_data(sample_rate=16000, duration_sec=1.0):
    """Создаёт мок AudioData для тестирования"""
    import struct
    # Генерируем простой синусоидальный сигнал
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
async def test_recognize_google_runs_in_executor(voice_integration):
    """Тест: recognize_google запускается в отдельном потоке через run_in_executor"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок AudioData
    audio_data = create_mock_audio_data(sample_rate=16000, duration_sec=0.5)
    session_id = "test_session_123"
    
    # Мокируем recognize_google чтобы не делать реальный запрос к Google API
    original_recognize = integration._google_recognizer.recognize_google
    
    def mock_recognize_google(audio, language=None):
        """Мок recognize_google, который симулирует успешное распознавание"""
        return "test recognition result"
    
    integration._google_recognizer.recognize_google = mock_recognize_google
    
    # Проверяем, что run_in_executor вызывается
    with patch('asyncio.get_event_loop') as mock_get_loop:
        mock_loop = MagicMock()
        mock_loop.run_in_executor = AsyncMock(return_value="test recognition result")
        mock_get_loop.return_value = mock_loop
        
        # Вызываем метод распознавания
        await integration._recognize_google_audio(audio_data, session_id)
        
        # Проверяем, что run_in_executor был вызван
        assert mock_loop.run_in_executor.called, "run_in_executor должен быть вызван для изоляции recognize_google"
        
        # Проверяем, что событие успешного распознавания было опубликовано
        published_events = [
            (event_type, payload)
            for event_type, payload in [
                (call[0][0], call[0][1])
                for call in mock_event_bus.publish.call_args_list
            ]
            if event_type == "voice.recognition_completed"
        ]
        assert len(published_events) > 0, "voice.recognition_completed должен быть опубликован"
        
        # Восстанавливаем оригинальный метод
        integration._google_recognizer.recognize_google = original_recognize


@pytest.mark.asyncio
async def test_recognize_google_timeout_handling(voice_integration):
    """Тест: таймаут распознавания обрабатывается корректно"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок AudioData
    audio_data = create_mock_audio_data(sample_rate=16000, duration_sec=0.5)
    session_id = "test_session_123"
    
    # Мокируем recognize_google чтобы он зависал (симулируем таймаут)
    def mock_recognize_google_slow(audio, language=None):
        """Мок recognize_google, который зависает"""
        import time
        time.sleep(35)  # Больше таймаута (30 секунд)
        return "test recognition result"
    
    integration._google_recognizer.recognize_google = mock_recognize_google_slow
    
    # Мокируем asyncio.wait_for чтобы симулировать таймаут
    with patch('asyncio.wait_for') as mock_wait_for:
        mock_wait_for.side_effect = asyncio.TimeoutError()
        
        # Вызываем метод распознавания
        await integration._recognize_google_audio(audio_data, session_id)
        
        # Проверяем, что событие ошибки таймаута было опубликовано
        published_events = [
            (event_type, payload)
            for event_type, payload in [
                (call[0][0], call[0][1])
                for call in mock_event_bus.publish.call_args_list
            ]
            if event_type == "voice.recognition_failed"
        ]
        assert len(published_events) > 0, "voice.recognition_failed должен быть опубликован при таймауте"
        
        # Проверяем, что ошибка содержит информацию о таймауте
        failed_event = published_events[0][1]
        assert "timeout" in failed_event.get("error", "").lower(), "Ошибка должна содержать информацию о таймауте"


@pytest.mark.asyncio
async def test_recognize_google_empty_audio_handling(voice_integration):
    """Тест: пустые аудио данные обрабатываются корректно"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок AudioData с пустыми данными
    empty_audio_data = sr.AudioData(b'', 16000, 2)
    session_id = "test_session_123"
    
    # Вызываем метод распознавания
    await integration._recognize_google_audio(empty_audio_data, session_id)
    
    # Проверяем, что событие ошибки было опубликовано
    published_events = [
        (event_type, payload)
        for event_type, payload in [
            (call[0][0], call[0][1])
            for call in mock_event_bus.publish.call_args_list
        ]
        if event_type == "voice.recognition_failed"
    ]
    assert len(published_events) > 0, "voice.recognition_failed должен быть опубликован для пустых данных"
    
    # Проверяем, что ошибка содержит информацию о пустых данных
    failed_event = published_events[0][1]
    assert "empty" in failed_event.get("error", "").lower(), "Ошибка должна содержать информацию о пустых данных"


@pytest.mark.asyncio
async def test_recognize_google_executor_error_handling(voice_integration):
    """Тест: ошибки в executor обрабатываются корректно (включая segmentation fault)"""
    integration, mock_event_bus, mock_state_manager = voice_integration
    
    # Создаём мок AudioData
    audio_data = create_mock_audio_data(sample_rate=16000, duration_sec=0.5)
    session_id = "test_session_123"
    
    # Мокируем recognize_google чтобы он вызывал ошибку
    def mock_recognize_google_error(audio, language=None):
        """Мок recognize_google, который вызывает ошибку"""
        raise RuntimeError("Simulated segmentation fault or other error")
    
    integration._google_recognizer.recognize_google = mock_recognize_google_error
    
    # Мокируем run_in_executor чтобы он возвращал ошибку
    with patch('asyncio.get_event_loop') as mock_get_loop:
        mock_loop = MagicMock()
        mock_loop.run_in_executor = AsyncMock(side_effect=RuntimeError("Simulated segmentation fault"))
        mock_get_loop.return_value = mock_loop
        
        # Вызываем метод распознавания
        await integration._recognize_google_audio(audio_data, session_id)
        
        # Проверяем, что событие ошибки было опубликовано
        published_events = [
            (event_type, payload)
            for event_type, payload in [
                (call[0][0], call[0][1])
                for call in mock_event_bus.publish.call_args_list
            ]
            if event_type == "voice.recognition_failed"
        ]
        assert len(published_events) > 0, "voice.recognition_failed должен быть опубликован при ошибке executor"
        
        # Проверяем, что ошибка содержит информацию об executor error
        failed_event = published_events[0][1]
        assert "executor" in failed_event.get("error", "").lower() or "error" in failed_event.get("error", "").lower(), "Ошибка должна содержать информацию об executor error"

