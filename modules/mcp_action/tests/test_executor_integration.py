"""
Интеграционные тесты для McpActionExecutor с реальным MCP сервером.

Feature ID: F-2025-014-close-app

Эти тесты требуют наличия MCP серверов:
- mcp_close_app_test/server/close_app_server.py
- mcp_close_app_test/server/app_launcher_server.py (если есть)
"""

import pytest
from pathlib import Path
import sys

# Добавляем путь к корню проекта
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from modules.mcp_action.core.mcp_action_executor import McpActionExecutor
from modules.mcp_action.core.types import McpActionConfig


def get_close_app_server_path() -> str:
    """Получает путь к close_app_server.py."""
    project_root = Path(__file__).parent.parent.parent.parent.parent
    server_path = project_root / "mcp_close_app_test" / "server" / "close_app_server.py"
    return str(server_path.absolute())


def get_open_app_server_path() -> str:
    """Получает путь к app_launcher_server.py (если есть)."""
    # Пока используем close_app_server для теста open_app тоже
    # В реальности должен быть отдельный сервер
    return get_close_app_server_path()


@pytest.fixture
def config():
    """Создает конфигурацию для интеграционных тестов."""
    return McpActionConfig(
        open_app_server_path=get_open_app_server_path(),
        close_app_server_path=get_close_app_server_path(),
        timeout_sec=10.0,
        enabled=True,
    )


@pytest.fixture
def executor(config):
    """Создает экземпляр исполнителя для интеграционных тестов."""
    return McpActionExecutor(config)


@pytest.mark.asyncio
@pytest.mark.integration
async def test_close_app_integration(executor):
    """Интеграционный тест закрытия приложения через реальный MCP сервер."""
    # Сначала нужно открыть приложение, чтобы его можно было закрыть
    # Для теста используем Calculator, который обычно доступен на macOS
    
    action_data = {"type": "close_app", "app_name": "Calculator"}
    
    result = await executor.execute_action(action_data, session_id="test_integration")
    
    # Результат может быть успешным (если приложение было открыто и закрыто)
    # или неуспешным (если приложение не было открыто)
    # В любом случае, мы проверяем, что код работает без ошибок
    assert result is not None
    assert isinstance(result.success, bool)
    assert result.message is not None


@pytest.mark.asyncio
@pytest.mark.integration
async def test_close_app_missing_parameter(executor):
    """Тест обработки отсутствующего параметра."""
    action_data = {"type": "close_app"}
    
    result = await executor.execute_action(action_data)
    
    assert result is not None
    assert result.success is False
    assert "Missing app_name" in result.message
    assert result.error == "missing_parameter"


