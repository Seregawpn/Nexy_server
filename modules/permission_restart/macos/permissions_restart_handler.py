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
from modules.permission_restart.core.atomic_flag import AtomicRestartFlag
from integration.utils.resource_path import get_user_cache_dir

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
        self._last_reason: str = "unknown"
        self._last_permissions: Sequence[str] = ()
        self._config = config or PermissionRestartConfig()  # Default config if not provided
        
        # Атомарный флаг перезапуска в доступной директории (Caches вместо Application Support)
        cache_dir = get_user_cache_dir("Nexy")
        flag_path = cache_dir / "restart_completed.flag"
        self._restart_flag = AtomicRestartFlag(flag_path)

        # Разрешено ли скатываться в dev-фолбэк (перезапуск python-командой)
        if config is None and getattr(sys, "frozen", False):
            self._allow_dev_fallback = False
        else:
            self._allow_dev_fallback = bool(self._config.allow_dev_fallback)

        # Диагностический лог итоговой конфигурации
        logger.info(
            "[PERMISSION_RESTART] RestartHandler init: dry_run=%s allow_dev_fallback=%s env(NEXY_DISABLE_AUTO_RESTART)=%s ks(NEXY_KS_FIRST_RUN_RESTART)=%s",
            self._dry_run,
            self._allow_dev_fallback,
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

        self._last_reason = reason
        self._last_permissions = tuple(permissions)

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
            logger.info(
                "[PERMISSION_RESTART] Restart requested: reason=%s permissions=%s",
                self._last_reason,
                self._last_permissions,
            )

            if self._exec_current_bundle():
                return  # os.execv не возвращается при успехе

            # В dev-режиме (запуск через python main.py) предпочитаем перезапустить текущую команду
            if not getattr(sys, "frozen", False) and self._allow_dev_fallback:
                logger.info(
                    "[PERMISSION_RESTART] Dev restart path active (non-frozen build, restarting python command)"
                )
                self._launch_dev_process()
                restart_successful = True
                delay_sec = self._config.handler_launch_delay_ms / 1000.0
                logger.debug(
                    "[PERMISSION_RESTART] Sleeping %.2fs to allow dev process to boot",
                    delay_sec,
                )
                time.sleep(delay_sec)
                return

            # Пропускаем packaged app если уже знаем что он недоступен
            if not self._packaged_unavailable:
                if self._launch_packaged_app():
                    logger.info("[PERMISSION_RESTART] Packaged app launch verified (fallback)")
                    restart_successful = True
                    return
                else:
                    # Запоминаем что packaged app недоступен для следующих попыток
                    self._packaged_unavailable = True
                    logger.info(
                        "[PERMISSION_RESTART] Packaged app unavailable - will use dev fallback (bundle_path=%s)",
                        self._derive_bundle_path(),
                    )

            if not self._allow_dev_fallback:
                logger.error(
                    "[PERMISSION_RESTART] Dev fallback disabled (allow_dev_fallback=False). Restart aborted (reason=%s, permissions=%s)",
                    self._last_reason,
                    self._last_permissions,
                )
                return

            logger.info("[PERMISSION_RESTART] Restarting via dev process (python command)")
            self._launch_dev_process()
            restart_successful = True
            delay_sec = self._config.handler_launch_delay_ms / 1000.0
            logger.debug("[PERMISSION_RESTART] Sleeping %.2fs to allow dev process to boot", delay_sec)
            time.sleep(delay_sec)

        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Critical error during restart: %s", exc)
            restart_successful = False

        finally:
            if restart_successful:
                logger.info(
                    "[PERMISSION_RESTART] Exiting current process (reason=%s, permissions=%s)",
                    self._last_reason,
                    self._last_permissions,
                )
                os._exit(0)
            else:
                logger.error("[PERMISSION_RESTART] Restart failed - NOT exiting to allow fallback")
                logger.debug(
                    "[PERMISSION_RESTART] Restart failed context: packaged_unavailable=%s reason=%s permissions=%s",
                    self._packaged_unavailable,
                    self._last_reason,
                    self._last_permissions,
                )

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
            start_ts = time.time()

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
            logger.info(
                "[PERMISSION_RESTART] open -n -a returned code=%s elapsed=%.2fs",
                result.returncode,
                time.time() - start_ts,
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
            
            # КРИТИЧНО: Создаем атомарный флаг перезапуска ПЕРЕД завершением старого процесса
            # Это позволяет новому процессу обнаружить перезапуск даже если env переменные не передаются
            flag_success = self._restart_flag.write(
                reason=self._last_reason,
                permissions=list(self._last_permissions)
            )
            if flag_success:
                logger.info(
                    "[PERMISSION_RESTART] ✅ Atomic restart flag written: %s "
                    "(reason=%s, permissions=%s)",
                    self._restart_flag.flag_path,
                    self._last_reason,
                    list(self._last_permissions)
                )
            else:
                logger.warning(
                    "[PERMISSION_RESTART] ⚠️ Failed to write atomic restart flag - "
                    "new process may not detect restart"
                )

            logger.info("[PERMISSION_RESTART] Packaged app launch verified")
            return True

        except subprocess.TimeoutExpired:
            logger.error("[PERMISSION_RESTART] Launch timeout (>5 seconds) - app may not have started")
            logger.debug("[PERMISSION_RESTART] Timeout context: bundle_path=%s", bundle_path)
            return False
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Failed to relaunch packaged app: %s", exc)
            logger.debug("[PERMISSION_RESTART] Exception context: bundle_path=%s", bundle_path)
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
        
        # КРИТИЧНО: Создаем атомарный флаг перезапуска (fallback для production)
        flag_success = self._restart_flag.write(
            reason=self._last_reason,
            permissions=list(self._last_permissions)
        )
        if flag_success:
            logger.info(
                "[PERMISSION_RESTART] ✅ Atomic restart flag written: %s "
                "(reason=%s, permissions=%s)",
                self._restart_flag.flag_path,
                self._last_reason,
                list(self._last_permissions)
            )
        else:
            logger.warning(
                "[PERMISSION_RESTART] ⚠️ Failed to write atomic restart flag - "
                "will rely on env variable only"
            )

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

        current_pid = os.getpid()

        while time.time() < deadline:
            try:
                result = subprocess.run(
                    ["pgrep", "-f", executable_str],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if result.returncode == 0 and result.stdout.strip():
                    try:
                        pids = {
                            int(pid.strip())
                            for pid in result.stdout.strip().splitlines()
                            if pid.strip().isdigit()
                        }
                    except ValueError:
                        pids = set()

                    # Считаем запуск успешным только если появился новый PID,
                    # отличный от текущего процесса.
                    for pid in pids:
                        if pid != current_pid:
                            logger.debug(
                                "[PERMISSION_RESTART] Verified new process %s for %s",
                                pid,
                                executable_str,
                            )
                            return True

                    logger.debug(
                        "[PERMISSION_RESTART] pgrep matched current process only (pid=%s), waiting for new instance...",
                        current_pid,
                    )
                logger.debug(
                    "[PERMISSION_RESTART] pgrep pending (rc=%s stdout=%s)",
                    result.returncode,
                    result.stdout.strip(),
                )
            except Exception as exc:  # pragma: no cover - defensive
                logger.debug("[PERMISSION_RESTART] pgrep failed: %s", exc)
                break

            time.sleep(interval)

        logger.debug("[PERMISSION_RESTART] pgrep did not detect process for %s", executable_str)
        return False

    def _exec_current_bundle(self) -> bool:
        """Попытка перезапустить текущий PyInstaller-бандл через execve."""
        if not getattr(sys, "frozen", False):
            return False

        exe_path = Path(sys.executable).resolve()
        args = [str(exe_path), *sys.argv[1:]]

        # КРИТИЧНО: Передаём env переменную NEXY_FIRST_RUN_RESTARTED для нового процесса
        # Это позволяет FirstRunPermissionsIntegration обнаружить завершённый рестарт
        env = os.environ.copy()
        env["NEXY_FIRST_RUN_RESTARTED"] = "1"
        
        # КРИТИЧНО: Создаем атомарный флаг перезапуска (fallback для production)
        flag_success = self._restart_flag.write(
            reason=self._last_reason,
            permissions=list(self._last_permissions)
        )
        if flag_success:
            logger.info(
                "[PERMISSION_RESTART] ✅ Atomic restart flag written: %s "
                "(reason=%s, permissions=%s)",
                self._restart_flag.flag_path,
                self._last_reason,
                list(self._last_permissions)
            )
        else:
            logger.warning(
                "[PERMISSION_RESTART] ⚠️ Failed to write atomic restart flag - "
                "will rely on env variable only"
            )

        try:
            logger.info("[PERMISSION_RESTART] Restarting current bundle via execve (%s)", exe_path)
            logger.info("[PERMISSION_RESTART] Setting NEXY_FIRST_RUN_RESTARTED=1 for new process")
            os.execve(str(exe_path), args, env)
            # execve не возвращается при успехе - процесс заменяется
            # Эта строка недостижима, но нужна для type checker
        except Exception as exc:  # pragma: no cover - defensive
            logger.error("[PERMISSION_RESTART] execve failed: %s", exc)

        return False
