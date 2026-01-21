"""
Instance Manager Integration

Интеграция для управления экземплярами приложения и предотвращения дублирования.
Выполняется ПЕРВОЙ и является БЛОКИРУЮЩЕЙ.
"""

import sys
import os
import asyncio
import logging
from typing import Optional, Dict, Any

from modules.instance_manager import InstanceManager, InstanceStatus, InstanceManagerConfig
from integration.core.error_handler import ErrorHandler
from integration.core.state_manager import ApplicationStateManager
from integration.core.event_bus import EventBus

logger = logging.getLogger(__name__)


class InstanceManagerIntegration:
    """Интеграция для управления экземплярами приложения."""
    
    def __init__(self, event_bus: EventBus, state_manager: ApplicationStateManager, 
                 error_handler: ErrorHandler, config: Optional[Dict[str, Any]] = None):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or {}
        
        # Позволяем переопределять путь lock-файла через окружение (удобно в dev/sandbox)
        env_lock_file = os.environ.get("NEXY_INSTANCE_LOCK_FILE")
        if env_lock_file:
            logger.info("[INSTANCE_MANAGER] Using lock file from env NEXY_INSTANCE_LOCK_FILE=%s", env_lock_file)

        lock_file = env_lock_file or self.config.get('lock_file', '~/Library/Application Support/Nexy/nexy.lock')

        # Создаем конфигурацию модуля
        instance_config = InstanceManagerConfig(
            enabled=self.config.get('enabled', True),
            lock_file=lock_file,
            timeout_seconds=self.config.get('timeout_seconds', 30),
            cleanup_on_startup=self.config.get('cleanup_on_startup', True),
            show_duplicate_message=self.config.get('show_duplicate_message', True),
            pid_check=self.config.get('pid_check', True)
        )
        
        self.instance_manager = InstanceManager(instance_config)
        self._initialized = False
        
    async def initialize(self) -> bool:
        """Инициализация интеграции - НЕ БЛОКИРУЮЩАЯ."""
        try:
            # Подписка на события
            await self.event_bus.subscribe("app.startup", self._on_app_startup)
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown)
            await self.event_bus.subscribe("instance.check_request", self._on_instance_check_request)
            
            self._initialized = True
            self._initialized = True
            logger.info("✅ InstanceManagerIntegration инициализирован")
            return True
            
        except Exception as e:
            await self.error_handler.handle(e, category="initialization", severity="error")
            return False
    
    async def start(self) -> bool:
        """Запуск интеграции - БЛОКИРУЮЩИЙ МЕТОД."""
        try:
            logger.info("🚀 InstanceManagerIntegration.start() вызван")
            
            if not self._initialized:
                await self.initialize()
            
            
            # КРИТИЧНО: Проверка дублирования при старте
            logger.info("🔍 Проверка дублирования экземпляров...")
            
            status = await self.instance_manager.check_single_instance()
            logger.info(f"🔍 Результат проверки дублирования: {status}")
            
            if status == InstanceStatus.DUPLICATE:
                # ДУБЛИРОВАНИЕ ОБНАРУЖЕНО - ВОЗВРАЩАЕМ False ДЛЯ КОРРЕКТНОГО ЗАВЕРШЕНИЯ
                logger.warning("❌ Nexy уже запущен! Завершаем дубликат.")
                try:
                    logger.error(
                        "SAFE_EXIT: duplicate_instance lock_file=%s pid=%s",
                        self.instance_manager.lock_file,
                        os.getpid(),
                        stack_info=True,
                    )
                    logger.warning("🚫 InstanceManager: duplicate instance detected — returning False for clean shutdown")
                except Exception:
                    pass
                
                # АУДИО-СИГНАЛ ДЛЯ НЕЗРЯЧИХ ПОЛЬЗОВАТЕЛЕЙ
                try:
                    await self.event_bus.publish("signal.duplicate_instance", {
                        "message": "Nexy уже запущен",
                        "sound": "error"
                    })
                    # Даем время на отправку сигнала
                    await asyncio.sleep(0.1)
                except Exception as e:
                    print(f"⚠️ Не удалось отправить аудио-сигнал: {e}")
                
                if self.instance_manager.config.show_duplicate_message:
                    logger.warning("❌ Nexy уже запущен! Проверьте меню-бар.")
                
                # ВОЗВРАЩАЕМ False: координатор обработает это и вызовет stop() в finally блоке
                # Это обеспечивает корректное завершение через централизованный shutdown
                logger.info("💀 Возвращаем False для корректного завершения через координатор")
                return False
            
            elif status == InstanceStatus.ERROR:
                print("❌ Ошибка проверки дублирования")
                await self.error_handler.handle(
                    Exception("Failed to check instance status"),
                    category="runtime",
                    severity="error"
                )
                return False
            
            # ПЕРВЫЙ ЭКЗЕМПЛЯР - ПРОДОЛЖАЕМ
            print("✅ Дублирование не обнаружено, захватываем блокировку...")
            lock_acquired = await self.instance_manager.acquire_lock()
            
            if not lock_acquired:
                logger.error("❌ Не удалось захватить блокировку")
                await self.error_handler.handle(
                    Exception("Failed to acquire lock"),
                    category="runtime",
                    severity="error"
                )
                return False
            
            logger.info("✅ Nexy запущен успешно (первый экземпляр)")
            
            # Публикация события о успешном запуске
            try:
                lock_info = await self.instance_manager.get_lock_info()
                await self.event_bus.publish("instance.status_checked", {
                    "status": InstanceStatus.SINGLE.value,
                    "lock_info": lock_info
                })
            except Exception as e:
                print(f"⚠️ Не удалось опубликовать событие: {e}")
            
            return True
            
        except Exception as e:
            print(f"❌ Критическая ошибка в InstanceManagerIntegration.start(): {e}")
            import traceback
            traceback.print_exc()
            await self.error_handler.handle(e, category="runtime", severity="critical")
            return False
    
    async def stop(self) -> bool:
        """Остановка интеграции."""
        try:
            # Освобождение блокировки
            if self.instance_manager:
                await self.instance_manager.release_lock()
                print("✅ Блокировка освобождена")
            
            # Отписка от событий
            try:
                await self.event_bus.unsubscribe("app.startup", self._on_app_startup)
                await self.event_bus.unsubscribe("app.shutdown", self._on_app_shutdown)
                await self.event_bus.unsubscribe("instance.check_request", self._on_instance_check_request)
            except Exception as e:
                print(f"⚠️ Ошибка отписки от событий: {e}")
            
            return True
            
        except Exception as e:
            await self.error_handler.handle(e, category="runtime", severity="error")
            return False
    
    # Event handlers
    async def _on_app_startup(self, event: Dict[str, Any]) -> None:
        """Обработчик события запуска приложения."""
        try:
            print("📱 Обработка события app.startup")
            # Дополнительная логика при запуске (если нужна)
        except Exception as e:
            await self.error_handler.handle(e, category="runtime", severity="error")
    
    async def _on_app_shutdown(self, event: Dict[str, Any]) -> None:
        """Обработчик события завершения приложения."""
        try:
            print("📱 Обработка события app.shutdown")
            # Освобождение блокировки при завершении
            await self.stop()
        except Exception as e:
            await self.error_handler.handle(e, category="runtime", severity="error")
    
    async def _on_instance_check_request(self, event: Dict[str, Any]) -> None:
        """Обработчик запроса проверки экземпляра."""
        try:
            print("📱 Обработка события instance.check_request")
            status = await self.instance_manager.check_single_instance()
            
            await self.event_bus.publish("instance.status_response", {
                "status": status.value,
                "timestamp": asyncio.get_event_loop().time()
            })
        except Exception as e:
            await self.error_handler.handle(e, category="runtime", severity="error")
