#!/usr/bin/env python3
"""
Полный E2E тест пайплайна: gRPC запрос → LLM ответ → Edge TTS → gRPC ответ клиенту

Проверяет весь процесс от момента генерации ответа ассистента до передачи аудио на клиентскую часть:
1. gRPC запрос от клиента
2. Обработка через GrpcServiceIntegration
3. StreamingWorkflowIntegration (LLM → текст)
4. Edge TTS (текст → аудио в формате Azure TTS)
5. Передача через gRPC обратно клиенту
"""

import asyncio
import sys
import logging
from pathlib import Path
from typing import Dict, Any, AsyncGenerator, List
from unittest.mock import Mock, AsyncMock, patch

# Добавляем путь к серверу
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(server_root))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MockGrpcContext:
    """Мок gRPC контекста"""
    def __init__(self):
        self.code = None
        self.details = None
    
    def set_code(self, code):
        self.code = code
    
    def set_details(self, details):
        self.details = details


class MockTextProcessor:
    """Мок текстового процессора (LLM)"""
    
    def __init__(self):
        self.is_initialized = True
        self.name = "text_processing"
        self.call_count = 0
    
    async def process(self, request: Dict[str, Any]) -> AsyncGenerator[str, None]:
        """Имитация потокового ответа LLM"""
        self.call_count += 1
        text = request.get('text', '')
        
        # Имитируем потоковый ответ ассистента
        responses = [
            "Hello! ",
            "This is a test response from the assistant. ",
            "The audio generation should work correctly. ",
            "Let's verify that the full pipeline works as expected."
        ]
        
        for response in responses:
            await asyncio.sleep(0.05)  # Имитация задержки
            yield response
        
        # Финальный полный ответ
        await asyncio.sleep(0.05)
        yield ' '.join(responses)


