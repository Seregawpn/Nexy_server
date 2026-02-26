#!/usr/bin/env python3
"""
Тестирование форматов ответов LLM согласно промпту
Проверяет, что AssistantResponseParser корректно обрабатывает все форматы
"""

import asyncio
import json
import sys
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from server.integrations.core.assistant_response_parser import (
    AssistantResponseParser,
    ParsedResponse
)

def test_text_only_response():
    """Тест 1: Обычный текстовый ответ"""
    print("\n" + "="*60)
    print("ТЕСТ 1: Обычный текстовый ответ")
    print("="*60)
    
    parser = AssistantResponseParser()
    
    # Формат 1: JSON объект
    response1 = {"text": "The Calculator app is already open. What would you like to compute?"}
    result1 = parser.parse(response1)
    
    print(f"Вход: {json.dumps(response1, ensure_ascii=False)}")
    print(f"✅ text_response: '{result1.text_response}'")
    print(f"✅ command_payload: {result1.command_payload}")
    print(f"✅ session_id: {result1.session_id}")
    assert result1.text_response == response1["text"]
    assert result1.command_payload is None
    print("✅ ТЕСТ 1 ПРОЙДЕН")
    
    # Формат 2: JSON строка
    response2 = '{"text": "Hello! How can I help you?"}'
    result2 = parser.parse(response2)
    
    print(f"\nВход (строка): {response2}")
    print(f"✅ text_response: '{result2.text_response}'")
    print(f"✅ command_payload: {result2.command_payload}")
    assert result2.text_response == "Hello! How can I help you?"
    assert result2.command_payload is None
    print("✅ ТЕСТ 1 (строка) ПРОЙДЕН")


def test_action_response_valid():
    """Тест 2: Действие с валидными данными"""
    print("\n" + "="*60)
    print("ТЕСТ 2: Действие (валидный формат)")
    print("="*60)
    
    parser = AssistantResponseParser()
    
    response = {
        "session_id": "session_123",
        "command": "open_app",
        "args": {
            "app_name": "Calculator"
        },
        "text": "Opening Calculator."
    }
    
    result = parser.parse(response)
    
    print(f"Вход: {json.dumps(response, ensure_ascii=False, indent=2)}")
    print(f"✅ text_response: '{result.text_response}'")
    print(f"✅ command_payload: {result.command_payload}")
    print(f"✅ session_id: {result.session_id}")
    
    assert result.text_response == "Opening Calculator."
    assert result.command_payload is not None
    assert result.command_payload['event'] == 'mcp.command_request'
    assert result.command_payload['payload']['command'] == 'open_app'
    assert result.command_payload['payload']['args']['app_name'] == 'Calculator'
    assert result.session_id == "session_123"
    
    print("\n📋 Структура command_payload:")
    print(json.dumps(result.command_payload, ensure_ascii=False, indent=2))
    print("✅ ТЕСТ 2 ПРОЙДЕН")


def test_action_response_missing_session_id():
    """Тест 3: Действие без session_id (должно игнорироваться)"""
    print("\n" + "="*60)
    print("ТЕСТ 3: Действие без session_id (fallback на текст)")
    print("="*60)
    
    parser = AssistantResponseParser()
    
    response = {
        "command": "open_app",
        "args": {
            "app_name": "Safari"
        },
        "text": "Opening Safari."
    }
    
    result = parser.parse(response)
    
    print(f"Вход: {json.dumps(response, ensure_ascii=False, indent=2)}")
    print(f"✅ text_response: '{result.text_response}'")
    print(f"⚠️ command_payload: {result.command_payload} (должен быть None)")
    print(f"⚠️ session_id: {result.session_id}")
    
    assert result.text_response == "Opening Safari."
    assert result.command_payload is None  # Должен быть None из-за отсутствия session_id
    print("✅ ТЕСТ 3 ПРОЙДЕН (команда игнорируется, возвращается только текст)")


