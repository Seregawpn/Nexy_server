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

from config.unified_config_loader import UnifiedConfigLoader
from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_keys import StateKeys
from integration.core.event_types import EventTypes
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.utils.resource_path import get_user_data_dir

from modules.permissions.core.types import PermissionType
from modules.permission_restart.core.atomic_flag import AtomicRestartFlag
from modules.permissions.first_run.status_checker import (
    PermissionStatus,
    check_accessibility_status,
    check_contacts_status,
    check_full_disk_access_status,
    check_input_monitoring_status,
    check_microphone_status_no_prompt,
    check_screen_capture_status,
)

from modules.permissions.first_run.activator import (
    activate_microphone,
    activate_accessibility,
    activate_input_monitoring,
    activate_screen_capture,
    activate_contacts,
    activate_full_disk_access,
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
        
        # Batching настройки
        self.enable_batching = self.config.get('enable_batching', False)
        self.batch_size = self.config.get('batch_size', 3)

        logger.info(
            "[FIRST_RUN_PERMISSIONS] Configuration loaded: "
            "enabled=%s, pause_seconds=%s, activation_hold_seconds=%s, "
            "enable_batching=%s, batch_size=%s",
            self.enabled,
            self.pause_seconds,
            self.activation_hold_seconds,
            self.enable_batching,
            self.batch_size,
        )

        # Путь к флагам первого запуска (Application Support)
        self._data_dir = get_user_data_dir("Nexy")
        self.flag_file = self._data_dir / "permissions_first_run_completed.flag"
        
        # Атомарный флаг перезапуска в persistent директории
        restart_flag_path = self._data_dir / "restart_completed.flag"
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

    @property
    def are_all_granted(self) -> bool:
        """Проверить, все ли разрешения получены (для совместимости с coordinator)."""
        return self.flag_file.exists()

    # ==================== Batching Methods ====================

    def _get_batch_flag_path(self, batch_index: int) -> Path:
        """Get path to batch completion flag file."""
        return self._data_dir / f"permissions_batch_{batch_index}_completed.flag"

    def _get_current_batch_index(self) -> int:
        """
        Determine which batch to process based on existing flags.
        Returns 0-based batch index.
        """
        batch_index = 0
        while self._get_batch_flag_path(batch_index).exists():
            batch_index += 1
        return batch_index

    def _mark_batch_completed(self, batch_index: int) -> bool:
        """Mark a batch as completed by creating its flag file."""
        flag_path = self._get_batch_flag_path(batch_index)
        return self._safe_touch_flag(flag_path, f"batch_{batch_index}_completed")

    def _get_permissions_for_current_batch(self, all_permissions: list[str]) -> tuple[list[str], int, int]:
        """
        Get permissions for current batch based on batching settings.
        
        Returns:
            Tuple of (permissions_to_process, batch_index, total_batches)
        """
        if not self.enable_batching:
            # No batching - return all permissions
            return all_permissions, 0, 1

        total = len(all_permissions)
        batch_size = max(1, self.batch_size)
        total_batches = (total + batch_size - 1) // batch_size  # ceil division

        batch_index = self._get_current_batch_index()
        
        if batch_index >= total_batches:
            # All batches completed
            logger.info("[FIRST_RUN_PERMISSIONS] All batches already completed")
            return [], batch_index, total_batches

        start_idx = batch_index * batch_size
        end_idx = min(start_idx + batch_size, total)
        
        permissions_for_batch = all_permissions[start_idx:end_idx]
        
        logger.info(
            "[FIRST_RUN_PERMISSIONS] Batch %d/%d: permissions[%d:%d] = %s",
            batch_index + 1, total_batches, start_idx, end_idx, permissions_for_batch
        )
        print(f"📦 [FIRST_RUN] Батч {batch_index + 1}/{total_batches}: {permissions_for_batch}")
        
        return permissions_for_batch, batch_index, total_batches

    def _are_all_batches_completed(self) -> bool:
        """
        Check if all permission batches have been completed.
        
        Returns:
            True if all batches are done (or batching is disabled), False otherwise
        """
        if not self.enable_batching:
            # No batching - check only the main flag
            return self.flag_file.exists()

        # Load permission order to calculate total batches
        all_permissions = self._load_required_permissions_order()
        if not all_permissions:
            return True  # No permissions to request

        total = len(all_permissions)
        batch_size = max(1, self.batch_size)
        total_batches = (total + batch_size - 1) // batch_size

        current_batch_index = self._get_current_batch_index()
        all_done = current_batch_index >= total_batches
        
        logger.info(
            "[FIRST_RUN_PERMISSIONS] _are_all_batches_completed: batch_index=%d, total_batches=%d, all_done=%s",
            current_batch_index, total_batches, all_done
        )
        
        return all_done

    # ==================== End Batching Methods ====================

    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            logger.info("🔧 [FIRST_RUN_PERMISSIONS] Инициализация...")

            # Сбрасываем состояние при инициализации (важно для повторных запусков/тестов)
            self._restart_session_id = None
            self._permissions_in_progress = False
            self.state_manager.set_state_data(StateKeys.PERMISSIONS_RESTART_PENDING, False)
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
                logger.info("✅ [FIRST_RUN_PERMISSIONS] Перезапуск после батча обнаружен")
                if restarted_via_flag and restart_flag_data:
                    age_sec = time.monotonic() - restart_flag_data.timestamp if hasattr(time, 'monotonic') else 0
                    age_ms = int(age_sec * 1000)
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

                # КРИТИЧНО: Проверяем все ли батчи завершены
                all_batches_done = self._are_all_batches_completed()
                print(f"📊 [FIRST_RUN] После перезапуска: all_batches_done={all_batches_done}")
                
                if all_batches_done:
                    # Все батчи завершены - публикуем completed
                    logger.info("✅ [FIRST_RUN_PERMISSIONS] Все батчи завершены - публикуем completed")
                    await self.event_bus.publish("permissions.first_run_completed", {
                        "session_id": "restarted",
                        "source": "first_run_permissions_integration",
                        "note": "Published after all batches completed" + (" (test mode)" if test_mode else ""),
                        "restart_flag_data": {
                            "pid": restart_flag_data.pid if restart_flag_data else None,
                            "reason": restart_flag_data.reason if restart_flag_data else None,
                            "timestamp": restart_flag_data.timestamp if restart_flag_data else None,
                        } if restart_flag_data else None
                    })

                    self._clear_first_run_flag()
                    logger.info(
                        "[FIRST_RUN_PERMISSIONS] ✅ Флаги обработаны: restart_completed.flag удалён, "
                        "permissions_first_run_completed.flag сохранён"
                    )
                    self._update_first_run_state(completed=True, in_progress=False)
                    self.state_manager.set_state_data(StateKeys.PERMISSIONS_RESTART_COMPLETED_FALLBACK, True)
                else:
                    # Ещё есть батчи для обработки - продолжим в start()
                    current_batch = self._get_current_batch_index()
                    logger.info(f"📦 [FIRST_RUN_PERMISSIONS] Батчи не все завершены, текущий батч: {current_batch + 1}")
                    print(f"📦 [FIRST_RUN] Продолжаем с батча {current_batch + 1}...")
                    # НЕ устанавливаем completed, чтобы start() мог продолжить

                # Очищаем env переменную
                if restarted_via_env:
                    os.environ.pop("NEXY_FIRST_RUN_RESTARTED", None)

            elif self.flag_file.exists():
                # Флаг первого запуска присутствует, даже если restart flag уже очищен —
                # фиксируем завершение процедуры
                logger.info(
                    "[FIRST_RUN_PERMISSIONS] Обнаружен существующий permissions_first_run_completed.flag "
                    "- считаем процедуру первого запуска завершённой"
                )
                self.state_manager.set_state_data(StateKeys.PERMISSIONS_RESTART_COMPLETED_FALLBACK, True)
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
                # Запрашиваем разрешения последовательно (с поддержкой батчей)
                is_last_batch, batch_index, total_batches = await self._request_permissions_sequentially(session_id=session_id)
                
                print(f"📊 [FIRST_RUN] Результат: is_last_batch={is_last_batch}, batch={batch_index + 1}/{total_batches}")

                # Сохраняем финальный флаг ТОЛЬКО если это последний батч
                if is_last_batch:
                    if not self._safe_touch_flag(self.flag_file, "permissions_first_run_completed"):
                        logger.error("❌ [FIRST_RUN_PERMISSIONS] Критическая ошибка: не удалось сохранить флаг первого запуска")
                        await self.event_bus.publish("permissions.first_run_failed", {
                            "session_id": session_id,
                            "error": "Cannot create flag file",
                            "source": "first_run_permissions_integration"
                        })
                        self._handle_restart_failure()
                        return False

                    self._update_first_run_state(completed=True, in_progress=True)
                    logger.info("✅ [FIRST_RUN_PERMISSIONS] Все батчи завершены, первый запуск полностью завершён")
                    print("✅ [FIRST_RUN] Все батчи завершены!")
                else:
                    logger.info(f"📦 [FIRST_RUN_PERMISSIONS] Батч {batch_index + 1}/{total_batches} завершён, требуется перезапуск для следующего батча")
                    print(f"📦 [FIRST_RUN] Батч {batch_index + 1}/{total_batches} завершён, перезапуск для следующего батча...")

                # ВАЖНО: НЕ сбрасываем флаг permissions_in_progress!
                # Это предотвратит запуск остальных интеграций (voice_recognition и т.д.)
                # Флаг сбросится только при следующем запуске приложения после перезапуска

                # КРИТИЧНО: Устанавливаем флаг для публикации completed в НОВОМ процессе
                # Это предотвращает разблокировку voice_recognition ДО перезапуска
                if not self._set_restart_flag():
                    logger.warning("⚠️ [FIRST_RUN_PERMISSIONS] Не удалось установить restart_completed.flag")
                    # Используем state_manager как fallback

                self.state_manager.set_state_data(StateKeys.PERMISSIONS_RESTART_PENDING, True)
                self.state_manager.set_state_data(StateKeys.PERMISSIONS_RESTART_COMPLETED_FALLBACK, True)
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
                    "note": f"Batch {batch_index + 1}/{total_batches} - Restart required",
                    "is_last_batch": is_last_batch,
                    "batch_index": batch_index,
                    "total_batches": total_batches,
                })
                logger.info(
                    "[FIRST_RUN_PERMISSIONS] Event permissions.first_run_restart_pending published (session=%s, batch=%d/%d)",
                    session_id, batch_index + 1, total_batches,
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

    async def _request_permissions_sequentially(self, *, session_id: str) -> tuple[bool, int, int]:
        """
        Config-driven sequential permission activation with batching support.
        
        Returns:
            Tuple of (is_last_batch, batch_index, total_batches)
        """
        print(f"🔄 [FIRST_RUN] Начало последовательного запроса разрешений (session={session_id})")

        all_permissions = self._load_required_permissions_order()
        if not all_permissions:
            logger.error("❌ [FIRST_RUN_PERMISSIONS] Permission order is empty; aborting first-run flow")
            print("❌ [FIRST_RUN] Permission order is empty!")
            return True, 0, 1

        # Enhanced: Log the full order for debugging
        print(f"📋 [FIRST_RUN] Полный порядок разрешений ({len(all_permissions)} всего): {all_permissions}")
        logger.info("[FIRST_RUN_PERMISSIONS] Full permission order: %s", all_permissions)

        # Get permissions for current batch
        permissions_to_process, batch_index, total_batches = self._get_permissions_for_current_batch(all_permissions)
        
        if not permissions_to_process:
            # All batches already completed
            print(f"✅ [FIRST_RUN] Все батчи уже обработаны ({batch_index}/{total_batches})")
            return True, batch_index, total_batches

        activators = {
            "input_monitoring": (PermissionType.INPUT_MONITORING, activate_input_monitoring),
            "microphone": (PermissionType.MICROPHONE, activate_microphone),
            "screen_capture": (PermissionType.SCREEN_CAPTURE, activate_screen_capture),
            "contacts": (PermissionType.CONTACTS, activate_contacts),
            "full_disk_access": (PermissionType.FULL_DISK_ACCESS, activate_full_disk_access),
            "accessibility": (PermissionType.ACCESSIBILITY, activate_accessibility),
        }

        # Track which permissions were activated
        activated_permissions = []
        total_in_batch = len(permissions_to_process)

        for idx, perm_name in enumerate(permissions_to_process, start=1):
            entry = activators.get(perm_name)
            if not entry:
                logger.warning("⚠️ [FIRST_RUN_PERMISSIONS] Unknown permission in order: %s", perm_name)
                print(f"⚠️ [FIRST_RUN] Неизвестное разрешение: {perm_name}")
                continue

            permission_type, activate_fn = entry
            
            # Enhanced: Show progress with index
            print(f"🔐 [FIRST_RUN] Батч {batch_index + 1}/{total_batches} [{idx}/{total_in_batch}] Активация {perm_name}...")
            logger.info("🔐 [FIRST_RUN_PERMISSIONS] Batch %d/%d [%d/%d] Активация %s...", 
                       batch_index + 1, total_batches, idx, total_in_batch, perm_name)
            
            try:
                start_time = time.time()
                await activate_fn(hold_duration=self.activation_hold_seconds)
                elapsed = time.time() - start_time
                
                # Enhanced: Print success with timing
                print(f"   ✅ [FIRST_RUN] [{idx}/{total_in_batch}] {perm_name} завершена за {elapsed:.2f} сек")
                logger.info(
                    "   ✅ [%d/%d] %s завершена за %.2f сек",
                    idx, total_in_batch, perm_name, elapsed,
                )
                activated_permissions.append(perm_name)
                
            except Exception as exc:
                # Enhanced: Print errors too
                print(f"   ❌ [FIRST_RUN] [{idx}/{total_in_batch}] Ошибка активации {perm_name}: {exc}")
                logger.error(
                    "❌ [FIRST_RUN_PERMISSIONS] [%d/%d] Ошибка активации %s: %s",
                    idx, total_in_batch, perm_name, exc,
                )
                # NOTE: Continue to next permission - don't abort the whole flow
                continue

            await self._wait_for_permission_resolution(
                perm_name=perm_name,
                session_id=session_id,
                window_sec=self.activation_hold_seconds,
            )

            if self.pause_seconds:
                print(f"   ⏸️ [FIRST_RUN] Пауза {self.pause_seconds} сек перед следующим разрешением...")
                await asyncio.sleep(self.pause_seconds)

        # Mark current batch as completed
        if self.enable_batching:
            self._mark_batch_completed(batch_index)
            print(f"💾 [FIRST_RUN] Батч {batch_index + 1} сохранён")

        # Check if this is the last batch
        is_last_batch = (batch_index + 1) >= total_batches

        # Enhanced: Summary of what was processed
        print(f"✅ [FIRST_RUN] Батч {batch_index + 1}/{total_batches} обработан: {len(activated_permissions)}/{total_in_batch}")
        print(f"   Активированы: {activated_permissions}")
        print(f"   Последний батч: {'Да' if is_last_batch else 'Нет'}")
        logger.info(
            "✅ [FIRST_RUN_PERMISSIONS] Batch %d/%d completed: %d/%d - %s (is_last=%s)",
            batch_index + 1, total_batches, len(activated_permissions), total_in_batch, 
            activated_permissions, is_last_batch
        )

        return is_last_batch, batch_index, total_batches


    async def _wait_for_permission_resolution(
        self,
        *,
        perm_name: str,
        session_id: str,
        window_sec: float,
    ) -> None:
        """Waits up to window_sec for status to resolve; enforces a minimum window."""
        checkers = {
            "microphone": check_microphone_status_no_prompt,
            "accessibility": check_accessibility_status,
            "input_monitoring": check_input_monitoring_status,
            "screen_capture": check_screen_capture_status,
            "contacts": check_contacts_status,
            "full_disk_access": check_full_disk_access_status,
        }
        checker = checkers.get(perm_name)
        window_sec = max(0.0, float(window_sec))
        start_ts = time.monotonic()

        if not checker or window_sec <= 0.0:
            if window_sec:
                await asyncio.sleep(window_sec)
            return

        poll_interval = 0.5
        while True:
            status = checker()
            if status != PermissionStatus.NOT_DETERMINED:
                logger.info(
                    "[FIRST_RUN_PERMISSIONS] %s status resolved=%s (session=%s)",
                    perm_name,
                    status.value,
                    session_id,
                )
                break

            elapsed = time.monotonic() - start_ts
            if elapsed >= window_sec:
                logger.info(
                    "[FIRST_RUN_PERMISSIONS] %s status wait timeout after %.2fs (session=%s)",
                    perm_name,
                    elapsed,
                    session_id,
                )
                break

            await asyncio.sleep(poll_interval)

        elapsed_total = time.monotonic() - start_ts
        remaining = window_sec - elapsed_total
        if remaining > 0:
            await asyncio.sleep(remaining)

    def _load_required_permissions_order(self) -> list[str]:
        """Load permission order from unified_config.yaml (source of truth)."""
        try:
            config_loader = UnifiedConfigLoader.get_instance()
            config_data = config_loader._load_config()
            order = (
                config_data.get("integrations", {})
                .get("permissions", {})
                .get("required_permissions", [])
            )
            if isinstance(order, list) and order:
                return [str(item) for item in order]
        except Exception as exc:
            logger.error("❌ [FIRST_RUN_PERMISSIONS] Permission order config error: %s", exc)
        return []

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
                self.state_manager.set_state_data(StateKeys.FIRST_RUN_COMPLETED, completed)
                self.state_manager.set_state_data(StateKeys.FIRST_RUN_REQUIRED, not completed)
            if in_progress is not None:
                self.state_manager.set_state_data(StateKeys.FIRST_RUN_IN_PROGRESS, in_progress)
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
        self.state_manager.set_state_data(StateKeys.PERMISSIONS_RESTART_PENDING, False)
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
