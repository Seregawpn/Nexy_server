#!/usr/bin/env python3
"""
Полный E2E тест обработки запроса от клиента до сервера

Тестирует:
1. Подключение к gRPC серверу
2. Отправка StreamRequest
3. Получение потоковых ответов (text_chunk, audio_chunk)
4. Измерение времени на каждом этапе
5. Валидация всех чанков
"""

import asyncio
import sys
import time
from pathlib import Path
from typing import List, Dict, Any
import grpc
import grpc.aio as aio

# Добавляем путь к модулям
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Импортируем protobuf файлы
try:
    from modules.grpc_service import streaming_pb2, streaming_pb2_grpc
except ImportError:
    # Альтернативный путь для запуска из корня проекта
    server_root = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(server_root))
    from server.modules.grpc_service import streaming_pb2, streaming_pb2_grpc


class RequestFlowTester:
    """Тестер полного пути обработки запроса"""
    
    def __init__(self, host: str = "localhost", port: int = 50051):
        self.host = host
        self.port = port
        self.address = f"{host}:{port}"
        
        # Метрики
        self.metrics = {
            'connection_time': 0,
            'first_text_chunk_time': 0,
            'first_audio_chunk_time': 0,
            'total_time': 0,
            'text_chunks_count': 0,
            'audio_chunks_count': 0,
            'total_audio_bytes': 0,
            'errors': []
        }
        
    async def test_full_flow(self, prompt: str = "Hello, can you help me?", hardware_id: str = "test_hardware_123") -> Dict[str, Any]:
        """
        Полный тест обработки запроса
        
        Args:
            prompt: Текст запроса
            hardware_id: Идентификатор оборудования
            
        Returns:
            Словарь с результатами теста
        """
        print("=" * 80)
        print("🧪 ПОЛНЫЙ E2E ТЕСТ ОБРАБОТКИ ЗАПРОСА")
        print("=" * 80)
        print(f"\n📤 Запрос:")
        print(f"   Prompt: {prompt}")
        print(f"   Hardware ID: {hardware_id}")
        print(f"   Server: {self.address}")
        print()
        
        start_time = time.time()
        
        try:
            # Этап 1: Подключение
            print("🔌 Этап 1: Подключение к серверу...")
            connection_start = time.time()
            
            channel = aio.insecure_channel(self.address)
            stub = streaming_pb2_grpc.StreamingServiceStub(channel)
            
            try:
                await asyncio.wait_for(channel.channel_ready(), timeout=5.0)
                connection_time = time.time() - connection_start
                self.metrics['connection_time'] = connection_time * 1000
                print(f"   ✅ Подключение установлено за {connection_time*1000:.2f}ms")
            except asyncio.TimeoutError:
                print("   ❌ Таймаут подключения")
                return {'success': False, 'error': 'Connection timeout', 'metrics': self.metrics}
            
            # Этап 2: Создание запроса
            print("\n📝 Этап 2: Создание StreamRequest...")
            request = streaming_pb2.StreamRequest(
                prompt=prompt,
                hardware_id=hardware_id,
                session_id=f"test_session_{int(time.time())}"
            )
            print(f"   ✅ Запрос создан: session_id={request.session_id}")
            
            # Этап 3: Отправка запроса и получение ответов
            print("\n🔄 Этап 3: Отправка запроса и получение потоковых ответов...")
            print("   (Ожидание ответов от сервера...)\n")
            
            request_start = time.time()
            first_text_time = None
            first_audio_time = None
            
            text_chunks: List[str] = []
            audio_chunks: List[bytes] = []
            end_message = None
            error_message = None
            
            try:
                async for response in stub.StreamAudio(request, timeout=60.0):
                    response_time = time.time() - request_start
                    content_type = response.WhichOneof("content")
                    
                    if content_type == "text_chunk":
                        if first_text_time is None:
                            first_text_time = response_time
                            self.metrics['first_text_chunk_time'] = first_text_time * 1000
                            print(f"   📝 Первый text_chunk получен через {first_text_time*1000:.2f}ms")
                        
                        text = response.text_chunk
                        text_chunks.append(text)
                        self.metrics['text_chunks_count'] += 1
                        print(f"   📝 Text chunk #{len(text_chunks)}: '{text[:50]}{'...' if len(text) > 50 else ''}' ({len(text)} символов)")
                    
                    elif content_type == "audio_chunk":
                        if first_audio_time is None:
                            first_audio_time = response_time
                            self.metrics['first_audio_chunk_time'] = first_audio_time * 1000
                            print(f"   🎵 Первый audio_chunk получен через {first_audio_time*1000:.2f}ms")
                        
                        audio = response.audio_chunk
                        audio_data = audio.audio_data
                        audio_chunks.append(audio_data)
                        self.metrics['audio_chunks_count'] += 1
                        self.metrics['total_audio_bytes'] += len(audio_data)
                        
                        print(f"   🎵 Audio chunk #{len(audio_chunks)}: {len(audio_data)} bytes "
                              f"(sample_rate={audio.sample_rate}, channels={audio.channels}, dtype={audio.dtype})")
                    
                    elif content_type == "end_message":
                        end_message = response.end_message
                        total_time = time.time() - request_start
                        self.metrics['total_time'] = total_time * 1000
                        print(f"\n   ✅ End message получен через {total_time*1000:.2f}ms: '{end_message}'")
                        break
                    
                    elif content_type == "error_message":
                        error_message = response.error_message
                        print(f"\n   ❌ Error message: '{error_message}'")
                        self.metrics['errors'].append(error_message)
                        break
                
                # Если не было end_message или error_message, но стрим закончился
                if end_message is None and error_message is None:
                    total_time = time.time() - request_start
                    self.metrics['total_time'] = total_time * 1000
                    print(f"\n   ⚠️ Стрим завершился без end_message или error_message (время: {total_time*1000:.2f}ms)")
                
            except grpc.RpcError as e:
                error_time = time.time() - request_start
                error_msg = f"gRPC ошибка: {e.code()} - {e.details()}"
                print(f"\n   ❌ {error_msg} (время: {error_time*1000:.2f}ms)")
                self.metrics['errors'].append(error_msg)
                self.metrics['total_time'] = error_time * 1000
                return {'success': False, 'error': error_msg, 'metrics': self.metrics}
            
            except asyncio.TimeoutError:
                error_time = time.time() - request_start
                error_msg = "Таймаут ожидания ответов (60 секунд)"
                print(f"\n   ❌ {error_msg} (время: {error_time*1000:.2f}ms)")
                self.metrics['errors'].append(error_msg)
                self.metrics['total_time'] = error_time * 1000
                return {'success': False, 'error': error_msg, 'metrics': self.metrics}
            
            finally:
                await channel.close()
            
            # Этап 4: Анализ результатов
            print("\n" + "=" * 80)
            print("📊 РЕЗУЛЬТАТЫ ТЕСТА")
            print("=" * 80)
            
            success = error_message is None and len(text_chunks) > 0
            
            print(f"\n✅ Успешность: {'✅ УСПЕХ' if success else '❌ ОШИБКА'}")
            print(f"\n📈 Метрики:")
            print(f"   • Время подключения: {self.metrics['connection_time']:.2f}ms")
            print(f"   • Время до первого text_chunk: {self.metrics['first_text_chunk_time']:.2f}ms")
            print(f"   • Время до первого audio_chunk: {self.metrics['first_audio_chunk_time']:.2f}ms")
            print(f"   • Общее время обработки: {self.metrics['total_time']:.2f}ms ({self.metrics['total_time']/1000:.2f} сек)")
            print(f"\n📦 Полученные данные:")
            print(f"   • Text chunks: {self.metrics['text_chunks_count']}")
            print(f"   • Audio chunks: {self.metrics['audio_chunks_count']}")
            print(f"   • Всего аудио данных: {self.metrics['total_audio_bytes']} bytes ({self.metrics['total_audio_bytes']/1024:.2f} KB)")
            
            if text_chunks:
                full_text = " ".join(text_chunks)
                print(f"\n📝 Полный текст ответа:")
                print(f"   '{full_text[:200]}{'...' if len(full_text) > 200 else ''}'")
                print(f"   (Всего символов: {len(full_text)})")
            
            if self.metrics['errors']:
                print(f"\n❌ Ошибки:")
                for error in self.metrics['errors']:
                    print(f"   • {error}")
            
            # Анализ производительности
            print(f"\n⚡ Анализ производительности:")
            if self.metrics['first_text_chunk_time'] > 0:
                print(f"   • LLM обработка (до первого text): {self.metrics['first_text_chunk_time']:.2f}ms")
            if self.metrics['first_audio_chunk_time'] > 0:
                tts_time = self.metrics['first_audio_chunk_time'] - self.metrics['first_text_chunk_time']
                if tts_time > 0:
                    print(f"   • TTS обработка (text → audio): {tts_time:.2f}ms")
            
            total_elapsed = time.time() - start_time
            print(f"\n⏱️ Общее время теста: {total_elapsed*1000:.2f}ms ({total_elapsed:.2f} сек)")
            
            return {
                'success': success,
                'text_chunks': text_chunks,
                'audio_chunks_count': len(audio_chunks),
                'total_audio_bytes': self.metrics['total_audio_bytes'],
                'end_message': end_message,
                'error_message': error_message,
                'metrics': self.metrics
            }
            
        except Exception as e:
            error_msg = f"Неожиданная ошибка: {str(e)}"
            print(f"\n❌ {error_msg}")
            import traceback
            traceback.print_exc()
            self.metrics['errors'].append(error_msg)
            return {'success': False, 'error': error_msg, 'metrics': self.metrics}


async def main():
    """Главная функция"""
    import argparse
    
    parser = argparse.ArgumentParser(description='E2E тест полного пути обработки запроса')
    parser.add_argument('--host', default='localhost', help='Адрес сервера (по умолчанию: localhost)')
    parser.add_argument('--port', type=int, default=50051, help='Порт сервера (по умолчанию: 50051)')
    parser.add_argument('--prompt', default='Hello, can you help me?', help='Текст запроса')
    parser.add_argument('--hardware-id', default='test_hardware_123', help='Hardware ID')
    
    args = parser.parse_args()
    
    tester = RequestFlowTester(host=args.host, port=args.port)
    result = await tester.test_full_flow(prompt=args.prompt, hardware_id=args.hardware_id)
    
    # Возвращаем код выхода
    sys.exit(0 if result.get('success') else 1)


if __name__ == "__main__":
    asyncio.run(main())
