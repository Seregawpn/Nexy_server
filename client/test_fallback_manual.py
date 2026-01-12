#!/usr/bin/env python3
"""
Ручной тест fallback после перезапуска tccd.
ТРЕБУЕТСЯ: sudo killall tccd (выполнить вручную)
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from modules.permissions.first_run.activator import activate_all_permissions
from modules.permissions.first_run.status_checker import (
    check_microphone_status,
    check_accessibility_status,
    check_screen_capture_status,
    check_input_monitoring_status,
)


def print_statuses(label):
    """Вывести статусы всех разрешений."""
    print(f"\n{label}:")
    print(f"  Microphone: {check_microphone_status().value}")
    print(f"  Accessibility: {check_accessibility_status().value}")
    print(f"  ScreenCapture: {check_screen_capture_status().value}")
    print(f"  InputMonitoring: {check_input_monitoring_status().value}")


async def main():
    print("\n" + "="*60)
    print("ТЕСТ: Fallback после перезапуска tccd")
    print("="*60)
    print("\n⚠️  ВАЖНО: Перед запуском выполните в терминале:")
    print("   sudo killall tccd")
    print("\nНажмите Enter когда выполните команду, или Ctrl+C для отмены...")
    try:
        input()
    except KeyboardInterrupt:
        print("\n⚠️  Прервано пользователем")
        return 1
    
    print("\n" + "="*60)
    print("ШАГ 1: Проверка статусов ДО активации")
    print("="*60)
    print_statuses("Статусы ДО")
    
    print("\n" + "="*60)
    print("ШАГ 2: Запуск activate_all_permissions()")
    print("="*60)
    print("Ожидаем: fallback должен открыть System Settings для разрешений")
    print("Ищем в логах: '🔧 ... открываем System Settings'")
    print("-" * 60)
    
    results = await activate_all_permissions()
    
    print("-" * 60)
    print("\nРезультаты activate_all_permissions():")
    for perm, result in results.items():
        status = "✅" if result else "❌"
        print(f"  {status} {perm}: {result}")
    
    print("\n" + "="*60)
    print("ШАГ 3: Проверка статусов ПОСЛЕ активации")
    print("="*60)
    print_statuses("Статусы ПОСЛЕ")
    
    print("\n" + "="*60)
    print("ИТОГИ")
    print("="*60)
    print("\nПроверьте:")
    print("  1. Появились ли системные диалоги для разрешений?")
    print("  2. Открылись ли System Settings для fallback?")
    print("  3. Есть ли в логах сообщения '🔧 ... открываем System Settings'?")
    print("  4. Изменились ли статусы разрешений?")
    
    return 0


if __name__ == "__main__":
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем")
        sys.exit(130)
