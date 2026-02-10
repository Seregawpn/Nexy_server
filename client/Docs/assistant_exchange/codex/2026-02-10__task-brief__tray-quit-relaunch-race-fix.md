# Task Brief: Tray quit relaunch race fix

## Context
- Пользователь сообщил, что после `Quit` приложение снова запускается вместо полного завершения.
- Архитектурно выход проходит через `tray.quit_clicked -> coordinator -> USER_QUIT_INTENT`.

## Diagnosis
- В `modules/tray_controller/core/tray_controller.py::_on_quit_clicked` событие `quit_clicked` отправлялось через `asyncio.create_task(...)` из `rumps` callback.
- `rumps` callback может выполняться вне активного asyncio loop, из-за чего событие теряется и `USER_QUIT_INTENT` не выставляется до завершения процесса.

## Change
- Добавлен единый thread-safe dispatch в `TrayController`:
  - зафиксирован основной loop в `initialize()` (`self._main_loop = asyncio.get_running_loop()`),
  - в `_on_quit_clicked` событие отправляется через `asyncio.run_coroutine_threadsafe(...)`,
  - добавлено короткое ожидание `future.result(timeout=0.5)` перед `tray_menu.quit()` для гарантии доставки quit-сигнала,
  - оставлен fallback для случаев без loop (с предупреждением в лог).

## Why this fits architecture
- Логика не вынесена в новый слой и не дублирует владельцев state.
- Сохраняется существующий SoT: `USER_QUIT_INTENT` выставляется текущей цепочкой координатора, но теперь событие не теряется из-за thread/loop boundary.

## Verification
- Запущен таргетный тест:
  - `pytest -q tests/verify_menu_quit_fix.py`
  - результат: `2 passed`.

## Risk
- Низкий: изменение локализовано в quit path `TrayController`.
- Возможная деградация ограничена только обработкой клика `Quit` (добавлено максимум ~0.5с ожидания в худшем случае).
