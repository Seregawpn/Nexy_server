#!/usr/bin/env python3
"""
Тестирование серверной части MCP команд

Проверяет:
1. Парсинг ответов LLM через AssistantResponseParser
2. Формирование command_payload
3. Формат передачи через gRPC (__MCP__ префикс)
4. Проверка feature flag
"""

import sys
import os
import json
import logging
from pathlib import Path

# Добавляем путь к серверу
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(server_root))

from integrations.core.assistant_response_parser import AssistantResponseParser, ParsedResponse
from config.unified_config import get_config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def test_parser_basic():
    """Тест 1: Базовый парсинг action-ответа"""
    print("\n" + "="*80)
    print("ТЕСТ 1: Базовый парсинг action-ответа")
    print("="*80)
    
    parser = AssistantResponseParser()
    
    response = {
        "session_id": "test-session-123",
        "command": "open_app",
        "args": {
            "app_name": "Safari"
        },
        "text": "Открываю Safari"
    }
    
    result = parser.parse(response)
    
    print(f"\n📋 Входные данные:")
    print(f"   {json.dumps(response, indent=2, ensure_ascii=False)}")
    
    print(f"\n📋 Результат парсинга:")
    print(f"   - text_response: '{result.text_response}'")
    print(f"   - session_id: {result.session_id}")
    print(f"   - command_payload: {result.command_payload is not None}")
    
    if result.command_payload:
        print(f"\n📋 command_payload:")
        print(f"   {json.dumps(result.command_payload, indent=2, ensure_ascii=False)}")
        
        # Проверки
        assert result.command_payload['event'] == 'mcp.command_request', "Неправильный event"
        assert result.command_payload['payload']['command'] == 'open_app', "Неправильный command"
        assert result.command_payload['payload']['args']['app_name'] == 'Safari', "Неправильный app_name"
        assert result.text_response == "Открываю Safari", "Неправильный text_response"
        
        print(f"\n✅ ТЕСТ 1 ПРОЙДЕН: Парсинг работает корректно")
        return True
    else:
        print(f"\n❌ ТЕСТ 1 ПРОВАЛЕН: command_payload отсутствует")
        return False


def test_parser_without_text():
    """Тест 2: Action-ответ без text"""
    print("\n" + "="*80)
    print("ТЕСТ 2: Action-ответ без text")
    print("="*80)
    
    parser = AssistantResponseParser()
    
    response = {
        "session_id": "test-session-456",
        "command": "open_app",
        "args": {
            "app_name": "Calculator"
        }
        # text отсутствует
    }
    
    result = parser.parse(response)
    
    print(f"\n📋 Входные данные:")
    print(f"   {json.dumps(response, indent=2, ensure_ascii=False)}")
    
    print(f"\n📋 Результат парсинга:")
    print(f"   - text_response: '{result.text_response}' (должна быть пустая строка)")
    print(f"   - command_payload: {result.command_payload is not None}")
    
    if result.command_payload:
        assert result.text_response == '', "text_response должна быть пустой строкой"
        assert result.command_payload['payload']['command'] == 'open_app', "Неправильный command"
        
        print(f"\n✅ ТЕСТ 2 ПРОЙДЕН: Парсинг без text работает корректно")
        return True
    else:
        print(f"\n❌ ТЕСТ 2 ПРОВАЛЕН: command_payload отсутствует")
        return False


def test_parser_plain_text():
    """Тест 3: Обычный текстовый ответ (без команды)"""
    print("\n" + "="*80)
    print("ТЕСТ 3: Обычный текстовый ответ (без команды)")
    print("="*80)
    
    parser = AssistantResponseParser()
    
    response = {
        "session_id": "test-session-789",
        "text": "Привет, как дела?"
        # command отсутствует
    }
    
    result = parser.parse(response)
    
    print(f"\n📋 Входные данные:")
    print(f"   {json.dumps(response, indent=2, ensure_ascii=False)}")
    
    print(f"\n📋 Результат парсинга:")
    print(f"   - text_response: '{result.text_response}'")
    print(f"   - command_payload: {result.command_payload}")
    
    assert result.text_response == "Привет, как дела?", "Неправильный text_response"
    assert result.command_payload is None, "command_payload должен быть None для обычного текста"
    
    print(f"\n✅ ТЕСТ 3 ПРОЙДЕН: Обычный текст обрабатывается корректно")
    return True


