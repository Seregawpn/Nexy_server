"""
Централизованная настройка логирования Nexy AI Assistant.

Этот модуль обеспечивает единую точку конфигурации логгеров
на основе настроек из unified_config.yaml.

Использование:
    from integration.utils.logging_setup import get_logger, setup_logging
    
    # Вместо: logger = logging.getLogger(__name__)
    logger = get_logger(__name__)
"""

import logging
from typing import Optional

# Singleton flag для однократной настройки
_logging_configured: bool = False


def setup_logging(force: bool = False) -> None:
    """
    Применяет настройки логирования из unified_config.yaml.
    
    Настраивает уровни логирования для модулей, указанных в конфиге.
    Вызывается автоматически при первом вызове get_logger().
    
    Args:
        force: Принудительно применить настройки даже если уже настроено
    """
    global _logging_configured
    
    if _logging_configured and not force:
        return
    
    try:
        from config.unified_config_loader import UnifiedConfigLoader
        
        config = UnifiedConfigLoader.get_instance()
        
        # Получаем raw config для logging секции т.к. структура YAML отличается
        raw_config = config._load_config()
        logging_section = raw_config.get('logging', {})
        
        # Устанавливаем уровень для root logger
        # YAML использует console_level / file_level
        console_level = logging_section.get('console_level', 'INFO')
        root_level = getattr(logging, console_level.upper(), logging.INFO)
        logging.getLogger().setLevel(root_level)
        
        # Устанавливаем уровни для конкретных интеграций из конфига
        # Можно добавить в будущем integrations.*.log_level
        integrations = raw_config.get('integrations', {})
        for integration_name, integration_config in integrations.items():
            if isinstance(integration_config, dict):
                log_level = integration_config.get('log_level')
                if log_level:
                    level = getattr(logging, log_level.upper(), logging.DEBUG)
                    logging.getLogger(f"integration.integrations.{integration_name}").setLevel(level)
        
        # Логируем успешную инициализацию (только если уже есть handlers)
        if logging.getLogger().handlers:
            logging.getLogger(__name__).debug(
                f"Logging configured from unified_config.yaml: root={console_level}"
            )
        
        _logging_configured = True
        
    except Exception as e:
        # Не падаем если конфиг недоступен - используем defaults
        logging.getLogger(__name__).warning(
            f"Could not load logging config from unified_config.yaml: {e}"
        )
        _logging_configured = True  # Не пытаемся снова


def get_logger(name: str) -> logging.Logger:
    """
    Получает логгер с гарантией применения централизованных настроек.
    
    Рекомендуется использовать вместо logging.getLogger(__name__).
    
    Args:
        name: Имя логгера (обычно __name__)
        
    Returns:
        Настроенный логгер
        
    Example:
        logger = get_logger(__name__)
        logger.info("Message")
    """
    setup_logging()
    return logging.getLogger(name)


def is_logging_configured() -> bool:
    """Проверяет, была ли выполнена централизованная настройка."""
    return _logging_configured


def reset_logging_state() -> None:
    """
    Сбрасывает состояние настройки (только для тестов!).
    
    WARNING: Не использовать в production.
    """
    global _logging_configured
    _logging_configured = False
