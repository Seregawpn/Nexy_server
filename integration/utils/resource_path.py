"""
Resource Path Resolver для Nexy на macOS.
Гарантирует корректное определение путей к ресурсам в dev-режиме
и внутри упакованного .app (Resources/… либо Frameworks/…).
"""

import sys
import os
from pathlib import Path
from typing import Optional


def get_resource_path(relative_path: str) -> Path:
    """
    Получить абсолютный путь к ресурсу для любого режима запуска.

    Поддерживаемые режимы:
    1. Dev mode (запуск из исходников)
    2. PyInstaller onefile (_MEIPASS)
    3. PyInstaller bundle (.app)
    4. Installed app (/Applications/Nexy.app)
    """

    if hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
        candidate = base_path / relative_path
        if candidate.exists():
            return candidate

    if getattr(sys, "frozen", False):
        exe_path = Path(sys.executable).resolve()
        contents_dir = exe_path.parent.parent

        candidate = contents_dir / "Resources" / relative_path
        if candidate.exists():
            return candidate

        candidate = contents_dir / "Frameworks" / relative_path
        if candidate.exists():
            return candidate

    # Dev mode
    main_module = sys.modules.get("__main__")
    if main_module and getattr(main_module, "__file__", None):
        project_root = Path(main_module.__file__).resolve().parent
        candidate = project_root / relative_path
        if candidate.exists():
            return candidate

    candidate = Path.cwd() / relative_path
    if candidate.exists():
        return candidate

    return Path(relative_path)


def get_user_data_dir(app_name: str = "Nexy") -> Path:
    data_dir = Path.home() / "Library" / "Application Support" / app_name
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def get_user_cache_dir(app_name: str = "Nexy") -> Path:
    cache_dir = Path.home() / "Library" / "Caches" / app_name
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


def get_user_logs_dir(app_name: str = "Nexy") -> Path:
    logs_dir = Path.home() / "Library" / "Logs" / app_name
    logs_dir.mkdir(parents=True, exist_ok=True)
    return logs_dir


def get_launch_agent_path(bundle_id: str = "com.nexy.assistant") -> Path:
    return Path.home() / "Library" / "LaunchAgents" / f"{bundle_id}.plist"


def resource_path(relative_path: str) -> str:
    return str(get_resource_path(relative_path))
