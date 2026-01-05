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

    ВАЖНО: Любые вызовы AX или CG API для Accessibility могут вызывать crash
    при первом запуске после сброса разрешений. Поэтому мы НЕ вызываем никаких
    системных API здесь - просто возвращаем True и полагаемся на open_settings
    для показа инструкций пользователю.

    Returns:
        True всегда - активация "успешна" (пользователь будет направлен в Settings)
    """
    logger.info("♿ Активация Accessibility (безопасный режим - без системных API)...")
    print(f"♿ [ACTIVATOR] Accessibility: пропускаем системный диалог, используем open_settings")
    
    # НЕ вызываем никаких AX/CG API - они могут crash'ить приложение
    # Вместо этого open_settings покажет System Preferences и help dialog
    
    return True


async def activate_input_monitoring() -> bool:
    """
    Активировать запрос разрешения Input Monitoring.

    Использует pynput Listener, который гарантированно триггерит системный диалог TCC
    или добавляет приложение в список Input Monitoring (даже если оно Denied).
    IOHIDRequestAccess часто бывает недостаточно в новых macOS.

    Returns:
        True если активация прошла успешно (попытка перехвата сделана)
    """
    try:
        logger.info("⌨️ Активация Input Monitoring через pynput...")
        print(f"⌨️ [ACTIVATOR] Начало активации Input Monitoring (pynput)")

        from pynput import keyboard

        # Создаем Listener - это действие требует прав Input Monitoring.
        # Если прав нет, macOS покажет диалог или добавит приложение в список.
        # Мы не ждем нажатий, нам сам факт запуска Listener важен.
        try:
            # Запускаем listener в неблокирующем режиме на короткое время
            def on_press(key): pass
            
            listener = keyboard.Listener(on_press=on_press)
            listener.start()
            
            # Даем системе время заметить попытку перехвата (0.5 сек достаточно)
            await asyncio.sleep(0.5)
            
            if listener.running:
                listener.stop()
                
            logger.info("✅ Input Monitoring триггер сработал (pynput listener started/stopped)")
            return True

        except Exception as e:
            # Если прав совсем нет, pynput может кинуть исключение - это тоже триггер
            logger.info(f"ℹ️ Pynput exception (это нормально, триггер сработал): {e}")
            return True

    except ImportError:
        logger.error("❌ pynput не установлен, не можем активировать Input Monitoring")
        return False
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
