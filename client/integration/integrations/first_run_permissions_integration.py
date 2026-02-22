"""
FirstRunPermissionsIntegration - запрос разрешений при первом запуске приложения.

Эта интеграция:
1. Проверяет настройки V2 системы разрешений
2. Инициализирует PermissionOrchestratorIntegration
3. Запускает процесс получения разрешений через V2 оркестратор
4. Обеспечивает обратную совместимость через генерацию событий (реализовано в V2 integration)

V1 система разрешений (batch sequential requests) полностью удалена.
"""

import logging
from typing import TYPE_CHECKING, Any

from config.unified_config_loader import UnifiedConfigLoader
from integration.core import selectors
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager

# V2 Imports
if TYPE_CHECKING:
    from modules.permission_restart.macos.permissions_restart_handler import (
        PermissionsRestartHandler,
    )
    from modules.permissions.v2.integration import PermissionOrchestratorIntegration

try:
    from modules.permission_restart.macos.permissions_restart_handler import (
        PermissionsRestartHandler,
    )
    from modules.permissions.v2.integration import PermissionOrchestratorIntegration

    _v2_available = True
except ImportError:
    _v2_available = False
    PermissionOrchestratorIntegration = None  # type: ignore
    PermissionsRestartHandler = None  # type: ignore

V2_AVAILABLE = _v2_available

logger = logging.getLogger(__name__)


