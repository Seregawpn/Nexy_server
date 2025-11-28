#!/usr/bin/env python3
"""
Диагностика доступа к Gemini Live API

Проверяет:
1. Наличие API ключа
2. Доступность библиотеки google.genai
3. Подключение к Gemini Live API
4. Причины ошибки 403
"""

import sys
import os
from pathlib import Path

# Добавляем путь к серверу
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "server"))

from config.unified_config import get_config


def test_gemini_imports():
    """Тест 1: Проверка импортов"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Проверка импортов Gemini")
    print("="*80)
    
    try:
        from google import genai
        from google.genai import types
        print("   ✅ google.genai импортирован успешно")
        print(f"   ✅ genai версия: {getattr(genai, '__version__', 'unknown')}")
        return True
    except ImportError as e:
        print(f"   ❌ Ошибка импорта: {e}")
        print(f"   ⚠️  Установите: pip install google-genai")
        return False


def test_api_key():
    """Тест 2: Проверка API ключа"""
    print("\n" + "="*80)
    print("ТЕСТ 2: Проверка API ключа")
    print("="*80)
    
    try:
        config = get_config()
        api_key = config.text_processing.gemini_api_key
        
        if not api_key:
            print("   ❌ GEMINI_API_KEY не установлен")
            print("   ⚠️  Установите переменную окружения GEMINI_API_KEY или в config.env")
            return False
        
        print(f"   ✅ API ключ найден: {api_key[:10]}...{api_key[-4:]}")
        print(f"   ✅ Длина ключа: {len(api_key)} символов")
        
        # Проверяем формат (обычно начинается с AIza)
        if api_key.startswith("AIza"):
            print("   ✅ Формат ключа выглядит корректно (начинается с AIza)")
        else:
            print("   ⚠️  Формат ключа необычный (обычно начинается с AIza)")
        
        return True
    except Exception as e:
        print(f"   ❌ Ошибка проверки ключа: {e}")
        return False


def test_client_creation():
    """Тест 3: Создание клиента"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Создание Gemini клиента")
    print("="*80)
    
    try:
        from google import genai
        config = get_config()
        api_key = config.text_processing.gemini_api_key
        
        if not api_key:
            print("   ❌ API ключ отсутствует")
            return False
        
        client = genai.Client(api_key=api_key)
        print("   ✅ Gemini клиент создан успешно")
        return True
    except Exception as e:
        print(f"   ❌ Ошибка создания клиента: {e}")
        return False


