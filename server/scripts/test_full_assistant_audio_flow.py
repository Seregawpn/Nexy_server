#!/usr/bin/env python3
"""
Тестирование полного flow: запрос → ответ ассистента → генерация аудио
Проверяет весь процесс от текстового запроса до аудио ответа
"""

import asyncio
import sys
from pathlib import Path
from typing import Dict, Any, AsyncIterator

# Добавляем путь к серверу
sys.path.insert(0, str(Path(__file__).parent.parent))

import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class MockTextProcessor:
    """Мок текстового процессора для тестирования"""
    
    def __init__(self):
        self.is_initialized = True
    
    async def process(self, request: Dict[str, Any]) -> AsyncIterator[Dict[str, Any]]:
        """Имитация генерации текста ассистентом"""
        text = request.get('text', '')
        
        # Имитируем потоковый ответ ассистента
        responses = [
            "Hello! ",
            "This is a test response from the assistant. ",
            "The audio generation should work correctly. ",
            "Let's see if everything is working as expected."
        ]
        
        for response in responses:
            await asyncio.sleep(0.1)  # Имитация задержки
            yield {
                'text_response': response,
                'type': 'text_chunk'
            }
        
        # Финальный ответ
        yield {
            'text_response': ' '.join(responses),
            'is_final': True,
            'type': 'final_response'
        }


async def test_full_flow_with_mock_text():
    """Тест 1: Полный flow с моком текстового процессора"""
    print("\n" + "="*60)
    print("ТЕСТ 1: Полный flow с моком текстового процессора")
    print("="*60)
    
    try:
        from modules.audio_generation.core.audio_processor import AudioProcessor
        from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
        
        # Создаем реальный AudioProcessor
        print("\n1. Инициализация AudioProcessor...")
        audio_processor = AudioProcessor()
        await audio_processor.initialize()
        print("   ✅ AudioProcessor инициализирован")
        
        # Создаем мок текстового процессора
        print("\n2. Создание мока текстового процессора...")
        text_processor = MockTextProcessor()
        print("   ✅ Мок создан")
        
        # Создаем StreamingWorkflowIntegration
        print("\n3. Создание StreamingWorkflowIntegration...")
        workflow = StreamingWorkflowIntegration(
            text_processor=text_processor,
            audio_processor=audio_processor,
            memory_workflow=None,
            text_filter_manager=None
        )
        await workflow.initialize()
        print("   ✅ StreamingWorkflowIntegration инициализирован")
        
        # Тестовый запрос
        request_data = {
            'text': 'Hello, can you tell me a test response?',
            'hardware_id': 'test_hardware',
            'session_id': 'test_session'
        }
        
        print(f"\n4. Обработка запроса: '{request_data['text']}'")
        
        text_responses = []
        audio_chunks = []
        total_audio_bytes = 0
        sentence_count = 0
        
        async for result in workflow.process_request_streaming(request_data):
            # Обрабатываем текстовые ответы
            if 'text_response' in result:
                text = result['text_response']
                text_responses.append(text)
                print(f"   📝 Текст: '{text[:80]}{'...' if len(text) > 80 else ''}'")
            
            # Обрабатываем аудио чанки
            if 'audio_chunk' in result:
                audio_chunk = result['audio_chunk']
                if isinstance(audio_chunk, bytes) and len(audio_chunk) > 0:
                    audio_chunks.append(audio_chunk)
                    total_audio_bytes += len(audio_chunk)
                    sentence_idx = result.get('sentence_index', 0)
                    chunk_idx = result.get('audio_chunk_index', 0)
                    if sentence_idx > sentence_count:
                        sentence_count = sentence_idx
                        print(f"   🔊 Аудио для предложения #{sentence_idx}, чанк #{chunk_idx}: {len(audio_chunk)} байт")
            
            # Финальный ответ
            if result.get('is_final'):
                print(f"\n   ✅ Финальный ответ получен")
        
        print(f"\n5. Итоговая статистика:")
        print(f"   Текстовых ответов: {len(text_responses)}")
        print(f"   Аудио чанков: {len(audio_chunks)}")
        print(f"   Всего аудио байт: {total_audio_bytes} ({total_audio_bytes / 1024:.2f} KB)")
        print(f"   Предложений с аудио: {sentence_count}")
        
        # Проверка результатов
        if len(text_responses) > 0 and len(audio_chunks) > 0:
            print("\n✅ Тест пройден - полный flow работает!")
            return True
        else:
            print("\n❌ Тест провален - не получены все данные")
            return False
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if 'workflow' in locals():
            # Cleanup не требуется, но можно добавить
            pass


