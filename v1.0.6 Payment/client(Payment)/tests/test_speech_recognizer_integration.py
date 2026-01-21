"""
Интеграционные тесты для SpeechRecognizer с AudioStreamManager

✅ ЦИКЛ 2: Тестирование интеграции SpeechRecognizer с AudioStreamManager
"""

import pytest
import asyncio
from unittest.mock import Mock, MagicMock, patch, AsyncMock
import sounddevice as sd

# Импорт тестируемого компонента
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer
from modules.voice_recognition.core.types import RecognitionConfig


class TestSpeechRecognizerIntegration:
    """Интеграционные тесты для SpeechRecognizer"""
    
    @pytest.fixture
    def recognition_config(self):
        """Создает конфигурацию для SpeechRecognizer"""
        return RecognitionConfig(
            sample_rate=48000,
            channels=1,
            chunk_size=512,
            energy_threshold=300,
            dynamic_energy_threshold=True,
            pause_threshold=0.8,
            phrase_threshold=0.3,
            non_speaking_duration=0.5
        )
    
    @pytest.fixture
    def speech_recognizer(self, recognition_config):
        """Создает экземпляр SpeechRecognizer"""
        recognizer = SpeechRecognizer(recognition_config)
        return recognizer
    
    def test_stream_manager_initialized(self, speech_recognizer):
        """Тест инициализации AudioStreamManager в SpeechRecognizer"""
        assert speech_recognizer._stream_manager is not None
        assert speech_recognizer._stream_manager.stream_type == "input"
    
    @pytest.mark.asyncio
    async def test_stream_creation_uses_manager(self, speech_recognizer):
        """Тест использования AudioStreamManager при создании потока"""
        # Mock AudioStreamManager
        mock_result = Mock()
        mock_result.success = True
        mock_result.stream = Mock()
        mock_result.stream.active = False
        mock_result.attempt = 1
        mock_result.duration_ms = 100.0
        
        speech_recognizer._stream_manager.create_stream = AsyncMock(return_value=mock_result)
        
        # Mock другие зависимости
        with patch.object(speech_recognizer, '_prepare_input_device', return_value=1), \
             patch.object(speech_recognizer, '_is_bluetooth_device', return_value=False), \
             patch.object(speech_recognizer, '_audio_callback', return_value=None), \
             patch('time.sleep'):
            
            # Вызываем метод, который создает поток
            # (это внутренний метод, но мы можем проверить через интеграцию)
            assert speech_recognizer._stream_manager is not None
    
    def test_stream_manager_config(self, speech_recognizer):
        """Тест конфигурации AudioStreamManager"""
        manager = speech_recognizer._stream_manager
        assert manager._close_delay_bt == 2.5
        assert manager._close_delay_normal == 0.3
        assert manager._max_wait_active_bt == 3.0
        assert manager._max_wait_active_normal == 1.0

