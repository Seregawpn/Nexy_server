"""
ттNexy AI Assistant - Главный файл приложения
Только точка входа и инициализация SimpleModuleCoordinator
"""

import asyncio
import logging
import os
import sys
import signal
import traceback
import platform
from pathlib import Path
from datetime import datetime

# Добавляем пути к модулям (централизованно)
CLIENT_ROOT = Path(__file__).parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

# --- Ранняя инициализация pydub/ffmpeg (до любых вызовов pydub) ---
def init_ffmpeg_for_pydub():
    """Настраивает путь к встроенному ffmpeg для pydub.

     1) PyInstaller onefile: sys._MEIPASS/resources/ffmpeg/ffmpeg
    2) PyInstaller bundle:  Contents/Resources/resources/ffmpeg/ffmpeg
    3) Dev-режим:           resources/ffmpeg/ffmpeg (в корне проекта)
    """
    try:
        from pydub import AudioSegment  # noqa: F401
    except Exception:
        return

    ffmpeg_path = None
    # 1) onefile (временная распаковка)
    if hasattr(sys, "_MEIPASS"):
        cand = Path(getattr(sys, "_MEIPASS")) / "resources" / "ffmpeg" / "ffmpeg"
        if cand.exists():
            ffmpeg_path = cand
    # 2) bundle (.app): .../Contents/MacOS/main.py -> ../Resources/resources/ffmpeg/ffmpeg
    if ffmpeg_path is None:
        macos_dir = Path(__file__).resolve().parent
        resources_ffmpeg = macos_dir.parent / "Resources" / "resources" / "ffmpeg" / "ffmpeg"
        if resources_ffmpeg.exists():
            ffmpeg_path = resources_ffmpeg
        else:
            # Проверяем альтернативное расположение в Frameworks (PyInstaller иногда кладет туда)
            frameworks_ffmpeg = macos_dir.parent / "Frameworks" / "resources" / "ffmpeg" / "ffmpeg"
            if frameworks_ffmpeg.exists():
                ffmpeg_path = frameworks_ffmpeg
    # 3) dev-режим (репозиторий)
    if ffmpeg_path is None:
        dev_ffmpeg = Path(__file__).resolve().parent / "resources" / "ffmpeg" / "ffmpeg"
        if dev_ffmpeg.exists():
            ffmpeg_path = dev_ffmpeg

    if ffmpeg_path and ffmpeg_path.exists():
        try:
            from pydub import AudioSegment
            os.environ["FFMPEG_BINARY"] = str(ffmpeg_path)
            AudioSegment.converter = str(ffmpeg_path)
        except Exception:
            pass

    return ffmpeg_path


# Список ранних заметок до инициализации логгера
BOOT_NOTES: list[str] = []

# Выполняем инициализацию до импортов модулей, использующих pydub
_ffmpeg_path = init_ffmpeg_for_pydub()
BOOT_NOTES.append(f"init_ffmpeg_for_pydub: path={(str(_ffmpeg_path) if _ffmpeg_path else 'not found')}")

# --- Автоматический dev-bypass разрешений при запуске из терминала ---
def _is_terminal_launch() -> bool:
    """Определяет запуск из терминала (dev-режим), не для .app bundle."""
    if getattr(sys, "frozen", False):
        return False
    if os.environ.get("NEXY_DISABLE_TERMINAL_PERMISSIONS_BYPASS") in {"1", "true", "yes"}:
        return False
    return bool(sys.stdin.isatty() and sys.stdout.isatty() and os.environ.get("TERM"))


if _is_terminal_launch():
    os.environ.setdefault("NEXY_TEST_SKIP_PERMISSIONS", "1")
    os.environ.setdefault("NEXY_DEV_FORCE_PERMISSIONS", "1")
    BOOT_NOTES.append("terminal_launch: forced permissions bypass (NEXY_TEST_SKIP_PERMISSIONS=1, NEXY_DEV_FORCE_PERMISSIONS=1)")
    print("ℹ️ Terminal launch detected: permissions bypass enabled (test/dev mode)")

