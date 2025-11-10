#!/usr/bin/env python3
"""
Тест метода GenerateWelcomeAudio на удалённом сервере
"""
import asyncio
import sys
import os
from pathlib import Path

# Добавляем путь к модулям
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "server" / "modules" / "grpc_service"))

try:
    import grpc
    from grpc import aio
    import streaming_pb2
    import streaming_pb2_grpc
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    sys.exit(1)

async def test_generate_welcome_audio():
    """Тест метода GenerateWelcomeAudio"""
    host = "localhost"
    port = 50051
    
    print(f"🧪 Тестирование GenerateWelcomeAudio на {host}:{port}")
    print("=" * 60)
    
    # Создаём insecure channel для локального тестирования
    address = f"{host}:{port}"
    channel = aio.insecure_channel(address)
    stub = streaming_pb2_grpc.StreamingServiceStub(channel)
    
    try:
        # Ждём готовности канала
        await asyncio.wait_for(channel.channel_ready(), timeout=5.0)
        print(f"✅ Подключение к {address} установлено")
        
        # Создаём запрос
        request = streaming_pb2.WelcomeAudioRequest(
            hardware_id="test_hardware_id_123",
            message="Hello! Welcome to Nexy Assistant. How can I help you today?"
        )
        
        print(f"📨 Отправка запроса:")
        print(f"   - hardware_id: {request.hardware_id}")
        print(f"   - message: {request.message}")
        print()
        
        # Вызываем метод
        print("🔄 Вызов GenerateWelcomeAudio...")
        audio_chunks_received = 0
        total_bytes = 0
        
        async for response in stub.GenerateWelcomeAudio(request, timeout=30.0):
            if response.HasField('audio_chunk'):
                chunk = response.audio_chunk
                audio_chunks_received += 1
                total_bytes += len(chunk.audio_data)
                print(f"   ✅ Получен audio_chunk #{audio_chunks_received}: {len(chunk.audio_data)} байт")
            elif response.HasField('end_message'):
                print(f"   ✅ {response.end_message}")
            elif response.HasField('error_message'):
                print(f"   ❌ Ошибка: {response.error_message}")
                return False
        
        print()
        print("=" * 60)
        if audio_chunks_received > 0:
            print(f"✅ Тест пройден успешно!")
            print(f"   - Получено аудио чанков: {audio_chunks_received}")
            print(f"   - Всего байт: {total_bytes}")
            return True
        else:
            print(f"⚠️  Тест завершён, но аудио чанки не получены")
            return False
            
    except grpc.RpcError as e:
        print(f"❌ gRPC ошибка: {e.code()} - {e.details()}")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        await channel.close()

if __name__ == "__main__":
    result = asyncio.run(test_generate_welcome_audio())
    sys.exit(0 if result else 1)

