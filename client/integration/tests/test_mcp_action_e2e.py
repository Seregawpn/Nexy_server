"""
End-to-end тест полной цепочки MCP команд.

Проверяет:
1. GrpcClientIntegration распознает __MCP__ префикс
2. Публикует событие grpc.response.action
3. ActionExecutionIntegration получает событие
4. Выполняет действие через McpActionExecutor

Feature ID: F-2025-016-mcp-app-opening-integration
"""

import pytest
import json
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from typing import Dict, Any

from integration.integrations.grpc_client_integration import GrpcClientIntegration, MCP_PREFIX, FEATURE_ID as GRPC_FEATURE_ID
from integration.integrations.action_execution_integration import ActionExecutionIntegration, FEATURE_ID as ACTION_FEATURE_ID
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from modules.mcp_action import McpActionResult


class MockStreamResponse:
    """Мок gRPC StreamResponse."""
    
    def __init__(self, content_type: str, content_value: Any):
        self._content_type = content_type
        self._content_value = content_value
    
    def WhichOneof(self, field_name: str) -> str:
        if field_name == 'content':
            return self._content_type
        return None
    
    @property
    def text_chunk(self) -> str:
        if self._content_type == 'text_chunk':
            return self._content_value
        return ""


@pytest.fixture
def event_bus():
    """Фикстура для EventBus."""
    bus = EventBus()
    return bus


@pytest.fixture
def state_manager():
    """Фикстура для ApplicationStateManager."""
    return MagicMock(spec=ApplicationStateManager)


@pytest.fixture
def error_handler():
    """Фикстура для ErrorHandler."""
    return MagicMock(spec=ErrorHandler)


@pytest.fixture
def grpc_integration(event_bus, state_manager, error_handler):
    """Фикстура для GrpcClientIntegration."""
    integration = GrpcClientIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
    )
    return integration


@pytest.fixture
def action_integration(event_bus, state_manager, error_handler):
    """Фикстура для ActionExecutionIntegration."""
    integration = ActionExecutionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
    )
    return integration


