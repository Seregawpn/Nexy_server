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


def get_bundle_id() -> str:
    """Определить bundle_id текущего процесса."""
    try:
        from Foundation import NSBundle  # type: ignore
        bundle_id = NSBundle.mainBundle().bundleIdentifier()
        if bundle_id:
            return bundle_id
    except Exception:
        pass
    return "com.nexy.assistant"


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
            import AVFoundation  # type: ignore

            # Получаем статус через AVCaptureDevice
            auth_status = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(  # type: ignore
                AVFoundation.AVMediaTypeAudio  # type: ignore
            )

            logger.debug(f"🎙️ Microphone: AVFoundation auth_status raw = {auth_status}")
            # FORCE PRINT for debugging during manual tests
            if auth_status != 3:
                print(f"🎙️ [STATUS_CHECKER] Mic AuthStatus: {auth_status} (waiting for 3/Authorized)")

            # Маппинг статусов AVFoundation на наши
            # AVAuthorizationStatusNotDetermined = 0
            # AVAuthorizationStatusRestricted = 1
            # AVAuthorizationStatusDenied = 2
            # AVAuthorizationStatusAuthorized = 3

            if auth_status == 3:  # Authorized
                logger.debug("🎙️ Microphone: GRANTED (AVFoundation)")
                return PermissionStatus.GRANTED
            elif auth_status == 2:  # Denied
                logger.debug("🎙️ Microphone: DENIED (AVFoundation)")
                return PermissionStatus.DENIED
            elif auth_status == 1:  # Restricted
                logger.debug("🎙️ Microphone: DENIED (Restricted)")
                return PermissionStatus.DENIED
            else:  # auth_status == 0 (NotDetermined)
                # AVFoundation can return stale cached value (0/NotDetermined) even after
                # permission is granted in packaged apps. This is a known macOS issue.
                # We use sounddevice fallback to verify ACTUAL microphone access.
                logger.debug("🎙️ Microphone: AVFoundation=NOT_DETERMINED, trying sounddevice fallback")
                fallback_status = _check_microphone_via_sounddevice()
                if fallback_status == PermissionStatus.GRANTED:
                    logger.info("🎙️ Microphone: GRANTED (via sounddevice fallback, AVFoundation cache stale)")
                    return PermissionStatus.GRANTED
                # If sounddevice also fails, return NOT_DETERMINED to continue prompting
                logger.debug("🎙️ Microphone: sounddevice fallback returned %s", fallback_status.value)
                return PermissionStatus.NOT_DETERMINED

        except ImportError:
            logger.warning("⚠️ AVFoundation недоступен, используем sounddevice fallback")
            return _check_microphone_via_sounddevice()

    except Exception as e:
        logger.error(f"❌ Ошибка проверки микрофона: {e}")
        return PermissionStatus.ERROR


def check_microphone_status_no_prompt() -> PermissionStatus:
    """
    Неинвазивная проверка статуса микрофона без sounddevice fallback.
    Используется для старта first_run и readiness, чтобы не вызвать prompt раньше времени.
    """
    if _force_granted():
        logger.debug("🎙️ Microphone: forced GRANTED via NEXY_DEV_FORCE_PERMISSIONS")
        return PermissionStatus.GRANTED

    try:
        try:
            import AVFoundation  # type: ignore
            capture_device = getattr(AVFoundation, "AVCaptureDevice", None)
            media_type = getattr(AVFoundation, "AVMediaTypeAudio", None)
            if not capture_device or media_type is None:
                return PermissionStatus.NOT_DETERMINED

            auth_status = capture_device.authorizationStatusForMediaType_(media_type)
            if auth_status == 3:
                return PermissionStatus.GRANTED
            if auth_status in (1, 2):
                return PermissionStatus.DENIED
            return PermissionStatus.NOT_DETERMINED
        except ImportError:
            logger.warning("⚠️ AVFoundation недоступен (no_prompt), returning NOT_DETERMINED")
            return PermissionStatus.NOT_DETERMINED
    except Exception as e:
        logger.debug(f"🎙️ Microphone: no_prompt check error: {e}")
        return PermissionStatus.NOT_DETERMINED


