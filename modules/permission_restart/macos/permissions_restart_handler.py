"""
Restart helper for the permission flow that mirrors the updater behaviour
but adds a development fallback when the packaged .app is unavailable.
"""

from __future__ import annotations

import asyncio
import logging
import os
import shlex
import subprocess
import sys
import textwrap
import time
from pathlib import Path
from typing import Dict, Optional, Sequence

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

            # ПРИОРИТЕТ 1: Полное закрытие/открытие для packaged .app
            if not self._packaged_unavailable:
                if self._launch_packaged_app():
                    logger.info("[PERMISSION_RESTART] Packaged app launch verified (full restart)")
                    restart_successful = True
                    return
                else:
                    self._packaged_unavailable = True
                    logger.info(
                        "[PERMISSION_RESTART] Packaged app unavailable - will use execve fallback (bundle_path=%s)",
                        self._derive_bundle_path(),
                    )

            # ПРИОРИТЕТ 2: os.execve() как fallback (только для PyInstaller bundle)
            if getattr(sys, "frozen", False) and self._exec_current_bundle():
                return  # os.execv не возвращается при успехе

            # ПРИОРИТЕТ 3: Dev fallback (запуск через python main.py)
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

        Schedules a lightweight helper that waits for the current PID to exit
        before invoking `open -n -a`, which prevents Control Center races.
        """
        bundle_path = self._derive_bundle_path()
        if bundle_path is None:
            logger.debug("[PERMISSION_RESTART] Unable to determine Nexy.app bundle path")
            self._packaged_unavailable = True
            return False
        if not bundle_path.exists():
            logger.debug("[PERMISSION_RESTART] Bundle path does not exist: %s", bundle_path)
            self._packaged_unavailable = True
            return False

        try:
            verify_target = self._resolve_bundle_binary_path(bundle_path)
            post_delay = max(0.0, self._config.packaged_launch_grace_ms / 1000.0)

            helper_started = self._spawn_delayed_launch_helper(
                command=["/usr/bin/open", "-n", "-a", str(bundle_path)],
                env=None,
                label="packaged",
                timeout_sec=self._config.graceful_shutdown_timeout_sec,
                poll_interval_sec=self._config.graceful_shutdown_poll_interval_sec,
                post_exit_delay_sec=post_delay,
                verification_target=verify_target,
            )

            if not helper_started:
                logger.error("[PERMISSION_RESTART] Failed to schedule packaged relaunch helper")
                return False

            self._persist_restart_signal()
            logger.info(
                "[PERMISSION_RESTART] Scheduled delayed packaged relaunch (bundle=%s, delay=%.2fs)",
                bundle_path,
                post_delay,
            )
            return True

        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Failed to schedule packaged relaunch: %s", exc)
            logger.debug("[PERMISSION_RESTART] Exception context: bundle_path=%s", bundle_path)
            return False

    def _persist_restart_signal(self) -> None:
        flag_success = self._restart_flag.write(
            reason=self._last_reason,
            permissions=list(self._last_permissions),
        )
        if flag_success:
            logger.info(
                "[PERMISSION_RESTART] ✅ Atomic restart flag written: %s (reason=%s, permissions=%s)",
                self._restart_flag.flag_path,
                self._last_reason,
                list(self._last_permissions),
            )
        else:
            logger.warning(
                "[PERMISSION_RESTART] ⚠️ Failed to write atomic restart flag - "
                "new process may not detect restart"
            )

    def _resolve_bundle_binary_path(self, bundle_path: Path) -> Optional[str]:
        executable_dir = bundle_path / "Contents" / "MacOS"
        if not executable_dir.exists():
            return None

        candidate = executable_dir / bundle_path.stem
        if candidate.exists():
            return str(candidate)

        binaries = sorted(executable_dir.glob("*"))
        if not binaries:
            return None
        return str(binaries[0])

    def _spawn_delayed_launch_helper(
        self,
        *,
        command: Sequence[str],
        env: Optional[Dict[str, str]],
        label: str,
        timeout_sec: float,
        poll_interval_sec: float,
        post_exit_delay_sec: float,
        verification_target: Optional[str],
    ) -> bool:
        if not command:
            return False

        target_pid = os.getpid()
        timeout_s = max(1, int(round(timeout_sec)))
        poll_interval = max(0.05, float(poll_interval_sec))
        post_delay = max(0.0, float(post_exit_delay_sec))
        verify_timeout = max(1, int(round(self._config.graceful_shutdown_timeout_sec)))
        command_str = " ".join(shlex.quote(part) for part in command)
        log_tag = f"NexyRestartHelper-{label}"

        env_exports = ""
        if env:
            lines = []
            for key, value in env.items():
                if value is None:
                    continue
                lines.append(f"export {key}={shlex.quote(str(value))}")
            if lines:
                env_exports = "\n".join(lines) + "\n"

        verification_block = ""
        if verification_target:
            verification_block = textwrap.dedent(
                f"""
                VERIFY_TARGET={shlex.quote(verification_target)}
                VERIFY_TIMEOUT={verify_timeout}
                VERIFY_INTERVAL=0.5
                VERIFY_SUCCESS=0
                log "verifying new process for $VERIFY_TARGET"
                VERIFY_DEADLINE=$(( $(date +%s) + VERIFY_TIMEOUT ))
                while [ $(date +%s) -lt $VERIFY_DEADLINE ]; do
                    FOUND=$(pgrep -f "$VERIFY_TARGET" 2>/dev/null || true)
                    for pid in $FOUND; do
                        if [ "$pid" != "$TARGET_PID" ]; then
                            log "detected new pid $pid for $VERIFY_TARGET"
                            VERIFY_SUCCESS=1
                            break
                        fi
                    done
                    if [ $VERIFY_SUCCESS -eq 1 ]; then
                        break
                    fi
                    sleep $VERIFY_INTERVAL
                done
                if [ $VERIFY_SUCCESS -ne 1 ]; then
                    log "failed to detect new pid for $VERIFY_TARGET"
                fi
                """
            )

        script = textwrap.dedent(
            f"""
            TARGET_PID={target_pid}
            TIMEOUT={timeout_s}
            INTERVAL={poll_interval:.2f}
            POST_DELAY={post_delay:.2f}
            LOG_TAG={shlex.quote(log_tag)}

            log() {{
                /usr/bin/logger -t "$LOG_TAG" "$1" 2>/dev/null || echo "$LOG_TAG: $1" >&2
            }}

            log "waiting for process $TARGET_PID to exit (timeout=${{TIMEOUT}}s)"
            START=$(date +%s)
            while kill -0 $TARGET_PID 2>/dev/null; do
                NOW=$(date +%s)
                if [ $((NOW - START)) -ge $TIMEOUT ]; then
                    log "timeout waiting for $TARGET_PID; continuing with relaunch"
                    break
                fi
                sleep $INTERVAL
            done

            sleep $POST_DELAY
            {env_exports}log "launching: {command_str}"
            {command_str}
            LAUNCH_STATUS=$?
            if [ $LAUNCH_STATUS -ne 0 ]; then
                log "launch command exited with status $LAUNCH_STATUS"
            else
                log "launch command finished successfully"
            fi
            {verification_block}
            """
        )

        try:
            subprocess.Popen(
                ["/bin/sh", "-c", script],
                start_new_session=True,
                close_fds=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            logger.debug("[PERMISSION_RESTART] Spawned delayed relaunch helper (label=%s)", label)
            return True
        except Exception as exc:
            logger.error("[PERMISSION_RESTART] Failed to spawn relaunch helper (%s): %s", label, exc)
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
        self._persist_restart_signal()

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
        self._persist_restart_signal()

        try:
            logger.info("[PERMISSION_RESTART] Restarting current bundle via execve (%s)", exe_path)
            logger.info("[PERMISSION_RESTART] Setting NEXY_FIRST_RUN_RESTARTED=1 for new process")
            os.execve(str(exe_path), args, env)
            # execve не возвращается при успехе - процесс заменяется
            # Эта строка недостижима, но нужна для type checker
        except Exception as exc:  # pragma: no cover - defensive
            logger.error("[PERMISSION_RESTART] execve failed: %s", exc)

        return False
