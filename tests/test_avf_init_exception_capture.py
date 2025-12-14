"""
Тест для перехвата исключения при инициализации AVF
"""
import pytest
import sys
import logging
from pathlib import Path
from unittest.mock import patch

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)


class TestAVFInitExceptionCapture:
    """Тесты для перехвата исключения при инициализации AVF"""
    
    def test_avf_init_step_by_step(self):
        """Тест: Пошаговая проверка инициализации AVF"""
        print(f"\n{'='*80}")
        print(f"🔍 ПОШАГОВАЯ ПРОВЕРКА ИНИЦИАЛИЗАЦИИ AVF")
        print(f"{'='*80}")
        
        # Шаг 1: Проверка импорта
        print(f"\n📋 ШАГ 1: Проверка импорта AVFAudioEngine")
        try:
            from modules.audio_avf import AVFAudioEngine
            from config.audio_config import AudioConfig
            print(f"   ✅ AVFAudioEngine импортирован")
            print(f"   ✅ AudioConfig импортирован")
        except Exception as e:
            print(f"   ❌ Ошибка импорта: {e}")
            import traceback
            traceback.print_exc()
            assert False, f"Ошибка импорта: {e}"
        
        # Шаг 2: Проверка загрузки конфигурации
        print(f"\n📋 ШАГ 2: Проверка загрузки конфигурации")
        try:
            from config.unified_config_loader import UnifiedConfigLoader
            loader = UnifiedConfigLoader()
            print(f"   ✅ UnifiedConfigLoader создан")
            
            audio_config = loader.get_audio_config_object()
            print(f"   ✅ audio_config загружен: {audio_config is not None}")
            
            avf_config = loader.get_audio_avf_config()
            print(f"   ✅ avf_config загружен: {avf_config is not None}")
            
            avf_enabled = avf_config.get("avf", {}).get("enabled", False)
            ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
            print(f"   - avf.enabled: {avf_enabled}")
            print(f"   - ks_avf.enabled: {ks_avf_enabled}")
            
        except Exception as e:
            print(f"   ❌ Ошибка загрузки конфигурации: {e}")
            import traceback
            traceback.print_exc()
            assert False, f"Ошибка загрузки конфигурации: {e}"
        
        # Шаг 3: Проверка env переменной
        print(f"\n📋 ШАГ 3: Проверка env переменной")
        import os
        disable_avf_env = os.getenv("NEXY_DISABLE_AVF_AUDIO", "false").lower() == "true"
        print(f"   - NEXY_DISABLE_AVF_AUDIO: {os.getenv('NEXY_DISABLE_AVF_AUDIO', 'не установлена')}")
        print(f"   - disable_avf_env: {disable_avf_env}")
        
        # Шаг 4: Проверка _AVF_AVAILABLE
        print(f"\n📋 ШАГ 4: Проверка _AVF_AVAILABLE")
        try:
            import integration.integrations.voice_recognition_integration as vri_module
            avf_available = getattr(vri_module, '_AVF_AVAILABLE', None)
            print(f"   - _AVF_AVAILABLE: {avf_available}")
        except Exception as e:
            print(f"   ❌ Ошибка проверки _AVF_AVAILABLE: {e}")
            import traceback
            traceback.print_exc()
        
        # Шаг 5: Проверка создания AVFAudioEngine
        print(f"\n📋 ШАГ 5: Проверка создания AVFAudioEngine")
        try:
            avf_engine = AVFAudioEngine(audio_config)
            print(f"   ✅ AVFAudioEngine создан: {avf_engine is not None}")
        except Exception as e:
            print(f"   ❌ Ошибка создания AVFAudioEngine: {e}")
            import traceback
            traceback.print_exc()
            assert False, f"Ошибка создания AVFAudioEngine: {e}"
        
        # Шаг 6: Проверка условия _use_avf
        print(f"\n📋 ШАГ 6: Проверка условия _use_avf")
        use_avf_expected = avf_enabled and not ks_avf_enabled and not disable_avf_env and avf_available
        print(f"   - avf_enabled: {avf_enabled}")
        print(f"   - not ks_avf_enabled: {not ks_avf_enabled}")
        print(f"   - not disable_avf_env: {not disable_avf_env}")
        print(f"   - avf_available: {avf_available}")
        print(f"   - use_avf_expected: {use_avf_expected}")
        
        if not use_avf_expected:
            print(f"   ❌ _use_avf должен быть False")
            if not avf_enabled:
                print(f"      - Причина: avf.enabled=False")
            if ks_avf_enabled:
                print(f"      - Причина: ks_avf.enabled=True")
            if disable_avf_env:
                print(f"      - Причина: NEXY_DISABLE_AVF_AUDIO=true")
            if not avf_available:
                print(f"      - Причина: _AVF_AVAILABLE=False")
        else:
            print(f"   ✅ _use_avf должен быть True")
        
        assert True  # Тест для диагностики
    
    def test_avf_init_with_exception_capture(self):
        """Тест: Перехват исключения при инициализации AVF в интеграции"""
        print(f"\n{'='*80}")
        print(f"🔍 ПЕРЕХВАТ ИСКЛЮЧЕНИЯ ПРИ ИНИЦИАЛИЗАЦИИ AVF")
        print(f"{'='*80}")
        
        # Симулируем инициализацию интеграции с перехватом исключений
        from integration.core.event_bus import EventBus
        from integration.core.state_manager import ApplicationStateManager
        from integration.core.error_handler import ErrorHandler
        
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        print(f"\n📋 Создание VoiceRecognitionIntegration...")
        
        captured_exception = None
        
        try:
            from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
            
            # Перехватываем логирование для поиска исключений
            import logging
            
            class ExceptionHandler(logging.Handler):
                def __init__(self):
                    super().__init__()
                    self.exceptions = []
                
                def emit(self, record):
                    if record.levelno >= logging.ERROR:
                        if 'AVF' in record.getMessage() or 'инициализации' in record.getMessage():
                            self.exceptions.append(record)
            
            handler = ExceptionHandler()
            logger = logging.getLogger('integration.integrations.voice_recognition_integration')
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG)
            
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            print(f"\n📊 Результаты инициализации:")
            use_avf = getattr(integration, '_use_avf', None)
            avf_engine = getattr(integration, '_avf_engine', None)
            
            print(f"   - _use_avf: {use_avf}")
            print(f"   - _avf_engine: {avf_engine is not None if avf_engine else False}")
            
            if handler.exceptions:
                print(f"\n❌ Найдены исключения при инициализации:")
                for exc_record in handler.exceptions:
                    print(f"   - {exc_record.getMessage()}")
                    if exc_record.exc_info:
                        import traceback
                        traceback.print_exception(*exc_record.exc_info)
            
            logger.removeHandler(handler)
            
        except Exception as e:
            print(f"\n❌ Исключение при создании интеграции: {e}")
            import traceback
            traceback.print_exc()
            captured_exception = e
        
        assert True  # Тест для диагностики

