#!/usr/bin/env python3
"""
Trigger Accessibility Prompt — отдельный скрипт для безопасного вызова диалога.

ВАЖНО: Этот скрипт запускается как subprocess из основного приложения.
Если macOS Sequoia решит "убить" процесс за вызов AXIsProcessTrustedWithOptions,
умрёт только этот subprocess, а не основное приложение.

Exit codes:
  0 - Разрешение уже есть (trusted=True) или диалог показан успешно
  1 - Разрешения нет (trusted=False) — диалог должен был появиться
  2 - Ошибка выполнения
"""

import sys


def main():
    try:
        # Попытка 1: Используем PyObjC (если доступен)
        try:
            import ApplicationServices as AS
            
            # Создаём опции с prompt=True
            options = {AS.kAXTrustedCheckOptionPrompt: True}
            
            # Этот вызов либо:
            # - Покажет диалог (если NOT_DETERMINED)
            # - Вернёт True/False (если уже resolved)
            # - Крашнет этот процесс (на Sequoia без entitlement)
            is_trusted = AS.AXIsProcessTrustedWithOptions(options)
            
            # Если дошли сюда — не крашнулось
            sys.exit(0 if is_trusted else 1)
            
        except ImportError:
            # PyObjC недоступен, пробуем ctypes
            pass
        
        # Попытка 2: Используем ctypes напрямую
        import ctypes
        import ctypes.util
        from CoreFoundation import (
            CFDictionaryCreate,
            CFStringCreateWithCString,
            kCFStringEncodingUTF8,
            kCFTypeDictionaryKeyCallBacks,
            kCFTypeDictionaryValueCallBacks,
            kCFBooleanTrue,
        )
        
        # Загружаем ApplicationServices
        lib_path = ctypes.util.find_library("ApplicationServices")
        if not lib_path:
            sys.exit(2)
        
        app_services = ctypes.cdll.LoadLibrary(lib_path)
        
        # Создаём CFString для ключа
        key = CFStringCreateWithCString(
            None, b"AXTrustedCheckOptionPrompt", kCFStringEncodingUTF8
        )
        
        # Создаём CFDictionary с опцией prompt=True
        keys = (ctypes.c_void_p * 1)(ctypes.cast(key, ctypes.c_void_p))
        values = (ctypes.c_void_p * 1)(ctypes.cast(kCFBooleanTrue, ctypes.c_void_p))
        
        options_dict = CFDictionaryCreate(
            None,
            keys,
            values,
            1,
            kCFTypeDictionaryKeyCallBacks,
            kCFTypeDictionaryValueCallBacks,
        )
        
        # Вызываем AXIsProcessTrustedWithOptions
        AXIsProcessTrustedWithOptions = app_services.AXIsProcessTrustedWithOptions
        AXIsProcessTrustedWithOptions.argtypes = [ctypes.c_void_p]
        AXIsProcessTrustedWithOptions.restype = ctypes.c_bool
        
        is_trusted = AXIsProcessTrustedWithOptions(
            ctypes.cast(options_dict, ctypes.c_void_p)
        )
        
        sys.exit(0 if is_trusted else 1)
        
    except Exception as e:
        # Любая ошибка — выходим с кодом 2
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
