# Analysis: Tray threadsafe dispatch for billing menu

Date: 2026-02-18
Assistant: Codex

## Problem
Menu click "Subscription & Billing..." did not open payment page reliably.

## Root cause
Tray menu callbacks were using `asyncio.create_task(...)` directly from rumps UI thread.
In UI thread there may be no running asyncio loop, so events were dropped before reaching EventBus.

## Fix
- File: `client/modules/tray_controller/core/tray_controller.py`
- Added `_dispatch_event_threadsafe(...)`:
  - Uses `asyncio.run_coroutine_threadsafe(..., self._dispatch_loop)` when owner loop exists.
  - Fallback to current running loop if available.
  - Warn log if no loop.
- Replaced direct `asyncio.create_task(...)` in tray callbacks with thread-safe dispatch for:
  - `icon_clicked`
  - `icon_right_clicked`
  - `settings_clicked`
  - `updater.check_manual`
  - `ui.action.buy_subscription`
  - `about_clicked`

## Architecture gates
- Single owner: EventBus owner loop remains single dispatch owner.
- Zero duplication: reused existing dispatch-loop concept already used for quit path.
- Anti-race: cross-thread dispatch made deterministic via run_coroutine_threadsafe.
- New state: none.

## Validation
- `python3 -m py_compile client/modules/tray_controller/core/tray_controller.py`
- Diff check confirms all menu callbacks now route via thread-safe dispatcher.
