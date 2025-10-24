"""
Manual test для activator.py

ВНИМАНИЕ: Этот тест ПОКАЖЕТ системные диалоги разрешений!
Перед запуском убедитесь что хотите видеть эти диалоги.

Для сброса разрешений перед тестом:
  tccutil reset Microphone com.nexy.assistant
  tccutil reset Accessibility com.nexy.assistant
  tccutil reset ScreenCapture com.nexy.assistant

Запуск: python3 tests/manual_test_activator.py
"""

import asyncio
import sys
from pathlib import Path

# Добавляем пути
CLIENT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(CLIENT_ROOT))

from modules.permissions.first_run.activator import (
    activate_microphone,
    activate_accessibility,
    activate_screen_capture,
)


async def test_microphone():
    print("="*60)
    print("🎙️  ТЕСТ: Активация Microphone")
    print("="*60)
    print()
    print("Сейчас будет вызван API для открытия микрофона.")
    print("Если разрешение NOT_DETERMINED, увидите системный диалог.")
    print()
    input("Нажмите Enter чтобы продолжить...")
    print()

    result = await activate_microphone()
    print()
    print(f"Результат: {'✅ Успех' if result else '❌ Ошибка'}")
    print()
    input("Видели диалог микрофона? Нажмите Enter...")
    print()


async def test_accessibility():
    print("="*60)
    print("♿ ТЕСТ: Активация Accessibility")
    print("="*60)
    print()
    print("Сейчас будет вызван API для Accessibility.")
    print("Если разрешение NOT_DETERMINED, откроется System Settings.")
    print()
    input("Нажмите Enter чтобы продолжить...")
    print()

    result = await activate_accessibility()
    print()
    print(f"Результат: {'✅ Успех' if result else '❌ Ошибка'}")
    print()
    input("Видели System Settings (Accessibility)? Нажмите Enter...")
    print()


async def test_screen_capture():
    print("="*60)
    print("📺 ТЕСТ: Активация Screen Capture")
    print("="*60)
    print()
    print("Сейчас будет вызван API для Screen Capture.")
    print("Если разрешение NOT_DETERMINED, увидите системный диалог.")
    print()
    input("Нажмите Enter чтобы продолжить...")
    print()

    result = await activate_screen_capture()
    print()
    print(f"Результат: {'✅ Успех' if result else '❌ Ошибка'}")
    print()
    input("Видели диалог Screen Capture? Нажмите Enter...")
    print()


async def main():
    print()
    print("╔"+"═"*58+"╗")
    print("║" + " "*15 + "ТЕСТ ACTIVATOR.PY" + " "*26 + "║")
    print("╚"+"═"*58+"╝")
    print()
    print("⚠️  ВНИМАНИЕ: Этот тест покажет системные диалоги!")
    print()
    print("Для лучшего тестирования, сначала сбросьте разрешения:")
    print("  tccutil reset Microphone com.nexy.assistant")
    print("  tccutil reset Accessibility com.nexy.assistant")
    print("  tccutil reset ScreenCapture com.nexy.assistant")
    print()
    input("Готовы начать тестирование? Нажмите Enter...")
    print()

    # Тест по очереди
    await test_microphone()
    await asyncio.sleep(2)

    await test_accessibility()
    await asyncio.sleep(2)

    await test_screen_capture()

    print("="*60)
    print("✅ ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ")
    print("="*60)
    print()
    print("Проверьте:")
    print("  • Появились ли диалоги последовательно?")
    print("  • Работает ли активация без ошибок?")
    print()


if __name__ == "__main__":
    asyncio.run(main())
