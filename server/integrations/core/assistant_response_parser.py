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

# Try to import Pydantic for validation (optional dependency)
try:
    from .response_models import LLMResponseValidator, TextResponse, ActionResponse
    PYDANTIC_AVAILABLE = True
except ImportError:
    PYDANTIC_AVAILABLE = False
    LLMResponseValidator = None
    TextResponse = None
    ActionResponse = None

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

    def _normalize_command(self, command: Any) -> Any:
        """Нормализует имя команды к каноническому виду"""
        if not isinstance(command, str):
            return command
        normalized = command.strip().lower()
        normalized = normalized.replace("-", "_").replace(".", "_").replace(" ", "_")
        while "__" in normalized:
            normalized = normalized.replace("__", "_")
        return normalized

    def _normalize_action_payload(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Возвращает копию data с нормализованной командой (если есть)"""
        if 'command' not in data or not isinstance(data.get('command'), str):
            return data
        normalized = self._normalize_command(data['command'])
        if normalized == data['command']:
            return data
        normalized_data = data.copy()
        normalized_data['command'] = normalized
        return normalized_data

    def _looks_like_action_intent(self, text: Any) -> bool:
        """Быстрый эвристический детектор action-like текста для диагностики."""
        if not isinstance(text, str):
            return False
        text_l = text.lower()
        markers = (
            "send_message",
            "read_messages",
            "find_contact",
            "open_app",
            "close_app",
            "browser_use",
            "send_whatsapp_message",
            "buy_subscription",
            "manage_subscription",
            "отправ",
            "сообщен",
            "откро",
            "закро",
            "команд",
        )
        return any(marker in text_l for marker in markers)
    
    def parse(self, response: Union[str, Dict[str, Any]], session_id: Optional[str] = None) -> ParsedResponse:
        """
        Парсинг ответа ассистента
        
        Args:
            response: Строка (JSON или обычный текст) или словарь
            session_id: Optional session ID to inject if missing in action responses
            
        Returns:
            ParsedResponse с text_response и опциональным command_payload
        """
        # Если уже словарь, используем напрямую
        if isinstance(response, dict):
            return self._parse_dict(response, session_id=session_id)
        
        # Пытаемся распарсить как JSON
        if isinstance(response, str):
            return self._parse_string(response, session_id=session_id)
        
        # Неизвестный тип - возвращаем как текст
        self.logger.warning(f"Неизвестный тип ответа: {type(response)}, возвращаем как текст")
        return ParsedResponse(
            text_response=str(response),
            command_payload=None
        )
    
    def _extract_json_from_markdown(self, text: str) -> str:
        """
        Удаляет Markdown-обёртки и возвращает чистый JSON текст.
        Поддерживает различные вариации ответов LLM:
        - ```json {...}```
        - ``` {...}```
        - json {...}
        - Текст до/после JSON
        - JSON с лишними пробелами/переносами
        - JSON с trailing commas (удаляются)
        - JSON с комментариями (удаляются)
        
        Args:
            text: Текст, который может содержать JSON в различных форматах
            
        Returns:
            Чистый JSON текст без markdown-разметки и лишних символов
        """
        if not text:
            return ""

        import re
        
        text = str(text).strip()

        # Вариант 1: Markdown code fence ```json ... ``` или ``` ... ```
        if text.startswith("```"):
            # Удаляем открывающий fence
            text = text[3:]
            text = text.lstrip()
            
            # Опциональный язык (json/JSON/JSONC и т.д.)
            lowered = text.lower()
            if lowered.startswith("json"):
                text = text[4:]
            text = text.lstrip()
            
            # Удаляем ведущие переводы строки
            while text.startswith(("\n", "\r")):
                text = text[1:]
            
            # Удаляем закрывающий fence
            text = text.rstrip()
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()

        # Вариант 2: Текст начинается с "json" (без markdown)
        # Удаляем "json" если он стоит перед JSON объектом
        text_lower = text.lower()
        if text_lower.startswith("json") and len(text) > 4:
            # Проверяем, что после "json" идёт пробел/перенос и затем {
            after_json = text[4:].lstrip()
            if after_json.startswith("{") or after_json.startswith("\n{") or after_json.startswith("\r{"):
                text = after_json

        # Вариант 3: Текст до/после JSON - извлекаем только JSON объект
        # Ищем первую открывающую скобку и последнюю закрывающую
        first_brace = text.find("{")
        last_brace = text.rfind("}")
        
        if first_brace != -1 and last_brace != -1 and first_brace < last_brace:
            # Извлекаем JSON объект
            json_candidate = text[first_brace:last_brace + 1]
            
            # Очищаем от лишних символов вокруг
            json_candidate = json_candidate.strip()
            
            # Удаляем возможные артефакты:
            # 1. Удаляем комментарии (// и /* */) - хотя JSON не поддерживает, LLM может их добавить
            json_candidate = re.sub(r'//.*?$', '', json_candidate, flags=re.MULTILINE)  # Однострочные комментарии
            json_candidate = re.sub(r'/\*.*?\*/', '', json_candidate, flags=re.DOTALL)  # Многострочные комментарии
            
            # 2. Удаляем trailing commas перед закрывающими скобками/фигурными скобками
            json_candidate = re.sub(r',\s*}', '}', json_candidate)  # Trailing comma перед }
            json_candidate = re.sub(r',\s*]', ']', json_candidate)  # Trailing comma перед ]
            
            # 3. Нормализуем пробелы и переносы строк
            json_candidate = re.sub(r'\n\s*\n', '\n', json_candidate)  # Удаляем пустые строки
            json_candidate = re.sub(r'[ \t]+', ' ', json_candidate)  # Нормализуем пробелы
            
            # 4. Удаляем лишние пробелы вокруг двоеточий и запятых
            json_candidate = re.sub(r'\s*:\s*', ': ', json_candidate)  # Нормализуем пробелы вокруг :
            json_candidate = re.sub(r'\s*,\s*', ', ', json_candidate)  # Нормализуем пробелы вокруг ,
            
            return json_candidate

        # Если JSON объект не найден, возвращаем очищенный текст
        return text.strip()
    
    def _parse_string(self, response_str: str, session_id: Optional[str] = None) -> ParsedResponse:
        """
        Парсинг строкового ответа
        
        Args:
            response_str: Строка (может быть JSON или обычный текст)
            session_id: Optional session ID to inject if missing in action responses
            
        Returns:
            ParsedResponse
        """
        # Удаляем markdown-разметку перед парсингом
        cleaned_str = self._extract_json_from_markdown(response_str)
        
        # Пытаемся распарсить как JSON
        try:
            data = json.loads(cleaned_str)
            if isinstance(data, dict):
                return self._parse_dict(data, session_id=session_id)
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
    
    def _parse_dict(self, data: Dict[str, Any], session_id: Optional[str] = None) -> ParsedResponse:
        """
        Парсинг словаря ответа с валидацией через Pydantic (если доступен)
        
        Args:
            data: Словарь с полями ответа
            session_id: Optional session ID to inject if missing in action responses
            
        Returns:
            ParsedResponse
        """
        normalized_data = self._normalize_action_payload(data)
        # Always propagate or enforce session_id (even for text-only JSON).
        if session_id:
            if normalized_data.get("session_id") and normalized_data.get("session_id") != session_id:
                self.logger.warning(
                    "⚠️ LLM session_id override: response=%s request=%s",
                    normalized_data.get("session_id"),
                    session_id,
                )
                try:
                    from utils.metrics_collector import record_decision_metric
                    record_decision_metric("assistant_response", "session_id_override")
                except Exception:
                    self.logger.debug("Failed to record session_id_override metric")
            normalized_data["session_id"] = session_id

        # Попытка валидации через Pydantic (если доступен)
        if PYDANTIC_AVAILABLE and LLMResponseValidator and ActionResponse is not None:
            # Используем session_id из данных, если есть, иначе из параметра
            context_session_id = normalized_data.get('session_id') or session_id
            validated_model, error_msg = LLMResponseValidator.validate_response(normalized_data, session_id=context_session_id)
            
            if validated_model:
                # Валидация успешна - используем валидированную модель
                if isinstance(validated_model, ActionResponse):
                    # Action-ответ
                    # Используем session_id из модели, если есть, иначе из параметра
                    final_session_id = validated_model.session_id or session_id
                    
                    if not final_session_id:
                        # Нет session_id - не можем выполнить команду
                        self.logger.warning(
                            f"⚠️ Action-ответ не может быть обработан: отсутствует session_id "
                            f"(command={validated_model.command}). Возвращаем только текст."
                        )
                        return ParsedResponse(
                            text_response=validated_model.text,
                            command_payload=None,
                            session_id=None,
                            raw_args=validated_model.args
                        )
                    
                    command_payload = {
                        'event': 'mcp.command_request',
                        'payload': {
                            'session_id': final_session_id,
                            'command': validated_model.command,
                            'args': validated_model.args
                        }
                    }
                    
                    self.logger.info(
                        f"✅ Валидирован action-ответ через Pydantic: command={validated_model.command}, "
                        f"session_id={final_session_id}, text_len={len(validated_model.text)}"
                    )
                    
                    return ParsedResponse(
                        text_response=validated_model.text,
                        command_payload=command_payload,
                        session_id=final_session_id,
                        raw_args=validated_model.args
                    )
                else:
                    # Text-only ответ
                    self.logger.debug(f"✅ Валидирован text-only ответ через Pydantic: text_len={len(validated_model.text)}")
                    return ParsedResponse(
                        text_response=validated_model.text,
                        command_payload=None,
                        session_id=context_session_id,
                        raw_args=None
                    )
            else:
                # Валидация не прошла - логируем и используем fallback
                self.logger.warning(
                    f"⚠️ Pydantic валидация не прошла: {error_msg}. "
                    f"Используем fallback парсинг. Данные: {normalized_data}"
                )
                # Продолжаем с обычным парсингом ниже
        
        # Fallback: обычный парсинг без Pydantic (или если Pydantic недоступен)
        # Извлекаем text (обязательное поле, но может быть пустым)
        text_response = normalized_data.get('text', '')
        if not isinstance(text_response, str):
            self.logger.warning("Поле 'text' не является строкой, подставляем пустую строку")
            text_response = ''
        
        # Проверяем наличие команды
        command = normalized_data.get('command')
        if command is None or command == '':
            # Обычный текстовый ответ без команды
            if self._looks_like_action_intent(text_response):
                self.logger.warning(
                    "[ACTION_PIPELINE][SERVER] stage=parse_no_command session=%s text_preview=%s",
                    normalized_data.get('session_id'),
                    text_response.replace("\n", "\\n")[:220],
                )
            return ParsedResponse(
                text_response=text_response,
                command_payload=None,
                session_id=normalized_data.get('session_id'),
                raw_args=None
            )
        
        # Action-ответ с командой
        # Используем session_id из данных, если есть, иначе из параметра
        action_session_id = normalized_data.get('session_id') or session_id
        args = normalized_data.get('args', {})
        
        # Валидация обязательных полей для action-ответа
        validation_errors = []

        # Проверяем, что команда разрешена фичами (fallback без Pydantic)
        try:
            from config.unified_config import get_config, get_allowed_commands
            cfg = get_config()
            allowed_commands = get_allowed_commands(cfg.features, cfg)
            if command not in allowed_commands:
                validation_errors.append(
                    f"Команда '{command}' отключена или не разрешена. Allowed: {allowed_commands}"
                )
        except Exception:
            # Если конфиг недоступен, не блокируем fallback
            pass
        
        if not action_session_id:
            validation_errors.append("Отсутствует обязательное поле 'session_id' (не предоставлен ни в данных, ни в контексте)")
        
        if not isinstance(args, dict):
            validation_errors.append("Поле 'args' должно быть словарём")
            args = {}
        
        # Для команды open_app проверяем наличие app_name
        if command == 'open_app':
            if 'app_name' not in args or not args.get('app_name'):
                validation_errors.append("Для команды 'open_app' требуется поле 'args.app_name'")
        
        # Для команды close_app проверяем наличие app_name
        if command == 'close_app':
            if 'app_name' not in args or not args.get('app_name'):
                validation_errors.append("Для команды 'close_app' требуется поле 'args.app_name'")
        
        # Для команды browser_use проверяем наличие task
        if command == 'browser_use':
            if 'task' not in args or not args.get('task'):
                validation_errors.append("Для команды 'browser_use' требуется поле 'args.task'")
        
        # Для команды close_browser аргументы не требуются
        # if command == 'close_browser':
        #     pass  # No required args

        # Для команды send_whatsapp_message требуются contact и message
        if command == 'send_whatsapp_message':
            if 'contact' not in args or not args.get('contact'):
                validation_errors.append("Для команды 'send_whatsapp_message' требуется поле 'args.contact'")
            if 'message' not in args or not args.get('message'):
                validation_errors.append("Для команды 'send_whatsapp_message' требуется поле 'args.message'")
        
        # Для команды read_whatsapp_messages аргументы опциональны, но если есть contact - он должен быть не пустой
        if command == 'read_whatsapp_messages':
            if 'contact' in args and not args.get('contact'):
                validation_errors.append("Для команды 'read_whatsapp_messages' поле 'args.contact' не может быть пустым")

        
        # Логируем ошибки валидации
        if validation_errors:
            self.logger.warning(
                f"Ошибки валидации action-ответа (command={command}, session_id={action_session_id}): "
                f"{'; '.join(validation_errors)}"
            )
            self.logger.warning(
                "[ACTION_PIPELINE][SERVER] stage=parse_validation_failed session=%s command=%s args=%s errors=%s",
                action_session_id,
                command,
                args,
                validation_errors,
            )
            # Возвращаем только текст, без команды (fallback)
            return ParsedResponse(
                text_response=text_response,
                command_payload=None,
                session_id=action_session_id,
                raw_args=args
            )
        
        # Формируем command_payload для MCP
        command_payload = {
            'event': 'mcp.command_request',
            'payload': {
                'session_id': action_session_id,
                'command': command,
                'args': args
            }
        }
        
        self.logger.info(
            f"Распознан action-ответ: command={command}, session_id={action_session_id}, "
            f"text_len={len(text_response)}"
        )
        self.logger.info(
            "[ACTION_PIPELINE][SERVER] stage=parse_success session=%s command=%s args=%s",
            action_session_id,
            command,
            args,
        )
        
        return ParsedResponse(
            text_response=text_response,
            command_payload=command_payload,
            session_id=action_session_id,
            raw_args=args
        )
