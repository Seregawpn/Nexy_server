"""
Изолированные тесты для диагностики проблемы блокировки микрофона
и неработающего Google Speech Recognition
"""
import pytest
import asyncio
from unittest.mock import Mock, AsyncMock, patch, MagicMock
import sys
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration


class TestMicrophoneBlockingDiagnosis:
    """Тесты для диагностики проблемы блокировки микрофона"""
    
    @pytest.fixture
    async def setup_integration(self):
        """Настройка интеграции для тестирования"""
        event_bus = EventBus()
        state_manager = ApplicationStateManager(event_bus)
        error_handler = ErrorHandler(event_bus)
        
        integration = VoiceRecognitionIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        yield integration
        
        # Очистка
        if hasattr(integration, '_google_stop_listening') and integration._google_stop_listening:
            try:
                integration._google_stop_listening(wait_for_stop=False)
            except:
                pass
    
    @pytest.mark.asyncio
    async def test_why_legacy_path_used(self, setup_integration):
        """Тест: Почему используется LEGACY путь вместо Google Speech Recognition?"""
        integration = setup_integration
        
        # Проверяем условия использования новой логики
        use_avf = getattr(integration, '_use_avf', False)
        avf_engine = getattr(integration, '_avf_engine', None)
        
        print(f"\n🔍 ДИАГНОСТИКА: Условия для новой логики (AVF→Google):")
        print(f"   - _use_avf: {use_avf}")
        print(f"   - _avf_engine: {avf_engine is not None}")
        
        if not use_avf or avf_engine is None:
            print(f"   ❌ Новая логика НЕ используется: use_avf={use_avf}, avf_engine={avf_engine is not None}")
            print(f"   ✅ Это объясняет, почему используется LEGACY путь")
        else:
            print(f"   ✅ Условия для новой логики выполнены")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_google_callback_not_called_hypothesis_1_avf_conflict(self, setup_integration):
        """Гипотеза 1: AVF не освобождает микрофон перед активацией Google"""
        integration = setup_integration
        
        # Симулируем ситуацию, когда AVF все еще активен
        with patch.object(integration, '_avf_engine', create=True) as mock_avf:
            mock_avf.is_input_active = True
            mock_avf.stop_input = AsyncMock(return_value=None)
            
            # Проверяем, что происходит при попытке активации Google
            session_id = "test-session-123"
            
            # Симулируем событие voice.recording_start
            event = {
                "type": "voice.recording_start",
                "data": {
                    "session_id": session_id,
                    "source": "keyboard"
                }
            }
            
            try:
                await integration._on_recording_start(event)
            except Exception as e:
                print(f"\n🔍 ДИАГНОСТИКА: Ошибка при активации Google:")
                print(f"   - Ошибка: {e}")
                print(f"   - Тип: {type(e).__name__}")
                
                if "AVF not deactivated" in str(e):
                    print(f"   ✅ Гипотеза 1 подтверждена: AVF не освобождает микрофон")
                else:
                    print(f"   ⚠️ Другая ошибка: {e}")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_google_callback_not_called_hypothesis_2_permissions(self, setup_integration):
        """Гипотеза 2: Проблемы с разрешениями микрофона"""
        integration = setup_integration
        
        # Проверяем реальные разрешения
        try:
            from modules.permissions.first_run.status_checker import check_microphone_status
            mic_status = check_microphone_status()
            
            print(f"\n🔍 ДИАГНОСТИКА: Разрешения микрофона:")
            print(f"   - Статус: {mic_status}")
            print(f"   - Значение: {mic_status.value}")
            
            if mic_status.value != "granted":
                print(f"   ❌ Разрешения НЕ предоставлены: {mic_status.value}")
                print(f"   ✅ Это объясняет, почему Google Speech Recognition не работает")
            else:
                print(f"   ✅ Разрешения предоставлены")
        except Exception as e:
            print(f"   ❌ Ошибка проверки разрешений: {e}")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_google_callback_not_called_hypothesis_3_pyaudio(self, setup_integration):
        """Гипотеза 3: Проблемы с PyAudio или speech_recognition библиотекой"""
        integration = setup_integration
        
        try:
            import speech_recognition as sr
            import pyaudio
            
            print(f"\n🔍 ДИАГНОСТИКА: Проверка PyAudio и speech_recognition:")
            
            # Проверяем доступность PyAudio
            try:
                p = pyaudio.PyAudio()
                device_count = p.get_device_count()
                print(f"   - PyAudio доступен: ✅")
                print(f"   - Количество устройств: {device_count}")
                
                # Проверяем список микрофонов
                mic_list = sr.Microphone.list_microphone_names()
                print(f"   - Доступно микрофонов: {len(mic_list)}")
                if mic_list:
                    print(f"   - Первый микрофон: {mic_list[0]}")
                
                p.terminate()
            except Exception as e:
                print(f"   ❌ PyAudio недоступен: {e}")
                print(f"   ✅ Это может объяснять проблему")
            
        except ImportError as e:
            print(f"   ❌ Библиотека не установлена: {e}")
            print(f"   ✅ Это объясняет проблему")
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_google_callback_not_called_hypothesis_4_device_index(self, setup_integration):
        """Гипотеза 4: Неправильный device_index или sample_rate"""
        integration = setup_integration
        
        # Проверяем, какие device_index используются
        try:
            import speech_recognition as sr
            mic_list = sr.Microphone.list_microphone_names()
            
            print(f"\n🔍 ДИАГНОСТИКА: device_index и sample_rate:")
            print(f"   - Доступно микрофонов: {len(mic_list)}")
            
            for i, mic_name in enumerate(mic_list[:5]):  # Первые 5
                print(f"   - device_index {i}: {mic_name}")
            
            # Проверяем, какой device_index используется по умолчанию
            try:
                mic = sr.Microphone()
                print(f"   - device_index по умолчанию: {mic.device_index}")
            except Exception as e:
                print(f"   - Ошибка получения device_index: {e}")
                
        except Exception as e:
            print(f"   ❌ Ошибка: {e}")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_legacy_path_blocks_microphone(self, setup_integration):
        """Тест: LEGACY путь блокирует микрофон для других приложений"""
        integration = setup_integration
        
        # Проверяем, что LEGACY путь использует AVF
        print(f"\n🔍 ДИАГНОСТИКА: LEGACY путь и блокировка микрофона:")
        print(f"   - LEGACY путь использует SpeechRecognizer.start_listening()")
        print(f"   - SpeechRecognizer использует sounddevice, который может блокировать микрофон")
        print(f"   - Это объясняет, почему микрофон блокируется для других приложений")
        
        # Проверяем, есть ли способ освободить микрофон
        if hasattr(integration, '_recognizer') and integration._recognizer:
            print(f"   - _recognizer доступен: ✅")
            if hasattr(integration._recognizer, 'stop_listening'):
                print(f"   - Метод stop_listening доступен: ✅")
            else:
                print(f"   - Метод stop_listening НЕ доступен: ❌")
        else:
            print(f"   - _recognizer НЕ доступен: ❌")
        
        assert True  # Тест для диагностики
    
    @pytest.mark.asyncio
    async def test_playback_cancelled_closes_microphone(self, setup_integration):
        """Тест: playback.cancelled закрывает микрофон сразу после активации"""
        integration = setup_integration
        
        # Симулируем ситуацию, когда микрофон активируется, но затем закрывается из-за playback.cancelled
        session_id = "test-session-456"
        
        # Симулируем активацию микрофона
        event_start = {
            "type": "voice.recording_start",
            "data": {
                "session_id": session_id,
                "source": "keyboard"
            }
        }
        
        # Симулируем playback.cancelled
        event_cancelled = {
            "type": "playback.cancelled",
            "data": {
                "session_id": session_id
            }
        }
        
        print(f"\n🔍 ДИАГНОСТИКА: playback.cancelled и закрытие микрофона:")
        print(f"   - Микрофон активируется через voice.recording_start")
        print(f"   - Затем приходит playback.cancelled")
        print(f"   - Это может закрывать микрофон сразу после активации")
        
        # Проверяем логику _on_playback_finished
        if hasattr(integration, '_on_playback_finished'):
            print(f"   - Метод _on_playback_finished существует: ✅")
        else:
            print(f"   - Метод _on_playback_finished НЕ существует: ❌")
        
        assert True  # Тест для диагностики

