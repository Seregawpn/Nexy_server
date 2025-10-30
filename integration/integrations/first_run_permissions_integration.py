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

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from integration.utils.resource_path import get_user_data_dir

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

        self._initialized = False
        self._running = False
        self._permissions_in_progress = False

    async def initialize(self) -> bool:
        """Инициализация интеграции"""
        try:
            logger.info("🔧 [FIRST_RUN_PERMISSIONS] Инициализация...")

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
                # Запрашиваем разрешения последовательно
                await self._request_permissions_sequentially()

                # Сохраняем флаг
                try:
                    self.flag_file.touch()
                    logger.info(f"✅ [FIRST_RUN_PERMISSIONS] Флаг сохранён: {self.flag_file}")
                except Exception as e:
                    logger.error(f"❌ [FIRST_RUN_PERMISSIONS] Не удалось сохранить флаг: {e}")

                # Публикуем успешное завершение
                await self.event_bus.publish("permissions.first_run_completed", {
                    "session_id": session_id,
                    "source": "first_run_permissions_integration"
                })

                logger.info("✅ [FIRST_RUN_PERMISSIONS] Первый запуск завершён")
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
            try:
                self.flag_file.touch()
                logger.info("✅ [FIRST_RUN_PERMISSIONS] Флаг сохранён (после ошибки)")
            except Exception:
                pass
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

    async def _request_permissions_sequentially(self):
        """Запросить все разрешения последовательно с умными паузами"""
        import time

        # 1. MICROPHONE
        logger.info("🎙️ [FIRST_RUN_PERMISSIONS] Проверка Microphone...")
        mic_status = check_microphone_status()
        logger.info(f"   Статус: {mic_status.value}")

        if mic_status == PermissionStatus.NOT_DETERMINED:
            logger.info(
                "   Активируем Microphone с hold_duration=%s сек...",
                self.activation_hold_seconds
            )
            start_time = time.time()
            # activate_microphone держит микрофон открытым всю паузу
            # это гарантирует что диалог успеет появиться
            success = await activate_microphone(hold_duration=self.activation_hold_seconds)
            elapsed = time.time() - start_time
            logger.info(
                "   ✅ Microphone activation завершена за %.2f сек (ожидалось %.2f сек)",
                elapsed,
                self.activation_hold_seconds
            )
            # Отдельная пауза НЕ нужна - функция уже подождала
        else:
            logger.info("   Пропускаем (разрешение уже решено)")

        # 2. ACCESSIBILITY
        logger.info("♿ [FIRST_RUN_PERMISSIONS] Проверка Accessibility...")
        acc_status = check_accessibility_status()
        logger.info(f"   Статус: {acc_status.value}")

        if acc_status == PermissionStatus.NOT_DETERMINED:
            logger.info(
                "   Активируем Accessibility с hold_duration=%s сек...",
                self.activation_hold_seconds
            )
            start_time = time.time()
            # activate_accessibility держит паузу внутри себя
            success = await activate_accessibility(hold_duration=self.activation_hold_seconds)
            elapsed = time.time() - start_time
            logger.info(
                "   ✅ Accessibility activation завершена за %.2f сек (ожидалось %.2f сек)",
                elapsed,
                self.activation_hold_seconds
            )
            # Отдельная пауза НЕ нужна - функция уже подождала
        else:
            logger.info("   Пропускаем (разрешение уже решено)")

        # 3. INPUT MONITORING
        logger.info("⌨️ [FIRST_RUN_PERMISSIONS] Проверка Input Monitoring...")
        input_status = check_input_monitoring_status()
        logger.info(f"   Статус: {input_status.value}")

        if input_status == PermissionStatus.NOT_DETERMINED:
            logger.info(
                "   Активируем Input Monitoring с hold_duration=%s сек...",
                self.activation_hold_seconds
            )
            start_time = time.time()
            success = await activate_input_monitoring(hold_duration=self.activation_hold_seconds)
            elapsed = time.time() - start_time
            logger.info(
                "   ✅ Input Monitoring activation завершена за %.2f сек (ожидалось %.2f сек)",
                elapsed,
                self.activation_hold_seconds
            )
        else:
            logger.info("   Пропускаем (разрешение уже решено)")

        # 4. SCREEN CAPTURE
        logger.info("📺 [FIRST_RUN_PERMISSIONS] Проверка Screen Capture...")
        screen_status = check_screen_capture_status()
        logger.info(f"   Статус: {screen_status.value}")

        if screen_status == PermissionStatus.NOT_DETERMINED:
            logger.info(
                "   Активируем Screen Capture с hold_duration=%s сек...",
                self.activation_hold_seconds
            )
            start_time = time.time()
            # activate_screen_capture держит паузу внутри себя
            success = await activate_screen_capture(hold_duration=self.activation_hold_seconds)
            elapsed = time.time() - start_time
            logger.info(
                "   ✅ Screen Capture activation завершена за %.2f сек (ожидалось %.2f сек)",
                elapsed,
                self.activation_hold_seconds
            )
            # Отдельная пауза НЕ нужна - функция уже подождала
        else:
            logger.info("   Пропускаем (разрешение уже решено)")

        logger.info("✅ [FIRST_RUN_PERMISSIONS] Все разрешения обработаны")
        
        # Сбрасываем флаг процесса после завершения
        self._permissions_in_progress = False

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
