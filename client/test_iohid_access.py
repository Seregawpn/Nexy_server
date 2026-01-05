#!/usr/bin/env python3
"""
Тестовый скрипт для проверки IOHIDCheckAccess API.
Проверяет, возвращает ли API IOHIDAccessType (uint32) с тремя значениями.

Запуск: python test_iohid_access.py
"""

import ctypes
from ctypes import util
import sys

def test_iohid_check_access():
    """Тест IOHIDCheckAccess с правильным типом возврата."""
    
    print("=" * 60)
    print("ТЕСТ: IOHIDCheckAccess API")
    print("=" * 60)
    
    # Находим IOKit
    iokit_path = util.find_library("IOKit")
    if not iokit_path:
        print("❌ IOKit не найден!")
        return
    
    print(f"✅ IOKit найден: {iokit_path}")
    
    iokit = ctypes.CDLL(iokit_path)
    
    try:
        check_access = iokit.IOHIDCheckAccess
    except AttributeError:
        print("❌ IOHIDCheckAccess недоступен (возможно старая macOS)")
        return
    
    # IOHIDAccessType константы
    kIOHIDAccessTypeGranted = 0
    kIOHIDAccessTypeDenied = 1
    kIOHIDAccessTypeUnknown = 2
    
    # IOHIDRequestType константы
    kIOHIDRequestTypePostEvent = 0   # Accessibility (posting events)
    kIOHIDRequestTypeListenEvent = 1  # Input Monitoring (listening to events)
    
    print("\n--- Тест 1: Текущая реализация (c_bool - НЕПРАВИЛЬНО) ---")
    check_access.argtypes = [ctypes.c_uint32]
    check_access.restype = ctypes.c_bool
    
    result_bool = check_access(kIOHIDRequestTypeListenEvent)
    print(f"IOHIDCheckAccess(ListenEvent) с c_bool = {result_bool}")
    print(f"  Тип: {type(result_bool)}")
    
    print("\n--- Тест 2: Правильная реализация (c_uint32) ---")
    check_access.argtypes = [ctypes.c_uint32]
    check_access.restype = ctypes.c_uint32
    
    result_uint = check_access(kIOHIDRequestTypeListenEvent)
    print(f"IOHIDCheckAccess(ListenEvent) с c_uint32 = {result_uint}")
    print(f"  Тип: {type(result_uint)}")
    
    # Интерпретация
    print("\n--- Интерпретация результата (uint32) ---")
    if result_uint == kIOHIDAccessTypeGranted:
        print(f"  Статус: ✅ GRANTED (разрешение выдано)")
    elif result_uint == kIOHIDAccessTypeDenied:
        print(f"  Статус: ❌ DENIED (разрешение отклонено)")
    elif result_uint == kIOHIDAccessTypeUnknown:
        print(f"  Статус: ❓ UNKNOWN (не определено, нужно запросить)")
    else:
        print(f"  Статус: ⚠️ Неизвестное значение: {result_uint}")
    
    print("\n--- Тест PostEvent (Accessibility) ---")
    result_post = check_access(kIOHIDRequestTypePostEvent)
    print(f"IOHIDCheckAccess(PostEvent) = {result_post}")
    if result_post == kIOHIDAccessTypeGranted:
        print(f"  Accessibility: ✅ GRANTED")
    elif result_post == kIOHIDAccessTypeDenied:
        print(f"  Accessibility: ❌ DENIED")
    elif result_post == kIOHIDAccessTypeUnknown:
        print(f"  Accessibility: ❓ UNKNOWN")
    
    print("\n--- ВЫВОД ---")
    print("Если c_bool и c_uint32 дают разные логические результаты,")
    print("это подтверждает баг в текущей реализации!")
    
    # Ключевая проверка
    if result_uint == 1 and result_bool == True:
        print("\n🐛 БАГ ПОДТВЕРЖДЁН!")
        print("   API вернул 1 (DENIED), но c_bool превратил это в True!")
        print("   Текущий код неправильно считает что разрешение ВЫДАНО!")
    elif result_uint == 0 and result_bool == True:
        print("\n✅ Разрешение выдано (оба способа дают одинаковый результат)")
    elif result_uint == 2 and result_bool == True:
        print("\n⚠️ API вернул UNKNOWN (2), c_bool превратил в True")
        print("   Это некорректно — нужно обрабатывать как NOT_DETERMINED")

if __name__ == "__main__":
    test_iohid_check_access()
