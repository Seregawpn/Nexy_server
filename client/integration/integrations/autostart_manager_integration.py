"""
AutostartManagerIntegration - Минимальная интеграция для управления автозапуском
Поскольку автозапуск уже настроен через PKG LaunchAgent, эта интеграция только мониторит статус
"""

import asyncio
from dataclasses import dataclass
import logging
import os
from typing import Any

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from modules.autostart_manager.core.autostart_manager import AutostartManager
from modules.autostart_manager.core.types import AutostartConfig, AutostartStatus

# Импорт конфигурации

logger = logging.getLogger(__name__)


@dataclass
class AutostartManagerIntegrationConfig:
    """Конфигурация AutostartManagerIntegration"""

    check_interval: float = 60.0  # Проверка каждую минуту
    monitor_enabled: bool = True
    auto_repair: bool = False  # Не чиним автоматически - PKG управляет
    launch_agent_path: str = "~/Library/LaunchAgents/com.nexy.assistant.plist"
    bundle_id: str = "com.nexy.assistant"
    cleanup_legacy_launch_agent: bool = False
    legacy_launch_agent_path: str = (
        "/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist"
    )
    legacy_launch_agent_label: str = "com.sergiyzasorin.nexy.voiceassistant"


class AutostartManagerIntegration:
    """
    Минимальная интеграция autostart_manager

    ВАЖНО: Автозапуск настроен через PKG LaunchAgent!
    Эта интеграция только мониторит статус, не управляет.
    """

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: dict[str, Any] | None = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler

        # Конфигурация
        config = config or {}
        self.config = AutostartManagerIntegrationConfig(
            check_interval=config.get("check_interval", 60.0),
            monitor_enabled=config.get("monitor_enabled", True),
            auto_repair=config.get("auto_repair", False),
            launch_agent_path=config.get(
                "launch_agent_path", "~/Library/LaunchAgents/com.nexy.assistant.plist"
            ),
            bundle_id=config.get("bundle_id", "com.nexy.assistant"),
            cleanup_legacy_launch_agent=config.get("cleanup_legacy_launch_agent", False),
            legacy_launch_agent_path=config.get(
                "legacy_launch_agent_path",
                "/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist",
            ),
            legacy_launch_agent_label=config.get(
                "legacy_launch_agent_label",
                "com.sergiyzasorin.nexy.voiceassistant",
            ),
        )

        self._autostart_manager = AutostartManager(
            AutostartConfig(
                enabled=True,
                method="launch_agent",
                launch_agent_path=self.config.launch_agent_path,
                bundle_id=self.config.bundle_id,
            )
        )

        # Состояние
        self.is_initialized = False
        self.is_running = False
        self._monitor_task: asyncio.Task[Any] | None = None

        logger.info("AutostartManagerIntegration created (мониторинг LaunchAgent)")

    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            logger.info("🔧 Инициализация AutostartManagerIntegration")

            # Подписываемся на события
            await self.event_bus.subscribe("app.startup", self._on_app_startup, EventPriority.LOW)
            await self.event_bus.subscribe(
                "autostart.check_status", self._on_check_status, EventPriority.MEDIUM
            )

            self.is_initialized = True
            logger.info("✅ AutostartManagerIntegration инициализирован")
            return True

        except Exception as e:
            logger.error(f"❌ Ошибка инициализации AutostartManagerIntegration: {e}")
            return False

    async def start(self) -> bool:
        """Запуск интеграции"""
        try:
            if not self.is_initialized:
                logger.error("❌ AutostartManagerIntegration не инициализирован")
                return False

            if self.is_running:
                logger.warning("⚠️ AutostartManagerIntegration уже запущен")
                return True

            logger.info("🚀 Запуск AutostartManagerIntegration")

            # Проверяем текущий статус автозапуска
            await self._check_autostart_status()

            # Запускаем мониторинг если включен
            if self.config.monitor_enabled:
                self._monitor_task = asyncio.create_task(self._monitor_autostart())

            self.is_running = True
            logger.info("✅ AutostartManagerIntegration запущен")
            return True

        except Exception as e:
            logger.error(f"❌ Ошибка запуска AutostartManagerIntegration: {e}")
            return False

    async def stop(self) -> bool:
        """Остановка интеграции"""
        try:
            if not self.is_running:
                return True

            logger.info("⏹️ Остановка AutostartManagerIntegration")

            # Останавливаем мониторинг
            if self._monitor_task and not self._monitor_task.done():
                self._monitor_task.cancel()
                try:
                    await self._monitor_task
                except asyncio.CancelledError:
                    pass

            self.is_running = False
            logger.info("✅ AutostartManagerIntegration остановлен")
            return True

        except Exception as e:
            logger.error(f"❌ Ошибка остановки AutostartManagerIntegration: {e}")
            return False

    async def _on_app_startup(self, event):
        """Обработка события запуска приложения"""
        try:
            logger.info("📱 App startup - проверяем статус автозапуска")
            await self._check_autostart_status()
        except Exception as e:
            logger.error(f"❌ Ошибка обработки app.startup: {e}")

    async def _on_check_status(self, event):
        """Обработка запроса проверки статуса"""
        try:
            await self._check_autostart_status()
        except Exception as e:
            logger.error(f"❌ Ошибка проверки статуса: {e}")

    async def _check_autostart_status(self):
        """Проверка статуса автозапуска"""
        try:
            # Проверяем LaunchAgent
            launch_agent_path = os.path.expanduser(self.config.launch_agent_path)
            launch_agent_exists = os.path.exists(launch_agent_path)
            legacy_launch_agent_path = os.path.expanduser(self.config.legacy_launch_agent_path)
            legacy_launch_agent_exists = os.path.exists(legacy_launch_agent_path)

            # Публикуем статус
            status_data = {
                "launch_agent_exists": launch_agent_exists,
                "launch_agent_path": launch_agent_path,
                "method": "launch_agent",
                "managed_by": "PKG installer",
                "legacy_launch_agent_exists": legacy_launch_agent_exists,
                "legacy_launch_agent_path": legacy_launch_agent_path,
                "legacy_cleanup_enabled": bool(self.config.cleanup_legacy_launch_agent),
            }

            await self.event_bus.publish("autostart.status_checked", status_data)

            if launch_agent_exists:
                logger.info("✅ LaunchAgent автозапуск настроен корректно")
            else:
                logger.warning("⚠️ LaunchAgent автозапуск не найден")
            if legacy_launch_agent_exists:
                logger.warning(
                    "⚠️ Detected legacy LaunchAgent (duplicate autostart): %s",
                    legacy_launch_agent_path,
                )
                if self.config.cleanup_legacy_launch_agent:
                    logger.info("🧹 Attempting legacy LaunchAgent cleanup")
                    removed = await self._autostart_manager.cleanup_legacy_launch_agent(
                        legacy_path=legacy_launch_agent_path,
                        legacy_label=self.config.legacy_launch_agent_label,
                    )
                    if removed:
                        logger.info("✅ Legacy LaunchAgent removed")
                    else:
                        logger.warning("⚠️ Legacy LaunchAgent removal failed (permissions?)")
                if self.config.auto_repair:
                    logger.info("🔧 Пытаемся восстановить LaunchAgent (auto_repair=true)")
                    result = await self._autostart_manager.enable_autostart()
                    if result == AutostartStatus.ENABLED:
                        logger.info("✅ LaunchAgent восстановлен")
                    else:
                        logger.warning("⚠️ Не удалось восстановить LaunchAgent")

        except Exception as e:
            logger.error(f"❌ Ошибка проверки автозапуска: {e}")

    async def _monitor_autostart(self):
        """Мониторинг автозапуска"""
        try:
            while self.is_running:
                await self._check_autostart_status()
                await asyncio.sleep(self.config.check_interval)

        except asyncio.CancelledError:
            logger.info("🔄 Мониторинг автозапуска остановлен")
        except Exception as e:
            logger.error(f"❌ Ошибка мониторинга автозапуска: {e}")
