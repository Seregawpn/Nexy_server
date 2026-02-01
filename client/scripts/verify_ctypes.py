#!/usr/bin/env python3
"""
verify_ctypes.py — Preflight проверки для ctypes/нативного кода

Этот скрипт выполняется перед сборкой приложения и проверяет:
1. Корректность работы с CoreFoundation (CFDictionary, CFString, CFBoolean)
2. Корректность вызовов ApplicationServices (AXIsProcessTrustedWithOptions)
3. Правильное использование ctypes (argtypes, restype, .value)

Типичные ошибки, которые ловит этот скрипт:
- Забытый .value при использовании c_void_p.in_dll()
- Неправильные argtypes/restype
- NULL-указатели после вызовов CF-функций
"""

import sys
import ctypes
from ctypes import util as ctypes_util

# Цвета для вывода
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
NC = "\033[0m"

class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    def ok(self, name: str):
        self.passed += 1
        print(f"  {GREEN}✓{NC} {name}")

    def fail(self, name: str, reason: str):
        self.failed += 1
        self.errors.append(f"{name}: {reason}")
        print(f"  {RED}✗{NC} {name}: {reason}")

    def summary(self) -> bool:
        total = self.passed + self.failed
        if self.failed == 0:
            print(f"\n{GREEN}✅ Все {total} тестов пройдены{NC}")
            return True
        else:
            print(f"\n{RED}❌ Провалено {self.failed} из {total} тестов{NC}")
            for err in self.errors:
                print(f"   • {err}")
            return False


def test_corefoundation_basics(result: TestResult):
    """Тест базовых функций CoreFoundation."""
    try:
        cf_path = ctypes_util.find_library("CoreFoundation")
        if not cf_path:
            result.fail("CoreFoundation_load", "Библиотека не найдена")
            return
        
        cf = ctypes.CDLL(cf_path)
        result.ok("CoreFoundation загружен")
        
        # Тест kCFBooleanTrue
        try:
            kCFBooleanTrue = ctypes.c_void_p.in_dll(cf, "kCFBooleanTrue")
            if kCFBooleanTrue.value is None or kCFBooleanTrue.value == 0:
                result.fail("kCFBooleanTrue", f"Невалидное значение: {kCFBooleanTrue.value}")
            else:
                result.ok(f"kCFBooleanTrue.value = {hex(kCFBooleanTrue.value)}")
        except Exception as e:
            result.fail("kCFBooleanTrue", str(e))
        
        # Тест kCFBooleanFalse
        try:
            kCFBooleanFalse = ctypes.c_void_p.in_dll(cf, "kCFBooleanFalse")
            if kCFBooleanFalse.value is None or kCFBooleanFalse.value == 0:
                result.fail("kCFBooleanFalse", f"Невалидное значение: {kCFBooleanFalse.value}")
            else:
                result.ok(f"kCFBooleanFalse.value = {hex(kCFBooleanFalse.value)}")
        except Exception as e:
            result.fail("kCFBooleanFalse", str(e))
            
    except Exception as e:
        result.fail("CoreFoundation_load", str(e))


def test_cfstring_creation(result: TestResult):
    """Тест создания CFString."""
    try:
        cf = ctypes.CDLL(ctypes_util.find_library("CoreFoundation"))
        
        cf.CFStringCreateWithCString.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32]
        cf.CFStringCreateWithCString.restype = ctypes.c_void_p
        cf.CFRelease.argtypes = [ctypes.c_void_p]
        cf.CFRelease.restype = None
        
        test_string = cf.CFStringCreateWithCString(None, b"TestString", 0)
        if not test_string or test_string == 0:
            result.fail("CFStringCreateWithCString", "Вернул NULL")
            return
        
        result.ok(f"CFStringCreateWithCString = {hex(test_string)}")
        cf.CFRelease(test_string)
        result.ok("CFRelease работает корректно")
        
    except Exception as e:
        result.fail("CFStringCreateWithCString", str(e))


