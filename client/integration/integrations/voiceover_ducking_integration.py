"""
Интеграция для управления VoiceOver Ducking
Тонкая обертка над VoiceOverController для интеграции с EventBus
"""
import logging
from typing import Any

from integration.core import selectors
from integration.core.base_integration import BaseIntegration
from modules.voiceover_control.core.controller import VoiceOverController, VoiceOverControlSettings

logger = logging.getLogger(__name__)


class VoiceOverDuckingIntegration(BaseIntegration):
    """Интеграция для управления VoiceOver Ducking через EventBus."""

    def __init__(self, event_bus, state_manager, error_handler, config=None):
        super().__init__(event_bus, state_manager, error_handler, "voiceover_ducking")
        self.config = config or {}
        self.controller = None
        self._initialized = False
        self._controller_ready = False
        self._awaiting_permissions = False
        self._awaiting_first_run = False

    async def _do_initialize(self) -> bool:
        """Инициализация интеграции VoiceOver Ducking."""
        try:
            logger.info("🔧 Инициализация VoiceOverDuckingIntegration...")

            # Если это первый запуск — не поднимаем VoiceOver до завершения first-run
            snapshot = selectors.create_snapshot_from_state(self.state_manager)
            if snapshot.first_run:
                self._awaiting_first_run = True
                await self.event_bus.subscribe("permissions.first_run_completed", self._on_first_run_completed)
                logger.info("ℹ️ VoiceOverDuckingIntegration: first-run not completed, postponing init until permissions.first_run_completed")
                # Всё равно подписываемся на permissions_ready для последующего старта
                await self.event_bus.subscribe("system.permissions_ready", self._on_permissions_ready)
                self._initialized = True
                return True
            
            # Создаем настройки из конфигурации
            settings = VoiceOverControlSettings(**self.config)
            
            # Создаем контроллер
            self.controller = VoiceOverController(settings)
            await self.event_bus.subscribe("system.permissions_ready", self._on_permissions_ready)

            # Инициализируем контроллер только если есть разрешение Accessibility
            if await self._maybe_initialize_controller():
                logger.info("✅ VoiceOverDuckingIntegration: controller initialized")
            else:
                self._awaiting_permissions = True
                logger.info("ℹ️ VoiceOverDuckingIntegration: awaiting Accessibility permission before init")
            
            # Подписываемся на события
            await self.event_bus.subscribe("app.mode_changed", self.handle_mode_change)
            await self.event_bus.subscribe("keyboard.press", self.handle_keyboard_press)
            await self.event_bus.subscribe("app.shutdown", self.handle_shutdown)
            await self.event_bus.subscribe("system.permissions_ready", self._on_permissions_ready)
            await self.event_bus.subscribe("permissions.first_run_completed", self._on_first_run_completed)
            
            self._initialized = True
            logger.info("✅ VoiceOverDuckingIntegration инициализирован")
            return True
            
        except Exception as exc:
            logger.error("Failed to initialize VoiceOverDuckingIntegration: %s", exc)
            return False

    async def _do_start(self) -> bool:
        """Запуск интеграции."""
        if not self._initialized:
            logger.error("VoiceOverDuckingIntegration: Not initialized")
            return False
        
        try:
            logger.info("🚀 VoiceOverDuckingIntegration запущен")
            return True
        except Exception as exc:
            logger.error("Failed to start VoiceOverDuckingIntegration: %s", exc)
            return False

    async def _do_stop(self) -> bool:
        """Остановка интеграции."""
        try:
            if self.controller:
                await self.controller.shutdown()
            logger.info("🛑 VoiceOverDuckingIntegration остановлен")
            return True
        except Exception as exc:
            logger.error("Failed to stop VoiceOverDuckingIntegration: %s", exc)
            return False

    async def handle_mode_change(self, event: dict[str, Any]) -> None:
        """Обработка изменения режима приложения."""
        try:
            if not self.controller or not self._controller_ready:
                return
            
            mode_data = event.get("data", {})
            mode = mode_data.get("mode")
            
            if not mode:
                logger.warning("VoiceOverDuckingIntegration: No mode in event data")
                return
            
            # Обновляем состояние VoiceOver перед применением режима
            await self.controller.update_voiceover_status()
            
            # Применяем режим к контроллеру
            await self.controller.apply_mode(mode.value)
            logger.debug("VoiceOverDuckingIntegration: Applied mode %s", mode.value)
            
        except Exception as exc:
            await self.error_handler.handle(exc, category="runtime", severity="warning", context={"where": "handle_mode_change"})

    async def handle_keyboard_press(self, event: dict[str, Any]) -> None:
        """Обработка нажатия клавиши для ducking."""
        try:
            if not self.controller or not self._controller_ready:
                return
            
            # Проверяем, нужно ли ducking при нажатии клавиши
            if self.controller.settings.engage_on_keyboard_events:
                # Обновляем состояние VoiceOver перед ducking
                await self.controller.update_voiceover_status()
                await self.controller.duck(reason="keyboard.press")
                logger.debug("VoiceOverDuckingIntegration: Ducking on keyboard press")
                
        except Exception as exc:
            await self.error_handler.handle(exc, category="runtime", severity="warning", context={"where": "handle_keyboard_press"})

    async def handle_shutdown(self, event: dict[str, Any]) -> None:
        """Обработка завершения работы приложения."""
        try:
            if self.controller:
                await self.controller.shutdown()
                logger.info("VoiceOverDuckingIntegration: Shutdown completed")
                
        except Exception as exc:
            await self.error_handler.handle(exc, category="runtime", severity="warning", context={"where": "handle_shutdown"})

    async def manual_duck(self, reason: str = "manual") -> bool:
        """Ручное отключение VoiceOver."""
        try:
            if not self.controller or not self._controller_ready:
                logger.error("VoiceOverDuckingIntegration: Controller not initialized")
                return False
            
            return await self.controller.duck(reason=reason)
            
        except Exception as exc:
            await self.error_handler.handle(exc, category="runtime", severity="warning", context={"where": "manual_duck"})
            return False

    async def manual_release(self, force: bool = False) -> bool:
        """Ручное восстановление VoiceOver."""
        try:
            if not self.controller or not self._controller_ready:
                logger.error("VoiceOverDuckingIntegration: Controller not initialized")
                return False
            
            await self.controller.release(force=force)
            return True
            
        except Exception as exc:
            await self.error_handler.handle(exc, category="runtime", severity="warning", context={"where": "manual_release"})
            return False

    def get_status(self) -> dict[str, Any]:
        """Получить статус интеграции."""
        return {
            "initialized": self._initialized,
            "controller_available": self.controller is not None,
            "controller_ready": self._controller_ready,
            "config": self.config,
            "enabled": self.config.get("enabled", True)
        }

    async def _on_permissions_ready(self, event: dict[str, Any]) -> None:
        """Когда получены критические разрешения, пробуем инициализировать VoiceOver."""
        if self._controller_ready:
            return
        if not self.controller:
            return
        if await self._maybe_initialize_controller():
            self._awaiting_permissions = False
            logger.info("✅ VoiceOverDuckingIntegration: controller initialized after permissions_ready")

    async def _maybe_initialize_controller(self) -> bool:
        """Инициализируем контроллер, если разрешения уже есть."""
        if self.controller is None:
            logger.warning("VoiceOverDuckingIntegration: controller is None, cannot initialize")
            return False
        
        try:
            ok = await self.controller.initialize()
            self._controller_ready = bool(ok)
            return self._controller_ready
        except Exception as exc:
            logger.debug("VoiceOverDuckingIntegration: controller init failed (%s)", exc)
            self._controller_ready = False
            return False

    async def _on_first_run_completed(self, event: dict[str, Any]) -> None:
        """После завершения первого запуска пробуем инициализировать контроллер."""
        if self._controller_ready:
            return
        self._awaiting_first_run = False
        if not self.controller:
            settings = VoiceOverControlSettings(**self.config)
            self.controller = VoiceOverController(settings)
        if await self._maybe_initialize_controller():
            logger.info("✅ VoiceOverDuckingIntegration: controller initialized after first_run_completed")
