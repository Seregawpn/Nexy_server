#!/usr/bin/env python3
"""
Изолированные тесты для проверки race conditions при остановке микрофона.

Тестирует:
1. Race condition между остановкой и callback'ами
2. Дублирование логики остановки
3. Конфликты между разными источниками остановки
4. Последовательность событий при LONG_PRESS → SHORT_PRESS
"""

import asyncio
import sys
import os
import time
import threading
from pathlib import Path
from typing import Dict, Any, List

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


class RaceConditionMonitor:
    """Монитор для отслеживания race conditions"""
    
    def __init__(self):
        self.events: List[Dict[str, Any]] = []
        self.lock = threading.Lock()
    
    def log_event(self, event_type: str, details: Dict[str, Any]):
        """Логирование события с временной меткой"""
        with self.lock:
            self.events.append({
                "type": event_type,
                "timestamp": time.time(),
                "details": details
            })
    
    def get_events(self) -> List[Dict[str, Any]]:
        """Получить все события"""
        with self.lock:
            return self.events.copy()
    
    def clear(self):
        """Очистить события"""
        with self.lock:
            self.events.clear()


async def test_race_condition_callback_stop():
    """Тест 1: Race condition между остановкой и callback'ами"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Race condition между остановкой и callback'ами")
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
    
    monitor = RaceConditionMonitor()
    callback_called = []
    stop_called = []
    
    print(f"\n1.1 Активация микрофона с мониторингом:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def callback(recognizer, audio):
            """Callback с мониторингом"""
            callback_time = time.time()
            callback_called.append(callback_time)
            monitor.log_event("callback", {
                "time": callback_time,
                "recording_active": integration._google_recording_active if hasattr(integration, '_google_recording_active') else 'N/A',
                "stop_listening": integration._google_stop_listening is not None if hasattr(integration, '_google_stop_listening') else 'N/A'
            })
            print(f"   🔔 Callback вызван в {callback_time:.3f} (recording_active={integration._google_recording_active if hasattr(integration, '_google_recording_active') else 'N/A'})")
        
        integration._google_recording_active = True
        integration._google_stop_listening = recognizer.listen_in_background(microphone, callback)
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        
        print(f"   ✅ Микрофон активирован")
        print(f"   Ожидание callback'ов (3 секунды)...")
        
        # Ждём callback'и
        await asyncio.sleep(3)
        print(f"   Получено callback'ов: {len(callback_called)}")
        
        # Симулируем остановку в отдельной задаче (race condition)
        print(f"\n1.2 Симуляция race condition (остановка во время callback'ов):")
        
        async def stop_microphone():
            stop_time = time.time()
            stop_called.append(stop_time)
            monitor.log_event("stop_start", {"time": stop_time})
            
            # Сбрасываем флаг
            integration._google_recording_active = False
            await asyncio.sleep(0.1)
            
            # Останавливаем
            if integration._google_stop_listening:
                integration._google_stop_listening(wait_for_stop=False)
            
            monitor.log_event("stop_complete", {"time": time.time()})
            print(f"   🛑 Остановка вызвана в {stop_time:.3f}")
        
        # Запускаем остановку параллельно с callback'ами
        stop_task = asyncio.create_task(stop_microphone())
        await asyncio.sleep(2)  # Ждём ещё callback'и после остановки
        await stop_task
        
        # Анализируем события
        print(f"\n1.3 Анализ race condition:")
        events = monitor.get_events()
        callback_after_stop = 0
        callback_before_stop = 0
        
        stop_start_time = None
        for event in events:
            if event["type"] == "stop_start":
                stop_start_time = event["timestamp"]
        
        if stop_start_time:
            for event in events:
                if event["type"] == "callback":
                    if event["timestamp"] > stop_start_time:
                        callback_after_stop += 1
                        print(f"   ⚠️ Callback после остановки: {event['timestamp']:.3f} (recording_active={event['details'].get('recording_active', 'N/A')})")
                    else:
                        callback_before_stop += 1
        
        print(f"   Callback'ов до остановки: {callback_before_stop}")
        print(f"   Callback'ов после остановки: {callback_after_stop}")
        
        if callback_after_stop > 0:
            print(f"   ⚠️ ОБНАРУЖЕНА RACE CONDITION: {callback_after_stop} callback'ов пришли после остановки")
        else:
            print(f"   ✅ Race condition не обнаружена")
        
        # Очищаем состояние
        integration._google_recording_active = False
        integration._google_stop_listening = None
        integration._google_recognizer = None
        integration._google_microphone = None
        
    except Exception as e:
        print(f"   ❌ Ошибка в тесте: {e}", exc_info=True)
    
    print("\n" + "="*80)
    print("ТЕСТ 1 ЗАВЕРШЁН")
    print("="*80)


async def test_duplicate_stop_logic():
    """Тест 2: Дублирование логики остановки"""
    print("\n" + "="*80)
    print("ТЕСТ 2: Дублирование логики остановки")
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
    
    stop_calls = []
    
    print(f"\n2.1 Симуляция активации микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        integration._google_recording_active = True
        original_stop = recognizer.listen_in_background(microphone, dummy_callback)
        
        # Обёртка для отслеживания вызовов
        def tracked_stop(wait_for_stop=False):
            stop_calls.append({
                "time": time.time(),
                "wait_for_stop": wait_for_stop
            })
            return original_stop(wait_for_stop=wait_for_stop)
        
        integration._google_stop_listening = tracked_stop
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        
        session_id = "test_session_123"
        state_manager.update_session_id(session_id)
        state_manager.set_microphone_state("active", session_id=session_id, reason="test")
        
        print(f"   ✅ Микрофон активирован")
        
        # Симулируем несколько источников остановки одновременно
        print(f"\n2.2 Симуляция множественных источников остановки:")
        
        async def stop_from_session_none():
            """Остановка из-за session_id=None"""
            await asyncio.sleep(0.1)
            state_manager.update_session_id(None)
            await event_bus.publish("voice.recording_stop", {
                "source": "session_reset",
                "timestamp": time.time(),
                "session_id": None
            })
        
        async def stop_from_session_mismatch():
            """Остановка из-за session mismatch"""
            await asyncio.sleep(0.15)
            await event_bus.publish("voice.recording_stop", {
                "source": "session_reset",
                "timestamp": time.time(),
                "session_id": "different_session"
            })
        
        async def stop_from_normal():
            """Нормальная остановка"""
            await asyncio.sleep(0.2)
            await event_bus.publish("voice.recording_stop", {
                "source": "keyboard",
                "timestamp": time.time(),
                "session_id": session_id
            })
        
        # Запускаем все остановки параллельно
        await asyncio.gather(
            stop_from_session_none(),
            stop_from_session_mismatch(),
            stop_from_normal(),
            return_exceptions=True
        )
        
        await asyncio.sleep(1)  # Ждём обработки
        
        # Анализируем вызовы остановки
        print(f"\n2.3 Анализ дублирования:")
        print(f"   Всего вызовов _google_stop_listening: {len(stop_calls)}")
        
        if len(stop_calls) > 1:
            print(f"   ⚠️ ОБНАРУЖЕНО ДУБЛИРОВАНИЕ: {len(stop_calls)} вызовов остановки")
            for i, call in enumerate(stop_calls):
                print(f"      Вызов {i+1}: время={call['time']:.3f}, wait_for_stop={call['wait_for_stop']}")
        else:
            print(f"   ✅ Дублирование не обнаружено")
        
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


async def test_conflicting_stop_sources():
    """Тест 3: Конфликты между разными источниками остановки"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Конфликты между разными источниками остановки")
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
    
    print(f"\n3.1 Симуляция активации микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        integration._google_recording_active = True
        integration._google_stop_listening = recognizer.listen_in_background(microphone, dummy_callback)
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        
        session_id = "test_session_456"
        state_manager.update_session_id(session_id)
        state_manager.set_microphone_state("active", session_id=session_id, reason="test")
        
        print(f"   ✅ Микрофон активирован, session_id={session_id}")
        
        # Симулируем конфликтующие источники остановки
        print(f"\n3.2 Симуляция конфликтующих источников:")
        
        # Сценарий 1: session_id сбрасывается в None ДО voice.recording_stop
        print(f"\n3.2.1 Сценарий 1: session_id сбрасывается ДО voice.recording_stop")
        state_manager.update_session_id(None)
        print(f"   session_id сброшен в None")
        
        await event_bus.publish("voice.recording_stop", {
            "source": "session_reset",
            "timestamp": time.time(),
            "session_id": session_id  # Оригинальный session_id
        })
        
        await asyncio.sleep(0.5)
        
        print(f"   После обработки:")
        print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
        print(f"   integration._google_recording_active: {integration._google_recording_active if hasattr(integration, '_google_recording_active') else 'N/A'}")
        print(f"   integration._google_stop_listening: {integration._google_stop_listening is not None if hasattr(integration, '_google_stop_listening') else 'N/A'}")
        
        # Сценарий 2: session_id сбрасывается ПОСЛЕ voice.recording_stop
        print(f"\n3.2.2 Сценарий 2: session_id сбрасывается ПОСЛЕ voice.recording_stop")
        
        # Реактивируем микрофон
        integration._google_recording_active = True
        integration._google_stop_listening = recognizer.listen_in_background(microphone, dummy_callback)
        session_id_2 = "test_session_789"
        state_manager.update_session_id(session_id_2)
        state_manager.set_microphone_state("active", session_id=session_id_2, reason="test")
        
        await event_bus.publish("voice.recording_stop", {
            "source": "keyboard",
            "timestamp": time.time(),
            "session_id": session_id_2
        })
        
        # Сбрасываем session_id ПОСЛЕ публикации события
        await asyncio.sleep(0.1)
        state_manager.update_session_id(None)
        
        await asyncio.sleep(0.5)
        
        print(f"   После обработки:")
        print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
        print(f"   integration._google_recording_active: {integration._google_recording_active if hasattr(integration, '_google_recording_active') else 'N/A'}")
        print(f"   integration._google_stop_listening: {integration._google_stop_listening is not None if hasattr(integration, '_google_stop_listening') else 'N/A'}")
        
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


async def test_long_press_short_press_sequence():
    """Тест 4: Последовательность событий при LONG_PRESS → SHORT_PRESS"""
    print("\n" + "="*80)
    print("ТЕСТ 4: Последовательность событий при LONG_PRESS → SHORT_PRESS")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    voice_integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=None
    )
    
    input_integration = InputProcessingIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=None
    )
    
    await voice_integration.initialize()
    await input_integration.initialize()
    
    event_sequence = []
    
    # Подписываемся на события для отслеживания последовательности
    async def track_event(event_name: str):
        async def handler(event: Dict[str, Any]):
            event_sequence.append({
                "event": event_name,
                "time": time.time(),
                "data": event.get("data", {})
            })
        return handler
    
    # Подписываемся на ключевые события
    event_bus.subscribe("voice.recording_start", await track_event("voice.recording_start"), priority=1)
    event_bus.subscribe("voice.recording_stop", await track_event("voice.recording_stop"), priority=1)
    event_bus.subscribe("playback.cancelled", await track_event("playback.cancelled"), priority=1)
    event_bus.subscribe("microphone.opened", await track_event("microphone.opened"), priority=1)
    event_bus.subscribe("microphone.closed", await track_event("microphone.closed"), priority=1)
    
    print(f"\n4.1 Симуляция LONG_PRESS:")
    session_id = f"test_{int(time.time())}"
    
    await event_bus.publish("keyboard.long_press", {
        "timestamp": time.time(),
        "duration": 0.6
    })
    
    await asyncio.sleep(2)  # Ждём активации микрофона
    
    print(f"   После LONG_PRESS:")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
    
    # Симулируем SHORT_PRESS (прерывание)
    print(f"\n4.2 Симуляция SHORT_PRESS (прерывание):")
    
    # Сбрасываем session_id (как в _reset_session)
    state_manager.update_session_id(None)
    print(f"   session_id сброшен в None")
    
    # Публикуем playback.cancelled
    await event_bus.publish("playback.cancelled", {
        "source": "keyboard",
        "session_id": session_id
    })
    
    await asyncio.sleep(0.2)
    
    # Публикуем voice.recording_stop с оригинальным session_id
    await event_bus.publish("voice.recording_stop", {
        "source": "session_reset",
        "timestamp": time.time(),
        "reason": "playback_playback.cancelled",
        "session_id": session_id
    })
    
    await asyncio.sleep(1)  # Ждём обработки
    
    # Анализируем последовательность событий
    print(f"\n4.3 Анализ последовательности событий:")
    for i, event in enumerate(event_sequence):
        print(f"   {i+1}. {event['event']} в {event['time']:.3f}: {event['data']}")
    
    # Проверяем финальное состояние
    print(f"\n4.4 Финальное состояние:")
    print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
    print(f"   state_manager.get_current_session_id(): {state_manager.get_current_session_id()}")
    print(f"   voice_integration._google_recording_active: {voice_integration._google_recording_active if hasattr(voice_integration, '_google_recording_active') else 'N/A'}")
    print(f"   voice_integration._google_stop_listening: {voice_integration._google_stop_listening is not None if hasattr(voice_integration, '_google_stop_listening') else 'N/A'}")
    
    # Проверяем синхронизацию
    mic_active = state_manager.is_microphone_active()
    google_active = voice_integration._google_recording_active if hasattr(voice_integration, '_google_recording_active') else False
    stop_listening = voice_integration._google_stop_listening is not None if hasattr(voice_integration, '_google_stop_listening') else False
    
    if mic_active or google_active or stop_listening:
        print(f"   ❌ ПРОБЛЕМА: Микрофон всё ещё активен после SHORT_PRESS")
        print(f"      state_manager: {mic_active}, google_recording_active: {google_active}, stop_listening: {stop_listening}")
    else:
        print(f"   ✅ Микрофон полностью остановлен после SHORT_PRESS")
    
    print("\n" + "="*80)
    print("ТЕСТ 4 ЗАВЕРШЁН")
    print("="*80)


