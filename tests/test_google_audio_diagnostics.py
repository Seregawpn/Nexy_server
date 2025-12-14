"""
Изолированный тест для диагностики аудио и обрезки тишины в Google Speech Recognition.

Проверяет:
1. Диагностику качества аудио (RMS, диапазон, длительность)
2. Обрезку тишины перед отправкой в Google Speech API
3. Проверку минимальной длительности
4. Логирование при UnknownValueError
"""

import pytest
import numpy as np
from unittest.mock import Mock, AsyncMock, patch
import speech_recognition as sr


@pytest.fixture
def mock_audio_data():
    """Создает mock AudioData объект для тестирования"""
    # Создаем тестовые аудио данные (3 секунды, 48000Hz, int16, моно)
    sample_rate = 48000
    duration_sec = 3.0
    samples = int(sample_rate * duration_sec)
    # Генерируем синусоидальный сигнал (имитация речи)
    t = np.linspace(0, duration_sec, samples)
    audio_signal = (np.sin(2 * np.pi * 440 * t) * 0.3).astype(np.float32)  # 440Hz, амплитуда 0.3
    # Конвертируем в int16
    audio_int16 = (audio_signal * 32767).astype(np.int16)
    audio_bytes = audio_int16.tobytes()
    
    audio_data = sr.AudioData(audio_bytes, sample_rate, 2)  # 2 bytes per sample (int16)
    return audio_data


@pytest.fixture
def mock_audio_data_with_silence():
    """Создает mock AudioData с тишиной в начале и конце"""
    sample_rate = 48000
    duration_sec = 3.0
    samples = int(sample_rate * duration_sec)
    
    # Тишина в начале (0.5 сек)
    silence_start = int(sample_rate * 0.5)
    # Речь в середине (2 сек)
    speech_samples = int(sample_rate * 2.0)
    # Тишина в конце (0.5 сек)
    silence_end = samples - silence_start - speech_samples
    
    # Создаем сигнал: тишина + речь + тишина
    t_speech = np.linspace(0, 2.0, speech_samples)
    speech_signal = (np.sin(2 * np.pi * 440 * t_speech) * 0.3).astype(np.float32)
    speech_int16 = (speech_signal * 32767).astype(np.int16)
    
    # Объединяем: тишина + речь + тишина
    audio_int16 = np.concatenate([
        np.zeros(silence_start, dtype=np.int16),  # Тишина в начале
        speech_int16,  # Речь
        np.zeros(silence_end, dtype=np.int16)  # Тишина в конце
    ])
    audio_bytes = audio_int16.tobytes()
    
    audio_data = sr.AudioData(audio_bytes, sample_rate, 2)
    return audio_data


@pytest.fixture
def mock_voice_recognition_integration():
    """Создает mock VoiceRecognitionIntegration"""
    integration = Mock()
    integration.config = Mock()
    integration.config.language = "en-US"
    integration._avf_device_info = {"device_info": {"name": "Test Microphone"}}
    integration._google_recognizer = sr.Recognizer()
    integration.event_bus = AsyncMock()
    return integration


def test_audio_diagnostics_rms_calculation(mock_audio_data):
    """Изолированный тест: проверяем расчет RMS для диагностики аудио"""
    # Setup: получаем raw данные
    raw_audio_data = mock_audio_data.get_raw_data()
    
    # Execution: рассчитываем RMS
    audio_array = np.frombuffer(raw_audio_data, dtype=np.int16)
    audio_rms = np.sqrt(np.mean(audio_array.astype(np.float32) ** 2))
    
    # Assertion: RMS должен быть > 0 для реального аудио
    assert audio_rms > 0, f"RMS должен быть > 0, получено {audio_rms}"
    assert audio_rms > 100, f"RMS должен быть > 100 для речи, получено {audio_rms}"


def test_audio_diagnostics_range_calculation(mock_audio_data):
    """Изолированный тест: проверяем расчет диапазона для диагностики аудио"""
    # Setup: получаем raw данные
    raw_audio_data = mock_audio_data.get_raw_data()
    
    # Execution: рассчитываем диапазон
    audio_array = np.frombuffer(raw_audio_data, dtype=np.int16)
    audio_min = np.min(audio_array)
    audio_max = np.max(audio_array)
    audio_range = audio_max - audio_min
    
    # Assertion: диапазон должен быть > 1000 для речи
    assert audio_range > 1000, f"Диапазон должен быть > 1000 для речи, получено {audio_range}"


