"""
AutostartManagerIntegration - интеграция мониторинга/обслуживания автозапуска.
Упаковка не создает LaunchAgent; интеграция работает от runtime-конфига.
"""

import asyncio
from dataclasses import dataclass
import logging
import os
from pathlib import Path
from typing import Any

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core.selectors import (
    get_state_value,
    is_first_run_in_progress,
    is_update_in_progress,
)
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager
from integration.utils.resource_path import get_user_data_dir
from modules.autostart_manager.core.autostart_manager import AutostartManager
from modules.autostart_manager.core.types import AutostartConfig, AutostartStatus

# Импорт конфигурации

logger = logging.getLogger(__name__)

@dataclass
class AutostartManagerIntegrationConfig:
    """Конфигурация AutostartManagerIntegration"""
    check_interval: float = 60.0  # Проверка каждую минуту
    monitor_enabled: bool = True
    auto_repair: bool = False  # По умолчанию только мониторинг, без auto-repair.
    launch_agent_path: str = "~/Library/LaunchAgents/com.nexy.assistant.plist"
    bundle_id: str = "com.nexy.assistant"
    cleanup_legacy_launch_agent: bool = False
    legacy_launch_agent_path: str = "/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist"
    legacy_launch_agent_label: str = "com.sergiyzasorin.nexy.voiceassistant"

