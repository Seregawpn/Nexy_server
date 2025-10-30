#!/usr/bin/env python3
"""
Тестирование новых HTTPS эндпоинтов для gRPC и Update Server
"""

import sys
import ssl
import os
import asyncio
import urllib3
import grpc
import grpc.aio
from pathlib import Path

# Отключаем проверку SSL для gRPC (для тестирования self-signed сертификатов)
os.environ['GRPC_DEFAULT_SSL_ROOTS_FILE_PATH'] = ''

# Добавляем пути
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))

print("=" * 80)
print("ТЕСТИРОВАНИЕ HTTPS ЭНДПОИНТОВ")
print("=" * 80)

# ===== ТЕСТ 1: Update Server HTTPS =====
print("\n📦 ТЕСТ 1: Update Server HTTPS")
print("-" * 80)

SERVER_HOST = "20.151.51.172"
UPDATE_URL = f"https://{SERVER_HOST}/updates/appcast.xml"

print(f"URL: {UPDATE_URL}")
print("Попытка получить appcast.xml...")

# Отключаем предупреждения для self-signed сертификатов
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Создаём HTTP клиент без проверки сертификата
http = urllib3.PoolManager(
    cert_reqs='CERT_NONE',
    assert_hostname=False
)

try:
    response = http.request("GET", UPDATE_URL, timeout=10.0)
    print(f"✅ Статус: {response.status}")
    print(f"✅ Content-Type: {response.headers.get('Content-Type', 'N/A')}")
    print(f"✅ Content-Length: {len(response.data)} bytes")

    # Показываем первые 200 символов
    content = response.data.decode('utf-8')
    print(f"\nПервые 200 символов ответа:")
    print(content[:200])
    print()

except Exception as e:
    print(f"❌ Ошибка: {e}")
    print()

# ===== ТЕСТ 2: gRPC HTTPS =====
print("\n🔌 ТЕСТ 2: gRPC HTTPS")
print("-" * 80)

GRPC_ADDRESS = f"{SERVER_HOST}:443"
print(f"Address: {GRPC_ADDRESS}")
print(f"Path: / (gRPC на корневом пути)")
print("Попытка установить gRPC соединение...")

async def test_grpc():
    try:
        # Создаём SSL credentials БЕЗ проверки сертификата (для self-signed)
        # root_certificates=None означает "не проверять сертификат"
        credentials = grpc.ssl_channel_credentials(
            root_certificates=None,
            private_key=None,
            certificate_chain=None
        )

        # Опции для HTTPS + HTTP/2 + отключения проверки сертификата
        options = [
            ('grpc.ssl_target_name_override', SERVER_HOST),
            ('grpc.default_authority', f'{SERVER_HOST}'),
            ('grpc.http2.true_binary', 1),
            ('grpc.max_send_message_length', 50 * 1024 * 1024),
            ('grpc.max_receive_message_length', 50 * 1024 * 1024),
        ]

        # gRPC через HTTPS на корневом пути (location / в Nginx)
        channel = grpc.aio.secure_channel(
            GRPC_ADDRESS,
            credentials,
            options=options
        )

        print("Канал создан, проверяем готовность...")

        # Пытаемся дождаться готовности канала
        try:
            await asyncio.wait_for(channel.channel_ready(), timeout=10.0)
            print("✅ Канал готов к использованию!")
            print("✅ gRPC соединение установлено")
        except asyncio.TimeoutError:
            print("⏰ Таймаут при ожидании готовности канала")
            print("   Это может означать:")
            print("   - Nginx не настроен для gRPC")
            print("   - Неверный путь /grpc")
            print("   - gRPC сервер недоступен")

        # Закрываем канал
        await channel.close()

    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        import traceback
        traceback.print_exc()

# Запускаем асинхронный тест
asyncio.run(test_grpc())

print("\n" + "=" * 80)
print("ТЕСТЫ ЗАВЕРШЕНЫ")
print("=" * 80)