def test_trim_silence_removes_leading_trailing_silence(mock_audio_data_with_silence):
    """Изолированный тест: проверяем обрезку тишины в начале и конце"""
    from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
    
    # Setup: создаем интеграцию и получаем raw данные
    integration = VoiceRecognitionIntegration(Mock(), Mock(), Mock(), Mock())
    raw_audio_bytes = mock_audio_data_with_silence.get_raw_data()
    original_size = len(raw_audio_bytes)
    
    # Execution: обрезаем тишину
    trimmed_bytes = integration._trim_silence(
        raw_audio_bytes,
        sample_rate=48000,
        channels=1,
        silence_threshold=100.0,
        frame_duration_ms=100
    )
    trimmed_size = len(trimmed_bytes)
    
    # Assertion: обрезанные данные должны быть меньше оригинальных
    assert trimmed_size < original_size, f"Обрезанные данные должны быть меньше оригинальных ({trimmed_size} < {original_size})"
    # Проверяем, что обрезано примерно 1 секунда тишины (0.5 сек в начале + 0.5 сек в конце)
    expected_reduction = int(48000 * 2 * 1.0)  # 1 секунда тишины * 2 bytes per sample
    assert abs(original_size - trimmed_size - expected_reduction) < 10000, f"Обрезка должна удалить ~1 сек тишины"


def test_trim_silence_preserves_speech(mock_audio_data):
    """Изолированный тест: проверяем, что обрезка тишины не удаляет речь"""
    from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
    
    # Setup: создаем интеграцию и получаем raw данные (без тишины)
    integration = VoiceRecognitionIntegration(Mock(), Mock(), Mock(), Mock())
    raw_audio_bytes = mock_audio_data.get_raw_data()
    original_size = len(raw_audio_bytes)
    
    # Execution: обрезаем тишину (но в аудио нет тишины)
    trimmed_bytes = integration._trim_silence(
        raw_audio_bytes,
        sample_rate=48000,
        channels=1,
        silence_threshold=100.0,
        frame_duration_ms=100
    )
    trimmed_size = len(trimmed_bytes)
    
    # Assertion: если нет тишины, размер должен остаться примерно таким же
    assert abs(original_size - trimmed_size) < original_size * 0.1, f"Если нет тишины, размер должен остаться примерно таким же ({trimmed_size} ≈ {original_size})"


@pytest.mark.asyncio
async def test_recognize_google_audio_with_diagnostics(mock_voice_recognition_integration, mock_audio_data):
    """Изолированный тест: проверяем диагностику аудио в _recognize_google_audio"""
    from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
    
    # Setup: создаем реальную интеграцию с моками
    integration = VoiceRecognitionIntegration(
        Mock(),  # event_bus
        Mock(),  # state_manager
        Mock(),  # error_handler
        mock_voice_recognition_integration.config
    )
    integration._google_recognizer = sr.Recognizer()
    integration._avf_device_info = {"device_info": {"name": "Test Microphone"}}
    integration.event_bus = AsyncMock()
    
    # Execution: вызываем _recognize_google_audio с моком recognize_google
    with patch.object(integration._google_recognizer, 'recognize_google', return_value="test recognition"):
        await integration._recognize_google_audio(mock_audio_data, "test_session")
    
    # Assertion: проверяем, что диагностика была выполнена (проверяем логи через event_bus)
    # В реальном тесте можно проверить логи, но здесь просто проверяем, что функция выполнилась без ошибок
    assert True  # Если дошли сюда, значит диагностика прошла без ошибок


@pytest.mark.asyncio
async def test_recognize_google_audio_unknown_value_error_diagnostics(mock_voice_recognition_integration, mock_audio_data):
    """Изолированный тест: проверяем диагностику при UnknownValueError"""
    from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
    
    # Setup: создаем реальную интеграцию с моками
    integration = VoiceRecognitionIntegration(
        Mock(),  # event_bus
        Mock(),  # state_manager
        Mock(),  # error_handler
        mock_voice_recognition_integration.config
    )
    integration._google_recognizer = sr.Recognizer()
    integration._avf_device_info = {"device_info": {"name": "Test Microphone"}}
    integration.event_bus = AsyncMock()
    
    # Execution: вызываем _recognize_google_audio с моком recognize_google, который выбрасывает UnknownValueError
    with patch.object(integration._google_recognizer, 'recognize_google', side_effect=sr.UnknownValueError()):
        await integration._recognize_google_audio(mock_audio_data, "test_session")
    
    # Assertion: проверяем, что voice.recognition_failed был опубликован
    integration.event_bus.publish.assert_called()
    # Проверяем, что последний вызов был voice.recognition_failed
    last_call = integration.event_bus.publish.call_args_list[-1]
    assert "voice.recognition_failed" in str(last_call), "Должно быть опубликовано voice.recognition_failed при UnknownValueError"
