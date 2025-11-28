#!/usr/bin/env python3
"""
Быстрый тест API ключа Gemini
"""

import sys
import os
from pathlib import Path

# Добавляем путь к серверу
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "server"))

# API ключ для тестирования
API_KEY = "AIzaSyBJD7HeddPpAL90vbzIsHCv1f5tXA_cxPE"

async def test_api_key():
    """Тест API ключа"""
    print("\n" + "="*80)
    print("ТЕСТ API КЛЮЧА GEMINI")
    print("="*80)
    print(f"API ключ: {API_KEY[:10]}...{API_KEY[-4:]}")
    
    try:
        from google import genai
        from google.genai import types
        print("✅ google.genai импортирован")
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        print("   Установите: pip install google-genai")
        return False
    
    # Создаем клиент
    try:
        print("\n🔍 Создание Gemini клиента...")
        client = genai.Client(api_key=API_KEY)
        print("✅ Клиент создан")
    except Exception as e:
        print(f"❌ Ошибка создания клиента: {e}")
        return False
    
    # Тестируем разные модели
    models_to_test = [
        "gemini-live-2.5-flash-preview",
        "gemini-2.0-flash-exp",
        "gemini-1.5-pro",
        "gemini-1.5-flash"
    ]
    
    print("\n" + "="*80)
    print("ТЕСТИРОВАНИЕ МОДЕЛЕЙ")
    print("="*80)
    
    for model_name in models_to_test:
        print(f"\n🔍 Тестируем модель: {model_name}")
        try:
            live_config = {
                "response_modalities": ["TEXT"]
            }
            
            async with client.aio.live.connect(model=model_name, config=live_config) as session:
                print(f"   ✅ WebSocket подключение установлено")
                
                # Отправляем тестовое сообщение
                await session.send_client_content(
                    turns={"role": "user", "parts": [{"text": "Hello"}]},
                    turn_complete=True
                )
                
                # Ждем ответ
                response_received = False
                async for response in session.receive():
                    if response.text:
                        print(f"   ✅ Получен ответ: {response.text[:50]}...")
                        response_received = True
                        break
                
                if response_received:
                    print(f"   ✅ МОДЕЛЬ {model_name} РАБОТАЕТ!")
                    return True
                else:
                    print(f"   ⚠️  Ответ не получен")
                    
        except Exception as e:
            error_str = str(e)
            print(f"   ❌ Ошибка: {error_str[:100]}")
            
            # Анализируем ошибку
            if "403" in error_str or "HTTP 403" in error_str:
                print(f"   🔍 HTTP 403 Forbidden - нет доступа к этой модели")
            elif "401" in error_str:
                print(f"   🔍 HTTP 401 Unauthorized - неверный API ключ")
            elif "429" in error_str:
                print(f"   🔍 HTTP 429 Too Many Requests - превышен лимит")
            elif "404" in error_str:
                print(f"   🔍 HTTP 404 Not Found - модель не найдена")
    
    print("\n" + "="*80)
    print("РЕЗУЛЬТАТ")
    print("="*80)
    print("❌ Ни одна из моделей не работает с этим API ключом")
    print("\n💡 ВОЗМОЖНЫЕ ПРИЧИНЫ:")
    print("   1. API ключ не имеет доступа к Gemini Live API")
    print("   2. Gemini Live API не включен в Google Cloud Console")
    print("   3. Модели недоступны для этого ключа/проекта")
    print("   4. Региональные ограничения")
    print("   5. Исчерпана квота")
    
    return False

if __name__ == "__main__":
    import asyncio
    success = asyncio.run(test_api_key())
    sys.exit(0 if success else 1)



