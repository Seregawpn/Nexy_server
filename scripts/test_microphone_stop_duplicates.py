#!/usr/bin/env python3
"""
Тест для проверки дублирования логики остановки микрофона.

Проверяет:
1. Сколько раз вызывается _google_stop_listening при одном voice.recording_stop
2. Сколько раз вызывается force_close_microphone
3. Сколько раз публикуется microphone.closed
4. Есть ли дублирование между разными ветками логики
"""

import asyncio
import sys
import os
import time
from pathlib import Path
from typing import Dict, Any, List
from unittest.mock import MagicMock, patch

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


class StopCallTracker:
    """Трекер вызовов остановки"""
    
    def __init__(self):
        self.stop_calls: List[Dict[str, Any]] = []
        self.force_close_calls: List[Dict[str, Any]] = []
        self.microphone_closed_events: List[Dict[str, Any]] = []
        self.set_idle_calls: List[Dict[str, Any]] = []
    
    def track_stop(self, wait_for_stop: bool, context: str):
        """Отслеживание вызова _google_stop_listening"""
        self.stop_calls.append({
            "time": time.time(),
            "wait_for_stop": wait_for_stop,
            "context": context
        })
    
    def track_force_close(self, reason: str, context: str):
        """Отслеживание вызова force_close_microphone"""
        self.force_close_calls.append({
            "time": time.time(),
            "reason": reason,
            "context": context
        })
    
    def track_set_idle(self, reason: str, context: str):
        """Отслеживание вызова set_microphone_state('idle')"""
        self.set_idle_calls.append({
            "time": time.time(),
            "reason": reason,
            "context": context
        })
    
    def track_microphone_closed(self, event: Dict[str, Any]):
        """Отслеживание события microphone.closed"""
        self.microphone_closed_events.append({
            "time": time.time(),
            "data": event.get("data", {})
        })
    
    def get_summary(self) -> Dict[str, Any]:
        """Получить сводку вызовов"""
        return {
            "stop_calls": len(self.stop_calls),
            "force_close_calls": len(self.force_close_calls),
            "set_idle_calls": len(self.set_idle_calls),
            "microphone_closed_events": len(self.microphone_closed_events),
            "details": {
                "stop_calls": self.stop_calls,
                "force_close_calls": self.force_close_calls,
                "set_idle_calls": self.set_idle_calls,
                "microphone_closed_events": self.microphone_closed_events
            }
        }


