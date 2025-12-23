#!/usr/bin/env python3
"""
Тест мониторинга разрешений - проверка polling механизма
"""

import asyncio
import sys
from pathlib import Path

# Добавляем корень проекта в PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from modules.permissions.first_run.status_checker import (
    check_accessibility_status,
    check_input_monitoring_status,
    PermissionStatus,
)


async def test_permission_monitoring():
    """
    Тестирует механизм мониторинга разрешений.

    Запускает polling каждые 3 секунды и отображает изменения статусов.
    """
    print("=" * 70)
    print("🔍 ТЕСТ МОНИТОРИНГА РАЗРЕШЕНИЙ")
    print("=" * 70)
    print()
    print("Этот тест симулирует работу PermissionRestartIntegration._permission_monitoring_loop()")
    print("Проверяет статусы разрешений каждые 3 секунды и выводит изменения")
    print()
    print("Инструкции:")
    print("1. Запустите тест")
    print("2. Откройте System Settings → Privacy & Security → Accessibility")
    print("3. Включите/выключите Nexy.app")
    print("4. Наблюдайте как тест обнаруживает изменения")
    print()
    print("Нажмите Ctrl+C для остановки")
    print("=" * 70)
    print()

    # Инициализация - получаем начальное состояние
    last_known_statuses = {
        "accessibility": None,
        "input_monitoring": None,
    }

    try:
        last_known_statuses["accessibility"] = check_accessibility_status()
        last_known_statuses["input_monitoring"] = check_input_monitoring_status()

        print(f"📊 Начальное состояние:")
        print(f"   • Accessibility:      {last_known_statuses['accessibility'].value}")
        print(f"   • Input Monitoring:   {last_known_statuses['input_monitoring'].value}")
        print()
        print("🔄 Начинаем мониторинг (проверка каждые 3 секунды)...")
        print()

    except Exception as e:
        print(f"❌ Ошибка получения начального состояния: {e}")
        return

    # Monitoring loop
    check_count = 0
    try:
        while True:
            await asyncio.sleep(3.0)
            check_count += 1

            try:
                # Проверяем текущие статусы
                current_accessibility = check_accessibility_status()
                current_input_monitoring = check_input_monitoring_status()

                # Выводим точку чтобы показать что проверка идёт
                print(f"[{check_count}] Проверка выполнена... ", end="", flush=True)

                # Проверяем изменения Accessibility
                if last_known_statuses["accessibility"] != current_accessibility:
                    print()
                    print("=" * 70)
                    print(f"🔔 ИЗМЕНЕНИЕ ОБНАРУЖЕНО: Accessibility")
                    print(f"   Было:   {last_known_statuses['accessibility'].value}")
                    print(f"   Стало:  {current_accessibility.value}")

                    if current_accessibility == PermissionStatus.GRANTED:
                        print("   ✅ Разрешение ПРЕДОСТАВЛЕНО → Должен быть перезапуск!")
                    elif current_accessibility == PermissionStatus.DENIED:
                        print("   ❌ Разрешение ОТКЛОНЕНО")
                    else:
                        print("   ⚠️ Статус неопределён")

                    print("=" * 70)
                    print()

                    last_known_statuses["accessibility"] = current_accessibility

                # Проверяем изменения Input Monitoring
                if last_known_statuses["input_monitoring"] != current_input_monitoring:
                    print()
                    print("=" * 70)
                    print(f"🔔 ИЗМЕНЕНИЕ ОБНАРУЖЕНО: Input Monitoring")
                    print(f"   Было:   {last_known_statuses['input_monitoring'].value}")
                    print(f"   Стало:  {current_input_monitoring.value}")

                    if current_input_monitoring == PermissionStatus.GRANTED:
                        print("   ✅ Разрешение ПРЕДОСТАВЛЕНО → Должен быть перезапуск!")
                    elif current_input_monitoring == PermissionStatus.DENIED:
                        print("   ❌ Разрешение ОТКЛОНЕНО")
                    else:
                        print("   ⚠️ Статус неопределён")

                    print("=" * 70)
                    print()

                    last_known_statuses["input_monitoring"] = current_input_monitoring

                # Если изменений не было, просто выводим ОК
                if (last_known_statuses["accessibility"] == current_accessibility and
                    last_known_statuses["input_monitoring"] == current_input_monitoring):
                    print("OK (без изменений)")

            except Exception as e:
                print()
                print(f"❌ Ошибка при проверке разрешений: {e}")

    except KeyboardInterrupt:
        print()
        print()
        print("=" * 70)
        print("⏹️  Мониторинг остановлен пользователем")
        print("=" * 70)
        print()
        print(f"Выполнено проверок: {check_count}")
        print(f"Финальное состояние:")
        print(f"   • Accessibility:      {last_known_statuses['accessibility'].value}")
        print(f"   • Input Monitoring:   {last_known_statuses['input_monitoring'].value}")
        print()


if __name__ == "__main__":
    asyncio.run(test_permission_monitoring())
