"""
Activator для активации разрешений macOS.

Вызывает системные API чтобы триггернуть показ диалогов разрешений.
Не ждёт ответа пользователя - просто вызывает API и возвращается.
"""

import asyncio
import ctypes
import os
import subprocess
import sys
from ctypes import util


from integration.utils.logging_setup import get_logger

logger = get_logger(__name__)


def _get_system_preferences_url(permission_key: str) -> str:
    try:
        from config.unified_config_loader import UnifiedConfigLoader

        permissions_config = UnifiedConfigLoader.get_instance().get_permission_config()
        return permissions_config.get("system_preferences", {}).get(permission_key, "")
    except Exception as e:
        logger.warning(f"⚠️ Не удалось получить System Settings URL для {permission_key}: {e}")
        return ""


def _open_permission_settings(permission_key: str, label: str) -> None:
    url = _get_system_preferences_url(permission_key)
    if not url:
        logger.warning(f"⚠️ System Settings URL не найден для {label}")
        return

    logger.info(f"🔧 {label}: открываем System Settings...")
    print(f"🔧 [ACTIVATOR] {label}: открываем System Settings...")
    try:
        subprocess.run(["open", url], check=True)
        logger.info(f"✅ System Settings открыт для {label}")
    except Exception as e:
        logger.warning(f"⚠️ Не удалось открыть System Settings для {label}: {e}")


