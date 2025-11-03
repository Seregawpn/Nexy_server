"""
Status Checker для проверки статусов разрешений macOS.

Проверяет текущий статус разрешений БЕЗ показа диалогов.
Используется для определения нужно ли вызывать активацию.
"""

import logging
import os
import sys
import ctypes
from ctypes import util
from enum import Enum

logger = logging.getLogger(__name__)


class PermissionStatus(Enum):
    """Статус разрешения"""
    NOT_DETERMINED = "not_determined"  # Пользователь ещё не видел диалог
    GRANTED = "granted"                # Разрешение дано
    DENIED = "denied"                  # Разрешение отклонено
    ERROR = "error"                    # Ошибка проверки


def check_microphone_status() -> PermissionStatus:
    """
    Проверить статус разрешения микрофона.

    Returns:
        PermissionStatus: текущий статус разрешения
    """
    if _force_granted():
        logger.debug("🎙️ Microphone: forced GRANTED via NEXY_DEV_FORCE_PERMISSIONS")
        return PermissionStatus.GRANTED

    try:
        # Пытаемся использовать AVFoundation через PyObjC
        try:
            import AVFoundation

            # Получаем статус через AVCaptureDevice
            auth_status = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
                AVFoundation.AVMediaTypeAudio
            )

            # Маппинг статусов AVFoundation на наши
            # AVAuthorizationStatusNotDetermined = 0
            # AVAuthorizationStatusRestricted = 1
            # AVAuthorizationStatusDenied = 2
            # AVAuthorizationStatusAuthorized = 3

            if auth_status == 0:  # NotDetermined
                logger.debug("🎙️ Microphone: NOT_DETERMINED")
                return PermissionStatus.NOT_DETERMINED
            elif auth_status == 3:  # Authorized
                logger.debug("🎙️ Microphone: GRANTED")
                return PermissionStatus.GRANTED
            else:  # Denied or Restricted
                logger.debug("🎙️ Microphone: DENIED")
                return PermissionStatus.DENIED

        except ImportError:
            logger.warning("⚠️ AVFoundation недоступен, используем fallback")
            # Fallback: предполагаем NOT_DETERMINED чтобы попытаться активировать
            return PermissionStatus.NOT_DETERMINED

    except Exception as e:
        logger.error(f"❌ Ошибка проверки микрофона: {e}")
        return PermissionStatus.ERROR


def check_accessibility_status() -> PermissionStatus:
    """
    Проверить статус разрешения Accessibility.

    Returns:
        PermissionStatus: текущий статус разрешения
    """
    if _force_granted():
        logger.debug("♿ Accessibility: forced GRANTED via NEXY_DEV_FORCE_PERMISSIONS")
        return PermissionStatus.GRANTED

    try:
        # Используем существующий AccessibilityHandler
        from modules.permissions.macos.accessibility_handler import AccessibilityHandler

        handler = AccessibilityHandler()
        is_granted = handler.check_accessibility_permission()

        if is_granted:
            logger.debug("♿ Accessibility: GRANTED")
            return PermissionStatus.GRANTED
        else:
            # AXIsProcessTrustedWithOptions возвращает False если:
            # 1. Разрешение не дано (NOT_DETERMINED или DENIED)
            # Мы не можем различить эти два случая через публичный API
            # Предполагаем NOT_DETERMINED чтобы попытаться показать диалог
            logger.debug("♿ Accessibility: NOT_DETERMINED or DENIED")
            return PermissionStatus.NOT_DETERMINED

    except Exception as e:
        logger.error(f"❌ Ошибка проверки Accessibility: {e}")
        return PermissionStatus.ERROR


