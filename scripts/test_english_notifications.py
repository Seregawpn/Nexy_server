#!/usr/bin/env python3
"""
Простой тест голосовых уведомлений об обновлении

Этот скрипт тестирует только UpdateNotificationIntegration без запуска всей системы.
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


async def test_update_notifications_simple():
    """Простой тест голосовых уведомлений"""
    
    print("🎤 Простой тест UpdateNotificationIntegration")
    print("=" * 50)
    print("🎧 СЛУШАЙТЕ: Должны прозвучать голосовые уведомления на английском!")
    print("=" * 50)
    
    # Создаем компоненты
    bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config={
            "enabled": True,
            "voice": "en-US",
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
    print("\n🔄 Тестируем голосовые уведомления...")
    
    # 1. Начало обновления
    print("\n1️⃣ Начало обновления")
    await bus.publish("updater.update_started", {"trigger": "manual"})
    print("🎧 Должно прозвучать: 'Nexy update has started. This may take up to five minutes. Please wait for completion.'")
    await asyncio.sleep(3)
    
    # 2. Прогресс скачивания
    print("\n2️⃣ Прогресс скачивания")
    await bus.publish("updater.download_progress", {
        "percent": 50, 
        "stage": "download"
    })
    print("🎧 Должно прозвучать: 'Nexy update: downloading 50 percent completed.'")
    await asyncio.sleep(3)
    
    # 3. Прогресс установки
    print("\n3️⃣ Прогресс установки")
    await bus.publish("updater.install_progress", {
        "percent": 80, 
        "stage": "install"
    })
    print("🎧 Должно прозвучать: 'Nexy update: installing 80 percent completed.'")
    await asyncio.sleep(3)
    
    # 4. Завершение обновления
    print("\n4️⃣ Завершение обновления")
    await bus.publish("updater.update_completed", {"trigger": "manual"})
    print("🎧 Должно прозвучать: 'Update completed. Nexy will restart to apply changes.'")
    await asyncio.sleep(3)
    
    # 5. Ошибка обновления
    print("\n5️⃣ Ошибка обновления")
    await bus.publish("updater.update_failed", {"error": "network timeout"})
    print("🎧 Должно прозвучать: 'Nexy update failed. Reason: network timeout. Please try again later.'")
    await asyncio.sleep(3)
    
    print("\n✅ Тест завершен")
    print("🎧 Проверьте: прозвучали ли все голосовые уведомления на английском?")
    
    # Останавливаем интеграцию
    await integration.stop()
    
    print("\n" + "=" * 50)
    print("📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 50)
    print("✅ Если вы услышали голосовые уведомления на английском:")
    print("   - 'Nexy update has started. This may take up to five minutes...'")
    print("   - 'Nexy update: downloading 50 percent completed'")
    print("   - 'Nexy update: installing 80 percent completed'")
    print("   - 'Update completed. Nexy will restart to apply changes'")
    print("   - 'Nexy update failed. Reason: network timeout...'")
    print("\n🎉 ТЕСТ ПРОЙДЕН: Голосовые уведомления работают на английском!")
    print("\n❌ Если голосовых уведомлений не было:")
    print("   - Проверьте подключение к серверу")
    print("   - Убедитесь, что сервер обрабатывает запросы TTS")
    print("   - Проверьте настройки звука в системе")
    print("   - Проверьте логи на наличие ошибок")


if __name__ == "__main__":
    try:
        asyncio.run(test_update_notifications_simple())
    except KeyboardInterrupt:
        print("\n⚠️ Тест прерван пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка в тесте: {e}")
        import traceback
        traceback.print_exc()




