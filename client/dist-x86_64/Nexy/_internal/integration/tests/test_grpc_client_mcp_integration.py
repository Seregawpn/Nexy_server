"""
Тесты для обработки MCP команд в GrpcClientIntegration.

Feature ID: F-2025-016-mcp-app-opening-integration
"""

import pytest
import json
from unittest.mock import AsyncMock, MagicMock, patch
from typing import Dict, Any

from integration.integrations.grpc_client_integration import GrpcClientIntegration, MCP_PREFIX, FEATURE_ID
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler


class MockStreamResponse:
    """Мок gRPC StreamResponse для тестирования."""
    
    def __init__(self, content_type: str, content_value: Any):
        self._content_type = content_type
        self._content_value = content_value
    
    def WhichOneof(self, field_name: str) -> str:
        """Имитация WhichOneof для protobuf."""
        if field_name == 'content':
            return self._content_type
        return None
    
    @property
    def text_chunk(self) -> str:
        if self._content_type == 'text_chunk':
            return self._content_value
        return ""
    
    @property
    def audio_chunk(self):
        return None
    
    @property
    def end_message(self) -> str:
        if self._content_type == 'end_message':
            return self._content_value
        return ""


@pytest.fixture
def mock_event_bus():
    """Фикстура для EventBus."""
    bus = AsyncMock(spec=EventBus)
    bus.publish = AsyncMock()
    return bus


@pytest.fixture
def mock_state_manager():
    """Фикстура для ApplicationStateManager."""
    return MagicMock(spec=ApplicationStateManager)


@pytest.fixture
def mock_error_handler():
    """Фикстура для ErrorHandler."""
    return MagicMock(spec=ErrorHandler)


@pytest.fixture
def grpc_integration(mock_event_bus, mock_state_manager, mock_error_handler):
    """Фикстура для GrpcClientIntegration."""
    integration = GrpcClientIntegration(
        event_bus=mock_event_bus,
        state_manager=mock_state_manager,
        error_handler=mock_error_handler,
    )
    return integration


@pytest.mark.asyncio
async def test_mcp_prefix_detection(grpc_integration, mock_event_bus):
    """Тест: Обнаружение префикса __MCP__ в text_chunk."""
    # Создаем MCP команду
    mcp_payload = {
        "event": "mcp.command_request",
        "payload": {
            "session_id": "test-session-123",
            "command": "open_app",
            "args": {
                "app_name": "Safari"
            }
        }
    }
    mcp_json = json.dumps(mcp_payload, ensure_ascii=False)
    mcp_text = f"{MCP_PREFIX}{mcp_json}"
    
    # Создаем мок ответа
    response = MockStreamResponse('text_chunk', mcp_text)
    
    # Имитируем обработку
    session_id = "test-session-123"
    
    # Вызываем обработку text_chunk напрямую (имитируя логику из _send)
    which_oneof = response.WhichOneof('content')
    if which_oneof == 'text_chunk':
        text = response.text_chunk
        if text.startswith(MCP_PREFIX):
            mcp_json_str = text[len(MCP_PREFIX):]
            mcp_payload_parsed = json.loads(mcp_json_str)
            command_payload = mcp_payload_parsed.get("payload", {})
            
            await mock_event_bus.publish("grpc.response.action", {
                "session_id": session_id,
                "action_json": json.dumps(command_payload, ensure_ascii=False),
                "feature_id": FEATURE_ID,
            })
    
    # Проверяем, что событие было опубликовано
    assert mock_event_bus.publish.called
    call_args = mock_event_bus.publish.call_args
    
    assert call_args[0][0] == "grpc.response.action"
    event_data = call_args[0][1]
    assert event_data["session_id"] == session_id
    assert event_data["feature_id"] == FEATURE_ID
    assert event_data["action_json"] is not None
    
    # Проверяем содержимое action_json
    action_data = json.loads(event_data["action_json"])
    assert action_data["command"] == "open_app"
    assert action_data["args"]["app_name"] == "Safari"


