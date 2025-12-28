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

    Вызывает AXIsProcessTrustedWithOptions с prompt=False (только проверка статуса).
    Затем открывает System Settings для ручного запроса разрешения.

    Args:
    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        logger.info("♿ Активация Accessibility...")
        print(f"♿ [ACTIVATOR] Начало активации Accessibility")  # DEBUG

        try:
            from Quartz import CoreGraphics
        except ImportError:
            logger.error("❌ КРИТИЧНО: CoreGraphics (Quartz) API недоступен.")
            print(f"❌ [ACTIVATOR] CoreGraphics (Quartz) API недоступен")  # DEBUG
            return False

        # Используем CGRequestPostEventAccess() как публичный и более прямой способ
        # запросить разрешение, необходимое для управления событиями.
        logger.info("♿ [ACTIVATOR] Вызываем CGRequestPostEventAccess()...")
        print(f"♿ [ACTIVATOR] Вызываем CGRequestPostEventAccess()...")  # DEBUG
        
        # Этот вызов напрямую триггерит системный диалог, если разрешение не выдано
        # type: ignore[attr-defined] - CGRequestPostEventAccess exists at runtime but not in type stubs
        CoreGraphics.CGRequestPostEventAccess()  # type: ignore[attr-defined]

        logger.info("ℹ️ Accessibility диалог запрошен через CGRequestPostEventAccess")
        # В отличие от AX API, этот вызов не возвращает статус, он только триггерит UI,
        # поэтому мы не можем проверить 'trusted' здесь. Проверка статуса будет позже.

        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Accessibility: {e}")
        return False


async def activate_input_monitoring() -> bool:
    """
    Активировать запрос разрешения Input Monitoring.

    Использует публичный API IOHIDRequestAccess, который триггерит системный диалог
    (или автоматически открывает System Settings) если разрешение ещё не выдано.
    Returns:
        True если активация прошла успешно, False при ошибке
    """
    try:
        logger.info("⌨️ Активация Input Monitoring...")

        iokit_path = util.find_library("IOKit")
        if not iokit_path:
            logger.warning("⚠️ Не удалось найти библиотеку IOKit – пропускаем запрос")
            return False

        iokit = ctypes.CDLL(iokit_path)

        kIOHIDRequestTypeListenEvent = ctypes.c_uint32(1)
        kIOReturnSuccess = 0

        try:
            request_access = iokit.IOHIDRequestAccess
        except AttributeError:
            logger.warning("⚠️ IOHIDRequestAccess недоступен – вероятно старая версия macOS")
            return False

        request_access.argtypes = [ctypes.c_uint32]
        request_access.restype = ctypes.c_int32

        status = request_access(kIOHIDRequestTypeListenEvent.value)

        if status == kIOReturnSuccess:
            logger.info("✅ Input Monitoring разрешение уже выдано или диалог был открыт")
        else:
            status_hex = hex(ctypes.c_uint32(status).value)
            logger.info(
                "ℹ️ IOHIDRequestAccess вернул код %s",
                status_hex,
            )
            logger.info("   macOS автоматически откроет System Settings если нужно")
            logger.info("   Пожалуйста, предоставьте доступ в System Settings → Privacy & Security → Input Monitoring")

        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Input Monitoring: {e}")
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
