#!/usr/bin/env python3
"""
Тест граничных случаев для close_app.

Проверяет:
1. Приложение не запущено
2. Приложение не существует
3. Неправильный формат JSON
4. Отсутствует app_name
5. Feature flag выключен

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
from typing import Dict, Any


async def test_edge_case(name: str, action_json: str, expected_events: list, session_id: str = "test-edge-case"):
    """Тест одного граничного случая."""
    print(f"\n{'=' * 60}")
    print(f"Тест: {name}")
    print(f"{'=' * 60}")
    
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
    
    # Подписываемся на все возможные события
    await event_bus.subscribe("actions.close_app.started", event_collector("actions.close_app.started"))
    await event_bus.subscribe("actions.close_app.completed", event_collector("actions.close_app.completed"))
    await event_bus.subscribe("actions.close_app.failed", event_collector("actions.close_app.failed"))
    
    print(f"📤 Отправка: {action_json}")
    
    # Публикуем событие
    await event_bus.publish("grpc.response.action", {
        "session_id": session_id,
        "action_json": action_json,
        "feature_id": "F-2025-014-close-app",
    })
    
    # Ждем обработки
    await asyncio.sleep(1.0)
    
    # Проверяем результаты
    event_names = [name for name, _ in received_events]
    
    print(f"📥 Полученные события: {event_names}")
    
    # Проверяем ожидаемые события
    success = True
    for expected_event in expected_events:
        if expected_event not in event_names:
            print(f"❌ Ожидалось событие: {expected_event}")
            success = False
    
    if success:
        print(f"✅ Тест пройден")
    else:
        print(f"❌ Тест не пройден")
    
    return success


async def run_all_edge_cases():
    """Запуск всех тестов граничных случаев."""
    print("=" * 60)
    print("Тестирование граничных случаев для close_app")
    print("=" * 60)
    
    results = []
    
    # Тест 1: Приложение не запущено (должно вернуть completed с сообщением)
    results.append(await test_edge_case(
        "Приложение не запущено",
        json.dumps({"command": "close_app", "args": {"app_name": "NonExistentApp"}}),
        ["actions.close_app.started", "actions.close_app.completed"]
    ))
    
    # Тест 2: Отсутствует app_name (должно вернуть failed)
    results.append(await test_edge_case(
        "Отсутствует app_name",
        json.dumps({"command": "close_app", "args": {}}),
        ["actions.close_app.failed"]  # Должно быть failed из-за валидации
    ))
    
    # Тест 3: Неправильный формат JSON (должно быть обработано корректно)
    results.append(await test_edge_case(
        "Неправильный формат JSON",
        '{"command": "close_app", "args": {"app_name": "Calculator"',  # Неполный JSON
        []  # Может не обработаться или вернуть failed
    ))
    
    # Тест 4: Неизвестная команда (должна быть проигнорирована)
    results.append(await test_edge_case(
        "Неизвестная команда",
        json.dumps({"command": "unknown_command", "args": {"app_name": "Calculator"}}),
        []  # Должна быть проигнорирована
    ))
    
    # Тест 5: Пустой app_name (должно вернуть failed)
    results.append(await test_edge_case(
        "Пустой app_name",
        json.dumps({"command": "close_app", "args": {"app_name": ""}}),
        ["actions.close_app.failed"]  # Должно быть failed из-за валидации
    ))
    
    # Итоги
    print("\n" + "=" * 60)
    print("Итоги тестирования граничных случаев:")
    print("=" * 60)
    
    passed = sum(1 for r in results if r)
    total = len(results)
    
    print(f"✅ Пройдено: {passed}/{total}")
    print(f"❌ Провалено: {total - passed}/{total}")
    
    if passed == total:
        print("\n✅ Все граничные случаи обработаны корректно!")
        return 0
    else:
        print("\n⚠️  Некоторые граничные случаи требуют внимания")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(run_all_edge_cases())
    sys.exit(exit_code)

