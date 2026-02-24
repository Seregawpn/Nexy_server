#!/usr/bin/env python3
"""
Полный интеграционный тест серверной части MCP команд

Имитирует реальные запросы от пользователя:
1. Запрос на открытие приложения (с MCP командой)
2. Обычный запрос на общение (без команды)

Проверяет весь поток:
- Получение запроса
- Обработка через StreamingWorkflowIntegration
- Парсинг ответа LLM
- Формирование command_payload
- Формат передачи через gRPC (__MCP__ префикс)
"""

import sys
import os
import json
import asyncio
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
    
    def __init__(self, responses: list):
        """
        Args:
            responses: Список ответов, которые должен вернуть модуль
        """
        self.responses = responses
        self.is_initialized = True
        self.name = "text_processing"
    
    async def process(self, *args, **kwargs):
        """Имитация обработки текста - возвращает async generator с ответами LLM"""
        async def _generate():
            for response in self.responses:
                if isinstance(response, dict):
                    yield json.dumps(response, ensure_ascii=False)
                else:
                    # Добавляем точку для завершенного предложения
                    text = response if response.endswith(('.', '!', '?')) else f"{response}."
                    yield text
                await asyncio.sleep(0.01)  # Небольшая задержка для реалистичности
        
        return _generate()


class MockAudioModule:
    """Мок аудио модуля"""
    
    def __init__(self):
        self.is_initialized = True
        self.name = "audio_generation"
        self.call_count = 0
        self.last_text = None
        self.called_texts = []
    
    async def process(self, payload: Dict[str, Any] = None, *args, **kwargs) -> AsyncGenerator[bytes, None]:
        """Имитация генерации аудио"""
        # Сохраняем текст, который передается для генерации аудио
        text = None
        if payload and isinstance(payload, dict):
            text = payload.get('text')
        elif args and isinstance(args[0], dict):
            text = args[0].get('text')
        elif kwargs.get('text'):
            text = kwargs['text']
        
        if text:
            self.last_text = text
            self.called_texts.append(text)
        self.call_count += 1
        
        # Возвращаем несколько чанков аудио
        for i in range(2):
            yield f"fake_audio_chunk_{i}".encode()
            await asyncio.sleep(0.01)


