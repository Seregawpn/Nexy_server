#!/usr/bin/env python3
"""
Комплексный скрипт для запуска всех тестов серверной части

Использование:
    python server/scripts/run_all_tests.py [--level LEVEL] [--host HOST] [--port PORT]
    
Примеры:
    # Все тесты
    python server/scripts/run_all_tests.py
    
    # Только unit тесты
    python server/scripts/run_all_tests.py --level unit
    
    # Только smoke тесты
    python server/scripts/run_all_tests.py --level smoke --host nexy-prod-sergiy.canadacentral.cloudapp.azure.com --port 443
"""

import sys
import os
import subprocess
import argparse
import time
from pathlib import Path
from typing import List, Tuple, Optional
from dataclasses import dataclass

# Цвета для вывода
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color

@dataclass
class TestResult:
    """Результат выполнения теста"""
    name: str
    success: bool
    duration: float
    output: str
    error: Optional[str] = None

def print_header(text: str):
    """Печать заголовка"""
    print(f"\n{BLUE}{'='*80}{NC}")
    print(f"{BLUE}{text:^80}{NC}")
    print(f"{BLUE}{'='*80}{NC}\n")

def print_test_result(result: TestResult):
    """Печать результата теста"""
    status = f"{GREEN}✅ PASS{NC}" if result.success else f"{RED}❌ FAIL{NC}"
    print(f"{status} - {result.name} ({result.duration:.2f}s)")
    if result.error:
        print(f"   {RED}Ошибка: {result.error}{NC}")

def run_command(cmd: List[str], timeout: Optional[int] = None) -> Tuple[bool, str, str]:
    """
    Запуск команды и получение результата
    
    Returns:
        (success, stdout, stderr)
    """
    try:
        # Исправляем путь: скрипт находится в server/scripts/, нужно подняться на 2 уровня
        script_dir = Path(__file__).parent.parent.parent
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(script_dir)
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", f"Таймаут выполнения ({timeout}s)"
    except Exception as e:
        return False, "", str(e)

def run_unit_tests() -> TestResult:
    """Запуск unit тестов"""
    print(f"{YELLOW}🧪 Запуск unit тестов...{NC}")
    start_time = time.time()
    
    success, stdout, stderr = run_command(
        ["python3", "-m", "pytest", "server/tests/", "-v", "--tb=short"],
        timeout=300
    )
    
    duration = time.time() - start_time
    
    # Извлекаем количество пройденных тестов
    passed = stdout.count("PASSED")
    failed = stdout.count("FAILED")
    
    output = f"Пройдено: {passed}, Провалено: {failed}"
    if failed > 0:
        output += f"\n{stderr}"
    
    return TestResult(
        name="Unit тесты (pytest)",
        success=success and failed == 0,
        duration=duration,
        output=output,
        error=stderr if not success else None
    )

def run_smoke_test(host: str, port: int) -> TestResult:
    """Запуск smoke теста"""
    print(f"{YELLOW}🧪 Запуск gRPC smoke теста ({host}:{port})...{NC}")
    start_time = time.time()
    
    success, stdout, stderr = run_command(
        ["python3", "server/scripts/grpc_smoke.py", host, str(port)],
        timeout=60
    )
    
    duration = time.time() - start_time
    
    return TestResult(
        name=f"gRPC Smoke Test ({host}:{port})",
        success=success,
        duration=duration,
        output=stdout,
        error=stderr if not success else None
    )

def run_health_check(host: str, port: int) -> TestResult:
    """Запуск health check"""
    print(f"{YELLOW}🏥 Запуск health check ({host}:{port})...{NC}")
    start_time = time.time()
    
    success, stdout, stderr = run_command(
        ["python3", "server/scripts/check_grpc_health.py", host, str(port)],
        timeout=30
    )
    
    duration = time.time() - start_time
    
    return TestResult(
        name=f"Health/Status Check ({host}:{port})",
        success=success,
        duration=duration,
        output=stdout,
        error=stderr if not success else None
    )

def run_e2e_test() -> TestResult:
    """Запуск E2E теста"""
    print(f"{YELLOW}🔄 Запуск E2E теста...{NC}")
    start_time = time.time()
    
    success, stdout, stderr = run_command(
        ["python3", "server/scripts/test_full_pipeline_e2e.py"],
        timeout=120
    )
    
    duration = time.time() - start_time
    
    return TestResult(
        name="E2E тест (полный пайплайн)",
        success=success,
        duration=duration,
        output=stdout,
        error=stderr if not success else None
    )

