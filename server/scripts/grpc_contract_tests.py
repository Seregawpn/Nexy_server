#!/usr/bin/env python3
"""
gRPC Contract Tests - PR-6
Автоматические тесты на основе контракт-таблиц из GRPC_PROTOCOL_AUDIT.md

Проверяет 8-12 сценариев из контракт-таблиц:
- Валидные/невалидные входы
- Таймауты
- Обрывы соединения
- Коды ошибок
"""

import sys
import os
import asyncio
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum

# Добавляем путь к модулям
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import grpc
    from grpc import aio
    
    # Импорт protobuf файлов
    sys.path.insert(0, str(project_root / "modules" / "grpc_service"))
    import streaming_pb2
    import streaming_pb2_grpc
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print("Убедитесь, что установлены зависимости: pip install grpcio grpcio-tools")
    sys.exit(1)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TestResult(Enum):
    """Результат теста"""
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"


@dataclass
class ContractTest:
    """Контракт-тест"""
    name: str
    method: str
    input_data: Dict[str, Any]
    expected_output: Optional[Dict[str, Any]] = None
    expected_error_code: Optional[str] = None
    expected_latency_ms: Optional[float] = None
    should_fail: bool = False
    description: str = ""


class GrpcContractTester:
    """Тестер контракт-таблиц"""
    
    def __init__(self, host: str, port: int):
        """
        Инициализация тестера
        
        Args:
            host: Хост сервера
            port: Порт сервера
        """
        self.host = host
        self.port = port
        self.channel = None
        self.stub = None
        
        # Результаты тестов
        self.results: List[tuple[ContractTest, TestResult, str]] = []
    
    async def connect(self) -> bool:
        """Подключение к серверу"""
        try:
            address = f"{self.host}:{self.port}"
            
            if self.port == 443:
                credentials = grpc.ssl_channel_credentials()
                self.channel = aio.secure_channel(address, credentials)
            else:
                self.channel = aio.insecure_channel(address)
            
            self.stub = streaming_pb2_grpc.StreamingServiceStub(self.channel)
            
            await asyncio.wait_for(self.channel.channel_ready(), timeout=5.0)
            return True
        except Exception as e:
            logger.error(f"Ошибка подключения: {e}")
            return False
    
    def get_contract_tests(self) -> List[ContractTest]:
        """
        Получение списка контракт-тестов из таблиц
        
        Returns:
            Список контракт-тестов
        """
        tests = []
        
        # Тесты для StreamAudio (из контракт-таблицы)
        tests.append(ContractTest(
            name="StreamAudio - valid request",
            method="StreamAudio",
            input_data={
                "prompt": "test",
                "hardware_id": "test_hardware_id"
            },
            expected_output={"type": "streaming", "has_text": True, "has_audio": True},
            expected_latency_ms=600.0,  # p95 ≤ 600ms
            description="Успешный сценарий StreamAudio"
        ))
        
        tests.append(ContractTest(
            name="StreamAudio - empty prompt",
            method="StreamAudio",
            input_data={
                "prompt": "",
                "hardware_id": "test_hardware_id"
            },
            expected_error_code="INVALID_ARGUMENT",
            expected_latency_ms=100.0,  # < 100ms
            should_fail=True,
            description="Валидация: пустой prompt"
        ))
        
        tests.append(ContractTest(
            name="StreamAudio - empty hardware_id",
            method="StreamAudio",
            input_data={
                "prompt": "test",
                "hardware_id": ""
            },
            expected_error_code="INVALID_ARGUMENT",
            expected_latency_ms=100.0,  # < 100ms
            should_fail=True,
            description="Валидация: пустой hardware_id"
        ))
        
        tests.append(ContractTest(
            name="StreamAudio - with screenshot",
            method="StreamAudio",
            input_data={
                "prompt": "test",
                "hardware_id": "test_hardware_id",
                "screenshot": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="  # 1x1 PNG
            },
            expected_output={"type": "streaming", "has_text": True},
            expected_latency_ms=800.0,  # p95 ≤ 800ms
            description="StreamAudio с изображением"
        ))
        
        # Тесты для InterruptSession (из контракт-таблицы)
        tests.append(ContractTest(
            name="InterruptSession - valid request",
            method="InterruptSession",
            input_data={
                "hardware_id": "test_hardware_id"
            },
            expected_output={"success": True},
            expected_latency_ms=100.0,  # < 100ms
            description="Успешное прерывание сессии"
        ))
        
        tests.append(ContractTest(
            name="InterruptSession - empty hardware_id",
            method="InterruptSession",
            input_data={
                "hardware_id": ""
            },
            expected_error_code="INVALID_ARGUMENT",
            expected_latency_ms=50.0,  # < 50ms
            should_fail=True,
            description="Валидация: пустой hardware_id"
        ))
        
        tests.append(ContractTest(
            name="InterruptSession - invalid hardware_id",
            method="InterruptSession",
            input_data={
                "hardware_id": "invalid_hardware_id"
            },
            expected_output={"success": False, "message": "No active sessions found"},
            expected_latency_ms=100.0,  # < 100ms
            description="Нет активных сессий"
        ))
        
        # Тесты на таймауты (добавляем длительный запрос)
        tests.append(ContractTest(
            name="StreamAudio - timeout",
            method="StreamAudio",
            input_data={
                "prompt": "test",
                "hardware_id": "test_hardware_id"
            },
            expected_error_code="DEADLINE_EXCEEDED",
            expected_latency_ms=10000.0,  # Таймаут 10s
            should_fail=True,
            description="Таймаут запроса (10 секунд)"
        ))
        
        return tests
    
    async def run_test(self, test: ContractTest) -> tuple[TestResult, str]:
        """
        Запуск одного контракт-теста
        
        Args:
            test: Контракт-тест
        
        Returns:
            (результат, сообщение)
        """
        try:
            start_time = asyncio.get_event_loop().time()
            
            if test.method == "StreamAudio":
                # Создаем запрос
                request = streaming_pb2.StreamRequest(
                    prompt=test.input_data.get("prompt", ""),
                    hardware_id=test.input_data.get("hardware_id", ""),
                    screenshot=test.input_data.get("screenshot") or None
                )
                
                # Вызываем RPC с таймаутом
                timeout = 10.0 if test.name == "StreamAudio - timeout" else 5.0
                
                try:
                    response_count = 0
                    has_text = False
                    has_audio = False
                    
                    async for response in self.stub.StreamAudio(request, timeout=timeout):
                        response_count += 1
                        content_type = response.WhichOneof("content")
                        
                        if content_type == "text_chunk":
                            has_text = True
                        elif content_type == "audio_chunk":
                            has_audio = True
                        elif content_type == "error_message":
                            # Проверяем код ошибки
                            if test.expected_error_code:
                                return (TestResult.PASS, f"Получена ожидаемая ошибка: {response.error_message}")
                            else:
                                return (TestResult.FAIL, f"Неожиданная ошибка: {response.error_message}")
                        
                        # Ограничиваем количество ответов для smoke-теста
                        if response_count >= 3:
                            break
                    
                    duration_ms = (asyncio.get_event_loop().time() - start_time) * 1000
                    
                    # Проверяем ожидаемый результат
                    if test.expected_output:
                        if test.expected_output.get("has_text") and not has_text:
                            return (TestResult.FAIL, "Ожидался text_chunk, но не получен")
                        if test.expected_output.get("has_audio") and not has_audio:
                            return (TestResult.FAIL, "Ожидался audio_chunk, но не получен")
                    
                    # Проверяем latency
                    if test.expected_latency_ms and duration_ms > test.expected_latency_ms:
                        return (TestResult.FAIL, f"Latency превышена: {duration_ms}ms > {test.expected_latency_ms}ms")
                    
                    if test.should_fail:
                        return (TestResult.FAIL, "Тест должен был провалиться, но прошёл")
                    
                    return (TestResult.PASS, f"Тест пройден (duration: {duration_ms:.2f}ms)")
                    
                except grpc.RpcError as e:
                    duration_ms = (asyncio.get_event_loop().time() - start_time) * 1000
                    error_code = e.code().name if hasattr(e.code(), 'name') else str(e.code())
                    
                    if test.expected_error_code and error_code == test.expected_error_code:
                        return (TestResult.PASS, f"Получена ожидаемая ошибка: {error_code}")
                    elif test.should_fail:
                        return (TestResult.PASS, f"Ожидаемая ошибка получена: {error_code}")
                    else:
                        return (TestResult.FAIL, f"Неожиданная ошибка: {error_code} - {e.details()}")
            
            elif test.method == "InterruptSession":
                # Создаем запрос
                request = streaming_pb2.InterruptRequest(
                    hardware_id=test.input_data.get("hardware_id", "")
                )
                
                try:
                    response = await self.stub.InterruptSession(request, timeout=5.0)
                    duration_ms = (asyncio.get_event_loop().time() - start_time) * 1000
                    
                    # Проверяем ожидаемый результат
                    if test.expected_output:
                        if test.expected_output.get("success") is not None:
                            if response.success != test.expected_output["success"]:
                                return (TestResult.FAIL, f"Успешность не совпадает: ожидалось {test.expected_output['success']}, получено {response.success}")
                    
                    # Проверяем latency
                    if test.expected_latency_ms and duration_ms > test.expected_latency_ms:
                        return (TestResult.FAIL, f"Latency превышена: {duration_ms}ms > {test.expected_latency_ms}ms")
                    
                    if test.should_fail:
                        return (TestResult.FAIL, "Тест должен был провалиться, но прошёл")
                    
                    return (TestResult.PASS, f"Тест пройден (duration: {duration_ms:.2f}ms, success: {response.success})")
                    
                except grpc.RpcError as e:
                    duration_ms = (asyncio.get_event_loop().time() - start_time) * 1000
                    error_code = e.code().name if hasattr(e.code(), 'name') else str(e.code())
                    
                    if test.expected_error_code and error_code == test.expected_error_code:
                        return (TestResult.PASS, f"Получена ожидаемая ошибка: {error_code}")
                    elif test.should_fail:
                        return (TestResult.PASS, f"Ожидаемая ошибка получена: {error_code}")
                    else:
                        return (TestResult.FAIL, f"Неожиданная ошибка: {error_code} - {e.details()}")
            
            return (TestResult.SKIP, "Тест не реализован")
            
        except Exception as e:
            return (TestResult.FAIL, f"Критическая ошибка: {e}")
    
    async def run_all_tests(self) -> bool:
        """
        Запуск всех контракт-тестов
        
        Returns:
            True если все тесты прошли, False иначе
        """
        if not await self.connect():
            return False
        
        tests = self.get_contract_tests()
        
        print(f"🧪 Запуск {len(tests)} контракт-тестов...")
        print()
        
        passed = 0
        failed = 0
        skipped = 0
        
        for test in tests:
            result, message = await self.run_test(test)
            self.results.append((test, result, message))
            
            status = "✅" if result == TestResult.PASS else "❌" if result == TestResult.FAIL else "⏭️"
            print(f"{status} {test.name}: {message}")
            
            if result == TestResult.PASS:
                passed += 1
            elif result == TestResult.FAIL:
                failed += 1
            else:
                skipped += 1
        
        # Закрываем канал
        if self.channel:
            await self.channel.close()
        
        print()
        print("=" * 60)
        print(f"Результаты: {passed} пройдено, {failed} провалено, {skipped} пропущено")
        print("=" * 60)
        
        return failed == 0


async def main():
    """Основная функция"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="gRPC Contract Tests - проверка контракт-таблиц"
    )
    parser.add_argument(
        "host",
        nargs="?",
        default="nexy-server.canadacentral.cloudapp.azure.com",
        help="Хост сервера (по умолчанию: nexy-server.canadacentral.cloudapp.azure.com)"
    )
    parser.add_argument(
        "port",
        nargs="?",
        type=int,
        default=50051,
        help="Порт сервера (по умолчанию: 50051)"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("gRPC Contract Tests - PR-6")
    print("=" * 60)
    print(f"Хост: {args.host}")
    print(f"Порт: {args.port}")
    print("=" * 60)
    print()
    
    tester = GrpcContractTester(args.host, args.port)
    success = await tester.run_all_tests()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️ Прервано пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

