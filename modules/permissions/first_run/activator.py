"""
Activator для активации разрешений macOS.

Вызывает системные API чтобы триггернуть показ диалогов разрешений.
Не ждёт ответа пользователя - просто вызывает API и возвращается.
"""

import asyncio
import logging
import subprocess
import ctypes
from ctypes import util

logger = logging.getLogger(__name__)


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

        # Используем sounddevice для открытия микрофона
        import sounddevice as sd

        # Открываем input stream и держим открытым всю паузу
        # Это вызовет системный диалог если разрешение NOT_DETERMINED
        try:
            # Получаем дефолтное устройство
            default_device = sd.query_devices(kind='input')
            logger.debug(f"   Default input device: {default_device['name']}")

            # Открываем stream и держим открытым на протяжении всей паузы
            # Это гарантирует что диалог успеет появиться до следующего запроса
            with sd.InputStream(
                samplerate=16000,
                channels=1,
                dtype='int16',
                blocksize=8000,
            ):
                # Держим микрофон открытым всю паузу
                logger.debug(f"   ⏸️ Удерживаем микрофон открытым {hold_duration} сек...")
                await asyncio.sleep(hold_duration)

            logger.info("✅ Микрофон активирован успешно")
            return True

        except Exception as e:
            logger.warning(f"⚠️ Не удалось открыть микрофон: {e}")
            # Это OK - возможно разрешения нет, диалог показан
            return True

    except ImportError:
        logger.warning("⚠️ sounddevice недоступен")
        return False
    except Exception as e:
        logger.error(f"❌ Ошибка активации микрофона: {e}")
        return False


async def activate_accessibility(hold_duration: float = 7.0) -> bool:
    """
    Активировать запрос разрешения Accessibility.

    Вызывает AXIsProcessTrustedWithOptions с prompt=True для показа диалога.
    Затем ждёт hold_duration секунд чтобы дать пользователю время ответить.

    Args:
        hold_duration: сколько секунд ждать после активации (по умолчанию 7.0)

    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        logger.info(f"♿ Активация Accessibility (пауза {hold_duration} сек)...")

        try:
            from Quartz import AXIsProcessTrustedWithOptions, kAXTrustedCheckOptionPrompt
            from Foundation import NSDictionary, NSNumber
        except ImportError:
            logger.warning("⚠️ Quartz/AX API недоступен – не удалось запросить Accessibility")
            return False

        try:
            # Вызываем с prompt=True, чтобы система показала диалог, если доступ ещё не выдан
            options = NSDictionary.dictionaryWithObject_forKey_(
                NSNumber.numberWithBool_(True),
                kAXTrustedCheckOptionPrompt,
            )
            trusted = bool(AXIsProcessTrustedWithOptions(options))
        except Exception as ax_err:
            logger.error(f"❌ Ошибка вызова AXIsProcessTrustedWithOptions: {ax_err}")
            return False

        if trusted:
            logger.info("✅ Accessibility уже предоставлен")
        else:
            logger.info("✅ Accessibility диалог показан (или будет открыт System Settings)")
            try:
                subprocess.Popen([
                    'open',
                    'x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility'
                ])
                logger.debug("   🔗 Открываем System Settings -> Privacy & Security → Accessibility")
            except Exception as open_err:
                logger.debug(f"   ⚠️ Не удалось открыть System Settings: {open_err}")
            else:
                try:
                    subprocess.Popen([
                        'osascript',
                        '-e',
                        'tell application "System Settings" to activate'
                    ])
                    logger.debug("   🪟 Делаем System Settings активным окном")
                except Exception as activate_err:
                    logger.debug(f"   ⚠️ Не удалось активировать System Settings: {activate_err}")

                try:
                    dialog_script = (
                        'set dialogResult to display dialog '
                        '"Nexy нужен доступ к Accessibility, чтобы отслеживать клавиатуру и автоматизировать действия.\\n\\n'
                        '1. Нажмите на замок в левом нижнем углу и введите пароль.\\n'
                        '2. Поставьте галочку напротив Nexy.\\n'
                        '3. Перезапустите Nexy." '
                        'buttons {"Готово", "Открыть настройки"} default button "Открыть настройки" with icon caution\n'
                        'if button returned of dialogResult is "Открыть настройки" then\n'
                        '    tell application "System Settings" to activate\n'
                        '    do shell script "open x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"\n'
                        'end if'
                    )
                    subprocess.Popen(['osascript', '-e', dialog_script])
                    logger.debug("   💬 Показано диалоговое окно с инструкцией по выдаче доступа")
                except Exception as dialog_err:
                    logger.debug(f"   ⚠️ Не удалось показать диалоговое окно: {dialog_err}")

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
                "ℹ️ IOHIDRequestAccess вернул код %s – "
                "System Settings должно открыться для выдачи доступа",
                status_hex,
            )
            try:
                subprocess.Popen([
                    'open',
                    'x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent'
                ])
                logger.debug("   🔗 Открываем System Settings для Input Monitoring")
            except Exception as open_err:
                logger.debug(f"   ⚠️ Не удалось открыть System Settings: {open_err}")

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
    Активировать все разрешения последовательно с паузами.

    Args:
        pause_seconds: пауза между активациями в секундах

    Returns:
        dict: словарь с результатами {permission_name: bool}
    """
    results = {}

    # Microphone
    results['microphone'] = await activate_microphone()
    if results['microphone']:
        logger.info(f"   Пауза {pause_seconds} сек...")
        await asyncio.sleep(pause_seconds)

    # Accessibility
    results['accessibility'] = await activate_accessibility()
    if results['accessibility']:
        logger.info(f"   Пауза {pause_seconds} сек...")
        await asyncio.sleep(pause_seconds)

    # Input Monitoring
    results['input_monitoring'] = await activate_input_monitoring()
    if results['input_monitoring']:
        logger.info(f"   Пауза {pause_seconds} сек...")
        await asyncio.sleep(pause_seconds)

    # Screen Capture
    results['screen_capture'] = await activate_screen_capture()
    if results['screen_capture']:
        logger.info(f"   Пауза {pause_seconds} сек...")
        await asyncio.sleep(pause_seconds)

    return results