async def test_direct_audio_generation():
    """Тест 2: Прямая генерация аудио из текста (без ассистента)"""
    print("\n" + "="*60)
    print("ТЕСТ 2: Прямая генерация аудио из текста")
    print("="*60)
    
    try:
        from modules.audio_generation.core.audio_processor import AudioProcessor
        
        # Создаем AudioProcessor
        print("\n1. Инициализация AudioProcessor...")
        audio_processor = AudioProcessor()
        await audio_processor.initialize()
        print("   ✅ AudioProcessor инициализирован")
        
        # Тестовый текст (имитация ответа ассистента)
        test_text = "Hello! This is a test response from the assistant. The audio generation should work correctly."
        
        print(f"\n2. Генерация аудио для текста:")
        print(f"   '{test_text}'")
        
        chunks = []
        total_bytes = 0
        
        async for audio_chunk in audio_processor.generate_speech_streaming(test_text):
            chunks.append(audio_chunk)
            total_bytes += len(audio_chunk)
            print(f"   🔊 Чанк #{len(chunks)}: {len(audio_chunk)} байт")
        
        print(f"\n3. Результат:")
        print(f"   Чанков: {len(chunks)}")
        print(f"   Всего байт: {total_bytes} ({total_bytes / 1024:.2f} KB)")
        
        if total_bytes > 0:
            print("\n✅ Тест пройден - аудио сгенерировано!")
            return True
        else:
            print("\n❌ Тест провален - аудио не сгенерировано")
            return False
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_multiple_sentences():
    """Тест 3: Генерация аудио для нескольких предложений"""
    print("\n" + "="*60)
    print("ТЕСТ 3: Генерация аудио для нескольких предложений")
    print("="*60)
    
    try:
        from modules.audio_generation.core.audio_processor import AudioProcessor
        
        # Создаем AudioProcessor
        audio_processor = AudioProcessor()
        await audio_processor.initialize()
        
        # Несколько предложений (как в реальном flow)
        sentences = [
            "Hello! This is the first sentence.",
            "This is the second sentence with more words.",
            "And finally, this is the third sentence."
        ]
        
        print(f"\nГенерация аудио для {len(sentences)} предложений:")
        
        total_chunks = 0
        total_bytes = 0
        
        for i, sentence in enumerate(sentences, 1):
            print(f"\n   Предложение {i}: '{sentence}'")
            
            sentence_chunks = 0
            sentence_bytes = 0
            
            async for audio_chunk in audio_processor.generate_speech_streaming(sentence):
                sentence_chunks += 1
                sentence_bytes += len(audio_chunk)
                total_chunks += 1
                total_bytes += len(audio_chunk)
            
            print(f"      🔊 Чанков: {sentence_chunks}, Байт: {sentence_bytes}")
        
        print(f"\nИтого:")
        print(f"   Всего чанков: {total_chunks}")
        print(f"   Всего байт: {total_bytes} ({total_bytes / 1024:.2f} KB)")
        
        if total_bytes > 0:
            print("\n✅ Тест пройден!")
            return True
        else:
            print("\n❌ Тест провален")
            return False
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Основная функция тестирования"""
    print("="*60)
    print("ТЕСТИРОВАНИЕ ПОЛНОГО FLOW: АССИСТЕНТ → АУДИО")
    print("="*60)
    print("\nПроверка всего процесса от запроса до аудио ответа")
    
    results = {
        "direct_audio": False,
        "multiple_sentences": False,
        "full_flow_mock": False,
    }
    
    # Запускаем тесты
    results["direct_audio"] = await test_direct_audio_generation()
    results["multiple_sentences"] = await test_multiple_sentences()
    results["full_flow_mock"] = await test_full_flow_with_mock_text()
    
    # Итоговый отчет
    print("\n" + "="*60)
    print("ИТОГОВЫЙ ОТЧЕТ")
    print("="*60)
    
    for test_name, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    total_tests = len(results)
    passed_tests = sum(1 for s in results.values() if s)
    
    print(f"\nВсего тестов: {total_tests}")
    print(f"Пройдено: {passed_tests}")
    print(f"Провалено: {total_tests - passed_tests}")
    
    if passed_tests == total_tests:
        print("\n🎉 Все тесты пройдены! Полный flow работает корректно.")
        return 0
    else:
        print("\n⚠️  Некоторые тесты провалены. Проверьте ошибки выше.")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

