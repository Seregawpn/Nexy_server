"""
Единый формат логирования для сервера Nexy (PR-4)

Формат: ts=... level=INFO scope=grpc method=StreamAudio decision=<...> ctx={...} dur_ms=123

Все логи должны использовать этот формат для единообразия и удобства анализа.

Секреты автоматически маскируются (PR-8).
"""

import logging
import time
import json
import re
from datetime import datetime
from typing import Optional, Dict, Any


class StructuredFormatter(logging.Formatter):
    """
    Структурированный форматтер логов
    
    Формат: ts=... level=INFO scope=grpc method=StreamAudio decision=<...> ctx={...} dur_ms=123
    
    Секреты автоматически маскируются (PR-8).
    """
    
    # Паттерны для маскировки секретов
    SECRET_PATTERNS = [
        (r'api[_-]?key["\s:=]+([a-zA-Z0-9_-]{20,})', r'api_key="****"'),
        (r'token["\s:=]+([a-zA-Z0-9_-]{20,})', r'token="****"'),
        (r'password["\s:=]+([^\s,"}]+)', r'password="****"'),
        (r'secret["\s:=]+([^\s,"}]+)', r'secret="****"'),
        (r'GEMINI_API_KEY["\s:=]+([a-zA-Z0-9_-]+)', r'GEMINI_API_KEY="****"'),
        (r'AZURE_SPEECH_KEY["\s:=]+([a-zA-Z0-9_-]+)', r'AZURE_SPEECH_KEY="****"'),
        (r'GITHUB_TOKEN["\s:=]+([a-zA-Z0-9_-]+)', r'GITHUB_TOKEN="****"'),
    ]
    
    def _mask_secrets(self, text: str) -> str:
        """
        Маскировка секретов в тексте
        
        Args:
            text: Текст для маскировки
        
        Returns:
            Текст с замаскированными секретами
        """
        masked = text
        for pattern, replacement in self.SECRET_PATTERNS:
            masked = re.sub(pattern, replacement, masked, flags=re.IGNORECASE)
        return masked
    
    def format(self, record: logging.LogRecord) -> str:
        """
        Форматирование лога в структурированный формат
        
        Args:
            record: LogRecord для форматирования
        
        Returns:
            Отформатированная строка лога
        """
        # Базовые поля
        parts = [
            f"ts={datetime.utcnow().isoformat()}",
            f"level={record.levelname}",
        ]
        
        # Scope (из имени логгера или экстра)
        scope = getattr(record, 'scope', None)
        if not scope:
            # Извлекаем scope из имени логгера (например, "modules.grpc_service" -> "grpc")
            logger_name = record.name
            if 'grpc' in logger_name.lower():
                scope = 'grpc'
            elif 'update' in logger_name.lower():
                scope = 'update'
            elif 'module' in logger_name.lower():
                scope = 'module'
            else:
                scope = 'server'
        parts.append(f"scope={scope}")
        
        # Метод (если есть)
        method = getattr(record, 'method', None)
        if method:
            parts.append(f"method={method}")
        
        # Decision (если есть)
        decision = getattr(record, 'decision', None)
        if decision:
            parts.append(f"decision={decision}")
        
        # Context (если есть, маскируем секреты)
        ctx = getattr(record, 'ctx', None)
        if ctx:
            # Маскируем секреты в контексте перед сериализацией
            masked_ctx = self._mask_secrets_in_dict(ctx) if isinstance(ctx, dict) else ctx
            
            # Сериализуем контекст в JSON
            try:
                ctx_str = json.dumps(masked_ctx, ensure_ascii=False, default=str)
                parts.append(f"ctx={ctx_str}")
            except (TypeError, ValueError):
                # Если не удается сериализовать, используем строковое представление
                ctx_str = str(masked_ctx)
                parts.append(f"ctx={self._mask_secrets(ctx_str)}")
        
        # Duration (если есть)
        dur_ms = getattr(record, 'dur_ms', None)
        if dur_ms is not None:
            parts.append(f"dur_ms={int(dur_ms)}")
        
        # Сообщение (маскируем секреты)
        message = record.getMessage()
        if message:
            masked_message = self._mask_secrets(message)
            parts.append(f"msg={masked_message}")
        
        # Exception (если есть, маскируем секреты)
        if record.exc_info:
            exception_text = self.formatException(record.exc_info)
            masked_exception = self._mask_secrets(exception_text)
            parts.append(f"exception={masked_exception}")
        
        # Маскируем секреты в итоговой строке
        result = " ".join(parts)
        return self._mask_secrets(result)
    
    def _mask_secrets_in_dict(self, d: Dict[str, Any]) -> Dict[str, Any]:
        """
        Маскировка секретов в словаре
        
        Args:
            d: Словарь для маскировки
        
        Returns:
            Словарь с замаскированными секретами
        """
        masked = {}
        secret_keys = ['api_key', 'token', 'password', 'secret', 'key', 'GEMINI_API_KEY', 'AZURE_SPEECH_KEY', 'GITHUB_TOKEN']
        
        for key, value in d.items():
            if any(sk in key.lower() for sk in secret_keys) and isinstance(value, str) and len(value) > 10:
                masked[key] = "****"
            elif isinstance(value, dict):
                masked[key] = self._mask_secrets_in_dict(value)
            else:
                masked[key] = value
        
        return masked


