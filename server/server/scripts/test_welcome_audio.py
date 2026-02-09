#!/usr/bin/env python3
"""
Тест генерации приветственного аудио через GenerateWelcomeAudio
"""
import sys
import asyncio
from pathlib import Path

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
    sys.exit(1)


async def test_generate_welcome_audio(host: str = "localhost", port: int = 50051):
    """Тест генерации приветственного аудио"""
    print("=" * 60)
    print("Тест GenerateWelcomeAudio")
    print("=" * 60)
    print(f"Подключение к {host}:{port}")
    print()
    
    # Создаем канал
    address = f"{host}:{port}"
    channel = aio.insecure_channel(address)
    
    try:
        # Создаем stub
        stub = streaming_pb2_grpc.StreamingServiceStub(channel)
        
        # Ждем готовности канала
        try:
            await asyncio.wait_for(channel.channel_ready(), timeout=5.0)
            print("✅ Подключение установлено")
        except asyncio.TimeoutError:
            print("❌ Таймаут подключения")
            return False
        
        # Создаем запрос
        request = streaming_pb2.WelcomeRequest(
            text="Hello! This is a test of audio generation. How are you today?",
            session_id="test_welcome_123"
        )
        
        print(f"📤 Отправка запроса:")
        print(f"   Text: {request.text}")
        print(f"   Session ID: {request.session_id}")
        print()
        
        # Вызываем GenerateWelcomeAudio
        print("🎵 Генерация аудио...")
        chunk_count = 0
        total_bytes = 0
        error_occurred = False
        
        try:
            async for response in stub.GenerateWelcomeAudio(request, timeout=30.0):
                # Проверяем тип контента
                if response.HasField("audio_chunk"):
                    chunk_count += 1
                    audio_data = response.audio_chunk.audio_data
                    total_bytes += len(audio_data)
                    print(f"   ✅ Chunk #{chunk_count}: {len(audio_data)} bytes "
                          f"(sample_rate={response.audio_chunk.sample_rate}, "
                          f"channels={response.audio_chunk.channels}, "
                          f"dtype={response.audio_chunk.dtype})")
                
                elif response.HasField("metadata"):
                    print(f"   📋 Metadata: {response.metadata}")
                
                elif response.HasField("end_message"):
                    print(f"   ✅ {response.end_message}")
                
                elif response.HasField("error_message"):
                    print(f"   ❌ Ошибка: {response.error_message}")
                    error_occurred = True
                    break
        
        except grpc.RpcError as e:
            print(f"   ❌ gRPC ошибка: {e.code()} - {e.details()}")
            error_occurred = True
        
        print()
        print("=" * 60)
        if error_occurred:
            print("❌ Тест не пройден: произошла ошибка")
            return False
        elif chunk_count == 0:
            print("⚠️ Тест не пройден: не получено аудио chunks")
            return False
        else:
            print(f"✅ Тест пройден успешно!")
            print(f"   Получено chunks: {chunk_count}")
            print(f"   Всего байт: {total_bytes}")
            return True
        
    finally:
        await channel.close()


async def main():
    """Основная функция"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Тест GenerateWelcomeAudio")
    parser.add_argument("--host", default="localhost", help="Хост сервера")
    parser.add_argument("--port", type=int, default=50051, help="Порт сервера")
    
    args = parser.parse_args()
    
    success = await test_generate_welcome_audio(args.host, args.port)
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
