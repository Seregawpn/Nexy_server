#!/usr/bin/env python3
"""Тест Шага 2: Проверка инициализации VoiceRecognitionIntegration"""

import sys
import asyncio
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

sys.path.insert(0, 'client')

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

async def test_init():
    print("=" * 60)
    print("ШАГ 2: Проверка инициализации VoiceRecognitionIntegration")
    print("=" * 60)
    
    try:
        print("\n🔍 Создание компонентов...")
        event_bus = EventBus()
        print("   ✅ EventBus создан")
        
        state_manager = ApplicationStateManager()
        print("   ✅ ApplicationStateManager создан")
        
        error_handler = ErrorHandler(event_bus)
        print("   ✅ ErrorHandler создан")
        
        integration = VoiceRecognitionIntegration(
            event_bus, state_manager, error_handler, None
        )
        
        print("\n🔍 Инициализация интеграции...")
        result = await integration.initialize()
        
        if result:
            print("✅ Инициализация успешна!")
            
            # Проверка состояния
            print("\n🔍 Состояние после инициализации:")
            print(f"   - _use_avf: {integration._use_avf}")
            print(f"   - _avf_engine: {integration._avf_engine is not None}")
            print(f"   - _use_streaming: {integration._use_streaming}")
            print(f"   - _sf_recognizer: {integration._sf_recognizer is not None}")
            print(f"   - _streaming_feature_enabled: {integration._streaming_feature_enabled}")
            print(f"   - _streaming_env_disabled: {integration._streaming_env_disabled}")
            
            if integration._avf_engine:
                print("\n✅ AVFAudioEngine создан")
            else:
                print("\n⚠️ AVFAudioEngine не создан")
            
            if integration._sf_recognizer:
                print("✅ SFSpeechRecognizerWrapper создан")
            else:
                print("⚠️ SFSpeechRecognizerWrapper не создан (возможно, стриминг отключен)")
            
            print("\n✅ ШАГ 2 ПРОЙДЕН!")
            
        else:
            print("❌ Инициализация не удалась")
            return False
            
    except Exception as e:
        print(f"\n❌ Ошибка при инициализации: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = asyncio.run(test_init())
    sys.exit(0 if success else 1)

