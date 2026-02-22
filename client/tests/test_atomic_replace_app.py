"""
Tests for atomic_replace_app — covers both fresh-install and update paths.
"""

import os
import shutil
from unittest.mock import patch

import pytest

from modules.updater.replace import atomic_replace_app


@pytest.fixture()
def app_dirs(tmp_path):
    """Create a source .app dir and a target parent directory."""
    src = tmp_path / "New.app"
    src.mkdir()
    (src / "Contents").mkdir()
    (src / "Contents" / "Info.plist").write_text("new")

    target_parent = tmp_path / "Applications"
    target_parent.mkdir()
    target = target_parent / "Nexy.app"
    return src, target


# ── Fresh install (target absent) ────────────────────────────────────────


def test_fresh_install_copies_app(app_dirs):
    """When target is absent, app is installed without error."""
    src, target = app_dirs
    assert not target.exists()

    with patch("modules.updater.replace.subprocess.check_call") as mock_ditto:
        # Simulate ditto by actually copying
        def _fake_ditto(cmd):
            shutil.copytree(cmd[1], cmd[2])

        mock_ditto.side_effect = _fake_ditto
        atomic_replace_app(str(src), str(target))

    assert target.exists()
    assert not (str(target) + ".backup") or not os.path.exists(str(target) + ".backup")


def test_fresh_install_creates_parent_directory(tmp_path):
    """When even the parent directory is missing, it is created."""
    src = tmp_path / "New.app"
    src.mkdir()
    (src / "Contents").mkdir()

    target = tmp_path / "deep" / "nest" / "Nexy.app"
    assert not target.parent.exists()

    with patch("modules.updater.replace.subprocess.check_call") as mock_ditto:
        mock_ditto.side_effect = lambda cmd: shutil.copytree(cmd[1], cmd[2])
        atomic_replace_app(str(src), str(target))

    assert target.exists()


def test_fresh_install_failure_cleans_up(app_dirs):
    """If ditto fails during fresh install, partial copy is removed."""
    src, target = app_dirs

    with patch("modules.updater.replace.subprocess.check_call") as mock_ditto:
        # Simulate partial copy then failure
        def _partial_then_fail(cmd):
            os.makedirs(cmd[2])  # partial directory created
            raise RuntimeError("ditto failed")

        mock_ditto.side_effect = _partial_then_fail

        with pytest.raises(RuntimeError, match="ditto failed"):
            atomic_replace_app(str(src), str(target))

    # Partial copy should be cleaned up
    assert not target.exists()


# ── Normal update (target exists) ────────────────────────────────────────


def test_update_replaces_existing_app(app_dirs):
    """When target exists, it is backed up, replaced, and backup removed."""
    src, target = app_dirs
    # Create existing app at target
    target.mkdir()
    (target / "Contents").mkdir()
    (target / "Contents" / "Info.plist").write_text("old")

    backup = str(target) + ".backup"

    with patch("modules.updater.replace.subprocess.check_call") as mock_ditto:
        def _fake_ditto(cmd):
            shutil.copytree(cmd[1], cmd[2])

        mock_ditto.side_effect = _fake_ditto
        atomic_replace_app(str(src), str(target))

    assert target.exists()
    # Backup should have been cleaned up
    assert not os.path.exists(backup)
    # New content should be in place
    assert (target / "Contents" / "Info.plist").read_text() == "new"


def test_update_failure_rolls_back(app_dirs):
    """If ditto fails during update, the backup is restored."""
    src, target = app_dirs
    target.mkdir()
    (target / "Contents").mkdir()
    (target / "Contents" / "Info.plist").write_text("old")

    with patch("modules.updater.replace.subprocess.check_call") as mock_ditto:
        mock_ditto.side_effect = RuntimeError("ditto failed")

        with pytest.raises(RuntimeError, match="ditto failed"):
            atomic_replace_app(str(src), str(target))

    # Original app should be restored from backup
    assert target.exists()
    assert (target / "Contents" / "Info.plist").read_text() == "old"
    assert not os.path.exists(str(target) + ".backup")
