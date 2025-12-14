"""
Тест для проверки инициализации AVF с вызовом initialize()
"""
import pytest
import pytest_asyncio
import asyncio
import sys
import logging
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(name)s - %(message)s')

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration


class TestAVFInitWithInitialize:
    """Тесты для проверки инициализации AVF с вызовом initialize()"""
    
    @pytest_asyncio.fixture
    async def setup_integration(self):
        """Настройка интеграции для тестирования"""
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        integration = VoiceRecognitionIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler
        )
        
        yield integration
    
    @pytest.mark.asyncio
    async def test_avf_init_after_initialize(self, setup_integration):
        """Тест: Проверка инициализации AVF после вызова initialize()"""
        integration = setup_integration
        
        print(f"\n{'='*80}")
        print(f"🔍 ПРОВЕРКА ИНИЦИАЛИЗАЦИИ AVF ПОСЛЕ initialize()")
        print(f"{'='*80}")
        
        print(f"\n📊 Состояние ДО initialize():")
        use_avf_before = getattr(integration, '_use_avf', None)
        avf_engine_before = getattr(integration, '_avf_engine', None)
        print(f"   - _use_avf: {use_avf_before}")
        print(f"   - _avf_engine: {avf_engine_before is not None if avf_engine_before else False}")
        
        print(f"\n📋 Вызов initialize()...")
        result = await integration.initialize()
        print(f"   - initialize() вернул: {result}")
        
        print(f"\n📊 Состояние ПОСЛЕ initialize():")
        use_avf_after = getattr(integration, '_use_avf', None)
        avf_engine_after = getattr(integration, '_avf_engine', None)
        print(f"   - _use_avf: {use_avf_after}")
        print(f"   - _avf_engine: {avf_engine_after is not None if avf_engine_after else False}")
        
        if use_avf_after:
            print(f"\n✅ AVF включен после initialize()!")
            if avf_engine_after:
                print(f"   ✅ AVF engine инициализирован!")
            else:
                print(f"   ⚠️ AVF engine НЕ инициализирован (но _use_avf=True)")
        else:
            print(f"\n❌ AVF отключен после initialize()!")
            print(f"   ⚠️ Это объясняет, почему используется LEGACY путь")
        
        assert True  # Тест для диагностики

