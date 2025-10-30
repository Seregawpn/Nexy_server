#!/usr/bin/env python3
"""
Тест реального gRPC вызова через HTTPS
"""

import sys
import os
import asyncio
from pathlib import Path

# Отключаем проверку SSL для self-signed
os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = ''

# Добавляем пути
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "modules" / "grpc_client" / "proto"))

import grpc
import grpc.aio
import streaming_pb2
import streaming_pb2_grpc

SERVER_HOST = "20.151.51.172"
GRPC_ADDRESS = f"{SERVER_HOST}:443"

print("=" * 80)
print("ТЕСТ РЕАЛЬНОГО gRPC ВЫЗОВА ЧЕРЕЗ HTTPS")
print("=" * 80)
print(f"\nEndpoint: {GRPC_ADDRESS}")
print("Protocol: HTTPS + HTTP/2")
print("Certificate: Self-signed (verification disabled)")
print()

async def test_grpc_welcome():
    try:
        # Читаем сертификат сервера (с SAN)
        with open('/tmp/server_cert_new.pem', 'rb') as f:
            root_cert = f.read()

        # SSL credentials с сертификатом сервера
        credentials = grpc.ssl_channel_credentials(
            root_certificates=root_cert,
            private_key=None,
            certificate_chain=None
        )

        # Опции для HTTPS + HTTP/2
        options = [
            # НЕ используем ssl_target_name_override когда доверяем сертификату!
            ('grpc.default_authority', SERVER_HOST),
            ('grpc.http2.true_binary', 1),
            ('grpc.max_send_message_length', 50 * 1024 * 1024),
            ('grpc.max_receive_message_length', 50 * 1024 * 1024),
            ('grpc.keepalive_time_ms', 120000),
            ('grpc.keepalive_timeout_ms', 10000),
        ]

        print("🔌 Создаём HTTPS канал...")
        channel = grpc.aio.secure_channel(
            GRPC_ADDRESS,
            credentials,
            options=options
        )

        print("📡 Создаём gRPC stub...")
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)

        print("🎤 Отправляем Welcome запрос...")

        # Создаём запрос
        request = streaming_pb2.WelcomeRequest(
            text="Привет",
            voice="alloy",
            language="ru-RU",
            session_id="test-session-123"
        )

        # Делаем вызов с таймаутом (это stream, нужно получить первый чанк)
        try:
            print("   Ожидаем ответ от сервера...")
            stream = stub.GenerateWelcomeAudio(request)

            # Получаем первый chunk
            first_chunk = await asyncio.wait_for(
                stream.read(),
                timeout=10.0
            )

            print(f"✅ SUCCESS! Получен ответ от сервера:")
            print(f"   Response: {first_chunk}")
            print(f"\n🎉 gRPC через HTTPS работает корректно!")

            # Закрываем stream
            stream.cancel()

        except asyncio.TimeoutError:
            print("❌ TIMEOUT: Сервер не ответил за 10 секунд")
            print("   Возможные причины:")
            print("   - Nginx не передаёт gRPC запросы")
            print("   - gRPC сервер не отвечает")
            print("   - Проблема с SSL/TLS handshake")
            print()

        except grpc.aio.AioRpcError as e:
            print(f"❌ gRPC ERROR: {e.code()}")
            print(f"   Details: {e.details()}")
            print(f"   Debug: {e.debug_error_string()}")
            print()

        # Закрываем канал
        await channel.close()
        print("🔒 Канал закрыт")

    except Exception as e:
        print(f"❌ EXCEPTION: {e}")
        import traceback
        traceback.print_exc()

print("Запуск теста...")
asyncio.run(test_grpc_welcome())

print("=" * 80)
print("ТЕСТ ЗАВЕРШЁН")
print("=" * 80)
