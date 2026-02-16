from __future__ import annotations

import os
import time

from modules.permission_restart.macos.permissions_restart_handler import PermissionsRestartHandler


def test_restart_control_dir_uses_runtime_user_data_dir(tmp_path, monkeypatch) -> None:
    runtime_dir = tmp_path / "Nexy-Dev"
    monkeypatch.setattr(
        "modules.permission_restart.macos.permissions_restart_handler.get_user_data_dir",
        lambda app_name=None: runtime_dir,
    )

    control_dir = PermissionsRestartHandler._restart_control_dir()
    assert control_dir == runtime_dir
    assert control_dir.exists()


def test_cleanup_stale_restart_lock_removes_dead_pid(tmp_path, monkeypatch) -> None:
    runtime_dir = tmp_path / "Nexy-Dev"
    runtime_dir.mkdir(parents=True, exist_ok=True)
    lock_path = runtime_dir / "restart_in_progress.lock"
    lock_path.write_text(f"999999:{time.time()}", encoding="utf-8")

    monkeypatch.setattr(
        "modules.permission_restart.macos.permissions_restart_handler.get_user_data_dir",
        lambda app_name=None: runtime_dir,
    )

    removed = PermissionsRestartHandler.cleanup_stale_restart_lock(source="unit_test")
    assert removed is True
    assert not lock_path.exists()


def test_cleanup_stale_restart_lock_keeps_live_owner_pid(tmp_path, monkeypatch) -> None:
    runtime_dir = tmp_path / "Nexy-Dev"
    runtime_dir.mkdir(parents=True, exist_ok=True)
    lock_path = runtime_dir / "restart_in_progress.lock"
    lock_path.write_text(f"{os.getpid()}:{time.time()}", encoding="utf-8")

    monkeypatch.setattr(
        "modules.permission_restart.macos.permissions_restart_handler.get_user_data_dir",
        lambda app_name=None: runtime_dir,
    )

    removed = PermissionsRestartHandler.cleanup_stale_restart_lock(source="unit_test")
    assert removed is False
    assert lock_path.exists()
