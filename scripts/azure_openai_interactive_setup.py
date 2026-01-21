#!/usr/bin/env python3
"""
Интерактивный скрипт для настройки и тестирования Azure OpenAI
Помогает пошагово проверить конфигурацию
"""

import json
import os
import sys
import subprocess
import requests
from typing import Optional, Dict, List, Tuple


def check_azure_cli() -> bool:
    """Проверяет, установлен ли Azure CLI"""
    try:
        result = subprocess.run(
            ["az", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def get_deployments_via_cli(resource_name: str, resource_group: Optional[str] = None) -> List[Dict]:
    """Получает список развертываний через Azure CLI"""
    if not check_azure_cli():
        return []
    
    try:
        cmd = ["az", "cognitiveservices", "account", "list-deployments"]
        cmd.extend(["--name", resource_name])
        
        if resource_group:
            cmd.extend(["--resource-group", resource_group])
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            try:
                deployments = json.loads(result.stdout)
                return deployments if isinstance(deployments, list) else []
            except json.JSONDecodeError:
                return []
    except Exception as e:
        print(f"⚠️  Ошибка при получении развертываний через Azure CLI: {e}")
    
    return []


def test_deployment(base_url: str, deployment_name: str, api_key: str) -> Tuple[bool, Dict]:
    """Тестирует конкретное развертывание"""
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
            "response": response.json() if response.status_code == 200 else response.text
        }
    except Exception as e:
        return False, {"error": str(e)}


def interactive_setup():
    """Интерактивная настройка"""
    print("=" * 70)
    print("🔧 ИНТЕРАКТИВНАЯ НАСТРОЙКА AZURE OPENAI")
    print("=" * 70)
    print()
    
    # Шаг 1: Base URL
    print("📋 Шаг 1: Base URL")
    base_url = input("Введите Base URL [https://nexy-ai-core-01.openai.azure.com]: ").strip()
    if not base_url:
        base_url = "https://nexy-ai-core-01.openai.azure.com"
    print(f"   ✅ Base URL: {base_url}")
    print()
    
    # Шаг 2: API Key
    print("📋 Шаг 2: API Key")
    api_key = input("Введите API ключ: ").strip()
    if not api_key:
        print("❌ API ключ обязателен!")
        sys.exit(1)
    print(f"   ✅ API Key: {api_key[:10]}...{api_key[-4:]}")
    print()
    
    # Шаг 3: Проверка подключения
    print("📋 Шаг 3: Проверка подключения...")
    test_url = f"{base_url.rstrip('/')}/"
    try:
        response = requests.get(test_url, headers={"api-key": api_key}, timeout=10)
        if response.status_code == 200:
            print("   ✅ Подключение работает!")
        else:
            print(f"   ⚠️  HTTP {response.status_code} - возможно проблема с ключом")
    except Exception as e:
        print(f"   ❌ Ошибка подключения: {e}")
        sys.exit(1)
    print()
    
    # Шаг 4: Получение списка развертываний
    print("📋 Шаг 4: Поиск развертываний...")
    
    # Пробуем через Azure CLI
    resource_name = base_url.split("//")[1].split(".")[0] if "//" in base_url else ""
    print(f"   🔍 Пробую получить список через Azure CLI (ресурс: {resource_name})...")
    
    deployments_cli = get_deployments_via_cli(resource_name)
    
    if deployments_cli:
        print(f"   ✅ Найдено развертываний через Azure CLI: {len(deployments_cli)}")
        print("\n📦 Доступные развертывания:")
        for i, dep in enumerate(deployments_cli, 1):
            dep_name = dep.get("name", dep.get("id", "unknown"))
            model = dep.get("properties", {}).get("model", {}).get("name", "unknown")
            status = dep.get("properties", {}).get("provisioningState", "unknown")
            print(f"   {i}. {dep_name} (модель: {model}, статус: {status})")
    else:
        print("   ⚠️  Не удалось получить список через Azure CLI")
        print("   💡 Убедитесь, что:")
        print("      - Azure CLI установлен: https://docs.microsoft.com/cli/azure/install-azure-cli")
        print("      - Выполнен вход: az login")
        print("      - У вас есть права на ресурс")
    
    print()
    
    # Шаг 5: Выбор или ввод Deployment Name
    print("📋 Шаг 5: Deployment Name")
    if deployments_cli:
        print("   Выберите развертывание из списка выше или введите свое:")
    else:
        print("   Введите имя развертывания из Azure Portal:")
        print("   (Откройте Azure Portal → ваш ресурс → Model deployments)")
    
    deployment_name = input("Deployment Name: ").strip()
    
    if not deployment_name:
        print("❌ Deployment Name обязателен!")
        sys.exit(1)
    
    print(f"   ✅ Deployment Name: {deployment_name}")
    print()
    
    # Шаг 6: Тестирование
    print("📋 Шаг 6: Тестирование конфигурации...")
    print()
    
    success, result = test_deployment(base_url, deployment_name, api_key)
    
    if success:
        print("=" * 70)
        print("✅ УСПЕХ! Конфигурация работает!")
        print("=" * 70)
        print(f"\n📝 Настройки для Cursor:")
        print(f"   Base URL: {base_url}/")
        print(f"   Deployment Name: {deployment_name}")
        print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
        print()
        print("💡 Скопируйте эти настройки в Cursor (Cmd + , → Model → Azure OpenAI)")
    else:
        print("=" * 70)
        print("❌ ОШИБКА! Конфигурация не работает")
        print("=" * 70)
        
        if "status_code" in result:
            status = result["status_code"]
            print(f"\nHTTP Status: {status}")
            
            if status == 404:
                print("\n🔧 Возможные причины:")
                print("   1. Развертывание не существует или имя неправильное")
                print("   2. Развертывание создано менее 5 минут назад (подождите)")
                print("   3. Развертывание находится в другом ресурсе")
                print("\n💡 Что делать:")
                print("   1. Откройте Azure Portal → ваш ресурс → Model deployments")
                print("   2. Проверьте точное имя развертывания (регистр важен!)")
                print("   3. Убедитесь, что статус развертывания 'Succeeded'")
            elif status == 401:
                print("\n🔧 Возможные причины:")
                print("   1. Неверный API ключ")
                print("   2. Ключ истек или был удален")
                print("\n💡 Что делать:")
                print("   1. Получите новый ключ в Azure Portal → Keys and Endpoint")
                print("   2. Убедитесь, что используете Azure OpenAI ключ (не OpenAI API key)")
        
        sys.exit(1)


if __name__ == "__main__":
    try:
        interactive_setup()
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Неожиданная ошибка: {e}")
        sys.exit(1)
