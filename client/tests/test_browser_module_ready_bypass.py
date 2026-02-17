import asyncio
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.browser_automation import module as browser_module


@pytest.mark.asyncio
async def test_process_bypasses_setup_wait_when_local_chromium_ready(tmp_path, monkeypatch):
    monkeypatch.setattr(browser_module, "_check_browser_use_available", lambda: True)
    monkeypatch.setattr(browser_module, "_reset_browser_use_cache", lambda: None)
    monkeypatch.setattr(browser_module, "get_user_data_dir", lambda: str(tmp_path))

    chromium_dir = tmp_path / "ms-playwright" / "chromium-1208"
    chromium_dir.mkdir(parents=True)
    (chromium_dir / "INSTALLATION_COMPLETE").write_text("ok", encoding="utf-8")

    m = browser_module.BrowserUseModule()

    async def fake_run_agent(task, task_id, session_id, config_preset, *, retry_count=0):
        yield {
            "type": "BROWSER_TASK_COMPLETED",
            "task_id": task_id,
            "session_id": session_id,
            "description": "done",
        }

    monkeypatch.setattr(m, "_run_agent", fake_run_agent)

    async def never_finishes():
        await asyncio.sleep(999)

    stale_install_task = asyncio.create_task(never_finishes())

    browser_module.BrowserUseModule._browser_installed = False
    browser_module.BrowserUseModule._install_task = stale_install_task

    try:
        events = []
        async for ev in m.process({"args": {"task": "open site"}, "session_id": "s1"}):
            events.append(ev)
            if ev.get("type") == "BROWSER_TASK_COMPLETED":
                break

        assert events
        assert events[0].get("type") == "BROWSER_TASK_STARTED"
        assert all(ev.get("type") != "BROWSER_SETUP_IN_PROGRESS" for ev in events)

        await asyncio.sleep(0)
        assert stale_install_task.cancelled()
    finally:
        if not stale_install_task.done():
            stale_install_task.cancel()
            with pytest.raises(asyncio.CancelledError):
                await stale_install_task
        browser_module.BrowserUseModule._install_task = None
        browser_module.BrowserUseModule._browser_installed = False


@pytest.mark.asyncio
async def test_process_does_not_emit_setup_in_progress_when_not_ready(monkeypatch):
    monkeypatch.setattr(browser_module, "_check_browser_use_available", lambda: True)
    monkeypatch.setattr(browser_module, "_reset_browser_use_cache", lambda: None)

    m = browser_module.BrowserUseModule()
    browser_module.BrowserUseModule._browser_installed = False
    browser_module.BrowserUseModule._install_task = None

    async def fake_get_or_start_install_task(*, restart_if_failed):
        return None, True

    async def fake_run_agent(task, task_id, session_id, config_preset, *, retry_count=0):
        yield {
            "type": "BROWSER_TASK_COMPLETED",
            "task_id": task_id,
            "session_id": session_id,
            "description": "done",
        }

    monkeypatch.setattr(m, "_get_or_start_install_task", fake_get_or_start_install_task)
    monkeypatch.setattr(m, "_run_agent", fake_run_agent)

    events = []
    async for ev in m.process({"args": {"task": "open site"}, "session_id": "s2"}):
        events.append(ev)
        if ev.get("type") == "BROWSER_TASK_COMPLETED":
            break

    assert events
    assert events[0].get("type") == "BROWSER_TASK_STARTED"
    assert all(ev.get("type") != "BROWSER_SETUP_IN_PROGRESS" for ev in events)


@pytest.mark.asyncio
async def test_process_uses_url_when_task_missing(monkeypatch):
    monkeypatch.setattr(browser_module, "_check_browser_use_available", lambda: True)
    monkeypatch.setattr(browser_module, "_reset_browser_use_cache", lambda: None)

    m = browser_module.BrowserUseModule()
    browser_module.BrowserUseModule._browser_installed = True

    captured = {"task": None}

    async def fake_run_agent(task, task_id, session_id, config_preset, *, retry_count=0):
        captured["task"] = task
        yield {
            "type": "BROWSER_TASK_COMPLETED",
            "task_id": task_id,
            "session_id": session_id,
            "description": "done",
        }

    monkeypatch.setattr(m, "_run_agent", fake_run_agent)

    events = []
    async for ev in m.process({"args": {"url": "https://example.com"}, "session_id": "s3"}):
        events.append(ev)
        if ev.get("type") == "BROWSER_TASK_COMPLETED":
            break

    assert events
    assert events[0].get("type") == "BROWSER_TASK_STARTED"
    assert captured["task"] == "Open this page: https://example.com"


@pytest.mark.asyncio
async def test_process_fails_when_task_and_url_missing(monkeypatch):
    monkeypatch.setattr(browser_module, "_check_browser_use_available", lambda: True)
    monkeypatch.setattr(browser_module, "_reset_browser_use_cache", lambda: None)

    m = browser_module.BrowserUseModule()
    browser_module.BrowserUseModule._browser_installed = True

    async def fake_run_agent(*args, **kwargs):  # pragma: no cover
        raise AssertionError("_run_agent should not be called for invalid request")
        yield  # pragma: no cover

    monkeypatch.setattr(m, "_run_agent", fake_run_agent)

    events = [ev async for ev in m.process({"args": {}, "session_id": "s4"})]
    assert len(events) == 1
    assert events[0].get("type") == "BROWSER_TASK_FAILED"
    assert events[0].get("error") == "missing_task_or_url"
