"""
Restart helper for the permission flow that mirrors the updater behaviour
but adds a development fallback when the packaged .app is unavailable.
"""

from __future__ import annotations

import asyncio
import logging
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional, Sequence

from modules.updater.migrate import get_user_app_path

logger = logging.getLogger(__name__)


class PermissionsRestartHandler:
    """
    Relaunches the Nexy client after critical permissions become available.

    Behaviour:
    - Production / packaged build: launch bundled Nexy.app via `open -a`.
    - Development (no Nexy.app): restart the current Python command.
    """

    def __init__(self, *, dry_run: Optional[bool] = None):
        env_flag = os.environ.get("NEXY_DISABLE_AUTO_RESTART")
        kill_switch = os.environ.get("NEXY_KS_FIRST_RUN_RESTART")

        if dry_run is None:
            dry_run = bool(env_flag) and env_flag.strip().lower() in {"1", "true", "yes"}

        # Kill-switch для emergency отключения restart механизма
        if kill_switch and kill_switch.strip().lower() in {"1", "true", "yes"}:
            logger.warning("[PERMISSION_RESTART] Kill-switch active (NEXY_KS_FIRST_RUN_RESTART) - disabling restart")
            dry_run = True

        self._dry_run = bool(dry_run)

    async def trigger_restart(self, *, reason: str, permissions: Sequence[str]) -> bool:
        """Kick off the relaunch flow. Returns False in dry-run mode."""

        if self._dry_run:
            logger.info(
                "[PERMISSION_RESTART] Dry-run enabled, skipping restart (reason=%s, permissions=%s)",
                reason,
                list(permissions),
            )
            return False

        logger.info(
            "[PERMISSION_RESTART] Restart requested (reason=%s, permissions=%s)",
            reason,
            list(permissions),
        )

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._perform_restart)
        return True

    def _perform_restart(self) -> None:
        """Blocking part executed in a worker thread."""
        restart_successful = False

        try:
            if self._launch_packaged_app():
                logger.info("[PERMISSION_RESTART] Packaged app launched successfully")
                restart_successful = True
                # Даём новому процессу время запуститься перед завершением текущего
                time.sleep(2.0)
                return

            logger.info("[PERMISSION_RESTART] Packaged app not available, restarting current command")
            self._launch_dev_process()
            restart_successful = True
            # Даём dev процессу время запуститься
            time.sleep(1.0)

        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Critical error during restart: %s", exc)
            restart_successful = False

        finally:
            if restart_successful:
                logger.info("[PERMISSION_RESTART] Exiting current process (new process should be running)")
                os._exit(0)
            else:
                logger.error("[PERMISSION_RESTART] Restart failed - NOT exiting to allow fallback")
                # НЕ вызываем os._exit(0) если перезапуск не удался

    def _launch_packaged_app(self) -> bool:
        """
        Try to relaunch a packaged Nexy.app. Returns True on success,
        False when we should fall back to dev mode.

        Uses 'open -W' to wait for the application to launch before returning.
        """
        bundle_path = self._derive_bundle_path()
        if bundle_path is None:
            logger.debug("[PERMISSION_RESTART] Unable to determine Nexy.app bundle path")
            return False

        try:
            logger.info("[PERMISSION_RESTART] Relaunching packaged app at %s", bundle_path)

            # КРИТИЧНО: Используем -W (--wait-apps) для ожидания запуска приложения
            # Это блокирует выполнение пока приложение не откроется
            result = subprocess.run(
                ["/usr/bin/open", "-n", "-W", "-a", str(bundle_path)],
                check=False,  # Не падаем на non-zero exit code
                timeout=10.0,  # Увеличенный timeout для PyInstaller unpacking
                capture_output=True,
                text=True,
            )

            # Проверяем exit code
            if result.returncode != 0:
                logger.error(
                    "[PERMISSION_RESTART] open command failed (exit_code=%d, stderr=%s)",
                    result.returncode,
                    result.stderr.strip() if result.stderr else "no stderr"
                )
                return False

            if not self._verify_app_launched(bundle_path):
                logger.error("[PERMISSION_RESTART] Unable to verify launched process for %s", bundle_path)
                return False

            # Даём дополнительное время для PyInstaller unpacking и инициализации
            time.sleep(3.0)

            logger.info("[PERMISSION_RESTART] Packaged app launch verified")
            return True

        except subprocess.TimeoutExpired:
            logger.error("[PERMISSION_RESTART] Launch timeout (>10 seconds) - app may not have started")
            return False
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Failed to relaunch packaged app: %s", exc)
            return False

    def _launch_dev_process(self) -> None:
        """Restart the current Python command (development mode)."""
        python_executable = sys.executable or "python3"
        argv = sys.argv or []

        if not argv:
            logger.warning("[PERMISSION_RESTART] sys.argv empty, nothing to relaunch")
            return

        cmd = [python_executable] + argv
        cwd = os.getcwd()

        logger.info("[PERMISSION_RESTART] Launching dev process: %s (cwd=%s)", cmd, cwd)
        try:
            subprocess.Popen(cmd, cwd=cwd)
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Failed to relaunch dev process: %s", exc)

    @property
    def dry_run(self) -> bool:
        return self._dry_run

    def _derive_bundle_path(self) -> Optional[Path]:
        """
        Определяем путь к Nexy.app.

        1. Если запущено из PyInstaller bundle — поднимаемся от sys.executable к .app
        2. Фолбэк: get_user_app_path() (обычно /Applications/Nexy.app)
        """
        # 1. Попытка взять путь из текущего исполняемого файла
        try:
            if getattr(sys, "frozen", False):
                exe_path = Path(sys.executable).resolve()
                bundle_path = exe_path.parent.parent.parent  # .../Nexy.app
                if bundle_path.exists() and bundle_path.suffix == ".app":
                    return bundle_path
        except Exception as exc:  # pragma: no cover - defensive
            logger.debug("[PERMISSION_RESTART] Unable to derive bundle path from sys.executable: %s", exc)

        # 2. Фолбэк на конфигурационный путь
        try:
            fallback_path = Path(get_user_app_path())
            if fallback_path.exists():
                return fallback_path
        except Exception as exc:
            logger.debug("[PERMISSION_RESTART] get_user_app_path() failed: %s", exc)

        return None

    def _verify_app_launched(self, bundle_path: Path, timeout: float = 5.0, interval: float = 0.5) -> bool:
        """
        Проверяем, что стартовал новый процесс приложения.

        Используем pgrep -f с путём к бинарнику в Contents/MacOS.
        """
        executable = (bundle_path / "Contents" / "MacOS")
        if not executable.exists():
            logger.debug("[PERMISSION_RESTART] Executable directory missing: %s", executable)
            return False

        executable_str = str(executable)
        deadline = time.time() + timeout

        while time.time() < deadline:
            try:
                result = subprocess.run(
                    ["pgrep", "-f", executable_str],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if result.returncode == 0 and result.stdout.strip():
                    logger.debug("[PERMISSION_RESTART] Verified process launched for %s", executable_str)
                    return True
            except Exception as exc:  # pragma: no cover - defensive
                logger.debug("[PERMISSION_RESTART] pgrep failed: %s", exc)
                break

            time.sleep(interval)

        logger.debug("[PERMISSION_RESTART] pgrep did not detect process for %s", executable_str)
        return False
