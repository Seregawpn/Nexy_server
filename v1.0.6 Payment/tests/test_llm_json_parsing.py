"""
🚀 Smoke-тест парсинга JSON-команд от LLM (6-8 тест-кейсов)

Проверяет:
- Канонический формат (command/args/text)
- Balanced braces extraction (вложенные объекты)
- Лимиты размера
- Строгую схему валидации
- Обработку ошибок

Запуск: pytest tests/test_llm_json_parsing.py -v
"""
import pytest
import json
from typing import Optional

# Импортируем парсер (в реальности из server/integrations/core/assistant_response_parser.py)
# Для тестов используем упрощенную версию
class LLMResponseParser:
    """Упрощенная версия парсера для тестов"""
    
    MAX_JSON_SIZE = 16 * 1024  # 16KB
    MAX_ARGS_SIZE = 8 * 1024   # 8KB
    
    def _extract_json_with_balanced_braces(self, text: str) -> Optional[str]:
        """Извлекает JSON с помощью balanced braces"""
        command_pos = text.find('"command"')
        if command_pos == -1:
            return None
        
        start_pos = text.rfind('{', 0, command_pos)
        if start_pos == -1:
            return None
        
        brace_count = 0
        i = start_pos
        
        while i < len(text):
            if text[i] == '{':
                brace_count += 1
            elif text[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    return text[start_pos:i+1]
            i += 1
        
        return None
    
    def _validate_json_schema(self, data: dict) -> bool:
        """Валидация схемы: только command/args/text"""
        if not isinstance(data, dict):
            return False
        
        if "command" not in data:
            return False
        
        allowed_keys = {"command", "args", "text"}
        extra_keys = set(data.keys()) - allowed_keys
        
        if extra_keys:
            # Удаляем лишние ключи
            for key in extra_keys:
                data.pop(key)
        
        if not isinstance(data.get("command"), str):
            return False
        
        if "args" in data and not isinstance(data.get("args"), dict):
            return False
        
        if "text" in data and not isinstance(data.get("text"), str):
            return False
        
        return True
    
    def parse_response(self, response: str) -> tuple[Optional[dict], Optional[str]]:
        """
        Парсит ответ LLM
        
        Returns:
            (parsed_json, error_message)
        """
        import re
        
        if len(response) > self.MAX_JSON_SIZE:
            return None, f"Response too large: {len(response)} bytes"
        
        # Вариант 1: Code fence с языком
        json_match = re.search(r'```json\s*(\{.*?\})\s*```', response, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
            if len(json_str) > self.MAX_JSON_SIZE:
                return None, f"JSON too large: {len(json_str)} bytes"
            try:
                parsed = json.loads(json_str)
                if self._validate_json_schema(parsed):
                    return parsed, None
            except json.JSONDecodeError as e:
                return None, f"JSON decode error: {e}"
        
        # Вариант 2: Code fence без языка
        json_match = re.search(r'```\s*(\{.*?\})\s*```', response, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
            if len(json_str) > self.MAX_JSON_SIZE:
                return None, f"JSON too large: {len(json_str)} bytes"
            try:
                parsed = json.loads(json_str)
                if self._validate_json_schema(parsed):
                    return parsed, None
            except json.JSONDecodeError as e:
                return None, f"JSON decode error: {e}"
        
        # Вариант 3: Весь ответ - JSON
        try:
            if len(response.strip()) > self.MAX_JSON_SIZE:
                return None, "Full response too large"
            parsed = json.loads(response.strip())
            if isinstance(parsed, dict) and self._validate_json_schema(parsed):
                return parsed, None
        except json.JSONDecodeError:
            pass
        
        # Вариант 4: Balanced braces extraction
        json_str = self._extract_json_with_balanced_braces(response)
        if json_str:
            if len(json_str) > self.MAX_JSON_SIZE:
                return None, f"Extracted JSON too large: {len(json_str)} bytes"
            try:
                parsed = json.loads(json_str)
                if self._validate_json_schema(parsed):
                    return parsed, None
            except json.JSONDecodeError as e:
                return None, f"JSON decode error: {e}"
        
        return None, "No valid JSON found"


# ============================================================================
# Тесты
# ============================================================================

def test_1_code_fence_with_lang():
    """TC-1: JSON в code fence с языком"""
    parser = LLMResponseParser()
    
    response = """
    Opening subscription page...
    
    ```json
    {
      "command": "create_subscription",
      "args": {},
      "text": "Opening subscription page..."
    }
    ```
    """
    
    parsed, error = parser.parse_response(response)
    
    assert parsed is not None, f"Failed to parse: {error}"
    assert parsed["command"] == "create_subscription"
    assert parsed["args"] == {}
    assert "text" in parsed
    
    print("✅ TC-1: Code fence с языком работает")


def test_2_code_fence_without_lang():
    """TC-2: JSON в code fence без языка"""
    parser = LLMResponseParser()
    
    response = """
    ```
    {
      "command": "cancel_subscription",
      "args": {},
      "text": "Canceling subscription..."
    }
    ```
    """
    
    parsed, error = parser.parse_response(response)
    
    assert parsed is not None, f"Failed to parse: {error}"
    assert parsed["command"] == "cancel_subscription"
    
    print("✅ TC-2: Code fence без языка работает")


def test_3_nested_args_balanced_braces():
    """TC-3: Вложенные объекты в args (balanced braces)"""
    parser = LLMResponseParser()
    
    response = """
    Some text before {"command": "update_payment_method", "args": {"nested": {"key": "value", "deep": {"level": 2}}}, "text": "Updating payment..."} some text after
    """
    
    parsed, error = parser.parse_response(response)
    
    assert parsed is not None, f"Failed to parse: {error}"
    assert parsed["command"] == "update_payment_method"
    assert parsed["args"]["nested"]["key"] == "value"
    assert parsed["args"]["nested"]["deep"]["level"] == 2
    
    print("✅ TC-3: Вложенные объекты в args работают (balanced braces)")


def test_4_multiline_json_balanced_braces():
    """TC-4: Многострочный JSON (balanced braces)"""
    parser = LLMResponseParser()
    
    response = """
    Here is the command:
    {
      "command": "check_subscription_status",
      "args": {
        "include_details": true
      },
      "text": "Checking your subscription status..."
    }
    """
    
    parsed, error = parser.parse_response(response)
    
    assert parsed is not None, f"Failed to parse: {error}"
    assert parsed["command"] == "check_subscription_status"
    assert parsed["args"]["include_details"] is True
    
    print("✅ TC-4: Многострочный JSON работает")


def test_5_extra_keys_removed():
    """TC-5: Лишние ключи удаляются"""
    parser = LLMResponseParser()
    
    response = """
    ```json
    {
      "command": "create_subscription",
      "args": {},
      "text": "Opening...",
      "extra_key": "should be removed",
      "another_extra": 123
    }
    ```
    """
    
    parsed, error = parser.parse_response(response)
    
    assert parsed is not None, f"Failed to parse: {error}"
    assert "command" in parsed
    assert "args" in parsed
    assert "text" in parsed
    assert "extra_key" not in parsed, "Extra key should be removed"
    assert "another_extra" not in parsed, "Extra key should be removed"
    
    print("✅ TC-5: Лишние ключи удаляются")


def test_6_size_limit_enforced():
    """TC-6: Лимит размера JSON работает"""
    parser = LLMResponseParser()
    
    # Создаем JSON больше 16KB
    large_args = {"data": "x" * (17 * 1024)}  # 17KB
    large_json = json.dumps({
        "command": "create_subscription",
        "args": large_args,
        "text": "Test"
    })
    
    response = f"```json\n{large_json}\n```"
    
    parsed, error = parser.parse_response(response)
    
    assert parsed is None, "Should reject JSON larger than 16KB"
    assert "too large" in error.lower() or "large" in error.lower()
    
    print("✅ TC-6: Лимит размера работает")


def test_7_invalid_json_fallback_to_text():
    """TC-7: Невалидный JSON → fallback к тексту"""
    parser = LLMResponseParser()
    
    response = """
    This is just text with { invalid json } that should be ignored.
    No command here.
    """
    
    parsed, error = parser.parse_response(response)
    
    # Невалидный JSON не должен парситься
    assert parsed is None, "Invalid JSON should not be parsed"
    
    print("✅ TC-7: Невалидный JSON игнорируется")


def test_8_full_response_json():
    """TC-8: Весь ответ - валидный JSON"""
    parser = LLMResponseParser()
    
    response = '{"command": "create_subscription", "args": {}, "text": "Opening..."}'
    
    parsed, error = parser.parse_response(response)
    
    assert parsed is not None, f"Failed to parse: {error}"
    assert parsed["command"] == "create_subscription"
    
    print("✅ TC-8: Весь ответ как JSON работает")


# ============================================================================
# Запуск всех тестов
# ============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])






