def _check_microphone_via_sounddevice() -> PermissionStatus:
    """
    Проверяет доступ к микрофону путём реальной попытки записи.
    Если запись удалась — разрешение есть.
    """
    try:
        import sounddevice as sd
        import numpy as np
        
        # Пробуем записать очень короткий фрагмент (50ms)
        duration = 0.05  # секунд
        sample_rate = 16000
        
        # Это вызовет системный диалог если разрешения нет,
        # или вернёт данные если разрешение есть
        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype=np.float32,
            blocking=True
        )
        
        # Если дошли сюда без ошибки — разрешение есть
        logger.debug("🎙️ Microphone: GRANTED (sounddevice test)")
        return PermissionStatus.GRANTED
        
    except ImportError:
        logger.debug("🎙️ Microphone: sounddevice not available")
        return PermissionStatus.NOT_DETERMINED
    except Exception as e:
        # Check if it's a PortAudioError by checking the exception type name
        # We can't use sd.PortAudioError directly because sd might not be imported
        error_type_name = type(e).__name__
        if error_type_name == "PortAudioError":
            error_str = str(e).lower()
            # Explicit permission denial keywords
            if "permission" in error_str or "denied" in error_str or "not allowed" in error_str:
                logger.debug(f"🎙️ Microphone: DENIED (sounddevice error: {e})")
                return PermissionStatus.DENIED
            # Device busy/host errors usually mean permission IS granted but device is in use
            # These errors indicate the system CAN access the device (permission granted)
            if any(kw in error_str for kw in ["device", "busy", "host", "invalid", "timeout", "unavailable"]):
                logger.info(f"🎙️ Microphone: GRANTED (device accessible but busy/error: {e})")
                return PermissionStatus.GRANTED
            # Unknown PortAudio errors - assume NOT_DETERMINED
            logger.debug(f"🎙️ Microphone: PortAudio unknown error, assuming NOT_DETERMINED: {e}")
            return PermissionStatus.NOT_DETERMINED
        
        # For other exceptions, check if they suggest device access
        error_str = str(e).lower()
        if any(kw in error_str for kw in ["device", "busy", "stream", "audio"]):
            logger.info(f"🎙️ Microphone: GRANTED (device error suggests access: {e})")
            return PermissionStatus.GRANTED
        logger.debug(f"🎙️ Microphone: sounddevice fallback error: {e}")
        return PermissionStatus.NOT_DETERMINED


