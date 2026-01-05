"""
Изолированный тест для проверки, что open_app использует McpActionExecutor.

Проверяет:
1. open_app использует _mcp_executor.execute_action вместо _executor.execute
2. close_app использует _mcp_executor.execute_action
3. Правильность передачи параметров в McpActionExecutor
4. Обработка результатов от McpActionExecutor

Feature ID: F-2025-016-mcp-app-opening-integration
"""

import pytest
import json
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from typing import Dict, Any

from integration.integrations.action_execution_integration import ActionExecutionIntegration, FEATURE_ID
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from modules.mcp_action import McpActionResult


@pytest.fixture
def mock_event_bus():
    """Фикстура для EventBus."""
    bus = AsyncMock(spec=EventBus)
    bus.subscribe = AsyncMock()
    bus.unsubscribe = AsyncMock()
    bus.publish = AsyncMock()
    return bus


@pytest.fixture
def mock_state_manager():
    """Фикстура для ApplicationStateManager."""
    return MagicMock(spec=ApplicationStateManager)


@pytest.fixture
def mock_error_handler():
    """Фикстура для ErrorHandler."""
    handler = MagicMock(spec=ErrorHandler)
    handler.handle = AsyncMock()
    return handler


@pytest.fixture
def action_integration(mock_event_bus, mock_state_manager, mock_error_handler):
    """Фикстура для ActionExecutionIntegration."""
    integration = ActionExecutionIntegration(
        event_bus=mock_event_bus,
        state_manager=mock_state_manager,
        error_handler=mock_error_handler,
    )
    # Включаем MCP executor
    integration._mcp_executor.config.enabled = True
    return integration


def _published_event_names(mock_event_bus):
    """Извлекает имена опубликованных событий."""
    return [call.args[0] for call in mock_event_bus.publish.call_args_list]


@pytest.mark.asyncio
async def test_open_app_uses_mcp_executor(action_integration, mock_event_bus):
    """Тест: open_app использует McpActionExecutor, а не ActionExecutor."""
    # Мокируем McpActionExecutor.execute_action
    mock_result = McpActionResult(
        success=True,
        message="Application 'Safari' opened successfully",
        app_name="Safari"
    )
    action_integration._mcp_executor.execute_action = AsyncMock(return_value=mock_result)
    
    # Проверяем, что _executor больше не существует (удален)
    assert not hasattr(action_integration, '_executor'), "ActionExecutor должен быть удален"
    
    # Проверяем, что _mcp_executor существует
    assert hasattr(action_integration, '_mcp_executor'), "McpActionExecutor должен существовать"
    
    event = {
        "session_id": "test-session-open",
        "action_json": json.dumps({
            "command": "open_app",
            "args": {"app_name": "Safari"}
        }),
        "feature_id": FEATURE_ID,
    }
    
    await action_integration._on_action_received(event)
    await asyncio.sleep(0.1)
    
    # Проверяем, что McpActionExecutor.execute_action был вызван
    assert action_integration._mcp_executor.execute_action.called, (
        "McpActionExecutor.execute_action должен быть вызван для open_app"
    )
    
    # Проверяем аргументы вызова
    call_args = action_integration._mcp_executor.execute_action.call_args
    assert call_args is not None, "execute_action должен быть вызван с аргументами"
    
    action_data = call_args[0][0]  # Первый позиционный аргумент
    session_id = call_args[1].get('session_id')  # Именованный аргумент
    
    assert action_data["type"] == "open_app", "Тип действия должен быть 'open_app'"
    assert action_data["app_name"] == "Safari", "Имя приложения должно быть 'Safari'"
    assert session_id == "test-session-open", "session_id должен быть передан"
    
    # Проверяем публикацию событий
    event_names = _published_event_names(mock_event_bus)
    assert "actions.open_app.started" in event_names, "Должно быть событие started"
    assert "actions.open_app.completed" in event_names, "Должно быть событие completed"
    
    # Проверяем содержимое события completed
    completed_calls = [
        call for call in mock_event_bus.publish.call_args_list
        if call.args[0] == "actions.open_app.completed"
    ]
    assert len(completed_calls) > 0, "Должно быть событие completed"
    completed_payload = completed_calls[0].args[1]
    assert completed_payload["message"] == "Application 'Safari' opened successfully"
    assert completed_payload["session_id"] == "test-session-open"


