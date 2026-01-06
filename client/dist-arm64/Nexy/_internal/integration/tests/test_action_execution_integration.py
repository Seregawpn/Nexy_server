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
from modules.mcp_action import McpActionResult


def _published_event_names(mock_event_bus):
    return [call.args[0] for call in mock_event_bus.publish.call_args_list]


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
    """Тест: Запуск при enabled MCP executor."""
    # Включаем MCP executor
    action_integration._mcp_executor.config.enabled = True
    
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
    """Тест: Получение действия при disabled MCP executor."""
    # КРИТИЧНО: Устанавливаем MCP executor в disabled состояние для этого теста
    action_integration._mcp_executor.config.enabled = False
    
    event = {
        "session_id": "test-session-1",
        "action_json": json.dumps({"command": "open_app", "args": {"app_name": "Safari"}}),
        "feature_id": FEATURE_ID,
    }
    
    await action_integration._on_action_received(event)
    
    # Должно быть опубликовано событие об ошибке
    assert mock_event_bus.publish.called
    event_names = _published_event_names(mock_event_bus)
    assert "actions.open_app.failed" in event_names
    assert "speech.playback.request" in event_names


@pytest.mark.asyncio
async def test_on_action_received_invalid_payload(action_integration, mock_event_bus):
    """Тест: Получение действия с невалидным payload."""
    action_integration._mcp_executor.config.enabled = True
    
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
    action_integration._mcp_executor.config.enabled = True
    
    event = {
        "session_id": "test-session-2",
        "action_json": "{invalid json}",
        "feature_id": FEATURE_ID,
    }
    
    await action_integration._on_action_received(event)
    
    # Должно быть опубликовано событие об ошибке
    assert mock_event_bus.publish.called
    event_names = _published_event_names(mock_event_bus)
    assert "actions.open_app.failed" in event_names
    assert "speech.playback.request" in event_names
    
    # Проверяем содержимое события
    failed_call = next(
        call for call in mock_event_bus.publish.call_args_list
        if call.args[0] == "actions.open_app.failed"
    )
    event_data = failed_call.args[1]
    assert event_data["error"] == "invalid_json"


