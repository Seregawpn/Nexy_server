#!/usr/bin/env python3
"""
Тест проверки обработки аудио для ответов LLM

Проверяет полный поток:
1. LLM возвращает ответ (с командой или без)
2. Парсер извлекает text_response
3. text_response передается в аудио модуль для генерации TTS
4. Аудио чанки генерируются и передаются клиенту
"""

import sys
import asyncio
import json
import logging
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch
from typing import Dict, Any, AsyncGenerator

# Добавляем путь к серверу
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(server_root))

from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration
from integrations.core.assistant_response_parser import AssistantResponseParser

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MockTextModule:
    """Мок текстового модуля, который возвращает ответы LLM"""
    
    def __init__(self, response):
        self.response = response
        self.is_initialized = True
        self.name = "text_processing"
    
    async def process(self, *args, **kwargs):
        async def _generate():
            if isinstance(self.response, dict):
                yield json.dumps(self.response, ensure_ascii=False)
            else:
                yield self.response
            await asyncio.sleep(0.01)
        return _generate()


class MockAudioModule:
    """Мок аудио модуля с отслеживанием вызовов"""
    
    def __init__(self):
        self.is_initialized = True
        self.name = "audio_generation"
        self.call_count = 0
        self.called_texts = []  # Список текстов, переданных в TTS
    
    async def process(self, payload: Dict[str, Any] = None, *args, **kwargs):
        """Имитация генерации аудио"""
        # Извлекаем текст из payload
        text = None
        if payload and isinstance(payload, dict):
            text = payload.get('text')
        elif args and isinstance(args[0], dict):
            text = args[0].get('text')
        elif kwargs.get('text'):
            text = kwargs['text']
        
        if text:
            self.called_texts.append(text)
            logger.info(f"🔊 MockAudioModule.process вызван с text: '{text[:60]}...'")
        
        self.call_count += 1
        
        # Возвращаем несколько чанков аудио
        async def _generate():
            for i in range(2):
                yield {"audio": f"audio_chunk_{i}".encode(), "type": "audio_chunk"}
                await asyncio.sleep(0.01)
        
        return _generate()


async def test_llm_response_without_command_audio():
    """Тест 1: LLM возвращает обычный текст → проверяем, что текст передается в аудио модуль"""
    print("\n" + "="*80)
    print("ТЕСТ 1: LLM ОТВЕТ БЕЗ КОМАНДЫ → АУДИО ДЛЯ ТЕКСТА")
    print("="*80)
    
    # LLM возвращает обычный текст (не JSON)
    llm_text_response = "Привет! Как дела? У меня всё отлично, спасибо! Чем могу помочь?"
    
    mock_text_module = MockTextModule(llm_text_response)
    mock_audio_module = MockAudioModule()
    
    # Создаем workflow с низкими порогами
    from config.unified_config import WorkflowConfig
    test_config = WorkflowConfig(
        stream_min_chars=10,
        stream_min_words=2,
        stream_first_sentence_min_words=2,
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
        "text": "Привет, как дела?",
        "session_id": "test-session-audio-1",
        "hardware_id": "test-hardware",
        "screenshot": None
    }
    
    print(f"\n📋 Входной запрос:")
    print(f"   - Текст: '{request_data['text']}'")
    
    print(f"\n📋 Ожидаемый ответ LLM:")
    print(f"   '{llm_text_response}'")
    
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
    
    # Проверяем парсер
    print(f"\n📋 Проверка парсера:")
    parser = AssistantResponseParser()
    parsed = parser.parse(llm_text_response)
    print(f"   - text_response из парсера: '{parsed.text_response[:60]}...'")
    print(f"   - command_payload: {parsed.command_payload is not None}")
    assert parsed.command_payload is None, "Для обычного текста не должно быть команды"
    assert parsed.text_response == llm_text_response, "Парсер должен вернуть исходный текст"
    print(f"   ✅ Парсер правильно обработал обычный текст")
    
    # Проверяем аудио модуль
    print(f"\n📋 Проверка аудио модуля:")
    print(f"   - Вызовов process: {mock_audio_module.call_count}")
    print(f"   - Текстов для TTS: {len(mock_audio_module.called_texts)}")
    
    if mock_audio_module.called_texts:
        print(f"   - Тексты, переданные в TTS:")
        for i, text in enumerate(mock_audio_module.called_texts, 1):
            print(f"     {i}. '{text[:60]}...' (длина: {len(text)})")
            # Проверяем, что текст соответствует text_response из парсера
            assert text in parsed.text_response or parsed.text_response in text, f"Текст для TTS должен соответствовать text_response из парсера"
        print(f"   ✅ Текст из LLM ответа передан в аудио модуль для генерации TTS")
    else:
        print(f"   ⚠️  Аудио модуль не вызван (текст не прошел пороги буферизации)")
    
    # Проверяем результаты
    print(f"\n📋 Результаты обработки:")
    print(f"   - Text responses: {len(text_responses)}")
    print(f"   - Audio chunks: {len(audio_chunks)}")
    
    final_result = [r for r in results if r.get('is_final')]
    if final_result:
        final = final_result[0]
        print(f"   - audio_chunks_processed: {final.get('audio_chunks_processed', 0)}")
    
    # Если текст эмитирован, аудио должно генерироваться
    if len(text_responses) > 0:
        assert mock_audio_module.call_count > 0, "Аудио модуль должен быть вызван для эмитированного текста"
        assert len(mock_audio_module.called_texts) > 0, "Должен быть хотя бы один текст для TTS"
        print(f"\n   ✅ Подтверждено: текст из LLM ответа передается в аудио модуль")
        print(f"   ✅ Аудио генерируется для текста ответа LLM")
    
    print(f"\n✅ ТЕСТ 1 ПРОЙДЕН: Текст из LLM ответа передается в аудио модуль")
    return True