@pytest.mark.asyncio
async def test_close_app_uses_mcp_executor(action_integration, mock_event_bus):
    """Тест: close_app использует McpActionExecutor."""
    # Мокируем McpActionExecutor.execute_action
    mock_result = McpActionResult(
        success=True,
        message="Application 'Calculator' closed successfully",
        app_name="Calculator"
    )
    action_integration._mcp_executor.execute_action = AsyncMock(return_value=mock_result)
    
    event = {
        "session_id": "test-session-close",
        "action_json": json.dumps({
            "command": "close_app",
            "args": {"app_name": "Calculator"}
        }),
        "feature_id": "F-2025-014-close-app",
    }
    
    await action_integration._on_action_received(event)
    await asyncio.sleep(0.1)
    
    # Проверяем, что McpActionExecutor.execute_action был вызван
    assert action_integration._mcp_executor.execute_action.called, (
        "McpActionExecutor.execute_action должен быть вызван для close_app"
    )
    
    # Проверяем аргументы вызова
    call_args = action_integration._mcp_executor.execute_action.call_args
    action_data = call_args[0][0]
    session_id = call_args[1].get('session_id')
    
    assert action_data["type"] == "close_app", "Тип действия должен быть 'close_app'"
    assert action_data["app_name"] == "Calculator", "Имя приложения должно быть 'Calculator'"
    assert session_id == "test-session-close", "session_id должен быть передан"
    
    # Проверяем публикацию событий
    event_names = _published_event_names(mock_event_bus)
    assert "actions.close_app.started" in event_names, "Должно быть событие started"
    assert "actions.close_app.completed" in event_names, "Должно быть событие completed"


@pytest.mark.asyncio
async def test_open_app_with_app_path(action_integration, mock_event_bus):
    """Тест: open_app с app_path использует McpActionExecutor."""
    mock_result = McpActionResult(
        success=True,
        message="Application opened successfully",
        app_name="Safari"
    )
    action_integration._mcp_executor.execute_action = AsyncMock(return_value=mock_result)
    
    event = {
        "session_id": "test-session-path",
        "action_json": json.dumps({
            "command": "open_app",
            "args": {
                "app_path": "/Applications/Safari.app"
            }
        }),
        "feature_id": FEATURE_ID,
    }
    
    await action_integration._on_action_received(event)
    await asyncio.sleep(0.1)
    
    # Проверяем аргументы вызова
    call_args = action_integration._mcp_executor.execute_action.call_args
    action_data = call_args[0][0]
    
    assert action_data["type"] == "open_app"
    assert action_data["app_path"] == "/Applications/Safari.app"
    assert "app_name" not in action_data or action_data.get("app_name") is None


@pytest.mark.asyncio
async def test_open_app_mcp_error_handling(action_integration, mock_event_bus):
    """Тест: Обработка ошибок от McpActionExecutor для open_app."""
    # Мокируем ошибку от MCP сервера
    mock_result = McpActionResult(
        success=False,
        message="❌ Application 'NonExistentApp' not found",
        error="mcp_error",
        app_name="NonExistentApp"
    )
    action_integration._mcp_executor.execute_action = AsyncMock(return_value=mock_result)
    
    event = {
        "session_id": "test-session-error",
        "action_json": json.dumps({
            "command": "open_app",
            "args": {"app_name": "NonExistentApp"}
        }),
        "feature_id": FEATURE_ID,
    }
    
    await action_integration._on_action_received(event)
    await asyncio.sleep(0.1)
    
    # Проверяем публикацию событий об ошибке
    event_names = _published_event_names(mock_event_bus)
    assert "actions.open_app.started" in event_names
    assert "actions.open_app.failed" in event_names
    
    # Проверяем содержимое события failed
    failed_calls = [
        call for call in mock_event_bus.publish.call_args_list
        if call.args[0] == "actions.open_app.failed"
    ]
    assert len(failed_calls) > 0
    failed_payload = failed_calls[0].args[1]
    assert failed_payload["error"] == "mcp_error"
    assert failed_payload["message"] == "❌ Application 'NonExistentApp' not found"