async def activate_microphone() -> bool:
    """
    Активировать запрос разрешения микрофона.

    Открывает микрофон для триггера системного диалога.

    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        # ШАГ 1: Проверяем - если разрешение уже есть, не делаем ничего
        from .status_checker import check_microphone_status, PermissionStatus
        
        current_status = check_microphone_status()
        if current_status == PermissionStatus.GRANTED:
            logger.info("✅ Microphone: Разрешение уже предоставлено, пропускаем активацию")
            print("✅ [ACTIVATOR] Microphone: Разрешение уже есть")
            return True
        
        # ШАГ 2: Разрешение не предоставлено - активируем
        logger.info("🎙️ Активация микрофона...")
        print(f"🎙️ [ACTIVATOR] Начало активации микрофона")  # DEBUG: Для console.app

        # Используем sounddevice для открытия микрофона
        import sounddevice as sd

        # Открываем input stream для триггера системного диалога
        # Это вызовет системный диалог если разрешение NOT_DETERMINED
        try:
            # Получаем дефолтное устройство
            print(f"🎙️ [ACTIVATOR] Запрос default input device...")  # DEBUG
            default_device = sd.query_devices(kind='input')
            device_name = default_device.get('name', 'unknown') if isinstance(default_device, dict) else getattr(default_device, 'name', 'unknown')
            logger.debug(f"   Default input device: {device_name}")
            print(f"🎙️ [ACTIVATOR] Default device: {device_name}")  # DEBUG

            # Открываем stream и держим открытым на протяжении всей паузы
            # Это гарантирует что диалог успеет появиться до следующего запроса
            print(f"🎙️ [ACTIVATOR] Открываем InputStream...")  # DEBUG
            with sd.InputStream(
                samplerate=16000,
                channels=1,
                dtype='int16',
                blocksize=8000,
            ):
                # Yield to event loop to allow system dialog to appear
                await asyncio.sleep(0)
                print("🎙️ [ACTIVATOR] Поток открыт")  # DEBUG

            logger.info("✅ Микрофон активирован успешно")
            print(f"✅ [ACTIVATOR] Микрофон активирован успешно")  # DEBUG

        except Exception as e:
            logger.warning(f"⚠️ Не удалось открыть микрофон: {e}")
            print(f"⚠️ [ACTIVATOR] Exception при открытии микрофона: {e}")  # DEBUG
            # Это OK - возможно разрешения нет, диалог показан
        
        await asyncio.sleep(0.5)
        new_status = check_microphone_status()
        if new_status != PermissionStatus.GRANTED:
            _open_permission_settings("microphone", "Microphone")
        return True

    except ImportError:
        logger.warning("⚠️ sounddevice недоступен")
        print(f"⚠️ [ACTIVATOR] sounddevice недоступен")  # DEBUG
        _open_permission_settings("microphone", "Microphone")
        return True
    except Exception as e:
        logger.error(f"❌ Ошибка активации микрофона: {e}")
        print(f"❌ [ACTIVATOR] Критическая ошибка: {e}")  # DEBUG
        _open_permission_settings("microphone", "Microphone")
        return False


async def activate_accessibility() -> bool:
    """
    Активировать запрос разрешения Accessibility.

    КРИТИЧНО (macOS Sequoia 15+):
    AXIsProcessTrustedWithOptions КРАШИТ ПРОЦЕСС независимо от опций!
    
    БЕЗОПАСНЫЙ ПОДХОД: 
    1. Сначала проверяем статус
    2. Если не предоставлено - пробуем AppleScript с System Events (может вызвать диалог)
    3. Если AppleScript не сработал - пользователь должен включить вручную в Settings

    Returns:
        True если разрешение уже предоставлено или попытка активации выполнена
        False если произошла ошибка
    """
    try:
        # ШАГ 1: Проверяем - если разрешение уже есть, не делаем ничего
        from .status_checker import check_accessibility_status, PermissionStatus

        current_status = check_accessibility_status()
        if current_status == PermissionStatus.GRANTED:
            logger.info("✅ Accessibility: Разрешение уже предоставлено, пропускаем активацию")
            print("✅ [ACTIVATOR] Accessibility: Разрешение уже есть")
            return True

        logger.info("♿ Accessibility: разрешение не предоставлено, пробуем активировать...")
        print("♿ [ACTIVATOR] Accessibility: пробуем вызвать диалог...")

        # ШАГ 2: Запускаем безопасный subprocess для prompt
        helper_exit_code = None
        helper_stdout = None
        helper_stderr = None
        try:
            script_dir = os.path.dirname(__file__)
            script_path = os.path.join(script_dir, "trigger_accessibility_prompt.py")
            logger.info("♿ Accessibility: запуск prompt helper subprocess...")
            print("♿ [ACTIVATOR] Accessibility: запуск prompt helper subprocess...")
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                timeout=5
            )
            helper_exit_code = result.returncode
            helper_stdout = result.stdout.strip() if result.stdout else None
            helper_stderr = result.stderr.strip() if result.stderr else None
            
            # Интерпретация exit code согласно документации trigger_accessibility_prompt.py
            exit_code_meaning = {
                0: "Разрешение уже есть (trusted=True) или диалог показан успешно",
                1: "Разрешения нет (trusted=False) — диалог должен был появиться",
                2: "Ошибка выполнения"
            }.get(helper_exit_code, f"Неизвестный exit code: {helper_exit_code}")
            
            logger.info(
                "♿ Accessibility: prompt helper завершён — exit_code=%s (%s) stdout=%s stderr=%s",
                helper_exit_code,
                exit_code_meaning,
                helper_stdout[:100] if helper_stdout else "(пусто)",
                helper_stderr[:100] if helper_stderr else "(пусто)",
            )
            print(f"♿ [ACTIVATOR] Accessibility prompt helper: exit={helper_exit_code} ({exit_code_meaning})")
            if helper_stderr:
                print(f"   stderr: {helper_stderr[:200]}")
        except subprocess.TimeoutExpired:
            logger.warning("⚠️ Accessibility prompt helper timeout (5s)")
            print("⚠️ [ACTIVATOR] Accessibility prompt helper timeout (5s)")
            helper_exit_code = -1  # Специальный код для timeout
        except Exception as e:
            logger.warning(f"⚠️ Accessibility prompt helper error: {e}")
            print(f"⚠️ [ACTIVATOR] Accessibility prompt helper error: {e}")
            helper_exit_code = -2  # Специальный код для exception
            import traceback
            logger.debug(f"Traceback: {traceback.format_exc()}")

        # Если helper упал/ошибся — сразу показываем fallback
        if helper_exit_code in (-1, -2, 2):
            _open_permission_settings("accessibility", "Accessibility")

        # ШАГ 3: Проверяем ещё раз после попытки
        await asyncio.sleep(0.5)

        new_status = check_accessibility_status()
        status_before = current_status.value
        status_after = new_status.value
        
        logger.info(
            "♿ Accessibility: статус до/после prompt helper — %s → %s (helper exit=%s)",
            status_before,
            status_after,
            helper_exit_code if helper_exit_code is not None else "N/A"
        )
        print(f"♿ [ACTIVATOR] Accessibility статус: {status_before} → {status_after} (helper exit={helper_exit_code if helper_exit_code is not None else 'N/A'})")
        
        if new_status == PermissionStatus.GRANTED:
            logger.info("✅ Accessibility: разрешение получено после prompt helper!")
            print("✅ [ACTIVATOR] Accessibility: разрешение получено!")
            return True

        # ШАГ 4: Fallback — открываем System Settings напрямую
        _open_permission_settings("accessibility", "Accessibility")

        # Разрешение ещё не получено - polling отследит когда пользователь включит
        logger.info("♿ Accessibility: ожидаем предоставления разрешения...")
        print("♿ [ACTIVATOR] Accessibility: ожидаем (пользователь должен включить в System Settings)")

        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Accessibility: {e}")
        print(f"❌ [ACTIVATOR] Accessibility error: {e}")
        import traceback
        traceback.print_exc()
        return False


async def activate_input_monitoring() -> bool:
    """
    Активировать запрос разрешения Input Monitoring.

    ВАЖНО: НЕ используем pynput для активации!
    pynput внутренне вызывает AXIsProcessTrustedWithOptions, который триггерит
    TCC error для Accessibility при первом запуске:
    "attempted to call TCCAccessRequest for kTCCServiceAccessibility 
    without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement"
    
    Вместо этого используем IOHIDRequestAccess - нативный API который:
    - Добавляет приложение в список Input Monitoring
    - Показывает системный диалог запроса разрешения
    - НЕ триггерит проверку Accessibility

    Returns:
        True если активация прошла успешно
    """
    try:
        # ШАГ 1: Проверяем - если разрешение уже есть, не делаем ничего
        from .status_checker import check_input_monitoring_status, PermissionStatus
        
        current_status = check_input_monitoring_status()
        if current_status == PermissionStatus.GRANTED:
            logger.info("✅ Input Monitoring: Разрешение уже предоставлено, пропускаем активацию")
            print("✅ [ACTIVATOR] Input Monitoring: Разрешение уже есть")
            return True
        
        # ШАГ 2: Разрешение не предоставлено - активируем
        logger.info("⌨️ Активация Input Monitoring через IOHIDRequestAccess...")
        print(f"⌨️ [ACTIVATOR] Начало активации Input Monitoring (IOHIDRequestAccess)")

        # Используем IOHIDRequestAccess - безопасный нативный API
        iokit_path = util.find_library("IOKit")
        if not iokit_path:
            logger.warning("⚠️ IOKit недоступен")
            _open_permission_settings("input_monitoring", "Input Monitoring")
            return False

        iokit = ctypes.CDLL(iokit_path)

        try:
            request_access = iokit.IOHIDRequestAccess
        except AttributeError:
            logger.warning("⚠️ IOHIDRequestAccess недоступен (старая macOS?)")
            _open_permission_settings("input_monitoring", "Input Monitoring")
            return False

        # IOHIDRequestAccess(requestType) -> bool
        # requestType = 1 для kIOHIDRequestTypeListenEvent (Input Monitoring)
        request_access.argtypes = [ctypes.c_uint32]
        request_access.restype = ctypes.c_bool

        kIOHIDRequestTypeListenEvent = 1  # Input Monitoring

        # Вызов IOHIDRequestAccess:
        # - Если разрешение NOT_DETERMINED: показывает системный диалог
        # - Если разрешение DENIED: добавляет в список (пользователь может включить вручную)
        # - Если разрешение GRANTED: возвращает True без диалога
        result = request_access(kIOHIDRequestTypeListenEvent)
        
        logger.info(f"✅ IOHIDRequestAccess(ListenEvent) вызван, result={result}")
        print(f"✅ [ACTIVATOR] IOHIDRequestAccess result={result}")
        
        # Даем системе время обработать запрос
        await asyncio.sleep(0.2)

        new_status = check_input_monitoring_status()
        if new_status != PermissionStatus.GRANTED:
            _open_permission_settings("input_monitoring", "Input Monitoring")

        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Input Monitoring: {e}")
        print(f"❌ [ACTIVATOR] Input Monitoring error: {e}")
        _open_permission_settings("input_monitoring", "Input Monitoring")
        return False


async def activate_screen_capture() -> bool:
    """
    Активировать запрос разрешения Screen Capture.

    Вызывает CGRequestScreenCaptureAccess для показа диалога.
    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        # ШАГ 1: Проверяем - если разрешение уже есть, не делаем ничего
        from .status_checker import check_screen_capture_status, PermissionStatus
        
        current_status = check_screen_capture_status()
        if current_status == PermissionStatus.GRANTED:
            logger.info("✅ Screen Capture: Разрешение уже предоставлено, пропускаем активацию")
            print("✅ [ACTIVATOR] Screen Capture: Разрешение уже есть")
            return True
        
        # ШАГ 2: Разрешение не предоставлено - активируем
        logger.info("📺 Активация Screen Capture...")

        # Используем существующий ScreenCapturePermissionManager
        from modules.permissions.macos.screen_capture_permission import ScreenCapturePermissionManager

        manager = ScreenCapturePermissionManager()

        if not manager.is_available:
            logger.warning("⚠️ Screen Capture API недоступен")
            _open_permission_settings("screen_capture", "Screen Capture")
            return False

        # request_permission() вызывает CGRequestScreenCaptureAccess
        # Это покажет диалог если разрешение NOT_DETERMINED
        granted = manager.request_permission()

        if granted:
            logger.info("✅ Screen Capture предоставлен (или диалог показан)")
        else:
            logger.info("✅ Screen Capture диалог показан")

        await asyncio.sleep(0.2)
        new_status = check_screen_capture_status()
        if new_status != PermissionStatus.GRANTED:
            _open_permission_settings("screen_capture", "Screen Capture")

        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Screen Capture: {e}")
        _open_permission_settings("screen_capture", "Screen Capture")
        return False


async def activate_all_permissions() -> dict:
    """
    Активировать все разрешения ПОСЛЕДОВАТЕЛЬНО.
    
    ВАЖНО: Запускаем разрешения по одному, чтобы диалоги не появлялись одновременно.
    Это улучшает UX и предотвращает путаницу пользователя.
    """
    logger.info("🚀 Активация всех разрешений в последовательном режиме...")
    
    results = {}
    
    # Порядок важен: сначала микрофон (самый простой), потом остальные
    permission_order = [
        ('microphone', activate_microphone),
        ('accessibility', activate_accessibility),
        ('input_monitoring', activate_input_monitoring),
        ('screen_capture', activate_screen_capture),
    ]
    
    for perm_name, activate_func in permission_order:
        logger.info(f"📝 Активация {perm_name}...")
        try:
            result = await activate_func()
            results[perm_name] = result
            logger.info(f"   → {perm_name}: {result}")
        except Exception as e:
            logger.error(f"❌ Ошибка активации {perm_name}: {e}")
            results[perm_name] = False
    
    logger.info(f"🏁 Все запросы разрешений завершены. Результаты: {results}")
    
    return results
