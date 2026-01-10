"""
FirstRunPermissionsIntegration - проверка и запрос разрешений при запуске приложения.

Упрощённая логика (v3):
1. При запуске проверяет ВСЕ разрешения (mic, accessibility, screen, input)
2. Если ВСЕ есть → создаёт флаг permissions_granted.flag → продолжает работу
3. Если НЕ все → запрашивает каждое разрешение с таймаутом (15 сек)
4. После запроса всех:
   - Если ВСЕ получены → один перезапуск (для Accessibility/Screen) → работа
   - Если НЕ все → показывает ОДИН диалог с недостающими → продолжает с ограничениями

ВАЖНО: Нет бесконечных циклов перезапуска. Один перезапуск если все разрешения получены.
"""

import asyncio
import logging
import os
import time
import uuid
import warnings
from pathlib import Path
from typing import Any, Dict, List, Optional

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.utils.resource_path import get_user_data_dir

from config.unified_config_loader import UnifiedConfigLoader

from modules.permissions.core.types import PermissionType
from modules.permissions.first_run.status_checker import (
    PermissionStatus,
    check_microphone_status,
    check_accessibility_status,
    check_input_monitoring_status,
    check_screen_capture_status,
    get_bundle_id,
)

from modules.permissions.first_run.activator import (
    activate_microphone,
    activate_accessibility,
    activate_input_monitoring,
    activate_screen_capture,
)
from modules.permission_restart.macos.permissions_restart_handler import (
    PermissionsRestartHandler,
)

logger = logging.getLogger(__name__)


