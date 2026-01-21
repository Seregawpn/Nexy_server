"""
Activator для активации разрешений macOS.

Вызывает системные API чтобы триггернуть показ диалогов разрешений.
Не ждёт ответа пользователя - просто вызывает API и возвращается.
"""

import asyncio
import ctypes
import os
import subprocess
import threading
from ctypes import util
from typing import List, Optional


from integration.utils.logging_setup import get_logger
from config.unified_config_loader import UnifiedConfigLoader

logger = get_logger(__name__)
_PENDING_ALERTS: list[object] = []


def _get_system_preferences_url(permission_key: str) -> str:
    try:
        from config.unified_config_loader import UnifiedConfigLoader

        permissions_config = UnifiedConfigLoader.get_instance().get_permission_config()
        return permissions_config.get("system_preferences", {}).get(permission_key, "")
    except Exception as e:
        logger.warning(f"⚠️ Не удалось получить System Settings URL для {permission_key}: {e}")
        return ""


def _open_permission_settings(permission_key: str, label: str, *, background: bool = True) -> None:
    url = _get_system_preferences_url(permission_key)
    if not url:
        logger.warning(f"⚠️ System Settings URL не найден для {label}")
        return

    logger.info(f"🔧 {label}: открываем System Settings...")
    print(f"🔧 [ACTIVATOR] {label}: открываем System Settings...")
    try:
        command = ["open"]
        if background:
            command.append("-g")
        command.append(url)
        # Не блокируем поток на открытии System Settings.
        subprocess.Popen(command)
        logger.info(f"✅ System Settings открыт для {label}")
    except Exception as e:
        logger.warning(f"⚠️ Не удалось открыть System Settings для {label}: {e}")


def _open_permission_settings_no_focus(permission_key: str, label: str) -> None:
    """Open System Settings in background to avoid stealing app focus."""
    _open_permission_settings(permission_key, label, background=True)


async def activate_microphone(hold_duration: float = 0.2) -> bool:
    """
    Активировать запрос разрешения микрофона.

    Открывает микрофон для триггера системного диалога.

    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        # ВАЖНО: НЕ проверяем статус здесь!
        # Интеграция решает когда вызывать, активатор просто делает своё дело.
        # Если разрешение уже выдано, sounddevice просто откроет поток без диалога.
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

            # Открываем stream для триггера системного диалога
            print(f"🎙️ [ACTIVATOR] Открываем InputStream...")  # DEBUG
            with sd.InputStream(
                samplerate=16000,
                channels=1,
                dtype='int16',
                blocksize=8000,
            ):
                print("🎙️ [ACTIVATOR] Поток открыт")  # DEBUG
                # Держим поток открытым кратко, чтобы инициировать prompt
                stream_hold = min(max(0.0, hold_duration), 0.5)
                if stream_hold:
                    await asyncio.sleep(stream_hold)

            remaining_hold = max(0.0, hold_duration) - stream_hold
            if remaining_hold:
                logger.info("   ⏸️ Holding %.2fs after stream close...", remaining_hold)
                await asyncio.sleep(remaining_hold)

            logger.info("✅ Микрофон активирован успешно")
            print(f"✅ [ACTIVATOR] Микрофон активирован успешно")  # DEBUG

        except Exception as e:
            logger.warning(f"⚠️ Не удалось открыть микрофон: {e}")
            print(f"⚠️ [ACTIVATOR] Exception при открытии микрофона: {e}")  # DEBUG
            # Это OK - возможно разрешения нет, диалог показан
            await asyncio.sleep(max(0.0, hold_duration))
        
        # Dialog-only: не открываем Settings автоматически
        # Fallback будет вызван из интеграции если нужно
        await asyncio.sleep(0)
        return True

    except ImportError:
        logger.warning("⚠️ sounddevice недоступен")
        print(f"⚠️ [ACTIVATOR] sounddevice недоступен")  # DEBUG
        # Dialog-only: не открываем Settings автоматически
        # Fallback будет вызван из интеграции если нужно
        return True
    except Exception as e:
        logger.error(f"❌ Ошибка активации микрофона: {e}")
        print(f"❌ [ACTIVATOR] Критическая ошибка: {e}")  # DEBUG
        # Dialog-only: не открываем Settings автоматически
        # Fallback будет вызван из интеграции если нужно
        return False


async def activate_accessibility(hold_duration: float = 7.0) -> bool:
    """
    Активировать запрос разрешения Accessibility.

    Args:
        hold_duration: сколько секунд ждать после активации (по умолчанию 7.0)

    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        logger.info("♿ Активация Accessibility (CGRequestPostEventAccess)...")
        print("♿ [ACTIVATOR] Начало активации Accessibility")  # DEBUG

        try:
            from Quartz import CGRequestPostEventAccess  # type: ignore
            logger.info("♿ [ACTIVATOR] Вызываем CGRequestPostEventAccess()...")
            print("♿ [ACTIVATOR] Вызываем CGRequestPostEventAccess()...")  # DEBUG
            CGRequestPostEventAccess()
            logger.info("✅ Accessibility: CGRequestPostEventAccess() вызван")
        except ImportError:
            logger.warning("⚠️ CGRequestPostEventAccess недоступен")
            return False
        except Exception as e:
            logger.warning("⚠️ CGRequestPostEventAccess error: %s", e)
            return False

        logger.debug("   ⏸️ Пауза %.2f сек...", hold_duration)
        await asyncio.sleep(max(0.0, hold_duration))
        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Accessibility: {e}")
        return False


