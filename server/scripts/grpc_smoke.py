#!/usr/bin/env python3
"""
gRPC Smoke Test - PR-3
Проверка базовой совместимости gRPC сервера и валидации идентификаторов

Использование:
    python scripts/grpc_smoke.py [HOST] [PORT]
    
Примеры:
    # Production сервер
    python scripts/grpc_smoke.py nexy-server.canadacentral.cloudapp.azure.com 443
    
    # Локальный сервер
    python scripts/grpc_smoke.py localhost 50051

Тесты:
    - InterruptSession: базовый тест прерывания сессии
    - StreamAudio: тест с валидными session_id и hardware_id
    - StreamAudio (missing session_id): проверка валидации отсутствующего session_id
    - StreamAudio (invalid hardware_id): проверка валидации hardware_id="unknown"
"""

import sys
import os
import asyncio
import logging
from pathlib import Path
from typing import Optional

# Добавляем путь к модулям
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import grpc
    from grpc import aio
    import subprocess
    
    # Импорт protobuf файлов
    sys.path.insert(0, str(project_root / "modules" / "grpc_service"))
    import streaming_pb2
    import streaming_pb2_grpc
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print("Убедитесь, что установлены зависимости: pip install grpcio grpcio-tools")
    sys.exit(1)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class GrpcSmokeTest:
    """Smoke-тест для gRPC сервера"""
    
    def __init__(self, host: str, port: int):
        """
        Инициализация smoke-теста
        
        Args:
            host: Хост сервера
            port: Порт сервера
        """
        self.host = host
        self.port = port
        self.channel = None
        self.stub = None
        
    async def connect(self) -> bool:
        """
        Подключение к серверу
        
        Returns:
            True если подключение успешно, False иначе
        """
        try:
            # Формируем адрес
            address = f"{self.host}:{self.port}"
            
            # Для HTTPS (порт 443) используем secure_channel с TLS
            # ВАЖНО: insecure_channel НЕ работает с TLS портом 443
            if self.port == 443:
                # Для self-signed сертификата скачиваем сертификат сервера
                import subprocess
                try:
                    result = subprocess.run(
                        ['openssl', 's_client', '-connect', address, '-showcerts'],
                        input=b'', capture_output=True, timeout=5
                    )
                    cert_start = result.stdout.find(b'-----BEGIN CERTIFICATE-----')
                    cert_end = result.stdout.find(b'-----END CERTIFICATE-----', cert_start)
                    if cert_start != -1 and cert_end != -1:
                        cert_pem = result.stdout[cert_start:cert_end + len(b'-----END CERTIFICATE-----')]
                        credentials = grpc.ssl_channel_credentials(root_certificates=cert_pem)
                        self.channel = aio.secure_channel(address, credentials)
                        logger.info("✅ Используется secure_channel с сертификатом сервера")
                    else:
                        credentials = grpc.ssl_channel_credentials()
                        self.channel = aio.secure_channel(address, credentials)
                        logger.warning("⚠️ Используется secure_channel без сертификата (может не работать)")
                except Exception as e:
                    logger.error(f"Ошибка получения сертификата: {e}, используем стандартные credentials")
                    credentials = grpc.ssl_channel_credentials()
                    self.channel = aio.secure_channel(address, credentials)
            else:
                # Для локального тестирования используем insecure channel
                self.channel = aio.insecure_channel(address)
            
            # Создаем stub
            self.stub = streaming_pb2_grpc.StreamingServiceStub(self.channel)
            
            # Проверяем подключение (попытка получить метаданные)
            try:
                await asyncio.wait_for(
                    self.channel.channel_ready(),
                    timeout=5.0
                )
                logger.info(f"✅ Подключение к {address} установлено")
                return True
            except asyncio.TimeoutError:
                logger.error(f"❌ Таймаут подключения к {address}")
                return False
            except Exception as e:
                logger.error(f"❌ Ошибка подключения к {address}: {e}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка создания канала: {e}")
            return False
    
    async def test_interrupt_session(self) -> bool:
        """
        Тест RPC метода InterruptSession
        
        Returns:
            True если тест прошёл успешно, False иначе
        """
        try:
            logger.info("🧪 Тестирование InterruptSession...")
            
            # Создаем запрос
            request = streaming_pb2.InterruptRequest(
                hardware_id="smoke_test_hardware_id_interrupt"
            )
            
            # Вызываем RPC
            response = await self.stub.InterruptSession(
                request,
                timeout=5.0
            )
            
            # Проверяем ответ
            if response is not None:
                logger.info(f"✅ InterruptSession успешен: success={response.success}")
                return True
            else:
                logger.error("❌ InterruptSession вернул None")
                return False
                
        except grpc.RpcError as e:
            logger.error(f"❌ gRPC ошибка в InterruptSession: {e.code()} - {e.details()}")
            return False
        except Exception as e:
            logger.error(f"❌ Ошибка в InterruptSession: {e}")
            return False
    
    async def test_stream_audio(self) -> bool:
        """
        Тест RPC метода StreamAudio (базовый вызов с валидными идентификаторами)
        
        Returns:
            True если тест прошёл успешно, False иначе
        """
        try:
            logger.info("🧪 Тестирование StreamAudio с валидными идентификаторами...")
            
            # Создаем запрос с валидными session_id и hardware_id
            import uuid
            request = streaming_pb2.StreamRequest(
                prompt="test",
                hardware_id="smoke_test_hardware_id",
                session_id=str(uuid.uuid4())
            )
            
            # Вызываем RPC (streaming)
            response_count = 0
            async for response in self.stub.StreamAudio(request, timeout=10.0):
                response_count += 1
                
                # Проверяем, что ответ валиден
                if response.WhichOneof("content") is None:
                    logger.warning("⚠️ Получен ответ без content")
                else:
                    content_type = response.WhichOneof("content")
                    logger.info(f"   → Получен ответ: {content_type}")
                    if content_type == "error_message":
                        logger.error(f"   → Сообщение об ошибке: {response.error_message}")
                
                # Ограничиваем количество ответов для smoke-теста
                if response_count >= 3:
                    break
            
            if response_count > 0:
                logger.info(f"✅ StreamAudio успешен: получено {response_count} ответов")
                return True
            else:
                logger.error("❌ StreamAudio не вернул ответов")
                return False
                
        except grpc.RpcError as e:
            logger.error(f"❌ gRPC ошибка в StreamAudio: {e.code()} - {e.details()}")
            return False
        except Exception as e:
            logger.error(f"❌ Ошибка в StreamAudio: {e}")
            return False
    
    async def test_stream_audio_missing_session_id(self) -> bool:
        """
        Тест валидации: запрос без session_id должен вернуть INVALID_ARGUMENT
        
        Returns:
            True если тест прошёл (ошибка получена корректно), False иначе
        """
        try:
            logger.info("🧪 Тестирование валидации: запрос без session_id...")
            
            # Создаем запрос БЕЗ session_id
            request = streaming_pb2.StreamRequest(
                prompt="test",
                hardware_id="smoke_test_hardware_id"
                # session_id отсутствует
            )
            
            # Вызываем RPC (streaming)
            error_received = False
            error_message = None
            async for response in self.stub.StreamAudio(request, timeout=10.0):
                content_type = response.WhichOneof("content")
                if content_type == "error_message":
                    error_received = True
                    error_message = response.error_message
                    logger.info(f"   → Получена ошибка: {error_message}")
                    break
            
            if error_received and "session_id is required" in error_message.lower():
                logger.info("✅ Валидация session_id работает: получена ожидаемая ошибка")
                return True
            else:
                logger.error(f"❌ Валидация session_id не работает: получено {error_message}")
                return False
                
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                logger.info(f"✅ Валидация session_id работает: получен INVALID_ARGUMENT - {e.details()}")
                return True
            else:
                logger.error(f"❌ Неожиданная ошибка: {e.code()} - {e.details()}")
                return False
        except Exception as e:
            logger.error(f"❌ Ошибка в тесте валидации session_id: {e}")
            return False
    
    async def test_stream_audio_invalid_hardware_id(self) -> bool:
        """
        Тест валидации: запрос с hardware_id="unknown" должен вернуть ошибку
        
        Returns:
            True если тест прошёл (ошибка получена корректно), False иначе
        """
        try:
            logger.info("🧪 Тестирование валидации: запрос с hardware_id='unknown'...")
            
            # Создаем запрос с невалидным hardware_id
            import uuid
            request = streaming_pb2.StreamRequest(
                prompt="test",
                hardware_id="unknown",
                session_id=str(uuid.uuid4())
            )
            
            # Вызываем RPC (streaming)
            error_received = False
            error_message = None
            async for response in self.stub.StreamAudio(request, timeout=10.0):
                content_type = response.WhichOneof("content")
                if content_type == "error_message":
                    error_received = True
                    error_message = response.error_message
                    logger.info(f"   → Получена ошибка: {error_message}")
                    break
            
            if error_received and ("hardware_id" in error_message.lower() or "unknown" in error_message.lower()):
                logger.info("✅ Валидация hardware_id работает: получена ожидаемая ошибка")
                return True
            else:
                logger.error(f"❌ Валидация hardware_id не работает: получено {error_message}")
                return False
                
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                logger.info(f"✅ Валидация hardware_id работает: получен INVALID_ARGUMENT - {e.details()}")
                return True
            else:
                logger.error(f"❌ Неожиданная ошибка: {e.code()} - {e.details()}")
                return False
        except Exception as e:
            logger.error(f"❌ Ошибка в тесте валидации hardware_id: {e}")
            return False
    
    async def run_all_tests(self) -> bool:
        """
        Запуск всех тестов
        
        Returns:
            True если все тесты прошли, False иначе
        """
        results = []
        
        # Подключение
        if not await self.connect():
            return False
        
        # Тест InterruptSession
        results.append(await self.test_interrupt_session())
        
        # Тест StreamAudio с валидными идентификаторами
        results.append(await self.test_stream_audio())
        
        # Тесты валидации идентификаторов
        results.append(await self.test_stream_audio_missing_session_id())
        results.append(await self.test_stream_audio_invalid_hardware_id())
        
        # Закрываем канал
        if self.channel:
            await self.channel.close()
        
        # Итоговый результат
        all_passed = all(results)
        if all_passed:
            logger.info("✅ Все smoke-тесты прошли успешно")
        else:
            logger.error(f"❌ Некоторые тесты не прошли: {results}")
        
        return all_passed


async def main():
    """Основная функция"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="gRPC Smoke Test для проверки совместимости сервера"
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
    print("gRPC Smoke Test - PR-3")
    print("=" * 60)
    print(f"Хост: {args.host}")
    print(f"Порт: {args.port}")
    print("=" * 60)
    print()
    
    # Создаем тест
    test = GrpcSmokeTest(args.host, args.port)
    
    # Запускаем тесты
    success = await test.run_all_tests()
    
    print()
    print("=" * 60)
    if success:
        print("✅ Все тесты прошли успешно")
        sys.exit(0)
    else:
        print("❌ Некоторые тесты не прошли")
        sys.exit(1)


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