# --- Фикс PyObjC для macOS (до импорта rumps) ---
# ВАЖНО: Должен быть выполнен ДО импорта любых модулей, использующих rumps
# Исправляет проблему "dlsym cannot find symbol NSMakeRect in CFBundle"
try:
    # Правильный порядок импорта: сначала AppKit, потом Foundation
    import AppKit
    import Foundation
    
    # Убеждаемся, что AppKit полностью загружен
    if hasattr(AppKit, 'NSMakeRect'):
        # Копируем символы из AppKit в Foundation для совместимости
        # type: ignore[attr-defined] - PyObjC динамически создает атрибуты
        Foundation.NSMakeRect = AppKit.NSMakeRect  # type: ignore[attr-defined]
        Foundation.NSMakePoint = AppKit.NSMakePoint  # type: ignore[attr-defined]
        Foundation.NSMakeSize = AppKit.NSMakeSize  # type: ignore[attr-defined]
        Foundation.NSMakeRange = AppKit.NSMakeRange  # type: ignore[attr-defined]
        print("✅ AppKit символы успешно скопированы в Foundation")
    else:
        print("⚠️ AppKit.NSMakeRect не найден")
    BOOT_NOTES.append("pyobjc_fix: success (main.py)")

except ImportError as e:
    print(f"⚠️ PyObjC недоступен: {e}")
    BOOT_NOTES.append(f"pyobjc_fix: import_error:{e}")
except Exception as e:
    print(f"⚠️ Ошибка инициализации PyObjC: {e}")
    BOOT_NOTES.append(f"pyobjc_fix: error:{e}")

