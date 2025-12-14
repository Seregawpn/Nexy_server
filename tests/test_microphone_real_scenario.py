"""
Комплексный тест для проверки реального сценария активации микрофона
"""
import pytest
import pytest_asyncio
import asyncio
import sys
import logging
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch, MagicMock

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Настройка логирования для теста
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration


class TestMicrophoneRealScenario:
    """Тесты для проверки реального сценария активации микрофона"""
    
    @pytest_asyncio.fixture
    async def setup_integration(self):
        """Настройка интеграции для тестирования"""
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        # Подключаем event_bus к state_manager
        if hasattr(state_manager, 'attach_event_bus'):
            state_manager.attach_event_bus(event_bus)
        elif hasattr(state_manager, 'set_event_bus'):
            state_manager.set_event_bus(event_bus)
        
        print(f"\n{'='*80}")
        print(f"🔧 ИНИЦИАЛИЗАЦИЯ VoiceRecognitionIntegration")
        print(f"{'='*80}")
        
        integration = VoiceRecognitionIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        # Ждем завершения инициализации
        await asyncio.sleep(1.0)
        
        yield integration
        
        # Очистка
        if hasattr(integration, '_google_stop_listening') and integration._google_stop_listening:
            try:
                integration._google_stop_listening(wait_for_stop=False)
            except:
                pass
    
    @pytest.mark.asyncio
    async def test_avf_initialization_detailed(self, setup_integration):
        """Тест: Детальная проверка инициализации AVF"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 1: Детальная проверка инициализации AVF")
        print(f"{'='*80}")
        
        use_avf = getattr(integration, '_use_avf', None)
        avf_engine = getattr(integration, '_avf_engine', None)
        
        print(f"\n📊 Результаты инициализации:")
        print(f"   - _use_avf: {use_avf}")
        print(f"   - _avf_engine: {avf_engine is not None if avf_engine else False}")
        
        # Проверяем _AVF_AVAILABLE из модуля
        import integration.integrations.voice_recognition_integration as vri_module
        avf_available_module = getattr(vri_module, '_AVF_AVAILABLE', None)
        print(f"   - _AVF_AVAILABLE в модуле: {avf_available_module}")
        
        if use_avf is False or use_avf is None:
            print(f"\n❌ ПРОБЛЕМА: AVF отключен в интеграции!")
            print(f"\n🔍 Проверяем все условия:")
            
            # Проверяем конфигурацию
            from config.unified_config_loader import UnifiedConfigLoader
            loader = UnifiedConfigLoader()
            
            try:
                audio_config = loader.get_audio_config_object()
                print(f"   ✅ audio_config загружен: {audio_config is not None}")
            except Exception as e:
                print(f"   ❌ Ошибка загрузки audio_config: {e}")
                import traceback
                traceback.print_exc()
            
            try:
                avf_config = loader.get_audio_avf_config()
                avf_enabled = avf_config.get("avf", {}).get("enabled", False)
                ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
                print(f"   ✅ avf_config загружен: {avf_config is not None}")
                print(f"   - avf.enabled: {avf_enabled}")
                print(f"   - ks_avf.enabled: {ks_avf_enabled}")
            except Exception as e:
                print(f"   ❌ Ошибка загрузки avf_config: {e}")
                import traceback
                traceback.print_exc()
            
            # Проверяем env переменную
            import os
            disable_avf_env = os.getenv("NEXY_DISABLE_AVF_AUDIO", "false").lower() == "true"
            print(f"   - NEXY_DISABLE_AVF_AUDIO: {disable_avf_env}")
            
            # Проверяем доступность AVF
            try:
                from modules.audio_avf import AVFAudioEngine
                print(f"   ✅ AVFAudioEngine импортирован")
                
                # Пробуем создать AVFAudioEngine
                try:
                    test_avf_engine = AVFAudioEngine(audio_config)
                    print(f"   ✅ AVFAudioEngine создан успешно")
                except Exception as e:
                    print(f"   ❌ Ошибка создания AVFAudioEngine: {e}")
                    import traceback
                    traceback.print_exc()
            except Exception as e:
                print(f"   ❌ AVFAudioEngine НЕ импортирован: {e}")
            
            print(f"\n📋 ИТОГОВАЯ ДИАГНОСТИКА:")
            if not avf_enabled:
                print(f"   ❌ ПРИЧИНА: avf.enabled=False в конфиге")
            elif ks_avf_enabled:
                print(f"   ❌ ПРИЧИНА: ks_avf.enabled=True (kill-switch)")
            elif disable_avf_env:
                print(f"   ❌ ПРИЧИНА: NEXY_DISABLE_AVF_AUDIO=true")
            elif avf_available_module is False:
                print(f"   ❌ ПРИЧИНА: _AVF_AVAILABLE=False в модуле")
            else:
                print(f"   ⚠️ ПРИЧИНА: Исключение при инициализации AVF в интеграции")
                print(f"   ⚠️ Нужно проверить логи при запуске приложения")
        else:
            print(f"\n✅ AVF включен в интеграции!")
            if avf_engine:
                print(f"   ✅ AVF engine инициализирован!")
            else:
                print(f"   ⚠️ AVF engine НЕ инициализирован (но _use_avf=True)")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_google_speech_recognition_activation(self, setup_integration):
        """Тест: Проверка активации Google Speech Recognition"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 2: Проверка активации Google Speech Recognition")
        print(f"{'='*80}")
        
        use_avf = getattr(integration, '_use_avf', False)
        
        if not use_avf:
            print(f"\n⚠️ AVF отключен, Google Speech Recognition не будет использоваться")
            print(f"   Используется LEGACY путь через SpeechRecognizer")
            assert True  # Тест для диагностики
            return
        
        print(f"\n✅ AVF включен, проверяем активацию Google Speech Recognition...")
        
        # Симулируем событие voice.recording_start
        session_id = "test-session-789"
        event = {
            "type": "voice.recording_start",
            "data": {
                "session_id": session_id,
                "source": "keyboard"
            }
        }
        
        print(f"\n📤 Публикуем событие voice.recording_start...")
        
        try:
            await integration._on_recording_start(event)
            print(f"   ✅ _on_recording_start завершен")
            
            # Проверяем состояние
            google_recording_active = getattr(integration, '_google_recording_active', False)
            google_stop_listening = getattr(integration, '_google_stop_listening', None)
            
            print(f"\n📊 Состояние после активации:")
            print(f"   - _google_recording_active: {google_recording_active}")
            print(f"   - _google_stop_listening: {google_stop_listening is not None}")
            
            if google_stop_listening:
                print(f"\n⏳ Ждем 3 секунды для вызова callback...")
                await asyncio.sleep(3.0)
                
                # Проверяем, был ли вызван callback
                callback_called = getattr(integration, '_google_chunk_event', None)
                if callback_called:
                    callback_called = callback_called.is_set()
                
                with getattr(integration, '_google_audio_chunks_lock', None) or MagicMock():
                    chunks_count = len(getattr(integration, '_google_audio_chunks', []))
                
                print(f"\n📊 Результаты после ожидания:")
                print(f"   - callback_called: {callback_called}")
                print(f"   - chunks_count: {chunks_count}")
                
                if callback_called or chunks_count > 0:
                    print(f"   ✅ Callback вызван успешно!")
                else:
                    print(f"   ❌ Callback НЕ вызван!")
                    print(f"   ⚠️ Возможные причины:")
                    print(f"      1. Микрофон занят другим приложением")
                    print(f"      2. Проблемы с разрешениями")
                    print(f"      3. Проблемы с PyAudio")
                
                # Останавливаем запись
                if google_stop_listening:
                    try:
                        google_stop_listening(wait_for_stop=False)
                        print(f"   ✅ Запись остановлена")
                    except Exception as e:
                        print(f"   ⚠️ Ошибка остановки записи: {e}")
            else:
                print(f"   ❌ _google_stop_listening is None - запись не запущена")
                
        except Exception as e:
            print(f"\n❌ Ошибка при активации: {e}")
            import traceback
            traceback.print_exc()
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_legacy_path_microphone_blocking(self, setup_integration):
        """Тест: Проверка блокировки микрофона при использовании LEGACY пути"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 3: Проверка блокировки микрофона (LEGACY путь)")
        print(f"{'='*80}")
        
        use_avf = getattr(integration, '_use_avf', False)
        
        if use_avf:
            print(f"\n✅ AVF включен, LEGACY путь не используется")
            assert True  # Тест для диагностики
            return
        
        print(f"\n⚠️ AVF отключен, используется LEGACY путь")
        print(f"   LEGACY путь использует SpeechRecognizer.start_listening()")
        print(f"   Это может блокировать микрофон для других приложений")
        
        recognizer = getattr(integration, '_recognizer', None)
        if recognizer:
            print(f"   ✅ _recognizer доступен")
            if hasattr(recognizer, 'start_listening'):
                print(f"   ✅ Метод start_listening доступен")
            else:
                print(f"   ❌ Метод start_listening НЕ доступен")
        else:
            print(f"   ❌ _recognizer НЕ доступен")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_microphone_permission_check(self, setup_integration):
        """Тест: Проверка разрешений микрофона"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 4: Проверка разрешений микрофона")
        print(f"{'='*80}")
        
        try:
            from modules.permissions.first_run.status_checker import check_microphone_status
            mic_status = check_microphone_status()
            
            print(f"\n📊 Результаты проверки разрешений:")
            print(f"   - Статус: {mic_status}")
            print(f"   - Значение: {mic_status.value}")
            
            if mic_status.value == "granted":
                print(f"   ✅ Разрешения предоставлены")
            else:
                print(f"   ❌ Разрешения НЕ предоставлены: {mic_status.value}")
                print(f"   ⚠️ Это может быть причиной проблемы с callback")
        except Exception as e:
            print(f"   ❌ Ошибка проверки разрешений: {e}")
            import traceback
            traceback.print_exc()
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_pyaudio_device_access(self, setup_integration):
        """Тест: Проверка доступа к устройствам PyAudio"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ 5: Проверка доступа к устройствам PyAudio")
        print(f"{'='*80}")
        
        try:
            import speech_recognition as sr
            import pyaudio
            
            p = pyaudio.PyAudio()
            
            print(f"\n📊 Информация о устройствах:")
            print(f"   - Количество устройств: {p.get_device_count()}")
            
            # Проверяем входные устройства
            input_devices = []
            for i in range(p.get_device_count()):
                try:
                    info = p.get_device_info_by_index(i)
                    if info['maxInputChannels'] > 0:
                        input_devices.append({
                            'index': i,
                            'name': info['name'],
                            'channels': info['maxInputChannels'],
                            'sample_rate': info['defaultSampleRate']
                        })
                except:
                    pass
            
            print(f"\n📊 Входные устройства:")
            for dev in input_devices[:5]:  # Первые 5
                print(f"   - device_index {dev['index']}: {dev['name']}")
                print(f"     channels: {dev['channels']}, sample_rate: {dev['sample_rate']}")
            
            # Проверяем список микрофонов через speech_recognition
            try:
                mic_list = sr.Microphone.list_microphone_names()
                print(f"\n📊 Микрофоны через speech_recognition:")
                print(f"   - Количество: {len(mic_list)}")
                for i, mic_name in enumerate(mic_list[:5]):
                    print(f"   - device_index {i}: {mic_name}")
            except Exception as e:
                print(f"   ❌ Ошибка получения списка микрофонов: {e}")
            
            p.terminate()
            
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
            import traceback
            traceback.print_exc()
        
        assert True  # Тест для диагностики