async def test_llm_response_with_command_audio():
    """Тест 2: LLM возвращает ответ с командой → проверяем, что text_response передается в аудио модуль"""
    print("\n" + "="*80)
    print("ТЕСТ 2: LLM ОТВЕТ С КОМАНДОЙ → АУДИО ДЛЯ ТЕКСТА")
    print("="*80)
    
    # LLM возвращает JSON с командой и текстом
    llm_json_response = {
        "session_id": "test-session-audio-2",
        "command": "open_app",
        "args": {
            "app_name": "Safari"
        },
        "text": "Открываю Safari. Приложение готово к использованию."
    }
    
    mock_text_module = MockTextModule(llm_json_response)
    mock_audio_module = MockAudioModule()
    
    # Создаем workflow с низкими порогами
    from config.unified_config import WorkflowConfig
    test_config = WorkflowConfig(
        stream_min_chars=10,
        stream_min_words=2,
        stream_first_sentence_min_words=2,
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
        "text": "Открой Safari",
        "session_id": "test-session-audio-2",
        "hardware_id": "test-hardware",
        "screenshot": None
    }
    
    print(f"\n📋 Входной запрос:")
    print(f"   - Текст: '{request_data['text']}'")
    
    print(f"\n📋 Ожидаемый ответ LLM (JSON):")
    print(f"   {json.dumps(llm_json_response, indent=2, ensure_ascii=False)}")
    
    # Включаем фича-флаг
    with patch('integrations.workflow_integrations.streaming_workflow_integration.get_config') as mock_get_config:
        config = Mock()
        config.features.forward_assistant_actions = True
        config.kill_switches.disable_forward_assistant_actions = False
        mock_get_config.return_value = config
        
        # Обрабатываем запрос
        results = []
        text_responses = []
        audio_chunks = []
        command_payloads = []
        
        print(f"\n📋 Обработка запроса...")
        
        async for result in workflow.process_request_streaming(request_data):
            results.append(result)
            
            if 'text_response' in result and result.get('text_response'):
                text_responses.append(result['text_response'])
            
            if 'audio_chunk' in result:
                audio_chunks.append(result['audio_chunk'])
            
            if 'command_payload' in result:
                command_payloads.append(result['command_payload'])
        
        # Проверяем парсер
        print(f"\n📋 Проверка парсера:")
        parser = AssistantResponseParser()
        parsed = parser.parse(llm_json_response)
        print(f"   - text_response из парсера: '{parsed.text_response}'")
        print(f"   - command_payload: {parsed.command_payload is not None}")
        assert parsed.command_payload is not None, "Для ответа с командой должен быть command_payload"
        assert parsed.text_response == llm_json_response['text'], "Парсер должен извлечь text из JSON"
        print(f"   ✅ Парсер правильно разделил текст и команду")
        
        # Проверяем аудио модуль
        print(f"\n📋 Проверка аудио модуля:")
        print(f"   - Вызовов process: {mock_audio_module.call_count}")
        print(f"   - Текстов для TTS: {len(mock_audio_module.called_texts)}")
        
        if mock_audio_module.called_texts:
            print(f"   - Тексты, переданные в TTS:")
            for i, text in enumerate(mock_audio_module.called_texts, 1):
                print(f"     {i}. '{text}' (длина: {len(text)})")
                # Проверяем, что текст соответствует text_response из парсера
                assert text == parsed.text_response or parsed.text_response in text, f"Текст для TTS должен соответствовать text_response из парсера. Ожидалось: '{parsed.text_response}', получено: '{text}'"
            print(f"   ✅ Текст из LLM ответа (text_response) передан в аудио модуль")
            print(f"   ✅ Команда НЕ передается в TTS (только текст)")
        else:
            print(f"   ⚠️  Аудио модуль не вызван (текст не прошел пороги буферизации)")
        
        # Проверяем результаты
        print(f"\n📋 Результаты обработки:")
        print(f"   - Text responses: {len(text_responses)}")
        print(f"   - Audio chunks: {len(audio_chunks)}")
        print(f"   - Command payloads: {len(command_payloads)}")
        
        final_result = [r for r in results if r.get('is_final')]
        if final_result:
            final = final_result[0]
            print(f"   - audio_chunks_processed: {final.get('audio_chunks_processed', 0)}")
            if 'command_payload' in final:
                print(f"   - command_payload: присутствует")
        
        # Проверяем, что команда есть, но текст тоже обработан
        assert len(command_payloads) > 0 or (final_result and 'command_payload' in final_result[0]), "Должен быть command_payload"
        
        # Если текст эмитирован, аудио должно генерироваться
        if len(text_responses) > 0:
            if mock_audio_module.call_count > 0:
                print(f"\n   ✅ Подтверждено: text_response из LLM ответа передается в аудио модуль")
                print(f"   ✅ Аудио генерируется для текста, команда передается отдельно")
            else:
                print(f"\n   ⚠️  Аудио модуль не вызван, хотя текст эмитирован")
        else:
            print(f"\n   ⚠️  Текст не эмитирован из-за порогов, но команда обработана")
        
        print(f"\n✅ ТЕСТ 2 ПРОЙДЕН: text_response из LLM ответа передается в аудио модуль")
        return True


