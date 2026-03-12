#!/usr/bin/env python3
"""
Проверка health/status/портов для gRPC сервера - PR-3
Валидация эндпоинтов и версий

Использование:
    python scripts/check_grpc_health.py [HOST] [PORT]
    
Примеры:
    # Production сервер
    python scripts/check_grpc_health.py nexy-prod-sergiy.canadacentral.cloudapp.azure.com 443
    
    # Локальный сервер
    python scripts/check_grpc_health.py localhost 8080
"""

import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any
from urllib.parse import urljoin

try:
    import requests
except ImportError:
    print("❌ Ошибка: требуется requests. Установите: pip install requests")
    sys.exit(1)

# Цвета для вывода
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'  # No Color


def check_http_endpoint(url: str, expected_status: int = 200) -> tuple[bool, Optional[Dict[str, Any]]]:
    """
    Проверка HTTP endpoint
    
    Args:
        url: URL для проверки
        expected_status: Ожидаемый HTTP статус
    
    Returns:
        (success, response_data)
    """
    try:
        response = requests.get(url, timeout=10, verify=False)
        
        if response.status_code == expected_status:
            # Пытаемся распарсить JSON
            try:
                data = response.json()
                return True, data
            except json.JSONDecodeError:
                # Если не JSON, возвращаем текст
                return True, {"text": response.text}
        else:
            return False, {"status_code": response.status_code, "text": response.text}
    except requests.exceptions.RequestException as e:
        return False, {"error": str(e)}


def check_port(host: str, port: int) -> bool:
    """
    Проверка доступности порта
    
    Args:
        host: Хост
        port: Порт
    
    Returns:
        True если порт доступен, False иначе
    """
    try:
        # Используем nc (netcat) для проверки порта
        result = subprocess.run(
            ["nc", "-zv", host, str(port)],
            capture_output=True,
            timeout=5
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        # Если nc не установлен, пробуем через Python socket
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except Exception:
            return False


def check_versions_match(health_data: Dict[str, Any], appcast_data: Optional[str] = None) -> tuple[bool, str]:
    """
    Проверка согласованности версий
    
    Args:
        health_data: Данные из health endpoint
        appcast_data: Данные из appcast.xml (опционально)
    
    Returns:
        (success, message)
    """
    try:
        # Получаем версии из health
        latest_version = health_data.get("latest_version")
        latest_build = health_data.get("latest_build")
        
        if not latest_version or not latest_build:
            return False, "Версии не найдены в health endpoint"
        
        # Проверяем, что версии - строки
        if not isinstance(latest_version, str) or not isinstance(latest_build, str):
            return False, f"Версии должны быть строками: version={type(latest_version)}, build={type(latest_build)}"
        
        # Проверяем совпадение version и build
        if latest_version != latest_build:
            return False, f"Версии не совпадают: version={latest_version}, build={latest_build}"
        
        # Если есть appcast, проверяем совпадение
        if appcast_data:
            # Простая проверка наличия версии в appcast
            if latest_version not in appcast_data:
                return False, f"Версия {latest_version} не найдена в appcast.xml"
        
        return True, f"Версии согласованы: {latest_version}"
        
    except Exception as e:
        return False, f"Ошибка проверки версий: {e}"


def main():
    """Основная функция"""
    parser = argparse.ArgumentParser(
        description="Проверка health/status/портов для gRPC сервера"
    )
    parser.add_argument(
        "host",
        nargs="?",
        default="nexy-prod-sergiy.canadacentral.cloudapp.azure.com",
        help="Хост сервера (по умолчанию: nexy-prod-sergiy.canadacentral.cloudapp.azure.com)"
    )
    parser.add_argument(
        "port",
        nargs="?",
        type=int,
        default=443,
        help="Порт сервера (по умолчанию: 443)"
    )
    
    args = parser.parse_args()
    
    # Определяем протокол
    protocol = "https" if args.port == 443 else "http"
    base_url = f"{protocol}://{args.host}:{args.port}"
    
    print("=" * 60)
    print("gRPC Health/Status/Port Check - PR-3")
    print("=" * 60)
    print(f"Хост: {args.host}")
    print(f"Порт: {args.port}")
    print(f"URL: {base_url}")
    print("=" * 60)
    print()
    
    errors = 0
    
    # 1. Проверка /health
    print("1. Проверка /health endpoint...")
    health_url = urljoin(base_url, "/health")
    success, health_data = check_http_endpoint(health_url, 200)
    
    if success:
        print(f"   {GREEN}✓{NC} Health endpoint доступен: HTTP 200")
        if isinstance(health_data, dict) and "latest_version" in health_data:
            print(f"   {GREEN}✓{NC} Health содержит версии")
    else:
        print(f"   {RED}✗{NC} Health endpoint недоступен: {health_data}")
        errors += 1
    
    print()
    
    # 2. Проверка /status
    print("2. Проверка /status endpoint...")
    status_url = urljoin(base_url, "/status")
    success, status_data = check_http_endpoint(status_url, 200)
    
    if success:
        print(f"   {GREEN}✓{NC} Status endpoint доступен: HTTP 200")
        if isinstance(status_data, dict):
            print(f"   {GREEN}✓{NC} Status возвращает JSON")
    else:
        print(f"   {RED}✗{NC} Status endpoint недоступен: {status_data}")
        errors += 1
    
    print()
    
    # 3. Проверка порта gRPC (50051)
    print("3. Проверка порта gRPC (50051)...")
    if check_port(args.host, 50051):
        print(f"   {GREEN}✓{NC} Порт 50051 доступен")
    else:
        print(f"   {YELLOW}⚠{NC} Порт 50051 недоступен (может быть нормально, если используется Nginx reverse proxy)")
    
    print()
    
    # 4. Проверка версий (если есть health data)
    if isinstance(health_data, dict) and "latest_version" in health_data:
        print("4. Проверка согласованности версий...")
        success, message = check_versions_match(health_data)
        
        if success:
            print(f"   {GREEN}✓{NC} {message}")
        else:
            print(f"   {RED}✗{NC} {message}")
            errors += 1
        
        print()
    
    # 5. Проверка /updates/health (если доступен)
    print("5. Проверка /updates/health endpoint...")
    updates_health_url = urljoin(base_url, "/updates/health")
    success, updates_health_data = check_http_endpoint(updates_health_url, 200)
    
    if success:
        print(f"   {GREEN}✓{NC} Updates health endpoint доступен: HTTP 200")
    else:
        print(f"   {YELLOW}⚠{NC} Updates health endpoint недоступен (может быть нормально)")
    
    print()
    
    # Итоговый результат
    print("=" * 60)
    if errors == 0:
        print(f"{GREEN}✅ Все проверки пройдены успешно!{NC}")
        sys.exit(0)
    else:
        print(f"{RED}❌ Обнаружено {errors} ошибок{NC}")
        sys.exit(1)


if __name__ == "__main__":
    main()

