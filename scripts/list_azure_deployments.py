#!/usr/bin/env python3
"""
Скрипт для получения списка доступных развертываний Azure OpenAI
"""

import json
import os
import sys
import requests
from typing import List, Dict


def list_deployments(base_url: str, api_key: str) -> List[Dict]:
    """Получает список развертываний из Azure OpenAI"""
    url = f"{base_url.rstrip('/')}/openai/deployments?api-version=2024-02-15-preview"
    
    headers = {
        "api-key": api_key
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("data", [])
        else:
            print(f"❌ Ошибка HTTP {response.status_code}")
            try:
                error = response.json()
                print(f"   Сообщение: {error.get('error', {}).get('message', 'unknown')}")
            except:
                print(f"   Ответ: {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка сети: {e}")
        return []


def main():
    """Главная функция"""
    # Получаем параметры
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        base_url = os.getenv("AZURE_OPENAI_BASE_URL", "https://nexy-ai-core-01.openai.azure.com")
    
    if len(sys.argv) > 2:
        api_key = sys.argv[2]
    else:
        api_key = os.getenv("AZURE_OPENAI_API_KEY", "")
    
    if not api_key:
        print("❌ API ключ не указан.")
        print("Использование: python3 scripts/list_azure_deployments.py <base_url> <api_key>")
        print("Или установите переменные окружения:")
        print("  export AZURE_OPENAI_BASE_URL='https://...'")
        print("  export AZURE_OPENAI_API_KEY='ваш_ключ'")
        sys.exit(1)
    
    print("=" * 70)
    print("🔍 ПОЛУЧЕНИЕ СПИСКА РАЗВЕРТЫВАНИЙ AZURE OPENAI")
    print("=" * 70)
    print(f"\n📋 Конфигурация:")
    print(f"   Base URL: {base_url}")
    print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
    print()
    
    deployments = list_deployments(base_url, api_key)
    
    if deployments:
        print(f"✅ Найдено развертываний: {len(deployments)}\n")
        print("📦 СПИСОК РАЗВЕРТЫВАНИЙ:")
        print("-" * 70)
        
        for i, dep in enumerate(deployments, 1):
            dep_id = dep.get("id", "unknown")
            model = dep.get("model", "unknown")
            status = dep.get("status", "unknown")
            created = dep.get("created_at", "unknown")
            
            print(f"\n{i}. Имя (ID): {dep_id}")
            print(f"   Модель: {model}")
            print(f"   Статус: {status}")
            if created != "unknown":
                print(f"   Создано: {created}")
        
        print("\n" + "=" * 70)
        print("💡 ИСПОЛЬЗОВАНИЕ:")
        print(f"   Используйте одно из имен выше как Deployment Name в Cursor")
        print(f"   Например: {deployments[0].get('id', 'ваше-развертывание')}")
    else:
        print("❌ Развертывания не найдены или произошла ошибка")
        print("\n🔧 ЧТО ПРОВЕРИТЬ:")
        print("   1. Правильность Base URL")
        print("   2. Правильность API ключа")
        print("   3. Наличие развертываний в Azure Portal")
        print("   4. Доступность Azure OpenAI сервиса")


if __name__ == "__main__":
    main()