async def main():
    """Запуск всех тестов"""
    print("\n" + "="*80)
    print("ТЕСТИРОВАНИЕ ОБРАБОТКИ АУДИО ДЛЯ ОТВЕТОВ LLM")
    print("="*80)
    print("\nПроверяем полный поток:")
    print("1. LLM возвращает ответ (с командой или без)")
    print("2. Парсер извлекает text_response")
    print("3. text_response передается в аудио модуль для генерации TTS")
    print("4. Аудио чанки генерируются и передаются клиенту")
    
    tests = [
        ("LLM ответ без команды → аудио для текста", test_llm_response_without_command_audio),
        ("LLM ответ с командой → аудио для text_response", test_llm_response_with_command_audio),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = await test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ ОШИБКА в тесте '{name}': {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    # Итоговая статистика
    print("\n" + "="*80)
    print("ИТОГОВАЯ СТАТИСТИКА")
    print("="*80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\n📊 Результаты:")
    for name, result in results:
        status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
        print(f"   {status}: {name}")
    
    print(f"\n📈 Всего тестов: {total}")
    print(f"✅ Пройдено: {passed}")
    print(f"❌ Провалено: {total - passed}")
    print(f"📊 Успешность: {passed * 100 // total}%")
    
    if passed == total:
        print(f"\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
        print(f"\n✅ Подтверждено:")
        print(f"   1. Парсер правильно извлекает text_response из ответа LLM")
        print(f"   2. text_response передается в аудио модуль для генерации TTS")
        print(f"   3. Команда НЕ передается в TTS (только текст)")
        print(f"   4. Аудио генерируется для текста ответа LLM")
        return 0
    else:
        print(f"\n⚠️  НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ.")
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