async def test_stop_duplicates_session_none():
    """Тест 1: Дублирование при session_id=None"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Дублирование при session_id=None")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    tracker = StopCallTracker()
    
    # Подписываемся на microphone.closed
    async def on_microphone_closed(event: Dict[str, Any]):
        tracker.track_microphone_closed(event)
    
    from integration.core.event_bus import EventPriority
    await event_bus.subscribe("microphone.closed", on_microphone_closed, priority=EventPriority.MEDIUM)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=None
    )
    
    await integration.initialize()
    
    print(f"\n1.1 Активация микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        session_id = "test_session_none"
        state_manager.update_session_id(session_id)
        
        integration._google_recording_active = True
        original_stop = recognizer.listen_in_background(microphone, dummy_callback)
        
        # Обёртка для отслеживания
        def tracked_stop(wait_for_stop=False):
            tracker.track_stop(wait_for_stop, "session_none")
            return original_stop(wait_for_stop=wait_for_stop)
        
        integration._google_stop_listening = tracked_stop
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        state_manager.set_microphone_state("active", session_id=session_id, reason="test")
        
        print(f"   ✅ Микрофон активирован")
        
        # Мокаем force_close_microphone и set_microphone_state
        original_force_close = state_manager.force_close_microphone
        original_set_state = state_manager.set_microphone_state
        
        def tracked_force_close(reason: str):
            tracker.track_force_close(reason, "session_none")
            return original_force_close(reason)
        
        def tracked_set_state(state: str, session_id=None, reason: str = None):
            if state == "idle":
                tracker.track_set_idle(reason or "unknown", "session_none")
            return original_set_state(state, session_id=session_id, reason=reason)
        
        state_manager.force_close_microphone = tracked_force_close
        state_manager.set_microphone_state = tracked_set_state
        
        # Сбрасываем session_id
        print(f"\n1.2 Сброс session_id и публикация voice.recording_stop:")
        state_manager.update_session_id(None)
        
        await event_bus.publish("voice.recording_stop", {
            "source": "session_reset",
            "timestamp": time.time(),
            "session_id": None
        })
        
        await asyncio.sleep(1)
        
        # Анализируем дублирование
        print(f"\n1.3 Анализ дублирования:")
        summary = tracker.get_summary()
        print(f"   Вызовов _google_stop_listening: {summary['stop_calls']}")
        print(f"   Вызовов force_close_microphone: {summary['force_close_calls']}")
        print(f"   Вызовов set_microphone_state('idle'): {summary['set_idle_calls']}")
        print(f"   Событий microphone.closed: {summary['microphone_closed_events']}")
        
        if summary['stop_calls'] > 1:
            print(f"   ⚠️ ДУБЛИРОВАНИЕ: _google_stop_listening вызван {summary['stop_calls']} раз")
            for i, call in enumerate(summary['details']['stop_calls']):
                print(f"      Вызов {i+1}: время={call['time']:.3f}, wait_for_stop={call['wait_for_stop']}, context={call['context']}")
        else:
            print(f"   ✅ Нет дублирования _google_stop_listening")
        
        if summary['force_close_calls'] > 1:
            print(f"   ⚠️ ДУБЛИРОВАНИЕ: force_close_microphone вызван {summary['force_close_calls']} раз")
        else:
            print(f"   ✅ Нет дублирования force_close_microphone")
        
        if summary['microphone_closed_events'] > 1:
            print(f"   ⚠️ ДУБЛИРОВАНИЕ: microphone.closed опубликовано {summary['microphone_closed_events']} раз")
        else:
            print(f"   ✅ Нет дублирования microphone.closed")
        
        # Восстанавливаем оригинальные методы
        state_manager.force_close_microphone = original_force_close
        state_manager.set_microphone_state = original_set_state
        
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


async def test_stop_duplicates_session_mismatch():
    """Тест 2: Дублирование при session mismatch"""
    print("\n" + "="*80)
    print("ТЕСТ 2: Дублирование при session mismatch")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    tracker = StopCallTracker()
    
    # Подписываемся на microphone.closed
    async def on_microphone_closed(event: Dict[str, Any]):
        tracker.track_microphone_closed(event)
    
    from integration.core.event_bus import EventPriority
    await event_bus.subscribe("microphone.closed", on_microphone_closed, priority=EventPriority.MEDIUM)
    
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
        
        session_id = "test_session_mismatch"
        state_manager.update_session_id(session_id)
        
        integration._google_recording_active = True
        original_stop = recognizer.listen_in_background(microphone, dummy_callback)
        
        # Обёртка для отслеживания
        def tracked_stop(wait_for_stop=False):
            tracker.track_stop(wait_for_stop, "session_mismatch")
            return original_stop(wait_for_stop=wait_for_stop)
        
        integration._google_stop_listening = tracked_stop
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        state_manager.set_microphone_state("active", session_id=session_id, reason="test")
        
        print(f"   ✅ Микрофон активирован, session_id={session_id}")
        
        # Мокаем force_close_microphone и set_microphone_state
        original_force_close = state_manager.force_close_microphone
        original_set_state = state_manager.set_microphone_state
        
        def tracked_force_close(reason: str):
            tracker.track_force_close(reason, "session_mismatch")
            return original_force_close(reason)
        
        def tracked_set_state(state: str, session_id=None, reason: str = None):
            if state == "idle":
                tracker.track_set_idle(reason or "unknown", "session_mismatch")
            return original_set_state(state, session_id=session_id, reason=reason)
        
        state_manager.force_close_microphone = tracked_force_close
        state_manager.set_microphone_state = tracked_set_state
        
        # Сбрасываем session_id
        print(f"\n2.2 Сброс session_id и публикация voice.recording_stop с другим session_id:")
        state_manager.update_session_id(None)
        
        await event_bus.publish("voice.recording_stop", {
            "source": "session_reset",
            "timestamp": time.time(),
            "session_id": "different_session"
        })
        
        await asyncio.sleep(1)
        
        # Анализируем дублирование
        print(f"\n2.3 Анализ дублирования:")
        summary = tracker.get_summary()
        print(f"   Вызовов _google_stop_listening: {summary['stop_calls']}")
        print(f"   Вызовов force_close_microphone: {summary['force_close_calls']}")
        print(f"   Вызовов set_microphone_state('idle'): {summary['set_idle_calls']}")
        print(f"   Событий microphone.closed: {summary['microphone_closed_events']}")
        
        if summary['stop_calls'] > 1:
            print(f"   ⚠️ ДУБЛИРОВАНИЕ: _google_stop_listening вызван {summary['stop_calls']} раз")
        else:
            print(f"   ✅ Нет дублирования _google_stop_listening")
        
        if summary['microphone_closed_events'] > 1:
            print(f"   ⚠️ ДУБЛИРОВАНИЕ: microphone.closed опубликовано {summary['microphone_closed_events']} раз")
        else:
            print(f"   ✅ Нет дублирования microphone.closed")
        
        # Восстанавливаем оригинальные методы
        state_manager.force_close_microphone = original_force_close
        state_manager.set_microphone_state = original_set_state
        
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


async def test_stop_duplicates_normal_stop():
    """Тест 3: Дублирование при нормальной остановке"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Дублирование при нормальной остановке")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    tracker = StopCallTracker()
    
    # Подписываемся на microphone.closed
    async def on_microphone_closed(event: Dict[str, Any]):
        tracker.track_microphone_closed(event)
    
    from integration.core.event_bus import EventPriority
    await event_bus.subscribe("microphone.closed", on_microphone_closed, priority=EventPriority.MEDIUM)
    
    integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=None
    )
    
    await integration.initialize()
    
    print(f"\n3.1 Активация микрофона:")
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        def dummy_callback(recognizer, audio):
            pass
        
        session_id = "test_normal_stop"
        state_manager.update_session_id(session_id)
        
        integration._google_recording_active = True
        original_stop = recognizer.listen_in_background(microphone, dummy_callback)
        
        # Обёртка для отслеживания
        def tracked_stop(wait_for_stop=False):
            tracker.track_stop(wait_for_stop, "normal_stop")
            return original_stop(wait_for_stop=wait_for_stop)
        
        integration._google_stop_listening = tracked_stop
        integration._google_recognizer = recognizer
        integration._google_microphone = microphone
        state_manager.set_microphone_state("active", session_id=session_id, reason="test")
        
        print(f"   ✅ Микрофон активирован, session_id={session_id}")
        
        # Мокаем force_close_microphone и set_microphone_state
        original_force_close = state_manager.force_close_microphone
        original_set_state = state_manager.set_microphone_state
        
        def tracked_force_close(reason: str):
            tracker.track_force_close(reason, "normal_stop")
            return original_force_close(reason)
        
        def tracked_set_state(state: str, session_id=None, reason: str = None):
            if state == "idle":
                tracker.track_set_idle(reason or "unknown", "normal_stop")
            return original_set_state(state, session_id=session_id, reason=reason)
        
        state_manager.force_close_microphone = tracked_force_close
        state_manager.set_microphone_state = tracked_set_state
        
        # Нормальная остановка
        print(f"\n3.2 Нормальная остановка:")
        await event_bus.publish("voice.recording_stop", {
            "source": "keyboard",
            "timestamp": time.time(),
            "session_id": session_id
        })
        
        await asyncio.sleep(1)
        
        # Анализируем дублирование
        print(f"\n3.3 Анализ дублирования:")
        summary = tracker.get_summary()
        print(f"   Вызовов _google_stop_listening: {summary['stop_calls']}")
        print(f"   Вызовов force_close_microphone: {summary['force_close_calls']}")
        print(f"   Вызовов set_microphone_state('idle'): {summary['set_idle_calls']}")
        print(f"   Событий microphone.closed: {summary['microphone_closed_events']}")
        
        if summary['stop_calls'] > 1:
            print(f"   ⚠️ ДУБЛИРОВАНИЕ: _google_stop_listening вызван {summary['stop_calls']} раз")
        else:
            print(f"   ✅ Нет дублирования _google_stop_listening")
        
        if summary['microphone_closed_events'] > 1:
            print(f"   ⚠️ ДУБЛИРОВАНИЕ: microphone.closed опубликовано {summary['microphone_closed_events']} раз")
        else:
            print(f"   ✅ Нет дублирования microphone.closed")
        
        # Восстанавливаем оригинальные методы
        state_manager.force_close_microphone = original_force_close
        state_manager.set_microphone_state = original_set_state
        
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


async def main():
    """Запуск всех тестов дублирования"""
    print("\n" + "="*80)
    print("ИЗОЛИРОВАННЫЕ ТЕСТЫ ДЛЯ ПРОВЕРКИ ДУБЛИРОВАНИЯ ЛОГИКИ ОСТАНОВКИ")
    print("="*80)
    
    try:
        await test_stop_duplicates_session_none()
        await asyncio.sleep(1)
        
        await test_stop_duplicates_session_mismatch()
        await asyncio.sleep(1)
        
        await test_stop_duplicates_normal_stop()
        
        print("\n" + "="*80)
        print("ВСЕ ТЕСТЫ ДУБЛИРОВАНИЯ ЗАВЕРШЕНЫ")
        print("="*80)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Тесты прерваны пользователем")
    except Exception as e:
        print(f"\n\n❌ Критическая ошибка: {e}", exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())

