"""
Тест для перехвата реального исключения при инициализации AVF
"""
import pytest
import sys
import logging
from pathlib import Path
from unittest.mock import patch, MagicMock

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Настройка логирования для перехвата всех сообщений
logging.basicConfig(level=logging.DEBUG)

# Список для хранения всех логов
captured_logs = []

class LogCaptureHandler(logging.Handler):
    def emit(self, record):
        captured_logs.append(record)


class TestAVFInitRealException:
    """Тесты для перехвата реального исключения"""
    
    def test_avf_init_with_log_capture(self):
        """Тест: Перехват всех логов при инициализации AVF"""
        global captured_logs
        captured_logs = []
        
        print(f"\n{'='*80}")
        print(f"🔍 ПЕРЕХВАТ ВСЕХ ЛОГОВ ПРИ ИНИЦИАЛИЗАЦИИ AVF")
        print(f"{'='*80}")
        
        # Настраиваем перехват логов
        handler = LogCaptureHandler()
        logger = logging.getLogger('integration.integrations.voice_recognition_integration')
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        
        try:
            from integration.core.event_bus import EventBus
            from integration.core.state_manager import ApplicationStateManager
            from integration.core.error_handler import ErrorHandler
            from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
            
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler(event_bus)
            
            print(f"\n📋 Создание VoiceRecognitionIntegration...")
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
            
            # Ищем логи об AVF
            print(f"\n📋 Логи об AVF:")
            avf_logs = [log for log in captured_logs if 'AVF' in log.getMessage() or 'avf' in log.getMessage().lower()]
            
            if avf_logs:
                for log in avf_logs:
                    level = log.levelname
                    message = log.getMessage()
                    print(f"   [{level}] {message}")
                    
                    if log.exc_info:
                        print(f"      Исключение:")
                        import traceback
                        traceback.print_exception(*log.exc_info)
            else:
                print(f"   ⚠️ Логи об AVF не найдены")
            
            # Ищем ошибки
            error_logs = [log for log in captured_logs if log.levelno >= logging.ERROR]
            if error_logs:
                print(f"\n❌ Найдены ошибки:")
                for log in error_logs:
                    print(f"   [{log.levelname}] {log.getMessage()}")
                    if log.exc_info:
                        import traceback
                        traceback.print_exception(*log.exc_info)
            
            logger.removeHandler(handler)
            
        except Exception as e:
            print(f"\n❌ Исключение при создании интеграции: {e}")
            import traceback
            traceback.print_exc()
        
        assert True  # Тест для диагностики
    
    def test_avf_init_manual_check(self):
        """Тест: Ручная проверка каждого шага инициализации"""
        print(f"\n{'='*80}")
        print(f"🔍 РУЧНАЯ ПРОВЕРКА КАЖДОГО ШАГА")
        print(f"{'='*80}")
        
        # Шаг 1: Проверка всех условий
        print(f"\n📋 ШАГ 1: Проверка всех условий")
        
        from config.unified_config_loader import UnifiedConfigLoader
        import os
        import integration.integrations.voice_recognition_integration as vri_module
        
        loader = UnifiedConfigLoader()
        audio_config = loader.get_audio_config_object()
        avf_config = loader.get_audio_avf_config()
        
        avf_enabled = avf_config.get("avf", {}).get("enabled", False)
        ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
        disable_avf_env = os.getenv("NEXY_DISABLE_AVF_AUDIO", "false").lower() == "true"
        avf_available = getattr(vri_module, '_AVF_AVAILABLE', False)
        
        print(f"   - avf_enabled: {avf_enabled}")
        print(f"   - ks_avf_enabled: {ks_avf_enabled}")
        print(f"   - disable_avf_env: {disable_avf_env}")
        print(f"   - avf_available: {avf_available}")
        
        use_avf_expected = avf_enabled and not ks_avf_enabled and not disable_avf_env and avf_available
        print(f"   - use_avf_expected: {use_avf_expected}")
        
        # Шаг 2: Попытка создания AVFAudioEngine
        print(f"\n📋 ШАГ 2: Попытка создания AVFAudioEngine")
        
        if use_avf_expected:
            try:
                from modules.audio_avf import AVFAudioEngine
                avf_engine = AVFAudioEngine(audio_config)
                print(f"   ✅ AVFAudioEngine создан успешно")
            except Exception as e:
                print(f"   ❌ Ошибка создания AVFAudioEngine: {e}")
                import traceback
                traceback.print_exc()
                print(f"   ⚠️ Это может быть причиной, почему _use_avf = False")
        
        assert True  # Тест для диагностики