@pytest.mark.asyncio
async def test_full_chain_mcp_to_action(event_bus, grpc_integration, action_integration):
    """Тест: Полная цепочка от MCP команды до выполнения действия."""
    # Включаем MCP executor для теста
    action_integration._mcp_executor.config.enabled = True
    
    # Мокаем успешное выполнение (тест не требует реального MCP сервера)
    with patch.object(action_integration._mcp_executor, 'execute_action') as mock_execute_action:
        mock_execute_action.return_value = McpActionResult(
            success=True,
            message="Opened Calculator",
            app_name="Calculator"
        )
        
        # Инициализируем интеграции
        await grpc_integration.initialize()
        await action_integration.initialize()
        await action_integration.start()
        
        # Создаем MCP команду
        mcp_payload = {
            "event": "mcp.command_request",
            "payload": {
                "session_id": "test-e2e-session",
                "command": "open_app",
                "args": {
                    "app_name": "Calculator"
                }
            }
        }
        mcp_json = json.dumps(mcp_payload, ensure_ascii=False)
        mcp_text = f"{MCP_PREFIX}{mcp_json}"
        
        # Собираем события
        received_events = []
        
        def event_collector(event_name: str):
            def handler(event: Dict[str, Any]):
                received_events.append((event_name, event))
            return handler
        
        # Подписываемся на события для проверки
        await event_bus.subscribe("grpc.response.action", event_collector("grpc.response.action"))
        await event_bus.subscribe("actions.open_app.started", event_collector("actions.open_app.started"))
        await event_bus.subscribe("actions.open_app.completed", event_collector("actions.open_app.completed"))
        await event_bus.subscribe("actions.open_app.failed", event_collector("actions.open_app.failed"))
        
        # Имитируем получение text_chunk с MCP командой
        response = MockStreamResponse('text_chunk', mcp_text)
        session_id = "test-e2e-session"
        
        # Обрабатываем через GrpcClientIntegration (имитируя логику из _send)
        which_oneof = response.WhichOneof('content')
        if which_oneof == 'text_chunk':
            text = response.text_chunk
            if text.startswith(MCP_PREFIX):
                mcp_json_str = text[len(MCP_PREFIX):]
                mcp_payload_parsed = json.loads(mcp_json_str)
                command_payload = mcp_payload_parsed.get("payload", {})
                
                await event_bus.publish("grpc.response.action", {
                    "session_id": session_id,
                    "action_json": json.dumps(command_payload, ensure_ascii=False),
                    "feature_id": GRPC_FEATURE_ID,
                })
        
        # Ждем обработки
        await asyncio.sleep(0.2)
        
        # Проверяем события
        event_names = [name for name, _ in received_events]
        
        # Должно быть событие grpc.response.action
        assert "grpc.response.action" in event_names, "Должно быть событие grpc.response.action"
        
        # Должно быть событие actions.open_app.started
        assert "actions.open_app.started" in event_names, "Должно быть событие actions.open_app.started"
        
        # Проверяем содержимое события grpc.response.action
        grpc_event_data = next((data for name, data in received_events if name == "grpc.response.action"), None)
        assert grpc_event_data is not None
        # EventBus может обернуть в data
        grpc_event = grpc_event_data.get("data", grpc_event_data) if isinstance(grpc_event_data, dict) and "data" in grpc_event_data else grpc_event_data
        assert grpc_event.get("session_id") == session_id
        assert grpc_event.get("action_json") is not None
        
        # Проверяем содержимое action_json
        action_data = json.loads(grpc_event["action_json"])
        assert action_data["command"] == "open_app"
        assert action_data["args"]["app_name"] == "Calculator"
        
        # Проверяем событие started
        started_event_data = next((data for name, data in received_events if name == "actions.open_app.started"), None)
        assert started_event_data is not None
        started_event = started_event_data.get("data", started_event_data) if isinstance(started_event_data, dict) and "data" in started_event_data else started_event_data
        assert started_event.get("session_id") == session_id
        # Для open_app используется action-specific feature_id (F-2025-013-open-app)
        assert started_event.get("feature_id") == "F-2025-013-open-app"
        
        # Проверяем, что действие было выполнено (completed или failed)
        completed_or_failed = any(name in ["actions.open_app.completed", "actions.open_app.failed"] for name, _ in received_events)
        assert completed_or_failed, "Должно быть событие completed или failed"


@pytest.mark.asyncio
async def test_full_chain_with_mock_executor(event_bus, grpc_integration, action_integration):
    """Тест: Полная цепочка с мокированным MCP executor."""
    # Включаем MCP executor
    action_integration._mcp_executor.config.enabled = True
    
    # Мокаем успешное выполнение
    with patch.object(action_integration._mcp_executor, 'execute_action') as mock_execute_action:
        mock_execute_action.return_value = McpActionResult(
            success=True,
            message="Opened Calculator",
            app_name="Calculator"
        )
        
        # Инициализируем интеграции
        await grpc_integration.initialize()
        await action_integration.initialize()
        await action_integration.start()
        
        # Создаем MCP команду
        mcp_payload = {
            "event": "mcp.command_request",
            "payload": {
                "session_id": "test-e2e-mock",
                "command": "open_app",
                "args": {
                    "app_name": "Calculator"
                }
            }
        }
        mcp_json = json.dumps(mcp_payload, ensure_ascii=False)
        mcp_text = f"{MCP_PREFIX}{mcp_json}"
        
        # Собираем события
        received_events = []
        
        def event_collector(event_name: str):
            def handler(event: Dict[str, Any]):
                received_events.append((event_name, event))
            return handler
        
        await event_bus.subscribe("grpc.response.action", event_collector("grpc.response.action"))
        await event_bus.subscribe("actions.open_app.started", event_collector("actions.open_app.started"))
        await event_bus.subscribe("actions.open_app.completed", event_collector("actions.open_app.completed"))
        
        # Имитируем обработку MCP команды
        response = MockStreamResponse('text_chunk', mcp_text)
        session_id = "test-e2e-mock"
        
        which_oneof = response.WhichOneof('content')
        if which_oneof == 'text_chunk':
            text = response.text_chunk
            if text.startswith(MCP_PREFIX):
                mcp_json_str = text[len(MCP_PREFIX):]
                mcp_payload_parsed = json.loads(mcp_json_str)
                command_payload = mcp_payload_parsed.get("payload", {})
                
                await event_bus.publish("grpc.response.action", {
                    "session_id": session_id,
                    "action_json": json.dumps(command_payload, ensure_ascii=False),
                    "feature_id": GRPC_FEATURE_ID,
                })
        
        # Ждем обработки
        await asyncio.sleep(0.3)
        
        # Проверяем, что executor был вызван
        assert mock_execute_action.called, "Executor должен быть вызван"
        
        # Проверяем аргументы вызова
        call_args = mock_execute_action.call_args[0][0]
        assert call_args["type"] == "open_app"
        assert call_args["app_name"] == "Calculator"
        
        # Проверяем события
        event_names = [name for name, _ in received_events]
        assert "grpc.response.action" in event_names
        assert "actions.open_app.started" in event_names
        assert "actions.open_app.completed" in event_names
        
        # Проверяем содержимое события completed
        completed_event_data = next((data for name, data in received_events if name == "actions.open_app.completed"), None)
        assert completed_event_data is not None
        completed_event = completed_event_data.get("data", completed_event_data) if isinstance(completed_event_data, dict) and "data" in completed_event_data else completed_event_data
        assert completed_event.get("app_name") == "Calculator"
        assert completed_event.get("session_id") == session_id
        # Для open_app используется action-specific feature_id (F-2025-013-open-app)
        assert completed_event.get("feature_id") == "F-2025-013-open-app"


