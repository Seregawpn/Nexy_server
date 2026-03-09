#!/usr/bin/env python3
"""
Тестовые запросы к Gemini Live API
Проверяет:
1. Обычные текстовые запросы
2. Запросы на открытие приложений (MCP команды)
3. Формат ответов (текст и JSON)
"""

import sys
import os
import json
import asyncio
from pathlib import Path

# Добавляем путь к серверу
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "server"))

# API ключ
API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL = "gemini-live-2.5-flash-preview"

# Загружаем системный промпт из конфига
def get_system_prompt():
    """Загружает системный промпт из конфигурации"""
    try:
        from config.unified_config import get_config
        config = get_config()
        return config.text_processing.gemini_system_prompt
    except Exception as e:
        print(f"⚠️  Не удалось загрузить системный промпт: {e}")
        return None

async def test_request(client, model_name, prompt, system_prompt=None, test_name=""):
    """Отправляет тестовый запрос к модели"""
    print(f"\n{'='*80}")
    print(f"ТЕСТ: {test_name}")
    print(f"{'='*80}")
    print(f"📝 Запрос: {prompt}")
    
    try:
        live_config = {
            "response_modalities": ["TEXT"]
        }
        
        # Добавляем системный промпт если есть
        if system_prompt:
            from google.genai import types
            try:
                if hasattr(types, 'Content') and hasattr(types, 'Part'):
                    live_config["system_instruction"] = types.Content(
                        parts=[types.Part.from_text(text=system_prompt)],
                        role="user"
                    )
                else:
                    live_config["system_instruction"] = system_prompt
            except Exception as e:
                print(f"⚠️  Не удалось добавить system_instruction: {e}")
        
        async with client.aio.live.connect(model=model_name, config=live_config) as session:
            # Отправляем запрос
            await session.send_client_content(
                turns={"role": "user", "parts": [{"text": prompt}]},
                turn_complete=True
            )
            
            # Собираем ответ
            full_response = ""
            response_received = False
            
            print("\n📥 Ответ от модели:")
            async for response in session.receive():
                if response.text:
                    chunk = response.text
                    full_response += chunk
                    print(chunk, end="", flush=True)
                    response_received = True
            
            print("\n")  # Новая строка после ответа
            
            if not response_received:
                print("❌ Ответ не получен")
                return False
            
            # Анализируем ответ
            print(f"\n📊 Анализ ответа:")
            print(f"   Длина: {len(full_response)} символов")
            
            # Проверяем наличие JSON
            json_found = False
            try:
                # Пытаемся найти JSON в ответе
                json_start = full_response.find('{')
                json_end = full_response.rfind('}') + 1
                
                if json_start >= 0 and json_end > json_start:
                    json_str = full_response[json_start:json_end]
                    try:
                        json_data = json.loads(json_str)
                        json_found = True
                        print(f"   ✅ JSON найден и валиден")
                        print(f"   Структура: {list(json_data.keys())}")
                        
                        # Проверяем наличие команды
                        if 'command' in json_data:
                            print(f"   ✅ Команда найдена: {json_data.get('command')}")
                            if 'args' in json_data:
                                print(f"   ✅ Аргументы: {json_data.get('args')}")
                        if 'session_id' in json_data:
                            print(f"   ✅ session_id: {json_data.get('session_id')}")
                    except json.JSONDecodeError:
                        print(f"   ⚠️  JSON найден, но невалиден")
            except Exception as e:
                print(f"   ⚠️  Ошибка анализа JSON: {e}")
            
            if not json_found:
                print(f"   ℹ️  Обычный текстовый ответ (без JSON команды)")
            
            return True
            
    except Exception as e:
        error_str = str(e)
        print(f"\n❌ Ошибка: {error_str}")
        
        if "403" in error_str:
            print("   🔍 HTTP 403 - нет доступа")
        elif "401" in error_str:
            print("   🔍 HTTP 401 - неверный API ключ")
        elif "429" in error_str:
            print("   🔍 HTTP 429 - превышен лимит")
        
        return False

async def main():
    """Основная функция тестирования"""
    print("\n" + "="*80)
    print("ТЕСТИРОВАНИЕ GEMINI LIVE API")
    print("="*80)
    print(f"Модель: {MODEL}")
    if not API_KEY:
        print("❌ GEMINI_API_KEY не задан")
        return 1
    print(f"API ключ: {API_KEY[:10]}...{API_KEY[-4:]}")
    
    # Загружаем системный промпт
    system_prompt = get_system_prompt()
    if system_prompt:
        print(f"\n✅ Системный промпт загружен ({len(system_prompt)} символов)")
        # Показываем первые 200 символов
        print(f"   Начало: {system_prompt[:200]}...")
    else:
        print("\n⚠️  Системный промпт не загружен, используем без него")
    
    try:
        from google import genai
        client = genai.Client(api_key=API_KEY)
        print("\n✅ Gemini клиент создан")
    except Exception as e:
        print(f"\n❌ Ошибка создания клиента: {e}")
        return 1
    
    # Тестовые запросы
    test_cases = [
        {
            "name": "Простой текстовый запрос",
            "prompt": "Привет! Как дела?",
            "expect_json": False
        },
        {
            "name": "Запрос на открытие приложения (Safari)",
            "prompt": "open Safari application please",
            "expect_json": True
        },
        {
            "name": "Запрос на открытие приложения (Calculator)",
            "prompt": "open Calculator",
            "expect_json": True
        },
        {
            "name": "Обычный вопрос",
            "prompt": "What is the weather like today?",
            "expect_json": False
        },
        {
            "name": "Запрос на открытие приложения (TextEdit)",
            "prompt": "please open TextEdit",
            "expect_json": True
        }
    ]
    
    results = []
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n\n{'#'*80}")
        print(f"ТЕСТ {i}/{len(test_cases)}")
        print(f"{'#'*80}")
        
        success = await test_request(
            client,
            MODEL,
            test_case["prompt"],
            system_prompt,
            test_case["name"]
        )
        
        results.append({
            "name": test_case["name"],
            "success": success,
            "expected_json": test_case["expect_json"]
        })
        
        # Небольшая пауза между запросами
        if i < len(test_cases):
            await asyncio.sleep(2)
    
    # Итоги
    print("\n\n" + "="*80)
    print("ИТОГИ ТЕСТИРОВАНИЯ")
    print("="*80)
    
    passed = sum(1 for r in results if r["success"])
    total = len(results)
    
    for result in results:
        status = "✅ PASS" if result["success"] else "❌ FAIL"
        print(f"{status} - {result['name']}")
    
    print(f"\n📊 Результат: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("\n🎉 Все тесты пройдены успешно!")
        return 0
    else:
        print(f"\n⚠️  {total - passed} тест(ов) не пройдено")
        return 1

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))