def test_parser_validation_errors():
    """Тест 4: Валидация ошибок (отсутствует app_name)"""
    print("\n" + "="*80)
    print("ТЕСТ 4: Валидация ошибок (отсутствует app_name)")
    print("="*80)
    
    parser = AssistantResponseParser()
    
    response = {
        "session_id": "test-session-999",
        "command": "open_app",
        "args": {
            # app_name отсутствует
        },
        "text": "Открываю приложение"
    }
    
    result = parser.parse(response)
    
    print(f"\n📋 Входные данные:")
    print(f"   {json.dumps(response, indent=2, ensure_ascii=False)}")
    
    print(f"\n📋 Результат парсинга:")
    print(f"   - text_response: '{result.text_response}'")
    print(f"   - command_payload: {result.command_payload}")
    
    # При ошибке валидации command_payload должен быть None, но text_response должен остаться
    assert result.text_response == "Открываю приложение", "text_response должен остаться"
    assert result.command_payload is None, "command_payload должен быть None при ошибке валидации"
    
    print(f"\n✅ ТЕСТ 4 ПРОЙДЕН: Валидация ошибок работает корректно")
    return True


def test_mcp_format_generation():
    """Тест 5: Формирование формата для передачи через gRPC"""
    print("\n" + "="*80)
    print("ТЕСТ 5: Формирование формата для передачи через gRPC")
    print("="*80)
    
    parser = AssistantResponseParser()
    
    response = {
        "session_id": "test-session-grpc",
        "command": "open_app",
        "args": {
            "app_name": "Telegram"
        },
        "text": "Открываю Telegram"
    }
    
    result = parser.parse(response)
    
    if not result.command_payload:
        print(f"\n❌ ТЕСТ 5 ПРОВАЛЕН: command_payload отсутствует")
        return False
    
    # Формируем формат для gRPC (как в grpc_server.py)
    mcp_json = json.dumps(result.command_payload, ensure_ascii=False)
    mcp_text_chunk = f"__MCP__{mcp_json}"
    
    print(f"\n📋 command_payload:")
    print(f"   {json.dumps(result.command_payload, indent=2, ensure_ascii=False)}")
    
    print(f"\n📋 Формат для gRPC:")
    print(f"   - Длина JSON: {len(mcp_json)}")
    print(f"   - Длина с префиксом: {len(mcp_text_chunk)}")
    print(f"   - Префикс: __MCP__")
    print(f"   - Начинается с __MCP__: {mcp_text_chunk.startswith('__MCP__')}")
    
    # Проверяем формат
    assert mcp_text_chunk.startswith('__MCP__'), "Должен начинаться с префикса __MCP__"
    
    # Извлекаем JSON обратно
    extracted_json = mcp_text_chunk[7:]  # Убираем префикс __MCP__
    parsed = json.loads(extracted_json)
    
    print(f"\n📋 Извлечённый JSON:")
    print(f"   {json.dumps(parsed, indent=2, ensure_ascii=False)}")
    
    assert parsed['event'] == 'mcp.command_request', "Неправильный event"
    assert parsed['payload']['command'] == 'open_app', "Неправильный command"
    assert parsed['payload']['args']['app_name'] == 'Telegram', "Неправильный app_name"
    
    print(f"\n✅ ТЕСТ 5 ПРОЙДЕН: Формат для gRPC корректен")
    return True


