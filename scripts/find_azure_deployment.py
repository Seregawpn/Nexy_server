#!/usr/bin/env python3
"""
Скрипт для поиска правильного Deployment Name
Пробует различные варианты имен и форматы
"""

import requests
import sys
from typing import List, Tuple, Dict


def test_deployment_name(base_url: str, deployment_name: str, api_key: str) -> Tuple[bool, Dict]:
    """Тестирует конкретное имя развертывания"""
    url = f"{base_url.rstrip('/')}/openai/deployments/{deployment_name}/chat/completions?api-version=2024-02-15-preview"
    
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    
    payload = {
        "messages": [
            {"role": "user", "content": "Hello"}
        ],
        "max_tokens": 10
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        return response.status_code == 200, {
            "status_code": response.status_code,
            "deployment_name": deployment_name,
            "response": response.json() if response.status_code == 200 else response.text[:200]
        }
    except Exception as e:
        return False, {
            "deployment_name": deployment_name,
            "error": str(e)
        }


def try_common_deployment_names(base_url: str, api_key: str) -> List[Dict]:
    """Пробует распространенные имена развертываний"""
    common_names = [
        "gpt-4",
        "gpt-4o",
        "gpt-4-turbo",
        "gpt-35-turbo",
        "gpt-3.5-turbo",
        "gpt-4o-mini",
        "OpenAICreate-20260120103424",
        "openAICreate-20260120103424",
        "openai-create-20260120103424",
    ]
    
    print("🔍 Пробую распространенные имена развертываний...\n")
    
    results = []
    for name in common_names:
        print(f"   Тестирую: {name}...", end=" ")
        success, result = test_deployment_name(base_url, name, api_key)
        
        if success:
            print("✅ РАБОТАЕТ!")
            results.append(result)
        else:
            status = result.get("status_code", "error")
            print(f"❌ HTTP {status}")
        
        result["success"] = success
        results.append(result)
    
    return results


def try_variations(base_name: str, base_url: str, api_key: str) -> List[Dict]:
    """Пробует варианты имени (без пробелов, разный регистр)"""
    variations = [
        base_name.strip(),  # Без пробелов
        base_name.strip().lower(),  # Нижний регистр
        base_name.strip().upper(),  # Верхний регистр
        base_name.strip().capitalize(),  # Первая буква заглавная
    ]
    
    # Убираем дубликаты
    variations = list(dict.fromkeys(variations))
    
    print(f"\n🔍 Пробую варианты имени '{base_name}':\n")
    
    results = []
    for var in variations:
        if var == base_name.strip():
            continue  # Уже проверили
        
        print(f"   Тестирую: '{var}'...", end=" ")
        success, result = test_deployment_name(base_url, var, api_key)
        
        if success:
            print("✅ РАБОТАЕТ!")
            results.append(result)
        else:
            status = result.get("status_code", "error")
            print(f"❌ HTTP {status}")
        
        result["success"] = success
        results.append(result)
    
    return results


def main():
    """Главная функция"""
    if len(sys.argv) < 4:
        print("Использование: python3 scripts/find_azure_deployment.py <base_url> <api_key> <deployment_name>")
        print("\nПример:")
        print("  python3 scripts/find_azure_deployment.py \\")
        print("    'https://nexy-ai-core-01.openai.azure.com' \\")
        print("    'ваш_ключ' \\")
        print("    'OpenAICreate-20260120103424'")
        sys.exit(1)
    
    base_url = sys.argv[1].rstrip('/')
    api_key = sys.argv[2]
    deployment_name = sys.argv[3]
    
    print("=" * 70)
    print("🔍 ПОИСК ПРАВИЛЬНОГО DEPLOYMENT NAME")
    print("=" * 70)
    print(f"\n📋 Конфигурация:")
    print(f"   Base URL: {base_url}")
    print(f"   Deployment Name (исходный): '{deployment_name}'")
    print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
    print()
    
    # Шаг 1: Проверяем исходное имя (без пробелов)
    print("📋 Шаг 1: Проверка исходного имени (без пробелов)...")
    clean_name = deployment_name.strip()
    if clean_name != deployment_name:
        print(f"   ⚠️  Обнаружен пробел в имени! Оригинал: '{deployment_name}' → Очищено: '{clean_name}'")
    
    success, result = test_deployment_name(base_url, clean_name, api_key)
    
    if success:
        print(f"   ✅ УСПЕХ! Имя '{clean_name}' работает!")
        print("\n" + "=" * 70)
        print("✅ РЕЗУЛЬТАТ")
        print("=" * 70)
        print(f"\n📝 Правильное Deployment Name: {clean_name}")
        print(f"\n💡 Настройки для Cursor:")
        print(f"   Base URL: {base_url}/")
        print(f"   Deployment Name: {clean_name}")
        print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
        sys.exit(0)
    else:
        print(f"   ❌ Имя '{clean_name}' не работает (HTTP {result.get('status_code', 'error')})")
    
    print()
    
    # Шаг 2: Пробуем варианты исходного имени
    variations_results = try_variations(deployment_name, base_url, api_key)
    working = [r for r in variations_results if r.get("success")]
    
    if working:
        print("\n" + "=" * 70)
        print("✅ РЕЗУЛЬТАТ")
        print("=" * 70)
        print(f"\n📝 Найдено рабочее имя: {working[0]['deployment_name']}")
        print(f"\n💡 Настройки для Cursor:")
        print(f"   Base URL: {base_url}/")
        print(f"   Deployment Name: {working[0]['deployment_name']}")
        print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
        sys.exit(0)
    
    print()
    
    # Шаг 3: Пробуем распространенные имена
    common_results = try_common_deployment_names(base_url, api_key)
    working_common = [r for r in common_results if r.get("success")]
    
    if working_common:
        print("\n" + "=" * 70)
        print("✅ РЕЗУЛЬТАТ")
        print("=" * 70)
        print(f"\n📝 Найдено рабочее имя: {working_common[0]['deployment_name']}")
        print(f"\n💡 Настройки для Cursor:")
        print(f"   Base URL: {base_url}/")
        print(f"   Deployment Name: {working_common[0]['deployment_name']}")
        print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
        sys.exit(0)
    
    # Ничего не найдено
    print("\n" + "=" * 70)
    print("❌ РЕЗУЛЬТАТ: Развертывание не найдено")
    print("=" * 70)
    
    print("\n🔧 ЧТО ДЕЛАТЬ:")
    print("\n1. Проверьте Azure Portal:")
    print("   - Откройте: https://portal.azure.com")
    print("   - Найдите ресурс: nexy-ai-core-01")
    print("   - Перейдите в: Model deployments")
    print("   - Скопируйте ТОЧНОЕ имя развертывания (регистр важен!)")
    
    print("\n2. Создайте новое развертывание (если нет):")
    print("   - В Azure Portal → ваш ресурс → Model deployments")
    print("   - Нажмите 'Create' или 'Deploy model'")
    print("   - Выберите модель (например, gpt-4 или gpt-35-turbo)")
    print("   - Укажите имя (например, 'gpt-4')")
    print("   - Дождитесь статуса 'Succeeded'")
    
    print("\n3. Попробуйте снова с правильным именем:")
    print(f"   python3 scripts/find_azure_deployment.py \\")
    print(f"     '{base_url}' \\")
    print(f"     '{api_key}' \\")
    print(f"     'ПРАВИЛЬНОЕ_ИМЯ_ИЗ_AZURE_PORTAL'")
    
    sys.exit(1)


if __name__ == "__main__":
    main()