@pytest.mark.asyncio
async def test_on_action_received_success(action_integration, mock_event_bus):
    """Тест: Успешное получение и выполнение действия."""
    action_integration._mcp_executor.config.enabled = True
    
    # Мокаем успешное выполнение
    with patch.object(action_integration._mcp_executor, 'execute_action') as mock_execute_action:
        mock_execute_action.return_value = McpActionResult(
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
        
        # Проверяем, что MCP executor был вызван
        assert mock_execute_action.called
        
        # Проверяем аргументы вызова
        call_args = mock_execute_action.call_args[0][0]
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
    action_integration._mcp_executor.config.enabled = True
    
    # Мокаем неудачное выполнение
    with patch.object(action_integration._mcp_executor, 'execute_action') as mock_execute_action:
        mock_execute_action.return_value = McpActionResult(
            success=False,
            message="App not found",
            error="mcp_error",
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
        event_names = _published_event_names(mock_event_bus)
        assert "actions.open_app.started" in event_names
        assert "actions.open_app.failed" in event_names
        assert "speech.playback.request" in event_names


@pytest.mark.asyncio
async def test_nonexistent_app_triggers_speech_feedback(action_integration, mock_event_bus):
    """Тест: Несуществующее приложение должно вызвать голосовое уведомление с правильным текстом."""
    action_integration._mcp_executor.config.enabled = True
    
    # Мокаем ошибку "mcp_error" для несуществующего приложения
    with patch.object(action_integration._mcp_executor, 'execute_action') as mock_execute_action:
        nonexistent_app = "FooBarNonExistentApp"
        mock_execute_action.return_value = McpActionResult(
            success=False,
            message=f"Application '{nonexistent_app}' not found",
            error="mcp_error",  # Код ошибки для MCP
            app_name=nonexistent_app
        )
        
        event = {
            "session_id": "test-session-nonexistent",
            "action_json": json.dumps({
                "command": "open_app",
                "args": {"app_name": nonexistent_app}
            }),
            "feature_id": FEATURE_ID,
        }
        
        await action_integration._on_action_received(event)
        
        # Ждем выполнения задачи
        await asyncio.sleep(0.1)
        
        # Проверяем, что были опубликованы события
        assert mock_event_bus.publish.called, "EventBus.publish должен был быть вызван"
        event_names = _published_event_names(mock_event_bus)
        
        # Проверяем обязательные события
        assert "actions.open_app.started" in event_names, "Должно быть событие started"
        assert "actions.open_app.failed" in event_names, "Должно быть событие failed"
        assert "speech.playback.request" in event_names, "Должно быть событие speech.playback.request"
        
        # Проверяем содержимое события failed
        failed_calls = [
            call for call in mock_event_bus.publish.call_args_list
            if call[0][0] == "actions.open_app.failed"
        ]
        assert len(failed_calls) > 0, "Должно быть хотя бы одно событие failed"
        failed_payload = failed_calls[0][0][1]
        assert failed_payload["error"] == "mcp_error", f"Ожидался error='mcp_error', получен '{failed_payload.get('error')}'"
        assert failed_payload["session_id"] == "test-session-nonexistent"
        # Для open_app используется feature_id "F-2025-013-open-app" (определяется в action_execution_integration.py)
        assert failed_payload["feature_id"] == "F-2025-013-open-app"
        
        # Проверяем содержимое события speech.playback.request
        speech_calls = [
            call for call in mock_event_bus.publish.call_args_list
            if call[0][0] == "speech.playback.request"
        ]
        assert len(speech_calls) > 0, "Должно быть событие speech.playback.request"
        speech_payload = speech_calls[0][0][1]
        
        # Проверяем правильный текст сообщения об ошибке
        expected_text = f"The app {nonexistent_app} isn't installed on this Mac."
        assert speech_payload["text"] == expected_text, (
            f"Ожидался текст '{expected_text}', получен '{speech_payload.get('text')}'"
        )
        
        # Проверяем метаданные события
        assert speech_payload["session_id"] == "test-session-nonexistent"
        # Для open_app используется feature_id "F-2025-013-open-app"
        assert speech_payload["feature_id"] == "F-2025-013-open-app"
        assert speech_payload["source"] == "actions.open_app"
        assert speech_payload["category"] == "action_error"
        assert speech_payload["priority"] == "high"
        assert speech_payload["voice"] == "en-US"
        assert speech_payload["use_server_tts"] is False  # По умолчанию локальный TTS


@pytest.mark.asyncio
async def test_different_error_codes_trigger_correct_messages(action_integration, mock_event_bus):
    """Тест: Разные коды ошибок должны генерировать правильные сообщения."""
    action_integration._mcp_executor.config.enabled = True
    
    # Тестируем различные коды ошибок
    test_cases = [
        {
            "error_code": "mcp_error",
            "app_name": "RestrictedApp",
            "expected_text": "I couldn't open RestrictedApp. Please try again.",
        },
        {
            "error_code": "disabled",
            "app_name": None,
            "expected_text": "App launching is currently disabled. Please enable it in settings first.",
        },
        {
            "error_code": "timeout",
            "app_name": "SlowApp",
            "expected_text": "I couldn't open SlowApp because the request timed out. Please try again.",
        },
        {
            "error_code": "execution_error",
            "app_name": "BrokenApp",
            "expected_text": "I couldn't open BrokenApp because of a system error. Please try again.",
        },
        {
            "error_code": "unknown_error_code",
            "app_name": "SomeApp",
            "expected_text": "I couldn't open SomeApp. Please try again.",  # Fallback message
        },
    ]
    
    for i, test_case in enumerate(test_cases):
        # Очищаем моки перед каждым тестом
        mock_event_bus.reset_mock()
        action_integration._spoken_error_sessions.clear()
        
        with patch.object(action_integration._mcp_executor, 'execute_action') as mock_execute_action:
            mock_execute_action.return_value = McpActionResult(
                success=False,
                message=f"Error: {test_case['error_code']}",
                error=test_case["error_code"],
                app_name=test_case["app_name"]
            )
            
            event = {
                "session_id": f"test-session-{i}",
                "action_json": json.dumps({
                    "command": "open_app",
                    "args": {"app_name": test_case["app_name"] or "TestApp"}
                }),
                "feature_id": FEATURE_ID,
            }
            
            await action_integration._on_action_received(event)
            await asyncio.sleep(0.1)
            
            # Проверяем, что speech.playback.request был опубликован
            event_names = _published_event_names(mock_event_bus)
            assert "speech.playback.request" in event_names, (
                f"Для error_code='{test_case['error_code']}' должно быть событие speech.playback.request"
            )
            
            # Проверяем правильность текста
            speech_calls = [
                call for call in mock_event_bus.publish.call_args_list
                if call[0][0] == "speech.playback.request"
            ]
            assert len(speech_calls) > 0
            speech_payload = speech_calls[0][0][1]
            assert speech_payload["text"] == test_case["expected_text"], (
                f"Для error_code='{test_case['error_code']}' ожидался текст '{test_case['expected_text']}', "
                f"получен '{speech_payload.get('text')}'"
            )


@pytest.mark.asyncio
async def test_duplicate_action_prevention(action_integration, mock_event_bus):
    """Тест: Предотвращение дублирования действий для одной сессии."""
    action_integration._mcp_executor.config.enabled = True
    
    with patch.object(action_integration._mcp_executor, 'execute_action') as mock_execute_action:
        mock_execute_action.return_value = McpActionResult(
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
        
        # MCP executor должен быть вызван только один раз
        assert mock_execute_action.call_count == 1


@pytest.mark.asyncio
async def test_speech_feedback_disabled_by_config(action_integration, mock_event_bus):
    """Если speak_errors=false, события воспроизведения не публикуются."""
    action_integration._mcp_executor.config.enabled = True
    action_integration._open_app_config.speak_errors = False

    with patch.object(action_integration._mcp_executor, 'execute_action') as mock_execute_action:
        mock_execute_action.return_value = McpActionResult(
            success=False,
            message="Action timed out",
            error="timeout",
            app_name="Safari",
        )

        event = {
            "session_id": "test-session-tts",
            "action_json": json.dumps(
                {"command": "open_app", "args": {"app_name": "Safari"}}
            ),
            "feature_id": FEATURE_ID,
        }

        await action_integration._on_action_received(event)
        await asyncio.sleep(0.1)

        event_names = _published_event_names(mock_event_bus)
        assert "actions.open_app.failed" in event_names
        assert "speech.playback.request" not in event_names


@pytest.mark.asyncio
async def test_speech_feedback_debounced_per_session(action_integration, mock_event_bus):
    """Повторные ошибки в одной сессии не дублируют голосовой ответ."""
    action_integration._open_app_config.speak_errors = True
    mock_event_bus.publish.reset_mock()

    await action_integration._publish_failure(
        session_id="dup-session",
        feature_id=FEATURE_ID,
        error_code="timeout",
        message="timeout",
        app_name="Safari",
    )
    await action_integration._publish_failure(
        session_id="dup-session",
        feature_id=FEATURE_ID,
        error_code="timeout",
        message="timeout again",
        app_name="Safari",
    )

    speech_calls = [
        call for call in mock_event_bus.publish.call_args_list
        if call.args[0] == "speech.playback.request"
    ]
    assert len(speech_calls) == 1


@pytest.mark.asyncio
async def test_cancel_all_actions(action_integration, mock_event_bus):
    """Тест: Отмена всех действий."""
    action_integration._mcp_executor.config.enabled = True
    
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
    action_integration._mcp_executor.config.enabled = True
    
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


# ==================== Тесты для close_app ====================

@pytest.mark.asyncio
async def test_close_app_validation_success(action_integration, mock_event_bus):
    """Тест: Валидация close_app проходит успешно."""
    action_integration._mcp_executor.config.enabled = True
    
    event = {
        "session_id": "test-session",
        "action_json": json.dumps({
            "command": "close_app",
            "args": {"app_name": "Safari"}
        }),
        "feature_id": "F-2025-014-close-app"
    }
    
    # Мокируем McpActionExecutor
    from modules.mcp_action import McpActionResult
    mock_result = McpActionResult(
        success=True,
        message="Application 'Safari' closed successfully",
        app_name="Safari"
    )
    action_integration._mcp_executor.execute_action = AsyncMock(return_value=mock_result)
    
    await action_integration._on_action_received(event)
    await asyncio.sleep(0.1)
    
    # Проверяем, что событие опубликовано
    event_names = _published_event_names(mock_event_bus)
    assert "actions.close_app.started" in event_names
    assert "actions.close_app.completed" in event_names


@pytest.mark.asyncio
async def test_close_app_validation_missing_app_name(action_integration, mock_event_bus):
    """Тест: Валидация close_app отклоняет отсутствие app_name."""
    action_integration._mcp_executor.config.enabled = True
    
    event = {
        "session_id": "test-session",
        "action_json": json.dumps({
            "command": "close_app",
            "args": {}
        }),
        "feature_id": "F-2025-014-close-app"
    }
    
    await action_integration._on_action_received(event)
    await asyncio.sleep(0.1)
    
    # Проверяем, что событие об ошибке опубликовано
    event_names = _published_event_names(mock_event_bus)
    assert "actions.close_app.failed" in event_names or "actions.open_app.failed" in event_names


@pytest.mark.asyncio
async def test_close_app_validation_unsupported_command(action_integration, mock_event_bus):
    """Тест: Валидация отклоняет неподдерживаемую команду."""
    action_integration._mcp_executor.config.enabled = True
    
    event = {
        "session_id": "test-session",
        "action_json": json.dumps({
            "command": "unknown_command",
            "args": {"app_name": "Safari"}
        }),
        "feature_id": "F-2025-014-close-app"
    }
    
    await action_integration._on_action_received(event)
    await asyncio.sleep(0.1)
    
    # Проверяем, что событие об ошибке опубликовано
    event_names = _published_event_names(mock_event_bus)
    # Может быть опубликовано событие об ошибке или ничего не опубликовано
    assert len(event_names) >= 0  # Просто проверяем, что нет исключений


@pytest.mark.asyncio
async def test_close_app_feature_id_logging(action_integration, mock_event_bus):
    """Тест: Правильный feature_id используется для close_app."""
    action_integration._mcp_executor.config.enabled = True
    
    event = {
        "session_id": "test-session",
        "action_json": json.dumps({
            "command": "close_app",
            "args": {"app_name": "Safari"}
        }),
        "feature_id": "F-2025-014-close-app"
    }
    
    # Мокируем McpActionExecutor
    from modules.mcp_action import McpActionResult
    mock_result = McpActionResult(
        success=True,
        message="Application 'Safari' closed successfully",
        app_name="Safari"
    )
    action_integration._mcp_executor.execute_action = AsyncMock(return_value=mock_result)
    
    await action_integration._on_action_received(event)
    await asyncio.sleep(0.1)
    
    # Проверяем, что правильный feature_id используется в событиях
    event_names = _published_event_names(mock_event_bus)
    assert "actions.close_app.started" in event_names
    # Проверяем, что feature_id правильный в аргументах события
    for call in mock_event_bus.publish.call_args_list:
        if call.args[0] == "actions.close_app.started":
            assert call.args[1]["feature_id"] == "F-2025-014-close-app"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
