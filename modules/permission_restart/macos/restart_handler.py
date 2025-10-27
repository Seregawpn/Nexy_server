"""
macOS specific restart helper used by the permission restart module.
"""

from __future__ import annotations

import asyncio
import logging
import os
import subprocess
from typing import Iterable, Optional

from modules.updater.migrate import get_user_app_path

logger = logging.getLogger(__name__)


class MacOSRestartHandler:
    """
    Wrapper around the existing relaunch logic used by the updater module.
    """

    def __init__(self, *, dry_run: Optional[bool] = None):
        env_flag = os.environ.get("NEXY_DISABLE_AUTO_RESTART")
        if dry_run is None:
            dry_run = bool(env_flag) and env_flag.strip().lower() in {"1", "true", "yes"}
        self._dry_run = bool(dry_run)

    async def trigger_restart(self, *, reason: str, permissions: Iterable[str]) -> bool:
        """
        Relaunch the Nexy application. Returns False when running in dry-run mode.
        """

        permissions_list = list(permissions)
        if self._dry_run:
            logger.info(
                "[PERMISSION_RESTART] Dry-run mode enabled, restart skipped (reason=%s, permissions=%s)",
                reason,
                permissions_list,
            )
            return False

        logger.info(
            "[PERMISSION_RESTART] Relaunching Nexy (reason=%s, permissions=%s)",
            reason,
            permissions_list,
        )
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._perform_restart)
        return True

    def _perform_restart(self) -> None:
        try:
            user_app_path = get_user_app_path()
            subprocess.Popen(["/usr/bin/open", "-a", user_app_path])
            os._exit(0)
        except Exception as exc:  # pragma: no cover - process will exit on success
            logger.error("[PERMISSION_RESTART] Failed to relaunch Nexy: %s", exc)
            raise

    @property
    def dry_run(self) -> bool:
        return self._dry_run
