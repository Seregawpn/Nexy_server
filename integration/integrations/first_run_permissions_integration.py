"""
FirstRunPermissionsIntegration - запрос разрешений при первом запуске приложения.

Последовательно запрашивает системные разрешения с паузами между ними.
Работает ТОЛЬКО при первом запуске (определяется по флагу).
"""

import asyncio
import logging
from typing import Optional, Dict, Any
from pathlib import Path
import uuid
import os

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.utils.resource_path import get_user_data_dir

from modules.permissions.core.types import PermissionType
from modules.permissions.first_run.status_checker import (
    PermissionStatus,
    check_microphone_status,
    check_accessibility_status,
    check_input_monitoring_status,
    check_screen_capture_status,
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
    """Интеграция для запроса разрешений при первом запуске"""

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
        self.pause_seconds = self.config.get('pause_between_requests_sec', 1.0)
        self.activation_hold_seconds = self.config.get('activation_hold_duration_sec', 7.0)

        logger.info(
            "[FIRST_RUN_PERMISSIONS] Configuration loaded: "
            "enabled=%s, pause_seconds=%s, activation_hold_seconds=%s",
            self.enabled,
            self.pause_seconds,
            self.activation_hold_seconds,
        )

        # Путь к флагу
        self.flag_file = get_user_data_dir("Nexy") / "permissions_first_run_completed.flag"
        self._restart_flag = self.flag_file.parent / "restart_completed.flag"

        self._initialized = False
        self._running = False
        self._permissions_in_progress = False
        self._restart_session_id: Optional[str] = None  # Session ID для перезапуска

    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            logger.info("🔧 [FIRST_RUN_PERMISSIONS] Инициализация...")

            # Сбрасываем состояние при инициализации (важно для повторных запусков/тестов)
            self._restart_session_id = None
            self._permissions_in_progress = False
            self.state_manager.set_state_data("permissions_restart_pending", False)

            # КРИТИЧНО: Проверяем был ли перезапуск после first_run
            # Это позволяет опубликовать completed ТОЛЬКО после успешного перезапуска
            # Также проверяем env переменную NEXY_FIRST_RUN_RESTARTED (для dev-режима)
            restarted_via_flag = self._restart_flag.exists()
            restarted_via_env = os.environ.get("NEXY_FIRST_RUN_RESTARTED") == "1"

            if restarted_via_flag or restarted_via_env:
                logger.info("✅ [FIRST_RUN_PERMISSIONS] Перезапуск после first_run завершён успешно")
                if restarted_via_env:
                    logger.info("   (обнаружено через NEXY_FIRST_RUN_RESTARTED env)")

                # Публикуем completed в НОВОМ процессе (после перезапуска)
                await self.event_bus.publish("permissions.first_run_completed", {
                    "session_id": "restarted",
                    "source": "first_run_permissions_integration",
                    "note": "Published after successful restart"
                })

                # Удаляем флаг после публикации
                self._clear_restart_flag()

                # Очищаем env переменную
                if restarted_via_env:
                    os.environ.pop("NEXY_FIRST_RUN_RESTARTED", None)

            if not self.enabled:
                logger.info("ℹ️ [FIRST_RUN_PERMISSIONS] Отключено в конфиге")

            self._initialized = True
            logger.info("✅ [FIRST_RUN_PERMISSIONS] Инициализирован")
            return True

        except Exception as e:
            logger.error(f"❌ [FIRST_RUN_PERMISSIONS] Ошибка инициализации: {e}")
            return False

    async def start(self) -> bool:
        """
        Запуск интеграции - главная логика запроса разрешений.

        Проверяет флаг первого запуска. Если это первый запуск:
        - Для каждого разрешения проверяет статус
        - Если NOT_DETERMINED - активирует и делает паузу
        - Если GRANTED/DENIED - пропускает без паузы

        БЛОКИРУЕТ запуск остальных интеграций пока не завершится!
        """
        try:
            if not self._initialized:
                logger.error("❌ [FIRST_RUN_PERMISSIONS] Не инициализирован")
                return False

            # Проверяем enabled
            if not self.enabled:
                logger.info("ℹ️ [FIRST_RUN_PERMISSIONS] Отключено - пропускаем")
                return True

            # Проверяем флаг первого запуска
            if self.flag_file.exists():
                logger.info("✅ [FIRST_RUN_PERMISSIONS] Первый запуск уже завершён - пропускаем")
                return True

            # ПЕРВЫЙ ЗАПУСК!
            logger.info("🔐 [FIRST_RUN_PERMISSIONS] Первый запуск обнаружен - запрашиваем разрешения")

            # Публикуем начало процесса запроса разрешений
            session_id = str(uuid.uuid4())
            await self.event_bus.publish("permissions.first_run_started", {
                "session_id": session_id,
                "source": "first_run_permissions_integration"
            })

            self._running = True
            self._permissions_in_progress = True

            try:
                # Запрашиваем разрешения последовательно (простая блокирующая схема)
                await self._request_permissions_sequentially(session_id=session_id)

                # Сохраняем флаг с обработкой ошибок
                if not self._safe_touch_flag(self.flag_file, "permissions_first_run_completed"):
                    logger.error("❌ [FIRST_RUN_PERMISSIONS] Критическая ошибка: не удалось сохранить флаг первого запуска")
                    # Публикуем событие ошибки
                    await self.event_bus.publish("permissions.first_run_failed", {
                        "session_id": session_id,
                        "error": "Cannot create flag file",
                        "source": "first_run_permissions_integration"
                    })
                    # Сбрасываем состояние и продолжаем без перезапуска
                    self._handle_restart_failure()
                    return False

                # ВАЖНО: НЕ сбрасываем флаг permissions_in_progress!
                # Это предотвратит запуск остальных интеграций (voice_recognition и т.д.)
                # Флаг сбросится только при следующем запуске приложения после перезапуска

                logger.info("✅ [FIRST_RUN_PERMISSIONS] Первый запуск завершён")

                # КРИТИЧНО: Устанавливаем флаг для публикации completed в НОВОМ процессе
                # Это предотвращает разблокировку voice_recognition ДО перезапуска
                if not self._set_restart_flag():
                    logger.warning("⚠️ [FIRST_RUN_PERMISSIONS] Не удалось установить restart_completed.flag")
                    # Используем state_manager как fallback

                self.state_manager.set_state_data("permissions_restart_pending", True)
                self.state_manager.set_state_data("permissions_restart_completed_fallback", True)

                # НЕ публикуем permissions.first_run_completed здесь!
                # Оно будет опубликовано в НОВОМ процессе после успешного перезапуска
                # Это предотвращает преждевременную разблокировку voice_recognition

                logger.info("🔄 [FIRST_RUN_PERMISSIONS] Запрос перезапуска приложения...")

                # Публикуем ТОЛЬКО restart_pending для coordinator
                await self.event_bus.publish("permissions.first_run_restart_pending", {
                    "session_id": session_id,
                    "source": "first_run_permissions_integration",
                    "note": "Restart required - completed will be published after restart"
                })

                # ВАЖНО: НЕ вызываем _force_restart() здесь!
                # Coordinator проверит флаг _permissions_in_progress и сам запустит перезапуск
                # Это позволит корректно остановить запуск остальных интеграций

                # Сохраняем session_id для вызова из coordinator
                self._restart_session_id = session_id

                # Возвращаем True чтобы coordinator проверил флаг и запустил перезапуск
                return True

            except Exception as e:
                # Публикуем ошибку
                await self.event_bus.publish("permissions.first_run_failed", {
                    "session_id": session_id,
                    "error": str(e),
                    "source": "first_run_permissions_integration"
                })
                raise

        except Exception as e:
            logger.error(f"❌ [FIRST_RUN_PERMISSIONS] Ошибка запуска: {e}")
            # Сбрасываем флаги состояния
            self._running = False
            self._permissions_in_progress = False

            # Сохраняем флаг даже при ошибке чтобы не застрять в цикле
            if not self._safe_touch_flag(self.flag_file, "permissions_first_run_completed (after error)"):
                logger.warning("⚠️ [FIRST_RUN_PERMISSIONS] Не удалось сохранить флаг даже после ошибки")
            return False

    async def stop(self) -> bool:
        """Остановка интеграции"""
        try:
            self._running = False
            self._permissions_in_progress = False
            logger.info("✅ [FIRST_RUN_PERMISSIONS] Остановлен")
            return True

        except Exception as e:
            logger.error(f"❌ [FIRST_RUN_PERMISSIONS] Ошибка остановки: {e}")
            return False

    async def _request_permissions_sequentially(self, *, session_id: str):
        """Простая последовательная схема запроса разрешений с задержками."""
        import time

        # 1. MICROPHONE
        logger.info("🎙️ [FIRST_RUN_PERMISSIONS] Проверка Microphone...")
        mic_status = check_microphone_status()
        logger.info(f"   Статус: {mic_status.value}")
        await self._publish_status_checked(
            permission=PermissionType.MICROPHONE,
            status=mic_status,
            session_id=session_id,
            source="first_run.pre_activation",
        )
        if mic_status == PermissionStatus.NOT_DETERMINED:
            logger.info(
                "   Активируем Microphone с hold_duration=%s сек...",
                self.activation_hold_seconds
            )
            start_time = time.time()
            await activate_microphone(hold_duration=self.activation_hold_seconds)
            elapsed = time.time() - start_time
            logger.info(
                "   ✅ Microphone activation завершена за %.2f сек (ожидалось %.2f сек)",
                elapsed,
                self.activation_hold_seconds
            )
            new_status = check_microphone_status()
            await self._publish_status_checked(
                permission=PermissionType.MICROPHONE,
                status=new_status,
                session_id=session_id,
                source="first_run.post_activation",
            )
            if new_status != mic_status:
                await self._publish_permission_changed(
                    permission=PermissionType.MICROPHONE,
                    old_status=mic_status,
                    new_status=new_status,
                    session_id=session_id,
                    source="first_run.microphone",
                )
            mic_status = new_status
        else:
            logger.info("   Пропускаем (разрешение уже решено)")

        # 2. ACCESSIBILITY
        logger.info("♿ [FIRST_RUN_PERMISSIONS] Проверка Accessibility...")
        acc_status = check_accessibility_status()
        logger.info(f"   Статус: {acc_status.value}")
        await self._publish_status_checked(
            permission=PermissionType.ACCESSIBILITY,
            status=acc_status,
            session_id=session_id,
            source="first_run.pre_activation",
        )
        if acc_status == PermissionStatus.NOT_DETERMINED:
            logger.info(
                "   Активируем Accessibility с hold_duration=%s сек...",
                self.activation_hold_seconds
            )
            start_time = time.time()
            await activate_accessibility(hold_duration=self.activation_hold_seconds)
            elapsed = time.time() - start_time
            logger.info(
                "   ✅ Accessibility activation завершена за %.2f сек (ожидалось %.2f сек)",
                elapsed,
                self.activation_hold_seconds
            )
            new_status = check_accessibility_status()
            await self._publish_status_checked(
                permission=PermissionType.ACCESSIBILITY,
                status=new_status,
                session_id=session_id,
                source="first_run.post_activation",
            )
            if new_status != acc_status:
                await self._publish_permission_changed(
                    permission=PermissionType.ACCESSIBILITY,
                    old_status=acc_status,
                    new_status=new_status,
                    session_id=session_id,
                    source="first_run.accessibility",
                )
            acc_status = new_status
        else:
            logger.info("   Пропускаем (разрешение уже решено)")

        # 3. INPUT MONITORING
        logger.info("⌨️ [FIRST_RUN_PERMISSIONS] Проверка Input Monitoring...")
        input_status = check_input_monitoring_status()
        logger.info(f"   Статус: {input_status.value}")
        await self._publish_status_checked(
            permission=PermissionType.INPUT_MONITORING,
            status=input_status,
            session_id=session_id,
            source="first_run.pre_activation",
        )
        if input_status == PermissionStatus.NOT_DETERMINED:
            logger.info(
                "   Активируем Input Monitoring с hold_duration=%s сек...",
                self.activation_hold_seconds
            )
            start_time = time.time()
            await activate_input_monitoring(hold_duration=self.activation_hold_seconds)
            elapsed = time.time() - start_time
            logger.info(
                "   ✅ Input Monitoring activation завершена за %.2f сек (ожидалось %.2f сек)",
                elapsed,
                self.activation_hold_seconds
            )
            new_status = check_input_monitoring_status()
            await self._publish_status_checked(
                permission=PermissionType.INPUT_MONITORING,
                status=new_status,
                session_id=session_id,
                source="first_run.post_activation",
            )
            if new_status != input_status:
                await self._publish_permission_changed(
                    permission=PermissionType.INPUT_MONITORING,
                    old_status=input_status,
                    new_status=new_status,
                    session_id=session_id,
                    source="first_run.input_monitoring",
                )
            input_status = new_status
        else:
            logger.info("   Пропускаем (разрешение уже решено)")

        # 4. SCREEN CAPTURE
        logger.info("📺 [FIRST_RUN_PERMISSIONS] Проверка Screen Capture...")
        screen_status = check_screen_capture_status()
        logger.info(f"   Статус: {screen_status.value}")
        await self._publish_status_checked(
            permission=PermissionType.SCREEN_CAPTURE,
            status=screen_status,
            session_id=session_id,
            source="first_run.pre_activation",
        )
        if screen_status == PermissionStatus.NOT_DETERMINED:
            logger.info(
                "   Активируем Screen Capture с hold_duration=%s сек...",
                self.activation_hold_seconds
            )
            start_time = time.time()
            await activate_screen_capture(hold_duration=self.activation_hold_seconds)
            elapsed = time.time() - start_time
            logger.info(
                "   ✅ Screen Capture activation завершена за %.2f сек (ожидалось %.2f сек)",
                elapsed,
                self.activation_hold_seconds
            )
            new_status = check_screen_capture_status()
            await self._publish_status_checked(
                permission=PermissionType.SCREEN_CAPTURE,
                status=new_status,
                session_id=session_id,
                source="first_run.post_activation",
            )
            if new_status != screen_status:
                await self._publish_permission_changed(
                    permission=PermissionType.SCREEN_CAPTURE,
                    old_status=screen_status,
                    new_status=new_status,
                    session_id=session_id,
                    source="first_run.screen_capture",
                )
            screen_status = new_status
        else:
            logger.info("   Пропускаем (разрешение уже решено)")

        logger.info("✅ [FIRST_RUN_PERMISSIONS] Все разрешения обработаны")

    async def request_restart(self, *, session_id: Optional[str] = None) -> bool:
        """
        Публичный API для запроса перезапуска приложения.

        Args:
            session_id: ID сессии для логирования (опционально)

        Returns:
            True если перезапуск успешно инициирован, False в противном случае
        """
        session = session_id or self._restart_session_id or "unknown"
        logger.info(f"🔄 [FIRST_RUN_PERMISSIONS] Инициирован перезапуск (session={session})")

        try:
            handler = PermissionsRestartHandler()
            success = await handler.trigger_restart(
                reason="first_run_completed",
                permissions=("microphone", "accessibility", "input_monitoring", "screen_capture"),
            )

            if not success:
                logger.warning(
                    "⚠️ [FIRST_RUN_PERMISSIONS] Перезапуск не выполнен (возможно dry-run режим). session_id=%s",
                    session,
                )
                # Fallback: сбрасываем флаг чтобы не блокировать интеграции
                self._handle_restart_failure()
                return False

            return True

        except Exception as exc:
            logger.error(
                "❌ [FIRST_RUN_PERMISSIONS] Ошибка перезапуска (session_id=%s): %s",
                session,
                exc,
            )
            # Fallback: сбрасываем флаг чтобы не блокировать интеграции
            self._handle_restart_failure()
            return False

    async def _force_restart(self, *, session_id: str) -> None:
        """
        DEPRECATED: Используйте request_restart() вместо этого.
        Оставлено для обратной совместимости.
        """
        await self.request_restart(session_id=session_id)

    def _set_restart_flag(self) -> bool:
        """
        Установить флаг restart_completed для нового процесса.

        Returns:
            True если флаг успешно создан, False в противном случае
        """
        return self._safe_touch_flag(self._restart_flag, "restart_completed")

    def _safe_touch_flag(self, flag_path: Path, flag_name: str) -> bool:
        """
        Безопасно создать флаг с обработкой PermissionError.

        Args:
            flag_path: Путь к флагу
            flag_name: Имя флага для логирования

        Returns:
            True если флаг создан успешно, False если ошибка
        """
        try:
            # Убедимся что родительская директория существует
            flag_path.parent.mkdir(parents=True, exist_ok=True)
            flag_path.touch()
            logger.info(f"✅ [FIRST_RUN_PERMISSIONS] Флаг {flag_name} установлен: {flag_path}")
            return True
        except PermissionError as exc:
            logger.error(
                f"❌ [FIRST_RUN_PERMISSIONS] PermissionError при создании {flag_name}: {exc}\n"
                f"   Путь: {flag_path}\n"
                f"   Возможно запуск из sandbox - флаги будут использовать state_manager fallback"
            )
            return False
        except Exception as exc:
            logger.error(f"❌ [FIRST_RUN_PERMISSIONS] Не удалось установить {flag_name}: {exc}")
            return False

    def _clear_restart_flag(self) -> None:
        try:
            if self._restart_flag.exists():
                self._restart_flag.unlink()
                logger.debug("[FIRST_RUN_PERMISSIONS] restart_completed.flag удалён")
        except Exception as exc:
            logger.warning(f"[FIRST_RUN_PERMISSIONS] Не удалось удалить restart_completed.flag: {exc}")

    def _handle_restart_failure(self) -> None:
        """Fallback: разблокируем интеграции и очищаем флаг."""
        self._permissions_in_progress = False
        self._restart_session_id = None
        self._clear_restart_flag()
        self.state_manager.set_state_data("permissions_restart_pending", False)

    async def _publish_status_checked(
        self,
        *,
        permission: PermissionType,
        status: PermissionStatus,
        session_id: str,
        source: str,
    ) -> None:
        payload = {
            "permission": permission.value,
            "status": status.value,
            "session_id": session_id,
            "source": source,
        }
        logger.info(
            "[FIRST_RUN_PERMISSIONS] permissions.status_checked -> %s (status=%s, session=%s, source=%s)",
            permission.value,
            status.value,
            session_id,
            source,
        )
        try:
            await self.event_bus.publish("permissions.status_checked", payload)
        except Exception as exc:
            logger.debug(
                "[FIRST_RUN_PERMISSIONS] Не удалось опубликовать permissions.status_checked: %s",
                exc,
            )

    async def _publish_permission_changed(
        self,
        *,
        permission: PermissionType,
        old_status: PermissionStatus,
        new_status: PermissionStatus,
        session_id: str,
        source: str,
    ) -> None:
        payload = {
            "permission": permission.value,
            "old_status": old_status.value,
            "new_status": new_status.value,
            "session_id": session_id,
            "source": source,
        }
        logger.info(
            "[FIRST_RUN_PERMISSIONS] permissions.changed -> %s (%s → %s, session=%s, source=%s)",
            permission.value,
            old_status.value,
            new_status.value,
            session_id,
            source,
        )
        try:
            await self.event_bus.publish("permissions.changed", payload)
        except Exception as exc:
            logger.debug(
                "[FIRST_RUN_PERMISSIONS] Не удалось опубликовать permissions.changed: %s",
                exc,
            )

    def get_status(self) -> Dict[str, Any]:
        """Получить статус интеграции"""
        return {
            "initialized": self._initialized,
            "running": self._running,
            "permissions_in_progress": self._permissions_in_progress,
            "enabled": self.enabled,
            "pause_seconds": self.pause_seconds,
            "activation_hold_seconds": self.activation_hold_seconds,
            "first_run_completed": self.flag_file.exists(),
            "flag_file": str(self.flag_file),
        }