async def test_live_api_connection():
    """Тест 4: Подключение к Live API"""
    print("\n" + "="*80)
    print("ТЕСТ 4: Подключение к Gemini Live API")
    print("="*80)
    
    try:
        from google import genai
        from google.genai import types
        config = get_config()
        api_key = config.text_processing.gemini_api_key
        model_name = config.text_processing.gemini_live_model
        
        if not api_key:
            print("   ❌ API ключ отсутствует")
            return False
        
        print(f"   🔍 Модель: {model_name}")
        print(f"   🔍 API ключ: {api_key[:10]}...{api_key[-4:]}")
        
        client = genai.Client(api_key=api_key)
        
        # Базовая конфигурация
        live_config = {
            "response_modalities": ["TEXT"]
        }
        
        print(f"   🔍 Пытаемся подключиться к Live API...")
        
        try:
            async with client.aio.live.connect(model=model_name, config=live_config) as session:
                print("   ✅ WebSocket подключение установлено")
                
                # Отправляем тестовое сообщение
                print("   🔍 Отправляем тестовое сообщение...")
                await session.send_client_content(
                    turns={"role": "user", "parts": [{"text": "Hello"}]},
                    turn_complete=True
                )
                
                # Ждем ответ
                print("   🔍 Ожидаем ответ...")
                response_received = False
                async for response in session.receive():
                    if response.text:
                        print(f"   ✅ Получен ответ: {response.text[:50]}...")
                        response_received = True
                        break
                
                if response_received:
                    print("   ✅ Live API работает корректно")
                    return True
                else:
                    print("   ⚠️  Ответ не получен")
                    return False
                    
        except Exception as conn_error:
            error_str = str(conn_error)
            print(f"   ❌ Ошибка подключения: {error_str}")
            
            # Анализируем ошибку
            if "403" in error_str or "HTTP 403" in error_str:
                print("\n   🔍 АНАЛИЗ ОШИБКИ 403:")
                print("   ⚠️  HTTP 403 Forbidden означает:")
                print("      1. API ключ не имеет доступа к Gemini Live API")
                print("      2. Gemini Live API не включен в Google Cloud Console")
                print("      3. Модель недоступна для этого ключа")
                print("      4. Исчерпана квота или превышены лимиты")
                print("\n   💡 РЕШЕНИЯ:")
                print("      1. Проверьте Google Cloud Console:")
                print("         - Включен ли 'Generative Language API'")
                print("         - Есть ли доступ к 'Gemini Live API'")
                print("         - Не исчерпана ли квота")
                print("      2. Проверьте API ключ:")
                print("         - Правильность ключа")
                print("         - Ограничения API ключа (API restrictions)")
                print("      3. Попробуйте другую модель:")
                print("         - gemini-2.0-flash-exp")
                print("         - gemini-1.5-pro")
            elif "401" in error_str:
                print("\n   🔍 АНАЛИЗ ОШИБКИ 401:")
                print("   ⚠️  HTTP 401 Unauthorized означает неверный API ключ")
                print("   💡 Проверьте правильность GEMINI_API_KEY в config.env")
            elif "429" in error_str:
                print("\n   🔍 АНАЛИЗ ОШИБКИ 429:")
                print("   ⚠️  HTTP 429 Too Many Requests означает превышение лимитов")
                print("   💡 Подождите и попробуйте позже")
            
            return False
            
    except ImportError:
        print("   ❌ google.genai не импортирован")
        return False
    except Exception as e:
        print(f"   ❌ Неожиданная ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_model_availability():
    """Тест 5: Проверка доступности модели"""
    print("\n" + "="*80)
    print("ТЕСТ 5: Проверка доступности модели")
    print("="*80)
    
    try:
        config = get_config()
        model_name = config.text_processing.gemini_live_model
        
        print(f"   🔍 Текущая модель: {model_name}")
        
        # Список возможных моделей
        available_models = [
            "gemini-live-2.5-flash-preview",
            "gemini-2.0-flash-exp",
            "gemini-1.5-pro",
            "gemini-1.5-flash"
        ]
        
        print(f"\n   📋 Доступные модели для тестирования:")
        for model in available_models:
            status = "✅" if model == model_name else "  "
            print(f"      {status} {model}")
        
        if model_name not in available_models:
            print(f"\n   ⚠️  Модель {model_name} не в списке стандартных")
            print(f"   💡 Попробуйте одну из стандартных моделей")
        
        return True
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")
        return False


async def main():
    """Запуск всех тестов"""
    print("\n" + "="*80)
    print("ДИАГНОСТИКА ДОСТУПА К GEMINI LIVE API")
    print("="*80)
    
    results = []
    
    # Тест 1: Импорты
    results.append(("Импорты Gemini", test_gemini_imports()))
    
    # Тест 2: API ключ
    results.append(("API ключ", test_api_key()))
    
    # Тест 3: Создание клиента
    if results[0][1]:  # Если импорты прошли
        results.append(("Создание клиента", test_client_creation()))
    else:
        results.append(("Создание клиента", False))
    
    # Тест 4: Подключение к Live API
    if all(r[1] for r in results[:3]):  # Если все предыдущие прошли
        results.append(("Подключение к Live API", await test_live_api_connection()))
    else:
        results.append(("Подключение к Live API", False))
    
    # Тест 5: Доступность модели
    results.append(("Доступность модели", test_model_availability()))
    
    # Итоги
    print("\n" + "="*80)
    print("ИТОГИ ДИАГНОСТИКИ")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\n📊 Результат: {passed}/{total} тестов пройдено")
    
    if passed < total:
        print("\n💡 РЕКОМЕНДАЦИИ:")
        if not results[0][1]:
            print("   1. Установите google-genai: pip install google-genai")
        if not results[1][1]:
            print("   2. Установите GEMINI_API_KEY в config.env")
        if results[3][1] == False and results[0][1] and results[1][1]:
            print("   3. Проверьте доступ к Gemini Live API в Google Cloud Console")
            print("   4. Убедитесь, что API ключ имеет права на Gemini Live API")
    
    return 0 if passed == total else 1


if __name__ == "__main__":
    import asyncio
    sys.exit(asyncio.run(main()))