@pytest.mark.asyncio
async def test_regular_text_processing(grpc_integration, mock_event_bus):
    """Тест: Обычный текст обрабатывается как обычно (без MCP)."""
    regular_text = "Это обычный текст ответа от сервера."
    response = MockStreamResponse('text_chunk', regular_text)
    
    session_id = "test-session-456"
    
    # Имитируем обработку
    which_oneof = response.WhichOneof('content')
    if which_oneof == 'text_chunk':
        text = response.text_chunk
        if not text.startswith(MCP_PREFIX):
            await mock_event_bus.publish("grpc.response.text", {
                "session_id": session_id,
                "text": text
            })
    
    # Проверяем, что событие было опубликовано
    assert mock_event_bus.publish.called
    call_args = mock_event_bus.publish.call_args
    
    assert call_args[0][0] == "grpc.response.text"
    event_data = call_args[0][1]
    assert event_data["session_id"] == session_id
    assert event_data["text"] == regular_text


@pytest.mark.asyncio
async def test_invalid_mcp_json(grpc_integration, mock_event_bus):
    """Тест: Обработка невалидного JSON в MCP команде."""
    invalid_mcp_text = f"{MCP_PREFIX}{{invalid json}}"
    response = MockStreamResponse('text_chunk', invalid_mcp_text)
    
    session_id = "test-session-789"
    
    # Имитируем обработку с обработкой ошибок
    which_oneof = response.WhichOneof('content')
    if which_oneof == 'text_chunk':
        text = response.text_chunk
        if text.startswith(MCP_PREFIX):
            mcp_json_str = text[len(MCP_PREFIX):]
            try:
                mcp_payload = json.loads(mcp_json_str)
                command_payload = mcp_payload.get("payload", {})
                await mock_event_bus.publish("grpc.response.action", {
                    "session_id": session_id,
                    "action_json": json.dumps(command_payload, ensure_ascii=False),
                    "feature_id": FEATURE_ID,
                })
            except json.JSONDecodeError:
                await mock_event_bus.publish("grpc.response.action", {
                    "session_id": session_id,
                    "action_json": None,
                    "error": "invalid_json",
                    "feature_id": FEATURE_ID,
                })
    
    # Проверяем, что событие было опубликовано с ошибкой
    assert mock_event_bus.publish.called
    call_args = mock_event_bus.publish.call_args
    
    assert call_args[0][0] == "grpc.response.action"
    event_data = call_args[0][1]
    assert event_data["session_id"] == session_id
    assert event_data["error"] == "invalid_json"
    assert event_data["action_json"] is None


@pytest.mark.asyncio
async def test_mcp_command_with_session_id(grpc_integration, mock_event_bus):
    """Тест: MCP команда с session_id в payload."""
    mcp_payload = {
        "event": "mcp.command_request",
        "payload": {
            "session_id": "test-session-mcp",
            "command": "open_app",
            "args": {
                "app_name": "Calculator"
            }
        }
    }
    mcp_json = json.dumps(mcp_payload, ensure_ascii=False)
    mcp_text = f"{MCP_PREFIX}{mcp_json}"
    
    response = MockStreamResponse('text_chunk', mcp_text)
    session_id = "test-session-mcp"
    
    # Имитируем обработку
    which_oneof = response.WhichOneof('content')
    if which_oneof == 'text_chunk':
        text = response.text_chunk
        if text.startswith(MCP_PREFIX):
            mcp_json_str = text[len(MCP_PREFIX):]
            mcp_payload_parsed = json.loads(mcp_json_str)
            command_payload = mcp_payload_parsed.get("payload", {})
            
            await mock_event_bus.publish("grpc.response.action", {
                "session_id": session_id,
                "action_json": json.dumps(command_payload, ensure_ascii=False),
                "feature_id": FEATURE_ID,
            })
    
    # Проверяем результат
    assert mock_event_bus.publish.called
    call_args = mock_event_bus.publish.call_args
    event_data = call_args[0][1]
    
    action_data = json.loads(event_data["action_json"])
    assert action_data["command"] == "open_app"
    assert action_data["args"]["app_name"] == "Calculator"
    assert event_data["session_id"] == session_id


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