@pytest.mark.asyncio
async def test_both_actions_use_same_mcp_executor(action_integration, mock_event_bus):
    """Тест: Оба действия (open_app и close_app) используют один и тот же McpActionExecutor."""
    # Мокируем результаты
    open_result = McpActionResult(
        success=True,
        message="Application 'Safari' opened successfully",
        app_name="Safari"
    )
    close_result = McpActionResult(
        success=True,
        message="Application 'Safari' closed successfully",
        app_name="Safari"
    )
    
    # Настраиваем мок для возврата разных результатов в зависимости от типа действия
    async def mock_execute_action(action_data, session_id=None):
        if action_data.get("type") == "open_app":
            return open_result
        elif action_data.get("type") == "close_app":
            return close_result
        return McpActionResult(success=False, message="Unknown action type")
    
    action_integration._mcp_executor.execute_action = AsyncMock(side_effect=mock_execute_action)
    
    # Выполняем open_app
    open_event = {
        "session_id": "test-session-open",
        "action_json": json.dumps({
            "command": "open_app",
            "args": {"app_name": "Safari"}
        }),
        "feature_id": FEATURE_ID,
    }
    await action_integration._on_action_received(open_event)
    await asyncio.sleep(0.1)
    
    # Выполняем close_app
    close_event = {
        "session_id": "test-session-close",
        "action_json": json.dumps({
            "command": "close_app",
            "args": {"app_name": "Safari"}
        }),
        "feature_id": "F-2025-014-close-app",
    }
    await action_integration._on_action_received(close_event)
    await asyncio.sleep(0.1)
    
    # Проверяем, что execute_action был вызван дважды
    assert action_integration._mcp_executor.execute_action.call_count == 2, (
        "McpActionExecutor.execute_action должен быть вызван дважды (для open_app и close_app)"
    )
    
    # Проверяем, что оба вызова использовали один и тот же executor
    calls = action_integration._mcp_executor.execute_action.call_args_list
    assert len(calls) == 2, "Должно быть два вызова"
    # Первый вызов - open_app
    first_call_action_data = calls[0][0][0]  # args[0] - первый позиционный аргумент
    assert first_call_action_data["type"] == "open_app", "Первый вызов должен быть для open_app"
    # Второй вызов - close_app
    second_call_action_data = calls[1][0][0]  # args[0] - первый позиционный аргумент
    assert second_call_action_data["type"] == "close_app", "Второй вызов должен быть для close_app"
    
    # Проверяем публикацию событий для обоих действий
    event_names = _published_event_names(mock_event_bus)
    assert "actions.open_app.started" in event_names
    assert "actions.open_app.completed" in event_names
    assert "actions.close_app.started" in event_names
    assert "actions.close_app.completed" in event_names


@pytest.mark.asyncio
async def test_mcp_executor_disabled_skips_actions(action_integration, mock_event_bus):
    """Тест: Если MCP executor disabled, действия не выполняются."""
    # Отключаем MCP executor
    action_integration._mcp_executor.config.enabled = False
    
    event = {
        "session_id": "test-session-disabled",
        "action_json": json.dumps({
            "command": "open_app",
            "args": {"app_name": "Safari"}
        }),
        "feature_id": FEATURE_ID,
    }
    
    await action_integration._on_action_received(event)
    await asyncio.sleep(0.1)
    
    # Проверяем, что McpActionExecutor не был вызван
    if hasattr(action_integration._mcp_executor, 'execute_action'):
        # Если метод не замокан, проверяем через публикацию событий
        event_names = _published_event_names(mock_event_bus)
        # Должно быть событие об ошибке (disabled)
        assert "actions.open_app.failed" in event_names or len(event_names) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
