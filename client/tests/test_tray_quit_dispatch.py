from concurrent.futures import TimeoutError as FutureTimeoutError
from unittest.mock import AsyncMock, Mock

import pytest

import modules.tray_controller.core.tray_controller as tray_controller_module
from modules.tray_controller.core.tray_controller import TrayController


class _RunningLoopStub:
    def is_running(self):
        return True


class _FutureOk:
    def __init__(self):
        self.timeout_seen = None

    def result(self, timeout=None):
        self.timeout_seen = timeout


class _FutureTimeout:
    def result(self, timeout=None):
        raise FutureTimeoutError()


def test_quit_click_waits_for_dispatch_ack_before_quit(monkeypatch):
    controller = TrayController()
    controller.tray_menu = Mock()
    controller._dispatch_loop = _RunningLoopStub()
    controller._publish_event = AsyncMock()

    future = _FutureOk()

    def fake_run_coroutine_threadsafe(coro, loop):
        coro.close()
        return future

    monkeypatch.setattr(
        tray_controller_module.asyncio,
        "run_coroutine_threadsafe",
        fake_run_coroutine_threadsafe,
    )

    controller._on_quit_clicked(None)

    controller.tray_menu.quit.assert_called_once()
    assert future.timeout_seen == 1.5


def test_quit_click_continues_when_dispatch_timeout(monkeypatch):
    controller = TrayController()
    controller.tray_menu = Mock()
    controller._dispatch_loop = _RunningLoopStub()
    controller._publish_event = AsyncMock()

    def fake_run_coroutine_threadsafe(coro, loop):
        coro.close()
        return _FutureTimeout()

    monkeypatch.setattr(
        tray_controller_module.asyncio,
        "run_coroutine_threadsafe",
        fake_run_coroutine_threadsafe,
    )

    controller._on_quit_clicked(None)

    controller.tray_menu.quit.assert_called_once()


@pytest.mark.asyncio
async def test_initialize_does_not_override_preconfigured_dispatch_loop():
    controller = TrayController()
    sentinel_loop = object()
    controller.set_dispatch_loop(sentinel_loop)  # integration preconfigures owner loop

    ok = await controller.initialize()

    assert ok is True
    assert controller._dispatch_loop is sentinel_loop