class FirstRunPermissionsIntegration:
    """
    Интеграция для запроса разрешений при первом запуске (V2 System).

    Делегирует всю работу PermissionOrchestratorIntegration из modules/permissions/v2.
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
        self.config = config or {}

        self._v2_integration: Any | None = (
            None  # PermissionOrchestratorIntegration when V2_AVAILABLE
        )
        self._v2_enabled = False
        self._running = False
        self._advance_on_timeout = False
        self._timeout_wait_s: float | None = None

    @property
    def are_all_granted(self) -> bool:
        """
        Проверяет, выданы ли все критические разрешения.
        """
        if self._v2_integration:
            try:
                all_granted, _ = self._v2_integration.hard_permissions_summary()
                return bool(all_granted)
            except Exception as e:
                logger.warning(
                    "⚠️ [FIRST_RUN_PERMISSIONS] Failed to summarize hard permissions: %s", e
                )
        return False

    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            logger.info("🔧 [FIRST_RUN_PERMISSIONS] Инициализация...")

            # Загружаем полный конфиг для доступа к интеграциям
            full_config = UnifiedConfigLoader.get_instance()._load_config()
            integrations_config = (
                full_config.get("integrations", {}) if isinstance(full_config, dict) else {}
            )
            permissions_v2_config = integrations_config.get("permissions_v2", {})
            self._advance_on_timeout = bool(permissions_v2_config.get("advance_on_timeout", False))
            if self._advance_on_timeout:
                default_step_timeout_s = permissions_v2_config.get("default_step_timeout_s")
                steps = (
                    permissions_v2_config.get("steps", {})
                    if isinstance(permissions_v2_config, dict)
                    else {}
                )
                order = permissions_v2_config.get("order", [])
                inter_step_pause_s = float(permissions_v2_config.get("inter_step_pause_s", 0.0))
                total_s = 0.0
                for name in order:
                    step_cfg = steps.get(name, {}) if isinstance(steps, dict) else {}
                    step_timeout = step_cfg.get("step_timeout_s", default_step_timeout_s)
                    if step_timeout is not None:
                        total_s += float(step_timeout)
                if order:
                    total_s += max(len(order) - 1, 0) * inter_step_pause_s
                # Small buffer to allow completion event to propagate
                self._timeout_wait_s = total_s + 5.0 if total_s > 0 else 300.0

            if permissions_v2_config.get("enabled", False) and V2_AVAILABLE:
                logger.info(
                    "🆕 [FIRST_RUN_PERMISSIONS] V2 система включена (permissions_v2.enabled=true)"
                )
                self._v2_enabled = True

                # Проверяем доступность V2 классов
                if PermissionOrchestratorIntegration is None or PermissionsRestartHandler is None:
                    logger.error(
                        "❌ [FIRST_RUN_PERMISSIONS] V2 classes not available despite V2_AVAILABLE=True"
                    )
                    return False

                # Создаём V2 интеграцию
                from integration.utils.resource_path import get_user_data_dir

                ledger_path = str(get_user_data_dir() / "permission_ledger.json")
                self._v2_integration = PermissionOrchestratorIntegration(
                    event_bus=self.event_bus,
                    config=full_config,  # Полный конфиг
                    ledger_path=ledger_path,
                    restart_handler=PermissionsRestartHandler(),
                    should_abort_restart=self._is_user_quit_intent,
                    is_gui_process=True,
                    advance_on_timeout=self._advance_on_timeout,
                )

                # Инициализируем V2
                if self._v2_integration is None:
                    logger.error("❌ [FIRST_RUN_PERMISSIONS] Failed to create V2 integration")
                    return False
                v2_init_ok = await self._v2_integration.initialize()
                if not v2_init_ok:
                    logger.error("❌ [FIRST_RUN_PERMISSIONS] V2 initialization failed")
                    self._v2_integration = None
                    return False

                logger.info("✅ [FIRST_RUN_PERMISSIONS] V2 система инициализирована (V1 отключена)")
                return True
            else:
                logger.warning(
                    "⚠️ [FIRST_RUN_PERMISSIONS] V2 отключена или недоступна. Разрешения пропускаются."
                )
                return True

        except Exception as e:
            logger.error(f"❌ [FIRST_RUN_PERMISSIONS] Ошибка инициализации: {e}")
            await self.error_handler.handle(
                error=e,
                category="initialization",
                severity="error",
                context={"module": "first_run_permissions"},
            )
            return False

    async def start(self) -> bool:
        """
        Запуск интеграции.
        """
        if self._running:
            return True

        self._running = True

        # Если V2 активен - запускаем его и ЖДЁМ завершения
        if self._v2_enabled and self._v2_integration:
            # Check if already completed
            completed = self._v2_integration.is_first_run_complete()
            if completed is True:
                logger.info(
                    "ℹ️ [FIRST_RUN_PERMISSIONS] Ledger shows completed - re-emitting completion without pipeline start"
                )
                try:
                    reemitted = await self._v2_integration.reemit_completion_from_ledger()
                    if reemitted:
                        return True
                    logger.warning(
                        "⚠️ [FIRST_RUN_PERMISSIONS] Completed ledger re-emit unavailable, falling back to orchestrator start"
                    )
                except Exception as e:
                    logger.warning(
                        "⚠️ [FIRST_RUN_PERMISSIONS] Failed completed ledger re-emit, fallback to orchestrator start: %s",
                        e,
                    )
            else:
                logger.info("🆕 [FIRST_RUN_PERMISSIONS] Запускаем V2 систему разрешений")

            try:
                # Запускаем V2 orchestrator (will handle completed state internally)
                await self._v2_integration.start()
                logger.info("⏳ [FIRST_RUN_PERMISSIONS] Ожидаем завершения V2 pipeline...")

                # КРИТИЧНО: ЖДЁМ завершения pipeline!
                # Это блокирует startup других модулей до получения разрешений
                wait_timeout = self._timeout_wait_s or 300.0
                all_granted = await self._v2_integration.wait_for_completion(timeout=wait_timeout)

                if self._advance_on_timeout:
                    if all_granted:
                        logger.info(
                            "✅ [FIRST_RUN_PERMISSIONS] Timeout-mode: terminal completion handled by V2 owner-path"
                        )
                    else:
                        logger.info(
                            "⏳ [FIRST_RUN_PERMISSIONS] Timeout-mode completion deferred: "
                            "pipeline not in terminal completed state yet"
                        )
                    return True

                if all_granted:
                    logger.info(
                        "✅ [FIRST_RUN_PERMISSIONS] V2 pipeline завершён, все разрешения получены"
                    )
                    return True
                else:
                    logger.warning(
                        "⚠️ [FIRST_RUN_PERMISSIONS] V2 pipeline завершён, не все разрешения получены. FORCING STARTUP."
                    )
                    # FORCED: Return True anyway to prevent blocking
                    return True

            except Exception as e:
                logger.error(f"❌ [FIRST_RUN_PERMISSIONS] Ошибка запуска V2: {e}")
                # FORCED: Return True even on error
                return True
        else:
            logger.info("⏭️ [FIRST_RUN_PERMISSIONS] V2 не активна - пропускаем")

        return True

    async def stop(self) -> bool:
        """Остановка интеграции"""
        self._running = False
        if self._v2_integration:
            try:
                await self._v2_integration.stop()
            except Exception as e:
                logger.warning("⚠️ [FIRST_RUN_PERMISSIONS] Ошибка остановки V2 integration: %s", e)
        return True

    def _is_user_quit_intent(self) -> bool:
        try:
            return bool(
                selectors.get_state_value(self.state_manager, StateKeys.USER_QUIT_INTENT, False)
            )
        except Exception:
            return False
