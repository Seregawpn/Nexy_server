"""
Resource Path Resolver для Nexy на macOS.
Гарантирует корректное определение путей к ресурсам в dev-режиме
и внутри упакованного .app (Resources/… либо Frameworks/…).
"""

import os
from pathlib import Path
import sys

from integration.utils.env_detection import is_production_env

# Глобальный кэш для стабильности пути user data directory
# КРИТИЧНО: Гарантирует что все вызовы get_user_data_dir() возвращают один и тот же путь
_USER_DATA_DIR_CACHE = None


def _resolve_app_name(app_name: str) -> str:
    """
    Resolve app data name with optional overrides for dev/test isolation.
    Env priority:
    - NEXY_APP_NAME (explicit full name)
    - NEXY_APP_DATA_SUFFIX (appended with dash)
    """
    explicit = os.environ.get("NEXY_APP_NAME")
    if explicit:
        if is_production_env():
            import logging
            logging.getLogger(__name__).warning(
                "[RESOURCE_PATH] NEXY_APP_NAME override used in production: %s",
                explicit,
            )
        return explicit
        
    # Validating environment: if not frozen (Dev), default to AppName-Dev
    is_frozen = getattr(sys, "frozen", False)
    suffix = os.environ.get("NEXY_APP_DATA_SUFFIX")
    
    if not is_frozen:
        # Dev mode: use suffix or default to "Dev"
        if suffix and is_production_env():
            import logging
            logging.getLogger(__name__).warning(
                "[RESOURCE_PATH] NEXY_APP_DATA_SUFFIX override used in production: %s",
                suffix,
            )
        return f"{app_name}-{suffix or 'Dev'}"
    
    # Prod mode: use suffix only if explicitly set
    if suffix:
        if is_production_env():
            import logging
            logging.getLogger(__name__).warning(
                "[RESOURCE_PATH] NEXY_APP_DATA_SUFFIX override used in production: %s",
                suffix,
            )
        return f"{app_name}-{suffix}"
    return app_name


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
        base_path = Path(sys._MEIPASS)  # type: ignore[reportAttributeAccessIssue, reportArgumentType]
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
        project_root = Path(str(main_module.__file__)).resolve().parent
        candidate = project_root / relative_path
        if candidate.exists():
            return candidate

    candidate = Path.cwd() / relative_path
    if candidate.exists():
        return candidate

    return Path(relative_path)


def get_user_data_dir(app_name: str = "Nexy") -> Path:
    """
    Получить путь к пользовательской директории данных с поддержкой sandbox.

    Пытается создать директорию в следующем порядке:
    1. ~/Library/Application Support/{app_name} (стандартный путь)
    2. ~/Library/Containers/{bundle_id}/Data/Library/Application Support/{app_name} (sandbox)
    3. /tmp/{app_name} (последний fallback)

    КРИТИЧНО: Кэширует результат в _USER_DATA_DIR_CACHE для гарантии стабильности пути.

    Raises:
        RuntimeError: Если не удалось создать ни одну из директорий
    """
    import logging
    logger = logging.getLogger(__name__)

    # КРИТИЧНО: Кэшируем путь чтобы всегда возвращать один и тот же
    global _USER_DATA_DIR_CACHE
    if _USER_DATA_DIR_CACHE is not None:
        logger.debug(f"Using cached user data dir: {_USER_DATA_DIR_CACHE}")
        return _USER_DATA_DIR_CACHE

    app_name = _resolve_app_name(app_name)

    # Попытка 1: Стандартный путь
    data_dir = Path.home() / "Library" / "Application Support" / app_name
    try:
        data_dir.mkdir(parents=True, exist_ok=True)
        # Проверяем возможность записи
        test_file = data_dir / ".write_test"
        test_file.touch()
        test_file.unlink()
        logger.info(f"✅ Using standard user data directory: {data_dir}")
        _USER_DATA_DIR_CACHE = data_dir  # type: ignore[reportConstantRedefinition]
        return data_dir
    except (PermissionError, OSError) as e:
        logger.warning(f"Cannot write to {data_dir}: {e}, trying sandbox path...")

    # Попытка 2: Sandbox container (определяем bundle_id из окружения или используем дефолтный)
    bundle_id = os.environ.get("APP_BUNDLE_ID", "com.nexy.assistant")
    sandbox_dir = Path.home() / "Library" / "Containers" / bundle_id / "Data" / "Library" / "Application Support" / app_name
    try:
        sandbox_dir.mkdir(parents=True, exist_ok=True)
        # Проверяем возможность записи
        test_file = sandbox_dir / ".write_test"
        test_file.touch()
        test_file.unlink()
        logger.warning(f"⚠️ Using sandbox data directory: {sandbox_dir}")
        _USER_DATA_DIR_CACHE = sandbox_dir  # type: ignore[reportConstantRedefinition]
        return sandbox_dir
    except (PermissionError, OSError) as e:
        logger.warning(f"Cannot write to sandbox {sandbox_dir}: {e}, trying /tmp fallback...")

    # Попытка 3: /tmp fallback (последняя надежда)
    tmp_dir = Path("/tmp") / app_name
    try:
        tmp_dir.mkdir(parents=True, exist_ok=True)
        logger.error(f"🚨 CRITICAL: Using temporary data directory: {tmp_dir} - flags will be lost on reboot!")
        _USER_DATA_DIR_CACHE = tmp_dir  # type: ignore[reportConstantRedefinition]
        return tmp_dir
    except (PermissionError, OSError) as e:
        logger.error(f"Cannot write to /tmp: {e}")
        raise RuntimeError(
            f"Failed to create user data directory. Tried:\n"
            f"1. {data_dir}\n"
            f"2. {sandbox_dir}\n"
            f"3. {tmp_dir}\n"
            f"All paths are not writable. Check file permissions and sandbox entitlements."
        ) from e


