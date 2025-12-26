"""
FirstRunPermissionsIntegration - проверка и запрос разрешений при КАЖДОМ запуске приложения.

Логика:
1. При каждом запуске проверяет ВСЕ разрешения (mic, accessibility, screen, input)
2. Если какое-то не GRANTED → активирует и ждёт получения (БЕЗ таймаута)
3. После получения всех → проверяет нужен ли перезапуск:
   - Accessibility/Input Monitoring/Screen Capture: требуют перезапуска
   - Microphone: не требует перезапуска

БЛОКИРУЕТ запуск остальных интеграций пока ВСЕ разрешения не будут получены!
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
        self.activation_hold_seconds = self.config.get('activation_hold_duration_sec', 13.0)

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
            self.state_manager.set_restart_pending(False)
            self._update_first_run_state(completed=self.flag_file.exists(), in_progress=False)
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
                self.state_manager.set_restart_completed_fallback(True)
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
                self.state_manager.set_restart_completed_fallback(True)
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
        Запуск интеграции - проверка разрешений при КАЖДОМ запуске.

        Логика:
        1. Проверяем ВСЕ разрешения
        2. Если какое-то не GRANTED → активируем и ждём (БЕЗ таймаута)
        3. Когда все получены → проверяем, нужен ли перезапуск
        4. Перезапуск нужен для Accessibility/Input Monitoring (CGEventTap)

        БЛОКИРУЕТ запуск остальных интеграций пока ВСЕ разрешения не будут получены!
        """
        try:
            if not self._initialized:
                logger.error("❌ [PERMISSIONS] Не инициализирован")
                return False

            # Проверяем enabled
            if not self.enabled:
                logger.info("ℹ️ [PERMISSIONS] Отключено - пропускаем")
                return True

            # 🧪 ВРЕМЕННАЯ ЗАГЛУШКА для тестирования
            if os.environ.get("NEXY_TEST_SKIP_PERMISSIONS") == "1":
                logger.warning("🧪 [PERMISSIONS] ТЕСТОВЫЙ РЕЖИМ: пропускаем проверку разрешений")
                return True

            # Публикуем начало проверки разрешений
            session_id = str(uuid.uuid4())
            logger.info(f"🔐 [PERMISSIONS] Проверка разрешений при запуске (session={session_id})")

            # Проверяем текущие статусы
            mic_status = check_microphone_status()
            accessibility_status = check_accessibility_status()
            screen_status = check_screen_capture_status()
            input_status = check_input_monitoring_status()

            logger.info(
                f"📋 [PERMISSIONS] Текущие статусы: "
                f"mic={mic_status.value}, accessibility={accessibility_status.value}, "
                f"screen={screen_status.value}, input={input_status.value}"
            )

            # Если все разрешения выданы — сразу продолжаем
            if (mic_status == PermissionStatus.GRANTED and
                accessibility_status == PermissionStatus.GRANTED and
                screen_status == PermissionStatus.GRANTED and
                input_status == PermissionStatus.GRANTED):
                logger.info("✅ [PERMISSIONS] Все разрешения уже выданы — продолжаем работу")
                self._update_first_run_state(completed=True, in_progress=False)
                
                # Публикуем готовность
                await self.event_bus.publish("permissions.first_run_completed", {
                    "session_id": session_id,
                    "source": "permissions_integration",
                    "all_granted": True
                })
                return True

            # Есть разрешения которые нужно получить
            logger.info("⏳ [PERMISSIONS] Некоторые разрешения не выданы — начинаем запрос")
            
            await self.event_bus.publish("permissions.first_run_started", {
                "session_id": session_id,
                "source": "permissions_integration"
            })
            self._update_first_run_state(completed=False, in_progress=True)

            self._running = True
            self._permissions_in_progress = True

            # Отслеживаем, нужен ли перезапуск
            needs_restart = False

            try:
                # Запрашиваем каждое разрешение и ждём получения
                needs_restart = await self._request_and_wait_for_permissions(session_id=session_id)

                logger.info("✅ [PERMISSIONS] Все разрешения получены!")

                if needs_restart:
                    logger.info("🔄 [PERMISSIONS] Требуется перезапуск для активации Accessibility/Input Monitoring")
                    
                    # Сохраняем флаги для нового процесса
                    self._safe_touch_flag(self.flag_file, "permissions_completed")
                    self._set_restart_flag()
                    
                    self.state_manager.set_restart_pending(True)
                    self.state_manager.set_restart_completed_fallback(True)

                    # Публикуем событие ожидания перезапуска
                    await self.event_bus.publish("permissions.first_run_restart_pending", {
                        "session_id": session_id,
                        "source": "permissions_integration",
                        "reason": "accessibility_or_input_monitoring_granted"
                    })

                    self._restart_session_id = session_id
                    return True
                else:
                    # Перезапуск не нужен — продолжаем
                    self._update_first_run_state(completed=True, in_progress=False)
                    self._permissions_in_progress = False
                    
                    await self.event_bus.publish("permissions.first_run_completed", {
                        "session_id": session_id,
                        "source": "permissions_integration",
                        "all_granted": True,
                        "restart_needed": False
                    })
                    return True

            except Exception as e:
                logger.error(f"❌ [PERMISSIONS] Ошибка при запросе разрешений: {e}")
                await self.event_bus.publish("permissions.first_run_failed", {
                    "session_id": session_id,
                    "error": str(e),
                    "source": "permissions_integration"
                })
                raise

        except Exception as e:
            logger.error(f"❌ [PERMISSIONS] Ошибка запуска: {e}")
            self._running = False
            self._permissions_in_progress = False
            self._update_first_run_state(completed=False, in_progress=False)
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

    async def _request_and_wait_for_permissions(self, *, session_id: str) -> bool:
        """
        Запрашивает каждое разрешение и ждёт его получения (без таймаута).

        Returns:
            True если требуется перезапуск (Accessibility/Input Monitoring были запрошены)
            False если перезапуск не нужен
        """
        needs_restart = False

        # Порядок важен: сначала те, что требуют перезапуска
        # 1. INPUT MONITORING (требует перезапуска для CGEventTap)
        input_status = check_input_monitoring_status()
        if input_status != PermissionStatus.GRANTED:
            logger.info("⌨️ [PERMISSIONS] Input Monitoring не выдан — запрашиваем...")
            await self._activate_and_wait_for_permission(
                permission_type=PermissionType.INPUT_MONITORING,
                check_func=check_input_monitoring_status,
                activate_func=activate_input_monitoring,
                open_settings_func=self._open_input_monitoring_settings,
                session_id=session_id
            )
            needs_restart = True  # Input Monitoring требует перезапуска

        # 2. ACCESSIBILITY (требует перезапуска для CGEventTap)
        accessibility_status = check_accessibility_status()
        if accessibility_status != PermissionStatus.GRANTED:
            logger.info("♿ [PERMISSIONS] Accessibility не выдан — запрашиваем...")
            await self._activate_and_wait_for_permission(
                permission_type=PermissionType.ACCESSIBILITY,
                check_func=check_accessibility_status,
                activate_func=activate_accessibility,
                open_settings_func=self._open_accessibility_settings,
                session_id=session_id
            )
            needs_restart = True  # Accessibility требует перезапуска

        # 3. MICROPHONE (не требует перезапуска)
        mic_status = check_microphone_status()
        if mic_status != PermissionStatus.GRANTED:
            logger.info("🎙️ [PERMISSIONS] Microphone не выдан — запрашиваем...")
            await self._activate_and_wait_for_permission(
                permission_type=PermissionType.MICROPHONE,
                check_func=check_microphone_status,
                activate_func=activate_microphone,
                open_settings_func=self._open_microphone_settings,
                session_id=session_id
            )
            # Microphone НЕ требует перезапуска

        # 4. SCREEN CAPTURE (требует перезапуска для CGWindowListCreateImage и др.)
        screen_status = check_screen_capture_status()
        if screen_status != PermissionStatus.GRANTED:
            logger.info("📺 [PERMISSIONS] Screen Capture не выдан — запрашиваем...")
            await self._activate_and_wait_for_permission(
                permission_type=PermissionType.SCREEN_CAPTURE,
                check_func=check_screen_capture_status,
                activate_func=activate_screen_capture,
                open_settings_func=self._open_screen_capture_settings,
                session_id=session_id
            )
            needs_restart = True  # Screen Capture тоже требует перезапуска


        return needs_restart

    async def _activate_and_wait_for_permission(
        self,
        *,
        permission_type: PermissionType,
        check_func,
        activate_func,
        open_settings_func,
        session_id: str
    ):
        """
        Активирует запрос разрешения и ждёт его получения БЕЗ таймаута.

        Args:
            permission_type: Тип разрешения
            check_func: Функция проверки статуса
            activate_func: Функция активации (показ диалога)
            open_settings_func: Функция открытия настроек (для DENIED)
            session_id: ID сессии
        """
        check_interval = 1.0  # Проверка каждую секунду
        log_interval = 10  # Логируем каждые 10 секунд
        checks_since_log = 0

        # Сначала проверяем текущий статус
        status = check_func()
        
        await self._publish_status_checked(
            permission=permission_type,
            status=status,
            session_id=session_id,
            source="permissions.pre_activation"
        )

        if status == PermissionStatus.GRANTED:
            logger.info(f"✅ [{permission_type.value}] Уже выдано!")
            return

        # Активируем (покажет диалог для NOT_DETERMINED)
        logger.info(f"⏳ [{permission_type.value}] Активация запроса разрешения...")
        await activate_func(hold_duration=self.activation_hold_seconds)

        # Проверяем после активации
        status = check_func()
        if status == PermissionStatus.GRANTED:
            logger.info(f"✅ [{permission_type.value}] Получено после активации!")
            await self._publish_status_checked(
                permission=permission_type,
                status=status,
                session_id=session_id,
                source="permissions.post_activation"
            )
            return

        # Если всё ещё не получено — открываем настройки и ждём
        if status != PermissionStatus.GRANTED:
            logger.info(f"📋 [{permission_type.value}] Открываем настройки и ждём выдачи...")
            open_settings_func()

        # Ждём бесконечно пока не получим GRANTED
        while True:
            status = check_func()

            if status == PermissionStatus.GRANTED:
                logger.info(f"✅ [{permission_type.value}] Разрешение получено!")
                await self._publish_status_checked(
                    permission=permission_type,
                    status=status,
                    session_id=session_id,
                    source="permissions.granted"
                )
                return

            checks_since_log += 1
            if checks_since_log >= log_interval:
                logger.info(f"⏳ [{permission_type.value}] Ожидание разрешения... (status={status.value})")
                checks_since_log = 0

            await asyncio.sleep(check_interval)

    def _open_accessibility_settings(self):
        """Открывает настройки Accessibility."""
        import subprocess
        try:
            subprocess.run(
                ['open', 'x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility'],
                check=True,
            )
            logger.info("📋 Открыты настройки Accessibility")
        except Exception as e:
            logger.warning(f"⚠️ Не удалось открыть настройки Accessibility: {e}")

    def _open_input_monitoring_settings(self):
        """Открывает настройки Input Monitoring."""
        import subprocess
        try:
            subprocess.run(
                ['open', 'x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent'],
                check=True,
            )
            logger.info("📋 Открыты настройки Input Monitoring")
        except Exception as e:
            logger.warning(f"⚠️ Не удалось открыть настройки Input Monitoring: {e}")

    def _open_microphone_settings(self):
        """Открывает настройки Microphone."""
        import subprocess
        try:
            subprocess.run(
                ['open', 'x-apple.systempreferences:com.apple.preference.security?Privacy_Microphone'],
                check=True,
            )
            logger.info("📋 Открыты настройки Microphone")
        except Exception as e:
            logger.warning(f"⚠️ Не удалось открыть настройки Microphone: {e}")

    def _open_screen_capture_settings(self):
        """Открывает настройки Screen Recording."""
        import subprocess
        try:
            subprocess.run(
                ['open', 'x-apple.systempreferences:com.apple.preference.security?Privacy_ScreenCapture'],
                check=True,
            )
            logger.info("📋 Открыты настройки Screen Capture")
        except Exception as e:
            logger.warning(f"⚠️ Не удалось открыть настройки Screen Capture: {e}")


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
            # We assume sensible defaults if partial args are given, but usually both are provided.
            is_completed = completed if completed is not None else False 
            is_in_progress = in_progress if in_progress is not None else False
            is_required = not is_completed

            self.state_manager.set_first_run_state(
                in_progress=is_in_progress,
                required=is_required,
                completed=is_completed
            )
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
        self._restart_session_id = None
        self._clear_restart_flag()
        self.state_manager.set_restart_pending(False)
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