class FirstRunPermissionsIntegration:
    """
    Интеграция для запроса разрешений при запуске.
    
    Простая логика:
    1. Проверить все разрешения
    2. Если все есть → продолжить
    3. Если нет → запросить каждое (15 сек таймаут)
    4. Если все получены → перезапуск (для Accessibility/Screen)
    5. Если не все → показать диалог → продолжить с ограничениями
    """

    # Разрешения, требующие перезапуска после получения
    RESTART_REQUIRED_PERMISSIONS = {"accessibility", "input_monitoring", "screen_capture"}

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[Dict[str, Any]] = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or {}

        # Настройки из конфига
        self.enabled = self.config.get('enabled', True)
        
        # Загружаем конфигурацию
        self._load_configuration()

        # Путь к флагу разрешений (Application Support)
        self._data_dir = get_user_data_dir("Nexy")
        self.flag_file = self._data_dir / "permissions_granted.flag"
        
        logger.info(
            "[PERMISSIONS] Initialized: enabled=%s, timeout=%.1fs, flag=%s",
            self.enabled,
            self.request_timeout_sec,
            self.flag_file,
        )

        self._initialized = False
        self._running = False
        self.detected_bundle_id: Optional[str] = None

    def _load_configuration(self):
        """Загрузка конфигурации из unified_config.yaml"""
        try:
            config_loader = UnifiedConfigLoader.get_instance()
            config_data = config_loader._load_config()
            
            # Список требуемых разрешений
            permissions_config = config_data.get("integrations", {}).get("permissions", {})
            self.required_permissions = permissions_config.get("required_permissions", [
                "microphone",
                "accessibility",
                "screen_capture",
                "input_monitoring"
            ])
            
            # Параметры запроса
            first_run_config = config_data.get("permissions", {}).get("first_run", {})
            self.request_timeout_sec = first_run_config.get("request_timeout_sec", 15.0)
            self.open_settings_after_sec = first_run_config.get("open_settings_after_sec", 10.0)
            
        except Exception as e:
            logger.warning(f"⚠️ [PERMISSIONS] Config error: {e}, using defaults")
            self.required_permissions = ["microphone", "accessibility", "screen_capture", "input_monitoring"]
            self.request_timeout_sec = 15.0
            self.open_settings_after_sec = 10.0

    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            logger.info("🔧 [PERMISSIONS] Initializing...")
            
            # Определяем Bundle ID
            self.detected_bundle_id = get_bundle_id()
            logger.info(f"🔍 [PERMISSIONS] Bundle ID: {self.detected_bundle_id}")
            
            # Миграция старых флагов
            self._migrate_old_flags()
            
            # Устанавливаем начальное состояние
            self._update_first_run_state(
                completed=self.flag_file.exists(),
                in_progress=False
            )
            
            self._initialized = True
            logger.info("✅ [PERMISSIONS] Initialized")
            return True

        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Init error: {e}")
            return False

    def _migrate_old_flags(self):
        """Миграция старых флагов (одноразовая)"""
        try:
            # Миграция permissions_first_run_completed.flag → permissions_granted.flag
            old_flag = self._data_dir / "permissions_first_run_completed.flag"
            if old_flag.exists() and not self.flag_file.exists():
                old_flag.rename(self.flag_file)
                logger.info("✅ [PERMISSIONS] Migrated old flag to permissions_granted.flag")
            
            # Удаляем устаревший restart_completed.flag
            old_restart_flag = self._data_dir / "restart_completed.flag"
            if old_restart_flag.exists():
                old_restart_flag.unlink()
                logger.info("🧹 [PERMISSIONS] Removed obsolete restart_completed.flag")
                
        except Exception as e:
            logger.warning(f"⚠️ [PERMISSIONS] Migration error: {e}")

    async def start(self) -> bool:
        """
        Запуск: проверка и запрос разрешений.
        
        Логика:
        1. Проверяем все разрешения
        2. Если все есть → создаём флаг, продолжаем
        3. Если нет → запрашиваем каждое
        4. Если все получены → перезапуск (если нужен)
        5. Если не все → показываем диалог → продолжаем с ограничениями
        """
        if not self._initialized:
            logger.error("❌ [PERMISSIONS] Not initialized")
            return False

        if not self.enabled:
            logger.info("ℹ️ [PERMISSIONS] Disabled in config")
            return True

        # Тестовый режим
        if os.environ.get("NEXY_TEST_SKIP_PERMISSIONS") == "1":
            logger.warning("🧪 [PERMISSIONS] TEST MODE: skipping permission checks")
            self._update_first_run_state(completed=True, in_progress=False)
            return True

        self._running = True
        session_id = str(uuid.uuid4())[:8]
        start_time = time.time()

        try:
            # 1. Проверяем все разрешения (НАЧАЛЬНЫЕ статусы)
            initial_statuses = self._check_all_permissions()
            logger.info(
                f"📋 [PERMISSIONS] session={session_id} INITIAL statuses: "
                f"mic={initial_statuses['microphone'].value}, "
                f"accessibility={initial_statuses['accessibility'].value}, "
                f"screen={initial_statuses['screen_capture'].value}, "
                f"input={initial_statuses['input_monitoring'].value}"
            )

            # 2. Если все есть → продолжаем
            if self._all_granted(initial_statuses):
                logger.info(f"✅ [PERMISSIONS] session={session_id} All permissions granted")
                self._touch_flag()
                await self._publish_completed(session_id, all_granted=True)
                return True

            # 3. Не все → запрашиваем (polling по 15 сек каждое)
            logger.info(f"⏳ [PERMISSIONS] session={session_id} Requesting missing permissions...")
            await self._publish_started(session_id)
            
            for perm in self.required_permissions:
                if initial_statuses[perm] != PermissionStatus.GRANTED:
                    await self._request_permission(perm, session_id)

            # 4. Проверяем финальный результат ПОСЛЕ всех polling-ов
            final_statuses = self._check_all_permissions()
            duration_ms = int((time.time() - start_time) * 1000)
            all_granted = self._all_granted(final_statuses)
            missing = [p for p, s in final_statuses.items() if s != PermissionStatus.GRANTED]
            
            # 5. Определяем нужен ли restart:
            # Сравниваем НАЧАЛЬНЫЕ и ФИНАЛЬНЫЕ статусы для RESTART_REQUIRED разрешений
            # Если хотя бы одно из них перешло от NOT GRANTED → GRANTED, нужен restart
            newly_granted_restart_required = []
            for perm in self.RESTART_REQUIRED_PERMISSIONS:
                initial = initial_statuses.get(perm, PermissionStatus.NOT_DETERMINED)
                final = final_statuses.get(perm, PermissionStatus.NOT_DETERMINED)
                if initial != PermissionStatus.GRANTED and final == PermissionStatus.GRANTED:
                    newly_granted_restart_required.append(perm)
            
            needs_restart = len(newly_granted_restart_required) > 0

            logger.info(
                f"📊 [PERMISSIONS] session={session_id} Results: "
                f"all_granted={all_granted}, needs_restart={needs_restart}, "
                f"newly_granted_restart_required={newly_granted_restart_required}, "
                f"missing={missing}, duration_ms={duration_ms}"
            )

            # 6. Перезапуск нужен если ХОТЯ БЫ ОДНО restart-required разрешение было получено
            # Это касается accessibility, input_monitoring, screen_capture
            if needs_restart:
                logger.info(f"🔄 [PERMISSIONS] session={session_id} Restarting app to activate permissions: {newly_granted_restart_required}")
                self._touch_flag()
                await self._restart_app(session_id)
                return True

            # 7. Если все разрешения получены → готово
            if all_granted:
                logger.info(f"✅ [PERMISSIONS] session={session_id} All granted, no restart needed")
                self._touch_flag()
                await self._publish_completed(session_id, all_granted=True)
                return True

            # 8. Не все получены и перезапуск не нужен → показываем диалог
            logger.warning(f"⚠️ [PERMISSIONS] session={session_id} Missing: {missing}")
            await self._show_missing_permissions_dialog(missing)
            
            # Продолжаем с ограничениями
            await self._publish_completed(session_id, all_granted=False, missing=missing)
            return True

        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] session={session_id} Error: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            self._running = False

    async def stop(self) -> bool:
        """Остановка интеграции"""
        self._running = False
        logger.info("⏹️ [PERMISSIONS] Stopped")
        return True

    # -------------------------------------------------------------------------
    # Вспомогательные методы
    # -------------------------------------------------------------------------

    def _check_all_permissions(self) -> Dict[str, PermissionStatus]:
        """Проверить статус всех разрешений"""
        return {
            "microphone": check_microphone_status(),
            "accessibility": check_accessibility_status(),
            "screen_capture": check_screen_capture_status(),
            "input_monitoring": check_input_monitoring_status(),
        }

    def _all_granted(self, statuses: Dict[str, PermissionStatus]) -> bool:
        """Проверить, что все разрешения получены"""
        return all(
            statuses.get(perm) == PermissionStatus.GRANTED
            for perm in self.required_permissions
        )

    async def _request_permission(self, perm: str, session_id: str) -> bool:
        """
        Запрос одного разрешения с таймаутом.
        
        Returns:
            True если разрешение получено, False если таймаут/отказ
        """
        logger.info(f"📝 [PERMISSIONS] session={session_id} Requesting {perm}...")
        
        # Маппинг разрешений на функции
        activators = {
            "microphone": (activate_microphone, check_microphone_status),
            "accessibility": (activate_accessibility, check_accessibility_status),
            "screen_capture": (activate_screen_capture, check_screen_capture_status),
            "input_monitoring": (activate_input_monitoring, check_input_monitoring_status),
        }
        
        if perm not in activators:
            logger.warning(f"⚠️ [PERMISSIONS] Unknown permission: {perm}")
            return False
        
        activate_func, check_func = activators[perm]
        
        # Активируем запрос (async функции!)
        try:
            await activate_func()
        except Exception as e:
            logger.warning(f"⚠️ [PERMISSIONS] Activation error for {perm}: {e}")
        
        # Ждём с таймаутом (polling каждую секунду)
        start_time = time.time()
        check_interval = 1.0
        
        while (time.time() - start_time) < self.request_timeout_sec:
            status = check_func()
            
            if status == PermissionStatus.GRANTED:
                # Подтверждение (защита от stale cache)
                await asyncio.sleep(0.3)
                confirm_status = check_func()
                if confirm_status == PermissionStatus.GRANTED:
                    elapsed_ms = int((time.time() - start_time) * 1000)
                    logger.info(f"✅ [PERMISSIONS] session={session_id} {perm}=granted (confirmed) after {elapsed_ms}ms")
                    return True
                else:
                    logger.warning(f"⚠️ [PERMISSIONS] session={session_id} {perm} status unstable, continuing...")
            
            # НЕ открываем System Settings автоматически - пользователь должен сам решить
            # Polling продолжает проверять статус каждую секунду
            
            await asyncio.sleep(check_interval)
        
        # Таймаут
        logger.warning(f"⏱️ [PERMISSIONS] session={session_id} {perm} timeout after {self.request_timeout_sec}s")
        return False

    def _open_settings_for_permission(self, perm: str):
        """Открыть System Settings для разрешения"""
        import subprocess
        
        urls = {
            "microphone": "x-apple.systempreferences:com.apple.preference.security?Privacy_Microphone",
            "accessibility": "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility",
            "screen_capture": "x-apple.systempreferences:com.apple.preference.security?Privacy_ScreenCapture",
            "input_monitoring": "x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent",
        }
        
        url = urls.get(perm)
        if url:
            try:
                subprocess.run(["open", url], check=True)
                logger.info(f"🔧 [PERMISSIONS] Opened Settings for {perm}")
            except Exception as e:
                logger.warning(f"⚠️ [PERMISSIONS] Failed to open Settings: {e}")

    async def _show_missing_permissions_dialog(self, missing: List[str]):
        """Показать ОДИН диалог со всеми недостающими разрешениями"""
        if not missing:
            return
        
        try:
            from AppKit import NSAlert, NSAlertFirstButtonReturn, NSApplication
            
            perm_names = "\n".join(f"• {p.replace('_', ' ').title()}" for p in missing)
            missing_first = missing[0]  # Для closure
            open_settings_func = self._open_settings_for_permission  # Для closure
            
            def show_alert():
                try:
                    app = NSApplication.sharedApplication()
                    app.activateIgnoringOtherApps_(True)
                    
                    alert = NSAlert.alloc().init()
                    alert.setMessageText_("Nexy needs additional permissions")
                    alert.setInformativeText_(
                        f"Please open System Settings → Privacy & Security and enable:\n\n"
                        f"{perm_names}\n\n"
                        f"Nexy will work with limited functionality until permissions are granted."
                    )
                    alert.addButtonWithTitle_("Open Settings")
                    alert.addButtonWithTitle_("Continue")
                    
                    response = alert.runModal()
                    
                    if response == NSAlertFirstButtonReturn:
                        open_settings_func(missing_first)
                except Exception as e:
                    logger.warning(f"⚠️ [PERMISSIONS] Alert error: {e}")
            
            # Запускаем в executor для главного потока
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, show_alert)
            
        except Exception as e:
            logger.warning(f"⚠️ [PERMISSIONS] Dialog error: {e}")

    async def _restart_app(self, session_id: str):
        """Перезапуск приложения для активации Accessibility/Screen"""
        logger.info(f"🔄 [PERMISSIONS] session={session_id} Initiating app restart...")
        
        try:
            restart_handler = PermissionsRestartHandler()
            success = await restart_handler.trigger_restart(
                reason="permissions_granted",
                permissions=tuple(self.required_permissions),
            )
            
            if success:
                logger.info(f"✅ [PERMISSIONS] session={session_id} Restart initiated successfully")
            else:
                logger.warning(f"⚠️ [PERMISSIONS] session={session_id} Restart not performed")
                
        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] session={session_id} Restart error: {e}")
            import traceback
            traceback.print_exc()

    def _touch_flag(self):
        """Создать флаг permissions_granted.flag"""
        try:
            self.flag_file.parent.mkdir(parents=True, exist_ok=True)
            self.flag_file.touch()
            logger.info(f"✅ [PERMISSIONS] Flag created: {self.flag_file}")
        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Flag creation error: {e}")

    def _update_first_run_state(self, completed: bool, in_progress: bool):
        """Обновить состояние в StateManager"""
        try:
            self.state_manager.set_first_run_state(
                in_progress=in_progress,
                required=not completed,
                completed=completed
            )
        except Exception as e:
            logger.debug(f"[PERMISSIONS] State update error: {e}")

    async def _publish_started(self, session_id: str):
        """Публикация события начала запроса разрешений"""
        self._update_first_run_state(completed=False, in_progress=True)
        
        await self.event_bus.publish("permissions.first_run_started", {
            "session_id": session_id,
            "source": "permissions_integration"
        })

    async def _publish_completed(
        self,
        session_id: str,
        all_granted: bool,
        missing: Optional[List[str]] = None
    ):
        """Публикация события завершения запроса разрешений"""
        self._update_first_run_state(completed=True, in_progress=False)
        
        await self.event_bus.publish("permissions.first_run_completed", {
            "session_id": session_id,
            "source": "permissions_integration",
            "all_granted": all_granted,
            "missing": missing or []
        })

    # -------------------------------------------------------------------------
    # Deprecated методы (для обратной совместимости)
    # -------------------------------------------------------------------------

    async def request_restart(self) -> bool:
        """DEPRECATED: Перезапуск теперь автоматический"""
        warnings.warn("request_restart is deprecated", DeprecationWarning)
        return False
