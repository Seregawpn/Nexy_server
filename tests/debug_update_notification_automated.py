#!/usr/bin/env python3
"""
Отладочный тест UpdateNotificationIntegration

Проверяем, почему события не публикуются в автоматическом тесте.
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


async def debug_test():
    """Отладочный тест"""
    
    print("🔍 Отладочный тест UpdateNotificationIntegration")
    print("=" * 60)
    
    bus = EventBus()
    state = ApplicationStateManager()
    integration = UpdateNotificationIntegration(
        bus, 
        state, 
        ErrorHandler(), 
        config={
            "enabled": True,
            "voice": "ru-RU",
            "progress_interval_sec": 0.5,
            "progress_step_percent": 10,
            "use_signals": True,
            "dry_run": True,  # Без реального воспроизведения
        }
    )

    published = []
    async def fake_publish(event_type, payload):
        print(f"🔍 DEBUG: fake_publish called with {event_type} -> {payload}")
        published.append((event_type, payload))

    # Подменяем метод publish для отслеживания событий
    original_publish = integration.event_bus.publish
    integration.event_bus.publish = fake_publish

    try:
        print("🔄 Инициализация интеграции...")
        await integration.initialize()
        print("✅ Интеграция инициализирована")
        
        print("🔄 Запуск интеграции...")
        await integration.start()
        print("✅ Интеграция запущена")

        print("\n🔄 Тестируем обработчики напрямую...")
        
        # Тестируем начало обновления
        print("1️⃣ Тест _on_update_started")
        await integration._on_update_started({"data": {"trigger": "manual"}})
        print(f"   Опубликовано событий: {len(published)}")
        
        # Тестируем прогресс скачивания
        print("2️⃣ Тест _on_progress")
        await integration._on_progress({"data": {"percent": 30, "stage": "download"}})
        print(f"   Опубликовано событий: {len(published)}")
        
        # Тестируем завершение
        print("3️⃣ Тест _on_update_completed")
        await integration._on_update_completed({"data": {"trigger": "manual"}})
        print(f"   Опубликовано событий: {len(published)}")

        print("\n📊 Анализ результатов:")
        print(f"Всего опубликованных событий: {len(published)}")
        
        for i, (event_type, payload) in enumerate(published, 1):
            print(f"  {i}. {event_type} -> {payload}")
        
        speech_events = [evt for evt, payload in published if evt == "speech.playback.request"]
        signal_events = [evt for evt, payload in published if evt == "signal.play"]
        
        print(f"\n🗣️ Голосовых уведомлений: {len(speech_events)}")
        print(f"🔊 Сигналов: {len(signal_events)}")
        
        await integration.stop()
        
    finally:
        # Восстанавливаем оригинальный метод
        integration.event_bus.publish = original_publish


if __name__ == "__main__":
    asyncio.run(debug_test())




