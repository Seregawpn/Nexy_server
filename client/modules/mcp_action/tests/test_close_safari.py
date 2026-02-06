#!/usr/bin/env python3
"""
Тестовый скрипт для закрытия Safari через McpActionExecutor.

Feature ID: F-2025-014-close-app
"""

import asyncio
import logging
from pathlib import Path
import sys

import pytest

# Добавляем путь к client(prod)
client_prod_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(client_prod_root))

from modules.mcp_action.core.mcp_action_executor import McpActionExecutor
from modules.mcp_action.core.types import McpActionConfig

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_close_app_server_path() -> str:
    """Получает путь к close_app_server.py."""
    # Путь относительно client(prod) к корню проекта
    client_prod_root = Path(__file__).parent.parent.parent.parent
    project_root = client_prod_root.parent
    server_path = project_root / "mcp_close_app_test" / "server" / "close_app_server.py"
    return str(server_path.absolute())


def get_open_app_server_path() -> str:
    """Получает путь к app_launcher_server.py (если есть)."""
    # Пока используем close_app_server для теста open_app тоже
    # В реальности должен быть отдельный сервер
    return get_close_app_server_path()


@pytest.mark.asyncio
async def test_close_safari():
    """Тест закрытия Safari."""
    logger.info("=== Тест закрытия Safari ===")
    
    # Создаем конфигурацию
    config = McpActionConfig(
        open_app_server_path=get_open_app_server_path(),
        close_app_server_path=get_close_app_server_path(),
        timeout_sec=10.0,
        enabled=True,
    )
    
    # Создаем исполнитель
    executor = McpActionExecutor(config)
    
    # Подготавливаем данные для закрытия Safari
    action_data = {
        "type": "close_app",
        "app_name": "Safari"
    }
    
    logger.info(f"Выполняем закрытие Safari...")
    logger.info(f"Данные действия: {action_data}")
    
    # Выполняем действие
    result = await executor.execute_action(
        action_data,
        session_id="test_close_safari"
    )
    
    # Выводим результат
    logger.info("=== Результат ===")
    logger.info(f"Успех: {result.success}")
    logger.info(f"Сообщение: {result.message}")
    logger.info(f"Ошибка: {result.error}")
    logger.info(f"Имя приложения: {result.app_name}")
    
    if result.success:
        print("\n✅ Safari успешно закрыт!")
    else:
        print(f"\n❌ Ошибка при закрытии Safari: {result.message}")
    
    return result


if __name__ == "__main__":
    try:
        result = asyncio.run(test_close_safari())
        sys.exit(0 if result.success else 1)
    except KeyboardInterrupt:
        logger.info("Тест прерван пользователем")
        sys.exit(1)
    except Exception as exc:
        logger.error(f"Ошибка при выполнении теста: {exc}", exc_info=True)
        sys.exit(1)