def setup_structured_logging(level: str = "INFO") -> None:
    """
    Настройка структурированного логирования
    
    Args:
        level: Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Получаем root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, level.upper()))
    
    # Удаляем существующие handlers
    root_logger.handlers.clear()
    
    # Создаем console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, level.upper()))
    
    # Устанавливаем структурированный форматтер
    formatter = StructuredFormatter()
    console_handler.setFormatter(formatter)
    
    # Добавляем handler
    root_logger.addHandler(console_handler)


def log_structured(
    logger: logging.Logger,
    level: int,
    message: str,
    scope: Optional[str] = None,
    method: Optional[str] = None,
    decision: Optional[str] = None,
    ctx: Optional[Dict[str, Any]] = None,
    dur_ms: Optional[float] = None,
    **kwargs
) -> None:
    """
    Логирование с структурированными полями
    
    Args:
        logger: Logger для логирования
        level: Уровень логирования (logging.INFO, logging.ERROR и т.д.)
        message: Сообщение
        scope: Область (grpc, update, module и т.д.)
        method: Метод (StreamAudio, InterruptSession и т.д.)
        decision: Решение (start, abort, retry, degrade и т.д.)
        ctx: Контекст (словарь с дополнительными данными)
        dur_ms: Длительность в миллисекундах
        **kwargs: Дополнительные поля для контекста
    """
    # Объединяем kwargs с ctx
    if ctx is None:
        ctx = {}
    ctx.update(kwargs)
    
    # Создаем экстра-поля
    extra = {
        'scope': scope,
        'method': method,
        'decision': decision,
        'ctx': ctx if ctx else None,
        'dur_ms': dur_ms
    }
    
    # Логируем
    logger.log(level, message, extra=extra)


# Удобные функции для логирования ключевых событий

def log_server_start(logger: logging.Logger, port: int, version: str) -> None:
    """Логирование старта сервера"""
    log_structured(
        logger,
        logging.INFO,
        "Server started",
        scope="server",
        decision="start",
        ctx={"port": port, "version": version}
    )


def log_server_stop(logger: logging.Logger, reason: str = "shutdown") -> None:
    """Логирование остановки сервера"""
    log_structured(
        logger,
        logging.INFO,
        f"Server stopped: {reason}",
        scope="server",
        decision="stop",
        ctx={"reason": reason}
    )


def log_rpc_error(
    logger: logging.Logger,
    method: str,
    error_code: str,
    error_message: str,
    dur_ms: Optional[float] = None,
    ctx: Optional[Dict[str, Any]] = None
) -> None:
    """Логирование ошибки RPC"""
    error_ctx = ctx or {}
    error_ctx.update({
        "error_code": error_code,
        "error_message": error_message
    })
    log_structured(
        logger,
        logging.ERROR,
        f"RPC error in {method}",
        scope="grpc",
        method=method,
        decision="error",
        ctx=error_ctx,
        dur_ms=dur_ms
    )


def log_module_error(
    logger: logging.Logger,
    module_name: str,
    error_message: str,
    ctx: Optional[Dict[str, Any]] = None
) -> None:
    """Логирование ошибки модуля"""
    error_ctx = ctx or {}
    error_ctx.update({
        "module": module_name,
        "error": error_message
    })
    log_structured(
        logger,
        logging.ERROR,
        f"Module error in {module_name}",
        scope="module",
        method=module_name,
        decision="error",
        ctx=error_ctx
    )


def log_decision(
    logger: logging.Logger,
    decision: str,
    method: str,
    ctx: Optional[Dict[str, Any]] = None,
    dur_ms: Optional[float] = None
) -> None:
    """Логирование решения (decision)"""
    log_structured(
        logger,
        logging.INFO,
        f"Decision: {decision}",
        scope="grpc",
        method=method,
        decision=decision,
        ctx=ctx,
        dur_ms=dur_ms
    )


def log_degradation(
    logger: logging.Logger,
    reason: str,
    ctx: Optional[Dict[str, Any]] = None
) -> None:
    """Логирование деградации"""
    log_structured(
        logger,
        logging.WARNING,
        f"Service degraded: {reason}",
        scope="server",
        decision="degrade",
        ctx=ctx or {"reason": reason}
    )

