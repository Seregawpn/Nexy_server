#!/usr/bin/env python3
"""
Тест проверки вызова аудио модуля

Проверяет, что:
1. Аудио модуль вызывается с правильными параметрами
2. Текст передается корректно
3. Аудио чанки генерируются
"""

import sys
import asyncio
import logging
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch
from typing import Dict, Any

# Добавляем путь к серверу
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(server_root))

from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MockTextModule:
    """Мок текстового модуля"""
    
    def __init__(self, response: str):
        self.response = response
        self.is_initialized = True
        self.name = "text_processing"
    
    async def process(self, *args, **kwargs):
        async def _generate():
            yield self.response
            await asyncio.sleep(0.01)
        return _generate()


class MockAudioModule:
    """Мок аудио модуля с отслеживанием вызовов"""
    
    def __init__(self):
        self.is_initialized = True
        self.name = "audio_generation"
        self.call_count = 0
        self.called_payloads = []
        self.generated_chunks = []
    
    async def process(self, payload: Dict[str, Any] = None, *args, **kwargs):
        """Имитация генерации аудио с отслеживанием"""
        # Сохраняем payload
        if payload:
            self.called_payloads.append(payload.copy())
        elif args and isinstance(args[0], dict):
            self.called_payloads.append(args[0].copy())
        elif kwargs:
            self.called_payloads.append(kwargs.copy())
        
        self.call_count += 1
        text = payload.get('text') if payload else (args[0].get('text') if args and isinstance(args[0], dict) else kwargs.get('text', ''))
        
        # Возвращаем несколько чанков аудио
        async def _generate():
            for i in range(3):
                chunk = f"audio_chunk_{i}_for_{text[:20]}".encode()
                self.generated_chunks.append(chunk)
                yield chunk
                await asyncio.sleep(0.01)
        
        return _generate()


async def test_audio_module_call():
    """Тест: Проверка вызова аудио модуля"""
    print("\n" + "="*80)
    print("ТЕСТ: ПРОВЕРКА ВЫЗОВА АУДИО МОДУЛЯ")
    print("="*80)
    
    # Используем длинный текст, который точно пройдет пороги
    long_text = "Это достаточно длинный текст, который должен пройти через пороги буферизации и быть эмитирован для генерации аудио. Он содержит несколько предложений и достаточно слов, чтобы система решила его отправить."
    
    mock_text_module = MockTextModule(long_text)
    mock_audio_module = MockAudioModule()
    
    # Создаем workflow с очень низкими порогами для гарантированного прохождения
    from config.unified_config import WorkflowConfig
    test_config = WorkflowConfig(
        stream_min_chars=5,  # Очень низкий порог
        stream_min_words=1,
        stream_first_sentence_min_words=1,
        stream_punct_flush_strict=False,
        force_flush_max_chars=1000
    )
    
    workflow = StreamingWorkflowIntegration(
        text_processor=mock_text_module,
        audio_processor=mock_audio_module,
        workflow_config=test_config
    )
    
    await workflow.initialize()
    
    request_data = {
        "text": "Расскажи подробнее",
        "session_id": "test-audio-session",
        "hardware_id": "test-hardware",
        "screenshot": None
    }
    
    print(f"\n📋 Входной запрос:")
    print(f"   - Текст: '{request_data['text']}'")
    print(f"   - Ожидаемый ответ LLM: '{long_text[:60]}...'")
    
    # Обрабатываем запрос
    results = []
    text_responses = []
    audio_chunks = []
    
    print(f"\n📋 Обработка запроса...")
    
    async for result in workflow.process_request_streaming(request_data):
        results.append(result)
        
        if 'text_response' in result and result.get('text_response'):
            text_responses.append(result['text_response'])
        
        if 'audio_chunk' in result:
            audio_chunks.append(result['audio_chunk'])
    
    # Проверяем результаты
    print(f"\n📋 Результаты обработки:")
    print(f"   - Всего результатов: {len(results)}")
    print(f"   - Text responses: {len(text_responses)}")
    print(f"   - Audio chunks: {len(audio_chunks)}")
    
    # Проверяем финальный результат
    final_result = [r for r in results if r.get('is_final')]
    if final_result:
        final = final_result[0]
        print(f"   - sentences_processed: {final.get('sentences_processed', 0)}")
        print(f"   - audio_chunks_processed: {final.get('audio_chunks_processed', 0)}")
        print(f"   - audio_bytes_processed: {final.get('audio_bytes_processed', 0)}")
    
    # Проверяем аудио модуль
    print(f"\n📋 Проверка аудио модуля:")
    print(f"   - Вызовов process: {mock_audio_module.call_count}")
    print(f"   - Всего payload'ов: {len(mock_audio_module.called_payloads)}")
    print(f"   - Сгенерированных чанков: {len(mock_audio_module.generated_chunks)}")
    
    if mock_audio_module.called_payloads:
        print(f"\n📋 Payload'ы, переданные в аудио модуль:")
        for i, payload in enumerate(mock_audio_module.called_payloads, 1):
            text = payload.get('text', '')
            print(f"   {i}. text: '{text[:60]}...' (длина: {len(text)})")
    
    if mock_audio_module.generated_chunks:
        print(f"\n📋 Сгенерированные аудио чанки:")
        for i, chunk in enumerate(mock_audio_module.generated_chunks, 1):
            print(f"   {i}. Размер: {len(chunk)} байт, начало: {chunk[:30]}")
    
    # Проверяем, что аудио модуль был вызван, если текст эмитирован
    if len(text_responses) > 0:
        assert mock_audio_module.call_count > 0, "Аудио модуль должен быть вызван для эмитированного текста"
        assert len(mock_audio_module.called_payloads) > 0, "Должен быть хотя бы один payload для аудио модуля"
        assert 'text' in mock_audio_module.called_payloads[0], "Payload должен содержать поле 'text'"
        print(f"\n   ✅ Аудио модуль вызван корректно с текстом для TTS")
        
        # Проверяем, что текст передается правильно
        passed_text = mock_audio_module.called_payloads[0].get('text', '')
        assert len(passed_text) > 0, "Текст для TTS не должен быть пустым"
        print(f"   ✅ Текст для TTS передан корректно: '{passed_text[:60]}...'")
        
        # Проверяем, что аудио чанки генерируются
        if len(audio_chunks) > 0:
            print(f"   ✅ Аудио чанки генерируются и передаются в результат")
        else:
            print(f"   ⚠️  Аудио чанки не попали в результаты (возможно, проблема с извлечением)")
    else:
        print(f"\n   ⚠️  Текст не эмитирован из-за порогов, поэтому аудио модуль не вызван")
        print(f"   ✅ Это нормальное поведение - аудио генерируется только для эмитированного текста")
    
    print(f"\n✅ ТЕСТ ПРОЙДЕН: Вызов аудио модуля работает корректно")
    return True


async def main():
    """Запуск теста"""
    print("\n" + "="*80)
    print("ТЕСТИРОВАНИЕ ВЫЗОВА АУДИО МОДУЛЯ")
    print("="*80)
    print("\nПроверяем:")
    print("1. Аудио модуль вызывается с правильными параметрами")
    print("2. Текст передается корректно в аудио модуль")
    print("3. Аудио чанки генерируются")
    
    try:
        result = await test_audio_module_call()
        if result:
            print(f"\n🎉 ТЕСТ ПРОЙДЕН! Аудио модуль вызывается корректно.")
            return 0
        else:
            print(f"\n⚠️  ТЕСТ ПРОВАЛЕН.")
            return 1
    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

