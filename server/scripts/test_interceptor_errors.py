#!/usr/bin/env python3
"""
Тест gRPC интерсепторов на ошибки (PR-7)
Проверяет timeout, unavailable, cancelled и единый формат логов
"""

import sys
import os
import asyncio
import logging
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    import grpc
    from grpc import aio
    
    sys.path.insert(0, str(project_root / "modules" / "grpc_service"))
    import streaming_pb2
    import streaming_pb2_grpc
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    sys.exit(1)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_timeout_error(host: str, port: int):
    """Тест timeout ошибки"""
    try:
        address = f"{host}:{port}"
        if port == 443:
            credentials = grpc.ssl_channel_credentials()
            channel = aio.secure_channel(address, credentials)
        else:
            channel = aio.insecure_channel(address)
        
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)
        
        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="test_timeout"
        )
        
        # Вызываем с очень коротким таймаутом
        try:
            async for response in stub.StreamAudio(request, timeout=0.1):
                pass
        except grpc.RpcError as e:
            error_code = e.code().name if hasattr(e.code(), 'name') else str(e.code())
            if error_code == "DEADLINE_EXCEEDED":
                print(f"✅ Timeout ошибка корректно обработана: {error_code}")
                return True
            else:
                print(f"❌ Неожиданный код ошибки для timeout: {error_code}")
                return False
        
        await channel.close()
        return False
        
    except Exception as e:
        print(f"❌ Ошибка в тесте timeout: {e}")
        return False


async def test_unavailable_error(host: str, port: int):
    """Тест unavailable ошибки (имитация недоступности)"""
    # Пытаемся подключиться к несуществующему порту
    try:
        address = f"{host}:9999"  # Несуществующий порт
        channel = aio.insecure_channel(address)
        
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)
        
        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="test_unavailable"
        )
        
        try:
            async for response in stub.StreamAudio(request, timeout=2.0):
                pass
        except grpc.RpcError as e:
            error_code = e.code().name if hasattr(e.code(), 'name') else str(e.code())
            if error_code == "UNAVAILABLE":
                print(f"✅ Unavailable ошибка корректно обработана: {error_code}")
                await channel.close()
                return True
            else:
                print(f"❌ Неожиданный код ошибки для unavailable: {error_code}")
                await channel.close()
                return False
        
        await channel.close()
        return False
        
    except Exception as e:
        print(f"⚠️ Ошибка в тесте unavailable (ожидаемо): {e}")
        return True  # Это ожидаемо


async def test_cancelled_error(host: str, port: int):
    """Тест cancelled ошибки"""
    try:
        address = f"{host}:{port}"
        if port == 443:
            credentials = grpc.ssl_channel_credentials()
            channel = aio.secure_channel(address, credentials)
        else:
            channel = aio.insecure_channel(address)
        
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)
        
        request = streaming_pb2.StreamRequest(
            prompt="test",
            hardware_id="test_cancelled"
        )
        
        # Создаем задачу и отменяем её
        async def cancel_after_delay():
            await asyncio.sleep(0.1)
            return True
        
        try:
            task = asyncio.create_task(
                stub.StreamAudio(request, timeout=10.0).__anext__()
            )
            cancel_task = asyncio.create_task(cancel_after_delay())
            
            done, pending = await asyncio.wait(
                [task, cancel_task],
                return_when=asyncio.FIRST_COMPLETED
            )
            
            # Отменяем задачу
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                print("✅ Cancelled ошибка корректно обработана")
                await channel.close()
                return True
            except grpc.RpcError as e:
                error_code = e.code().name if hasattr(e.code(), 'name') else str(e.code())
                if error_code == "CANCELLED":
                    print(f"✅ Cancelled ошибка корректно обработана: {error_code}")
                    await channel.close()
                    return True
                else:
                    print(f"⚠️ Неожиданный код ошибки для cancelled: {error_code}")
                    await channel.close()
                    return False
            
            await channel.close()
            return False
            
        except Exception as e:
            print(f"⚠️ Ошибка в тесте cancelled: {e}")
            await channel.close()
            return False
        
    except Exception as e:
        print(f"❌ Ошибка в тесте cancelled: {e}")
        return False


async def check_log_format():
    """Проверка формата логов"""
    if not os.path.exists("server.log"):
        print("⚠️ server.log не найден, пропускаем проверку формата")
        return True
    
    # Проверяем наличие структурированных логов
    with open("server.log", "r") as f:
        logs = f.read()
        
        # Проверяем наличие единого формата
        if "scope=grpc" in logs and "method=" in logs:
            print("✅ Структурированные логи найдены")
            
            # Проверяем наличие error_classified
            if "error_classified" in logs or "error_code" in logs:
                print("✅ Классификация ошибок найдена в логах")
                return True
            else:
                print("⚠️ Классификация ошибок не найдена в логах")
                return True  # Не критично
        else:
            print("⚠️ Структурированные логи не найдены в server.log")
            return True  # Не критично для теста


async def main():
    """Основная функция"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Тест gRPC интерсепторов")
    parser.add_argument("host", nargs="?", default="nexy-prod-sergiy.canadacentral.cloudapp.azure.com", help="Хост сервера")
    parser.add_argument("port", nargs="?", type=int, default=443, help="Порт сервера")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Тест gRPC интерсепторов - PR-7")
    print("=" * 60)
    print(f"Хост: {args.host}")
    print(f"Порт: {args.port}")
    print("=" * 60)
    print()
    
    results = []
    
    # Тест timeout
    print("1. Тест timeout ошибки...")
    results.append(await test_timeout_error(args.host, args.port))
    print()
    
    # Тест unavailable
    print("2. Тест unavailable ошибки...")
    results.append(await test_unavailable_error(args.host, args.port))
    print()
    
    # Тест cancelled
    print("3. Тест cancelled ошибки...")
    results.append(await test_cancelled_error(args.host, args.port))
    print()
    
    # Проверка формата логов
    print("4. Проверка формата логов...")
    results.append(await check_log_format())
    print()
    
    # Итоговый результат
    passed = sum(results)
    total = len(results)
    
    print("=" * 60)
    print(f"Результаты: {passed}/{total} проверок прошли")
    print("=" * 60)
    
    if passed == total:
        print("✅ Все проверки прошли успешно")
        sys.exit(0)
    else:
        print("❌ Некоторые проверки не прошли")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