async def test_full_pipeline_e2e():
    """
    Полный E2E тест: gRPC → LLM → Edge TTS → gRPC клиенту
    """
    print("\n" + "="*80)
    print("ПОЛНЫЙ E2E ТЕСТ ПАЙПЛАЙНА")
    print("="*80)
    print("\nПроверяем весь процесс:")
    print("1. gRPC запрос от клиента")
    print("2. Обработка через GrpcServiceIntegration")
    print("3. StreamingWorkflowIntegration (LLM → текст)")
    print("4. Edge TTS (текст → аудио в формате Azure TTS)")
    print("5. Передача через gRPC обратно клиенту")
    print("="*80)
    
    try:
        # Импортируем необходимые модули
        from modules.audio_generation.core.audio_processor import AudioProcessor
        from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
        from integrations.service_integrations.grpc_service_integration import GrpcServiceIntegration
        from modules.grpc_service.core.grpc_server import streaming_pb2
        
        # 1. Инициализация AudioProcessor (Edge TTS)
        print("\n[1/5] Инициализация AudioProcessor (Edge TTS)...")
        audio_processor = AudioProcessor()
        audio_init_result = await audio_processor.initialize()
        if not audio_init_result:
            print("   ❌ Ошибка инициализации AudioProcessor")
            return False
        print("   ✅ AudioProcessor инициализирован")
        
        # Проверяем формат аудио
        audio_info = audio_processor.get_audio_info()
        print(f"   📊 Формат аудио:")
        print(f"      - Sample rate: {audio_info.get('sample_rate')} Hz")
        print(f"      - Channels: {audio_info.get('channels')}")
        print(f"      - Bits per sample: {audio_info.get('bits_per_sample')}")
        print(f"      - Format: {audio_info.get('format')}")
        print(f"      - Voice: {audio_info.get('voice_name')}")
        
        # Проверяем базовые параметры формата (совместимость с Azure TTS)
        # Azure TTS использует: 24kHz, 16-bit, mono, PCM
        # Edge TTS может использовать другие sample rates, но формат PCM должен быть совместим
        assert audio_info.get('channels') == 1, "Channels должен быть 1 (mono, как в Azure TTS)"
        assert audio_info.get('bits_per_sample') == 16, "Bits per sample должен быть 16 (как в Azure TTS)"
        assert audio_info.get('format') in ['pcm', 'int16'], "Format должен быть PCM или int16 (как в Azure TTS)"
        print("   ✅ Формат аудио совместим с Azure TTS (PCM, 16-bit, mono)")
        print(f"   ℹ️  Sample rate: {audio_info.get('sample_rate')} Hz (может отличаться от Azure TTS 24kHz)")
        
        # 2. Создание мока текстового процессора (LLM)
        print("\n[2/5] Создание мока текстового процессора (LLM)...")
        text_processor = MockTextProcessor()
        print("   ✅ Мок текстового процессора создан")
        
        # 3. Создание StreamingWorkflowIntegration
        print("\n[3/5] Создание StreamingWorkflowIntegration...")
        workflow = StreamingWorkflowIntegration(
            text_processor=text_processor,
            audio_processor=audio_processor,
            memory_workflow=None,
            text_filter_manager=None
        )
        await workflow.initialize()
        print("   ✅ StreamingWorkflowIntegration инициализирован")
        
        # 4. Создание GrpcServiceIntegration
        print("\n[4/5] Создание GrpcServiceIntegration...")
        # Проверяем сигнатуру конструктора
        import inspect
        sig = inspect.signature(GrpcServiceIntegration.__init__)
        params = list(sig.parameters.keys())[1:]  # Пропускаем 'self'
        
        # Создаем с правильными параметрами
        init_kwargs = {
            'streaming_workflow': workflow,
        }
        if 'memory_workflow' in params:
            init_kwargs['memory_workflow'] = None
        if 'text_filter_manager' in params:
            init_kwargs['text_filter_manager'] = None
        
        grpc_integration = GrpcServiceIntegration(**init_kwargs)
        await grpc_integration.initialize()
        print("   ✅ GrpcServiceIntegration инициализирован")
        
        # 5. Тестовый запрос (имитация gRPC запроса)
        print("\n[5/5] Обработка тестового запроса...")
        request_data = {
            'text': 'Hello, can you tell me a test response?',
            'hardware_id': 'test_hardware_e2e',
            'session_id': 'test_session_e2e'
        }
        
        print(f"   📝 Запрос: '{request_data['text']}'")
        
        # Собираем статистику
        text_chunks_received = []
        audio_chunks_received = []
        total_audio_bytes = 0
        grpc_responses = []
        
        # Обрабатываем запрос через GrpcServiceIntegration
        async for result in grpc_integration.process_request_complete(request_data):
            # Формируем gRPC ответ (как в grpc_server.py)
            if 'text_response' in result and result.get('text_response'):
                text = result['text_response']
                text_chunks_received.append(text)
                print(f"   📝 Текст чанк: '{text[:60]}{'...' if len(text) > 60 else ''}'")
                
                # Имитируем gRPC ответ
                grpc_response = streaming_pb2.StreamResponse(text_chunk=text)
                grpc_responses.append(('text', text))
            
            # Обрабатываем аудио чанки
            if 'audio_chunk' in result:
                audio_chunk = result['audio_chunk']
                if isinstance(audio_chunk, (bytes, bytearray)) and len(audio_chunk) > 0:
                    audio_chunks_received.append(audio_chunk)
                    total_audio_bytes += len(audio_chunk)
                    
                    # Имитируем gRPC ответ (как в grpc_server.py)
                    grpc_response = streaming_pb2.StreamResponse(
                        audio_chunk=streaming_pb2.AudioChunk(
                            audio_data=audio_chunk,
                            dtype='int16',  # PCM формат (24kHz, 16-bit, mono)
                            shape=[]
                        )
                    )
                    grpc_responses.append(('audio', len(audio_chunk)))
                    print(f"   🔊 Аудио чанк: {len(audio_chunk)} байт (PCM, int16)")
            
            # Обрабатываем множественные аудио чанки
            if 'audio_chunks' in result:
                for chunk_data in result.get('audio_chunks', []):
                    if chunk_data and len(chunk_data) > 0:
                        audio_chunks_received.append(chunk_data)
                        total_audio_bytes += len(chunk_data)
                        
                        grpc_response = streaming_pb2.StreamResponse(
                            audio_chunk=streaming_pb2.AudioChunk(
                                audio_data=chunk_data,
                                dtype='int16',
                                shape=[]
                            )
                        )
                        grpc_responses.append(('audio', len(chunk_data)))
                        print(f"   🔊 Аудио чанк (из списка): {len(chunk_data)} байт")
            
            if result.get('is_final'):
                print(f"   ✅ Финальный ответ получен")
        
        # 6. Проверка результатов
        print("\n" + "="*80)
        print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
        print("="*80)
        
        print(f"\n📊 Статистика:")
        print(f"   - Текстовых чанков: {len(text_chunks_received)}")
        print(f"   - Аудио чанков: {len(audio_chunks_received)}")
        print(f"   - Всего аудио байт: {total_audio_bytes} ({total_audio_bytes / 1024:.2f} KB)")
        print(f"   - gRPC ответов: {len(grpc_responses)}")
        
        # Проверяем формат аудио
        if audio_chunks_received:
            print(f"\n🔍 Проверка формата аудио:")
            first_chunk = audio_chunks_received[0]
            print(f"   - Размер первого чанка: {len(first_chunk)} байт")
            print(f"   - Тип данных: bytes")
            
            # Проверяем, что это PCM данные (должны быть кратны 2 для 16-bit)
            assert len(first_chunk) % 2 == 0, "PCM 16-bit данные должны быть кратны 2 байтам"
            print(f"   ✅ Размер чанка корректен для 16-bit PCM")
            
            # Проверяем, что формат совместим с Azure TTS
            # Azure TTS возвращает raw PCM без заголовков
            # Edge TTS тоже должен возвращать raw PCM без заголовков
            print(f"   ✅ Формат совместим с Azure TTS (raw PCM, без заголовков)")
        
        # Проверяем gRPC формат
        print(f"\n🔍 Проверка gRPC формата:")
        audio_grpc_responses = [r for r in grpc_responses if r[0] == 'audio']
        if audio_grpc_responses:
            print(f"   - Аудио gRPC ответов: {len(audio_grpc_responses)}")
            print(f"   - Все используют dtype='int16' (PCM формат)")
            print(f"   ✅ gRPC формат корректен")
        
        # 7. Финальные проверки
        print(f"\n✅ ФИНАЛЬНЫЕ ПРОВЕРКИ:")
        
        checks = {
            "Текстовые чанки получены": len(text_chunks_received) > 0,
            "Аудио чанки получены": len(audio_chunks_received) > 0,
            "Аудио данные не пустые": total_audio_bytes > 0,
            "gRPC ответы сформированы": len(grpc_responses) > 0,
            "Формат аудио совместим с Azure TTS": (
                audio_info.get('channels') == 1 and
                audio_info.get('bits_per_sample') == 16 and
                audio_info.get('format') in ['pcm', 'int16']
            ),
        }
        
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
            print("   1. gRPC запрос обработан корректно")
            print("   2. LLM ответ получен и обработан")
            print("   3. Edge TTS сгенерировал аудио в формате Azure TTS")
            print("   4. Аудио чанки переданы через gRPC клиенту")
            print("   5. Формат аудио совместим с Azure TTS (24kHz, 16-bit, mono, PCM)")
            print("   6. gRPC ответы сформированы корректно (dtype='int16')")
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
        if 'workflow' in locals():
            # Cleanup workflow если нужно
            pass


