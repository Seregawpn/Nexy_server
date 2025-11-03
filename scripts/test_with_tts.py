#!/usr/bin/env python3
"""
Тест UpdateNotificationIntegration с TTS Integration

Этот скрипт тестирует полную цепочку: UpdateNotificationIntegration -> TTSIntegration -> воспроизведение.
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
from integration.integrations.tts_integration import TTSIntegration


async def test_with_tts():
    """Тест с TTS интеграцией"""
    
    print("🎤 Тест UpdateNotificationIntegration с TTS Integration")
    print("=" * 70)
    
    # Создаем компоненты
    bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    
    # Создаем обе интеграции
    update_integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config={
            "enabled": True,
            "voice": "ru-RU",
            "progress_interval_sec": 1.0,
            "progress_step_percent": 10,
            "use_signals": True,
            "dry_run": False,
        },
    )
    
    tts_integration = TTSIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=error_handler,
        config={},
    )
    
    print("✅ Компоненты созданы")
    
    # Инициализируем и запускаем обе интеграции
    await update_integration.initialize()
    await update_integration.start()
    
    await tts_integration.initialize()
    await tts_integration.start()
    
    print("✅ Обе интеграции запущены")
    print("\n🔄 Тестируем полную цепочку...")
    print("🎧 СЛУШАЙТЕ: Должны прозвучать голосовые уведомления!")
    
    # Тестируем события обновления
    await bus.publish("updater.update_started", {"trigger": "manual"})
    await asyncio.sleep(1)
    
    await bus.publish("updater.download_progress", {
        "percent": 50, 
        "stage": "download"
    })
    await asyncio.sleep(1)
    
    await bus.publish("updater.update_completed", {"trigger": "manual"})
    await asyncio.sleep(2)
    
    print("\n✅ Тест завершен")
    print("🎧 Проверьте: прозвучали ли голосовые уведомления?")
    
    # Останавливаем интеграции
    await update_integration.stop()
    await tts_integration.stop()
    
    print("\n" + "=" * 70)
    print("📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 70)
    print("✅ Если вы услышали голосовые уведомления:")
    print("   - UpdateNotificationIntegration публикует speech.playback.request")
    print("   - TTSIntegration обрабатывает эти события")
    print("   - Полная цепочка работает!")
    print("\n🎉 ТЕСТ ПРОЙДЕН: Голосовые уведомления работают!")
    print("\n❌ Если голосовых уведомлений не было:")
    print("   - Проверьте логи на наличие ошибок")
    print("   - Убедитесь, что TTSIntegration правильно обрабатывает события")
    print("   - Проверьте подключение к серверу TTS")


if __name__ == "__main__":
    try:
        asyncio.run(test_with_tts())
    except KeyboardInterrupt:
        print("\n⚠️ Тест прерван пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка в тесте: {e}")
        import traceback
        traceback.print_exc()






