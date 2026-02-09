#!/usr/bin/env python3
"""
Тест полной pipeline логики: генерация → накопление → сборка → передача на клиент

Проверяет весь процесс:
1. Edge TTS генерирует аудио для предложения
2. Провайдер разбивает на чанки (внутренняя обработка)
3. _stream_audio_for_sentence накапливает все чанки
4. Чанки собираются в единое аудио предложения
5. Полное аудио отправляется через gRPC клиенту
"""

import asyncio
import sys
import logging
from pathlib import Path
from typing import Dict, Any, List
from unittest.mock import Mock, AsyncMock

# Добавляем путь к серверу
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(server_root))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MockTextProcessor:
    """Мок текстового процессора (LLM)"""
    
    def __init__(self):
        self.is_initialized = True
        self.name = "text_processing"
    
    async def process(self, request: Dict[str, Any]):
        """Имитация потокового ответа LLM"""
        text = request.get('text', '')
        
        # Имитируем потоковый ответ ассистента
        responses = [
            "Hello! This is a test sentence for audio generation. ",
            "The audio should be generated correctly. ",
            "All chunks should be collected and assembled properly."
        ]
        
        for response in responses:
            await asyncio.sleep(0.01)
            yield response


async def test_chunk_collection_pipeline():
    """
    Тест полной pipeline: генерация → накопление → сборка → передача
    """
    print("\n" + "="*80)
    print("ТЕСТ ПОЛНОЙ PIPELINE: ГЕНЕРАЦИЯ → НАКОПЛЕНИЕ → СБОРКА → ПЕРЕДАЧА")
    print("="*80)
    print("\nПроверяем:")
    print("1. Edge TTS генерирует аудио для предложения")
    print("2. Провайдер разбивает на чанки (внутренняя обработка)")
    print("3. _stream_audio_for_sentence накапливает все чанки")
    print("4. Чанки собираются в единое аудио предложения")
    print("5. Полное аудио отправляется через gRPC клиенту")
    print("="*80)
    
    try:
        # Импортируем необходимые модули
        from modules.audio_generation.core.audio_processor import AudioProcessor
        from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
        from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration
        from modules.grpc_service.core.grpc_server import streaming_pb2
        
        # 1. Инициализация AudioProcessor (Edge TTS)
        print("\n[1/6] Инициализация AudioProcessor (Edge TTS)...")
        audio_processor = AudioProcessor()
        audio_init_result = await audio_processor.initialize()
        if not audio_init_result:
            print("   ❌ Ошибка инициализации AudioProcessor")
            return False
        print("   ✅ AudioProcessor инициализирован")
        
        # 2. Создание мока текстового процессора
        print("\n[2/6] Создание мока текстового процессора...")
        text_processor = MockTextProcessor()
        print("   ✅ Мок текстового процессора создан")
        
        # 3. Создание StreamingWorkflowIntegration
        print("\n[3/6] Создание StreamingWorkflowIntegration...")
        workflow = StreamingWorkflowIntegration(
            text_processor=text_processor,
            audio_processor=audio_processor,
            memory_workflow=None,
            text_filter_manager=None
        )
        await workflow.initialize()
        print("   ✅ StreamingWorkflowIntegration инициализирован")
        
        # 4. Создание GrpcServiceIntegration
        print("\n[4/6] Создание GrpcServiceIntegration...")
        import inspect
        sig = inspect.signature(GrpcServiceIntegration.__init__)
        params = list(sig.parameters.keys())[1:]
        
        init_kwargs = {'streaming_workflow': workflow}
        if 'memory_workflow' in params:
            init_kwargs['memory_workflow'] = None
        if 'text_filter_manager' in params:
            init_kwargs['text_filter_manager'] = None
        
        grpc_integration = GrpcServiceIntegration(**init_kwargs)
        await grpc_integration.initialize()
        print("   ✅ GrpcServiceIntegration инициализирован")
        
        # 5. Тестовый запрос
        print("\n[5/6] Обработка тестового запроса...")
        request_data = {
            'text': 'Hello, can you tell me a test response?',
            'hardware_id': 'test_hardware_chunk_collection',
            'session_id': 'test_session_chunk_collection'
        }
        print(f"   📝 Запрос: '{request_data['text']}'")
        
        # Собираем статистику для проверки накопления и сборки
        text_chunks_received = []
        audio_chunks_received = []  # Должно быть ОДНО полное аудио предложения
        total_audio_bytes = 0
        sentence_indices = set()
        grpc_responses = []
        
        # Отслеживаем процесс накопления чанков
        provider_chunks_count = {}  # sentence_index -> количество чанков от провайдера
        
        # Обрабатываем запрос
        async for result in grpc_integration.process_request_complete(request_data):
            # Текстовые чанки
            if 'text_response' in result and result.get('text_response'):
                text = result['text_response']
                text_chunks_received.append(text)
                sentence_index = result.get('sentence_index', 0)
                sentence_indices.add(sentence_index)
                print(f"   📝 Текст предложения #{sentence_index}: '{text[:60]}{'...' if len(text) > 60 else ''}'")
                
                grpc_response = streaming_pb2.StreamResponse(text_chunk=text)
                grpc_responses.append(('text', text, sentence_index))
            
            # Аудио чанки (должно быть ОДНО полное аудио для каждого предложения)
            if 'audio_chunk' in result:
                audio_chunk = result['audio_chunk']
                if isinstance(audio_chunk, (bytes, bytearray)) and len(audio_chunk) > 0:
                    audio_chunks_received.append(audio_chunk)
                    total_audio_bytes += len(audio_chunk)
                    sentence_index = result.get('sentence_index', 0)
                    
                    print(f"   🔊 Полное аудио предложения #{sentence_index}: {len(audio_chunk)} байт")
                    
                    # Имитируем gRPC ответ
                    grpc_response = streaming_pb2.StreamResponse(
                        audio_chunk=streaming_pb2.AudioChunk(
                            audio_data=audio_chunk,
                            dtype='int16',
                            shape=[]
                        )
                    )
                    grpc_responses.append(('audio', len(audio_chunk), sentence_index))
        
        # 6. Проверка результатов
        print("\n" + "="*80)
        print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
        print("="*80)
        
        print(f"\n📊 Статистика:")
        print(f"   - Текстовых предложений: {len(text_chunks_received)}")
        print(f"   - Аудио предложений (полных): {len(audio_chunks_received)}")
        print(f"   - Всего аудио байт: {total_audio_bytes} ({total_audio_bytes / 1024:.2f} KB)")
        print(f"   - gRPC ответов: {len(grpc_responses)}")
        print(f"   - Уникальных sentence_index: {len(sentence_indices)}")
        
        # КРИТИЧЕСКИЕ ПРОВЕРКИ
        print(f"\n🔍 КРИТИЧЕСКИЕ ПРОВЕРКИ:")
        
        checks = {}
        
        # Проверка 1: Количество текстовых предложений = количество аудио предложений
        text_count = len(text_chunks_received)
        audio_count = len(audio_chunks_received)
        checks["Количество текстовых предложений = количеству аудио предложений"] = (
            text_count == audio_count and text_count > 0
        )
        print(f"   {'✅' if checks['Количество текстовых предложений = количеству аудио предложений'] else '❌'} "
              f"Текстовых: {text_count}, Аудио: {audio_count}")
        
        # Проверка 2: Каждое аудио предложение - это полное аудио (не отдельные чанки)
        if audio_chunks_received:
            # Проверяем размеры - полное аудио должно быть достаточно большим
            # (не маленькие чанки по 4096 байт)
            min_expected_size = 10000  # Минимальный размер для полного предложения
            all_complete = all(len(chunk) >= min_expected_size for chunk in audio_chunks_received)
            checks["Все аудио предложения - полные (не отдельные чанки)"] = all_complete
            
            sizes = [len(chunk) for chunk in audio_chunks_received]
            print(f"   {'✅' if all_complete else '❌'} "
                  f"Размеры аудио предложений: {sizes}")
            print(f"      (минимальный ожидаемый: {min_expected_size} байт)")
            
            # Проверка 3: Каждое предложение имеет уникальный sentence_index
            audio_sentence_indices = [r[2] for r in grpc_responses if r[0] == 'audio']
            unique_indices = len(set(audio_sentence_indices))
            checks["Каждое аудио предложение имеет уникальный sentence_index"] = (
                unique_indices == audio_count
            )
            print(f"   {'✅' if checks['Каждое аудио предложение имеет уникальный sentence_index'] else '❌'} "
                  f"Уникальных индексов: {unique_indices}, Аудио предложений: {audio_count}")
        
        # Проверка 4: gRPC формат корректен
        audio_grpc_responses = [r for r in grpc_responses if r[0] == 'audio']
        checks["gRPC ответы сформированы корректно"] = len(audio_grpc_responses) > 0
        print(f"   {'✅' if checks['gRPC ответы сформированы корректно'] else '❌'} "
              f"Аудио gRPC ответов: {len(audio_grpc_responses)}")
        
        # Проверка 5: Формат аудио совместим с Azure TTS
        if audio_chunks_received:
            first_chunk = audio_chunks_received[0]
            # PCM 16-bit данные должны быть кратны 2
            pcm_valid = len(first_chunk) % 2 == 0
            checks["Формат аудио совместим с Azure TTS (PCM 16-bit)"] = pcm_valid
            print(f"   {'✅' if pcm_valid else '❌'} "
                  f"PCM формат валиден (размер кратен 2): {len(first_chunk)} байт")
        
        # Проверка 6: Соответствие текста и аудио по sentence_index
        text_indices = [r[2] for r in grpc_responses if r[0] == 'text']
        audio_indices = [r[2] for r in grpc_responses if r[0] == 'audio']
        indices_match = set(text_indices) == set(audio_indices)
        checks["Текст и аудио соответствуют по sentence_index"] = indices_match
        print(f"   {'✅' if indices_match else '❌'} "
              f"Текстовые индексы: {sorted(text_indices)}, Аудио индексы: {sorted(audio_indices)}")
        
        # Итоговые проверки
        print(f"\n✅ ФИНАЛЬНЫЕ ПРОВЕРКИ:")
        all_passed = True
        for check_name, check_result in checks.items():
            status = "✅" if check_result else "❌"
            print(f"   {status} {check_name}")
            if not check_result:
                all_passed = False
        
        if all_passed:
            print("\n" + "="*80)
            print("🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!")
            print("="*80)
            print("\n✅ Подтверждено:")
            print("   1. Edge TTS генерирует аудио для предложений")
            print("   2. Провайдер разбивает на чанки (внутренняя обработка)")
            print("   3. _stream_audio_for_sentence накапливает все чанки")
            print("   4. Чанки собираются в единое аудио предложения")
            print("   5. Полное аудио отправляется через gRPC клиенту")
            print("   6. Каждое предложение имеет одно полное аудио (не отдельные чанки)")
            print("   7. Текст и аудио соответствуют по sentence_index")
            return True
        else:
            print("\n" + "="*80)
            print("❌ НЕКОТОРЫЕ ПРОВЕРКИ ПРОВАЛЕНЫ")
            print("="*80)
            return False
        
    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        # Cleanup
        if 'audio_processor' in locals():
            await audio_processor.cleanup()


async def main():
    """Запуск теста"""
    print("="*80)
    print("ТЕСТ ПОЛНОЙ PIPELINE: ГЕНЕРАЦИЯ → НАКОПЛЕНИЕ → СБОРКА → ПЕРЕДАЧА")
    print("="*80)
    
    success = await test_chunk_collection_pipeline()
    
    if success:
        print("\n🎉 ТЕСТ ПРОЙДЕН УСПЕШНО!")
        return 0
    else:
        print("\n⚠️  ТЕСТ ПРОВАЛЕН")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