def check_accessibility_status() -> PermissionStatus:
    """
    Проверить статус разрешения Accessibility.
    
    ЕДИНСТВЕННЫЙ SOURCE OF TRUTH для проверки Accessibility.
    
    КРИТИЧНО (macOS Sequoia 26+): 
    AXIsProcessTrustedWithOptions КРАШИТ ПРОЦЕСС когда статус NOT_DETERMINED!
    Система внутренне вызывает TCCAccessRequest который требует приватный entitlement
    com.apple.private.tcc.manager.check-by-audit-token.
    
    БЕЗОПАСНЫЙ ПОДХОД: Используем AXIsProcessTrusted() через ctypes.
    Эта функция просто возвращает Bool без внутреннего TCC запроса.
    
    Rate-limit: не чаще 1 раза в 2 секунды (кеширование результата).

    Returns:
        PermissionStatus: GRANTED, DENIED или NOT_DETERMINED (при ошибке)
    """
    if _force_granted():
        logger.debug("♿ Accessibility: forced GRANTED via NEXY_DEV_FORCE_PERMISSIONS")
        return PermissionStatus.GRANTED

    import time
    
    # Кеш отключён — для polling нужны реальные проверки каждую секунду
    # Ранее был кеш 2 секунды, но он мешал polling'у
    
    try:
        from ctypes import util as ctypes_util
        
        # БЕЗОПАСНЫЙ СПОСОБ: Используем AXIsProcessTrusted() (без Options)
        # Этот API просто возвращает Bool и НЕ вызывает TCCAccessRequest.
        # 
        # ВАЖНО: НЕ используем AXIsProcessTrustedWithOptions!
        # На macOS Sequoia этот API крашит процесс при NOT_DETERMINED статусе.
        
        app_services_path = ctypes_util.find_library("ApplicationServices")
        if not app_services_path:
            logger.warning("⚠️ ApplicationServices framework не найден")
            return PermissionStatus.NOT_DETERMINED

        app_services = ctypes.CDLL(app_services_path)
        
        try:
            app_services.AXIsProcessTrusted.argtypes = []
            app_services.AXIsProcessTrusted.restype = ctypes.c_bool
            is_trusted = app_services.AXIsProcessTrusted()
            
            if is_trusted:
                logger.debug("♿ Accessibility: GRANTED (AXIsProcessTrusted)")
                return PermissionStatus.GRANTED
                
            # НЕ используем функциональный fallback для проверки статуса
            # Функциональные проверки могут давать ложные GRANTED если разрешение
            # не предоставлено через TCC, но доступно через другие механизмы.
            # 
            # Если AXIsProcessTrusted возвращает False, это означает:
            # - NOT_DETERMINED: разрешение ещё не запрошено
            # - DENIED: разрешение отклонено пользователем
            # 
            # В обоих случаях возвращаем NOT_DETERMINED для запуска flow запроса разрешения.
            # После DENIED prompt может не появляться, но это обрабатывается в activator.
            logger.debug("♿ Accessibility: AXIsProcessTrusted=False, returning NOT_DETERMINED")
            return PermissionStatus.NOT_DETERMINED
            
        except Exception as e:
            logger.warning(f"⚠️ AXIsProcessTrusted failed: {e}")
            # При ошибке возвращаем NOT_DETERMINED для запуска flow запроса разрешения
            return PermissionStatus.NOT_DETERMINED
            
    except Exception as e:
        logger.warning(f"♿ Accessibility check failed: {e}")
        return PermissionStatus.NOT_DETERMINED


def _check_accessibility_via_script() -> PermissionStatus:
    """
    Проверить Accessibility функциональным тестом (AppleScript).
    Если скрипт выполняется успешно, значит разрешение ЕСТЬ, 
    даже если AXIsProcessTrusted говорит False.
    """
    import subprocess
    try:
        # Простой скрипт, требующий взаимодействия с System Events
        # (получение имени переднего процесса)
        cmd = [
            "osascript", 
            "-e", 
            'tell application "System Events" to get name of first application process whose frontmost is true'
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=1.0  # Быстрый таймаут
        )
        
        if result.returncode == 0:
            logger.info("♿ Accessibility: GRANTED (Functional Script Check)")
            # Если скрипт сработал - разрешение ТОЧНО есть
            return PermissionStatus.GRANTED
        else:
            # Ошибка выполнения - разрешения нет или другая ошибка
            # logger.debug(f"♿ Functional check failed: {result.stderr.strip()[:100]}")
            return PermissionStatus.NOT_DETERMINED
            
    except Exception as e:
        logger.debug(f"♿ Functional check error: {e}")
        return PermissionStatus.NOT_DETERMINED



