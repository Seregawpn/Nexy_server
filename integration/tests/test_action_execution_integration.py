"""
Тесты для ActionExecutionIntegration.

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
from modules.action_executor import ActionResult


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
    return integration


@pytest.mark.asyncio
async def test_initialization(action_integration):
    """Тест: Инициализация интеграции."""
    result = await action_integration.initialize()
    assert result is True
    assert action_integration.is_initialized is True


@pytest.mark.asyncio
async def test_start_disabled_executor(action_integration, mock_event_bus):
    """Тест: Запуск при disabled executor."""
    # Executor по умолчанию disabled
    result = await action_integration.initialize()
    assert result is True
    
    result = await action_integration.start()
    assert result is True
    
    # Не должно быть подписок, если executor disabled
    # (но start все равно возвращает True)


@pytest.mark.asyncio
async def test_start_enabled_executor(action_integration, mock_event_bus):
    """Тест: Запуск при enabled executor."""
    # Включаем executor
    action_integration._executor._config.enabled = True
    
    result = await action_integration.initialize()
    assert result is True
    
    result = await action_integration.start()
    assert result is True
    
    # Проверяем подписки
    assert mock_event_bus.subscribe.called
    subscribe_calls = [call[0][0] for call in mock_event_bus.subscribe.call_args_list]
    assert "grpc.response.action" in subscribe_calls
    assert "interrupt.request" in subscribe_calls
    assert "keyboard.short_press" in subscribe_calls


@pytest.mark.asyncio
async def test_on_action_received_disabled(action_integration, mock_event_bus):
    """Тест: Получение действия при disabled executor."""
    event = {
        "session_id": "test-session-1",
        "action_json": json.dumps({"command": "open_app", "args": {"app_name": "Safari"}}),
        "feature_id": FEATURE_ID,
    }
    
    await action_integration._on_action_received(event)
    
    # Должно быть опубликовано событие об ошибке
    assert mock_event_bus.publish.called
    publish_calls = [call[0][0] for call in mock_event_bus.publish.call_args_list]
    assert "actions.open_app.failed" in publish_calls


@pytest.mark.asyncio
async def test_on_action_received_invalid_payload(action_integration, mock_event_bus):
    """Тест: Получение действия с невалидным payload."""
    action_integration._executor._config.enabled = True
    
    # Нет session_id
    event = {
        "action_json": json.dumps({"command": "open_app", "args": {"app_name": "Safari"}}),
    }
    
    await action_integration._on_action_received(event)
    
    # Не должно быть публикаций (только логирование ошибки)
    # Проверяем, что не было публикации started
    publish_calls = [call[0][0] for call in mock_event_bus.publish.call_args_list]
    assert "actions.open_app.started" not in publish_calls


@pytest.mark.asyncio
async def test_on_action_received_invalid_json(action_integration, mock_event_bus):
    """Тест: Получение действия с невалидным JSON."""
    action_integration._executor._config.enabled = True
    
    event = {
        "session_id": "test-session-2",
        "action_json": "{invalid json}",
        "feature_id": FEATURE_ID,
    }
    
    await action_integration._on_action_received(event)
    
    # Должно быть опубликовано событие об ошибке
    assert mock_event_bus.publish.called
    publish_calls = [call[0][0] for call in mock_event_bus.publish.call_args_list]
    assert "actions.open_app.failed" in publish_calls
    
    # Проверяем содержимое события
    failed_call = next(
        call for call in mock_event_bus.publish.call_args_list
        if call[0][0] == "actions.open_app.failed"
    )
    event_data = failed_call[0][1]
    assert event_data["error"] == "invalid_json"


@pytest.mark.asyncio
async def test_on_action_received_success(action_integration, mock_event_bus):
    """Тест: Успешное получение и выполнение действия."""
    action_integration._executor._config.enabled = True
    
    # Мокаем успешное выполнение
    with patch.object(action_integration._executor, 'execute') as mock_execute:
        mock_execute.return_value = ActionResult(
            success=True,
            message="Opened Safari",
            app_name="Safari"
        )
        
        event = {
            "session_id": "test-session-3",
            "action_json": json.dumps({
                "command": "open_app",
                "args": {"app_name": "Safari"}
            }),
            "feature_id": FEATURE_ID,
        }
        
        await action_integration._on_action_received(event)
        
        # Ждем выполнения задачи
        await asyncio.sleep(0.1)
        
        # Проверяем, что executor был вызван
        assert mock_execute.called
        
        # Проверяем аргументы вызова
        call_args = mock_execute.call_args[0][0]
        assert call_args["type"] == "open_app"
        assert call_args["app_name"] == "Safari"
        
        # Проверяем публикацию событий
        assert mock_event_bus.publish.called
        publish_calls = [call[0][0] for call in mock_event_bus.publish.call_args_list]
        assert "actions.open_app.started" in publish_calls
        assert "actions.open_app.completed" in publish_calls


@pytest.mark.asyncio
async def test_on_action_received_failed_execution(action_integration, mock_event_bus):
    """Тест: Неудачное выполнение действия."""
    action_integration._executor._config.enabled = True
    
    # Мокаем неудачное выполнение
    with patch.object(action_integration._executor, 'execute') as mock_execute:
        mock_execute.return_value = ActionResult(
            success=False,
            message="App not found",
            error="not_found",
            app_name="UnknownApp"
        )
        
        event = {
            "session_id": "test-session-4",
            "action_json": json.dumps({
                "command": "open_app",
                "args": {"app_name": "UnknownApp"}
            }),
            "feature_id": FEATURE_ID,
        }
        
        await action_integration._on_action_received(event)
        
        # Ждем выполнения задачи
        await asyncio.sleep(0.1)
        
        # Проверяем публикацию событий
        assert mock_event_bus.publish.called
        publish_calls = [call[0][0] for call in mock_event_bus.publish.call_args_list]
        assert "actions.open_app.started" in publish_calls
        assert "actions.open_app.failed" in publish_calls


@pytest.mark.asyncio
async def test_duplicate_action_prevention(action_integration, mock_event_bus):
    """Тест: Предотвращение дублирования действий для одной сессии."""
    action_integration._executor._config.enabled = True
    
    with patch.object(action_integration._executor, 'execute') as mock_execute:
        mock_execute.return_value = ActionResult(
            success=True,
            message="Opened Safari",
            app_name="Safari"
        )
        
        event = {
            "session_id": "test-session-5",
            "action_json": json.dumps({
                "command": "open_app",
                "args": {"app_name": "Safari"}
            }),
            "feature_id": FEATURE_ID,
        }
        
        # Отправляем два события для одной сессии
        await action_integration._on_action_received(event)
        await action_integration._on_action_received(event)
        
        # Ждем выполнения
        await asyncio.sleep(0.1)
        
        # Executor должен быть вызван только один раз
        assert mock_execute.call_count == 1


@pytest.mark.asyncio
async def test_cancel_all_actions(action_integration, mock_event_bus):
    """Тест: Отмена всех действий."""
    action_integration._executor._config.enabled = True
    
    # Создаем активные задачи
    task1 = asyncio.create_task(asyncio.sleep(10))
    task2 = asyncio.create_task(asyncio.sleep(10))
    
    async with action_integration._actions_lock:
        action_integration._active_actions["session-1"] = task1
        action_integration._active_actions["session-2"] = task2
    
    # Отменяем все действия
    await action_integration._cancel_all_actions(reason="test")
    
    # Проверяем, что задачи отменены
    assert task1.cancelled() or task1.done()
    assert task2.cancelled() or task2.done()
    
    # Проверяем, что список активных действий очищен
    async with action_integration._actions_lock:
        assert len(action_integration._active_actions) == 0


@pytest.mark.asyncio
async def test_stop_integration(action_integration, mock_event_bus):
    """Тест: Остановка интеграции."""
    action_integration._executor._config.enabled = True
    
    await action_integration.initialize()
    await action_integration.start()
    
    result = await action_integration.stop()
    assert result is True
    
    # Проверяем отписки
    assert mock_event_bus.unsubscribe.called
    unsubscribe_calls = [call[0][0] for call in mock_event_bus.unsubscribe.call_args_list]
    assert "grpc.response.action" in unsubscribe_calls
    assert "interrupt.request" in unsubscribe_calls
    assert "keyboard.short_press" in unsubscribe_calls


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

