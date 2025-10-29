#!/usr/bin/env python3
"""
Диагностический скрипт для проверки полной цепочки речи

Этот скрипт проверяет, кто обрабатывает события speech.playback.request
и как работает полная цепочка от события до воспроизведения.
"""

import asyncio
import sys
import os

# Добавляем пути для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.update_notification_integration import UpdateNotificationIntegration


class DiagnosticEventBus(EventBus):
    """Диагностический EventBus для отслеживания всех событий"""
    
    def __init__(self):
        super().__init__()
        self.published_events = []
        self.subscribers = {}
    
    async def publish(self, event_type: str, payload) -> None:
        print(f"📢 PUBLISH: {event_type} -> {payload}")
        self.published_events.append((event_type, payload))
        await super().publish(event_type, payload)
    
    async def subscribe(self, event_type: str, handler, priority=None) -> None:
        print(f"📝 SUBSCRIBE: {event_type} -> {handler.__name__}")
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler.__name__)
        await super().subscribe(event_type, handler, priority)


async def diagnostic_test():
    """Диагностический тест полной цепочки речи"""
    
    print("🔍 Диагностический тест полной цепочки речи")
    print("=" * 70)
    
    bus = DiagnosticEventBus()
    state_manager = ApplicationStateManager()
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "voice": "ru-RU",
            "progress_interval_sec": 1.0,
            "progress_step_percent": 10,
            "use_signals": True,
            "dry_run": False,
        },
    )
    
    print("✅ Компоненты созданы")
    
    # Инициализируем и запускаем интеграцию
    await integration.initialize()
    await integration.start()
    
    print("✅ Интеграция запущена")
    print("\n📊 Анализ подписок:")
    for event_type, handlers in bus.subscribers.items():
        print(f"  {event_type}: {handlers}")
    
    print("\n🔄 Тестируем одно событие обновления...")
    await bus.publish("updater.update_started", {"trigger": "manual"})
    
    print("\n📊 Анализ опубликованных событий:")
    for i, (event_type, payload) in enumerate(bus.published_events, 1):
        print(f"  {i}. {event_type} -> {payload}")
    
    # Проверяем, есть ли подписчики на speech.playback.request
    speech_subscribers = bus.subscribers.get("speech.playback.request", [])
    print(f"\n🔍 Подписчики на speech.playback.request: {speech_subscribers}")
    
    if not speech_subscribers:
        print("\n❌ ПРОБЛЕМА: Нет подписчиков на speech.playback.request!")
        print("💡 РЕШЕНИЕ: Нужно создать интеграцию, которая обрабатывает эти события")
        print("   Возможные варианты:")
        print("   1. Добавить обработку в SpeechPlaybackIntegration")
        print("   2. Создать новую интеграцию для TTS")
        print("   3. Использовать другой тип события")
    else:
        print(f"\n✅ Есть {len(speech_subscribers)} подписчик(ов) на speech.playback.request")
    
    await integration.stop()
    
    print("\n" + "=" * 70)
    print("📊 ДИАГНОСТИЧЕСКИЙ ОТЧЕТ")
    print("=" * 70)
    print(f"📢 Всего событий опубликовано: {len(bus.published_events)}")
    print(f"📝 Всего подписок: {sum(len(handlers) for handlers in bus.subscribers.values())}")
    
    speech_events = [evt for evt, payload in bus.published_events if evt == "speech.playback.request"]
    signal_events = [evt for evt, payload in bus.published_events if evt == "signal.play"]
    
    print(f"🗣️ Голосовых уведомлений: {len(speech_events)}")
    print(f"🔊 Сигналов: {len(signal_events)}")
    
    if speech_events and not speech_subscribers:
        print("\n⚠️ ВЫВОД: События speech.playback.request публикуются, но никто их не обрабатывает!")
        print("   Это объясняет, почему голосовые уведомления не воспроизводятся.")
    elif speech_events and speech_subscribers:
        print("\n✅ ВЫВОД: События публикуются и есть подписчики - цепочка должна работать!")
    else:
        print("\n❓ ВЫВОД: События speech.playback.request не публикуются")


if __name__ == "__main__":
    asyncio.run(diagnostic_test())

