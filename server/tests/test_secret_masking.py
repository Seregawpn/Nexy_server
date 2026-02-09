"""
Негативные тесты для маскирования секретов (PR-7)
Проверяет edge-кейсы: не маскируются значения, похожие на токены, внутри JSON строк
"""

import pytest
import json
from utils.logging_formatter import StructuredFormatter
from logging import LogRecord


class TestSecretMasking:
    """Тесты маскирования секретов"""
    
    @pytest.fixture
    def formatter(self):
        """Создание форматтера"""
        return StructuredFormatter()
    
    def test_api_key_masking(self, formatter):
        """Тест маскирования API ключа"""
        record = LogRecord(
            name="test",
            level=20,
            pathname="test.py",
            lineno=1,
            msg="API key: sk_live_1234567890abcdef",
            args=(),
            exc_info=None
        )
        
        formatted = formatter.format(record)
        
        # Проверяем, что ключ замаскирован
        assert "****" in formatted or "api_key" in formatted.lower()
        assert "sk_live_1234567890abcdef" not in formatted
    
    def test_token_in_json_string(self, formatter):
        """Тест маскирования токена в JSON строке"""
        # Создаем JSON строку с токеном
        json_data = {
            "api_key": "sk_live_1234567890abcdef",
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            "password": "secret123"
        }
        
        record = LogRecord(
            name="test",
            level=20,
            pathname="test.py",
            lineno=1,
            msg="Request data",
            args=(),
            exc_info=None
        )
        record.ctx = json_data
        
        formatted = formatter.format(record)
        
        # Проверяем, что секреты замаскированы
        assert "sk_live_1234567890abcdef" not in formatted
        assert "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" not in formatted
        assert "secret123" not in formatted
        assert "****" in formatted
    
    def test_no_mask_short_values(self, formatter):
        """Тест, что короткие значения не маскируются"""
        json_data = {
            "api_key": "short",  # < 10 символов
            "token": "abc123"  # < 10 символов
        }
        
        record = LogRecord(
            name="test",
            level=20,
            pathname="test.py",
            lineno=1,
            msg="Request data",
            args=(),
            exc_info=None
        )
        record.ctx = json_data
        
        formatted = formatter.format(record)
        
        # Короткие значения не должны маскироваться
        # (так как условие len(value) > 10)
        assert "short" in formatted or "abc123" in formatted
    
    def test_no_mask_non_secret_keys(self, formatter):
        """Тест, что несекретные ключи не маскируются"""
        json_data = {
            "user_id": "1234567890",
            "session_id": "abcdef123456",
            "message": "Hello world"
        }
        
        record = LogRecord(
            name="test",
            level=20,
            pathname="test.py",
            lineno=1,
            msg="Request data",
            args=(),
            exc_info=None
        )
        record.ctx = json_data
        
        formatted = formatter.format(record)
        
        # Несекретные ключи не должны маскироваться
        assert "1234567890" in formatted
        assert "abcdef123456" in formatted
        assert "Hello world" in formatted

    def test_no_mask_key_substring_words(self, formatter):
        """Тест, что слова с подстрокой key не маскируются"""
        json_data = {
            "keyboard": "value123",
            "monkey": "banana456"
        }
        
        record = LogRecord(
            name="test",
            level=20,
            pathname="test.py",
            lineno=1,
            msg="Request data",
            args=(),
            exc_info=None
        )
        record.ctx = json_data
        
        formatted = formatter.format(record)
        
        assert "value123" in formatted
        assert "banana456" in formatted
    
    def test_nested_dict_masking(self, formatter):
        """Тест маскирования вложенных словарей"""
        json_data = {
            "request": {
                "headers": {
                    "Authorization": "Bearer sk_live_1234567890abcdef",
                    "X-API-Key": "api_key_1234567890"
                },
                "body": {
                    "password": "secret123456"
                }
            }
        }
        
        record = LogRecord(
            name="test",
            level=20,
            pathname="test.py",
            lineno=1,
            msg="Request data",
            args=(),
            exc_info=None
        )
        record.ctx = json_data
        
        formatted = formatter.format(record)
        
        # Проверяем, что секреты замаскированы даже во вложенных словарях
        assert "sk_live_1234567890abcdef" not in formatted
        assert "api_key_1234567890" not in formatted
        assert "secret123456" not in formatted
        assert "****" in formatted
    
    def test_exception_masking(self, formatter):
        """Тест маскирования секретов в исключениях"""
        class TestException(Exception):
            pass
        
        try:
            raise TestException("API key: sk_live_1234567890abcdef")
        except TestException:
            import sys
            record = LogRecord(
                name="test",
                level=40,
                pathname="test.py",
                lineno=1,
                msg="Error occurred",
                args=(),
                exc_info=sys.exc_info()
            )
            
            formatted = formatter.format(record)
            
            # Проверяем, что секрет замаскирован в исключении
            assert "sk_live_1234567890abcdef" not in formatted
            assert "****" in formatted or "api_key" in formatted.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
