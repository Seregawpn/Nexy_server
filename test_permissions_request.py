#!/usr/bin/env python3
"""
Простой тест запроса разрешений
Проверяет последовательный запрос всех 4 разрешений
"""

import asyncio
import sys
import os

# Добавляем пути
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "modules"))

from modules.permissions.first_run.activator import (
    activate_microphone,
    activate_accessibility,
    activate_input_monitoring,
    activate_screen_capture,
)
from modules.permissions.first_run.status_checker import (
    check_microphone_status,
    check_accessibility_status,
    check_input_monitoring_status,
    check_screen_capture_status,
)

async def test_permissions():
    """Тест последовательного запроса разрешений"""
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║  ТЕСТ ПОСЛЕДОВАТЕЛЬНОГО ЗАПРОСА РАЗРЕШЕНИЙ                     ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print("")
    
    # 1. MICROPHONE
    print("=" * 70)
    print("1️⃣  MICROPHONE")
    print("=" * 70)
    status = check_microphone_status()
    print(f"   Текущий статус: {status.value}")
    
    if status.value == "not_determined":
        print("   🔔 Запрашиваем разрешение (ожидайте диалог)...")
        result = await activate_microphone(hold_duration=7.0)
        print(f"   Результат активации: {result}")
        new_status = check_microphone_status()
        print(f"   Новый статус: {new_status.value}")
    else:
        print(f"   ✅ Разрешение уже {status.value}")
    
    print("")
    await asyncio.sleep(2)
    
    # 2. ACCESSIBILITY
    print("=" * 70)
    print("2️⃣  ACCESSIBILITY")
    print("=" * 70)
    status = check_accessibility_status()
    print(f"   Текущий статус: {status.value}")
    
    if status.value == "not_determined":
        print("   🔔 Запрашиваем разрешение (ожидайте диалог или System Settings)...")
        result = await activate_accessibility(hold_duration=7.0)
        print(f"   Результат активации: {result}")
        new_status = check_accessibility_status()
        print(f"   Новый статус: {new_status.value}")
    else:
        print(f"   ✅ Разрешение уже {status.value}")
    
    print("")
    await asyncio.sleep(2)
    
    # 3. INPUT MONITORING
    print("=" * 70)
    print("3️⃣  INPUT MONITORING")
    print("=" * 70)
    status = check_input_monitoring_status()
    print(f"   Текущий статус: {status.value}")
    
    if status.value == "not_determined":
        print("   🔔 Запрашиваем разрешение (ожидайте диалог или System Settings)...")
        result = await activate_input_monitoring(hold_duration=7.0)
        print(f"   Результат активации: {result}")
        new_status = check_input_monitoring_status()
        print(f"   Новый статус: {new_status.value}")
    else:
        print(f"   ✅ Разрешение уже {status.value}")
    
    print("")
    await asyncio.sleep(2)
    
    # 4. SCREEN CAPTURE
    print("=" * 70)
    print("4️⃣  SCREEN CAPTURE")
    print("=" * 70)
    status = check_screen_capture_status()
    print(f"   Текущий статус: {status.value}")
    
    if status.value == "not_determined":
        print("   🔔 Запрашиваем разрешение (ожидайте диалог)...")
        result = await activate_screen_capture(hold_duration=7.0)
        print(f"   Результат активации: {result}")
        new_status = check_screen_capture_status()
        print(f"   Новый статус: {new_status.value}")
    else:
        print(f"   ✅ Разрешение уже {status.value}")
    
    print("")
    print("=" * 70)
    print("✅ ТЕСТ ЗАВЕРШЁН")
    print("=" * 70)
    print("")
    print("📋 ИТОГОВЫЕ СТАТУСЫ:")
    print(f"   🎙️  Microphone:       {check_microphone_status().value}")
    print(f"   ♿  Accessibility:    {check_accessibility_status().value}")
    print(f"   ⌨️   Input Monitoring: {check_input_monitoring_status().value}")
    print(f"   📺  Screen Capture:   {check_screen_capture_status().value}")

if __name__ == "__main__":
    try:
        asyncio.run(test_permissions())
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем")
    except Exception as e:
        print(f"\n\n❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()



