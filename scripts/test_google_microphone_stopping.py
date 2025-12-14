#!/usr/bin/env python3
"""
Изолированный тест для диагностики залипания Google микрофона.

Тестирует:
1. Проверку состояния Google микрофона (_google_stop_listening)
2. Остановку Google микрофона при session mismatch
3. Синхронизацию состояния после остановки
4. Проверку физического состояния микрофона после остановки
"""

import asyncio
import sys
import os
import time
from pathlib import Path

# Отключаем AVF для тестов (избегаем проблем с PyObjC)
os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
from config.unified_config_loader import UnifiedConfigLoader


async def test_google_mic_state_check():
    """Тест 1: Проверка состояния Google микрофона"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Проверка состояния Google микрофона")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    # Используем переменную окружения для отключения AVF
    os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"
    
    from integration.integrations.voice_recognition_integration import VoiceRecognitionConfig
    
    # Создаём конфиг с симуляцией для избежания проблем с AVF
    config = VoiceRecognitionConfig(simulate=True)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config
    )
    
    # Устанавливаем _use_avf=False перед инициализацией
    integration._use_avf = False
    
    try:
        await integration.initialize()
    except Exception as e:
        print(f"   ⚠️ Ошибка инициализации (продолжаем тест): {e}")
        # Устанавливаем минимальное состояние для теста
        integration._initialized = True
    
    # Проверяем начальное состояние
    print(f"\n1.1 Начальное состояние:")
    print(f"   _google_stop_listening: {integration._google_stop_listening}")
    print(f"   hasattr('_google_stop_listening'): {hasattr(integration, '_google_stop_listening')}")
    google_mic_active = hasattr(integration, '_google_stop_listening') and integration._google_stop_listening is not None
    print(f"   google_mic_active: {google_mic_active}")
    
    # Симулируем активацию микрофона
    print(f"\n1.2 Симуляция активации микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        integration._google_stop_listening = recognizer.listen_in_background(microphone, dummy_callback)
        print(f"   _google_stop_listening установлен: {integration._google_stop_listening is not None}")
        
        google_mic_active = hasattr(integration, '_google_stop_listening') and integration._google_stop_listening is not None
        print(f"   google_mic_active после активации: {google_mic_active}")
        
        # Проверяем состояние после установки
        print(f"\n1.3 Проверка состояния после активации:")
        print(f"   _google_stop_listening: {integration._google_stop_listening}")
        print(f"   type(_google_stop_listening): {type(integration._google_stop_listening)}")
        print(f"   callable(_google_stop_listening): {callable(integration._google_stop_listening)}")
        
        # Останавливаем микрофон
        print(f"\n1.4 Остановка микрофона:")
        try:
            integration._google_stop_listening(wait_for_stop=False)
            print(f"   ✅ _google_stop_listening вызван успешно")
        except Exception as e:
            print(f"   ❌ Ошибка при вызове _google_stop_listening: {e}")
        
        # Проверяем состояние после остановки
        print(f"\n1.5 Проверка состояния после остановки:")
        print(f"   _google_stop_listening: {integration._google_stop_listening}")
        google_mic_active = hasattr(integration, '_google_stop_listening') and integration._google_stop_listening is not None
        print(f"   google_mic_active после остановки: {google_mic_active}")
        
        # Очищаем состояние
        integration._google_stop_listening = None
        integration._google_recognizer = None
        integration._google_microphone = None
        print(f"\n1.6 Очистка состояния:")
        print(f"   _google_stop_listening после очистки: {integration._google_stop_listening}")
        google_mic_active = hasattr(integration, '_google_stop_listening') and integration._google_stop_listening is not None
        print(f"   google_mic_active после очистки: {google_mic_active}")
        
    except Exception as e:
        import traceback
        print(f"   ❌ Ошибка в тесте: {e}")
        print(traceback.format_exc())
    
    print("\n" + "="*80)
    print("ТЕСТ 1 ЗАВЕРШЁН")
    print("="*80)


async def test_session_mismatch_stopping():
    """Тест 2: Остановка Google микрофона при session mismatch"""
    print("\n" + "="*80)
    print("ТЕСТ 2: Остановка Google микрофона при session mismatch")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    # Используем переменную окружения для отключения AVF
    os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"
    
    from integration.integrations.voice_recognition_integration import VoiceRecognitionConfig
    
    # Создаём конфиг с симуляцией для избежания проблем с AVF
    config = VoiceRecognitionConfig(simulate=True)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config
    )
    
    # Устанавливаем _use_avf=False перед инициализацией
    integration._use_avf = False
    
    try:
        await integration.initialize()
    except Exception as e:
        print(f"   ⚠️ Ошибка инициализации (продолжаем тест): {e}")
        # Устанавливаем минимальное состояние для теста
        integration._initialized = True
    
    # Симулируем активацию микрофона с session_id
    session_id = "test_session_123"
    state_manager.update_session_id(session_id)
    state_manager.set_microphone_state("active", session_id=session_id, reason="test_activation")
    
    print(f"\n2.1 Начальное состояние:")
    print(f"   session_id: {session_id}")
    print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    
    # Симулируем активацию Google микрофона
    print(f"\n2.2 Симуляция активации Google микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        integration._google_stop_listening = recognizer.listen_in_background(microphone, dummy_callback)
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        
        print(f"   ✅ Google микрофон активирован")
        print(f"   _google_stop_listening: {integration._google_stop_listening is not None}")
        
        # Симулируем session mismatch (сброс session_id)
        print(f"\n2.3 Симуляция session mismatch:")
        state_manager.update_session_id(None)
        print(f"   session_id сброшен в None")
        print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
        
        # Публикуем voice.recording_stop с оригинальным session_id
        print(f"\n2.4 Публикация voice.recording_stop с session_id={session_id}:")
        await event_bus.publish("voice.recording_stop", {
            "source": "test",
            "timestamp": time.time(),
            "session_id": session_id
        })
        
        # Ждём обработки
        await asyncio.sleep(0.5)
        
        # Проверяем состояние после обработки
        print(f"\n2.5 Проверка состояния после обработки:")
        print(f"   _google_stop_listening: {integration._google_stop_listening}")
        print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
        print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
        
    except Exception as e:
        import traceback
        print(f"   ❌ Ошибка в тесте: {e}")
        print(traceback.format_exc())
    
    print("\n" + "="*80)
    print("ТЕСТ 2 ЗАВЕРШЁН")
    print("="*80)


async def test_physical_mic_state():
    """Тест 3: Проверка физического состояния микрофона после остановки"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Проверка физического состояния микрофона после остановки")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    # Используем переменную окружения для отключения AVF
    os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"
    
    from integration.integrations.voice_recognition_integration import VoiceRecognitionConfig
    
    # Создаём конфиг с симуляцией для избежания проблем с AVF
    config = VoiceRecognitionConfig(simulate=True)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config
    )
    
    # Устанавливаем _use_avf=False перед инициализацией
    integration._use_avf = False
    
    try:
        await integration.initialize()
    except Exception as e:
        print(f"   ⚠️ Ошибка инициализации (продолжаем тест): {e}")
        # Устанавливаем минимальное состояние для теста
        integration._initialized = True
    
    print(f"\n3.1 Активация Google микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        callback_called = []
        
        def callback(recognizer, audio):
            callback_called.append(time.time())
            print(f"   🔔 Callback вызван (всего: {len(callback_called)})")
        
        integration._google_stop_listening = recognizer.listen_in_background(microphone, callback)
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        
        print(f"   ✅ Google микрофон активирован")
        print(f"   Ожидание callback'ов (5 секунд)...")
        
        # Ждём callback'и
        await asyncio.sleep(5)
        print(f"   Получено callback'ов: {len(callback_called)}")
        
        # Останавливаем микрофон
        print(f"\n3.2 Остановка Google микрофона:")
        try:
            integration._google_stop_listening(wait_for_stop=False)
            print(f"   ✅ _google_stop_listening вызван")
        except Exception as e:
            print(f"   ❌ Ошибка при остановке: {e}")
        
        # Ждём ещё немного для проверки, что callback'и не приходят
        print(f"\n3.3 Проверка callback'ов после остановки (3 секунды):")
        initial_callback_count = len(callback_called)
        await asyncio.sleep(3)
        final_callback_count = len(callback_called)
        new_callbacks = final_callback_count - initial_callback_count
        
        if new_callbacks == 0:
            print(f"   ✅ Callback'и не приходят после остановки (новых: {new_callbacks})")
        else:
            print(f"   ⚠️ Callback'и всё ещё приходят после остановки (новых: {new_callbacks})")
        
        # Очищаем состояние
        integration._google_stop_listening = None
        integration._google_recognizer = None
        integration._google_microphone = None
        
    except Exception as e:
        import traceback
        print(f"   ❌ Ошибка в тесте: {e}")
        print(traceback.format_exc())
    
    print("\n" + "="*80)
    print("ТЕСТ 3 ЗАВЕРШЁН")
    print("="*80)


async def test_state_synchronization():
    """Тест 4: Синхронизация состояния после остановки"""
    print("\n" + "="*80)
    print("ТЕСТ 4: Синхронизация состояния после остановки")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    # Используем переменную окружения для отключения AVF
    os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"
    
    from integration.integrations.voice_recognition_integration import VoiceRecognitionConfig
    
    # Создаём конфиг с симуляцией для избежания проблем с AVF
    config = VoiceRecognitionConfig(simulate=True)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=config
    )
    
    # Устанавливаем _use_avf=False перед инициализацией
    integration._use_avf = False
    
    try:
        await integration.initialize()
    except Exception as e:
        print(f"   ⚠️ Ошибка инициализации (продолжаем тест): {e}")
        # Устанавливаем минимальное состояние для теста
        integration._initialized = True
    
    print(f"\n4.1 Начальное состояние:")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
    
    # Симулируем активацию
    session_id = "test_session_456"
    state_manager.update_session_id(session_id)
    state_manager.set_microphone_state("active", session_id=session_id, reason="test_activation")
    
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        integration._google_stop_listening = recognizer.listen_in_background(microphone, dummy_callback)
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        
        print(f"\n4.2 После активации:")
        print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
        print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
        print(f"   _google_stop_listening: {integration._google_stop_listening is not None}")
        
        # Симулируем остановку при session mismatch
        print(f"\n4.3 Симуляция остановки при session mismatch:")
        state_manager.update_session_id(None)
        
        # Вызываем логику остановки напрямую
        google_mic_active = hasattr(integration, '_google_stop_listening') and integration._google_stop_listening is not None
        print(f"   google_mic_active: {google_mic_active}")
        
        if google_mic_active:
            try:
                integration._google_stop_listening(wait_for_stop=False)
                print(f"   ✅ _google_stop_listening вызван")
                
                # Очищаем состояние
                integration._google_stop_listening = None
                integration._google_recognizer = None
                integration._google_microphone = None
                
                # Обновляем состояние микрофона
                state_manager.set_microphone_state("idle", session_id=None, reason="test_stopped")
                await event_bus.publish("microphone.closed", {"session_id": session_id})
                
                print(f"   ✅ Состояние очищено")
            except Exception as e:
                print(f"   ❌ Ошибка при остановке: {e}")
        
        # Проверяем финальное состояние
        print(f"\n4.4 Финальное состояние:")
        print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
        print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
        print(f"   _google_stop_listening: {integration._google_stop_listening}")
        google_mic_active = hasattr(integration, '_google_stop_listening') and integration._google_stop_listening is not None
        print(f"   google_mic_active: {google_mic_active}")
        
        if state_manager.is_microphone_active() and not google_mic_active:
            print(f"   ⚠️ РАССИНХРОНИЗАЦИЯ: state_manager показывает active, но _google_stop_listening=None")
        elif not state_manager.is_microphone_active() and not google_mic_active:
            print(f"   ✅ СИНХРОНИЗАЦИЯ: state_manager показывает idle, _google_stop_listening=None")
        else:
            print(f"   ⚠️ НЕОЖИДАННОЕ СОСТОЯНИЕ")
        
    except Exception as e:
        import traceback
        print(f"   ❌ Ошибка в тесте: {e}")
        print(traceback.format_exc())
    
    print("\n" + "="*80)
    print("ТЕСТ 4 ЗАВЕРШЁН")
    print("="*80)


async def main():
    """Запуск всех тестов"""
    print("\n" + "="*80)
    print("ИЗОЛИРОВАННЫЕ ТЕСТЫ ДЛЯ ДИАГНОСТИКИ ЗАЛИПАНИЯ GOOGLE МИКРОФОНА")
    print("="*80)
    
    try:
        await test_google_mic_state_check()
        await asyncio.sleep(1)
        
        await test_session_mismatch_stopping()
        await asyncio.sleep(1)
        
        await test_physical_mic_state()
        await asyncio.sleep(1)
        
        await test_state_synchronization()
        
        print("\n" + "="*80)
        print("ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")
        print("="*80)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Тесты прерваны пользователем")
    except Exception as e:
        import traceback
        print(f"\n\n❌ Критическая ошибка: {e}")
        print(traceback.format_exc())


if __name__ == "__main__":
    asyncio.run(main())

