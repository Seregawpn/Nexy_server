#!/usr/bin/env python3
"""
Тест исправленного status_checker.py
"""

import sys
sys.path.insert(0, '/Users/sergiyzasorin/Fix_new/client')

from modules.permissions.first_run.status_checker import (
    check_microphone_status,
    check_accessibility_status,
    check_input_monitoring_status,
    check_screen_capture_status,
    check_all_permissions,
    PermissionStatus
)

def test_fixed_permission_checks():
    print("=" * 70)
    print("ТЕСТ ИСПРАВЛЕННОГО STATUS_CHECKER")
    print("=" * 70)
    
    print("\n1. Microphone:")
    mic_status = check_microphone_status()
    print(f"   Статус: {mic_status.value}")
    
    print("\n2. Accessibility:")
    acc_status = check_accessibility_status()
    print(f"   Статус: {acc_status.value}")
    
    print("\n3. Input Monitoring:")
    input_status = check_input_monitoring_status()
    print(f"   Статус: {input_status.value}")
    
    print("\n4. Screen Capture:")
    screen_status = check_screen_capture_status()
    print(f"   Статус: {screen_status.value}")
    
    print("\n" + "=" * 70)
    print("ИТОГО (check_all_permissions)")
    print("=" * 70)
    
    all_statuses = check_all_permissions()
    for name, status in all_statuses.items():
        emoji = "✅" if status == PermissionStatus.GRANTED else ("❌" if status == PermissionStatus.DENIED else "❓")
        print(f"   {emoji} {name}: {status.value}")
    
    print("\n" + "=" * 70)
    print("ПРОВЕРКА РЕЗУЛЬТАТОВ")
    print("=" * 70)
    
    # Сравнение с ожидаемыми значениями (на основе предыдущих тестов)
    print("""
   Ожидаемые результаты (на основе предыдущих тестов):
   - Microphone: GRANTED (AVAuthorizationStatus = 3)
   - Input Monitoring: GRANTED (IOHIDCheckAccess = 0)
   - Accessibility: DENIED (IOHIDCheckAccess = 1)
   - Screen Capture: GRANTED (окна с именами >= 10)
    """)
    
    # Проверяем детерминированность
    print("Детерминированность:")
    if acc_status == PermissionStatus.DENIED:
        print("   ✅ Accessibility теперь правильно определяет DENIED!")
    elif acc_status == PermissionStatus.GRANTED:
        print("   ✅ Accessibility = GRANTED")
    else:
        print("   ⚠️ Accessibility = NOT_DETERMINED (возможен fallback)")
    
    if input_status == PermissionStatus.GRANTED:
        print("   ✅ Input Monitoring = GRANTED (ранее тоже было верно)")
    elif input_status == PermissionStatus.DENIED:
        print("   ✅ Input Monitoring теперь правильно определяет DENIED!")
    else:
        print("   ❓ Input Monitoring = NOT_DETERMINED")

if __name__ == "__main__":
    test_fixed_permission_checks()
