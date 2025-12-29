#!/usr/bin/env python3
"""
Тест открытия приложения через MCP интеграцию.

Feature ID: F-2025-016-mcp-app-opening-integration
"""

import asyncio
import json
import sys
from pathlib import Path

# Добавляем путь к client
client_root = Path(__file__).parent
sys.path.insert(0, str(client_root))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.action_execution_integration import ActionExecutionIntegration, FEATURE_ID


async def test_open_app_via_mcp():
    """Тест открытия приложения через MCP."""
    print("=== Тест открытия приложения через MCP ===\n")
    
    # Создаем компоненты
    event_bus = EventBus()
    state_manager = ApplicationStateManager()
    error_handler = ErrorHandler()
    
    # Создаем интеграцию
    integration = ActionExecutionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
    )
    
    # Включаем MCP executor
    integration._mcp_executor.config.enabled = True
    
    # Инициализируем и запускаем
    await integration.initialize()
    await integration.start()
    
    # Собираем события
    received_events = []
    
    def create_event_handler(event_name: str):
        def handler(event_data):
            received_events.append((event_name, event_data))
            print(f"📢 Событие: {event_name}")
            if isinstance(event_data, dict):
                if "message" in event_data:
                    print(f"   Сообщение: {event_data['message']}")
                if "error" in event_data:
                    print(f"   Ошибка: {event_data['error']}")
        return handler
    
    # Подписываемся на события
    await event_bus.subscribe("actions.open_app.started", create_event_handler("actions.open_app.started"))
    await event_bus.subscribe("actions.open_app.completed", create_event_handler("actions.open_app.completed"))
    await event_bus.subscribe("actions.open_app.failed", create_event_handler("actions.open_app.failed"))
    
    # Создаем событие для открытия приложения
    app_name = sys.argv[1] if len(sys.argv) > 1 else "Calculator"
    event = {
        "session_id": "test-mcp-open-session",
        "action_json": json.dumps({
            "command": "open_app",
            "args": {"app_name": app_name}
        }),
        "feature_id": FEATURE_ID,
    }
    
    print(f"🚀 Отправляем команду открытия {app_name}...\n")
    
    # Отправляем событие
    await integration._on_action_received(event)
    
    # Ждем выполнения
    await asyncio.sleep(2)
    
    # Проверяем результаты
    print(f"\n=== Результаты ===")
    print(f"Получено событий: {len(received_events)}")
    
    event_names = [name for name, _ in received_events]
    
    if "actions.open_app.completed" in event_names:
        print("✅ Приложение успешно открыто через MCP!")
        completed_event = next(data for name, data in received_events if name == "actions.open_app.completed")
        if isinstance(completed_event, dict):
            print(f"   Сообщение: {completed_event.get('message', 'N/A')}")
    elif "actions.open_app.failed" in event_names:
        print("❌ Ошибка при открытии приложения")
        failed_event = next(data for name, data in received_events if name == "actions.open_app.failed")
        if isinstance(failed_event, dict):
            print(f"   Ошибка: {failed_event.get('error', 'N/A')}")
            print(f"   Сообщение: {failed_event.get('message', 'N/A')}")
    else:
        print("⚠️  Не получено событие о завершении")
    
    # Останавливаем интеграцию
    await integration.stop()
    
    return "actions.open_app.completed" in event_names


if __name__ == "__main__":
    try:
        success = asyncio.run(test_open_app_via_mcp())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️  Тест прерван пользователем")
        sys.exit(1)
    except Exception as exc:
        print(f"\n❌ Ошибка при выполнении теста: {exc}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
