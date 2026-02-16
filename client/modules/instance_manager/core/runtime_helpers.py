"""Runtime helpers for single-instance checks used outside integration startup."""

import os

from .types import InstanceManagerConfig

DEFAULT_LOCK_FILE = "~/Library/Application Support/Nexy/nexy.lock"
DEFAULT_TIMEOUT_SECONDS = 30


def resolve_lock_file_path(default: str = DEFAULT_LOCK_FILE) -> str:
    """Resolve lock file path with env override support."""
    env_lock_file = os.environ.get("NEXY_INSTANCE_LOCK_FILE")
    return env_lock_file or default


def make_probe_config(
    *,
    lock_file: str | None = None,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> InstanceManagerConfig:
    """Build conservative config for read-only "is other instance running" probes."""
    return InstanceManagerConfig(
        enabled=True,
        lock_file=lock_file or resolve_lock_file_path(),
        timeout_seconds=timeout_seconds,
        cleanup_on_startup=False,
        show_duplicate_message=False,
        pid_check=True,
    )
