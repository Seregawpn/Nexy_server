#!/usr/bin/env python3
"""
Финальная проверка Azure OpenAI конфигурации
Проверяет все возможные варианты и дает четкие инструкции
"""

import json
import sys
import requests
from typing import Dict, List, Optional


def check_endpoint(base_url: str, api_key: str, endpoint: str, description: str) -> Dict:
    """Проверяет конкретный endpoint"""
    url = f"{base_url.rstrip('/')}{endpoint}"
    
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        # Пробуем GET запрос
        response = requests.get(url, headers=headers, timeout=10)
        
        # Пробуем распарсить JSON, если не получается - берем текст
        try:
            response_data = response.json()
        except:
            response_data = response.text[:500]
        
        return {
            "success": response.status_code in [200, 401],  # 401 означает, что endpoint существует
            "status_code": response.status_code,
            "url": url,
            "description": description,
            "response": response_data
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "url": url,
            "description": description
        }


def try_get_deployments(base_url: str, api_key: str) -> Optional[List[str]]:
    """Пробует получить список развертываний разными способами"""
    endpoints = [
        ("/openai/deployments?api-version=2024-02-15-preview", "Стандартный API"),
        ("/openai/deployments?api-version=2023-05-15", "Старая версия API"),
        ("/openai/models?api-version=2024-02-15-preview", "Список моделей"),
    ]
    
    print("🔍 Пробую получить список развертываний...\n")
    
    for endpoint, desc in endpoints:
        result = check_endpoint(base_url, api_key, endpoint, desc)
        
        if result["success"] and result["status_code"] == 200:
            try:
                data = result["response"]
                if isinstance(data, dict) and "data" in data:
                    deployments = data["data"]
                    if deployments:
                        names = [dep.get("id", dep.get("name", "unknown")) for dep in deployments]
                        return names
            except:
                pass
    
    return None


def main():
    """Главная функция"""
    if len(sys.argv) < 3:
        print("Использование: python3 scripts/azure_openai_final_check.py <base_url> <api_key>")
        sys.exit(1)
    
    base_url = sys.argv[1].rstrip('/')
    api_key = sys.argv[2]
    
    print("=" * 70)
    print("🔍 ФИНАЛЬНАЯ ПРОВЕРКА AZURE OPENAI")
    print("=" * 70)
    print(f"\n📋 Конфигурация:")
    print(f"   Base URL: {base_url}")
    print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
    print()
    
    # Шаг 1: Проверка базового подключения
    print("📋 Шаг 1: Проверка базового подключения...")
    root_check = check_endpoint(base_url, api_key, "/", "Корневой endpoint")
    
    if root_check["success"]:
        print("   ✅ Подключение работает!")
    else:
        print("   ❌ Проблема с подключением!")
        print(f"   Ошибка: {root_check.get('error', 'unknown')}")
        sys.exit(1)
    
    print()
    
    # Шаг 2: Попытка получить список развертываний
    print("📋 Шаг 2: Поиск развертываний...")
    deployments = try_get_deployments(base_url, api_key)
    
    if deployments:
        print(f"   ✅ Найдено развертываний: {len(deployments)}")
        print("\n📦 Доступные развертывания:")
        for i, name in enumerate(deployments, 1):
            print(f"   {i}. {name}")
        
        print("\n" + "=" * 70)
        print("✅ РЕЗУЛЬТАТ: Развертывания найдены!")
        print("=" * 70)
        print(f"\n💡 Используйте одно из имен выше для тестирования:")
        print(f"\n   python3 scripts/test_azure_openai_config.py \\")
        print(f"     '{base_url}' \\")
        print(f"     '{deployments[0]}' \\")
        print(f"     '{api_key}'")
        
    else:
        print("   ❌ Не удалось получить список развертываний")
        
        print("\n" + "=" * 70)
        print("❌ РЕЗУЛЬТАТ: Развертывания не найдены")
        print("=" * 70)
        
        print("\n🔧 ВОЗМОЖНЫЕ ПРИЧИНЫ:")
        print("   1. Развертывания еще не созданы в этом ресурсе")
        print("   2. Ресурс не имеет доступа к моделям Azure OpenAI")
        print("   3. Используется неправильный Base URL")
        print("   4. Нужны дополнительные права доступа")
        
        print("\n💡 РЕШЕНИЕ:")
        print("\n1. Создайте развертывание через Azure Portal:")
        print("   - Откройте: https://portal.azure.com")
        print("   - Найдите ресурс: nexy-ai-core-01")
        print("   - Перейдите в: Model deployments")
        print("   - Нажмите: Create или Deploy model")
        print("   - Выберите модель (например, gpt-4 или gpt-35-turbo)")
        print("   - Укажите имя (например, 'gpt-4')")
        print("   - Дождитесь статуса 'Succeeded'")
        
        print("\n2. Или используйте Azure OpenAI Studio:")
        print("   - Откройте: https://oai.azure.com/")
        print("   - Выберите ваш ресурс")
        print("   - Перейдите в: Deployments")
        print("   - Создайте новое развертывание")
        
        print("\n3. После создания развертывания запустите тест:")
        print(f"   python3 scripts/find_azure_deployment.py \\")
        print(f"     '{base_url}' \\")
        print(f"     '{api_key}' \\")
        print(f"     'ИМЯ_РАЗВЕРТЫВАНИЯ'")
        
        print("\n📚 Подробная инструкция:")
        print("   См. Docs/AZURE_OPENAI_CREATE_DEPLOYMENT.md")
        
        sys.exit(1)


if __name__ == "__main__":
    main()
