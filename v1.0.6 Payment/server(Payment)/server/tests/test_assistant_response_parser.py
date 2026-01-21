"""
Unit-тесты для AssistantResponseParser (Фаза 1)

Покрывает все сценарии из плана:
1. Action-ответ с валидными полями
2. Action-ответ без text
3. Обычный текстовый ответ (не JSON)
4. JSON без command
5. Некорректный JSON (не парсится) → fallback на обычный текст
"""

import pytest
import json
import logging
from unittest.mock import patch
from pathlib import Path
import sys

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.core.assistant_response_parser import (
    AssistantResponseParser,
    ParsedResponse
)


class TestAssistantResponseParser:
    """Тесты для AssistantResponseParser"""
    
    @pytest.fixture
    def parser(self):
        """Фикстура для парсера"""
        return AssistantResponseParser()
    
    def test_action_response_valid(self, parser):
        """Тест 1: Action-ответ с валидными полями"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": "open_app",
            "args": {
                "app_name": "Telegram"
            },
            "text": "Открываю Telegram, дайте знать, если понадобится что-то ещё."
        }
        
        result = parser.parse(response)
        
        assert isinstance(result, ParsedResponse)
        assert result.text_response == "Открываю Telegram, дайте знать, если понадобится что-то ещё."
        assert result.command_payload is not None
        assert result.command_payload['event'] == 'mcp.command_request'
        assert result.command_payload['payload']['command'] == 'open_app'
        assert result.command_payload['payload']['args']['app_name'] == 'Telegram'
        assert result.session_id == "123e4567-e89b-12d3-a456-426614174000"
    
    def test_action_response_no_text(self, parser):
        """Тест 2: Action-ответ без text"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": "open_app",
            "args": {
                "app_name": "Telegram"
            }
        }
        
        with patch.object(parser.logger, 'warning') as mock_warning:
            result = parser.parse(response)
            
            # text должен быть пустой строкой
            assert result.text_response == ''
            assert result.command_payload is not None
            assert result.command_payload['payload']['command'] == 'open_app'
    
    def test_plain_text_response(self, parser):
        """Тест 3: Обычный текстовый ответ (не JSON)"""
        response = "Это обычный текстовый ответ без JSON"
        
        result = parser.parse(response)
        
        assert result.text_response == "Это обычный текстовый ответ без JSON"
        assert result.command_payload is None
        assert result.session_id is None
    
    def test_json_without_command(self, parser):
        """Тест 4: JSON без command"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "text": "Просто текстовый ответ в формате JSON"
        }
        
        result = parser.parse(response)
        
        assert result.text_response == "Просто текстовый ответ в формате JSON"
        assert result.command_payload is None
        assert result.session_id == "123e4567-e89b-12d3-a456-426614174000"
    
    def test_invalid_json_fallback(self, parser):
        """Тест 5: Некорректный JSON (не парсится) → fallback на обычный текст"""
        response = '{"invalid": json, syntax}'
        
        with patch.object(parser.logger, 'warning') as mock_warning:
            result = parser.parse(response)
            
            # Должен вернуть исходную строку как текст
            assert result.text_response == '{"invalid": json, syntax}'
            assert result.command_payload is None
    
    def test_json_string_valid(self, parser):
        """Дополнительный тест: JSON в виде строки с валидными полями"""
        response_str = json.dumps({
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": "open_app",
            "args": {
                "app_name": "Telegram"
            },
            "text": "Открываю Telegram"
        })
        
        result = parser.parse(response_str)
        
        assert result.text_response == "Открываю Telegram"
        assert result.command_payload is not None
        assert result.command_payload['payload']['command'] == 'open_app'
    
    def test_action_response_missing_session_id(self, parser):
        """Дополнительный тест: Action-ответ без session_id (валидация)"""
        response = {
            "command": "open_app",
            "args": {
                "app_name": "Telegram"
            },
            "text": "Открываю Telegram"
        }
        
        with patch.object(parser.logger, 'warning') as mock_warning:
            result = parser.parse(response)
            
            # Должен вернуть только текст, без команды (fallback из-за ошибки валидации)
            assert result.text_response == "Открываю Telegram"
            assert result.command_payload is None
            # Проверяем, что было предупреждение
            assert mock_warning.called
    
    def test_action_response_missing_app_name(self, parser):
        """Дополнительный тест: Action-ответ open_app без app_name (валидация)"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": "open_app",
            "args": {},
            "text": "Открываю приложение"
        }
        
        with patch.object(parser.logger, 'warning') as mock_warning:
            result = parser.parse(response)
            
            # Должен вернуть только текст, без команды (fallback из-за ошибки валидации)
            assert result.text_response == "Открываю приложение"
            assert result.command_payload is None
            # Проверяем, что было предупреждение
            assert mock_warning.called
    
    def test_command_null(self, parser):
        """Дополнительный тест: command равен null (должен обрабатываться как отсутствие команды)"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": None,
            "text": "Обычный ответ"
        }
        
        result = parser.parse(response)
        
        assert result.text_response == "Обычный ответ"
        assert result.command_payload is None
    
    def test_command_empty_string(self, parser):
        """Дополнительный тест: command равен пустой строке (должен обрабатываться как отсутствие команды)"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": "",
            "text": "Обычный ответ"
        }
        
        result = parser.parse(response)
        
        assert result.text_response == "Обычный ответ"
        assert result.command_payload is None
    
    def test_text_not_string(self, parser):
        """Дополнительный тест: text не является строкой"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "text": 12345  # Не строка
        }
        
        with patch.object(parser.logger, 'warning') as mock_warning:
            result = parser.parse(response)
            
            # Должен подставить пустую строку
            assert result.text_response == ''
            assert result.command_payload is None
            # Проверяем, что было предупреждение
            assert mock_warning.called
    
    def test_args_not_dict(self, parser):
        """Дополнительный тест: args не является словарём"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": "open_app",
            "args": "not_a_dict",  # Не словарь
            "text": "Текст"
        }
        
        with patch.object(parser.logger, 'warning') as mock_warning:
            result = parser.parse(response)
            
            # Должен вернуть только текст из-за ошибки валидации
            assert result.text_response == "Текст"
            assert result.command_payload is None
            # Проверяем, что было предупреждение
            assert mock_warning.called
    
    # ==================== Тесты для close_app ====================
    
    def test_close_app_response_valid(self, parser):
        """Тест: Action-ответ close_app с валидными полями"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": "close_app",
            "args": {
                "app_name": "Safari"
            },
            "text": "Закрываю Safari."
        }
        
        result = parser.parse(response)
        
        assert isinstance(result, ParsedResponse)
        assert result.text_response == "Закрываю Safari."
        assert result.command_payload is not None
        assert result.command_payload['event'] == 'mcp.command_request'
        assert result.command_payload['payload']['command'] == 'close_app'
        assert result.command_payload['payload']['args']['app_name'] == 'Safari'
        assert result.session_id == "123e4567-e89b-12d3-a456-426614174000"
    
    def test_close_app_response_missing_app_name(self, parser):
        """Тест: Action-ответ close_app без app_name (валидация)"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": "close_app",
            "args": {},
            "text": "Закрываю приложение"
        }
        
        with patch.object(parser.logger, 'warning') as mock_warning:
            result = parser.parse(response)
            
            # Должен вернуть только текст, без команды (fallback из-за ошибки валидации)
            assert result.text_response == "Закрываю приложение"
            assert result.command_payload is None
            # Проверяем, что было предупреждение
            assert mock_warning.called
    
    def test_close_app_response_empty_app_name(self, parser):
        """Тест: Action-ответ close_app с пустым app_name (валидация)"""
        response = {
            "session_id": "123e4567-e89b-12d3-a456-426614174000",
            "command": "close_app",
            "args": {
                "app_name": ""
            },
            "text": "Закрываю приложение"
        }
        
        with patch.object(parser.logger, 'warning') as mock_warning:
            result = parser.parse(response)
            
            # Должен вернуть только текст, без команды (fallback из-за ошибки валидации)
            assert result.text_response == "Закрываю приложение"
            assert result.command_payload is None
            # Проверяем, что было предупреждение
            assert mock_warning.called


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

