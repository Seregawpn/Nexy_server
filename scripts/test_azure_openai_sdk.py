#!/usr/bin/env python3
"""
Тестовый скрипт для проверки Azure OpenAI через официальный SDK
"""

import sys
from openai import AzureOpenAI


def test_azure_openai(endpoint: str, deployment: str, api_key: str, api_version: str = "2024-12-01-preview"):
    """Тестирует подключение к Azure OpenAI через официальный SDK"""
    
    print("=" * 70)
    print("🧪 ТЕСТИРОВАНИЕ AZURE OPENAI ЧЕРЕЗ SDK")
    print("=" * 70)
    print(f"\n📋 Конфигурация:")
    print(f"   Endpoint: {endpoint}")
    print(f"   Deployment: {deployment}")
    print(f"   API Version: {api_version}")
    print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
    print()
    
    try:
        # Создаем клиент
        print("📋 Шаг 1: Создание клиента Azure OpenAI...")
        client = AzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=api_key,
        )
        print("   ✅ Клиент создан успешно")
        print()
        
        # Тестовый запрос
        print("📋 Шаг 2: Отправка тестового запроса...")
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": "Say 'Hello, Azure OpenAI is working!' in one sentence.",
                }
            ],
            max_completion_tokens=16384,
            model=deployment
        )
        
        print("   ✅ Запрос выполнен успешно!")
        print()
        
        # Выводим результат
        print("=" * 70)
        print("✅ УСПЕХ! Azure OpenAI работает!")
        print("=" * 70)
        print(f"\n📝 Ответ модели:")
        print("-" * 70)
        print(response.choices[0].message.content)
        print("-" * 70)
        
        print(f"\n📊 Детали ответа:")
        print(f"   Model: {response.model}")
        print(f"   Finish reason: {response.choices[0].finish_reason}")
        print(f"   Usage:")
        print(f"      Prompt tokens: {response.usage.prompt_tokens}")
        print(f"      Completion tokens: {response.usage.completion_tokens}")
        print(f"      Total tokens: {response.usage.total_tokens}")
        
        print("\n" + "=" * 70)
        print("💡 НАСТРОЙКИ ДЛЯ CURSOR:")
        print("=" * 70)
        print(f"\n   Base URL: {endpoint.rstrip('/')}/")
        print(f"   Deployment Name: {deployment}")
        print(f"   API Key: {api_key}")
        print(f"   API Version: {api_version}")
        
        return True
        
    except Exception as e:
        print("=" * 70)
        print("❌ ОШИБКА!")
        print("=" * 70)
        print(f"\n📋 Детали ошибки:")
        print(f"   Тип: {type(e).__name__}")
        print(f"   Сообщение: {str(e)}")
        
        print("\n🔧 ВОЗМОЖНЫЕ ПРИЧИНЫ:")
        if "401" in str(e) or "Unauthorized" in str(e):
            print("   1. Неверный API ключ")
            print("   2. Ключ истек или был удален")
        elif "404" in str(e) or "not found" in str(e).lower():
            print("   1. Развертывание не существует")
            print("   2. Неправильное имя развертывания")
            print("   3. Неправильный endpoint")
        elif "module" in str(e).lower() or "import" in str(e).lower():
            print("   1. Библиотека openai не установлена")
            print("   2. Установите: pip install openai")
        else:
            print("   1. Проверьте правильность всех параметров")
            print("   2. Проверьте доступность Azure OpenAI сервиса")
        
        return False


def main():
    """Главная функция"""
    if len(sys.argv) < 4:
        print("Использование: python3 scripts/test_azure_openai_sdk.py <endpoint> <deployment> <api_key> [api_version]")
        print("\nПример:")
        print("  python3 scripts/test_azure_openai_sdk.py \\")
        print("    'https://sereg-mkmt1o4s-eastus2.cognitiveservices.azure.com/' \\")
        print("    'gpt-5.2-chat' \\")
        print("    'ваш_ключ'")
        sys.exit(1)
    
    endpoint = sys.argv[1].rstrip('/')
    if not endpoint.startswith('http'):
        endpoint = f"https://{endpoint}"
    
    deployment = sys.argv[2]
    api_key = sys.argv[3]
    api_version = sys.argv[4] if len(sys.argv) > 4 else "2024-12-01-preview"
    
    success = test_azure_openai(endpoint, deployment, api_key, api_version)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
