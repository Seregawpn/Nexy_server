#!/usr/bin/env python3
"""
Тестовый скрипт для демонстрации бага с c_bool.
Эмулируем что произойдет если API вернёт значение 1 (DENIED).

Запуск: python3 test_bool_bug.py
"""

import ctypes
from ctypes import util

def test_bool_bug():
    """Демонстрация бага с c_bool для значения 1 (DENIED)."""
    
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ БАГА: c_bool vs c_uint32")
    print("=" * 60)
    
    iokit_path = util.find_library("IOKit")
    iokit = ctypes.CDLL(iokit_path)
    
    check_access = iokit.IOHIDCheckAccess
    
    # Константы
    kIOHIDRequestTypePostEvent = 0   # Accessibility - на вашей машине = DENIED (1)
    kIOHIDRequestTypeListenEvent = 1  # Input Monitoring
    
    print("\n--- Тест с PostEvent (Accessibility = DENIED на вашей машине) ---")
    
    # Неправильный способ (текущий код для Input Monitoring)
    check_access.argtypes = [ctypes.c_uint32]
    check_access.restype = ctypes.c_bool
    result_bool = check_access(kIOHIDRequestTypePostEvent)
    
    # Правильный способ
    check_access.restype = ctypes.c_uint32
    result_uint = check_access(kIOHIDRequestTypePostEvent)
    
    print(f"Сырое значение API (uint32): {result_uint}")
    print(f"Через c_bool: {result_bool}")
    
    print("\n--- АНАЛИЗ ---")
    if result_uint == 1:
        print("API вернул 1 = kIOHIDAccessTypeDenied (ОТКЛОНЕНО!)")
        if result_bool == True:
            print("НО c_bool превратил 1 в True!")
            print("")
            print("🐛 ЭТО БАГ!")
            print("Текущий код:")
            print("  granted = bool(check_access(...))  # granted = True")
            print("  if granted:  # True!")
            print("      return PermissionStatus.GRANTED  # НЕПРАВИЛЬНО!")
            print("")
            print("Код думает что разрешение ВЫДАНО, хотя оно ОТКЛОНЕНО!")
    
    print("\n--- Как это влияет на Input Monitoring ---")
    check_access.restype = ctypes.c_uint32
    input_result = check_access(kIOHIDRequestTypeListenEvent)
    print(f"Input Monitoring статус: {input_result}")
    
    if input_result == 0:
        print("Сейчас = GRANTED, баг не проявляется")
        print("Но если пользователь отклонит разрешение (статус = 1),")
        print("то c_bool вернёт True и код подумает что GRANTED!")
    elif input_result == 1:
        print("🐛 Сейчас = DENIED, но c_bool скажет True!")
    elif input_result == 2:
        print("⚠️ Сейчас = UNKNOWN, c_bool скажет True!")

if __name__ == "__main__":
    test_bool_bug()