def check_input_monitoring_status() -> PermissionStatus:
    """
    Проверить статус разрешения Input Monitoring.

    Returns:
        PermissionStatus: текущий статус разрешения
    """
    if _force_granted():
        logger.debug("⌨️ Input Monitoring: forced GRANTED via NEXY_DEV_FORCE_PERMISSIONS")
        return PermissionStatus.GRANTED

    try:
        iokit_path = util.find_library("IOKit")
        if not iokit_path:
            logger.warning("⚠️ IOKit недоступен – предполагаем NOT_DETERMINED")
            return PermissionStatus.NOT_DETERMINED

        iokit = ctypes.CDLL(iokit_path)

        try:
            check_access = iokit.IOHIDCheckAccess
        except AttributeError:
            logger.warning("⚠️ IOHIDCheckAccess недоступен – используем tccutil fallback")
            raise AttributeError("IOHIDCheckAccess unavailable")

        check_access.argtypes = [ctypes.c_uint32]
        check_access.restype = ctypes.c_bool

        kIOHIDRequestTypeListenEvent = ctypes.c_uint32(1)
        granted = bool(check_access(kIOHIDRequestTypeListenEvent.value))

        if granted:
            logger.debug("⌨️ Input Monitoring: GRANTED (IOHIDCheckAccess)")
            return PermissionStatus.GRANTED

        # IOHIDCheckAccess иногда возвращает False даже при выданном разрешении
        # (например, сразу после обновления приложения). Дополнительно проверяем
        # статус через tccutil, чтобы не триггерить повторный запрос зря.
        logger.debug("⌨️ Input Monitoring: IOHIDCheckAccess вернул False, выполняем tccutil check…")
        try:
            import subprocess

            result = subprocess.run(
                ['tccutil', 'check', 'ListenEvent', 'com.nexy.assistant'],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                logger.debug("⌨️ Input Monitoring: GRANTED (tccutil fallback)")
                return PermissionStatus.GRANTED
        except Exception as tcc_err:
            logger.debug(f"⌨️ Input Monitoring: tccutil fallback недоступен ({tcc_err})")

        logger.debug("⌨️ Input Monitoring: NOT_DETERMINED or DENIED")
        return PermissionStatus.NOT_DETERMINED

    except Exception:
        # Fallback: используем tccutil для проверки
        try:
            import subprocess

            result = subprocess.run(
                ['tccutil', 'check', 'ListenEvent', 'com.nexy.assistant'],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                logger.debug("⌨️ Input Monitoring (fallback): GRANTED")
                return PermissionStatus.GRANTED
            else:
                logger.debug("⌨️ Input Monitoring (fallback): NOT_DETERMINED or DENIED")
                return PermissionStatus.NOT_DETERMINED
        except Exception as e:
            logger.error(f"❌ Ошибка проверки Input Monitoring: {e}")
            return PermissionStatus.ERROR


def check_screen_capture_status() -> PermissionStatus:
    """
    Проверить статус разрешения Screen Capture.

    Returns:
        PermissionStatus: текущий статус разрешения
    """
    if _force_granted():
        logger.debug("📺 Screen Capture: forced GRANTED via NEXY_DEV_FORCE_PERMISSIONS")
        return PermissionStatus.GRANTED

    try:
        # Используем существующий ScreenCapturePermissionManager
        from modules.permissions.macos.screen_capture_permission import ScreenCapturePermissionManager

        manager = ScreenCapturePermissionManager()

        if not manager.is_available:
            logger.warning("⚠️ Screen Capture API недоступен")
            return PermissionStatus.ERROR

        has_permission = manager.check_permission()

        if has_permission:
            logger.debug("📺 Screen Capture: GRANTED")
            return PermissionStatus.GRANTED
        else:
            # CGPreflightScreenCaptureAccess возвращает False если:
            # 1. Разрешение не дано (NOT_DETERMINED или DENIED)
            # Предполагаем NOT_DETERMINED чтобы попытаться показать диалог
            logger.debug("📺 Screen Capture: NOT_DETERMINED or DENIED")
            return PermissionStatus.NOT_DETERMINED

    except Exception as e:
        logger.error(f"❌ Ошибка проверки Screen Capture: {e}")
        return PermissionStatus.ERROR


def _force_granted() -> bool:
    """
    Определяет, нужно ли принудительно считать разрешения выданными.

    Логика:
    1. Если явно задана переменная окружения NEXY_DEV_FORCE_PERMISSIONS:
       - 1/true/yes  → форсируем GRANTED
       - 0/false/no  → не форсируем
    2. По умолчанию форсируем только при dev-запуске из терминала
       (не упакованный билд, stdout или stdin привязаны к TTY).
    """
    value = os.environ.get("NEXY_DEV_FORCE_PERMISSIONS")
    if value is not None:
        return value.strip().lower() in {"1", "true", "yes"}

    if not getattr(sys, "frozen", False):
        try:
            if sys.stdout.isatty() or sys.stdin.isatty():
                return True
        except Exception:
            pass

    return False


def check_all_permissions() -> dict:
    """
    Проверить статусы всех разрешений.

    Returns:
        dict: словарь с статусами {permission_name: PermissionStatus}
    """
    return {
        "microphone": check_microphone_status(),
        "accessibility": check_accessibility_status(),
        "input_monitoring": check_input_monitoring_status(),
        "screen_capture": check_screen_capture_status(),
    }
