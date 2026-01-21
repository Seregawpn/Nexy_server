#!/usr/bin/env python3
"""
Logging Configuration для платежной системы

Feature ID: F-2025-017-stripe-payment
Централизованная настройка логирования
"""
import logging
import os
from pathlib import Path
from datetime import datetime
from logging.handlers import RotatingFileHandler


def setup_payment_logging(
    log_dir: str = "logs",
    log_level: str = "INFO",
    max_bytes: int = 10 * 1024 * 1024,  # 10 MB
    backup_count: int = 5
) -> logging.Logger:
    """
    Настроить логирование для платежной системы
    
    Args:
        log_dir: Директория для логов
        log_level: Уровень логирования (DEBUG, INFO, WARNING, ERROR)
        max_bytes: Максимальный размер файла лога
        backup_count: Количество резервных файлов
    
    Returns:
        Настроенный logger
    """
    # Создаем директорию для логов
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)
    
    # Создаем logger для платежной системы
    logger = logging.getLogger('payment_system')
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    # Удаляем существующие handlers
    logger.handlers.clear()
    
    # Формат логов
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler для файла (ротация)
    log_file = log_path / f'payment_system_{datetime.now().strftime("%Y%m%d")}.log'
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Handler для консоли
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # Handler для критических ошибок (отдельный файл)
    error_log_file = log_path / f'payment_errors_{datetime.now().strftime("%Y%m%d")}.log'
    error_handler = RotatingFileHandler(
        error_log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)
    
    logger.info("Payment system logging configured")
    logger.info(f"Log directory: {log_path.absolute()}")
    logger.info(f"Log level: {log_level}")
    
    return logger


def setup_component_logging(component_name: str, log_dir: str = "logs") -> logging.Logger:
    """
    Настроить логирование для конкретного компонента
    
    Args:
        component_name: Имя компонента (например, 'webhook_handler', 'quota_checker')
        log_dir: Директория для логов
    
    Returns:
        Настроенный logger для компонента
    """
    # Создаем директорию для логов
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)
    
    # Создаем logger для компонента
    logger = logging.getLogger(f'payment_system.{component_name}')
    
    # Если уже настроен, возвращаем
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)
    
    # Формат логов
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(name)s] [%(filename)s:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler для файла компонента
    log_file = log_path / f'{component_name}_{datetime.now().strftime("%Y%m%d")}.log'
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Handler для консоли
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger


# Глобальная настройка логирования
def init_payment_logging():
    """Инициализировать логирование для всей платежной системы"""
    log_dir = os.getenv('PAYMENT_LOG_DIR', 'logs')
    log_level = os.getenv('PAYMENT_LOG_LEVEL', 'INFO')
    
    return setup_payment_logging(log_dir=log_dir, log_level=log_level)

