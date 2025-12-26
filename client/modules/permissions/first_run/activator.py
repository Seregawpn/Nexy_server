"""
Activator для активации разрешений macOS.

Вызывает системные API чтобы триггернуть показ диалогов разрешений.
Не ждёт ответа пользователя - просто вызывает API и возвращается.
"""

import asyncio
import logging
import ctypes
from ctypes import util


from integration.utils.logging_setup import get_logger
from config.unified_config_loader import UnifiedConfigLoader

logger = get_logger(__name__)


async def activate_microphone(hold_duration: float = 7.0) -> bool:
    """
    Активировать запрос разрешения микрофона.

    Открывает микрофон и держит его открытым на протяжении hold_duration секунд.
    Это даёт системе время показать диалог, а пользователю - ответить.

    Args:
        hold_duration: сколько секунд держать микрофон открытым (по умолчанию 7.0)

    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        logger.info(f"🎙️ Активация микрофона (держим открытым {hold_duration} сек)...")
        print(f"🎙️ [ACTIVATOR] Начало активации микрофона")  # DEBUG: Для console.app

        # Используем sounddevice для открытия микрофона
        import sounddevice as sd

        # Открываем input stream и держим открытым всю паузу
        # Это вызовет системный диалог если разрешение NOT_DETERMINED
        try:
            # Получаем дефолтное устройство
            print(f"🎙️ [ACTIVATOR] Запрос default input device...")  # DEBUG
            default_device = sd.query_devices(kind='input')
            logger.debug(f"   Default input device: {default_device['name']}")
            print(f"🎙️ [ACTIVATOR] Default device: {default_device['name']}")  # DEBUG

            # Открываем stream и держим открытым на протяжении всей паузы
            # Это гарантирует что диалог успеет появиться до следующего запроса
            print(f"🎙️ [ACTIVATOR] Открываем InputStream...")  # DEBUG
            with sd.InputStream(
                samplerate=16000,
                channels=1,
                dtype='int16',
                blocksize=8000,
            ):
                # Держим микрофон открытым всю паузу
                logger.debug(f"   ⏸️ Удерживаем микрофон открытым {hold_duration} сек...")
                print(f"🎙️ [ACTIVATOR] Удерживаем микрофон {hold_duration} сек...")  # DEBUG
                await asyncio.sleep(hold_duration)
                print(f"🎙️ [ACTIVATOR] Удержание завершено")  # DEBUG

            logger.info("✅ Микрофон активирован успешно")
            print(f"✅ [ACTIVATOR] Микрофон активирован успешно")  # DEBUG
            return True

        except Exception as e:
            logger.warning(f"⚠️ Не удалось открыть микрофон: {e}")
            print(f"⚠️ [ACTIVATOR] Exception при открытии микрофона: {e}")  # DEBUG
            # Это OK - возможно разрешения нет, диалог показан
            # Но даём ещё паузу для показа диалога
            print(f"⏸️ [ACTIVATOR] Ждём {hold_duration} сек для диалога...")  # DEBUG
            await asyncio.sleep(hold_duration)
            print(f"✅ [ACTIVATOR] Ожидание завершено")  # DEBUG
            return True

    except ImportError:
        logger.warning("⚠️ sounddevice недоступен")
        print(f"⚠️ [ACTIVATOR] sounddevice недоступен")  # DEBUG
        return False
    except Exception as e:
        logger.error(f"❌ Ошибка активации микрофона: {e}")
        print(f"❌ [ACTIVATOR] Критическая ошибка: {e}")  # DEBUG
        return False


async def activate_accessibility(hold_duration: float = 7.0) -> bool:
    """
    Активировать запрос разрешения Accessibility.

    Вызывает AXIsProcessTrustedWithOptions с prompt=False (только проверка статуса).
    Затем открывает System Settings для ручного запроса разрешения.
    Ждёт hold_duration секунд чтобы дать пользователю время ответить.

    Args:
        hold_duration: сколько секунд ждать после активации (по умолчанию 7.0)

    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        logger.info(f"♿ Активация Accessibility (пауза {hold_duration} сек)...")
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
        CoreGraphics.CGRequestPostEventAccess()

        logger.info("ℹ️ Accessibility диалог запрошен через CGRequestPostEventAccess")
        # В отличие от AX API, этот вызов не возвращает статус, он только триггерит UI,
        # поэтому мы не можем проверить 'trusted' здесь. Проверка статуса будет позже.

        # Ждём чтобы дать пользователю время ответить
        logger.debug(f"   ⏸️ Пауза {hold_duration} сек...")
        await asyncio.sleep(hold_duration)

        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Accessibility: {e}")
        return False


async def activate_input_monitoring(hold_duration: float = 7.0) -> bool:
    """
    Активировать запрос разрешения Input Monitoring.

    Использует публичный API IOHIDRequestAccess, который триггерит системный диалог
    (или автоматически открывает System Settings) если разрешение ещё не выдано.
    Затем делает паузу, чтобы дать пользователю время выдать доступ.

    Args:
        hold_duration: сколько секунд ждать после активации (по умолчанию 7.0)

    Returns:
        True если активация прошла успешно, False при ошибке
    """
    try:
        logger.info(f"⌨️ Активация Input Monitoring (пауза {hold_duration} сек)...")

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

        logger.debug(f"   ⏸️ Пауза {hold_duration} сек...")
        await asyncio.sleep(hold_duration)
        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Input Monitoring: {e}")
        return False


async def activate_screen_capture(hold_duration: float = 7.0) -> bool:
    """
    Активировать запрос разрешения Screen Capture.

    Вызывает CGRequestScreenCaptureAccess для показа диалога.
    Затем ждёт hold_duration секунд чтобы дать пользователю время ответить.

    Args:
        hold_duration: сколько секунд ждать после активации (по умолчанию 7.0)

    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        logger.info(f"📺 Активация Screen Capture (пауза {hold_duration} сек)...")

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

        # Ждём чтобы дать пользователю время ответить
        logger.debug(f"   ⏸️ Пауза {hold_duration} сек...")
        await asyncio.sleep(hold_duration)

        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Screen Capture: {e}")
        return False


async def activate_all_permissions(pause_seconds: float = 7.0) -> dict:
    """
    Активировать все разрешения ПАРАЛЛЕЛЬНО.
    Длительность паузы берется из центральной конфигурации.
    """
    try:
        permission_config = UnifiedConfigLoader.get_instance().get_permission_config()
        hold_duration = permission_config.get('first_run', {}).get('activation_hold_duration_sec', 13.0)
        logger.info(f"Используем 'activation_hold_duration_sec' из конфига: {hold_duration} сек.")
    except Exception as e:
        logger.warning(f"Не удалось загрузить 'activation_hold_duration_sec' из конфига. Используем значение по-умолчанию 13.0 сек. Ошибка: {e}")
        hold_duration = 13.0

    logger.info("🚀 Активация всех разрешений в параллельном режиме...")

    tasks = {
        'microphone': activate_microphone(hold_duration=hold_duration),
        'accessibility': activate_accessibility(hold_duration=hold_duration),
        'input_monitoring': activate_input_monitoring(hold_duration=hold_duration),
        'screen_capture': activate_screen_capture(hold_duration=hold_duration)
    }

    # Запускаем все задачи одновременно
    task_results = await asyncio.gather(*tasks.values())
    
    results = dict(zip(tasks.keys(), task_results))
    logger.info(f"   🏁 Все запросы разрешений завершены. Результаты: {results}")

    return results
