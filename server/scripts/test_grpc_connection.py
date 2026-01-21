#!/usr/bin/env python3
"""
Тестовый скрипт для проверки gRPC подключения к удалённому серверу
"""
import asyncio
import grpc
from grpc import aio
import sys
import os

# Добавляем путь к protobuf файлам
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/grpc_service'))
try:
    import streaming_pb2
    import streaming_pb2_grpc
except ImportError as e:
    print(f"❌ Ошибка импорта protobuf: {e}")
    print("Убедитесь, что protobuf файлы сгенерированы:")
    print("  cd server/modules/grpc_service")
    print("  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto")
    sys.exit(1)

async def test_grpc_connection(host: str = "20.63.24.187", port: int = 443):
    """Тестирование gRPC подключения"""
    address = f"{host}:{port}"
    print(f"🔍 Тестирование gRPC подключения к {address}...")
    print()
    
    try:
        # Для порта 443 используем secure_channel с TLS
        # ВАЖНО: insecure_channel НЕ работает с TLS портом 443
        # Для self-signed сертификата нужно либо скачать сертификат,
        # либо использовать экспериментальный API
        if port == 443:
            # Пробуем скачать сертификат сервера для использования в credentials
            import subprocess
            import tempfile
            import ssl
            
            try:
                # Скачиваем сертификат сервера
                cert_pem = None
                try:
                    result = subprocess.run(
                        ['openssl', 's_client', '-connect', address, '-showcerts'],
                        input=b'', capture_output=True, timeout=5, check=False
                    )
                    if result.returncode == 0:
                        # Извлекаем сертификат из вывода
                        cert_start = result.stdout.find(b'-----BEGIN CERTIFICATE-----')
                        if cert_start != -1:
                            cert_end = result.stdout.find(b'-----END CERTIFICATE-----', cert_start)
                            if cert_end != -1:
                                cert_pem = result.stdout[cert_start:cert_end + len(b'-----END CERTIFICATE-----')]
                except Exception:
                    pass
                
                if cert_pem:
                    # Используем скачанный сертификат
                    credentials = grpc.ssl_channel_credentials(root_certificates=cert_pem)
                    print("🔒 Используется secure_channel с сертификатом сервера")
                else:
                    # Fallback: используем стандартные credentials
                    # В production это должно работать с правильным сертификатом
                    credentials = grpc.ssl_channel_credentials()
                    print("🔒 Используется secure_channel (стандартные credentials)")
                    print("⚠️  Для self-signed может потребоваться скачать сертификат")
                
                channel = aio.secure_channel(address, credentials)
            except Exception as e:
                print(f"⚠️  Ошибка создания secure_channel: {e}")
                print("   Пробуем insecure_channel (может не работать с TLS портом)...")
                channel = aio.insecure_channel(address)
        else:
            # Для локального тестирования используем insecure channel
            channel = aio.insecure_channel(address)
            print("🔓 Используется insecure_channel (локальное тестирование)")
        
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)
        
        print("✅ Канал создан")
        
        # Проверяем подключение
        try:
            await asyncio.wait_for(channel.channel_ready(), timeout=10.0)
            print("✅ Канал готов к использованию")
        except asyncio.TimeoutError:
            print("⚠️ Таймаут ожидания готовности канала (10 сек)")
        except Exception as e:
            print(f"⚠️ Ошибка готовности канала: {e}")
        
        # Пробуем отправить простой запрос
        print()
        print("📤 Отправка тестового запроса...")
        import uuid
        session_id = str(uuid.uuid4())
        request = streaming_pb2.StreamRequest(
            prompt="Привет, как дела? Это тестовый запрос для проверки работы gRPC.",
            hardware_id="test-hardware-id-12345",
            session_id=session_id
        )
        print(f"   Session ID: {session_id}")
        print(f"   Prompt: {request.prompt[:50]}...")
        
        try:
            # Пробуем получить хотя бы один ответ
            response_count = 0
            async for response in stub.StreamAudio(request, timeout=30.0):
                response_count += 1
                if response.HasField('text_chunk'):
                    print(f"✅ Получен text_chunk: {response.text_chunk[:50]}...")
                elif response.HasField('audio_chunk'):
                    print(f"✅ Получен audio_chunk: {len(response.audio_chunk.audio_data)} байт")
                elif response.HasField('end_message'):
                    print(f"✅ Получен end_message: {response.end_message}")
                    break
                elif response.HasField('error_message'):
                    print(f"⚠️  Получена ошибка от сервера: {response.error_message}")
                    # Это нормально - запрос дошёл до сервера, значит gRPC работает!
                    if "session_id" in response.error_message.lower():
                        print("   (Это ожидаемо - сервер требует session_id)")
                    break
                
                # Ограничиваем количество ответов для теста
                if response_count >= 5:
                    print("⚠️ Получено 5 ответов, прерываем тест")
                    break
            
            if response_count == 0:
                print("❌ Не получено ни одного ответа от сервера")
                print("   Возможные причины:")
                print("   - Сервер не обрабатывает запросы")
                print("   - Nginx не проксирует gRPC правильно")
                print("   - gRPC сервер не запущен на порту 50051")
            else:
                print(f"✅ Успешно получено {response_count} ответов")
        
        except grpc.RpcError as e:
            print(f"❌ gRPC ошибка: {e.code()} - {e.details()}")
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print("   Сервер недоступен. Проверьте:")
                print("   - Запущен ли gRPC сервер")
                print("   - Правильно ли настроен Nginx")
                print("   - Доступен ли порт 443")
            elif e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
                print("   Таймаут. Сервер не отвечает.")
            elif e.code() == grpc.StatusCode.UNIMPLEMENTED:
                print("   Метод не реализован. Проверьте версию protobuf.")
        
        finally:
            await channel.close()
            print("✅ Канал закрыт")
    
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "20.63.24.187"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 443
    
    print("=" * 70)
    print("🔍 ТЕСТИРОВАНИЕ gRPC ПОДКЛЮЧЕНИЯ")
    print("=" * 70)
    print()
    
    asyncio.run(test_grpc_connection(host, port))
