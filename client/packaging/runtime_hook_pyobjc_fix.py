"""
PyInstaller runtime hook ensuring AppKit symbols are available in Foundation
before any PyObjC-based modules (e.g. rumps) are imported.

КРИТИЧНО: Этот hook выполняется ДО всех импортов rumps и является единственным
источником истины для PyObjC-fix в упакованном .app bundle.

В dev-режиме (не frozen) фикс применяется в main.py как fallback.

ВАЖНО: Этот hook применяет фикс НАПРЯМУЮ, без зависимости от logger или других модулей,
чтобы гарантировать раннее выполнение до любых импортов.
"""

import os
import sys
import tempfile


def _log_to_file(message: str):
    """Логирует сообщение в файл для подтверждения выполнения hook."""
    try:
        log_file = os.path.join(tempfile.gettempdir(), "nexy_pyobjc_fix.log")
        with open(log_file, "a", encoding="utf-8") as f:
            from datetime import datetime

            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
    except Exception:
        pass  # Игнорируем ошибки логирования


def _apply_fix():
    """
    Применяет PyObjC fix для упакованных приложений.

    КРИТИЧНО: Выполняется ДО всех импортов rumps через PyInstaller runtime hook.
    Это единственный источник истины для PyObjC-fix в упакованном .app.

    Применяет фикс НАПРЯМУЮ, без зависимости от других модулей.
    """
    try:
        # Проверяем, что мы на macOS
        if sys.platform != "darwin":
            return

        msg = "[NEXY_INIT] Applying PyObjC Foundation fix (runtime hook)..."
        sys.stderr.write(f"{msg}\n")
        sys.stderr.flush()
        _log_to_file(msg)

        # Импортируем AppKit первым (здесь находится настоящий NSMakeRect)
        import AppKit

        # Импортируем Foundation
        import Foundation

        # Применяем фикс для всех проблемных символов.
        # ВАЖНО: не используем hasattr(Foundation, symbol), чтобы не триггерить
        # dlsym lookup noise ("cannot find symbol ... in Foundation").
        symbols_to_fix = ["NSMakeRect", "NSMakePoint", "NSMakeSize", "NSMakeRange"]
        fixed_symbols: list[str] = []

        for symbol in symbols_to_fix:
            appkit_symbol = getattr(AppKit, symbol, None)
            if appkit_symbol is not None:
                setattr(Foundation, symbol, appkit_symbol)
                fixed_symbols.append(symbol)

        if fixed_symbols:
            success_msg = f"[NEXY_INIT] SUCCESS: Fixed symbols: {', '.join(fixed_symbols)}"
            sys.stderr.write(f"{success_msg}\n")
            sys.stderr.flush()
            _log_to_file(f"SUCCESS: fixed_inline:{','.join(fixed_symbols)}")
        else:
            info_msg = "[NEXY_INIT] INFO: All symbols already present in Foundation"
            sys.stderr.write(f"{info_msg}\n")
            sys.stderr.flush()
            _log_to_file("INFO: symbols_already_present")

    except ImportError as e:
        error_msg = f"[NEXY_INIT] ERROR: PyObjC not available: {e}"
        sys.stderr.write(f"{error_msg}\n")
        sys.stderr.flush()
        _log_to_file(f"ERROR: import_error:{e}")
    except Exception as exc:
        error_msg = f"[NEXY_INIT] ERROR: Failed to apply PyObjC Foundation fix: {exc}"
        sys.stderr.write(f"{error_msg}\n")
        sys.stderr.flush()
        _log_to_file(f"ERROR: error:{exc}")


def _activate_nsapplication():
    """
    CRITICAL: Activate NSApplication for LSUIElement applications.

    Эта активация происходит РАНО (в runtime hook) для .app bundle.
    Это необходимо для создания NSApplication instance до импорта rumps.

    ВАЖНО: Задержка для ControlCenter происходит ПОЗЖЕ в main.py (2 сек),
    перед app.run(). Здесь мы только создаем NSApplication и устанавливаем policy.
    """
    import sys

    try:
        sys.stderr.write("[NEXY_INIT] Activating NSApplication for menu bar app...\n")
        sys.stderr.flush()
        import AppKit

        app = AppKit.NSApplication.sharedApplication()  # type: ignore[reportAttributeAccessIssue]
        # NSApplicationActivationPolicyAccessory (hide from Dock, show in menu bar)
        app.setActivationPolicy_(AppKit.NSApplicationActivationPolicyAccessory)  # type: ignore[reportAttributeAccessIssue]
        # Не делаем force activate в runtime hook: это вызывает focus stealing.
        # Управление foreground-фокусом централизовано в main.py через focus policy.
        sys.stderr.write("[NEXY_INIT] SUCCESS: NSApplication prepared (no force activate)\n")
        sys.stderr.flush()
    except Exception as e:
        sys.stderr.write(f"[NEXY_INIT] ERROR: NSApplication activation failed: {e}\n")
        sys.stderr.flush()


_apply_fix()
_activate_nsapplication()