def get_user_cache_dir(app_name: str = "Nexy") -> Path:
    """
    Получить путь к директории кэша с поддержкой sandbox.

    Аналогично get_user_data_dir, пытается создать в стандартном пути,
    затем в sandbox container, затем в /tmp.
    """
    import logging
    logger = logging.getLogger(__name__)

    app_name = _resolve_app_name(app_name)

    # Попытка 1: Стандартный путь
    cache_dir = Path.home() / "Library" / "Caches" / app_name
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        test_file = cache_dir / ".write_test"
        test_file.touch()
        test_file.unlink()
        return cache_dir
    except (PermissionError, OSError):
        pass

    # Попытка 2: Sandbox
    bundle_id = os.environ.get("APP_BUNDLE_ID", "com.nexy.assistant")
    sandbox_dir = Path.home() / "Library" / "Containers" / bundle_id / "Data" / "Library" / "Caches" / app_name
    try:
        sandbox_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Using sandbox cache directory: {sandbox_dir}")
        return sandbox_dir
    except (PermissionError, OSError):
        pass

    # Попытка 3: /tmp fallback
    tmp_dir = Path("/tmp") / f"{app_name}_cache"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    logger.warning(f"Using temporary cache directory: {tmp_dir}")
    return tmp_dir


def get_user_logs_dir(app_name: str = "Nexy") -> Path:
    """
    Получить путь к директории логов с поддержкой sandbox.

    Аналогично get_user_data_dir, пытается создать в стандартном пути,
    затем в sandbox container, затем в /tmp.
    """
    import logging
    logger = logging.getLogger(__name__)

    app_name = _resolve_app_name(app_name)

    # Попытка 1: Стандартный путь
    logs_dir = Path.home() / "Library" / "Logs" / app_name
    try:
        logs_dir.mkdir(parents=True, exist_ok=True)
        test_file = logs_dir / ".write_test"
        test_file.touch()
        test_file.unlink()
        return logs_dir
    except (PermissionError, OSError):
        pass

    # Попытка 2: Sandbox
    bundle_id = os.environ.get("APP_BUNDLE_ID", "com.nexy.assistant")
    sandbox_dir = Path.home() / "Library" / "Containers" / bundle_id / "Data" / "Library" / "Logs" / app_name
    try:
        sandbox_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Using sandbox logs directory: {sandbox_dir}")
        return sandbox_dir
    except (PermissionError, OSError):
        pass

    # Попытка 3: /tmp fallback
    tmp_dir = Path("/tmp") / f"{app_name}_logs"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    logger.warning(f"Using temporary logs directory: {tmp_dir}")
    return tmp_dir


def get_launch_agent_path(bundle_id: str = "com.nexy.assistant") -> Path:
    return Path.home() / "Library" / "LaunchAgents" / f"{bundle_id}.plist"


def resource_path(relative_path: str) -> str:
    return str(get_resource_path(relative_path))
