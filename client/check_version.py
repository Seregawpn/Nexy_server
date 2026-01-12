#!/usr/bin/env python3
"""Проверка версий клиента и сервера"""

import json
import sys
import requests
import yaml
from pathlib import Path

def get_client_version():
    """Получает версию клиента из конфигурации"""
    config_path = Path(__file__).parent / "config" / "unified_config.yaml"
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        return config.get('app', {}).get('version', 'unknown')
    except Exception as e:
        print(f"❌ Ошибка чтения конфигурации: {e}")
        return None

def get_server_version():
    """Получает версию сервера"""
    server_url = "https://20.63.24.187"
    
    try:
        # Пробуем health endpoint
        response = requests.get(f"{server_url}/health", verify=False, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get('latest_version'), data.get('latest_build')
    except Exception as e:
        print(f"⚠️ Ошибка получения версии с /health: {e}")
    
    try:
        # Пробуем status endpoint
        response = requests.get(f"{server_url}/status", verify=False, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get('latest_version'), data.get('latest_build')
    except Exception as e:
        print(f"⚠️ Ошибка получения версии с /status: {e}")
    
    return None, None

def compare_versions(client_ver, server_ver):
    """Сравнивает версии"""
    if not client_ver or not server_ver:
        return None
    
    # Простое сравнение строк (для семантического версионирования)
    client_parts = [int(x) for x in client_ver.split('.')]
    server_parts = [int(x) for x in server_ver.split('.')]
    
    for i in range(max(len(client_parts), len(server_parts))):
        client_part = client_parts[i] if i < len(client_parts) else 0
        server_part = server_parts[i] if i < len(server_parts) else 0
        
        if client_part > server_part:
            return "newer"  # Клиент новее
        elif client_part < server_part:
            return "older"  # Клиент старше
    
    return "equal"  # Версии равны

def main():
    print("=" * 70)
    print("🔍 ПРОВЕРКА ВЕРСИЙ ДЛЯ ОБНОВЛЕНИЯ")
    print("=" * 70)
    
    # Получаем версию клиента
    print("\n📱 Клиент:")
    client_version = get_client_version()
    if client_version:
        print(f"   Версия: {client_version}")
    else:
        print("   ❌ Не удалось определить версию клиента")
        return 1
    
    # Получаем версию сервера
    print("\n🌐 Сервер:")
    server_version, server_build = get_server_version()
    if server_version:
        print(f"   Версия: {server_version}")
        if server_build and server_build != server_version:
            print(f"   Build: {server_build}")
    else:
        print("   ❌ Не удалось получить версию сервера")
        print("   Проверьте доступность сервера")
        return 1
    
    # Сравниваем версии
    print("\n📊 Сравнение:")
    comparison = compare_versions(client_version, server_version)
    
    if comparison == "equal":
        print(f"   ✅ Версии совпадают: {client_version} = {server_version}")
        print("   Обновление не требуется")
    elif comparison == "newer":
        print(f"   ⬆️  Клиент новее сервера: {client_version} > {server_version}")
        print("   Клиент использует более новую версию")
    elif comparison == "older":
        print(f"   ⬇️  Клиент старше сервера: {client_version} < {server_version}")
        print("   ⚠️  ТРЕБУЕТСЯ ОБНОВЛЕНИЕ КЛИЕНТА")
        print(f"   Рекомендуется обновить до версии {server_version}")
    else:
        print("   ⚠️  Не удалось сравнить версии")
    
    print("\n" + "=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(main())