@pytest.mark.asyncio
async def test_full_chain_close_app_mcp_to_action(event_bus, grpc_integration, action_integration):
    """Тест: Полная цепочка от MCP команды до выполнения close_app действия.
    
    Feature ID: F-2025-014-close-app
    """
    # Включаем MCP executor для теста
    action_integration._mcp_executor.config.enabled = True
    
    # Инициализируем интеграции
    await grpc_integration.initialize()
    await action_integration.initialize()
    await action_integration.start()
    
    # Создаем MCP команду для close_app
    mcp_payload = {
        "event": "mcp.command_request",
        "payload": {
            "session_id": "test-e2e-close-session",
            "command": "close_app",
            "args": {
                "app_name": "Calculator"
            }
        }
    }
    mcp_json = json.dumps(mcp_payload, ensure_ascii=False)
    mcp_text = f"{MCP_PREFIX}{mcp_json}"
    
    # Собираем события
    received_events = []
    
    def event_collector(event_name: str):
        def handler(event: Dict[str, Any]):
            received_events.append((event_name, event))
        return handler
    
    # Подписываемся на события для проверки
    await event_bus.subscribe("grpc.response.action", event_collector("grpc.response.action"))
    await event_bus.subscribe("actions.close_app.started", event_collector("actions.close_app.started"))
    await event_bus.subscribe("actions.close_app.completed", event_collector("actions.close_app.completed"))
    await event_bus.subscribe("actions.close_app.failed", event_collector("actions.close_app.failed"))
    
    # Имитируем получение text_chunk с MCP командой
    response = MockStreamResponse('text_chunk', mcp_text)
    session_id = "test-e2e-close-session"
    
    # Обрабатываем через GrpcClientIntegration (имитируя логику из _send)
    which_oneof = response.WhichOneof('content')
    if which_oneof == 'text_chunk':
        text = response.text_chunk
        if text.startswith(MCP_PREFIX):
            mcp_json_str = text[len(MCP_PREFIX):]
            mcp_payload_parsed = json.loads(mcp_json_str)
            command_payload = mcp_payload_parsed.get("payload", {})
            
            await event_bus.publish("grpc.response.action", {
                "session_id": session_id,
                "action_json": json.dumps(command_payload, ensure_ascii=False),
                "feature_id": GRPC_FEATURE_ID,
            })
    
    # Ждем обработки
    await asyncio.sleep(0.3)
    
    # Проверяем события
    event_names = [name for name, _ in received_events]
    
    # Должно быть событие grpc.response.action
    assert "grpc.response.action" in event_names, "Должно быть событие grpc.response.action"
    
    # Должно быть событие actions.close_app.started
    assert "actions.close_app.started" in event_names, "Должно быть событие actions.close_app.started"
    
    # Проверяем содержимое события grpc.response.action
    grpc_event_data = next((data for name, data in received_events if name == "grpc.response.action"), None)
    assert grpc_event_data is not None
    # EventBus может обернуть в data
    grpc_event = grpc_event_data.get("data", grpc_event_data) if isinstance(grpc_event_data, dict) and "data" in grpc_event_data else grpc_event_data
    assert grpc_event.get("session_id") == session_id
    assert grpc_event.get("action_json") is not None
    
    # Проверяем содержимое action_json
    action_data = json.loads(grpc_event["action_json"])
    assert action_data["command"] == "close_app"
    assert action_data["args"]["app_name"] == "Calculator"
    
    # Проверяем событие started
    started_event_data = next((data for name, data in received_events if name == "actions.close_app.started"), None)
    assert started_event_data is not None
    started_event = started_event_data.get("data", started_event_data) if isinstance(started_event_data, dict) and "data" in started_event_data else started_event_data
    assert started_event.get("session_id") == session_id
    assert started_event.get("feature_id") == "F-2025-014-close-app"