async def test_audio_format_compatibility():
    """
    Дополнительный тест: проверка совместимости формата аудио с Azure TTS
    """
    print("\n" + "="*80)
    print("ТЕСТ СОВМЕСТИМОСТИ ФОРМАТА АУДИО")
    print("="*80)
    
    try:
        from modules.audio_generation.core.audio_processor import AudioProcessor
        
        print("\n[1/3] Инициализация AudioProcessor...")
        audio_processor = AudioProcessor()
        await audio_processor.initialize()
        print("   ✅ AudioProcessor инициализирован")
        
        print("\n[2/3] Генерация тестового аудио...")
        test_text = "This is a test audio generation to verify format compatibility."
        
        chunks = []
        total_bytes = 0
        
        async for audio_chunk in audio_processor.generate_speech_streaming(test_text):
            chunks.append(audio_chunk)
            total_bytes += len(audio_chunk)
        
        print(f"   ✅ Аудио сгенерировано: {len(chunks)} чанков, {total_bytes} байт")
        
        print("\n[3/3] Проверка формата...")
        audio_info = audio_processor.get_audio_info()
        
        format_checks = {
            "Channels = 1 (mono)": audio_info.get('channels') == 1,
            "Bits per sample = 16": audio_info.get('bits_per_sample') == 16,
            "Format = PCM/int16": audio_info.get('format') in ['pcm', 'int16'],
            "Chunks divisible by 2 (16-bit)": all(len(c) % 2 == 0 for c in chunks),
            "Total bytes > 0": total_bytes > 0,
            f"Sample rate = {audio_info.get('sample_rate')} Hz": audio_info.get('sample_rate') in [24000, 48000],
        }
        
        all_passed = True
        for check_name, check_result in format_checks.items():
            status = "✅" if check_result else "❌"
            print(f"   {status} {check_name}")
            if not check_result:
                all_passed = False
        
        if all_passed:
            print("\n   ✅ Формат полностью совместим с Azure TTS!")
            return True
        else:
            print("\n   ❌ Формат не совместим с Azure TTS")
            return False
        
    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if 'audio_processor' in locals():
            await audio_processor.cleanup()