def run_backpressure_test(host: str, port: int) -> TestResult:
    """Запуск backpressure теста"""
    print(f"{YELLOW}🛡️ Запуск backpressure теста ({host}:{port})...{NC}")
    start_time = time.time()
    
    success, stdout, stderr = run_command(
        ["python3", "server/scripts/test_backpressure.py", host, str(port)],
        timeout=120
    )
    
    duration = time.time() - start_time
    
    return TestResult(
        name=f"Backpressure Test ({host}:{port})",
        success=success,
        duration=duration,
        output=stdout,
        error=stderr if not success else None
    )

def run_contract_test(host: str, port: int) -> TestResult:
    """Запуск contract теста"""
    print(f"{YELLOW}📋 Запуск contract теста ({host}:{port})...{NC}")
    start_time = time.time()
    
    # Проверяем наличие файла
    contract_test = Path(__file__).parent / "grpc_contract_tests.py"
    if not contract_test.exists():
        return TestResult(
            name="Contract Test",
            success=True,
            duration=0,
            output="Пропущен (файл не найден)",
            error=None
        )
    
    success, stdout, stderr = run_command(
        ["python3", "server/scripts/grpc_contract_tests.py", host, str(port)],
        timeout=60
    )
    
    duration = time.time() - start_time
    
    return TestResult(
        name=f"Contract Test ({host}:{port})",
        success=success,
        duration=duration,
        output=stdout,
        error=stderr if not success else None
    )

def main():
    """Основная функция"""
    parser = argparse.ArgumentParser(description="Комплексное тестирование серверной части")
    parser.add_argument(
        "--level",
        choices=["unit", "smoke", "integration", "e2e", "all"],
        default="all",
        help="Уровень тестирования"
    )
    parser.add_argument(
        "--host",
        default="nexy-prod-sergiy.canadacentral.cloudapp.azure.com",
        help="Хост сервера для тестирования"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=443,
        help="Порт сервера для тестирования"
    )
    parser.add_argument(
        "--skip-unit",
        action="store_true",
        help="Пропустить unit тесты"
    )
    parser.add_argument(
        "--skip-smoke",
        action="store_true",
        help="Пропустить smoke тесты"
    )
    parser.add_argument(
        "--skip-e2e",
        action="store_true",
        help="Пропустить E2E тесты"
    )
    
    args = parser.parse_args()
    
    print_header("КОМПЛЕКСНОЕ ТЕСТИРОВАНИЕ СЕРВЕРНОЙ ЧАСТИ")
    print(f"Уровень: {args.level}")
    print(f"Сервер: {args.host}:{args.port}")
    print()
    
    results: List[TestResult] = []
    
    # Unit тесты
    if args.level in ["unit", "all"] and not args.skip_unit:
        results.append(run_unit_tests())
        print()
    
    # Smoke тесты
    if args.level in ["smoke", "all"] and not args.skip_smoke:
        results.append(run_smoke_test(args.host, args.port))
        print()
        results.append(run_health_check(args.host, args.port))
        print()
    
    # E2E тесты
    if args.level in ["e2e", "all"] and not args.skip_e2e:
        results.append(run_e2e_test())
        print()
    
    # Integration тесты (backpressure, contract)
    if args.level in ["integration", "all"]:
        results.append(run_backpressure_test(args.host, args.port))
        print()
        results.append(run_contract_test(args.host, args.port))
        print()
    
    # Итоги
    print_header("ИТОГИ ТЕСТИРОВАНИЯ")
    
    total = len(results)
    passed = sum(1 for r in results if r.success)
    failed = total - passed
    total_duration = sum(r.duration for r in results)
    
    print(f"\n📊 Статистика:")
    print(f"   Всего тестов: {total}")
    print(f"   {GREEN}✅ Пройдено: {passed}{NC}")
    if failed > 0:
        print(f"   {RED}❌ Провалено: {failed}{NC}")
    print(f"   ⏱️  Общее время: {total_duration:.2f}s")
    print()
    
    print(f"📋 Детальные результаты:")
    for result in results:
        print_test_result(result)
        if not result.success and result.error:
            print(f"   {YELLOW}Детали:{NC}")
            print(f"   {result.error[:200]}...")
    
    print()
    
    if failed == 0:
        print(f"{GREEN}✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!{NC}")
        return 0
    else:
        print(f"{RED}❌ НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ{NC}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
