"""
Activator для активации разрешений macOS.

Вызывает системные API чтобы триггернуть показ диалогов разрешений.
Не ждёт ответа пользователя - просто вызывает API и возвращается.
"""

import asyncio
import ctypes
from ctypes import util


from integration.utils.logging_setup import get_logger

logger = get_logger(__name__)


async def activate_microphone() -> bool:
    """
    Активировать запрос разрешения микрофона.

    Открывает микрофон для триггера системного диалога.

    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
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
            return True

        except Exception as e:
            logger.warning(f"⚠️ Не удалось открыть микрофон: {e}")
            print(f"⚠️ [ACTIVATOR] Exception при открытии микрофона: {e}")  # DEBUG
            # Это OK - возможно разрешения нет, диалог показан
            return True

    except ImportError:
        logger.warning("⚠️ sounddevice недоступен")
        print(f"⚠️ [ACTIVATOR] sounddevice недоступен")  # DEBUG
        return False
    except Exception as e:
        logger.error(f"❌ Ошибка активации микрофона: {e}")
        print(f"❌ [ACTIVATOR] Критическая ошибка: {e}")  # DEBUG
        return False


async def activate_accessibility() -> bool:
    """
    Активировать запрос разрешения Accessibility.

    КРИТИЧНО (macOS Sequoia 26+):
    AXIsProcessTrustedWithOptions КРАШИТ ПРОЦЕСС независимо от опций!
    Даже с prompt=True система вызывает внутренний TCCAccessRequest который
    требует приватный entitlement com.apple.private.tcc.manager.check-by-audit-token.
    
    БЕЗОПАСНЫЙ ПОДХОД: Открываем System Settings напрямую.
    Это единственный безопасный способ показать пользователю где включить Accessibility.

    Returns:
        True если настройки открыты успешно
        False если произошла ошибка
    """
    try:
        logger.info("♿ Активация Accessibility - открываем System Settings...")
        print("♿ [ACTIVATOR] Открываем System Settings > Security & Privacy > Accessibility")

        import subprocess
        
        # Открываем System Settings на странице Accessibility
        # Это безопасный способ - не вызывает TCCAccessRequest
        subprocess.run([
            "open", 
            "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"
        ], check=False)
        
        logger.info("✅ Accessibility: System Settings открыты")
        print("✅ [ACTIVATOR] Accessibility: System Settings открыты")
        
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
        logger.info("⌨️ Активация Input Monitoring через IOHIDRequestAccess...")
        print(f"⌨️ [ACTIVATOR] Начало активации Input Monitoring (IOHIDRequestAccess)")

        # Используем IOHIDRequestAccess - безопасный нативный API
        iokit_path = util.find_library("IOKit")
        if not iokit_path:
            logger.warning("⚠️ IOKit недоступен")
            return False

        iokit = ctypes.CDLL(iokit_path)

        try:
            request_access = iokit.IOHIDRequestAccess
        except AttributeError:
            logger.warning("⚠️ IOHIDRequestAccess недоступен (старая macOS?)")
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
        await asyncio.sleep(0.1)
        
        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Input Monitoring: {e}")
        print(f"❌ [ACTIVATOR] Input Monitoring error: {e}")
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
        logger.info("📺 Активация Screen Capture...")

        # Используем существующий ScreenCapturePermissionManager
        from modules.permissions.macos.screen_capture_permission import ScreenCapturePermissionManager

        manager = ScreenCapturePermissionManager()

        if not manager.is_available:
            logger.warning("⚠️ Screen Capture API недоступен")
            return False

        # request_permission() вызывает CGRequestScreenCaptureAccess
        # Это покажет диалог если разрешение NOT_DETERMINED
        granted = manager.request_permission()

        if granted:
            logger.info("✅ Screen Capture предоставлен (или диалог показан)")
        else:
            logger.info("✅ Screen Capture диалог показан")

        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Screen Capture: {e}")
        return False


async def activate_all_permissions() -> dict:
    """
    Активировать все разрешения ПАРАЛЛЕЛЬНО.
    """
    logger.info("🚀 Активация всех разрешений в параллельном режиме...")

    tasks = {
        'microphone': activate_microphone(),
        'accessibility': activate_accessibility(),
        'input_monitoring': activate_input_monitoring(),
        'screen_capture': activate_screen_capture()
    }

    # Запускаем все задачи одновременно
    task_results = await asyncio.gather(*tasks.values())
    
    results = dict(zip(tasks.keys(), task_results))
    logger.info(f"   🏁 Все запросы разрешений завершены. Результаты: {results}")

    return results