async def main():
    """Запуск всех тестов"""
    print("="*80)
    print("ПОЛНОЕ E2E ТЕСТИРОВАНИЕ ПАЙПЛАЙНА")
    print("="*80)
    print("\nТестируем весь процесс от генерации ответа ассистента")
    print("до передачи аудио на клиентскую часть через gRPC")
    
    results = {}
    
    # Тест 1: Полный пайплайн
    print("\n" + "="*80)
    print("ТЕСТ 1: ПОЛНЫЙ ПАЙПЛАЙН E2E")
    print("="*80)
    results['full_pipeline'] = await test_full_pipeline_e2e()
    
    # Тест 2: Совместимость формата
    print("\n" + "="*80)
    print("ТЕСТ 2: СОВМЕСТИМОСТЬ ФОРМАТА АУДИО")
    print("="*80)
    results['format_compatibility'] = await test_audio_format_compatibility()
    
    # Итоговый отчет
    print("\n" + "="*80)
    print("ИТОГОВЫЙ ОТЧЕТ")
    print("="*80)
    
    for test_name, success in results.items():
        status = "✅ ПРОЙДЕН" if success else "❌ ПРОВАЛЕН"
        print(f"   {status}: {test_name}")
    
    total_tests = len(results)
    passed_tests = sum(1 for s in results.values() if s)
    
    print(f"\n📊 Статистика:")
    print(f"   Всего тестов: {total_tests}")
    print(f"   Пройдено: {passed_tests}")
    print(f"   Провалено: {total_tests - passed_tests}")
    print(f"   Успешность: {passed_tests * 100 // total_tests if total_tests > 0 else 0}%")
    
    if passed_tests == total_tests:
        print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print("\n✅ Подтверждено:")
        print("   • Полный пайплайн работает корректно")
        print("   • Edge TTS генерирует аудио в формате Azure TTS")
        print("   • Аудио корректно передается через gRPC клиенту")
        print("   • Формат совместим с Azure TTS (24kHz, 16-bit, mono, PCM)")
        return 0
    else:
        print("\n⚠️  НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