def test_action_response_missing_app_name():
    """Тест 4: Действие без app_name (должно игнорироваться)"""
    print("\n" + "="*60)
    print("ТЕСТ 4: Действие без app_name (fallback на текст)")
    print("="*60)
    
    parser = AssistantResponseParser()
    
    response = {
        "session_id": "session_123",
        "command": "open_app",
        "args": {},
        "text": "I need to know which app to open."
    }
    
    result = parser.parse(response)
    
    print(f"Вход: {json.dumps(response, ensure_ascii=False, indent=2)}")
    print(f"✅ text_response: '{result.text_response}'")
    print(f"⚠️ command_payload: {result.command_payload} (должен быть None)")
    
    assert result.text_response == "I need to know which app to open."
    assert result.command_payload is None  # Должен быть None из-за отсутствия app_name
    print("✅ ТЕСТ 4 ПРОЙДЕН (команда игнорируется, возвращается только текст)")


def test_action_response_json_string():
    """Тест 5: Действие в виде JSON строки"""
    print("\n" + "="*60)
    print("ТЕСТ 5: Действие (JSON строка)")
    print("="*60)
    
    parser = AssistantResponseParser()
    
    response = '{"session_id": "session_456", "command": "open_app", "args": {"app_name": "Safari"}, "text": "Opening Safari."}'
    
    result = parser.parse(response)
    
    print(f"Вход (строка): {response}")
    print(f"✅ text_response: '{result.text_response}'")
    print(f"✅ command_payload: {result.command_payload is not None}")
    print(f"✅ session_id: {result.session_id}")
    
    assert result.text_response == "Opening Safari."
    assert result.command_payload is not None
    assert result.command_payload['payload']['args']['app_name'] == 'Safari'
    assert result.session_id == "session_456"
    print("✅ ТЕСТ 5 ПРОЙДЕН")


def test_empty_text():
    """Тест 6: Действие с пустым text"""
    print("\n" + "="*60)
    print("ТЕСТ 6: Действие с пустым text")
    print("="*60)
    
    parser = AssistantResponseParser()
    
    response = {
        "session_id": "session_123",
        "command": "open_app",
        "args": {
            "app_name": "Calculator"
        },
        "text": ""
    }
    
    result = parser.parse(response)
    
    print(f"Вход: {json.dumps(response, ensure_ascii=False, indent=2)}")
    print(f"✅ text_response: '{result.text_response}' (пустая строка)")
    print(f"✅ command_payload: {result.command_payload is not None}")
    
    assert result.text_response == ""
    assert result.command_payload is not None
    print("✅ ТЕСТ 6 ПРОЙДЕН")


def test_plain_string():
    """Тест 7: Обычная строка (не JSON)"""
    print("\n" + "="*60)
    print("ТЕСТ 7: Обычная строка (не JSON)")
    print("="*60)
    
    parser = AssistantResponseParser()
    
    response = "Hello! How can I help you?"
    
    result = parser.parse(response)
    
    print(f"Вход: {response}")
    print(f"✅ text_response: '{result.text_response}'")
    print(f"✅ command_payload: {result.command_payload}")
    
    assert result.text_response == "Hello! How can I help you?"
    assert result.command_payload is None
    print("✅ ТЕСТ 7 ПРОЙДЕН")


def run_all_tests():
    """Запуск всех тестов"""
    print("\n" + "="*60)
    print("🧪 ТЕСТИРОВАНИЕ ФОРМАТОВ ОТВЕТОВ LLM")
    print("="*60)
    
    try:
        test_text_only_response()
        test_action_response_valid()
        test_action_response_missing_session_id()
        test_action_response_missing_app_name()
        test_action_response_json_string()
        test_empty_text()
        test_plain_string()
        
        print("\n" + "="*60)
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
        print("="*60)
        print("\n📋 Выводы:")
        print("1. ✅ Формат текстового ответа: {\"text\": \"...\"}")
        print("2. ✅ Формат действия: {\"session_id\": \"...\", \"command\": \"open_app\", \"args\": {\"app_name\": \"...\"}, \"text\": \"...\"}")
        print("3. ✅ Парсер корректно обрабатывает оба формата")
        print("4. ✅ Валидация работает: отсутствие session_id или app_name → команда игнорируется")
        print("5. ✅ Поддерживаются JSON объекты, JSON строки и обычные строки")
        
    except AssertionError as e:
        print(f"\n❌ ТЕСТ ПРОВАЛЕН: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()

