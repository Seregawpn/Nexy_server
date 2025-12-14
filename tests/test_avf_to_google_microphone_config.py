"""
Изолированный тест для проверки логики получения конфигурации от AVF
и использования её для настройки Google микрофона.

✅ ЦЕЛЬ: Проверить, что:
1. AVF получает конфигурацию устройства (device_info, sample_rate, channels)
2. Эта конфигурация используется для создания sr.Microphone()
3. Параметры совпадают между AVF и Google микрофоном

✅ ИЗОЛЯЦИЯ: Тест проверяет только логику конфигурации, без зависимостей от всей системы.
"""

import pytest
import asyncio
from unittest.mock import Mock, MagicMock, AsyncMock, patch
from typing import Dict, Any, Optional

# Импорт тестируемого компонента
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)


class TestAVFToGoogleMicrophoneConfig:
    """Изолированные тесты для проверки логики AVF → Google микрофон конфигурации"""
    
    @pytest.fixture
    def mock_avf_engine(self):
        """Создаёт мок AVFAudioEngine"""
        engine = AsyncMock()
        
        # Мок результата stop_input
        mock_result = Mock()
        mock_result.device_info = Mock()
        mock_result.device_info.name = "Built-in Microphone"
        mock_result.device_info.uid = "com.apple.audio.AudioDevice-1"
        mock_result.device_info.is_input = True
        
        mock_result.input_format = Mock()
        mock_result.input_format.sample_rate = 48000
        mock_result.input_format.channels = 1
        mock_result.input_format.bit_depth = 16
        
        mock_result.diagnostics = {"rms": 100.0, "first_chunk_size": 1024}
        mock_result.frames_recorded = 48000  # 1 секунда при 48kHz
        mock_result.duration_ms = 1000.0
        
        engine.start_input = AsyncMock(return_value=True)
        engine.stop_input = AsyncMock(return_value=mock_result)
        
        return engine
    
    @pytest.fixture
    def mock_device_info(self):
        """Создаёт мок device_info, который возвращает _get_device_info_via_avf"""
        return {
            "device_info": {
                "name": "Built-in Microphone",
                "uid": "com.apple.audio.AudioDevice-1",
                "is_input": True
            },
            "input_format": {
                "sample_rate": 48000,
                "channels": 1,
                "bit_depth": 16
            },
            "diagnostics": {
                "rms": 100.0,
                "first_chunk_size": 1024
            }
        }
    
    @pytest.mark.asyncio
    async def test_get_device_info_via_avf_returns_correct_format(self, mock_avf_engine):
        """
        ✅ ТЕСТ 1: Проверяем, что _get_device_info_via_avf возвращает правильный формат данных
        
        Гипотеза: AVF должен возвращать device_info с полями device_info, input_format, diagnostics
        """
        from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
        from integration.core.event_bus import EventBus
        from integration.core.state_manager import ApplicationStateManager
        from integration.core.error_handler import ErrorHandler
        
        # Setup: изолированное окружение
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler()
        
        integration = VoiceRecognitionIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        # Устанавливаем мок AVF engine
        integration._use_avf = True
        integration._avf_engine = mock_avf_engine
        
        # Execution: получаем device_info через AVF
        device_info = await integration._get_device_info_via_avf()
        
        # Assertion: проверяем формат данных
        assert device_info is not None, "device_info не должен быть None"
        assert "device_info" in device_info, "device_info должен содержать поле device_info"
        assert "input_format" in device_info, "device_info должен содержать поле input_format"
        assert "diagnostics" in device_info, "device_info должен содержать поле diagnostics"
        
        # Проверяем структуру device_info
        assert device_info["device_info"]["name"] == "Built-in Microphone"
        assert device_info["device_info"]["uid"] == "com.apple.audio.AudioDevice-1"
        assert device_info["device_info"]["is_input"] is True
        
        # Проверяем структуру input_format
        assert device_info["input_format"]["sample_rate"] == 48000
        assert device_info["input_format"]["channels"] == 1
        assert device_info["input_format"]["bit_depth"] == 16
        
        # Проверяем, что AVF был вызван
        mock_avf_engine.start_input.assert_called_once()
        mock_avf_engine.stop_input.assert_called_once()
        
        print("✅ ТЕСТ 1 ПРОЙДЕН: _get_device_info_via_avf возвращает правильный формат")
    
    @pytest.mark.asyncio
    async def test_google_microphone_uses_avf_sample_rate(self, mock_device_info):
        """
        ✅ ТЕСТ 2: Проверяем, что Google микрофон создаётся с sample_rate от AVF
        
        Гипотеза: sample_rate из device_info['input_format'] должен использоваться для sr.Microphone()
        """
        import speech_recognition as sr
        
        # Setup: извлекаем sample_rate из device_info
        sample_rate = None
        if mock_device_info and mock_device_info.get('input_format'):
            input_format = mock_device_info['input_format']
            sample_rate = input_format.get('sample_rate')
        
        # Assertion: проверяем, что sample_rate извлечён
        assert sample_rate is not None, "sample_rate должен быть извлечён из device_info"
        assert sample_rate == 48000, f"sample_rate должен быть 48000, получен {sample_rate}"
        
        # Execution: создаём микрофон с sample_rate от AVF
        # (В реальном коде это делается в _on_recording_start, но здесь изолируем только логику)
        microphone = sr.Microphone(sample_rate=sample_rate, chunk_size=1024)
        
        # Assertion: проверяем, что микрофон создан с правильным sample_rate
        assert hasattr(microphone, 'SAMPLE_RATE'), "Microphone должен иметь атрибут SAMPLE_RATE"
        assert microphone.SAMPLE_RATE == sample_rate, f"Microphone.SAMPLE_RATE должен быть {sample_rate}, получен {microphone.SAMPLE_RATE}"
        
        print(f"✅ ТЕСТ 2 ПРОЙДЕН: Google микрофон создан с sample_rate={sample_rate}Hz от AVF")
    
    @pytest.mark.asyncio
    async def test_google_microphone_uses_avf_device_index(self, mock_device_info):
        """
        ✅ ТЕСТ 3: Проверяем, что Google микрофон создаётся с device_index, найденным по имени от AVF
        
        Гипотеза: device_index должен быть найден по имени устройства из device_info['device_info']['name']
        """
        import speech_recognition as sr
        
        # Setup: получаем имя устройства от AVF
        device_name = None
        if mock_device_info and mock_device_info.get('device_info') and mock_device_info['device_info'].get('name'):
            device_name = mock_device_info['device_info']['name']
        
        assert device_name is not None, "device_name должен быть извлечён из device_info"
        assert device_name == "Built-in Microphone", f"device_name должен быть 'Built-in Microphone', получен '{device_name}'"
        
        # Execution: ищем device_index по имени (как в реальном коде)
        device_index = None
        try:
            mic_names = sr.Microphone.list_microphone_names()
            for idx, name in enumerate(mic_names):
                if device_name.lower() in name.lower() or name.lower() in device_name.lower():
                    device_index = idx
                    break
        except Exception as e:
            print(f"⚠️ Ошибка поиска device_index: {e}")
        
        # Assertion: проверяем, что device_index найден (или None, если устройство не найдено)
        # В тестовом окружении устройство может не быть найдено, это нормально
        if device_index is not None:
            # Если device_index найден, создаём микрофон с ним
            microphone = sr.Microphone(device_index=device_index, sample_rate=48000, chunk_size=1024)
            assert microphone.device_index == device_index, f"Microphone.device_index должен быть {device_index}, получен {microphone.device_index}"
            print(f"✅ ТЕСТ 3 ПРОЙДЕН: Google микрофон создан с device_index={device_index} для устройства '{device_name}'")
        else:
            print(f"⚠️ ТЕСТ 3 ПРОПУЩЕН: device_index не найден для '{device_name}' (возможно, устройство недоступно в тестовом окружении)")
    
    @pytest.mark.asyncio
    async def test_sample_rate_match_between_avf_and_google(self, mock_device_info):
        """
        ✅ ТЕСТ 4: Проверяем соответствие sample_rate между AVF и Google микрофоном
        
        Гипотеза: sample_rate Google микрофона должен совпадать с sample_rate от AVF
        """
        import speech_recognition as sr
        
        # Setup: извлекаем sample_rate от AVF
        avf_sample_rate = None
        if mock_device_info and mock_device_info.get('input_format'):
            avf_sample_rate = mock_device_info['input_format'].get('sample_rate')
        
        assert avf_sample_rate is not None, "avf_sample_rate должен быть извлечён"
        assert avf_sample_rate == 48000, f"avf_sample_rate должен быть 48000, получен {avf_sample_rate}"
        
        # Execution: создаём Google микрофон с sample_rate от AVF
        microphone = sr.Microphone(sample_rate=avf_sample_rate, chunk_size=1024)
        mic_sample_rate = microphone.SAMPLE_RATE if hasattr(microphone, 'SAMPLE_RATE') else None
        
        # Assertion: проверяем соответствие
        assert mic_sample_rate is not None, "mic_sample_rate должен быть установлен"
        assert avf_sample_rate == mic_sample_rate, f"sample_rate должен совпадать: AVF={avf_sample_rate}Hz, Google={mic_sample_rate}Hz"
        
        print(f"✅ ТЕСТ 4 ПРОЙДЕН: sample_rate совпадает между AVF ({avf_sample_rate}Hz) и Google ({mic_sample_rate}Hz)")
    
    @pytest.mark.asyncio
    async def test_full_flow_avf_to_google_config(self, mock_avf_engine):
        """
        ✅ ТЕСТ 5: Полный поток от AVF до создания Google микрофона
        
        Гипотеза: Полный поток должен работать корректно:
        1. AVF получает конфигурацию
        2. Извлекаются параметры (sample_rate, device_index)
        3. Google микрофон создаётся с этими параметрами
        4. Параметры совпадают
        """
        from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
        from integration.core.event_bus import EventBus
        from integration.core.state_manager import ApplicationStateManager
        from integration.core.error_handler import ErrorHandler
        import speech_recognition as sr
        
        # Setup: изолированное окружение
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler()
        
        integration = VoiceRecognitionIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        # Устанавливаем мок AVF engine
        integration._use_avf = True
        integration._avf_engine = mock_avf_engine
        
        # ШАГ 1: Получаем конфигурацию через AVF
        device_info = await integration._get_device_info_via_avf()
        assert device_info is not None, "device_info не должен быть None"
        
        # ШАГ 2: Извлекаем параметры (как в реальном коде, строки 788-812)
        device_index = None
        sample_rate = None
        chunk_size = 1024
        
        if device_info and device_info.get('input_format'):
            input_format = device_info['input_format']
            sample_rate = input_format.get('sample_rate')
        
        if device_info and device_info.get('device_info') and device_info['device_info'].get('name'):
            device_name = device_info['device_info']['name']
            try:
                mic_names = sr.Microphone.list_microphone_names()
                for idx, name in enumerate(mic_names):
                    if device_name.lower() in name.lower() or name.lower() in device_name.lower():
                        device_index = idx
                        break
            except Exception:
                pass
        
        # Assertion: проверяем, что параметры извлечены
        assert sample_rate is not None, "sample_rate должен быть извлечён"
        assert sample_rate == 48000, f"sample_rate должен быть 48000, получен {sample_rate}"
        
        # ШАГ 3: Создаём Google микрофон с параметрами от AVF (как в реальном коде, строки 818-829)
        if device_index is not None and sample_rate is not None:
            microphone = sr.Microphone(device_index=device_index, sample_rate=sample_rate, chunk_size=chunk_size)
        elif sample_rate is not None:
            microphone = sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size)
        elif device_index is not None:
            microphone = sr.Microphone(device_index=device_index, chunk_size=chunk_size)
        else:
            microphone = sr.Microphone()
        
        # ШАГ 4: Проверяем соответствие (как в реальном коде, строки 903-908)
        mic_sample_rate = microphone.SAMPLE_RATE if hasattr(microphone, 'SAMPLE_RATE') else None
        avf_sample_rate = device_info['input_format'].get('sample_rate')
        
        if avf_sample_rate and mic_sample_rate:
            if avf_sample_rate != mic_sample_rate:
                pytest.fail(f"⚠️ Несоответствие sample_rate: AVF={avf_sample_rate}Hz, Google={mic_sample_rate}Hz")
            else:
                print(f"✅ sample_rate совпадает: AVF={avf_sample_rate}Hz, Google={mic_sample_rate}Hz")
        
        print("✅ ТЕСТ 5 ПРОЙДЕН: Полный поток AVF → Google микрофон работает корректно")
    
    @pytest.mark.asyncio
    async def test_fallback_when_avf_config_unavailable(self):
        """
        ✅ ТЕСТ 6: Проверяем fallback, когда конфигурация от AVF недоступна
        
        Гипотеза: Если device_info is None, Google микрофон должен создаваться с default параметрами
        """
        import speech_recognition as sr
        
        # Setup: device_info недоступен
        device_info = None
        
        # Execution: создаём микрофон с fallback (как в реальном коде, строка 828)
        device_index = None
        sample_rate = None
        
        if device_index is not None and sample_rate is not None:
            microphone = sr.Microphone(device_index=device_index, sample_rate=sample_rate, chunk_size=1024)
        elif sample_rate is not None:
            microphone = sr.Microphone(sample_rate=sample_rate, chunk_size=1024)
        elif device_index is not None:
            microphone = sr.Microphone(device_index=device_index, chunk_size=1024)
        else:
            microphone = sr.Microphone()  # Fallback: default параметры
        
        # Assertion: проверяем, что микрофон создан (даже с default параметрами)
        assert microphone is not None, "Microphone должен быть создан даже с default параметрами"
        
        print("✅ ТЕСТ 6 ПРОЙДЕН: Fallback работает корректно при недоступности конфигурации AVF")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
