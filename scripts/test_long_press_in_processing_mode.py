#!/usr/bin/env python3
"""
Тест для проверки LONG_PRESS в режиме PROCESSING.

Проверяет, что микрофон не останавливается при LONG_PRESS в режиме PROCESSING.
"""

import asyncio
import sys
import os
import time
from pathlib import Path
from typing import Dict, Any

# Отключаем AVF для тестов (избегаем проблем с PyObjC)
os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler
from integration.integrations.input_processing_integration import InputProcessingIntegration
from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration
from integration.integrations.mode_management_integration import ModeManagementIntegration
from integration.core.event_bus import EventPriority


class SessionTracker:
    """Трекер для отслеживания изменений session_id"""
    
    def __init__(self):
        self.session_resets = []
        self.session_set = []
        self.microphone_closed = []
        self.recording_stops = []
    
    def track_session_reset(self, reason: str):
        self.session_resets.append({
            "reason": reason,
            "timestamp": time.time()
        })
    
    def track_session_set(self, session_id: Any, reason: str):
        self.session_set.append({
            "session_id": session_id,
            "reason": reason,
            "timestamp": time.time()
        })
    
    def track_microphone_closed(self, event: Dict[str, Any]):
        self.microphone_closed.append({
            "session_id": event.get("data", {}).get("session_id"),
            "timestamp": time.time()
        })
    
    def track_recording_stop(self, event: Dict[str, Any]):
        self.recording_stops.append({
            "session_id": event.get("data", {}).get("session_id"),
            "reason": event.get("data", {}).get("reason"),
            "timestamp": time.time()
        })