def test_feature_flag():
    """Тест 6: Проверка feature flag"""
    print("\n" + "="*80)
    print("ТЕСТ 6: Проверка feature flag")
    print("="*80)
    
    try:
        config = get_config()
        
        # Проверяем наличие feature flag
        forward_assistant_actions = getattr(config, 'forward_assistant_actions', None)
        disable_forward_assistant_actions = getattr(config, 'disable_forward_assistant_actions', None)
        
        print(f"\n📋 Конфигурация:")
        print(f"   - forward_assistant_actions: {forward_assistant_actions}")
        print(f"   - disable_forward_assistant_actions: {disable_forward_assistant_actions}")
        
        if forward_assistant_actions is None:
            print(f"\n⚠️  ПРЕДУПРЕЖДЕНИЕ: forward_assistant_actions не найден в конфиге")
            print(f"   Это нормально, если используется значение по умолчанию (False)")
        else:
            print(f"\n✅ Feature flag найден: {forward_assistant_actions}")
        
        if disable_forward_assistant_actions is None:
            print(f"\n⚠️  ПРЕДУПРЕЖДЕНИЕ: disable_forward_assistant_actions не найден в конфиге")
            print(f"   Это нормально, если используется значение по умолчанию (False)")
        else:
            print(f"\n✅ Kill-switch найден: {disable_forward_assistant_actions}")
        
        # Проверяем логику включения
        is_enabled = forward_assistant_actions and not disable_forward_assistant_actions
        print(f"\n📋 Статус функциональности:")
        print(f"   - Включена: {is_enabled}")
        
        if not is_enabled:
            print(f"\n⚠️  Функциональность выключена (по умолчанию)")
            print(f"   Для включения установите forward_assistant_actions=true в конфиге")
        
        print(f"\n✅ ТЕСТ 6 ПРОЙДЕН: Feature flag проверен")
        return True
        
    except Exception as e:
        print(f"\n❌ ТЕСТ 6 ПРОВАЛЕН: Ошибка при проверке конфигурации: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_json_string_input():
    """Тест 7: Парсинг JSON строки (вместо словаря)"""
    print("\n" + "="*80)
    print("ТЕСТ 7: Парсинг JSON строки (вместо словаря)")
    print("="*80)
    
    parser = AssistantResponseParser()
    
    response_str = json.dumps({
        "session_id": "test-session-string",
        "command": "open_app",
        "args": {
            "app_name": "Notes"
        },
        "text": "Открываю Notes"
    })
    
    result = parser.parse(response_str)
    
    print(f"\n📋 Входные данные (строка):")
    print(f"   {response_str}")
    
    print(f"\n📋 Результат парсинга:")
    print(f"   - text_response: '{result.text_response}'")
    print(f"   - command_payload: {result.command_payload is not None}")
    
    if result.command_payload:
        assert result.command_payload['payload']['command'] == 'open_app', "Неправильный command"
        assert result.command_payload['payload']['args']['app_name'] == 'Notes', "Неправильный app_name"
        
        print(f"\n✅ ТЕСТ 7 ПРОЙДЕН: Парсинг JSON строки работает корректно")
        return True
    else:
        print(f"\n❌ ТЕСТ 7 ПРОВАЛЕН: command_payload отсутствует")
        return False


def test_invalid_json():
    """Тест 8: Обработка невалидного JSON"""
    print("\n" + "="*80)
    print("ТЕСТ 8: Обработка невалидного JSON")
    print("="*80)
    
    parser = AssistantResponseParser()
    
    # Невалидный JSON
    response_str = "Это просто обычный текст, не JSON"
    
    result = parser.parse(response_str)
    
    print(f"\n📋 Входные данные:")
    print(f"   '{response_str}'")
    
    print(f"\n📋 Результат парсинга:")
    print(f"   - text_response: '{result.text_response}'")
    print(f"   - command_payload: {result.command_payload}")
    
    assert result.text_response == response_str, "text_response должен быть исходным текстом"
    assert result.command_payload is None, "command_payload должен быть None для невалидного JSON"
    
    print(f"\n✅ ТЕСТ 8 ПРОЙДЕН: Невалидный JSON обрабатывается корректно (fallback на текст)")
    return True


def main():
    """Запуск всех тестов"""
    print("\n" + "="*80)
    print("ТЕСТИРОВАНИЕ СЕРВЕРНОЙ ЧАСТИ MCP КОМАНД")
    print("="*80)
    print("\nПроверяем:")
    print("1. Парсинг ответов LLM через AssistantResponseParser")
    print("2. Формирование command_payload")
    print("3. Формат передачи через gRPC (__MCP__ префикс)")
    print("4. Проверка feature flag")
    print("5. Обработка граничных случаев")
    
    tests = [
        ("Базовый парсинг", test_parser_basic),
        ("Action-ответ без text", test_parser_without_text),
        ("Обычный текстовый ответ", test_parser_plain_text),
        ("Валидация ошибок", test_parser_validation_errors),
        ("Формат для gRPC", test_mcp_format_generation),
        ("Feature flag", test_feature_flag),
        ("Парсинг JSON строки", test_json_string_input),
        ("Обработка невалидного JSON", test_invalid_json),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
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
        print(f"\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! Серверная часть работает корректно.")
        print(f"\n✅ Можно приступать к реализации клиентской части.")
        return 0
    else:
        print(f"\n⚠️  НЕКОТОРЫЕ ТЕСТЫ ПРОВАЛЕНЫ. Проверьте ошибки выше.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

