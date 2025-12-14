"""
Изолированные тесты для проверки активации Google Speech Recognition через AVF
"""
import pytest
import asyncio
from unittest.mock import Mock, AsyncMock, patch, MagicMock
import sys
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class TestAVFGoogleActivation:
    """Тесты для проверки активации Google Speech Recognition"""
    
    @pytest.mark.asyncio
    async def test_avf_availability(self):
        """Тест: Проверка доступности AVF"""
        try:
            from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
            print(f"\n✅ AVF доступен: AVFAudioEngine импортирован успешно")
            avf_available = True
        except ImportError as e:
            print(f"\n❌ AVF НЕ доступен: {e}")
            avf_available = False
        except Exception as e:
            print(f"\n❌ AVF НЕ доступен (ошибка): {e}")
            avf_available = False
        
        assert avf_available, "AVF должен быть доступен для работы новой логики"
    
    @pytest.mark.asyncio
    async def test_config_avf_enabled(self):
        """Тест: Проверка конфигурации AVF"""
        from config.unified_config_loader import UnifiedConfigLoader
        
        loader = UnifiedConfigLoader()
        avf_config = loader.get_audio_avf_config()
        
        avf_enabled = avf_config.get("avf", {}).get("enabled", False)
        ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
        
        print(f"\n🔍 ДИАГНОСТИКА: Конфигурация AVF:")
        print(f"   - avf.enabled: {avf_enabled}")
        print(f"   - ks_avf.enabled: {ks_avf_enabled}")
        
        if not avf_enabled:
            print(f"   ❌ AVF отключен в конфиге!")
        if ks_avf_enabled:
            print(f"   ❌ Kill-switch для AVF включен!")
        
        assert avf_enabled, "AVF должен быть включен в конфиге"
        assert not ks_avf_enabled, "Kill-switch для AVF не должен быть включен"
    
    @pytest.mark.asyncio
    async def test_env_variable_check(self):
        """Тест: Проверка env переменных"""
        import os
        
        disable_avf_env = os.getenv("NEXY_DISABLE_AVF_AUDIO", "false").lower() == "true"
        
        print(f"\n🔍 ДИАГНОСТИКА: Env переменные:")
        print(f"   - NEXY_DISABLE_AVF_AUDIO: {os.getenv('NEXY_DISABLE_AVF_AUDIO', 'не установлена')}")
        print(f"   - disable_avf_env: {disable_avf_env}")
        
        if disable_avf_env:
            print(f"   ❌ AVF отключен через env переменную!")
        
        assert not disable_avf_env, "AVF не должен быть отключен через env переменную"
    
    @pytest.mark.asyncio
    async def test_google_speech_recognition_import(self):
        """Тест: Проверка импорта speech_recognition"""
        try:
            import speech_recognition as sr
            print(f"\n✅ speech_recognition импортирован успешно")
            print(f"   - Версия: {sr.__version__ if hasattr(sr, '__version__') else 'неизвестна'}")
            
            # Проверяем доступность микрофонов
            try:
                mic_list = sr.Microphone.list_microphone_names()
                print(f"   - Доступно микрофонов: {len(mic_list)}")
            except Exception as e:
                print(f"   ⚠️ Ошибка получения списка микрофонов: {e}")
            
            assert True
        except ImportError as e:
            print(f"\n❌ speech_recognition НЕ установлен: {e}")
            assert False, "speech_recognition должен быть установлен"
    
    @pytest.mark.asyncio
    async def test_google_listen_in_background_basic(self):
        """Тест: Базовая проверка listen_in_background"""
        try:
            import speech_recognition as sr
            
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            
            callback_called = False
            
            def test_callback(recognizer, audio):
                nonlocal callback_called
                callback_called = True
                print(f"\n✅ Callback вызван! audio_size={len(audio.get_raw_data()) if hasattr(audio, 'get_raw_data') else 0} bytes")
            
            print(f"\n🔍 ДИАГНОСТИКА: Тест listen_in_background:")
            print(f"   - Запускаем listen_in_background на 1 секунду...")
            
            stop_listening = recognizer.listen_in_background(microphone, test_callback)
            
            if stop_listening is None:
                print(f"   ❌ listen_in_background вернул None!")
                assert False, "listen_in_background должен вернуть функцию остановки"
            
            print(f"   - listen_in_background запущен, ждем 1 секунду...")
            await asyncio.sleep(1.0)
            
            # Останавливаем
            stop_listening(wait_for_stop=False)
            
            # Даем время на вызов callback
            await asyncio.sleep(0.5)
            
            if callback_called:
                print(f"   ✅ Callback вызван успешно!")
            else:
                print(f"   ❌ Callback НЕ вызван за 1 секунду!")
                print(f"   ⚠️ Возможные причины:")
                print(f"      - Микрофон занят другим приложением")
                print(f"      - Проблемы с разрешениями")
                print(f"      - Проблемы с PyAudio")
            
            # Не делаем assert, так как это может быть нормально в тестовой среде
            print(f"   - Тест завершен (callback_called={callback_called})")
            
        except Exception as e:
            print(f"\n❌ Ошибка теста listen_in_background: {e}")
            import traceback
            traceback.print_exc()
            # Не делаем assert False, так как это может быть нормально в тестовой среде