def test_cfdictionary_creation(result: TestResult):
    """Тест создания CFDictionary — критический тест для Accessibility."""
    try:
        cf = ctypes.CDLL(ctypes_util.find_library("CoreFoundation"))
        
        # Настройка функций
        cf.CFStringCreateWithCString.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32]
        cf.CFStringCreateWithCString.restype = ctypes.c_void_p
        cf.CFDictionaryCreate.argtypes = [
            ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p),
            ctypes.POINTER(ctypes.c_void_p), ctypes.c_long,
            ctypes.c_void_p, ctypes.c_void_p
        ]
        cf.CFDictionaryCreate.restype = ctypes.c_void_p
        cf.CFRelease.argtypes = [ctypes.c_void_p]
        cf.CFRelease.restype = None
        
        # Получаем kCFBooleanTrue
        kCFBooleanTrue = ctypes.c_void_p.in_dll(cf, "kCFBooleanTrue")
        
        # Создаём ключ
        key = cf.CFStringCreateWithCString(None, b"TestKey", 0)
        if not key:
            result.fail("CFDictionaryCreate", "Не удалось создать ключ")
            return
        
        try:
            # КРИТИЧЕСКИЙ ТЕСТ: правильно ли используется .value
            keys = (ctypes.c_void_p * 1)(key)
            values = (ctypes.c_void_p * 1)(kCFBooleanTrue.value)  # Должен быть .value!
            
            options = cf.CFDictionaryCreate(None, keys, values, 1, None, None)
            
            if not options or options == 0:
                result.fail("CFDictionaryCreate", "Вернул NULL (возможно ошибка с .value)")
            else:
                result.ok(f"CFDictionaryCreate = {hex(options)}")
                cf.CFRelease(options)
                
        finally:
            cf.CFRelease(key)
            
    except Exception as e:
        result.fail("CFDictionaryCreate", str(e))


def test_accessibility_api(result: TestResult):
    """Тест API Accessibility (без реального запроса разрешений)."""
    try:
        app_services_path = ctypes_util.find_library("ApplicationServices")
        if not app_services_path:
            result.fail("ApplicationServices_load", "Библиотека не найдена")
            return
            
        app_services = ctypes.CDLL(app_services_path)
        result.ok("ApplicationServices загружен")
        
        # Проверяем что функция существует и можно установить argtypes/restype
        try:
            app_services.AXIsProcessTrustedWithOptions.argtypes = [ctypes.c_void_p]
            app_services.AXIsProcessTrustedWithOptions.restype = ctypes.c_bool
            result.ok("AXIsProcessTrustedWithOptions доступна")
        except AttributeError as e:
            result.fail("AXIsProcessTrustedWithOptions", f"Функция недоступна: {e}")
        
        # Тест вызова с NULL (просто проверка статуса, без prompt)
        try:
            is_trusted = app_services.AXIsProcessTrustedWithOptions(None)
            result.ok(f"AXIsProcessTrustedWithOptions(None) = {is_trusted}")
        except Exception as e:
            result.fail("AXIsProcessTrustedWithOptions(None)", str(e))
            
    except Exception as e:
        result.fail("ApplicationServices", str(e))





def main():
    print(f"\n{YELLOW}🧪 CTYPES PREFLIGHT ПРОВЕРКИ{NC}")
    print("=" * 50)
    
    result = TestResult()
    
    print(f"\n{YELLOW}1. CoreFoundation базовые тесты{NC}")
    test_corefoundation_basics(result)
    
    print(f"\n{YELLOW}2. CFString создание{NC}")
    test_cfstring_creation(result)
    
    print(f"\n{YELLOW}3. CFDictionary создание (критический){NC}")
    test_cfdictionary_creation(result)
    
    print(f"\n{YELLOW}4. Accessibility API{NC}")
    test_accessibility_api(result)
    

    
    print("=" * 50)
    success = result.summary()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
