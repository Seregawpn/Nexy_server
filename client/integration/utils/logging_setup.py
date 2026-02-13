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
from logging.handlers import RotatingFileHandler
import os
import sys

# Singleton flag для однократной настройки
_logging_configured: bool = False


def _is_terminal_dev_launch() -> bool:
    """Detect plain dev launch from interactive terminal (non-bundled run)."""
    if getattr(sys, "frozen", False):
        return False
    try:
        return bool(sys.stdin and sys.stdin.isatty() and os.getenv("TERM"))
    except Exception:
        return False


def _resolve_log_file_path(config_path: str | None) -> str | None:
    """
    Resolve effective log file path.

    Rule:
    - packaged/default flow uses config path as-is;
    - dev launch from terminal writes to sibling `nexy-dev.log`.
    """
    if not config_path:
        return None

    abs_path = os.path.abspath(os.path.expanduser(config_path))
    if not _is_terminal_dev_launch():
        return abs_path

    log_dir = os.path.dirname(abs_path)
    ext = os.path.splitext(abs_path)[1] or ".log"
    dev_name = f"nexy-dev{ext}"
    return os.path.join(log_dir, dev_name)


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
        logging_section = raw_config.get("logging", {})

        # Уровни логирования и формат
        console_level_name = logging_section.get("console_level", "INFO")
        file_level_name = logging_section.get("file_level", console_level_name)
        console_level = getattr(logging, console_level_name.upper(), logging.INFO)
        file_level = getattr(logging, file_level_name.upper(), console_level)
        log_format = logging_section.get(
            "format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Root уровень должен пропускать самый детальный handler
        root_level = min(console_level, file_level)
        logging.getLogger().setLevel(root_level)

        # Настраиваем handlers (если еще не настроены)
        root_logger = logging.getLogger()
        formatter = logging.Formatter(log_format)

        # Console handler
        has_console = any(isinstance(h, logging.StreamHandler) for h in root_logger.handlers)
        if not has_console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(console_level)
            console_handler.setFormatter(formatter)
            root_logger.addHandler(console_handler)

        # File handler
        file_path = logging_section.get("file_path")
        if file_path:
            abs_path = _resolve_log_file_path(file_path)
            if not abs_path:
                return
            try:
                log_dir = os.path.dirname(abs_path)
                if log_dir:
                    os.makedirs(log_dir, exist_ok=True)

                has_file = any(
                    isinstance(h, (logging.FileHandler, RotatingFileHandler))
                    and getattr(h, "baseFilename", "") == abs_path
                    for h in root_logger.handlers
                )
                if not has_file:
                    use_rotation = bool(logging_section.get("rotation", True))
                    max_bytes = int(logging_section.get("max_file_size", 10 * 1024 * 1024))
                    backup_count = int(logging_section.get("max_files", 5))
                    if use_rotation:
                        file_handler = RotatingFileHandler(
                            abs_path,
                            maxBytes=max_bytes,
                            backupCount=backup_count,
                            encoding="utf-8",
                        )
                    else:
                        file_handler = logging.FileHandler(abs_path, encoding="utf-8")
                    file_handler.setLevel(file_level)
                    file_handler.setFormatter(formatter)
                    root_logger.addHandler(file_handler)
            except OSError as e:
                logging.getLogger(__name__).warning(
                    "Could not set up file logging at %s: %s (console logging only)",
                    abs_path,
                    e,
                )

        # Устанавливаем уровни для конкретных интеграций из конфига
        # Можно добавить в будущем integrations.*.log_level
        integrations = raw_config.get("integrations", {})
        for integration_name, integration_config in integrations.items():
            if isinstance(integration_config, dict):
                log_level = integration_config.get("log_level")
                if log_level:
                    level = getattr(logging, log_level.upper(), logging.DEBUG)
                    logging.getLogger(f"integration.integrations.{integration_name}").setLevel(
                        level
                    )

        # Логируем успешную инициализацию (только если уже есть handlers)
        if logging.getLogger().handlers:
            logging.getLogger(__name__).debug(
                "Logging configured from unified_config.yaml: root=%s console=%s file=%s",
                logging.getLevelName(root_level),
                logging.getLevelName(console_level),
                logging.getLevelName(file_level),
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


def get_effective_log_file_path() -> str | None:
    """Return current effective log file path using centralized resolution rules."""
    try:
        from config.unified_config_loader import UnifiedConfigLoader

        raw_config = UnifiedConfigLoader.get_instance()._load_config()
        configured_path = raw_config.get("logging", {}).get("file_path")
        return _resolve_log_file_path(configured_path)
    except Exception:
        return None


def reset_logging_state() -> None:
    """
    Сбрасывает состояние настройки (только для тестов!).

    WARNING: Не использовать в production.
    """
    global _logging_configured
    _logging_configured = False
