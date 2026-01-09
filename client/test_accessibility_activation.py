#!/usr/bin/env python3
"""
Тестовый скрипт для проверки активации Accessibility разрешения.
"""

import asyncio
import sys
import os

# Добавляем путь к модулям
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_direct_api_call():
    """Тест прямого вызова AXIsProcessTrustedWithOptions."""
    print("\n" + "="*60)
    print("TEST 1: Прямой вызов AXIsProcessTrustedWithOptions")
    print("="*60)
    
    try:
        from Quartz import (
            AXIsProcessTrustedWithOptions,
            kAXTrustedCheckOptionPrompt,
        )
        from Foundation import NSDictionary
        
        print("✅ Импорт Quartz/AX API успешен")
        
        # Проверяем без показа диалога (только проверка статуса)
        options_no_prompt = NSDictionary.dictionaryWithObject_forKey_(
            False,  # НЕ показывать диалог
            kAXTrustedCheckOptionPrompt
        )
        current_status = AXIsProcessTrustedWithOptions(options_no_prompt)
        print(f"📊 Текущий статус Accessibility (без диалога): {current_status}")
        
        # Теперь с показом диалога
        print("\n🔔 Вызываем AXIsProcessTrustedWithOptions с prompt=True...")
        print("   (Если разрешение не дано, должен появиться системный диалог)")
        
        options_with_prompt = NSDictionary.dictionaryWithObject_forKey_(
            True,  # Показывать диалог
            kAXTrustedCheckOptionPrompt
        )
        result = AXIsProcessTrustedWithOptions(options_with_prompt)
        
        if result:
            print("✅ Accessibility: разрешение ПРЕДОСТАВЛЕНО")
        else:
            print("⚠️ Accessibility: разрешение НЕ предоставлено")
            print("   → Проверьте, появился ли диалог или приложение в System Settings → Accessibility")
        
        return True
        
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False


async def test_activator_function():
    """Тест функции activate_accessibility из activator.py."""
    print("\n" + "="*60)
    print("TEST 2: Функция activate_accessibility() из activator.py")
    print("="*60)
    
    try:
        from modules.permissions.first_run.activator import activate_accessibility
        print("✅ Импорт activate_accessibility успешен")
        
        result = await activate_accessibility()
        print(f"📊 Результат activate_accessibility(): {result}")
        
        return result
        
    except ImportError as e:
        print(f"❌ Ошибка импорта activator: {e}")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("\n🧪 ТЕСТИРОВАНИЕ АКТИВАЦИИ ACCESSIBILITY")
    print("="*60)
    
    # Тест 1: Прямой вызов API
    direct_ok = test_direct_api_call()
    
    # Тест 2: Функция из activator.py
    activator_ok = asyncio.run(test_activator_function())
    
    # Итоги
    print("\n" + "="*60)
    print("ИТОГИ ТЕСТИРОВАНИЯ:")
    print("="*60)
    print(f"  Прямой вызов API:     {'✅ OK' if direct_ok else '❌ FAIL'}")
    print(f"  Функция activator:    {'✅ OK' if activator_ok else '❌ FAIL'}")
    
    if direct_ok and activator_ok:
        print("\n✅ ВСЕ ТЕСТЫ ПРОШЛИ!")
        print("\n📋 Проверьте:")
        print("   1. Появился ли системный диалог Accessibility?")
        print("   2. Добавилось ли приложение в System Settings → Privacy → Accessibility?")
    else:
        print("\n❌ НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОШЛИ")
    
    return 0 if (direct_ok and activator_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