async def test_long_press_in_processing_mode():
    """Тест LONG_PRESS в режиме PROCESSING"""
    print("\n" + "="*80)
    print("ТЕСТ: LONG_PRESS в режиме PROCESSING")
    print("="*80)
    
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    state_manager.attach_event_bus(event_bus)
    error_handler = ErrorHandler(event_bus)
    
    # Используем переменную окружения для отключения AVF
    os.environ["NEXY_DISABLE_AVF_AUDIO"] = "true"
    
    from integration.integrations.voice_recognition_integration import VoiceRecognitionConfig
    from config.unified_config_loader import InputProcessingConfig, KeyboardConfig
    
    # Создаём конфиги
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
    
    tracker = SessionTracker()
    
    # Подписываемся на события
    async def on_session_reset(event: Dict[str, Any]):
        # Отслеживаем через патч _reset_session
        pass
    
    async def on_microphone_closed(event: Dict[str, Any]):
        tracker.track_microphone_closed(event)
    
    async def on_recording_stop(event: Dict[str, Any]):
        tracker.track_recording_stop(event)
    
    # Подписываемся на события ДО создания интеграций
    await event_bus.subscribe("microphone.closed", on_microphone_closed, priority=EventPriority.MEDIUM)
    await event_bus.subscribe("voice.recording_stop", on_recording_stop, priority=EventPriority.MEDIUM)
    
    # Создаём интеграции
    mode_management = ModeManagementIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler
    )
    await mode_management.initialize()
    
    voice_integration = VoiceRecognitionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=voice_config
    )
    await voice_integration.initialize()
    
    input_integration = InputProcessingIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config=input_config
    )
    await input_integration.initialize()
    
    # Переходим в режим PROCESSING
    print("\n1. Переход в режим PROCESSING:")
    await event_bus.publish("mode.request", {
        "target": AppMode.PROCESSING,
        "source": "test",
        "session_id": None
    })
    await asyncio.sleep(0.1)
    
    current_mode = state_manager.get_current_mode()
    print(f"   Текущий режим: {current_mode}")
    
    if current_mode != AppMode.PROCESSING:
        print(f"   ❌ ПРОБЛЕМА: Не удалось перейти в режим PROCESSING (текущий режим: {current_mode})")
        return
    
    print(f"   ✅ Режим PROCESSING установлен")
    
    # Симулируем LONG_PRESS
    print("\n2. Симуляция LONG_PRESS:")
    long_press_session_id = time.time()
    
    # Патчим _reset_session для отслеживания
    original_reset = input_integration._reset_session
    def patched_reset(reason: str):
        tracker.track_session_reset(reason)
        return original_reset(reason)
    input_integration._reset_session = patched_reset
    
    # Публикуем keyboard.long_press
    await event_bus.publish("keyboard.long_press", {
        "timestamp": long_press_session_id,
        "duration": 0.7,
        "key": "ctrl_n"
    })
    
    await asyncio.sleep(1.0)  # Ждём активации микрофона
    
    # Проверяем состояние
    print("\n3. Состояние после LONG_PRESS:")
    mic_active = state_manager.is_microphone_active()
    active_session_id = state_manager.get_current_session_id()
    recording_started = input_integration._recording_started
    
    print(f"   mic_active: {mic_active}")
    print(f"   active_session_id: {active_session_id}")
    print(f"   recording_started: {recording_started}")
    print(f"   session_resets: {len(tracker.session_resets)}")
    print(f"   microphone_closed: {len(tracker.microphone_closed)}")
    
    # Симулируем playback.cancelled (как при LONG_PRESS в PROCESSING)
    print("\n4. Симуляция playback.cancelled (как при LONG_PRESS в PROCESSING):")
    old_session_id = "old_session_123"
    
    await event_bus.publish("playback.cancelled", {
        "session_id": old_session_id,
        "reason": "keyboard_interrupt",
        "source": "input_processing"
    })
    
    await asyncio.sleep(0.2)  # Ждём обработки
    
    # Проверяем состояние после playback.cancelled
    print("\n5. Состояние после playback.cancelled:")
    mic_active_after = state_manager.is_microphone_active()
    active_session_id_after = state_manager.get_current_session_id()
    recording_started_after = input_integration._recording_started
    
    print(f"   mic_active: {mic_active_after}")
    print(f"   active_session_id: {active_session_id_after}")
    print(f"   recording_started: {recording_started_after}")
    print(f"   session_resets: {len(tracker.session_resets)}")
    print(f"   microphone_closed: {len(tracker.microphone_closed)}")
    
    # Анализ результатов
    print("\n6. Анализ результатов:")
    
    if mic_active and recording_started:
        print(f"   ✅ Микрофон активирован после LONG_PRESS")
    else:
        print(f"   ❌ ПРОБЛЕМА: Микрофон не активирован после LONG_PRESS")
    
    if mic_active_after and recording_started_after and active_session_id_after is not None:
        print(f"   ✅ Микрофон остаётся активным после playback.cancelled")
        print(f"   ✅ session_id не сброшен: {active_session_id_after}")
    else:
        print(f"   ❌ ПРОБЛЕМА: Микрофон остановлен или session_id сброшен после playback.cancelled")
        if not mic_active_after:
            print(f"      - Микрофон остановлен")
        if active_session_id_after is None:
            print(f"      - session_id сброшен в None")
        if len(tracker.session_resets) > 0:
            print(f"      - Произошёл сброс сессии: {tracker.session_resets[-1]}")
    
    if len(tracker.microphone_closed) > 0:
        print(f"   ⚠️ ПРОБЛЕМА: microphone.closed опубликовано ({len(tracker.microphone_closed)} раз)")
        for closed in tracker.microphone_closed:
            print(f"      - session_id={closed['session_id']}")
    else:
        print(f"   ✅ microphone.closed не опубликовано (микрофон не закрыт)")
    
    print("\n" + "="*80)
    print("ТЕСТ ЗАВЕРШЁН")
    print("="*80)


async def main():
    """Запуск теста"""
    try:
        await test_long_press_in_processing_mode()
    except Exception as e:
        import traceback
        print(f"❌ Ошибка теста: {e}")
        print(traceback.format_exc())


if __name__ == "__main__":
    asyncio.run(main())

