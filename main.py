"""
Nexy AI Assistant - Главный файл приложения
Только точка входа и инициализация SimpleModuleCoordinator
"""

import asyncio
import logging
import os
import sys
from pathlib import Path

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

# Выполняем инициализацию до импортов модулей, использующих pydub
init_ffmpeg_for_pydub()

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
        Foundation.NSMakeRect = AppKit.NSMakeRect
        Foundation.NSMakePoint = AppKit.NSMakePoint
        Foundation.NSMakeSize = AppKit.NSMakeSize
        Foundation.NSMakeRange = AppKit.NSMakeRange
        print("✅ AppKit символы успешно скопированы в Foundation")
    else:
        print("⚠️ AppKit.NSMakeRect не найден")

    # CRITICAL: Activate NSApplication for LSUIElement applications
    # Without this, menu bar icon doesn't appear when launched from .app on macOS Sequoia
    # Must be called BEFORE creating rumps.App and NSStatusItem
    try:
        print("[NEXY_INIT] Activating NSApplication for menu bar app...")
        app = AppKit.NSApplication.sharedApplication()
        print(f"[NEXY_INIT] NSApplication instance: {app}")
        print(f"[NEXY_INIT] Current activation policy: {app.activationPolicy()}")

        # Set activation policy for menu bar application
        # NSApplicationActivationPolicyAccessory (hide from Dock, show in menu bar)
        result = app.setActivationPolicy_(AppKit.NSApplicationActivationPolicyAccessory)
        print(f"[NEXY_INIT] setActivationPolicy(Accessory) returned: {result}")
        print(f"[NEXY_INIT] New activation policy: {app.activationPolicy()}")

        # Активируем приложение - ВАЖНО: True заставляет приложение стать активным
        app.activateIgnoringOtherApps_(True)
        print("[NEXY_INIT] Called activateIgnoringOtherApps_(True)")

        print("[NEXY_INIT] SUCCESS: NSApplication activated for menu bar app")
    except Exception as e:
        print(f"[NEXY_INIT] ERROR: NSApplication activation failed: {e}")
        import traceback
        traceback.print_exc()

except ImportError as e:
    print(f"⚠️ PyObjC недоступен: {e}")
except Exception as e:
    print(f"⚠️ Ошибка инициализации PyObjC: {e}")

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

logger = logging.getLogger(__name__)
logger.info(f"📝 Логи записываются в: {log_file}")
print(f"📝 Логи записываются в: {log_file}")

async def main():
    """Главная функция"""
    try:
        # Импортируем SimpleModuleCoordinator
        from integration.core.simple_module_coordinator import SimpleModuleCoordinator
        
        # Создаем координатор
        coordinator = SimpleModuleCoordinator()
        
        # Запускаем (run() сам вызовет initialize() и проверку дублирования)
        await coordinator.run()                                                         
        
    except Exception as e:
        print(f"💥 Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if "--diagnostics" in sys.argv or os.getenv("NEXY_DIAG") == "voice":
        from integration.integrations.voice_recognition_integration import VoiceRecognitionIntegration

        ok = VoiceRecognitionIntegration.run_dependency_check()
        sys.exit(0 if ok else 1)

    # Создаем новый event loop для главного потока
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n⏹️ Приложение прервано пользователем")
    finally:
        loop.close()