async def activate_input_monitoring(hold_duration: float = 1.0) -> bool:
    """
    Активировать запрос разрешения Input Monitoring.

    ВАЖНО: НЕ используем pynput для активации!
    pynput внутренне вызывает AXIsProcessTrustedWithOptions, который триггерит
    TCC error для Accessibility при первом запуске:
    attempted to call TCCAccessRequest for kTCCServiceAccessibility 
    without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
    
    Вместо этого используем IOHIDRequestAccess - нативный API который:
    - Добавляет приложение в список Input Monitoring
    - Показывает системный диалог запроса разрешения
    - НЕ триггерит проверку Accessibility

    Returns:
        True если активация прошла успешно
    """
    try:
        # Всегда активируем - НЕ проверяем статус!
        logger.info("⌨️ Активация Input Monitoring через IOHIDRequestAccess...")
        print("⌨️ [ACTIVATOR] Начало активации Input Monitoring (IOHIDRequestAccess)")

        # Используем IOHIDRequestAccess - безопасный нативный API
        iokit_path = util.find_library("IOKit")
        if not iokit_path:
            logger.warning("⚠️ IOKit недоступен")
            # Dialog-only: не открываем Settings автоматически
            # Fallback будет вызван из интеграции если нужно
            return False

        iokit = ctypes.CDLL(iokit_path)

        try:
            request_access = iokit.IOHIDRequestAccess
        except AttributeError:
            logger.warning("⚠️ IOHIDRequestAccess недоступен (старая macOS?)")
            # Dialog-only: не открываем Settings автоматически
            # Fallback будет вызван из интеграции если нужно
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
        
        if result:
            logger.info(f"✅ IOHIDRequestAccess(ListenEvent) вернул True (Granted)")
            print(f"✅ [ACTIVATOR] IOHIDRequestAccess=True (Granted)")
        else:
            logger.info(f"ℹ️ IOHIDRequestAccess(ListenEvent) вернул False (Prompt shown or Denied)")
            print(f"ℹ️ [ACTIVATOR] IOHIDRequestAccess=False (Prompt shown or Denied)")
        
        hold_duration = max(0.0, hold_duration)
        logger.info("   ⏸️ Holding %.2fs after IOHIDRequestAccess...", hold_duration)
        # Dialog-only: не открываем Settings автоматически
        # Fallback будет вызван из интеграции если нужно
        await asyncio.sleep(hold_duration)
        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Input Monitoring: {e}")
        print(f"❌ [ACTIVATOR] Input Monitoring error: {e}")
        # Dialog-only: не открываем Settings автоматически
        # Fallback будет вызван из интеграции если нужно
        return False