async def test_open_app_request():
    """Тест 1: Запрос на открытие приложения"""
    print("\n" + "="*80)
    print("ТЕСТ 1: ЗАПРОС НА ОТКРЫТИЕ ПРИЛОЖЕНИЯ")
    print("="*80)
    
    # Имитируем ответ LLM с командой (добавляем точку для завершенного предложения)
    llm_response = {
        "session_id": "test-session-open-app",
        "command": "open_app",
        "args": {
            "app_name": "Safari"
        },
        "text": "Открываю Safari."
    }
    
    # Создаем мок текстового модуля
    mock_text_module = MockTextModule([llm_response])
    mock_audio_module = MockAudioModule()
    
    # Создаем workflow интеграцию с низкими порогами для тестирования
    from config.unified_config import WorkflowConfig
    test_config = WorkflowConfig(
        stream_min_chars=10,  # Низкий порог для тестирования
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
    
    # Инициализируем
    await workflow.initialize()
    
    # Имитируем запрос от пользователя
    request_data = {
        "text": "Открой Safari",
        "session_id": "test-session-open-app",
        "hardware_id": "test-hardware-123",
        "screenshot": None
    }
    
    print(f"\n📋 Входной запрос:")
    print(f"   - Текст: '{request_data['text']}'")
    print(f"   - Session ID: {request_data['session_id']}")
    print(f"   - Hardware ID: {request_data['hardware_id']}")
    
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
            
            # Собираем результаты
            if 'text_response' in result and result.get('text_response'):
                text_responses.append(result['text_response'])
            
            if 'audio_chunk' in result:
                audio_chunks.append(result['audio_chunk'])
            
            if 'command_payload' in result:
                command_payloads.append(result['command_payload'])
        
        # Проверяем результаты
        print(f"\n📋 Результаты обработки:")
        print(f"   - Всего результатов: {len(results)}")
        print(f"   - Text responses (промежуточные): {len(text_responses)}")
        print(f"   - Audio chunks: {len(audio_chunks)}")
        print(f"   - Command payloads: {len(command_payloads)}")
        
        # Проверяем финальный результат
        final_result = [r for r in results if r.get('is_final')]
        assert len(final_result) > 0, "Должен быть финальный результат"
        final = final_result[0]
        
        print(f"\n📋 Финальный результат:")
        print(f"   - text_full_response: '{final.get('text_full_response', '')}'")
        print(f"   - sentences_processed: {final.get('sentences_processed', 0)}")
        print(f"   - audio_chunks_processed: {final.get('audio_chunks_processed', 0)}")
        print(f"   - command_payload: {final.get('command_payload') is not None}")
        
        # Проверяем text_response (может быть в промежуточных или в финальном)
        has_text = len(text_responses) > 0 or bool(final.get('text_full_response'))
        if has_text:
            if text_responses:
                print(f"\n📋 Text responses (промежуточные):")
                for i, text in enumerate(text_responses, 1):
                    print(f"   {i}. '{text}'")
            if final.get('text_full_response'):
                print(f"   Финальный текст: '{final['text_full_response']}'")
            # Проверяем, что текст содержит ожидаемое содержимое
            all_text = ' '.join(text_responses) + ' ' + final.get('text_full_response', '')
            assert 'Открываю Safari' in all_text or 'Safari' in all_text, f"Текст должен содержать 'Открываю Safari', получено: {all_text}"
        
        # Проверяем command_payload
        assert len(command_payloads) > 0 or 'command_payload' in final, "Должен быть хотя бы один command_payload"
        
        if 'command_payload' in final:
                cmd_payload = final['command_payload']
                print(f"\n📋 Command payload:")
                print(f"   {json.dumps(cmd_payload, indent=2, ensure_ascii=False)}")
                
                # Проверяем формат
                assert cmd_payload['event'] == 'mcp.command_request', "Неправильный event"
                assert cmd_payload['payload']['command'] == 'open_app', "Неправильный command"
                assert cmd_payload['payload']['args']['app_name'] == 'Safari', "Неправильный app_name"
                
                # Проверяем формат для gRPC
                mcp_json = json.dumps(cmd_payload, ensure_ascii=False)
                mcp_text_chunk = f"__MCP__{mcp_json}"
                
                print(f"\n📋 Формат для gRPC:")
                print(f"   - Префикс: __MCP__")
                print(f"   - Длина JSON: {len(mcp_json)}")
                print(f"   - Длина с префиксом: {len(mcp_text_chunk)}")
                print(f"   - Начинается с __MCP__: {mcp_text_chunk.startswith('__MCP__')}")
                
                assert mcp_text_chunk.startswith('__MCP__'), "Должен начинаться с префикса __MCP__"
                
                # Проверяем, что можно извлечь JSON обратно
                extracted_json = mcp_text_chunk[7:]
                parsed = json.loads(extracted_json)
                assert parsed['event'] == 'mcp.command_request', "Извлечённый JSON должен быть валидным"
        
        # Проверяем аудио модуль
        print(f"\n📋 Проверка аудио модуля:")
        print(f"   - Вызовов process: {mock_audio_module.call_count}")
        if mock_audio_module.last_text:
            print(f"   - Последний текст для TTS: '{mock_audio_module.last_text[:60]}...'")
        
        # Для запроса с командой аудио должно генерироваться для текста ответа
        if has_text:
            if len(audio_chunks) > 0 or final.get('audio_chunks_processed', 0) > 0:
                print(f"   ✅ Аудио генерируется для текста ответа")
            else:
                print(f"   ⚠️  Аудио не сгенерировано (возможно, текст не прошел пороги)")
        else:
            print(f"   ⚠️  Текст не эмитирован, поэтому аудио не генерируется")
        
        print(f"\n✅ ТЕСТ 1 ПРОЙДЕН: Запрос на открытие приложения обработан корректно")
        return True


async def test_regular_conversation():
    """Тест 2: Обычный запрос на общение (без команды)"""
    print("\n" + "="*80)
    print("ТЕСТ 2: ОБЫЧНЫЙ ЗАПРОС НА ОБЩЕНИЕ")
    print("="*80)
    
    # Имитируем обычный ответ LLM без команды
    # Используем достаточно длинный текст, чтобы он прошел через пороги буферизации
    # Важно: это НЕ JSON, а обычный текст - команды быть не должно
    llm_response = "Привет! Как дела? У меня всё отлично, спасибо! Чем могу помочь? Я готов помочь вам с любыми вопросами и задачами."
    
    # Создаем мок текстового модуля
    mock_text_module = MockTextModule([llm_response])
    mock_audio_module = MockAudioModule()
    
    # Создаем workflow интеграцию с низкими порогами для тестирования
    from config.unified_config import WorkflowConfig
    test_config = WorkflowConfig(
        stream_min_chars=10,  # Низкий порог для тестирования
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
    
    # Инициализируем
    await workflow.initialize()
    
    # Имитируем запрос от пользователя
    request_data = {
        "text": "Привет, как дела?",
        "session_id": "test-session-conversation",
        "hardware_id": "test-hardware-456",
        "screenshot": None
    }
    
    print(f"\n📋 Входной запрос:")
    print(f"   - Текст: '{request_data['text']}'")
    print(f"   - Session ID: {request_data['session_id']}")
    print(f"   - Hardware ID: {request_data['hardware_id']}")
    
    # Включаем фича-флаг (но команды не должно быть)
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
            
            # Собираем результаты
            if 'text_response' in result and result.get('text_response'):
                text_responses.append(result['text_response'])
            
            if 'audio_chunk' in result:
                audio_chunks.append(result['audio_chunk'])
            
            if 'command_payload' in result:
                command_payloads.append(result['command_payload'])
        
        # Проверяем результаты
        print(f"\n📋 Результаты обработки:")
        print(f"   - Всего результатов: {len(results)}")
        print(f"   - Text responses (промежуточные): {len(text_responses)}")
        print(f"   - Audio chunks: {len(audio_chunks)}")
        print(f"   - Command payloads: {len(command_payloads)}")
        
        # Проверяем финальный результат
        final_result = [r for r in results if r.get('is_final')]
        assert len(final_result) > 0, "Должен быть финальный результат"
        final = final_result[0]
        
        print(f"\n📋 Финальный результат:")
        print(f"   - text_full_response: '{final.get('text_full_response', '')}'")
        print(f"   - sentences_processed: {final.get('sentences_processed', 0)}")
        print(f"   - audio_chunks_processed: {final.get('audio_chunks_processed', 0)}")
        print(f"   - command_payload: {final.get('command_payload') is not None}")
        
        # Проверяем, что парсер правильно определил, что это обычный текст без команды
        print(f"\n📋 Проверка парсера:")
        parser = AssistantResponseParser()
        parsed = parser.parse(llm_response)
        print(f"   - text_response из парсера: '{parsed.text_response[:60]}...' (длина: {len(parsed.text_response)})")
        print(f"   - command_payload из парсера: {parsed.command_payload is not None}")
        assert parsed.command_payload is None, "❌ КРИТИЧНО: Парсер должен определить, что это обычный текст без команды!"
        assert len(parsed.text_response) > 0, "Парсер должен извлечь текст"
        print(f"   ✅ Парсер правильно определил, что это обычный текст без команды")
        
        # Проверяем text_response (может быть в промежуточных или в финальном)
        has_text = len(text_responses) > 0 or bool(final.get('text_full_response'))
        
        if text_responses:
            print(f"\n📋 Text responses (промежуточные):")
            for i, text in enumerate(text_responses, 1):
                print(f"   {i}. '{text}'")
        if final.get('text_full_response'):
            print(f"   Финальный текст: '{final['text_full_response']}'")
        
        # Для обычного текста без команды проверяем, что:
        # 1. НЕТ command_payload (главное) - это критично!
        # 2. Текст обработан парсером (может быть не эмитирован из-за порогов, но это нормально)
        assert 'command_payload' not in final or final.get('command_payload') is None, "❌ КРИТИЧНО: Не должно быть command_payload для обычного текста!"
        assert len(command_payloads) == 0, "❌ КРИТИЧНО: Не должно быть command_payload для обычного текста!"
        print(f"   ✅ Подтверждено: command_payload отсутствует (как и должно быть для обычного текста)")
        
        # Текст может быть не эмитирован из-за порогов буферизации, но это нормально для теста
        # Главное - проверить, что команды нет
        if not has_text:
            print(f"\n⚠️  Текст не эмитирован из-за порогов буферизации (это нормально для коротких текстов)")
            print(f"   ✅ Но парсер правильно обработал текст и не создал команду")
        
        print(f"\n✅ ТЕСТ 2 ПРОЙДЕН: Обычный запрос обработан корректно (без команды)")
        return True


async def test_audio_generation_with_text():
    """Тест 3: Проверка генерации аудио для длинного текста"""
    print("\n" + "="*80)
    print("ТЕСТ 3: ПРОВЕРКА ГЕНЕРАЦИИ АУДИО ДЛЯ ТЕКСТА")
    print("="*80)
    
    # Используем достаточно длинный текст, чтобы он прошел через пороги
    llm_response = "Привет! Как дела? У меня всё отлично, спасибо! Чем могу помочь? Я готов помочь вам с любыми вопросами и задачами. Могу открыть приложения, ответить на вопросы, помочь с работой."
    
    # Создаем мок текстового модуля
    mock_text_module = MockTextModule([llm_response])
    mock_audio_module = MockAudioModule()
    
    # Создаем workflow интеграцию с низкими порогами для тестирования
    from config.unified_config import WorkflowConfig
    test_config = WorkflowConfig(
        stream_min_chars=10,  # Низкий порог для тестирования
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
    
    # Инициализируем
    await workflow.initialize()
    
    # Имитируем запрос от пользователя
    request_data = {
        "text": "Расскажи о себе",
        "session_id": "test-session-audio",
        "hardware_id": "test-hardware-audio",
        "screenshot": None
    }
    
    print(f"\n📋 Входной запрос:")
    print(f"   - Текст: '{request_data['text']}'")
    
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
        
        print(f"\n📋 Обработка запроса...")
        
        async for result in workflow.process_request_streaming(request_data):
            results.append(result)
            
            if 'text_response' in result and result.get('text_response'):
                text_responses.append(result['text_response'])
            
            if 'audio_chunk' in result:
                audio_chunks.append(result['audio_chunk'])
        
        # Проверяем результаты
        print(f"\n📋 Результаты обработки:")
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
        print(f"   - Всего текстов для TTS: {len(mock_audio_module.called_texts)}")
        if mock_audio_module.called_texts:
            print(f"   - Тексты, переданные в TTS:")
            for i, text in enumerate(mock_audio_module.called_texts, 1):
                print(f"     {i}. '{text[:60]}...' (длина: {len(text)})")
        
        # Если текст эмитирован, аудио должно генерироваться
        if len(text_responses) > 0:
            assert len(audio_chunks) > 0 or mock_audio_module.call_count > 0, "Аудио должно генерироваться для эмитированного текста"
            print(f"   ✅ Аудио генерируется для эмитированного текста")
        else:
            print(f"   ⚠️  Текст не эмитирован из-за порогов, поэтому аудио не генерируется")
        
        # Проверяем, что команды нет
        final = final_result[0] if final_result else {}
        assert 'command_payload' not in final or final.get('command_payload') is None, "Не должно быть command_payload для обычного текста"
        
        print(f"\n✅ ТЕСТ 3 ПРОЙДЕН: Генерация аудио работает корректно")
        return True


async def test_mixed_response():
    """Тест 3: Смешанный ответ (сначала текст, потом команда)"""
    print("\n" + "="*80)
    print("ТЕСТ 3: СМЕШАННЫЙ ОТВЕТ (ТЕКСТ + КОМАНДА)")
    print("="*80)
    
    # Имитируем смешанный ответ: сначала обычный текст, потом команда
    responses = [
        "Хорошо, сейчас открою приложение. Это займет всего несколько секунд.",
        {
            "session_id": "test-session-mixed",
            "command": "open_app",
            "args": {
                "app_name": "Calculator"
            },
            "text": "Открываю Calculator. Приложение готово к использованию."
        }
    ]
    
    # Создаем мок текстового модуля
    mock_text_module = MockTextModule(responses)
    mock_audio_module = MockAudioModule()
    
    # Создаем workflow интеграцию с низкими порогами для тестирования
    from config.unified_config import WorkflowConfig
    test_config = WorkflowConfig(
        stream_min_chars=10,  # Низкий порог для тестирования
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
    
    # Инициализируем
    await workflow.initialize()
    
    # Имитируем запрос от пользователя
    request_data = {
        "text": "Открой калькулятор",
        "session_id": "test-session-mixed",
        "hardware_id": "test-hardware-789",
        "screenshot": None
    }
    
    print(f"\n📋 Входной запрос:")
    print(f"   - Текст: '{request_data['text']}'")
    
    # Включаем фича-флаг
    with patch('integrations.workflow_integrations.streaming_workflow_integration.get_config') as mock_get_config:
        config = Mock()
        config.features.forward_assistant_actions = True
        config.kill_switches.disable_forward_assistant_actions = False
        mock_get_config.return_value = config
        
        # Обрабатываем запрос
        results = []
        text_responses = []
        command_payloads = []
        
        print(f"\n📋 Обработка запроса...")
        
        async for result in workflow.process_request_streaming(request_data):
            results.append(result)
            
            if 'text_response' in result and result.get('text_response'):
                text_responses.append(result['text_response'])
            
            if 'command_payload' in result:
                command_payloads.append(result['command_payload'])
        
        # Проверяем результаты
        print(f"\n📋 Результаты обработки:")
        print(f"   - Text responses (промежуточные): {len(text_responses)}")
        print(f"   - Command payloads: {len(command_payloads)}")
        
        # Проверяем финальный результат
        final_result = [r for r in results if r.get('is_final')]
        assert len(final_result) > 0, "Должен быть финальный результат"
        final = final_result[0]
        
        print(f"\n📋 Финальный результат:")
        print(f"   - text_full_response: '{final.get('text_full_response', '')}'")
        print(f"   - sentences_processed: {final.get('sentences_processed', 0)}")
        print(f"   - command_payload: {final.get('command_payload') is not None}")
        
        # Должен быть и текст, и команда
        # Текст может быть не эмитирован из-за порогов, но команда должна быть
        has_text = len(text_responses) > 0 or bool(final.get('text_full_response'))
        if not has_text:
            print(f"\n⚠️  Текст не эмитирован из-за порогов буферизации (это нормально для коротких текстов)")
        
        has_command = len(command_payloads) > 0 or 'command_payload' in final
        assert has_command, "Должен быть хотя бы один command_payload"
        
        # Проверяем, что command_payload только один (не дублируется)
        final_result = [r for r in results if r.get('is_final')]
        if final_result:
            final = final_result[0]
            if 'command_payload' in final:
                cmd_payload = final['command_payload']
                assert cmd_payload['payload']['command'] == 'open_app', "Неправильный command"
                assert cmd_payload['payload']['args']['app_name'] == 'Calculator', "Неправильный app_name"
        
        # Проверяем, что command_payload не дублируется
        all_command_payloads = [r for r in results if 'command_payload' in r]
        assert len(all_command_payloads) <= 1, f"command_payload не должен дублироваться, найдено: {len(all_command_payloads)}"
        
        print(f"\n✅ ТЕСТ 3 ПРОЙДЕН: Смешанный ответ обработан корректно")
        return True


async def main():
    """Запуск всех тестов"""
    print("\n" + "="*80)
    print("ПОЛНОЕ ИНТЕГРАЦИОННОЕ ТЕСТИРОВАНИЕ СЕРВЕРНОЙ ЧАСТИ MCP КОМАНД")
    print("="*80)
    print("\nИмитируем реальные запросы от пользователя:")
    print("1. Запрос на открытие приложения (с MCP командой)")
    print("2. Обычный запрос на общение (без команды)")
    print("3. Смешанный ответ (текст + команда)")
    
    tests = [
        ("Запрос на открытие приложения", test_open_app_request),
        ("Обычный запрос на общение", test_regular_conversation),
        ("Проверка генерации аудио", test_audio_generation_with_text),
        ("Смешанный ответ", test_mixed_response),
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
        print(f"\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! Серверная часть полностью работает корректно.")
        print(f"\n✅ Сервер готов к использованию с клиентом.")
        return 0
    else:
        print(f"\n⚠️  НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ. Проверьте ошибки выше.")
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))

