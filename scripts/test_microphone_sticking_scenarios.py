#!/usr/bin/env python3
"""
Тест сценариев залипания микрофона.

Тестирует критические сценарии:
1. LONG_PRESS → SHORT_PRESS (прерывание записи)
2. LONG_PRESS → playback.cancelled → voice.recording_stop с session mismatch
3. Повторная активация после остановки
4. Проверка физического состояния микрофона
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
from integration.integrations.input_processing_integration import InputProcessingIntegration
from config.unified_config_loader import UnifiedConfigLoader


async def test_long_press_short_press_scenario():
    """Тест сценария: LONG_PRESS → SHORT_PRESS"""
    print("\n" + "="*80)
    print("ТЕСТ СЦЕНАРИЯ: LONG_PRESS → SHORT_PRESS")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    # Используем переменную окружения для отключения AVF
    os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"
    
    from integration.integrations.voice_recognition_integration import VoiceRecognitionConfig
    from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
    
    # Создаём конфиги для тестов
    voice_config = VoiceRecognitionConfig(simulate=True)
    keyboard_config = KeyboardConfig(
        key_to_monitor="ctrl_n",
        short_press_threshold=0.1,
        long_press_threshold=0.6,
        event_cooldown=0.1,
        hold_check_interval=0.05,
        debounce_time=0.1,
        backend="auto"
    )
    input_config = InputProcessingConfig(
        keyboard=keyboard_config,
        enable_keyboard_monitoring=True,
        auto_start=True,
        keyboard_backend="auto",
        min_recording_duration_sec=0.6,
        playback_idle_grace_sec=0.3,
        playback_wait_timeout_sec=5.0,
        recording_prestart_delay_sec=0.3,
        mic_reset_timeout_sec=60.0
    )
    
    voice_integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=voice_config
    )

    input_integration = InputProcessingIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=input_config
    )
    
    await voice_integration.initialize()
    await input_integration.initialize()
    
    # Симулируем LONG_PRESS
    print(f"\n1. Симуляция LONG_PRESS:")
    session_id = f"test_{int(time.time())}"
    
    await event_bus.publish("keyboard.long_press", {
        "timestamp": time.time(),
        "duration": 0.6
    })
    
    await asyncio.sleep(2)  # Ждём активации микрофона
    
    print(f"   После LONG_PRESS:")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
    print(f"   voice_integration._google_stop_listening: {voice_integration._google_stop_listening is not None if hasattr(voice_integration, '_google_stop_listening') else 'N/A'}")
    
    # Симулируем SHORT_PRESS (прерывание)
    print(f"\n2. Симуляция SHORT_PRESS (прерывание):")
    
    # Сбрасываем session_id (как в _reset_session)
    state_manager.update_session_id(None)
    print(f"   session_id сброшен в None")
    
    # Публикуем playback.cancelled
    await event_bus.publish("playback.cancelled", {
        "source": "keyboard",
        "session_id": session_id
    })
    
    await asyncio.sleep(0.5)
    
    # Публикуем voice.recording_stop с оригинальным session_id
    await event_bus.publish("voice.recording_stop", {
        "source": "session_reset",
        "timestamp": time.time(),
        "reason": "playback_playback.cancelled",
        "session_id": session_id
    })
    
    await asyncio.sleep(1)  # Ждём обработки
    
    print(f"   После SHORT_PRESS:")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
    print(f"   voice_integration._google_stop_listening: {voice_integration._google_stop_listening is not None if hasattr(voice_integration, '_google_stop_listening') else 'N/A'}")
    
    # Проверяем, что микрофон действительно остановлен
    if state_manager.is_microphone_active():
        print(f"   ❌ ПРОБЛЕМА: Микрофон всё ещё активен после SHORT_PRESS")
    else:
        print(f"   ✅ Микрофон остановлен после SHORT_PRESS")
    
    print("\n" + "="*80)
    print("ТЕСТ СЦЕНАРИЯ ЗАВЕРШЁН")
    print("="*80)


async def test_repeated_activation():
    """Тест повторной активации после остановки"""
    print("\n" + "="*80)
    print("ТЕСТ: Повторная активация после остановки")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    # Используем переменную окружения для отключения AVF
    os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"
    
    from integration.integrations.voice_recognition_integration import VoiceRecognitionConfig
    
    voice_config = VoiceRecognitionConfig(simulate=True)
    
    voice_integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=voice_config
    )
    
    await voice_integration.initialize()
    
    # Первая активация
    print(f"\n1. Первая активация:")
    session_id_1 = f"test_1_{int(time.time())}"
    
    await event_bus.publish("voice.recording_start", {
        "source": "keyboard",
        "timestamp": time.time(),
        "session_id": session_id_1
    })
    
    await asyncio.sleep(2)
    
    print(f"   После первой активации:")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    print(f"   voice_integration._google_stop_listening: {voice_integration._google_stop_listening is not None if hasattr(voice_integration, '_google_stop_listening') else 'N/A'}")
    
    # Останавливаем первую активацию
    print(f"\n2. Остановка первой активации:")
    await event_bus.publish("voice.recording_stop", {
        "source": "keyboard",
        "timestamp": time.time(),
        "session_id": session_id_1
    })
    
    await asyncio.sleep(1)
    
    print(f"   После остановки:")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    print(f"   voice_integration._google_stop_listening: {voice_integration._google_stop_listening is not None if hasattr(voice_integration, '_google_stop_listening') else 'N/A'}")
    
    # Вторая активация
    print(f"\n3. Вторая активация:")
    session_id_2 = f"test_2_{int(time.time())}"
    
    await event_bus.publish("voice.recording_start", {
        "source": "keyboard",
        "timestamp": time.time(),
        "session_id": session_id_2
    })
    
    await asyncio.sleep(2)
    
    print(f"   После второй активации:")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
    print(f"   voice_integration._google_stop_listening: {voice_integration._google_stop_listening is not None if hasattr(voice_integration, '_google_stop_listening') else 'N/A'}")
    
    # Проверяем, что вторая активация работает корректно
    if state_manager.is_microphone_active() and state_manager.get_current_session_id() == session_id_2:
        print(f"   ✅ Вторая активация работает корректно")
    else:
        print(f"   ❌ ПРОБЛЕМА: Вторая активация не работает корректно")
    
    print("\n" + "="*80)
    print("ТЕСТ ЗАВЕРШЁН")
    print("="*80)


async def test_physical_mic_check_after_stop():
    """Тест проверки физического состояния микрофона после остановки"""
    print("\n" + "="*80)
    print("ТЕСТ: Проверка физического состояния микрофона после остановки")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    # Используем переменную окружения для отключения AVF
    os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"
    
    from integration.integrations.voice_recognition_integration import VoiceRecognitionConfig
    
    voice_config = VoiceRecognitionConfig(simulate=True)
    
    voice_integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=voice_config
    )
    
    await voice_integration.initialize()
    
    # Активируем микрофон
    print(f"\n1. Активация микрофона:")
    session_id = f"test_{int(time.time())}"
    
    await event_bus.publish("voice.recording_start", {
        "source": "keyboard",
        "timestamp": time.time(),
        "session_id": session_id
    })
    
    await asyncio.sleep(2)
    
    # Проверяем состояние перед остановкой
    print(f"\n2. Состояние перед остановкой:")
    google_mic_active = hasattr(voice_integration, '_google_stop_listening') and voice_integration._google_stop_listening is not None
    print(f"   google_mic_active: {google_mic_active}")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    
    # Останавливаем с session mismatch
    print(f"\n3. Остановка с session mismatch:")
    state_manager.update_session_id(None)
    
    await event_bus.publish("voice.recording_stop", {
        "source": "session_reset",
        "timestamp": time.time(),
        "reason": "test_mismatch",
        "session_id": session_id
    })
    
    await asyncio.sleep(1)
    
    # Проверяем состояние после остановки
    print(f"\n4. Состояние после остановки:")
    google_mic_active = hasattr(voice_integration, '_google_stop_listening') and voice_integration._google_stop_listening is not None
    print(f"   google_mic_active: {google_mic_active}")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    print(f"   voice_integration._google_stop_listening: {voice_integration._google_stop_listening}")
    
    # ✅ КРИТИЧНО: Дополнительная проверка через get_microphone_state
    mic_state, mic_session_id = state_manager.get_microphone_state()
    print(f"   state_manager.get_microphone_state(): state={mic_state}, session_id={mic_session_id}")
    
    # Проверяем синхронизацию
    if google_mic_active and state_manager.is_microphone_active():
        print(f"   ❌ ПРОБЛЕМА: Микрофон всё ещё активен (и Google, и state_manager)")
    elif not google_mic_active and not state_manager.is_microphone_active():
        print(f"   ✅ Микрофон остановлен (и Google, и state_manager)")
    elif google_mic_active and not state_manager.is_microphone_active():
        print(f"   ⚠️ РАССИНХРОНИЗАЦИЯ: Google активен, но state_manager показывает idle")
    elif not google_mic_active and state_manager.is_microphone_active():
        print(f"   ⚠️ РАССИНХРОНИЗАЦИЯ: Google остановлен, но state_manager показывает active")
        # ✅ КРИТИЧНО: Принудительно синхронизируем состояние
        print(f"   🔧 Принудительная синхронизация состояния...")
        state_manager.force_close_microphone(reason="test_sync_after_mismatch")
        await asyncio.sleep(0.1)
        print(f"   После синхронизации: state_manager.is_microphone_active()={state_manager.is_microphone_active()}")
        if not state_manager.is_microphone_active():
            print(f"   ✅ Синхронизация восстановлена")
        else:
            print(f"   ❌ Синхронизация НЕ восстановлена")
    
    print("\n" + "="*80)
    print("ТЕСТ ЗАВЕРШЁН")
    print("="*80)


async def main():
    """Запуск всех тестов сценариев"""
    print("\n" + "="*80)
    print("ТЕСТЫ СЦЕНАРИЕВ ЗАЛИПАНИЯ МИКРОФОНА")
    print("="*80)
    
    try:
        await test_long_press_short_press_scenario()
        await asyncio.sleep(2)
        
        await test_repeated_activation()
        await asyncio.sleep(2)
        
        await test_physical_mic_check_after_stop()
        
        print("\n" + "="*80)
        print("ВСЕ ТЕСТЫ СЦЕНАРИЕВ ЗАВЕРШЕНЫ")
        print("="*80)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Тесты прерваны пользователем")
    except Exception as e:
        import traceback
        print(f"\n\n❌ Критическая ошибка: {e}")
        print(traceback.format_exc())


if __name__ == "__main__":
    asyncio.run(main())

