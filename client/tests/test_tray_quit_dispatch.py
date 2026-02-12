from __future__ import annotations

import concurrent.futures
import os
import sys
from unittest.mock import AsyncMock, Mock, patch

import pytest

sys.path.insert(0, os.getcwd())

from modules.tray_controller.core.tray_controller import TrayController


def test_quit_waits_for_dispatch_before_quit() -> None:
    controller = TrayController()
    controller.tray_menu = Mock()
    controller._dispatch_loop = Mock()
    controller._dispatch_loop.is_running.return_value = True

    future = Mock()

    def _run_threadsafe_stub(coro, _loop):
        coro.close()
        return future

    with patch("asyncio.run_coroutine_threadsafe", side_effect=_run_threadsafe_stub) as run_threadsafe:
        controller._on_quit_clicked(sender=None)

    run_threadsafe.assert_called_once()
    future.result.assert_called_with(timeout=2.0)
    controller.tray_menu.quit.assert_called_once()


def test_quit_continues_on_dispatch_timeout() -> None:
    controller = TrayController()
    controller.tray_menu = Mock()
    controller._dispatch_loop = Mock()
    controller._dispatch_loop.is_running.return_value = True

    future = Mock()
    future.result.side_effect = concurrent.futures.TimeoutError()

    def _run_threadsafe_stub(coro, _loop):
        coro.close()
        return future

    with patch("asyncio.run_coroutine_threadsafe", side_effect=_run_threadsafe_stub):
        controller._on_quit_clicked(sender=None)

    controller.tray_menu.quit.assert_called_once()


def test_quit_fallback_dispatch_when_no_loop_available() -> None:
    controller = TrayController()
    controller.tray_menu = Mock()
    controller._dispatch_loop = None
    callback = AsyncMock()
    controller.set_event_callback("quit_clicked", callback)

    with patch("asyncio.create_task", side_effect=RuntimeError("no running event loop")):
        controller._on_quit_clicked(sender=None)

    callback.assert_awaited_once_with("quit_clicked", {})
    controller.tray_menu.quit.assert_called_once()


@pytest.mark.asyncio
async def test_start_registers_system_quit_callback_to_unified_quit_flow() -> None:
    controller = TrayController()
    controller.tray_icon = Mock()
    controller.tray_icon.create_icon_file.return_value = "/tmp/icon.png"
    controller.tray_menu = Mock()
    controller.tray_menu.create_app.return_value = Mock()
    controller._create_default_menu = AsyncMock(return_value=None)

    with patch.object(controller, "_create_default_menu", new=AsyncMock(return_value=None)):
        with patch.object(controller, "_on_quit_clicked", autospec=False) as on_quit_clicked:
            success = await controller.start()
            controller.tray_menu.set_quit_callback.assert_called_once()
            quit_cb = controller.tray_menu.set_quit_callback.call_args.args[0]
            quit_cb()
            on_quit_clicked.assert_called_once_with(sender=None)

    assert success is True