async def activate_screen_capture(hold_duration: float = 0.2) -> bool:
    """
    Активировать запрос разрешения Screen Capture.

    Вызывает CGRequestScreenCaptureAccess для показа диалога.
    Returns:
        True если активация прошла успешно
        False если произошла ошибка
    """
    try:
        # ВАЖНО: НЕ проверяем статус здесь!
        # Интеграция решает когда вызывать, активатор просто делает своё дело.
        # CGRequestScreenCaptureAccess() безопасен при повторных вызовах.
        logger.info("📺 Активация Screen Capture...")

        # Используем существующий ScreenCapturePermissionManager
        from modules.permissions.macos.screen_capture_permission import ScreenCapturePermissionManager

        manager = ScreenCapturePermissionManager()

        if not manager.is_available:
            logger.warning("⚠️ Screen Capture API недоступен")
            # Dialog-only: не открываем Settings автоматически
            # Fallback будет вызван из интеграции если нужно
            return False

        # request_permission() вызывает CGRequestScreenCaptureAccess
        # Это покажет диалог если разрешение NOT_DETERMINED
        granted = manager.request_permission()

        if granted:
            logger.info("✅ Screen Capture предоставлен (или диалог показан)")
        else:
            logger.info("✅ Screen Capture диалог показан")

        # Dialog-only: не открываем Settings автоматически
        # Fallback будет вызван из интеграции если нужно
        await asyncio.sleep(max(0.0, hold_duration))
        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Screen Capture: {e}")
        # Dialog-only: не открываем Settings автоматически
        # Fallback будет вызван из интеграции если нужно
        return False


async def activate_contacts(hold_duration: float = 1.0) -> bool:
    """
    Активировать запрос разрешения Contacts.
    
    Использует CNContactStore.requestAccessForEntityType для показа диалога.
    
    Returns:
        True если активация прошла успешно
    """
    try:
        logger.info("📇 Активация Contacts...")
        print("📇 [ACTIVATOR] Активация Contacts...")
        
        from Contacts import CNContactStore, CNEntityTypeContacts  # type: ignore
        
        store = CNContactStore.alloc().init()
        
        # requestAccessForEntityType показывает системный диалог
        logger.info("📇 Contacts: запрашиваем доступ...")
        print("📇 [ACTIVATOR] Contacts: запрашиваем доступ...")
        
        granted = [None]
        error = [None]
        done = asyncio.Event()
        
        def completion_handler(success, err):
            granted[0] = success
            error[0] = err
            logger.info(f"📇 Contacts completion_handler: success={success}, err={err}")
            print(f"📇 [ACTIVATOR] Contacts callback: success={success}")
            try:
                loop = asyncio.get_running_loop()
                loop.call_soon_threadsafe(done.set)
            except RuntimeError:
                pass
            except Exception as e:
                logger.error(f"Error in contacts completion handler: {e}")
        
        store.requestAccessForEntityType_completionHandler_(
            CNEntityTypeContacts,
            completion_handler
        )
        
        # Ждём завершения или timeout
        try:
            await asyncio.wait_for(done.wait(), timeout=hold_duration)
        except asyncio.TimeoutError:
            logger.info(f"📇 Contacts: hold_duration {hold_duration}s elapsed (user didn't respond yet)")
            # Это нормально - диалог может висеть дольше
        
        if granted[0] is True:
            logger.info("✅ Contacts: разрешение получено (Granted)")
            print("✅ [ACTIVATOR] Contacts: GRANTED")
        elif granted[0] is False:
            logger.info(f"🚫 Contacts: доступ запрещен (Denied) или ошибка: {error[0]}")
            print(f"🚫 [ACTIVATOR] Contacts: DENIED/ERROR: {error[0]}")
        else:
            logger.info("📇 Contacts: нет ответа (Not Determined / Ignored)")
            print("📇 [ACTIVATOR] Contacts: No response yet")

        # Дополнительная попытка доступа, чтобы TCC добавил приложение в список
        try:
            _ = store.defaultContainerIdentifier()
        except Exception:
            pass
        
        return True

    except ImportError:
        logger.warning("⚠️ Contacts framework not available; no dialog can be shown")
        print("⚠️ [ACTIVATOR] Contacts framework not available")
        await asyncio.sleep(max(0.0, hold_duration))
        return True
    except Exception as e:
        logger.error(f"❌ Ошибка активации Contacts: {e}")
        return False


