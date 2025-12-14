#!/usr/bin/env python3
"""
Изолированные тесты для проверки синхронизации состояния микрофона.

Тестирует:
1. Синхронизацию между state_manager и _google_recording_active
2. Синхронизацию между state_manager и _google_stop_listening
3. Проверку рассинхронизации после различных операций
4. Восстановление синхронизации после ошибок
"""

import asyncio
import sys
import os
import time
from pathlib import Path
from typing import Dict, Any, Optional

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


def check_synchronization(integration: VoiceRecognitionIntegration, state_manager: ApplicationStateManager) -> Dict[str, Any]:
    """Проверка синхронизации состояния микрофона"""
    mic_active = state_manager.is_microphone_active()
    google_active = integration._google_recording_active if hasattr(integration, '_google_recording_active') else False
    stop_listening = integration._google_stop_listening is not None if hasattr(integration, '_google_stop_listening') else False
    
    synchronized = (mic_active == google_active == stop_listening) or (not mic_active and not google_active and not stop_listening)
    
    return {
        "synchronized": synchronized,
        "state_manager": mic_active,
        "google_recording_active": google_active,
        "stop_listening": stop_listening,
        "session_id": state_manager.get_current_session_id()
    }


async def test_state_sync_after_activation():
    """Тест 1: Синхронизация после активации"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Синхронизация после активации")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=None
    )
    
    await integration.initialize()
    
    print(f"\n1.1 Начальное состояние:")
    sync = check_synchronization(integration, state_manager)
    print(f"   {sync}")
    
    print(f"\n1.2 Активация микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        session_id = "test_activation"
        state_manager.update_session_id(session_id)
        
        # Активируем через событие
        await event_bus.publish("voice.recording_start", {
            "source": "keyboard",
            "timestamp": time.time(),
            "session_id": session_id
        })
        
        await asyncio.sleep(2)  # Ждём активации
        
        print(f"   После активации:")
        sync = check_synchronization(integration, state_manager)
        print(f"   {sync}")
        
        if sync["synchronized"]:
            print(f"   ✅ Состояние синхронизировано")
        else:
            print(f"   ❌ РАССИНХРОНИЗАЦИЯ обнаружена:")
            print(f"      state_manager: {sync['state_manager']}")
            print(f"      google_recording_active: {sync['google_recording_active']}")
            print(f"      stop_listening: {sync['stop_listening']}")
        
        # Останавливаем
        await event_bus.publish("voice.recording_stop", {
            "source": "keyboard",
            "timestamp": time.time(),
            "session_id": session_id
        })
        
        await asyncio.sleep(1)
        
        print(f"\n1.3 После остановки:")
        sync = check_synchronization(integration, state_manager)
        print(f"   {sync}")
        
        if sync["synchronized"]:
            print(f"   ✅ Состояние синхронизировано после остановки")
        else:
            print(f"   ❌ РАССИНХРОНИЗАЦИЯ после остановки")
        
    except Exception as e:
        print(f"   ❌ Ошибка в тесте: {e}", exc_info=True)
    
    print("\n" + "="*80)
    print("ТЕСТ 1 ЗАВЕРШЁН")
    print("="*80)


async def test_state_sync_after_session_reset():
    """Тест 2: Синхронизация после сброса session_id"""
    print("\n" + "="*80)
    print("ТЕСТ 2: Синхронизация после сброса session_id")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=None
    )
    
    await integration.initialize()
    
    print(f"\n2.1 Активация микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        session_id = "test_session_reset"
        state_manager.update_session_id(session_id)
        
        integration._google_recording_active = True
        integration._google_stop_listening = recognizer.listen_in_background(microphone, dummy_callback)
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        state_manager.set_microphone_state("active", session_id=session_id, reason="test")
        
        print(f"   Микрофон активирован, session_id={session_id}")
        sync = check_synchronization(integration, state_manager)
        print(f"   {sync}")
        
        # Сбрасываем session_id
        print(f"\n2.2 Сброс session_id:")
        state_manager.update_session_id(None)
        
        # Публикуем voice.recording_stop с оригинальным session_id
        await event_bus.publish("voice.recording_stop", {
            "source": "session_reset",
            "timestamp": time.time(),
            "session_id": session_id
        })
        
        await asyncio.sleep(1)
        
        print(f"   После обработки:")
        sync = check_synchronization(integration, state_manager)
        print(f"   {sync}")
        
        if sync["synchronized"]:
            print(f"   ✅ Состояние синхронизировано после сброса session_id")
        else:
            print(f"   ❌ РАССИНХРОНИЗАЦИЯ после сброса session_id:")
            print(f"      state_manager: {sync['state_manager']}")
            print(f"      google_recording_active: {sync['google_recording_active']}")
            print(f"      stop_listening: {sync['stop_listening']}")
        
        # Очищаем состояние
        integration._google_recording_active = False
        integration._google_stop_listening = None
        integration._google_recognizer = None
        integration._google_microphone = None
        
    except Exception as e:
        print(f"   ❌ Ошибка в тесте: {e}", exc_info=True)
    
    print("\n" + "="*80)
    print("ТЕСТ 2 ЗАВЕРШЁН")
    print("="*80)


async def test_state_sync_after_error():
    """Тест 3: Синхронизация после ошибки"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Синхронизация после ошибки")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=None
    )
    
    await integration.initialize()
    
    print(f"\n3.1 Симуляция ошибки при остановке:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        session_id = "test_error"
        state_manager.update_session_id(session_id)
        
        integration._google_recording_active = True
        integration._google_stop_listening = recognizer.listen_in_background(microphone, dummy_callback)
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        state_manager.set_microphone_state("active", session_id=session_id, reason="test")
        
        print(f"   Микрофон активирован")
        sync = check_synchronization(integration, state_manager)
        print(f"   {sync}")
        
        # Симулируем ошибку при остановке (устанавливаем _google_stop_listening в None)
        print(f"\n3.2 Симуляция ошибки (установка _google_stop_listening в None):")
        integration._google_stop_listening = None
        
        # Пытаемся остановить
        await event_bus.publish("voice.recording_stop", {
            "source": "keyboard",
            "timestamp": time.time(),
            "session_id": session_id
        })
        
        await asyncio.sleep(1)
        
        print(f"   После обработки с ошибкой:")
        sync = check_synchronization(integration, state_manager)
        print(f"   {sync}")
        
        if sync["synchronized"]:
            print(f"   ✅ Состояние синхронизировано после ошибки")
        else:
            print(f"   ⚠️ РАССИНХРОНИЗАЦИЯ после ошибки (ожидаемо, но должно быть восстановлено)")
            print(f"      state_manager: {sync['state_manager']}")
            print(f"      google_recording_active: {sync['google_recording_active']}")
            print(f"      stop_listening: {sync['stop_listening']}")
        
        # Очищаем состояние
        integration._google_recording_active = False
        integration._google_stop_listening = None
        integration._google_recognizer = None
        integration._google_microphone = None
        
    except Exception as e:
        print(f"   ❌ Ошибка в тесте: {e}", exc_info=True)
    
    print("\n" + "="*80)
    print("ТЕСТ 3 ЗАВЕРШЁН")
    print("="*80)


async def test_state_sync_multiple_activations():
    """Тест 4: Синхронизация при множественных активациях"""
    print("\n" + "="*80)
    print("ТЕСТ 4: Синхронизация при множественных активациях")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=None
    )
    
    await integration.initialize()
    
    print(f"\n4.1 Множественные активации и остановки:")
    try:
        import speech_recognition as sr
        
        for i in range(3):
            print(f"\n4.1.{i+1} Цикл {i+1}:")
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            
            def dummy_callback(recognizer, audio):
                pass
            
            session_id = f"test_cycle_{i}"
            state_manager.update_session_id(session_id)
            
            integration._google_recording_active = True
            integration._google_stop_listening = recognizer.listen_in_background(microphone, dummy_callback)
            integration._google_recognizer = recognizer
            integration._google_microphone = microphone
            state_manager.set_microphone_state("active", session_id=session_id, reason="test")
            
            print(f"   Активация {i+1}")
            sync = check_synchronization(integration, state_manager)
            if not sync["synchronized"]:
                print(f"   ❌ РАССИНХРОНИЗАЦИЯ на активации {i+1}: {sync}")
            
            await asyncio.sleep(0.5)
            
            # Останавливаем
            integration._google_recording_active = False
            if integration._google_stop_listening:
                integration._google_stop_listening(wait_for_stop=False)
            integration._google_stop_listening = None
            integration._google_recognizer = None
            integration._google_microphone = None
            state_manager.set_microphone_state("idle", session_id=None, reason="test")
            
            print(f"   Остановка {i+1}")
            sync = check_synchronization(integration, state_manager)
            if not sync["synchronized"]:
                print(f"   ❌ РАССИНХРОНИЗАЦИЯ на остановке {i+1}: {sync}")
            else:
                print(f"   ✅ Синхронизация восстановлена после остановки {i+1}")
            
            await asyncio.sleep(0.5)
        
        print(f"\n4.2 Финальное состояние:")
        sync = check_synchronization(integration, state_manager)
        print(f"   {sync}")
        
        if sync["synchronized"]:
            print(f"   ✅ Финальное состояние синхронизировано")
        else:
            print(f"   ❌ РАССИНХРОНИЗАЦИЯ в финальном состоянии")
        
    except Exception as e:
        print(f"   ❌ Ошибка в тесте: {e}", exc_info=True)
    
    print("\n" + "="*80)
    print("ТЕСТ 4 ЗАВЕРШЁН")
    print("="*80)


async def main():
    """Запуск всех тестов синхронизации"""
    print("\n" + "="*80)
    print("ИЗОЛИРОВАННЫЕ ТЕСТЫ ДЛЯ ПРОВЕРКИ СИНХРОНИЗАЦИИ СОСТОЯНИЯ МИКРОФОНА")
    print("="*80)
    
    try:
        await test_state_sync_after_activation()
        await asyncio.sleep(1)
        
        await test_state_sync_after_session_reset()
        await asyncio.sleep(1)
        
        await test_state_sync_after_error()
        await asyncio.sleep(1)
        
        await test_state_sync_multiple_activations()
        
        print("\n" + "="*80)
        print("ВСЕ ТЕСТЫ СИНХРОНИЗАЦИИ ЗАВЕРШЕНЫ")
        print("="*80)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Тесты прерваны пользователем")
    except Exception as e:
        print(f"\n\n❌ Критическая ошибка: {e}", exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())

