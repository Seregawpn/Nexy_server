#!/usr/bin/env python3
"""
Скрипт для получения списка реальных развертываний Azure OpenAI
Пробует несколько способов получения информации
"""

import json
import sys
import subprocess
import requests
from typing import List, Dict, Optional


def get_deployments_via_api(base_url: str, api_key: str) -> Optional[List[Dict]]:
    """Получает список развертываний через Azure OpenAI API"""
    endpoints = [
        "/openai/deployments?api-version=2024-02-15-preview",
        "/openai/deployments?api-version=2023-05-15",
        "/openai/deployments?api-version=2023-12-01-preview",
    ]
    
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }
    
    for endpoint in endpoints:
        url = f"{base_url.rstrip('/')}{endpoint}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, dict) and "data" in data:
                    deployments = data["data"]
                    if deployments and isinstance(deployments, list):
                        return deployments
        except Exception as e:
            continue
    
    return None


def get_deployments_via_cli(resource_name: str, resource_group: Optional[str] = None) -> Optional[List[Dict]]:
    """Получает список развертываний через Azure CLI"""
    try:
        cmd = ["az", "cognitiveservices", "account", "deployment", "list"]
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
                return None
    except Exception:
        return None
    
    return None


def get_resource_info_via_cli(resource_name: str) -> Optional[Dict]:
    """Получает информацию о ресурсе через Azure CLI"""
    try:
        # Пробуем найти ресурс
        cmd = ["az", "cognitiveservices", "account", "list", "--query", f"[?name=='{resource_name}']"]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            try:
                resources = json.loads(result.stdout)
                if resources and len(resources) > 0:
                    return resources[0]
            except json.JSONDecodeError:
                pass
    except Exception:
        pass
    
    return None


def format_deployment_info(deployment: Dict) -> str:
    """Форматирует информацию о развертывании"""
    name = deployment.get("id", deployment.get("name", "unknown"))
    model = deployment.get("properties", {}).get("model", {})
    if isinstance(model, dict):
        model_name = model.get("name", model.get("format", "unknown"))
    else:
        model_name = str(model)
    
    status = deployment.get("properties", {}).get("provisioningState", 
                 deployment.get("status", "unknown"))
    
    created = deployment.get("properties", {}).get("createdAt",
              deployment.get("created_at", "unknown"))
    
    return f"   • {name}"
    return f"   • {name} (модель: {model_name}, статус: {status})"


def main():
    """Главная функция"""
    if len(sys.argv) < 3:
        print("Использование: python3 scripts/get_azure_deployments.py <base_url> <api_key> [resource_group]")
        print("\nПример:")
        print("  python3 scripts/get_azure_deployments.py \\")
        print("    'https://nexy-ai-core-01.openai.azure.com' \\")
        print("    'ваш_ключ'")
        sys.exit(1)
    
    base_url = sys.argv[1].rstrip('/')
    api_key = sys.argv[2]
    resource_group = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Извлекаем имя ресурса из URL
    resource_name = base_url.split("//")[1].split(".")[0] if "//" in base_url else ""
    
    print("=" * 70)
    print("🔍 ПОЛУЧЕНИЕ СПИСКА РАЗВЕРТЫВАНИЙ AZURE OPENAI")
    print("=" * 70)
    print(f"\n📋 Конфигурация:")
    print(f"   Base URL: {base_url}")
    print(f"   Resource Name: {resource_name}")
    if resource_group:
        print(f"   Resource Group: {resource_group}")
    print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
    print()
    
    deployments = None
    method = None
    
    # Способ 1: Через Azure OpenAI API
    print("📋 Способ 1: Получение через Azure OpenAI API...")
    deployments = get_deployments_via_api(base_url, api_key)
    
    if deployments:
        method = "Azure OpenAI API"
        print(f"   ✅ Найдено развертываний: {len(deployments)}")
    else:
        print("   ❌ Не удалось получить через API")
    
    print()
    
    # Способ 2: Через Azure CLI
    if not deployments:
        print("📋 Способ 2: Получение через Azure CLI...")
        
        # Сначала получаем информацию о ресурсе
        resource_info = get_resource_info_via_cli(resource_name)
        if resource_info:
            actual_resource_group = resource_info.get("resourceGroup", resource_group)
            print(f"   ✅ Ресурс найден в группе: {actual_resource_group}")
            
            deployments = get_deployments_via_cli(resource_name, actual_resource_group)
            
            if deployments:
                method = "Azure CLI"
                print(f"   ✅ Найдено развертываний: {len(deployments)}")
            else:
                print("   ❌ Развертывания не найдены через Azure CLI")
        else:
            print("   ⚠️  Ресурс не найден через Azure CLI")
            print("   💡 Убедитесь, что:")
            print("      - Azure CLI установлен: https://docs.microsoft.com/cli/azure/install-azure-cli")
            print("      - Выполнен вход: az login")
            print("      - У вас есть права на ресурс")
    
    print()
    
    # Вывод результатов
    if deployments and len(deployments) > 0:
        print("=" * 70)
        print(f"✅ РЕЗУЛЬТАТ: Найдено {len(deployments)} развертываний (через {method})")
        print("=" * 70)
        print("\n📦 СПИСОК РАЗВЕРТЫВАНИЙ:\n")
        
        for i, dep in enumerate(deployments, 1):
            name = dep.get("id", dep.get("name", "unknown"))
            model = dep.get("properties", {}).get("model", {})
            
            if isinstance(model, dict):
                model_name = model.get("name", model.get("format", "unknown"))
            else:
                model_name = str(model) if model else "unknown"
            
            status = dep.get("properties", {}).get("provisioningState",
                       dep.get("status", "unknown"))
            
            print(f"{i}. Имя: {name}")
            print(f"   Модель: {model_name}")
            print(f"   Статус: {status}")
            print()
        
        print("=" * 70)
        print("💡 ИСПОЛЬЗОВАНИЕ:")
        print(f"\n   Используйте одно из имен выше для тестирования:")
        first_deployment_name = deployments[0].get("id", deployments[0].get("name", "unknown"))
        print(f"\n   python3 scripts/test_azure_openai_config.py \\")
        print(f"     '{base_url}' \\")
        print(f"     '{first_deployment_name}' \\")
        print(f"     '{api_key}'")
        
    else:
        print("=" * 70)
        print("❌ РЕЗУЛЬТАТ: Развертывания не найдены")
        print("=" * 70)
        
        print("\n🔧 ВОЗМОЖНЫЕ ПРИЧИНЫ:")
        print("   1. Развертывания еще не созданы в этом ресурсе")
        print("   2. Ресурс не имеет доступа к Azure OpenAI")
        print("   3. Нужны дополнительные права доступа")
        
        print("\n💡 РЕШЕНИЕ:")
        print("\n1. Создайте развертывание через Azure Portal:")
        print("   - Откройте: https://portal.azure.com")
        print("   - Найдите ресурс: nexy-ai-core-01")
        print("   - Перейдите в: Model deployments")
        print("   - Нажмите: Create или Deploy model")
        
        print("\n2. Или используйте Azure OpenAI Studio:")
        print("   - Откройте: https://oai.azure.com/")
        print("   - Выберите ваш ресурс")
        print("   - Перейдите в: Deployments")
        print("   - Создайте новое развертывание")
        
        print("\n📚 Подробная инструкция:")
        print("   См. Docs/AZURE_OPENAI_SOLUTION.md")
        
        sys.exit(1)


if __name__ == "__main__":
    main()