async def activate_full_disk_access(hold_duration: float = 1.0) -> bool:
    """
    Активировать запрос разрешения Full Disk Access.
    
    ВАЖНО: Full Disk Access НЕЛЬЗЯ запросить программно!
    Открываем System Settings сразу (без диалога).
    
    Returns:
        True если Settings открыт успешно
    """
    try:
        logger.info("💾 Активация Full Disk Access (settings-only)...")
        print("💾 [ACTIVATOR] Full Disk Access: settings-only")

        try:
            # ВАЖНО: Открываем С фокусом (background=False) чтобы пользователь заметил окно!
            _open_permission_settings("full_disk_access", "Full Disk Access", background=False)
        except Exception as exc:
            logger.warning("⚠️ Full Disk Access settings open failed: %s", exc)

        def _fda_access_attempt():
            try:
                from pathlib import Path
                protected_file = Path.home() / "Library" / "Messages" / "chat.db"
                if protected_file.exists():
                    with open(protected_file, "rb") as handle:
                        handle.read(1)
                    logger.info("💾 Full Disk Access: access attempt succeeded (async)")
                else:
                    logger.info("💾 Full Disk Access: chat.db not found; access attempt skipped (async)")
            except PermissionError:
                logger.info("💾 Full Disk Access: access attempt denied (async)")
            except Exception as exc:
                logger.debug("💾 Full Disk Access: access attempt failed (async): %s", exc)

        threading.Thread(
            target=_fda_access_attempt,
            name="FDAAccessAttempt",
            daemon=True,
        ).start()

        # Не блокируем first-run: настройки открыты, попытка доступа запущена.
        await asyncio.sleep(max(0.0, hold_duration))
        return True

    except Exception as e:
        logger.error(f"❌ Ошибка активации Full Disk Access: {e}")
        return False


def _load_permission_order() -> List[str]:
    """Load permission order from unified_config.yaml (no fallback)."""
    try:
        config_loader = UnifiedConfigLoader.get_instance()
        config_data = config_loader._load_config()
        permissions_config = config_data.get("integrations", {}).get("permissions", {})
        order = permissions_config.get("required_permissions", [])
        if isinstance(order, list) and order:
            return [str(item) for item in order]
    except Exception as e:
        logger.error("❌ Permission order config error: %s", e)
    return []


async def activate_all_permissions(permission_order: Optional[List[str]] = None) -> dict:
    """
    Активировать все разрешения ПОСЛЕДОВАТЕЛЬНО.
    
    ВАЖНО: Запускаем разрешения по одному, чтобы диалоги не появлялись одновременно.
    Это улучшает UX и предотвращает путаницу пользователя.
    """
    if os.environ.get("NEXY_ALLOW_ACTIVATE_ALL_PERMISSIONS") not in {"1", "true", "yes"}:
        logger.warning("⚠️ activate_all_permissions disabled by default; set NEXY_ALLOW_ACTIVATE_ALL_PERMISSIONS=1 to allow")
        return {}
    logger.info("🚀 Активация всех разрешений в последовательном режиме...")
    
    results = {}
    
    # Порядок берём из unified_config.yaml (integrations.permissions.required_permissions)
    order = permission_order or _load_permission_order()
    if not order:
        logger.error("❌ Permission order is empty; aborting activation")
        return results
    activators = {
        "input_monitoring": activate_input_monitoring,
        "microphone": activate_microphone,
        "screen_capture": activate_screen_capture,
        "accessibility": activate_accessibility,
        "contacts": activate_contacts,
        "full_disk_access": activate_full_disk_access,
    }

    for perm_name in order:
        activate_func = activators.get(perm_name)
        if not activate_func:
            logger.warning("⚠️ Unknown permission in order: %s", perm_name)
            results[perm_name] = False
            continue
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
