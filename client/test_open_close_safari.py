#!/usr/bin/env python3
"""
Тест открытия и закрытия Safari через MCP.

Feature ID: F-2025-016-mcp-app-opening-integration, F-2025-014-close-app
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


async def test_open_close_safari():
    """Тест открытия и закрытия Safari через MCP."""
    print("=== Тест открытия и закрытия Safari через MCP ===\n")
    
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
    await event_bus.subscribe("actions.close_app.started", create_event_handler("actions.close_app.started"))
    await event_bus.subscribe("actions.close_app.completed", create_event_handler("actions.close_app.completed"))
    await event_bus.subscribe("actions.close_app.failed", create_event_handler("actions.close_app.failed"))
    
    # Шаг 1: Открываем Safari
    print("🚀 Шаг 1: Открываем Safari...\n")
    
    open_event = {
        "session_id": "test-safari-open",
        "action_json": json.dumps({
            "command": "open_app",
            "args": {"app_name": "Safari"}
        }),
        "feature_id": FEATURE_ID,
    }
    
    await integration._on_action_received(open_event)
    await asyncio.sleep(2)  # Ждем открытия
    
    # Проверяем результат открытия
    event_names = [name for name, _ in received_events]
    if "actions.open_app.completed" in event_names:
        print("✅ Safari успешно открыт!\n")
    elif "actions.open_app.failed" in event_names:
        print("❌ Ошибка при открытии Safari\n")
        await integration.stop()
        return False
    else:
        print("⚠️  Не получено событие о завершении открытия\n")
    
    # Шаг 2: Ждем немного перед закрытием
    print("⏳ Ждем 3 секунды перед закрытием...\n")
    await asyncio.sleep(3)
    
    # Шаг 3: Закрываем Safari
    print("🚪 Шаг 2: Закрываем Safari...\n")
    
    close_event = {
        "session_id": "test-safari-close",
        "action_json": json.dumps({
            "command": "close_app",
            "args": {"app_name": "Safari"}
        }),
        "feature_id": "F-2025-014-close-app",
    }
    
    await integration._on_action_received(close_event)
    await asyncio.sleep(2)  # Ждем закрытия
    
    # Проверяем результат закрытия
    event_names = [name for name, _ in received_events]
    if "actions.close_app.completed" in event_names:
        print("✅ Safari успешно закрыт!\n")
    elif "actions.close_app.failed" in event_names:
        print("❌ Ошибка при закрытии Safari\n")
        await integration.stop()
        return False
    else:
        print("⚠️  Не получено событие о завершении закрытия\n")
    
    # Итоги
    print("=== Итоги ===")
    print(f"Всего получено событий: {len(received_events)}")
    
    open_success = "actions.open_app.completed" in event_names
    close_success = "actions.close_app.completed" in event_names
    
    if open_success and close_success:
        print("✅ Все операции выполнены успешно!")
        result = True
    else:
        print("⚠️  Некоторые операции не завершились успешно")
        result = False
    
    # Останавливаем интеграцию
    await integration.stop()
    
    return result


if __name__ == "__main__":
    try:
        success = asyncio.run(test_open_close_safari())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⚠️  Тест прерван пользователем")
        sys.exit(1)
    except Exception as exc:
        print(f"\n❌ Ошибка при выполнении теста: {exc}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