# Функция активации NSApplication - вызывается при каждом запуске
def activate_nsapplication_for_menu_bar():
    """
    CRITICAL: Activate NSApplication for LSUIElement applications.
    Without this, menu bar icon doesn't appear when launched from .app on macOS Sequoia.
    Must be called BEFORE creating rumps.App and NSStatusItem.

    This function is called on EVERY startup (including after restart via os.execv())
    to ensure NSApplication is properly configured.

    NOTE: Задержки удалены - tray теперь запускается рано и имеет собственную retry-логику.
    """
    try:
        import AppKit

        # Используем print для раннего лога (до настройки logging)
        msg = "[NEXY_INIT] Activating NSApplication for menu bar app..."
        print(msg)

        app = AppKit.NSApplication.sharedApplication()  # type: ignore[attr-defined]
        print(f"[NEXY_INIT] NSApplication instance: {app}")
        print(f"[NEXY_INIT] Current activation policy: {app.activationPolicy()}")

        # ДИАГНОСТИКА: Проверяем статус автоматической терминации
        try:
            import Foundation
            process_info = Foundation.NSProcessInfo.processInfo()  # type: ignore[attr-defined]
            auto_term_enabled = process_info.automaticTerminationSupportEnabled()
            print(f"[NEXY_INIT] 🔍 DIAGNOSTICS: automaticTerminationSupportEnabled = {auto_term_enabled}")
            print(f"[NEXY_INIT] 🔍 DIAGNOSTICS: System uptime = {process_info.systemUptime():.2f}s")
            print(f"[NEXY_INIT] 🔍 DIAGNOSTICS: Process ID = {process_info.processIdentifier()}")

            # Пытаемся отключить автоматическую терминацию на время старта
            if auto_term_enabled:
                process_info.disableAutomaticTermination_("Waiting for tray icon")
                print(f"[NEXY_INIT] 🛡️  ANTI-TAL: Disabled automatic termination until tray ready")
            else:
                print(f"[NEXY_INIT] ℹ️  INFO: Automatic termination was already disabled")
        except Exception as diag_err:
            print(f"[NEXY_INIT] ⚠️  WARNING: Could not check/modify termination status: {diag_err}")

        # Set activation policy for menu bar application
        # NSApplicationActivationPolicyAccessory (hide from Dock, show in menu bar)
        result = app.setActivationPolicy_(AppKit.NSApplicationActivationPolicyAccessory)  # type: ignore[attr-defined]
        print(f"[NEXY_INIT] setActivationPolicy(Accessory) returned: {result}")
        print(f"[NEXY_INIT] New activation policy: {app.activationPolicy()}")

        # Активируем приложение - ВАЖНО: True заставляет приложение стать активным
        app.activateIgnoringOtherApps_(True)
        print("[NEXY_INIT] Called activateIgnoringOtherApps_(True)")

        print("[NEXY_INIT] SUCCESS: NSApplication activated for menu bar app")
        return True
    except Exception as e:
        print(f"[NEXY_INIT] ERROR: NSApplication activation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

# Настройка логирования
# ВАЖНО: Для .app bundle логи должны писаться в файл, т.к. stdout недоступен
import tempfile
log_file = os.path.join(tempfile.gettempdir(), 'nexy_debug.log')

# Создаем два handler'а: один для файла, один для консоли
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Настраиваем root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(file_handler)
root_logger.addHandler(console_handler)

# [ARCH] Phase 2: Применяем централизованные настройки уровней логирования
from integration.utils.logging_setup import setup_logging
setup_logging()

logger = logging.getLogger(__name__)
logger.info(f"📝 Логи записываются в: {log_file}")
print(f"📝 Логи записываются в: {log_file}")
logger.info("BOOT: logger initialized")
logger.info(
    "BOOT: environment macOS=%s arch=%s python=%s cwd=%s",
    platform.mac_ver()[0] or "unknown",
    platform.machine(),
    sys.version.split()[0],
    os.getcwd(),
)
for note in BOOT_NOTES:
    logger.info("BOOT: %s", note)
logger.info("BOOT: tempr log file=%s", log_file)
def safe_exit(reason: str, code: int = 0) -> None:
    """Единая точка корректного завершения приложения."""
    try:
        logger.error(
            "SAFE_EXIT: reason=%s code=%s",
            reason,
            code,
            stack_info=True,
        )
    except Exception:
        pass

    # Пытаемся сбросить все handler'ы перед выходом
    for handler in logging.getLogger().handlers:
        try:
            handler.flush()
        except Exception:
            pass

    sys.exit(code)

# Глобальная переменная для отслеживания состояния приложения
_app_shutting_down = False

def log_crash_to_file(error_type, error_value, tb, context=""):
    """Записывает информацию о падении приложения в лог-файл"""
    try:
        crash_log_file = os.path.join(tempfile.gettempdir(), 'nexy_crash.log')
        with open(crash_log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*80 + "\n")
            f.write(f"💥 CRASH REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*80 + "\n")
            if context:
                f.write(f"Context: {context}\n")
            f.write(f"Error Type: {error_type.__name__}\n")
            f.write(f"Error Value: {error_value}\n")
            f.write(f"PID: {os.getpid()}\n")
            f.write(f"Python: {sys.version}\n")
            f.write(f"Working Dir: {os.getcwd()}\n")
            f.write("\nFull Traceback:\n")
            f.write("".join(traceback.format_exception(error_type, error_value, tb)))
            f.write("\n" + "="*80 + "\n\n")
        
        # Пытаемся использовать logger, если он доступен
        try:
            logger.critical(f"💥 CRASH записан в: {crash_log_file}")
        except Exception:
            pass
        print(f"💥 CRASH записан в: {crash_log_file}")
    except Exception as e:
        print(f"❌ Не удалось записать crash log: {e}")
        import traceback as tb_module
        tb_module.print_exc()

def exception_hook(error_type, error_value, tb):
    """Глобальный обработчик необработанных исключений"""
    global _app_shutting_down
    if _app_shutting_down:
        return
    
    # Логируем в основной лог
    logger.critical(
        f"💥 НЕОБРАБОТАННОЕ ИСКЛЮЧЕНИЕ: {error_type.__name__}: {error_value}",
        exc_info=(error_type, error_value, tb)
    )
    
    # Записываем в crash log
    log_crash_to_file(error_type, error_value, tb, "Unhandled exception")
    
    # Выводим в консоль
    print("\n" + "="*80)
    print("💥 НЕОБРАБОТАННОЕ ИСКЛЮЧЕНИЕ")
    print("="*80)
    traceback.print_exception(error_type, error_value, tb)
    print("="*80)
    print(f"📝 Полный лог ошибки записан в: {log_file}")
    print(f"💥 Crash report записан в: {os.path.join(tempfile.gettempdir(), 'nexy_crash.log')}")
    print("="*80 + "\n")
    
    # Вызываем стандартный обработчик для завершения приложения
    sys.__excepthook__(error_type, error_value, tb)

def signal_handler(signum, frame):
    """Обработчик сигналов для корректного завершения"""
    global _app_shutting_down
    signal_name = signal.Signals(signum).name
    logger.info(f"📡 Получен сигнал {signal_name} (PID: {os.getpid()})")
    print(f"\n📡 Получен сигнал {signal_name}, завершение работы...")
    
    _app_shutting_down = True
    
    # Записываем информацию о сигнале
    try:
        crash_log_file = os.path.join(tempfile.gettempdir(), 'nexy_crash.log')
        with open(crash_log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "="*80 + "\n")
            f.write(f"📡 SIGNAL RECEIVED - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Signal: {signal_name} ({signum})\n")
            f.write(f"PID: {os.getpid()}\n")
            f.write("="*80 + "\n\n")
    except Exception as e:
        logger.error(f"Не удалось записать signal log: {e}")
    
    # Завершаем приложение через safe_exit
    safe_exit(f"signal_handler signal={signal_name}", 0)

# Устанавливаем глобальный обработчик исключений
sys.excepthook = exception_hook

# Устанавливаем обработчики сигналов
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

async def main():
    """Главная функция"""
    try:
        logger.info("🚀 Запуск приложения Nexy...")
        logger.info(f"Python version: {sys.version}")
        logger.info(f"PID: {os.getpid()}")
        logger.info(f"Working directory: {os.getcwd()}")
        
        logger.info("BOOT: step 1 - importing SimpleModuleCoordinator")
        # Импортируем SimpleModuleCoordinator
        from integration.core.simple_module_coordinator import SimpleModuleCoordinator
        logger.info("BOOT: step 1 - SimpleModuleCoordinator import complete")

        # Создаем координатор
        coordinator = SimpleModuleCoordinator()
        logger.info("BOOT: step 2 - SimpleModuleCoordinator instantiated")

        # Передаем функцию активации NSApplication координатору
        # Она будет вызвана непосредственно перед app.run()
        coordinator.nsapp_activator = activate_nsapplication_for_menu_bar

        # Запускаем (run() сам вызовет initialize() и проверку дублирования)
        logger.info("BOOT: step 3 - coordinator.run() start")
        logger.info("READY: Nexy initialized successfully, entering run loop")
        await coordinator.run()
        logger.info("BOOT: step 3 - coordinator.run() completed")

    except KeyboardInterrupt:
        logger.info("⏹️ Приложение прервано пользователем (KeyboardInterrupt в main)")
        raise
    except Exception as e:
        logger.critical(f"💥 КРИТИЧЕСКАЯ ОШИБКА в main(): {e}", exc_info=True)
        log_crash_to_file(type(e), e, e.__traceback__, "Exception in main()")
        print(f"\n💥 Критическая ошибка: {e}")
        traceback.print_exc()
        raise

if __name__ == "__main__":
    if "--diagnostics" in sys.argv or os.getenv("NEXY_DIAG") == "voice":
        from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

        ok = VoiceRecognitionIntegration.run_dependency_check()
        sys.exit(0 if ok else 1)

    # Создаем новый event loop для главного потока
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        logger.info("="*80)
        logger.info("🚀 NEXY APPLICATION START")
        logger.info("="*80)
        logger.info("BOOT: event loop run_until_complete start")
        loop.run_until_complete(main())
        logger.info("BOOT: event loop run_until_complete finished")
    except KeyboardInterrupt:
        logger.info("⏹️ Приложение прервано пользователем (KeyboardInterrupt)")
        print("\n⏹️ Приложение прервано пользователем")
    except Exception as e:
        logger.critical(f"💥 КРИТИЧЕСКАЯ ОШИБКА в event loop: {e}", exc_info=True)
        log_crash_to_file(type(e), e, e.__traceback__, "Exception in event loop")
        print(f"\n💥 Критическая ошибка в event loop: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        logger.info("="*80)
        logger.info("🛑 NEXY APPLICATION STOP")
        logger.info("="*80)
        try:
            loop.close()
        except Exception as e:
            logger.error(f"Ошибка при закрытии event loop: {e}")
