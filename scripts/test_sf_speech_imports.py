#!/usr/bin/env python3
"""
Тест импортов SFSpeechRecognizer

Проверяет доступность Speech framework и базовую функциональность.
"""

import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def test_speech_imports():
    """Проверка импортов Speech framework"""
    print("\n" + "="*60)
    print("🔍 Тест импортов Speech framework")
    print("="*60)
    
    try:
        from Speech import (
            SFSpeechRecognizer,
            SFSpeechAudioBufferRecognitionRequest,
            SFSpeechRecognizerAuthorizationStatus
        )
        from Foundation import NSLocale
        print("✅ Speech framework импортирован успешно")
        return True
    except ImportError as e:
        print(f"❌ Ошибка импорта Speech framework: {e}")
        print("\n📦 Установите зависимости:")
        print("  pip install pyobjc-framework-Speech")
        return False

def test_speech_recognizer_creation():
    """Проверка создания SFSpeechRecognizer"""
    print("\n" + "="*60)
    print("🔍 Тест создания SFSpeechRecognizer")
    print("="*60)
    
    try:
        from Speech import SFSpeechRecognizer
        from Foundation import NSLocale
        
        # Создаём locale
        locale = NSLocale.alloc().initWithLocaleIdentifier_("en-US")
        print(f"✅ NSLocale создан: {locale}")
        
        # Создаём recognizer
        recognizer = SFSpeechRecognizer.alloc().initWithLocale_(locale)
        
        if recognizer is None:
            print("❌ SFSpeechRecognizer не создан (None)")
            return False
        
        print(f"✅ SFSpeechRecognizer создан: {recognizer}")
        
        # Проверяем доступность
        is_available = recognizer.isAvailable()
        print(f"ℹ️  Распознавание доступно: {is_available}")
        
        # Проверяем авторизацию
        auth_status = SFSpeechRecognizer.authorizationStatus()
        print(f"ℹ️  Статус авторизации: {auth_status}")
        
        # Проверяем поддержку on-device
        if hasattr(recognizer, 'supportsOnDeviceRecognition'):
            supports_on_device = recognizer.supportsOnDeviceRecognition()
            print(f"ℹ️  Поддержка On-Device: {supports_on_device}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка создания SFSpeechRecognizer: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_sf_speech_wrapper():
    """Проверка SFSpeechRecognizerWrapper"""
    print("\n" + "="*60)
    print("🔍 Тест SFSpeechRecognizerWrapper")
    print("="*60)
    
    try:
        import asyncio
        from modules.speech_recognition_sf import SFSpeechRecognizerWrapper
        
        print("✅ SFSpeechRecognizerWrapper импортирован")
        
        # Создаём wrapper
        wrapper = SFSpeechRecognizerWrapper(language="en-US", on_device=True)
        print(f"✅ SFSpeechRecognizerWrapper создан: {wrapper}")
        
        # Проверяем доступность (асинхронно)
        async def check_availability():
            available = await wrapper.is_available()
            print(f"ℹ️  Распознавание доступно: {available}")
            return available
        
        result = asyncio.run(check_availability())
        return result
        
    except ImportError as e:
        print(f"❌ Ошибка импорта SFSpeechRecognizerWrapper: {e}")
        import traceback
        traceback.print_exc()
        return False
    except Exception as e:
        print(f"❌ Ошибка тестирования wrapper: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Главная функция тестирования"""
    print("\n" + "="*60)
    print("🧪 ТЕСТИРОВАНИЕ SFSpeechRecognizer")
    print("="*60)
    
    results = []
    
    # Тест 1: Импорты
    results.append(("Импорты Speech framework", test_speech_imports()))
    
    if not results[-1][1]:
        print("\n⚠️  Пропускаем остальные тесты из-за ошибки импорта")
        return
    
    # Тест 2: Создание recognizer
    results.append(("Создание SFSpeechRecognizer", test_speech_recognizer_creation()))
    
    # Тест 3: Wrapper
    results.append(("SFSpeechRecognizerWrapper", test_sf_speech_wrapper()))
    
    # Итоги
    print("\n" + "="*60)
    print("📊 ИТОГИ ТЕСТИРОВАНИЯ")
    print("="*60)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n✅ Все тесты пройдены!")
        return 0
    else:
        print("\n❌ Некоторые тесты провалены")
        return 1

if __name__ == "__main__":
    sys.exit(main())



