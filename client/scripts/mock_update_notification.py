#!/usr/bin/env python3
"""
Мини-скрипт для эмуляции событий обновления с реальным воспроизведением речи

Этот скрипт позволяет изолированно протестировать UpdateNotificationIntegration
с реальным воспроизведением речи без необходимости реального скачивания обновления.
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

# Конфигурация для тестирования
CONFIG = {
    "enabled": True,
    "voice": "ru-RU",  # Русский язык для тестирования
    "progress_interval_sec": 1.0,
    "progress_step_percent": 10,
    "use_signals": True,  # Включаем сигналы для полного тестирования
    "dry_run": False,  # РЕАЛЬНОЕ воспроизведение речи
}

async def main():
    """Основная функция тестирования"""
    
    print("🎤 Тест UpdateNotificationIntegration с реальным воспроизведением")
    print("=" * 70)
    print(f"Конфигурация: {CONFIG}")
    print("=" * 70)
    
    # Создаем компоненты
    bus = EventBus()
    state_manager = ApplicationStateManager()
    integration = UpdateNotificationIntegration(
        event_bus=bus,
        state_manager=state_manager,
        error_handler=ErrorHandler(),
        config=CONFIG,
    )
    
    print("✅ Компоненты созданы")
    
    # Инициализируем и запускаем интеграцию
    await integration.initialize()
    await integration.start()
    
    print("✅ Интеграция запущена")
    print("\n🔄 Начинаем эмуляцию процесса обновления...")
    print("🎧 СЛУШАЙТЕ: Должны прозвучать голосовые уведомления!")
    
    # 1. Начало обновления
    print("\n1️⃣ Начало обновления")
    await bus.publish("updater.update_started", {"trigger": "manual"})
    await asyncio.sleep(2)  # Даем время на воспроизведение
    
    # 2. Прогресс скачивания
    print("\n2️⃣ Прогресс скачивания")
    for percent in (10, 20, 30, 40, 50):
        print(f"   📥 Скачивание: {percent}%")
        await bus.publish("updater.download_progress", {
            "percent": percent, 
            "stage": "download"
        })
        await asyncio.sleep(1.5)  # Интервал между уведомлениями
    
    # 3. Прогресс установки
    print("\n3️⃣ Прогресс установки")
    for percent in (60, 80, 100):
        print(f"   📦 Установка: {percent}%")
        await bus.publish("updater.install_progress", {
            "percent": percent, 
            "stage": "install"
        })
        await asyncio.sleep(1.5)
    
    # 4. Завершение обновления
    print("\n4️⃣ Завершение обновления")
    await bus.publish("updater.update_completed", {"trigger": "manual"})
    await asyncio.sleep(3)  # Даем время на финальное уведомление
    
    print("\n✅ Эмуляция завершена")
    print("🎧 Проверьте: прозвучали ли голосовые уведомления?")
    
    # Останавливаем интеграцию
    await integration.stop()
    print("🛑 Интеграция остановлена")
    
    print("\n" + "=" * 70)
    print("📊 РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 70)
    print("✅ Если вы услышали голосовые уведомления:")
    print("   - 'Началось обновление Nexy...'")
    print("   - 'Обновление Nexy: скачивание X процентов'")
    print("   - 'Обновление Nexy: установка X процентов'")
    print("   - 'Обновление завершено. Nexy перезапустится...'")
    print("   - Звуковые сигналы (update_start, update_success)")
    print("\n🎉 ТЕСТ ПРОЙДЕН: Голосовые уведомления работают!")
    print("\n❌ Если голосовых уведомлений не было:")
    print("   - Проверьте настройки звука в системе")
    print("   - Убедитесь, что SpeechPlaybackIntegration работает")
    print("   - Проверьте подключение к серверу TTS")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️ Тест прерван пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка в тесте: {e}")
        import traceback
        traceback.print_exc()




