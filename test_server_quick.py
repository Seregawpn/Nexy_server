#!/usr/bin/env python3
"""
Быстрая проверка доступности production сервера
"""
import sys
import socket
import requests
from pathlib import Path

def check_port(host, port, timeout=5):
    """Проверка доступности порта"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"❌ Ошибка проверки порта: {e}")
        return False

def check_http_endpoint(url, timeout=10):
    """Проверка HTTP endpoint"""
    try:
        response = requests.get(url, timeout=timeout, verify=False)
        return response.status_code == 200, response.text[:200]
    except requests.exceptions.Timeout:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)

def main():
    """Главная функция"""
    print("=" * 60)
    print("Быстрая проверка production сервера")
    print("=" * 60)
    print()
    
    host = "20.151.51.172"
    port_443 = 443
    port_50051 = 50051
    
    # 1. Проверка порта 443
    print(f"1. Проверка порта {port_443}...")
    if check_port(host, port_443):
        print(f"   ✅ Порт {port_443} доступен")
    else:
        print(f"   ❌ Порт {port_443} недоступен")
    print()
    
    # 2. Проверка порта 50051
    print(f"2. Проверка порта {port_50051}...")
    if check_port(host, port_50051):
        print(f"   ✅ Порт {port_50051} доступен")
    else:
        print(f"   ❌ Порт {port_50051} недоступен")
    print()
    
    # 3. Проверка HTTP endpoints
    print("3. Проверка HTTP endpoints...")
    endpoints = [
        f"https://{host}:{port_443}/health",
        f"https://{host}:{port_443}/status",
    ]
    
    for endpoint in endpoints:
        print(f"   Проверка {endpoint}...")
        success, result = check_http_endpoint(endpoint, timeout=5)
        if success:
            print(f"   ✅ {endpoint} доступен")
        else:
            print(f"   ⚠️  {endpoint} недоступен: {result}")
    print()
    
    # 4. Проверка конфигурации
    print("4. Проверка конфигурации...")
    config_path = Path("client/config/unified_config.yaml")
    if config_path.exists():
        print(f"   ✅ Конфигурация найдена: {config_path}")
        
        import yaml
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        
        grpc_config = config.get('grpc', {})
        servers = grpc_config.get('servers', {})
        production = servers.get('production', {})
        
        if production:
            print(f"   ✅ Production сервер настроен:")
            print(f"      Host: {production.get('host')}")
            print(f"      Port: {production.get('port')}")
            print(f"      SSL: {production.get('ssl')}")
            print(f"      Timeout: {production.get('timeout')}s")
        else:
            print(f"   ⚠️  Production сервер не найден в конфигурации")
    else:
        print(f"   ❌ Конфигурация не найдена: {config_path}")
    print()
    
    print("=" * 60)
    print("Проверка завершена")
    print("=" * 60)

if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print("❌ Требуется requests. Установите: pip install requests")
        sys.exit(1)
    
    main()
