#!/usr/bin/env python3
"""
E2E тест для полного цикла close_app.

Проверяет:
1. Получение команды от сервера (симуляция)
2. Парсинг и валидацию
3. Выполнение через MCP сервер
4. Обработку результатов

Feature ID: F-2025-014-close-app
"""

import asyncio
import json
import sys
from pathlib import Path

# Добавляем корень проекта в путь
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root / "client(prod)"))

from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.action_execution_integration import ActionExecutionIntegration
from unittest.mock import MagicMock


async def test_close_app_e2e():
    """E2E тест для close_app."""
    print("=" * 60)
    print("E2E тест: close_app полный цикл")
    print("=" * 60)
    print()
    
    # Создаем компоненты
    event_bus = EventBus()
    state_manager = MagicMock(spec=ApplicationStateManager)
    error_handler = MagicMock(spec=ErrorHandler)
    
    # Создаем интеграцию
    integration = ActionExecutionIntegration(
        event_bus=event_bus,
        state_manager=state_manager,
        error_handler=error_handler,
    )
    
    # Инициализируем
    await integration.initialize()
    await integration.start()
    
    # Собираем события
    received_events = []
    
    def event_collector(event_name: str):
        def handler(event: Dict[str, Any]):
            received_events.append((event_name, event))
        return handler
    
    # Подписываемся на события
    await event_bus.subscribe("actions.close_app.started", event_collector("actions.close_app.started"))
    await event_bus.subscribe("actions.close_app.completed", event_collector("actions.close_app.completed"))
    await event_bus.subscribe("actions.close_app.failed", event_collector("actions.close_app.failed"))
    
    # Создаем тестовую команду
    session_id = "test-e2e-close-app"
    action_json = json.dumps({
        "command": "close_app",
        "args": {
            "app_name": "Calculator"
        }
    }, ensure_ascii=False)
    
    print(f"📤 Отправка команды: {action_json}")
    print()
    
    # Публикуем событие grpc.response.action (симуляция получения от сервера)
    await event_bus.publish("grpc.response.action", {
        "session_id": session_id,
        "action_json": action_json,
        "feature_id": "F-2025-014-close-app",
    })
    
    # Ждем обработки
    print("⏳ Ожидание обработки...")
    await asyncio.sleep(2.0)
    
    # Проверяем результаты
    print()
    print("=" * 60)
    print("Результаты:")
    print("=" * 60)
    
    event_names = [name for name, _ in received_events]
    
    if "actions.close_app.started" in event_names:
        print("✅ Событие actions.close_app.started получено")
        started_event = next((data for name, data in received_events if name == "actions.close_app.started"), None)
        if started_event:
            event_data = started_event.get("data", started_event) if isinstance(started_event, dict) and "data" in started_event else started_event
            print(f"   Session ID: {event_data.get('session_id')}")
            print(f"   Feature ID: {event_data.get('feature_id')}")
    else:
        print("❌ Событие actions.close_app.started НЕ получено")
    
    if "actions.close_app.completed" in event_names:
        print("✅ Событие actions.close_app.completed получено")
        completed_event = next((data for name, data in received_events if name == "actions.close_app.completed"), None)
        if completed_event:
            event_data = completed_event.get("data", completed_event) if isinstance(completed_event, dict) and "data" in completed_event else completed_event
            print(f"   Message: {event_data.get('message')}")
            print(f"   App Name: {event_data.get('app_name')}")
    elif "actions.close_app.failed" in event_names:
        print("⚠️  Событие actions.close_app.failed получено")
        failed_event = next((data for name, data in received_events if name == "actions.close_app.failed"), None)
        if failed_event:
            event_data = failed_event.get("data", failed_event) if isinstance(failed_event, dict) and "data" in failed_event else failed_event
            print(f"   Error: {event_data.get('error_code')}")
            print(f"   Message: {event_data.get('message')}")
    else:
        print("❌ События completed/failed НЕ получены")
    
    print()
    print("=" * 60)
    
    # Проверяем успешность
    success = "actions.close_app.completed" in event_names
    if success:
        print("✅ E2E тест пройден успешно!")
        return 0
    else:
        print("❌ E2E тест не прошел")
        return 1


if __name__ == "__main__":
    from typing import Dict, Any
    exit_code = asyncio.run(test_close_app_e2e())
    sys.exit(exit_code)


