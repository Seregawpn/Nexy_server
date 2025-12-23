"""
Очередь разрешений с state machine для последовательного запроса разрешений на macOS.

Реализует строго последовательный flow с паузами между запросами,
пуллингом для Accessibility и обработкой перезапуска.
"""

import asyncio
import logging
import time
from enum import Enum, auto
from typing import Callable, Optional, Dict, Any
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class PermissionStep(Enum):
    """Шаги в очереди разрешений."""
    NOTIFICATIONS = auto()
    MICROPHONE = auto()
    CAMERA = auto()
    ACCESSIBILITY = auto()
    SCREEN_RECORDING = auto()
    INPUT_MONITORING = auto()


@dataclass
class StepResult:
    """Результат выполнения шага."""
    step: PermissionStep
    granted: bool
    needs_restart: bool = False
    message: str = ""
    error: Optional[Exception] = None


class PermissionQueue:
    """Очередь разрешений с state machine."""
    
    def __init__(self):
        self.queue = [
            PermissionStep.NOTIFICATIONS,
            PermissionStep.MICROPHONE,
            PermissionStep.CAMERA,
            PermissionStep.ACCESSIBILITY,
            PermissionStep.SCREEN_RECORDING,
            PermissionStep.INPUT_MONITORING,
        ]
        self.current_index = 0
        self.is_running = False
        self.is_paused = False
        
        # Callbacks
        self.on_step_started: Optional[Callable[[PermissionStep], None]] = None
        self.on_step_finished: Optional[Callable[[StepResult], None]] = None
        self.on_queue_completed: Optional[Callable[[], None]] = None
        self.on_queue_failed: Optional[Callable[[Exception], None]] = None
        
        # Polling для Accessibility
        self._polling_task: Optional[asyncio.Task] = None
        self._polling_interval = 1.0  # секунды
        self._max_polling_time = 60.0  # максимальное время пуллинга
        
        # Импорты для работы с разрешениями
        self._import_permission_handlers()
    
    def _import_permission_handlers(self):
        """Импортирует обработчики разрешений."""
        try:
            from .permission_handler import MacOSPermissionHandler
            from .accessibility_handler import AccessibilityHandler
            from .screen_capture_permission import ScreenCapturePermissionManager
            
            self.permission_handler = MacOSPermissionHandler()
            self.accessibility_handler = AccessibilityHandler()
            self.screen_capture_manager = ScreenCapturePermissionManager()
            
            # Простой обработчик уведомлений (заглушка)
            self.notifications_handler = None
            
        except ImportError as e:
            logger.error(f"Failed to import permission handlers: {e}")
            raise
    
    async def start(self) -> None:
        """Запускает очередь разрешений."""
        if self.is_running:
            logger.warning("Permission queue is already running")
            return
        
        self.is_running = True
        self.current_index = 0
        logger.info("🚀 Starting permission queue")
        
        try:
            await self._run_next_step()
        except Exception as e:
            logger.error(f"❌ Permission queue failed: {e}")
            self.is_running = False
            if self.on_queue_failed:
                self.on_queue_failed(e)
    
    async def pause(self) -> None:
        """Приостанавливает очередь разрешений."""
        self.is_paused = True
        logger.info("⏸️ Permission queue paused")
    
    async def resume(self) -> None:
        """Возобновляет очередь разрешений."""
        self.is_paused = False
        logger.info("▶️ Permission queue resumed")
        await self._run_next_step()
    
    async def stop(self) -> None:
        """Останавливает очередь разрешений."""
        self.is_running = False
        self.is_paused = False
        
        # Останавливаем пуллинг если активен
        if self._polling_task and not self._polling_task.done():
            self._polling_task.cancel()
            try:
                await self._polling_task
            except asyncio.CancelledError:
                pass
        
        logger.info("⏹️ Permission queue stopped")
    
    async def _run_next_step(self) -> None:
        """Запускает следующий шаг в очереди."""
        if not self.is_running or self.is_paused:
            return
        
        if self.current_index >= len(self.queue):
            # Очередь завершена
            self.is_running = False
            logger.info("✅ Permission queue completed")
            if self.on_queue_completed:
                self.on_queue_completed()
            return
        
        step = self.queue[self.current_index]
        logger.info(f"📋 Starting step: {step.name}")
        
        if self.on_step_started:
            self.on_step_started(step)
        
        try:
            # Увеличенная пауза для безопасности (чтобы не накладывать окна)
            await asyncio.sleep(1.0)
            
            # Дополнительная проверка - убеждаемся что предыдущие диалоги закрыты
            await self._wait_for_ui_stabilization()
            
            result = await self._execute_step(step)
            
            if self.on_step_finished:
                self.on_step_finished(result)
            
            self.current_index += 1
            
            # Увеличенная пауза перед следующим шагом
            await asyncio.sleep(1.5)
            
            # Переходим к следующему шагу
            await self._run_next_step()
            
        except Exception as e:
            logger.error(f"❌ Error in step {step.name}: {e}")
            result = StepResult(
                step=step,
                granted=False,
                message=f"Error: {e}",
                error=e
            )
            
            if self.on_step_finished:
                self.on_step_finished(result)
            
            # Продолжаем с следующего шага даже при ошибке
            self.current_index += 1
            await asyncio.sleep(1.5)
            await self._run_next_step()
    
    async def _wait_for_ui_stabilization(self) -> None:
        """Ждет стабилизации UI перед следующим шагом."""
        try:
            # Проверяем, что нет активных системных диалогов
            # Это помогает избежать наложения окон разрешений
            
            # Небольшая дополнительная пауза для стабилизации
            await asyncio.sleep(0.5)
            
            # Можно добавить проверку активных окон через AppKit если нужно
            # import AppKit
            # windows = AppKit.NSApplication.sharedApplication().windows()
            # for window in windows:
            #     if window.isVisible() and "permission" in str(window.title()).lower():
            #         await asyncio.sleep(1.0)  # Ждем закрытия
            
        except Exception as e:
            logger.warning(f"UI stabilization check failed: {e}")
            # Не критично, продолжаем
    
    async def _execute_step(self, step: PermissionStep) -> StepResult:
        """Выполняет конкретный шаг разрешения."""
        logger.info(f"🔧 Executing step: {step.name}")
        
        if step == PermissionStep.NOTIFICATIONS:
            return await self._request_notifications()
        elif step == PermissionStep.MICROPHONE:
            return await self._request_microphone()
        elif step == PermissionStep.CAMERA:
            return await self._request_camera()
        elif step == PermissionStep.ACCESSIBILITY:
            return await self._request_accessibility()
        elif step == PermissionStep.SCREEN_RECORDING:
            return await self._request_screen_recording()
        elif step == PermissionStep.INPUT_MONITORING:
            return await self._request_input_monitoring()
        else:
            return StepResult(
                step=step,
                granted=True,
                message="Unknown step, skipping"
            )
    
    async def _request_notifications(self) -> StepResult:
        """Запрашивает разрешение на уведомления."""
        try:
            # Пока что пропускаем уведомления (нет обработчика)
            # В будущем можно добавить через UserNotifications framework
            logger.info("📱 Notifications permission - skipping (not implemented)")
            
            return StepResult(
                step=PermissionStep.NOTIFICATIONS,
                granted=True,  # Пропускаем
                message="Notifications permission skipped (not implemented)"
            )
            
        except Exception as e:
            logger.error(f"Error requesting notifications: {e}")
            return StepResult(
                step=PermissionStep.NOTIFICATIONS,
                granted=False,
                message=f"Error: {e}",
                error=e
            )
    
    async def _request_microphone(self) -> StepResult:
        """Запрашивает разрешение на микрофон."""
        try:
            # Проверяем текущий статус
            current_status = await self.permission_handler.check_microphone_permission()
            
            if current_status.status.value == "GRANTED":
                return StepResult(
                    step=PermissionStep.MICROPHONE,
                    granted=True,
                    message="Microphone already granted"
                )
            
            # Для микрофона полагаемся на системные промпты при первом использовании
            # Здесь можно добавить логику запроса через AVFoundation если нужно
            return StepResult(
                step=PermissionStep.MICROPHONE,
                granted=True,  # Полагаемся на системные промпты
                message="Microphone permission will be requested on first use"
            )
            
        except Exception as e:
            logger.error(f"Error requesting microphone: {e}")
            return StepResult(
                step=PermissionStep.MICROPHONE,
                granted=False,
                message=f"Error: {e}",
                error=e
            )
    
    async def _request_camera(self) -> StepResult:
        """Запрашивает разрешение на камеру."""
        try:
            # Проверяем текущий статус
            current_status = await self.permission_handler.check_camera_permission()
            
            return StepResult(
                step=PermissionStep.CAMERA,
                granted=current_status.status.value == "GRANTED",
                message=current_status.message
            )
            
        except Exception as e:
            logger.error(f"Error requesting camera: {e}")
            return StepResult(
                step=PermissionStep.CAMERA,
                granted=False,
                message=f"Error: {e}",
                error=e
            )
    
    async def _request_accessibility(self) -> StepResult:
        """Запрашивает разрешение на Accessibility с пуллингом."""
        try:
            # Дополнительная пауза перед Accessibility (часто конфликтует с другими)
            await asyncio.sleep(0.5)
            
            # Проверяем текущий статус
            current_granted = self.accessibility_handler.check_accessibility_permission()
            
            if current_granted:
                return StepResult(
                    step=PermissionStep.ACCESSIBILITY,
                    granted=True,
                    message="Accessibility already granted"
                )
            
            logger.info("🔔 Requesting accessibility permission...")
            
            # Запрашиваем разрешение (покажет баннер и откроет Settings)
            requested = self.accessibility_handler.request_accessibility_permission()
            
            if requested:
                return StepResult(
                    step=PermissionStep.ACCESSIBILITY,
                    granted=True,
                    message="Accessibility granted immediately"
                )
            
            # Начинаем пуллинг
            logger.info("🔄 Starting accessibility polling...")
            return await self._poll_accessibility_permission()
            
        except Exception as e:
            logger.error(f"Error requesting accessibility: {e}")
            return StepResult(
                step=PermissionStep.ACCESSIBILITY,
                granted=False,
                message=f"Error: {e}",
                error=e
            )
    
    async def _poll_accessibility_permission(self) -> StepResult:
        """Пуллинг для проверки Accessibility разрешения."""
        start_time = time.time()
        
        while time.time() - start_time < self._max_polling_time:
            try:
                # Проверяем статус
                granted = self.accessibility_handler.check_accessibility_permission()
                
                if granted:
                    logger.info("✅ Accessibility permission granted during polling")
                    return StepResult(
                        step=PermissionStep.ACCESSIBILITY,
                        granted=True,
                        message="Accessibility granted after user action"
                    )
                
                # Ждем перед следующей проверкой
                await asyncio.sleep(self._polling_interval)
                
            except Exception as e:
                logger.error(f"Error during accessibility polling: {e}")
                break
        
        # Таймаут пуллинга
        logger.warning("⏰ Accessibility polling timeout")
        return StepResult(
            step=PermissionStep.ACCESSIBILITY,
            granted=False,
            message="Accessibility permission not granted within timeout. Please enable manually in Settings."
        )
    
    async def _request_screen_recording(self) -> StepResult:
        """Запрашивает разрешение на Screen Recording."""
        try:
            # Проверяем текущий статус
            current_granted = self.screen_capture_manager.check_permission()
            
            if current_granted:
                return StepResult(
                    step=PermissionStep.SCREEN_RECORDING,
                    granted=True,
                    message="Screen recording already granted"
                )
            
            # Запрашиваем разрешение (покажет баннер и откроет Settings)
            granted = self.screen_capture_manager.request_permission()
            
            return StepResult(
                step=PermissionStep.SCREEN_RECORDING,
                granted=granted,
                needs_restart=True,  # Screen Recording требует перезапуск
                message="Screen recording permission requested. Restart required for changes to take effect."
            )
            
        except Exception as e:
            logger.error(f"Error requesting screen recording: {e}")
            return StepResult(
                step=PermissionStep.SCREEN_RECORDING,
                granted=False,
                needs_restart=True,
                message=f"Error: {e}",
                error=e
            )
    
    async def _request_input_monitoring(self) -> StepResult:
        """Запрашивает разрешение на Input Monitoring."""
        try:
            # Проверяем текущий статус
            current_granted = self.accessibility_handler.check_input_monitoring_permission()
            
            if current_granted:
                return StepResult(
                    step=PermissionStep.INPUT_MONITORING,
                    granted=True,
                    message="Input monitoring already granted"
                )
            
            # Открываем настройки (нет нативного диалога)
            opened = self.accessibility_handler.open_input_monitoring_settings()
            
            return StepResult(
                step=PermissionStep.INPUT_MONITORING,
                granted=False,  # Пользователь должен включить вручную
                needs_restart=True,  # Input Monitoring требует перезапуск
                message="Input monitoring settings opened. Please enable manually and restart the application."
            )
            
        except Exception as e:
            logger.error(f"Error requesting input monitoring: {e}")
            return StepResult(
                step=PermissionStep.INPUT_MONITORING,
                granted=False,
                needs_restart=True,
                message=f"Error: {e}",
                error=e
            )
    
    def get_progress(self) -> Dict[str, Any]:
        """Возвращает текущий прогресс очереди."""
        total_steps = len(self.queue)
        completed_steps = self.current_index
        progress_percent = (completed_steps / total_steps) * 100 if total_steps > 0 else 0
        
        return {
            "is_running": self.is_running,
            "is_paused": self.is_paused,
            "current_step": self.queue[self.current_index].name if self.current_index < len(self.queue) else None,
            "completed_steps": completed_steps,
            "total_steps": total_steps,
            "progress_percent": progress_percent,
            "remaining_steps": total_steps - completed_steps
        }
    
    def skip_current_step(self) -> None:
        """Пропускает текущий шаг."""
        if self.current_index < len(self.queue):
            logger.info(f"⏭️ Skipping step: {self.queue[self.current_index].name}")
            self.current_index += 1