async def test_concurrent_stop_attempts():
    """Тест 5: Одновременные попытки остановки из разных мест"""
    print("\n" + "="*80)
    print("ТЕСТ 5: Одновременные попытки остановки из разных мест")
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
    
    stop_attempts = []
    
    print(f"\n5.1 Активация микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        integration._google_recording_active = True
        original_stop = recognizer.listen_in_background(microphone, dummy_callback)
        
        # Обёртка для отслеживания вызовов
        def tracked_stop(wait_for_stop=False):
            stop_attempts.append({
                "time": time.time(),
                "wait_for_stop": wait_for_stop,
                "thread": threading.current_thread().name
            })
            return original_stop(wait_for_stop=wait_for_stop)
        
        integration._google_stop_listening = tracked_stop
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        
        session_id = "test_session_concurrent"
        state_manager.update_session_id(session_id)
        state_manager.set_microphone_state("active", session_id=session_id, reason="test")
        
        print(f"   ✅ Микрофон активирован")
        
        # Симулируем одновременные попытки остановки
        print(f"\n5.2 Одновременные попытки остановки:")
        
        async def stop_attempt_1():
            """Попытка 1: session_id=None"""
            await asyncio.sleep(0.05)
            state_manager.update_session_id(None)
            await event_bus.publish("voice.recording_stop", {
                "source": "session_reset",
                "timestamp": time.time(),
                "session_id": None
            })
        
        async def stop_attempt_2():
            """Попытка 2: session mismatch"""
            await asyncio.sleep(0.05)
            await event_bus.publish("voice.recording_stop", {
                "source": "session_reset",
                "timestamp": time.time(),
                "session_id": "different_session"
            })
        
        async def stop_attempt_3():
            """Попытка 3: нормальная остановка"""
            await asyncio.sleep(0.05)
            await event_bus.publish("voice.recording_stop", {
                "source": "keyboard",
                "timestamp": time.time(),
                "session_id": session_id
            })
        
        # Запускаем все попытки одновременно
        await asyncio.gather(
            stop_attempt_1(),
            stop_attempt_2(),
            stop_attempt_3(),
            return_exceptions=True
        )
        
        await asyncio.sleep(1)  # Ждём обработки
        
        # Анализируем попытки остановки
        print(f"\n5.3 Анализ попыток остановки:")
        print(f"   Всего попыток остановки: {len(stop_attempts)}")
        
        if len(stop_attempts) > 1:
            print(f"   ⚠️ ОБНАРУЖЕНО МНОЖЕСТВЕННЫХ ПОПЫТОК: {len(stop_attempts)}")
            for i, attempt in enumerate(stop_attempts):
                print(f"      Попытка {i+1}: время={attempt['time']:.3f}, wait_for_stop={attempt['wait_for_stop']}, thread={attempt['thread']}")
        else:
            print(f"   ✅ Только одна попытка остановки (защита от дублирования работает)")
        
        # Проверяем финальное состояние
        print(f"\n5.4 Финальное состояние:")
        print(f"   state_manager.is_microphone_active(): {state_manager.is_microphone_active()}")
        print(f"   integration._google_recording_active: {integration._google_recording_active if hasattr(integration, '_google_recording_active') else 'N/A'}")
        print(f"   integration._google_stop_listening: {integration._google_stop_listening is not None if hasattr(integration, '_google_stop_listening') else 'N/A'}")
        
        # Очищаем состояние
        integration._google_recording_active = False
        integration._google_stop_listening = None
        integration._google_recognizer = None
        integration._google_microphone = None
        
    except Exception as e:
        print(f"   ❌ Ошибка в тесте: {e}", exc_info=True)
    
    print("\n" + "="*80)
    print("ТЕСТ 5 ЗАВЕРШЁН")
    print("="*80)


async def main():
    """Запуск всех тестов race conditions"""
    print("\n" + "="*80)
    print("ИЗОЛИРОВАННЫЕ ТЕСТЫ ДЛЯ ПРОВЕРКИ RACE CONDITIONS И КОНФЛИКТОВ")
    print("="*80)
    
    try:
        await test_race_condition_callback_stop()
        await asyncio.sleep(1)
        
        await test_duplicate_stop_logic()
        await asyncio.sleep(1)
        
        await test_conflicting_stop_sources()
        await asyncio.sleep(1)
        
        await test_long_press_short_press_sequence()
        await asyncio.sleep(1)
        
        await test_concurrent_stop_attempts()
        
        print("\n" + "="*80)
        print("ВСЕ ТЕСТЫ RACE CONDITIONS ЗАВЕРШЕНЫ")
        print("="*80)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Тесты прерваны пользователем")
    except Exception as e:
        print(f"\n\n❌ Критическая ошибка: {e}", exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())