class AutostartManagerIntegration:
    """
    Интеграция autostart_manager.

    По умолчанию выполняет мониторинг статуса LaunchAgent.
    При auto_repair=true может восстановить LaunchAgent.
    """
    
    def __init__(self, event_bus: EventBus, state_manager: ApplicationStateManager, 
                 error_handler: ErrorHandler, config: dict[str, Any] | None = None):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        
        # Конфигурация
        config = config or {}
        self.config = AutostartManagerIntegrationConfig(
            check_interval=config.get('check_interval', 60.0),
            monitor_enabled=config.get('monitor_enabled', True),
            auto_repair=config.get('auto_repair', False),
            launch_agent_path=config.get('launch_agent_path', "~/Library/LaunchAgents/com.nexy.assistant.plist"),
            bundle_id=config.get('bundle_id', "com.nexy.assistant"),
            cleanup_legacy_launch_agent=config.get('cleanup_legacy_launch_agent', False),
            legacy_launch_agent_path=config.get(
                'legacy_launch_agent_path',
                "/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist",
            ),
            legacy_launch_agent_label=config.get(
                'legacy_launch_agent_label',
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
        self._status_check_lock = asyncio.Lock()
        self._user_opt_out_flag_path: Path = get_user_data_dir("Nexy") / "autostart_user_opt_out.flag"
        
        logger.info("AutostartManagerIntegration created (мониторинг LaunchAgent)")
    
    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            logger.info("🔧 Инициализация AutostartManagerIntegration")
            
            # Подписываемся на события
            await self.event_bus.subscribe("app.startup", self._on_app_startup, EventPriority.LOW)
            await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.HIGH)
            await self.event_bus.subscribe("autostart.check_status", self._on_check_status, EventPriority.MEDIUM)
            await self.event_bus.subscribe("autostart.enable_requested", self._on_enable_requested, EventPriority.HIGH)
            await self.event_bus.subscribe("autostart.disable_requested", self._on_disable_requested, EventPriority.HIGH)
            
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

    async def _on_enable_requested(self, event):
        """Явный opt-in: снимаем user opt-out и включаем LaunchAgent."""
        try:
            async with self._status_check_lock:
                self._set_user_opt_out(False)
                result = await self._autostart_manager.enable_autostart()
                await self.event_bus.publish(
                    "autostart.command_result",
                    {"command": "enable", "status": result.value},
                )
                if result == AutostartStatus.ENABLED:
                    logger.info("✅ Autostart enabled by explicit request")
                else:
                    logger.warning("⚠️ Failed to enable autostart by explicit request")
        except Exception as e:
            logger.error(f"❌ Ошибка обработки autostart.enable_requested: {e}")

    async def _on_disable_requested(self, event):
        """Явный opt-out: включаем persistent opt-out и отключаем LaunchAgent."""
        try:
            async with self._status_check_lock:
                self._set_user_opt_out(True)
                result = await self._autostart_manager.disable_autostart()
                await self.event_bus.publish(
                    "autostart.command_result",
                    {"command": "disable", "status": result.value},
                )
                if result == AutostartStatus.DISABLED:
                    logger.info("✅ Autostart disabled by explicit request")
                else:
                    logger.warning("⚠️ Failed to disable autostart by explicit request")
        except Exception as e:
            logger.error(f"❌ Ошибка обработки autostart.disable_requested: {e}")

    async def _on_app_shutdown(self, event):
        """На user quit отключаем автозапуск и ставим persistent opt-out."""
        try:
            data = (event or {}).get("data", {}) if isinstance(event, dict) else {}
            if not self._is_user_quit_intent(data):
                return
            async with self._status_check_lock:
                self._set_user_opt_out(True)
                result = await self._autostart_manager.disable_autostart()
                if result == AutostartStatus.DISABLED:
                    logger.info("✅ Autostart disabled after user quit (persistent opt-out enabled)")
                else:
                    logger.warning("⚠️ Failed to disable autostart after user quit")
        except Exception as e:
            logger.error(f"❌ Ошибка обработки app.shutdown в autostart: {e}")
    
    async def _check_autostart_status(self):
        """Проверка статуса автозапуска"""
        try:
            # Single-flight: исключаем параллельные status/repair проверки.
            async with self._status_check_lock:
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
                    "managed_by": "autostart_manager_integration",
                    "legacy_launch_agent_exists": legacy_launch_agent_exists,
                    "legacy_launch_agent_path": legacy_launch_agent_path,
                    "legacy_cleanup_enabled": bool(self.config.cleanup_legacy_launch_agent),
                    "user_opt_out": self._is_autostart_opted_out(),
                }

                await self.event_bus.publish("autostart.status_checked", status_data)

                if launch_agent_exists:
                    logger.info("✅ LaunchAgent автозапуск настроен корректно")
                else:
                    logger.warning("⚠️ LaunchAgent автозапуск не найден")

                should_repair, block_reason = self._should_repair_autostart(
                    launch_agent_exists=launch_agent_exists
                )
                if should_repair:
                    logger.info("🔧 Пытаемся восстановить LaunchAgent (auto_repair=true)")
                    result = await self._autostart_manager.enable_autostart()
                    if result == AutostartStatus.ENABLED:
                        logger.info("✅ LaunchAgent восстановлен")
                    else:
                        logger.warning("⚠️ Не удалось восстановить LaunchAgent")
                elif block_reason:
                    logger.info("ℹ️ Auto-repair skipped: %s", block_reason)

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

        except Exception as e:
            logger.error(f"❌ Ошибка проверки автозапуска: {e}")

    def _should_repair_autostart(self, *, launch_agent_exists: bool) -> tuple[bool, str]:
        """
        Централизованная policy-проверка для auto-repair.
        Возвращает (can_repair, reason_if_blocked).
        """
        if not self.config.auto_repair:
            return False, "auto_repair_disabled"
        if launch_agent_exists:
            return False, "launch_agent_already_exists"
        if self._is_user_quit_intent():
            return False, "user_quit_intent_active"
        if is_update_in_progress(self.state_manager):
            return False, "update_in_progress"
        if is_first_run_in_progress(self.state_manager):
            return False, "first_run_in_progress"
        if bool(get_state_value(self.state_manager, StateKeys.FIRST_RUN_RESTART_SCHEDULED, False)):
            return False, "first_run_restart_scheduled"
        if self._is_autostart_opted_out():
            return False, "user_opt_out"
        return True, ""

    def _is_user_quit_intent(self, data: dict[str, Any] | None = None) -> bool:
        try:
            payload = data or {}
            return bool(payload.get("user_initiated")) or bool(
                get_state_value(self.state_manager, StateKeys.USER_QUIT_INTENT, False)
            )
        except Exception:
            return False

    def _is_autostart_opted_out(self) -> bool:
        try:
            return self._user_opt_out_flag_path.exists()
        except Exception:
            return False

    def _set_user_opt_out(self, enabled: bool) -> None:
        try:
            self._user_opt_out_flag_path.parent.mkdir(parents=True, exist_ok=True)
            if enabled:
                self._user_opt_out_flag_path.write_text("1\n", encoding="utf-8")
            else:
                if self._user_opt_out_flag_path.exists():
                    self._user_opt_out_flag_path.unlink()
        except Exception as exc:
            logger.debug("Failed to update autostart opt-out flag: %s", exc)
    
    async def _monitor_autostart(self):
        """Мониторинг автозапуска"""
        try:
            while self.is_running:
                await asyncio.sleep(self.config.check_interval)
                await self._check_autostart_status()
                
        except asyncio.CancelledError:
            logger.info("🔄 Мониторинг автозапуска остановлен")
        except Exception as e:
            logger.error(f"❌ Ошибка мониторинга автозапуска: {e}")
