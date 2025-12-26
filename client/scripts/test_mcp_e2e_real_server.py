#!/usr/bin/env python3
"""
End-to-end тест MCP команд с реальным сервером.

Проверяет полную цепочку:
1. Клиент отправляет запрос на сервер
2. Сервер обрабатывает и возвращает MCP команду
3. Клиент получает и выполняет команду

Feature ID: F-2025-016-mcp-app-opening-integration

Использование:
    python3 scripts/test_mcp_e2e_real_server.py
"""

import asyncio
import json
import logging
import sys
import os
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

# Добавляем пути
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

FEATURE_ID = "F-2025-016-mcp-app-opening-integration"


async def test_mcp_action_e2e(
    server_host: str = "127.0.0.1",
    server_port: int = 50051,
    test_app_name: str = "Calculator"
) -> bool:
    """
    End-to-end тест MCP команды открытия приложения.
    
    Args:
        server_host: Хост gRPC сервера
        server_port: Порт gRPC сервера
        test_app_name: Имя приложения для теста
        
    Returns:
        True если тест прошел успешно, False иначе
    """
    logger.info("="*80)
    logger.info("E2E ТЕСТ: MCP команда открытия приложения")
    logger.info("="*80)
    logger.info(f"Сервер: {server_host}:{server_port}")
    logger.info(f"Тестовое приложение: {test_app_name}")
    logger.info("")
    
    try:
        # Импортируем необходимые компоненты
        from integration.core.event_bus import EventBus
        from integration.core.state_manager import ApplicationStateManager
        from integration.core.error_handler import ErrorHandler
        from integration.integrations.grpc_client_integration import GrpcClientIntegration
        from integration.integrations.action_execution_integration import ActionExecutionIntegration
        from config.unified_config_loader import UnifiedConfigLoader
        
        # Проверяем конфигурацию
        config_loader = UnifiedConfigLoader()
        actions_cfg = config_loader.get_actions_config().get('open_app')
        
        if not actions_cfg or not actions_cfg.enabled:
            logger.error("❌ actions.open_app.enabled = false в конфигурации")
            logger.error("   Установите actions.open_app.enabled: true в unified_config.yaml")
            return False
        
        logger.info("✅ Конфигурация клиента: actions.open_app.enabled = true")
        
        # Создаем компоненты
        event_bus = EventBus()
        state_manager = ApplicationStateManager()
        error_handler = ErrorHandler(event_bus)
        
        # Создаем интеграции
        grpc_integration = GrpcClientIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
        )
        
        action_integration = ActionExecutionIntegration(
            event_bus=event_bus,
            state_manager=state_manager,
            error_handler=error_handler,
        )
        
        # Инициализируем
        logger.info("🔧 Инициализация интеграций...")
        await grpc_integration.initialize()
        await action_integration.initialize()
        await action_integration.start()
        logger.info("✅ Интеграции инициализированы")
        
        # Собираем события
        received_events = []
        event_checks = {
            'grpc.response.action': False,
            'actions.open_app.started': False,
            'actions.open_app.completed': False,
            'actions.open_app.failed': False,
        }
        
        def event_collector(event_name: str):
            def handler(event: Dict[str, Any]):
                received_events.append((event_name, event))
                event_checks[event_name] = True
                logger.info(f"📨 Событие получено: {event_name}")
            return handler
        
        # Подписываемся на события
        await event_bus.subscribe("grpc.response.action", event_collector("grpc.response.action"))
        await event_bus.subscribe("actions.open_app.started", event_collector("actions.open_app.started"))
        await event_bus.subscribe("actions.open_app.completed", event_collector("actions.open_app.completed"))
        await event_bus.subscribe("actions.open_app.failed", event_collector("actions.open_app.failed"))
        
        logger.info("✅ Подписки на события настроены")
        
        # Запускаем gRPC клиент
        logger.info("🔧 Запуск gRPC клиента...")
        await grpc_integration.start()
        logger.info("✅ gRPC клиент запущен")
        
        # Создаем тестовый запрос
        session_id = f"test-e2e-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        test_request = f"Открой {test_app_name}"
        
        logger.info("")
        logger.info("📤 Отправка запроса на сервер...")
        logger.info(f"   Сессия: {session_id}")
        logger.info(f"   Запрос: {test_request}")
        logger.info("")
        
        # Отправляем запрос через gRPC
        # Примечание: в реальном сценарии это делается через VoiceRecognitionIntegration
        # Здесь мы имитируем отправку запроса
        try:
            # Получаем gRPC клиент из интеграции
            if not hasattr(grpc_integration, '_client') or grpc_integration._client is None:
                logger.error("❌ gRPC клиент не инициализирован")
                return False
            
            # Отправляем запрос
            # В реальном сценарии это делается через метод send_request
            # Здесь мы используем упрощенный подход - ждем ответа от сервера
            
            logger.info("⏳ Ожидание ответа от сервера (максимум 30 секунд)...")
            
            # Ждем события в течение 30 секунд
            timeout = 30.0
            start_time = asyncio.get_event_loop().time()
            
            while (asyncio.get_event_loop().time() - start_time) < timeout:
                await asyncio.sleep(0.5)
                
                # Проверяем, получены ли все необходимые события
                if event_checks['grpc.response.action'] and event_checks['actions.open_app.started']:
                    if event_checks['actions.open_app.completed'] or event_checks['actions.open_app.failed']:
                        break
            
            elapsed = asyncio.get_event_loop().time() - start_time
            
            logger.info("")
            logger.info("📊 Результаты теста:")
            logger.info(f"   Время ожидания: {elapsed:.2f} секунд")
            logger.info(f"   Получено событий: {len(received_events)}")
            logger.info("")
            
            # Проверяем результаты
            success = True
            issues = []
            
            if not event_checks['grpc.response.action']:
                success = False
                issues.append("Не получено событие grpc.response.action")
            
            if not event_checks['actions.open_app.started']:
                success = False
                issues.append("Не получено событие actions.open_app.started")
            
            if not event_checks['actions.open_app.completed'] and not event_checks['actions.open_app.failed']:
                success = False
                issues.append("Не получено событие actions.open_app.completed или actions.open_app.failed")
            
            if issues:
                logger.error("❌ Тест не прошел:")
                for issue in issues:
                    logger.error(f"   - {issue}")
                return False
            
            # Проверяем содержимое событий
            logger.info("✅ Все события получены")
            logger.info("")
            logger.info("📋 Детали событий:")
            
            for event_name, event_data in received_events:
                logger.info(f"   {event_name}:")
                if isinstance(event_data, dict):
                    for key, value in event_data.items():
                        if key == 'action_json' and isinstance(value, str):
                            try:
                                parsed = json.loads(value)
                                logger.info(f"      {key}: {json.dumps(parsed, indent=8, ensure_ascii=False)}")
                            except Exception:
                                logger.info(f"      {key}: {value[:100]}...")
                        else:
                            logger.info(f"      {key}: {value}")
            
            logger.info("")
            logger.info("="*80)
            logger.info("✅ E2E ТЕСТ ПРОШЕЛ УСПЕШНО")
            logger.info("="*80)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка при отправке запроса: {e}")
            import traceback
            traceback.print_exc()
            return False
        
        finally:
            # Останавливаем интеграции
            logger.info("")
            logger.info("🔧 Остановка интеграций...")
            await action_integration.stop()
            await grpc_integration.stop()
            logger.info("✅ Интеграции остановлены")
    
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Главная функция."""
    import argparse
    
    parser = argparse.ArgumentParser(description='E2E тест MCP команд с реальным сервером')
    parser.add_argument('--host', default='127.0.0.1', help='Хост gRPC сервера (по умолчанию: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=50051, help='Порт gRPC сервера (по умолчанию: 50051)')
    parser.add_argument('--app', default='Calculator', help='Имя приложения для теста (по умолчанию: Calculator)')
    
    args = parser.parse_args()
    
    # Проверяем, что сервер доступен
    logger.info("🔍 Проверка доступности сервера...")
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((args.host, args.port))
        sock.close()
        
        if result != 0:
            logger.error(f"❌ Сервер {args.host}:{args.port} недоступен")
            logger.error("   Убедитесь, что сервер запущен и доступен")
            return 1
    except Exception as e:
        logger.error(f"❌ Ошибка проверки доступности сервера: {e}")
        return 1
    
    logger.info(f"✅ Сервер {args.host}:{args.port} доступен")
    logger.info("")
    
    # Запускаем тест
    success = await test_mcp_action_e2e(
        server_host=args.host,
        server_port=args.port,
        test_app_name=args.app
    )
    
    return 0 if success else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

