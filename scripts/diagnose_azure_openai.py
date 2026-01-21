#!/usr/bin/env python3
"""
Диагностический скрипт для проверки Azure OpenAI конфигурации
Проверяет различные варианты URL и форматов
"""

import json
import sys
import requests
from typing import Tuple, Dict


def test_endpoint(url: str, api_key: str, description: str) -> Tuple[bool, Dict]:
    """Тестирует endpoint и возвращает результат"""
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }
    
    try:
        # Пробуем простой GET запрос
        response = requests.get(url, headers=headers, timeout=10)
        
        result = {
            "success": response.status_code in [200, 401],  # 401 означает, что endpoint существует
            "status_code": response.status_code,
            "url": url,
            "description": description
        }
        
        try:
            result["response"] = response.json()
        except:
            result["response"] = response.text[:200]
        
        return result["success"], result
        
    except requests.exceptions.RequestException as e:
        return False, {
            "success": False,
            "error": str(e),
            "url": url,
            "description": description
        }


def main():
    """Главная функция"""
    if len(sys.argv) < 3:
        print("Использование: python3 scripts/diagnose_azure_openai.py <base_url> <api_key>")
        sys.exit(1)
    
    base_url = sys.argv[1].rstrip('/')
    api_key = sys.argv[2]
    
    print("=" * 70)
    print("🔍 ДИАГНОСТИКА AZURE OPENAI КОНФИГУРАЦИИ")
    print("=" * 70)
    print(f"\n📋 Конфигурация:")
    print(f"   Base URL: {base_url}")
    print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
    print()
    
    # Тестируем различные варианты URL
    test_urls = [
        (f"{base_url}/openai/deployments", "Список развертываний (стандартный)"),
        (f"{base_url}/openai/models", "Список моделей (альтернативный)"),
        (f"{base_url}/", "Корневой endpoint"),
        (f"{base_url}/health", "Health check"),
    ]
    
    print("🧪 Тестирую различные endpoints...\n")
    
    working_urls = []
    failed_urls = []
    
    for url, description in test_urls:
        success, result = test_endpoint(url, api_key, description)
        
        if success:
            working_urls.append((url, description, result))
            print(f"✅ {description}")
            print(f"   URL: {url}")
            print(f"   HTTP {result['status_code']}")
        else:
            failed_urls.append((url, description, result))
            print(f"❌ {description}")
            print(f"   URL: {url}")
            if "status_code" in result:
                print(f"   HTTP {result['status_code']}")
            if "error" in result:
                print(f"   Ошибка: {result['error']}")
        print()
    
    print("=" * 70)
    print("📊 РЕЗУЛЬТАТЫ")
    print("=" * 70)
    
    if working_urls:
        print(f"\n✅ Работающие endpoints: {len(working_urls)}")
        for url, desc, result in working_urls:
            print(f"   • {desc}: {url}")
    else:
        print("\n❌ Ни один endpoint не работает")
    
    print(f"\n❌ Не работающие endpoints: {len(failed_urls)}")
    
    print("\n🔧 РЕКОМЕНДАЦИИ:")
    
    if not working_urls:
        print("   1. Проверьте правильность Base URL в Azure Portal")
        print("   2. Проверьте правильность API ключа")
        print("   3. Убедитесь, что ресурс Azure OpenAI активен")
        print("   4. Проверьте, что у вас есть доступ к ресурсу")
    else:
        print("   ✅ Endpoint работает! Проблема может быть в:")
        print("   1. Неправильном Deployment Name")
        print("   2. Развертывание еще не создано или не готово")
        print("   3. Развертывание находится в другом регионе")
    
    print("\n💡 СЛЕДУЮЩИЕ ШАГИ:")
    print("   1. Откройте Azure Portal → ваш ресурс Azure OpenAI")
    print("   2. Перейдите в 'Model deployments' или 'Deployments'")
    print("   3. Проверьте список развертываний и их имена")
    print("   4. Убедитесь, что развертывание имеет статус 'Succeeded'")


if __name__ == "__main__":
    main()