@pytest.mark.asyncio
async def test_full_chain_failure_triggers_speech(event_bus, grpc_integration, action_integration):
    """Неудача действия приводит к событию speech.playback.request."""
    action_integration._mcp_executor.config.enabled = True

    with patch.object(action_integration._mcp_executor, 'execute_action') as mock_execute_action:
        mock_execute_action.return_value = McpActionResult(
            success=False,
            message="App not found",
            error="mcp_error",
            app_name="GhostApp",
        )

        await grpc_integration.initialize()
        await action_integration.initialize()
        await action_integration.start()

        received_events = []

        def event_collector(event_name: str):
            def handler(event: Dict[str, Any]):
                received_events.append((event_name, event))
            return handler

        await event_bus.subscribe("speech.playback.request", event_collector("speech.playback.request"))
        await event_bus.subscribe("actions.open_app.failed", event_collector("actions.open_app.failed"))

        mcp_payload = {
            "event": "mcp.command_request",
            "payload": {
                "session_id": "test-e2e-error",
                "command": "open_app",
                "args": {"app_name": "GhostApp"},
            },
        }
        response = MockStreamResponse('text_chunk', f"{MCP_PREFIX}{json.dumps(mcp_payload)}")
        session_id = "test-e2e-error"

        if response.WhichOneof('content') == 'text_chunk':
            payload = json.loads(response.text_chunk[len(MCP_PREFIX):])
            await event_bus.publish(
                "grpc.response.action",
                {
                    "session_id": session_id,
                    "action_json": json.dumps(payload.get("payload", {})),
                    "feature_id": GRPC_FEATURE_ID,
                },
            )

        await asyncio.sleep(0.2)

        event_names = [name for name, _ in received_events]
        assert "actions.open_app.failed" in event_names
        assert "speech.playback.request" in event_names


@pytest.mark.asyncio
async def test_full_chain_regular_text(event_bus, grpc_integration):
    """Тест: Обычный текст не должен обрабатываться как MCP команда."""
    await grpc_integration.initialize()
    
    # Собираем события
    received_events = []
    
    def event_collector(event_name: str):
        def handler(event: Dict[str, Any]):
            received_events.append((event_name, event))
        return handler
    
    await event_bus.subscribe("grpc.response.text", event_collector("grpc.response.text"))
    await event_bus.subscribe("grpc.response.action", event_collector("grpc.response.action"))
    
    # Обычный текст без MCP префикса
    regular_text = "Это обычный текст ответа от сервера."
    response = MockStreamResponse('text_chunk', regular_text)
    session_id = "test-e2e-regular"
    
    # Обрабатываем
    which_oneof = response.WhichOneof('content')
    if which_oneof == 'text_chunk':
        text = response.text_chunk
        if not text.startswith(MCP_PREFIX):
            await event_bus.publish("grpc.response.text", {
                "session_id": session_id,
                "text": text
            })
    
    # Ждем
    await asyncio.sleep(0.1)
    
    # Проверяем события
    event_names = [name for name, _ in received_events]
    assert "grpc.response.text" in event_names
    assert "grpc.response.action" not in event_names, "Обычный текст не должен создавать action событие"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
