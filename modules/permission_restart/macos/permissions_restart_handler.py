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
from modules.permission_restart.core.config import PermissionRestartConfig

logger = logging.getLogger(__name__)


class PermissionsRestartHandler:
    """
    Relaunches the Nexy client after critical permissions become available.

    Behaviour:
    - Production / packaged build: launch bundled Nexy.app via `open -a`.
    - Development (no Nexy.app): restart the current Python command.
    """

    def __init__(
        self,
        *,
        dry_run: Optional[bool] = None,
        config: Optional[PermissionRestartConfig] = None,
    ):
        env_flag = os.environ.get("NEXY_DISABLE_AUTO_RESTART")
        kill_switch = os.environ.get("NEXY_KS_FIRST_RUN_RESTART")

        if dry_run is None:
            dry_run = bool(env_flag) and env_flag.strip().lower() in {"1", "true", "yes"}

        # Kill-switch для emergency отключения restart механизма
        if kill_switch and kill_switch.strip().lower() in {"1", "true", "yes"}:
            logger.warning("[PERMISSION_RESTART] Kill-switch active (NEXY_KS_FIRST_RUN_RESTART) - disabling restart")
            dry_run = True

        self._dry_run = bool(dry_run)
        self._packaged_unavailable = False  # Флаг что .app бандл недоступен (для избежания повторных попыток)
        self._config = config or PermissionRestartConfig()  # Default config if not provided

        # Диагностический лог итоговой конфигурации
        logger.info(
            "[PERMISSION_RESTART] RestartHandler init: dry_run=%s env(NEXY_DISABLE_AUTO_RESTART)=%s ks(NEXY_KS_FIRST_RUN_RESTART)=%s",
            self._dry_run,
            env_flag,
            kill_switch,
        )

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
            logger.debug(
                "[PERMISSION_RESTART] _perform_restart start (packaged_unavailable=%s)",
                self._packaged_unavailable,
            )

            if self._exec_current_bundle():
                return  # os.execv не возвращается при успехе

            # Пропускаем packaged app если уже знаем что он недоступен
            if not self._packaged_unavailable:
                if self._launch_packaged_app():
                    logger.info("[PERMISSION_RESTART] Packaged app launch verified (fallback)")
                    restart_successful = True
                    return
                else:
                    # Запоминаем что packaged app недоступен для следующих попыток
                    self._packaged_unavailable = True
                    logger.info("[PERMISSION_RESTART] Packaged app unavailable - will use dev fallback")

            logger.info("[PERMISSION_RESTART] Restarting via dev process (python command)")
            self._launch_dev_process()
            restart_successful = True
            delay_sec = self._config.handler_launch_delay_ms / 1000.0
            time.sleep(delay_sec)

        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Critical error during restart: %s", exc)
            restart_successful = False

        finally:
            if restart_successful:
                logger.info("[PERMISSION_RESTART] Exiting current process (new process should be running)")
                os._exit(0)
            else:
                logger.error("[PERMISSION_RESTART] Restart failed - NOT exiting to allow fallback")

    def _launch_packaged_app(self) -> bool:
        """
        Try to relaunch a packaged Nexy.app. Returns True on success,
        False when we should fall back to dev mode.

        Uses `open -n -a` and verifies the spawned process via `pgrep`.
        """
        bundle_path = self._derive_bundle_path()
        if bundle_path is None:
            logger.debug("[PERMISSION_RESTART] Unable to determine Nexy.app bundle path")
            return False

        try:
            logger.info("[PERMISSION_RESTART] Relaunching packaged app at %s", bundle_path)

            # Запускаем новый экземпляр Nexy.app напрямую.
            # Ранее использовался флаг -W (wait-apps), из-за чего команда `open`
            # блокировала выполнение до закрытия нового процесса и регулярно
            # завершалась по таймауту. Это приводило к тому, что перезапуск
            # распознавался как неуспешный и текущий процесс не завершался.
            result = subprocess.run(
                ["/usr/bin/open", "-n", "-a", str(bundle_path)],
                check=False,  # Не падаем на non-zero exit code
                timeout=5.0,
                capture_output=True,
                text=True,
            )

            # Проверяем exit code
            if result.returncode != 0:
                stderr = result.stderr.strip() if result.stderr else ""
                logger.error(
                    "[PERMISSION_RESTART] open command failed (exit_code=%d, stderr=%s)",
                    result.returncode,
                    stderr
                )
                # Специальная обработка kLSNoExecutableErr (10810) - нет исполняемого файла в bundle
                if "10810" in stderr or "kLSNoExecutableErr" in stderr:
                    logger.error(
                        "[PERMISSION_RESTART] Bundle missing executable (kLSNoExecutableErr) - "
                        "check packaging/build_final.sh creates Contents/MacOS/Nexy"
                    )
                    self._packaged_unavailable = True
                return False

            if not self._verify_app_launched(bundle_path):
                logger.error("[PERMISSION_RESTART] Unable to verify launched process for %s", bundle_path)
                return False

            # Даём дополнительное время для PyInstaller unpacking и инициализации
            grace_sec = self._config.packaged_launch_grace_ms / 1000.0
            time.sleep(grace_sec)

            logger.info("[PERMISSION_RESTART] Packaged app launch verified")
            return True

        except subprocess.TimeoutExpired:
            logger.error("[PERMISSION_RESTART] Launch timeout (>5 seconds) - app may not have started")
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

        # КРИТИЧНО: Передаём env переменную NEXY_FIRST_RUN_RESTARTED для нового процесса
        # Это позволяет FirstRunPermissionsIntegration обнаружить завершённый рестарт
        # даже если флаг restart_completed.flag не создался из-за PermissionError
        env = os.environ.copy()
        env["NEXY_FIRST_RUN_RESTARTED"] = "1"

        logger.info("[PERMISSION_RESTART] Launching dev process: %s (cwd=%s)", cmd, cwd)
        logger.info("[PERMISSION_RESTART] Setting NEXY_FIRST_RUN_RESTARTED=1 for new process")

        try:
            subprocess.Popen(cmd, cwd=cwd, env=env)
            logger.info("[PERMISSION_RESTART] Dev process launched with restart env flag")
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
        executable_dir = bundle_path / "Contents" / "MacOS"
        if not executable_dir.exists():
            logger.debug("[PERMISSION_RESTART] Executable directory missing: %s", executable_dir)
            return False

        candidate = executable_dir / bundle_path.stem
        if not candidate.exists():
            binaries = list(executable_dir.glob("*"))
            if not binaries:
                logger.debug("[PERMISSION_RESTART] No binaries found in %s", executable_dir)
                return False
            candidate = binaries[0]

        executable_str = str(candidate)
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

    def _exec_current_bundle(self) -> bool:
        """Попытка перезапустить текущий PyInstaller-бандл через execv."""
        if not getattr(sys, "frozen", False):
            return False

        exe_path = Path(sys.executable).resolve()
        args = [str(exe_path), *sys.argv[1:]]
        try:
            logger.info("[PERMISSION_RESTART] Restarting current bundle via execv (%s)", exe_path)
            os.execv(str(exe_path), args)
            # execv не возвращается при успехе - процесс заменяется
            # Эта строка недостижима, но нужна для type checker
        except Exception as exc:  # pragma: no cover - defensive
            logger.error("[PERMISSION_RESTART] execv failed: %s", exc)

        return False
