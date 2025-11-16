#!/usr/bin/env python3
"""
Assistant Response Parser - парсинг и валидация ответов ассистента с поддержкой MCP команд

Поддерживает формат:
{
  "session_id": "<uuid>",
  "command": "open_app",
  "args": {
    "app_name": "Telegram"
  },
  "text": "Открываю Telegram, дайте знать, если понадобится что-то ещё."
}
"""

import json
import logging
from typing import Dict, Any, Optional, Tuple, Union
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class ParsedResponse:
    """Результат парсинга ответа ассистента"""
    text_response: str
    command_payload: Optional[Dict[str, Any]] = None
    session_id: Optional[str] = None
    raw_args: Optional[Dict[str, Any]] = None


class AssistantResponseParser:
    """
    Парсер и валидатор ответов ассистента
    
    Обрабатывает как обычные текстовые ответы, так и комбинированные ответы
    с MCP командами (command + args + text).
    """
    
    def __init__(self):
        """Инициализация парсера"""
        self.logger = logger
    
    def parse(self, response: Union[str, Dict[str, Any]]) -> ParsedResponse:
        """
        Парсинг ответа ассистента
        
        Args:
            response: Строка (JSON или обычный текст) или словарь
            
        Returns:
            ParsedResponse с text_response и опциональным command_payload
        """
        # Если уже словарь, используем напрямую
        if isinstance(response, dict):
            return self._parse_dict(response)
        
        # Пытаемся распарсить как JSON
        if isinstance(response, str):
            return self._parse_string(response)
        
        # Неизвестный тип - возвращаем как текст
        self.logger.warning(f"Неизвестный тип ответа: {type(response)}, возвращаем как текст")
        return ParsedResponse(
            text_response=str(response),
            command_payload=None
        )
    
    def _parse_string(self, response_str: str) -> ParsedResponse:
        """
        Парсинг строкового ответа
        
        Args:
            response_str: Строка (может быть JSON или обычный текст)
            
        Returns:
            ParsedResponse
        """
        # Пытаемся распарсить как JSON
        try:
            data = json.loads(response_str.strip())
            if isinstance(data, dict):
                return self._parse_dict(data)
            # Если JSON, но не словарь - возвращаем как текст
            return ParsedResponse(
                text_response=response_str,
                command_payload=None
            )
        except (json.JSONDecodeError, ValueError):
            # Не JSON - возвращаем как обычный текст
            return ParsedResponse(
                text_response=response_str,
                command_payload=None
            )
    
    def _parse_dict(self, data: Dict[str, Any]) -> ParsedResponse:
        """
        Парсинг словаря ответа
        
        Args:
            data: Словарь с полями ответа
            
        Returns:
            ParsedResponse
        """
        # Извлекаем text (обязательное поле, но может быть пустым)
        text_response = data.get('text', '')
        if not isinstance(text_response, str):
            self.logger.warning("Поле 'text' не является строкой, подставляем пустую строку")
            text_response = ''
        
        # Проверяем наличие команды
        command = data.get('command')
        if command is None or command == '':
            # Обычный текстовый ответ без команды
            return ParsedResponse(
                text_response=text_response,
                command_payload=None,
                session_id=data.get('session_id'),
                raw_args=None
            )
        
        # Action-ответ с командой
        session_id = data.get('session_id')
        args = data.get('args', {})
        
        # Валидация обязательных полей для action-ответа
        validation_errors = []
        
        if not session_id:
            validation_errors.append("Отсутствует обязательное поле 'session_id'")
        
        if not isinstance(args, dict):
            validation_errors.append("Поле 'args' должно быть словарём")
            args = {}
        
        # Для команды open_app проверяем наличие app_name
        if command == 'open_app':
            if 'app_name' not in args or not args.get('app_name'):
                validation_errors.append("Для команды 'open_app' требуется поле 'args.app_name'")
        
        # Логируем ошибки валидации
        if validation_errors:
            self.logger.warning(
                f"Ошибки валидации action-ответа (command={command}, session_id={session_id}): "
                f"{'; '.join(validation_errors)}"
            )
            # Возвращаем только текст, без команды (fallback)
            return ParsedResponse(
                text_response=text_response,
                command_payload=None,
                session_id=session_id,
                raw_args=args
            )
        
        # Формируем command_payload для MCP
        command_payload = {
            'event': 'mcp.command_request',
            'payload': {
                'session_id': session_id,
                'command': command,
                'args': args
            }
        }
        
        self.logger.info(
            f"Распознан action-ответ: command={command}, session_id={session_id}, "
            f"text_len={len(text_response)}"
        )
        
        return ParsedResponse(
            text_response=text_response,
            command_payload=command_payload,
            session_id=session_id,
            raw_args=args
        )

