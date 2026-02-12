# ruff: noqa: I001
"""
Интеграция системы обновлений с EventBus
"""

import asyncio
from pathlib import Path
import sys
from typing import Any

from config.unified_config_loader import UnifiedConfigLoader
from config.updater_manager import get_updater_manager
from integration.core.event_bus import EventBus, EventPriority
from integration.core.selectors import (
    get_current_mode,
    get_state_value,
    is_first_run_in_progress,
    is_update_in_progress as selector_is_update_in_progress,
)
from integration.core.state_keys import StateKeys
from integration.core.state_manager import ApplicationStateManager
from integration.utils.logging_setup import get_logger

try: # ruff: noqa: I001
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except ImportError:
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

from modules.updater import Updater
from modules.updater.config import UpdaterConfig

logger = get_logger(__name__)

class UpdaterIntegration:
    """Интеграция системы обновлений с архитектурой приложения"""
    
    def __init__(self, event_bus: EventBus, state_manager: ApplicationStateManager, config: dict[str, Any]):
        self.event_bus = event_bus
        self.state_manager = state_manager
        
        # Получаем централизованную конфигурацию обновлений
        self.updater_manager = get_updater_manager()
        updater_config_data = self.updater_manager.get_updater_config()
        
        # Создаем конфигурацию обновлений из централизованной системы
        updater_config = UpdaterConfig(
            enabled=updater_config_data.enabled,
            manifest_url=self.updater_manager.get_manifest_url(),
            check_interval=updater_config_data.check_interval,
            check_on_startup=updater_config_data.check_on_startup,
            auto_install=updater_config_data.auto_install,
            public_key=updater_config_data.security.get("public_key", ""),
            timeout=updater_config_data.network.get("timeout", 30),
            retries=updater_config_data.network.get("retries", 3),
            show_notifications=updater_config_data.ui.get("show_notifications", True),
            auto_download=updater_config_data.ui.get("auto_download", True),
            ssl_verify=updater_config_data.security.get("ssl_verify", True)
        )
        
        self.updater = Updater(updater_config)
        self.check_task = None
        self.is_running = False
        self._update_in_progress: bool = False
        self._loop: asyncio.AbstractEventLoop | None = None
        self._last_download_percent: int = 0
        self._last_install_percent: int = 0
        # Поведение миграции регулируется конфигом/ENV
        # Отключаем миграцию в ~/Applications (стратегия: системная установка в /Applications)
        self._migrate_mode: str = "never"
        self._migrate_on_start: bool = False
        # Config loader for feature flags
        self._config_loader = UnifiedConfigLoader.get_instance()
        # Current app mode (tracked via events instead of direct state access)
        self._current_mode: AppMode = AppMode.SLEEPING
    
    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            logger.info("🔄 Инициализация UpdaterIntegration...")
            
            # Миграция в пользовательскую папку отключена (установка в /Applications)
            
            # Настраиваем обработчики событий
            await self._setup_event_handlers()
            # Initialize current mode from state (one-time read allowed during init)
            # After init, mode is tracked via events only
            try:
                initial_mode = get_current_mode(self.state_manager)
                if isinstance(initial_mode, AppMode):
                    self._current_mode = initial_mode
            except Exception:
                self._current_mode = AppMode.SLEEPING
            # Attach event loop for async event publishing
            try:
                self._loop = asyncio.get_running_loop()
                # НЕ переприсваиваем loop в event_bus! 
                # SimpleModuleCoordinator уже установил правильный _bg_loop
                # Переприсваивание здесь ломает async callbacks в QuartzMonitor!
                # if hasattr(self.event_bus, "attach_loop"):
                #     self.event_bus.attach_loop(self._loop)
            except RuntimeError:
                self._loop = None
            self._set_update_state(False, trigger="initialize")
            
            logger.info("✅ UpdaterIntegration инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации UpdaterIntegration: {e}")
            return False
    
    async def start(self) -> bool:
        """Запуск интеграции"""
        try:
            if not self.updater.config.enabled:
                logger.info("⏭️ Пропускаю запуск UpdaterIntegration - отключен")
                return True
            
            logger.info("🚀 Запуск UpdaterIntegration...")
            
            # Проверка при запуске (если включена)
            if self.updater.config.check_on_startup:
                logger.info("🔍 Проверка обновлений при запуске...")
                if await self._can_update():
                    update_performed = False
                    try:
                        update_performed = await self._execute_update(trigger="startup")
                    except Exception as exc:
                        logger.error(
                            "❌ Ошибка проверки/установки обновления при запуске (trigger=startup). "
                            "Продолжаем работу без авто-обновления: %s",
                            exc,
                            exc_info=True,
                        )
                        update_performed = False
                    if update_performed:
                        return True  # Приложение перезапустится
            
            # Запускаем периодическую проверку
            self.check_task = asyncio.create_task(self._check_loop())
            
            self.is_running = True
            logger.info("✅ UpdaterIntegration запущен")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска UpdaterIntegration: {e}")
            return False
    
    async def _check_loop(self):
        """Цикл проверки обновлений"""
        while self.is_running:
            try:
                # Проверяем, можно ли обновляться
                if await self._can_update():
                    if await self._execute_update(trigger="scheduled"):
                        return  # Приложение перезапустится
                
                # Ждем до следующей проверки
                await asyncio.sleep(self.updater.config.check_interval)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Ошибка в цикле проверки обновлений: {e}")
                await asyncio.sleep(300)  # Ждем 5 минут при ошибке
    
    async def _can_update(self) -> bool:
        """Проверка, можно ли обновляться.
        
        Использует tracked mode (из событий app.mode_changed) вместо прямого доступа к state_manager.
        Это соответствует правилу 21.3: запрет прямого доступа к состоянию вне selectors/gateways.
        
        Fallback: Если tracked mode не обновлен событиями (например, в тестах без реального EventBus),
        читаем из state_manager для совместимости. В production режим должен обновляться через события.
        """
        # Block updates during first-run permission flow
        try:
            if is_first_run_in_progress(self.state_manager):
                logger.info("[UPDATER] Update blocked: first_run_in_progress=true")
                return False
        except Exception as exc:
            logger.debug("[UPDATER] first_run guard check failed: %s", exc)

        # Use tracked mode from events (updated in _on_mode_changed/_on_mode_changed_via_gateway)
        current_mode = self._current_mode
        
        # Fallback: Если tracked mode == SLEEPING (initial state), проверяем актуальный режим
        # Это необходимо для тестов и edge cases, когда события не работают
        # TODO: Remove fallback after all consumers migrate to event-based mode tracking
        try:
            actual_mode = get_current_mode(self.state_manager)
            if isinstance(actual_mode, AppMode):
                # Update tracked mode if different (fallback sync)
                if actual_mode != current_mode:
                    self._current_mode = actual_mode
                    current_mode = actual_mode
            elif not isinstance(actual_mode, AppMode):
                # Normalize string/other types to AppMode
                try:
                    actual_mode = AppMode(actual_mode)
                    self._current_mode = actual_mode
                    current_mode = actual_mode
                except Exception:
                    pass
        except Exception:
            pass  # Use tracked mode if fallback fails
        
        if current_mode in (AppMode.LISTENING, AppMode.PROCESSING):
            return False
        return True
    
    async def _setup_event_handlers(self):
        """Настройка обработчиков событий"""
        # Подписываемся на события
        await self.event_bus.subscribe("app.startup", self._on_app_startup, EventPriority.MEDIUM)
        await self.event_bus.subscribe("app.shutdown", self._on_app_shutdown, EventPriority.HIGH)
        await self.event_bus.subscribe("updater.check_manual", self._on_manual_check, EventPriority.HIGH)
        await self.event_bus.subscribe("app.mode_changed", self._on_mode_changed, EventPriority.LOW)
    
    async def _on_app_startup(self, event_data):
        """Обработка запуска приложения"""
        logger.info("🚀 Обработка запуска приложения в UpdaterIntegration")
    
    async def _on_app_shutdown(self, event_data):
        """Обработка завершения приложения"""
        logger.info("🛑 Обработка завершения приложения в UpdaterIntegration")
        await self.stop()
    
    async def _on_manual_check(self, event_data):
        """Ручная проверка обновлений"""
        logger.info("🔍 Ручная проверка обновлений")
        if await self._can_update():
            await self._execute_update(trigger="manual")
    
    async def _on_mode_changed(self, event_data):
        """Обработка изменения режима приложения (legacy event)"""
        data = (event_data or {}).get("data", event_data or {})
        new_mode = data.get("mode") or event_data.get("mode")
        if new_mode:
            try:
                if not isinstance(new_mode, AppMode):
                    new_mode = AppMode(new_mode)
                self._current_mode = new_mode
            except Exception:
                pass
        logger.info(f"Режим приложения изменен на: {new_mode}")
    
    async def _execute_update(self, trigger: str) -> bool:
        """
        Проверяет, скачивает и устанавливает обновление с публикацией событий.

        ВАЖНО: Сначала проверяется наличие обновления (check_for_updates),
        и только если обновление есть, публикуется updater.update_started.
        Это предотвращает ложные уведомления при старте приложения с актуальной версией.
        """
        if self._update_in_progress:
            logger.info("⏳ Обновление уже выполняется (trigger=%s)", trigger)
            return False

        # ШАГ 1: Сначала ПРОВЕРЯЕМ, есть ли обновление (БЕЗ изменения состояния)
        manifest = await asyncio.to_thread(self.updater.check_for_updates)

        if not manifest:
            # НЕТ обновления - публикуем update_skipped и выходим
            await self._safe_publish("updater.update_skipped", {
                "trigger": trigger,
                "reason": "no_updates_available",
                "current_version": self.updater.get_current_build()
            })
            logger.info("✅ Обновления не требуются (trigger=%s)", trigger)
            return False

        # ШАГ 2: Обновление ЕСТЬ - теперь публикуем update_started
        version = manifest.get("version", "unknown")
        logger.info(f"🔄 Найдено обновление до версии {version} (trigger={trigger})")

        self._set_update_state(True, trigger=trigger)
        await self._safe_publish("updater.update_started", {
            "trigger": trigger,
            "version": version
        })

        # ШАГ 3: Настраиваем callbacks для прогресса
        try:
            loop = self._loop if (self._loop is not None and self._loop.is_running()) else asyncio.get_running_loop()
        except RuntimeError:
            loop = None
        self._last_download_percent = 0
        self._last_install_percent = 0
        if loop is not None:
            self.updater.on_download_progress = lambda downloaded, total: asyncio.run_coroutine_threadsafe(  # type: ignore[assignment]
                self._handle_download_progress(downloaded, total, trigger),
                loop,
            )
            self.updater.on_install_progress = lambda stage, percent: asyncio.run_coroutine_threadsafe(  # type: ignore[assignment]
                self._handle_install_progress(stage, percent, trigger),
                loop,
            )
        else:
            # Fallback: if no loop available, use async call directly (for tests)
            # In production, loop should always be available
            logger.debug("[UPDATER] No loop available for progress callbacks (test mode?)")
            # Use simple async call - will be handled by event loop when available
            self.updater.on_download_progress = lambda downloaded, total: None  # type: ignore[assignment]  # Skip in test mode
            self.updater.on_install_progress = lambda stage, percent: None  # type: ignore[assignment]  # Skip in test mode

        # ШАГ 4: Выполняем скачивание и установку (проверка уже выполнена!)
        try:
            # download_and_verify
            artifact_path = await asyncio.to_thread(
                self.updater.download_and_verify,
                manifest["artifact"]
            )

            # install_update
            await asyncio.to_thread(
                self.updater.install_update,
                artifact_path,
                manifest["artifact"]
            )

            # ШАГ 5: Успешно завершено
            await self._safe_publish("updater.update_completed", {
                "trigger": trigger,
                "version": version
            })

            # relaunch
            # Respect explicit user quit intent: do not force relaunch if user decided to exit.
            if bool(get_state_value(self.state_manager, StateKeys.USER_QUIT_INTENT, False)):
                logger.info("⏭️ Updater relaunch skipped: USER_QUIT_INTENT=true")
                return True
            await asyncio.to_thread(self.updater.relaunch_app)
            return True

        except Exception as exc:
            await self._safe_publish("updater.update_failed", {
                "trigger": trigger,
                "error": str(exc),
                "version": version
            })
            raise
        finally:
            self.updater.on_download_progress = None
            self.updater.on_install_progress = None
            self._set_update_state(False, trigger=trigger)

    async def stop(self):
        """Остановка интеграции"""
        if self.check_task:
            self.check_task.cancel()
        self.is_running = False
        self._set_update_state(False, trigger="stop")
        logger.info("✅ UpdaterIntegration остановлен")


    def _should_migrate_on_start(self) -> bool:
        """Миграция отключена по политике установки (/Applications)."""
        return False

    def _is_in_user_applications(self) -> bool:
        """Проверяет, расположен ли бандл в ~/Applications."""
        try:
            p = Path(sys.argv[0]).resolve()
            home_apps = Path.home() / "Applications"
            return str(p).startswith(str(home_apps))
        except Exception:
            return False

    def _is_running_from_app_bundle(self) -> bool:
        """Определяет, запущены ли мы как .app (PyInstaller бандл), и не из ~/Applications.
        Сценарии: запуск из DMG (/Volumes/...), из произвольной папки — да; запуск из исходников — нет.
        """
        try:
            exe_path = Path(sys.argv[0]).resolve()
            s = str(exe_path)
            if ".app/Contents/MacOS" in s or s.endswith("/MacOS/Nexy"):
                # .app бандл
                return not self._is_in_user_applications()
            # Запуск из исходников / интерпретатора — не мигрируем
            return False
        except Exception:
            return False

    def is_update_in_progress(self) -> bool:
        """Возвращает текущий статус установки обновления."""
        return self._update_in_progress

    def _set_update_state(self, active: bool, trigger: str = "unknown") -> None:
        if self._update_in_progress == active:
            # Обновляем state manager даже если значение не меняется, чтобы синхронизировать потребителей.
            try:
                self.state_manager.set_update_in_progress(active)
            except Exception:
                pass
            
            # Shadow-mode: diagnostic logging for accessor vs state_data comparison
            try:
                feature_config = self._config_loader._load_config().get("features", {}).get("use_events_for_update_status", {})
                if feature_config.get("enabled", False):
                    # Compare accessor vs state_data
                    from integration.core.selectors import is_update_in_progress
                    state_data_value = is_update_in_progress(self.state_manager)
                    accessor_value = self._update_in_progress
                    if state_data_value != accessor_value:
                        logger.warning(
                            "[UPDATER] Shadow-mode mismatch: accessor=%s vs state_data=%s (trigger=%s)",
                            accessor_value,
                            state_data_value,
                            trigger,
                        )
                    else:
                        logger.debug(
                            "[UPDATER] Shadow-mode sync: accessor=%s == state_data=%s (trigger=%s)",
                            accessor_value,
                            state_data_value,
                            trigger,
                        )
            except Exception:
                pass  # Don't fail if feature flag check fails
            
            # Публикуем событие изменения состояния (shadow-mode)
            try:
                if self._loop is not None and self._loop.is_running():
                    asyncio.run_coroutine_threadsafe(
                        self._safe_publish(
                            "updater.in_progress.changed",
                            {"active": active, "trigger": trigger},
                        ),
                        self._loop,
                    )
                else:
                    try:
                        loop = asyncio.get_running_loop()
                        asyncio.run_coroutine_threadsafe(
                            self._safe_publish(
                                "updater.in_progress.changed",
                                {"active": active, "trigger": trigger},
                            ),
                            loop,
                        )
                    except RuntimeError:
                        # No running loop - can't publish event (test mode with Mock EventBus)
                        # In production, loop should always be attached in initialize()
                        logger.debug("[UPDATER] No running loop for event publishing (test mode?)")
            except Exception as e:
                logger.debug(f"[UPDATER] Failed to publish event: {e}")
                pass
            return

        self._update_in_progress = active
        try:
            self.state_manager.set_update_in_progress(active)
        except Exception:
            pass
        
        # Shadow-mode: diagnostic logging for accessor vs state_data comparison
        try:
            feature_config = self._config_loader._load_config().get("features", {}).get("use_events_for_update_status", {})
            if feature_config.get("enabled", False):
                # Compare accessor vs state_data
                state_data_value = selector_is_update_in_progress(self.state_manager)
                accessor_value = self._update_in_progress
                if state_data_value != accessor_value:
                    logger.warning(
                        "[UPDATER] Shadow-mode mismatch: accessor=%s vs state_data=%s (trigger=%s)",
                        accessor_value,
                        state_data_value,
                        trigger,
                    )
                else:
                    logger.debug(
                        "[UPDATER] Shadow-mode sync: accessor=%s == state_data=%s (trigger=%s)",
                        accessor_value,
                        state_data_value,
                        trigger,
                    )
        except Exception as e:
            logger.debug(f"[UPDATER] Shadow-mode error: {e}")
        
        logger.debug("UpdaterIntegration: update_in_progress=%s (trigger=%s)", active, trigger)
        # Публикуем событие изменения состояния
        try:
            if self._loop is not None and self._loop.is_running():
                # Use attached loop for thread-safe publishing
                asyncio.run_coroutine_threadsafe(
                    self._safe_publish(
                        "updater.in_progress.changed", {"active": active, "trigger": trigger}
                    ),
                    self._loop,
                )
            else:
                # Fallback: try to get running loop or use async call
                try:
                    loop = asyncio.get_running_loop()
                    asyncio.run_coroutine_threadsafe(
                        self._safe_publish(
                            "updater.in_progress.changed", {"active": active, "trigger": trigger}
                        ),
                        loop,
                    )
                except RuntimeError:
                    # No running loop - log warning but don't fail
                    # In test mode with Mock EventBus, this is expected
                    logger.debug("[UPDATER] No running loop for event publishing (test mode?)")
        except Exception as e:
            logger.debug(f"[UPDATER] Failed to publish event: {e}")
            pass

    async def _handle_download_progress(
        self,
        downloaded: int,
        expected_size: int | None,
        trigger: str,
    ) -> None:
        if not expected_size or expected_size <= 0:
            return
        percent = int(min(100, max(0, downloaded * 100 // expected_size)))
        if percent <= self._last_download_percent:
            return
        self._last_download_percent = percent
        await self._safe_publish(
            "updater.download_progress",
            {
                "percent": percent,
                "stage": "download",
                "trigger": trigger,
            },
        )

    async def _handle_install_progress(self, stage: str, percent: int, trigger: str) -> None:
        percent = int(min(100, max(0, percent)))
        if percent <= self._last_install_percent:
            return
        self._last_install_percent = percent
        await self._safe_publish(
            "updater.install_progress",
            {
                "percent": percent,
                "stage": stage,
                "trigger": trigger,
            },
        )

    async def _safe_publish(self, event_type: str, payload: dict[str, Any]) -> None:
        """
        Safely publish event to EventBus.
        
        This method can be called from:
        - Async context (await directly)
        - Sync context (via run_coroutine_threadsafe)
        - Test context (with Mock EventBus)
        """
        try:
            # If we're already in async context, await directly
            if self._loop is not None and self._loop.is_running():
                # Use async call directly
                await self.event_bus.publish(event_type, payload)
            else:
                # Try to get running loop
                try:
                    loop = asyncio.get_running_loop()
                    await self.event_bus.publish(event_type, payload)
                except RuntimeError:
                    # No running loop - this is expected in test mode with Mock EventBus
                    # In production, this should not happen (loop is attached in initialize)
                    logger.debug("[UPDATER] No running loop for _safe_publish (test mode?)")
        except Exception as exc:
            logger.debug("UpdaterIntegration: не удалось опубликовать %s: %s", event_type, exc)
