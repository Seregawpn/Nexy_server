"""
FirstRunPermissionsIntegration - запрос разрешений при первом запуске приложения.

Последовательно запрашивает системные разрешения с паузами между ними.
Работает ТОЛЬКО при первом запуске (определяется по флагу).
"""

import asyncio
import logging
import time
from typing import Optional, Dict, Any
from pathlib import Path
import uuid
import os

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.utils.resource_path import get_user_data_dir

from modules.permissions.core.types import PermissionType
from modules.permission_restart.core.atomic_flag import AtomicRestartFlag
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

        # Путь к флагам первого запуска (Application Support)
        data_dir = get_user_data_dir("Nexy")
        self.flag_file = data_dir / "permissions_first_run_completed.flag"
        
        # Атомарный флаг перезапуска в persistent директории
        restart_flag_path = data_dir / "restart_completed.flag"
        self._restart_flag = AtomicRestartFlag(restart_flag_path)
        logger.info(
            "[FIRST_RUN_PERMISSIONS] Флаги: permissions=%s restart=%s",
            self.flag_file,
            restart_flag_path,
        )
        if str(restart_flag_path).startswith("/tmp"):
            logger.warning(
                "[FIRST_RUN_PERMISSIONS] ⚠️ restart_completed.flag расположен во временной директории (%s) "
                "- перезапуск может не зафиксироваться",
                restart_flag_path,
            )

        # Фиксируем базовое состояние first_run (флаг присутствует → процедура завершена)
        self._update_first_run_state(completed=self.flag_file.exists(), in_progress=False)

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
            self._update_first_run_state(completed=self.flag_file.exists(), in_progress=False)

            # КРИТИЧНО: Проверяем был ли перезапуск после first_run
            # Это позволяет опубликовать completed ТОЛЬКО после успешного перезапуска
            # Также проверяем env переменную NEXY_FIRST_RUN_RESTARTED (для dev-режима)
            # Используем атомарный флаг для чтения-и-удаления
            restart_flag_data = self._restart_flag.read_and_remove()
            restarted_via_flag = restart_flag_data is not None
            restarted_via_env = os.environ.get("NEXY_FIRST_RUN_RESTARTED") == "1"
            
            # 🧪 ТЕСТОВЫЙ РЕЖИМ: эмулируем перезапуск если флаги существуют
            test_mode = os.environ.get("NEXY_TEST_SKIP_PERMISSIONS") == "1"
            if test_mode and self.flag_file.exists() and restart_flag_data:
                logger.info("🧪 [FIRST_RUN_PERMISSIONS] ТЕСТОВЫЙ РЕЖИМ: эмулируем перезапуск")
                restarted_via_flag = True  # Принудительно активируем логику перезапуска

            if restarted_via_flag or restarted_via_env:
                logger.info("✅ [FIRST_RUN_PERMISSIONS] Перезапуск после first_run завершён успешно")
                if restarted_via_flag and restart_flag_data:
                    age_sec = time.monotonic() - restart_flag_data.timestamp if hasattr(time, 'monotonic') else 0
                    age_ms = int(age_sec * 1000)
                    # КРИТИЧНО: Логируем RESTART_FLAG в формате для приёмки
                    # Фиксируем возраст флага и PID инициатора для диагностики
                    logger.info(
                        f"RESTART_FLAG seen_ts={restart_flag_data.timestamp:.2f}, "
                        f"age_ms={age_ms}, pid={restart_flag_data.pid}, "
                        f"reason={restart_flag_data.reason}, "
                        f"permissions={restart_flag_data.permissions}"
                    )
                if restarted_via_env:
                    logger.info("   (обнаружено через NEXY_FIRST_RUN_RESTARTED env)")
                if test_mode:
                    logger.info("   (тестовый режим)")

                # Публикуем completed в НОВОМ процессе (после перезапуска)
                await self.event_bus.publish("permissions.first_run_completed", {
                    "session_id": "restarted",
                    "source": "first_run_permissions_integration",
                    "note": "Published after successful restart" + (" (test mode)" if test_mode else ""),
                    "restart_flag_data": {
                        "pid": restart_flag_data.pid if restart_flag_data else None,
                        "reason": restart_flag_data.reason if restart_flag_data else None,
                        "timestamp": restart_flag_data.timestamp if restart_flag_data else None,
                    } if restart_flag_data else None
                })

                # КРИТИЧНО: Обновляем флаги после публикации
                # restart_completed.flag уже удален через read_and_remove()
                # permissions_first_run_completed.flag сохраняем для пропуска повторной процедуры
                self._clear_first_run_flag()
                logger.info(
                    "[FIRST_RUN_PERMISSIONS] ✅ Флаги обработаны: restart_completed.flag удалён, "
                    "permissions_first_run_completed.flag сохранён"
                )
                self._update_first_run_state(completed=True, in_progress=False)
                
                # Устанавливаем fallback флаг в state_manager (для других интеграций)
                self.state_manager.set_state_data("permissions_restart_completed_fallback", True)
                logger.info("[FIRST_RUN_PERMISSIONS] Set restart_completed_fallback=True in state_manager")

                # Очищаем env переменную
                if restarted_via_env:
                    os.environ.pop("NEXY_FIRST_RUN_RESTARTED", None)

            elif self.flag_file.exists():
                # Флаг первого запуска присутствует, даже если restart flag уже очищен —
                # фиксируем завершение процедуры, чтобы PermissionRestartIntegration
                # мог полагаться на fallback без повторной проверки Permission APIs.
                logger.info(
                    "[FIRST_RUN_PERMISSIONS] Обнаружен существующий permissions_first_run_completed.flag "
                    "- считаем процедуру первого запуска завершённой"
                )
                self.state_manager.set_state_data("permissions_restart_completed_fallback", True)
                logger.info("[FIRST_RUN_PERMISSIONS] Set restart_completed_fallback=True in state_manager (flag only)")
                self._update_first_run_state(completed=True, in_progress=False)

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

            # 🧪 ВРЕМЕННАЯ ЗАГЛУШКА для тестирования: пропускаем проверку разрешений
            if os.environ.get("NEXY_TEST_SKIP_PERMISSIONS") == "1":
                logger.warning("🧪 [FIRST_RUN_PERMISSIONS] ТЕСТОВЫЙ РЕЖИМ: пропускаем проверку разрешений (NEXY_TEST_SKIP_PERMISSIONS=1)")
                
                # Если флага НЕТ - создаём флаги (эмулируем первый запуск)
                # При следующем запуске initialize() обработает их и опубликует событие
                if not self.flag_file.exists():
                    logger.info("🧪 [FIRST_RUN_PERMISSIONS] Создаём флаги для эмуляции первого запуска")
                    self._safe_touch_flag(self.flag_file, "permissions_first_run_completed")
                    self._safe_touch_flag(self._restart_flag, "restart_completed")
                    logger.info("🧪 [FIRST_RUN_PERMISSIONS] Флаги созданы - при следующем запуске будет эмулирован перезапуск")
                    self._update_first_run_state(completed=True, in_progress=False)
            
                return True

            # Проверяем флаг первого запуска
            if self.flag_file.exists():
                logger.info("✅ [FIRST_RUN_PERMISSIONS] Первый запуск уже завершён - пропускаем")
                self._update_first_run_state(completed=True, in_progress=False)
                return True

            # Если флага нет, но ВСЕ разрешения уже выданы - считаем что первый запуск был
            # (например, флаги были удалены после успешного перезапуска)
            mic_status = check_microphone_status()
            accessibility_status = check_accessibility_status()
            screen_status = check_screen_capture_status()
            input_status = check_input_monitoring_status()
            
            if (mic_status == PermissionStatus.GRANTED and
                accessibility_status == PermissionStatus.GRANTED and
                screen_status == PermissionStatus.GRANTED and
                input_status == PermissionStatus.GRANTED):
                logger.info("✅ [FIRST_RUN_PERMISSIONS] Все разрешения уже выданы - первый запуск был ранее")
                self._update_first_run_state(completed=True, in_progress=False)
                return True

            # ПЕРВЫЙ ЗАПУСК!
            logger.info("🔐 [FIRST_RUN_PERMISSIONS] Первый запуск обнаружен - запрашиваем разрешения")

            # Публикуем начало процесса запроса разрешений
            session_id = str(uuid.uuid4())
            await self.event_bus.publish("permissions.first_run_started", {
                "session_id": session_id,
                "source": "first_run_permissions_integration"
            })
            self._update_first_run_state(completed=False, in_progress=True)

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

                self._update_first_run_state(completed=True, in_progress=True)

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
                logger.info(
                    "[FIRST_RUN_PERMISSIONS] State updated: permissions_restart_pending=True, permissions_restart_completed_fallback=True"
                )

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
                logger.info(
                    "[FIRST_RUN_PERMISSIONS] Event permissions.first_run_restart_pending published (session=%s)",
                    session_id,
                )

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
            self._update_first_run_state(completed=False, in_progress=False)

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

        print(f"🔄 [FIRST_RUN] Начало последовательного запроса разрешений (session={session_id})")  # DEBUG

        # 1. MICROPHONE
        logger.info("🎙️ [FIRST_RUN_PERMISSIONS] Проверка Microphone...")
        # На первом запросе считаем статус неопределённым, даже если TCC хранит решение.
        mic_status = PermissionStatus.NOT_DETERMINED
        logger.info("   Статус: not_determined (форсированный перед активацией)")
        await self._publish_status_checked(
            permission=PermissionType.MICROPHONE,
            status=mic_status,
            session_id=session_id,
            source="first_run.pre_activation",
        )

        logger.info(
            "   Активируем Microphone независимо от текущего статуса (hold_duration=%s сек)...",
            self.activation_hold_seconds,
        )
        start_time = time.time()
        await activate_microphone(hold_duration=self.activation_hold_seconds)
        elapsed = time.time() - start_time
        logger.info(
            "   ✅ Microphone activation завершена за %.2f сек (ожидалось %.2f сек)",
            elapsed,
            self.activation_hold_seconds,
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

        # 2. ACCESSIBILITY
        logger.info("♿ [FIRST_RUN_PERMISSIONS] Проверка Accessibility...")
        acc_status = PermissionStatus.NOT_DETERMINED
        logger.info("   Статус: not_determined (форсированный перед активацией)")
        await self._publish_status_checked(
            permission=PermissionType.ACCESSIBILITY,
            status=acc_status,
            session_id=session_id,
            source="first_run.pre_activation",
        )
        logger.info(
            "   Активируем Accessibility независимо от статуса (hold_duration=%s сек)...",
            self.activation_hold_seconds,
        )
        start_time = time.time()
        await activate_accessibility(hold_duration=self.activation_hold_seconds)
        elapsed = time.time() - start_time
        logger.info(
            "   ✅ Accessibility activation завершена за %.2f сек (ожидалось %.2f сек)",
            elapsed,
            self.activation_hold_seconds,
        )
        new_status = check_accessibility_status()
        if new_status != PermissionStatus.GRANTED:
            logger.warning(
                "⚠️ [FIRST_RUN_PERMISSIONS] Accessibility status=%s после %.2f сек, считаем GRANTED",
                new_status.value,
                elapsed,
            )
            new_status = PermissionStatus.GRANTED
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

        # 3. INPUT MONITORING
        logger.info("⌨️ [FIRST_RUN_PERMISSIONS] Проверка Input Monitoring...")
        input_status = PermissionStatus.NOT_DETERMINED
        logger.info("   Статус: not_determined (форсированный перед активацией)")
        await self._publish_status_checked(
            permission=PermissionType.INPUT_MONITORING,
            status=input_status,
            session_id=session_id,
            source="first_run.pre_activation",
        )
        logger.info(
            "   Активируем Input Monitoring независимо от статуса (hold_duration=%s сек)...",
            self.activation_hold_seconds,
        )
        start_time = time.time()
        await activate_input_monitoring(hold_duration=self.activation_hold_seconds)
        elapsed = time.time() - start_time
        logger.info(
            "   ✅ Input Monitoring activation завершена за %.2f сек (ожидалось %.2f сек)",
            elapsed,
            self.activation_hold_seconds,
        )
        new_status = check_input_monitoring_status()
        if new_status != PermissionStatus.GRANTED:
            logger.warning(
                "⚠️ [FIRST_RUN_PERMISSIONS] Input Monitoring status=%s после %.2f сек, считаем GRANTED",
                new_status.value,
                elapsed,
            )
            new_status = PermissionStatus.GRANTED
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

        # 4. SCREEN CAPTURE
        logger.info("📺 [FIRST_RUN_PERMISSIONS] Проверка Screen Capture...")
        screen_status = PermissionStatus.NOT_DETERMINED
        logger.info("   Статус: not_determined (форсированный перед активацией)")
        await self._publish_status_checked(
            permission=PermissionType.SCREEN_CAPTURE,
            status=screen_status,
            session_id=session_id,
            source="first_run.pre_activation",
        )
        logger.info(
            "   Активируем Screen Capture независимо от статуса (hold_duration=%s сек)...",
            self.activation_hold_seconds,
        )
        start_time = time.time()
        await activate_screen_capture(hold_duration=self.activation_hold_seconds)
        elapsed = time.time() - start_time
        logger.info(
            "   ✅ Screen Capture activation завершена за %.2f сек (ожидалось %.2f сек)",
            elapsed,
            self.activation_hold_seconds,
        )
        new_status = check_screen_capture_status()
        if new_status != PermissionStatus.GRANTED:
            logger.warning(
                "⚠️ [FIRST_RUN_PERMISSIONS] Screen Capture status=%s после %.2f сек, считаем GRANTED",
                new_status.value,
                elapsed,
            )
            new_status = PermissionStatus.GRANTED
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
            logger.info("✅ [FIRST_RUN_PERMISSIONS] Permissions restart handler accepted request (session=%s)", session)

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
        logger.info(f"[FIRST_RUN_PERMISSIONS] Установка restart_completed.flag: {self._restart_flag.flag_path}")
        try:
            # Используем метод write() из AtomicRestartFlag вместо _safe_touch_flag
            result = self._restart_flag.write(
                reason="first_run_completed",
                permissions=["microphone", "accessibility", "input_monitoring", "screen_capture"]
            )
            if result:
                logger.info(f"[FIRST_RUN_PERMISSIONS] ✅ restart_completed.flag установлен: {self._restart_flag.flag_path}")
            else:
                logger.error(f"[FIRST_RUN_PERMISSIONS] ❌ restart_completed.flag не удалось установить: {self._restart_flag.flag_path}")
            return result
        except Exception as exc:
            logger.error(f"[FIRST_RUN_PERMISSIONS] ❌ Не удалось установить restart_completed: {exc}")
            return False

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
        """Удаляем restart_completed.flag после успешного перезапуска."""
        # Флаг уже удален через read_and_remove() в initialize()
        # Этот метод оставлен для обратной совместимости
        try:
            if self._restart_flag.exists():
                self._restart_flag.remove()
                logger.info(
                    f"[FIRST_RUN_PERMISSIONS] restart_completed.flag удалён: {self._restart_flag.flag_path}"
                )
            else:
                logger.debug(
                    f"[FIRST_RUN_PERMISSIONS] restart_completed.flag отсутствует: {self._restart_flag.flag_path}"
                )
        except Exception as exc:
            logger.error(f"[FIRST_RUN_PERMISSIONS] ❌ Ошибка удаления restart_completed.flag: {exc}")
    
    def _clear_first_run_flag(self) -> None:
        """Фиксируем флаг первого запуска (сохраняем его для последующих запусков)"""
        try:
            if self.flag_file.exists():
                logger.info(
                    f"[FIRST_RUN_PERMISSIONS] permissions_first_run_completed.flag сохранён: {self.flag_file}"
                )
            else:
                logger.debug(
                    f"[FIRST_RUN_PERMISSIONS] permissions_first_run_completed.flag отсутствует: {self.flag_file}"
                )
        except Exception as exc:
            logger.error(f"[FIRST_RUN_PERMISSIONS] ❌ Ошибка обработки permissions_first_run_completed.flag: {exc}")

    def _update_first_run_state(self, *, completed: Optional[bool] = None, in_progress: Optional[bool] = None) -> None:
        """Синхронизирует состояние first_run в state_manager (fallback для селекторов)."""
        try:
            if completed is not None:
                self.state_manager.set_state_data("first_run_completed", completed)
                self.state_manager.set_state_data("first_run_required", not completed)
            if in_progress is not None:
                self.state_manager.set_state_data("first_run_in_progress", in_progress)
        except Exception:
            logger.debug(
                "[FIRST_RUN_PERMISSIONS] Не удалось обновить состояние first_run (completed=%s, in_progress=%s)",
                completed,
                in_progress,
            )

    def _handle_restart_failure(self) -> None:
        """Fallback: разблокируем интеграции и очищаем флаг."""
        self._permissions_in_progress = False
        self._restart_session_id = None
        self._clear_restart_flag()
        self.state_manager.set_state_data("permissions_restart_pending", False)
        logger.warning("[FIRST_RUN_PERMISSIONS] Restart flow failed, state reset (permissions_restart_pending=False)")

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
