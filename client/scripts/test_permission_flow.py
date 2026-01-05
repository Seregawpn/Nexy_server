#!/usr/bin/env python3
"""
Headless тест permission flow БЕЗ UI/tray.

Запускает FirstRunPermissionsIntegration изолированно с корректной инициализацией
всех зависимостей (EventBus, StateManager, ErrorHandler).

Использование:
    python scripts/test_permission_flow.py [--skip-flag]

Опции:
    --skip-flag   Пропустить проверку first_run флага (всегда запускать permission flow)

Что тестируется:
    1. Проверка статусов всех разрешений
    2. Активация запроса разрешений
    3. Polling-цикл с ожиданием решения пользователя
    4. Публикация events (permissions.changed, permissions.status_checked)
    5. Таймауты для Settings-разрешений
"""

import asyncio
import sys
import os
import logging
import signal
import time
from pathlib import Path
from typing import Optional

# Добавляем путь к клиенту
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Настройка логирования ДО импорта модулей
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("test_permission_flow")

# Импортируем зависимости
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.integrations.first_run_permissions_integration import (
    FirstRunPermissionsIntegration
)


class PermissionFlowTestHarness:
    """
    Минимальный harness для изолированного тестирования permission flow.
    
    Создаёт все необходимые зависимости и запускает FirstRunPermissionsIntegration
    через стандартный lifecycle: initialize() → start().
    """
    
    def __init__(self, skip_flag: bool = False):
        self.skip_flag = skip_flag
        self._shutdown_event = asyncio.Event()
        
        # Создаём зависимости
        logger.info("🔧 Создание зависимостей...")
        self.event_bus = EventBus()
        self.state_manager = ApplicationStateManager(self.event_bus)
        self.error_handler = ErrorHandler(self.event_bus)
        
        # Конфигурация - более короткие таймауты для тестирования
        self.config = {
            "enabled": True,
            "max_wait_after_settings_open_sec": 30.0,  # Уменьшаем для быстрого теста
        }
        
        # Создаём интеграцию
        self.integration: Optional[FirstRunPermissionsIntegration] = None
        
    def _setup_event_listeners(self):
        """Подписаться на события для мониторинга."""
        
        @self.event_bus.on("permissions.changed")
        async def on_permissions_changed(event):
            data = event.get("data", {})
            permission = data.get("permission", "?")
            old_status = data.get("old_status", "?")
            new_status = data.get("new_status", "?")
            is_timeout = data.get("is_timeout", False)
            
            if is_timeout:
                logger.warning(
                    f"⏱️  permissions.changed [TIMEOUT]: {permission} "
                    f"({old_status} → {new_status})"
                )
            else:
                logger.info(
                    f"📢 permissions.changed: {permission} "
                    f"({old_status} → {new_status})"
                )
        
        @self.event_bus.on("permissions.status_checked")
        async def on_status_checked(event):
            data = event.get("data", {})
            permission = data.get("permission", "?")
            status = data.get("status", "?")
            logger.debug(f"🔍 permissions.status_checked: {permission} = {status}")
        
        @self.event_bus.on("permissions.first_run_completed")
        async def on_first_run_completed(event):
            logger.info("✅ permissions.first_run_completed!")
            self._shutdown_event.set()
        
        @self.event_bus.on("system.restart_required")
        async def on_restart_required(event):
            logger.warning("🔄 system.restart_required (не выполняем в тесте)")
            self._shutdown_event.set()
        
        logger.info("📡 Event listeners настроены")
    
    def _remove_flag_if_needed(self):
        """Удалить first_run флаг если указан --skip-flag."""
        if not self.skip_flag:
            return
        
        try:
            from config.paths import get_user_data_dir
            data_dir = get_user_data_dir("Nexy")
            flag_file = data_dir / "permissions_first_run_completed.flag"
            
            if flag_file.exists():
                flag_file.unlink()
                logger.info(f"🗑️  Удалён флаг: {flag_file}")
            else:
                logger.info(f"ℹ️  Флаг не существует: {flag_file}")
        except Exception as e:
            logger.warning(f"⚠️  Не удалось удалить флаг: {e}")
    
    async def run(self):
        """Запустить тест permission flow."""
        print("\n" + "=" * 80)
        print("🧪 HEADLESS PERMISSION FLOW TEST")
        print("=" * 80)
        print()
        print("Этот скрипт запускает FirstRunPermissionsIntegration изолированно.")
        print("Следите за логами — они покажут весь permission flow.")
        print()
        print("Ctrl+C для остановки")
        print("-" * 80)
        print()
        
        # Удаляем флаг если нужно
        self._remove_flag_if_needed()
        
        # Настраиваем event listeners
        self._setup_event_listeners()
        
        # Создаём и инициализируем интеграцию
        logger.info("🚀 Создание FirstRunPermissionsIntegration...")
        self.integration = FirstRunPermissionsIntegration(
            event_bus=self.event_bus,
            state_manager=self.state_manager,
            error_handler=self.error_handler,
            config=self.config,
        )
        
        # Initialize
        logger.info("📦 Вызов initialize()...")
        await self.integration.initialize()
        
        # Start (это запустит permission flow если first_run)
        logger.info("▶️  Вызов start()...")
        await self.integration.start()
        
        # Ждём завершения или shutdown
        logger.info("⏳ Ожидание завершения permission flow...")
        try:
            await asyncio.wait_for(self._shutdown_event.wait(), timeout=300.0)
        except asyncio.TimeoutError:
            logger.warning("⏱️  Таймаут ожидания (5 минут)")
        
        # Cleanup
        logger.info("🛑 Остановка...")
        await self.integration.stop()
        
        print()
        print("=" * 80)
        print("✅ ТЕСТ ЗАВЕРШЁН")
        print("=" * 80)


async def main():
    """Главная функция."""
    skip_flag = "--skip-flag" in sys.argv
    
    harness = PermissionFlowTestHarness(skip_flag=skip_flag)
    
    # Обработчик Ctrl+C
    def signal_handler(sig, frame):
        logger.info("📡 Получен сигнал остановки")
        harness._shutdown_event.set()
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        await harness.run()
    except KeyboardInterrupt:
        logger.info("⏹️  Прервано пользователем")
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}", exc_info=True)
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
