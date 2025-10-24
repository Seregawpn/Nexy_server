"""
Activator для активации разрешений macOS.

Вызывает системные API чтобы триггернуть показ диалогов разрешений.
Не ждёт ответа пользователя - просто вызывает API и возвращается.
"""

import asyncio
import logging
from typing import Optional

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
            import AppKit

            # Вызываем с prompt=True чтобы показать диалог
            # Если разрешение уже дано, диалог не появится
            options = {
                'prompt': True  # Показать диалог если нужно
            }

            trusted = AppKit.AXIsProcessTrustedWithOptions(options)

            if trusted:
                logger.info("✅ Accessibility уже предоставлен")
            else:
                logger.info("✅ Accessibility диалог показан (или открыт System Settings)")

            # Ждём чтобы дать пользователю время ответить
            logger.debug(f"   ⏸️ Пауза {hold_duration} сек...")
            await asyncio.sleep(hold_duration)

            return True

        except ImportError:
            logger.warning("⚠️ AppKit недоступен")
            return False

    except Exception as e:
        logger.error(f"❌ Ошибка активации Accessibility: {e}")
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

    # Screen Capture
    results['screen_capture'] = await activate_screen_capture()
    if results['screen_capture']:
        logger.info(f"   Пауза {pause_seconds} сек...")
        await asyncio.sleep(pause_seconds)

    return results
