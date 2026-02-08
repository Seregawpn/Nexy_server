#!/usr/bin/env python3
"""
Полный тест gRPC запроса с получением ответа
"""
import asyncio
import grpc
from grpc import aio
import sys
import os
import subprocess
import uuid

# Добавляем путь к protobuf файлам
sys.path.append(os.path.join(os.path.dirname(__file__), '../modules/grpc_service'))
try:
    import streaming_pb2
    import streaming_pb2_grpc
except ImportError as e:
    print(f"❌ Ошибка импорта protobuf: {e}")
    sys.exit(1)

def get_server_certificate(host: str, port: int) -> bytes:
    """Получение сертификата сервера"""
    try:
        result = subprocess.run(
            ['openssl', 's_client', '-connect', f'{host}:{port}', '-showcerts'],
            input=b'', capture_output=True, timeout=5
        )
        if result.returncode == 0:
            cert_start = result.stdout.find(b'-----BEGIN CERTIFICATE-----')
            cert_end = result.stdout.find(b'-----END CERTIFICATE-----', cert_start)
            if cert_start != -1 and cert_end != -1:
                return result.stdout[cert_start:cert_end + len(b'-----END CERTIFICATE-----')]
    except Exception as e:
        print(f"⚠️  Ошибка получения сертификата: {e}")
    return None

async def test_full_request(host: str = "nexy-server.canadacentral.cloudapp.azure.com", port: int = 443):
    """Полный тест gRPC запроса"""
    address = f"{host}:{port}"
    print("=" * 70)
    print("🔍 ПОЛНЫЙ ТЕСТ gRPC ЗАПРОСА")
    print("=" * 70)
    print()
    
    try:
        # Создаём secure_channel для порта 443
        print(f"🔒 Создание secure_channel к {address}...")
        cert_pem = get_server_certificate(host, port)
        
        if cert_pem:
            credentials = grpc.ssl_channel_credentials(root_certificates=cert_pem)
            print("✅ Сертификат сервера получен")
        else:
            credentials = grpc.ssl_channel_credentials()
            print("⚠️  Используются стандартные credentials")
        
        channel = aio.secure_channel(address, credentials)
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)
        
        # Проверяем готовность канала
        try:
            await asyncio.wait_for(channel.channel_ready(), timeout=10.0)
            print("✅ Канал готов к использованию")
        except asyncio.TimeoutError:
            print("⚠️  Таймаут готовности канала (продолжаем...)")
        
        # Создаём запрос
        print()
        print("📤 Отправка запроса...")
        session_id = str(uuid.uuid4())
        request = streaming_pb2.StreamRequest(
            prompt="Привет! Это тестовый запрос. Расскажи, как дела?",
            hardware_id="test-device-full-12345",
            session_id=session_id
        )
        print(f"   Session ID: {session_id}")
        print(f"   Hardware ID: {request.hardware_id}")
        print(f"   Prompt: {request.prompt}")
        print()
        
        # Получаем ответы
        print("📥 Ожидание ответов от сервера...")
        print("-" * 70)
        
        text_chunks = []
        audio_chunks = []
        end_message = None
        error_message = None
        
        try:
            async for response in stub.StreamAudio(request, timeout=60.0):
                if response.HasField('text_chunk'):
                    text = response.text_chunk
                    text_chunks.append(text)
                    print(f"📝 Text chunk: {text[:100]}...")
                
                elif response.HasField('audio_chunk'):
                    audio_data = response.audio_chunk.audio_data
                    audio_chunks.append(audio_data)
                    print(f"🔊 Audio chunk: {len(audio_data)} байт")
                
                elif response.HasField('end_message'):
                    end_message = response.end_message
                    print(f"✅ End message: {end_message}")
                    break
                
                elif response.HasField('error_message'):
                    error_message = response.error_message
                    print(f"❌ Error message: {error_message}")
                    break
            
            print("-" * 70)
            print()
            print("📊 РЕЗУЛЬТАТЫ:")
            print(f"   Text chunks: {len(text_chunks)}")
            if text_chunks:
                full_text = "".join(text_chunks)
                print(f"   Полный текст ({len(full_text)} символов): {full_text[:200]}...")
            print(f"   Audio chunks: {len(audio_chunks)}")
            if audio_chunks:
                total_audio = sum(len(chunk) for chunk in audio_chunks)
                print(f"   Общий размер аудио: {total_audio} байт")
            if end_message:
                print(f"   ✅ Завершено: {end_message}")
            if error_message:
                print(f"   ❌ Ошибка: {error_message}")
            
            # Итоговая оценка
            print()
            if error_message:
                print("❌ ТЕСТ НЕ ПРОЙДЕН: получена ошибка от сервера")
                return False
            elif len(text_chunks) > 0 or len(audio_chunks) > 0:
                print("✅ ТЕСТ ПРОЙДЕН: получены данные от сервера")
                return True
            else:
                print("⚠️  ТЕСТ ЧАСТИЧНО ПРОЙДЕН: ответ получен, но данных нет")
                return True
        
        except grpc.RpcError as e:
            print(f"❌ gRPC ошибка: {e.code()} - {e.details()}")
            return False
        
        finally:
            await channel.close()
            print("✅ Канал закрыт")
    
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "nexy-server.canadacentral.cloudapp.azure.com"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 443
    
    success = asyncio.run(test_full_request(host, port))
    sys.exit(0 if success else 1)