def check_input_monitoring_status() -> PermissionStatus:
    """
    Проверить статус разрешения Input Monitoring.
    
    Использует IOHIDCheckAccess(ListenEvent) который возвращает детерминированные статусы:
    - 0 = kIOHIDAccessTypeGranted
    - 1 = kIOHIDAccessTypeDenied  
    - 2 = kIOHIDAccessTypeUnknown (NOT_DETERMINED)

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
            logger.warning("⚠️ IOHIDCheckAccess недоступен")
            return PermissionStatus.NOT_DETERMINED

        check_access.argtypes = [ctypes.c_uint32]
        # ВАЖНО: restype должен быть c_uint32 (IOHIDAccessType), НЕ c_bool!
        # c_bool неправильно интерпретирует 1 (Denied) как True
        check_access.restype = ctypes.c_uint32

        # IOHIDAccessType константы
        kIOHIDAccessTypeGranted = 0
        kIOHIDAccessTypeDenied = 1
        kIOHIDAccessTypeUnknown = 2
        kIOHIDRequestTypeListenEvent = 1  # Input Monitoring
        
        access_type = check_access(kIOHIDRequestTypeListenEvent)
        logger.debug(f"⌨️ Input Monitoring: IOHIDCheckAccess(ListenEvent) = {access_type}")
        # FORCE PRINT for debugging
        print(f"⌨️ [STATUS_CHECKER] Input Monitoring: IOHIDCheckAccess = {access_type} (0=Granted, 1=Denied, 2=Unknown)")

        if access_type == kIOHIDAccessTypeGranted:
            logger.debug("⌨️ Input Monitoring: GRANTED")
            print("⌨️ [STATUS_CHECKER] Input Monitoring: GRANTED")
            return PermissionStatus.GRANTED
        elif access_type == kIOHIDAccessTypeDenied:
            logger.debug("⌨️ Input Monitoring: DENIED")
            print("⌨️ [STATUS_CHECKER] Input Monitoring: DENIED")
            return PermissionStatus.DENIED
        else:  # kIOHIDAccessTypeUnknown
            logger.debug("⌨️ Input Monitoring: NOT_DETERMINED")
            print("⌨️ [STATUS_CHECKER] Input Monitoring: NOT_DETERMINED")
            return PermissionStatus.NOT_DETERMINED

    except Exception as e:
        logger.error(f"❌ Ошибка проверки Input Monitoring: {e}")
        return PermissionStatus.ERROR


# Session guard: запоминаем что диалог уже показывался
_screen_capture_prompt_shown_this_session = False


def check_screen_capture_status() -> PermissionStatus:
    """
    Проверить статус разрешения Screen Capture.
    
    Использует публичный API CGPreflightScreenCaptureAccess.
    Примечание: API возвращает только Bool, не различает NOT_DETERMINED от DENIED.
    
    Session Guard: Если в этой сессии уже показывался диалог и статус False,
    возвращаем DENIED вместо NOT_DETERMINED чтобы не показывать повторно.

    Returns:
        PermissionStatus: текущий статус разрешения
    """
    global _screen_capture_prompt_shown_this_session
    
    if _force_granted():
        logger.debug("📺 Screen Capture: forced GRANTED via NEXY_DEV_FORCE_PERMISSIONS")
        return PermissionStatus.GRANTED

    try:
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
            # Session guard: если уже показывали диалог в этой сессии → DENIED
            if _screen_capture_prompt_shown_this_session:
                logger.debug("📺 Screen Capture: DENIED (session guard: prompt already shown)")
                return PermissionStatus.DENIED
            
            # CGPreflightScreenCaptureAccess возвращает False если:
            # 1. Разрешение не дано (NOT_DETERMINED или DENIED)
            # Мы не можем различить эти два случая через публичный API
            # Возвращаем NOT_DETERMINED для запуска flow запроса разрешения
            logger.debug("📺 Screen Capture: NOT_DETERMINED (cannot distinguish from DENIED via public API)")
            return PermissionStatus.NOT_DETERMINED

    except Exception as e:
        logger.error(f"❌ Ошибка проверки Screen Capture: {e}")
        return PermissionStatus.ERROR


def mark_screen_capture_prompt_shown():
    """Отметить что диалог Screen Capture был показан в этой сессии."""
    global _screen_capture_prompt_shown_this_session
    _screen_capture_prompt_shown_this_session = True
    logger.debug("📺 Screen Capture: session guard activated (prompt shown)")


def reset_screen_capture_session_guard():
    """Сбросить session guard (для тестов)."""
    global _screen_capture_prompt_shown_this_session
    _screen_capture_prompt_shown_this_session = False


def _force_granted() -> bool:
    """
    Определяет, нужно ли принудительно считать разрешения выданными.

    Логика:
    1. Если явно задана переменная окружения NEXY_DEV_FORCE_PERMISSIONS:
       - 1/true/yes  → форсируем GRANTED
       - 0/false/no  → не форсируем
    2. По умолчанию считаем, что разрешения НЕ форсятся.
    """
    value = os.environ.get("NEXY_DEV_FORCE_PERMISSIONS")
    if value is not None:
        return value.strip().lower() in {"1", "true", "yes"}

    return False


def check_contacts_status() -> PermissionStatus:
    """
    Проверить статус разрешения Contacts.
    
    Использует CNContactStore.authorizationStatus для проверки.
    
    Returns:
        PermissionStatus: текущий статус разрешения
    """
    if _force_granted():
        logger.debug("📇 Contacts: forced GRANTED via NEXY_DEV_FORCE_PERMISSIONS")
        return PermissionStatus.GRANTED

    try:
        from Contacts import CNContactStore, CNEntityTypeContacts  # type: ignore
        
        # CNAuthorizationStatus enum:
        # 0 = NotDetermined
        # 1 = Restricted
        # 2 = Denied
        # 3 = Authorized
        auth_status = CNContactStore.authorizationStatusForEntityType_(CNEntityTypeContacts)
        
        logger.debug(f"📇 Contacts: CNContactStore auth_status = {auth_status}")
        print(f"📇 [STATUS_CHECKER] Contacts: auth_status = {auth_status} (0=NotDet, 1=Restricted, 2=Denied, 3=Authorized)")

        if auth_status == 3:  # Authorized
            logger.debug("📇 Contacts: GRANTED")
            return PermissionStatus.GRANTED
        elif auth_status == 2:  # Denied
            logger.debug("📇 Contacts: DENIED")
            return PermissionStatus.DENIED
        elif auth_status == 1:  # Restricted
            logger.debug("📇 Contacts: DENIED (Restricted)")
            return PermissionStatus.DENIED
        else:  # 0 = NotDetermined
            logger.debug("📇 Contacts: NOT_DETERMINED")
            return PermissionStatus.NOT_DETERMINED

    except ImportError:
        logger.warning("⚠️ Contacts framework not available")
        return PermissionStatus.NOT_DETERMINED
    except Exception as e:
        logger.error(f"❌ Error checking Contacts status: {e}")
        return PermissionStatus.ERROR


def check_full_disk_access_status() -> PermissionStatus:
    """
    Проверить статус разрешения Full Disk Access.
    
    Full Disk Access нельзя проверить через API напрямую.
    Проверяем пытаясь прочитать защищённый файл ~/Library/Messages/chat.db
    
    Returns:
        PermissionStatus: текущий статус разрешения
    """
    if _force_granted():
        logger.debug("💾 Full Disk Access: forced GRANTED via NEXY_DEV_FORCE_PERMISSIONS")
        return PermissionStatus.GRANTED

    try:
        import os
        from pathlib import Path
        
        # Путь к защищённому файлу (требует Full Disk Access)
        protected_file = Path.home() / "Library" / "Messages" / "chat.db"
        
        if not protected_file.exists():
            # Файл не существует (например, Messages никогда не использовался)
            logger.debug("💾 Full Disk Access: chat.db не существует, предполагаем NOT_DETERMINED")
            return PermissionStatus.NOT_DETERMINED
        
        # Пытаемся прочитать файл
        try:
            with open(protected_file, 'rb') as f:
                f.read(1)  # Читаем 1 байт
            
            logger.debug("💾 Full Disk Access: GRANTED (удалось прочитать chat.db)")
            print("💾 [STATUS_CHECKER] Full Disk Access: GRANTED")
            return PermissionStatus.GRANTED
            
        except PermissionError:
            logger.debug("💾 Full Disk Access: DENIED (PermissionError)")
            print("💾 [STATUS_CHECKER] Full Disk Access: DENIED")
            return PermissionStatus.DENIED
        except OSError as e:
            if e.errno == 1:  # Operation not permitted
                logger.debug("💾 Full Disk Access: DENIED (Operation not permitted)")
                print("💾 [STATUS_CHECKER] Full Disk Access: DENIED")
                return PermissionStatus.DENIED
            raise

    except Exception as e:
        logger.error(f"❌ Error checking Full Disk Access status: {e}")
        return PermissionStatus.ERROR


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
        "contacts": check_contacts_status(),
        "full_disk_access": check_full_disk_access_status(),
    }
