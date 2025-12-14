"""
Тест для проверки инициализации AVF в VoiceRecognitionIntegration
"""
import pytest
import asyncio
from unittest.mock import Mock, AsyncMock, patch
import sys
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration


class TestIntegrationAVFInit:
    """Тесты для проверки инициализации AVF в интеграции"""
    
    @pytest.mark.asyncio
    async def test_integration_avf_initialization(self):
        """Тест: Проверка инициализации AVF в VoiceRecognitionIntegration"""
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        print(f"\n🔍 ДИАГНОСТИКА: Инициализация VoiceRecognitionIntegration:")
        
        try:
            integration = VoiceRecognitionIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Ждем немного для завершения инициализации
            await asyncio.sleep(0.5)
            
            use_avf = getattr(integration, '_use_avf', None)
            avf_engine = getattr(integration, '_avf_engine', None)
            
            print(f"   - _use_avf: {use_avf}")
            print(f"   - _avf_engine: {avf_engine is not None if avf_engine else False}")
            
            # Проверяем _AVF_AVAILABLE из модуля
            import integration.integrations.voice_recognition_integration as vri_module
            avf_available_module = getattr(vri_module, '_AVF_AVAILABLE', None)
            print(f"   - _AVF_AVAILABLE в модуле: {avf_available_module}")
            
            if use_avf is False:
                print(f"   ❌ AVF отключен в интеграции!")
                print(f"   🔍 Проверяем причины...")
                
                # Проверяем конфигурацию
                from config.unified_config_loader import UnifiedConfigLoader
                loader = UnifiedConfigLoader()
                avf_config = loader.get_audio_avf_config()
                
                avf_enabled = avf_config.get("avf", {}).get("enabled", False)
                ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
                
                print(f"      - avf.enabled в конфиге: {avf_enabled}")
                print(f"      - ks_avf.enabled в конфиге: {ks_avf_enabled}")
                
                # Проверяем env переменную
                import os
                disable_avf_env = os.getenv("NEXY_DISABLE_AVF_AUDIO", "false").lower() == "true"
                print(f"      - NEXY_DISABLE_AVF_AUDIO: {disable_avf_env}")
                
                # Проверяем доступность AVF
                try:
                    from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
                    print(f"      - AVFAudioEngine импортирован: ✅")
                    avf_available = True
                except Exception as e:
                    print(f"      - AVFAudioEngine НЕ импортирован: ❌ {e}")
                    avf_available = False
                
                # Проверяем _AVF_AVAILABLE из модуля
                print(f"      - _AVF_AVAILABLE в модуле: {avf_available_module}")
                
                if not avf_enabled:
                    print(f"      ❌ ПРИЧИНА: avf.enabled=False в конфиге")
                elif ks_avf_enabled:
                    print(f"      ❌ ПРИЧИНА: ks_avf.enabled=True (kill-switch)")
                elif disable_avf_env:
                    print(f"      ❌ ПРИЧИНА: NEXY_DISABLE_AVF_AUDIO=true")
                elif not avf_available:
                    print(f"      ❌ ПРИЧИНА: AVFAudioEngine недоступен")
                elif avf_available_module is False:
                    print(f"      ❌ ПРИЧИНА: _AVF_AVAILABLE=False в модуле (ошибка при импорте)")
                else:
                    print(f"      ⚠️ ПРИЧИНА: Неизвестна (все условия выполнены)")
                    print(f"      ⚠️ Возможно, исключение произошло при создании AVFAudioEngine в интеграции")
            else:
                print(f"   ✅ AVF включен в интеграции!")
                if avf_engine:
                    print(f"   ✅ AVF engine инициализирован!")
                else:
                    print(f"   ⚠️ AVF engine НЕ инициализирован (но _use_avf=True)")
            
        except Exception as e:
            print(f"   ❌ Ошибка инициализации: {e}")
            import traceback
            traceback.print_exc()
            raise

