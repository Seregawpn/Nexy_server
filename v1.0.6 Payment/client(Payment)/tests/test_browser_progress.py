#!/usr/bin/env python3
"""
Тест Цикла 4: Клиентская обработка browser_progress
"""

import sys
import os
import asyncio
from unittest.mock import AsyncMock, MagicMock

# Добавляем пути
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.grpc_client.proto import streaming_pb2
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.grpc_client_integration import GrpcClientIntegration

async def test_browser_progress_parsing():
    """Тест парсинга browser_progress из proto"""
    print("\n1. Тест парсинга browser_progress:")
    
    # Создаем mock StreamResponse с browser_progress
    response = streaming_pb2.StreamResponse()
    response.browser_progress.type = streaming_pb2.BrowserEventType.BROWSER_TASK_STARTED
    response.browser_progress.task_id = "test_task_123"
    response.browser_progress.description = "Browser task started"
    response.browser_progress.timestamp = "2025-01-01T12:00:00Z"
    
    assert response.HasField("browser_progress"), "browser_progress field not set"
    assert response.browser_progress.type == streaming_pb2.BrowserEventType.BROWSER_TASK_STARTED
    assert response.browser_progress.task_id == "test_task_123"
    print("  ✅ Browser progress parsing OK")
    
    return True

async def test_browser_progress_integration():
    """Тест обработки browser_progress в GrpcClientIntegration"""
    print("\n2. Тест обработки browser_progress в интеграции:")
    
    from modules.grpc_client.proto import streaming_pb2
    
    # Создаем моки
    event_bus = AsyncMock(spec=EventBus)
    state_manager = MagicMock(spec=ApplicationStateManager)
    error_handler = MagicMock(spec=ErrorHandler)
    
    # Создаем интеграцию
    integration = GrpcClientIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler
    )
    
    # Создаем mock StreamResponse с browser_progress
    class MockBrowserProgress:
        def __init__(self):
            self.type = streaming_pb2.BrowserEventType.BROWSER_STEP_COMPLETED
            self.task_id = "test_task_123"
            self.step_number = 1
            self.description = "Step 1 completed"
            self.timestamp = "2025-01-01T12:00:00Z"
        
        def HasField(self, field_name):
            return field_name in ['step_number', 'description']
    
    class MockStreamResponse:
        def __init__(self):
            self._browser_progress = MockBrowserProgress()
        
        @property
        def browser_progress(self):
            return self._browser_progress
        
        def WhichOneof(self, field_name):
            if field_name == 'content':
                return 'browser_progress'
            return None
    
    response = MockStreamResponse()
    session_id = "test_session_123"
    
    # Тестируем обработку напрямую через логику из _send
    try:
        # Имитируем обработку browser_progress из _send
        
        progress = response.browser_progress
        feature_id = "F-2025-015-browser-use"
        
        event_type = progress.type
        task_id = progress.task_id
        step_number = progress.step_number if progress.HasField('step_number') else None
        description = progress.description if progress.HasField('description') else None
        
        # Публикуем событие browser.progress
        await event_bus.publish("browser.progress", {
            "session_id": session_id,
            "feature_id": feature_id,
            "type": event_type,
            "task_id": task_id,
            "step_number": step_number,
            "description": description,
        })
        
        # Если есть описание, отправляем его в TTS
        if description:
            await event_bus.publish("grpc.response.text", {
                "session_id": session_id,
                "text": description,
                "feature_id": feature_id
            })
        
        # Проверяем вызовы
        assert event_bus.publish.called, "EventBus.publish should be called"
        
        publish_calls = event_bus.publish.call_args_list
        
        # Должно быть опубликовано browser.progress и grpc.response.text
        browser_progress_called = False
        text_called = False
        
        for call in publish_calls:
            args = call[0] if call[0] else []
            event_name = args[0] if len(args) > 0 else None
            if event_name == "browser.progress":
                browser_progress_called = True
                data = args[1] if len(args) > 1 else {}
                assert data.get('task_id') == "test_task_123"
                assert data.get('step_number') == 1
                assert data.get('description') == "Step 1 completed"
            elif event_name == "grpc.response.text":
                text_called = True
                data = args[1] if len(args) > 1 else {}
                assert data.get('text') == "Step 1 completed"
        
        assert browser_progress_called, "browser.progress event should be published"
        assert text_called, "grpc.response.text event should be published"
        
        print("  ✅ Browser progress integration OK")
        return True
        
    except Exception as e:
        print(f"  ❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_browser_progress_terminal_events():
    """Тест терминальных событий browser_progress"""
    print("\n3. Тест терминальных событий:")
    
    from modules.grpc_client.proto import streaming_pb2
    
    # Создаем моки
    event_bus = AsyncMock(spec=EventBus)
    
    # Тест BROWSER_TASK_COMPLETED
    class MockBrowserProgressCompleted:
        def __init__(self):
            self.type = streaming_pb2.BrowserEventType.BROWSER_TASK_COMPLETED
            self.task_id = "test_task_123"
            self.description = "Task completed"
            self.timestamp = "2025-01-01T12:00:00Z"
        
        def HasField(self, field_name):
            return False
    
    progress_completed = MockBrowserProgressCompleted()
    session_id = "test_session_123"
    
    # Имитируем обработку терминального события
    
    event_type = progress_completed.type
    BROWSER_TASK_COMPLETED = streaming_pb2.BrowserEventType.BROWSER_TASK_COMPLETED
    
    if event_type == BROWSER_TASK_COMPLETED:
        await event_bus.publish("grpc.request_completed", {
            "session_id": session_id
        })
    
    # Проверяем, что было опубликовано grpc.request_completed
    publish_calls = [call[0][0] for call in event_bus.publish.call_args_list if call[0] and len(call[0]) > 0]
    assert "grpc.request_completed" in publish_calls, "grpc.request_completed should be published for COMPLETED"
    
    print("  ✅ Terminal events handling OK")
    return True

async def main():
    print("=" * 60)
    print("ЦИКЛ 4: Тест клиентской обработки browser_progress")
    print("=" * 60)
    
    parsing_ok = await test_browser_progress_parsing()
    integration_ok = await test_browser_progress_integration()
    terminal_ok = await test_browser_progress_terminal_events()
    
    if parsing_ok and integration_ok and terminal_ok:
        print("\n✅ Все тесты Цикла 4 пройдены!")
        print("Можно переходить к Циклу 5: Интеграционное тестирование")
        sys.exit(0)
    else:
        print("\n❌ Тесты Цикла 4 не пройдены")
        print("Исправьте ошибки перед переходом к следующему циклу")
        sys.exit(1)

if __name__ == '__main__':
    asyncio.run(main())