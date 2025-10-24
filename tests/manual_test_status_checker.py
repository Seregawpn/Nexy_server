"""
Manual test для status_checker.py

Запуск: python3 tests/manual_test_status_checker.py
"""

import sys
from pathlib import Path

# Добавляем пути
CLIENT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(CLIENT_ROOT))

from modules.permissions.first_run.status_checker import (
    PermissionStatus,
    check_microphone_status,
    check_accessibility_status,
    check_screen_capture_status,
    check_all_permissions,
)


def main():
    print("="*60)
    print("🔐 Проверка статусов разрешений")
    print("="*60)
    print()

    # Проверка микрофона
    print("🎙️  Проверка Microphone...")
    mic_status = check_microphone_status()
    print(f"   Статус: {mic_status.value}")
    print()

    # Проверка accessibility
    print("♿ Проверка Accessibility...")
    acc_status = check_accessibility_status()
    print(f"   Статус: {acc_status.value}")
    print()

    # Проверка screen capture
    print("📺 Проверка Screen Capture...")
    screen_status = check_screen_capture_status()
    print(f"   Статус: {screen_status.value}")
    print()

    # Все сразу
    print("="*60)
    print("📋 Все разрешения:")
    print("="*60)
    all_statuses = check_all_permissions()
    for perm, status in all_statuses.items():
        icon = "✅" if status == PermissionStatus.GRANTED else "❌"
        print(f"{icon} {perm:20} → {status.value}")
    print()

    # Подсказки
    print("="*60)
    print("💡 Подсказки:")
    print("="*60)
    print("• NOT_DETERMINED - система покажет диалог при активации")
    print("• GRANTED - разрешение уже дано")
    print("• DENIED - разрешение отклонено")
    print()
    print("Для сброса разрешений:")
    print("  tccutil reset Microphone com.nexy.assistant")
    print("  tccutil reset Accessibility com.nexy.assistant")
    print("  tccutil reset ScreenCapture com.nexy.assistant")
    print()


if __name__ == "__main__":
    main()
